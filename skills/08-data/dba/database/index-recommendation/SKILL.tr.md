---
description: "Bir tablo veya veritabanı için gerçek iş yükünden indeks önerir: sorguları erişim desenine göre gruplar, anahtar sütun sırasını, dahil edilen sütunları, filtreli/kısmi indeksleri tasarlar, örtüşen indeksleri birleştirir ve kullanılmayanları kaldırır; okuma kazancını yazma yükü, depolama ve bakım maliyetine karşı tartar. Yeni bir şema veya özellik için indeks tasarlanırken, fazla ya da eksik indeksli bir tablo gözden geçirilirken veya motorun eksik indeks önerileri değerlendirilirken kullanılır."
related: "query-optimization, database-health-check, schema-migration-plan, database-schema-design, capacity-planning"
prompt: "orders tablomuzda 14 indeks var, insert'ler yavaşlıyor ve bazı raporlar hâlâ tarama yapıyor. En pahalı 20 sorgu ve indeks kullanım istatistikleri ekte; bir indeks seti öner."
---

# İndeks Önerisi

## Amaç
Bir iş yükü için bilinçli bir indeks seti üretmek: her indeks hizmet ettiği sorgularla gerekçelendirilir, örtüşmeler birleştirilir, ölü indeksler kaldırılır ve yazma tarafı maliyeti belirtilir. Sonuç, her şikâyet için bir indeks yerine daha az ama daha iyi indekstir.

## Ne zaman kullanılır
- Yeni bir tablo, şema veya özellik bilinen erişim desenlerinden ilk indekslerine ihtiyaç duyuyorsa.
- Bir tabloda çok sayıda indeks, yavaş yazma veya büyük depolama varken okumalar hâlâ tarama yapıyorsa.
- Motorun eksik indeks önerileri veya bir danışman raporu uygulanmadan önce değerlendirilecekse.

## Ne zaman kullanılmaz
- Belirli bir sorgu yavaşsa ve planı elde varsa `query-optimization` kullanılır.
- Tablo yapısının kendisi (anahtarlar, normalizasyon, bölümleme) tasarlanıyorsa `database-schema-design` kullanılır.
- Seçilen indeks değişiklikleri büyük ve canlı bir tabloya güvenle uygulanacaksa `schema-migration-plan` kullanılır.

