---
name: research-plan
description: "Araştırmanın desteklediği kararı, araştırma hedeflerini ve sorularını, yöntem seçimini ve gerekçesini, katılımcı kriterlerini ve örneklemi, lojistiği, etik ve onamı, takvimi ve çıktıları içeren bir kullanıcı araştırması planı yazar. Ekip \"kullanıcılarla konuşmak\", bir konsepti doğrulamak, bir davranışı anlamak veya bir tasarımı değerlendirmek istediğinde ve katılımcı toplamadan ya da oturum ayarlamadan önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 10-design
  role: ux-researcher
  area: research
  title: "Araştırma planı"
  related: "screener-survey, usability-test-script, interview-question-set, research-synthesis, hypothesis-statement"
  prompt: "Küçük işletme sahiplerinin fatura uygulamamızı ilk hafta içinde neden bıraktığını anlamak için bir araştırma planı yaz."
---

# Araştırma Planı

## Amaç
Ekibi, araştırmanın hangi karara hizmet ettiği, neyin öğrenilmesi gerektiği ve bunun nasıl yapılacağı konusunda hizalamak. Böylece çalışma ilginç ama kullanılamaz anekdotlar yerine bir kararı değiştiren kanıt üretir.

## Ne zaman kullanılır
- Bir ürün veya tasarım kararı bilinmeyen kullanıcı ihtiyaçlarına, davranışlarına ya da tepkilerine bağlıysa.
- Bir konseptin, prototipin veya canlı ürünün kullanıcılarla değerlendirilmesi gerekiyorsa.
- Paydaşlar araştırma talep ediyor ve kapsam, yöntem ve bütçe üzerinde anlaşılması gerekiyorsa.

## Ne zaman kullanılmaz
- Plan hazırsa ve yalnızca oturum senaryosu gerekiyorsa `usability-test-script` veya `interview-question-set` kullanılır.
- Veri zaten toplandıysa ve analiz gerekiyorsa `research-synthesis` kullanılır.

## Girdiler
Zorunlu:
- İş veya ürün sorusu ve ona bağlı karar.

İsteğe bağlı, kaliteyi artırır:
- Mevcut bilgi: analitik, destek kayıtları, önceki çalışmalar, personalar.
- Hedef kullanıcılar ve segmentler, kısıtlar (bütçe, tarihler, teşvikler, kullanıcılara erişim), ürünün aşaması.

Araştırmanın arkasındaki karar belirsizse önce onu sor; o olmadan plan önceliklendirilemez. Diğer eksikler açık soru olur.

## Süreç
1. Araştırmanın desteklediği kararı, kararı kimin verdiğini ve ne zamana kadar verileceğini yaz; hiçbir karar buna bağlı değilse bunu belirt ve kapsamın daraltılmasını öner.
2. Halihazırda bilinenleri ve dayandıkları kanıtı özetle; test edilecek varsayımları açık bilinmeyenlerden ayır.
3. 2-4 araştırma hedefi ve her birinin altında somut araştırma soruları yaz (katılımcıya sorulacak sorular değil, öğrenmek istediklerimiz).
4. Yöntemi soru türüne göre seç: ihtiyaç ve davranış için keşfedici (görüşme, bağlamsal sorgulama, günlük çalışması); tasarımlar için değerlendirici (moderasyonlu veya moderasyonsuz kullanılabilirlik testi, konsept testi); "kaç kişi" soruları için nicel (anket, analitik, A/B). Seçimi gerekçelendir ve sınırlarını belirt.
5. Katılımcıları tanımla: segmentler, dahil etme ve hariç tutma kriterleri, gerekçesiyle segment başına örneklem büyüklüğü (ör. nitel doygunluk için segment başına 5-8, anketler için daha fazla), erişilebilirlik ve çeşitlilik kapsamı.
6. Katılımcı toplama ve lojistiği planla: kanal, eleme anketi, teşvikler, oturum süresi, uzaktan veya yüz yüze, araç kategorisi, not alanlar ve gözlemciler.
7. Etik ve gizliliği ele al: aydınlatılmış onam, kayıt izni, veri minimizasyonu ve maskeleme, saklama ve imha, KVKK/GDPR dayanağı, hassas gruptaki katılımcılar.
8. Analiz yaklaşımını ve çıktıları tanımla: sentez yöntemi, format (bulgu raporu, öne çıkan video kesitleri, güncellenmiş yolculuk haritası) ve sonuçların karar vericiye nasıl ulaşacağı.
9. Kilometre taşlarıyla takvimi oluştur (plan onayı, katılımcı toplama, saha çalışması, sentez, sunum) ve teyit edilmemiş tarihleri `[TBD]` olarak işaretle.
10. Riskleri (katılımcı bulma zorluğu, yanlılık, paydaş beklentileri) önlemleriyle listele.
11. Çıkarımları `[VARSAYIM]` olarak işaretle, açık soruları listele; katılımcı toplama için `screener-survey`, oturumlar için `usability-test-script` veya `interview-question-set` öner.

