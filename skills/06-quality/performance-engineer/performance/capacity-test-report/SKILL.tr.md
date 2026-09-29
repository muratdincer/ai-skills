---
description: Kademeli yük veya stres testi sonuçlarından SLO'lar içinde sürdürülebilir maksimum yükü belirleyen, sınırlayıcı kaynağı tespit eden, mevcut ve tahmini zirvelere göre payı hesaplayan, ölçekleme davranışını ve sınırlarını açıklayan ve tetikleyicileriyle kapasite aksiyonları öneren bir kapasite raporu yazar. Kapasite, stres veya ölçeklenebilirlik testlerinden sonra, yönetim sistemin ne kadar büyümeyi kaldırabileceğini sorduğunda ya da altyapı boyutlandırması ve ölçekleme sınırlarının test kanıtıyla gerekçelendirilmesi gerektiğinde kullanılır.
related: load-test-analysis, performance-test-plan, capacity-planning, scalability-review, finops-review
prompt: Arama servisinde kırılana kadar kademeli yük testi koştuk. Bir kapasite raporu yaz: gelecek yılın tahminine göre ne kadar payımız var?
---

# Kapasite Raporu

## Amaç
Sistemin SLO'larını karşılarken ne kadar yükü sürdürebildiğini, önce hangi kaynağın tükendiğini ve mevcut ve tahmini talebe göre ne kadar pay kaldığını kanıtla ortaya koymak; böylece ölçekleme ve yatırım kararları, kullanıcılar sınırı hissetmeden alınır.

## Ne zaman kullanılır
- Sistemin sınırlarını bulmak için kademeli, stres veya ölçeklenebilirlik testi koşulduysa.
- Paydaşlar sistemin tahmini büyümeyi, bir kampanyayı veya yeni bir müşteriyi (tenant) kaldırıp kaldıramayacağını soruyorsa.
- Altyapı boyutlandırması, otomatik ölçekleme sınırları veya ayrılmış kapasite gerekçelendirilecekse.

## Ne zaman kullanılmaz
- Tek bir test koşumu için geçti/kaldı yorumu gerekiyorsa `load-test-analysis` kullanılır.
- Test sonuçları yerine üretim telemetrisinden uzun vadeli kapasite planlaması gerekiyorsa `capacity-planning` kullanılır.
- Test henüz tasarlanmadıysa `performance-test-plan` kullanılır.

## Girdiler
Zorunlu:
- Artan yük seviyelerindeki test sonuçları (kademe başına verim, gecikme yüzdelikleri, hatalar) ve "sürdürülebilir"i değerlendirmek için SLO veya kabul kriterleri.

İsteğe bağlı, kaliteyi artırır:
- Kademe başına kaynak metrikleri (CPU, bellek, havuzlar, veritabanı, kuyruklar), instance sayıları ve otomatik ölçekleme yapılandırması.
- Mevcut üretim zirvesi ve büyüme tahmini, ortamın üretimden farkları, instance başına maliyet.

Yük kademesi başına sonuçlar yoksa iste. SLO verilmemişse sor; o olmadan "sürdürülebilir" tanımlanamaz. Kullanıcı veremiyorsa `[VARSAYIM]` olarak işaretlenmiş önerilen bir eşik kullan.

