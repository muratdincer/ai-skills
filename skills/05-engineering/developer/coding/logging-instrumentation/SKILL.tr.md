---
name: logging-instrumentation
description: "Koda, gerçek operasyonel soruları yanıtlayan noktalarda yapılandırılmış log, metrik ve dağıtık iz (trace) ekler; tutarlı alan adları, doğru seviyeler, düşük kardinaliteli metrik etiketleri, trace bağlamı aktarımı sağlar ve sır ya da kişisel veri yazmaz. Bir özellik canlıya çıkacağında, bir olay görünürlük eksikliğini ortaya koyduğunda veya koda loglama, metrik, tracing ya da telemetri (ör. OpenTelemetry) eklenmesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: coding
  title: "Loglama ve ölçümleme ekleme"
  related: "observability-plan, alert-design, slo-definition, error-handling-review, log-analysis"
  prompt: "Dosya okuyan, satırları doğrulayan ve stok API'sini çağıran bu sipariş içe aktarma işine loglama, metrik ve tracing ekle."
---

# Loglama ve Ölçümleme Ekleme

## Amaç
Kodun canlıdaki davranışını gözlemlenebilir kılmak; operasyon ekibinin sorunu fark etmesini, teşhis etmesini ve ölçmesini sağlarken telemetriyi ucuz, tutarlı ve hassas veriden arınmış tutmak.

## Ne zaman kullanılır
- Yeni kod veya yeni bir entegrasyon yayına alınmak üzereyken.
- Bir olay ya da destek kaydı mevcut telemetriyle teşhis edilemediğinde.
- Bir SLO veya alarm, kodun henüz üretmediği bir sinyale ihtiyaç duyduğunda.

## Ne zaman kullanılmaz
- Bir sistemin veya servis haritasının tamamı için gözlemlenebilirlik tasarlanıyorsa `observability-plan` kullanılır.
- Alarm kuralları ve eşikleri tanımlanıyorsa `alert-design` kullanılır.
- Mevcut loglar inceleniyorsa `log-analysis` kullanılır.

## Girdiler
Zorunlu:
- Ölçümlenecek kod ve dili/çalışma ortamı.

İsteğe bağlı, kaliteyi artırır:
- Ekibin telemetri altyapısı ve kuralları (log formatı, alan adları, metrik isimlendirme, OpenTelemetry kullanımı), mevcut SLO'lar, bilinen olay soruları.

Altyapı bilinmiyorsa üreticiden bağımsız OpenTelemetry kavramlarını ve semantic conventions'ı kullan; altyapıya özgü ayrıntıları `[TBD]` olarak işaretle.

## Süreç
1. Önce operasyonel soruları yaz: Çalışıyor mu? Ne kadar hızlı? Ne sıklıkla ve neden hata veriyor? Hangi girdi soruna yol açtı? Bekleyen iş ne kadar?
2. Her soruyu bir sinyale eşle: metrik (oranlar, süreler, boyutlar, doygunluk), trace/span (atlamalar arası gecikme), log (bağlamıyla birlikte tekil olay).
3. Metrikler: istek yolları için RED (rate, errors, duration), kaynaklar için USE kullan; süreler için histogram; yalnızca sınırlı kardinaliteli etiketler (asla kullanıcı id, sipariş id, ham URL).
4. Trace: dış çağrıların ve önemli iç adımların etrafında span oluştur; bağlamı HTTP/mesajlaşma üzerinden aktar; hataları span'e kaydet; öznitelikleri semantic conventions'a göre ekle.
5. Loglar: yapılandırılmış anahtar-değer/JSON; her anlamlı durum değişikliği veya hata için tek olay; correlation/trace id, operasyon, sonuç, süre ve kararlı bir hata kodu içersin.
6. Seviyeler: ERROR = aksiyon gerekir, WARN = bozulma var ama ele alındı, INFO = iş açısından önemli yaşam döngüsü olayları, DEBUG = varsayılan kapalı teşhis. Örnekleme olmadan sıkı döngülerin içinde log yazma.
7. Gizlilik ve güvenlik: sır, token, tam kart numarası veya parola asla loglanmaz; kişisel veriyi maskele veya hash'le; payload yerine ID logla.
8. Ölçümlemeyi mümkün olduğunca iş mantığının dışında tut (middleware, decorator, interceptor).
9. Nasıl doğrulanacağını tanımla: log satırını, metrik artışını ve span'i gösteren bir test veya yerel çalıştırma.
10. Sinyallere bağlı dashboard panelleri ve alarm adayları öner; eşik uydurma.
11. Hedef devam ediyorsa adayları alarma dönüştürmek için `alert-design` veya servis genelinde kapsam için `observability-plan` öner.

## Çıktı formatı
```markdown
# Ölçümleme: <bileşen>
## Operasyonel Sorular → Sinyaller
| Soru | Sinyal türü | Ad | Etiketler / öznitelikler |

## Kod Değişiklikleri
<ölçümleme eklenmiş kod>

## Log Olayları
| Olay | Seviye | Alanlar | Ne zaman |

## Gizlilik Notları
## Doğrulama
## Dashboard / Alarm Adayları
```

## Kalite kontrol listesi
- [ ] Her sinyal belirtilmiş bir operasyonel soruyu yanıtlıyor.
- [ ] Metrik etiketlerinin kardinalitesi sınırlı.
- [ ] Trace bağlamı her giden çağrıda ve mesajda aktarılıyor.
- [ ] Loglarda, etiketlerde veya span özniteliklerinde sır ya da maskelenmemiş kişisel veri yok.
- [ ] Log seviyeleri belirtilen kurallara uyuyor ve hiçbir olay iki kez loglanmıyor.
- [ ] İsimler ekibin kuralına veya OpenTelemetry semantic conventions'a uyuyor.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve varsayım ya da açık soru olarak listeli; dayanağı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Metrik depolamasını ve maliyeti patlatan yüksek kardinaliteli etiketler (kullanıcı id, tam yol).
- "Hata ayıklamak için" istek/yanıt gövdelerinin tamamını loglamak ve kişisel veri sızdırmak.
- Yalnızca hataları saymak; toplam deneme sayısı olmadan hata oranı hesaplanamaz.

## Örnek
Girdi: "Sipariş içe aktarma işi: dosyayı oku, satırları doğrula, her satır için stok API'sini çağır."

Çıktıdan bir bölüm:
- Metrik `order_import_rows_total{result="imported|invalid|failed"}` ve histogram `order_import_duration_seconds`.
- Her çağrı için `http.response.status_code` içeren `inventory.reserve` span'i; iş span'i satır span'lerine bağlanır.
- `file_id`, `rows_total`, `rows_invalid`, `duration_ms` alanlarıyla INFO seviyesinde `import.completed` logu; geçersiz satırlar satır numarası ve hata koduyla loglanır, asla müşteri adı veya adresiyle değil.
