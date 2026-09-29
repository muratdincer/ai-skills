---
name: portfolio-prioritization
description: "Bir proje veya girişim portföyünü değer, stratejik uyum, risk ve efor üzerinden puanlayarak önceliklendirir; sıralamayı gerçek kapasite ve bağımlılıklarla sınar ve her biri için gerekçeli fonla / sıraya al / durdur önerisi üretir. Kapasiteden fazla girişim olduğunda, yıllık veya çeyreklik portföy planlamasında, yeni bir talebin yerleştirilmesi gerektiğinde ya da yönetim \"neyi fonlayalım, neyi durduralım\" diye sorduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: program-pmo
  area: portfolio
  title: "Proje portföyü önceliklendirme"
  related: "decision-matrix, cost-benefit-analysis, okr-definition, program-roadmap, steering-committee-pack"
  prompt: "Önümüzdeki yıl için bu 12 girişimi önceliklendir; yaklaşık 6 teslimat ekibimiz var ve strateji dijital satışı büyütmek ve işletme maliyetini düşürmek."
---

# Proje Portföyü Önceliklendirme

## Amaç
Birbiriyle yarışan girişimler listesini şeffaf ve kapasiteye sığan bir sıralamaya, her biri için net bir fonla, sıraya al veya durdur kararına dönüştürmek. Böylece yönetim, kurumun sınırlı teslimat kapasitesini stratejiye en iyi hizmet eden işlere ayırır.

## Ne zaman kullanılır
- Talebin kapasiteyi aştığı yıllık veya çeyreklik portföy planlamasında.
- Önemli yeni bir girişimin eklenmesi ve bir şeylerin yer değiştirmesi gerektiğinde.
- Portföy birikerek büyüdüyse ve durdur/devam et gözden geçirmesine ihtiyaç varsa.

## Ne zaman kullanılmaz
- Öğeler tek bir ürün içindeki özellikler veya backlog öğeleriyse `backlog-prioritization` veya `requirements-prioritization` kullanılır.
- Tek bir girişimin iş gerekçesi hazırlanıyorsa `cost-benefit-analysis` veya `feasibility-study` kullanılır.
- Yalnızca birkaç seçenek arasında tek bir tercih gerekiyorsa `decision-matrix` kullanılır.

## Girdiler
Zorunlu:
- Her biri için kısa açıklamasıyla girişimler listesi.
- Portföyün hizmet etmesi gereken stratejik hedefler (ya da etiketlenerek çıkarım yapma izni).

İsteğe bağlı, kaliteyi artırır:
- Değer, maliyet/efor, süre tahminleri ve her birinin ihtiyaç duyduğu ekip veya yetkinlikler.
- Planlama dönemi için ekip veya yetkinlik bazında kullanılabilir kapasite.
- Zorunlu işler (mevzuat, sözleşme, destek sonu), bağımlılıklar, devam eden işlerin durumu ve batık maliyet.
- Kurumun mevcut puanlama modeli veya ağırlıkları.

Liste veya hedefler eksikse sor. Eksik tahminleri `[BİLİNMİYOR]` olarak işaretle ve sıfır puanlamak yerine görünür tut.

## Süreç
1. Listeyi standartlaştır: her girişim için sahip, hizmet ettiği hedef, aşama (fikir, onaylı, devam ediyor) ve tek satırlık sonuç içeren bir satır. Tekrarları birleştir, ayrılabilir kapsamları gizleyen paketleri böl.
2. Zorunlu işleri (mevzuat, sözleşme, güvenlik, destek sonu) isteğe bağlı olanlardan ayır; zorunlu işler kapasiteyi önce kullanır ama yine de boyutlandırılır.
3. Puanlama kriterlerini ve ağırlıkları kullanıcıyla netleştir ya da varsayılan bir model önerip `[VARSAYIM]` olarak etiketle: iş değeri, stratejik uyum, zaman kritikliği, risk azaltma/fırsat yaratma, teslimat riski (ters), efor/maliyet. Puanların karşılaştırılabilir olması için her kriterde 1-5 çıpaları tanımla.
4. Her girişimi puanla ve her puanın dayandığı kanıtı veya tahmini belirt. Çıkarıma dayanan puanları `[VARSAYIM]` olarak işaretle ve güveni Düşük/Orta/Yüksek olarak yaz.
5. Ağırlıklı puanı ve efor biliniyorsa değer/efor oranını hesapla (ör. WSJF tarzı gecikme maliyeti bölü büyüklük). Formülü görünür tut.
6. Duyarlılığı kontrol et: bir ağırlık makul ölçüde değişse veya düşük güvenli puanlar bir puan oynasa ilk sıralar ve kesme çizgisi değişir mi? Kararsız sıralamaları işaretle.
7. Kapasiteye yerleştir: bağımlılıklara ve devam eden taahhütlere uyarak ekip/yetkinlik bazındaki kapasiteyi sıra düzeninde doldur. Kesme çizgisini puanların bittiği yere değil, kapasitenin bittiği yere çiz.
8. Her öğeye karar ata: Şimdi fonla, Sıraya al (başlama tetikleyicisiyle), Yeniden kapsamla, Durdur/Başlatma. Durdurma önerirken batık maliyeti yok say; bunun yerine çıkış maliyetini yaz.
9. Ödünleşimleri özetle: kurumun açıkça yapmayacağı işler ve sonuçta yeterince desteklenmeyen hedefler.
10. Varsayımları, veri boşluklarını ve portföy sahibinden veya kuruldan beklenen kararları listele.
11. Hedef devam ediyorsa fonlanan işleri sıralamak için `program-roadmap`, kararları kurula taşımak için `steering-committee-pack` veya fayda takibini kurmak için `benefits-realization` öner.

