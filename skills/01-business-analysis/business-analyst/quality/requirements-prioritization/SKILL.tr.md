---
description: "Bir gereksinim setini uygun bir teknikle (MoSCoW, Kano, değer/efor, ağırlıklı puanlama veya gecikme maliyeti) önceliklendirir, kriterleri açıkça ortaya koyar ve her sıralamayı kanıt ve belirtilen varsayımlarla gerekçelendirir. Kapsamın bir tarihe veya bütçeye sığdırılması gerektiğinde, paydaşlar neyin önce geleceği konusunda anlaşamadığında ya da bir sürüm veya MVP kapsamı için savunulabilir bir sıra gerektiğinde kullanılır."
related: "backlog-prioritization, decision-matrix, mvp-scoping, stakeholder-map, requirements-sign-off"
prompt: "İlk sürüm için bu 25 gereksinimi MoSCoW ile önceliklendir; canlıya geçiş tarihimiz sabit."
---

# Gereksinim Önceliklendirme

## Amaç
Gereksinimler için şeffaf ve savunulabilir bir öncelik sırası üretmek; kapsam kararları sesi en çok çıkana göre değil, açık kriterlere göre verilsin. Çıktı yöntemi, kriterleri, sıralamayı ve her yerleşimin gerekçesini gösterir.

## Ne zaman kullanılır
- Kapsam, sabit bir tarih, bütçe veya sürüm için kapasiteyi aşıyorsa.
- Paydaşlar öncelik konusunda anlaşamıyor ve ortak bir zemine ihtiyaç duyuyorsa.
- Bir gereksinim setinin ilk sürüm veya MVP kapsamı belirlenirken.

## Ne zaman kullanılmaz
- Sürekli işleyen bir ürün backlog'u sıralanıyorsa `backlog-prioritization` kullanılır.
- Gereksinimler değil çözüm seçenekleri arasında seçim yapılıyorsa `decision-matrix` kullanılır.
- Projeler portföy düzeyinde sıralanıyorsa `portfolio-prioritization` kullanılır.

## Girdiler
Zorunlu:
- ID ve kısa açıklamalarıyla gereksinim listesi.
- Karar bağlamı: önceliğin ne için olduğu (sürüm, MVP, bütçe kesintisi) ve bağlayıcı kısıt.

İsteğe bağlı, kaliteyi artırır:
- İş hedefleri/OKR'ler, paydaş görüşleri, efor tahminleri, bağımlılıklar, yasal yükümlülükler.
- Tercih edilen teknik veya kurumsal standart.

Karar bağlamı yoksa sor; amacı olmayan öncelik anlamsızdır.

## Süreç
1. Tekniği seç ve nedenini belirt:
   - Katı tarihli, sabit kapsamlı sürüm için MoSCoW; "Must"ı "o olmadan sürüm başarısız, yasa dışı veya güvensiz" diye tanımla.
   - Ürünü müşteri memnuniyeti yönlendiriyorsa Kano (temel, performans, heyecan verici).
   - Tahminler varsa ve hızlı kazanımlar önemliyse değer/efor.
   - Birden fazla kriter ve paydaş dengelenecekse ağırlıklı puanlama.
   - Kalemlerin zamana duyarlılığı çok farklıysa gecikme maliyeti (ve CD3).
2. Kriterleri ve ölçekleri açıkça tanımla (ör. iş değeri 1-5, risk azaltımı 1-5, yasal evet/hayır, efor S/M/L). Ağırlıkları al veya öner; önerilenleri `[VARSAYIM]` olarak işaretle.
3. Önce pazarlık konusu olmayanları ayır: yasal/düzenleyici, sözleşmesel, emniyet, temel güvenlik. Bunlar puandan bağımsız olarak Must'tır (veya en üsttedir).
4. Her gereksinimi bir hedefe, paydaş görüşüne veya veriye dayanan tek satırlık gerekçeyle puanla. Kanıt yoksa `[VARSAYIM]` işaretle.
5. Bağımlılıkları uygula: bir gereksinim, teslimat için bağımlı olduğu bir şeyin üstünde sıralanamaz; sağlayıcı (enabler) kalemleri buna göre yükselt.
6. Dengeyi kontrol et: MoSCoW'da efor verisi varsa Must eforunu kapasitenin yaklaşık %60'ı veya altında tut; aşılırsa işaretle.
7. Sıralı listeyi ve kısıta göre kesim çizgisini üret.
8. Tartışmalı kalemleri, karşı görüşteki paydaşlar ve gereken kararla birlikte listele.
9. Nasıl teyit edileceğini öner: paydaş incelemesi, onay sahibi, yeniden değerlendirme tarihi.
10. Kullanıcı devam etmek isterse kabul edilen öncelikleri temel sürüme bağlamak için `requirements-sign-off` veya Must maddelerinden ilk sürümü çıkarmak için `mvp-scoping` öner.

## Çıktı formatı
```markdown
# Gereksinim Önceliklendirmesi: <kapsam / sürüm>
Karar bağlamı: <amaç, kısıt> · Teknik: <ad> – <neden>

## Kriterler
| Kriter | Ölçek | Ağırlık | Kaynak |
|---|---|---|---|

## Sıralı Gereksinimler
| Sıra | Ger. ID | Başlık | Kategori/Puan | Gerekçe | Bağımlılıklar | Efor |
|---|---|---|---|---|---|---|
--- kesim çizgisi: <kısıt> ---

## Pazarlık Konusu Olmayanlar
- <ID> – <mevzuat / sözleşme referansı>

## Tartışmalı Kalemler
| Ger. ID | Görüşler (kim, ne) | Gereken karar | Karar sahibi |
|---|---|---|---|

## Varsayımlar ve Sonraki Adımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Teknik seçimi karar bağlamıyla gerekçelendirildi.
- [ ] Her yerleşimin gerekçesi var; hiçbiri yalnızca "paydaş istiyor" değil.
- [ ] Yasal ve sözleşmesel kalemler belirlendi ve en başa yerleştirildi.
- [ ] Bağımlılıklar sıralamayla çelişmiyor.
- [ ] Must/üst kalemler kısıta sığıyor ya da taşma açıkça işaretli.
- [ ] Varsayılan ağırlık, değer ve eforlar `[VARSAYIM]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her şeyin "Must" olması. "O olmadan sürüm başarısız olur" testini uygula ve her Must'ı sorgula.
- Tek listede teknikleri karıştırmak (Kano kategorileri ile değer puanları yan yana). Bir ana yöntem seç; diğerleri gerekçeyi besleyebilir.
- Yalnızca efora göre sıralamak. Ucuz kalemler otomatik olarak değerli değildir.

## Örnek
Girdi: Mobil bankacılık sürümü için 6 gereksinim, tarih sabit; R2 yasal bir açık rıza ekranı.

Çıktıdan bir bölüm:
| Sıra | Ger. ID | Başlık | Kategori | Gerekçe |
|---|---|---|---|---|
| 1 | R2 | Açık rıza ekranı | Must | Yasal yükümlülük `[madde referansını teyit et]` |
| 2 | R1 | Biyometrik giriş | Must | Ana akış; mağaza sürümü yeni kimlik doğrulamaya bağlı |
| 5 | R5 | Karanlık mod | Could | Kano'ya göre heyecan verici; hedef bağlantısı yok |
