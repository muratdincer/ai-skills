---
name: ml-problem-framing
description: "Bir iş ihtiyacını makine öğrenmesi problemi olarak tanımlar; desteklenen karar, tahmin hedefi ve etiket, tahminin birimi ve zamanı, tahmin anında mevcut öznitelikler, başarı metrikleri (çevrim dışı ve iş), taban çizgisi, veri fizibilitesi ve devam/dur kararı. Biri \"X'i tahmin etmek için ML/YZ kullanalım\" dediğinde, herhangi bir veri çalışması veya model seçimi başlamadan önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: ml-ai-engineer
  area: ml
  title: "ML problemini tanımlama"
  related: "ai-use-case-assessment, feature-engineering-plan, model-evaluation-report, analysis-plan, problem-statement"
  prompt: "Bunu bir ML problemi olarak tanımla: tahsilat ekibi, faturasını zamanında ödemeyecek müşterileri tahmin edip onları daha erken aramak istiyor."
---

# ML Problemini Tanımlama

## Amaç
Belirsiz bir "X için ML kullanalım" fikrini etiketi, kararı, taban çizgisi ve başarı kriterleri olan, kesin ve test edilebilir bir problem tanımına dönüştürmek. Böylece ekip, modellemeye yatırım yapmadan önce ML'in gerekçeli olup olmadığını ve "yeterince iyi"nin ne demek olduğunu bilir.

## Ne zaman kullanılır
- Bir iş ekibi tahmin, sınıflandırma, sıralama veya öngörü yeteneği istediğinde.
- Bir veri bilimi projesi başlatılırken veya yeniden kapsamlandırılırken.
- Bir model var ama neyi optimize ettiği konusunda kimse hemfikir değilken.

## Ne zaman kullanılmaz
- Soru, bir YZ girişiminin değer, risk ve hazırlık açısından yapmaya değer olup olmadığıysa `ai-use-case-assessment` kullanılır.
- Problem üretken nitelikteyse (metin, özet, sohbet) `prompt-design` veya `rag-design` kullanılır.
- İhtiyaç tek seferlik açıklayıcı bir analizse `analysis-plan` kullanılır.

## Girdiler
Zorunlu:
- İş ihtiyacı ve tahminin değiştireceği karar veya süreç.

İsteğe bağlı, kaliteyi artırır:
- Mevcut veri kaynakları ve geçmiş verinin uzunluğu.
- Mevcut süreç ve performansı (örtük taban çizgisi).
- Hata maliyetleri, hacim, gecikme ve mevzuat kısıtları.

Karar veya süreç yoksa sor; karar olmadan ML problemi tanımlanmış sayılmaz.

