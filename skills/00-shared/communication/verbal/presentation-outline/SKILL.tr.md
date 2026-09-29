---
name: presentation-outline
description: "Hedef kitleye özel bir akış ve her slaytta tek mesaj, destekleyici kanıt, net bir talep ve süre planı içeren slayt slayt bir sunum iskeleti çıkarır. Birinin yöneticilere, müşteriye, bir kurula veya ekibe öneri, durum, tasarım, sonuç ya da karar sunması gerektiğinde ve slaytları tasarlamadan önce yapıya ihtiyaç duyduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: communication
  area: verbal
  title: "Sunum iskeleti çıkarma"
  related: "executive-summary, steering-committee-pack, demo-script, elevator-pitch, stakeholder-map"
  prompt: "Yönetim ekibine, raporlama iş yüklerimizi gelecek yıl yeni veri platformuna taşımayı önerdiğimiz 20 dakikalık bir sunumun iskeletini çıkar."
---

# Sunum İskeleti Çıkarma

## Amaç
Bir konuyu ve hedef kitleyi, her slaytın kitleyi bir karara veya anlayışa taşıyan tek bir mesaj içerdiği bir akışa dönüştürmek; böylece slayt tasarımı bir içerik yığınından değil, sınanmış bir argümandan başlar.

## Ne zaman kullanılır
- Bir öneri, tasarım, sonuç veya durumun yüz yüze ya da çevrim içi sunulması gerektiğinde.
- Mevcut bir sunum uzun ve dağınıksa ve yeni bir akışa ihtiyaç varsa.
- Aynı içeriğin iki farklı kitleye (örneğin yöneticiler ve mühendisler) anlatılması gerektiğinde.

## Ne zaman kullanılmaz
- İçerik sunulmayacak, okunacaksa. `executive-summary` kullanın.
- Oturumun özü çalışan yazılımı göstermekse. `demo-script` kullanın.
- Bir yönetişim kurulu standart paketini bekliyorsa. `steering-committee-pack` kullanın.

## Girdiler
Zorunlu:
- Konu ve kitleden beklenen sonuç (karar verme, onaylama, anlama, benimseme).
- Hedef kitle (kim, kıdem, ne biliyor) ve ayrılan süre.

İsteğe bağlı:
- Kaynak materyal, veriler, kısıtlar, daha önce gelen itirazlar, kurum şablonu.

Beklenen sonuç veya kitle eksikse önce bunu sorun (her seferinde tek soru). Bilinmeyen rakam, tarih ve isimler `[TBD]` kalır; bir slaytı etkili kılmak için asla veri uydurmayın.

## Süreç
1. Ana mesajı tek cümleyle yazın: sunumun sonunda kitle ne düşünmeli veya ne yapmalı. Yazamıyorsanız konu hazır değildir; eksikleri açık soru olarak listeleyin.
2. Kitleyi profilleyin: karar yetkisi, neyi önemsedikleri (maliyet, risk, hız, müşteri, ekip yükü), ön bilgileri, olası itirazları. Her çıkarımı `[VARSAYIM]` olarak işaretleyin.
3. Akışı seçin: öneriler için Durum-Sorun-Çözüm, yöneticiler için önce cevap (piramit), teknik incelemeler için problem-yaklaşım-sonuç, değişim için önce-sonra-köprü.
4. Kıdemli kitlelerde talebi veya sonucu başa koyun; yalnızca önce bağlama ihtiyaç duyan kitlelerde sona doğru inşa edin.
5. Eylem başlıkları yazın: her slayt başlığı mesajını söyleyen tam bir cümledir ("Batch işler haftada iki kez 07:00 SLA'ini kaçırıyor"), etiket değildir ("Mevcut durum").
6. Her mesaja kanıt bağlayın: bir grafik, tablo, örnek veya alıntı; eksik kanıtı `[TBD: kaynak]` olarak işaretleyin.
7. Süreyi planlayın: içerik slaytı başına yaklaşık 2 dakika; sürenin en az %25'ini soru ve tartışmaya ayırın. Ana mesajı desteklemeyen slaytları eke taşıyın.
8. En olası 2-3 itirazı bir slaytla veya ekte hazır bir cevapla önceden karşılayın.
9. Açık bir taleple kapatın: karar, sorumlu, tarih ve sonraki adım.
10. Başlık testini yapın: yalnızca slayt başlıkları sırayla okunduğunda tüm hikâye anlaşılmalı. Boşlukları ve tekrarları düzeltin.
11. Kullanıcının hedefi devam ediyorsa canlı ürün bölümü için `demo-script`, ön okuma için `executive-summary`, kısa sözlü sürüm için `elevator-pitch` öner.

## Çıktı formatı
```markdown
# Sunum İskeleti: <başlık>
Kitle: <kim, karar yetkisi> | Süre: <dakika> | Beklenen sonuç: <karar/onay/...>
Ana mesaj: <tek cümle>
Akış: <DSÇ / önce cevap / ...>

| # | Eylem başlığı (mesaj) | Kanıt / görsel | Süre | Not |
|---|---|---|---|---|
| 1 | <mesaj cümlesi> | <grafik/tablo/örnek veya [TBD]> | 2 dk | |
| ... | | | | |
| n | Talep: <karar, sorumlu, tarih> | | | |

Soru-cevap payı: <dakika>
Beklenen itirazlar: <itiraz> -> <cevap / ek slayt>
Ek: <yedek slaytlar>
Varsayımlar ve açık sorular: [VARSAYIM] ... / [TBD] ...
```

## Kalite kontrol listesi
- [ ] Ana mesaj tek cümle ve kitlenin ne düşünmesi veya yapması gerektiğini söylüyor.
- [ ] Her slayt başlığı tam cümlelik bir mesaj; başlıklar tek başına hikâyeyi anlatıyor.
- [ ] Her mesajın kanıtı var ya da `[TBD]` olarak işaretli; uydurma rakam yok.
- [ ] Süre plana uyuyor ve en az %25'i tartışmaya kalıyor.
- [ ] Talep açık: karar, sorumlu, tarih.
- [ ] Başlıca itirazlar önceden ele alınmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yöneticilere kronolojik anlatım ("önce şunu yaptık, sonra şunu bulduk"). Cevapla başlayın.
- Başlık olarak konu etiketleri kullanmak; kitle her slaytı çözmek zorunda kalır. Mesajı başlığa yazın.
- Tüm analizleri ana akışa doldurmak. Ana akışta yalnızca mesajı destekleyenler kalsın, gerisi eke gitsin.

## Örnek
Girdi: 20 dakika, yönetim ekibi, raporlama iş yüklerini yeni veri platformuna taşıma önerisi.

Zayıf başlıklar: "Arka Plan", "Mevcut Mimari", "Seçenekler", "Sonraki Adımlar".

Güçlü (alıntı):
- Ana mesaj: Raporlamanın yeni platforma iki aşamalı taşınmasını, finans raporlarından başlayarak onaylayın `[tarih TBD]`.
- 1 "Raporlama sabah SLA'ini düzenli olarak kaçırıyor ve açık büyüyor" – SLA ihlali grafiği `[TBD: veri kaynağı]`.
- 2 "Mevcut platformu ölçeklemek taşımaktan daha pahalı" – maliyet karşılaştırması `[VARSAYIM: tahminler bekleniyor]`.
- 6 "Talep: 1. aşama bütçesini onaylayın ve `[tarih]` itibarıyla bir iş sahibi atayın".
