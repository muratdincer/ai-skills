---
description: Kullanıcı hikâyesine dayalı akış, adım adım tıklama sırası, kitlenin değer gördüğü noktalara bağlı anlatım, hazır veri, süre planı ve her riskli adım için yedek plan içeren bir ürün veya özellik demo senaryosu yazar. Bir ekip yazılımı paydaşlara, müşteriye, bir inceleme oturumuna veya potansiyel müşteriye göstermesi gerektiğinde ve doğaçlama yerine prova edilebilir bir akış istediğinde kullanılır.
related: presentation-outline, iteration-review-prep, stakeholder-review-prep, uat-scenarios, elevator-pitch
prompt: Yeni fatura onay akışını iterasyon incelemesinde finans müdürlerine göstermek için 10 dakikalık bir demo senaryosu yaz.
---

# Demo Senaryosu Yazma

## Amaç
Çalışan yazılımı gerçekçi bir kullanıcı yolculuğu üzerinden gösteren, her adımı kitlenin önemsediği değere bağlayan ve olağan demo aksiliklerine dayanan, prova edilebilir bir akış hazırlamak; böylece oturum özürlerle değil geri bildirim veya kararla biter.

## Ne zaman kullanılır
- Tamamlanmış veya geliştirilmekte olan bir özellik iterasyon incelemesinde ya da paydaş oturumunda gösterilecekse.
- Bir müşteriye, potansiyel müşteriye veya yöneticiye ürün yeteneği gösterilecekse.
- Kısa ve tekrarlanabilir olması gereken bir tanıtım videosu kaydedilecekse.

## Ne zaman kullanılmaz
- Oturum çoğunlukla argüman ve veriden oluşuyor, canlı yazılım azsa. `presentation-outline` kullanın.
- Amaç kullanıcıların resmi kabulü ise. `uat-scenarios` kullanın.
- Yalnızca demo değil, inceleme toplantısının tamamı hazırlanıyorsa. `iteration-review-prep` veya `stakeholder-review-prep` kullanın.

## Girdiler
Zorunlu:
- Neyin gösterileceği (özellik, kapsam, ortam) ve kime.
- Ayrılan süre.

İsteğe bağlı:
- Kullanıcı hikâyeleri veya kabul kriterleri, bilinen hatalar, ortam ve veri kısıtları, kitlenin sonrasında cevaplaması gereken soru.

Özellik veya kitle bilinmiyorsa önce sorun. Kullanıcının doğrulamadığı ekranları veya davranışları tarif etmeyin; `[TBD: arayüzü doğrula]` olarak işaretleyin.

## Süreç
1. Demo hedefini tanımlayın: kitlenin sonrasında inanması veya karar vermesi gereken tek şey (ör. "2. bölgeye yaygınlaştırmayı onaylamak", "onay kurallarına geri bildirim vermek").
2. Kitlenin dünyasından bir persona ve gerçekçi bir senaryo seçin ("Ayşe, finans müdürü, ay sonunda 40 fatura onaylıyor"); menü turu yapmayın.
3. Akışı hikâye gibi sıralayın: tetikleyici, ana yol, "vay" anı, sonuç. En değerli anı dikkat düşmeden, ilk üçte birlik bölüme koyun.
4. Adımları akış tablosu olarak yazın: eylem (ne tıklanır veya yazılır), kitlenin gördüğü, değer diliyle anlatım noktası ("ikinci onay e-postasına gerek kalmıyor"); uygulama ayrıntısı değil.
5. Veriyi ve durumu hazırlayın: adlandırılmış hesaplar, test kayıtları, sıfırlama adımları, feature flag'ler; ekranda sentetik veya maskelenmiş veri kullanın, asla gerçek kişisel veya müşteri verisi göstermeyin.
6. Her adımın riskini işaretleyin (yavaş servis, kararsız entegrasyon, bilinen hata) ve yedek plan yazın: önceden kaydedilmiş klip, ekran görüntüsü, önceden açılmış ikinci sekme veya "anlat ve geç".
7. Kapsamı dürüstçe belirtin: bitmemiş veya taklit (mock) olan kısımları biri fark etmeden önce sesli söyleyin.
8. Süreyi planlayın: demo sürenin en fazla %60'ı olsun; kalan süre sorulara ve geri bildirim ya da karar talebine kalsın.
9. Sonda sorulacak, kullanılabilir cevap almaya yetecek kadar kapalı 2-3 hedefli geri bildirim sorusu yazın.
10. Demo öncesi kontrol listesi (ortam ayakta, oturum açık, bildirimler kapalı, yakınlaştırma seviyesi, veri sıfırlandı) ve prova notu ekleyin.
11. Kullanıcının hedefi devam ediyorsa çerçeve slaytları için `presentation-outline`, inceleme oturumunun geri kalanı için `iteration-review-prep` öner.

## Çıktı formatı
```markdown
# Demo Senaryosu: <kitle> için <özellik>
Hedef: <kitlenin karar vereceği/inanacağı> | Süre: <dk> (demo <dk>, soru-cevap <dk>)
Persona ve senaryo: <ad, rol, durum>
Kapsam dışı / taklit: ...

## Demo öncesi kontrol listesi
- [ ] <ad> ortamı ayakta, build <[TBD]>   - [ ] Test verisi sıfırlandı   - [ ] Bildirimler kapalı, yakınlaştırma %125

## Akış tablosu
| # | Eylem | Kitlenin gördüğü | Anlatım noktası (değer) | Risk | Yedek plan | Süre |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | Düşük/Orta/Yüksek | ... | 1 dk |

## Kapanış
- Tek cümlelik özet: ...
- Geri bildirim soruları: 1. ... 2. ...
- Talep / sonraki adım: ...
Varsayımlar: [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Demo menü menü bir tur değil, tek bir personanın senaryosunu izliyor.
- [ ] Her adımın değer odaklı bir anlatım noktası var.
- [ ] Orta veya yüksek riskli her adımın somut bir yedek planı var.
- [ ] Ekranda gerçek kişisel veya müşteri verisi görünmüyor.
- [ ] Bitmemiş veya taklit kısımlar açıkça belirtilmiş.
- [ ] Süre planı, sürenin en az %40'ını soru ve geri bildirime bırakıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İş kitlesine build pipeline'ı, yönetim ekranlarını veya kodu göstermek. Kullanıcının elde ettiği sonucu gösterin.
- Uzun formları canlı doldurmak. Önceden doldurun, yalnızca anlamlı alanları gösterin.
- "Sorusu olan var mı?" deyip sessizlikle bitirmek. Senaryoda hazırlanan belirli geri bildirim sorularını sorun.

## Örnek
Girdi: 10 dakika, finans müdürleri, yeni fatura onay akışı.

Zayıf adım: "Faturalar menüsünü aç, sonra Ayarlar'a gir, akış yapılandırma tablosunu göster."

Güçlü (alıntı):
| 2 | Gelen kutusundan INV-TEST-014 faturasını aç | Tutar limit üstünde, otomatik olarak ikinci onaylayıcıya yönlendirilmiş | "Artık e-posta iletmek yok: limit üstü faturalar doğru onaylayıcıyı kendisi buluyor" | Orta (yönlendirme servisi yavaş) | Yönlendirilmiş faturanın açık olduğu ikinci sekme | 1,5 dk |
Geri bildirim sorusu: "10 bin € eşiği `[TBD: doğrula]` bölgeniz için doğru mu, yoksa masraf merkezi bazında ayarlanabilir mi olmalı?"
