---
name: ticket-response
description: "Bir destek kaydına müşteriye yönelik yanıt yazar: sorunu kabul eder, bilineni söyler, sahibi ve zamanı belli net bir yanıt veya sonraki adım verir ve yalnızca gereken bilgiyi ister. Yeni veya güncellenmiş bir kayda yanıt verirken, bekleyen bir kaydı takip ederken, çözüm iletirken, bir talebi reddederken ya da fazla teknik, uzun veya savunmacı bir taslak yanıtı yeniden yazarken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Destek kaydı yanıtı"
  related: "ticket-triage, ticket-escalation-summary, known-error-article, tone-rewrite, bad-news-delivery"
  prompt: "Bu müşteriye yanıt yaz: parola sıfırlamadan sonra giriş yapamıyor, bu hafta ikinci kez oluyor ve çok sinirli."
---

# Destek Kaydı Yanıtı

## Amaç
Müşteriye tek okumada harekete geçebileceği bir yanıt vermek: dinlendiğini hisseder, sırada ne olduğunu ve ne zaman olacağını bilir, kayıt yeni bir soru turu doğurmak yerine ilerler.

## Ne zaman kullanılır
- Yeni bir kayda ilk yanıt veya alındı bildirimi verirken.
- Bekleyen bir kayıtta durum güncellemesi, bilgi talebi veya takip yaparken.
- Çözüm, geçici çözüm veya "hayır" (kapsam dışı, desteklenmiyor, tasarım gereği) iletirken.
- Taslak bir yanıtı göndermeden önce iyileştirirken.

## Ne zaman kullanılmaz
- Kayıt henüz sınıflandırılmamış veya önceliklendirilmemişse `ticket-triage` kullanılır.
- Aynı kesintiden çok sayıda müşteri etkileniyorsa `customer-outage-notice` kullanılır.
- Mesaj başka bir destek seviyesine iç devir notuysa `ticket-escalation-summary` kullanılır.

## Girdiler
Zorunlu:
- Müşterinin mesajı (son mesaj ve ilgili geçmiş).
- Desteğin bildiği veya karar verdiği: yanıt, durum ya da sonraki adım.

İsteğe bağlı, kaliteyi artırır:
- Müşteri adı, dili ve kanalı (e-posta, portal, sohbet), sözleşme seviyesi veya SLA.
- Bilinen hata veya bilgi bankası makalesi, geçici çözüm, politikanın izin verdiği taahhüt tarihleri.
- Şirketin üslup kuralları ve imza formatı.

Desteğin tutumu veya sonraki adım yoksa iste; çözüm, neden veya tarih uydurma. Kayıttaki hassas verileri (parola, kart numarası, T.C. kimlik numarası) tekrar etme; müşteri bir gizli bilgi paylaştıysa değiştirmesini öner.

## Süreç
1. Müşterinin bu yanıttan gerçekte neye ihtiyacı olduğunu belirle: bir cevap, bir çözüm, güvence, bir tarih veya devam izni. Duygu durumunu ve geçmişini (tekrarlanan başvuru, önceki sözler) not et.
2. Yanıt türünü seç: alındı bildirimi, bilgi talebi, güncelleme, çözüm, geçici çözüm, ret, kapanış.
3. Durumunu ve etkisini somut olarak kabul eden tek bir cümleyle başla (genel bir özür değil). Sorunu şirket yarattıysa yaşanan deneyim için özür dile; sorumluluk kabul etme veya neden hakkında tahmin yürütme.
4. Ana mesajı ilk iki üç cümlede ver: yanıt, durum veya karar.
5. Sonraki adımları kısa numaralı bir liste olarak ver: müşterinin ne yapacağı, desteğin ne yapacağı ve bir sonraki güncellemenin ne zaman geleceği. Yalnızca politikanın izin verdiği tarihleri kullan; aksi halde çözüm sözü değil güncelleme zamanı ver.
6. Eksik bilgileri tek seferde iste ve her birinin neden gerektiğini kısaca açıkla.
7. "Hayır" yanıtında gerekçeyi sade bir dille açıkla ve bir alternatif sun (geçici çözüm, özellik talep kanalı, ücretli hizmet).
8. Dili ve derinliği hedef kitleye uyarla: iş kullanıcılarına sade kelimeler, teknik muhataplara tam komutlar veya hata kodları. Müşterinin dilini (Türkçe veya İngilizce) kullan, gerekiyorsa "siz" hitabıyla resmi yaz.
9. Kısa tut (sohbet veya portal için genellikle 150 kelimenin, e-posta için 250 kelimenin altında); iç jargonu, kayıt yönlendirme ayrıntılarını ve diğer ekiplere suç atmayı çıkar.
10. Sonraki beceriyi öner: kaydın bir üst seviyeye gitmesi gerekiyorsa `ticket-escalation-summary`, aynı yanıt tekrar tekrar yazılıyorsa `known-error-article`, hassas durumlar için `tone-rewrite`.

