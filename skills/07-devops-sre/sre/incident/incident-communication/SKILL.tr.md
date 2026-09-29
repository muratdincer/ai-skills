---
description: "Her aşama (araştırılıyor, tespit edildi, izleniyor, çözüldü) ve hedef kitle için olay iletişimini yazar: iç paydaş güncellemeleri, yönetici özetleri ve herkese açık durum sayfası paylaşımları; teyitli etki, müşteri aksiyonları, sonraki güncelleme zamanı içerir ve neden hakkında spekülasyon yapmaz. Bir olay sırasında veya hemen sonrasında bir güncelleme, durum sayfası girdisi, müşteri bildirimi ya da yönetim brifingi yazılması veya gözden geçirilmesi gerektiğinde kullanılır."
related: "incident-response, customer-outage-notice, postmortem, bad-news-delivery, status-update"
prompt: "İlk durum sayfası güncellemesini ve iç Slack güncellemesini yaz: 09:40'tan beri AB müşterilerinin yaklaşık %20'sinde ödemeler başarısız, neden bilinmiyor, ekip inceliyor."
---

# Olay İletişimi Yazma

## Amaç
Bir olay sırasında her hedef kitleyi doğru bilgilendirmek: teyitli etkiyi ve sonraki adımları belirten, spekülasyon ve suçlamadan kaçınan, öngörülebilir aralıklarla gelen mesajlarla. Böylece güven korunur ve müdahale ekibi sorularla bölünmez.

## Ne zaman kullanılır
- Bir olay ilan edildi ve ilk veya takip güncellemesinin zamanı geldi.
- Bir durum sayfası paylaşımı, iç duyuru veya yönetici brifingi hazırlanmalı ya da gözden geçirilmeli.
- Olay çözüldü ve postmortem'den önce bir kapanış mesajı gerekiyor.

## Ne zaman kullanılmaz
- Olayın kendisi koordine edilmeliyse `incident-response` kullanılır.
- Olaydan sonra sözleşmesel veya yasal içerikli resmi bir müşteri bildirimi gerekiyorsa `customer-outage-notice` kullanılır.
- Amaç ne olduğunun tam analiziyse `postmortem` kullanılır.

## Girdiler
Zorunlu:
- Güncel olay olguları: etkilenen servis veya işlev, başlangıç zamanı, bilinen etki, durum aşaması.

İsteğe bağlı, kaliteyi artırır:
- Kullanılan hedef kitleler ve kanallar (durum sayfası, iç kanal, e-posta, müşteri temsilcileri).
- Kurum şablonları, üslup kuralları, yasal veya düzenleyici bildirim yükümlülükleri.
- Müşteri geçici çözümleri, gerçekten biliniyorsa tahmini süre, sonraki güncelleme zamanı.

Etki veya aşama bilinmiyorsa bunun için tek bir soru sor. Teyit edilmemiş bir nedeni, tahmini süreyi veya etkilenen müşteri sayısını asla yazma; `[TBD]` veya tarafsız bir ifade kullan.

