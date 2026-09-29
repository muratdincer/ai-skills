---
description: Her iş öğesi için üç noktalı tahmin (iyimser, en olası, kötümser) üretir ve bunları PERT veya üçgen dağılım formülleriyle beklenen değer, standart sapma ve toplam için güven aralıklarına dönüştürür. Efor veya süre belirsiz olduğunda ve paydaşlar tek bir sayı yerine belirtilmiş bir güven düzeyiyle aralık istediğinde kullanılır.
related: wbs, schedule-plan, budget-plan, technical-estimation, monte-carlo-forecast
prompt: Bu 12 iş paketi için üç noktalı tahmin ver ve toplamı %85 güvenle söyle.
---

# Üç Noktalı (PERT) Tahmin

## Amaç
Belirsiz efor veya süreyi güven düzeyleri belirtilmiş açık aralıklara dönüştürmek; tahmin riskini görünür kılmak ve yedek pay kararlarını desteklemek.

## Ne zaman kullanılır
- Belirsizliği anlamlı olan iş paketlerinde (yeni teknoloji, net olmayan gereksinimler, dış bağımlılıklar).
- Sponsor bir tarih veya maliyet için "ne kadar eminsin?" diye sorduğunda.
- Bütçe veya takvim için yedek pay (contingency) belirlenirken.

## Ne zaman kullanılmaz
- Backlog öğelerinin ekip içi göreli tahmini için `estimation-session` kullanılır.
- Geçmiş verim verisinden öngörü için `monte-carlo-forecast` kullanılır.
- Tek bir teknik görevin mühendislik tahmini için `technical-estimation` kullanılır.

## Girdiler
Zorunlu:
- Açıklamalarıyla iş öğeleri listesi (tercihen WBS paketleri).
- Öğe başına İ/O/K değerleri ya da ekibin bunları verebileceği kadar bağlam.

İsteğe bağlı, kaliteyi artırır:
- Benzer işlerin geçmiş gerçekleşmeleri, ekip kapasitesi, birim (saat, gün, maliyet).

İ/O/K değerlerini asla uydurma. Eksikse bir toplama şablonu ver ve tahmin edenlerden doldurmalarını iste; örnek sayılar `[ÖRNEK]` olarak etiketlenmeli.

## Süreç
1. Birimi (efor saati, adam-gün, takvim süresi) netleştir ve birimleri karıştırma.
2. Her öğe için İ, O, K değerlerini işi yapacak kişilerden topla. İ ≤ O ≤ K olduğunu ve K'nin felaketi değil gerçekçi kötü durumu yansıttığını kontrol et.
3. Dağılımı seç: PERT (beta) B = (İ + 4O + K) / 6, SS = (K − İ) / 6; ekip O ağırlığına güvenmiyorsa üçgen B = (İ + O + K) / 3. Hangisinin kullanıldığını belirt.
4. Öğe başına B ve SS hesapla.
5. Topla: toplam B = B'lerin toplamı; toplam SS = √(SS² toplamı), yalnızca öğeler bağımsızsa geçerlidir. Korelasyonlu öğeleri (ortak risk etkenleri) işaretle ve varsa aralığı genişlet.
6. Normal yaklaşımla güven değerlerini türet: ~%84 ≈ B + 1 SS, ~%90 ≈ B + 1,28 SS, ~%95 ≈ B + 1,645 SS.
7. Varyansa en çok katkı yapan öğeleri (en büyük SS²) belirle ve belirsizliklerini neyin azaltacağını not et.
8. Yedek payı, seçilen güven değeri ile B arasındaki fark olarak öner.
9. Her tahminin varsayımlarını belgele; süre tahmin edilmediyse sonucun takvim süresi değil efor olduğunu belirt.

## Çıktı formatı
```markdown
# Üç Noktalı Tahmin: <kapsam>
Birim: <birim> | Yöntem: <PERT/üçgen> | Tahmin edenler: <roller>
| No | Öğe | İ | O | K | B | SS | Temel varsayım |
|---|---|---|---|---|---|---|---|
| Toplam | | | | | ΣB | √ΣSS² | |

## Güven Düzeyleri
| Güven | Değer |
| %50 | B |
| ~%84 | B + 1 SS |
| ~%95 | B + 1,645 SS |

## Başlıca Varyans Kaynakları
## Önerilen Yedek Pay
## Varsayımlar, Korelasyonlar, Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her öğede İ ≤ O ≤ K sağlanıyor.
- [ ] Formül ve birim belirtildi.
- [ ] Hiçbir İ/O/K değeri uydurulmadı; örnekler etiketli.
- [ ] Toplam verilmeden önce korelasyonlar ele alındı.
- [ ] Sonuçlar tek sayı değil, güven düzeyiyle aralık olarak verildi.

## Sık yapılan hatalar
- "Güvenli" toplam için kötümser değerleri toplamak; bu riski aşırı büyütür. Bunun yerine SS'leri topla.
- Beklenen değeri taahhüt gibi sunmak. Üzerinde anlaşılan bir güven düzeyinde taahhüt ver.
- Çıpalama: önce O'yu sorup İ/K'yi ±%20 olarak türetmek. K'yi "ne ters gidebilir?" diye sorarak topla.

## Örnek
Girdi: "Veri taşıma paketi: İ=10, O=15, K=35 gün."

Çıktıdan bir bölüm:
| İP-4 | Veri taşıma | 10 | 15 | 35 | 17,5 | 4,17 | Kaynak veri kalitesi profillendiği gibi |
- İP-4 toplam varyansın %46'sını oluşturuyor; bir veri profilleme spike'ı K'yi daraltabilir.
