---
name: capacity-planning
description: "Bir servis veya platform için kapasite planı çıkarır: organik büyüme ve bilinen olaylardan talep öngörüsü, yük testlerinden veya canlı veriden kaynak bazında doygunluk sınırları, pay (headroom) ve N+1 yedeklilikle gereken kapasite, tedarik süreleri, ölçekleme tetikleyicileri ve maliyet etkisi. Bir lansman, kampanya veya sezonsal zirve yaklaşırken, kullanım sınırlara doğru ilerlerken ya da sonraki dönemin altyapı bütçesi planlanırken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Kapasite planlama"
  related: "capacity-test-report, load-test-analysis, scalability-review, finops-review, observability-plan"
  prompt: "Black Friday için checkout kapasitesini planla. Normal zirve 800 istek/sn, pazarlama 4 kat trafik bekliyor; 12 pod ve tek bir birincil veritabanıyla çalışıyoruz."
---

# Kapasite Planlama

## Amaç
Bir servisin öngörülen talebi SLO'ları içinde karşılayacak, açık bir pay ve yedeklilik içeren yeterli kapasiteye sahip olmasını ve uzun tedarik süreli kaynakların zamanında sağlanmasını güvence altına almak; bunu bütçeyi boşa harcayan aşırı kaynak ayırmadan yapmak.

## Ne zaman kullanılır
- Bilinen bir talep olayı yaklaşıyor: lansman, kampanya, sezonsal zirve, yeni müşteri devreye alma, trafik taşıma.
- Kullanım eğilimleri bir kaynağın sınırına yaklaştığını gösteriyor (bağlantılar, depolama, iş hacmi, kotalar).
- Sonraki dönem için altyapı bütçesi veya rezerve kapasite planlanmalı.

## Ne zaman kullanılmaz
- İhtiyaç yük testini yürütmek veya analiz etmekse `performance-test-plan` veya `load-test-analysis` kullanılır.
- Mimari ölçeklenemiyor ve yeniden tasarım gerekiyorsa `scalability-review` kullanılır.
- Amaç mevcut kapasitenin maliyetini düşürmekse `finops-review` kullanılır.

## Girdiler
Zorunlu:
- Servis kapsamı ve güncel bir başlangıç değeriyle birlikte talep etkeni (istek, kullanıcı, işlem, veri hacmi).
- Öngörü dönemi ve bilinen talep olayları.

İsteğe bağlı, kaliteyi artırır:
- Kaynak başına geçmiş kullanım (yalnızca ortalama değil, zirve), yük testi sonuçları, bilinen darboğazlar.
- Ölçekleme mekanizmaları (autoscaling sınırları, manuel adımlar), sağlayıcı kotaları, tedarik süreleri.
- SLO hedefleri, yedeklilik gereksinimleri, bütçe limitleri.

Başlangıç değeri veya öngörü etkeni yoksa sor. Büyüme oranı uydurma; tahminleri kaynaklarıyla birlikte `[VARSAYIM]` olarak işaretle.