## Çıktı formatı
```markdown
# Portföy Önceliklendirme: <portföy> — <dönem>
Hedefler: <liste> · Kapasite: <ekip/FTE/bütçe veya [BİLİNMİYOR]>

## Puanlama Modeli
| Kriter | Ağırlık | 1 = | 5 = |
|---|---|---|---|

## Sıralı Portföy
| Sıra | Girişim | Zorunlu | Değer | Uyum | Zaman krit. | Risk azalt. | Teslimat riski | Efor | Ağırlıklı | Güven | Karar |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Kapasite Uyumu
| Ekip / yetkinlik | Mevcut | Talep (fonlanan) | Açık |
|---|---|---|---|
Kesme çizgisi: <girişim> sonrası

## Duyarlılık Notları
## Ödünleşimler (yapmayacaklarımız)
## Varsayımlar ve Veri Boşlukları
- [VARSAYIM] ...
## Gereken Kararlar
1. <karar> — <kim> — <ne zamana kadar>
```

## Kalite kontrol listesi
- [ ] Puanlama çıpaları ve ağırlıklar açık; üzerinde uzlaşıldı veya `[VARSAYIM]` olarak etiketli.
- [ ] Her puanın bir kanıtı ya da varsayımı ve güven düzeyi var; eksik veri sıfır değil `[BİLİNMİYOR]`.
- [ ] Zorunlu işler ayrıldı ve boyutlandırıldı.
- [ ] Kesme çizgisi yalnızca puana değil, kapasiteye ve bağımlılıklara dayanıyor.
- [ ] Her girişimin bir kararı var; durdurma kararları batık maliyet mantığı olmadan gerekçelendirildi.
- [ ] Kesme çizgisinin duyarlılığı belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ağırlıklı puanı cevap sanmak. Puanlar kararı besler; kararı kapasite, bağımlılıklar ve risk dengesi verir.
- Her şeyi kısmi kapasiteyle fonlamak. Kapasitenin izin verdiğinden fazla iş başlatmak tüm teslim sürelerini uzatır; bunun yerine sıraya al.
- Girdileri en yüksek sesli sponsorun belirlemesine izin vermek. Çıpalı ölçekler kullan ve yüksek puanların arkasındaki kanıtı iste.

## Örnek
Girdi: "12 girişim, 6 ekip, hedefler: dijital satışı büyütmek, işletme maliyetini düşürmek."

Çıktıdan bir bölüm:
| Sıra | Girişim | Zorunlu | Ağırlıklı | Güven | Karar |
|---|---|---|---|---|---|
| — | e-Fatura mevzuat güncellemesi | Evet | yok | Yüksek | Şimdi fonla (2 ekip, 1. çeyrek) |
| 1 | Mobil ödeme akışı yenileme | Hayır | 4,3 | Orta | Şimdi fonla |
| 2 | Depo yerleşim otomasyonu | Hayır | 4,1 | Düşük `[VARSAYIM: tasarruf tahmini doğrulanmadı]` | Şimdi fonla, keşif sonrası kapı |
| 6 | Sadakat uygulaması v2 | Hayır | 3,2 | Orta | Sıraya al: ödeme ekibi boşalınca başla |

Duyarlılık: stratejik uyum ağırlığı %25'ten %20'ye inerse 5-7. sıralar yer değiştiriyor; kesme çizgisine kurulla birlikte açıkça karar verin.
