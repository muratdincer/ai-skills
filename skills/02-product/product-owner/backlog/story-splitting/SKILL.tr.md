---
name: story-splitting
description: "Büyük bir kullanıcı hikayesini veya iş maddesini adlandırılmış desenlerle (iş akışı adımı, iş kuralı, veri çeşitliliği, arayüz, işlem, olumlu/olumsuz yol, spike) ince ve bağımsız değer taşıyan dikey dilimlere böler; her dilim için kabul kriterlerini ve önerilen sırayı gösterir. Bir hikaye tek iterasyona/sprint'e sığmadığında, tahminler çok dağınık olduğunda ya da bir hikayenin bölünmesi, dilimlenmesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-owner
  area: backlog
  title: "Büyük hikayeleri bölme"
  related: "epic-breakdown, invest-check, backlog-refinement, acceptance-criteria, user-story"
  prompt: "Bu hikaye 21 puan ve kimse tahmine güvenmiyor: 'Müşteri olarak faturamı çevrim içi ödemek istiyorum.' Böl."
---

# Büyük Hikayeleri Bölme

## Amaç
Tek bir büyük maddeyi, her biri uçtan uca gözlemlenebilir değer sunan küçük dilimlere dönüştürmek. Böylece ekip kısa döngülerde bitirebilir, test edebilir, geri bildirim alabilir ve tahmin riski azalır.

## Ne zaman kullanılır
- Bir hikaye tek iterasyonda/sprint'te veya birkaç günlük akışta makul biçimde bitirilemeyecekse.
- Ekibin bir madde için tahminleri çok farklıysa ya da "bakarız" türü işler gizliyse.
- Bir hikaye birden fazla kullanıcı rolünü, kuralı veya kanalı bir arada içeriyorsa.
- Özelliğin tamamı yapılmadan önce erken geri bildirim gerekiyorsa.

## Ne zaman kullanılmaz
- Girdi, birçok hikayeye ilk seviye kırılım gerektiren bir epic veya özellikse `epic-breakdown` ya da `story-mapping` kullanılır.
- Hikaye küçük ama kötü yazılmışsa `user-story` veya `invest-check` kullanılır.
- Hazır bir hikaye için yalnızca teknik görevler gerekiyorsa `task-breakdown` kullanılır.

## Girdiler
Zorunlu:
- Hikaye veya madde metni ve varsa kabul kriterleri.

İsteğe bağlı, kaliteyi artırır:
- Mevcut tahmin ve ekibin tipik hikaye büyüklüğü.
- İlgili iş kuralları, kullanıcı rolleri, kanallar, veri çeşitleri.
- Bilinen teknik riskler veya bilinmeyenler.

Hikaye metni yoksa iste.

## Süreç
1. Hikayenin temel değerini tek satırda yeniden ifade et; örtük olarak içerdiği kabul kriterlerini, kuralları, rolleri, kanalları ve veri çeşitlerini listele.
2. Bilinmeyenleri belirle; büyük bir teknik veya alan sorusu boyutlandırmayı engelliyorsa, somut bir soru ve çıkış kriteri olan süre sınırlı bir spike dilimi öner.
3. Desenleri şu sırayla dene ve anlamlı dilim üretenleri tut:
   - İş akışı adımları (önce en basit uçtan uca yol, sonra zenginleştirme).
   - İş kuralı çeşitleri (her dilimde bir kural).
   - Olumlu yol ile hata/istisna yönetimi.
   - Veri çeşitleri (bir seferde tek veri tipi, para birimi, dosya formatı).
   - Arayüz/kanal (önce web, sonra mobil, sonra API).
   - İşlemler (oluşturma/okuma/güncelleme/silme ayrı ayrı).
   - Performans veya ölçeği ertele ("1M kayıtta" öncesi "100 kayıtta çalışıyor").
4. Yatay dilimleri reddet (sadece arayüz, sadece veritabanı, "backend hikayesi"); her dilim bir kullanıcıya gösterilebilir veya bir arayüz üzerinden test edilebilir olmalı.
5. Her dilimi 2-5 kabul kriterli bir hikaye olarak yaz. Orijinal kabul kriterlerinin tamamının dilimlerin birleşimiyle karşılandığından emin ol.
6. Her dilimi INVEST'e göre, özellikle Bağımsız, Değerli ve Küçük ölçütlerine göre kontrol et; bilinçli bağımlılıkları not et.
7. Bir sıra öner: en riskli varsayımı test eden ya da iskelet uçtan uca akışı (walking skeleton) sunan dilim önce gelir.
8. Geri bildirim düşük değer gösterirse tamamen çıkarılabilecek dilimleri adlandır.
9. Kullanıcının hedefi devam ediyorsa her dilimi doğrulamak için `invest-check`, korunan dilimlerin kriterlerini yazmak için `acceptance-criteria` öner.

## Çıktı formatı
```markdown
# Hikaye Bölme: <orijinal hikaye başlığı>
Orijinal: <hikaye metni>
Temel değer: <tek satır>
Kullanılan desenler: <desen listesi>

| # | Dilim | Desen | Kabul kriterleri (kısa) | Bağımlı olduğu | Çıkarılabilir mi? |
|---|---|---|---|---|---|
| 1 | <hikaye> | <desen> | <KK1; KK2> | – | Hayır |

## Spike (gerekirse)
- Soru: <ne öğrenilmeli>
- Süre sınırı: <süre>
- Çıkış: <soruyu cevaplayan kanıt>

## Kapsama Kontrolü
| Orijinal kabul kriteri | Karşılayan dilim |
|---|---|

## Önerilen Sıra ve Gerekçe
1. <dilim> – <neden önce>
```

## Kalite kontrol listesi
- [ ] Her dilim dikey ve bir kullanıcının veya testçinin gözlemleyebileceği bir şey sunuyor.
- [ ] Orijinal kabul kriterlerinin her biri en az bir dilimle eşleşiyor.
- [ ] İlk dilim bir bileşen değil, ince bir uçtan uca yol.
- [ ] Spike'ların sorusu, süre sınırı ve çıkış kriteri var.
- [ ] Tahmin uydurulmadı; boyutlandırma ekibe bırakıldı veya `[VARSAYIM]` olarak işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Katmana veya ekibe göre bölmek ("frontend hikayesi", "API hikayesi"). Bu değeri ve entegrasyon riskini erteler; davranışa göre böl.
- Aslında bitmemiş iş olan bir "bölüm 2: cilalama" dilimi oluşturmak. Her dilim tek başına Bitti Tanımını karşılamalı.
- Kullanıcı değeri olmayacak kadar ince bölmek (ör. "bir alan ekle"). En küçük değerli davranışa kadar geri birleştir.

## Örnek
Girdi: "Müşteri olarak faturamı çevrim içi ödemek istiyorum."

Çıktıdan bir bölüm:
| 1 | Tek bir faturayı kartla tamamen ödeme | İş akışı (en basit yol) | Ödeme onaylanır; fatura ödendi olarak işaretlenir | – | Hayır |
| 2 | Reddedilen kartı yeniden deneme ile yönetme | Olumlu/olumsuz yol | Anlaşılır hata; mükerrer tahsilat yok | 1 | Hayır |
| 3 | Birden fazla faturayı tek seferde ödeme | Veri çeşitliliği | Toplam gösterilir; her fatura işaretlenir | 1 | Evet |
| 4 | Havale/EFT ile ödeme | Kural/kanal çeşitliliği | Referans numarası üretilir | 1 | Evet |
- Spike: Ödeme sağlayıcı ödeme akışımızda 3-D Secure'u destekliyor mu? Süre sınırı 2 gün.
