---
name: integration-requirements
description: "Sistemler arası entegrasyon gereksinimlerini; katılan sistemleri, yönü, aktarılan veriyi, tetikleyiciyi ve sıklığı, hacimleri, hata yönetimini, güvenliği ve SLA'ları iki tarafın da geliştirip test edebileceği biçimde tanımlar. Bir özelliğin başka bir sisteme veri göndermesi veya oradan veri alması gerektiğinde, yeni bir arayüz ya da API talep edildiğinde veya tasarımdan önce bir tedarikçi/üçüncü taraf entegrasyonu üzerinde anlaşılması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Entegrasyon gereksinimi tanımlama"
  related: "field-mapping, error-scenario-catalog, api-contract, integration-pattern-selection, data-requirements"
  prompt: "E-ticaret platformumuzdan onaylanan siparişlerin ERP'ye gönderilmesi ve stok seviyelerinin geri alınması için entegrasyon gereksinimlerini tanımla."
---

# Entegrasyon Gereksinimi Tanımlama

## Amaç
Her arayüz için hangi sistemler arasında neyin, ne zaman, ne hacimde taşındığını, hataların nasıl ele alındığını ve hangi hizmet seviyesinin beklendiğini tanımlamak. Böylece iki sahip ekip de temel konuları sonradan yeniden pazarlık etmeden entegrasyonu tasarlayıp geliştirebilir ve test edebilir.

## Ne zaman kullanılır
- Bir özellik başka bir iç veya dış sistemden veri almak ya da oraya veri göndermek zorunda olduğunda.
- Sözleşme veya tasarım öncesinde bir tedarikçi, iş ortağı ya da SaaS entegrasyonu üzerinde anlaşılması gerektiğinde.
- Mevcut noktadan noktaya bir arayüz değiştirilirken veya genişletilirken davranışının açıkça yazılması gerektiğinde.

## Ne zaman kullanılmaz
- Açık soru desen veya ara katman seçimiyse (senkron/asenkron, ESB/event bus) `integration-pattern-selection` kullanılır.
- Tek eksik alan düzeyinde kaynak-hedef eşlemesiyse `field-mapping` kullanılır.
- API uç nokta/şema düzeyinde tasarlanıyorsa `api-contract` kullanılır.

## Girdiler
Zorunlu:
- Entegrasyonu gerektiren iş ihtiyacı veya özellik.
- İlgili sistemler (en az kaynak ve hedef).

İsteğe bağlı, kaliteyi artırır:
- Mevcut arayüz dokümanları, API tanımları, örnek mesajlar.
- Hacimler, yoğun saatler, iş takvimleri, sözleşmelerdeki SLA'lar.
- Güvenlik, veri sınıflandırması ve mevzuat kısıtları (ör. KVKK/GDPR).
- Sistem sahipleri ve destek muhatapları.

İhtiyaç veya sistemler eksikse bunları tek bir kısa soru grubuyla iste. Geri kalan her şeyi açık soru olarak ele al.

## Süreç
1. İş ihtiyacını tek cümleyle yeniden yaz ve entegrasyonu gerekli kılan iş olayını adlandır (ör. "sipariş onaylandı"). Kullanıcının söylediğini kendi çıkarımından ayır; çıkarımları `[VARSAYIM]` olarak etiketle.
2. Arayüz envanterini çıkar: her arayüz için ID, kaynak sistem, hedef sistem, yön, iş sahibi ve teknik sahip içeren bir satır. Çift yönlü akışları iki ayrı arayüze böl.
3. Her arayüz için tetikleyiciyi ve zamanlamayı tanımla: olay tabanlı, zamanlanmış (takvim ve saat dilimiyle) veya isteğe bağlı; gereken gecikme (gerçek zamanlı, azami gecikmesi belli yakın gerçek zamanlı, batch).
4. Aktarılan veriyi varlık düzeyinde tanımla: iş nesneleri, anahtar tanımlayıcılar, zorunlu nitelikler, her niteliğin master sistemi ve eşleşmesi gereken referans veri/kod listeleri. Alan ayrıntısını `field-mapping`e bırak.
5. Hacimleri sayısallaştır: dönem başına ortalama ve en yoğun mesaj veya kayıt sayısı, mesaj boyutu ve büyüme. Eksik sayıları `[BİLİNMİYOR]` olarak işaretle; asla uydurma.
6. Teslim semantiğini belirle: sıralama ihtiyacı, idempotency anahtarı, tekrar eden mesajların ele alınması, en az bir kez/tam bir kez beklentisi, batch'lerde kısmi başarı kuralları.
7. Her arayüz için hata yönetimini belirle: doğrulama hataları, hedefin erişilemez olması, zaman aşımları, iş kuralı retleri; yeniden deneme politikası, dead-letter/park etme, alarm, kime bildirileceği ve elle yeniden işleme yolu.
8. Fonksiyonel olmayan gereksinimleri kaydet: erişilebilirlik penceresi, yanıt süresi, verim, SLA/OLA ve destek saatleri, bakım pencereleri, izleme ve mutabakat (sistemler arası adet/toplam kontrolü).
9. Güvenlik ve uyumu kaydet: kimlik doğrulama yöntemi, yetki kapsamı, aktarımda ve durağan halde şifreleme, taşınan kişisel veya hassas veri (en aza indir ve maskele), denetim kaydı, saklama süresi.
10. Bağımlılıkları, kısıtları (istek limitleri, tedarikçi sözleşme şartları, eski formatlar) ve ilk yükleme ile geriye dönük veri doldurma gibi geçiş ihtiyaçlarını kaydet.
11. Şablonu doldur, desteklenmeyen her alanı `[BİLİNMİYOR]` veya `[TBD]` olarak işaretle ve açık soruları cevaplayabilecek kişiyle birlikte listele.
12. Hedef devam ediyorsa nitelik ayrıntısı için `field-mapping`, hata durumları için `error-scenario-catalog`, arayüz tasarımı için `api-contract` veya desen henüz belli değilse `integration-pattern-selection` öner.