## Süreç
1. "Sürdürülebilir"i tanımla: tüm SLO kriterlerinin (ör. p95 gecikme, hata oranı) kademe süresinin tamamında sabit durumda sağlandığı ve kötüleşen bir trendin olmadığı en yüksek yük.
2. Her yük kademesini sonuçlarıyla tablola ve tanımı karşılayan son kademeyi işaretle; bu sürdürülebilir maksimum yüktür (SMY). Kırılma noktasını ayrıca not et.
3. SMY'deki sınırlayıcı kaynağı belirle: ilk doyan kaynak (CPU, bellek, bağlantı veya thread havuzları, veritabanı, aşağı akış bağımlılığı, rate limit). Metriklerle destekle; aksi halde `[VARSAYIM]` olarak etiketle.
4. Ölçekleme davranışını açıkla: verim instance sayısıyla doğrusal artıyor mu; nerede duruyor (paylaşılan veritabanı, kilitler, dış sınırlar); otomatik ölçeklemenin tepki süresi ile ani yükün yükselme süresi.
5. Üretimden ortam farklarına (instance boyutu, sayısı, veri hacmi) göre düzelt ve ortaya çıkan belirsizliği belirt; kanıtın ötesinde doğrusal ekstrapolasyon yapma.
6. Payı hesapla: (SMY − mevcut zirve) / mevcut zirve ve aynı hesabı tahmini zirveler için yap; büyüme oranı verildiyse tükenmeye kalan süre olarak da ifade et.
7. Bir güvenlik marjı ve alarm eşikleri belirle (ör. zirve SMY'nin belirtilen bir oranına ulaştığında harekete geç) ve gerekçesini yaz.
8. Kapasite aksiyonları öner: yükseltilecek yatay ölçekleme sınırları, kaldırılacak darboğaz, yapılandırma değişiklikleri, maliyetle ilgili seçenekler; her birinin beklenen yeni SMY'si doğrulanacak bir hipotez olarak yazılsın.
9. Varsayımları, sınırlamaları ve açık soruları listele.
10. Hedef devam ediyorsa sürekli tahmin için `capacity-planning`, sınır mimari kaynaklıysa `scalability-review`, ölçekleme seçeneklerinin maliyet tarafı için `finops-review` öner.

## Çıktı formatı
```markdown
# Kapasite Raporu: <sistem / test tarihi>
Sürdürülebilir = <SLO değerleriyle tanım>
Sürdürülebilir maksimum yük: <değer> · Sınırlayıcı kaynak: <kaynak> · Kırılma noktası: <değer>

## Yük Kademesi Başına Sonuçlar
| Kademe | Hedef yük | Ulaşılan | p95 | p99 | Hata oranı | Önemli kaynak kullanımı | SLO içinde mi? |
|---|---|---|---|---|---|---|---|

## Pay
| Referans | Yük | SMY'ye göre pay | Tükenmeye kalan süre |
|---|---|---|---|
| Mevcut zirve | | | |
| Tahmini zirve | | | |

## Ölçekleme Davranışı
## Ortam Farkları ve Güven
## Öneriler ve Alarm Eşikleri
| Aksiyon | Beklenen etki (hipotez) | Tetikleyici / eşik | Doğrulama |
|---|---|---|---|
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] SMY belirtilmeden önce "sürdürülebilir" açık SLO değerleriyle tanımlandı.
- [ ] SMY ölçülmüş bir kademeden geliyor; test edilen yükün ötesine interpolasyon veya ekstrapolasyon yok.
- [ ] Sınırlayıcı kaynak metriklerle destekleniyor ya da `[VARSAYIM]` olarak etiketli.
- [ ] Pay hem mevcut hem tahmini zirveye göre, formülü gösterilerek hesaplandı.
- [ ] Ortam farkları ve bunun getirdiği güven düzeyi belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kırılma noktasını kapasite olarak raporlamak. Kapasite, SLO'yu hâlâ karşılayan en yüksek yüktür ve genellikle kırılma noktasının epey altındadır.
- Doğrusal ekstrapolasyon ("2 instance 200 istek/sn kaldırıyorsa 10 instance 1000 kaldırır"). Paylaşılan kaynaklar doğrusal ölçeklemeyi durdurur; test et veya varsayım olarak belirt.
- Otomatik ölçekleme gecikmesini yok saymak: ani yük yeni instance'ların açılmasından hızlı yükseliyorsa ölçekleme sonrası kapasite işe yaramaz.

## Örnek
Girdi: Kademeler 100/150/200/250/300 istek/sn; p95 SLO 500 ms; p95 = 180/220/310/480/1900 ms; hatalar %0/0/0,1/0,3/4; 250'de DB CPU %85; mevcut zirve 160 istek/sn; tahmin gelecek yıl +%40.

Çıktıdan bir bölüm:
- SMY: 250 istek/sn (SLO içindeki son kademe). Kırılma noktası: 300 istek/sn. Sınırlayıcı kaynak: veritabanı CPU'su (250'de %85) `[bekleme istatistikleriyle teyit et]`.
| Referans | Yük | SMY'ye göre pay |
|---|---|---|
| Mevcut zirve | 160 istek/sn | (250 − 160) / 160 = %56 |
| Tahmini zirve (+%40) | 224 istek/sn | (250 − 224) / 224 = %12 |
- Öneri: zirve 200 istek/sn'yi (SMY'nin %80'i) aştığında alarm üret; tahmini zirveden önce veritabanı yükünü azalt.
