---
description: "Başarısız olan veya sessizce yanlış veri üreten bir veri hattı çalışmasını analiz eder: zaman çizelgesini çıkarır, kök nedeni (kaynak, kod, altyapı, veri, bağımlılık) ayırır, bölümler, tablolar ve tüketiciler üzerindeki veri etkisini ölçer, güvenli ve idempotent bir geriye dönük yükleme ile önleme planı üretir. Bir yükleme hata verdiğinde, mükerrer, eksik veya geç veri ürettiğinde, bir kalite kontrolü tetiklendiğinde ya da bir tüketici rakamların tutmadığını bildirdiğinde kullanılır."
related: "incremental-load-design, pipeline-spec, data-lineage-doc, data-quality-rules, postmortem"
prompt: "Dün geceki sipariş yüklemesi başarılı görünüyor ama bugünkü ciro panosu %12 düşük. Çalışma logları ve satır sayıları ekte; ne olduğunu ve veriyi nasıl düzelteceğimizi bul."
---

# Veri Hattı Hata Analizi

## Amaç
Bir veri hattı hatasının gerçek kök nedenini bulmak, tam olarak hangi verinin yanlış veya eksik olduğunu ve kimin tükettiğini belirtmek ve durumu kötüleştiremeyecek bir geriye dönük yüklemeyle (backfill) onarmak. Veri olayı, iş yeşile döndüğünde değil veri yeniden doğru olduğunda kapanır.

## Ne zaman kullanılır
- Bir veri hattı çalışması hata verdi, takıldı veya yeniden denendi ve hedefin durumu belirsiz.
- Çalışma "başarılı" oldu ama mükerrer, eksik, bayat veya yanlış değerli veri üretti.
- Bir veri kalitesi kontrolü veya mutabakat tetiklendi ya da bir tüketici rakamların kaydığını bildirdi.

## Ne zaman kullanılmaz
- Başarısız olan bir veri hattı değil CI/CD derleme veya dağıtım pipeline'ı ise `pipeline-failure-triage` kullanılır.
- Yükleme mantığının kendisi (watermark, CDC, merge) yeniden tasarlanacaksa `incremental-load-design` kullanılır.
- Analizden sonra geniş bir kitle için zaman çizelgesi ve aksiyonlarıyla resmi bir olay değerlendirmesi gerekiyorsa `postmortem` kullanılır.

## Girdiler
Zorunlu:
- Belirti (hata mesajı, başarısız kontrol veya gözlenen yanlış rakam) ve etkilenen veri hattı/tablo.
- Çalışma kanıtı: en azından başarısız çalışmanın ve son sağlıklı çalışmanın logları veya çalışma geçmişi.

İsteğe bağlı:
- Bölüm bazında satır sayıları/checksum'lar, son kod/yapılandırma/şema değişiklikleri, kaynak sistem duyuruları, alt akış tüketicilerine köken bilgisi, veri hattı tanımı.

Hiç çalışma kanıtı yoksa iste; kök nedeni yalnızca belirtiden tahmin etme.

## Süreç
1. Belirtiyi kesin ifade et: ne yanlış (hata, mükerrer, eksik, geç, yanlış değer), hangi tablo/bölümlerde, ilk ne zaman ve kim tarafından fark edildi. Gözlenen olguları aktarılanlardan ayır, çıkarımları `[VARSAYIM]` ile işaretle.
2. Hatanın tamamını ve çalışma zaman çizelgesini oku: başlangıç/bitiş, yeniden denemeler, adım süreleri, adım başına okunan/yazılan satırlar; son sağlıklı çalışmayla karşılaştır. Rakamların ilk ayrıştığı noktayı tam olarak belirle.
3. Son sağlıklı çalışmadan bu yana neyin değiştiğini listele: kod, yapılandırma, bağımlılık sürümleri, kaynak şema veya hacmi, kimlik bilgileri, altyapı, üst akış zamanlaması, takvim etkileri (ay sonu, yaz saati, tatil).
4. Hata sınıfları boyunca hipotez kur: kaynak (kesinti, geç teslim, şema kayması, geriye tarihli değişiklikler, kalıcı silmeler), mantık (join çoğalması, filtre, saat dilimi, null işleme), yükleme mekaniği (commit olmadan ilerleyen watermark, idempotent olmayan yeniden deneme, kısmi üzerine yazma), altyapı (zaman aşımı, bellek yetersizliği, yetkiler), bağımlılık (üst akış işi geç veya eksik veriyle çalıştı).
5. Hipotezleri somut sorgularla (bölüm ve anahtar bazında sayımlar, mükerrer anahtar kontrolleri, min/max zaman damgaları, kaynak-hedef farkları) her seferinde tek değişkenle test et. Her hipotezi kanıtla doğrula veya ele. Kök neden doğrulanmadan düzeltme önerme; üç düzeltme başarısız olursa tasarımı sorgula.
6. Veri etkisini ölç: etkilenen tablolar, bölümler/zaman aralığı, satır sayıları, kayan temel metrikler ve köken üzerinden kötü veriyi zaten okumuş alt akış tüketicileri (raporlar, modeller, dışa aktarımlar, reverse ETL).
7. Onarımı tasarla: veri hattı veriyi bozmaya devam ediyorsa durdur veya beklet; ardından açık aralık, sıra, yeniden çalıştırılacak alt akış bağımlılıkları, kaynak yük sınırları ve tek bölümde deneme çalışması (dry run) içeren idempotent bir backfill (bölüm üzerine yazma veya anahtarlı merge) planla.
8. Doğrulamayı tanımla: backfill sonrası geçmesi gereken mutabakat sorguları ve eşikler (sayılar, toplamlar, mükerrer anahtarlar, tazelik) ve tüketicilerle birlikte kimin onay vereceği.
9. Önlemeyi tanımla: bu hatayı yakalayacak veya önleyecek eksik test, kalite kuralı, alarm veya tasarım değişikliği; her biri için bir sorumlu.
10. Tüketici bildirimini taslakla: ne yanlıştı, hangi zaman aralığı, kötü veri kararlarda veya dış çıktılarda kullanıldı mı, ne zaman düzeltilecek. Örneklerde görünen kişisel verileri maskele.
11. Çıktı şablonunu doldur. Hedef devam ediyorsa resmi değerlendirme için `postmortem`, yeni kontroller için `data-quality-rules` veya neden yükleme mekanizmasıysa `incremental-load-design` öner.

