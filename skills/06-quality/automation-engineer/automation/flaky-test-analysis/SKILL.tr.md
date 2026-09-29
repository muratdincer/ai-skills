---
name: flaky-test-analysis
description: "Kararsız (flaky) otomatik testleri analiz eder: koşum geçmişinden kararsızlık oranını ölçer, nedeni sınıflar (zamanlama ve async, paylaşılan durum ve sıra bağımlılığı, test verisi, ortam ve altyapı, dış bağımlılıklar, eşzamanlılık, ürünün deterministik olmayan davranışı), tek değişkenli deneylerle teyit eder ve kök nedene yönelik kararlılaştırma ile karantina politikası önerir. Kod değişmeden testler bazen geçip bazen kaldığında, CI'da yeniden koşum rutinleştiğinde ya da ekip kırmızı build'lere artık güvenmediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: automation-engineer
  area: automation
  title: "Kararsız test analizi"
  related: "test-automation-script, automation-framework-design, debugging-hypotheses, pipeline-failure-triage, log-analysis"
  prompt: "Bu 6 uçtan uca test CI'da yaklaşık 10 koşumda bir rastgele kalıyor, lokalde hiç kalmıyor. Hata logları ekte. Neden ve nasıl düzeltiriz?"
---

# Kararsız Test Analizi

## Amaç
Belirli testlerin aynı kod üzerinde neden farklı sonuç verdiğini bulup nedeni retry ile gizlemeden düzelterek test setine güveni geri kazanmak; bu sırada gerçek ürün hatalarının "sadece flaky" diye geçiştirilmesini önlemek.

## Ne zaman kullanılır
- Bir test değişmemiş kod üzerinde, lokalde veya CI'da, aralıklı olarak kaldığında.
- Yeşil build almak için yeniden koşum normal bir adım haline geldiğinde.
- Ekip testleri devre dışı bırakmak veya karantinaya almak üzereyken ve karar için dayanak gerektiğinde.

## Ne zaman kullanılmaz
- Bir test kod değişikliğinden sonra sürekli kalıyorsa `debugging-hypotheses` veya `stack-trace-analysis` kullanılır.
- Tüm pipeline altyapı veya konfigürasyon nedeniyle kalıyorsa `pipeline-failure-triage` kullanılır.
- Test sıfırdan yeniden yazılacaksa `test-automation-script` kullanılır.

## Girdiler
Zorunlu:
- Kararsız test(ler) ve en az bir hata çıktısı (hata, stack trace, ekran görüntüsü veya log).

İsteğe bağlı, kaliteyi artırır:
- Koşum geçmişi (koşum başına geçti/kaldı, runner, paralellik, sıra, süre), test kodu, testlerde, üründe veya altyapıda son değişiklikler.
- Ortam ayrıntıları: paralel worker'lar, paylaşılan veritabanları, dış servisler, saat/saat dilimi ayarları.

Hata çıktısı yoksa iste. Koşum geçmişi yoksa kararsızlık oranının bilinmediğini belirt ve tahmin etme.

## Süreç
1. Her kalan koşumun hata çıktısının tamamını oku, yalnızca doğrulama satırını değil; nerede kaldığını (kurulum, aksiyon, doğrulama, temizlik) ve tüm hataların aynı noktada olup olmadığını not et.
2. Nicelleştir: mevcut koşumlardaki kararsızlık oranı, ilk görülme tarihi, runner, paralellik, günün saati, test sırası veya süreyle ilişki. İlk görülme tarihi civarındaki son değişiklikleri kontrol et.
3. Olası nedeni sınıfla: zamanlama/async (sabit bekleme, eksik bekleme, animasyonlar), paylaşılan durum/sıra bağımlılığı, test verisi çakışmaları, ortam/kaynaklar (CPU, bellek, konteyner), dış bağımlılık, üründe eşzamanlılık, saat/yerel ayar ya da ürünün gerçekten deterministik olmayan davranışı (gerçek bir hata).
4. Her seferinde tek hipotez kur; her birinin lehine ve aleyhine kanıtı yaz ve `[HİPOTEZ]` olarak etiketle.
5. Her hipotez için tek değişkenli bir deney tasarla: tek başına ve set içinde koşum, sırayı rastgeleleştirme, paralelliği zorlama, testi N kez döngüde koşma, CPU veya ağı kısma, saati dondurma. Her koşumda yalnızca bir etkeni değiştir.
6. Kalan doğrulamadan geriye doğru, buna yol açan duruma (hangi veri, hangi önceki adım, hangi async olay) kadar iz sür; kök neden teyit edilene kadar devam et.
7. Kök neden üründeyse (race condition, kaybolan güncelleme, tutarsız okuma) bunu test sorunu olarak ele almayı bırak ve kanıtlarıyla bir hata kaydı aç.
8. Kararlılaştırmayı nedende öner: koşula dayalı beklemeler, yalıtılmış veri, paylaşılan durumun sıfırlanması, dış bağımlılığın stub'lanması veya sözleşme testiyle kapsanması, deterministik saat. Zaman aşımının kanıtlanabilir biçimde çok kısa olduğu durum dışında "retry ekle" veya "timeout'u artır" önerisini çözüm olarak kabul etme.
9. Üç kararlılaştırma denemesi başarısız olursa dur ve testin tasarımını veya seviyesini sorgula (kontrol API veya bileşen seviyesine taşınabilir mi?).
10. Ara dönem için karantina politikasını tanımla: karantinadaki testler koşmaya ve raporlamaya devam eder, bir sorumlusu ve bitiş tarihi olur, merge'ü bloke etmez; hiçbir test süresiz karantinada kalmaz.
11. Kullanıcı devam ederse testi yeniden yazmak için `test-automation-script`, sistemik nedenler (paylaşılan veri, beklemeler) için `automation-framework-design`, hata üründeyse `bug-report` öner.

