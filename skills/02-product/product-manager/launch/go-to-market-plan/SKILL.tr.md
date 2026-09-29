---
description: Bir ürün veya büyük özellik için lansman seviyesi, hedef segment ve alıcı, konumlandırma ve mesajlar, kanallar, fiyat ve paketleme bağlantıları, hazırlık kapılarıyla zaman çizelgesi, satış/destek hazırlığı ve lansman başarı metriklerini kapsayan bir pazara çıkış (GTM) planı yazar. Bir ürün, özellik veya pazar girişi lansmana yaklaşıyorsa, biri GTM veya lansman planı istiyorsa ya da pazarlama, satış ve destek tek ve uyumlu bir plana ihtiyaç duyuyorsa kullanılır.
related: positioning-statement, release-announcement, pricing-analysis, competitive-battle-card, communication-plan
prompt: Yapay zeka destekli fatura eşleştirme modülümüzü mevcut orta ölçekli ERP müşterilerine sunmak için bir pazara çıkış planı yaz.
---

# Pazara Çıkış Planı

## Amaç
Ürün, pazarlama, satış, destek ve operasyonu lansmanın kimi hedeflediği, ne söylediği, onlara nasıl ulaştığı, her ekibin ne zaman hazır olması gerektiği ve başarının nasıl değerlendirileceği konusunda hizalamak. Böylece lansman bir sürüm tarihi değil, koordineli bir olay olur.

## Ne zaman kullanılır
- Yeni bir ürün, büyük bir özellik, yeni bir segment veya yeni bir pazar lansmana yaklaşıyorsa.
- Birden çok ekip (pazarlama, satış, müşteri başarısı, destek, hukuk) paralel hazırlanmalıysa.
- Yönetim, lansmanın nasıl benimsenme veya gelir üreteceğini soruyorsa.

## Ne zaman kullanılmaz
- Yalnızca temel konumlandırma belirsizse önce `positioning-statement` kullanılır.
- Yalnızca müşteriye yönelik duyuru metni gerekiyorsa `release-announcement` kullanılır.
- Sürüm iç kullanıma yönelik veya küçük bir değişiklikse ve yalnızca sürüm notu gerekiyorsa `release-notes` kullanılır.

## Girdiler
Zorunlu:
- Lansmanı yapılan şey (yetenek ve ana fayda), hedef müşteriler ve öngörülen lansman dönemi.

İsteğe bağlı, kaliteyi artırır:
- Konumlandırma, rakip bağlamı, fiyat/paketleme kararları, iş hedefi.
- Kullanılabilir kanallar ve bütçe, satış modeli (self-servis, satış odaklı, iş ortağı), mevzuat kısıtları.

Hedef müşteri veya lansman kapsamı yoksa sor. Bütçe, tarih veya hedef uydurma; `[TBD]` olarak işaretle.

## Süreç
1. Müşteri etkisi, gelir potansiyeli ve rekabetçi öneme göre lansman seviyesini belirle (ör. Seviye 1 pazarı etkileyen, Seviye 2 dikkat çekici, Seviye 3 sessiz); seviye sonraki her adımın eforunu ölçekler.
2. Hedefi tanımla: segment, ideal müşteri profili (ICP), alıcı / kullanıcı / etkileyici rolleri, mevcut ve yeni müşteriler. Şimdilik açıkça hedef dışı bırakılan segmenti adlandır.
3. Konumlandırmayı tek satırda yaz ve bir mesaj evi türet: ana mesaj, her biri kanıt noktalı 3 destek sütunu. Kanıtlanmamış iddiaları `[VARSAYIM]` olarak işaretle ya da çıkar.
4. Fiyat ve paketleme temas noktalarına karar ver: dahil, eklenti, yeni paket, deneme/pilot koşulları; hâlâ açık kararları sahibiyle işaretle.
5. Kanalları hedef kitle ve huni aşamasına (farkındalık, değerlendirme, dönüşüm, genişleme) göre seç: ör. uygulama içi, mevcut müşterilere e-posta, webinar, iş ortakları, satış ulaşımı, basın. Her birini kitle uyumuyla gerekçelendir.
6. Hazırlığı planla: satış sunumu ve demo, itiraz karşılama, rekabet kartı, destek SSS'si ve sorun giderme, dokümantasyon, fiyat/teklif kurulumu, iş ortağı bilgilendirmeleri.
7. Zaman çizelgesini lansman gününden geriye doğru, sahipleri olan hazırlık kapılarıyla kur (ör. T-6 hafta mesajlar kilitli, T-2 hafta hazırlık tamam, T-1 hafta go/no-go); gerekirse beta veya erken erişim aşamasını ekle.
8. Lansman başarı metriklerini farklı ufuklarda tanımla: öncü (erişim, deneme, demo talebi), benimsenme (hedef hesaplarda aktivasyon), iş (satış fırsatı hattı, genişleme geliri, kayıp etkisi). Başlangıç değerleri ve hedefler verilmişse yaz, yoksa `[TBD]`.
9. Riskleri ve önlemleri (hazırlık gecikmesi, kapasite, uyum incelemesi, rakip tepkisi) ve go/no-go kriterlerini listele.
10. Çıkarımları `[VARSAYIM]` olarak işaretle. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: konumlandırma zayıfsa `positioning-statement`, müşteri mesajı için `release-announcement`, satış için `competitive-battle-card`, ayrıntılı sıralama için `communication-plan`.

