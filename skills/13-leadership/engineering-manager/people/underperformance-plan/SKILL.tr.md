---
description: Belirli beklenti açıkları, ölçülebilir başarı kriterleri, sağlanan destek, ara değerlendirmeler ve açıkça belirtilmiş sonuçlarla adil ve kanıta dayalı bir performans iyileştirme planı (PIP) taslağı hazırlar; plan İK incelemesine hazır olur. Gayri resmi geri bildirimle çözülmeyen süregelen bir performans açığı olduğunda veya yönetici bir durumun resmi plana hazır olup olmadığını kontrol etmek istediğinde kullanılır.
related: performance-review, feedback-sbi, one-on-one-notes, bad-news-delivery, goal-setting
prompt: Nisan'dan beri geri bildirime rağmen PR'ları sürekli incelemeden geçemeyen ve üç sprint taahhüdünü kaçıran bir geliştirici için 60 günlük iyileştirme planı taslağı hazırla.
---

# Performans İyileştirme Planı

## Amaç
Kişiye başarılı olması için gerçek ve açık yapılandırılmış bir şans vermek: ne bekleniyor, nasıl ölçülecek, hangi destek sağlanacak ve sonunda ne olacak; hepsi belgelenmiş kanıtlara dayanır.

## Ne zaman kullanılır
- Rol beklentilerine göre bir açık, belgelenmiş gayri resmi geri bildirime rağmen sürüyorsa.
- İK veya politika, sonraki adımlardan önce yazılı bir plan gerektiriyorsa.
- Yönetici, kanıtların ve önceki geri bildirimlerin resmi bir planı başlatmak için yeterli olup olmadığını sınamak istiyorsa.

## Ne zaman kullanılmaz
- Konu henüz gayri resmi olarak konuşulmadıysa önce `feedback-sbi` ve `one-on-one-notes` kullanılır.
- Sorun disiplin veya politika ihlaliyse PIP değil, İK/disiplin süreci işletilir.
- Olağan değerlendirme yazımı için `performance-review` kullanılır.

## Girdiler
Zorunlu:
- Rol ve seviye beklentileri, açığa dair tarihli örnekler ve daha önce verilen geri bildirimin kayıtları.

İsteğe bağlı, kaliteyi artırır:
- Kurumun PIP şablonu, hukuki/İK kısıtları, standart süre.
- Açığı açıklayabilecek bağlam: iş yükü, belirsiz gereksinimler, araçlar, ekip değişiklikleri, İK'ya bildirilmiş sağlık veya kişisel durumlar.

Önceki geri bildirimin kaydı yoksa resmi planın erken olduğunu belirt ve önce belgelenmiş geri bildirim öner. Bu beceri İK veya hukuk danışmanlığının yerini tutmaz; paylaşmadan önce İK incelemesi öner.

## Süreç
1. Hazırlık kontrolü: Beklentiler açıktı, geri bildirim verildi ve belgelendi, makul süre geçti ve sistemik nedenler (belirsiz kapsam, aşırı yük, eksik oryantasyon, araçlar) elendi veya ele alındı.
2. Makul düzenleme veya destek ihtiyacı söz konusu olabilir mi kontrol et; öyleyse devam etmeden İK'ya yönlendir ve nedenler hakkında spekülasyon yapma.
3. 2-4 belirli açık alanı tanımla. Her biri için: beklenti, mevcut davranışın tarihli örnekleri, etki.
4. Her alan için bu seviyedeki ortalama bir çalışanın karşılayacağı, daha yüksek bir çıta olmayan ölçülebilir başarı kriterleri yaz.
5. Desteği listele: mentor veya eşli çalışma, netleştirilmiş öncelikler, eğitim, daha az bağlam değiştirme, haftalık görüşmeler.
6. Süreyi (yerel politikaya göre genellikle 30-90 gün) ve tarihli ara değerlendirmeleri belirle.
7. Başarı ve kriterlerin karşılanmaması durumundaki sonuçları tarafsız ve politikaya uygun biçimde yaz.
8. Dil kontrolü: davranışa odaklı, yargısız; kişilik etiketi, korunan özelliklere, izne veya özel hayata atıf yok.
9. Tutarlılık kontrolü: Benzer açıkları olan aynı seviyedeki diğer kişilerle beklentiler ve muamele aynı mı?
10. Haftalık kanıtlar için bir değerlendirme kaydı bölümü ekle ve her bilinmeyeni `[TBD]` veya `[BİLİNMİYOR]` olarak işaretle.

## Çıktı formatı
```markdown
# Performans İyileştirme Planı: <ad> [taslak – İK incelemesi gerekli]
Rol / seviye: <rol> · Yönetici: <ad> · Başlangıç: <tarih> · Bitiş: <tarih> · Süre: <gün>

## Arka Plan
- Önceki geri bildirimler: <tarihler, kanal, özet>

## Beklenti Açıkları ve Başarı Kriterleri
| Alan | Beklenti | Mevcut durum (tarihli örnekler) | Dönem sonu başarı kriteri | Ölçüm |
|---|---|---|---|---|

## Sağlanan Destek
- ...

## Ara Değerlendirmeler
| Tarih | Odak | Sonuç |
|---|---|---|

## Sonuçlar
- Kriterler karşılanırsa: ...
- Kriterler karşılanmazsa: <politikaya göre>

## Değerlendirme Kaydı
| Hafta | Kanıt | İlerleme (yolunda / riskli) | Notlar |
|---|---|---|---|
```

## Kalite kontrol listesi
- [ ] Belgelenmiş önceki geri bildirim var; yoksa plan erken olarak işaretlendi.
- [ ] Her açığın tarihli, gözlemlenebilir örnekleri var.
- [ ] Başarı kriterleri ölçülebilir ve daha yüksek bir çıta değil, seviyeye uygun.
- [ ] Somut destek, kimin sağlayacağıyla birlikte listelendi.
- [ ] Sonuçlar tarafsız ve politikaya dayalı; İK incelemesi işaretlendi.
- [ ] Etiket, nedenlere dair spekülasyon veya kişisel/sağlık ayrıntısı yok.

## Sık yapılan hatalar
- PIP'i önceden verilmiş bir karar için belge izi olarak kullanmak. Başarı için gerçek bir şans yoksa bunu İK ile konuş.
- Belirsiz kriterler ("iletişimi geliştir"). Gözlemlenebilir davranışı ve sıklığı belirt.
- Sürpriz. Plandaki hiçbir şey ilk kez PIP toplantısında duyulmamalı.

## Örnek
Girdi: "PR'lar sürekli incelemeden dönüyor; Nisan'dan beri üç sprint taahhüdü kaçtı; Nisan ve Haziran birebirlerinde geri bildirim verildi."

Çıktıdan bir bölüm:
| Kod kalitesi | PR'lar yalnızca küçük yorumlarla incelemeden geçer | Mayıs-Haziran'da 9 PR'dan 7'si büyük düzeltme gerektirdi (inceleme geçmişi) | PR'ların ≥ %80'i en fazla bir tur küçük yorumla birleştirilir `[ekip normuyla teyit et]` | PR inceleme geçmişi |
- Destek: Teknik liderle haftalık eşli çalışma; işler başlamadan önce kabul kriterleriyle netleştirilir.
