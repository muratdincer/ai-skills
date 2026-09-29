---
name: chaos-experiment
description: "Kontrollü bir kaos deneyi tasarlar: kararlı durum tanımı, yanlışlanabilir hipotez, enjekte edilecek hata, etki alanı ve kademeli kapsam, durdurma koşulları ve geri alma, gözlem planı, ön koşullar ve bulgu kaydı. Bir ekip dayanıklılık iddialarını (failover, retry, timeout, autoscaling) doğrulamak, bir game day hazırlamak ya da bir felaket kurtarma veya kademeli bozulma tasarımına güvenmeden önce onu sınamak istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: sre
  area: reliability
  title: "Kaos deneyi tasarlama"
  related: "resilience-review, dr-plan, slo-definition, runbook, observability-plan"
  prompt: "Sipariş servisimizin üç Redis replikasından birini kaybettiğinde müşteriye görünür hata olmadan ayakta kaldığını kontrol eden bir kaos deneyi tasarla."
---

# Kaos Deneyi Tasarlama

## Amaç
Bir dayanıklılık varsayımını, etki alanı sınırlı ve durdurma kuralları açık, güvenli ve yanlışlanabilir bir deneye dönüştürmek. Böylece ekip, sistemin hata altında gerçekte nasıl davrandığını müşteriler fark etmeden öğrenir.

## Ne zaman kullanılır
- Bir dayanıklılık mekanizması kâğıt üzerinde var (failover, retry, circuit breaker, autoscaling) ama hiç sınanmadı.
- Bir game day veya hata enjeksiyonu programı planlanıyor.
- Yakın tarihli bir olay, doğrulanması gereken gizli bir bağımlılığa veya zayıf bir yedek yola işaret ediyor.

## Ne zaman kullanılmaz
- Mimari henüz hata modları açısından incelenmediyse neyin test edileceğini bulmak için önce `resilience-review` kullanılır.
- Amaç tam bir site veya bölge kurtarma prosedürüyse `dr-plan` kullanılır (testleri daha sonra bu beceriyi kullanabilir).
- Sistem şu an kararsız veya bir olay yaşanıyorsa önce stabilize edilir; deneyler bilinen bir kararlı duruma ihtiyaç duyar.

## Girdiler
Zorunlu:
- Hedef sistem ve test edilecek dayanıklılık iddiası.
- Deneyin çalışabileceği ortam ve onayı kimin vereceği.

İsteğe bağlı, kaliteyi artırır:
- Normal davranışı tanımlayan SLO'lar ve panolar.
- Mimari ve bağımlılık haritası, bilinen hata geçmişi, mevcut runbook'lar.
- Mevcut hata enjeksiyonu yetenekleri ve değişiklik yönetimi kuralları.

İddia veya izin verilen ortam bilinmiyorsa sor. Açık onay ve bir durdurma mekanizması olmadan asla canlı ortamda enjeksiyon önerme.

