---
description: "İş süreçlerinden boyutsal (yıldız/kar tanesi) model tasarlar: tanecik (grain), olgu tabloları ve ölçü toplanabilirliği, ortak (conformed) boyutlar, nitelik bazında SCD tipi ve geç gelen ile bilinmeyen üyelerin yönetimi. Veri ambarı veya lakehouse gold/mart katmanı, BI için semantik model kurulurken ya da yıldız şema, bus matrix veya olgu/boyut tasarımı istendiğinde kullanılır."
related: "metric-definition, dashboard-spec, report-requirements, data-vault-model, source-to-target-mapping"
prompt: "Perakende satış ve iade analizi için yıldız şema tasarla; kullanıcılar günlük mağaza/ürün KPI'larına ve müşteri segmenti tarihçesine ihtiyaç duyuyor."
---

# Boyutsal Model Tasarlama

## Amaç
İş sorularını raporlar arasında tutarlı rakamlarla, öngörülebilir sorgu performansıyla ve doğru tarihçeyle yanıtlayan bir analitik model üretmek. Bunu, herhangi bir tablo kurulmadan önce tanecik, olgular ve ortak boyutları sabitleyerek yapar.

## Ne zaman kullanılır
- BI, raporlama veya self-servis analitik katmanı kurulurken ya da yeniden kurulurken.
- Aynı KPI için farklı raporlar farklı rakam veriyor ve ortak bir model gerekiyorsa.
- Semantik katman veya metrik deposu altında iyi tanımlanmış bir yıldız şemaya ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- Hedef denetlenebilir, kaynağa hizalı bir entegrasyon katmanıysa `data-vault-model` kullanılır.
- Operasyonel/işlemsel şema tasarımı için `logical-data-model` veya `database-schema-design` kullanılır.
- Yalnızca tek bir metrik kesin tanımlanacaksa `metric-definition` kullanılır.

## Girdiler
Zorunlu:
- Analiz edilecek iş süreci/süreçleri ve kullanıcıların ihtiyaç duyduğu temel sorular veya KPI'lar.
- Mevcut kaynak olaylar/kayıtlar (tablolar, akışlar veya tanımlar).

İsteğe bağlı:
- Mevcut raporlar, metrik tanımları, boyutsal bus matrix, hacimler, gecikme ihtiyaçları, BI aracı kısıtları (genel ifadeyle), tarihçe gereksinimleri.

İş soruları veya kaynaklar yoksa iste; süreci ve taneciği beyan edilmemiş bir model doğrulanamaz.

## Süreç
1. Departman veya rapor değil, iş sürecini (operasyonel bir olay, ör. sipariş kalemi sevk edildi) seç.
2. Taneciği, kaynağın desteklediği en atomik düzeyde tek cümleyle beyan et ("sevkiyat başına sipariş kalemi başına bir satır"). Diğer her şey buna uymalı.
3. Olgu tablosu tipini seç: işlem (transaction), dönemsel anlık görüntü, biriken anlık görüntü veya olgusuz (kapsama/olay). Farklı tanecikler için ayrı olgular kullan; tek tabloda tanecik karıştırma.
4. Ölçüleri listele ve toplanabilirliği sınıflandır: toplanabilir, yarı toplanabilir (bakiyeler: zaman boyunca toplanmaz), toplanamaz (oranlar: pay ve paydayı sakla, semantik katmanda hesapla).
5. Olayın "kim, ne, nerede, ne zaman, neden, nasıl" sorularıyla boyutları belirle. Bus matrix'i (süreçler × boyutlar) kur ve ortak boyutları olgular arasında yeniden kullan.
6. Her boyutu tasarla: vekil anahtar, kalıcı doğal anahtar, düzleştirilmiş tanımlayıcı nitelikler (paylaşılan bir outrigger gerekçeli değilse kar tanesi yerine yıldız), hiyerarşiler sütun olarak.
7. SCD tipini tablo bazında değil nitelik bazında ata: 0 (sabit), 1 (üzerine yaz), 2 (geçerlilik tarihleri ve güncel bayrağıyla tarihçe), hızlı değişen nitelikler için 3/6 veya mini boyut. Her Tip 2'yi "olduğu haliyle" raporlama gerektiren bir soruyla gerekçelendir.
8. Özel durumları ele al: tarih/saat boyutları (mali takvim, saat dilimi), görünümlerle rol oynayan boyutlar, dejenere boyutlar (sipariş no), düşük kardinaliteli bayraklar için junk boyut, çok değerli boyutlar için ağırlık faktörlü köprü tablolar.
9. Bilinmeyen/uygulanamaz/geç gelen üyeleri (sabit vekil anahtarlar, sonradan güncellenen çıkarsanmış üyeler) ve geç gelen olgu politikasını tanımla.
10. Tablo bazında yükleme kurallarını belirt: anahtar eşleme, SCD işleme, yeniden düzeltme penceresi ve kaynağa karşı mutabakat toplamları.
11. Her iş sorusunu onu yanıtlayan olgu ve boyutlara eşle; tasarımın yanıtlayamadığı soruları işaretle.
12. Fiziksel ipuçlarını genel ifadeyle not et: olguları tarihe göre bölümle, sık filtrelerde kümeleme, özet tabloları yalnızca ölçülmüş performans ihtiyacında.

