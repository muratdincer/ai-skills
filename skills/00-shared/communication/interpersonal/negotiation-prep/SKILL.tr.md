---
name: negotiation-prep
description: "Bir müzakereye hazırlık için hedefinizi, çıkarlarınızı, BATNA'nızı, masadan kalkma noktanızı, karşı tarafın olası çıkarlarını ve BATNA'sını, olası anlaşma alanını, takas edilebilir tavizleri ve gerekçesiyle açılış pozisyonunu belirler. Birinin müşteri, tedarikçi, sponsor veya başka bir ekiple kapsam, teslim tarihi, bütçe, kaynak, tedarikçi sözleşmesi, ücret veya koşullar üzerine müzakere etmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: communication
  area: interpersonal
  title: "Müzakereye hazırlanma"
  related: "conflict-resolution, stakeholder-map, trade-off-analysis, vendor-evaluation, pricing-analysis"
  prompt: "Mevcut ekiple ancak %60'ını teslim edebilecekken kapsamın tamamını mart ayına kadar isteyen iş sponsoruyla müzakereye hazırlanmama yardım et."
---

# Müzakereye Hazırlanma

## Amaç
Müzakereye neye ihtiyacınız olduğunu, neyi verebileceğinizi, nerede masadan kalkacağınızı ve karşı tarafın muhtemelen neye ihtiyaç duyduğunu bilerek girmek; böylece sonucu odadaki baskı değil hazırlık ve nesnel kriterler belirler.

## Ne zaman kullanılır
- Bir sponsor veya müşteriyle kapsam, teslim tarihi, bütçe veya kadro müzakere edilecekse.
- Bir tedarikçi sözleşmesi, ücretler, SLA veya ödeme koşulları müzakere edilecekse.
- Aynı kapasite için yarışan başka bir ekiple kaynak veya öncelik üzerinde anlaşılacaksa.

## Ne zaman kullanılmaz
- Başkalarının anlaşmazlığını çözmelerine yardım eden tarafsız bir tarafsanız. `conflict-resolution` kullanın.
- Soru taraflar arası koşullar değil, hangi teknik veya teslimat seçeneğinin en iyi olduğuysa. `trade-off-analysis` kullanın.
- Seçim yapmadan önce tedarikçiler karşılaştırılıyorsa. `vendor-evaluation` kullanın.

## Girdiler
Zorunlu:
- Neyin, kiminle müzakere edildiği ve kullanıcının hedefi.

İsteğe bağlı:
- Mevcut teklif veya talep, kısıtlar (bütçe tavanı, hukuki, sözleşme), ilişki geçmişi, son tarih, piyasa veya kurum içi karşılaştırma verileri, her iki tarafın yetki sınırları.

Hedef veya karşı taraf bilinmiyorsa önce sorun. Asla fiyat, ücret, tarih veya karşı tarafın sınırlarını uydurmayın; tahminleri `[VARSAYIM]`, bilinmeyenleri `[BİLİNMİYOR]` olarak işaretleyin. Sözleşme ve ticari veriler gizli olabilir; gerekenle sınırlı tutun.

## Süreç
1. Masadaki konuları (kapsam, tarih, fiyat, kalite, risk paylaşımı, ödeme, destek) ve her biri için hedefinizi tanımlayın; sizin için önem sırasına koyun.
2. Her hedefin arkasındaki çıkarlarınızı (neden önemli olduğunu) pozisyonlarınızdan ayrı yazın.
3. BATNA'nızı tanımlayın: anlaşma olmazsa gerçekte ne yapacağınız ve bunun ne kadar iyi olduğu. Mümkünse toplantıdan önce güçlendirin.
4. Her ana konu için BATNA'dan türetilmiş masadan kalkma noktanızı (rezervasyon değeri) ve hedefinizi (iddialı ama gerekçelendirilebilir) belirleyin.
5. Karşı tarafı modelleyin: çıkarları, kısıtları, karar yetkisi, olası BATNA'sı ve üzerindeki baskılar (son tarihler, iç politika). Tümünü `[VARSAYIM]` olarak işaretleyin ve sınamak için sorular listeleyin.
6. Olası anlaşma alanını tahmin edin; görünmüyorsa BATNA'nızı iyileştirmeyi, yeni konular eklemeyi veya müzakere etmemeyi planlayın.
7. Taviz planı yapın: sizin için ucuz, onlar için değerli takas edilebilir kalemler ve her birine karşılık ne isteyeceğiniz (karşılığını almadan asla taviz vermeyin).
8. Pozisyonları gerekçelendirecek nesnel kriterleri ve kanıtları hazırlayın (hız verisi, piyasa ücretleri, efor tahminleri, emsaller).
9. Açılışı taslaklayın: pozisyon, gerekçe ve ilk çıpayı sizin mi atacağınız (iyi bilginiz varsa önce siz çıpa atın; yoksa onların açmasına izin verin ve sorgulayın).
10. Çıkarları ortaya çıkaracak soruları, beklenen baskı taktiklerine (son tarih baskısı, "son teklif", ufak ek talepler) cevapları ve iki tarafta son onayı kimin verdiğini hazırlayın.
11. Kapanışı planlayın: anlaşmaların yazılı olarak nasıl özetleneceği, açık maddeler ve sonraki adımlar.
12. Kullanıcının hedefi devam ediyorsa karşı tarafın arkasındaki etkileyicileri analiz etmek için `stakeholder-map`, paket seçeneklerini değerlendirmek için `trade-off-analysis`, ilişki zaten bozulduysa `conflict-resolution` öner.

