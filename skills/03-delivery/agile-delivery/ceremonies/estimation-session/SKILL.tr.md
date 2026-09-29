---
name: estimation-session
description: "Göreli tahmin oturumunu (planning poker, tişört bedeni, benzerlik tahmini) hazırlar ve yönlendirir: ölçeği seçer, referans hikaye merdiveni kurar, varsayımları ortaya çıkaran tahmin turlarını yürütür ve boyutları, dağılımı ve takip işlerini kaydeder. Ekip backlog maddelerini boyutlandırmak, yeni bir ölçeği kalibre etmek veya yavaş tahmin toplantılarını hızlandırmak istediğinde ya da planning poker veya tişört bedeni oturumunun nasıl yürütüleceği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Göreli tahmin oturumu"
  related: "backlog-refinement, story-splitting, technical-estimation, velocity-analysis, iteration-planning"
  prompt: "Yeni onboarding epic'i için boyutlandırılmamış 25 hikayemiz ve 1 saatlik bir oturumumuz var. Ekip yeni ve referans hikaye yok. Nasıl tahmin yapalım?"
---

# Göreli Tahmin Oturumu

## Amaç
Ekibe hızlıca tutarlı göreli boyutlar kazandırmak ve tahminin asıl değerini yakalamak: ortak anlayış, görünür hale gelen varsayımlar ve bölünmesi ya da spike yapılması gereken maddelerin işaretlenmesi.

## Ne zaman kullanılır
- İyileştirilmiş bir grup backlog maddesinin planlama veya öngörü öncesi boyutlandırılması gerekiyor.
- Yeni bir ekibin veya büyük değişiklik geçirmiş bir ekibin kalibre edilmiş bir ölçeğe ve referans hikayelere ihtiyacı var.
- Tahmin toplantıları uzuyor, tek bir sesin hakimiyetinde geçiyor veya kimsenin güvenmediği sayılar üretiyor.

## Ne zaman kullanılmaz
- Maddeler hâlâ belirsizse veya kabul kriterleri yoksa önce `backlog-refinement` kullanılır.
- Bir tasarım veya teklif için saat ya da gün cinsinden aşağıdan yukarı mühendislik tahmini için `technical-estimation` veya `estimation-three-point` kullanılır.
- Ekip boyutlandırma yapmadan verim sayılarından öngörü yapıyorsa `monte-carlo-forecast` kullanılır.

## Girdiler
Zorunlu:
- Kısa açıklamalarıyla tahmin edilecek maddelerin listesi.
- Ayrılan süre ve tahmin yapacak kişi sayısı.

İsteğe bağlı, kaliteyi artırır:
- Mevcut referans hikayeler ve boyutları; kullanılan ölçek.
- Kabul kriterleri, bilinen teknik kısıtlar.
- Tahminlerin amacı (iterasyon planlama, sürüm öngörüsü, bir epic için devam/dur kararı).

Madde listesi yoksa iste. Boyut uydurma; boyutları ekip üretir.

## Süreç
1. Amacı netleştir; ayrıntı düzeyini amaç belirler. Sürüm seviyesinde tişört bedeni yeterli olabilir; iterasyon planlaması genellikle daha ince bir ölçek ister.
2. Tekniği grup büyüklüğüne göre seç: yaklaşık 15'ten az madde → planning poker; 15-100 madde → benzerlik/sessiz gruplama, ardından yalnızca tartışmalı maddeler için poker; epic'ler → tişört bedenleri.
3. Ölçeği (ör. değiştirilmiş Fibonacci 1, 2, 3, 5, 8, 13, 20 veya XS-XL) ve bir boyutun neyi birleştirdiğini tanımla: tek kişinin saatleri değil; efor, karmaşıklık ve belirsizlik.
4. Referans merdiveni kur: ekibin iyi bildiği 3-5 tamamlanmış maddeyi küçük, orta ve büyük için çapa olarak seç. Hiç yoksa net, küçük bir maddeyi "2" kabul et ve diğerlerini ona göre boyutlandır; bu kalibrasyonu geçici olarak işaretle.
5. Kuralları belirle: ürün sahibi soruları cevaplar ama tahmin yapmaz; kartlar aynı anda açılır; madde başına zaman kutusu (ör. 3-5 dakika); kararlaştırılan eşiğin (ör. 13) üzerindeki madde bölünmeli veya spike yapılmalı.
6. Her turda: maddeyi oku, netleştir, kartları aç, en yüksek ve en düşük tahmini verenler açıklasın, bir kez yeniden oyla. Dağılım hâlâ iki adımdan fazlaysa varsayımları kaydet ve maddeyi beklemeye al.
7. Her madde için kaydet: boyut, dağılım (ilk oylamanın en düşük-en yüksek değeri), temel varsayımlar ve takip işleri (bölme, spike, ürün sahibine soru).
8. Sonda grubu referans merdivenine göre tutarlılık açısından gözden geçir; aykırı değerleri düzelt.
9. Toplam boyutu, bölünmesi veya spike yapılması gereken maddeleri ve açık soruları özetle; puanları saate veya tarihe çevirme.
10. Kullanıcının hedefi devam ediyorsa fazla büyük maddeler için `story-splitting`, seçim için `iteration-planning`, öngörü için `velocity-analysis` öner.

## Çıktı formatı
```markdown
# Tahmin Oturumu – <ekip>, <tarih>
Amaç: <...> · Teknik: <poker/benzerlik/tişört> · Ölçek: <...>

## Referans Merdiveni
| Boyut | Referans madde | Neden bu boyutta |
|---|---|---|

## Oturum Kuralları
- ...

## Sonuçlar
| Madde | Boyut | İlk oy dağılımı | Temel varsayımlar | Takip |
|---|---|---|---|---|

## Bölünmeli / Spike Gerekli
- <madde> – <neden>

## Ürün Sahibine Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Teknik, madde sayısına ve zaman kutusuna uygun.
- [ ] Bir referans merdiveni var; geçici kalibrasyon bu şekilde etiketlendi.
- [ ] Asistan hiçbir boyut uydurmadı; tahmin edilmemiş maddeler `[TBD]` olarak işaretli.
- [ ] Geniş dağılımlar ortalaması alınarak kapatılmadı, kaydedilen varsayımlarla açıklandı.
- [ ] Eşiğin üzerindeki maddeler bölmeye veya spike'a yönlendirildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Birbirinden uzak oyların ortalamasını almak. Farklılık asıl sinyaldir; tartış ve varsayımı kaydet.
- Puanları saate çevirmek veya ekipler arasında puan karşılaştırmak. Göreli boyutlar ekibe özeldir.
- Kimsenin anlamadığı maddeleri tahmin etmek. Dur ve maddeyi iyileştirmeye geri gönder.
- En kıdemli kişinin önce açıklamasına veya çapa atmasına izin vermek. Kartları her zaman aynı anda aç.

## Örnek
Girdi: "Boyutlandırılmamış 25 onboarding hikayesi, 1 saat, yeni ekip, referans yok."

Çıktıdan bir bölüm:
- Teknik: sessiz benzerlik gruplaması (20 dk) → yalnızca tartışmalı maddeler için poker (30 dk) → tutarlılık turu (10 dk).
- Referans: "Hoş geldin e-postası metnini değiştir" = 2 (geçici kalibrasyon).
- Sonuç: "Kimlik belgesi yükleme" | 13 | 5-20 | harici bir doğrulama servisi varsayılıyor `[teyit et]` | Sağlayıcı API'si için spike.
