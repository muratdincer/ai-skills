---
description: Bir dokümanı stil rehberine ve terminoloji listesine göre kontrol eder; her sapmayı konum, kural, önem derecesi ve somut yeniden yazımla raporlar: terminoloji, anlatım ve ton, dil bilgisi ve yazım, biçim kuralları, arayüz ve kod atıfları, kapsayıcı ve erişilebilir dil. Dokümantasyon, arayüz metni, sürüm notu veya bilgi bankası makalesi yayımlanmadan ya da gözden geçirmeye gönderilmeden önce, birden fazla yazar tutarsız içerik ürettiğinde ya da bir ekip kendi veya kamuya açık bir stil rehberini uygulamak istediğinde kullanılır.
related: glossary-builder, document-review, document-simplify, user-guide, how-to-guide
prompt: Bu kurulum kılavuzunu stil rehberimize ve terminoloji listemize göre kontrol et, düzeltmeleri tablo olarak ver.
---

# Stil Rehberi Kontrolü

## Amaç
Bir dokümanı kurumun yazım kuralları ve onaylı terminolojisiyle tutarlı hâle getirmek. Her bulgu bir kurala bağlanır ve uygulanmaya hazır bir düzeltme içerir; böylece gözden geçirenler ve yazarlar zamanı üslup tartışmasına değil içeriğe harcar.

## Ne zaman kullanılır
- Bir doküman, yardım sayfası veya arayüz metni seti yayımlanmak ya da gözden geçirmeye gönderilmek üzereyken.
- Birden fazla yazar veya çevirmen tutarsız terim ve biçimle içerik ürettiğinde.
- Bir ekip bir stil rehberini (kendi rehberini ya da büyük bir üreticinin geliştirici dokümantasyon rehberi gibi kamuya açık bir rehberi) benimseyip mevcut içeriği kontrol etmek istediğinde.

## Ne zaman kullanılmaz
- Teknik doğruluk, eksiksizlik veya yapı gözden geçirilecekse `document-review` kullanılır.
- İçerik daha sade bir okuma düzeyine veya uzman olmayan bir kitleye göre yeniden yazılacaksa `document-simplify` kullanılır.
- Terminolojinin kendisi tanımlanacaksa önce `glossary-builder` kullanılır, ardından ona göre kontrol yapılır.

## Girdiler
Zorunlu:
- Kontrol edilecek metin.
- Uygulanacak stil kuralları: stil rehberi (veya ilgili bölümleri) ve varsa terminoloji listesi; ya da kullanıcının açıkça seçtiği, adı belli kamuya açık bir rehber.

İsteğe bağlı, kaliteyi artırır:
- İçerik türü ve hedef kitle (arayüz metni, API dokümanı, son kullanıcı yardımı), hedef dil ve yerel ayar kuralları.
- Bilinen istisnalar, ürün adları ve ticari markalar, önceki gözden geçirme yorumları.

Stil kuralları verilmediyse hangi rehberin uygulanacağını sor. Kullanıcının rehberi yoksa asgari bir temel öner (tutarlı terimler, etken çatı, yalnızca ilk harfi büyük başlıklar, ikinci tekil/çoğul şahıs, yerel tarih/sayı biçimleri) ve bu temelden gelen her bulguyu `[TEMEL – üzerinde anlaşılmış kural değil]` olarak etiketle. Sana verilmemiş bir rehbere kural atfetme.

