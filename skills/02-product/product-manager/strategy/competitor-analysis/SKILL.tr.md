---
description: Doğrudan, dolaylı ve ikame rakipleri hedef segment, karşılanan iş, özellikler, fiyatlandırma ve konumlandırma açısından karşılaştırır; tarihli kaynaklarla boşlukları, tehditleri ve farklılaşma fırsatlarını belirler. Bir pazara girerken, strateji veya konumlandırma planlarken, satış kayıplarına hazırlanırken ya da ürünün rakiplerle nasıl kıyaslandığı sorulduğunda kullanılır.
related: market-analysis, positioning-statement, pricing-analysis, product-strategy-one-pager, swot-analysis
prompt: Masraf yönetimi uygulamamızı Türk KOBİ'lerinin kullandığı başlıca rakiplerle karşılaştır ve nerede farklılaşabileceğimizi göster.
---

# Rakip Analizi

## Amaç
Ürünün, müşterilerin gerçekten değerlendirdiği alternatiflerle nasıl kıyaslandığını kanıtlarla göstermek ve karşılaştırmayı kararlara dönüştürmek: nerede farklılaşılacak, nerede eşitlik yeterli, nerede hiç rekabet edilmeyecek.

## Ne zaman kullanılır
- Strateji, konumlandırma veya yol haritası planlamasında.
- Belirli bir rakibe tekrar tekrar satış veya müşteri kaybedildiğinde.
- Yeni bir segmente girerken veya satış karşılaştırma kartları (battlecard) hazırlanırken.

## Ne zaman kullanılmaz
- Genel pazar büyüklüğü ve segmentler gerekiyorsa `market-analysis` kullanılır.
- Nihai konumlandırma cümlesi gerekiyorsa `positioning-statement` kullanılır.
- Kendi durumunuzun genel güçlü/zayıf yön görünümü gerekiyorsa `swot-analysis` kullanılır.

## Girdiler
Zorunlu:
- Kendi ürününüz ve hedef segment; en azından rakip adları veya aranacak problem alanı.

İsteğe bağlı, kaliteyi artırır:
- Kazanma/kaybetme notları, satış geri bildirimleri, müşteri görüşmeleri, yorumlar.
- Herkese açık fiyat sayfaları, ürün dokümanları, analist notları (erişim tarihleriyle).

Ürün veya segment yoksa sor. Kaynak gösteremediğin rakip bilgisini kesin bilgi gibi yazma; tarihle birlikte `[DOĞRULANMADI]` olarak işaretle.

## Süreç
1. Rakipleri üç halkada listele: doğrudan (aynı iş, aynı segment), dolaylı (aynı iş, farklı yaklaşım) ve ikameler (tablolar, ajanslar, hiçbir şey yapmamak).
2. Müşterilerin ne sıklıkla değerlendirdiğine göre ayrıntılı analiz için 3-6 tanesini seç.
3. Her biri için şunları kaydet: hedef segment, temel iş, ana yetkinlikler, fiyat modeli ve giriş fiyatı, pazara çıkış yaklaşımı, konumlandırma iddiası, belirgin güçlü ve zayıf yönler. Kaynağı ve erişim tarihini not et.
4. Karşılaştırmayı her özellik üzerinden değil, hedef segmentin satın alma kriterleri açısından önemli yetkinlikler üzerinden yap. Daha iyi / Eşit / Daha kötü / Yok olarak derecelendir.
5. Konumlandırmayı alıcılar için anlamlı iki eksende haritala (ör. derinlik-kolaylık, fiyat-kapsam).
6. Boşlukları belirle: kimsenin iyi karşılamadığı ihtiyaçlar ve yeterince hizmet alamayan segmentler.
7. Tehditleri belirle: rakiplerin nereye gittiği (yeni lansmanlar, fiyat değişiklikleri, yatırımlar) ve bunun anlamı.
8. Öneri yap: 1-2 alanda farklılaş, olmazsa olmazlarda eşitliği yakala, diğerlerini bilerek görmezden gel.
9. Kanıt boşluklarını ve nasıl kapatılacaklarını (kazanma/kaybetme görüşmeleri, deneme kayıtları) listele.

## Çıktı formatı
```markdown
# Rakip Analizi: <ürün> — <segment> (<tarih> itibarıyla)
## Rekabet Kümesi
| Halka | Rakip | Neden değerlendiriliyor |
|---|---|---|

## Profiller
### <Rakip>
Segment · Temel iş · Fiyatlandırma · Pazara çıkış · Konumlandırma · Güçlü yönler · Zayıf yönler · Kaynaklar (tarih)

## Satın Alma Kriterlerine Göre Karşılaştırma
| Kriter | Biz | A | B | C |
|---|---|---|---|---|

## Konumlandırma Haritası
<eksenler ve yerleşim>

## Boşluklar, Tehditler ve Öneriler
- Farklılaşılacak alanlar: ...
- Eşitlik gereken alanlar: ...
- Rekabet edilmeyecek alanlar: ...

## Kanıt Boşlukları
- ...
```

## Kalite kontrol listesi
- [ ] "Hiçbir şey yapmamak" dahil ikameler değerlendirildi.
- [ ] Her rakip bilgisinin kaynağı ve tarihi var ya da `[DOĞRULANMADI]` olarak işaretli.
- [ ] Karşılaştırma kriterleri sizin özellik listenizden değil, alıcı önceliklerinden geliyor.
- [ ] Analiz açık farklılaş/eşitle/görmezden gel seçimleriyle bitiyor.
- [ ] Dil olgusal; karalayıcı iddia yok.

## Sık yapılan hatalar
- Sizi iyi gösteren ama alıcının değer verdiği şeyi atlayan özellik sayma tabloları. Satın alma kriterlerine göre ağırlıklandır.
- Analizi kalıcı saymak. Tarih at ve yenileme zamanı planla.
- Rakiplerin yol haritasını kopyalamak. Boşlukları kendi stratejinizi keskinleştirmek için kullan.

## Örnek
Girdi: "Masraf uygulamamız ile Türk KOBİ'lerine yönelik başlıca rakipler."

Çıktıdan bir bölüm:
- İkame: Excel ve WhatsApp'tan gönderilen fiş fotoğrafları — ücretsiz, alışılmış, onay izi yok.
- "e-Arşiv fatura eşleştirme" kriteri: Biz Daha iyi; A Eşit; B Yok `[DOĞRULANMADI, fiyat sayfası 2026-09]`.
- Öneri: Mali müşavir iş birliğinde farklılaş; OCR'da eşitliği yakala; kurumsal kart çıkarma alanında rekabet etme.
