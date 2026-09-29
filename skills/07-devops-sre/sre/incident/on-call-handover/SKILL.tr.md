---
description: Çıkan nöbetin notlarından, alarmlarından, olaylarından ve değişiklik takviminden gelen nöbetçi için bir nöbet devri yazar: açık olaylar ve durumları, yakın geçmişteki ve yaklaşan değişiklikler, bilinen riskler ve bozulmuş bileşenler, gürültülü veya susturulmuş alarmlar, sorumlusu belli bekleyen takipler ve eşikleri ile ilk aksiyonları açıkça tanımlanmış izlenecekler. Bir nöbet vardiyası veya rotasyonu sona erdiğinde, tatil ya da değişiklik dondurma döneminden önce veya bir üretim sisteminin sorumluluğu kişiler ya da ekipler arasında devredildiğinde kullanılır.
related: incident-response, runbook, postmortem, alert-design, incident-communication
prompt: Nöbet haftam yarın bitiyor. Notlarım, alarm özeti ve değişiklik takvimi ekte. Sonraki nöbetçi için devir notunu yaz.
---

# Nöbet Devri

## Amaç
Operasyonel farkındalığı aktarmak; böylece gelen nöbetçi birkaç dakika içinde neyin bozuk, neyin kırılgan olduğunu, neyin değişmek üzere olduğunu ve izlenen bir sinyal tetiklenirse ne yapacağını bilir. İyi bir devir, bilinen sorunların gece 3'te yeniden keşfedilmesini önler.

## Ne zaman kullanılır
- Bir nöbet vardiyası veya rotasyonu bittiğinde ve sorumluluk sıradaki kişiye geçtiğinde.
- Bağlamın açık olması gereken tatiller, değişiklik dondurmaları veya büyük lansmanlar öncesinde.
- Bir servisin sorumluluğu ekipler veya zaman dilimleri arasında geçtiğinde (follow-the-sun).

## Ne zaman kullanılmaz
- Süren bir olay koordinasyon gerektiriyorsa `incident-response` kullanılır.
- Tamamlanmış bir olay resmi inceleme gerektiriyorsa `postmortem` kullanılır.
- Tekrarlayan prosedürler belgelenecekse `runbook` kullanılır.

## Girdiler
Zorunlu:
- Çıkan nöbetin materyali: notlar, vardiya sırasındaki olaylar ve alarmlar veya serbest metin bir açıklama.

İsteğe bağlı, kaliteyi artırır:
- Gelecek vardiyanın değişiklik ve sürüm takvimi, bakım pencereleri, susturulmuş alarmlar listesi.
- Açık kayıtlar ve takipler, SLO ve hata bütçesi durumu, eskalasyon kişileri.

Vardiya materyali verilmemişse iste. Bölümleri genel içerikle doldurma; boş bölümler "bildirilen yok" olarak belirtilir.