## Süreç
1. Uygulanacak kuralları kategorilere göre kısa bir kontrol listesine çıkar: terminoloji, anlatım ve ton, dil bilgisi ve yazım, büyük harf ve noktalama, başlıklar ve listeler, arayüz etiketleri ve kod biçimi, sayı/tarih/birim, bağlantılar, kapsayıcı ve erişilebilir dil.
2. Terim listesini oluştur: onaylı terim, yasaklı varyantlar, ürün adları ve yazılışları; metnin tek bir kavram için birden fazla varyant kullandığı yerleri not et.
3. Dokümanı bölüm bölüm oku; her sapmayı konumu (başlık veya paragraf), alıntılanan orijinal metin, çiğnenen kural ve somut yeniden yazımla kaydet.
4. Önem derecesini belirle: Mutlaka düzelt (terminolojiyi, hukuki/ticari marka kurallarını, erişilebilirliği veya anlamı bozuyor), Düzeltilmeli (açık kural ihlali), Değerlendir (tercih veya okunabilirlik).
5. Erişilebilirlikle ilgili yazımı kontrol et: açıklayıcı bağlantı metni, görseller için alternatif metin yer tutucuları, yalnızca renge veya konuma dayanan talimat olmaması, sade dilli başlıklar (WCAG 2.2 içerik rehberliğiyle uyumlu).
6. Kural ihlallerini kendi tercihlerinden ayır; verilen kurallarla desteklenmeyen her şey `[ÖNERİ]` olarak etiketlenir ve asla Mutlaka düzelt olmaz.
7. Tekrarlayan sorunları, aynı düzeltmeyi defalarca listelemek yerine tekrar sayısı ve konumlarıyla tek bir örüntü bulgusunda topla.
8. Belirsiz veya birbiriyle çelişen kuralları ve bir kuralın uygulanmasının teknik anlamı değiştireceği durumları işaretle; bunları sessizce yeniden yazmak yerine açık sorulara taşı.
9. İstenirse düzeltilmiş metni üret; kural doğrudan onlarla ilgili değilse teknik içeriği, kodu ve arayüz etiketlerini değiştirme.
10. Özetle: önem derecesine ve kategoriye göre sayılar, öne çıkan örüntüler ve rehberde netleştirilmesi gereken kurallar.
11. Kullanıcının hedefi devam ediyorsa terimleri resmileştirmek için `glossary-builder`, teknik doğruluk için `document-review` ya da okunabilirlik için `document-simplify` öner.

## Çıktı formatı
```markdown
# Stil Kontrolü: <doküman>
Uygulanan kurallar: <stil rehberi / sürüm / bölümler> | Terminoloji listesi: <ad veya yok>

## Özet
Mutlaka düzelt: <n> | Düzeltilmeli: <n> | Değerlendir: <n>
Öne çıkan örüntüler: ...

## Bulgular
| # | Konum | Orijinal | Kural | Önem | Önerilen yeniden yazım |

## Terminoloji Tutarlılığı
| Kavram | Onaylı terim | Bulunan varyantlar (sayı) |

## Erişilebilirlik Notları
- ...

## Açık Sorular ve Kural Boşlukları
- <belirsiz veya çelişen kural / anlam riski>
```

## Kalite kontrol listesi
- [ ] Her bulgu verilen rehberden belirli bir kurala dayanıyor ya da `[ÖNERİ]` / `[TEMEL – üzerinde anlaşılmış kural değil]` olarak etiketli.
- [ ] Her bulgunun kesin konumu, alıntılanmış orijinali ve somut yeniden yazımı var.
- [ ] Tekrarlayan sorunlar sayılarıyla birlikte örüntü olarak gruplanmış.
- [ ] Hiçbir yeniden yazım teknik anlamı, kodu, komutları veya arayüz etiketlerini istemeden değiştirmiyor.
- [ ] Terminoloji varyantları terminoloji tablosunda toplanmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kişisel zevki kural gibi sunmak. Her Mutlaka düzelt/Düzeltilmeli bulgusunu rehbere bağla; gerisi öneridir.
- Arayüz etiketlerini veya kod tanımlayıcılarını metin kurallarına uydurmak için "düzeltmek". Arayüz ve kodu üründe göründüğü gibi birebir alıntıla.
- Aynı virgül hatasını 40 kez listelemek. Örüntüyü konumlarıyla bir kez raporla ki yazar tek seferde düzeltsin.

## Örnek
Girdi: "Rehberimize göre kontrol et: başlıklarda yalnızca ilk harf büyük, 'oturum açın' kullanılır ('login olun' değil), okura 'siz' diye hitap edilir, 'sadece/basitçe' kullanılmaz."

Çıktıdan bir bölüm:
- Zayıf: "Bazı yerlerde ton daha iyi olabilir."
- Güçlü: "| 3 | §Başlarken, 2. paragraf | 'Admin Console'a basitçe login olun' | 'basitçe' yasak; fiil olarak 'oturum açın' | Düzeltilmeli | 'Admin Console'da oturum açın' |"
- Örüntü: "Ağ Geçidini Yapılandırma" başlığı ve 6 başlık daha her kelimeyi büyük harfle yazıyor → yalnızca ilk harf büyük (Düzeltilmeli, 7 tekrar).
- Açık soru: "Admin Console" her yerde büyük harfle yazılmış – ürün adı mı, genel terim mi? Terminoloji listesiyle teyit et.
