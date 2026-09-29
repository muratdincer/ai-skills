---
name: test-data-design
description: "Gerçekçi, gizlilik açısından güvenli; denklik sınıflarını, sınırları, durumları ve ilişkisel uç durumları kapsayan test veri setleri ile ortam bazında hazırlama ve sıfırlama yaklaşımı tasarlar. Testler belirli veriye ihtiyaç duyduğunda, test için üretim verisi kullanılması gündeme geldiğinde, veri hazırlığı koşumu veya otomasyonu engellediğinde ya da bir özelliğin testi için hangi verinin gerektiği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: design
  title: "Test verisi tasarlama"
  related: "equivalence-boundary-analysis, test-case-writing, data-classification, environment-strategy, privacy-impact-assessment"
  prompt: "Kredi başvuru akışımız için test verisi tasarla: farklı gelir bantlarında başvuranlar, ortak başvuranlar, mevcut müşteriler ve kara listedeki kimlikler; SIT ve UAT için."
---

# Test Verisi Tasarlama

## Amaç
Planlanan her testin bilinen ve tekrarlanabilir veriyle koşmasını sağlayan, riskli kombinasyonları kapsayan ve gerçek kişisel veriyi asla açığa çıkarmayan bir veri seti tanımı üretmek.

## Ne zaman kullanılır
- Test case'ler "geçerli bir müşteri" veya "borcu olan bir hesap" diyor ve hangi kaydın kullanılacağını kimse bilmiyor.
- Ekip üretim verisini test ortamına kopyalamayı planlıyor.
- Ortak veri başka koşumlar tarafından tüketildiği veya değiştirildiği için otomatik testler kırılıyor.
- Yeni bir özellik, mevcut veri setlerinin kapsamadığı varlıklar, durumlar veya kurallar getiriyor.

## Ne zaman kullanılmaz
- Hangi girdi değerlerinin test edileceğine henüz karar verilmediyse önce `equivalence-boundary-analysis` kullanılır.
- Tüm platform için veri hassasiyet sınıflandırması gerekiyorsa `data-classification` kullanılır.
- Ortam yapısı ve veri yenileme politikası gerekiyorsa `environment-strategy` kullanılır.

## Girdiler
Zorunlu:
- Veri gerektiren özellik, test case'ler veya senaryolar ya da ilgili veri modeli/varlıklar.

İsteğe bağlı, kaliteyi artırır:
- Alan kuralları, referans veriler, durum modelleri, entegrasyon bağımlılıkları.
- Hedef ortamlar, yenileme sıklığı, mevcut veri setleri veya üreteçler.
- Veri koruma kısıtları (KVKK/GDPR, sözleşmesel, kurum içi politika).

Ne testler ne de varlıklar biliniyorsa bunları iste. Bilinmeyen alan kuralları `[BİLİNMİYOR]` ve açık soru olur.

## Süreç
1. Testlerin dokunduğu varlıkları, nitelikleri ve ilişkileri; referans ve konfigürasyon verisi dahil listele.
2. Bir kararda kullanılan her nitelik için denklik sınıflarını ve sınırlarını çıkar; verilmiş bir analiz varsa onu kullan.
3. Durum kapsamını ekle: bir testin ihtiyaç duyduğu her yaşam döngüsü durumu (ör. taslak, aktif, askıda, kapalı).
4. İlişkisel uç durumları ekle: sahipsiz kayıtlar, çok sayıda alt kayıt, sıfır alt kayıt, döngüsel veya mükerrer referanslar, sistemler arası ID uyumsuzlukları.
5. İçerik uç durumlarını ekle: azami uzunluk, Unicode ve Türkçe karakterler (İ/ı, ş, ğ), boşluklar, baştaki sıfırlar, saat dilimleri ve yaz saati, artık gün, para birimi hassasiyeti.
6. Her alanı hassasiyetine göre sınıfla ve veri seti başına kaynak seç: sentetik üretim, maskelenmiş/takma adlı kopya veya referans veri alt kümesi. Varsayılan sentetiktir; maskelenmiş üretim kopyasını ve maskeleme kurallarını gerekçelendir.
7. Sahiplik ve izolasyonu tanımla: hangi veri salt okunur ortak, hangisi test başına oluşturulup temizleniyor, paralel koşumlar çakışmayı nasıl önlüyor (benzersiz önek, koşum başına tenant).
8. Hazırlama ve sıfırlamayı tanımla: seed script'leri, API ile kurulum, snapshot'lar, ortam bazında yenileme sıklığı ve bunları kimin çalıştırdığı.
9. Her veri setini onu kullanan testlere bağla; böylece kullanılmayan veri ve kapsanmayan testler görünür olur.
10. Çıkarımla belirlenen her kuralı veya hacmi `[VARSAYIM]` ile işaretle ve açık soruları listele.
11. Kullanıcı devam ederse adlandırılmış veri setlerine atıf yapmak için `test-case-writing`, gerçek kişisel veri hâlâ gündemdeyse `privacy-impact-assessment` öner.

