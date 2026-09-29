---
description: Her biri 2-5 ölçülebilir anahtar sonuç içeren sonuç odaklı hedefler yazar; başlangıç değeri, hedef, ölçüm kaynağı ve sorumluyu ekler, çıktı odaklı veya ölçülemeyen anahtar sonuçları işaretler. Bir ekip çeyrek veya yarıyıl planladığında, strateji ölçülebilir hedeflere dönüştürülmek istendiğinde ya da OKR yazılması veya gözden geçirilmesi istendiğinde kullanılır.
related: product-strategy-one-pager, north-star-metric, kpi-definition, goal-setting, quarterly-planning
prompt: Yeni müşterilerin değere daha hızlı ulaşması hedefine göre onboarding ekibimiz için 3. çeyrek OKR'larını yaz.
---

# OKR Tanımlama

## Amaç
Stratejiyi, müşteri veya iş davranışındaki değişimi anlatan az sayıda nitel hedef ve nicel anahtar sonuca çevirmek. Böylece ekip kendi işini seçebilir ve başarılı olup olmadığını bilebilir.

## Ne zaman kullanılır
- Bir ürün ekibi veya ürün alanı için çeyreklik ya da yarıyıllık planlamada.
- Strateji veya bahisler var ama ekiplerin ölçülebilir hedefleri yoksa.
- Taslak OKR'lar var ve sonuç odaklılık ile ölçülebilirlik açısından gözden geçirilmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Değişim hedefi değil sürekli sağlık metrikleri gerekiyorsa `kpi-definition` kullanılır.
- Tüm ürün için tek değer metriği gerekiyorsa `north-star-metric` kullanılır.
- Bireysel performans hedefleri gerekiyorsa `goal-setting` kullanılır.

## Girdiler
Zorunlu:
- Ekibin ele alması gereken stratejik niyet veya problem ve dönem.

İsteğe bağlı, kaliteyi artırır:
- Ürün stratejisi, Kuzey Yıldızı ve girdi metrikleri, mevcut başlangıç değerleri.
- Ekip kapsamı ve kapasitesi, hizalanılacak üst seviye OKR'lar.
- Kurumda OKR'ların taahhüt mü yoksa iddialı hedef mi olduğu.

Niyet veya dönem yoksa sor. Bilinmeyen başlangıç değerleri ölçüm aksiyonuyla birlikte `[BİLİNMİYOR]` olur.

## Süreç
1. Stratejik niyeti yeniden ifade et ve değişmesi gereken müşteri veya iş davranışını belirle.
2. 1-3 hedef (objective) yaz: nitel, motive edici, dönemle sınırlı ve ekibin etki alanında.
3. Her hedef için 2-5 anahtar sonucu sonuç olarak yaz: "<metrik> <başlangıç> değerinden <hedef> değerine, <tarih> itibarıyla". "X'i yayına al" gibi çıktılardan kaçın; teslimat kaçınılmazsa girişimlere taşı.
4. Her anahtar sonuca başlangıç değeri, hedef, veri kaynağı ve sorumlu ekle. Başlangıç değeri yoksa `[BİLİNMİYOR]` yaz ve "1-2. haftada başlangıç değerini ölç" ekle.
5. Anahtar sonuçları dengele: büyüme sonucunu kalite veya koruma (guardrail) sonucuyla eşleştir (ör. aktivasyon artsın, yeni hesap başına destek kaydı artmasın).
6. Her OKR'ı taahhüt veya iddialı olarak sınıflandır ve beklenen puanlamayı belirle (ör. iddialı hedefte 0,7 başarıdır).
7. Aday girişimleri anahtar sonuç olarak değil, hipotez olarak ayrı listele.
8. Yukarı (şirket/strateji) ve yana (diğer ekiplere bağımlılıklar) hizalamayı kontrol et.
9. Ara değerlendirme sıklığını ve güven seviyesinin nasıl izleneceğini tanımla.

## Çıktı formatı
```markdown
# OKR'lar: <ekip> — <dönem>
**Stratejik bağlantı:** <strateji/bahis>

## Hedef 1: <nitel hedef>
Tür: Taahhüt / İddialı
| # | Anahtar sonuç | Başlangıç | Hedef | Kaynak | Sorumlu |
|---|---|---|---|---|---|
| AS1 | ... | ... | ... | ... | ... |
Koruma metriği: <kötüleşmemesi gereken metrik>
Aday girişimler: <hipotezler>

## Bağımlılıklar
- ...

## Ara Değerlendirme ve Puanlama
- ...

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Her anahtar sonuç sayı, başlangıç değeri (veya `[BİLİNMİYOR]`) ve tarih içeren bir sonuç.
- [ ] Hiçbir anahtar sonuç görev, lansman veya teslimat değil.
- [ ] Her hedefte en fazla 5 anahtar sonuç, ekipte en fazla 3 hedef var.
- [ ] En az bir koruma metriği kaliteyi veya müşteri güvenini koruyor.
- [ ] Hedef değerler uydurulmadı; üzerinde anlaşılmamış olanlar `[TBD]`.
- [ ] Her anahtar sonucun belirli bir veri kaynağı ve sorumlusu var.

## Sık yapılan hatalar
- Yol haritasını OKR diye yazmak ("v2 onboarding'i yayınla"). "Yayına çıkınca ne değişecek?" diye sor ve onu ölç.
- Ekibin dönem içinde etkileyemeyeceği metrikleri seçmek. Bunun yerine öncü girdi metriklerini seç.
- Başlangıç değeri olmadan hedef koymak. Önce başlangıç ölçümünü planla.

## Örnek
Girdi: "Onboarding ekibi, 3. çeyrek, hedef: yeni müşteriler değere daha hızlı ulaşsın."

Çıktıdan bir bölüm:
- Hedef: Yeni müşteriler ilk başarılı faturalarına zahmetsizce ulaşsın.
- AS1: Kayıttan ilk gönderilen faturaya kadar geçen medyan süre `[BİLİNMİYOR]` değerinden `[TBD]` değerine, 3. çeyrek sonuna kadar (kaynak: ürün analitiği).
- AS2: 7 gün içinde aktive olan yeni hesap oranı %38'den %50'ye `[başlangıç değerini teyit et]`.
- Koruma metriği: Yeni hesap başına onboarding kaynaklı destek kaydı sayısı artmaz.
