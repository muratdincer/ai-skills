---
description: Bir sistemin nasıl ölçeklendiğini, yük artışını her bileşene göre modelleyerek inceler; darboğazları (CPU, I/O, kilitler, bağlantılar, sıcak bölümler, paylaşılan durum) bulur; durumsuzluk, bölümleme, önbellek, asenkron işleme ve veri katmanı limitlerini değerlendirir; önceliklendirilmiş öneriler ve mevcut tasarımın ölçekleme sınırını verir. Beklenen bir büyüme adımı veya tepe olay öncesinde, gecikme yükle birlikte bozulduğunda ya da dikey ve yatay ölçekleme arasında seçim yapılırken kullanılır.
related: capacity-planning, performance-test-plan, load-test-analysis, resilience-review, query-optimization
prompt: Raporlama API'mizin ölçeklenebilirliğini incele; büyük bir müşteriyi aldıktan sonra trafik 5 katına çıkacak ve p95 gecikme ay sonunda şimdiden sert yükseliyor.
---

# Ölçeklenebilirlik İncelemesi

## Amaç
Mevcut tasarımın ne kadar büyüyebileceğini, önce neyin ve neden bozulacağını ve hangi değişikliklerin en çok pay kazandıracağını belirlemek. Böylece büyüme acil donanım alımıyla değil tasarımla karşılanır.

## Ne zaman kullanılır
- Bilinen bir büyüme adımı, müşteri katılımı veya mevsimsel tepe yaklaşırken.
- Gecikme veya hata oranı yükle doğrusal olmayan biçimde arttığında.
- Ekip dikey ölçekleme, yatay ölçekleme veya bir bileşeni yeniden tasarlama arasında seçim yapmak zorunda olduğunda.

## Ne zaman kullanılmaz
- İhtiyaç bir kapasite tahmini ve tedarik planıysa `capacity-planning` kullanılır.
- Kaygı büyüme değil hata davranışıysa `resilience-review` kullanılır.
- Belirli bir yavaş sorgu veya kod yolu zaten belirlendiyse `query-optimization` veya `performance-optimization` kullanılır.

## Girdiler
Zorunlu:
- İncelenen akışların mimarisi (bileşenler, veri depoları, çağrı yolları).
- Mevcut ve beklenen yük (istekler, veri hacmi, eşzamanlı kullanıcılar) veya bunların `[BİLİNMİYOR]` olarak işaretlenmesine izin.

İsteğe bağlı:
- Performans ve kullanım metrikleri, yük testi sonuçları, tepe örüntüleri, veri büyüme hızları.
- Gecikme/işlem hacmi hedefleri, maliyet tavanı, platform limitleri (kotalar, lisans sınırları).

Yük rakamları yoksa göreli çarpanlarla (ör. "mevcudun 5 katı") ilerle ve toplanacak ölçümleri listele.

## Süreç
1. İş yükü modelini tanımla: temel işlemler, karışım, geliş örüntüsü (sabit, dalgalı, ay sonu), okuma/yazma oranı, veri büyümesi ve hedef çarpan.
2. Her temel işlemi bileşenler boyunca izle; adım başına kaynak kullanımını ve yayılımı (istek başına çağrı, istek başına sorgu, N+1 riskleri) kaydet.
3. Durumsuzluğu kontrol et: oturum, bellek içi önbellekler, yerel dosyalar, yapışkan yönlendirme, tek instance varsayan zamanlanmış işler.
4. Veri katmanını kontrol et: bağlantı limitleri ve havuzlama, kilit ve sıcak satır çekişmesi, büyüyen veride indeks ve sorgu planları, okuma replikası uygunluğu ve gecikme toleransı, bölümleme/sharding anahtarı ve sıcak bölüm riski.
5. Önbelleği kontrol et: ne önbelleğe alınıyor, isabet oranı, geçersizleştirme stratejisi, stampede koruması, önbelleğin gizli tekil hata noktası olması.
6. Asenkron yolları kontrol et: kuyruk derinliği artışı, sıralama kısıtlarına karşı tüketici paralelliği, geri basınç, veri büyüdükçe batch pencere süreleri.
7. Paylaşılan ve dış limitleri kontrol et: üçüncü taraf hız limitleri, platform kotaları, lisansa bağlı bileşenler, ağ çıkışı, tek yazıcılı bileşenler.
8. İlk üç darboğazı kanıt veya gerekçesiyle belirle ve her birinin doyuma ulaşacağı yükü tahmin et; ölçülene kadar tahminleri `[VARSAYIM]` olarak işaretle.
9. Değişiklikleri efor başına kazanılan paya göre sırala: yapılandırma ve havuzlama, sorgu/indeks düzeltmeleri, önbellek, yatay ölçekleme, asenkrona taşıma, bölümleme, yeniden tasarım; maliyet ve tutarlılık ödünleşimlerini not et.
10. Doğrulama yöntemini tanımla: yük testi senaryoları, izlenecek metrikler ve doyum sinyalleri (kullanım, doyum, hatalar).
11. Hedef devam ediyorsa limitleri doğrulamak için `performance-test-plan`, boyutlandırma için `capacity-planning` veya veri katmanı sıcak noktaları için `query-optimization` öner.

