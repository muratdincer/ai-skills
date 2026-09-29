---
name: concurrency-review
description: "Kodu eşzamanlılık hatalarına karşı inceler: veri yarışları, kontrol-et-sonra-yap ve kayıp güncellemeler, kilitlenmeler ve kilit sırası, güvensiz yayımlama, async/await yanlış kullanımı, thread pool açlığı ve dağıtık tüketicilerde mükerrer ya da sırasız işleme; her bulgu için somut bir iç içe geçme senaryosu ve çözüm verir. Kod thread, async, kilit, paylaşılan durum, arka plan işçisi, mesaj tüketicisi veya eşzamanlı veritabanı güncellemesi kullanıyorsa ya da zamanlamaya bağlı görünen aralıklı hatalar bildirildiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: coding
  title: "Eşzamanlılık incelemesi"
  related: "code-review, error-handling-review, debugging-hypotheses, resilience-review, integration-test-writing"
  prompt: "Bu cüzdan bakiye yükleme servisini eşzamanlılık sorunlarına karşı incele; bakiyeyi okuyor, tutarı ekliyor ve kaydediyor, hem API'den hem de bir mesaj tüketicisinden çağrılıyor."
---

# Eşzamanlılık İncelemesi

## Amaç
Veriyi bozan, sistemi kilitleyen veya yan etkileri çoğaltan iç içe geçmeleri canlıya çıkmadan bulmak ve doğruluğu umutla değil gerekçeyle savunulabilen çözümler vermek.

## Ne zaman kullanılır
- Kod, değiştirilebilir durumu thread'ler, task'lar, istekler veya servis instance'ları arasında paylaşıyorsa.
- Async kod, kilitler, arka plan işçileri veya mesaj tüketicileri ekleniyor ya da değişiyorsa.
- Bir hata aralıklıysa, yüke bağlıysa veya debugger altında kayboluyorsa.

## Ne zaman kullanılmaz
- Tüm yönleriyle genel pull request incelemesi için `code-review` kullanılır.
- Timeout, retry ve circuit breaker gibi sistem düzeyi arıza modları için `resilience-review` kullanılır.
- Hata zaten yeniden üretildiyse ve kök neden aranıyorsa `debugging-hypotheses` kullanılır.

## Girdiler
Zorunlu:
- Kod ve dili/çalışma ortamı (bellek modeli ve async modeli farklıdır).

İsteğe bağlı, kaliteyi artırır:
- Nasıl çağrıldığı (istek başına, zamanlanmış, tüketici, instance sayısı), veri deposu ve izolasyon seviyesi, mesaj broker'ının teslim garantileri, gözlenen belirtiler.

Dağıtım şekli (tek veya çok instance) bilinmiyorsa her ikisi için incele ve buna bağlı bulguları `[VARSAYIM]` olarak işaretle.

