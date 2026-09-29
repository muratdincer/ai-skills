---
description: "Veri üreticisi ile tüketicileri arasında veri sözleşmesi yazar: şema, anlam, kalite beklentileri, tazelik ve erişilebilirlik SLA'ları, sahiplik, erişim ve gizlilik koşulları, sürümleme ve değişiklik/kullanımdan kaldırma kuralları; makinece okunmaya uygun bir biçimde. Bir veri seti, olay akışı veya veri ürünü yayımlanırken, yeni bir tüketici alınırken ya da üretici-tüketici beklentileri resmileştirilmek istendiğinde kullanılır."
related: "schema-evolution-plan, data-quality-rules, api-contract, data-catalog-entry, data-classification"
prompt: "Finans ve öneri ekibinin tükettiği sipariş olay akışı için veri sözleşmesi yaz."
---

# Veri Sözleşmesi Yazma

## Amaç
Üreticinin bir veri setine dair vaatlerini açık ve test edilebilir hale getirmek. Böylece tüketiciler ona güvenebilir, üreticiler onu güvenle değiştirebilir; sessiz kırıcı değişiklikler yönetilen sürümlere dönüşür.

## Ne zaman kullanılır
- Bir veri seti, tablo, olay akışı veya veri ürünü başka ekiplere açılıyorsa.
- Tekrarlayan olaylar kaynaktaki şema veya anlam değişikliklerinden kaynaklanıyorsa.
- Yeni bir tüketici garanti edilmiş alanlara, tazeliğe veya kaliteye ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- Arayüz senkron bir servis API'siyse `api-contract` kullanılır.
- Yalnızca planlanan bir değişikliğin uyumluluğu değerlendiriliyorsa `schema-evolution-plan` kullanılır.
- Yalnızca keşif metaverisi gerekiyorsa `data-catalog-entry` kullanılır.

## Girdiler
Zorunlu:
- Veri seti veya akış (ad, amaç), şeması veya alan listesi, üretici ekip ve en az bir tüketici kullanım senaryosu.

İsteğe bağlı:
- Mevcut kalite sorunları, hacim, teslim mekanizması, hassasiyet sınıfı, saklama ihtiyaçları, tüketici SLA'ları.

Şema veya üretici bilinmiyorsa sor; hesap verebilir bir üreticisi olmayan sözleşme sözleşme değildir.

## Süreç
1. Tarafları belirle: üretici sahip (ekip ve hesap verebilir rol), tüketiciler ve kullanım senaryoları, sözleşme onaylayıcısı.
2. Arayüzü tanımla: teslim mekanizması (tablo, dosya, topic, API), genel ifadeyle konum, format, bölümlendirme, birincil anahtar ve olay anahtarı/sıralama garantileri.
3. Şemayı alan bazında belirt: ad, tip, boş olabilirlik, izinli değer veya aralık, birim/para birimi, iş tanımı ve alanın kararlı sözleşmenin parçası mı yoksa deneysel mi olduğu.
4. Anlamı belirt: tanecik, bir kaydın neyi temsil ettiği, olay zamanı ve işlem zamanı, tekilleştirme garantisi (en az bir kez, fiilen bir kez), silmelerin yönetimi (tombstone, mantıksal silme bayrağı), geç gelen veri.
5. Kalite beklentilerini test edilebilir kurallar olarak (bütünlük, teklik, geçerlilik, referans, hacim eşikleri) hata durumundaki aksiyonla tanımla: engelle, karantinaya al, uyar.
6. Hizmet düzeylerini tanımla: tazelik (olaydan itibaren azami gecikme), erişilebilirlik penceresi, teslim takvimi, destek saatleri, olay iletişim kanalı ve yanıt süreleri.
7. Erişim, gizlilik ve kullanımı tanımla: sınıflandırma, kişisel veri alanları ve hukuki dayanak, maskeleme kuralları, izinli ve yasak kullanımlar, saklama ve silmenin yayılması.
8. Sürümleme ve değişiklik politikasını tanımla: semantic versioning; hangi değişiklikler kırıcı değil (isteğe bağlı alan ekleme), hangileri kırıcı (silme/yeniden adlandırma, tip daraltma, anlam değişikliği); bildirim süresi, paralel koşum süresi, kullanımdan kaldırma süreci.
9. Uygulamayı (enforcement) tanımla: sözleşmenin nerede doğrulandığı (üretici CI, alım kapısı, schema registry uyumluluk modu) ve ihlallerin nasıl raporlandığı.
10. Sözleşmeyi yapılandırılmış, makinece okunmaya uygun bir düzende ve kısa bir insan özetiyle üret.