## Çıktı formatı
```markdown
# Kararsız Test Analizi: <test/set>
## Kanıt
| Test | Gözlenen koşum | Kalma | Kararsızlık oranı | Kalma noktası | İlişkili olduğu etken |
|---|---|---|---|---|---|

## Neden Sınıflandırması
| Test | Kategori | Kanıt | Güven |
|---|---|---|---|

## Hipotezler ve Deneyler
1. [HİPOTEZ] ... — deney: <tek değişken> — sonuç: <teyit edildi/çürütüldü/bekliyor>

## Kök Neden
- ... (veya: henüz teyit edilmedi — sonraki deney: ...)

## Kararlılaştırma Planı
| Test | Nedendeki düzeltme | Seviye değişikliği? | Sorumlu | Doğrulama (art arda N yeşil koşum) |
|---|---|---|---|---|

## Karantina Kararı
- Karantinaya alınan testler, sorumlu, bitiş tarihi, raporlanmaya devam: evet/hayır

## Açılan Ürün Hataları
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Hata çıktısının tamamı okundu ve her koşum için kalma noktası belirlendi.
- [ ] Kararsızlık oranları gerçek koşum verisinden geliyor; geçmiş olmadan tahmin yapılmadı.
- [ ] Her hipotez tek değişkenli bir deneyle sınandı ve teyit edilene kadar etiketli kaldı.
- [ ] Düzeltme kök nedeni hedefliyor; retry veya daha uzun timeout çözüm olarak sunulmadı.
- [ ] Olası ürün hataları test hatalarından ayrıldı ve kayda alındı.
- [ ] Karantinadaki her testin bir sorumlusu ve bitiş tarihi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Otomatik retry eklemek. Build'i yeşile çevirir, hem testteki hem üründeki yarış durumlarını gizler; retry'ı yalnızca kanıt toplamak için kullan.
- "Flaky" demenin "test sorunu" demek olduğunu varsaymak. Aralıklı hatalar çoğu zaman kullanıcıların da yaşayacağı gerçek eşzamanlılık hatalarıdır.
- Aynı anda birkaç şeyi değiştirmek. Test kararlı hale gelince nedenini artık bilemezsin ve sorun geri döner.

## Örnek
Girdi: 6 uçtan uca test CI'da yaklaşık 10 koşumda bir kalıyor, lokalde hiç kalmıyor; loglarda "element not clickable" ve bir kez "order not found" var.

Çıktıdan bir bölüm:
- Kanıt: tüm kalmalar 4 worker'lı koşumlarda; tek worker'lı koşumlarda hiç yok → paralellikle ilişkili.
- `[HİPOTEZ]` testler sabit `test-user-01` müşterisini paylaşıyor; paralel koşumlar aynı sepeti değiştiriyor — deney: seti 4 worker ve test başına benzersiz müşteriyle koş — sonuç: 50 koşumda 0 kalma → teyit edildi.
- Düzeltme: veri API'siyle test başına müşteri oluştur; paylaşılan hesabı fixture'lardan çıkar. "Element not clickable": 2 saniyelik sleep yerine overlay'in gizlenmesini bekle.