## Çıktı formatı
```markdown
# Veri Hattı Hata Analizi: <veri hattı> – <tarih>
Durum: <inceleniyor / kök neden doğrulandı / onarıldı> | Önem: <...>

## Belirti
<ne, nerede, ne zamandan beri, kim fark etti>

## Zaman Çizelgesi
| Zaman | Olay | Kanıt |
|---|---|---|

## Hipotezler
| # | Hipotez | Test | Sonuç (doğrulandı / elendi / açık) |
|---|---|---|---|

## Kök Neden
<neden> – <kanıt> | Katkıda bulunan etkenler: ...

## Veri Etkisi
| Tablo | Bölümler / aralık | Etkilenen satır | Etkilenen tüketiciler |
|---|---|---|---|

## Onarım ve Backfill
1. <adım, aralık, mod, dry run>
Doğrulama: <sorgu, eşik>

## Önleme
| Aksiyon | Tür (test/kural/alarm/tasarım) | Sorumlu |
|---|---|---|

## Tüketici Bildirimi
<kısa mesaj>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Kök neden yalnızca zamanlama tesadüfüne değil kanıta dayanıyor.
- [ ] Etki, kesin tabloları, aralıkları ve etkilenen alt akış tüketicilerini listeliyor.
- [ ] Backfill idempotent, kapsamı belirli, alt akış yeniden çalıştırmalarıyla sıralı ve bir dry run içeriyor.
- [ ] Doğrulama sorguları ve geçme eşikleri tanımlı.
- [ ] En az bir önleme aksiyonu bu hatayı daha erken yakalardı.
- [ ] Çıkarımlar işaretli; hiçbir şey (sayılar, tarihler, sorumlular) uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İşi yeniden çalıştırıp düzeldi saymak: idempotent olmayan bir yeniden deneme satırları ikiye katlar, yeşil bir çalışma da başarısız çalışmada kaybolan satırları gizler.
- Neden şimdi olduğunu (hacim ikiye katlandı, indeks eksik, üst akış geç kaldı) sormadan yakın nedende ("zaman aşımı") durmak.
- Tabloyu düzeltip kötü veriyi zaten tüketmiş alt akış özetlerini, dışa aktarımları ve önbellekleri unutmak.

## Örnek
Girdi: "Sipariş yüklemesi 02:10'da başarılı bitti, bugün ciro panosu %12 düşük. Yazılan satır 1,08M, normalde 1,23M."

Çıktıdan bir bölüm:
- Hipotez 2 (doğrulandı): kaynak replika 40 dk gecikmeliydi; çekme üst sınırı `now()` olduğundan geç commit edilen siparişler bir sonraki watermark'ın gerisinde kaldı `[VARSAYIM: 01:30'daki replika gecikme metriğini doğrula]`.
- Etki: `fact_orders` 2026-03-14 bölümünde ~150 bin satır eksik; `agg_daily_revenue` ve finans dışa aktarımı bu veriyi tüketti.
- Onarım: 2026-03-14 bölümünü kaynaktan üzerine yaz, ardından o gün için `agg_daily_revenue`'yu yeniden çalıştır; sayı ve sum(amount) kaynağa göre %0,1 içinde olmalı.
- Önleme: sabit üst sınır = çalışma başındaki kaynak commit konumu; çekmeden önce replika gecikmesi için tazelik kontrolü.
