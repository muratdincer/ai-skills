---
description: "Toplu (batch) veya akış (streaming) bir veri hattını uçtan uca tanımlar: kaynaklar ve çekme, zamanlama veya tetikleyici, bağımlılıklar, dönüşüm adımları, hedefler ve yazma modu, yükleme stratejisi, veri kalitesi kapıları, SLA'lar, hata yönetimi, geriye dönük yükleme, gözlemlenebilirlik, güvenlik ve sahiplik. Bir veri hattı kurulmadan veya değiştirilmeden önce, iş bir mühendise devredilirken ya da bir ETL/ELT veya streaming işinin tasarlanması veya belgelenmesi istendiğinde kullanılır."
related: "source-to-target-mapping, incremental-load-design, data-quality-rules, data-contract, runbook"
prompt: "ERP veritabanından günlük siparişleri finans martı için veri ambarına yükleyen veri hattının tanımını yaz."
---

# Veri Hattı Tanımlama

## Amaç
Uygulayıcılara ve operasyon ekibine, veri hattının neyi, ne zaman, nasıl, hangi garantilerle taşıdığını ve hata durumunda ne olacağını anlatan tek ve net bir tanım vermek. Böylece hat güvenle kurulur, gözden geçirilir, işletilir ve değiştirilir.

## Ne zaman kullanılır
- Yeni bir alım veya dönüşüm hattı kurulmak üzereyken.
- Mevcut bir veri hattı belgesizse ve operasyon ekibini sürekli şaşırtıyorsa.
- Bir veri hattı ekipler arasında veya bir tedarikçiye devrediliyorsa.

## Ne zaman kullanılmaz
- Yalnızca sütun düzeyinde dönüşüm mantığı gerekiyorsa `source-to-target-mapping` kullanılır.
- Yalnızca değişiklik yakalama ve watermark tasarımı sorgulanıyorsa `incremental-load-design` kullanılır.
- Uygulama kodunun CI/CD pipeline'ı kastediliyorsa `pipeline-design` kullanılır.

## Girdiler
Zorunlu:
- Kaynak(lar), hedef(ler) ve hattın karşıladığı tüketici ihtiyacı (hangi veri, kimin için, ne zamana kadar).

İsteğe bağlı:
- Hacimler ve büyüme, kaynak kısıtları (bakım pencereleri, yük sınırları), mevcut platform ve orkestrasyon standartları, eşlemeler, kalite beklentileri, hassasiyet sınıfı.

Tüketici ihtiyacı veya tazelik gereksinimi bilinmiyorsa sor; batch/streaming seçimi ve SLA buna bağlıdır.