## Süreç
1. Paylaşılan durumu envantere çıkar: alanlar, static'ler, cache'ler, singleton'lar, koleksiyonlar, dosyalar, veritabanı satırları, dış kaynaklar. Her birini kimin okuyup yazdığını not et.
2. Eşzamanlılık kaynaklarını belirle: thread'ler, thread pool'lar, async devamlar, paralel döngüler, istek handler'ları, çoklu instance'lar, paralel çalışan tüketiciler, retry'lar ve yeniden teslimler.
3. Her paylaşılan öğe için değişmezleri iç içe geçme altında kontrol et: kontrol-et-sonra-yap, oku-değiştir-yaz, tembel başlatma, değişiklik sırasında iterasyon, atomik olmayan bileşik güncellemeler.
4. Kilitler: en dar kapsam, çalışma ortamının yasakladığı veya cezalandırdığı yerlerde kritik bölge içinde I/O veya await yok, tutarlı kilit sırası, timeout'lar, dışarıdan erişilebilen nesneler üzerinde kilit yok.
5. Async: sync-over-async bloklama yok, hata yönetimi olmadan fire-and-forget yok, iptal (cancellation) aktarılıyor, event handler dışında async void yok, çalışma ortamının context yakalama kurallarına uyuluyor.
6. Dağıtık ve veritabanı: kayıp güncellemeler (versiyon/ETag ile optimistic concurrency veya atomik update ifadeleri kullan), idempotency için unique kısıtlar, en az bir kez teslimin idempotency anahtarlarıyla ele alınması, anahtar bazında sıralama varsayımlarının açıkça yazılması.
7. Kaynaklar: pool boyutları, sınırsız kuyruklar, thread pool açlığı, back-pressure.
8. Her bulgu için somut bir iç içe geçme yaz (T1 X yapar, T2 Y yapar, sonuç Z) ve önem derecesi ver: Kritik (veri bozulması, para, kilitlenme), Yüksek (mükerrer yan etki, açlık), Orta (etkili bayat okuma), Düşük (sağlamlaştırma).
9. En basit doğru çözümü öner, tercih sırasıyla: paylaşımı kaldır (değişmezlik, sınırlama), atomik bir primitive veya eşzamanlı koleksiyon kullan, veritabanı düzeyinde atomiklik veya kilit.
10. Nasıl test edileceğini belirt: stres veya yarış testi, deterministik zamanlama, gerçek depoya karşı eşzamanlı entegrasyon testi veya çalışma ortamı sunuyorsa race detector.
11. Hedef devam ediyorsa gerçek sınırlara karşı eşzamanlı testler için `integration-test-writing` veya sistem düzeyinde retry ve arıza davranışı için `resilience-review` öner.

## Çıktı formatı
```markdown
# Eşzamanlılık İncelemesi: <bileşen>
Çalışma modeli: <thread/async/instance/tüketici> · Varsayımlar: <liste>

## Paylaşılan Durum Envanteri
| Durum | Okuyanlar | Yazanlar | Bugünkü koruma |

## Bulgular
| # | Önem | Konum | İç içe geçme | Etki | Çözüm |

## Test Planı
- ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her bulgunun "güvensiz olabilir" değil somut bir iç içe geçme senaryosu var.
- [ ] Yalnızca süreç içi thread'ler değil çoklu instance ve yeniden teslim senaryoları da ele alındı.
- [ ] Çözümler geniş kilitler yerine paylaşımı kaldırmayı veya veritabanı atomikliğini tercih ediyor.
- [ ] Hiçbir çözüm, neden güvenli olduğunu söylemeden kilit içine I/O veya await eklemiyor.
- [ ] Her Kritik/Yüksek bulgunun bir test yaklaşımı var.
- [ ] Dağıtıma bağlı bulgular `[VARSAYIM]` olarak işaretli ve açık sorularda listeli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Servis birden fazla instance'ta çalışırken kayıp güncellemeyi süreç içi bir kilitle çözmeye çalışmak. Bunun yerine veritabanını kullan (versiyon kolonu, koşullu update).
- Thread-safe bir koleksiyonun bileşik işlemleri atomik yaptığını sanmak; "contains sonra add" hâlâ bir yarıştır.
- Mesaj broker'ının tam olarak bir kez veya global sırayla teslim ettiğini varsaymak.

## Örnek
Girdi: "TopUp(walletId, amount): balance = repo.Get(walletId); balance += amount; repo.Save(balance). API'den ve tüketiciden çağrılıyor; 3 instance."

Çıktıdan bir bölüm:
| # | Önem | Konum | İç içe geçme | Etki | Çözüm |
|---|---|---|---|---|---|
| 1 | Kritik | `TopUp` | T1 100 okur, T2 100 okur, T1 150 kaydeder, T2 120 kaydeder | 50'lik yükleme kaybolur | `UPDATE wallet SET balance = balance + @amt WHERE id=@id` veya retry'lı versiyon kontrollü update |
| 2 | Yüksek | Tüketici | Timeout sonrası yeniden teslim aynı yüklemeyi iki kez uygular | Çift bakiye | `topup_id`'yi aynı transaction içinde unique kısıtla sakla |
