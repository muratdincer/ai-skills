---
description: "Kodu sürdürülebilirlik açısından inceler: isimlendirme, fonksiyon büyüklüğü ve sorumluluğu, SOLID ve bağımlılık, tekrar, yorumlar ve tanınabilir kod kokuları; konum, etki ve somut düzeltme içeren önceliklendirilmiş bulgular üretir. Kodun temiz, okunabilir veya iyi tasarlanmış olup olmadığı sorulduğunda, bir dosya, sınıf veya modül için sürdürülebilirlik incelemesi istendiğinde ya da kod devre hazırlanırken kullanılır."
related: "refactoring, code-review, coding-standards, review-comment-writing, code-quality-report"
prompt: "Bu OrderService sınıfına Clean Code incelemesi yap; iki yılda büyüdü ve yeni gelenler değiştirmekte zorlanıyor."
---

# Clean Code İncelemesi

## Amaç
Bir kod parçası için kişisel zevke değil, onu okumayı ve değiştirmeyi pahalı hale getiren şeylere odaklanan, önceliklendirilmiş ve uygulanabilir bir sürdürülebilirlik değerlendirmesi vermek.

## Ne zaman kullanılır
- Bir dosya, sınıf veya modül anlaşılması ya da değiştirilmesi zor geliyorsa ve ekip somut bulgular istiyorsa.
- Kod devredilecekse veya önemli ölçüde genişletilecekse.
- Bir geliştirici "çalışıyor"un ötesinde tasarım kalitesi hakkında geri bildirim istiyorsa.

## Ne zaman kullanılmaz
- Doğruluk, güvenlik ve testler dahil tam bir pull request incelemesi gerekiyorsa `code-review` kullanılır.
- İyileştirmelerin uygulanması gerekiyorsa `refactoring` kullanılır.
- Ekip genelinde standartlar veya metrikler gerekiyorsa `coding-standards` veya `code-quality-report` kullanılır.

## Girdiler
Zorunlu:
- İncelenecek kod (dosya, sınıf veya modül) ve dili.

İsteğe bağlı, kaliteyi artırır:
- Ekip kodlama standartları, mimari kurallar, bu kodda yapılacak bir sonraki değişiklik, bilinen sıkıntılar.

Yalnızca bir parça verildiyse onu incele ve hangi sonuçların görülmeyen koda bağlı olduğunu belirt.

## Süreç
1. Önce niyeti anla: kodun neden sorumlu olduğunu 2-3 cümlede özetle; özetleyemiyorsan bu ilk bulgudur.
2. İsimlendirme: isimler niyeti ve alan dilini yansıtıyor mu; yanıltıcı isimler, kodlamalar, belirsiz fiiller (`process`, `handle`, `data`) var mı?
3. Fonksiyonlar: büyüklük, tek soyutlama düzeyi, parametre sayısı, flag argümanları, gizli yan etkiler, command-query ayrımı.
4. Sınıflar ve modüller: tek sorumluluk, bütünlük (cohesion), bağımlılık yönü, teorik değil gerçekten zarar veren SOLID ihlalleri, Demeter yasası, zamansal bağımlılık.
5. Tekrar: aynı ve neredeyse aynı mantık, özellikle tekrarlanan iş kuralları.
6. Kokular: uzun parametre listesi, primitive obsession, data clumps, feature envy, türe göre switch, shotgun surgery, speculative generality, ölü kod.
7. Okunabilirlik açısından yorumlar ve hata yönetimi: kodu tekrar eden ya da yanlış söyleyen yorumlar, yutulan istisnalar, istisnalarla karışık hata kodları.
8. Test edilebilirlik: sabit bağlanmış bağımlılıklar, statik durum, enjekte edilemeyen zaman/rastgelelik/IO.
9. Her bulguyu derecelendir: Blocker (hataya yol açar veya değişikliği engeller), Major (değişikliği yavaşlatır), Minor (okunabilirlik), Nit (stil). Genel kurallar yerine ekibin mevcut kurallarına saygı göster.
10. Her bulgu için konum, etki ve somut düzeltmeyi, tercihen kısa bir önce/sonra ile adlandırılmış bir refactoring olarak ver.
11. Güçlü yönler ve sıralı ilk 3 aksiyonla bitir.
12. Hedef devam ediyorsa öncelikli aksiyonları güvenle uygulamak için `refactoring`, bulguları pull request yorumlarına çevirmek için `review-comment-writing` öner.

## Çıktı formatı
```markdown
# Clean Code İncelemesi: <birim>
Sorumluluk özeti: <2-3 cümle>

## Bulgular
| # | Önem | Konum | Bulgu | Etki | Önerilen düzeltme |
|---|---|---|---|---|---|

## Önce / Sonra (öne çıkan bulgular)
<kısa kod parçaları>

## Güçlü Yönler
- ...

## İlk 3 Aksiyon
1. ...
```

## Kalite kontrol listesi
- [ ] Her bulgu bir konuma atıf yapıyor ve yalnızca kural adını değil maliyeti de açıklıyor.
- [ ] Önem derecesi zevki değil, değişikliğe ve doğruluğa etkiyi yansıtıyor.
- [ ] Önerilen düzeltmeler somut, dile ve mevcut kurallara uygun.
- [ ] Bulgular tekilleştirildi; sistemik sorunlar örneklerle bir kez yazıldı.
- [ ] Varsa en az bir güçlü yön belirtildi.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve varsayım ya da açık soru olarak listeli; dayanağı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kodun aslında net olduğu yerde dogmatik kural uygulamak (örn. "fonksiyonlar N satırın altında olmalı"). Okunabilirliğe ve değişiklik maliyetine göre değerlendir.
- Tek implementasyon için soyutlama önermek. Speculative generality de bir kokudur.
- Tek yapısal sorunu gizleyen uzun bir nit listesi. İlk 3 ile başla.

## Örnek
Girdi: "OrderService, 900 satır: doğrulama, fiyatlama, kalıcılık, e-posta gönderimi."

Çıktıdan bir bölüm:
| # | Önem | Konum | Bulgu | Etki | Önerilen düzeltme |
|---|---|---|---|---|---|
| 1 | Major | `OrderService` | Tek sınıfta dört sorumluluk | Her değişiklik ilgisiz davranışı riske atıyor; testler tüm bağımlılıklara ihtiyaç duyuyor | `OrderPricing` ve `OrderNotifier` çıkar; servisi orkestratör olarak bırak |
| 2 | Major | `placeOrder(…, boolean sendMail)` | Flag argümanı | Tek isim arkasında iki davranış | `placeOrder` olarak ayır, e-posta için `OrderPlaced` olayı yayınla |
