---
name: data-exploration
description: "Tanıdık olmayan bir veri seti için yapılandırılmış bir keşifsel veri analizi yürütür; yapı, tanecik, dağılımlar, boş değerler, mükerrer kayıtlar, aykırı değerler, zaman kapsamı, ilişkiler ve kalite sorunları; bulguları ve kullanıma uygunluğu raporlar. Yeni bir tablo, veri çekimi veya dosya geldiğinde, üzerine model, metrik veya dashboard kurulmadan önce ya da \"bu veride ne var?\" sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-analyst
  area: analytics
  title: "Veri setini keşfetme"
  related: "analysis-plan, data-quality-rules, metric-definition, feature-engineering-plan, data-catalog-entry"
  prompt: "Bu veri setini keşfet: order_id, customer_id, order_ts, amount, currency, status, channel kolonlarını içeren 250 bin e-ticaret siparişlik bir CSV. Profil çıktısı ekte."
---

# Veri Setini Keşfetme

## Amaç
Bir veri setinin gerçekte ne içerdiğini, ne kadar güvenilir olduğunu ve hangi sorulara cevap verebileceğini, kimse üzerine sonuç kurmadan anlamak ve başkalarının da kullanabileceği kısa bir profil üretmek.

## Ne zaman kullanılır
- Analiz veya modelleme için yeni bir kaynak, veri çekimi ya da dosya kullanılacağında.
- Bir veri setinden gelen sayılar yanlış göründüğünde ve nedeni bilinmediğinde.
- Veri kataloğu kaydı veya kalite kuralları için olgusal girdi gerektiğinde.

## Ne zaman kullanılmaz
- Soru ve yöntem zaten netse `analysis-plan` kullanılır.
- Bir veri hattı için resmi doğrulama kuralları yazılacaksa `data-quality-rules` kullanılır.
- Bir model için öznitelikler tasarlanıyorsa `feature-engineering-plan` kullanılır.

## Girdiler
Zorunlu:
- Veri seti tanımı: şema (kolon adları ve tipleri) ile birlikte örnek veri, profil çıktısı veya özet istatistikler.

İsteğe bağlı, kaliteyi artırır:
- Kolonların iş anlamı, kaynak sistem, veri çekme mantığı.
- Amaçlanan kullanım (analiz, dashboard, model).

Yalnızca kolon listesi varsa, çalıştırılacak kontrollerle bir keşif planı üret ve tüm bulguları `[TBD]` olarak işaretle. Asla istatistik uydurma.

## Süreç
1. Taneciği belirle: bir satırın neyi temsil ettiğini; aday anahtarın tekil ve boş olmadığını doğrula.
2. Kapsamı kontrol et: satır sayısı, zaman aralığı, gün/hafta bazında boşluklar, ani hacim sıçramaları (çoğunlukla geriye dönük yükleme veya izleme değişikliği).
3. Her kolonu tipine göre profille: sayısal (min, yüzdelikler, ortalama ve medyan, sıfırlar, negatifler), kategorik (kardinalite, en sık değerler, nadir/yanlış yazılmış seviyeler), tarih (aralık, gelecek tarihler, 1900-01-01 gibi varsayılan tarihler), metin/kimlik (format, uzunluk).
4. Her kolon için eksikliği ölç ve rastgele mi yoksa bir segmente veya döneme mi bağlı olduğunu kontrol et.
5. Mükerrer kayıtları (birebir ve iş anahtarı bazında) ve tutarsız birim, para birimi veya saat dilimlerini tespit et.
6. Aykırı değerleri açıkça belirtilmiş bir kuralla (IQR, yüzdelik, alan sınırları) bul ve sınıflandır: hata, meşru uç değer veya bilinmiyor.
7. İlişkileri incele: önemli korelasyonlar, önemli kategorikler arasında çapraz tablolar, ilişkili tablolara referans bütünlüğü.
8. Kişisel veya hassas veri kolonlarını (ad, e-posta, telefon, kimlik numarası, konum) işaretle; maskeleme veya hariç tutma öner (KVKK/GDPR).
9. Amaçlanan kullanıma uygunluğu değerlendir: olduğu gibi kullanılabilir, listelenen düzeltmelerle kullanılabilir veya kullanılamaz.
10. Sorunları önem derecesi ve sonraki kontrol ya da sorumluyla kaydet.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sorunları kontrollere çevirmek için `data-quality-rules` veya sonraki analitik adım için `analysis-plan` / `feature-engineering-plan` öner.

## Çıktı formatı
```markdown
# Veri Keşfi: <veri seti>
| Alan | Değer |
|---|---|
| Tanecik | <bir satır = ...> |
| Satır sayısı / zaman aralığı | ... |
| Aday anahtar tekil mi? | Evet / Hayır (<n> mükerrer) |
| Amaçlanan kullanım | ... |
| Uygunluk | Kullanılabilir / Düzeltmeyle kullanılabilir / Kullanılamaz |

## Kolon Profili
| Kolon | Tip | Boş % | Tekil | Notlar (aralık, sık değerler, anomaliler) |
|---|---|---|---|---|

## Temel Bulgular
1. ...

## Veri Kalitesi Sorunları
| Sorun | Kolonlar | Önem | Önerilen düzeltme / sorumlu |
|---|---|---|---|

## Hassas Veri
- <kolon> – <kategori> – <maskele / çıkar / gerekçeyle tut>

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Tanecik ve anahtarın tekilliği belirtildi ve doğrulandı.
- [ ] Her istatistik verilen profil veya örnekten geliyor; eksik olanlar `[TBD]`.
- [ ] Eksiklik yalnızca yüzde olarak değil örüntü açısından da incelendi.
- [ ] Aykırı değer kuralı açık; aykırı değerler sessizce silinmedi, sınıflandırıldı.
- [ ] Hassas kolonlar ele alınma önerisiyle işaretlendi.
- [ ] Kullanıma uygunluk konusunda net bir hüküm verildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çarpık veride ortalamaya güvenmek. Medyan ve yüzdelikleri raporla.
- Özel anlamlı değerleri (0, -1, 9999, 1900-01-01) gerçek değer gibi ele almak.
- Zaman boyutunu göz ardı etmek; birçok sorun yalnızca zaman içindeki basamaklı değişimler olarak görünür.

## Örnek
Girdi: 250 bin sipariş; kolonlar order_id, customer_id, order_ts, amount, currency, status, channel; profilde 312 mükerrer order_id, amount minimumu -45,00, currency'de hem "TRY" hem "TL" var.

Çıktıdan bir bölüm:
- Aday anahtar tekil mi? Hayır – 312 mükerrer order_id; muhtemelen durum güncellemeleri yeni satır olarak eklenmiş `[kaynak sahibiyle teyit et]`.
- Sorun: Negatif tutarlar (iade mi?) satışlarla karışık – gelir metrikleri için önem Yüksek.
- Sorun: "TRY" ve "TL" aynı para birimini temsil ediyor – normalize edilmeli.
