---
description: Olay güdümlü bir akışı uçtan uca tasarlar; olay türleri ve adlandırma, şemalar ve sürümleme, topic'ler ve bölümleme anahtarları, sıralama, teslim semantiği, idempotent tüketiciler, outbox ile yayınlama, yeniden deneme ve dead-letter kuyruklarıyla hata yönetimi ile telafili saga orkestrasyonu veya koreografisini kapsar. Servisler olaylar üzerinden asenkron entegre olacaksa, bir iş süreci birden fazla servise yayılıyorsa ya da mevcut bir olay akışında mükerrer işleme, kayıp mesaj veya sıralama hataları varsa kullanılır.
related: event-storming, aggregate-design, integration-pattern-selection, data-contract, schema-evolution-plan
prompt: Sipariş, ödeme, stok ve sevkiyat servisleri arasında sipariş verme olay akışını, ödeme başarısız olduğunda telafiyle birlikte tasarla.
---

# Olay Güdümlü Akış Tasarımı

## Amaç
Asenkron bir akışı, üreticiler ve tüketiciler birbirinden bağımsız geliştirilebilecek ve mükerrer mesaj, sıra bozulması, kısmi hata ve şema değişikliği altında yine doğru davranacak kadar net tanımlamak.

## Ne zaman kullanılır
- Bir iş süreci birden fazla servise yayılıyor ve dağıtık işleme (distributed transaction) dayanmamalıysa.
- Yeni bir entegrasyonun olay tabanlı olmasına karar verilmiş ve artık sözleşme ile semantik gerekiyorsa.
- Mevcut bir akışta mükerrer işleme, kayıp olay, sırası bozuk güncelleme veya takılı kalan saga'lar görülüyorsa.

## Ne zaman kullanılmaz
- Olay kullanılıp kullanılmayacağı hâlâ açıksa önce `integration-pattern-selection` kullanılır.
- İki ekip arasında yalnızca tek bir olay şeması sözleşmesi gerekiyorsa `data-contract` kullanılır.
- Alanın olayları ve komutları henüz bilinmiyorsa `event-storming` kullanılır.

## Girdiler
Zorunlu:
- İş akışı: tetikleyici, katılan servisler ve hata sonuçları dahil istenen son durum.

İsteğe bağlı:
- Kullanılan broker veya akış platformu, hacim ve gecikme hedefleri, saklama ihtiyaçları.
- Mevcut olay kataloğu, şema kayıt (schema registry) kuralları, olaylardaki veriye dair yasal kısıtlar.

Hata sonuçları belirtilmemişse her adım başarısız olduğunda ne olması gerektiğini sor. Bilinmeyen hedefleri `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Akışı adımlar dizisi olarak çiz ve koordinasyona karar ver: kısa ve kararlı akışlar için koreografi (servisler olaylara tepki verir); çok adım, dallanma veya telafi varsa orkestrasyon (saga orkestratörü komut gönderir). Seçimi gerekçelendir.
2. Her mesajı sınıflandır: alan olayı (olgu, geçmiş zaman, sahibi üretici), entegrasyon olayı (alan olaylarından türetilen yayımlanmış sözleşme) veya komut (tek bir işleyiciye istek). İç alan olaylarını kazara herkese açık sözleşme olarak yayınlama.
3. Her olay için yük (payload) biçimini seç: olay bildirimi (yalnızca kimlikler, tüketici geri çağırır), olayla durum aktarımı (event-carried state transfer; işlem için yeterli veri) veya tam anlık görüntü. Yükteki kişisel veriyi en aza indir, maskeleme veya şifreleme gereken alanları işaretle.
4. Zarfı (envelope) tanımla: olay kimliği, tür, sürüm, kaynak, oluşma zamanı, korelasyon ve nedensellik (causation) kimlikleri, bölümleme anahtarı; kurum kullanıyorsa CloudEvents ile hizala.
5. Topic veya kanalları eşle ve önemli olan sıralamayı koruyacak bölümleme anahtarlarını seç (genellikle aggregate kimliği). Küresel sıralamanın garanti edilmediği yerleri açıkça yaz.
6. Yayınlamayı garanti altına al: üreticinin deposundan transactional outbox veya change data capture (CDC); böylece durum değişikliği ile olay birbirinden ayrışamaz.
7. En az bir kez (at-least-once) teslimatı varsay: her tüketiciyi idempotent yap (işlenmiş kimlik deposu, doğal idempotency veya sürüm kontrolü) ve eski ya da sırası bozuk olayların nasıl tespit edilip yok sayılacağını tanımla.
8. Hata yönetimini tasarla: geri çekilmeli (backoff) ve sınırlı yeniden deneme politikası, zehirli mesajların dead-letter kuyruğuna (DLQ) yönlendirilmesi, alarm ve sahibi belli bir yeniden oynatma (replay) prosedürü.
9. Her saga adımı için telafi eylemini, onun idempotency'sini ve telafinin kendisi başarısız olursa ne olacağını (manuel müdahale yolu) tanımla. Hiç yanıt vermeyebilecek adımlara zaman aşımı ekle.
10. Şema evrimi kurallarını belirle: uyumluluk modu (backward/forward/full), yalnızca ekleme yapan değişiklikler, kırıcı değişiklikler için sürüm artırma ve kullanımdan kaldırma yolu.
11. Gözlemlenebilirliği tanımla: korelasyon kimlikleriyle izleme (tracing), tüketici gecikmesi (consumer lag), DLQ derinliği ve uçtan uca gecikme. Belirtilmiş bir gereksinime dayanmayan her tasarım seçimini `[VARSAYIM]` olarak etiketle.
12. Hedef devam ediyorsa yayınlanan her olay için `data-contract`, sürümleme için `schema-evolution-plan` veya koordinasyon seçimini kaydetmek için `adr` öner.

## Çıktı formatı
```markdown
# Olay Güdümlü Akış: <süreç>
Koordinasyon: <koreografi | orkestrasyon> — çünkü <gerekçe>