## Çıktı formatı
```markdown
# Entegrasyon Gereksinimleri: <entegrasyon adı>
İş ihtiyacı: <tek cümle> · Tetikleyen olay: <olay>

## Arayüz Envanteri
| ID | Kaynak → Hedef | Yön | Tetikleyici / zamanlama | Gecikme | İş sahibi | Teknik sahip |
|---|---|---|---|---|---|---|

## Arayüz <ID>: <ad>
- Aktarılan veri: <nesneler, anahtarlar, zorunlu nitelikler, master sistem>
- Eşlenecek referans veri: ...
- Hacim: ort. <n>/<dönem>, en yoğun <n> <saat> [verilmediyse BİLİNMİYOR]
- Teslim semantiği: sıralama, idempotency anahtarı, tekrarlar, batch kısmi başarı
- Hata yönetimi: | Hata türü | Tespit | Yeniden deneme | Nihai işlem | Bildirilen |
- NFR'ler: erişilebilirlik, yanıt süresi, verim, SLA, destek saatleri, mutabakat
- Güvenlik: kimlik doğrulama, yetkilendirme, şifreleme, kişisel veri (maskeli/asgari), denetim

## Bağımlılıklar ve Kısıtlar
## Geçiş / İlk Yükleme
## Varsayımlar
- [VARSAYIM] ...
## Açık Sorular
1. <soru> — <neden önemli> — <muhatap>
```

## Kalite kontrol listesi
- [ ] Her arayüzün adı konmuş bir kaynağı, hedefi, yönü ve iki tarafta da sahibi var.
- [ ] Tetikleyici, gecikme ve hacim yazılı ya da açıkça `[BİLİNMİYOR]` olarak işaretli; uydurulmuş sayı yok.
- [ ] Her arayüzde yeniden deneme, nihai hata ve bildirimi kapsayan hata yönetimi var.
- [ ] Idempotency/tekrar yönetimi ve mutabakat ele alındı.
- [ ] Kişisel veya hassas veri belirlendi; en aza indirme ve koruma yöntemi yazıldı.
- [ ] Çıkarımlar etiketli ve varsayımlarda ya da açık sorularda yer alıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Azami gecikme vermeden "gerçek zamanlı" yazmak. Veri geç gelirse hangi iş kararının bozulacağını sor ve sayıyı oradan türet.
- Yalnızca mutlu yolu tanımlamak. Entegrasyon olaylarının çoğu yeniden denemelerden, tekrar eden mesajlardan ve sessiz kısmi hatalardan çıkar; mutabakatı zorunlu tut.
- Nitelik sahipliğini belirsiz bırakmak. Bir alanı iki sistem de değiştirebiliyorsa hangisinin master olduğunu yaz, yoksa çakışma canlıda ortaya çıkar.

## Örnek
Girdi: "Onaylanan siparişler web mağazadan ERP'ye gidiyor; ERP stok bilgisini geri gönderiyor."

Çıktıdan bir bölüm:
| ID | Kaynak → Hedef | Yön | Tetikleyici / zamanlama | Gecikme |
|---|---|---|---|---|
| INT-01 | Web mağaza → ERP | Push | Olay: sipariş onaylandı | ≤ 5 dk `[VARSAYIM]` |
| INT-02 | ERP → Web mağaza | Push | Zamanlanmış, 15 dakikada bir `[TBD]` | Batch |

- INT-01 hata yönetimi: ERP erişilemezse artan aralıklarla 5 kez yeniden dene, ardından park et ve sipariş operasyonuna alarm gönder; tekrar eden mesajlar sipariş numarasıyla (idempotency anahtarı) reddedilir.
- Açık soru: Onaydan sonra teslimat adresinin master sistemi web mağaza mı, ERP mi? — Sipariş yönetimi sahibi.
