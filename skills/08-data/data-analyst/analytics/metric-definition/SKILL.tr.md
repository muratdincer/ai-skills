---
description: Bir iş metriğini, iki analistin aynı sayıyı hesaplayacağı kesinlikte tanımlar; amaç, formül, pay/payda, filtreler, tanecik, zaman mantığı, uç durumlar, kaynak alanlar ve sahip. Bir metrik tartışmalı olduğunda, ekipler arasında farklı raporlandığında, dashboard'a veya OKR'a eklenmek üzereyken ya da metrik kataloğuna yazılması gerektiğinde kullanılır.
related: kpi-definition, dashboard-spec, north-star-metric, data-quality-rules, glossary-builder
prompt: "Aktif müşteri" metriğini kesin olarak tanımla; finans ve ürün her ay farklı sayı raporluyor.
---

# Metriği Kesin Tanımlama

## Amaç
Yoruma yer bırakmayan, sürümlenmiş bir metrik tanımı üretmek. Böylece her rapor, dashboard ve ekip aynı sayıyı hesaplar; tartışma "kimin sayısı doğru"dan "ne yapmalıyız"a kayar.

## Ne zaman kullanılır
- İki rapor "aynı" metrik için farklı değer gösterdiğinde.
- Yeni bir KPI bir dashboard'a, OKR'a veya sözleşmeye eklenirken.
- Metrik kataloğu veya semantik katman kaydı yazılması gerektiğinde.

## Ne zaman kullanılmaz
- İhtiyaç bir hedef için hangi KPI'ların önemli olduğunu seçmekse `kpi-definition` kullanılır.
- Soru alan düzeyinde veri doğruluğuysa `data-quality-rules` kullanılır.
- Şirket genelinde tek bir yol gösterici metrik seçiliyorsa `north-star-metric` kullanılır.

## Girdiler
Zorunlu:
- Metrik adı ve cevaplaması gereken iş sorusu.

İsteğe bağlı, kaliteyi artırır:
- Farklı ekiplerin mevcut formülleri veya SQL'leri.
- Kaynak tablolar ve alan adları.
- Bilinen anlaşmazlıklar veya tutmayan sayı örnekleri.

İş sorusu yoksa sor; diğer eksikleri `[TBD]` olarak işaretle.

## Süreç
1. Amacı yaz: metriğin hangi kararı beslediğini ve "iyi" yönün ne olduğunu belirt.
2. Varlığı ve taneciği (müşteri başına, sipariş başına, gün başına) ve kapsamdaki popülasyonu tanımla.
3. Formülü düz dille ve sözde SQL olarak yaz: pay, payda, toplama (tekil sayım, toplam, medyan).
4. Filtreleri ve hariç tutmaları açıkça belirt: test/iç hesaplar, iptal veya iade edilen işlemler, botlar, para birimleri, vergi.
5. Zaman mantığını belirt: olay zamanı mı işlem zamanı mı, saat dilimi, dönem sınırları, kayan ya da takvim pencereleri, geç gelen veri ve geriye dönük düzeltme politikası.
6. Uç durumları ve nasıl ele alınacaklarını sırala: boş değerler, sıfır payda, yeniden aktifleşme, varlık birleşme/bölünmeleri, kısmi dönemler, mükerrer kayıtlar.
7. Kaynak alanlara ve kayıt sistemine eşle; veri soy ağacını (lineage) ve bilinen kalite sorunlarını not et.
8. Mevcut tanımlar çelişiyorsa bir mutabakat tablosu göster (tanım A ve B, farkın nedeni, farkın tahmini yönü) ve birini öner.
9. Sahip, gözden geçirme sıklığı, sürüm ve geçerlilik tarihi belirle; tanım değişince geçmiş değerlerin yeniden hesaplanması veya notlanması gerektiğini yaz.
10. Yorumlama rehberi ekle: bilinen mevsimsellik, ilişkili koruyucu metrikler, manipülasyona karşı notlar.

## Çıktı formatı
````markdown
# Metrik: <ad> (v<sürüm>)
| Alan | Değer |
|---|---|
| Amaç / karar | ... |
| İstenen yön | Yukarı / Aşağı / Bant içinde |
| Sahibi | <ad veya [BİLİNMİYOR]> |
| Tanecik / varlık | ... |
| Geçerlilik başlangıcı | <tarih veya [TBD]> |

## Tanım
Düz dille: ...
```sql
-- sözde SQL
SELECT ... FROM ... WHERE ... GROUP BY ...
```

## Filtreler ve Hariç Tutmalar
- ...

## Zaman Mantığı
- Kullanılan zaman damgası: ... | Saat dilimi: ... | Pencere: ... | Geç veri: ...

## Uç Durumlar
| Durum | Ele alınışı |
|---|---|

## Kaynaklar ve Soy Ağacı
- ...

## Mutabakat (çelişen tanımlar varsa)
| Konu | Tanım A | Tanım B | Sayıya etkisi |
|---|---|---|---|

## Yorumlama Notları
- Koruyucu metrikler: ... | Mevsimsellik: ... | Manipülasyon riski: ...
````

## Kalite kontrol listesi
- [ ] İki analist tanımı bağımsız uygulayıp aynı sayıyı bulabilir.
- [ ] Pay ve payda aynı popülasyonu ve zaman penceresini kullanıyor.
- [ ] Saat dilimi, dönem sınırları ve geç veri ele alınışı belirtildi.
- [ ] Her uç durumun ele alınışı yazıldı.
- [ ] Sahip ve sürüm belirlendi; bilinmeyenler tahmin edilmedi, `[TBD]` olarak işaretlendi.

## Sık yapılan hatalar
- Aktivite tanımı olmadan "aktif" demek. Sayılan olayları ve geriye bakış penceresini adlandır.
- Pay ve paydada olay tarihi ile kayıt tarihini karıştırmak.
- Tanımı sessizce değiştirmek. Sürümle ve geçmiş grafiklere not düş.

## Örnek
Girdi: "'Aktif müşteri'yi tanımla; finans ödeme yapan hesapları, ürün giriş yapan kullanıcıları sayıyor."

Çıktıdan bir bölüm:
- Amaç: Elde tutma kararları için etkileşimdeki ödeme yapan tabanın büyüklüğü.
- Tanım: Ayın son günü aktif ücretli aboneliği olan VE son 28 günde en az bir nitelikli ürün olayı bulunan tekil müşteri hesapları.
- Mutabakat: Finansın sayısı ödeme yapan ama pasif hesapları içerdiği için yüksek; ürünün sayısı ücretsiz kullanıcıları içeriyor.
- Uç durum: Ay içinde birleşen hesaplar, yaşayan hesap kimliği altında bir kez sayılır.