## Akış
| Adım | Üretici | Mesaj (tür: olay/komut) | Topic / kanal | Bölümleme anahtarı | Tüketiciler | Hata durumunda |
|---|---|---|---|---|---|---|

## Olay Kataloğu
| Olay | Sürüm | Yük biçimi | Temel alanlar | Kişisel veri | Sahip |
|---|---|---|---|---|---|

## Teslimat ve Tutarlılık
- Yayınlama: <outbox | CDC>
- Teslimat: en az bir kez; idempotency: <tüketici bazında mekanizma>
- Sıralama: <anahtar başına garanti / garanti olmayan yerler>

## Saga ve Telafi
| Adım | Eylem | Telafi | Zaman aşımı | Telafi başarısız olursa |
|---|---|---|---|---|

## Hata Yönetimi
- Yeniden deneme: <politika> · DLQ: <ad, sahip, alarm> · Yeniden oynatma: <prosedür>

## Şema Evrimi
- Uyumluluk: <mod> · Kırıcı değişiklik süreci: ...

## Gözlemlenebilirlik
- ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her tüketici idempotent ve mekanizması adlandırılmış.
- [ ] Yayınlama durum değişikliğinden ayrışamaz (outbox, CDC veya eşdeğeri).
- [ ] Sıralama garantileri bölümleme anahtarı bazında belirtilmiş, diğer yerlerde tüketiciler sıra bozulmasını tolere ediyor.
- [ ] Her saga adımının bir telafisi, zaman aşımı ve manuel yedek yolu var.
- [ ] Yüklerdeki kişisel veri en aza indirilmiş ve işaretlenmiş.
- [ ] DLQ'ların sahibi, alarmı ve yeniden oynatma prosedürü var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Uçtan uca tam bir kez (exactly-once) varsaymak. Broker bunu kendi içinde sunabilir, ama broker dışındaki yan etkiler yine idempotency ister.
- Outbox olmadan çift yazma (önce veritabanına kaydet, sonra yayınla); çökme anında olay kaybolur veya olmayan olay yayınlanır.
- Olayları komut gibi ("ReserveStock") veya CRUD gibi ("OrderUpdated") adlandırmak; bu, tüketicileri üreticinin niyetine bağlar ya da anlamı gizler.
- Kimsenin izlemediği bir DLQ; sessiz veri kaybına dönüşür.

## Örnek
Girdi: "Sipariş, ödeme, stok ve sevkiyat arasında sipariş verme; ödeme başarısız olursa telafi."

Çıktıdan bir bölüm:
- Koordinasyon: orkestrasyon; çünkü telafili dört adım ve harici ödeme sağlayıcısında zaman aşımı var.
- Adım 2: Orkestratör → "AuthorizePayment" (komut) → payment.commands, anahtar = orderId; hata durumunda → "ReleaseStock" telafisi, ardından "Order Rejected" olayı.
- Idempotency: stok servisi orderId başına işlenmiş eventId'yi saklar; mükerrer "ReserveStock" komutu ikinci bir ayırma yapılmadan onaylanır.
- `[VARSAYIM]` Ödeme zaman aşımı 15 dakika; ödeme sağlayıcısının SLA'sıyla teyit et.
