---
description: "Adayları koşum sıklığı, iş riski, özelliğin kararlılığı, deterministiklik, veri ve ortam kontrolü ile yazma/bakım maliyetine göre puanlayarak hangi testlerin otomatikleştirileceğini seçer; her birini güvenilir en ucuz test seviyesine yerleştirir ve kaba geri dönüş tahminiyle sıralı bir backlog verir. Ekip sırada neyi otomatikleştireceğini sorduğunda, büyük bir manuel regresyon seti olduğunda, otomasyon yatırımı gerekçelendirilecekken ya da düşük değerli UI testlerinin otomasyonu durdurulmak istendiğinde kullanılır."
related: automation-framework-design, test-automation-script, regression-selection, risk-based-testing, flaky-test-analysis
prompt: "350 manuel regresyon case'imiz var. Önce hangilerini, hangi seviyede otomatikleştirmeliyiz?"
---

# Otomasyon Adayı Seçimi

## Amaç
Otomasyon eforunu karşılığını verdiği yere harcamak: sık koşulan, yüksek riskli, kararlı ve deterministik kontroller, onları kanıtlayabilen en alt test seviyesinde. Böylece set, kırılgan bir UI katmanına dönüşmek yerine hızlı ve bakımı kolay kalır.

## Ne zaman kullanılır
- Manuel regresyon seti sürüm ritmine göre çok yavaş kaldığında ve ekibin nereden başlayacağını seçmesi gerektiğinde.
- Otomasyon bütçesi veya kapasitesi yönetime gerekçelendirilecekken.
- Mevcut otomatik setin bakımı pahalıya geldiğinde ve budanması ya da seviyesinin değiştirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Testlerin koşacağı çatının tasarlanması gerekiyorsa `automation-framework-design` kullanılır.
- Belirli bir değişiklik için hangi testlerin koşulacağı seçilecekse `regression-selection` kullanılır.
- Otomatik testin kendisi yazılacaksa `test-automation-script` kullanılır.

