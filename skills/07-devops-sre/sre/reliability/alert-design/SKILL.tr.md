---
description: "Bir servis için sayfalama (page) ve kayıt (ticket) alarm setini tasarlar: SLO'lara bağlı belirti bazlı alarmlar, çok pencereli ve çok burn-rate'li koşullar, önem derecesi ve yönlendirme, runbook bağlantıları ve mevcut gürültülü alarmların denetimi. Alarm yoksa, gürültülüyse, kullanıcı etkisi yerine nedene (CPU, disk) dayalıysa, nöbetçiler tükeniyorsa veya yeni SLO'lar için alarm gerekiyorsa kullanılır."
related: "slo-definition, error-budget-policy, observability-plan, runbook, incident-response"
prompt: "Ödeme API'miz için alarm tasarla. SLO 28 günde %99,9 erişilebilirlik; şu an CPU > %80 olunca page atıyoruz ve haftada 40 page geliyor."
---

# Alarm Tasarımı

## Amaç
Her page'in gerçek ya da yakın bir kullanıcı etkisini ve hemen müdahale gereğini gösterdiği, geri kalan her şeyin kayıt veya panoya dönüştüğü küçük bir alarm seti üretmek. Böylece nöbet yükü sürdürülebilir kalır ve olaylar erken yakalanır.

## Ne zaman kullanılır
- Servisin SLO'ları var ama bunlara bağlı alarm yok ya da yalnızca kaynak metriklerinde alarm var.
- Nöbetçiler alarm yorgunluğu bildiriyor: sık page, sürekli açılıp kapanan (flapping) alarmlar, aksiyonsuz page'ler.
- Yeni bir servis canlıya çıkıyor ve bir sayfalama politikasına ihtiyaç var.

## Ne zaman kullanılmaz
- Henüz SLI veya SLO yoksa önce `slo-definition` kullanılır; burn-rate alarmları bunlara dayanır.
- Telemetrinin kendisi eksikse (metrik, log, iz yok) `observability-plan` kullanılır.
- Soru page geldikten sonra nasıl müdahale edileceğiyse `runbook` veya `incident-response` kullanılır.

## Girdiler
Zorunlu:
- Servis ve SLO'ları (ya da en azından önemli olan kullanıcıya görünen belirtiler).
- Mevcut alarm listesi veya hiç alarm olmadığı bilgisi.

İsteğe bağlı, kaliteyi artırır:
- Alarm geçmişi: alarm başına sayı, aksiyon alınan/yok sayılan oranı, onaylama süresi.
- Nöbet yapısı: rotasyonlar, saatler, eskalasyon yolları, bildirim kanalları.
- Mevcut sinyaller ve alarm motorunun yetenekleri (pencereler, recording rule'lar).

SLO'lar ve belirtiler birlikte bilinmiyorsa önce bunları sor. Eşik tahmin etme; önerilen değerleri `[ÖNERİ]` olarak işaretle.

## Süreç
1. Mevcut alarmları hacim ve sonuçlarıyla envanterle; her birini belirti (kullanıcı etkisi) veya neden (kaynak, bileşen durumu) olarak sınıflandır. Geçmiş verilmediyse `[BİLİNMİYOR]` olarak işaretle.
2. Her SLO için burn-rate alarmları tanımla: hızlı tüketim page'i (örn. bütçenin %2'si 1 saatte, 14,4x) ve yavaş tüketim page'i veya kaydı (örn. %5'i 6 saatte, 6x; %10'u 3 günde, 1x). Her birine hızlı sıfırlanması için kısa bir teyit penceresi ekle.
3. SLO'nun kapsamadığı belirti alarmlarını ekle: trafiğin sıfıra düşmesi, pipeline'larda takılan kuyruk veya veri tazeliği, sertifika süresinin dolması, düşük trafikli yollarda sentetik probe hataları.
4. Nedene dayalı alarmları (CPU, bellek, disk, pod yeniden başlatma) kayıt veya panoya indir; yalnızca açık bir önceden uyarı süresiyle yakın kullanıcı etkisini öngörüyorlarsa page olarak tut (örn. doğrusal projeksiyonla diskin 4 saatten kısa sürede dolması).
5. Önem derecesi ve yönlendirme ata: page (hemen, 7/24), kayıt (mesai içinde), yalnızca log. Her page bir sahip rotasyonu ve eskalasyon yolu belirtmeli.
6. Her alarm için içeriği yaz: kullanıcı etkisini anlatan özet, eşiğe karşı güncel değer, pano bağlantısı, runbook bağlantısı ve ilk teşhis adımı.
7. Gürültü mekanizmalarını ekle: minimum süre veya teyit pencereleri, servis bazında gruplama ve tekilleştirme, üst bağımlılık alarmı çaldığında alt alarmları bastırma (inhibition), süresi olan bakım susturmaları.
8. Beklenen page hacmini tahmin et; sürdürülebilir seviyeyi aşıyorsa (yaygın bir sezgisel kural 12 saatlik vardiyada en fazla iki olaydır) eşikleri yükselt veya alarmları kayda taşı ve ödünleşimi not et.
9. Gözden geçirme döngüsünü tanımla: her page aksiyon alınabilir/alınamaz olarak etiketlenir; aksiyon oranı düşük alarmlar düzenli incelemede ayarlanır veya silinir.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle ve açık soruları listele. Hedef devam ediyorsa her page alarmı için `runbook`, eksik sinyaller için `observability-plan` veya bütçe tükenince yapılacaklar için `error-budget-policy` öner.

