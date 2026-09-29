---
description: "Belirtilen eşleşme ihtiyacı için hedef motorun lehçesinde bir düzenli ifade (regex) yazar; sade dille parça parça açıklama, eşleşmesi ve eşleşmemesi gereken test durumları tablosu, çapa ve kaçış kararları ve felaket düzeyinde geri izleme (catastrophic backtracking) kontrolü sunar. Mevcut bir regex'i açıklar veya düzeltir. Metni doğrulamak, çıkarmak, aramak veya değiştirmek için desen gerektiğinde, biri regex yapıştırıp ne yaptığını sorduğunda ya da fazla, eksik eşleşen veya yavaş çalışan bir regex bildirdiğinde kullanılır."
related: "code-explanation, unit-test-writing, data-quality-rules, secure-code-review, business-rules-catalog"
prompt: "E-posta konularından INV-2024-000123 gibi fatura numaralarını çıkaran bir regex yaz; JavaScript'te kullanıyoruz."
---

# Regex Oluşturma ve Açıklama

## Amaç
Çalışacağı motorda tam olarak amaçlananı eşleyen, açık pozitif ve negatif durumlarla kanıtlanmış, sonraki geliştiricinin okuyabileceği ve patolojik girdiye karşı güvenli bir desen üretmek.

## Ne zaman kullanılır
- Metni bir desenle doğrulamak, çıkarmak, aramak veya değiştirmek gerektiğinde.
- Mevcut bir regex'in anlaşılması, düzeltilmesi veya hızlandırılması gerektiğinde.
- Gereksinimlerden gelen bir doğrulama kuralının (kodlar, tanımlayıcılar, formatlar) desene dönüşmesi gerektiğinde.

## Ne zaman kullanılmaz
- Formatın gerçek bir ayrıştırıcısı veya standart kütüphane fonksiyonu varsa (URL, RFC 5322'ye göre e-posta, tarih, JSON, HTML) bunun yerine ayrıştırıcıyı öner.
- İhtiyaç bir veri kümesi genelinde veri kalitesi kuralıysa `data-quality-rules` kullanılır.
- Çevredeki kodun genel anlatımı için `code-explanation` kullanılır.

## Girdiler
Zorunlu:
- Neyin eşleşmesi ve neyin eşleşmemesi gerektiği, tercihen gerçek örneklerle.
- Regex motoru veya dil (ör. PCRE, JavaScript, .NET, Java, Python `re`, RE2, POSIX, veritabanı lehçesi).

İsteğe bağlı, kaliteyi artırır:
- Tüm metni mi doğruladığı yoksa metin içinde eşleşme mi aradığı, büyük/küçük harf duyarlılığı, Unicode ihtiyacı, çok satırlı girdi, gereken yakalama grupları, performans kısıtları (güvenilmeyen girdi, boyut).

Motor bilinmiyorsa sor; kullanıcı söyleyemiyorsa ortak bir alt küme için yaz ve motora özgü özellikleri `[MOTORA BAĞLI]` olarak işaretle.

## Süreç
1. Eşleşme kuralını kesin olarak yeniden yaz: izin verilen karakterler, uzunluklar, sabit kısımlar, isteğe bağlı kısımlar, ayraçlar ve eşleşmenin nerede olabileceği.
2. Önce test tablosunu kur: sınırlar (min/maks uzunluk, baştaki/sondaki boşluk, bitişik metin, Unicode, boş) dahil en az beş eşleşmeli ve beş eşleşmemeli durum.
3. Çapayı belirle: tam doğrulama için `^...$` veya `\A...\z` (bazı motorlarda `$` sondaki satır sonundan önce de eşleşir, belirt); çıkarma için kelime sınırları veya lookaround.
4. Tabloyu karşılayan en basit deseni yaz; `.` yerine açık karakter sınıflarını, uzunluklar biliniyorsa `*`/`+` yerine sınırlı niceleyicileri tercih et.
5. İsimli veya yakalamayan grupları bilinçli kullan; yalnızca çağıranın ihtiyaç duyduğunu yakala.
6. Felaket düzeyinde geri izlemeyi kontrol et: iç içe niceleyiciler, çakışan alternatifler, `(.*)*` benzeri şekiller; motor destekliyorsa atomik gruplar, possessive niceleyiciler veya belirsizliği olmayan sınıflarla yeniden yaz ya da girdi uzunluğunun sınırlanması gerektiğini belirt.
7. Bayrakları bilinçli uygula: büyük/küçük harf duyarsız, multiline, dotall, Unicode; hangilerinin gerektiğini söyle.
8. Test tablosunu desene karşı durum durum zihninde çalıştır ve her satır geçene kadar düzelt; emin olmadığın durumları `[DOĞRULA]` olarak bildir.
9. Deseni hedef dile göre doğru kaçışlanmış bir string literal olarak ve motor destekliyorsa yorumlu (verbose) sürümüyle ver.
10. Mevcut bir regex'i açıklarken veya düzeltirken: token'lara ayır, gerçekte neyi eşlediğini söyle, her hata için bir karşı örnek göster, sonra düzeltilmiş sürümü aynı test tablosuyla ver.
11. Hedef devam ediyorsa test tablosunu otomatik testlere dönüştürmek için `unit-test-writing` veya desen güvenilmeyen girdiyi koruyorsa `secure-code-review` öner.

## Çıktı formatı
````markdown
# Regex: <amaç>
Motor: <motor> · Mod: <tüm metni doğrula / çıkar> · Bayraklar: <...>

```<dil>
<doğru kaçışlanmış literal olarak desen>
```

## Parça Parça
| Parça | Anlamı |

## Test Durumları
| Girdi | Beklenen | Sonuç |

## Performans ve Güvenlik
- Geri izleme riski: <yok / ... ile azaltıldı>

## Notlar ve Sınırlar
- ...
````

## Kalite kontrol listesi
- [ ] Desen belirtilen motor için yazıldı ve hedef dile göre kaçışlandı.
- [ ] Test tablosunda sınırlar dahil hem eşleşmeli hem eşleşmemeli satırlar var.
- [ ] Çapa, moda (doğrulama veya çıkarma) uygun.
- [ ] Belirtilmiş bir önlem olmadan iç içe veya belirsiz niceleyici kalmadı.
- [ ] Kesin doğrulanmayan durumlar `[DOĞRULA]`, çıkarılan girdi formatları `[VARSAYIM]` olarak işaretli.
- [ ] Standart formatlar için ayrıştırıcı veya kütüphane alternatifi değerlendirildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çapaları unutmak; böylece "doğrulama" deseni `abcINV-2024-000123xyz` değerini kabul eder.
- Satır boyunca açgözlü `.*` kullanıp amaçlanandan çok daha fazlasını yakalamak.
- Desteklemeyen bir motor için lookbehind veya possessive niceleyici yazmak.
- E-posta veya HTML'i düzgün bir ayrıştırıcı ve pragmatik bir kontrol yerine tamamen regex'le doğrulamaya çalışmak.

## Örnek
Girdi: "E-posta konularından INV-2024-000123 gibi fatura numaralarını çıkar, JavaScript."

Zayıf: `/INV.*\d+/` (`INVALID code 42` ile eşleşir ve konunun geri kalanını yutar).

Güçlü, bir bölüm:
```javascript
/\bINV-(\d{4})-(\d{6})\b/g
```
| Girdi | Beklenen | Sonuç |
|---|---|---|
| `Re: INV-2024-000123 vadesi geçti` | `INV-2024-000123` eşleşir | geçti |
| `XINV-2024-000123` | eşleşme yok | geçti |
| `INV-24-000123` | eşleşme yok | geçti |
