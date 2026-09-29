---
description: "Günlük ekip toplantısının (stand-up) notlarını veya dökümünü; iterasyon hedefine göre ilerlemeyi, günün planını, sahipli engelleri ve takip görüşmelerini kişi ve ekip bazında veren kısa bir özete dönüştürür. Stand-up notları, asenkron güncelleme mesajları veya toplantı dökümü paylaşılıp özet, engel listesi ya da katılmayanlar için bilgi istendiğinde kullanılır."
related: "impediment-tracking, meeting-summary, action-item-extraction, burndown-analysis, iteration-goal"
prompt: "Bu notlardan bugünkü stand-up'ı özetle ve engelleri listele: Emre ödeme API mock'unu bitirdi, test ortamı sertifikasında takıldı; Selin Emre'nin PR'ını inceliyor, sonra iade akışına başlayacak..."
---

# Günlük Toplantı Özeti

## Amaç
Ekibe ve katılamayanlara, iterasyonun hedefe göre nerede olduğunu, bugün ne yapılacağını ve hangi engellerin birinin aksiyonunu beklediğini iki dakikada okunacak şekilde vermek. Böylece günlük toplantı bir durum kaydına değil, koordinasyona dönüşür.

## Ne zaman kullanılır
- Stand-up yapıldı ve notların, dökümün veya asenkron yazılı güncellemelerin özetlenmesi gerekiyor.
- Laf arasında geçen engellerin yakalanıp doğru kişiye yönlendirilmesi gerekiyor.
- Bir lider veya ürün sahibi toplantıyı kaçırdı ve özeti istiyor.

## Ne zaman kullanılmaz
- Engelleri günler boyunca izlemek, eskale etmek ve çözmek için `impediment-tracking` kullanılır.
- Kararlar ve tartışma içeren daha uzun bir toplantıyı özetlemek için `meeting-summary` veya `meeting-minutes` kullanılır.
- Ekip dışındaki paydaşlara durum raporlamak için `status-update` kullanılır.

## Girdiler
Zorunlu:
- Toplantının notları, dökümü veya yazılı güncellemeleri.

İsteğe bağlı, kaliteyi artırır:
- İterasyon hedefi ve gün numarası (ör. 10 günün 6. günü).
- Pano görüntüsü veya devam eden maddelerin listesi.
- Önceki günlerden açık kalan engeller.

Notlar yoksa iste. İsteğe bağlı girdileri sorma; eksik olduklarını belirt.

## Süreç
1. Girdiyi temizle: sohbet ve tekrarları çıkar, isimleri verildiği gibi koru. Notlarda kişisel veya sağlık bilgisi varsa (ör. hastalık izninin nedeni) bunları çıkar, yalnızca "müsait değil" yaz.
2. Kişi başına şunları çıkar: son toplantıdan beri biten, bugünkü plan, engel veya ihtiyaç duyulan yardım. Söyleneni çıkarımdan ayır; çıkarımları `[ÇIKARIM]` olarak etiketle.
3. Her engeli sınıflandır: engellendi (ilerleyemiyor), yavaşladı veya risk (ileride engelleyebilir). Kimin kaldırabileceğini ve bir sahibi olup olmadığını not et.
4. İlerlemeyi iterasyon hedefiyle ilişkilendir: yolunda, riskte veya yoldan çıktı; tek satırlık gerekçesiyle. Hedef bilinmiyorsa tahmin etme, bilinmediğini yaz.
5. Koordinasyon sinyallerini yakala: aynı madde üzerinde iki kişi, günlerdir kıpırdamayan devam eden işler, panoda olmayan işler, bir günden eski bekleyen incelemeler.
6. Toplantı dışına taşınacak takip görüşmelerini ("toplantı sonrası") katılımcılarıyla listele.
7. Verildiyse önceki günlerden açık engelleri gün cinsinden yaşlarıyla aktar.
8. Özeti çıktı formatında yaz; yaklaşık 25 satırın altında tut.
9. Kullanıcının hedefi devam ediyorsa eskalasyon gereken engeller için `impediment-tracking`, hedef riskteyse `burndown-analysis` öner.

## Çıktı formatı
```markdown
# Günlük Toplantı – <ekip>, <tarih> (<m> günün <n>. günü)
**İterasyon hedefi:** <hedef veya [BİLİNMİYOR]> – **Durum:** Yolunda / Riskte / Yoldan çıktı – <gerekçe>

## Engeller
| Engel | Tür | Etkilediği | Çözecek sahip | Yaş | Sonraki adım |
|---|---|---|---|---|---|

## Kişi Bazında
- **<isim>** – Biten: ... · Bugün: ... · İhtiyaç: ...

## Koordinasyon Sinyalleri
- ...

## Takip Görüşmeleri
- <konu> – <katılımcılar>

## Katılmayan / Bildirmeyen
- <isim veya yok>
```

## Kalite kontrol listesi
- [ ] Her engelin türü, etkilediği madde ve bir sahibi ya da `[BİLİNMİYOR]` sahibi var.
- [ ] Hedef durumu gerekçesiyle verildi veya hedef `[BİLİNMİYOR]` olarak işaretli.
- [ ] Çıkarımlar etiketli; kimseye söylemediği bir şey atfedilmedi.
- [ ] Müsaitlik dışındaki kişisel ayrıntılar çıkarıldı.
- [ ] Özet yaklaşık iki dakikada okunabiliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Hedefe doğru ilerleme yerine aktiviteyi ("X üzerinde çalıştı") özetlemek. Her zaman hedefe bağla.
- Bir engeli kişinin satırına gömmek. Her engeli tabloya taşı ki bir sahibi olsun.
- Özeti performans kaydı gibi kullanmak. Ekip odaklı tut; bireyleri puanlama.

## Örnek
Girdi: "Emre ödeme API mock'unu bitirdi, dünden beri test ortamı sertifikasında takılı. Selin Emre'nin PR'ını inceliyor, sonra iade akışı. Can hastaydı." Hedef: müşteriler staging'de kartla ödeme yapabilir. 10 günün 6. günü.

Çıktıdan bir bölüm:
- Durum: Riskte – test ortamı sertifikası düzelene kadar kartla ödeme test edilemiyor.
- Engel: Test ortamı sertifikasının süresi dolmuş | Engellendi | Ödeme API | `[BİLİNMİYOR]` (platform ekibi?) | 2 gün | Bugün platform ekibine ilet.
- Katılmayan: Can – müsait değil.
