---
name: hypothesis-statement
description: "Bir ürün fikrini, özellik talebini veya varsayımı \"İnanıyoruz ki / şu sonucu doğuracak / bunu şuradan anlayacağız\" formatında, hedef segmenti, en riskli varsayımı, ölçülebilir sinyali, eşik değeri ve süre sınırı olan yanlışlanabilir bir hipoteze dönüştürür. Ekip bir fikri tam geliştirmeden önce sınamak istediğinde, bir backlog maddesinin beklenen sonucu belirsiz olduğunda ya da ürün hipotezi yazılması, keskinleştirilmesi veya gözden geçirilmesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: discovery
  title: "Ürün hipotezi yazma"
  related: "experiment-design, assumption-mapping, opportunity-solution-tree, problem-statement, ab-test-analysis"
  prompt: "Sepeti sonraya kaydet\" butonu için bir hipotez yaz; mobilde ödeme adımındaki terk oranını düşüreceğini düşünüyoruz."
---

# Ürün Hipotezi Yazma

## Amaç
Bir fikri; kimin davranışının nasıl değişeceğini ve bunu hangi kanıtın doğrulayacağını ya da çürüteceğini söyleyen test edilebilir bir bahis olarak ifade etmek. Böylece ekip "işe yaradı"nın ne demek olduğuna sonuçları sonradan yorumlayarak değil, önceden karar verir.

## Ne zaman kullanılır
- Bir fikir veya özellik talebi, ima edilen bir faydayla ama ölçülebilir bir beklenen sonuç olmadan geldiğinde.
- Fırsat-çözüm ağacındaki bir çözümün yatırımdan önce sınanması gerektiğinde.
- Ekip bir deney yapmak üzereyken bahsin önce yazıya dökülmesi gerektiğinde.
- Yayınlanmış bir özellik değerlendirilirken ilk beklentinin hiç yazılmadığı anlaşıldığında.

## Ne zaman kullanılmaz
- Problemin kendisi henüz anlaşılmamışsa `problem-statement` veya `problem-interview-script` kullanılır.
- Hipotez hazırsa ve test mekaniği (varyantlar, örneklem, durdurma kuralları) gerekiyorsa `experiment-design` kullanılır.
- Hangisinin test edileceğini seçmeden önce çok sayıda varsayımın sıralanması gerekiyorsa `assumption-mapping` kullanılır.

## Girdiler
Zorunlu:
- Sınanacak fikir, değişiklik veya varsayım ve ele aldığı problem ya da fırsat.

İsteğe bağlı, kaliteyi artırır:
- Hedef segment, ilgili metriğin mevcut başlangıç değeri, erişilebilir trafik veya kullanıcı sayısı.
- Fikrin arkasındaki kanıt (araştırma, destek verisi, analitik).
- Sonucun besleyeceği karar ve kararı verecek kişi.

Fikir veya hedeflediği problem yoksa sor. Eksik başlangıç değerleri ölçüm aksiyonuyla birlikte `[BİLİNMİYOR]` olur; asla uydurulmaz.

## Süreç
1. Fikri yeniden ifade et; önerilen değişikliği (ne yapacağız) iddia edilen faydadan (neyin değişmesini bekliyoruz) ayır. Kullanıcının yalnızca ima ettiği faydaları `[VARSAYIM]` olarak işaretle.
2. Davranışı değişmesi beklenen segmenti "kullanıcılar" diye değil, belirli olarak adlandır (ör. "sepetinde 3+ ürün olan, ilk kez alışveriş yapan mobil müşteriler").
3. Altta yatan varsayımları (istenirlik, kullanılabilirlik, yapılabilirlik, sürdürülebilirlik) çıkar ve en riskli olanı seç: yanlışsa fikri öldürecek ve en az kanıta sahip olanı.
4. Hipotezi yaz: "İnanıyoruz ki <segment> için <değişiklik>, <davranış değişikliği> sonucunu doğuracak. <Süre> içinde <metrik> <başlangıç değeri>'nden <eşik>'e çıktığında haklı olduğumuzu anlayacağız."
5. Görüş veya çıktıyı değil davranışı ölçen tek bir birincil metrik ve kötüleşmemesi gereken 1-2 koruma (guardrail) metriği seç.
6. Eşiği, yatırımı haklı çıkaracak en küçük değişim olarak belirle; kullanıcı veremiyorsa bir aday öner ve `[VARSAYIM]` olarak işaretle.
7. Yanlışlama kuralını ve tetikleyeceği kararı yaz: hangi sonuç durdur, yinele veya ölçekle kararına yol açar.
8. En riskli varsayıma uygun, en ucuz ama güvenilir test türünü öner (görüşme, prototip testi, sahte kapı, concierge, A/B).
9. Şimdiye kadarki kanıtları ve açık soruları (başlangıç değerinin kaynağı, trafik, sorumlu) listele.
10. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: testi planlamak için `experiment-design`, birden çok varsayım test sırası için yarışıyorsa `assumption-mapping`.