## Süreç
1. Kararı yaz: kim, neye göre, ne zaman aksiyon alıyor ve tahminle neyi farklı yapıyor.
2. Hedefi kesin tanımla: varlık, olay, gözlem penceresi ve etiket kuralı (ör. "vade tarihinden 15 günden fazla sonra ödenen fatura"). Etiket gecikmesini ve etiket gürültüsünü not et.
3. Tahmin anını tanımla: model ne zaman çağrılıyor ve o anda hangi veri mevcut; bu, sızıntı (leakage) sınırını belirler.
4. ML görev tipini seç (ikili/çok sınıflı sınıflandırma, regresyon, sıralama, zaman serisi tahmini, anomali tespiti) ve karardan yola çıkarak gerekçelendir.
5. ML olmayan bir taban çizgisi tanımla (mevcut kural, sezgisel yöntem, önceki dönem değeri) ve ulaştığı metriği ya da `[BİLİNMİYOR]` yaz.
6. Başarıyı tanımla: karara uygun çevrim dışı metrik (ör. top-k kapasitede precision, sabit precision'da recall, MAE, kalibrasyon) ve hedefiyle iş KPI'ı. Yanlış pozitif ve yanlış negatifin maliyetini yaz.
7. Fizibiliteyi değerlendir: etiket hacmi ve sınıf dengesi, mevsimselliğe göre geçmiş uzunluğu, özniteliklerin varlığı, veri erişimi ve gizlilik kısıtları (KVKK/GDPR, hukuki dayanak, hassas nitelikler).
8. Riskleri belirle: geri besleme döngüleri (modelin aksiyonları gelecekteki etiketleri değiştirir), korunan gruplarda adillik, kavram kayması, açıklanabilirlik gereksinimleri, olumsuz kararların otomasyonu.
9. Dağıtım biçimini tanımla: toplu mu gerçek zamanlı mı, gecikme, hacim, döngüde insan, model erişilemezken yedek yol.
10. Belirsizliği azaltacak en küçük deneyle birlikte devam / dur / keşif çalışması (spike) önerisi ver.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Kullanıcının hedefi devam ediyorsa devam kararında `feature-engineering-plan`, iş gerekçesi hâlâ açıksa `ai-use-case-assessment` öner.

## Çıktı formatı
```markdown
# ML Problem Tanımı: <ad>
| Alan | Değer |
|---|---|
| Desteklenen karar | <kim, ne zaman, ne yapıyor> |
| Görev tipi | ... |
| Tahmin anı | <tetikleyici, veri kesim noktası> |
| Hedef / etiket | <kesin kural, pencere> |
| Tahmin birimi | ... |

## Taban Çizgisi
<mevcut yaklaşım ve performansı veya [BİLİNMİYOR]>

## Başarı Kriterleri
- Çevrim dışı: <metrik, eşik>
- İş: <KPI, hedef veya [TBD]>
- Hata maliyetleri: YP = ..., YN = ...

## Fizibilite
| Konu | Durum | Notlar |
|---|---|---|
| Etiket hacmi / denge | ... | ... |
| Tahmin anında öznitelik varlığı | ... | ... |
| Veri erişimi / gizlilik | ... | ... |

## Riskler
- ...

## Dağıtım Biçimi
<toplu/gerçek zamanlı, gecikme, insan onayı, yedek yol>

## Öneri
Devam / Dur / Spike: <en küçük sonraki deney>

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Tahmin somut bir aksiyona ve aktöre bağlı.
- [ ] Etiket kuralı kesin ve geçmiş veriden hesaplanabilir.
- [ ] Girdi olarak yalnızca tahmin anında mevcut veri varsayıldı.
- [ ] ML olmayan bir taban çizgisi tanımlandı.
- [ ] Çevrim dışı metrik iş hata maliyetlerini ve kapasiteyi yansıtıyor.
- [ ] Gizlilik, adillik ve geri besleme döngüsü riskleri ele alındı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Dengesiz sınıflarda accuracy'yi optimize etmek. Kapasiteye (precision@k) ve maliyete bağlı metrikler kullan.
- Karar anından çok sonra bilinen bir etiketi, etiket gecikmesini hesaba katmadan tanımlamak.
- Taban çizgisini atlamak; birçok "ML başarısı" basit bir kural tarafından geçilir.

## Örnek
Girdi: "Tahsilat ekibi zamanında ödemeyecek müşterileri tahmin edip daha erken aramak istiyor."

Çıktıdan bir bölüm:
- Karar: Tahsilat ekibi her sabah, vadeye 7 gün kala riske göre sıralanmış ilk N açık faturayı arar.
- Etiket: Vadeden 15 günden fazla sonra ödenen veya 45. günde ödenmemiş fatura `[eşiği finansla teyit et]`.
- Çevrim dışı metrik: N = günlük arama kapasitesi `[BİLİNMİYOR]` olmak üzere precision@N; taban çizgisi = mevcut kural "geçen çeyrek geç ödeyen müşteriler".
- Risk: Aramalar ödeme davranışını değiştirir, dolayısıyla gelecekteki etiketler modelden etkilenir; rastgele bir kontrol grubu (holdout) tut.