## Süreç
1. Başlığı oluştur: servis kapsamı, zaman dilimiyle vardiya dönemi, çıkan ve gelen roller, tek satırlık gerekçeyle genel durum (Yeşil/Sarı/Kırmızı).
2. Açık olayları ve problemleri listele: mevcut durum, etki, uygulanan hafifletme, sonraki adım, sorumlu ve kanal ya da kayıt bağlantıları. Çözülmemiş her şeyi "muhtemelen sorun yok" değil, hâlâ açık olarak işaretle.
3. Bozulmuş veya kırılgan bileşenleri listele: geçici çözümü olan bilinen sorunlar, geri alınması veya izlenmesi gereken manuel müdahaleler (yeniden başlatmalar, artırılmış replica sayısı, değiştirilen feature flag'ler, geçici yapılandırma).
4. Alarm hijyenini özetle: bilinen nedeniyle gürültülü alarmlar, bitiş zamanıyla susturulmuş alarmlar, tetiklenmesi gerekirken tetiklenmeyen alarmlar.
5. Yakın geçmişteki (son vardiya) ve yaklaşan (sonraki vardiya) değişiklikleri listele: deploy'lar, taşımalar, sertifika veya kimlik bilgisi süre dolumları, bakım pencereleri, üçüncü taraf olayları, trafik olayları.
6. İzlenecekleri tanımla: sinyal, eşik, neden önemli olduğu ve tetiklenirse ilk aksiyon ya da kullanılacak runbook.
7. Operasyonu etkileyen postmortem aksiyonları dahil, bekleyen takipleri sorumlusu ve bitiş tarihiyle listele.
8. Varsa SLO ve hata bütçesi durumunu ve eskalasyon ya da iletişim kişilerindeki değişiklikleri kaydet.
9. Kolay taranabilir tut: en acil olan önce, madde başına tek satır, yapıştırılmış loglar yerine bağlantılar; kimlik bilgilerini ve kişisel verileri maskele.
10. Çıkarıma dayalı her durumu `[VARSAYIM]`, bilinmeyen her şeyi `[BİLİNMİYOR]` olarak işaretle; durum Sarı veya Kırmızıysa kısa bir canlı devir görüşmesi öner. Hedef devam ediyorsa belgelenmemiş manuel düzeltmeler için `runbook`, gürültülü alarmlar için `alert-design`, inceleme gerektiren olaylar için `postmortem` öner.

## Çıktı formatı
```markdown
# Nöbet Devri: <servis/ekip> · <dönem, zaman dilimi>
Çıkan: <rol/ad> → Gelen: <rol/ad> · Genel durum: Yeşil/Sarı/Kırmızı – <gerekçe>

## Açık Olaylar ve Problemler
| Madde | Durum | Etki | Uygulanan hafifletme | Sonraki adım | Sorumlu | Bağlantı |
|---|---|---|---|---|---|---|

## Bozulmuş Bileşenler ve Manuel Müdahaleler
| Bileşen | Sorun / müdahale | Geri alma veya izleme süresi | Geçici çözüm |
|---|---|---|---|

## Alarmlar
- Gürültülü: ...
- Susturulmuş (bitiş): ...
- Kaçırılan / boşluklar: ...

## Değişiklikler
| Ne zaman | Değişiklik | Risk | İletişim |
|---|---|---|---|

## İzlenecekler
| Sinyal | Eşik | Neden | İlk aksiyon / runbook |
|---|---|---|---|

## Bekleyen Takipler
| Madde | Sorumlu | Bitiş |
|---|---|---|

## SLO / Hata Bütçesi ve Eskalasyon Notları
```

## Kalite kontrol listesi
- [ ] Her açık olayın durumu, sonraki adımı ve sorumlusu var; sessiz olduğu için hiçbiri atlanmadı.
- [ ] Geçici manuel müdahalelerin ve susturulmuş alarmların geri alma veya bitiş zamanı var.
- [ ] Her izlenecek maddenin eşiği ve ilk aksiyonu var.
- [ ] Sonraki vardiyadaki yaklaşan değişiklikler, süre dolumları ve bakım pencereleri listelendi ya da olmadığı belirtildi.
- [ ] Hiçbir şey uydurulmadı; bilinmeyen durumlar `[BİLİNMİYOR]`, secret veya kişisel veri yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Devri anlatı biçiminde bir günlüğe çevirmek. Gelen nöbetçinin haftanın hikâyesine değil, önceliklendirilmiş bir listeye ihtiyacı var.
- Geçici düzeltmeleri unutmak: artırılmış bir replica set veya susturulmuş bir alarm sessizce yeni normal olur.
- Sonraki vardiyaya denk gelen süre dolumlarını (sertifikalar, kimlik bilgileri, susturmalar) atlamak.

## Örnek
Girdi: "Salı checkout gecikme sıçraması, 2 pod eklenerek hafifletildi, kök neden bilinmiyor. Log node disk alarmı cumaya kadar susturuldu. Perşembe 02:00'de DB minör sürüm yükseltmesi."

Çıktıdan bir bölüm:
- Genel durum: Sarı – checkout gecikmesinin nedeni hâlâ bilinmiyor; geçici ölçek artışı devrede.
| Bileşen | Sorun / müdahale | Geri alma veya izleme süresi | Geçici çözüm |
|---|---|---|---|
| checkout | Gecikme sıçramasından sonra 4'ten 6 pod'a çıkarıldı | Kök neden bulunana kadar koru `[VARSAYIM]` | p95 > SLO olursa daha da ölçekle |
| Sinyal | Eşik | Neden | İlk aksiyon / runbook |
|---|---|---|---|
| checkout p95 gecikme | 10 dk boyunca > SLO | Açıklanamayan sıçrama tekrarladı mı? | DB beklemelerini kontrol et, checkout runbook'unu izle |
| Log node disk alarmı | Susturma cuma bitiyor | Alarm susturulmuş, disk dolabilir | Bitişten önce disk kullanımını doğrula |
