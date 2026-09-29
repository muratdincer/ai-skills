---
description: "Bir servis için kullanıcı odaklı SLI ve SLO'lar tanımlar: kritik kullanıcı yolculuklarını belirler, gösterge türlerini (erişilebilirlik, gecikme, tazelik, doğruluk, verim) seçer, iyi/geçerli olay tanımlarını ve ölçüm noktalarını netleştirir, hedefleri ve uyum pencerelerini ortaya çıkan hata bütçesiyle belirler. Bir servisin güvenilirlik hedeflerine ihtiyacı olduğunda, alarmlar gürültülü veya kullanıcı acısıyla ilgisiz olduğunda ya da bir SLO'nun ne olması gerektiği sorulduğunda kullanılır."
related: "error-budget-policy, alert-design, observability-plan, nfr-specification, kpi-definition"
prompt: "Checkout API'miz için SLI ve SLO tanımla. Load balancer logları ve Prometheus metriklerimiz var; iş birimi checkout'un 'her zaman çalışması' gerektiğini söylüyor."
---

# SLI ve SLO Tanımlama

## Amaç
Bir servisin ne kadar güvenilir olması gerektiğini kullanıcıların hissettiği terimlerle, kesin ve ölçülebilir göstergeler ve hedeflerle ifade etmek. Böylece güvenilirlik çalışmaları, alarmlar ve sürüm kararları tek bir nesnel tanımı paylaşır.

## Ne zaman kullanılır
- Yeni veya mevcut bir servisin üzerinde anlaşılmış güvenilirlik hedefi olmadığında.
- Mevcut hedefler kullanıcı odaklı değil altyapı odaklı olduğunda (CPU, sunucu ayakta).
- İş birimi "%100" veya "her zaman erişilebilir" istediğinde ve gerçekçi bir hedefin müzakere edilmesi gerektiğinde.

## Ne zaman kullanılmaz
- SLO mevcutsa ve soru bütçe tükendiğinde ne yapılacağıysa `error-budget-policy` kullanılır.
- Mevcut SLO'lar için alarmlar tasarlanacaksa `alert-design` kullanılır.
- Müşterilere sözleşmesel taahhütler hazırlanıyorsa; SLO'lar bunlara girdi olur ama bir SLA hukuki ve ticari inceleme gerektirir.

## Girdiler
Zorunlu:
- Servis tanımı ve ana kullanıcıları (kişiler veya diğer servisler).
- Kullanıcıların servisle ne yaptığı (kilit istekler, yolculuklar, tükettikleri veri).

İsteğe bağlı, kaliteyi artırır:
- Mevcut telemetri ve nerede ölçüldüğü (istemci, edge/load balancer, servis, sentetik problar).
- Geçmiş performans verisi, olaylar, bağımlılıkların SLO'ları.
- İş kritikliği, sözleşmesel SLA'lar, bakım pencereleri.

Kullanıcılar ve kilit etkileşimleri bilinmiyorsa sor. Geçmiş veri yoksa hedefler gerçek veriyle doğrulanmak üzere `[ÖNERİ]` olarak işaretlenmiş önerilerdir.