## Çıktı formatı
```markdown
# Müzakere Hazırlığı: <karşı taraf> ile <konu>
Hedef: ... | Tarih: ... | Yetki: bizim <...> / onların <...>

| Konu | Öncelik | Hedefimiz | Masadan kalkma noktamız | Olası pozisyonları [VARSAYIM] |
|---|---|---|---|---|

Çıkarlarımız: ...
BATNA'mız: ... (gücü: güçlü/orta/zayıf) | Nasıl iyileştirilir: ...
Onların çıkarları ve BATNA'sı [VARSAYIM]: ...
Olası anlaşma alanı: ...

## Taviz planı
| Verebileceğimiz | Bize maliyeti | Onlara değeri | Karşılığında istediğimiz |

## Açılış pozisyonu ve gerekçesi
...
## Sorulacak sorular
1. ...
## Baskı taktikleri ve cevaplar
- "<taktik>" -> <cevap>
## Kapanış
Yazılı özet sorumlusu: ... | Açık maddeler: ... | Sonraki adım: ...
```

## Kalite kontrol listesi
- [ ] Her ana konunun, belirtilmiş bir BATNA'dan türetilmiş hedefi ve masadan kalkma noktası var.
- [ ] İki taraf için de çıkarlar pozisyonlardan ayrılmış; karşı taraf analizi `[VARSAYIM]` olarak işaretli.
- [ ] Her tavize karşılık bir şey isteniyor.
- [ ] Pozisyonlar nesnel kriter veya kanıtla destekleniyor; uydurma rakam yok.
- [ ] İki taraftaki karar yetkisi biliniyor ya da açık soru olarak listelenmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tek bir konu üzerinden müzakere etmek (yalnızca fiyat veya tarih). Takas yapılabilsin diye konu ekleyin.
- Gerçek bir BATNA olmadığı için her anlaşmanın kabul edilebilir görünmesi. Önce anlaşmasız alternatifi çıkarın.
- Sözlü anlaşıp geçmek. Anlaşmayı aynı gün yazılı olarak özetleyin.

## Örnek
Girdi: Sponsor kapsamın tamamını mart ayına kadar istiyor; ekip yaklaşık %60'ını teslim edebilir.

Zayıf: "Sponsora bunun imkânsız olduğunu söyle ve ek süre iste."

Güçlü (alıntı):
- Konular: kapsam, tarih, ekip büyüklüğü, kalite çıtası.
- BATNA'mız: çekirdek %60'ı marta kadar teslim etmek ve kalan kapsamı yönlendirme kuruluna eskale etmek `[VARSAYIM: eskalasyon mümkün]`.
- Onların çıkarı `[VARSAYIM]`: kapsamdaki her kalem değil, mart ayındaki yasal raporlama özelliği.
- Taviz: `[TBD]` düşük değerli kalemi 2. çeyreğe kaydırır ve bir ek geliştiriciyi onaylarlarsa yasal raporlama özelliğini marta kadar taahhüt ederiz.
- Kanıt: son dört iterasyonun iş çıkarma hızı `[TBD: rakamlar]` marta projekte edilmiş hâli.