## Çıktı formatı
```markdown
# Test Verisi Tasarımı: <özellik / sistem>
## Kapsamdaki Varlıklar ve Kurallar
| Varlık | Nitelik | Sınıflar / sınırlar | Kaynak kural |
|---|---|---|---|

## Veri Setleri
| ID | Amaç | Anahtar değerler / durum | Hassasiyet | Kaynak (sentetik/maskeli/referans) | Kullanan testler |
|---|---|---|---|---|---|

## Uç Durum Kayıtları
- <kayıt>: <neden var>

## İzolasyon ve Yaşam Döngüsü
- Salt okunur ortak: ...
- Test başına oluşturulan / temizlik: ...
- Paralel koşum stratejisi: ...

## Ortam Bazında Hazırlama
| Ortam | Yöntem | Yenileme sıklığı | Sorumlu |
|---|---|---|---|

## Gizlilik Kontrolleri
- Maskeleme / üretim kuralları: ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Kapsamdaki her test en az bir veri setine bağlı ve her veri seti kullanılıyor.
- [ ] Sınıflar, sınırlar, durumlar ve ilişkisel uç durumların hepsi temsil ediliyor.
- [ ] Gerçek kişisel veri yok; maskelenmiş kopya varsa maskeleme kuralları ve hukuki dayanağı belirtilmiş.
- [ ] Paralel ve tekrarlanan koşumlar birbirinin verisini bozamıyor.
- [ ] Hazırlama ve sıfırlama tekrarlanabilir; sorumlusu var ya da `[TBD]`.
- [ ] Çıkarımla belirlenen kurallar ve hacimler `[VARSAYIM]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Üretimden bir kopya alalım." Maskeleme serbest metni, ekleri ve logları nadiren kapsar; sentetik veriyi tercih et, maskelenmiş kopyayı incelemeden geçen bir istisna olarak ele al.
- Herkesin kullandığı "altın" kayıtlar. Bir test durumu değiştirir, on test kırılır; veriyi test başına oluştur veya her koşumdan önce sıfırla.
- Yalnızca mutlu yol verisi. Hatalar olağandışı durum ve ilişkilerde yoğunlaşır; bunları bilinçli tasarla.
- Takvim gününe sabitlenmiş tarihler. Verinin eskimemesi için göreli tarih kullan ("bugün - 91 gün").

## Örnek
Girdi: "Kredi başvurusu: gelir bantları, ortak başvuranlar, mevcut müşteriler, kara listedeki kimlikler; SIT ve UAT."

Çıktıdan bir bölüm:
| ID | Amaç | Anahtar değerler / durum | Hassasiyet | Kaynak | Kullanan testler |
|---|---|---|---|---|---|
| LD-03 | Gelir tam bant sınırında | Aylık gelir = bant üst sınırı `[BİLİNMİYOR: sınır değeri]` | Kişisel (sentetik) | Üreteç | TC-011, TC-012 |
| LD-07 | Ortak başvuran kara listede, ana başvuran temiz | Ortak başvuran kimliği test kara listesinde | Kişisel (sentetik) | Seed script | TC-020 |
| LD-09 | Yalnızca kapalı hesabı olan mevcut müşteri | Müşteri Aktif, hesap Kapalı | Kişisel (sentetik) | API ile kurulum | TC-025 |

- Paralel koşum stratejisi: her otomatik koşum başvuranları `RUN<id>-` önekiyle oluşturur; gece temizliği önekli kayıtları siler.