## Süreç
1. Amacı ve tüketicileri belirt; tazelik gereksinimini ve tamamlanma son saatini kolaylığa göre değil tüketici ihtiyacından türet.
2. Her kaynağı tarif et: sistem, nesneler, erişim yöntemi (sorgu, CDC logu, API, dosya, olay topic'i), çalışma başına hacim, değişim deseni, kaynak tarafı kısıtlar ve sahip ekip.
3. İşleme modunu (batch, mikro-batch, streaming) ve tetikleyiciyi (zaman çizelgesi, üst akışın tamamlanması, dosya gelişi, olay) seç; üst ve alt akış bağımlılıklarını açıkça listele.
4. Dönüşümleri sıralı adımlar olarak tarif et (temizleme, uyumlama, tekilleştirme, join, toplama, zenginleştirme); sütun düzeyi mantık için eşleme dokümanına referans ver.
5. Hedefleri tanımla: nesne, katman, bölümleme, yazma modu (append, merge/upsert, bölüm üzerine yazma, SCD yönetimi) ve yeniden çalıştırmada idempotency garantisi.
6. Yükleme stratejisini tanımla: tam veya artımlı, değişiklik tespiti, geç ve sırasız gelen verinin ele alınışı, silmelerin iletimi.
7. Veri kalitesi kapılarını yerleştir: hangi kontrolün nerede çalıştığı ve hatanın yüklemeyi durdurduğu, karantinaya aldığı veya uyardığı.
8. Hata yönetimini tanımla: backoff'lu yeniden deneme politikası, hangi hataların yeniden denenebilir olduğu, kısmi hata davranışı, dead-letter veya karantina, alarm yolu ve eskalasyon.
9. Geriye dönük yükleme ve yeniden işlemeyi tanımla: bir tarih aralığının güvenle nasıl yeniden çalıştırılacağı, beklenen süre, kaynağa ve tüketicilere etkisi.
10. Gözlemlenebilirliği tanımla: çalışma metaverisi, giren/çıkan/reddedilen satır sayıları, gecikme, süre, maliyet göstergeleri ve SLA ihlalinde panolar veya alarmlar.
11. Güvenlik ve uyumu tanımla: kimlik bilgileri bir secret deposuyla yönetilir, en az yetki erişimi, kişisel veri maskeleme veya en aza indirme, gerektiğinde şifreleme ve veri yerleşimi.
12. Sahipliği, nöbeti, runbook bağlantısını ve açık soruları kaydet; teyit edilmemiş değerleri `[TBD]` veya `[VARSAYIM]` olarak işaretle. Hedef devam ediyorsa `source-to-target-mapping`, `incremental-load-design` veya `runbook` öner.

## Çıktı formatı
```markdown
# Veri Hattı Tanımı: <ad>
Sahip: <ekip> | Nöbet: <...> | Durum: <taslak/onaylı> | Sürüm: <...>

## Amaç ve Tüketiciler
<ne, kimin için> | Tazelik: <...> | Tamamlanma saati: <...>

## Kaynaklar
| Kaynak | Nesneler | Erişim | Hacim/çalışma | Değişim deseni | Kısıtlar | Sahip |
|---|---|---|---|---|---|---|

## Tetikleyici ve Bağımlılıklar
Mod: <batch/streaming> | Tetikleyici: <...> | Üst akış: <...> | Alt akış: <...>

## Dönüşümler
1. <adım> — eşleme <ref>

## Hedefler
| Hedef | Katman | Bölümleme | Yazma modu | Idempotency |
|---|---|---|---|---|

## Yükleme Stratejisi
<tam/artımlı, değişiklik tespiti, geç veri, silmeler>

## Kalite Kapıları
| Kontrol | Aşama | Hata durumunda |
|---|---|---|

## Hata Yönetimi ve Geriye Dönük Yükleme
<yeniden denemeler, karantina, alarm, yeniden çalıştırma prosedürü>

## Gözlemlenebilirlik
<metrikler, alarmlar, panolar>

## Güvenlik ve Uyum
<secret'lar, erişim, maskeleme, veri yerleşimi>

## Açık Sorular
- [TBD] ...
```

## Kalite kontrol listesi
- [ ] Tazelik ve tamamlanma saatleri bir tüketici ihtiyacına dayanıyor.
- [ ] Herhangi bir çalışmayı veya tarih aralığını yeniden çalıştırmak aynı hedef durumu üretiyor (idempotent).
- [ ] Geç veri, silmeler ve şema değişiklikleri için davranış tanımlı.
- [ ] Her kalite kapısının hata aksiyonu, her alarmın bir yolu var.
- [ ] Tanımda kimlik bilgisi yok; kişisel verinin nasıl ele alındığı belirtilmiş.
- [ ] Bilinmeyen hacimler ve SLA'lar uydurulmadı, `[TBD]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca mutlu yolu tanımlamak. Operasyon maliyetinin çoğu yeniden denemelerde, kısmi yüklemelerde ve geriye dönük yüklemelerde oluşur.
- Tekilleştirme olmadan yalnızca append yazma: her yeniden deneme mükerrer kayıt üretir.
- Asıl bağımlılık "üst akış bitti" iken saat bazlı zamanlama. Tamamlanma tetikleyicileri veya sensörler kullan.

## Örnek
Girdi: "ERP'deki günlük siparişler finans martı için ambara yüklenecek, saat 06:00'ya kadar lazım."

Çıktıdan bir bölüm:
- Tetikleyici: sabit 02:00 yerine ERP gece kapanış sinyalinden sonra; yerel saatle 06:00'ya kadar tamamlanır.
- Yazma modu: order_date ile bölümlenmiş olgu tablosuna (order_id) üzerinden merge; bir günün yeniden çalıştırılması yalnızca o günün bölümlerini yeniden yazar.
- Kalite kapısı: gün bazında ERP kontrol toplamına karşı satır sayısı, Kritik, mart yenilemesini durdurur ve nöbetçiyi çağırır.
