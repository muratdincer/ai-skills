---
description: "Yavaş bir SQL sorgusunu metni, çalışma planı ve istatistikleri üzerinden teşhis eder; baskın maliyeti (hatalı kardinalite tahmini, yanlış join sırası veya yöntemi, taramalar, diske taşmalar, sargable olmayan koşullar, parametre hassasiyeti, bloklanma) bulur ve beklenen etki ile doğrulama yöntemiyle sıralanmış yeniden yazım, indeks veya istatistik önerileri sunar. Bir sorgu, rapor veya endpoint yavaşsa, bir sürüm ya da veri büyümesi sonrası plan kötüleştiyse veya biri çalışma planını paylaşıp neden yavaş olduğunu sorduğunda kullanılır."
related: "index-recommendation, database-health-check, sql-query-writing, performance-optimization, schema-migration-plan"
prompt: "Bu sipariş arama sorgusu geçen haftaki veri aktarımından sonra 200 ms'den 9 saniyeye çıktı. Sorgu ve gerçek çalışma planı ekte; neden yavaş ve nasıl düzeltiriz?"
---

# Yavaş Sorgu İyileştirme

## Amaç
Belirli bir sorguyu, indeks tahmin ederek değil çalışma planında görünen gerçek nedeni düzelterek hızlı ve öngörülebilir biçimde hızlı hale getirmek. Her öneri beklenen etkisini, iş yükünün geri kalanına maliyetini ve işe yaradığının nasıl kanıtlanacağını içerir.

## Ne zaman kullanılır
- Bilinen bir sorgu, rapor veya API çağrısı hedef süresinden yavaşsa.
- Bir dağıtım, istatistik yenileme, parametre değişikliği veya veri büyümesi sonrası plan kötüleştiyse.
- Elde bir çalışma planı var ve soru "bu neden yavaş?" ise.

## Ne zaman kullanılmaz
- Veritabanının veya sunucunun tamamı yavaşsa ve sorumlu sorgu bilinmiyorsa `database-health-check` kullanılır.
- İndeksler tek bir sorgu için değil tüm iş yükü için tasarlanacaksa `index-recommendation` kullanılır.
- Sorgu henüz yok ve yazılması gerekiyorsa `sql-query-writing` kullanılır.

## Girdiler
Zorunlu:
- Sorgu metni (temsili parametre değerleriyle) ve veritabanı motoru.
- Gerçek çalışma planı (çalışma anı satır sayılarıyla) ya da o yoksa tahmini plan ve süre bilgisi.

İsteğe bağlı:
- Tablo boyutları, mevcut indeksler, istatistiklerin yaşı, çalışmaya ait bekleme/IO/CPU metrikleri, hedef gecikme, çağrı sıklığı, son değişiklikler.

Yalnızca tahmini plan varsa hangi sonuçlar için gerçek plan gerektiğini belirt. Satır sayısı uydurma.

