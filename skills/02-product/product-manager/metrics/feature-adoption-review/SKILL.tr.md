---
name: feature-adoption-review
description: "Yayınlanmış bir özelliğin benimsenmesini, tutunmasını ve sonucunu, lansman öncesi belirlenen hedeflere göre erişim-aktivasyon-tutunma-sonuç kırılımı, segment ayrımları ve nitel sinyallerle değerlendirir; sürdür, iyileştir, yaygınlaştır veya kaldır önerisiyle bitirir. Bir sürümden birkaç hafta sonra, lansman sonrası değerlendirmede ya da biri \"bu özelliği kullanan var mı, işe yaradı mı\" diye sorduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: metrics
  title: "Özellik benimsenme analizi"
  related: "kpi-definition, funnel-analysis, feedback-synthesis, benefits-realization, product-sunset-plan"
  prompt: "8 hafta önce yayınladığımız toplu düzenleme özelliğinin benimsenmesini değerlendir; kullanım sayıları ve destek kayıtları burada."
---

# Özellik Benimsenme Analizi

## Amaç
Yayınlanmış bir özelliğin hedeflenen kullanıcılara ulaşıp ulaşmadığını, alışkanlığa dönüşüp dönüşmediğini ve yapılma amacı olan sonucu etkileyip etkilemediğini değerlendirmek; kanıtı, kimsenin harekete geçmediği bir kullanım grafiği yerine net bir karara dönüştürmek.

## Ne zaman kullanılır
- Özellik, hedef kullanıcıların onunla birkaç kez karşılaşacağı kadar süredir yayındaysa (kullanım sıklığına bağlıdır).
- Lansman sonrası veya çeyreklik bir değerlendirme, yayınlanan özelliklerin ne sağladığına dair kanıt istiyorsa.
- Ekip bir özelliğe daha fazla yatırım yapmayı, onu değiştirmeyi ya da kaldırmayı tartışıyorsa.

## Ne zaman kullanılmaz
- Özellik henüz yayında değilse ve başarı ölçütleri belirlenecekse `kpi-definition` kullanılır.
- Soru, çok adımlı bir akışta kullanıcıların nerede düştüğüyse `funnel-analysis` kullanılır.
- Kaldırma kararı verildiyse ve uygulanacaksa `product-sunset-plan` kullanılır.

## Girdiler
Zorunlu:
- Özellik, hedef kullanıcıları ve amaçlanan sonuç ile eldeki kullanım verisi (bir dönem için sayılar, oranlar veya ham olaylar).

