---
name: persona
description: "Bağlam, hedefler, sorunlar, davranışlar, karar kriterleri ve alıntılarla kanıta dayalı bir persona oluşturur; her niteliği araştırmaya bağlar ve proto-persona varsayımlarını işaretler. Araştırma verisinin (görüşmeler, anketler, analitik, destek kayıtları) ortak bir kullanıcı modeline dönüştürülmesi gerektiğinde ya da tasarım ve ürün kararları için persona veya kullanıcı profili istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: discovery
  title: "Persona oluşturma"
  related: "jobs-to-be-done, customer-journey-map, research-synthesis, feedback-synthesis, problem-interview-script"
  prompt: "Bu 8 görüşme özetinden depo vardiya amirleri için bir persona oluştur."
---

# Persona Oluşturma

## Amaç
Bir kullanıcı grubu hakkındaki araştırmayı, ekiplerin tasarım ve önceliklendirme kararlarında kullanabileceği bir personaya dönüştürmek. Her nitelik kanıta bağlanır; böylece persona kurguya dönüşmez.

## Ne zaman kullanılır
- Görüşme, anket veya saha çalışmalarından sonra kullanıcıların kim olduğunu paylaşmak için.
- Ekipler "kullanıcı" hakkında kişisel görüşlerle tartışıyor ve ortak bir referansa ihtiyaç duyuyorsa.
- Araştırmayı planlamak için varsayıma dayalı bir proto-persona gerektiğinde (açıkça öyle etiketlenerek).

## Ne zaman kullanılmaz
- Kullanıcı tipinden bağımsız iş ve sonuçlar gerekiyorsa `jobs-to-be-done` kullanılır.
- Zaman içindeki adım adım deneyim gerekiyorsa `customer-journey-map` kullanılır.
- Ham araştırmanın önce temalara ayrılması gerekiyorsa `research-synthesis` kullanılır.

## Girdiler
Zorunlu:
- Araştırma malzemesi (notlar, dökümler, anket sonuçları) veya proto-persona için ekibin açık varsayımları.

İsteğe bağlı, kaliteyi artırır:
- Davranış ve segmentlere dair analitik, destek verisi, satış notları.
- Personanın yön vermesi beklenen ürün kararları.

Malzeme verilmediyse proto-persona oluşturulup oluşturulmayacağını sor; öyleyse `[PROTO-PERSONA – VARSAYIMLAR]` olarak etiketle. Alıntılardaki kişisel verileri maskele veya çıkar.

## Süreç
1. Segment sınırını tanımla: bu grubu hangi davranışlar veya bağlam ayırıyor (davranışı değiştirmiyorsa yaş veya cinsiyet değil).
2. Her kaynaktan nitelikleri çıkar: bağlam/ortam, hedefler, sorunlar, mevcut davranışlar ve geçici çözümler, araçlar, karar kriterleri, kısıtlar.
3. Nitelikleri kümele; birden fazla katılımcıda görülenleri tut. Sıklığı not et (ör. 6/8).
4. Tek personanın içinde birden fazla persona saklanıp saklanmadığını kontrol et: hedefler veya davranışlar ayrı kalıplara bölünüyorsa ayrı personalar oluştur.
5. Personayı yaz: rolle bağlantılı betimleyici bir ad, kısa bağlam, en önemli 3 hedef, en önemli 3 sorun, ana davranışlar, çözüm aramasını tetikleyenler, benimsemesini veya reddetmesini belirleyenler.
6. Zihniyeti yansıtan 2-3 gerçek, anonimleştirilmiş alıntı ekle.
7. Tasarım çıkarımlarını yaz: 3-5 adet "bu nedenle şunu yapmalı / yapmamalıyız" ifadesi.
8. Bir kanıt tablosu ve güven düzeyi ekle; bir sonraki araştırma turu için boşlukları listele.
9. Girdide yazmayan, senin çıkardığın her noktayı `[VARSAYIM]` olarak işaretle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: personanın hedeflerini derinleştirmek için `jobs-to-be-done` veya `customer-journey-map`, kanıt boşluklarını kapatmak için `problem-interview-script`.

## Çıktı formatı
```markdown
# Persona: <betimleyici ad> (<rol/segment>)
Güven: Y/O/D · Dayanak: <kaynaklar, n>

## Bağlam
...
## Hedefler
1. ...
## Sorunlar
1. ...
## Davranışlar ve Geçici Çözümler
- ...
## Tetikleyiciler ve Karar Kriterleri
- ...
## Alıntılar (anonim)
> "..."
## Tasarım Çıkarımları
- Bu nedenle şunu yapmalıyız ...
## Kanıt
| Nitelik | Kanıt | Sıklık |
|---|---|---|
## Boşluklar
- ...
```

## Kalite kontrol listesi
- [ ] Her nitelik bir kaynağa dayanıyor ya da `[VARSAYIM]` olarak işaretli.
- [ ] Demografik ayrıntılar yalnızca davranışı değiştiriyorsa yer alıyor.
- [ ] Alıntılar gerçek ve anonim; kişisel veri yok.
- [ ] Tasarım çıkarımları somut ve uygulanabilir.
- [ ] Güven düzeyi ve örneklem büyüklüğü belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Stok fotoğraf, hobiler ve hayat hikâyesi uydurmak. Süs niteliğindeki kurgu güveni azaltır; davranışla ilgili olgulara bağlı kal.
- Farklı grupların ortalamasını tek personada toplamak. Hedefler ayrışıyorsa böl.
- Personayı kalıcı saymak. Tarih at ve büyük araştırmalardan sonra yeniden gözden geçir.

## Örnek
Girdi: "Depo vardiya amirleriyle yapılmış 8 görüşme özeti."

Çıktıdan bir bölüm:
- Ad: "Yangın Söndüren Vardiya Amiri" — Güven: Orta, n=8.
- Sorun: Geciken gelen tırlardan ancak rampa boş kaldığında haberdar oluyor (6/8).
- Geçici çözüm: Şoförlerle kişisel WhatsApp grubu (5/8).
- Çıkarım: Gelen sevkiyat gecikme uyarılarını vardiya başlamadan önce mobilde göster.
