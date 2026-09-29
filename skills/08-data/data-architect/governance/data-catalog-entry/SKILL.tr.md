---
description: "Bir veri seti, tablo, rapor veya veri ürünü için veri kataloğu kaydı yazar: iş açıklaması, sahip ve veri sorumlusu (steward), tanecik, anahtar alanlar, köken özeti, kalite durumu, tazelik, hassasiyet ve erişim, kullanım rehberi. Bir veri seti keşif için kaydedilirken veya belgelenirken, self-servise hazırlanırken ya da bir tablo veya veri ürünü katalog için tarif edilmek istendiğinde kullanılır."
related: "data-lineage-doc, data-classification, data-quality-rules, data-contract, glossary-builder"
prompt: "Bu DDL'i ve finans ekibinin notlarını kullanarak sales.fact_invoice_line tablosu için katalog kaydı yaz."
---

# Veri Kataloğu Kaydı

## Amaç
Üreticiyle hiç konuşmamış bir tüketicinin, veri setinin ihtiyacına uyup uymadığına, nasıl doğru kullanılacağına ve kime sorulacağına iki dakikada karar verebilmesini sağlamak; yönetişime de ihtiyaç duyduğu sahiplik ve hassasiyet bilgilerini vermek.

## Ne zaman kullanılır
- Yeni bir veri seti, tablo, görünüm, rapor veya veri ürünü yayımlandığında.
- Tüketiciler bir veri seti hakkında sürekli aynı soruları soruyor ya da onu yanlış kullanıyorsa.
- Katalog temizliği veya sertifikasyon çalışması yürütülüyorsa.

## Ne zaman kullanılmaz
- Bağlayıcı üretici-tüketici garantileri gerekiyorsa `data-contract` kullanılır.
- Dönüşüm düzeyinde tam köken gerekiyorsa `data-lineage-doc` kullanılır.
- Veri setleri değil iş terimleri tanımlanıyorsa `glossary-builder` kullanılır.

## Girdiler
Zorunlu:
- Veri seti tanımlayıcısı ve şunlardan en az biri: şema/DDL, örnek sorgu, üretici açıklaması.

İsteğe bağlı:
- Sahip/veri sorumlusu, kaynaklar, yenileme takvimi, bilinen kalite sorunları, sınıflandırma, tipik sorgular, ilgili sözlük terimleri.

Ne şema ne açıklama verilmişse iste. Diğer her şey tahmin yerine `[BİLİNMİYOR]` olur.

## Süreç
1. İş odaklı bir özet yaz: bir satırın neyi temsil ettiği (tanecik), hangi soruları yanıtladığı ve neyi kapsamadığı.
2. Sahipliği kaydet: veri sahibi (hesap verebilir iş rolü), veri sorumlusu (günlük), teknik sorumlu; bilinmeyenleri işaretle.
3. Anahtar alanları tarif et: birincil/iş anahtarı, zaman alanları (hangi tarihe göre filtrelenmeli ve saat dilimi), birimleriyle ana ölçüler, ana boyutlar; her birini sözlük terimlerine bağla.
4. Kökeni her adım için bir satırla özetle: kaynak sistemler → ana dönüşümler → bu veri seti → bilinen alt tüketiciler.
5. Tazelik ve takvimi belirt: güncelleme sıklığı, beklenen hazır olma zamanı, tarihçe derinliği, geç veri davranışı.
6. Kalite durumunu belirt: sertifikalı/sertifikasız, aktif kontroller, bilinen sorunlar ve geçici çözümler, son olay.
7. Hassasiyet ve erişimi belirt: sınıf düzeyi, kişisel veri alanları, uygulanan maskeleme, erişim talebi yolu.
8. Kullanım rehberi ver: doğru join anahtarları, yaygın filtreler, tuzaklar (çift sayım, iptal kayıtlar, para birimi), tarafsız SQL ile örnek sorgu.
9. İşin gerçekten kullandığı etiketleri ve arama eş anlamlılarını ekle.
10. Yaşam döngüsü alanlarını belirle: durum (taslak, yayımlandı, kullanımdan kalkıyor), sürüm, gözden geçirme tarihi.

## Çıktı formatı
```markdown
# <Veri setinin görünen adı>
Tanımlayıcı: <...> | Tür: <tablo/görünüm/akış/rapor/veri ürünü> | Durum: <...> | Sertifikalı: <evet/hayır>

## Özet
<2-3 cümle: tanecik, amaç, kapsam dışı>

## Sahiplik
Sahip: <...> | Veri sorumlusu: <...> | Teknik sorumlu: <...>

## Anahtar Alanlar
| Alan | Anlam | Sözlük terimi | Notlar (birim, saat dilimi, boş değerler) |
|---|---|---|---|

## Köken (özet)
<kaynak> → <dönüşüm> → bu veri seti → <tüketiciler>

## Tazelik
Sıklık: <...> | Hazır olma: <...> | Tarihçe başlangıcı: <...>

## Kalite
Kontroller: <...> | Bilinen sorunlar: <...>

## Hassasiyet ve Erişim
Sınıf: <...> | Kişisel alanlar: <...> | Maskeleme: <...> | Erişim talebi: <...>

## Nasıl Kullanılır
- Join: <...> | Filtre: <...>
- Tuzaklar: <...>
- Örnek sorgu: <...>

## Etiketler / Eş Anlamlılar | Gözden geçirme tarihi
```

## Kalite kontrol listesi
- [ ] Tanecik tek cümleyle belirtildi.
- [ ] Sahip ve veri sorumlusu adıyla yazıldı ya da açıkça `[BİLİNMİYOR]`.
- [ ] Filtreleme için doğru tarih alanı ve saat dilimi belirtildi.
- [ ] Hassasiyet ve erişim süreci mevcut; kişisel alanlar listelendi.
- [ ] En az bir tuzak ve bir örnek sorgu verildi.
- [ ] Uydurulmuş SLA, sahip veya kalite iddiası yok.

## Sık yapılan hatalar
- Sütun adlarını açıklama olarak tekrarlamak ("customer_id: müşteri id"). Anlamı, birimleri ve uç durumları anlat.
- Yalnızca mühendislerin okuyabileceği teknik kayıtlar. İş özetiyle başla.
- Güncelliğini yitirmiş kayıtlar. Gözden geçirme tarihi koy ve güncellemeleri şema değişikliklerine bağla.

## Örnek
Girdi: "fact_invoice_line DDL'i; finans: iade faturaları negatif satır olarak dahil; her gece yükleniyor."

Çıktıdan bir bölüm:
- Özet: Fatura kalemi başına bir satır; iade faturaları negatif satır olarak dahildir. Müşteri, ürün ve döneme göre faturalanmış geliri yanıtlar. Faturalanmamış siparişleri içermez.
- Tuzak: Gelir için invoice_date'e (yerel saat) göre filtrele; order_date farklı toplamlar verir.
- Sahip: `[BİLİNMİYOR]` (öneri: Finansal Kontrol); Tazelik: her gece, hazır olma zamanı `[TBD]`.
