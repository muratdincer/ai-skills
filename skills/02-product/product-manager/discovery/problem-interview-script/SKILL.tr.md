---
description: The Mom Test yaklaşımıyla, görüş veya satış konuşması yerine geçmiş davranışları, gerçek harcamaları ve mevcut geçici çözümleri soran, yönlendirmeyen bir müşteri problem görüşmesi senaryosu yazar; huni sıralı rehber, derinleştirme soruları, taahhüt sinyalleri ve not formu içerir. Ekip bir problemin var olduğunu geliştirmeden önce doğrulamak istediğinde, keşif görüşmelerine hazırlanırken ya da yönlendirici veya varsayımsal olabilecek soruların gözden geçirilmesi istendiğinde kullanılır.
related: interview-question-set, research-plan, screener-survey, jobs-to-be-done, research-synthesis
prompt: Küçük klinik sahiplerinin randevuya gelmeyen hastalarla gerçekten sorun yaşayıp yaşamadığını anlamak için bir problem görüşmesi senaryosu yaz.
---

# Problem Görüşmesi Senaryosu

## Amaç
Görüşmecilere; bir problemin belirli bir müşteri için gerçek, sık ve maliyetli olup olmadığını iltifatlar, varsayımsal sorular veya nezaketen onaylar yerine geçmiş davranışlara dair olgularla ortaya çıkaran bir senaryo vermek.

## Ne zaman kullanılır
- Bir çözüme bağlanmadan önce hedef problemin var olup olmadığını ve önemini sınamak için.
- Ekip sürekli "harika fikir" duyuyor ama benimsenme görmüyor ve görüşmelerin yanlı olduğundan şüpheleniyorsa.
- Yeni bir segment veya pazar için keşif görüşmeleri turu hazırlanırken.

## Ne zaman kullanılmaz
- Amaç bir prototipin kullanılabilirliğini test etmekse `usability-test-script` kullanılır.
- İç paydaşlardan gereksinim toplanacaksa `requirements-interview` veya `interview-question-set` kullanılır.
- Tam bir çalışmanın (örneklem, katılımcı bulma, takvim) planlanması gerekiyorsa `research-plan`, katılımcı seçimi için `screener-survey` kullanılır.

## Girdiler
Zorunlu:
- Keşfedilecek problem hipotezi ve hedef müşteri segmenti.

İsteğe bağlı, kaliteyi artırır:
- Tetikleyiciler, geçici çözümler ve harcamalar hakkındaki mevcut varsayımlar.
- Görüşme süresi ve biçimi (uzaktan/yüz yüze), planlanan görüşme sayısı.
- Görüşmelerin destekleyeceği karar.

Problem veya segment yoksa sor. Kullanıcıya kayıt için rıza almayı ve notları anonimleştirmeyi hatırlat.

## Süreç
1. Problem hipotezini, çözüm hakkında değil davranış hakkında soru olarak ifade edilen 2-4 öğrenme hedefine dönüştür ("Klinik sahipleri bugün gelmeyen bir hastayı nasıl ele alıyor?").
2. Her hedefin sınadığı en riskli varsayımları ve bunları neyin doğrulayacağını veya çürüteceğini listele; kullanıcının belirtmediği varsayımları `[VARSAYIM]` olarak işaretle.
3. Rehberi huni şeklinde sırala: bağlam ve rol, sonra problemin son somut yaşanışı, sonra etkisi ve sıklığı, sonra mevcut geçici çözümler ve harcamalar, sonra diğer problemlere göre önceliği; genelden özele ilerle.
4. Soruları belirli geçmiş olaylar üzerine kur ("En son ... olduğu zamanı anlatır mısınız?"); asla varsayımsal ("Kullanır mıydınız?") veya yönlendirici ("... sinir bozucu değil mi?") sorma.
5. Her ana soruya derinleştirme soruları ekle: "Sonra ne yaptınız?", "Bu size neye mal oldu?", "Neden zordu?", "Başka ne denediniz?", "Başka kim işin içindeydi?".
6. Görüşmenin ilk %80'inde çözümden bahsetme; bir sunum gerekiyorsa sona koy ve görüş yerine somut bir taahhüt (zaman, tanıştırma, pilot, ön ödeme) iste.
7. Görüşmeci için uyarı işaretleri listesi ekle: iltifatlar, genel iddialar ("Her zaman ..."), gelecek vaatleri, nedeni söylenmeyen özellik talepleri.
8. Açılışı (amaç, satış olmadığı, kayıt rızası, anonimleştirme) ve kapanışı (başka kiminle konuşmalıyız, tekrar iletişim izni) yaz.
9. Olguları, alıntıları, duyguları, geçici çözümleri, harcamaları ve taahhütleri ayıran bir not formu ile görüşme sonrası problem sinyali puanlaması ver.
10. Rehberi belirtilen süreye sığdır; süre yetmezse çıkarılabilecek isteğe bağlı soruları işaretle.
11. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: doğru katılımcıları bulmak için `screener-survey`, görüşmelerden sonra `research-synthesis` / `jobs-to-be-done`.