## Süreç
1. Kritik kullanıcı yolculuklarını (CUJ) listele ve iş etkisine göre sırala; 1-3 tanesiyle başla.
2. Her CUJ için kullanıcı acısını yansıtan SLI türlerini seç: istek/yanıt → erişilebilirlik ve gecikme; veri hatları → tazelik, kapsam, doğruluk; depolama → dayanıklılık; akış → verim ve gecikme payı (lag).
3. Her SLI'ı bir oran olarak tanımla: iyi olaylar / geçerli olaylar. Neyin geçerli olduğunu (health check'ler, uygun olduğunda istemci kaynaklı 4xx'ler, sentetik trafik hariç) ve neyin iyi olduğunu (durum sınıfı, gecikme eşiği, doğru yanıt) kesin olarak belirt.
4. Ölçüm noktasını seç ve kör noktalarını yaz (sunucu tarafı ağ ve istemci hatalarını kaçırır; edge yaygın bir uzlaşmadır; sentetikler düşük trafikli yolları kapsar).
5. Hedefleri umuttan değil, kullanıcı beklentisinden ve geçmiş performanstan belirle; gecikmeyi ortalama yerine yüzdelik eşiklerle ifade et (ör. isteklerin %99'u X ms altında).
6. Ulaşılabilirliği kontrol et: bir servis yedeklilik olmadan sert bağımlılıklarının güvenilirliklerinin çarpımını aşamaz; çelişkileri işaretle.
7. Uyum penceresini seç (kayan 28 veya 30 gün yaygındır) ve hata bütçesini olay veya dakika cinsinden hesapla.
8. Sahipliği, gözden geçirme sıklığını ve kapsam dışını (planlı bakım, belirli istemciler) tanımla.
9. Varsa SLA'ları ayrı kaydet; güvenlik payı için SLO, SLA'dan daha sıkı olsun.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa bütçe tükenince yapılacaklar için `error-budget-policy`, burn-rate alarmları için `alert-design` veya telemetri boşluklarını kapatmak için `observability-plan` öner.

## Çıktı formatı
```markdown
# SLO'lar: <servis>
Sahip: <ekip> · Pencere: <kayan N gün> · Gözden geçirme: <sıklık>

## Kritik Kullanıcı Yolculukları
1. <yolculuk> – neden önemli

## SLI Tanımları
| CUJ | SLI türü | İyi olaylar | Geçerli olaylar | Ölçüm noktası | Kör noktalar |

## SLO Hedefleri
| SLI | Hedef | Pencere | Hata bütçesi | Dayanak (geçmiş / [ÖNERİ]) |

## Bağımlılıklar ve Ulaşılabilirlik
## Hariç Tutulanlar
## İlgili SLA (varsa)
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her SLI, kesin dahil etme ve hariç tutma kuralları olan bir iyi/geçerli oranı.
- [ ] SLI'lar kaynak kullanımını değil, kullanıcıya görünür davranışı anlatıyor.
- [ ] Gecikme ortalamalarla değil, yüzdelik eşiklerle ifade ediliyor.
- [ ] Hedefler %100'ün altında ve veriyle gerekçelendirilmiş ya da `[ÖNERİ]` olarak işaretli.
- [ ] Ölçüm noktası ve kör noktaları belirtildi.
- [ ] Hata bütçesi pencere için hesaplandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yedeksiz %99,9'luk bir veritabanına bağlı servise %99,99 hedef koymak. Bağımlılık hesabını kontrol et.
- Tüm 4xx'leri kötü (kullanıcının kendi hatası) veya tümünü iyi (kimlik doğrulama kesintilerini gizler) saymak. Durum koduna göre karar ver.
- Çok fazla SLO. Servis başına gerçek yolculuklara karşılık gelen birkaç SLO aksiyon alınabilir; düzinelercesi görmezden gelinir.

## Örnek
Girdi: "Checkout API, edge load balancer logları mevcut, günde ~2M istek."

Çıktıdan bir bölüm:
| CUJ | SLI türü | İyi olaylar | Geçerli olaylar | Ölçüm noktası |
|---|---|---|---|---|
| Sipariş verme | Erişilebilirlik | 5xx ve 429 olmayan yanıtlar | sentetik problar hariç tüm POST /orders | Edge LB |
| Sipariş verme | Gecikme | `[TBD]` ms altındaki yanıtlar | yukarıdakiyle aynı, yalnızca başarılılar | Edge LB |

Hedef: kayan 28 günde %99,9 erişilebilirlik `[ÖNERİ]` → bütçe ≈ geçerli isteklerin %0,1'i (~56M'nin ~56 bini `[VARSAYIM: hacim günde 2M'de kalıyor]`).
