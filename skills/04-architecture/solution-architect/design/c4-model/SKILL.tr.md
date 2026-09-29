---
description: Bir yazılım sistemini C4 modeliyle - sistem bağlamı, konteyner ve faydalı olduğu yerde bileşen diyagramları - tutarlı öğe adları, sorumluluklar, teknolojiler ve etiketli ilişkilerle kod olarak diyagram (Structurizr DSL, PlantUML C4 veya Mermaid) biçiminde tanımlar. Bir tasarım, inceleme, oryantasyon veya dokümantasyon için mimari diyagram gerektiğinde ya da metinsel bir tanım veya mevcut bir taslak C4 görünümlerine dönüştürülmek istendiğinde kullanılır.
related: solution-architecture-document, diagram-as-code, bounded-context-map, adr, architecture-review
prompt: E-ticaret ödeme akışımız için Structurizr DSL ile C4 bağlam ve konteyner diyagramları oluştur: web mağaza, mobil uygulama, checkout API, ödeme sağlayıcı, sipariş veritabanı ve mesaj kuyruğu.
---

# C4 ile Mimari Tanımlama

## Amaç
Mimarinin sürümlenebilmesi, incelenebilmesi ve yeniden üretilebilmesi için net ve tutarlı C4 görünümlerini kod olarak üretmek; her hedef kitlenin doğru ayrıntı düzeyini görmesini sağlamak.

## Ne zaman kullanılır
- Bir tasarım, inceleme veya ADR bağlam ve konteyner diyagramlarına ihtiyaç duyduğunda.
- Mevcut bir beyaz tahta taslağı veya düz yazı tanım sürdürülebilir diyagramlara dönüşmeli olduğunda.
- Oryantasyon için bir sistemin ve komşularının haritası gerektiğinde.
- Farklı dokümanlardaki diyagramlar birbirini tutmuyor ve tek bir modele ihtiyaç duyulduğunda.

## Ne zaman kullanılmaz
- Yalnızca tek bir etkileşimin sıralı akışı gerekiyorsa `sequence-flow` kullanılır.
- Mimari dışı diyagramlar (organizasyon şeması, genel akış şeması) için `diagram-as-code` kullanılır.
- Alan sınırları ve ekip ilişkileri için `bounded-context-map` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki sistem ile parçalarının, kullanıcılarının ve dış sistemlerinin tanımı.

İsteğe bağlı:
- Tercih edilen gösterim (Structurizr DSL, C4-PlantUML ile PlantUML, Mermaid C4); varsayılan Structurizr DSL.
- Teknolojiler, protokoller, dağıtım hedefleri.
- Mevcut diyagramlar veya adlandırma kuralları.

Kapsamdaki sistem belirsizse hangi sistemin tanımlandığını sor. Bilinmeyen teknolojiler `[TBD]` olarak etiketlenir.

## Süreç
1. Kapsamı sabitle: kapsamda tek bir yazılım sistemi var; geri kalan her şey kişi veya dış sistemdir.
2. Önce modeli, sonra görünümleri kur. Öğeleri listele: kişiler (isimler değil roller), yazılım sistemleri, konteynerler (ayrı dağıtılabilen/çalışan birimler ve veri depoları) ve yalnızca bir karara yardımcı olduğu yerde bileşenler.
3. Her öğe için ad, tek satırlık sorumluluk, teknoloji (konteyner ve bileşenlerde) ve biliniyorsa sahibi kaydet.
4. Her ilişki için bir fiil öbeği ve konteynerlerde protokol/format yaz (ör. "Sipariş verir [HTTPS/JSON]", "OrderPlaced yayınlar [AMQP]"). Yön, bağımlılığı veya verinin başlatıcısını izler.
5. Sistem Bağlamı görünümünü oluştur: kapsamdaki sistem, kullanıcılar, dış sistemler; teknoloji ayrıntısı yok.
6. Konteyner görünümünü oluştur: kapsamdaki sistemin konteynerleri ve doğrudan bağlı kişiler ile dış sistemler. Veri depolarını ve mesaj kuyruklarını tutarlı biçimde konteyner veya dış sistem olarak göster.
7. Bileşen görünümlerini yalnızca iç yapısı mimari açıdan önemli konteynerler için oluştur; 5-15 bileşenle sınırla.
8. İsteğe bağlı olarak konteynerleri ortam ve düğümlere eşleyen bir Dağıtım görünümü ekle.
9. Doğrula: her ilişkinin etiketi var; hiçbir öğe iki farklı adla geçmiyor; her görünüm ~20 öğeye sığıyor; bir açıklama (legend) mevcut.
10. Diyagram kodunu ve kısa bir öğe kataloğu tablosunu ver; `[TBD]` öğeleri açık soru olarak listele.

## Çıktı formatı
````markdown
# C4 Modeli – <sistem>
## Öğe Kataloğu
| Öğe | Tür | Sorumluluk | Teknoloji | Sahip |
|---|---|---|---|---|

## Diyagram Kodu (<gösterim>)
```
workspace { model { ... } views { systemContext ... container ... } }
```

## Notlar
- Varsayımlar ve `[TBD]` öğeler
- Açık sorular
````

## Kalite kontrol listesi
- [ ] Seviyeler karışmıyor: konteyner görünümünde bileşen, bağlam görünümünde teknoloji yok.
- [ ] Her ilişki yönlü, amacıyla ve (konteynerlerde) protokolle etiketli.
- [ ] Öğe adları ve sorumlulukları görünümlerde ve katalogda aynı.
- [ ] Veri depoları ve mesaj kuyrukları açıkça gösterildi.
- [ ] Kod seçilen gösterim için sözdizimsel olarak geçerli.

## Sık yapılan hatalar
- Sorumluluk olarak "API" veya "Servis" yazmak. Öğenin iş için ne yaptığını belirt.
- Kütüphaneleri veya modülleri konteyner olarak çizmek. Konteynerler ayrı çalışır veya ayrı veri saklar.
- Her yerde çift yönlü ok. Başlatan yönü seç; ikinci ilişkiyi yalnızca iki taraf da başlatıyorsa ekle.

## Örnek
Girdi: "Checkout: web mağaza ve mobil uygulama checkout API'yi çağırır; API siparişleri PostgreSQL'de saklar, ödeme sağlayıcıyı çağırır, olayları kuyruğa yayınlar."

Çıktıdan bir bölüm:
```
customer = person "Müşteri" "Çevrimiçi ürün satın alır"
shop = softwareSystem "Çevrimiçi Mağaza" {
  web = container "Web Mağaza" "Gezinme ve ödeme arayüzü" "React"
  api = container "Checkout API" "Sepeti doğrular, sipariş oluşturur, ödemeyi başlatır" "[TBD dil]"
  db = container "Sipariş Veritabanı" "Siparişleri ve ödeme durumunu saklar" "PostgreSQL"
}
psp = softwareSystem "Ödeme Sağlayıcı" "Kart ödemelerini onaylar" "External"
customer -> web "Sipariş verir" "HTTPS"
web -> api "Ödeme isteklerini gönderir" "HTTPS/JSON"
api -> psp "Ödeme onayı ister" "HTTPS/JSON"
```
