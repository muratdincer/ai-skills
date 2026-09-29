---
name: interview-question-set
description: "Paydaş tipine (üst yönetici, süreç sahibi, son kullanıcı, BT/sistem sahibi, uyum) göre uyarlanmış; açılış, bağlam, açık uçlu, derinleştirici ve doğrulayıcı sorular, süre planı ve takip sorularını içeren bir gereksinim görüşmesi rehberi hazırlar. Gereksinim görüşmesi öncesinde veya 'görüşmede kullanıcılara/yöneticilere ne sormalıyım?' sorusu geldiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Görüşme soruları hazırlama"
  related: "interview-notes-analysis, request-clarification-questions, workshop-plan, stakeholder-identification, problem-interview-script"
  prompt: "Depo vardiya amirleriyle bugün stok farklarını nasıl yönettiklerine dair 45 dakikalık bir görüşme hazırla."
---

# Görüşme Soruları Hazırlama

## Amaç
Analiste, belirli bir paydaş tipinden istek listesi yerine gerçek ihtiyaçları, sorunları, kuralları ve istisnaları ortaya çıkaran, odaklı ve süresi planlanmış bir görüşme rehberi vermek.

## Ne zaman kullanılır
- Birebir veya küçük grup gereksinim görüşmeleri öncesinde.
- Aynı girişime farklı paydaş tiplerinin farklı açılardan bakması gerektiğinde.
- Önceki bir görüşme muğlak ya da yalnızca çözüm odaklı cevaplar ürettiğinde.

## Ne zaman kullanılmaz
- Tek bir talebi netleştirmek için birkaç soru yetiyorsa `request-clarification-questions` kullanılır.
- Dış müşterilerle bir ürün problemini doğrulamak isteniyorsa `problem-interview-script` kullanılır.
- Çok sayıda katılımcının birlikte uzlaşması gerekiyorsa `workshop-plan` kullanılır.

## Girdiler
Zorunlu:
- Girişim veya konu.
- Görüşülecek kişinin tipi veya rolü.

İsteğe bağlı, kaliteyi artırır:
- Süre, format (yerinde, uzaktan), zaten bilinenler, önceki görüşme bulguları.
- Test edilecek belirli hipotezler veya çelişkiler.

Görüşülecek kişinin tipi yoksa sor; sorular buna bağlıdır.

## Süreç
1. 2-4 görüşme hedefi belirle: odadan çıkarken kesinlikle bilmen gerekenler.
2. Açıyı paydaş tipine göre uyarla: üst yöneticiler (hedefler, başarı, kısıtlar, öncelikler), süreç sahipleri (akış, kurallar, istisnalar, KPI'lar), son kullanıcılar (görevler, sorunlar, geçici çözümler, araçlar), BT/sistem sahipleri (arayüzler, veri, kısıtlar, teknik borç), uyum (yükümlülükler, kontroller, kanıtlar).
3. Bir açılış (amaç, gizlilik, kayıt izni, süre) ve kişinin rolüyle ilgili bir ısınma bölümü yaz.
4. Gerçek olaylara bağlı "anlatır mısınız" ve "en son ne zaman olduğunu adım adım anlatır mısınız" türünde açık sorular yaz.
5. Her açık soruya 2-3 derinleştirici soru ekle: sıklık, hacim, istisnalar, işler ters gittiğinde ne olduğu, başka kimlerin dahil olduğu, işin doğru yapıldığını nasıl anladıkları.
6. Mevcut hipotezleri yönlendirmeden teyit eden doğrulama soruları ekle ("Bazı kişiler X dedi; bu sizin deneyiminizle ne kadar örtüşüyor?").
7. Bir kapanış ekle: öncelikler ("tek bir şey değişecek olsa..."), başka kimlerle konuşulmalı, paylaşılacak doküman veya örnekler, takip izni.
8. Her bölümü huni (piramit) düzeninde sırala: önce geniş ve açık bağlam soruları, sonra daha dar olay soruları ve derinleştirmeler, en sonda kapalı teyit soruları. Böylece ilk cevaplar senin çerçevene çıpalanmaz.
9. Bölümleri süreye göre planla, mutlaka sorulacak soruları işaretle ve çözüm ima eden her soruyu çıkar. Getirdiğin hipotezleri soru metninde değil, görüşmeci notlarında `[VARSAYIM]` olarak etiketle.
10. Hedef devam ediyorsa görüşme sonrası notlar için `interview-notes-analysis`, çelişen görüşler ortak oturum gerektiriyorsa `workshop-plan` öner.

## Çıktı formatı
```markdown
# Görüşme Rehberi: <girişim> – <paydaş tipi>
Süre: <dk> · Hedefler: 1) ... 2) ...

## Açılış (<dk>)
- Amaç, gizlilik, kayıt izni

## Bağlam (<dk>)
1. ...

## Ana konular (<dk>)
| # | Soru | Derinleştirme | Mutlaka sor |
|---|---|---|---|

## Doğrulama (<dk>)
- ...

## Kapanış (<dk>)
- En önemli öncelik · Başka kim · Doküman/örnek · Takip

## İstenecek belgeler
- ...
```

## Kalite kontrol listesi
- [ ] Sorular açık uçlu ve gerçek, yakın tarihli olaylara dayanıyor.
- [ ] Hiçbir soru bir çözüm önermiyor veya varsaymıyor.
- [ ] Her hedef en az bir "mutlaka sor" sorusuyla karşılanıyor.
- [ ] Bölüm süreleri toplam süreye tampon payıyla sığıyor.
- [ ] Açılışta kayıt izni ve kişisel verilerin ele alınışı konuşuluyor.
- [ ] Açı paydaş tipine açıkça uyuyor.
- [ ] Her bölüm geniş açık sorulardan dar kapalı sorulara doğru huni düzeninde ilerliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Varsayımsal sorular sormak ("... kullanır mıydınız?"). Son seferde ne yaptıklarını ve nedenini sor.
- Süreye göre çok fazla soru. 45 dakika için 8-12 ana soru tipiktir; derinleştirme daha önemlidir.
- Yalnızca yöneticilerle görüşmek. İstisnaları ve geçici çözümleri işi yapan kişiler bilir.

## Örnek
Girdi: "45 dakikalık görüşme, depo vardiya amirleri, stok farkları."

Çıktıdan bir bölüm:
| # | Soru | Derinleştirme | Mutlaka sor |
|---|---|---|---|
| 1 | En son ilgilendiğiniz stok farkını adım adım anlatır mısınız? | Nasıl fark edildi? Kimleri dahil ettiniz? Çözülmesi ne kadar sürdü? | Evet |
| 2 | Hangi farkları kayda geçirmiyorsunuz, neden? | Ne sıklıkta? Ay sonunda ne oluyor? | Evet |
