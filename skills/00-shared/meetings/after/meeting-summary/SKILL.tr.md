---
description: Bir toplantının sonuçla başlayan, kararları, önemli aksiyonları ve açık noktaları listeleyen ve okuyucunun dikkat etmesi gerekenleri öne çıkaran, bir dakikadan kısa sürede okunabilen yönetici özetini çıkarır. Bir yönetici, sponsor veya katılamayan paydaş toplantıdan ne çıktığını tüm notları veya dökümü okumadan öğrenmek istediğinde kullanılır.
related: meeting-notes, meeting-minutes, meeting-follow-up, executive-summary, action-item-extraction
prompt: Bu 1 saatlik mimari inceleme dökümünü CTO'muz için birkaç satırda özetle.
---

# Toplantı Özeti Çıkarma

## Amaç
Yoğun bir okuyucuya bir dakikadan kısa sürede toplantının neyi başardığını, neye karar verildiğini, sırada ne olduğunu ve ondan bir şey beklenip beklenmediğini anlatmak. Böylece okuyucu toplantıya katılmadan veya tam kaydı okumadan harekete geçebilir.

## Ne zaman kullanılır
- Bir sponsor, yönetici veya katılamayan paydaş toplantının sonucunu öğrenmek istiyorsa.
- Notlar veya döküm var ama hedef kitle için fazla uzunsa.
- Bir toplantı serisi için tutarlı, kısa bir kayıt gerekiyorsa.

## Ne zaman kullanılmaz
- Konu konu eksiksiz bir kayıt gerekiyorsa `meeting-notes` kullanılır.
- Katılım ve kararları içeren resmi bir kayıt gerekiyorsa `meeting-minutes` kullanılır.
- Özet, sonraki adımlarla birlikte katılımcılara mesaj olarak gönderilecekse `meeting-follow-up` kullanılır.

## Girdiler
Zorunlu:
- Toplantı notları, dökümü veya ne olduğunun anlatımı.

İsteğe bağlı:
- Hedef okuyucu ve neyi önemsediği, toplantı hedefi/gündemi, önceki kararlar, tercih edilen uzunluk.

Kaynak yoksa iste. Okuyucu bilinmiyorsa ekip dışındaki üst düzey bir paydaş için yaz.

## Süreç
1. Toplantı hedefini belirle ve karşılanıp karşılanmadığını değerlendir: Ulaşıldı / Kısmen / Ulaşılamadı. Bu ilk satırdır.
2. Açıkça mutabık kalınan kararları çıkar; mutabakat olmayan önerileri dikkate alma.
3. Okuyucu için önemli olan en fazla 5 aksiyonu seç (sorumlu ve tarih); geri kalanı için tam listeye atıf yap.
4. Bir planı, maliyeti, tarihi veya kapsamı değiştirebilecek açık noktaları ve riskleri listele.
5. Okuyucunun ne yapması gerektiğini belirle: karar, onay, engel kaldırma, bilgi sahibi olma. Hiçbiri yoksa "Sizden bir aksiyon beklenmiyor" yaz.
6. Ana sonucu somut ifadelerle tek cümlede yaz (ne, ne zamana kadar, hangi sonuçla).
7. Tartışma geçmişini, kimin ne dediğini ve okuyucunun bilmediği jargonu çıkar.
8. Olguları söylendiği gibi koru; çıkarım olanları `[VARSAYIM]`, eksikleri `[BİLİNMİYOR]` olarak işaretle.
9. Uzunluğu kontrol et: 80-150 kelime hedefle, asla yarım sayfayı geçme.
10. Kullanıcının hedefi devam ediyorsa özeti göndermek için `meeting-follow-up`, taahhütlere sorumlu ve tarih atanması gerekiyorsa `action-item-extraction` öner.

## Çıktı formatı
```markdown
**<Toplantı> – <tarih>: <Ulaşıldı / Kısmen / Ulaşılamadı>**
<Tek cümlelik ana sonuç.>

**Kararlar**
- <karar>

**Sonraki adımlar**
- <aksiyon> — <sorumlu> — <tarih>

**Açık noktalar / riskler**
- <madde> — <etki>

**Sizden beklenen:** <karar/onay/bilgi veya "Aksiyon beklenmiyor">
Tam notlar: <atıf veya [TBD]>
```

## Kalite kontrol listesi
- [ ] İlk satır hedefe ulaşılıp ulaşılmadığını söylüyor.
- [ ] Yalnızca açıkça mutabık kalınan maddeler karar olarak geçiyor.
- [ ] Her sonraki adımın sorumlusu ve tarihi ya da `[BİLİNMİYOR]` işareti var.
- [ ] Okuyucudan beklenen aksiyon açık.
- [ ] En fazla 150 kelime, okuyucunun bilmediği jargon yok.
- [ ] Girdide söylenmeyen her şey `[VARSAYIM]` olarak işaretlendi veya açık soru olarak listelendi; olgu gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sonuç yerine tartışmayı özetlemek ("önbelleklemeyi konuştuk"). Neyin değiştiğini yaz.
- Kötü haberi açık noktaların arasına gizlemek. Hedefe ulaşılmadıysa bunu ilk satırda söyle.
- Tüm aksiyonları listelemek. Okuyucunun önemsediklerini seç, tam listeye atıf yap.

## Örnek
Girdi: Sipariş işlemenin olay güdümlü yeniden tasarımına ilişkin 1 saatlik incelemenin dökümü.

Çıktıdan bir bölüm:
**Sipariş işleme yeniden tasarım incelemesi – 12 Mayıs: Kısmen ulaşıldı**
Hedef mimari onaylandı; geçiş yaklaşımı bir yük testi sonucuna kadar açık.
**Kararlar** – Yeni sipariş akışları için Kafka tabanlı olay omurgası onaylandı.
**Sizden beklenen:** 16 Mayıs'a kadar yük testi için 2 ek mühendis-haftasının onayı.
