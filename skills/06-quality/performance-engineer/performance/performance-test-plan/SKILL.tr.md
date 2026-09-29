---
name: performance-test-plan
description: "Ölçülebilir kabul kriterlerine (gecikme yüzdelikleri, verim, hata oranı, kaynak sınırları) bağlı hedefler, üretim verisinden veya iş tahminlerinden türetilmiş bir iş yükü modeli, test türleri (yük, stres, dayanıklılık, ani yük, ölçeklenebilirlik), senaryolar, test verisi, ortam ve üretimden farkları, izleme, giriş/çıkış kriterleri ve riskler içeren bir performans test planı yazar. Bir sürüm, taşıma veya beklenen trafik artışı öncesinde, fonksiyonel olmayan gereksinimlerin doğrulanması gerektiğinde ya da sıfırdan bir performans testi tasarlanacağında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: performance-engineer
  area: performance
  title: "Performans test planı"
  related: "load-test-analysis, capacity-test-report, slo-definition, test-data-design, nfr-to-architecture"
  prompt: "Ödeme trafiğini üç katına çıkarabilecek bir kampanya başlatıyoruz. Checkout API'si ve bağımlılıkları için bir performans test planı yaz."
---

# Performans Test Planı

## Amaç
Somut bir iş sorusunu ("checkout kampanya zirvesini SLO içinde karşılayabilir mi?") gerçekçi bir iş yükü, temsil edici bir ortam ve ilk koşumdan önce üzerinde anlaşılmış geçti/kaldı kriterleriyle yanıtlayan performans testleri tasarlamak.

## Ne zaman kullanılır
- Bir sürüm, platform taşıması veya altyapı değişikliği performansı etkileyebilecekse.
- Trafik artışı (kampanya, sezon, yeni pazar) bekleniyorsa.
- Fonksiyonel olmayan gereksinimler veya SLO'lar var ama yük altında hiç doğrulanmamışsa.

## Ne zaman kullanılmaz
- Koşulmuş bir testin sonuçları yorumlanacaksa `load-test-analysis` kullanılır.
- Sürdürülebilir maksimum yük ve pay raporlanacaksa `capacity-test-report` kullanılır.
- Bilinen yavaş bir kod yolu optimize edilecekse `performance-optimization` kullanılır.

## Girdiler
Zorunlu:
- Test edilecek sistem veya işlemler ve testin yanıtlaması gereken soru (sürüm kontrolü, zirveye hazırlık, kapasite sınırı).

İsteğe bağlı, kaliteyi artırır:
- Üretim trafik verisi (endpoint başına saniyedeki istek, zirve saat, kullanıcı yolculukları, düşünme süreleri), büyüme tahminleri.
- NFR'ler/SLO'lar, mimari ve bağımlılıklar, ortam ayrıntıları, mevcut yük aracı ve bütçe.
- Veri hacimleri ve veri gizliliği kısıtları.

