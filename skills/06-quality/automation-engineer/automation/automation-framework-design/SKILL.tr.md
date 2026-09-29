---
description: "Bir test otomasyon çatısı tasarlar: test seviyeleri ve payları, katmanlı mimari (testler, iş aksiyonları, page object/API istemcileri, sürücüler), test verisi ve ortam yönetimi, konfigürasyon ve gizli bilgiler, raporlama ve izlenebilirlik, paralellik ve kalite kapılarıyla CI entegrasyonu ve bakım kolaylığı için kurallar. Bir ekip otomasyona başladığında, mevcut set yavaş, kırılgan veya sahipsiz olup yeniden tasarım gerektirdiğinde ya da UI, API ve sözleşme testleri için bir yapı seçilecekken kullanılır."
related: test-strategy, automation-candidate-selection, test-automation-script, pipeline-design, flaky-test-analysis
prompt: "Web uygulamamız ve REST API'lerimiz için bir test otomasyon çatısı tasarla; set her pull request'te 15 dakikadan kısa sürede koşmalı."
---

# Test Otomasyon Çatısı Tasarımı

## Amaç
Otomatik testlerin hızlı yazıldığı, bakımının ucuz olduğu ve CI'da güvenilir çalıştığı bir yapı tanımlamak. Böylece otomasyon, kırılgan UI script'leri ve paylaşılan veri altında çökmek yerine ürünle birlikte ölçeklenir.

## Ne zaman kullanılır
- Bir ekip otomasyona başlarken veya birkaç dağınık seti birleştirirken.
- Mevcut set yavaş, kararsız ya da UI'a o kadar bağlı olduğunda ki küçük değişiklikler çok sayıda testi bozuyor.
- Yeni bir ürün, platform (mobil, yalnızca API, olay güdümlü) veya CI kurulumu yeni bir yapı gerektirdiğinde.

## Ne zaman kullanılmaz
- Ürün genelinde test yaklaşımı (seviyeler, türler, ortamlar) gerekiyorsa `test-strategy` kullanılır.
- Hangi testlerin otomatikleştirileceğine karar verilecekse `automation-candidate-selection` kullanılır.
- Mevcut bir çatıda tek bir otomatik test yazılacaksa `test-automation-script` kullanılır.

## Girdiler
Zorunlu:
- Test edilen sistem: türü (web, mobil, API, olay güdümlü, batch), ana arayüzleri ve teknoloji yığını.
- Ekip bağlamı: testleri kim yazıyor (geliştiriciler, otomasyon mühendisleri, ikisi birden) ve hangi dilleri kullanıyorlar.

İsteğe bağlı, kaliteyi artırır:
- Mevcut setler ve sorunlu noktaları, CI platformu kısıtları, geri bildirim süresi hedefleri, mevcut ortamlar.
- Test verisi kaynakları, kimlik doğrulama mekanizmaları, dış bağımlılıklar, raporlama için uyum gereksinimleri.

Sistem veya ekip bağlamı yoksa iste (tek kısa numaralı soru grubu). Araç seçimleri ekibin teknoloji yığınını izlemeli; belirli bir araç önerdiğinde ekibin eşdeğeriyle değiştirebilmesi için seçim kriterlerini de ver.