## Çıktı formatı
```markdown
# Hipotez: <kısa ad>
**En riskli varsayım:** <tür> – <ifade>

> İnanıyoruz ki **<segment>** için **<değişiklik>**,
> **<gözlemlenebilir davranış değişikliği>** sonucunu doğuracak.
> **<Süre>** içinde **<birincil metrik>** **<başlangıç | [BİLİNMİYOR]>** değerinden **<eşik>** değerine ulaştığında haklı olduğumuzu anlayacağız.

| Madde | Değer |
|---|---|
| Birincil metrik | <ad, tanım, kaynak> |
| Koruma metrikleri | <metrik – X'in altına düşmemeli> |
| Yanlışlanma koşulu | <sonuç> |
| Başarı / başarısızlık kararı | <ölçekle / yinele / durdur> |
| Önerilen test | <tür> – <bu varsayıma neden uygun> |
| Karar sahibi | <ad veya [BİLİNMİYOR]> |

## Mevcut Kanıtlar
- <kaynak> – <neye işaret ediyor>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
- <soru> – <kim yanıtlayabilir>
```

## Kalite kontrol listesi
- [ ] Segment belirli, davranış değişikliği gözlemlenebilir.
- [ ] Metrik davranışı ölçüyor; görüşü, özelliğin kendi görüntülenmesini veya teslimatı değil.
- [ ] Eşik ve süre sınırı var; hipotezi çürütecek sonuç yazılmış.
- [ ] Başlangıç değerleri ve eşikler kaynaklı ya da `[BİLİNMİYOR]` / `[VARSAYIM]` olarak işaretli.
- [ ] Önerilen test en kolay olanı değil, en riskli varsayımı hedefliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yanlışlanamayan hipotez yazmak ("deneyimi iyileştirecek"). Yanlış çıkabilecek bir metrik ve eşik koymaya zorla.
- Yeni özelliğin kullanımını başarı saymak. Butona tıklanması merakı kanıtlar, sonucu değil; sonraki davranışı ölç.
- Birkaç değişikliği tek hipotezde toplamak. Ayır; yoksa hangisinin işe yaradığını anlayamazsın.

## Örnek
Girdi: "'Sepeti sonraya kaydet' butonu ekleyelim; mobilde ödeme adımındaki terk oranını düşüreceğini düşünüyoruz."

Zayıf: "Sonraya kaydet butonunun dönüşümü iyileştireceğine inanıyoruz."

Güçlü (bölüm):
> İnanıyoruz ki sepetinde 3+ ürün olan mobil ziyaretçiler için "sepeti sonraya kaydet" seçeneği, bu kişilerin daha fazlasının geri dönüp satın almayı tamamlaması sonucunu doğuracak. 4 hafta içinde 7 günlük sepet geri kazanım oranı [BİLİNMİYOR – mevcut değeri ölç] değerinden +3 puana çıktığında haklı olduğumuzu anlayacağız.
- En riskli varsayım (istenirlik): Mobilde sepeti terk edenler fiyat yüzünden değil, daha sonra almak niyetiyle ayrılıyor `[VARSAYIM]`.
- Koruma metriği: Aynı oturumdaki dönüşüm 1 puandan fazla düşmemeli.