## Süreç
1. Dayanıklılık iddiasını kullanıcının ifadesiyle yaz; ardından kararlı durumu, normal aralıklarıyla ölçülebilir sinyaller olarak tanımla (örn. başarı oranı, p99 gecikme, kuyruk lag'i), tercihen SLI'lar.
2. Yanlışlanabilir bir hipotez yaz: "<hedef> üzerinde <hata> olduğunda, <kararlı durum sinyalleri> <aralık> içinde kalır, çünkü <mekanizma>."
3. Enjekte edilecek hatayı ve gerçekçiliğini seç: instance veya pod sonlandırma, bağımlılıkta gecikme veya hata, ağ bölünmesi, kaynak tükenmesi, bölge kaybı, saat kayması, süresi dolmuş kimlik bilgisi.
4. Etki alanını sınırla: ortam, trafik veya host payı, süre, zaman penceresi ve kademeli plan (önce en küçük kapsam, yalnızca başarıdan sonra genişlet).
5. Kullanıcı etkisine bağlı durdurma koşullarını (örn. belirli bir eşiğin üstünde hata bütçesi tüketimi, SLI'nın bir tabanın altına düşmesi) ve geri almayı tanımla: hata nasıl durdurulur ve toparlanma ne kadar hızlı doğrulanır.
6. Ön koşulları listele: izleme kurulu ve takip ediliyor, nöbetçi bilgilendirildi, paydaşlara haber verildi, eşzamanlı değişiklik yok, onaylı değişiklik kaydı var, doğrulanmış bir manuel kurtarma yolu var.
7. Gözlemleri planla: hangi panolar, loglar ve izler kaydedilecek, kim neyi izleyecek ve çalışma sırasında hangi zaman çizelgesi notları alınacak.
8. Rolleri tanımla: deney lideri, hatayı enjekte eden operatör, gözlemci ve durdurma yetkisine sahip kişi.
9. Bulgu kaydını hazırla: hipotez doğrulandı mı çürütüldü mü, beklenen ve gözlenen davranış, sürprizler ve sahipli takip aksiyonları.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, açık soruları listele ve sonraki becerileri öner: müdahalede bulunan eksikler için `runbook`, tasarım düzeltmeleri için `resilience-review`, deney beklenmedik etki yarattıysa `postmortem` formatı.

## Çıktı formatı
```markdown
# Kaos Deneyi: <ad>
Sahip: <lider> · Ortam: <ortam> · Pencere: <tarih/saat veya [TBD]> · Onay: <kim>

## İddia ve Hipotez
- İddia: ...
- Kararlı durum: <sinyaller ve normal aralık>
- Hipotez: ... olduğunda ..., çünkü ...

## Hata Enjeksiyonu
| Hata | Hedef | Yöntem (tarafsız) | Süre |

## Etki Alanı ve Kademelendirme
## Durdurma Koşulları ve Geri Alma
## Ön Koşullar Listesi
## Roller
## Gözlem Planı
## Bulgular (çalışmadan sonra doldurulur)
| Beklenen | Gözlenen | Sonuç | Takip aksiyonu | Sahip |
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Hipotez yanlışlanabilir ve ölçülebilir kararlı durum sinyallerine dayanıyor.
- [ ] Etki alanı kapsam, trafik payı ve süre olarak sınırlı; genişleme kademeli.
- [ ] Durdurma koşulları kullanıcı etkisine bağlı ve hatayı durdurmanın sınanmış bir yolu var.
- [ ] Ön koşullar izleme, bilgilendirme, onay ve eşzamanlı değişiklik olmamasını içeriyor.
- [ ] Durdurma yetkisi adı belli bir kişide.
- [ ] Bulgu kaydı gözlenen olguları yorumdan ayırıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kararlı durum tanımlamadan deney yapmak. Başlangıç değeri olmadan "iyi görünüyordu" bir kanıt değildir.
- Canlı ortamda tam kapsamla başlamak. En küçük etki alanıyla, çoğu zaman canlı öncesi bir ortamda başla, sonra genişlet.
- Çürütülen hipotezi tatbikatın başarısızlığı saymak. Bir zayıflığı bulmak amacın ta kendisidir; kaydet ve düzelt.

## Örnek
Girdi: "Sipariş servisi üç Redis replikasından birinin kaybına dayanmalı."

Çıktıdan bir bölüm:
- Kararlı durum: 5 dakikalık pencerelerde sipariş API başarı oranı ≥ %99,9 ve p99 < 300 ms `[VARSAYIM: SLO'dan]`.
- Hipotez: Bir Redis replikası sonlandırıldığında başarı oranı ve p99 kararlı durum içinde kalır, çünkü istemci 5 sn içinde kalan replikalara yeniden bağlanır.
- Etki alanı: önce staging; ardından canlıda tek replika, 10 dakika, yoğun olmayan saat.
- Durdurma: başarı oranı art arda 2 dakika < %99,5 veya herhangi bir cache yazma hatası alarmı → replikayı yeniden başlat, toparlanmayı panoda teyit et.
