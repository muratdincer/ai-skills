---
name: observability-plan
description: "Bir veya birden çok servis için gözlemlenebilirliği planlar: hangi metriklerin, yapılandırılmış logların ve dağıtık izlerin üretileceği, korelasyon ve bağlam aktarımı, kardinalite ve saklama bütçeleri, hedef kitleye göre panolar ve SLO'lar ile runbook'lara karşı eksikler. Servis geliştirilirken veya canlıya alınırken, olayların teşhisi uzun sürdüğünde, telemetri maliyeti kontrolden çıktığında ya da neyin enstrümante edileceği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Gözlemlenebilirlik planı"
  related: "slo-definition, alert-design, logging-instrumentation, dashboard-spec, runbook"
  prompt: "Sipariş servisimiz için gözlemlenebilirlik planla: .NET API, Kafka consumer, PostgreSQL. Bugün yalnızca konteyner CPU/bellek grafikleri ve yapılandırılmamış loglarımız var."
---

# Gözlemlenebilirlik Planı

## Amaç
Her servisin hangi telemetriyi üreteceğini, bunun nasıl ilişkilendirileceğini, saklanacağını ve görselleştirileceğini tanımlamak. Böylece nöbetçi "bozuk mu, kimin için, neden" sorularını hızla yanıtlayabilir ve maliyet kurumun kabul ettiği sınırda kalır.

## Ne zaman kullanılır
- Yeni bir servis tasarlanıyor veya bir servis canlı ortama alınıyor.
- Postmortem'ler sinyaller eksik veya ilişkisiz olduğu için tespit ya da teşhis süresinin uzun olduğunu gösteriyor.
- Telemetri hacmi veya maliyeti plansız büyümüş (yüksek kardinaliteli metrikler, canlıda debug logları).

## Ne zaman kullanılmaz
- Sinyaller mevcut ve yalnızca alarm kurallarının tasarlanması gerekiyorsa `alert-design` kullanılır.
- İş belirli bir koda log satırları eklemekse `logging-instrumentation` kullanılır.
- Tek bir iş panosu gerekiyorsa `dashboard-spec` kullanılır.

## Girdiler
Zorunlu:
- Her birinin kısa açıklamasıyla servis listesi (tür: API, worker, consumer, batch, frontend) ve ana bağımlılıklar.
- Bugün hangi telemetrinin var olduğu veya bunun bilinmediği bilgisi.

İsteğe bağlı, kaliteyi artırır:
- SLO'lar ve kritik kullanıcı yolculukları; son olaylar ve teşhisi zor olan noktalar.
- Telemetri altyapısı kısıtları, saklama limitleri, bütçe.
- Loglarda görünebilecek verinin sınıflandırması (kişisel veri, gizli bilgiler).

Servis listesi yoksa iste. Bir ürün varsayma; sinyalleri tarafsız terimlerle anlat (referans olarak OpenTelemetry gibi açık bir standart anılabilir).