İsteğe bağlı, kaliteyi artırır:
- Lansman öncesi hedefler veya hipotez, yaygınlaştırma tarihleri ve maruz kalma (feature flag'ler, segmentler).
- Segment kırılımları, tutunma kohortları, sonuç metriği trendi, geri bildirim, destek kayıtları.

Kullanım verisi veya amaçlanan sonuç yoksa sor. Asla sayı uydurma; yalnızca verilen veriden hesapla ve hesabı göster.

## Süreç
1. Özelliğin hedef kullanıcılarını, amaçlanan işi ve lansman öncesi belirlenen başarı kriterlerini yeniden yaz; hiç yoksa aday kriterleri yeniden oluştur ve `[VARSAYIM]` olarak işaretle (sonradan konan hedefler daha zayıf kanıttır).
2. Uygun kitleyi tanımla: özelliği kullanabilecek kullanıcılar (doğru paket, platform, rol, yaygınlaştırmada maruz kalmış). Benimsenme oranlarının paydası tüm kullanıcılar değil, bu kitledir.
3. Benimsenmeyi aşamalara ayır: erişim/farkındalık (gördü veya açtı), aktivasyon (temel eylemi bir kez tamamladı), tekrar kullanım/tutunma (beklenen sıklıkta yeniden kullandı) ve derinlik (ilgili işlerin özellikle yapılan payı).
4. Her aşamayı dönem ve kohortu belirterek veriden hesapla; aritmetiği göster, eksik aşamaları gereken ölçümlemeyle birlikte `[TBD]` olarak işaretle.
5. Kullanıcı türü, paket, platform ve kohorta (lansman haftası ve sonrası) göre segmentle; özelliğin iyi çalıştığı bir segment ile başarısız olduğu bir segment ara.
6. Sonucu değerlendir: amaçlanan metrik, benimseyenlerde karşılaştırılabilir benimsemeyenlere ya da lansman öncesi trende göre değişti mi? Karıştırıcı etkenleri (mevsimsellik, diğer sürümler, öz seçim) belirt ve kontrollü karşılaştırma olmadan nedensellik iddia etme.
7. Nitel kanıt ekle: geri bildirim temaları, destek kayıtları, satış/müşteri başarısı notları; her birini bir boşluğu açıkladığı aşamaya bağla.
8. Ana darboğazı teşhis et: keşfedilebilirlik, değer, kullanılabilirlik, performans/güvenilirlik veya yanlış segmente uyum.
9. Gerekçesiyle tek bir karar öner: olduğu gibi sürdür, iyileştir (adı konmuş darboğaz + sonraki test), yaygınlaştır (keşfe/dağıtıma yatırım) veya kaldır. Biliniyorsa sürdürmenin maliyetini (bakım, karmaşıklık) ekle.
10. Çıkarımları `[VARSAYIM]` olarak işaretle. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: iyileştirme için `experiment-design` veya `hypothesis-statement`, daha derin nitel çalışma için `feedback-synthesis`, kaldırılacaksa `product-sunset-plan`.

## Çıktı formatı
```markdown
# Özellik Benimsenme Analizi: <özellik> · <tarih>'ten beri yayında · dönem <...>
Hedef kullanıcılar: <...> · Amaçlanan sonuç: <...> · Lansman öncesi hedef: <... veya [VARSAYIM]>

## Uygun Kitle
<tanım ve sayı>

## Benimsenme Aşamaları
| Aşama | Tanım | Değer | Hedef | Durum |
|---|---|---|---|---|
| Erişim | | | | |
| Aktivasyon | | | | |
| Tutunma | | | | |
| Derinlik | | | | |

## Segmentler
| Segment | Aktivasyon | Tutunma | Not |
|---|---|---|---|

## Sonuç Etkisi
- Gözlenen: ... · Karşılaştırma temeli: ... · Karıştırıcı etkenler: ...

## Nitel Sinyaller
- ...

## Teşhis ve Karar
- Darboğaz: ... · Karar: <sürdür/iyileştir/yaygınlaştır/kaldır> – gerekçe
- Sonraki adımlar: ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Benimsenme oranları payda olarak uygun kitleyi kullanıyor.
- [ ] Erişim, aktivasyon, tutunma ve derinlik ayrıldı; eksik olanlar `[TBD]`.
- [ ] Tüm sayılar verilen veriden, görünür aritmetikle geliyor.
- [ ] Sonuç iddiaları karşılaştırma temelini ve karıştırıcı etkenleri belirtiyor; desteksiz nedensellik yok.
- [ ] Sonradan konan hedefler `[VARSAYIM]` olarak etiketli.
- [ ] Değerlendirme tek bir karar ve somut sonraki adımlarla bitiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Kullanıcıların %30'u denedi" sonucunu başarı olarak raporlamak. Tek seferlik deneme meraktır; değeri tutunma ve sonuç gösterir.
- Özelliği yalnızca yöneticiler veya tek bir paket kullanabiliyorken tüm kullanıcılara bölmek. Uygunluğu her zaman tanımla.
- Benimseyenlerin daha iyi sonuçlarını özelliğe bağlamak. Yoğun kullanıcılar her şeyi ilk benimser; benzerle benzeri karşılaştır.

## Örnek
Girdi: "Toplu düzenleme 8 hafta önce yayınlandı. Uygun: 5.000 yönetici; 2.600'ü açtı, 1.300'ü toplu düzenleme tamamladı, 390'ı 4 hafta içinde tekrar kullandı. Geri alma ile ilgili 14 destek kaydı var."

Çıktıdan bir bölüm:
| Aşama | Değer | Durum |
|---|---|---|
| Erişim | 2.600 / 5.000 = %52 | Hedef `[VARSAYIM]` |
| Aktivasyon | 1.300 / 5.000 = %26 (erişimin %50'si) | – |
| Tutunma | 390 / 1.300 = 4 haftada %30 tekrar | Zayıf |
- Teşhis `[VARSAYIM]`: ilk kullanımda değer var, ancak geri alınamaz değişiklik korkusu (geri alma kayıtları) tekrar kullanımı bastırıyor.
- Karar: iyileştir – önizleme ve geri alma ekle, sonraki kohort için tutunmayı yeniden ölç.