## Çıktı formatı
```markdown
# Araştırma Planı: <çalışma adı>
Sorumlu: <araştırmacı> · Paydaşlar: <ad/rol> · Durum: <taslak/onaylı>

## Karar ve Arka Plan
- Karar: <ne, kim, ne zamana kadar>
- Bilinenler: <kanıt>
- Test edilecek varsayımlar: ...

## Hedefler ve Araştırma Soruları
1. Hedef: ...
   - AS1.1 ...

## Yöntem
<yöntem, gerekçe, sınırlar>

## Katılımcılar
| Segment | Kriterler | Hariç tutulanlar | Örneklem | Gerekçe |
|---|---|---|---|---|

## Katılımcı Toplama ve Lojistik
<kanal, teşvik, oturum formatı ve süresi, roller>

## Etik ve Gizlilik
<onam, kayıt, maskeleme, saklama, hukuki dayanak>

## Analiz ve Çıktılar
<sentez yaklaşımı, çıktılar, sunum kitlesi>

## Takvim
| Kilometre taşı | Tarih | Sorumlu |
|---|---|---|

## Riskler ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Plan desteklediği kararı ve son tarihini belirtiyor.
- [ ] Araştırma soruları görüşme sorusu veya yönlendirici ifade değil, öğrenme hedefi.
- [ ] Yöntem soru türüyle uyumlu ve sınırları belirtildi.
- [ ] Katılımcı kriterleri davranışa dayalı ve örneklem büyüklükleri gerekçeli.
- [ ] Onam, kayıt ve kişisel verinin ele alınması kapsandı.
- [ ] Teyit edilmemiş tarihler, bütçeler ve sayılar uydurulmadı, işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Kaç kişi" sorularını nitel görüşmelerle yanıtlamaya çalışmak. Bir anket veya analitikle birlikte kullan.
- Yalnızca demografiye göre katılımcı seçmek. Önemli olan davranışa göre ele (ör. "geçen ay en az 3 fatura kesmiş").
- Karar zaten verildikten sonra araştırma planlamak. Takvimi karar tarihine bağla.

## Örnek
Girdi: "Küçük işletme sahipleri fatura uygulamamızı ilk hafta neden bırakıyor?"

Çıktıdan bir bölüm:
- Karar: Gelecek çeyrekte hangi iki onboarding sorununun çözüleceği; ürün lideri, planlamadan önce `[TBD: tarih]`.
- AS1.1: Kullanıcılar ilk oturumlarında neyi başarmaya çalışıyordu ve onları ne durdurdu?
- Yöntem: Yakın zamanda ayrılan kullanıcılarla 10 uzaktan görüşme ve ilk hafta olaylarının huni analizi; görüşmeler nedenini, huni nerede ve kaç kişi olduğunu gösterir.
- Kriterler: son 30 günde kayıt olmuş, en fazla bir fatura oluşturmuş, 10'dan az çalışanı olan bir işletmenin sahibi.
