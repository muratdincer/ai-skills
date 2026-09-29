---
name: porters-five-forces
description: "Bir sektörü veya pazar segmentini Porter'ın beş gücüyle (rekabet, yeni girenlerin tehdidi, ikame ürünlerin tehdidi, alıcı gücü, tedarikçi gücü) analiz eder; her gücü etkenleri ve kanıtlarıyla puanlar ve yapının kârlılık, konumlandırma ve ürün stratejisi için ne anlama geldiğini çıkarır. Bir pazarın veya segmentin çekiciliği değerlendirilirken, strateji veya giriş kararı hazırlanırken, marj baskısı açıklanırken ya da beş güç veya sektör yapısı analizi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: strategy
  title: "Porter'ın beş gücü analizi"
  related: "pestle-analysis, competitor-analysis, market-analysis, swot-analysis, pricing-analysis"
  prompt: "Türkiye'de orta ölçekli şirketlere yönelik saha servis yönetimi yazılımı segmenti için beş güç analizi yap; bu segmente girip girmemeye karar veriyoruz."
---

# Porter'ın Beş Gücü Analizi

## Amaç
Bir pazar segmentinin neden daha çok veya daha az kârlı ve savunulabilir olduğunu açıklamak ve en güçlü kuvvetleri konumlandırma, fiyatlama, bağımlılık yaratma (lock-in) ve iş ortaklıkları üzerine stratejik tercihlere dönüştürmek.

## Ne zaman kullanılır
- Bir pazara veya segmente girme, büyüme ya da çıkma kararı verilirken.
- Süregelen fiyat veya marj baskısı açıklanırken.
- Platform, kanal veya tedarikçi bağımlılıklarının önemli olduğu ürün stratejisi hazırlanırken.

## Ne zaman kullanılmaz
- İhtiyaç, adı belli rakiplerin özellik bazında karşılaştırmasıysa `competitor-analysis` kullanılır.
- İhtiyaç mevzuat, ekonomi ve toplumun makro taramasıysa `pestle-analysis` kullanılır.
- İhtiyaç pazar büyüklüğünü hesaplamaksa `market-analysis` kullanılır.

## Girdiler
Zorunlu:
- Sektör veya segment tanımı: ne satılıyor, kime ve hangi coğrafyada.

İsteğe bağlı, kaliteyi artırır:
- Kullanıcının kendi konumu (yeni giren veya mevcut oyuncu), bilinen rakipler, ikameler, kilit tedarikçiler/platformlar, fiyatlama ve geçiş verileri, pazar araştırmaları.

Segment tanımsız veya çok genişse ("yazılım") daraltmak için tek bir soru sor. Pazar payı, marj veya sayı uydurma; bilinmeyen değerleri `[BİLİNMİYOR]` olarak işaretle ve hangi kanıtın bunu netleştireceğini belirt.

## Süreç
1. Segment sınırını kesin tanımla: ürün kategorisi, müşteri tipi, coğrafya ve bakış açısı (yeni giren, mevcut oyuncu, yatırımcı).
2. Rekabet: rakiplerin sayısı ve dengesi, büyüme hızı, farklılaşma, sabit maliyet yoğunluğu, çıkış engelleri, fiyat şeffaflığı.
3. Yeni girenlerin tehdidi: ölçek ekonomisi, ağ etkileri, geçiş maliyetleri, sermaye ihtiyacı, kanallara erişim, mevzuat/sertifikasyon, mevcut oyuncuların misillemesi, komşu platformların girişi.
4. İkamelerin tehdidi: müşterinin aynı işi yapmasının diğer yolları (tablolar, hizmetler, kurum içi geliştirme, hiçbir şey yapmamak), göreli fiyat-performans ve geçiş maliyeti.
5. Alıcı gücü: alıcı yoğunlaşması, alım hacmi, fiyat hassasiyeti, geriye entegrasyon imkânı, satın alma olgunluğu, teklifin standartlığı.
6. Tedarikçi gücü: kritik girdilerin yoğunlaşması (bulut, uygulama mağazaları, veri sağlayıcılar, uzman yetenek, entegrasyon ortakları), geçiş maliyeti, ileriye entegrasyon tehdidi.
7. Her güç için en güçlü 2-4 etkeni `[OLGU: kaynak]`, `[VARSAYIM]` veya `[BİLİNMİYOR]` kanıt etiketleriyle listele; Düşük/Orta/Yüksek olarak puanla ve eğilimini (artıyor/sabit/azalıyor) ver. Tamamlayıcıları ve düzenleyicileri altıncı güç olarak değil, değiştirici etken olarak ele al.
8. Sentezle: belirtilen bakış açısı için genel çekicilik ve kârlılığı sınırlayan güçler.
9. Stratejik çıkarımları türet: nerede konumlanmalı, geçiş maliyeti veya farklılaşma nasıl artırılır, hangi bağımlılıklar azaltılmalı, fiyatlama duruşu, iş ortaklıkları; her biri bir güce bağlı.
10. En zayıf puanları doğrulamak için toplanacak kanıtı listele, ardından sonraki beceriyi öner: adı belli rakipler için `competitor-analysis`, fiyat hamleleri için `pricing-analysis` veya iç yetkinliklerle birleştirmek için `swot-analysis`.