## Çıktı formatı
```markdown
# Ölçeklenebilirlik İncelemesi: <sistem> – <tarih>
## İş Yükü Modeli
| İşlem | Mevcut hız | Hedef hız | Örüntü | Okuma/Yazma |
|---|---|---|---|---|
## İstek Yolu Analizi
| İşlem | Adım | Kaynak | Yayılım | Kaygı |
|---|---|---|---|---|
## Darboğazlar
| Sıra | Bileşen | Mekanizma | Doyum noktası (tahmini) | Kanıt |
|---|---|---|---|---|
## Öneriler
| ID | Değişiklik | Kazanılan pay | Efor | Ödünleşim |
|---|---|---|---|---|
## Doğrulama Planı
## Mevcut Tasarımın Sınırı
## Varsayımlar, Toplanacak Ölçümler, Açık Sorular
```

## Kalite kontrol listesi
- [ ] İş yükü modeli yalnızca ortalamayı değil hedef çarpanı ve geliş örüntüsünü de belirtiyor.
- [ ] Her darboğaz yalnızca "veritabanı yavaş" demiyor, bir mekanizma (kilit, havuz, bölüm, yayılım) adlandırıyor.
- [ ] Doyum tahminleri, teyit için gereken veriyle birlikte tahmin olarak etiketli.
- [ ] Öneriler efor başına kazanılan paya göre sıralı ve ödünleşimleri belirtiyor.
- [ ] Durum tutan bileşenler ve dış limitler açıkça kontrol edildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tavan veritabanı veya bir üçüncü taraf limitiyken uygulama katmanını yatay ölçeklemenin her şeyi çözeceğini varsaymak.
- Ortalama yüke göre tasarlamak; gerçek ihtiyacı ay sonu veya kampanya dalgaları belirler.
- Geçersizleştirme ve stampede tasarımı olmadan önbellek eklemek; gecikmeyi yanlış veriyle takas etmek.

## Örnek
Girdi: "Raporlama API'si, 5 kat büyüme bekleniyor, p95 ay sonunda şimdiden sıçrıyor."

Çıktıdan bir bölüm:
| Sıra | Bileşen | Mekanizma | Doyum noktası (tahmini) |
|---|---|---|---|
| 1 | Birincil DB | Ay sonu raporları OLTP birincilde ağır toplamalar çalıştırıyor; kilit beklemeleri ve I/O doyumu | Mevcut ay sonu yükünün ~1,5 katı `[VARSAYIM – DB metrikleriyle teyit et]` |
| 2 | API pod'ları | Her rapor isteği sorgu boyunca bir DB bağlantısı tutuyor; pod başına 20'lik havuz | CPU'dan önce havuz tükeniyor |

Birinci öneri: rapor sorgularını okuma replikasına veya önceden toplanmış bir depoya taşı, büyük raporları asenkron yap (iste, sorgula, indir).
