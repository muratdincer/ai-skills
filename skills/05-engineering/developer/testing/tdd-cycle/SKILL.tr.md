---
description: "Bir davranışı kodlamayı katı kırmızı-yeşil-refactor döngüleriyle yönetir: en basitten en zora sıralı bir test listesi, her seferinde doğru nedenle kırıldığı görülen tek bir başarısız test, geçmek için gereken en az kod ve yalnızca yeşildeyken refactoring; başarısız bir test olmadan üretim kodu yazılmaz. Bir özellik, fonksiyon veya hata düzeltmesi test önce yaklaşımıyla geliştirilmek istendiğinde, TDD adımları sorulduğunda ya da somut bir davranış üzerinde TDD pratiği veya gösterimi yapılmak istendiğinde kullanılır."
related: "unit-test-writing, implement-from-story, refactoring, acceptance-criteria, test-gap-finder"
prompt: "TDD ile bir parola gücü doğrulayıcısı geliştirelim: en az 12 karakter, en az bir rakam ve bir sembol, kullanıcının e-postasını içermemeli."
---

# TDD ile Geliştirme

## Amaç
Çalışan ve tamamen test edilmiş kodu küçük, doğrulanmış adımlarla büyütmek. Böylece her üretim kodu satırı bir test onu gerektirdiği için vardır ve tasarım, tahminden değil kodun nasıl kullanıldığından ortaya çıkar.

## Ne zaman kullanılır
- Yeni bir davranış, fonksiyon veya sınıf yazılmak üzereyken ve beklenen davranış ifade edilebiliyorsa.
- Bir hata düzeltilecekse: onu yeniden üreten başarısız bir testle başla.
- Ekip somut bir davranış için örnek bir TDD dizisi istiyorsa (eşli çalışma, kata, eğitim).

## Ne zaman kullanılmaz
- Kod zaten varsa ve yalnızca test gerekiyorsa `unit-test-writing` kullanılır.
- Davranışın kendisi bilinmiyor ve önce keşfedilmesi gerekiyorsa; spike yap, `spike-report` kullan ve TDD ile yeniden başla.
- Birden fazla bileşene yayılan büyük bir hikaye planlanacaksa `implement-from-story` kullanılır; o beceri bu beceriyi görev bazında uygulayabilir.

## Girdiler
Zorunlu:
- Geliştirilecek davranış; kurallar, örnekler veya kabul kriterleri olarak.

İsteğe bağlı, kaliteyi artırır:
- Dil ve test çatısı, davranışın bağlanacağı mevcut kod, kodlama kuralları.

Davranış ilk başarısız testi yazmaya yetmeyecek kadar belirsizse kural hakkında her seferinde tek bir odaklı soru sor (bir seferde en fazla 5). Kendi doldurduğun her kuralı `[VARSAYIM]` olarak işaretle ve ilk döngüden önce listele.

