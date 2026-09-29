---
description: Yeni bir çalışan için aşama başına sonuçlar, somut ilk görevler, tanışılacak kişiler, erişim ve öğrenme ara hedefleri ile görüşme noktaları içeren 30-60-90 günlük bir oryantasyon planı yazar. Biri yeni bir ekibe veya role katıldığında, mentor ya da yöneticinin yapılandırılmış bir uyum sürecine ihtiyacı olduğunda veya mevcut plan yalnızca okunacak doküman listesinden ibaretse kullanılır.
related: technical-onboarding, onboarding-guide, goal-setting, one-on-one-prep, job-description
prompt: Gelecek ay ödeme ekibimize katılacak orta seviye bir backend mühendisi için 30-60-90 günlük plan yaz.
---

# 30-60-90 Günlük Oryantasyon Planı

## Amaç
Yeni çalışana ve yöneticiye ortak, sonuç odaklı bir uyum yolu vermek. Böylece her aşamanın beklentileri açık olur, destek planlanır ve ilerleme izlenimle değil kanıtla konuşulur.

## Ne zaman kullanılır
- Yeni bir çalışan, iç transfer veya terfi eden biri yeni rolüne başlıyor.
- Yöneticinin veya mentorun ilk günden önce bir plana ihtiyacı var.
- Önceki işe alımlar yavaş veya dengesiz uyum sağladı ve oryantasyonun yapıya kavuşması gerekiyor.

## Ne zaman kullanılmaz
- İhtiyaç yalnızca teknik kurulum ve kod tabanı turuysa `technical-onboarding` kullanılır.
- Herkes için genel bir ekip el kitabı gerekiyorsa `onboarding-guide` kullanılır.
- Uyum sonrasındaki uzun vadeli hedefler için `goal-setting` kullanılır.

## Girdiler
Zorunlu:
- Rol, seviye, ekip ve başlangıç tarihi (bilinmiyorsa "1. gün").

İsteğe bağlı, kaliteyi artırır:
- Ekibin misyonu, güncel öncelikleri, sahip olunan sistemler, nöbet modeli.
- Değerlendirme toplantısındaki güçlü yönler ve oryantasyon odağı, kişinin önceki rolü.
- Mentor, kilit paydaşlar, zorunlu eğitimler, erişim taleplerinin karşılanma süreleri.

Rol veya seviye yoksa sor; bunlar olmadan aşama beklentileri ayarlanamaz.

## Süreç
1. 90. gündeki son durumu seviye beklentileriyle uyumlu 2-3 sonuçla tanımla (ör. X servisinde orta büyüklükte değişiklikleri bağımsız teslim eder, nöbet rotasyonuna katılır).
2. 1. gün öncesini planla: ekipman, hesaplar, karşılanma süreleriyle erişim talepleri, atanmış mentor, ilk hafta takvimi.
3. 1-30. günler (öğren): ortam çalışıyor, 1-2. haftada ilk küçük değişiklik merge edildi, kilit kişilerle tanışıldı, mimari, müşteriler ve çalışma biçimi anlaşıldı.
4. 31-60. günler (katkı ver): kapsamı belirli işleri uçtan uca sahiplen, kod incelemelerine ve olaylara katıl, uygunsa nöbeti gölgele.
5. 61-90. günler (sahiplen): küçük bir özelliği veya iyileştirmeyi yönet, nöbette ters gölgeleme yap, taze bakış açısıyla bir iyileştirme öner.
6. Her aşama için 3-5 ölçülebilir başarı sinyali ve sağlanan desteği (mentor, eşli çalışma, dokümanlar, eğitimler) listele.
7. Kişi haritası ekle: kiminle, neden ve ne zamana kadar tanışılacak.
8. Görüşmeleri planla: haftalık birebirler, aşama sonlarında oryantasyonun kendisine dair karşılıklı geri bildirim içeren değerlendirmeler.
9. Çıtayı düşürmeden bağlama göre uyarla: yarı zamanlı, uzaktan, saat dilimleri, erişilebilirlik ihtiyaçları, önceki alan bilgisi; kişisel durumlar hakkında varsayımda bulunma.
10. Çıkarım yaptığın ekip bilgilerini (sistemler, rotasyon, araçlar) `[VARSAYIM]` olarak işaretle ve yöneticinin teyit etmesi gerekenleri listele.
11. Kullanıcının hedefi devam ediyorsa kurulum ayrıntısı için `technical-onboarding` veya 90. gün sonrası hedefler için `goal-setting` öner.

## Çıktı formatı
```markdown
# 30-60-90 Planı: <ad veya rol> – <ekip> – başlangıç <tarih>
Yönetici: <ad> · Mentor: <ad veya [TBD]>

## 90. Gün Sonuçları
1. ...

## 1. Günden Önce
- [ ] Erişim / ekipman / hesaplar – sorumlu – karşılanma süresi

## 1-30. Günler: Öğren
| Sonuç | İlk görevler | Başarı sinyalleri | Destek |
|---|---|---|---|

## 31-60. Günler: Katkı Ver
| Sonuç | Görevler | Başarı sinyalleri | Destek |
|---|---|---|---|

## 61-90. Günler: Sahiplen
| Sonuç | Görevler | Başarı sinyalleri | Destek |
|---|---|---|---|

## Tanışılacak Kişiler
| Kişi / rol | Neden | Tarih |
|---|---|---|

## Görüşmeler
- Haftalık birebir · 30. / 60. / 90. gün değerlendirmeleri (karşılıklı)

## Varsayımlar / Teyit Edilecekler
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her aşamanın yalnızca aktiviteleri veya okuma listesi değil, sonuçları var.
- [ ] İlk iki hafta içinde gerçek bir ilk katkı planlandı.
- [ ] Başarı sinyalleri gözlemlenebilir ve seviyeye göre ayarlı.
- [ ] Her aşama için destek (mentor, eşli çalışma, eğitimler) belirtildi.
- [ ] Görüşmeler yalnızca kişiye değil, oryantasyonun kendisine dair geri bildirimi de içeriyor.
- [ ] Kişisel durumlara dair varsayım yok; uyarlamalar seçenek olarak sunuldu.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bir ay boyunca doküman okutmak. Okumayı erken dönemde küçük, gerçek bir değişiklikle eşleştir.
- Seviyeye uymayan beklentiler (orta seviye birinden 60. günde mimariyi sahiplenmesini beklemek). Sonuçları seviye tanımına bağla.
- Erişim karşılanma sürelerini planlamamak. Talepleri 1. günden önce başlat.

## Örnek
Girdi: Orta seviye backend mühendisi, ödeme ekibi, servisler: payment-gateway, ledger; haftalık nöbet.

Çıktıdan bir bölüm:
- 90. gün sonucu: payment-gateway'de orta büyüklükte değişiklikleri bağımsız teslim eder ve bir haftalık ters gölgeleme nöbetini tamamlar.
- 1-30. gün ilk görev: Mentorla birlikte payment-gateway'deki etiketli bir başlangıç kaydını düzelt; 10. güne kadar merge edilsin.
- Zayıf sinyal (kaçın): "Sistemi anlıyor." Güçlü sinyal: "Mentorla yaptığı tahta oturumunda gateway ve ledger arasındaki iade akışını anlatıyor."