## Süreç
1. Başlangıç durumunu belirle: motor, mevcut süre, hedef süre, çağrı sıklığı, her zaman mı yoksa yalnızca bazı parametre değerlerinde mi yavaş olduğu. Çıkarımları `[VARSAYIM]` ile işaretle.
2. Planı yukarıdan aşağıya değil en pahalı operatörlerden başlayarak oku: en yüksek gerçek süre, satır veya IO; geçici alana taşmalar (spill); büyük girdiler üzerindeki sort ve hash'ler; büyük dış girdili nested loop'lar; çok sayıda tekrarlanan key/row lookup'lar.
3. Her operatörde tahmini ve gerçek satırları karşılaştır. Büyüklük mertebesinde bir fark genellikle kök nedendir; bunu eski veya eksik istatistiklere, ilişkili koşullara, çarpıklığa (skew), sütunlar üzerindeki fonksiyonlara, örtük dönüşümlere, tablo değişkenlerine veya parameter sniffing'e kadar izle.
4. Koşulların sargable olup olmadığını kontrol et: indeksli sütunlar üzerinde fonksiyon veya cast, baştaki joker karakterler, sütunlar arası OR, uyumsuz veri tipleri veya collation'lar, null olabilen sütunlarla `NOT IN`.
5. Sorgunun şeklini kontrol et: gereksiz sütunlar (kapsayan indeksi engelleyen `SELECT *`), satır satır çalışan skaler fonksiyonlar, join veya `EXISTS` olabilecek ilişkili alt sorgular, join çoğalmasını gizleyen `DISTINCT`, büyük offset'le sayfalama, işi geç aşamaya iten eksik filtreler.
6. Sorgu maliyetini ortamdan ayır: bloklanma, kilit beklemeleri, bellek tahsisi beklemeleri, soğuk önbellek, paralellik dengesizliği. Beklemeler baskınsa çözüm sorgu metninde değildir.
7. Düzeltmeleri etki ve riske göre sırala: istatistik yenileme veya genişletilmiş istatistik, koşul yeniden yazımı, sorgunun yeniden yapılandırılması, yeni veya değiştirilmiş indeks (yazma ve depolama maliyetiyle), son çare olarak planı sabitleyen seçenekler. Optimizer'ın neden farklı seçtiğini belirtmeden hint önerme.
8. Her düzeltme için beklenen plan değişikliğini (ör. tarama yerine seek, 200 satır üzerinde hash join yerine nested loop) ve diğer sorgular ile DML üzerindeki yan etkileri belirt.
9. Doğrulamayı tanımla: temsili ve uç parametre değerlerinde süreyi, mantıksal okumaları ve yeni planı karşılaştır; sonuçların birebir aynı olduğunu kontrol et.
10. Çıktı şablonunu doldur. Hedef devam ediyorsa iş yükü genelinde indeks tasarımı için `index-recommendation`, indeks veya şema değişikliklerini güvenle yaymak için `schema-migration-plan` ya da beklemeler baskınsa `database-health-check` öner.

## Çıktı formatı
```markdown
# Sorgu İyileştirme: <sorgu adı/amacı>
Motor: <...> | Mevcut: <süre, okuma> | Hedef: <...> | Sıklık: <...>

## Teşhis
- Baskın maliyet: <operatör, süre/IO yüzdesi>
- Tahmini ve gerçek: <operatör: tahmini X / gerçek Y> → neden: <...>
- Diğer bulgular: <sargable olmayan koşul, spill, lookup, bekleme>

## Öneriler
| # | Değişiklik | Neden (kanıt) | Beklenen etki | Maliyet / risk | Öncelik |
|---|---|---|---|---|---|

## Yeniden Yazılmış Sorgu (varsa)
<SQL>

## Doğrulama
- Test edilen parametreler: <tipik, uç>
- Karşılaştır: süre, mantıksal okuma, plan şekli, sonuçların aynılığı

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Teşhis genel tavsiyelere değil belirli plan operatörlerine ve rakamlara işaret ediyor.
- [ ] Tahmini-gerçek satır farkları bir nedenle açıklanmış.
- [ ] Her indeks önerisi yazma ve depolama maliyetini ve mevcut indekslerle örtüşmesini belirtiyor.
- [ ] Yeniden yazımlar sonuç anlamını (null'lar, mükerrerler, sıralama) koruyor.
- [ ] Doğrulama tipik ve uç parametre değerlerini kapsıyor.
- [ ] Desteklenmeyen iddialar işaretli; satır sayısı veya süre uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her yavaş sorgu için bir indeks eklemek: yazma yükü ve plan kararsızlığı artar; önce mevcut bir indeksin genişletilip genişletilemeyeceğine bak.
- Yalnızca hızlı çalışan parametre değeriyle test etmek; parametreye hassas planlar çarpık değerlerle de denenmelidir.
- Veri değiştikçe sessizce yanlışlaşan hint veya zorlanmış planlarla çözmek; önce tahminleri düzelt.

## Örnek
Girdi: "Sipariş arama aktarımdan sonra 200 ms → 9 sn. Plan: orders.created_at üzerinde index seek, tahmini 120 satır, gerçek 2,4M; order_lines'a nested loop."

Çıktıdan bir bölüm:
- Baskın maliyet: order_lines'a nested loop 2,4M kez çalışmış (okumaların ≈%85'i).
- Neden: `orders.created_at` istatistikleri aktarımdan eski; artan anahtar aralığı neredeyse boş tahmin ediliyor `[VARSAYIM: son istatistik güncelleme zamanını doğrula]`.
- Öneri 1: `orders` istatistiklerini güncelle (düşük risk); beklenen: hash join, ~50 kat daha az okuma. Öneri 2: lookup'ları kaldırmak için `created_at` indeksine `status` sütununu ekle; maliyet: yazma yoğun tabloda daha geniş indeks.
