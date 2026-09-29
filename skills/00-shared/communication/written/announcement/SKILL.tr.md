---
description: Bir değişikliği, sürümü, politikayı, süreci veya kararı; ne değişiyor, neden, kim ve nasıl etkileniyor, ne zaman yürürlüğe giriyor, okuyucunun ne yapması gerekiyor ve nereden yardım alınır yapısıyla duyuran bir metin yazar. Bir ekibin, departmanın veya kullanıcı kitlesinin yeni ya da farklı bir şeyden e-posta, sohbet kanalı, intranet yazısı veya bülten aracılığıyla haberdar edilmesi gerektiğinde kullanılır.
related: release-announcement, org-change-communication, communication-plan, faq-builder, stakeholder-email
prompt: Tüm yazılım ekiplerine 1 Mart'tan itibaren her canlı ortam dağıtımının yeni güvenlik tarama kapısından geçmesi gerektiğini ve o tarihe kadar ne yapmaları gerektiğini duyur.
---

# Duyuru Yazma

## Amaç
Etkilenen her okuyucunun neyin değiştiğini, kendisini etkileyip etkilemediğini ve ne zamana kadar ne yapması gerektiğini anlamasını sağlamak. Böylece benimseme zamanında gerçekleşir ve destek kanalları aynı sorularla dolmaz.

## Ne zaman kullanılır
- Bir gruba yeni bir süreç, politika, araç, standart veya son tarih uygulanacaksa.
- Bir karar alınmışsa ve yayılması gerekiyorsa.
- Bir iç sürüm, lansman veya kilometre taşı paylaşılacaksa.

## Ne zaman kullanılmaz
- Özellik ayrıntısı içeren müşteriye dönük sürüm içeriği için `release-announcement` veya `release-notes` kullanılır.
- Yeniden yapılanma, raporlama hattı veya rol değişiklikleri için `org-change-communication` kullanılır.
- Değişiklik bir gecikme, iptal veya başarısızlıksa `bad-news-delivery` kullanılır.

## Girdiler
Zorunlu:
- Neyin değiştiği veya duyurulduğu.
- Yürürlük tarihi veya zamanlaması.

İsteğe bağlı:
- Gerekçe, hedef kitle grupları, gereken aksiyonlar, sorumlu/iletişim kişisi, bağlantılar, istisnalar, önceki durum.

Hedef kitle veya yürürlük tarihi eksikse sor. Gerekçe uydurma: gerekçe bilinmiyorsa `[TBD – gerekçe]` bırak ve işaretle, çünkü "neden"i olmayan duyurular direnç yaratır.

## Süreç
1. Hedef kitleyi etkiye göre grupla: harekete geçmesi gerekenler, etkilenen ama aksiyon gerekmeyenler, yalnızca bilgilendirilenler. Grupların aksiyonları farklıysa her birine açıkça etiketlenmiş bir bölüm veya ayrı mesaj ver.
2. Değişikliği ve tarihi sade bir dille veren bir başlık yaz ("1 Mart'tan itibaren canlı ortam dağıtımlarında güvenlik tarama kapısı zorunlu").
3. Kısa özetle aç: ne, kim, ne zaman, ne yapmalısın; 2-3 satırda.
4. Nedeni okuyucunun tanıdığı bir problem veya faydaya bağlayarak bir ila üç cümlede açıkla; gerekiyorsa hangi karardan çıktığını belirt.
5. Neyin değiştiğini ve neyin değişmediğini yaz; "değişmeyenler" listesi söylentileri önler.
6. Gereken aksiyonları grup bazında, son tarihleriyle numaralı adımlar olarak listele.
7. Aşamalıysa zaman çizelgesini ekle: pilot, geçiş dönemi ve zorunlu uygulama tarihleri.
8. Yardım kanallarını ver: sorumlu, iletişim, dokümantasyon, soru-cevap saatleri; en olası 3 soruyu mini SSS olarak öngör.
9. Yayınlamadan önce istisnaları, erişilebilirliği (bilgi yalnızca bir görselde olmamalı) ve hassas verileri kontrol et.
10. Kullanıcının vermediği her şeyi (tarih, sorumlu, gerekçe) gönderene not olarak `[TBD]` veya `[VARSAYIM]` ile işaretle.
11. Kullanıcının hedefi devam ediyorsa tam bir SSS için `faq-builder`, değişiklik birden çok kanalda bir mesaj dizisi gerektiriyorsa `communication-plan` öner.

## Çıktı formatı
```markdown
# <Değişiklik> – <tarih> itibarıyla

**Kısaca:** <2-3 satırda ne, kim, ne zaman, aksiyon>

## Neden
<1-3 cümle>

## Ne değişiyor / ne değişmiyor
- Değişen: ...
- Aynı kalan: ...

## Yapmanız gerekenler
1. <aksiyon> – <tarih>'e kadar – <kim: grup>

## Zaman çizelgesi
| Tarih | Kilometre taşı |
|---|---|

## Sorular
- **<olası soru>?** <cevap>
Yardım: <sorumlu/kanal/bağlantı>

<!-- Gönderen için notlar: [TBD] alanlar, varsayımlar -->
```

## Kalite kontrol listesi
- [ ] Başlık ve kısa özet tek başına okuyucunun etkilenip etkilenmediğini ve ne zamana kadar ne yapacağını söylüyor.
- [ ] "Neden" yazılmış veya açıkça `[TBD]` olarak işaretlenmiş.
- [ ] Karışıklık olası yerlerde "ne değişmiyor" belirtilmiş.
- [ ] Aksiyonlar numaralı, tarihli ve bir gruba atanmış.
- [ ] Adı belli bir sorumlu veya yardım kanalı verilmiş.
- [ ] Uydurulmuş tarih, sorumlu veya gerekçe yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Arka plan ve geçmişle başlamak; okuyucu aksiyona gelmeden bırakır. Kısa özetle başla.
- Tüm gruplara tek mesaj; herkes aksiyonun başkası için olduğunu düşünür. Aksiyonları grup bazında etiketle.
- Yardım kanalı vermeden duyurmak; tüm sorular duyuruyu yapan kişiye yağar.

## Örnek
Girdi: 1 Mart'tan itibaren her canlı ortam dağıtımı yeni güvenlik tarama kapısından geçmeli.

Zayıf: "Herkese merhaba, güvenliği iyileştirme çalışmalarımız kapsamında güvenlik ekibi bir süredir seçenekleri değerlendiriyordu ve yeni bir süreç başlatmaya karar verdi..."

Güçlü (bölüm):
# Canlı ortam dağıtımlarında güvenlik tarama kapısı zorunlu – 1 Mart itibarıyla
**Kısaca:** 1 Mart'tan itibaren güvenlik taraması başarılı olmayan pipeline'lar canlıya dağıtım yapamayacak. Ekip liderleri: tarama adımını 22 Şubat'a kadar pipeline'larınıza ekleyin. Yardım: `[#security-gate kanalı – TBD]`.
