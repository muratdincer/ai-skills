---
description: "Bulut veya platform harcamasını inceleyerek israfı, doğru boyutlandırma fırsatlarını, taahhüt ve fiyatlandırma modeli seçeneklerini, depolama ve veri transferi tasarruflarını ve etiketleme/dağıtım boşluklarını bulur; efor ve riskle önceliklendirilmiş bir tasarruf listesi verir. Bir maliyet raporu, fatura dökümü veya kaynak envanteri paylaşıldığında, maliyetler beklenmedik şekilde arttığında ya da periyodik maliyet incelemesi zamanı geldiğinde kullanılır."
related: "cloud-cost-estimate, capacity-planning, iac-review, environment-strategy, budget-proposal"
prompt: "Son üç ayın servis ve kaynak grubu bazında bulut maliyetleri ekte. Nerede para israf ediyoruz ve önce ne yapmalıyız?"
---

# Bulut Maliyet İncelemesi

## Amaç
Bir maliyet veri setini, güvenilirlikten ödün vermeyen, sahibi belli ve önceliklendirilmiş tasarruf aksiyonlarına dönüştürmek ve kimin ne harcadığını gizleyen dağıtım boşluklarını kapatmak.

## Ne zaman kullanılır
- Bir fatura dökümü, maliyet analiz aracı çıktısı veya kaynak envanteri mevcut olduğunda.
- Harcama kullanımdan veya bütçeden hızlı arttığında.
- Üç aylık veya aylık FinOps incelemesi zamanı geldiğinde.
- Taahhüt (rezervasyon/tasarruf planı tarzı) alımları değerlendirilirken.

## Ne zaman kullanılmaz
- Henüz kurulmamış bir sistemin maliyeti tahmin ediliyorsa `cloud-cost-estimate` kullanılır.
- Büyüme için kaynak ihtiyacı öngörülüyorsa `capacity-planning` kullanılır.
- Gelecek yılın bütçesi talep ediliyorsa `budget-proposal` kullanılır.

## Girdiler
Zorunlu:
- En az bir aylık (ideal olarak üç aylık) dönem için en azından servis ve kaynak ya da etiket bazında maliyet verisi.

İsteğe bağlı, kaliteyi artırır:
- Kullanım metrikleri (CPU, bellek, depolama IOPS, istek hacmi), ortam etiketleri, mevcut taahhütler ve bunların kapsama/kullanım oranları.
- Birim maliyet analizi için iş sürücüleri (aktif kullanıcı, işlem sayısı).
- Yedekliliği gerekçelendiren güvenilirlik kısıtları (SLO'lar, DR gereksinimleri).

Maliyet verisi yoksa iste. Asla tutar uydurma; yalnızca verilen veriden hesapla, tahminleri `[VARSAYIM]` ile aralık olarak etiketle.

## Süreç
1. Harcamayı özetle: toplam, eğilim, ilk 10 servis ve kaynak, ortam ve ekip bazında pay; dağıtılmamış (etiketsiz) harcama oranını işaretle.
2. İsrafı bul: boşta veya sahipsiz kaynaklar (bağlı olmayan diskler, kullanılmayan IP'ler, boştaki load balancer'lar, durdurulmuş ama faturalanan makineler, eski snapshot'lar), 7/24 çalışan üretim dışı ortamlar, gereğinden uzun saklanan loglar.
3. Doğru boyutlandırma: ayrılan ve kullanılan kapasiteyi karşılaştır; daha küçük boyut, otomatik ölçekleme veya yeni nesil tipler öner; SLO'larla tutarlı pay bırak.
4. Fiyatlandırma modeli: taahhüt kapsama ve kullanım oranları, yalnızca kararlı taban kullanıma dayalı taahhüt adayları, hataya dayanıklı iş yükleri için spot/preemptible.
5. Depolama ve veri: katmanlama ve yaşam döngüsü politikaları, sıkıştırma, politikayla uyumlu saklama, yedek tekrarları.
6. Ağ: zone ve bölge arası transfer, egress, NAT/gateway işlem ücretleri, CDN önbellekleme.
7. Mimari düzey: yönetilen servis ile kendi kurulumun karşılaştırması, çok konuşkan tasarımlar, aşırı boyutlu veritabanları, lisans dahil ile kendi lisansını getirme.
8. Birim ekonomisi: sürücüler varsa işlem/kullanıcı/kiracı başına maliyet.
9. Aksiyonları tasarruf (veriden), efor ve riske göre önceliklendir; sahip ve doğrulama metriği ata.
10. Yönetişim öner: etiketleme politikasının zorunlu kılınması, bütçeler ve anomali alarmları, showback/chargeback.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa talebe dayalı boyutlandırma için `capacity-planning`, etiketleme ve boyutlandırmayı kodda zorunlu kılmak için `iac-review` veya sonraki bütçe dönemi için `budget-proposal` öner.

## Çıktı formatı
```markdown
# Bulut Maliyet İncelemesi: <kapsam, dönem>
## Harcama Özeti
- Toplam / eğilim / dağıtılmamış pay
| Sıra | Servis/kaynak | Maliyet | Pay | Eğilim |
## Tasarruf Listesi
| # | Aksiyon | Kategori | Kanıt | Tahmini tasarruf | Efor | Risk | Sahip |
## Taahhüt Önerisi
## Yönetişim Boşlukları
## Açık Sorular / Varsayımlar
```

## Kalite kontrol listesi
- [ ] Her tutar verilen veriye dayanıyor veya etiketli bir tahmin aralığı.
- [ ] Doğru boyutlandırma SLO ve DR kısıtlarına uyuyor.
- [ ] Taahhütler yalnızca kararlı taban kullanıma göre boyutlandırıldı.
- [ ] Her aksiyonun bir sahibi ve tasarrufu doğrulama yolu var.
- [ ] Dağıtılmamış harcama ölçüldü ve ele alındı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Doğru boyutlandırmadan önce taahhüt alıp israfı kilitlemek. Önce boyutlandır.
- DR veya SLO için var olan yedekliliği kesmek. Kaldırmadan önce nedenini kontrol et.
- İndirimler varken liste fiyatı üzerinden tasarruf saymak. Verideki efektif fiyatları kullan.

## Örnek
Girdi: 3 aylık döküm: compute %55, veritabanı %20, depolama %12; harcamanın %30'u etiketsiz; üretim dışı VM'ler 7/24 çalışıyor.

Çıktıdan bir bölüm:
| # | Aksiyon | Kanıt | Tahmini tasarruf | Efor | Risk |
|---|---|---|---|---|---|
| 1 | Üretim dışı compute'u gece ve hafta sonu kapat | Veride üretim dışı VM'ler 7/24 | ~ üretim dışı compute'un %60'ına kadar `[VARSAYIM: 12 saat x 5 gün kullanım]` | Düşük | Düşük |
| 2 | Oluşturma anında sahip/ortam etiketini zorunlu kıl | %30 etiketsiz | Maliyet dağıtımını mümkün kılar | Orta | Düşük |