## Süreç
1. Aşamayı (araştırılıyor, tespit edildi, izleniyor, çözüldü) ve şu an mesaj gereken hedef kitleleri belirle: müdahale ekibinin paydaşları, yöneticiler, müşteriler (herkese açık veya hedefli), iş ortakları.
2. Yalnızca teyitli olguları çıkar: kullanıcıların ne yaşadığı, ne zamandan beri, kapsam (bölgeler, özellikler, ölçüldüyse kullanıcı payı) ve ne yapıldığı; teyitsiz her şeyi işaretle ve dış metinden çıkar.
3. Dış mesajları kullanıcı diliyle yaz: belirti, etkilenen işlev, varsa geçici çözüm, sonraki güncelleme zamanı. İç sistem adlarını, neden hakkındaki spekülasyonu, tedarikçileri veya kişileri suçlamayı dışarıda bırak.
4. İç mesajlara şunları ekle: önem derecesi, olay komutanı, takip edilecek kanal, iş etkisi, gereken kararlar ve yapılmaması gerekenler (örn. ayrıca müşteriyle temas kurulmaması).
5. Yöneticiler için üç satır yaz: iş diliyle etki, güncel durum ve risk, gereken karar veya destek.
6. Her zaman sonraki güncelleme zamanını ekle ve haber olmasa da o zamana uy ("değişiklik yok, inceleme sürüyor").
7. Kişisel veri ve güvenliği kontrol et: müşteri kimlikleri yok, saldırganlara yardım edecek ayrıntı yok; veri ihlalinden şüpheleniliyorsa herhangi bir dış açıklamadan önce güvenlik ve hukuk sürecinden geçir.
8. Çözüldü mesajı için: çözüm zamanı, kullanıcıların hâlâ görebileceği etkiler (örn. gecikmeli bildirimler), kullanıcıların yapması gerekenler ve bir takip veya postmortem özeti yayımlanıp yayımlanmayacağı.
9. Üslubu gözden geçir: sade, sakin, sorumluluk alan, jargonsuz; küçümseyen ("ufak bir aksaklık") veya fazla söz veren ifadeler yok.
10. Çıkarımları `[VARSAYIM]` olarak etiketle, açık soruları listele ve sonraki becerileri öner: resmi takip için `customer-outage-notice`, kapanıştan sonra `postmortem`.

## Çıktı formatı
```markdown
# Olay İletişimi: <olay> · Aşama: <aşama> · <zaman, saat dilimi>

## Durum Sayfası (herkese açık)
**<Başlık: etkilenen işlev>**
<Kullanıcı diliyle belirti ve kapsam>. <Ne yapıyoruz>. <Varsa geçici çözüm>. Sonraki güncelleme en geç <zaman>.

## İç Güncelleme
Önem: <SEVn> · Komutan: <ad> · Kanal: <bağlantı veya ad>
- Etki: ...
- Durum: ...
- Gereken karar/destek: ...
- Sonraki güncelleme: <zaman>

## Yönetici Özeti (3 satır)
## Teyit Edilmemiş Konular (dış kullanım için değil)
## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Dış metin yalnızca teyitli olguları, kullanıcı diliyle, neden spekülasyonu ve iç adlar olmadan içeriyor.
- [ ] Her mesaj sonraki güncelleme zamanını belirtiyor.
- [ ] Her hedef kitle ihtiyaç duyduğu içeriği alıyor (müşteri aksiyonu, iç kararlar, yönetici riski).
- [ ] Kişisel veri veya saldırıya yarayacak ayrıntı yok; şüpheli ihlaller güvenlik ve hukuka yönlendirildi.
- [ ] Üslup sakin ve sorumluluk alan; küçümseme veya fazla söz verme yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İnsanları sakinleştirmek için tahmini süre vermek. Kaçırılan tahminler güvene "sonraki güncelleme 10:30'da" demekten daha çok zarar verir.
- Haber olmadığı için sessiz kalmak. "İnceleme sürüyor" güncellemesini zamanında paylaş.
- Erken bir neden söylemek ("veritabanı arızası") ve sonra yanlış çıkması. Neden teyit edilene kadar belirtiyi anlat.

## Örnek
Girdi: "~09:40'tan beri AB müşterilerinin ~%20'sinde ödemeler başarısız, neden bilinmiyor."

Zayıf durum sayfası paylaşımı: "eu-west'teki DB cluster'ımızda ufak bir aksaklık yaşıyoruz. 15 dakikada düzelir."

Güçlü durum sayfası paylaşımı:
**Avrupa'daki bazı müşterilerde kartlı ödemeler başarısız oluyor**
09:40 UTC'den bu yana Avrupa'daki bazı müşterilerimiz kartlı ödeme işlemlerini tamamlayamıyor. Diğer işlevler normal çalışıyor. Ekibimiz konuyu inceliyor. Sonraki güncelleme en geç 10:30 UTC'de.
