---
description: "CI ürününden bağımsız olarak uçtan uca bir CI/CD hattı tasarlar: aşamalar, kalite ve güvenlik kapıları, artefakt yönetimi, ortamlar ve terfi kuralları. Yeni bir hat kurulurken, yavaş veya kırılgan bir hat yeniden yapılandırılırken ya da kodun commit'ten üretime nasıl ilerlediği dokümante edilecekken kullanılır."
related: "environment-strategy, deployment-strategy, branching-strategy, release-quality-gate, secrets-management-plan"
prompt: "Kubernetes üzerinde dev, staging ve prod ortamlarına dağıtılan .NET API'miz için, prod öncesi manuel onay içeren bir CI/CD hattı tasarla."
---

# CI/CD Hattı Tasarlama

## Amaç
Her değişikliğin bir kez derlendiği, açık kapılarla doğrulandığı ve aynı değişmez artefakt olarak üretime terfi ettirildiği, hızlı geri bildirim veren ve denetlenebilir iz bırakan bir hat tasarımı üretmek.

## Ne zaman kullanılır
- Yeni bir servis veya repository için hat gerektiğinde.
- Mevcut hat yavaş, kırılgan ya da her ortam için yeniden derleme yapıyorsa.
- Denetim veya uyum gereği kapıların ve onayların dokümante edilmesi gerektiğinde.
- Ekip daha sık veya otomatik teslimata geçerken.

## Ne zaman kullanılmaz
- Belirli bir çalıştırma başarısız olduysa ve teşhis gerekiyorsa `pipeline-failure-triage` kullanılır.
- Yalnızca yayılım mekaniği (canary, blue-green) konuşuluyorsa `deployment-strategy` kullanılır.
- Yalnızca ortam yapısı konuşuluyorsa `environment-strategy` kullanılır.

## Girdiler
Zorunlu:
- Uygulama türü, dil/derleme aracı ve dağıtım hedefi (VM, konteyner platformu, serverless, mobil mağaza, paket deposu).
- Hedef ortamlar ve üretime terfiyi kimin onaylayabileceği.

İsteğe bağlı, kaliteyi artırır:
- Branching modeli, mevcut hat ve süreleri, test paketleri ve çalışma süreleri.
- Uyum kısıtları (görevler ayrılığı, değişiklik onayı, imzalı artefakt).
- Mevcut DORA metrikleri (dağıtım sıklığı, teslim süresi, değişiklik hata oranı, toparlanma süresi).

Dağıtım hedefi veya ortamlar yoksa sor. Diğer her şeyi açık soru olarak kaydet.

## Süreç
1. Tetikleyici modelini çıkar: hangi olay hangi hattı başlatır (pull request, main'e merge, tag, zamanlanmış, manuel).
2. Commit aşamasını tanımla (hedef 10 dakikanın altı): lockfile ile bağımlılık yükleme, derleme, birim testleri, lint/statik analiz, secret taraması, bağımlılık (SCA) taraması.
3. Artefaktı tanımla: bir kez derle, sürümle (commit SHA, yayınlanacaksa SemVer), imzala, SBOM üret, tek bir registry'ye gönder. Ortam başına yeniden derlemeyi yasakla.
4. Kabul aşamasını tanımla: artefaktı geçici veya paylaşılan test ortamına dağıt; entegrasyon, sözleşme, API ve smoke testlerini çalıştır; gerekiyorsa DAST veya konteyner taraması yap.
5. Her aşama için kapıyı açık bir kuralla tanımla: engelleyici mi uyarı mı, eşik (ör. kritik zafiyet yok, kapsam düşmüyor), kimin hangi kayıtla aşabileceği.
6. Terfiyi tanımla: aynı artefakt digest'i, dağıtım anında enjekte edilen ortama özel yapılandırma, secret store'dan çekilen gizli bilgiler, onay noktaları ve gerekiyorsa görevler ayrılığı.
7. Üretim dağıtım adımını tanımla: strateji referansı, otomatik dağıtım sonrası doğrulama, otomatik veya tek tıkla rollback.
8. Hız için tasarla: önbellek, paralel işler, test bölme, değişikliğe göre yol filtreleri; aşama başına beklenen süreyi yaz.
9. Hattın kendi güvenliğini tasarla: en az yetkili runner kimlikleri, kısa ömürlü kimlik bilgileri (mümkünse OIDC tarzı federasyon), sabitlenmiş eklenti sürümleri, korumalı branch'ler.
10. Hattın gözlemlenebilirliğini tanımla: aşama süreleri, hata oranları, kararsız test takibi, DORA metrik kaynakları.
11. Şablonu doldur, bilinmeyenleri işaretle.

## Çıktı formatı
```markdown
# CI/CD Hat Tasarımı: <servis>
## Tetikleyiciler
| Olay | Hat | Çalışan aşamalar |
## Aşamalar
| # | Aşama | Adımlar | Hedef süre | Kapı (engelleme kuralı) | Aşma yetkisi |
## Artefakt
- Tür / registry / sürümleme / imzalama / SBOM
## Ortamlar ve Terfi
| Nereden | Nereye | Tetikleyici | Onay | Dağıtım sonrası kontroller |
## Yapılandırma ve Gizli Bilgiler
## Üretim Dağıtımı ve Rollback
## Hat Güvenliği
## Metrikler
## Açık Sorular / Varsayımlar
```

## Kalite kontrol listesi
- [ ] Artefakt bir kez derleniyor ve digest ile terfi ediyor; ortam başına yeniden derleme yok.
- [ ] Her kapının ölçülebilir bir kuralı ve aşma yetkisi olan bir sorumlusu var.
- [ ] Commit aşaması geri bildirim hedefi yazılı ve gerçekçi.
- [ ] Hat değişkenlerinde uzun ömürlü bulut kimlik bilgisi veya düz metin secret yok.
- [ ] Rollback tanımlı ve yeni bir derlemeye bağlı değil.
- [ ] Bilinmeyenler uydurulmadı, `[BİLİNMİYOR]` veya `[VARSAYIM]` olarak işaretlendi.

## Sık yapılan hatalar
- Her ortam için yeniden derlemek; bu durumda üretimde test edilmemiş bir binary çalışır. Digest'i terfi ettir.
- Yavaş uçtan uca testleri commit aşamasına koymak. Bunları kabul aşamasına taşı, commit aşamasını hızlı tut.
- Yalnızca uyarı veren ve görmezden gelinen kapılar. Kritik kapıları engelleyici yap, aşmaları kayda al.
- Hat eklentilerinde veya base image'larda sabitlenmemiş sürümler. Sabitle ve bilinçli güncelle.

## Örnek
Girdi: ".NET 8 API, Docker imajı Kubernetes'e, dev/staging/prod, prod için ürün sahibi onayı gerekli."

Çıktıdan bir bölüm:
| # | Aşama | Adımlar | Hedef süre | Kapı |
|---|---|---|---|---|
| 1 | Commit | kilitli restore, build, birim test, analyzer, secret taraması, SCA | 8 dk | Testler geçer; kritik CVE yok |
| 2 | Paketleme | imaj build, imzalama, SBOM, digest ile push | 4 dk | İmaj taraması: kritik yok |
| 3 | Staging | digest dağıtımı, API + sözleşme testleri, smoke | 12 dk | Smoke %100 geçer |
| 4 | Prod | onay (PO), rolling dağıtım, sentetik kontrol | 10 dk | 15 dk boyunca hata oranı `[TBD]` altında |