## Süreç
1. Hedefleri ve kısıtları belirle: pipeline aşaması başına geri bildirim süresi (örneğin pull request ve gece koşumu), hedef kararsızlık oranı, testleri kimin yazdığı, desteklenen tarayıcılar/cihazlar ve neyin kime raporlanacağı.
2. Test seviyesi karışımını tanımla: geliştiricilerin sahip olduğu unit ve bileşen testleri, servis sınırlarında sözleşme testleri, iş kuralları için API/servis testleri ve ince bir UI uçtan uca yolculuk katmanı. Hedeflenen oranı ve hangi seviyenin hangi risk türüne sahip olduğunu yaz.
3. Katmanları tasarla: test spesifikasyonları (yalnızca niyet) → iş aksiyonları/akışlar → page object, ekran nesneleri veya API istemcileri → sürücüler ve adaptörler. Testler konum belirleyicilere, HTTP ayrıntılarına veya beklemelere doğrudan dokunmaz.
4. Test verisi yönetimini tanımla: benzersiz tanımlayıcılarla API, builder veya factory üzerinden test başına oluşturulan veri; kodla birlikte versiyonlanan referans veri; canlı kopyalarına bağımlılık yok; gerçek kişisel veri için maskeleme; temizlik veya kullan-at ortamlar.
5. Bağımlılıkları ve ortamları ele al: hangi dış sistemlerin stub'lanacağı, sanallaştırılacağı veya sözleşme testiyle kapsanacağı; değişkenlerle ortam konfigürasyonu; pipeline'ın gizli bilgi kasasından enjekte edilen, asla commit edilmeyen gizli bilgiler.
6. Güvenilirlik kurallarını belirle: yalnızca koşula dayalı beklemeler, test yalıtımı ve paralel güvenlik, deterministik saat ve yerel ayar; retry'a yalnızca kararsızlık takibiyle kanıt toplamak için izin.
7. Raporlama ve izlenebilirliği tanımla: hata artefaktlarıyla (ekran görüntüsü, istek/yanıt, log) seviye bazında sonuçlar, özellik/risk/gereksinim numarası etiketleri, süre ve kararsızlık oranı için trend verisi.
8. CI ile entegre et: pull request, merge, gece ve sürüm öncesi aşamalarda hangi alt kümelerin koşacağı; bölme (sharding) ve paralellik; kalite kapıları (merge'ü ne bloke eder); sorumlusu ve bitiş tarihi olan karantina mekanizması.
9. Kuralları koy: klasör ve isimlendirme yapısı, test adlandırma (davranış + beklenen sonuç), test kodu için code review kuralları, alan bazında sahiplik, yeni bir test için tamamlanma tanımı.
10. Geçişi planla: önce ince bir dikey dilim (tam pipeline'dan geçen bir UI yolculuğu, bir API testi, bir sözleşme testi), ardından mevcut testlerin değere göre taşınması; riskleri ve karar noktalarını listele.
11. Kullanıcı devam ederse backlog'u doldurmak için `automation-candidate-selection`, ilk dilim için `test-automation-script`, pipeline değişiklikleri için `pipeline-design` öner.

## Çıktı formatı
```markdown
# Test Otomasyon Çatısı Tasarımı: <ürün>
## Hedefler ve Kısıtlar
- Geri bildirim süresi hedefleri / kararsızlık hedefi / yazarlar / platformlar

## Test Seviyesi Karışımı
| Seviye | Sahip olduğu riskler | Sorumlu | Koştuğu aşama | Pay |
|---|---|---|---|---|

## Mimari
<katman diyagramı veya listesi: spesifikasyonlar → aksiyonlar → page object / API istemcileri → sürücüler>

## Test Verisi ve Ortamlar
- ...
## Bağımlılıklar (stub / sanallaştırma / sözleşme)
| Bağımlılık | Yaklaşım | Gerekçe |
|---|---|---|
## Güvenilirlik Kuralları
- ...
## Raporlama ve İzlenebilirlik
- ...
## CI Entegrasyonu
| Aşama | Alt küme | Paralellik | Kapı |
|---|---|---|---|
## Kurallar
- ...
## Geçiş Planı ve Riskler
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her test seviyesinin net bir risk sahipliği var ve UI uçtan uca testler ince bir katman.
- [ ] Testler katmanlar aracılığıyla konum belirleyicilerden, protokol ayrıntılarından ve beklemelerden ayrılmış.
- [ ] Test verisi test başına oluşturuluyor ve paralel koşuma uygun; kişisel veri maskelenmiş veya sentetik.
- [ ] Gizli bilgiler repodan değil pipeline'ın gizli bilgi kasasından geliyor.
- [ ] CI aşamalarının açık geri bildirim süresi hedefleri ve süresi sınırlı karantina dahil merge kapıları var.
- [ ] Önerilen araçlar, eşdeğerleriyle değiştirilebilmeleri için seçim kriterleriyle birlikte veriliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Dondurma külahı" set kurmak: kontrollerin çoğu UI uçtan uca testlerde. İş kurallarını API ve bileşen seviyelerine indir.
- Yazarı dışında kimsenin anlamadığı bir çatı tasarlamak. Katmanları ince, kuralları yazılı tut; test kodunu üretim kodu gibi review et.
- Büyük patlama (big-bang) geçişle başlamak. Yüzlerce testi taşımadan önce tasarımı tek bir dikey dilimde kanıtla.

## Örnek
Girdi: web uygulaması ve REST API'ler; geliştiriciler ve iki otomasyon mühendisi; pull request pipeline'ı 15 dakikada bitmeli.

Çıktıdan bir bölüm:
- Seviye karışımı: her commit'te unit/bileşen (geliştiriciler); 4 servis sınırı için sözleşme testleri; fiyatlandırma ve sipariş kuralları için ~150 API testi; paralel shard'larda 8 UI yolculuğu (giriş, arama, ödeme, iade...).
- CI: pull request'te unit, sözleşme ve API smoke (hedef 12 dakikanın altı); merge'te tam API; gece 2 tarayıcıda UI yolculukları. `[VARSAYIM]` CI platformu 4 paralel shard destekliyor.
- Veri: builder'lar iç API'ler üzerinden test başına müşteri ve ürün oluşturur; paylaşılan hesap yok.
