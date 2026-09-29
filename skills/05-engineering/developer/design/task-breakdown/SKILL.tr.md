---
description: "Bir kullanıcı hikayesini veya iş kalemini bağımlılıkları, göreli tahminleri ve her biri için tamamlanma tanımı olan, sıralı ve bağımsız doğrulanabilir teknik görevlere böler. Bir geliştirici veya ekip bir hikayeyi ele aldığında ve uygulama planına ihtiyaç duyduğunda, işi paralelleştirmek istediğinde veya hikayenin görevlere nasıl bölüneceği sorulduğunda kullanılır."
related: "user-story, story-splitting, technical-estimation, implement-from-story, technical-design-doc"
prompt: "Bu hikayeyi teknik görevlere böl: Müşteri olarak sipariş geçmişi sayfasından faturalarımı PDF olarak indirmek istiyorum."
---

# Hikayeyi Görevlere Bölme

## Amaç
Bir hikayeyi, her biri doğrulanabilir ve merge edilebilir bir durumda biten küçük teknik görevler dizisine çevirmek. Böylece iş takip edilebilir, geliştiriciler arasında paylaşılabilir ve sonda gizli işler ortaya çıkmadan tamamlanır.

## Ne zaman kullanılır
- Hikaye hazırsa ve ekip nasıl geliştireceğini planlıyorsa.
- Birden fazla geliştirici aynı hikaye üzerinde paralel çalışacaksa.
- Tahmin çok büyük görünüyorsa ve ekip eforun nerede olduğunu görmek istiyorsa.

## Ne zaman kullanılmaz
- Hikayenin kendisi çok büyükse veya birden fazla kullanıcı sonucunu karıştırıyorsa önce `story-splitting` kullanılır.
- Yaklaşım belirsiz veya riskliyse önce `spike-report` veya `technical-design-doc` kullanılır.
- Yalnızca bir efor rakamı gerekiyorsa `technical-estimation` kullanılır.

## Girdiler
Zorunlu:
- Kabul kriterleriyle birlikte hikaye veya iş kalemi.

İsteğe bağlı, kaliteyi artırır:
- Etkilenen bileşenler veya repository'ler, mevcut tasarım dokümanı, ekip kuralları (tahmin birimi, görev büyüklüğü sınırı).
- Bilinen kısıtlar: feature flag politikası, yayın penceresi, dahil olan diğer ekipler.

Kabul kriterleri yoksa iste ya da aday kriterler türet ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Kabul kriterlerini oku ve sistemin göstermesi gereken davranışları listele; her davranış için onu sağlayan ve doğrulayan en az bir görev olmalı.
2. Etkilenen katmanları ve varlıkları belirle: sözleşme/API, veri şeması, alan mantığı, arayüz, entegrasyonlar, yapılandırma, altyapı, dokümantasyon.
3. Mümkün olduğunca dikey dilimle (önce uçtan uca ince bir yol), sonra genişlet. "Önce tüm backend, sonra tüm frontend" yaklaşımından kaçın.
4. Destekleyici görevleri açıkça ekle: şema migration'ı, feature flag, sözleşme stub'ı veya mock, test verisi, yetkiler, gözlemlenebilirlik.
5. Her görevi yaklaşık bir günde (veya ekibin sınırında) bitirilip merge edilebilecek kadar küçük tut ve net bir tamamlanma koşulu ver.
6. Görevleri bağımlılığa göre sırala ve paralel yürüyebilecekleri işaretle. Riskli veya bilinmeyen işi başa al.
7. Diğer görevlerin içinde olmayan doğrulama görevlerini ekle: entegrasyon veya uçtan uca test, performans kontrolü, kişisel veri ya da yetkilendirme varsa güvenlik incelemesi.
8. Yayın görevlerini ekle: flag açılışı, dokümantasyon veya changelog, geçici kodun kaldırılması.
9. Ekibin biriminde göreli tahmin ver; belirsiz olanları işaretle, ekip saat kullanmıyorsa saat uydurma.
10. Kapsamı kontrol et: her kabul kriterini en az bir göreve eşle.

## Çıktı formatı
```markdown
# Görev Dağılımı: <hikaye başlığı>
Hikaye: <no/bağlantı> · Varsayımlar: <liste veya yok>

| # | Görev | Tamamlanma koşulu | Bağımlı olduğu | Paralel? | Tahmin |
|---|---|---|---|---|---|
| 1 | <fiil + nesne> | <doğrulanabilir koşul> | – | – | <birim> |

## Kabul Kriteri Kapsamı
| Kriter | Görevler |
|---|---|
| AC1 | 2, 4, 7 |

## Riskler ve Açık Sorular
- <risk veya soru> — <sorumlu>
```

## Kalite kontrol listesi
- [ ] Her kabul kriteri en az bir göreve eşlendi.
- [ ] Her görev bir fiille başlıyor ve kontrol edilebilir bir tamamlanma koşulu var.
- [ ] Hiçbir görev ekibin büyüklük sınırını aşmıyor; büyük olanlar bölündü.
- [ ] Migration, flag, test verisi ve temizlik görevleri açıkça yazıldı.
- [ ] İlk görevler en büyük riski veya bilinmeyeni azaltıyor.
- [ ] Tahminler ekibin biriminde; hiçbiri uydurulmadı.

## Sık yapılan hatalar
- Sonuna kadar doğrulanabilir hiçbir şey teslim etmeyen katman bazlı bölme ("backend", "frontend", "testler"). İnce dikey dilimleri tercih et.
- Kod dışı işi unutmak: yapılandırma, yetkiler, dashboard'lar, dokümanlar, flag kaldırma. Çoğu zaman eforun üçte biri budur.
- Sona konan bir "test yaz" görevi. Testler her görevin tamamlanma koşulunun içinde olmalı.

## Örnek
Girdi: "Müşteri olarak sipariş geçmişi sayfasından faturalarımı PDF olarak indirmek istiyorum. AC1: her sipariş için buton. AC2: PDF fatura düzenine uygun. AC3: yalnızca kendi faturaları."

Çıktıdan bir bölüm:
| # | Görev | Tamamlanma koşulu | Bağımlı olduğu | Paralel? | Tahmin |
|---|---|---|---|---|---|
| 1 | PDF üretim seçeneğini örnek düzene karşı spike ile dene | Örnek PDF ürün sahibince onaylandı | – | – | 1 |
| 2 | Flag arkasında sahiplik kontrollü `GET /orders/{id}/invoice.pdf` ekle | Sözleşme testi ve başka kullanıcının siparişi için 403 testi geçiyor | 1 | – | 2 |
| 3 | Sipariş geçmişi satırına indirme butonu ekle | Arayüz testi butonu yalnızca faturası kesilmiş siparişlerde gösteriyor | 2 (stub yeterli) | Evet | 1 |
