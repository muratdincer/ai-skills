---
name: spike-report
description: "Süre sınırlı bir araştırmanın yanıtlaması gereken soruyu, denenenleri, bulunan kanıtları, artı ve eksileriyle seçenekleri ve takip işleriyle birlikte net bir öneriyi kaydeden bir spike raporu yazar. Bir spike, proof of concept veya teknik araştırma bittiğinde (ya da planlanırken) ve ekibin karar verip tahmin yapabilmesi için sonucun paylaşılması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: design
  title: "Spike raporu yazma"
  related: "technical-design-doc, adr, technology-selection, trade-off-analysis, task-breakdown"
  prompt: "Bir spike raporu yaz: mevcut aramamızın yazım hatasına toleranslı ürün aramasını kaldırıp kaldıramayacağını ya da ayrı bir arama motoruna ihtiyacımız olup olmadığını iki gün inceledik."
---

# Spike Raporu Yazma

## Amaç
Süre sınırlı bir araştırmayı karar verilebilir bir özete dönüştürmek. Böylece edinilen bilgi tek bir kişinin kafasında kalmaz, takip işleri planlanıp tahmin edilebilir.

## Ne zaman kullanılır
- Bir spike veya proof of concept bitti ve ekibin nasıl ilerleyeceğine karar vermesi gerekiyorsa.
- Bir spike başlamak üzere ve keskin bir soruya, süre sınırına ve çıkış kriterlerine ihtiyaç varsa.
- Bir tahmin, artık araştırılmış olan teknik bir bilinmeyen yüzünden bekliyorsa.

## Ne zaman kullanılmaz
- Yaklaşım zaten seçildi ve tam bir tasarım gerekiyorsa `technical-design-doc` kullanılır.
- Yalnızca nihai kararın kaydedilmesi gerekiyorsa `adr` kullanılır.
- Ürünler veya tedarikçiler portföy düzeyinde karşılaştırılıyorsa `technology-selection` kullanılır.

## Girdiler
Zorunlu:
- Spike'ın yanıtlaması gereken soru ve ham bulgular (notlar, ölçümler, kod gözlemleri).

İsteğe bağlı, kaliteyi artırır:
- Kullanılan süre sınırı, ortam ve veri seti, önceden üzerinde anlaşılan kısıtlar ve değerlendirme kriterleri.
- Prototip branch'lerine, benchmark'lara, tedarikçi dokümanlarına bağlantılar.

Bulgular yoksa bunun yerine planlama yarısını (soru, süre sınırı, çıkış kriterleri, yöntem) yazmayı öner.

## Süreç
1. Soruyu bir konu ("X'e bak") olarak değil, verilecek bir karar olarak yaz ("X, Z koşulunda Y'yi karşılayabilir mi?").
2. Süre sınırını, harcanan gerçek süreyi ve spike'ın yanıtla mı yoksa süre dolduğu için mi bittiğini kaydet.
3. Önceden belirlenen eşik değerleriyle değerlendirme kriterlerini listele; belirlenmemişse türet ve `[VARSAYIM]` olarak işaretle.
4. Denenenleri anlat: yaklaşım, ortam, veri setinin büyüklüğü ve yapısı, sürümler. Başka birinin tekrarlayabileceği kadar ayrıntı ver.
5. Kanıtı yorumdan ayrı sun: ölçümler, gözlenen davranış, hatalar, ulaşılan limitler.
6. Seçenekleri (genellikle 2-4) kriterlere göre efor, risk ve geri alınabilirlik ile özetle.
7. Güven düzeyiyle (yüksek/orta/düşük) tek bir öneri ver ve öneriyi neyin değiştireceğini yaz.
8. Spike'ın neyi kapsamadığını ve kalan riskleri belirt.
9. Takip işlerini kaba büyüklükleriyle aday backlog kalemleri olarak listele; aksi belirtilmedikçe prototip kodun atılacağını not et.
10. Hedef devam ediyorsa kararı kaydetmek için `adr`, seçilen seçeneği ayrıntılandırmak için `technical-design-doc` veya takip işlerini planlamak için `task-breakdown` öner.

## Çıktı formatı
```markdown
# Spike Raporu: <sorunun kısa hali>
Süre sınırı: <planlanan> / Harcanan: <gerçek> · Bitiş nedeni: yanıt | süre sınırı · Yazar: <ad> · Tarih: <tarih>

## Soru
## Değerlendirme Kriterleri
| Kriter | Eşik | Sonuç |

## Denenenler
## Kanıtlar
## Seçenekler
| Seçenek | Kriterleri karşılıyor mu? | Efor | Risk | Geri alınabilir mi? |

## Öneri
<seçenek> — güven: <Y/O/D> — şu durumda değişir: <koşul>

## Kapsanmayanlar / Kalan Riskler
## Takip İşleri
| Kalem | Kaba büyüklük | Notlar |
```

## Kalite kontrol listesi
- [ ] Soru açık uçlu değil; evet/hayır ya da bir seçimle yanıtlanabiliyor.
- [ ] Kanıt tekrarlanabilir: ortam, veri ve sürümler belirtildi.
- [ ] Ölçümler gözlendiği gibi raporlandı; belirtilmeden hiçbir şey dışa kestirilmedi.
- [ ] Güven düzeyi ve değişme koşullarıyla tek bir öneri verildi.
- [ ] Kapsam boşlukları açıkça yazıldı.
- [ ] Takip kalemleri backlog'a girecek kadar somut.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve varsayım ya da açık soru olarak listeli; dayanağı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sorusu veya süre sınırı olmayan ve plansız özellik geliştirmeye dönüşen spike'lar. Önce soruyu ve çıkış kriterlerini sabitle.
- Prototip kodu üretim kodu olarak yayına almak. Yeniden yazılması veya sağlamlaştırılması gerektiğini açıkça belirt.
- Oyuncak veri üzerinde benchmark. Veri büyüklüğünü ve yapısını yaz, ölçeklenmeyebilecek sonuçları işaretle.

## Örnek
Girdi: "Yazım hatasına toleranslı arama için iki gün: mevcut veritabanı full-text'i mi, ayrı arama motoru mu? 50 bin ürün."

Çıktıdan bir bölüm:
- Soru: Mevcut veritabanı full-text araması, 50 bin ürün için gecikme hedefinin `[hedef BİLİNMİYOR, p95 < 200 ms varsayıldı]` altında yazım hatasına toleranslı sonuç döndürebilir mi?
- Kanıt: Trigram benzerliği 10 örnek yazım hatasının 9'unu buldu; üretim verisinin maskelenmiş 50 binlik kopyasında p95 140 ms.
- Öneri: Trigram indeksli veritabanı aramasında kal — güven orta — katalog büyümesi p95'i hedefin üzerine çıkarırsa veya faceting gereksinim olursa değişir.
