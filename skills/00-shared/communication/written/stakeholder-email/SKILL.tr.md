---
description: Paydaşa; eylemi belirten bir konu satırı, ilk iki satırda talep veya ana mesaj, yalnızca gerekli bağlam ve okuyucunun rolüne ve ilişkiye uygun bir tonla amacı önde olan bir e-posta yazar. Bir yöneticiden, sponsordan, müşteriden, tedarikçiden veya başka bir ekipten e-posta ya da uzun sohbet mesajıyla bir şey istemek, bilgi vermek, uzlaşmak veya takip etmek gerektiğinde kullanılır.
related: tone-rewrite, escalation-message, bad-news-delivery, stakeholder-map, meeting-follow-up
prompt: Finans direktörüne, gelecek hafta UAT'ye başlayabilmemiz için ekibinin yeni maliyet dağıtım kurallarını cumaya kadar doğrulamasını isteyen bir e-posta yaz.
---

# Paydaş E-postası Yazma

## Amaç
Okuyucunun mesajı konu satırından ve ilk iki cümleden anlayıp harekete geçmesini sağlamak; tonu ilişkiye uygun tutmak. Böylece talep, ek açıklama gerekmeden zamanında yanıtlanır.

## Ne zaman kullanılır
- Bir paydaştan karar, görüş, onay, veri veya zaman istenirken.
- Bir paydaşa onu etkileyen bir konuda bilgi verilirken.
- Başka bir ekip, müşteri veya tedarikçiyle uzlaşma ya da takip yapılırken.

## Ne zaman kullanılmaz
- Bloke olmuş bir konu üst seviyeye taşınıyorsa `escalation-message` kullanılır.
- Gecikme, iptal veya başarısızlık iletiliyorsa `bad-news-delivery` kullanılır.
- Yalnızca mevcut bir taslağın tonu düzeltilecekse `tone-rewrite` kullanılır.

## Girdiler
Zorunlu:
- Alıcı (rol, ilişki) ve amaç: ne bilmesini veya ne yapmasını istediğin.

İsteğe bağlı:
- Bağlam, son tarih ve gerekçesi, ekler, önceki yazışma, kültürel veya resmiyet beklentileri, gönderenin rolü.

Amaç veya alıcı belirsizse her seferinde tek soru sor. Bilinmeyen tarih, isim ve rakamları `[TBD]` olarak bırak; uydurma.

## Süreç
1. E-postayı sınıflandır: talep (karar, görüş, onay), bilgilendirme, uzlaşma veya takip. Bir e-posta, bir ana amaç; birbiriyle ilgisiz iki talep varsa ayır.
2. Alıcıyı oku: rolü, sonuç üzerindeki gücü, neyi önemsediği (maliyet, risk, müşteri, ekibinin iş yükü), ilişkinin resmiyeti. Alıcı hakkında çıkardığın her şeyi varsayım olarak işaretle.
3. Konu satırını `[Aksiyon/Bilgi] <konu> – <varsa son tarih>` biçiminde yaz (ör. "Aksiyon gerekli: maliyet dağıtım kurallarının 14 Mart cumaya kadar doğrulanması").
4. İlk iki cümleyi yaz: talep veya ana mesaj ve bunun okuyucu için neden önemli olduğu.
5. Yalnızca harekete geçmek için gereken bağlamı ekle: ne, neden şimdi, gecikirse ne olur. En fazla üç kısa paragraf veya madde.
6. Talebi uygulanabilir yap: net eylem, sorumlu, yanıt biçimi, gerekçesiyle son tarih ve işi kolaylaştırmak için ne sunacağın (ekli dosya, 15 dakikalık üzerinden geçme teklifi).
7. Tonu okuyucuya göre ayarla: üst düzey veya dış taraf = kısa ve resmi; eşdüzey = doğrudan ve sıcak; farklı kültür = açık, deyimsiz. Türkçede ilişki samimi değilse "siz" hitabını ve uygun unvanları (Hanım/Bey) kullan.
8. Genel bir "haber verirsiniz" yerine sonraki adımı ve sorumlusunu belirterek kapat.
9. Alıcıları kontrol et: Kime = harekete geçmesi gereken, Bilgi = bilmesi gereken; liste geniş veya dış taraf içeriyorsa hassas verileri çıkar.
10. Kullanıcının hedefi devam ediyorsa farklı bir üslup için `tone-rewrite`, talep son tarihe kadar yanıtsız kalırsa `escalation-message` öner.

## Çıktı formatı
```markdown
Kime: <harekete geçmesi gereken>   Bilgi: <bilmesi gereken>
Konu: <Aksiyon gerekli / Bilgi>: <konu> – <son tarih>

<Hitap>,

<Tek cümlede talep veya ana mesaj.> <Okuyucu için neden önemli.>

<Bağlam: 2-4 madde veya kısa cümle.>

<Talep: kim, ne yapacak, nasıl yanıtlayacak, ne zamana kadar ve neden o tarih.>
<Sunulan destek: ek, görüşme, iletişim kişisi.>

<Sonraki adım / kapanış>,
<Gönderen>

Gönderen için notlar: <yapılan varsayımlar, doldurulacak [TBD] alanlar>
```

## Kalite kontrol listesi
- [ ] Konu satırı tek başına okuyucunun harekete geçip geçmeyeceğini ve ne zamana kadar olduğunu söylüyor.
- [ ] Talep ilk iki cümlede.
- [ ] Tek bir ana amaç var; ikincil konular çıkarıldı veya açıkça ayrıldı.
- [ ] Son tarihin gerekçesi var; bilinmeyen değerler `[TBD]`, uydurulmadı.
- [ ] Ton ve resmiyet alıcıya ve kültüre uygun.
- [ ] Telefon ekranında talebi görmek için kaydırmak gerekmiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Önce geçmişi anlatıp talebi son satırda soran hikâye e-postaları. Sırayı ters çevir.
- Belirsiz ya da hiç yanıt getirmeyen muğlak talepler ("ne düşünürsünüz?"). Kapalı bir soru veya somut bir eylem iste.
- Baskı aracı olarak yöneticileri bilgiye eklemek. İlişkiyi zedeler; gerekiyorsa `escalation-message` ile açıkça eskale et.

## Örnek
Girdi: finans direktörü, UAT başlayabilsin diye maliyet dağıtım kurallarının cumaya kadar doğrulanması.

Zayıf: "Merhaba, umarım iyisinizdir. Bildiğiniz gibi bir süredir yeni maliyet dağıtım modülü üzerinde çalışıyoruz... Ekibiniz vakit bulduğunda bir göz atabilir mi acaba?"

Güçlü (bölüm):
Konu: Aksiyon gerekli: maliyet dağıtım kurallarının cuma `[tarih]` itibarıyla doğrulanması
"Ayşe Hanım merhaba, ekibiniz ekteki 12 dağıtım kuralını cumaya kadar doğrulayabilir mi? UAT pazartesi başlıyor ve bu kurallar için finans onayı olmadan başlayamıyor."
