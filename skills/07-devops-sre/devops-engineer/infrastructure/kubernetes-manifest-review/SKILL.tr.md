---
description: "Kubernetes manifest'lerini, Helm chart'larını veya Kustomize çıktısını kaynak istek ve limitleri, sağlık probe'ları, güvenlik bağlamı, erişilebilirlik (replika, kesinti bütçesi, dağılım), yapılandırma ve secret yönetimi ile işletilebilirlik açısından inceler. Düzeltilmiş YAML ile önceliklendirilmiş bulgular verir. Manifest'ler incelemeye geldiğinde, pod'lar yeniden başladığında veya tahliye edildiğinde ya da bir iş yükü üretime hazırlanırken kullanılır."
related: "dockerfile-review, secrets-management-plan, capacity-planning, deployment-strategy, resilience-review"
prompt: "Üretim cluster'ına çıkmadan önce sipariş API'mizin bu Deployment ve Service YAML'ını incele."
---

# Kubernetes Manifest İnceleme

## Amaç
Bir iş yükünü üretimde çalışmaya güvenli hale getirmek: doğru boyutlandırılmış, zamanlayıcı tarafından doğru değerlendirilen, sıkılaştırılmış, düğüm ve zone kaybına dayanıklı ve ortamlar arasında tutarlı.

## Ne zaman kullanılır
- Manifest'ler, bir Helm chart'ı veya render edilmiş Kustomize çıktısı incelemeye geldiğinde.
- Pod'lar OOMKilled oluyor, CPU kısıtlamasına uğruyor, tahliye ediliyor veya sürekli yeniden başlıyorsa.
- Bir iş yükü üretim veya paylaşımlı cluster'a alınırken.

## Ne zaman kullanılmaz
- Sorun konteyner imajının kendisiyse `dockerfile-review` kullanılır.
- Sorun bulut/cluster altyapı koduysa `iac-review` kullanılır.
- Uzun vadede kaç replika veya düğüm gerektiği soruluyorsa `capacity-planning` kullanılır.

## Girdiler
Zorunlu:
- Manifest YAML'ı (veya render edilmiş chart çıktısı).

İsteğe bağlı, kaliteyi artırır:
- İş yükü profili: durumsuz/durumlu, trafik, gecikme SLO'su, açılış süresi, bellek davranışı.
- Cluster politikaları (admission controller'lar, Pod Security Standards seviyesi, varsayılan network policy, service mesh).
- Gözlemlenen metrikler veya olaylar (OOMKill, throttling, yeniden başlatmalar).

YAML yoksa iste. Chart render edilmeden verildiyse values ve template'leri incele, varsayımları yaz.

## Süreç
1. Nesneleri ve ilişkilerini çıkar (Deployment/StatefulSet/Job, Service, Ingress/Gateway, ConfigMap, Secret, HPA, PDB, NetworkPolicy, ServiceAccount).
2. Kaynaklar: her konteynerde CPU ve bellek request'i tanımlı; bellek limiti tanımlı; CPU limiti yalnızca kurum şart koşuyorsa (throttling riskini not et); request'ler ölçülmüş kullanıma dayanıyor ya da `[VARSAYIM]` olarak işaretli.
3. Probe'lar: readiness hizmet verebilme durumunu yansıtır; liveness bağımlılıkları değil yalnızca süreci kontrol eder; yavaş açılanlar için startup probe; makul timeout ve eşikler.
4. Güvenlik: `runAsNonRoot`, sabit UID, `allowPrivilegeEscalation: false`, tüm capability'leri düşürme, `readOnlyRootFilesystem`, seccomp `RuntimeDefault`, hostPath/hostNetwork yok, gerekmedikçe automount kapalı özel ServiceAccount, en az yetkili RBAC. Pod Security Standards "restricted" seviyesiyle karşılaştır.
5. Erişilebilirlik: hizmet veren iş yükleri için en az 2 replika, PodDisruptionBudget, düğüm/zone arası topology spread veya anti-affinity, rolling update surge/unavailable ayarları, düzgün kapanma (`terminationGracePeriodSeconds`, preStop, bağlantı boşaltma).
6. Ölçekleme: HPA metrikleri ve sınırları request'lerle tutarlı; GitOps'ta HPA ile sabit replika çakışması yok.
7. Yapılandırma ve secret'lar: ConfigMap veya env literal'lerinde secret yok; imaj değişmez tag veya digest ile referanslı; `imagePullPolicy` makul; ortam farkları yalnızca values/overlay ile.
8. Ağ: varsayılan deny ve açık izinlerle NetworkPolicy; Service port ve selector'ları eşleşiyor; ingress TLS.
9. İşletilebilirlik: etiketler (app, version, team), metrik toplama annotation'ları, stdout'a log, tutarlı kaynak adları.
10. Bulguları derecelendir, düzeltilmiş YAML parçaları ver.

## Çıktı formatı
```markdown
# Kubernetes Manifest İncelemesi: <iş yükü>
Özet: <üretime hazırlık kararı: Hazır / Düzeltmelerle hazır / Hazır değil>
| # | Önem | Nesne | Alan | Bulgu | Düzeltme |
## Düzeltilmiş Parçalar
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her konteynerin request'i var; bellek limitleri tanımlı.
- [ ] Liveness probe'ları alt servislere bağımlı değil.
- [ ] Güvenlik bağlamı restricted seviyesini karşılıyor veya sapmalar gerekçeli.
- [ ] Hizmet veren iş yükleri tek bir düğüm boşaltmasına dayanıyor (replika, PDB, dağılım).
- [ ] Veriyle desteklenmeyen önerilen değerler `[VARSAYIM]` olarak işaretli.

## Sık yapılan hatalar
- Veritabanını çağıran liveness probe: kısa bir veritabanı kesintisi tüm pod'ları yeniden başlatır. Liveness'ı yerel tut.
- Request değerlerini başka bir servisten kopyalamak. Gözlemlenen kullanıma dayandır ve düzenli gözden geçir.
- `minAvailable` değeri replika sayısına eşit PDB; düğüm boşaltmayı engeller. En az bir kesintiye izin ver.

## Örnek
Girdi: 1 replikalı, kaynak tanımı olmayan, veritabanını kontrol eden `GET /health` liveness'ı olan, root olarak çalışan Deployment.

Çıktıdan bir bölüm:
| # | Önem | Nesne | Alan | Bulgu | Düzeltme |
|---|---|---|---|---|---|
| 1 | Yüksek | Deployment | replicas | Tek replika, PDB yok | 3 replika, PDB `maxUnavailable: 1`, zone dağılımı |
| 2 | Yüksek | Deployment | livenessProbe | Veritabanını kontrol ediyor; zincirleme yeniden başlatma | Liveness `/livez` (yalnızca süreç), readiness `/readyz` |
| 3 | Yüksek | Deployment | securityContext | Root olarak çalışıyor | `runAsNonRoot: true`, ALL düşür, salt okunur kök FS |