## Çıktı formatı
```markdown
# Veri Sözleşmesi: <veri seti> v<MAJOR.MINOR.PATCH>
Durum: <taslak/aktif/kullanımdan kalkıyor> | Üretici: <ekip, hesap verebilir rol> | Tüketiciler: <liste>

## Arayüz
Mekanizma: <...> | Format: <...> | Anahtar: <...> | Sıralama: <...> | Bölümlendirme: <...>

## Şema
| Alan | Tip | Boş | Kısıt / değerler | Birim | Tanım | Kararlılık |
|---|---|---|---|---|---|---|

## Anlam
Tanecik: <...> | Zaman: <olay/işlem> | Teslim: <en az bir kez/...> | Silmeler: <...> | Geç veri: <...>

## Kalite Kuralları
| Kural | Kontrol | Eşik | Hata durumunda |
|---|---|---|---|

## Hizmet Düzeyleri
Tazelik: <...> | Erişilebilirlik: <...> | Takvim: <...> | Destek: <...> | Olaylar: <kanal, yanıt süresi>

## Erişim, Gizlilik ve Kullanım
Sınıf: <...> | Kişisel alanlar: <...> | Maskeleme: <...> | İzinli kullanımlar: <...> | Saklama: <...>

## Değişiklik Politikası
Kırıcı değişiklikler: <liste> | Bildirim: <...> | Paralel koşum: <...> | Kullanımdan kaldırma: <...>

## Uygulama
- ...
```

## Kalite kontrol listesi
- [ ] Her alanın tipi, boş olabilirliği ve iş tanımı var.
- [ ] Tanecik, anahtar ve teslim anlamı belirtildi.
- [ ] Kalite kuralları test edilebilir ve her birinin hata aksiyonu var.
- [ ] SLA'lar sayısal; bilinmeyen değerler uydurulmadı, `[TBD]` olarak işaretlendi.
- [ ] Kırıcı ve kırıcı olmayan değişiklikler ile bildirim süreleri tanımlı.
- [ ] Kişisel veri, maskeleme ve saklama ele alındı.

## Sık yapılan hatalar
- Şema dökümünü sözleşme diye sunmak. Asıl değer anlamda, SLA'larda ve değişiklik politikasındadır.
- Uygulaması olmayan sözleşmeler. Üretici hattında ve alımda doğrula, yoksa kayarlar.
- Tip değişmedi diye anlam değişikliklerini (ör. tutar artık brüt değil net) kırıcı olmayan saymak.

## Örnek
Girdi: "Sipariş akışı, Ödeme ekibi üretiyor; Finans gelir için, Öneri ekibi satın alma geçmişi için kullanıyor."

Çıktıdan bir bölüm:
- Anahtar: order_id; order_id bazında sıralama garantili; teslim en az bir kez, tüketiciler (order_id, event_version) üzerinden tekilleştirir.
- total_amount alanı: decimal(18,2), boş olamaz, para birimi currency_code'da, KDV dahil brüt; net'e geçiş MAJOR değişikliktir.
- Tazelik: üzerinde anlaşılacak azami gecikme `[TBD]`; Finans günlük kapanış için 02:00'ye kadar tamlık istiyor `[teyit et]`.
