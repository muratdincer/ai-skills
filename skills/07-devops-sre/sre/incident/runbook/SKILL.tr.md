---
description: "Tek bir alarm veya hata modu için operasyonel runbook yazar: belirtiler ve etki, hızlı ön değerlendirme, net kontroller ve beklenen sonuçlarla teşhis dalları, doğrulama ve geri almayla güvenli çözüm adımları, eskalasyon ve takip. Bir page alarmının runbook'u yoksa, nöbetçiler yazılı olmayan bilgiye dayanıyorsa, bir olay eksik bir prosedürü gösterdiyse ya da tekrarlayan bir operasyonel sorunun nasıl ele alınacağı sorulduğunda kullanılır."
related: "alert-design, incident-response, known-error-article, postmortem, observability-plan"
prompt: "OrderQueueLagHigh alarmı için runbook yaz: order-events topic'inde Kafka consumer lag'i 10 dakika boyunca 10 bin'in üzerinde."
---

# Runbook Yazma

## Amaç
Sistemi tanımayabilecek bir nöbetçi mühendise, bir alarmdan veya belirtiden hafifletmeye giden, her adımı doğrulanabilir, güvenli ve hızlı bir yol vermek. Böylece toparlanma, o an nöbette kimin olduğuna bağlı kalmaz.

## Ne zaman kullanılır
- Bağlantılı runbook'u olmayan bir page alarmı var.
- Tekrarlayan bir operasyonel iş veya hata bir iki kişinin hafızasıyla yürütülüyor.
- Bir postmortem aksiyonu belgelenmiş bir prosedür istiyor.

## Ne zaman kullanılmaz
- Alarmın kendisi gürültülü veya aksiyon alınamaz durumdaysa önce `alert-design` ile düzeltilir; kötü bir alarm için geçici çözüm belgelenmez.
- Tam bir site veya bölge kurtarması gerekiyorsa `dr-plan` kullanılır.
- Hedef kitle son kullanıcılar veya bilinen bir geçici çözümü uygulayan destek ekibiyse `known-error-article` kullanılır.

## Girdiler
Zorunlu:
- Runbook'un kapsadığı alarm veya belirti ve etkilenen servis.
- Nedenler ve çözümler hakkında bilinenler (geçmiş olaylar, uzman notları) ya da çok az şey bilindiği bilgisi.

İsteğe bağlı, kaliteyi artırır:
- Mimari ve bağımlılıklar, panolar, log ve iz sorguları, erişim gereksinimleri.
- Bu hata için geçmiş olay zaman çizelgeleri ve postmortem'ler.
- Eskalasyon kişileri ve servis sahibi.

Alarm veya belirti net değilse sor. Kullanıcının vermediği komutlar, host adları ve sorgular `[TBD]` olarak işaretli yer tutuculardır; asla uydurma.

## Süreç
1. Alarmın kullanıcı açısından ne anlama geldiğini yaz: hangi kullanıcılar veya işlevler etkileniyor ve önem derecesi rehberi (ne zaman olay ilan edilir).
2. İlk beş dakikalık ön değerlendirmeyi yaz: alarmın gerçek olduğunu doğrula (pano bağlantısı, kontrol), kapsamı belirle (tek instance, zone, tenant veya tümü) ve son değişiklikleri kontrol et (deploy'lar, konfigürasyon, feature flag'ler, altyapı).
3. Olası nedenleri geçmişe dayanarak sıklık ve kontrol kolaylığına göre sırala; geçmiş verisi olmadan çıkarılan nedenleri `[VARSAYIM]` olarak işaretle.
4. Her neden için bir teşhis dalı yaz: net kontrol, neden buysa beklenen sonuç ve değilse sonraki adım.
5. Her neden için çözüm adımlarını yaz; riskli düzeltmelerden önce güvenli ve geri alınabilir hafifletmeleri tercih et (son değişikliği geri al, trafiği kaydır, ölçeği büyüt, tek bir instance'ı yeniden başlat, feature flag'i kapat).
6. Her çözüm adımına doğrulama (hangi sinyal ne kadar sürede normale döner) ve adım durumu kötüleştirirse geri alma ekle.
7. Tehlikeli adımları (veri silme, failover, kuyruk boşaltma) gereken onay ve ön koşullarla açıkça işaretle.
8. Eskalasyonu tanımla: ne zaman (süre sınırı, bilinmeyen neden, veri riski), kime ve hangi bilgilerle devredileceği.
9. Takibi ekle: olay zaman çizelgesine neyin kaydedileceği ve postmortem için neyin toplanacağı.
10. Üst bilgileri ekle: sahip, son gözden geçirme tarihi, son kullanım tarihi ve gözden geçirme tetikleyicisi (her kullanımdan sonra veya sistem değiştiğinde).
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, açık soruları listele ve sonraki becerileri öner: sorun büyürse `incident-response`, kullanımdan sonra `postmortem`, alarm ayar gerektiriyorsa `alert-design`.

## Çıktı formatı
```markdown
# Runbook: <alarm veya belirti>
Servis: <ad> · Sahip: <ekip> · Son gözden geçirme: <tarih veya [TBD]> · Önem rehberi: <ne zaman ilan edilir>

## Bu Ne Anlama Geliyor
## Ön Değerlendirme (ilk 5 dakika)
1. Doğrula: <kontrol> → <beklenen>
2. Kapsam: ...
3. Son değişiklikler: ...

## Teşhis
| Olası neden | Kontrol | Evet ise | Hayır ise |

## Çözüm
### Neden A
1. <adım> · Doğrula: <sinyal, süre> · Geri al: <nasıl>

## Tehlikeli Aksiyonlar (onay gerekir)
## Eskalasyon
## Takip ve Kayıtlar
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her adım somut ve doğrulanabilir; yer tutucular uydurulmak yerine `[TBD]` olarak işaretli.
- [ ] Ön değerlendirme, derin teşhisten önce son değişiklikleri ve kapsamı kontrol ediyor.
- [ ] Güvenli, geri alınabilir hafifletmeler riskli düzeltmelerden önce geliyor.
- [ ] Her çözüm adımının doğrulaması ve geri alması var.
- [ ] Tehlikeli aksiyonlar onay gerektiriyor ve ön koşulları belirtiyor.
- [ ] Eskalasyonun süre sınırı ve adı belli bir hedefi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Adım olarak "logları incele" yazmak. Sorguyu, alanı ve kötü sonucun neye benzediğini yaz.
- Kesinti sırasında kök neden düzeltmesine atlamak. Runbook'un işi önce hafifletmedir; kök neden postmortem'e aittir.
- Çürüyen runbook'lar. Gözden geçirmeyi her kullanıma ve sistem değişikliğine bağla, son kullanım tarihini kaydet.

## Örnek
Girdi: "OrderQueueLagHigh alarmı: order-events üzerinde 10 dk boyunca consumer lag > 10 bin."

Çıktıdan bir bölüm:
| Olası neden | Kontrol | Evet ise | Hayır ise |
|---|---|---|---|
| Yakın tarihli consumer deploy'u | Son 2 saatte order-consumer deploy geçmişi | Önceki sürüme geri al, lag eğilimini 10 dk izle | Sonraki satır |
| Zehirli mesaj | Tekrarlayan offset için consumer hata logları `[TBD: sorgu]` | Mesajı prosedüre göre dead-letter'a taşı (onay: servis sahibi) | Sonraki satır |
| Trafik artışı | 7 günlük başlangıç değerine karşı produce hızı | Consumer'ları partition sayısına kadar ölçekle | Sipariş ekibine eskale et |