## Çıktı formatı
```markdown
# Beş Güç: <segment> – <coğrafya> – <bakış açısı>
**Segment sınırı:** <ürün, müşteri, coğrafya>
**Genel çekicilik:** <Düşük/Orta/Yüksek> – <tek satırlık gerekçe>

| Güç | Puan | Eğilim | Temel etkenler (kanıt etiketi) |
|---|---|---|---|
| Rekabet | Y | ↑ | <etken> [OLGU: ...]; <etken> [VARSAYIM] |
| Yeni girenler | | | |
| İkameler | | | |
| Alıcı gücü | | | |
| Tedarikçi gücü | | | |

## Stratejik Çıkarımlar
| # | Çıkarım / hamle | İlgili güç | Güven |
|---|---|---|---|

## Toplanacak Kanıtlar
- <soru> – <kaynak> – <hangi puanı değiştirir>

## Varsayımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Segment sınırı, farklı bir sınırın puanları değiştireceği kadar belirgin.
- [ ] Her puan kanıt etiketli, adı konmuş etkenlere dayanıyor; pay veya marj uydurulmadı.
- [ ] İkameler ürün dışı alternatifleri de içeriyor (elle iş, hizmetler, kurum içi, hiçbir şey yapmamak).
- [ ] Çıkarımlar belirli güçlere bağlı ve belirtilen bakış açısı için uygulanabilir.
- [ ] En zayıf puanların bir doğrulama adımı var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Yazılım sektörünü" analiz etmek. Fazla geniş bir sınır her gücü Orta yapar ve çıktıyı işe yaramaz kılar.
- Rekabeti analizin tamamı sanmak. En büyük tehdit çoğu zaman bir ikame veya platform tedarikçisidir.
- Durağan fotoğraf. Eğilimi ekle; bugün Düşük ama artan bir güç kararı belirler.

## Örnek
Girdi: "Türkiye'de orta ölçekli saha servis yönetimi yazılımı için beş güç; girip girmemeye karar veriyoruz."

Çıktıdan bir bölüm:
| Güç | Puan | Eğilim | Temel etkenler |
|---|---|---|---|
| İkameler | Y | → | Tablolar ve mesajlaşma uygulamaları birçok firma için "yeterince iyi" [VARSAYIM]; ERP eklenti modülleri [DOĞRULA: hangi üreticiler paket hâlinde sunuyor] |
| Alıcı gücü | O | ↑ | Dağınık alıcılar, ancak yüksek fiyat hassasiyeti ve aylık kolay geçiş [VARSAYIM] |
| Tedarikçi gücü | O | → | Mobil uygulama mağazalarına ve harita/rota API'lerine bağımlılık [OLGU: ürün mimarisi] |

Çıkarım: Geçiş maliyetini artırmak için yerel e-fatura ve muhasebe sistemleriyle entegrasyonda rekabet et (ikameler ve alıcı gücüne karşı). Güven: Orta.