## Çıktı formatı
```markdown
Konu: <kayıt no> – <durumun sade özeti>

Merhaba <ad> Hanım/Bey,

<tek cümlelik somut kabul>
<ana mesaj: yanıt / durum / karar>

Sonraki adımlar:
1. <bizim yapacağımız> – <ne zaman>
2. <sizden gereken, varsa>

<bir sonraki güncellemenin ne zaman geleceği veya kaydın nasıl yeniden açılacağı>

<imza>

---
İç not (gönderilmez): yanıt türü, verilen sözler, açık konular, kullanılan [VARSAYIM]'lar
```

## Kalite kontrol listesi
- [ ] Ana mesaj ilk üç cümlede.
- [ ] Her taahhüdün bir sahibi ve zamanı var; yetki olmadan çözüm tarihi sözü verilmedi.
- [ ] Neden, çözüm veya tarih uydurulmadı; bilinmeyenler dürüstçe ifade edildi ("incelemeye devam ediyoruz").
- [ ] Bilgi talepleri gruplandı ve her birinin gerekçesi var.
- [ ] Hassas veri tekrarlanmadı; iç suçlama ve jargon çıkarıldı.
- [ ] Uzunluk ve dil kanala ve müşteriye uygun.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Gerçek etkiye değinmeden kalıp empati cümleleri ("Yaşanan aksaklıktan dolayı özür dileriz"). Asıl sorunu adıyla an.
- Yanıtı sorun giderme geçmişinin arkasına gömmek. Sonuçla başla.
- Kayıtta zaten olan bilgiyi müşteriden tekrar istemek. Önce geçmişi oku.
- Çözüm doğrulanmadan kaydı "sorun devam ederse bize bildirin" diyerek kapatmak. Doğrula veya bir kontrol zamanı planla.

## Örnek
Girdi: "Müşteri parola sıfırlamadan sonra giriş yapamıyor, bu hafta ikinci kez, sinirli. Neden: sıfırlama e-postaları eski kiracı adresine yönlendiriyor; düzeltme bu gece yayına çıkıyor; geçici çözüm: doğrudan giriş bağlantısı."

Zayıf: "Sayın müşterimiz, yaşanan aksaklıktan dolayı özür dileriz. Ekibimiz konu üzerinde çalışıyor. Lütfen daha sonra tekrar deneyin."
Güçlü: "Merhaba Ayşe Hanım, bir hafta içinde iki kez hesabınıza erişememeniz kabul edilemez, özür dilerim. Sıfırlama e-postası şu anda sizi güncel olmayan bir adrese yönlendiriyor. Düzeltme bu gece yayına çıkana kadar yeni parolanızla <doğrudan giriş bağlantısı> üzerinden giriş yapabilirsiniz. Düzeltmeyi doğruladıktan sonra yarın saat 10:00'a kadar size bilgi vereceğim."
