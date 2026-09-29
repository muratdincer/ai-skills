---
description: Aday bir modeli taban çizgisi ve mevcut modelle karşılaştıran bir model değerlendirme raporu yazar; belirsizlikle genel metrikler, eşik seçimi, kalibrasyon, dilim performansı, hata analizi, adillik ve yayın önerisi. Bir model eğitildiğinde ve canlıya alınmak üzere onaylanması, alternatiflerle karşılaştırılması ya da bir performans şikâyeti sonrası gözden geçirilmesi gerektiğinde kullanılır.
related: ml-problem-framing, model-card, ml-monitoring-plan, feature-engineering-plan, llm-eval-set
prompt: Dolandırıcılık modelimiz v3'ü v2 ile karşılaştıran bir değerlendirme raporu yaz; test seti metrikleri, karışıklık matrisleri ve kanal ile ülke bazında dilim sonuçları ekte.
---

# Model Değerlendirme Raporu

## Amaç
Karar vericilere bir modelin nasıl performans gösterdiğine, nerede başarısız olduğuna ve mevcut olandan daha iyi olup olmadığına dair dürüst ve tekrarlanabilir bir tablo sunmak. Böylece yayın kararı tek bir manşet metriğe değil kanıta dayanır.

## Ne zaman kullanılır
- Yeni veya yeniden eğitilmiş bir model yayın adayı olduğunda.
- Birden fazla model varyantının karşılaştırılması gerektiğinde.
- Kullanıcılar kötü tahminlerden şikâyet ettiğinde ve modelin yeniden değerlendirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Problem, etiket ve başarı metriği tanımlı değilse `ml-problem-framing` kullanılır.
- Model, puanlama kriterleriyle değerlendirilen bir LLM özelliğiyse `llm-eval-set` kullanılır.
- Kullanım ve sınırlara dair herkese açık bir özet gerekiyorsa `model-card` kullanılır.

## Girdiler
Zorunlu:
- Aday model için değerlendirme sonuçları (metrikler, karışıklık matrisi veya tahmin özeti) ve karşılaştırma noktası (taban çizgisi veya mevcut model).

İsteğe bağlı, kaliteyi artırır:
- Değerlendirme verisinin tanımı (dönem, büyüklük, bölme yöntemi).
- Dilim sonuçları, kalibrasyon verisi, gecikme ve maliyet ölçümleri.
- İş eşikleri ve hata maliyetleri.

Karşılaştırma noktası yoksa önerinin sınırlı olduğunu belirt ve taban çizgisini iste. Asla metrik değeri uydurma.

## Süreç
1. Değerlendirme kurulumunu tanımla: veri dönemi, bölme (zamana dayalı, gruplu), büyüklük, etiket tanımı ve üretim dağılımından farklar.
2. Birincil ve ikincil metrikleri aday, mevcut model ve taban çizgisi için yan yana, güven aralıklarıyla (bootstrap) ya da en azından örneklem büyüklükleriyle raporla.
3. Çalışma eşiğini iş kısıtlarından (kapasite, YP/YN maliyeti, hedef precision/recall) seç ve gerekçelendir; yalnızca eşikten bağımsız AUC değil, o eşikteki metrikleri göster.
4. Skorlar olasılık olarak kullanılıyorsa kalibrasyonu kontrol et (güvenilirlik eğrisi, Brier skoru, beklenen kalibrasyon hatası).
5. Dilimleri değerlendir: temel segmentler (kanal, bölge, ürün, yeni ve mevcut varlıklar), nadir ama kritik durumlar ve veri kalitesi katmanları. Adayın mevcut modelden kötü olduğu dilimleri işaretle.
6. Hata analizi yap: yanlış pozitif ve yanlış negatiflerden örnek al, nedenlerini kümele (etiket gürültüsü, eksik öznitelik, dağılım kayması) ve düzeltme öner.
7. Kararlar insanları etkiliyorsa adilliği değerlendir: korunan veya vekil gruplar arasında hata oranlarını karşılaştır, kullanılan adillik ölçütünü ve ödünleşimlerini belirt.
8. Sağlamlığı ve operasyonel uygunluğu değerlendir: zaman dilimleri arasında kararlılık, eksik özniteliklere duyarlılık, gecikme, bellek, çıkarım maliyeti.
9. Sızıntı sinyallerini kontrol et: şüpheli derecede yüksek metrikler, baskın tek öznitelik, en güncel dilimde performans düşüşü.
10. Öneri ver: yayınla, koşullu yayınla (gölge, kanarya, sınırlı segment) veya reddet; koşulları ve izleme gereksinimlerini listele.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Kullanıcının hedefi devam ediyorsa yayınlanan modeli belgelemek için `model-card`, yayın koşulları için `ml-monitoring-plan` öner.

## Çıktı formatı
```markdown
# Model Değerlendirmesi: <model> v<x> ve <karşılaştırma>
| Alan | Değer |
|---|---|
| Görev / etiket | ... |
| Değerlendirme verisi | <dönem, n, bölme> |
| Çalışma eşiği | <değer, gerekçe> |
| Öneri | Yayınla / Koşullu / Reddet |

## Genel Metrikler
| Metrik | Taban çizgisi | Mevcut | Aday | %95 GA (aday) |
|---|---|---|---|---|

## Kalibrasyon
...

## Dilim Performansı
| Dilim | n | Mevcut | Aday | Δ | İşaret |
|---|---|---|---|---|---|

## Hata Analizi
| Hata kümesi | Hatalar içindeki pay | Olası neden | Önerilen düzeltme |
|---|---|---|---|

## Adillik
<ölçüt, gruplar, sonuçlar, ödünleşim>

## Sağlamlık ve Operasyon
- Zaman içinde kararlılık: ...
- Gecikme / maliyet: ...

## Koşullar ve İzleme
- ...

## Sınırlamalar
- ...
```

## Kalite kontrol listesi
- [ ] Aday, aynı veri üzerinde taban çizgisi ve/veya mevcut modelle karşılaştırıldı.
- [ ] Metrikler seçilen çalışma eşiğinde, belirsizlik veya n ile gösterildi.
- [ ] Adayın gerilediği dilimler açıkça işaretlendi.
- [ ] Hata analizi yalnızca sayı değil neden veriyor.
- [ ] Adillik değerlendirildi ya da neden uygulanmadığı belirtildi.
- [ ] Tüm sayılar verilen sonuçlardan geliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İş tarafı sabit bir eşik kullanırken yalnızca AUC raporlamak. O eşikteki precision/recall'u raporla.
- Ortalamaların küçük ama kritik dilimlerdeki gerilemeleri gizlemesi.
- Üretimde gelecekteki veri skorlanırken rastgele bölme üzerinde değerlendirme yapmak.

## Örnek
Girdi: Dolandırıcılık v3 ve v2; son 8 haftada (zamana dayalı bölme) PR-AUC 0,61'e karşı 0,57; inceleme kapasitesi eşiğinde precision 0,42'ye karşı 0,39, recall 0,55'e karşı 0,51; kart-yok (card-not-present) diliminde recall 0,62 → 0,58.

Çıktıdan bir bölüm:
- Öneri: Koşullu yayın – 2 hafta gölge modda, ardından kanarya; kart-yok gerilemesi açıklanana kadar tam yayın engellenir.
- Dilim işareti: Genel recall +0,04 iken kart-yok recall -0,04; hata örnekleri eğitimde bulunmayan yeni üye işyeri kategori kodlarını gösteriyor `[teyit et]`.
