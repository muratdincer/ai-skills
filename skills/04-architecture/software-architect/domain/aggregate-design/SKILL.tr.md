---
name: aggregate-design
description: "DDD aggregate'lerini tek işlemde (transaction) korunması gereken değişmezlerden yola çıkarak kök, sınır ve üyeleriyle tasarlar; komutları, yayınlanan olayları, kimliği, aggregate'ler arası referansları ve nihai tutarlılık kurallarını tanımlar, boyut ve çekişmeyi kontrol eder. Bir alan modeli tutarlılık sınırlarına dönüştürülecekse, aggregate'ler çok büyükse veya kilit çekişmesine yol açıyorsa ya da neyin anında, neyin nihai olarak tutarlı olacağına karar verilecekse kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: software-architect
  area: domain
  title: "Aggregate tasarımı"
  related: "event-storming, bounded-context-map, event-driven-design, database-schema-design, business-rules-catalog"
  prompt: "Sipariş bağlamımız için aggregate'leri tasarla; kurallar müşteri başına kredi limiti, sipariş başına en fazla 50 satır ve sevkiyattan sonra değişiklik yapılamaması."
---

# Aggregate Tasarımı

## Amaç
Gerçek iş değişmezlerini tek bir işlemde koruyan, ama çekişmeyi önleyecek kadar küçük kalan tutarlılık sınırları tanımlamak. Böylece model eşzamanlılık altında doğru kalır ve kolay evrilir.

## Ne zaman kullanılır
- `event-storming` bir bağlam için aday aggregate, komut ve olayları ortaya çıkardıktan sonra.
- Mevcut bir aggregate büyükse, yavaş yükleniyorsa veya iyimser kilit (optimistic lock) çakışmaları yaşıyorsa.
- Ekip bir kuralın işlem içinde mi uygulanması gerektiğini yoksa nihai tutarlılıkla mı yetinileceğini tartışıyorsa.

## Ne zaman kullanılmaz
- Bağlam sınırları belirsizse önce `bounded-context-map` kullanılır.
- Asıl konu alan modeli değil fiziksel tablo yapısıysa `database-schema-design` kullanılır.
- Alan anlamlı değişmezleri olmayan basit bir CRUD ise transaction script veya active record yeterlidir; aggregate tasarımına gerek yoktur.

## Girdiler
Zorunlu:
- Sınırlı bağlam ve iş kuralları (veya komut ve olayları içeren event storming çıktısı).

İsteğe bağlı:
- Beklenen eşzamanlılık (kim neyi, ne sıklıkla değiştiriyor), varlık başına veri hacimleri.
- Mevcut model veya kod, kalıcılık teknolojisi, tüketilen/yayınlanan entegrasyon olayları.

İş kuralları verilmemişse asla ihlal edilmemesi gereken kuralları sor. Değişmez uydurma.

## Süreç
1. Aday değişmezleri test edilebilir ifadeler olarak listele ("sipariş toplamı müşterinin kullanılabilir kredisini asla aşmaz"). Her birini kullanıcının söylediği ya da `[VARSAYIM]` olarak etiketle.
2. Her değişmez için her işlem sonunda mutlaka geçerli mi olmalı (gerçek değişmez) yoksa kısa süre sonra onarılabilir mi (nihai kural) karar ver. İşe, kural saniyeler veya dakikalar boyunca ihlal edilirse ne olacağını sor.
3. Yalnızca gerçek değişmezleri uygulamak için gereken veriyi tek aggregate'te topla; tüm değişikliklerin geçtiği kökü seç. Geri kalan her şey ayrı aggregate olur.
4. Diğer aggregate'lere nesne referansıyla değil yalnızca kimlikle başvur; hangi kimlik türlerinin tutulduğunu kaydet.
5. Kök üzerinde niyeti açıkça gösteren adlarla komutları, ön koşulları, her komutun kontrol ettiği değişmezleri ve yayınladığı alan olaylarını tanımla.
6. Birden fazla aggregate'e yayılan kurallar için nihai tutarlılık mekanizmasını tasarla: alan olayı ve politika/işleyici, süreç yöneticisi (process manager) veya saga; hata durumunda telafi adımıyla.
7. Boyut ve çekişmeyi kontrol et: örnek başına üye sayısını (ör. sipariş başına satır) ve örnek başına eşzamanlı yazan sayısını tahmin et. Büyük veya sıcaksa böl ya da kuralı aggregate dışına taşı.
8. Kimliği (doğal ya da üretilen), iyimser eşzamanlılık için sürümlemeyi ve izin verilen geçişleriyle yaşam döngüsü durumlarını tanımla.
9. Kalıcılık etkilerini (işlem başına bir aggregate, yükleme stratejisi) tasarımı belirli bir ORM'e bağlamadan not et.
10. Ödünleşimleri ve açık soruları, özellikle katılığı iş tarafından teyit edilmemiş değişmezleri listele.
11. Hedef devam ediyorsa aggregate'ler arası olaylar için `event-driven-design`, kalıcılık için `database-schema-design` veya kuralları kaydetmek için `business-rules-catalog` öner.