## Çıktı formatı
```markdown
# Pazara Çıkış Planı: <ürün/özellik> · lansman dönemi <...> · Seviye <1/2/3>

## Hedef
- Segment / ICP: ... · Alıcı / kullanıcı / etkileyici: ... · Şimdilik hedef dışı: ...

## Konumlandırma ve Mesaj Evi
- Tek satır: ...
- Sütunlar: 1. <mesaj> – kanıt: <...> 2. ... 3. ...

## Fiyat ve Paketleme
- ...

## Kanallar
| Kitle | Aşama | Kanal | Neden | Sahip |
|---|---|---|---|---|

## Hazırlık (Enablement)
| Ekip | Materyal / eğitim | Sahip | Tarih |
|---|---|---|---|

## Zaman Çizelgesi ve Hazırlık Kapıları
| Ne zaman | Kilometre taşı / kapı | Sahip | Çıkış kriteri |
|---|---|---|---|

## Başarı Metrikleri
| Ufuk | Metrik | Başlangıç | Hedef |
|---|---|---|---|

## Riskler ve Go/No-Go Kriterleri
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Lansman seviyesi belirtildi ve efor ona uygun.
- [ ] Hedef segment ve alıcı/kullanıcı rolleri somut; hedef dışı bir segment adlandırıldı.
- [ ] Her mesaj sütununun bir kanıt noktası var ya da `[VARSAYIM]` olarak işaretli.
- [ ] Her ekibin sahibi ve tarihi olan (veya `[TBD]`) hazırlık maddeleri var.
- [ ] Başarı metrikleri öncü, benimsenme ve iş ufuklarını kapsıyor; uydurulmuş hedef yok.
- [ ] Go/no-go kriterleri ve hazırlık kapıları açık.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- GTM'i bir pazarlama kontrol listesi saymak. Satış ve destek hazır değilse talep, kaybedilen fırsatlara ve destek kayıtlarına dönüşür.
- "Herkese" lansman yapmak. Adı konmuş bir ICP ve açık bir hedef dışı tanımı, kıt kanalları odaklar.
- Yalnızca lansman günündeki erişimi ölçmek. Lansmandan sonraki haftalar için benimsenme ve iş metriklerini planla.

## Örnek
Girdi: "Mevcut orta ölçekli ERP müşterileri için yapay zeka destekli fatura eşleştirme modülü."

Çıktıdan bir bölüm:
- Seviye 2: mevcut müşteri tabanı için dikkat çekici bir eklenti; yeni pazar girişi yok.
- Hedef: yüksek fatura hacmi işleyen mevcut müşterilerdeki finans operasyon yöneticileri `[VARSAYIM: eşik TBD]`; alıcı: CFO; şimdilik hedef dışı: yeni müşteri adayları.
- Sütun: "Ay sonunu daha hızlı kapatın" – kanıt: pilot sonuçları `[TBD, beta müşterilerinden]`.
- T-2 hafta kapısı: destek ekibi düşük güvenli eşleşmeleri açıklama konusunda eğitildi; SSS verinin işlendiği yeri kapsıyor (KVKK/GDPR sorusu).
- İş metriği: hedef hesaplarda eklenti bağlanma oranı, başlangıç 0, hedef `[TBD]`.
