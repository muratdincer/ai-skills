---
name: north-star-metric
description: "Müşterinin üründen aldığı değeri yakalayan ve gelire bağlanan bir Kuzey Yıldızı metriği seçer; bunu sahipleri ve karşı metrikleriyle birlikte kontrol edilebilir 3-5 girdi metriğinden oluşan bir ağaca ayırır. Ürün ekibinin ortak bir değer metriği yoksa, ekipler birbiriyle çelişen sayıları optimize ediyorsa ya da biri \"Kuzey Yıldızımız ne olmalı\" diye soruyor veya ürün için metrik ağacı istiyorsa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: metrics
  title: "Kuzey Yıldızı metriği tanımlama"
  related: "kpi-definition, okr-definition, metric-definition, product-strategy-one-pager, funnel-analysis"
  prompt: "Küçük işletmelere yönelik B2B faturalama SaaS ürünümüz için Kuzey Yıldızı metriği ve girdi metrik ağacı tanımla."
---

# Kuzey Yıldızı Metriği Tanımlama

## Amaç
Ürüne, müşteriye sunulan değeri ifade eden ve sürdürülebilir gelirin öncüsü olan tek bir metrik ile ekiplerin gerçekten etkileyebileceği girdi metriklerini vermek. Böylece yol haritası ve ekip hedefleri aktivite yerine değer etrafında hizalanır.

## Ne zaman kullanılır
- Ekipler farklı sayıları optimize ediyor ve ödünleşimler ortak bir ölçüt olmadan tartışılıyorsa.
- Yeni bir ürün veya strateji, OKR ya da KPI belirlenmeden önce bir değer metriğine ihtiyaç duyuyorsa.
- Mevcut "Kuzey Yıldızı" gelir, kayıt sayısı veya ekiplerin doğrudan etkileyemediği başka bir çıktıysa.

## Ne zaman kullanılmaz
- Formülü, kaynağı ve sahibi belli operasyonel KPI'lar tanımlanacaksa `kpi-definition` kullanılır.
- Çeyreklik hedefler gerekiyorsa `okr-definition` kullanılır (Kuzey Yıldızı ve girdiler onu besler).
- Tek bir metriğin veri ekipleri için kesin teknik tanımı gerekiyorsa `metric-definition` kullanılır.

## Girdiler
Zorunlu:
- Ürün tanımı, birincil müşteri segmenti ve iş modeli (ürünün nasıl para kazandığı).

İsteğe bağlı, kaliteyi artırır:
- Mevcut metrikler ve erişilebilir veri, strateji, bilinen "aha" anı veya temel değer eylemi.
- Ekip yapısı (girdi metriklerini atamak için).

İş modeli veya temel müşteri yoksa sor. Başlangıç değeri veya hedef uydurma; `[TBD]` olarak işaretle.

## Süreç
1. Değer oyununu sınıflandır: dikkat (üründe geçen süre), işlem (tamamlanan alışverişler) veya verimlilik (verimli yapılan iş). Aday metrikleri bu belirler.
2. Temel değer anını tek cümleyle yaz: müşteri geldiği değeri ne zaman alıyor? Kullanıcının söylediğini kendi çıkarımından `[VARSAYIM]` ayır.
3. "<nitelikli müşteri> başına <dönem> içinde <değer eylemi> <sayısı/oranı>" biçiminde 3-5 aday metrik üret (ör. "aktif işletme başına aylık vadesinde ödenen fatura sayısı").
4. Adayları şu ölçütlerle puanla: müşteri değerini ifade ediyor, gelire öncülük ediyor, mevcut veya elde edilebilir veriyle ölçülebilir, herkesçe anlaşılır, ürün çalışmasıyla etkilenebilir, manipüle edilmesi zor. Birini seç; diğerlerinin neden elendiğini kaydet.
5. Kesin tanımla: formül, niteleme kuralları (neyin aktif/geçerli sayıldığı), zaman penceresi, segment kapsamı ve veri kaynağı veya `[TBD]`.
6. Kuzey Yıldızını, çarpılarak veya toplanarak ona ulaşan 3-5 girdi metriğine ayır (genişlik: kaç müşteri; derinlik: her biri ne kadar; sıklık: ne kadar sık; verimlilik/kalite: ne kadar iyi). Her biri bir ekip tarafından kontrol edilebilir olmalı.
7. Manipülasyonu veya zararı ortaya çıkaran 1-2 karşı metrik (koruma) ekle: kalite, müşteri güveni, destek yükü, kayıp (churn).
8. Her girdi metriğine bir sahip ekip ve gözden geçirme sıklığı ata; bilinen öncü-gecikmeli ilişkileri doğrulanacak hipotez olarak not et.
9. Riskleri listele: gecikmeli davranış, mevsimsellik, veri boşlukları, metriğin yanılttığı segmentler.
10. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: girdi metrikleri üzerine hedef koymak için `okr-definition`, operasyonel takip için `kpi-definition`, veri seviyesinde tanım için `metric-definition`.

