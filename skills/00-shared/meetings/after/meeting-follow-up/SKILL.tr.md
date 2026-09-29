---
name: meeting-follow-up
description: "Toplantı sonrasında katılımcılara ve paydaşlara teşekkür satırı, sonuç, kararlar, sorumlu ve tarihli aksiyonlar, açık sorular, sonraki toplantı ve düzeltme son tarihi içeren takip mesajını yazar. Bir toplantının hemen ardından herkesin aynı anlayış ve taahhütlerle ayrılması için özet e-posta veya sohbet mesajı gönderilmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: meetings
  area: after
  title: "Toplantı sonrası takip mesajı"
  related: "meeting-summary, action-item-extraction, meeting-notes, stakeholder-email, open-questions-tracker"
  prompt: "Bu notlara göre bugün tedarikçiyle yaptığımız başlangıç toplantısının katılımcılarına bir takip e-postası yaz."
---

# Toplantı Sonrası Takip Mesajı

## Amaç
Kararları ve taahhütleri teyit eden, kayda dönüşmeden önce düzeltmeye davet eden kısa bir özet göndererek toplantının ortak anlayışını birkaç saat içinde sabitlemek.

## Ne zaman kullanılır
- Karar veya taahhüt içeren bir toplantının hemen ardından, özellikle ekipler arası veya dış taraflarla.
- Katılım kısmiyse ve katılamayanların sonucu öğrenmesi gerekiyorsa.
- Toplantıdaki taahhütlerin yazılı teyidi gerekiyorsa (tedarikçi, müşteri).

## Ne zaman kullanılmaz
- Hedef kitle yalnızca sonucu isteyen bir yöneticiyse `meeting-summary` kullanılır.
- Yönetişim için resmi kayıt gerekiyorsa `meeting-minutes` kullanılır.
- Takip aracı için yalnızca aksiyon listesi gerekiyorsa `action-item-extraction` kullanılır.

## Girdiler
Zorunlu:
- Toplantı notları, dökümü veya sonuçların anlatımı.

İsteğe bağlı:
- Alıcı listesi ve dış tarafların olup olmadığı, gönderenin rolü, kanal (e-posta veya sohbet), sonraki toplantı tarihi, materyal bağlantıları.

Dış alıcılar varsa neyin paylaşılabileceğini teyit et; yalnızca içeride kalması gereken ifadeleri ekleme.

## Süreç
1. Kanalı ve uzunluğu seç: dış veya resmi gruplar için e-posta, küçük iç ekipler için sohbet. 120-250 kelime hedefle.
2. Konu satırını yaz: `Takip: <toplantı> – <tarih> – kararlar ve sonraki adımlar`.
3. Bir satırlık teşekkür ve en önemli tek sonuçla başla.
4. Kararları kısa ifadelerle listele; yalnızca açıkça mutabık kalınanlar.
5. Aksiyonları "Sorumlu – aksiyon – tarih" biçiminde listele. Tek kişiye yazıyorsan onun aksiyonlarını başa koy.
6. Açık soruları kimin, ne zamana kadar cevaplayacağıyla listele.
7. Sonraki adımları ekle: sonraki toplantı tarihi/saati veya onu tetikleyecek olay; notlar, sunum, kayıt bağlantıları.
8. Düzeltme satırı ekle: "Buradakilerden anladığınızla örtüşmeyen bir şey varsa lütfen <tarih> tarihine kadar yanıtlayın."
9. Tonu hedef kitleye göre ayarla: dış taraf = daha resmi, iç jargon ve iç anlaşmazlıklar yok; iç ekip = doğrudan.
10. Alıcılar dış taraf veya geniş bir liste ise hassas ayrıntıları (fiyat, kişisel veri, iç pozisyonlar) çıkar.
11. Kullanıcının hedefi devam ediyorsa çözülmemiş noktaları canlı tutmak için `open-questions-tracker`, toplantıda olmayan kişilere ayrı bir mesaj için `stakeholder-email` öner.

## Çıktı formatı
```markdown
Konu: Takip: <toplantı> – <tarih> – kararlar ve sonraki adımlar

Merhaba,

Bugün ayırdığınız zaman için teşekkürler. Ana sonuç: <tek cümle>.

Kararlar
- <karar>

Aksiyonlar
- <Sorumlu> – <aksiyon> – <tarih>

Açık sorular
- <soru> – <kim> – <ne zamana kadar>

Sonraki adımlar
- Sonraki toplantı: <tarih/saat veya tetikleyici veya [TBD]>
- Materyaller: <bağlantılar veya [TBD]>

Buradakilerden anladığınızla örtüşmeyen bir şey varsa lütfen <tarih> tarihine kadar yanıtlayın.

<Gönderen>
```

## Kalite kontrol listesi
- [ ] Gönderilmeye hazır: konu, hitap, kapanış ve gönderen mevcut.
- [ ] Kararlar ve aksiyonlar kaynakla uyumlu; hiçbir şey uydurulmadı.
- [ ] Her aksiyonun sorumlusu ve tarihi ya da `[TBD]` işareti var.
- [ ] Bir düzeltme son tarihi eklendi.
- [ ] İçerik en az güvenilen alıcıya (dış taraf, geniş liste) uygun.
- [ ] Girdide söylenmeyen her şey `[VARSAYIM]` olarak işaretlendi veya açık soru olarak listelendi; olgu gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Mesajı günler sonra göndermek. Değer hızdan gelir; aynı gün taslakla.
- Tartışmayı anlatmak. Yalnızca sonuçları, aksiyonları, soruları ve sonraki adımları tut.
- İç notları dış alıcılara sızdırmak. Her satırı en geniş kitle açısından gözden geçir.

## Örnek
Girdi: Tedarikçiyle başlangıç toplantısı; her salı haftalık durum görüşmesi, tedarikçi cumaya kadar kadro planını gönderecek, ekibimiz çarşambaya kadar API spesifikasyonlarını paylaşacak; veri yerleşimi sorusu açık.

Çıktıdan bir bölüm:
Ana sonuç: Çalışma modelinde ve ilk iki haftanın teslimatlarında anlaştık.
Aksiyonlar
- <Tedarikçi PY> – Kadro planını gönder – Cuma `[tarihi teyit et]`
- <Teknik liderimiz> – API spesifikasyonlarını paylaş – Çarşamba `[tarihi teyit et]`
Açık sorular
- Üretim verisi nerede barındırılacak (veri yerleşimi)? – [BİLİNMİYOR] – sözleşme imzasından önce
