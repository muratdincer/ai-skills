---
name: retrospective-format
description: "Ekibin o anki ruh haline, konuya, büyüklüğüne ve ortamına uygun bir retrospektif formatı tasarlar: her retro aşaması için etkinlik seçer veya uyarlar, yönergeleri, süreleri ve malzemeleri yazar, formatın neden uygun olduğunu açıklar. Retrolar tekdüzeleştiğinde, belirli bir tema (olay, çatışma, kilometre taşı, yeni ekip) için özel bir retro gerektiğinde veya yeni bir retro fikri ya da şablonu istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Retrospektif formatı tasarlama"
  related: "retrospective-facilitation, team-health-check, workshop-plan, facilitation-guide, conflict-resolution"
  prompt: "Retrolarımız sıkıcı hale geldi ve hep aynı üç kişi konuşuyor. Zor bir sürümden sonra yorgun, 9 kişilik ekip için 45 dakikalık uzaktan bir retro formatı tasarla."
---

# Retrospektif Formatı Tasarlama

## Amaç
Kolaylaştırıcıya, etkinlikleri ekibin enerjisine ve eldeki konuya uyan, hemen uygulanabilir bir retrospektif tasarımı vermek. Böylece oturum yıpranmış bir rutini tekrarlamak yerine gerçek sorunları yüzeye çıkarır ve aksiyonlarda yakınsar.

## Ne zaman kullanılır
- Alışılmış format hep aynı konuları üretiyor veya katılım düşük.
- Temalı bir retro gerekiyor: olay veya zor bir sürüm sonrası, kilometre taşında, yeni kurulan ekip için, bir çatışma etrafında veya yıl sonunda.
- Ortam değişiyor (uzaktan, hibrit, büyük grup, çok kısa süre).

## Ne zaman kullanılmaz
- Oturumu yürütmek ve notlardan aksiyon üretmek için `retrospective-facilitation` kullanılır.
- Geçmiş çalışmayı değerlendirmeye yönelik olmayan genel bir çalıştay için `workshop-plan` kullanılır.
- Grup oturumu yerine arabuluculuk gerektiren kişilerarası bir çatışma için `conflict-resolution` kullanılır.

## Girdiler
Zorunlu:
- Ekip büyüklüğü, ortam (uzaktan/yerinde/hibrit) ve ayrılan süre.
- Yeni bir format isteme nedeni veya ele alınacak tema.

İsteğe bağlı, kaliteyi artırır:
- Ekibin ruh hali veya sağlık sinyalleri, son olaylar.
- Yakın zamanda kullanılmış formatlar (tekrarı önlemek için).
- Katılım sorunları (baskın sesler, sessizlik, yeni üyeler).

Neden veya ortam eksikse sor (en fazla 3 soru).

## Süreç
1. İhtiyacı teşhis et: enerji seviyesi (düşük/normal/yüksek), güven seviyesi (suçlama, sessizlik veya yakın zamanda çatışma varsa düşük) ve konu genişliği (açık değerlendirme veya odaklı tema). Teşhisi yaz ve çıkarım olan kısımları `[ÇIKARIM]` olarak işaretle.
2. Bilinen kalıplardan her aşama (ortamı hazırla, veri topla, içgörü üret, aksiyonlara karar ver, kapanış) için bir etkinlik seç; ör. giriş ölçekleri, zaman çizelgesi, kızgın/üzgün/memnun, 4L, yelkenli, başla/bırak/devam et, 5 neden, etki çemberi, nokta oylaması, ROTI. Her seçimin uygunluğunu tek satırda açıkla.
3. Güvene göre uyarla: güven düşükse anonim girdi, genel oturumdan önce ikili çalışma kullan ve kişilere değil sisteme odaklan ("bunu zorlaştıran neydi"). Başta bir güven kontrolü oylaması düşün.
4. Katılıma göre uyarla: konuşmadan önce sessiz yazma, sırayla okuma, konuşmacı başına süre sınırı; yaklaşık 8 kişiden büyük gruplar için 3-4 kişilik küçük gruplar.
5. Ortama göre uyarla: uzaktan çalışmada pano düzenini, anonim modu ve kameranın isteğe bağlı olduğu kısımları belirt; hibritte herkesin aynı dijital panoyu kullanmasını sağla.
6. Kolaylaştırıcının her etkinlik için söyleyeceği veya panoya yazacağı yönergeleri birebir yaz.
7. Aşamaların toplamı süreye eşit olacak şekilde etkinliklere dakika ayır; sürenin en az dörtte birini içgörü ve aksiyonlara bırak.
8. Malzemeleri ve hazırlığı listele (pano şablonu, zaman çizelgesi verisi, önceki aksiyonlar).
9. Yedek plan ekle: süre yetmezse neyin kısaltılacağı, enerji çok düşükse ne yapılacağı.
10. Kullanıcının hedefi devam ediyorsa oturumu yürütmek ve sonuçları aksiyona dönüştürmek için `retrospective-facilitation` öner.

## Çıktı formatı
```markdown
# Retro Formatı: <ad> – <tema>
Kimin için: <ekip büyüklüğü, ortam> · Süre: <dk>
Teşhis: enerji <D/N/Y>, güven <D/N/Y>, odak <açık/tema> – <neden>

| Aşama | Etkinlik | Dakika | Yönerge (birebir) | Neden uygun |
|---|---|---|---|---|
| Ortamı hazırla | | | | |
| Veri topla | | | | |
| İçgörü üret | | | | |
| Aksiyonlara karar ver | | | | |
| Kapanış | | | | |

## Katılım ve Güven Kuralları
- ...

## Hazırlık ve Malzemeler
- ...

## Süre Yetmezse / Enerji Düşükse
- ...
```

## Kalite kontrol listesi
- [ ] Beş aşamanın tamamı kapsandı ve dakikaların toplamı süreye eşit.
- [ ] Her etkinliğin birebir bir yönergesi ve teşhise bağlı tek satırlık gerekçesi var.
- [ ] Güven ve katılım uyarlamaları belirtilen sorunla örtüşüyor.
- [ ] Sürenin en az dörtte biri içgörü ve aksiyonlara ayrıldı.
- [ ] Verildiyse, format ekibin yakın zamanda kullandığı formatlardan farklı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Amaca hizmet etmeyen eğlenceli bir etkinlik seçmek. Yenilik bir araçtır; sonuç aksiyonlarda yakınsamaktır.
- Güvenin düşük olduğu sancılı bir olaydan sonra "ne yanlış gitti" çerçevesi kullanmak. Kişilerle değil olgularla (zaman çizelgesi) ve sistemle başla.
- Çok fazla etkinlik sıkıştırmak. 45-60 dakika için aşama başına bir etkinlik yeterlidir.

## Örnek
Girdi: "9 kişilik yorgun ekip, uzaktan, 45 dakika, zor bir sürüm sonrası; hep aynı üç kişi konuşuyor."

Çıktıdan bir bölüm:
- Teşhis: enerji düşük, güven normal `[ÇIKARIM]`, odak teması "sürüm".
- Veri topla: Sürüm zaman çizelgesi (10 dk) – "Sürümün riskte olduğunu hissettiğin bir anı anonim olarak ekle."
- İçgörü: 3'er kişilik 3 küçük grupta etki çemberi (12 dk) – tartışmayı dert yanmaktan ekibin kontrol ettiklerine taşır.
- Kapanış: ROTI 1-5 (3 dk).