## Çıktı formatı
```markdown
# Problem Görüşmesi Senaryosu: <segment> – <problem alanı>
Süre: <dk> · Biçim: <uzaktan/yüz yüze> · Planlanan görüşme: <n | [TBD]>

## Öğrenme Hedefleri
1. <davranış sorusu> – şu durumda doğrulanır ... / şu durumda çürür ...

## Açılış (2 dk)
<amaç, satış olmadığı, kayıt rızası, anonim notlar>

## Rehber
| Dk | Bölüm | Ana soru | Derinleştirme |
|---|---|---|---|
| 3-8 | Bağlam | ... | ... |
| 8-20 | Son yaşanış | "En son ... olduğu zamanı anlatır mısınız?" | ... |
| ... | Geçici çözümler ve harcamalar | ... | ... |
| ... | Öncelik | ... | ... |
| ... | (İsteğe bağlı) Taahhüt | ... | ... |

## Kapanış
- Başka kiminle konuşmalıyız? · Tekrar iletişime geçebilir miyiz?

## Görüşmeci İçin Uyarı İşaretleri
- ...

## Not Formu
| Olgular | Alıntılar | Geçici çözümler | Harcama (zaman/para) | Taahhütler | Sinyal (güçlü/zayıf/yok) |
|---|---|---|---|---|---|
```

## Kalite kontrol listesi
- [ ] Hiçbir soru varsayımsal, yönlendirici değil ve fikir hakkında görüş istemiyor.
- [ ] Her ana soru belirli bir geçmiş olaya veya mevcut davranışa dayanıyor.
- [ ] Çözümden isteğe bağlı taahhüt bölümünden önce bahsedilmiyor.
- [ ] Her öğrenme hedefi için doğrulayan ve çürüten kanıt tanımlı.
- [ ] Rehber belirtilen süreye sığıyor, isteğe bağlı sorular işaretli.
- [ ] Rıza ve anonimleştirme ele alındı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "X için para öder miydiniz?" diye sormak. İnsanlar kendi davranışlarını tahmin etmekte kötüdür; son geçici çözüme ne ödediklerini sor.
- Erken sunum yapıp iltifat toplamak. Çözümü geride tut; harcamaları, geçici çözümleri ve duyguyu dinle.
- "Başka fikriniz var mı?" diye bitirmek. Bir tanıştırma veya taahhüt isteğiyle kapat; problemin ne kadar önemli olduğunu bu sınar.

## Örnek
Girdi: "Küçük klinik sahipleri randevuya gelmeyen hastalarla sorun yaşıyor mu, anlamak istiyoruz."

Zayıf: "Otomatik hatırlatma uygulaması gelmeyen hasta sayısını azaltmanıza yardımcı olur muydu?"

Güçlü (bölüm):
- "Bir hastanın en son gelmediği günü anlatır mısınız? Sonra ne oldu?"
- Derinleştirme: "O boş saati ne yaptınız? Size neye mal oldu?"
- "Bunu azaltmak için şimdiye kadar neler denediniz? Neyi sevdiniz, neyi sevmediniz?"
- Taahhüt (sonda): "Birkaç klinikle 4 haftalık bir pilot yürütüyoruz. Katılmak ister misiniz?"
