---
description: "Bir sonraki değişiklik için önemli olan kod kokularını belirleyerek, davranışı karakterizasyon testleriyle güvenceye alarak ve adlandırılmış refactoring'leri (Extract Function, Replace Conditional with Polymorphism, Introduce Parameter Object vb.) davranışı koruyan küçük adımlarla uygulayarak kodu güvenli biçimde yeniden düzenler. Kod değiştirilmesi zor olduğunda, dağınık koda özellik eklemeden önce ya da davranışı değiştirmeden kodun temizlenmesi, yeniden yapılandırılması istendiğinde kullanılır."
related: "clean-code-review, legacy-code-comprehension, unit-test-writing, tech-debt-assessment, code-review"
prompt: "Bu 200 satırlık calculatePrice metodunu refactor et; gelecek sprint yeni bir indirim türü eklemem gerekiyor ve burada her değişiklik bir şeyi bozuyor."
---

# Kodu Yeniden Düzenleme

## Amaç
Kodun gözlemlenebilir davranışını değiştirmeden iç yapısını iyileştirmek; böylece bir sonraki değişiklik ucuz ve güvenli hale gelir. Bunu doğrulanabilecek ve incelenebilecek kadar küçük adımlarla yapmak.

## Ne zaman kullanılır
- Bir özellik veya düzeltme, anlaşılması ya da değiştirilmesi zor kod yüzünden tıkanmışsa ("önce değişikliği kolaylaştır, sonra kolay değişikliği yap").
- İnceleme veya analiz, sık değişen kodda düzeltmeye değer kokular bulduysa.
- Tekrarlanan mantık daha fazla ayrışmadan birleştirilmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Değişiklik değil, yalnızca sorunların değerlendirmesi gerekiyorsa `clean-code-review` veya `tech-debt-assessment` kullanılır.
- Kod henüz anlaşılmadıysa önce `legacy-code-comprehension` kullanılır.
- Amaç yapı değil hızsa `performance-optimization` kullanılır.

## Girdiler
Zorunlu:
- Yeniden düzenlenecek kod ve gerekçe (yaklaşan değişiklik ya da yarattığı sıkıntı).

İsteğe bağlı, kaliteyi artırır:
- Mevcut testler, kodlama standartları, dil/framework sürümü, kısıtlar (public API değişmemeli, yeni bağımlılık yok).

Test yoksa ve çalıştırılamıyorsa bunu açıkça söyle ve karakterizasyon testleriyle başla; kanıt olmadan davranışın korunduğunu iddia etme.

## Süreç
1. Hedefi bir sonraki değişiklik üzerinden yaz ("yeni indirim türü eklemek tek bir sınıfa dokunmalı").
2. Bu hedefi engelleyen kokuları belirle (uzun fonksiyon, tekrarlanan koşul, feature envy, primitive obsession, shotgun surgery); kozmetik olanları yok say.
3. Güvenlik ağını kontrol et: hangi davranışlar testlerle kapsanıyor? Kapsanmayan yollar için, tuhaf mevcut davranışlar dahil karakterizasyon testleri ekle (kaydet, şimdi düzeltme).
4. Refactoring kataloğundaki adlandırılmış teknikleri seç ve düşük riskliden (rename, extract variable, extract function) yapısal olana (move function, replace conditional with polymorphism, split phase) doğru sırala.
5. Her adımda tek bir refactoring uygula; her adımdan sonra kod derlenir ve testler geçer. Davranış değişikliklerini ve hata düzeltmelerini refactoring commit'lerinin dışında tut.
6. Anlaşma olmadıkça public sözleşmeleri sabit tut; imza değişmek zorundaysa paralel değişiklik uygula (yeniyi ekle, çağıranları taşı, eskiyi kaldır).
7. Anlamsal tuzaklara dikkat et: değerlendirme sırası, taşınan koddaki yan etkiler, null/boş durumları, istisna tipleri, kayan nokta veya yuvarlama farkları, dışarı çıkarılan durumun thread güvenliği.
8. Dizi bitince önceki ve sonraki hali hedefe göre karşılaştır, geçici iskeleti kaldır.
9. Her adımı refactoring adı, önerilen commit sınırı ve keşfedilen davranış tuhaflıklarıyla raporla.
10. Hedef devam ediyorsa karakterizasyon testlerinin eksik olduğu yerler için `unit-test-writing` veya yeniden düzenlenen değişikliğin incelenmesi için `code-review` öner.

## Çıktı formatı
```markdown
# Refactoring: <birim>
Hedef: <bir sonraki değişiklik nasıl görünmeli>
Güvenlik ağı: <mevcut testler / eklenen karakterizasyon testleri>

## Ele Alınan Kokular
| Koku | Konum | Hedefi neden engelliyor |

## Adımlar
| # | Refactoring | Değişiklik | Testler yeşil mi? |
|---|---|---|---|
| 1 | Extract Function | .. satırlarından `applySeasonalDiscount` | Evet |

## Sonuç
<nihai kod veya diff>

## Keşfedilen Davranış Tuhaflıkları (değiştirilmedi)
- ...
```

## Kalite kontrol listesi
- [ ] Gözlemlenebilir davranış değişmedi; öncesinde ve sonrasında çalışan testlerle destekleniyor.
- [ ] Her adım, tek başına incelenebilecek kadar küçük, adlandırılmış bir refactoring.
- [ ] Araya hata düzeltmesi veya özellik karışmadı; tuhaflıklar ayrıca raporlandı.
- [ ] Public API değişmedi ya da paralel değişiklikle değiştirildi.
- [ ] Sonuç, belirtilen bir sonraki değişikliği gösterilebilir biçimde kolaylaştırıyor.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve varsayım ya da açık soru olarak listeli; dayanağı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Refactoring adı verilen "büyük patlama" yeniden yazımı. Yeşil adımlarla yapılamıyorsa bu bir yeniden yazımdır ve kendi planını gerektirir.
- Kimsenin bir daha değiştirmeyeceği kodu refactor etmek. Değişim sıklığına ve yaklaşan işe göre önceliklendir.
- Çıkarma sırasında tuhaf davranışı sessizce "düzeltmek"; çağıranlar ona bağımlı olabilir. Kaydet ve ayrı bir değişiklikte düzelt.

## Örnek
Girdi: "calculatePrice müşteri türü ve indirim türü için iç içe if/else içeriyor; yeni indirim eklemek bir şeyleri bozuyor."

Çıktıdan bir bölüm:
1. Karakterizasyon testleri: müşteri türü × indirim türünün 12 kombinasyonu, yarım kuruşların mevcut yuvarlanması dahil (tuhaflık kaydedildi).
2. Split Phase: "uygulanacak indirimleri belirle" ile "indirimleri fiyata uygula" ayrıldı.
3. Replace Conditional with Polymorphism: tür başına bir implementasyonu olan `Discount` arayüzü; yeni tür = yeni sınıf + kayıt.