## Süreç
1. Yükü belirleyen talep birimini tanımla (örn. zirve dakikadaki istek/sn, sipariş/saat, günlük alınan GB) ve güncel zirve başlangıç değerini gerçek veriden çıkar.
2. Dönem için talebi öngör: organik eğilim (geçmişten), artı bilinen olaylar (çarpan ve kaynağıyla), artı belirsizlik aralığı (düşük/beklenen/yüksek).
3. Talebi her kısıtlı kaynak için kaynak ihtiyacına çevir: işlem gücü, bellek, veritabanı bağlantıları ve IOPS, depolama büyümesi, kuyruk iş hacmi, ağ çıkışı, üçüncü taraf hız limitleri ve bulut kotaları.
4. Kapasite birimi başına güvenli sınırı yük testlerinden veya canlı doygunluk noktalarından belirle; bunu hata noktasında değil, SLO gecikme eşiğinde ölç.
5. Gereken kapasiteyi hesapla: öngörülen zirve / birim başına güvenli sınır, artı pay (genellikle %20-40 `[ÖNERİ]`) ve yedeklilik (N+1 veya bölge kaybı toleransı); ilk darboğazı belirle.
6. Ölçekleme yollarını ve tedarik sürelerini kontrol et: hangi kaynaklar ne hızda otomatik ölçekleniyor, hangileri manuel değişiklik, hangileri satın alma veya kota artışı gerektiriyor; bunları olay tarihinden geriye doğru takvimle.
7. Doğrusal olmayan riskleri belirle: paylaşılan veritabanları, soğuk başlangıç davranışı olan cache'ler, bağlantı havuzu tükenmesi, bağımlılık limitleri, retry fırtınaları.
8. Her senaryo için maliyet etkisini fiyat uydurmadan tahmin et; verilen birim fiyatları kullan ya da maliyeti `[TBD]` olarak işaretle.
9. Tetikleyicileri ve izlemeyi tanımla: bir sonraki ölçekleme adımını başlatan kullanım eşikleri ve talep yüksek senaryoyu aşarsa yük atma (load shedding) veya kademeli bozulma planı.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, açık soruları listele ve sınırları doğrulamak için `performance-test-plan`, maliyeti iyileştirmek için `finops-review` veya bir darboğaz tasarım değişikliği gerektiriyorsa `scalability-review` öner.

## Çıktı formatı
```markdown
# Kapasite Planı: <servis> – <dönem veya olay>
Talep birimi: <birim> · Başlangıç zirvesi: <değer, kaynak> · Sahip: <ekip>

## Talep Öngörüsü
| Senaryo | Zirve talep | Dayanak |

## Kaynak Gereksinimleri
| Kaynak | Birim başına güvenli sınır | Mevcut | Gereken (pay ve N+1 ile) | Açık | Ölçekleme yolu | Tedarik süresi |

## Darboğazlar ve Doğrusal Olmayan Riskler
## Aksiyonlar ve Takvim
| Aksiyon | Sahip | Termin (olaya göre) |

## Maliyet Etkisi
## Tetikleyiciler, İzleme ve Kademeli Bozulma Planı
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Başlangıç değeri gerçek veriden zirve değerleri kullanıyor ya da `[BİLİNMİYOR]` olarak işaretli.
- [ ] Kotalar ve üçüncü taraf limitleri dahil her kısıtlı kaynak ele alındı.
- [ ] Güvenli sınırlar kırılma noktasında değil, SLO eşiğinde ölçüldü.
- [ ] Pay ve yedeklilik açıkça uygulandı ve ilk darboğaz adlandırıldı.
- [ ] Tedarik süresi gerektiren aksiyonlar olay tarihinden geriye doğru takvimlendi.
- [ ] Hiçbir büyüme oranı veya fiyat uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ortalama kullanıma göre plan yapmak. Doygunluğu zirveler belirler; zirve dakikayı veya ilgili yüzdelik dilimi kullan.
- Durumsuz pod'ları ölçekleyip hepsinin paylaştığı veritabanı bağlantı limitini unutmak.
- Maksimumunu, tepki süresini ve alttaki kotayı kontrol etmeden autoscaling'i kapasite saymak.

## Örnek
Girdi: "Checkout, normal zirve 800 istek/sn, 4 kat bekleniyor, 12 pod, tek birincil veritabanı."

Çıktıdan bir bölüm:
| Kaynak | Birim başına güvenli sınır | Mevcut | Gereken | Açık |
|---|---|---|---|---|
| API pod'ları | p99 < 400 ms'de pod başına 90 istek/sn `[VARSAYIM: son yük testinden, teyit et]` | 12 | 3200 / 90 × 1,3 pay ≈ 47 | +35 |
| DB bağlantıları | en fazla 500 | 12 × 20 = 240 | 47 × 20 = 940 | limiti aşıyor: ilk darboğaz |

Aksiyon: bağlantı havuzu proxy'si ekle veya pod başına havuz boyutunu düşür; olaydan önce yük testiyle doğrula.
