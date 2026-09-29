---
name: velocity-analysis
description: "Bir ekibin hız (iterasyon başına puan) veya verim (hafta/iterasyon başına madde) geçmişini analiz eder: trend, değişkenlik, aykırı değerler ve nedenleri ile kalan iş için aralık tabanlı bir öngörü üretir. İterasyon veya verim rakamları paylaşılıp ekibin hızlanıp yavaşladığı, ne kadar öngörülebilir olduğu ya da bir backlog'un kaç iterasyon süreceği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "Hız/verim analizi"
  related: "monte-carlo-forecast, burndown-analysis, cycle-time-analysis, release-planning, engineering-metrics-review"
  prompt: "Son 10 sprint hızımız: 21, 34, 29, 18, 31, 33, 12, 30, 28, 32. Sürümde 180 puan kaldı. Bu bize ne söylüyor ve ne zaman bitirebiliriz?"
---

# Hız/Verim Analizi

## Amaç
Ham hız veya verim rakamlarını, ekibin teslim hızı ve öngörülebilirliği hakkında dürüst bir okumaya ve paydaşların planlamada kullanabileceği bir kalan iş öngörü aralığına dönüştürmek; bunu yaparken metriği bir hedefe çevirmemek.

## Ne zaman kullanılır
- İterasyon hızları veya haftalık verim sayıları var ve ne anlama geldikleri soruluyor.
- Bir sürüm veya backlog için "kaç iterasyon" tahmini gerekiyor.
- Hız düştü veya sıçradı ve ekip nedenini anlamak istiyor.

## Ne zaman kullanılmaz
- Güven seviyeleriyle olasılığa dayalı tarih veya kapsam öngörüsü için `monte-carlo-forecast` kullanılır.
- Mevcut iterasyon içindeki ilerleme için `burndown-analysis` kullanılır.
- Tek tek maddelerin ne kadar sürdüğünü anlamak için `cycle-time-analysis` kullanılır.

## Girdiler
Zorunlu:
- Eskiden yeniye en az 5 veri noktasından oluşan bir seri (iterasyon başına hız veya dönem başına verim).

İsteğe bağlı, kaliteyi artırır:
- Aynı birimde kalan backlog büyüklüğü.
- Dönem bazında bağlam: ekip değişiklikleri, tatiller, olaylar, kapsam değişiklikleri, tahmin ölçeği değişiklikleri.
- Devreden veya kısmen biten iş kuralları.

5'ten az nokta varsa her öngörünün çok belirsiz olduğunu belirt ve `[DÜŞÜK GÜVEN]` olarak işaretle. Boşlukları asla uydurma değerlerle doldurma.

## Süreç
1. Veriyi doğrula: baştan sona aynı birim, aynı ekip bileşimi, aynı sayma kuralı (yalnızca tamamen biten maddeler). Kırılmaları (ör. tahmin ölçeğinin sıfırlanması) işaretle ve yalnızca karşılaştırılabilir dönemleri analiz et.
2. Tanımlayıcı istatistikleri hesapla: ortalama, medyan, en düşük, en yüksek ve çeyrekler açıklığı; 8 veya daha fazla nokta varsa 25. ve 75. yüzdelikleri de ver. Hesabı göster.
3. Değişkenliği açıkla: değişim katsayısı (standart sapma / ortalama). Pratik kural olarak ~0,2 altı istikrarlı, 0,2-0,4 orta, ~0,4 üstü öngörülemez `[pratik kural]`.
4. Trendi 3 dönemlik hareketli ortalamayla belirle; son 3-5 dönemin yükseldiğini, yatay kaldığını veya düştüğünü belirt ve 2 noktadan trend çıkarma.
5. Aykırı değerleri verilen bağlamla açıkla; bağlam yoksa olası nedenleri ekibe sorulacak `[ÇIKARIM]` soruları olarak listele.
6. Kalan işi aralık olarak öngör: kalan ÷ yüksek hız (iyimser), ÷ medyan (olası), ÷ düşük hız (kötümser, ör. 25. yüzdelik). Tam iterasyona yukarı yuvarla ve verilmedikçe kapsam artışının dahil olmadığını belirt.
7. Kapsam zamanla değişiyorsa bunu not et; sabit kapsam varsaymak yerine kapsamı bir burnup grafiğinde izlemeyi öner.
8. Sağlık gözlemleri ekle: metrik manipülasyonu işaretleri (sonuçlar yatayken sürekli yükselen puanlar), büyük devir veya hız ile verim arasındaki uyumsuzluk.
9. 2-4 öneri yaz (ör. madde boyutu farklılığını azaltmak, ekibi istikrara kavuşturmak, tarihler için `monte-carlo-forecast` kullanmak).
10. Kullanıcının hedefi devam ediyorsa olasılığa dayalı taahhütler için `monte-carlo-forecast`, planı güncellemek için `release-planning` öner.

## Çıktı formatı
```markdown
# Hız/Verim Analizi – <ekip>, <dönemler>
Birim: <iterasyon/hafta başına puan/madde> · Veri noktası: <n> · Karşılaştırılabilir aralık: <...>

## İstatistikler
| Ortalama | Medyan | En düşük | En yüksek | P25 | P75 | DK |
|---|---|---|---|---|---|---|
Yorum: <istikrarlı / orta / öngörülemez>

## Trend
<yükseliyor/yatay/düşüyor> – <hareketli ortalamadan kanıt>

## Aykırı Değerler
| Dönem | Değer | Neden (belirtilen / [ÇIKARIM]) |
|---|---|---|

## <kalan büyüklük> için Öngörü
| Senaryo | Kullanılan hız | Gereken iterasyon |
|---|---|---|
Uyarılar: <kapsam artışı, ekip değişiklikleri, az veri>

## Öneriler
- ...
```

## Kalite kontrol listesi
- [ ] Hesaplamalar gösterildi ve girdiden yeniden üretilebilir.
- [ ] Karşılaştırılamayan dönemler çıkarıldı veya işaretlendi.
- [ ] Öngörü asla tek bir sayı değil, uyarılarıyla birlikte bir aralık.
- [ ] Aykırı değer nedenleri ya girdide belirtilmiş ya da `[ÇIKARIM]` olarak etiketli.
- [ ] Hız ekipleri veya bireyleri karşılaştırmak için kullanılmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Aykırı değerler çarpıtırken ortalamayı kullanmak. Medyanı ve yüzdelikleri tercih et.
- Hızı verimlilik olarak görmek. Hız, teslim edilen değeri değil ekibin kendi tahmin ölçeğini ölçer.
- Backlog büyümeye devam ederken sabit kapsamla öngörü yapmak. Kapsam artışını ayrıca izle.

## Örnek
Girdi: hızlar 21, 34, 29, 18, 31, 33, 12, 30, 28, 32; kalan 180 puan.

Çıktıdan bir bölüm:
- Medyan 29,5, P25 ~20, P75 ~32, ortalama 26,8, DK ~0,27 → orta değişkenlik.
- Aykırı: 7. iterasyonda 12 – nedeni bilinmiyor `[ÇIKARIM: tatil mi, olay mı?]`.
- Öngörü: 180 ÷ 32 ≈ 6 (iyimser), ÷ 29,5 ≈ 7 (olası), ÷ 20 = 9 (kötümser) iterasyon; kapsam artışı hariç.