## Süreç
1. Her servisin rolünü ve istek/veri akışını, bağlamın genellikle kaybolduğu asenkron adımlar (kuyruklar, topic'ler, zamanlayıcılar) dahil olmak üzere haritala.
2. Servis türüne göre altın sinyalleri tanımla: istek servisleri için rate, errors, duration (RED) ve doygunluk; kaynaklar için kullanım, doygunluk, hata (USE); consumer'lar için ek olarak lag ve en eski mesaj yaşı; batch işler için son başarılı çalışma zamanı, süre ve işlenen kayıt sayısı.
3. SLI'ları bu metriklere bağla ve her SLO'nun bunlardan hesaplanabildiğini doğrula; eksikleri listele.
4. Yapılandırılmış logu tanımla: zorunlu alanlar (zaman damgası, seviye, servis, sürüm, ortam, trace ID, span ID, istek veya korelasyon ID'si, gerekiyorsa tenant), olay adlandırma, seviye politikası (varsayılan olarak canlıda debug yok) ve asla loglanmayacaklar (secret'lar, token'lar, tam kişisel veri; bunun yerine maskele veya hash'le).
5. İzlemeyi (tracing) tanımla: giriş ve çıkış span'leri, HTTP ve mesajlaşma başlıklarında bağlam aktarımı, eklenecek span nitelikleri, örnekleme stratejisi (head-based oran artı hatalar ve yavaş istekler için tail-based saklama) ve bunun SLI doğruluğuna etkisi.
6. Kardinalite ve hacim bütçesi koy: metriklerde sınırsız etiketleri (kullanıcı ID, tam URL, istek ID) yasakla, servis başına log hacmini sınırla ve sinyal başına saklama süresi belirle (örn. yüksek çözünürlük kısa, özetler uzun) `[ÖNERİ]`.
7. Hedef kitleye göre panolar tasarla: servis özeti (SLO'lar ve altın sinyaller), bağımlılık görünümü ve derin inceleme; her pano tek bir soruyu yanıtlar ve aynı zaman aralığı ve filtrelerle izlere ve loglara bağlanır.
8. Alarmlar ve runbook'larla çapraz kontrol et: her page alarmının ilk teşhis adımı için gereken sinyaller mevcut olmalı.
9. Sahipliği, devreye alma sırasını (en riskli servis önce) ve doğrulama adımını tanımla: sinyallerin bunu gösterdiğini kanıtlamak için sentetik bir hata üret veya yakın tarihli bir olayı yeniden oynat.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, açık soruları listele ve sonraki becerileri öner: page'ler için `alert-design`, SLI yoksa `slo-definition`, kod değişiklikleri için `logging-instrumentation`, teşhis adımları için `runbook`.

## Çıktı formatı
```markdown
# Gözlemlenebilirlik Planı: <sistem>
Kapsam: <servisler> · Sahip: <ekip> · Altyapı: <tarafsız açıklama veya [BİLİNMİYOR]>

## Servis Sinyal Matrisi
| Servis | Tür | Metrikler (RED/USE/lag) | Önemli log olayları | İz span'leri | SLI kapsamı |

## Log Standardı
- Zorunlu alanlar / seviye politikası / asla loglanmayacaklar

## İzleme ve Bağlam Aktarımı
## Kardinalite, Hacim ve Saklama Bütçesi
| Sinyal | Çözünürlük | Saklama | Limit |

## Panolar
| Ad | Hedef kitle | Yanıtladığı soru | Bağlantılar |

## SLO, Alarm ve Runbook'lara Karşı Eksikler
## Devreye Alma ve Doğrulama
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her servisin türüne uygun altın sinyalleri var; gerekiyorsa asenkron lag dahil.
- [ ] Trace ve korelasyon ID'leri her senkron ve asenkron adımda aktarılıyor.
- [ ] Her SLO planlanan sinyallerden hesaplanabiliyor ya da eksik listelendi.
- [ ] Sınırsız metrik etiketleri dışarıda bırakıldı ve saklama sinyal başına tanımlandı.
- [ ] Asla loglanmayacaklar listesi secret'ları ve kişisel veriyi maskeleme rehberiyle kapsıyor.
- [ ] Sinyallerin gerçek bir hatayı göstereceğini kanıtlayan bir doğrulama adımı var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Host metrikleriyle dolu ama kullanıcıya dönük sinyali olmayan panolar. SLI'lardan ve altın sinyallerden başla, kaynakları bunların altına ekle.
- Mesaj aracısında bağlamı kaybetmek. Trace bağlamını mesaj başlıklarında taşı ve consumer span'lerini producer'a bağla.
- İhtiyaç duyulan hataları sessizce düşüren örnekleme. Head örnekleme oranından bağımsız olarak hataları ve yavaş izleri sakla.

## Örnek
Girdi: ".NET sipariş API'si, Kafka consumer, PostgreSQL; yalnızca konteyner CPU/bellek ve düz metin loglar."

Çıktıdan bir bölüm:
| Servis | Tür | Metrikler | İz span'leri | SLI kapsamı |
|---|---|---|---|---|
| order-api | API | rate, 5xx oranı, route şablonu başına p95/p99 süre | gelen HTTP, DB sorgusu, Kafka produce | erişilebilirlik, gecikme |
| order-consumer | Consumer | consumer lag, en eski mesaj yaşı, işleme hataları | producer span'ine bağlı Kafka consume | tazelik `[ÖNERİ]` |

Eksik: sipariş durumu tazelik SLO'su bugün hesaplanamıyor; mesaj yaşı metriği gerekiyor.