## Çıktı formatı
```markdown
# Aggregate Tasarımı: <bağlam>

## Değişmezler
| # | Kural | Kaynak | Katılık (işlemsel / nihai) | Uygulandığı yer |
|---|---|---|---|---|

## Aggregate'ler
### <Aggregate kökü>
- Üyeler: <varlıklar, değer nesneleri>
- Kimlik: <tür, üretim> · Eşzamanlılık: <sürüm alanı>
- Referanslar (kimlikle): <diğer aggregate'ler>
- Yaşam döngüsü: <durum> → <durum> ...
| Komut | Ön koşullar | Kontrol edilen değişmezler | Yayınlanan olaylar |
|---|---|---|---|

## Aggregate'ler Arası Kurallar
- <kural> — mekanizma: <olay + politika | saga> — telafi: <eylem>

## Boyut ve Çekişme Kontrolü
- <aggregate>: örnek başına ~<üye>, ~<yazan> eşzamanlı — Uygun / şu nedenle bölünmeli ...

## Ödünleşimler, Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her aggregate adı konmuş en az bir değişmezi koruyor; hiçbiri yalnızca gezinme için yok.
- [ ] Diğer aggregate'lere yalnızca kimlikle başvuruluyor.
- [ ] Bir komut işlem başına tek bir aggregate'i değiştiriyor; çok aggregate'li kurallar adı konmuş bir nihai mekanizma kullanıyor.
- [ ] Boyut ve eşzamanlı yazan tahminleri belirtilmiş veya `[BİLİNMİYOR]` olarak işaretli.
- [ ] Her değişmezin katılığı iş tarafından teyit edilmiş ya da `[VARSAYIM]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Aggregate'leri varlık-ilişki diyagramına göre modellemek ("Müşteri, Siparişlere; Sipariş, Satırlara sahip"). Sınırlar kapsamaya değil değişmezlere göre çizilir.
- Tüm örneklere yayılan bir kuralı kontrol etmek için bütün koleksiyonu köke çekmek (ör. benzersiz kullanıcı adı). Özel bir kontrol, rezervasyon aggregate'i veya veritabanı kısıtı kullan.
- Her kuralı işlemsel saymak. Birçok "kural" saniyelerce tutarsızlığı tolere eder ve politika olarak daha ucuzdur.

## Örnek
Girdi: "Kurallar: müşteri kredi limiti, sipariş başına en fazla 50 satır, sevkiyattan sonra değişiklik yok."

Çıktıdan bir bölüm:
- Order (kök): satırlar varlık olarak; "≤ 50 satır" ve "Sevk Edildikten sonra değişiklik yok" değişmezleri Order içinde işlemsel.
- Kredi limiti birçok siparişe yayılır: CustomerCredit aggregate'i "Sipariş Verildi" olayında krediyi ayırır; ayırma başarısız olursa sipariş politika ile reddedilir `[VARSAYIM: kısa gecikme kabul edilebilir, finansla teyit et]`.
- Order, Customer'a yalnızca CustomerId ile başvurur.
