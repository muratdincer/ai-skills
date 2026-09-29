---
description: Bir özellik, akış, API veya gereksinim için sınırlar, boş/null, mükerrer kayıtlar, eşzamanlılık, saat dilimleri ve tarihler, yetkiler, kısmi hata, yeniden deneme ve idempotency, hacim ve kötüye kullanım başlıklarında uç durumları sistematik olarak ortaya çıkarır; her birini beklenen davranışa veya açık soruya dönüştürür. Bir story, spesifikasyon veya tasarım yalnızca mutlu yolu anlatıyorsa, kabul kriteri veya test tasarımından önce ya da "ne ters gidebilir?", "hangi durumları atlıyoruz?" sorulduğunda kullanılır.
related: acceptance-criteria, error-scenario-catalog, equivalence-boundary-analysis, requirements-gap-analysis, test-scenarios-from-requirements
prompt: Bu story için uç durumları bul: depo görevlisi olarak müşteri siparişi için stok ayırmak istiyorum, böylece ürünler iki kez satılmaz.
---

# Uç Durumları Ortaya Çıkarma

## Amaç
Bir gereksinimin sessizce görmezden geldiği mutlu yol dışı durumları görünür kılmak ve her biri için beklenen davranışa, üretimde hata, olay veya anlaşmazlık olarak ortaya çıkmadan önce karar verilmesini sağlamak.

## Ne zaman kullanılır
- Bir story, use case, API veya ekran spesifikasyonu yalnızca ana akışı anlatıyorsa.
- Kabul kriterleri, test senaryoları veya hata yönetimi tasarımı yazılmadan önce.
- Özellik para, stok, kimlik, zamanlama veya paylaşılan kaynaklara dokunuyorsa.

## Ne zaman kullanılmaz
- Zaten bilinen hatalar için hata mesajları ve kurtarma adımları kataloglanacaksa `error-scenario-catalog` kullanılır.
- Test girdileri sınıflara ve sınırlara ayrılacaksa `equivalence-boundary-analysis` kullanılır.
- Tüm spesifikasyon eksik kategoriler açısından kontrol edilecekse `requirements-gap-analysis` kullanılır.

## Girdiler
Zorunlu:
- Analiz edilecek gereksinim, story, akış veya API tanımı.

İsteğe bağlı, kaliteyi artırır:
- Veri modeli veya alan tanımları, iş kuralları, roller, entegrasyonlar.
- Beklenen hacimler, kullanılan saat dilimleri ve yerel ayarlar, bilinen olaylar.

Gereksinim yoksa iste. Temel alan bilgileri eksikse (örneğin işlemi kimin yapabileceği veya hangi sistemlerin dahil olduğu) bir varsayım belirt ve açık soru olarak listele.

## Süreç
1. Ana akışı 3-7 adımda özetle; varlıklarını, aktörlerini, girdilerini, durum değişikliklerini ve dış çağrılarını listele. Saldırı yüzeyi bunlardır.
2. Sınırlar ve formatlar: min/maks, sıfır, negatif, sınırın hemen altı/üstü, uzunluk, hassasiyet ve yuvarlama, karakter kodlaması, özel karakterler, yerel formatlar.
3. Boş, null ve eksik: gelmeyen isteğe bağlı alanlar, boş listeler, ilk kullanım (hiç veri yok), silinmiş veya arşivlenmiş referans kayıtlar.
4. Mükerrerlik ve kimlik: çift gönderim, aynı isteğin iki kez gelmesi, içe aktarımdan gelen mükerrer kayıtlar, büyük/küçük harf ve boşluk varyantları, birleştirilmiş veya yeniden adlandırılmış varlıklar.
5. Eşzamanlılık ve sıralama: aynı kayıt üzerinde iki aktör, kontrol ile işlem arasında yarış, eski okuma, sırası bozuk veya geç gelen olaylar, kilit/zaman aşımı davranışı.
6. Zaman ve tarihler: saat dilimleri, yaz saati geçişleri, ay/yıl sonu, artık gün, iş takvimi ve tatiller, saat kayması, tam sınırda dolan süre, geriye veya ileriye tarihli girdi.
7. Yetkiler ve durum: yetkisiz rol, akış ortasında rol değişikliği, kiracılar arası erişim, yanlış durumdaki bir nesne üzerinde işlem, iptal edilmiş oturum.
8. Kısmi hata, yeniden deneme ve idempotency: yan etki oluştuktan sonra alt sistemde zaman aşımı, yeniden denemenin yarattığı mükerrerlik, telafi/geri alma, iki kez veya hiç teslim edilmeyen mesajlar, bu sırada kullanıcının ne gördüğü.
9. Hacim ve kötüye kullanım: büyük yükler, toplu işlemler, sayfalama sınırları, hız limitleri, numaralandırma (enumeration), enjeksiyon, otomatik kötüye kullanım, kaynak tüketimi.
10. Her durum için girdide belirtilmişse beklenen davranışı yaz; belirtilmemişse `[VARSAYIM]` işaretli bir davranış öner ve olası sahibiyle bir karar sorusu ekle. Olasılık ve etkiyi (Y/O/D) puanla, yalnızca ilgili durumları tut.
11. Sonraki beceriyi öner: karara bağlanan durumları kritere çevirmek için `acceptance-criteria`, test tasarımı için `test-scenarios-from-requirements`, hata mesajları için `error-scenario-catalog`.

