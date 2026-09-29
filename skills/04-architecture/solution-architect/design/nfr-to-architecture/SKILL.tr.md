---
name: nfr-to-architecture
description: "Fonksiyonel olmayan gereksinimleri ölçülebilir kalite niteliği senaryolarına (kaynak, uyaran, ortam, eser, yanıt, yanıt ölçüsü) dönüştürür ve her birini ödünleşimleri ve doğrulama yöntemiyle birlikte mimari taktiklere eşler. NFR'ler belirsiz olduğunda (\"hızlı\", \"güvenli\", \"yüksek erişilebilir\"), bir tasarımın kalite hedeflerini nasıl karşıladığını göstermesi gerektiğinde veya mimari inceleme ya da ATAM öncesinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: solution-architect
  area: design
  title: "NFR'leri mimari taktiklere eşleme"
  related: "nfr-specification, solution-architecture-document, atam-evaluation, trade-off-analysis, slo-definition"
  prompt: "Bu NFR'leri mimari taktiklere eşle: ödeme adımı hızlı olmalı, 7/24 erişilebilir olmalı, Black Friday tepe yüklerini kaldırmalı ve PCI DSS'e uymalı."
---

# NFR'leri Mimari Taktiklere Eşleme

## Amaç
Kalite gereksinimlerini test edilebilir ve somut tasarım kararlarına izlenebilir hale getirmek. Böylece mimarinin her kalite hedefine nasıl yanıt verdiği ve bunun bedeli görünür olur.

## Ne zaman kullanılır
- NFR'ler var ama ölçüsü olmayan sıfatlardan ibaretse.
- Bir çözüm tasarımının erişilebilirlik, performans, güvenlik, değiştirilebilirlik veya diğer nitelikleri nasıl sağladığını gerekçelendirmesi gerektiğinde.
- `architecture-review` veya `atam-evaluation` için girdi hazırlanırken.

## Ne zaman kullanılmaz
- NFR'ler hiç toplanmamışsa önce `nfr-specification` kullanılır.
- Amaç mevcut bir servis için hizmet seviyesi hedefleri tanımlamaksa `slo-definition` kullanılır.
- Paydaşlarla tam bir ödünleşim değerlendirmesi gerekiyorsa `atam-evaluation` kullanılır.

## Girdiler
Zorunlu:
- Herhangi bir biçimde NFR'ler veya kalite hedefleri.
- Sistemin veya ana konteynerlerinin kısa tanımı.

İsteğe bağlı:
- İş bağlamı (tepe olaylar, mevzuat, kullanıcı tabanı), mevcut ölçümler, kısıtlar (bütçe, platform, ekip).
- Mevcut mimari dokümanlar veya ADR'ler.

Sistem tanımı yoksa iste. Eksik ölçüler `[TBD]` olur, önerilen aday `[VARSAYIM]` olarak işaretlenir.

## Süreç
1. NFR'leri ISO/IEC 25010 karakteristiklerine (performans verimliliği, güvenilirlik, güvenlik, bakım yapılabilirlik, uyumluluk, kullanılabilirlik, taşınabilirlik) ve ek olarak işletilebilirlik ile maliyete göre grupla.
2. Her birini kalite niteliği senaryosu olarak yeniden yaz: kaynak, uyaran, ortam, eser, yanıt, yanıt ölçüsü. Kullanıcının söylediğini önerilen ölçülerden ayır.
3. Çelişkileri ve belirsizlikleri işaretle (ör. "gerçek zamanlı" ile "en ucuz seçenek", çok bölgeli yazma ile güçlü tutarlılık).
4. Senaryoları iş önemi ve teknik zorluğa göre (her biri Y/O/D) önceliklendir; Y/Y ve Y/O olanlara odaklan.
5. Öncelikli her senaryo için ilgili niteliğin taktik ailelerinden taktik seç (ör. erişilebilirlik: hatayı algıla, kurtar, önle; performans: talebi kontrol et, kaynakları yönet; güvenlik: diren, algıla, tepki ver, kurtar; değiştirilebilirlik: bağımlılığı azalt, uyumu artır, bağlamayı ertele).
6. Taktikleri somut mimari öğelere eşle: hangi konteyner, bileşen, platform servisi veya desen uyguluyor.
7. Her taktiğin diğer nitelikler ve maliyet üzerindeki ödünleşimini belirt (ör. önbellek gecikmeyi iyileştirir ama bayatlık ve geçersizleştirme karmaşıklığı getirir).
8. Her senaryo için doğrulama yöntemini tanımla: yük testi, kaos deneyi, güvenlik testi, mimari uygunluk fonksiyonu (fitness function), izleme SLI'ı.
9. Hiçbir taktiğin ölçüyü tam karşılamadığı yerleri kalan risk, tek parametrenin birden çok niteliği etkilediği yerleri hassasiyet noktası olarak işaretle.
10. İzlenebilirlik tablosunu ve ADR adayları listesini üret.
11. Hedef devam ediyorsa sonucu yerleştirmek için `solution-architecture-document`, paydaşlarla doğrulamak için `atam-evaluation` veya çalışma zamanı hedefleri için `slo-definition` öner.

## Çıktı formatı
```markdown
# NFR – Mimari Eşlemesi: <sistem>
## Kalite Niteliği Senaryoları
| ID | Nitelik | Kaynak | Uyaran | Ortam | Eser | Yanıt | Ölçü | Öncelik (İş/Teknik) |
|---|---|---|---|---|---|---|---|---|
## Taktikler ve Mimari Öğeler
| Senaryo | Taktikler | Uygulayan öğe | Ödünleşimler | Doğrulama |
|---|---|---|---|---|
## Çelişkiler ve Hassasiyet Noktaları
## Kalan Riskler
## ADR Adayları
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her senaryonun sayısal veya test edilebilir bir yanıt ölçüsü var ya da `[TBD]` olarak işaretli.
- [ ] Belirtilen ölçüler ile önerilen ölçüler ayırt edilebiliyor.
- [ ] Her taktik yalnızca bir desen adına değil, adı konmuş bir mimari öğeye eşlendi.
- [ ] Her taktik için diğer niteliklere ve maliyete etkisi belirtildi.
- [ ] Öncelikli her senaryonun bir doğrulama yöntemi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ortamı olmayan senaryolar: "p95 < 300 ms" yük seviyesi ve mod (normal, tepe, bozulmuş) olmadan anlamsızdır.
- Taktikleri moda kelime listesi gibi sıralamak. Her taktik bir senaryoya ve bir bileşene bağlanmalı.
- Güvenliği tek senaryo saymak. Tehdit ve varlığa göre böl; gerektiğinde `threat-model` ile bağla.

## Örnek
Girdi: "Ödeme hızlı olmalı, 7/24, Black Friday'i kaldırmalı, PCI DSS."

Çıktıdan bir bölüm:
| ID | Nitelik | Uyaran | Ortam | Ölçü |
|---|---|---|---|---|
| P1 | Performans | Müşteri ödemeyi gönderir | Tepe yük `[TBD: normalin x katı, geçen yılın verisinden]` | Ödeme API p95 < `[TBD]` ms `[VARSAYIM: 500 ms]` |
| A1 | Erişilebilirlik | Ödeme sağlayıcısı zaman aşımına uğrar | Normal işletim | Sipariş kabul edilir, ödeme yeniden denenir; denemelerin %99,9'unda müşteriye hata gösterilmez |

A1 taktikleri: ödeme adaptöründe zaman aşımı + devre kesici, bekleyen ödemeler için outbox. Ödünleşim: sipariş durumu "beklemede" olur ve müşteri bilgilendirmesi gerekir.
