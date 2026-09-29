---
description: "Hedef, birincil ve destekleyici aktörler, paydaş çıkarları, tetikleyici, ön koşullar, asgari ve başarı garantileri, numaralı ana başarı senaryosu ve ayrıldıkları adıma bağlı alternatif ve istisna akışlarıyla bir kullanım senaryosu (use case) tanımı yazar. Bir etkileşimin çok dalı, birden fazla aktörü veya sistemden sisteme adımları olduğunda ya da 'use case', 'UC tanımı' veya 'ayrıntılı kullanım senaryosu' istendiğinde kullanılır."
related: "frd-writing, user-story, business-rules-catalog, error-scenario-catalog, sequence-flow"
prompt: "Kartla iadeler ve fişi olmayan durumlarla birlikte 'Satın alınan ürünü mağazada iade etme' kullanım senaryosunu yaz."
---

# Kullanım Senaryosu (Use Case) Yazma

## Amaç
Bir aktör hedefini, dallanabileceği ve başarısız olabileceği her yol dahil, sistemle adım adım eksiksiz bir etkileşim olarak tarif etmek; böylece tasarımcı, geliştirici ve test uzmanı aynı kesin davranış modelini paylaşır.

## Ne zaman kullanılır
- Bir etkileşimin, yalnızca hikayelerle dağınık kalacak çok sayıda alternatif veya istisna yolu olduğunda.
- Tek bir hedef içinde birden fazla aktör veya dış sistem sırayla rol aldığında.
- Sözleşme, tedarikçi veya regülasyona tabi bir bağlam resmi bir davranış tanımı gerektirdiğinde.

## Ne zaman kullanılmaz
- Davranış basitse ve ekip backlog maddeleriyle çalışıyorsa `user-story` ile `acceptance-criteria` kullanılır.
- Birçok fonksiyona yayılan bir sistemin tüm davranışı gerekiyorsa `frd-writing` kullanılır.
- Yalnızca sistemler arası mesaj sırası önemliyse `sequence-flow` kullanılır.

## Girdiler
Zorunlu:
- Aktör hedefi (kullanım senaryosunun adı) ve bugün nasıl gerçekleştiğine veya nasıl gerçekleşmesi gerektiğine dair bir tarif.

İsteğe bağlı, kaliteyi artırır:
- İş kuralları, süreç modelleri, ekran taslakları, entegrasyon tarifleri, bilinen hata durumları, kurumun use case şablonu.

Hedef veya temel akış yoksa iste. Bir seferde en fazla 5 engelleyici soru sor; kalanları açık soru olarak tut.

## Süreç
1. Kullanım senaryosunu birincil aktörün hedefi olarak adlandır: fiil + nesne ("Satın alınan ürünü iade etme"). Seviyeyi (kullanıcı hedefi veya alt fonksiyon) ve kapsamı (hangi sistemin kara kutu olduğu) belirle.
2. Birincil aktörü, destekleyici aktörleri (kişi ve sistemler) ve sonuçla ilgili çıkarlarıyla paydaşları listele.
3. Tetikleyiciyi, ön koşulları (başlamadan önce sistemin garanti ettikleri) ve garantileri tanımla: asgari garanti (başarısızlıkta da doğru olan, ör. denetim kaydı) ve başarı garantisi.
4. Ana başarı senaryosunu 5-12 numaralı adım olarak, her biri "aktör yapar / sistem yapar" şeklinde, aktörün dilinde ve UI ayrıntısı olmadan yaz.
5. Her adım için "burada başka ne olabilir?" diye sor ve alternatif akışları (geçerli varyasyonlar) koşulu, adımları ve nerede ana akışa döndüğü veya bittiğiyle `3a`, `3b` şeklinde yaz.
6. Hatalar için istisna akışları yaz: geçersiz veri, kural ihlali, zaman aşımı veya erişilemeyen dış sistem, iptal, eşzamanlı değişiklik. Her birinin son durumunu belirt.
7. İş kurallarını gömmek yerine ID ile referans ver; bulunan yeni kuralları listele, çıkarım olanları `[VARSAYIM]` olarak işaretle.
8. Yalnızca bu senaryo için geçerli özel gereksinimleri (yanıt süresi, denetim, erişilebilirlik) ve dokunulan veriyi ekle.
9. Ana senaryonun başarı garantisini sağladığını ve her dalın tanımlı bir durumda bittiğini kontrol et.
10. Açık soruları muhataplarıyla listele.
11. Hedef devam ediyorsa ayrıntılı hata yönetimi için `error-scenario-catalog`, kurallar için `business-rules-catalog`, sistem etkileşimleri için `sequence-flow` öner.