## Girdiler
Zorunlu:
- Her birinin kısa açıklamasıyla aday listesi (test case'ler, senaryolar veya alanlar).

İsteğe bağlı, kaliteyi artırır:
- Koşum sıklığı, manuel koşum süresi, alan bazında hata geçmişi, risk dereceleri.
- Özelliklerde planlanan değişiklikler, zaten otomatik olan test seviyeleri, CI kısıtları, ekip yetkinlikleri.

Aday listesi yoksa iste. Sıklık veya efor rakamları yoksa göreli dereceler (Yüksek/Orta/Düşük) kullan ve `[VARSAYIM]` olarak işaretle; asla saat veya maliyet rakamı uydurma.

## Süreç
1. Adayları özellik alanına göre grupla; puanlamadan önce mükerrer veya geçersiz case'leri çıkar.
2. Aday olmayanları ele: tek seferlik kontroller, kullanılabilirlik ve görsel yargı, keşif çalışmaları, yeniden tasarlanmak üzere olan özellikler, deterministik hale getirilemeyen akışlar.
3. Kalan her adayı 1-3 arasında puanla: koşum sıklığı, bozulursa iş riski, özellik kararlılığı (az değişim), deterministiklik (net beklenen sonuç, kontrol edilebilir zamanlama), veri/ortam kontrol edilebilirliği ve yazma artı bakım eforu (ters).
4. Değer puanını (sıklık × risk) ve uygulanabilirlik puanını (kararlılık, deterministiklik, kontrol edilebilirlik, efor) hesapla; her adayı 2×2'ye yerleştir: şimdi otomatikleştir, hazırlık işinden sonra otomatikleştir, manuel bırak, çıkar.
5. Her "otomatikleştir" maddesi için test seviyesini seç: unit, bileşen/sözleşme, API/servis veya UI uçtan uca. Kural UI'ın altında kanıtlanabiliyorsa kontrolü aşağı it; UI testlerini birkaç kritik kullanıcı yolculuğuyla sınırla.
6. Yüksek değerli adayları bloke eden hazırlık işlerini (UI'da test ID'leri, API ile veri besleme, dış bağımlılığı stub'lama, test verisini sıfırlama) belirle ve backlog maddesi olarak listele.
7. Göreli geri dönüşü tahmin et: dönem başına tasarruf edilen manuel koşum ile yazma ve bakım eforu karşılaştırması. Kullanıcı rakam verdiyse onları kullan; yoksa gerekçesiyle Yüksek/Orta/Düşük olarak ifade et.
8. Dalgalar halinde sıralı bir otomasyon backlog'u çıkar (ilk dalga = en yüksek değer ve uygulanabilirlik, en küçük hazırlık işi); her maddede bir tamamlanma kriteri olsun (CI'da koşar, tekrarlı koşumlarda deterministik, sorumlu).
9. Manuel kalanları ve nedenlerini kaydet; böylece karar görünür olur ve koşullar değiştiğinde yeniden ele alınır.
10. Kullanıcı devam ederse uygun bir çatı yoksa `automation-framework-design`, ilk dalga maddeleri için `test-automation-script`, mevcut testler kararsızsa `flaky-test-analysis` öner.

## Çıktı formatı
```markdown
# Otomasyon Adayı Seçimi: <ürün/set>
## Puan Ölçeği
- 1 = düşük, 3 = yüksek (efor: 3 = düşük efor). Varsayılan değerler [VARSAYIM] ile işaretli.

## Puanlanan Adaylar
| No | Aday | Sıklık | Risk | Kararlılık | Deterministiklik | Kontrol edilebilirlik | Efor | Değer | Uygulanabilirlik | Karar | Seviye |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Otomasyon Backlog'u
| Dalga | Madde | Seviye | Hazırlık işi | Geri dönüş (Y/O/D) | Tamamlanma kriteri |
|---|---|---|---|---|---|

## Hazırlık İşleri
- ...
## Manuel Kalanlar (gerekçesiyle)
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Aday olmayanlar (görsel, keşif, değişken, deterministik olmayan) gerekçesiyle elendi.
- [ ] Her "otomatikleştir" kararı davranışı kanıtlayabilen en alt test seviyesini belirtiyor.
- [ ] UI uçtan uca testler kritik yolculuklarla sınırlı.
- [ ] Geri dönüş rakamları kullanıcı verisinden geliyor ya da `[VARSAYIM]` ile işaretli göreli dereceler.
- [ ] Her backlog maddesinin kararlı CI koşumunu içeren bir tamamlanma kriteri var.
- [ ] Manuel kalan maddeler gerekçesiyle listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Manuel seti UI üzerinden bire bir otomatikleştirmek. Yavaş ve kırılgan testler üretir; kuralları API veya unit seviyesine taşı.
- Başarıyı otomatik case sayısıyla ölçmek. Bunun yerine kapsanan riski ve ortadan kalkan manuel süreyi say.
- Değişmek üzere olan bir özelliği otomatikleştirmek. Kararlılığı bekle ya da değişiklikten yalıtılmış bir seviyede otomatikleştir.

## Örnek
Girdi: 350 manuel regresyon case'i; haftalık sürüm; ödeme, fiyatlandırma ve profil alanları.

Çıktıdan bir bölüm:
- PR-014 "12 müşteri segmenti için indirim kuralları": Sıklık 3, Risk 3, Kararlılık 3, Deterministiklik 3 → şimdi otomatikleştir, UI değil API seviyesinde (tablo güdümlü).
- CO-002 "Kartla ödeme mutlu yol": 5 UI yolculuğundan biri olarak şimdi otomatikleştir; hazırlık işi: ödeme sağlayıcısı sandbox stub'ı.
- PF-031 "Tablette profil sayfası yerleşimi": manuel kalır (görsel yargı).
