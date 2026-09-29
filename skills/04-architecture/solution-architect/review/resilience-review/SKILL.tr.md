---
description: Bir sistemin dayanıklılığını, her kritik akışı ve bağımlılığı hata modları üzerinden geçirerek inceler; zaman aşımları, yeniden denemeler, devre kesiciler, bölmeler (bulkhead), idempotency, kademeli bozulma, veri kalıcılığı ve felaket kurtarmayı erişilebilirlik hedeflerine (SLO, RTO, RPO) göre kontrol eder. Kritik bir servis canlıya çıkmadan önce, bağımlılık hatalarından kaynaklanan olaylardan sonra, yeni bir dış bağımlılık eklenirken veya DR hazırlığının kanıtlanması gerektiğinde kullanılır.
related: chaos-experiment, dr-plan, slo-definition, integration-pattern-selection, architecture-review
prompt: Ödeme akışımızın dayanıklılığını incele: fiyatlama, stok, ödeme sağlayıcısı ve fraud servisini senkron çağırıyor; geçen ay fraud servisi yavaşladığında iki kesinti yaşadık.
---

# Dayanıklılık İncelemesi

## Amaç
Parçaları veya bağımlılıkları çöktüğünde sistemin nerede kötü şekilde çökeceğini bulmak ve hataların sınırlı kalması, kademeli bozulması ve kabul edilen hedefler içinde toparlanması için somut mekanizmalar önermek.

## Ne zaman kullanılır
- Kritik bir servis canlıya geçişe veya büyük bir sürüme yaklaşırken.
- Olaylar yavaş veya çöken bir bağımlılık nedeniyle oluştuysa ya da büyüdüyse (zincirleme hata, yeniden deneme fırtınası).
- Yeni bir dış bağımlılık veya yeni bir bölge/DR kurulumu eklenirken.
- Denetçiler veya müşteriler DR hazırlığının kanıtını istediğinde.

## Ne zaman kullanılmaz
- Amaç dayanıklılığı pratikte test etmekse bu incelemeden sonra `chaos-experiment` kullanılır.
- Prosedürleri ve rolleriyle tam bir DR planı yazılacaksa `dr-plan` kullanılır.
- Kaygı hata değil, büyüme altında işlem hacmiyse `scalability-review` kullanılır.

## Girdiler
Zorunlu:
- Kritik akışlar ve bağımlılıkları (iç servisler, veritabanları, kuyruklar, üçüncü taraflar) ve çağrı biçimi (senkron/asenkron).
- Erişilebilirlik beklentileri (SLO, RTO, RPO) veya bunların `[TBD]` olarak işaretlenmesine izin.

İsteğe bağlı:
- Mevcut zaman aşımı/yeniden deneme/havuz ayarları, dağıtım topolojisi (zonlar, bölgeler), olay geçmişi ve postmortem'ler.
- Bağımlılık SLA'ları, hız limitleri, kapasite payı.

Akışlar veya bağımlılıklar yoksa iste; topoloji varsayma.