## Çıktı formatı
```markdown
# UC-<nn> <Hedef adı>
| Alan | Değer |
|---|---|
| Seviye / Kapsam | <kullanıcı hedefi / alt fonksiyon> · <sistem> |
| Birincil aktör | ... |
| Destekleyici aktörler | ... |
| Paydaşlar ve çıkarları | ... |
| Tetikleyici | ... |
| Ön koşullar | ... |
| Asgari garanti | ... |
| Başarı garantisi | ... |

## Ana Başarı Senaryosu
1. ...
## Alternatif Akışlar
- 3a. <koşul>: 3a1 ... → 4. adımda ana akışa döner
## İstisna Akışları
- 5x. <hata>: ... → <durum> ile biter
## Referans Verilen İş Kuralları
## Özel Gereksinimler ve Veri
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Ad bir aktör hedefi ve ana senaryo bu hedefe 5-12 adımda ulaşıyor.
- [ ] Her adım kimin yaptığını söylüyor; UI yerleşimi veya teknik ayrıntı yok.
- [ ] Her alternatif ve istisna akışı adımını, koşulunu ve bitiş ya da dönüş noktasını belirtiyor.
- [ ] Dış sistem hataları ve zaman aşımları kapsandı.
- [ ] Asgari garanti her istisna yolunda sağlanıyor.
- [ ] Kurallar ID ile referanslı; çıkarılan kurallar `[VARSAYIM]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kullanım senaryosunu ekran gezintisi gibi yazmak ("Tamam'a tıklar"). Niyeti ve sistem yanıtını tarif et; kontrolleri tasarıma bırak.
- Dalları "eğer" ile ana senaryoya doldurmak. Ana senaryoyu doğrusal tut, her koşulu bir uzantıya taşı.
- Yanlış seviyede senaryolar ("Giriş yap"ı kullanıcı hedefi saymak). Bu tür adımları, hedef seviyesindeki senaryolardan referans verilen alt fonksiyonlar olarak ele al.

## Örnek
Girdi: "Müşteri ürünü mağazada iade eder; kartlı alışverişler karta iade edilir, fişi olmayanlar bir şekilde çözülür."

Çıktıdan bir bölüm:
Ana başarı senaryosu:
1. Müşteri ürünü ve fişi kasiyere sunar.
2. Kasiyer satışı fiş numarasıyla bulur.
3. Sistem satışı ve BR-12'ye göre iade edilebilir ürünleri gösterir.
4. Kasiyer ürünü ve iade nedenini seçer.
5. Sistem iade tutarını hesaplar ve ödeme sağlayıcısından karta iade ister.
6. Sistem iadeyi kaydeder ve iade fişini basar.

Alternatif akışlar:
- 1a. Fiş yok: kasiyer kullanılan kartla arama yapar `[VARSAYIM]`; satış bulunamazsa 1 numaralı açık soruya bakılır.
İstisna akışları:
- 5x. Ödeme sağlayıcısına erişilemiyor: sistem iadeyi "İade beklemede" olarak kaydeder ve yeniden dener `[TBD: yeniden deneme politikası]`; müşteri bekleme fişi alır.

Açık soru 1: Fişsiz iadeye izin veriliyor mu, hediye çeki olarak mı? — Perakende operasyon
