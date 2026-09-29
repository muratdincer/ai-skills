---
name: risk-based-testing
description: "Ürün risk öğelerini olasılık ve etkiye göre değerlendirerek test eforunu önceliklendirir; risk matrisi, öğe bazında test derinliği ve koşum sırası üretir. Zaman veya kişi kısıtlı olduğunda, önce neyin ve ne derinlikte test edileceğine karar verilirken ya da paydaşlar hangi risklerin kapsandığını ve hangilerinin kaldığını görmek istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: strategy
  title: "Risk bazlı test önceliklendirme"
  related: "test-strategy, test-plan, regression-selection, risk-register, impact-analysis"
  prompt: "Bu sürüm için 5 test günümüz var. İşte 14 değişiklik. Önce neyi, ne derinlikte test edelim?"
---

# Risk Bazlı Test Önceliklendirme

## Amaç
Kısıtlı test süresini, hatanın hem olası hem de maliyetli olduğu alanlara yönlendirmek ve kalan riski açıkça göstermek. Böylece sürüm kararı umuda değil bilgiye dayanır.

## Ne zaman kullanılır
- Test penceresi tam kapsam için gereken süreden kısa.
- Sürüm, kritiklik düzeyi farklı çok sayıda değişiklik içeriyor.
- Paydaşlar "neyi test etmedik ve ne ters gidebilir?" diye soruyor.
- Bir test stratejisinin veya test planının risk bölümü hazırlanıyor.

## Ne zaman kullanılmaz
- Kod değişikliğinin etkisine göre regresyon testi seçilecekse `regression-selection` kullanılır.
- Proje teslimat riskleri (kişi, takvim, bütçe) yönetiliyorsa `risk-register` kullanılır.
- Bir ürün için bütüncül test yaklaşımı gerekiyorsa `test-strategy` kullanılır.

## Girdiler
Zorunlu:
- Değerlendirilecek özellik, değişiklik, gereksinim veya bileşen listesi.

İsteğe bağlı, kaliteyi artırır:
- Öğe bazında iş kritikliği, kullanım hacmi, mevzuatla ilgisi.
- Alan bazında değişiklik büyüklüğü, karmaşıklık, yeni teknoloji, geliştirici deneyimi, hata geçmişi.
- Mevcut test kapasitesi (gün, kişi).

Öğe listesi yoksa iste. Eksik faktör değerleri `[VARSAYIM]` ile derecelendirilir ve teyit için işaretlenir.

## Süreç
1. Girdiyi tutarlı bir ayrıntı düzeyinde risk öğelerine dönüştür (tekil test case değil, özellik veya iş akışı).
2. Ölçekte anlaş: olasılık ve etki için 1-5 veya Y/O/D; derecelerin karşılaştırılabilir olması için her birine tek satırlık tanım yaz.
3. Olasılığı teknik faktörlerden derecelendir: karmaşıklık, değişiklik miktarı, yeni veya yabancı teknoloji, entegrasyon sayısı, hata geçmişi, zaman baskısı.
4. Etkiyi iş faktörlerinden derecelendir: finansal kayıp, yasal/mevzuat riski, etkilenen kullanıcı sayısı, veri bütünlüğü, emniyet, itibar, geçici çözüm olup olmadığı.
5. Risk skorunu (olasılık x etki) hesapla ve öğeleri matrise yerleştir. Eşitlikte etkiye göre sırala.
6. Skor bantlarını test derinliğine eşle: ör. 15-25 kapsamlı (birden fazla teknik, negatif ve fonksiyonel olmayan testler, bağımsız gözden geçirme), 8-14 standart, 1-7 smoke veya kabul.
7. Yüksek riskli her öğe için teknik seç (sınır değer, karar tablosu, durum geçişi, keşif testi görev tanımı, performans, güvenlik).
8. Koşumu sırala: en yüksek risk önce; böylece en erken geri bildirim en maliyetli hataları hedefler.
9. Kapasite verildiyse derinliği kapasiteye uydur; azaltılan veya çıkarılanları listele.
10. Kalan riski belirt: hafif test edilen veya hiç test edilmeyen öğeler ve bunu kimin kabul etmesi gerektiği.
11. Yeniden değerlendirme tetikleyicilerini öner (kapsam değişikliği, hataların tek bir alanda yoğunlaşması).
12. Kullanıcı devam ederse odaklanan eforu planlamak için `test-plan`, dereceleri bir değişikliğe uygulamak için `regression-selection` öner.

## Çıktı formatı
```markdown
# Risk Bazlı Test Önceliklendirmesi: <sürüm / kapsam>
Ölçek: Olasılık 1-5 (<tanımlar>) · Etki 1-5 (<tanımlar>)

| # | Risk öğesi | Olasılık (neden) | Etki (neden) | Skor | Derinlik | Teknikler | Sıra |
|---|---|---|---|---|---|---|---|

## Risk Matrisi
<öğe numaralarını gösteren 5x5 veya Y/O/D ızgarası>

## Kapasiteye Uyum
- Mevcut: <gün / kişi veya [BİLİNMİYOR]>
- Azaltılan veya çıkarılan: <öğeler ve gerekçe>

## Kabul Edilecek Kalan Risk
| Öğe | Kalan risk | Kabul sorumlusu |

## Yeniden Değerlendirme Tetikleyicileri
- ...
```

## Kalite kontrol listesi
- [ ] Her derecenin kısa bir gerekçesi var; gerekçesiz derecelendirme yok.
- [ ] Olasılık ve etki birbirinden bağımsız derecelendirildi (ikisi de "önem"den türetilmedi).
- [ ] Öğeler tutarlı bir ayrıntı düzeyinde.
- [ ] En yüksek riskli öğeler koşum sırasında en başta.
- [ ] Kalan risk ve kabul sorumlusu açıkça yazılı.
- [ ] Varsayılan dereceler `[VARSAYIM]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her şeyi yüksek derecelendirmek. Dağılımı zorla; öğelerin üçte birinden fazlası en üst banttaysa ölçeği yeniden kalibre et.
- Az değişen ama iş açısından kritik alanların etkisini yok saymak. Ödeme kodundaki küçük değişiklik de derinlik ister.
- Değerlendirmeyi tek seferlik görmek. Hatalar yoğunlaştığında veya kapsam değiştiğinde yeniden derecelendir.

## Örnek
Girdi: "5 test günü, yeni KDV hesaplaması, logo değişikliği, PDF'e aktarma dahil 14 değişiklik."

Çıktıdan bir bölüm:
| 1 | Yeni KDV hesaplaması | 4 (yeni kurallar, 3 oran) | 5 (yasal, faturalar) | 20 | Kapsamlı | Karar tablosu, sınır değer | 1 |
| 9 | Logo değişikliği | 1 | 1 | 1 | Smoke | Görsel kontrol | 14 |
- Kalan risk: Eski tarayıcılarda PDF aktarımı test edilmedi; ürün sahibi kabulü `[TBD]`.