Soru veya işlemler bilinmiyorsa sor. Üretim verisi yoksa iş yükünü iş tahminlerinden türet ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Hedefleri test edilebilir sorular olarak yaz ve her birini kabul kriterlerine bağla: işlem başına p95/p99 gecikme, verim, hata oranı, kaynak tavanları (CPU, bellek, bağlantı havuzları); hepsi tanımlı bir yük altında belirtilir.
2. İş yükü modelini kur: işlem karışımı (yüzdeler), geliş hızı veya düşünme süreli eşzamanlı kullanıcı, zirve ve ortalama, büyüme katsayısı; genel trafik için açık (geliş hızına dayalı) model kullan. Hesabı ve kaynağını göster.
3. Test türlerini ve amaçlarını seç: temel çizgi, yük (beklenen zirve), stres (zirvenin ötesinde kırılma noktasına kadar), ani yük (spike), dayanıklılık (soak: sızıntılar için saatlerce sabit yük), ölçeklenebilirlik (otomatik ölçekleme davranışı).
4. Her test türü için senaryoları tanımla: ramp-up, sabit durum süresi, ramp-down, hedef yük seviyeleri ve her birinde neyin ölçüldüğü.
5. Test verisini tasarla: üretimle karşılaştırılabilir hacimler, kardinalite ve dağılım (sıcak anahtarlar, önbellek isabet oranı), yazma yolları için benzersiz veri, sıfırlama stratejisi; sentetik veya maskelenmiş veri kullan, asla ham kişisel veri kullanma.
6. Ortamı ve üretimden her farkını (boyut, topoloji, veri hacmi, paylaşılan bileşenler, üçüncü taraf stub'ları) ve sonuçların nasıl ölçekleneceğini veya hangi uyarılarla sunulacağını açıkla.
7. İki taraflı izleme planla: yük üreticisinin sağlığı, istemci tarafı metrikler, sunucu tarafı metrikler (kaynaklar, GC, havuzlar, kuyruklar, veritabanı), dağıtık izler; saatleri ve zaman damgalarını hizala.
8. Giriş kriterlerini (fonksiyonel kararlılık, ortam hazır, veri yüklü, izleme doğrulanmış) ve çıkış kriterlerini (kabul kriterleri karşılandı veya sapmalar adı verilen bir rol tarafından kabul edildi) tanımla.
9. Riskleri ve kısıtları listele: paylaşılan ortamlar, üçüncü taraf rate limit'leri, yük üretim maliyeti, test pencereleri; etkilenecek ekiplerin nasıl bilgilendirileceğini planla.
10. Takvimi, rolleri ve raporlama formatını tanımla; bilinmeyen sayıları `[TBD]` veya `[VARSAYIM]` olarak işaretle.
11. Hedef devam ediyorsa koşumdan sonra `load-test-analysis`, pay kararları için `capacity-test-report`, kabul kriterleri eksikse `slo-definition` öner.

## Çıktı formatı
```markdown
# Performans Test Planı: <sistem / sürüm>
Yanıtlanacak soru: ...

## Hedefler ve Kabul Kriterleri
| İşlem | Yük seviyesi | p95 | p99 | Verim | Hata oranı | Kaynak sınırı |
|---|---|---|---|---|---|---|

## İş Yükü Modeli
| İşlem | Karışım % | Zirve hızı | Düşünme süresi | Kaynak |
|---|---|---|---|---|
Hesap: ...

## Test Türleri ve Senaryolar
| Test | Amaç | Ramp-up | Sabit durum | Hedef yük | Ölçülen |
|---|---|---|---|---|---|

## Test Verisi
## Ortam ve Üretimden Farklar
| Konu | Üretim | Test | Sonuçlara etkisi |
|---|---|---|---|
## İzleme
## Giriş ve Çıkış Kriterleri
## Riskler, Takvim ve Roller
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her hedefin tanımlı bir yük altında yüzdelik olarak ifade edilmiş sayısal bir kabul kriteri var ya da `[TBD]` olarak işaretli.
- [ ] İş yükü modeli kaynağını ve hesabını gösteriyor; tahmine dayalı sayılar `[VARSAYIM]` olarak etiketli.
- [ ] Her test türünün yalnızca adı değil, belirtilmiş bir amacı var.
- [ ] Ortamın üretimden farkları sonuçlara etkileriyle listelendi.
- [ ] Test verisi ham kişisel veri içermiyor ve önemli olduğu yerde üretim dağılımına uyuyor.
- [ ] İzleme, test edilen sistemin yanında yük üreticilerini de kapsıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ortalamaları kabul kriteri olarak kullanmak. Ortalamalar kuyruk gecikmesini gizler; p95/p99 kullan.
- Az sayıda sanal kullanıcı ve düşünme süresi olmadan kapalı model testler; sistem yavaşladığında test kendini kısar (coordinated omission). Genel trafik için geliş hızı modelleri kullan.
- Önbellek isabeti kusursuz olan küçük test veritabanları; üretimin asla görmeyeceği sonuçlar üretir.

## Örnek
Girdi: "Kampanya checkout trafiğini üç katına çıkarabilir; mevcut zirve checkout'ta 40 istek/sn."

Çıktıdan bir bölüm:
- Hedef: Checkout'ta 120 istek/sn'de (girdideki 40 istek/sn mevcut zirvenin 3 katı) p95 ≤ 800 ms `[VARSAYIM: SLO'yu teyit et]`, hata oranı < %0,5.
| Test | Amaç | Ramp-up | Sabit durum | Hedef yük | Ölçülen |
|---|---|---|---|---|---|
| Yük | Kampanya zirvesini doğrula | 15 dk | 60 dk | 120 istek/sn | Gecikme, hatalar, DB havuz kullanımı |
| Stres | Kırılma noktasını bul | 10 dk'da bir +20 istek/sn | SLO ihlaline kadar | > 120 istek/sn | İlk doyan kaynak |
| Dayanıklılık | Sızıntıları tespit et | 10 dk | 6 sa | 60 istek/sn | Bellek trendi, bağlantı sayısı |