## Süreç
1. Test listesi yaz: davranışın somut örnekleri; en basit dejenere durumdan (boş, null, sıfır) çekirdek kurala, oradan uç ve hata durumlarına. Çıkarım yaptığın örnekleri `[VARSAYIM]` olarak işaretle. Liste yaşayan bir backlog'dur; yeni fikirleri kodlamak yerine listeye ekle.
2. Kırmızı: En az kodla en çok şey öğretecek sonraki örneği seç. Keşke var olsaydı dediğin API'yi kullanarak onun için Arrange-Act-Assert yapısında tek bir test yaz.
3. Testi çalıştır ve doğru nedenle kırıldığını gör: derleme hatası, eksik import veya yanlış hazırlık değil, beklenen değerde bir assertion hatası. Beklenmedik biçimde geçerse davranış zaten vardır ya da test yanlıştır; devam etmeden önce araştır.
4. Yeşil: Testi geçirmek için gereken en az üretim kodunu yaz; en basit adım buysa sahte değer döndürmek (fake-it) dahil. Başarısız bir testin gerektirmediği davranışı ekleme.
5. Tüm testleri çalıştır; hepsi yeşil olmalı. Önceki bir test kırılırsa test yanlış değilse testi değil kodu düzelt.
6. Yalnızca yeşildeyken refactor et: test ile kod arasındaki tekrarı kaldır, isimleri iyileştir, fonksiyon çıkar, ikinci bir örnek zorladığında sahte sabiti genelleştir (üçgenleme). Her değişiklikten sonra testler yeşil kalır; test kodunu da refactor et.
7. Sonraki madde için 2-6. adımları tekrarla. Her döngüyü birkaç dakikalık iş boyutunda tut; bir adım büyürse yeşile geri dön ve daha küçük bir örnek seç.
8. Bir hata ortaya çıktığında önce onu yeniden üreten testi ekle, kırıldığını gör, sonra düzelt.
9. Test listesi boşaldığında ve kabul kriterleri kapsandığında dur; son tasarımı ve test adlarını okunabilir bir şartname olarak gözden geçir.
10. Döngü kaydını, son kodu ve testleri ve yapılan varsayımları raporla.
11. Hedef devam ediyorsa atlanan durumları yoklamak için `test-gap-finder`, daha büyük yapısal düzenleme için `refactoring` veya çevreleyen hikayeye devam etmek için `implement-from-story` öner.

## Çıktı formatı
```markdown
# TDD: <davranış>
Varsayımlar: <liste veya yok>

## Test Listesi
- [x] <örnek> → <beklenen>
- [ ] <örnek> [VARSAYIM]

## Döngü Kaydı
| # | Kırmızı: test | Kırılma nedeni | Yeşil: en az değişiklik | Refactor |
|---|---|---|---|---|
| 1 | boş parola reddedilir | true döndürüyor (stub) | `boşsa false döndür` | – |

## Son Kod
<üretim kodu>

## Son Testler
<test kodu>
```

## Kalite kontrol listesi
- [ ] Onu gerektiren başarısız bir test olmadan hiçbir üretim kodu yazılmadı.
- [ ] Her kırmızı adımda kırılma nedeni yazılı ve bu, derleme veya hazırlık hatası değil beklenen assertion hatası.
- [ ] Her yeşil adım en az değişiklik; spekülatif genellik eklenmedi.
- [ ] Refactoring yalnızca yeşildeyken yapıldı ve tüm testler yeşil kaldı.
- [ ] Test listesi dejenere, çekirdek, uç ve hata durumlarını kapsıyor; çıkarılan kurallar `[VARSAYIM]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Önce birkaç test yazıp sonra tüm kodu yazmak; geri bildirim döngüsü ve ortaya çıkan tasarım kaybolur. Her seferinde tek test.
- Kırmızı kontrolünü atlamak; hiç kırılmamış bir test hiçbir şeyi doğrulamıyor olabilir. Her zaman kırıldığını gör.
- "Yeşil zaten" diye refactoring'i atlamak; tekrar birikir ve kod küçük adımlarla çürür.
- En zor örnekle başlamak; ilk test önemsiz olmalı ki API ve hazırlık ucuza doğrulansın.

## Örnek
Girdi: "Parola doğrulayıcı: en az 12 karakter, en az bir rakam ve bir sembol, kullanıcının e-postasını içermemeli."

Zayıf döngü: dört kuralın hepsini içeren tek test, ardından tüm doğrulayıcı tek seferde.

Güçlü döngüler (bölüm):
1. Kırmızı: `bos_parola_reddedilir` kırılır (stub geçerli döndürüyor). Yeşil: boşsa geçersiz döndür.
2. Kırmızı: `rakam_ve_sembollu_11_karakter_reddedilir`. Yeşil: `< 12` uzunluk kontrolü. Refactor: `MIN_LENGTH` çıkar.
3. Kırmızı: `rakamsiz_12_karakter_reddedilir`. Yeşil: rakam kontrolü.
4. Kırmızı: `buyuk_kucuk_harf_duyarsiz_eposta_iceren_parola_reddedilir` `[VARSAYIM: büyük/küçük harf duyarsız; güvenlik ekibiyle teyit et]`.