## Çıktı formatı
```markdown
# Alarm Tasarımı: <servis>
Kapsanan SLO'lar: <liste> · Nöbet rotasyonu: <ad veya [BİLİNMİYOR]>

## Mevcut Alarm Denetimi
| Alarm | Tür (belirti/neden) | Hacim/hafta | Aksiyon % | Karar (tut/ayarla/kayıt/sil) |

## Alarm Kataloğu
| Ad | Koşul (pencere, eşik) | Önem | Yönlendirme | Runbook | Gerekçe |

## Bildirim İçeriği Şablonu
## Gürültü Kontrolleri (gruplama, bastırma, susturma)
## Beklenen Yük ve Gözden Geçirme Sıklığı
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her page alarmı kullanıcı etkisini veya belirtilmiş bir önceden uyarı süresiyle yakın kullanıcı etkisini yansıtıyor.
- [ ] SLO alarmları ham hata oranı eşiği değil, en az iki pencerede burn-rate kullanıyor.
- [ ] Her page'in sahibi, runbook bağlantısı ve ilk teşhis adımı var.
- [ ] Nedene dayalı alarmlar indirildi veya tek tek gerekçelendirildi.
- [ ] Veriye dayanmayan eşikler `[ÖNERİ]` olarak işaretli.
- [ ] Beklenen page hacmi tahmin edildi ve gözden geçirme döngüsü tanımlandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tek bir kısa pencerede hata oranına page atmak: düşük trafikte flapping yapar, yavaş tüketimi kaçırır. Çok pencereli burn-rate ve minimum istek sayısı kullan.
- Bir alarmı "ne olur ne olmaz" diye tutmak. Kimsenin aksiyon almadığı alarm nöbetçiye page'leri yok saymayı öğretir; sil veya indir.
- Her bağımlılık için ayrı alarm kurmak. Alt gürültüyü bastır, kullanıcı belirtisi için tek page at.

## Örnek
Girdi: "Ödeme API'si, 28 günde %99,9, CPU > %80'de page, haftada ~40 page, çoğu kendiliğinden kapanıyor."

Çıktıdan bir bölüm:
| Ad | Koşul | Önem | Yönlendirme |
|---|---|---|---|
| PaymentsFastBurn | 1s'te burn rate > 14,4 VE 5dk'da > 14,4 | Page | payments-oncall |
| PaymentsSlowBurn | 6s'te burn rate > 6 VE 30dk'da > 6 | Page | payments-oncall |
| PaymentsBudgetDrift | 3g'de burn rate > 1 VE 6s'te > 1 | Kayıt | payments-team |
| HighCPU | 10dk boyunca CPU > %80 | Sil (kendiliğinden kapanıyor, kullanıcı etkisi kaydı yok) `[VARSAYIM: geçmişle teyit et]` | - |