## Çıktı formatı
```markdown
# Uç Durumlar: <özellik / story>
**Ana akış:** 1. ... 2. ... 3. ...
**İncelenen kapsam:** <varlıklar, aktörler, entegrasyonlar>

| # | Kategori | Durum (Diyelim ki/Olduğunda) | Beklenen davranış | Kaynak (belirtilmiş / [VARSAYIM]) | O | E |
|---|---|---|---|---|---|---|
| UD-01 | Eşzamanlılık | İki görevli son birimi aynı anda ayırıyor | Biri başarılı olur, diğeri "yetersiz stok" alır | [VARSAYIM] | O | Y |

## Gereken Kararlar
1. <soru> – <neden önemli> – <sahibi>

## İlgili Durum Çıkmayan Kategoriler
- <kategori> – <neden>
```

## Kalite kontrol listesi
- [ ] On kategorinin tamamı değerlendirildi; atlananlar gerekçesiyle listelendi.
- [ ] Her durum genel bir başlık değil, somut (belirli değerler, aktörler, zamanlama).
- [ ] Her durumun beklenen davranışı veya açık bir karar sorusu var; varsayılan davranış etiketli.
- [ ] Para, veri bütünlüğü, güvenlik veya gizlilikle ilgili yüksek etkili durumlar en üstte işaretlendi.
- [ ] Durumlar bu özellikle ilgili; genel gürültü ayıklandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Durum yerine kategori yazmak ("eşzamanlılık sorunları"). Somut durumu ve beklenen sonucu yaz.
- İş davranışına kendi başına karar vermek. Öner, `[VARSAYIM]` olarak etiketle ve kararı ürün sahibine yönlendir.
- Girdi doğrulamasında durmak. En pahalı durumlar genellikle eşzamanlılık, kısmi hata ve zamanla ilgilidir.
- Eşit ağırlıkta 80 durum üretmek. Ekibin önce en önemlilerini ele alması için etki ve olasılığa göre sırala.

## Örnek
Girdi: "Depo görevlisi olarak müşteri siparişi için stok ayırmak istiyorum, böylece ürünler iki kez satılmaz."

Çıktıdan bir bölüm:
| # | Kategori | Durum | Beklenen davranış | Kaynak | O | E |
|---|---|---|---|---|---|---|
| UD-03 | Yeniden deneme | Stok düşüldükten sonra ayırma çağrısı zaman aşımına uğruyor; görevli tekrar tıklıyor | İkinci çağrı idempotent (aynı sipariş no), çift ayırma olmaz | [VARSAYIM] | O | Y |
| UD-07 | Zaman | Ayırmanın süresi yaz saati geçiş gecesinde doluyor | Süre UTC ile hesaplanır; arayüz yerel saati gösterir | [VARSAYIM] | D | O |
| UD-09 | Yetki/durum | Ayırma oluşturulurken sipariş iptal ediliyor | Ayırma serbest bırakılır; görevli bilgilendirilir | [TBD] | O | O |

Gereken karar: Sipariş onaylanmazsa ayırma stoku ne kadar süre tutar? – Ürün sahibi.