## Çıktı formatı
```markdown
# Kuzey Yıldızı Metriği: <ürün>
Değer oyunu: <dikkat/işlem/verimlilik> · Temel değer anı: <cümle>

## Kuzey Yıldızı
- Metrik: <ad>
- Formül: <...> · Nitelikli sayılma: <...> · Pencere: <...> · Kaynak: <... veya [TBD]>
- Neden değeri yansıtıyor / gelire öncülük ediyor: <...>

## Değerlendirilen Adaylar
| Aday | Değer | Gelir bağı | Ölçülebilir | Etkilenebilir | Manipülasyon riski | Karar |
|---|---|---|---|---|---|---|

## Girdi Metrik Ağacı
Kuzey Yıldızı
├── Genişlik: <metrik> – sahibi <ekip>
├── Derinlik: <metrik> – sahibi <ekip>
├── Sıklık: <metrik> – sahibi <ekip>
└── Kalite: <metrik> – sahibi <ekip>

## Karşı Metrikler
- <metrik> – <...> riskine karşı korur

## Riskler, Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Kuzey Yıldızı gelir, kayıt veya ham aktiviteyi değil, müşteriye sunulan değeri ölçüyor.
- [ ] Formül, niteleme kuralı ve zaman penceresi belirsizlik içermiyor.
- [ ] Her girdi metriği adı belli bir ekip tarafından kontrol edilebiliyor ve mantıksal olarak Kuzey Yıldızını yürütüyor.
- [ ] Manipülasyona karşı en az bir karşı metrik var.
- [ ] Başlangıç değeri veya hedef uydurulmadı; eksik veri `[TBD]`.
- [ ] Elenen adaylar gerekçeleriyle listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Değer sunulmadan da büyüyen bir gösteriş metriği (kayıtlı kullanıcı, sayfa görüntüleme) seçmek. Bir değer eylemi ve nitelikli müşteri şartı koy.
- Kuzey Yıldızı olarak geliri seçmek. Gelir değerin gerisinden gelir; onu Kuzey Yıldızının öngörmesi gereken iş sonucu olarak tut.
- Sahibi olmayan girdi metrikleri. Her birini bir ekibe eşle, yoksa kıpırdamaz.

## Örnek
Girdi: "Küçük işletmelere yönelik B2B faturalama SaaS."

Zayıf: "Aylık aktif kullanıcı."
Güçlü, bir bölüm:
- Değer oyunu: verimlilik. Temel değer anı `[VARSAYIM]`: işletme, ürün üzerinden gönderdiği bir fatura için ödeme alır.
- Kuzey Yıldızı: aktif işletme başına aylık vadesinde ödenen fatura sayısı.
- Girdiler: ayda ≥1 fatura gönderen işletmeler (genişlik); işletme başına fatura (derinlik); online ödeme bağlantılı fatura payı (verimlilik); otomatik hatırlatma oranı (kalite).
- Karşı metrik: 1.000 fatura başına hatırlatma e-postalarıyla ilgili müşteri şikayeti.
