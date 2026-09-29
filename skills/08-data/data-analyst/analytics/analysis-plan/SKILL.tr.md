---
description: Herhangi bir sorgu çalıştırılmadan önce iş sorusunu, hipotezleri, veri kaynaklarını, yöntemi, geçerlilik kontrollerini ve çıktıyı netleştiren bir analiz planı yazar. Bir paydaş "X neden değişti", "Y işe yarıyor mu" veya "Z'yi yapmalı mıyız" diye sorduğunda ve kapsamın, yöntemin ve beklentilerin baştan uzlaşılması gerektiğinde kullanılır.
related: metric-definition, data-exploration, ab-test-analysis, insight-summary, hypothesis-statement
prompt: Şu soru için analiz planı yaz: pazarlama, yeni onboarding e-posta serisinin 30 günlük elde tutmayı artırıp artırmadığını öğrenmek istiyor.
---

# Analiz Planı Yazma

## Amaç
Sorgulara zaman harcamadan önce hangi sorunun, nasıl ve hangi veriyle cevaplanacağında uzlaşmak. Böylece sonuç karara hizmet eder, tekrarlanabilir olur ve analistin ilk bulduğu şeyin yönlendirmesine kalmaz.

## Ne zaman kullanılır
- Bir paydaş günlerce keşif gerektirebilecek açık uçlu bir soru getirdiğinde ("dönüşüm neden düştü?").
- Sonuca bağlı bir karar varsa ve yöntemin başkalarına savunulabilir olması gerekiyorsa.
- Aynı soru üzerinde birden fazla analist veya ekip çalışacak ve ortak bir kapsama ihtiyaç duyuluyorsa.

## Ne zaman kullanılmaz
- Soru kontrollü bir deneyin sonucunu okumaksa `ab-test-analysis` kullanılır.
- İhtiyaç tek seferlik bir soru değil, sürekli izlenecek bir görünümse `dashboard-spec` kullanılır.
- Veri tanıdık değilse ve önce anlaşılması gerekiyorsa `data-exploration` kullanılır.

## Girdiler
Zorunlu:
- Talep sahibinin kendi ifadesiyle iş sorusu.

İsteğe bağlı, kaliteyi artırır:
- Sonucun besleyeceği karar ve kararı kimin vereceği.
- Bilinen veri kaynakları, tablolar, mevcut metrik tanımları.
- Son tarih, önceki analizler, şüphelenilen nedenler.

Soru yoksa iste. Diğer tüm eksikleri planda açık soru olarak listele.

## Süreç
1. Soruyu bir karar sorusu olarak yeniden yaz: "<karar verici>, <kanıt> ışığında <aksiyon>u yapmalı mı?" Bir karar yoksa bunu belirt ve bir karar öner.
2. Birincil metriği ve 1-3 ikincil metriği tanımla. Mevcut bir tanıma atıf yap ya da `metric-definition` gerektiğini işaretle.
3. En az bir rakip açıklama (mevsimsellik, karma değişimi, izleme değişikliği, fiyatlama, dış olay) içeren, yanlışlanabilir hipotezler (H1, H2...) yaz.
4. Popülasyonu, analiz birimini, zaman penceresini ve karşılaştırmayı (önce/sonra, kohort, eşleştirilmiş kontrol, segment) belirt. Bu karşılaştırmanın etkiyi neden izole ettiğini açıkla.
5. Veri kaynaklarını tanecik (grain), sahip, güncellik ve bilinen kalite sorunlarıyla listele. Teyit edilmemiş kaynakları `[VARSAYIM]` olarak işaretle.
6. Yöntemi seç (tanımlayıcı kırılım, kohort analizi, farkların farkı, regresyon, segmentasyon); temel varsayımlarını ve geçerlilik tehditlerini (seçim yanlılığı, karıştırıcı değişkenler, hayatta kalan yanlılığı, Simpson paradoksu) not et.
7. Geçerlilik kontrollerini tanımla: kaynak sistemle satır sayısı mutabakatı, resmi dashboard ile metrik mutabakatı, pencere seçimine duyarlılık.
8. Veriye bakmadan önce kararı hangi sonucun değiştireceğini (karar eşikleri) yaz.
9. Çıktıyı planla: format, hedef kitle, ayrıntı düzeyi ve tarih.
10. Gizliliği ele al: kişisel veriyi en aza indir, tanımlayıcıları topla veya maskele, KVKK/GDPR amaçla sınırlılık ilkesine uy.
11. Şablonu doldur ve açık soruları sorumlularıyla listele.

## Çıktı formatı
```markdown
# Analiz Planı: <başlık>
| Alan | Değer |
|---|---|
| Talep sahibi / karar verici | <ad veya [BİLİNMİYOR]> |
| Beslenecek karar | <karar> |
| Teslim tarihi | <tarih veya [BİLİNMİYOR]> |

## Soru
<karar sorusu>

## Metrikler
- Birincil: <metrik> – <tanım referansı>
- İkincil / koruyucu: ...

## Hipotezler
- H1: ... (destekleyecek / çürütecek kanıt)
- H2 (rakip açıklama): ...

## Kapsam ve Karşılaştırma
Popülasyon: ... | Birim: ... | Pencere: ... | Karşılaştırma: ... | Hariç tutulanlar: ...

## Veri Kaynakları
| Kaynak | Tanecik | Güncellik | Bilinen sorunlar |
|---|---|---|---|

## Yöntem ve Geçerlilik Tehditleri
- Yöntem: ...
- Tehditler ve önlemler: ...

## Geçerlilik Kontrolleri
- ...

## Karar Eşikleri
- <sonuç> olursa <öneri>.

## Çıktı
<format, kitle, tarih>

## Açık Sorular
1. <soru> – <sorumlu>
```

## Kalite kontrol listesi
- [ ] Soru yalnızca meraka değil bir karara bağlı.
- [ ] En az bir rakip açıklama hipotez olarak yazıldı.
- [ ] Karşılaştırma grubu ve zaman penceresi açık ve gerekçeli.
- [ ] Karar eşikleri herhangi bir sonuç görülmeden yazıldı.
- [ ] Veri kaynakları uydurulmadı; teyitsiz olanlar işaretli.
- [ ] Kişisel verinin nasıl ele alınacağı belirtildi.

## Sık yapılan hatalar
- Mevsimselliği veya eş zamanlı lansmanları hesaba katmadan önce/sonra karşılaştırması planlamak. Kontrol grubu veya geçen yılla karşılaştırma ekle.
- Analiz sırasında metrik tanımının kaymasına izin vermek. Tanımı planda dondur, her değişikliği kaydet.
- Gözlemsel veriden nedensel sonuç vaat etmek. Yöntemin desteklediği kanıt düzeyini açıkça yaz.

## Örnek
Girdi: "Yeni onboarding e-posta serisi 30 günlük elde tutmayı artırdı mı?"

Çıktıdan bir bölüm:
- Soru: CRM ekibi yeni seriyi tüm kayıtlar için varsayılan olarak tutmalı mı?
- H2 (rakip): Elde tutma, aynı hafta yapılan fiyat değişikliği nedeniyle arttı.
- Karşılaştırma: Lansmandan önceki ve sonraki 4 haftada kayıt olan kullanıcılar, ücretli kampanya kohortu hariç; seriyi almayan bölgeye karşı farkların farkı `[VARSAYIM: dağıtım bölgesel yapıldı]`.
- Karar eşiği: 30 günlük elde tutma artışı en az `[TBD, CRM belirleyecek]` puan ve güven aralığı sıfırı içermiyorsa seri korunur.