## Girdiler
Zorunlu:
- Veritabanı motoru ve mevcut indeksleriyle tablo tanımları.
- İş yükü: toplam maliyet veya sıklığa göre en önemli sorgular (metin ya da tarif edilmiş koşullar, join'ler, sıralamalar) ve DML deseni (insert/update/delete oranları).

İsteğe bağlı:
- İndeks kullanım istatistikleri (seek, scan, lookup, update), tablo boyutları ve büyümesi, eksik indeks önerileri, gecikme hedefleri, bakım pencereleri, replikasyon yapısı.

İş yükü bilinmiyorsa en önemli sorguları iste; yalnızca şemadan indeks tasarlama, ancak `[VARSAYIM]` ile işaretli başlangıç noktaları olarak sun.

## Süreç
1. İş yükünü profille: sorguları sıklık, maliyet ve gecikme hedefiyle listele; tabloyu okuma yoğun, yazma yoğun veya karma olarak işaretle. Çıkarılan desenleri `[VARSAYIM]` ile işaretle.
2. Her sorgu için erişim desenini çıkar: eşitlik koşulları, aralık koşulları, join sütunları, `ORDER BY`/`GROUP BY`, seçilen sütunlar ve her koşulun seçiciliği.
3. Baştaki eşitlik sütunlarını paylaşan sorguları grupla; her sorgu için değil her grup için bir indeks tasarla.
4. Anahtar sütunları sırala: önce eşitlik sütunları (en seçici veya en çok paylaşılan önce), sonra aralık veya sıralama sütunu; motor destekliyorsa yalnızca çıktı için gereken sütunları sıcak yollarda lookup'ı önlemek üzere dahil edilen (anahtar dışı) sütun olarak ekle.
5. Gerekçesi varsa özel biçimleri değerlendir: sıcak alt kümeler için filtreli/kısmi indeksler (ör. açık siparişler), iş anahtarlarını da zorlayan unique indeksler, foreign key kontrollerini ve cascade'leri destekleyen bileşik indeksler, analitik veya arama desenleri için motora özgü tipler (full-text, spatial, inverted, columnar).
6. Mevcut indeksleri gözden geçir: kullanılmayanları (ay sonu işleri dahil temsili bir dönem boyunca okuma yok), mükerrerleri ve sol önek açısından gereksiz olanları işaretle; birleştirme öner.
7. Nihai setin yazma tarafı maliyetini tahmin et: insert/update başına ek yazmalar, kilit ve log hacmi, sıralı olmayan anahtarlarda sayfa bölünmeleri, depolama boyutu ve bakım/rebuild süresi.
8. Motor önerilerini eleştirel değerlendir: tek tek uygulamak yerine gruplanmış tasarıma kat; yazma yoğun tablolarda nadir sorgulara hizmet edenleri reddet.
9. Yayılımı tanımla: önce oluştur sonra sil, destekleniyorsa online oluşturma, mümkünse silmeden önce devre dışı bırakma veya görünmez yapma, hedef sorguların ve yazma gecikmesinin izlenmesi.
10. Çıktı şablonunu doldur. Hedef devam ediyorsa değişiklikleri uygulamak için `schema-migration-plan`, sonrasında hâlâ yavaş kalan sorgular için `query-optimization` veya depolama büyümesi önemliyse `capacity-planning` öner.

## Çıktı formatı
```markdown
# İndeks Önerisi: <tablo/şema>
Motor: <...> | İş yükü profili: <okuma yoğun/yazma yoğun/karma> | İstatistik dönemi: <...>

## İş Yükü Özeti
| Sorgu / desen | Sıklık | Koşullar (eşitlik / aralık) | Sıralama / gruplama | Mevcut erişim |
|---|---|---|---|---|

## Önerilen İndeks Seti
| Aksiyon (oluştur/değiştir/sil/koru) | İndeks | Anahtar sütunlar | Dahil edilen | Filtre | Hizmet ettiği sorgular | Yazma/depolama maliyeti |
|---|---|---|---|---|---|---|

## Kaldırılan veya Birleştirilen İndeksler
- <indeks> – <neden: şu tarihten beri kullanılmıyor / şunun mükerreri / şunun öneki>

## Yayılım ve İzleme
1. <adım> – online mı? – doğrulama
İzleme: <hedef sorgular, yazma gecikmesi, N gün sonra indeks kullanımı>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Önerilen her indeks hizmet ettiği sorguları listeliyor; hiçbir şeye hizmet etmeyen indeks yok.
- [ ] Sütun sırası önce eşitlik, sonra aralık/sıralama kuralına uyuyor ve gruplanmış desenlerle örtüşüyor.
- [ ] Örtüşen, mükerrer ve kullanılmayan indeksler ele alınmış; kullanım dönemi periyodik işlere karşı kontrol edilmiş.
- [ ] Nihai set için yazma yükü ve depolama maliyeti belirtilmiş.
- [ ] Yayılım silmeden önce oluşturuyor ve değişiklik sonrası izlemeyi belirtiyor.
- [ ] Varsayılan iş yükü desenleri işaretli; kullanım rakamları uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Eksik indeks önerilerini tek tek uygulamak; bunlar büyük ölçüde örtüşür ve yazma maliyetini hesaba katmaz.
- Kullanım istatistikleri bir yeniden başlatmayla sıfırlanmış veya çeyreklik bir işe hizmet eden "kullanılmayan" bir indeksi silmek.
- Düşük seçicilikli sütunları (durum, bayraklar) tek başına indekslemek; bunun yerine seçici bir sütunla birleştir veya filtreli indeks kullan.

## Örnek
Girdi: "orders: 14 indeks, saniyede 3 bin insert, status üzerinde saniyede 40 update; raporlar customer_id + created_at aralığıyla filtreliyor, operasyon ekranı depoya göre açık siparişleri gösteriyor."

Çıktıdan bir bölüm:
- `(customer_id, created_at) INCLUDE (status, total)` oluştur: 6 rapor sorgusuna hizmet eder; `ix_customer` ve `ix_customer_date`'in yerini alır (sol önek mükerrerleri).
- Filtreli `(warehouse_id, created_at) WHERE status = 'OPEN'` oluştur: operasyon ekranına hizmet eder; açık siparişler ~%2 olduğu için küçüktür `[VARSAYIM: oranı doğrula]`.
- Ay sonu dahil 35 gün boyunca sıfır okuması olan 4 indeksi sil; sonuç 9 indeks ve insert başına daha az yazma.