## Süreç
1. Her kritik akışın bağımlılık zincirini çiz; senkron/asenkron, kritiklik (zorunlu/esnek bağımlılık) ve senkron zincirlerin bileşik erişilebilirliğini işaretle.
2. Her bağımlılık için hata modlarını say: erişilemez, yavaş (gecikme sıçraması), hata dönüyor, yanlış/eksik veri dönüyor, kısıtlama (throttling), ağ bölünmesi; veri depoları için failover ve replikasyon gecikmesi.
3. Zaman aşımlarını kontrol et: her uzak çağrının, çağıranın kendi bütçesinden türetilmiş bir zaman aşımı var; zincir boyunca toplam, kullanıcıya dönük zaman aşımına sığıyor.
4. Yeniden denemeleri kontrol et: yalnızca idempotent veya idempotency anahtarlı işlemlerde, sınırlı deneme, jitter'lı üstel geri çekilme, fırtınayı önleyen yeniden deneme bütçesi, birden çok katmanda üst üste binen yeniden deneme yok.
5. Yalıtımı kontrol et: makul eşikli ve yarı açık yoklamalı devre kesiciler, bölmeler (bağımlılık başına ayrı havuz/kuyruk), girişte yük atma ve hız sınırlama.
6. Bozulmayı kontrol et: her esnek bağımlılık çöktüğünde kullanıcının ne aldığı (önbellek değeri, varsayılan, sonraya kuyruklama, özelliğin kapatılması); zorunlu bağımlılıklar en aza indirilmiş.
7. Veri kalıcılığı ve tutarlılığı kontrol et: outbox/işlemsel mesajlaşma, dead-letter kuyrukları ve yeniden oynatma, mutabakat, RPO'ya göre yedek sıklığı, test edilmiş geri yüklemeler.
8. Altyapı dayanıklılığını kontrol et: çoklu zon yedekliliği, tekil hata noktası olmaması (DNS, secret'lar, CI/CD, kimlik sağlayıcı dahil), gerçek hazır olmayı yansıtan sağlık kontrolleri, güvenli dağıtım ve rollback.
9. Tespit ve müdahaleyi kontrol et: belirtiye dayalı alarmlar, runbook'lar, nöbet sahipliği ve RTO/RPO'ya karşı DR tatbikatı kanıtı.
10. Her bulguyu olasılık × etki ile derecelendir; doğrulanana kadar `[VARSAYIM]` olarak işaretlenmiş parametre önerileriyle somut düzeltmeler öner ve bunları doğrulayacak deneyleri listele.
11. Hedef devam ediyorsa bulguları doğrulamak için `chaos-experiment`, kurtarma prosedürleri için `dr-plan` veya hedefler eksikse `slo-definition` öner.

## Çıktı formatı
```markdown
# Dayanıklılık İncelemesi: <sistem/akış> – <tarih>
## Hedefler
SLO: ... · RTO: ... · RPO: ...
## Bağımlılık Haritası
| Akış | Bağımlılık | Senk/Asenk | Zorunlu/Esnek | Zaman aşımı | Yeniden deneme | Devre kesici | Geri düşme |
|---|---|---|---|---|---|---|---|
## Hata Modu Analizi
| Bağımlılık | Hata modu | Mevcut davranış | Etki | Olasılık | Bulgu |
|---|---|---|---|---|---|
## Bulgular ve Öneriler
| ID | Önem | Bulgu | Öneri | Doğrulama |
|---|---|---|---|---|
## DR Hazırlığı
## Önerilen Deneyler
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her kritik akışın her bağımlılığı yalnızca "çöktü" için değil "yavaş" için de analiz edildi.
- [ ] Her senkron zincirdeki zaman aşımı bütçeleri toplamı kullanıcıya dönük limite sığıyor.
- [ ] Her yeniden deneme idempotent bir işleme bağlı, sınırı ve geri çekilmesi var.
- [ ] Her esnek bağımlılığın tanımlı bir bozulmuş davranışı var.
- [ ] RPO/RTO iddiaları test edilmiş geri yükleme veya tatbikat kanıtıyla destekleniyor ya da işaretlendi.
- [ ] Önerilen parametre değerleri doğrulanacak varsayımlar olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca "bağımlılık çöktü" durumunu test etmek. Yavaş bağımlılıklar thread ve bağlantı havuzlarını tüketir ve zincirleme hataların çoğuna yol açar.
- İstemci, gateway ve servis katmanlarında yeniden denemelerin olay sırasında yükü katlaması.
- Downstream bağımlılıkları çağıran sağlık kontrolleri; tek bir bağımlılık çökünce tüm instance'lar trafikten çıkar.

## Örnek
Girdi: "Ödeme adımı fiyatlama, stok, ödeme ve fraud servislerini senkron çağırıyor; fraud yavaşlamaları iki kesintiye yol açtı."

Çıktıdan bir bölüm:
| ID | Önem | Bulgu | Öneri |
|---|---|---|---|
| R1 | Kritik | Fraud çağrısının zaman aşımı yok; yavaş yanıtlar ortak HTTP havuzunu tüketti ve ödeme çağrılarını kilitledi | Zaman aşımı `[VARSAYIM: 800 ms]`, ayrı havuz (bulkhead), devre kesici; açıkken iş kuralına göre düşük riskli siparişleri kabul et ve yetkilendirme sonrası incelemeye kuyrukla `[risk ekibiyle teyit et]` |
| R2 | Büyük | Ödeme yeniden denemeleri hem gateway hem serviste (3 × 3) ve idempotency anahtarı yok | Yalnızca serviste, sağlayıcı idempotency anahtarı ve jitter'lı geri çekilmeyle yeniden dene |
