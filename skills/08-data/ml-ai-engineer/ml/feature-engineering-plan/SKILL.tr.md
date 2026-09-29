---
description: Tahmine dayalı bir model için öznitelikleri planlar; hipoteze göre aday öznitelikler, kaynak ve tahmin anındaki erişilebilirlik, zamana göre doğruluk (point-in-time), sızıntı kontrolleri, dönüşümler, kodlama, eksik değer stratejisi ve doğrulama yaklaşımı. ML problemi tanımlandıktan sonra ve model eğitiminden önce ya da bir model şüphe uyandıracak kadar iyi performans gösterdiğinde ve sızıntıdan şüphelenildiğinde kullanılır.
related: ml-problem-framing, data-exploration, model-evaluation-report, source-to-target-mapping, data-quality-rules
prompt: Bir telekom abonelik tabanı için churn modelinin öznitelik mühendisliğini planla; tahmin her ay sonraki 60 gün için yapılıyor.
---

# Öznitelik Mühendisliği Planı

## Amaç
Tahmin gücü olan, tahmin anında mevcut, sızıntı içermeyen ve üretimde tekrarlanabilir bir öznitelik seti tasarlamak. Böylece çevrim dışı sonuçlar canlıya geçişte de geçerli kalır.

## Ne zaman kullanılır
- Bir ML problemi tanımlandığında ve ekibin bir öznitelik backlog'una ihtiyacı olduğunda.
- Çevrim dışı metrikler gerçek olamayacak kadar iyi göründüğünde.
- Öznitelikler notebook'lardan bir öznitelik hattına veya feature store'a taşınacağında.

## Ne zaman kullanılmaz
- Hedef, tahmin anı veya başarı metriği henüz tanımlanmadıysa `ml-problem-framing` kullanılır.
- Ham veri henüz anlaşılmadıysa `data-exploration` kullanılır.
- Görev eğitilmiş bir modeli değerlendirmekse `model-evaluation-report` kullanılır.

## Girdiler
Zorunlu:
- Problem tanımı: hedef/etiket kuralı, tahmin anı ve tahmin birimi.
- Mevcut veri kaynakları (tablolar ve anahtar alanlar).

İsteğe bağlı, kaliteyi artırır:
- Etkenlere dair alan bilgisi, mevcut öznitelikler, sunum kısıtları (gecikme, toplu veya çevrim içi).

Tahmin anı yoksa sor; o olmadan sızıntı değerlendirilemez.

## Süreç
1. Tahmin anını ve etiket penceresini yeniden yaz; zaman çizelgesini çiz (öznitelik penceresi → kesim noktası → etiket penceresi).
2. Alan hipotezlerinden aday öznitelikleri aileler halinde çıkar: yakınlık/sıklık/parasal değer, trend ve değişim, davranış/kullanım, ilişki/kıdem, bağlam (takvim, bölge), etkileşimler.
3. Her öznitelik için kaynağı, toplama penceresini, sunum anındaki güncelliği ve zamana göre doğru getirme yöntemini (as-of join, anlık görüntü tabloları, olay zamanı filtresi) kaydet.
4. Sızıntı kontrollerini yap: kesim noktasından sonraki veriyi kullanıyor mu? Etiketin vekili mi (ör. "iptal nedeni", tahsilat bayrakları)? Hedeften türetilen kodlamalar tüm veri üzerinde mi hesaplandı? Aynı varlık hem eğitim hem testte mükerrer mi?
5. Dönüşümleri tanımla: çarpıklık için log/Box-Cox, oranlar, gruplama (binning), geçen süre öznitelikleri, kayan istatistikler; hangi modellerin ölçekleme gerektirdiğini not et.
6. Kategorik kodlamayı tanımla (one-hot, frekans, fold dışı hesaplanan target encoding), yüksek kardinaliteyi ve görülmemiş kategori politikasını belirle.
7. Her öznitelik için eksik değer stratejisini tanımla: anlamlı eksiklik göstergesi, yalnızca eğitim verisi üzerinde hesaplanan doldurma kuralı.
8. Hassas veya korunan nitelikleri ve vekillerini (posta kodu, isimden türetilen cinsiyet) işaretle; hariç tutma veya adillik izleme kararı ver (KVKK/GDPR).
9. Doğrulamayı tanımla: üretimi yansıtan zamana dayalı bölme, varlık bazında grup bölme, öznitelik ailelerinin ablasyonu, zaman dilimleri arasında önem ve kararlılık kontrolleri.
10. Üretim eşdeğerliğini tanımla: eğitim ve sunum için aynı kod yolu, öznitelik testleri ve öznitelik dağılımlarının izlenmesi.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Kullanıcının hedefi devam ediyorsa model eğitildikten sonra `model-evaluation-report` veya öznitelik hattı kontrolleri için `data-quality-rules` öner.

## Çıktı formatı
```markdown
# Öznitelik Mühendisliği Planı: <model>
Tahmin anı: ... | Öznitelik penceresi: ... | Etiket penceresi: ... | Birim: ...

## Aday Öznitelikler
| # | Öznitelik | Aile | Hipotez | Kaynak | Pencere | Kesimde mevcut mu? | Sızıntı riski |
|---|---|---|---|---|---|---|---|

## Dönüşümler ve Kodlama
| Öznitelik | Dönüşüm / kodlama | Neyle fit edilir | Notlar |
|---|---|---|---|

## Eksik Değerler
| Öznitelik | Strateji | Gösterge? |
|---|---|---|

## Hariç Tutulan Öznitelikler
- <öznitelik> – <neden: sızıntı / hassas / çevrim içi mevcut değil>

## Doğrulama Yaklaşımı
- Bölme: ...
- Ablasyonlar: ...

## Üretim Eşdeğerliği ve İzleme
- ...

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Her öznitelik yalnızca kesim noktasından önceki veriyle hesaplanabiliyor.
- [ ] Etiket vekilleri ve sonuç sonrası alanlar açıkça hariç tutuldu.
- [ ] Kodlayıcılar ve doldurucular yalnızca eğitim fold'larında fit edildi.
- [ ] Doğrulama bölmesi modelin zaman içinde nasıl kullanıldığını yansıtıyor.
- [ ] Hassas nitelikler ve vekilleri ele alındı.
- [ ] Her öznitelik için sunum anında erişilebilirlik ve gecikme kontrol edildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yavaş değişen bir tablonun as-of değeri yerine güncel görüntüsünü kullanmak; bu geleceği sızdırır.
- Aynı müşteri hem eğitim hem testte yer alırken rastgele satır bölmesi yapmak.
- Target encoding'i tüm veri seti üzerinde yapıp çevrim dışı metrikleri şişirmek.

## Örnek
Girdi: Telekom churn, sonraki 60 gün için aylık tahmin; kaynaklar: kullanım CDR özetleri, faturalama, destek kayıtları, sözleşme tablosu.

Çıktıdan bir bölüm:
| # | Öznitelik | Aile | Kesimde mevcut mu? | Sızıntı riski |
|---|---|---|---|---|
| 3 | Son 30 gün veri kullanımının önceki 90 güne göre değişimi | Trend | Evet | Düşük |
| 7 | Sözleşmenin 60 gün içinde bitmesi | İlişki | Evet | Düşük |
| 9 | Numara taşıma talebi bayrağı | Davranış | Hayır – churn ile birlikte gelir | Yüksek → hariç |
