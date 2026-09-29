---
name: tone-rewrite
description: "Mevcut bir mesajı; olgularını, taahhütlerini ve taleplerini koruyarak hedef bir tona (daha net, daha yumuşak, daha kararlı, daha resmi, daha kısa, daha tarafsız) göre yeniden yazar ve temel değişiklikleri açıklar. Elinde fazla sert, fazla belirsiz, fazla uzun, fazla gayriresmi veya fazla çekingen görünen bir e-posta, sohbet mesajı, inceleme yorumu veya yanıt taslağı olduğunda ya da \"daha iyi göster\", \"yumuşat\", \"daha kararlı yaz\", \"profesyonelleştir\" istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: communication
  area: written
  title: "Ton düzenleme"
  related: "stakeholder-email, feedback-sbi, bad-news-delivery, document-simplify, technical-translation"
  prompt: "Müşteriye yazdığım bu yanıtı nazik kalarak daha kararlı hale getir: \"Kusura bakmayın, özel raporu bu ay yapamayabiliriz, mümkünse belki gelecek ay?"
---

# Ton Düzenleme

## Amaç
Mesajın söylediğini değiştirmeden nasıl algılandığını değiştirmek. Böylece okuyucu ifadeye tepki vermek yerine içeriğe yanıt verir; gönderen hem ilişkisini hem güvenilirliğini korur.

## Ne zaman kullanılır
- Taslak duygusal yüklüyse (öfkeli, savunmacı, iğneleyici) ve gönderilmeden önce tarafsızlaştırılması gerekiyorsa.
- Mesaj fazla çekingen veya özür dolu olup daha kararlı olmalıysa.
- Üslup değişmeliyse: içten dışa, eşdüzeyden yöneticiye, sohbetten resmi yazıya.

## Ne zaman kullanılmaz
- Henüz taslak yoksa ve amaç belirsizse `stakeholder-email` kullanılır.
- Mesaj birinin davranışına dair geri bildirimse önce yeniden yapılandırmak için `feedback-sbi` kullanılır.
- Metin sadeleştirilecek uzun bir dokümantasyonsa `document-simplify` kullanılır.

## Girdiler
Zorunlu:
- Orijinal metin.
- Hedef ton veya mevcut tondaki sorun.

İsteğe bağlı:
- Alıcı ve ilişki, kanal, dil/kültür, gönderenin kısıtları (neyin söz verilemeyeceği).

Hedef ton verilmediyse 3-4 seçenek sunan tek bir soru sor (ör. "daha kararlı mı, daha yumuşak mı, daha resmi mi, daha kısa mı?"). Orijinalde olmayan olgu, söz, özür veya tarih ekleme.

## Süreç
1. Değişmez içeriği çıkar: olgular, rakamlar, taahhütler, talepler, son tarihler, retler. Bunlar yeniden yazımdan aynen çıkmalı.
2. Ton sorunlarını metinden kanıtla teşhis et: çekinceler ("belki", "sadece", "mümkünse"), suçlama ("siz yapmadınız"), mutlak ifadeler ("her zaman", "asla"), iğneleme, eylemi yapanı gizleyen edilgen yapı, aşırı özür, jargon, uzunluk.
3. Hedefi belirle: üslup (resmi/tarafsız/samimi), doğrudanlık (düşük/yüksek) ve sıcaklık (düşük/yüksek); alıcıya ve kültüre göre ayarla. Türkçede "siz" mi "sen" mi kullanılacağına açıkça karar ver.
4. Gerekirse yeniden yapılandır: önce ana mesaj veya talep, sonra gerekçe, sonra sonraki adım.
5. Cümle cümle yeniden yaz: kararlılık için çekinceleri çıkar; yumuşaklık için "sen/siz" suçlamalarını "ben/biz" ifadeleriyle veya tarafsız tanımlarla değiştir; eylemi yapanı belli eden etken yapı kullan; dolguyu at.
6. En fazla bir samimi kabul veya özür bırak; bunu da yalnızca gönderen tarafında bir şey ters gittiyse yap.
7. Yeniden yazımı değişmez içerik listesiyle karşılaştır; bir olgu, talep veya taahhüt değiştiyse geri getir. Tonun oturması yeni bir söz gerektiriyorsa eklemek yerine işaretle.
8. Hedef belirsizse bir alternatif sürüm sun (ör. kararlı-resmi ve kararlı-sıcak).
9. En önemli 3-5 değişikliği ve nedenini listele ki gönderen kalıbı öğrensin.
10. Kullanıcının hedefi devam ediyorsa mesaj aslında bir ret veya gecikmeyse `bad-news-delivery`, mesajı daha net bir amaç etrafında yeniden kurmak için `stakeholder-email` öner.

## Çıktı formatı
```markdown
**Yeniden yazılmış (<hedef ton>):**
<mesaj>

**Alternatif (<varyant>):** <isteğe bağlı>

**Temel değişiklikler**
- <değişiklik> – <neden>

**Korunanlar:** <korunan olgular/talepler/taahhütler>
**Uyarılar:** <gönderenin karar vermesi gerekenler; ör. tonun ima ettiği ama orijinalde olmayan bir söz>
```

## Kalite kontrol listesi
- [ ] Orijinaldeki tüm olgular, rakamlar, talepler ve taahhütler korundu, hiçbiri eklenmedi.
- [ ] Hedef ton hissediliyor: kararlılık için çekinceler, yumuşaklık için suçlama çıkarıldı; üslup alıcıya uygun.
- [ ] Ana mesaj veya talep ilk iki cümlede.
- [ ] Yeniden yazım gereğinden uzun değil; genellikle orijinale eşit veya daha kısa.
- [ ] Değişiklikler kısaca açıklandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Belirsizlik ekleyerek "yumuşatmak"; talep kaybolur. Ton yumuşak, içerik net olmalı.
- Saldırganlık veya büyük harf ekleyerek "kararlı" yapmak. Kararlılık sesin yüksekliğinden değil, kesinlik ve somutluktan gelir.
- Metni uzatan ve soğutan kurumsal kalıplar eklemek ("Bir önceki e-postamda da belirttiğim üzere", "Her türlü sorunuz için çekinmeden...").

## Örnek
Girdi (nazik ama daha kararlı): "Kusura bakmayın, özel raporu bu ay yapamayabiliriz, mümkünse belki gelecek ay?"

Zayıf yeniden yazım: "Maalesef çeşitli kısıtlar nedeniyle özel raporda olası bir gecikme yaşanabilir. Elimizden geleni yapacağız."

Güçlü yeniden yazım: "Özel raporu bu ay teslim edemiyoruz. `[ay – TBD]` içinde teslim edebiliriz; sizin için uygunsa lütfen `[tarih]`'e kadar teyit edin."
Temel değişiklikler: olguyu net söylemek için "yapamayabiliriz/belki" çıkarıldı; soru yerine somut bir seçenek ve karar talebi kondu. Uyarı: orijinal gelecek ay için söz vermiyordu; göndermeden önce teyit edin.