## Çıktı formatı
```markdown
# Boyutsal Model: <konu>
## Bus Matrix
| İş süreci (olgu) | Tanecik | Tarih | Müşteri | Ürün | Mağaza | ... |
|---|---|---|---|---|---|---|

## Olgu: <ad>
Tip: <işlem/dönemsel/biriken/olgusuz> | Tanecik: <tek cümle>
| Ölçü | Tanım | Toplanabilirlik | Birim |
|---|---|---|---|
Boyut anahtarları: <liste> | Dejenere: <liste>

## Boyut: <ad>
Doğal anahtar: <...> | Vekil anahtar: <...>
| Nitelik | SCD tipi | Gerekçe | Hiyerarşi düzeyi |
|---|---|---|---|
Özel üyeler: -1 Bilinmeyen, -2 Uygulanamaz, çıkarsanmış üye kuralı: <...>

## Soru Kapsamı
| İş sorusu | Olgu(lar) | Boyutlar | Yanıtlanabilir mi? |
|---|---|---|---|

## Yükleme ve Mutabakat Kuralları
- ...

## Açık Sorular / Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Her olgunun tam olarak bir beyan edilmiş taneciği var; tüm ölçü ve anahtarlar bu tanecikte doğru.
- [ ] Yarı ve toplanamaz ölçüler işaretli; oran bileşenleri saklanıyor.
- [ ] Paylaşılan boyutlar olgular arasında ortak (aynı anahtar, nitelik ve anlam).
- [ ] SCD tipi nitelik bazında seçildi ve her Tip 2 gerekçeli.
- [ ] Bilinmeyen ve geç gelen üye yönetimi tanımlı.
- [ ] Her iş sorusu modele eşlendi ya da yanıtlanamaz olarak işaretlendi.

## Sık yapılan hatalar
- Taneciği bir rapor olarak beyan etmek ("bölgeye göre aylık satış"). Atomikten başla, sonra özetle.
- "Ne olur ne olmaz" diye her şeyi Tip 2 yapmak; boyut büyür, kullanıcı şaşırır. Yalnızca "olduğu haliyle" sorusu olan nitelikleri izle.
- Olgulara yüzde veya ortalama koyup sonra toplamak. Bileşenleri sakla.
- Artık önemsiz olan depolama tasarrufu için kar tanesi yapıp her sorguya join eklemek.

## Örnek
Girdi: "Perakende satış ve iadeler, mağaza/ürün bazında günlük KPI'lar ve satın alma anındaki müşteri segmentine göre satışlar."

Çıktıdan bir bölüm:
- Olgu Satış Satırı: işlem tipi; tanecik "POS fişi satırı başına bir satır"; ölçüler miktar, net tutar (toplanabilir), birim fiyat (toplanamaz, toplanmaz).
- Olgu İadeler: iade satırı taneciğinde ayrı olgu; ortak Tarih, Mağaza, Ürün, Müşteri boyutları.
- Müşteri.segment: SCD Tip 2 ("olduğu haliyle" raporlama gerekli); Müşteri.e-posta: Tip 1, kişisel veri, mart katmanında maskeli.
