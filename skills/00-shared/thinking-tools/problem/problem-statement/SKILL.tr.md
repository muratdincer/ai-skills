---
name: problem-statement
description: "Bir problemi; kimin etkilendiğini, ne olduğunu, ne zaman ve nerede olduğunu nicel etki ve kanıtla, sınırları ve başarı sinyalleriyle birlikte çözüm içermeyen kesin bir ifadeyle tanımlar. Her girişim, inceleme, iyileştirme veya tasarım çalışmasının başında, ekip doğrudan çözüme atladığında, paydaşlar aynı sorunu farklı anlattığında veya bir problemin tanımlanması ya da yeniden çerçevelenmesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: thinking-tools
  area: problem
  title: "Problem tanımı yazma"
  related: "five-whys, fishbone-analysis, assumption-mapping, hypothesis-statement, request-intake-document"
  prompt: "Problem tanımı yaz: müşteriler aylık faturanın yanlış olduğundan sürekli şikâyet ediyor ve destek ekibi her ay başında aşırı yükleniyor."
---

# Problem Tanımı Yazma

## Amaç
Çözüm seçeneklerini açık tutan ve ekibin daha sonraki bir değişikliğin problemi gerçekten çözüp çözmediğini ölçmesini sağlayan, kanıta dayalı ortak bir problem tanımı oluşturmak.

## Ne zaman kullanılır
- Bir girişim, proje, deney veya kök neden analizi başlarken.
- Paydaşlar problem üzerinde anlaşmadan çözüm önerdiğinde.
- Bir şikâyet, metrik düşüşü veya olay örüntüsü üzerinde çalışılabilir bir probleme dönüştürülecekse.
- Bir problem üzerinde bir süredir ilerleme olmadan çalışılıyorsa ve yeniden çerçevelenmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Bilinen bir problemin nedeni aranıyorsa bu skill'den sonra `five-whys` veya `fishbone-analysis` kullanılır.
- Sınıflandırma için resmî bir iş talebi kaydedilecekse `request-intake-document` kullanılır.
- Test edilecek bir ürün hipotezi gerekiyorsa `hypothesis-statement` kullanılır.

## Girdiler
Zorunlu:
- Durumun, şikâyetin veya belirtinin tarifi.

İsteğe bağlı, kaliteyi artırır:
- Veri: metrikler, kayıt sayıları, olay kayıtları, kullanıcı geri bildirimleri (anonimleştirilmiş).
- Etkilenen kullanıcılar, süreçler, sistemler.
- Daha önceki çözüm girişimleri ve neden başarısız oldukları.

Durum tarifi yoksa iste. Eksik veriler, onları dolduracak kanıtla birlikte `[BİLİNMİYOR]` olarak işaretlenir.

## Süreç
1. Ham ifadeleri topla; gözlemleri (görülen, ölçülen) yorumlardan, nedenlerden ve önerilen çözümlerden ayır; sonrakileri kenara park et.
2. Problemi raporlayanı değil yaşayanı belirle (kullanıcı segmenti, rol, ekip).
3. Ne olduğunu gözlemlenebilir davranış veya sonuçlarla anlat; çözümü gizleyen "X eksikliği" kalıbından kaçın.
4. 5N2K ve Olan/Olmayan (Is/Is-Not) ile sınırla: nerede ve ne zaman oluyor, nerede ve ne zaman olmuyor; bu sınır sonrasında çoğu zaman nedenlere işaret eder.
5. Etkiyi nicelleştir: sıklık, hacim, maliyet, süre, risk, müşteri veya çalışan etkisi. Yalnızca verilen veriyi kullan; yoksa `[BİLİNMİYOR]` yaz ve gereken ölçüyü belirt.
6. Açığı adlandır: mevcut durum ile beklenen durum veya standart.
7. İfadeyi bir-iki cümleyle yaz: "<Kim>, <bağlam> olduğunda <ne> yaşıyor ve bu <etki> doğuruyor; oysa <beklenen>." Ardından çözümü adlandırmadan çözüm alanını açan bir "<Kim> için <beklenen duruma> nasıl ulaşabiliriz?" (How might we) yeniden çerçevelemesi ekle.
8. Test et: çözüm içeriyor mu? İki okuyucu farklı problemler hayal edebilir mi? Üzerinde çalışılamayacak kadar geniş mi, nedeni önceden varsayacak kadar dar mı? Düzelt.
9. Başarı sinyallerini tanımla: problemin çözüldüğünü gösterecek gözlemlenebilir metrik değişimi.
10. Doğrulanacak varsayımları ve kanıt boşluklarını listele.
11. Kullanıcının hedefi devam ediyorsa nedenleri bulmak için `five-whys` veya `fishbone-analysis`, önce neyin doğrulanacağını önceliklendirmek için `assumption-mapping` öner.

## Çıktı formatı
```markdown
# Problem Tanımı: <kısa başlık>

**İfade:** <Kim>, <bağlam> olduğunda <ne> yaşıyor ve bu <etki> doğuruyor; oysa <beklenen durum>.

**Nasıl yapabiliriz:** <Kim> için <beklenen duruma> nasıl ulaşabiliriz?

| Boyut | Olan | Olmayan |
|---|---|---|
| Kim | ... | ... |
| Ne | ... | ... |
| Nerede | ... | ... |
| Ne zaman | ... | ... |
| Boyut/Yaygınlık | ... | ... |

## Kanıt ve Etki
- <veri noktası + kaynak> / [BİLİNMİYOR] – gereken: <ölçü>

## Kapsam Dışı / Park Edilen Çözümler
- <dile getirilen, sonraya bırakılan fikirler>

## Başarı Sinyalleri
- <metrik X'ten Y'ye değişir> (yoksa başlangıç değeri [BİLİNMİYOR])

## Doğrulanacak Varsayımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] İfade herhangi bir çözüm veya teknoloji seçimi içermiyor.
- [ ] Etkilenen taraf somut.
- [ ] Etki nicelleştirilmiş ya da gereken ölçüyle birlikte açıkça `[BİLİNMİYOR]` olarak işaretlenmiş.
- [ ] Bilgi olan yerlerde Olan/Olmayan sınırları dolu.
- [ ] Başarı sinyalleri gözlemlenebilir ve etkiye bağlı.
- [ ] Önerilen çözümler atılmamış, park edilmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Dashboard'umuz yok" bir problem değil eksik bir çözümdür. İnsanların bugün neyi yapamadığını veya neye karar veremediğini sor.
- Çok geniş çerçevelemek ("müşteri deneyimi kötü"). Ekip ilk ölçümü adlandırabilene kadar daralt.
- Doğrulanmadan bir nedeni ifadeye gömmek ("çünkü batch job yavaş").

## Örnek
Girdi: "Müşteriler aylık faturanın yanlış olduğundan şikâyet ediyor; destek ekibi her ay başında aşırı yükleniyor."

Çıktıdan bir bölüm:
- İfade: Dönem ortasında paket değiştiren kurumsal müşteriler, her ayın ilk haftasında beklentilerinden farklı tutarlarda fatura alıyor ve bu faturalama kayıtlarında ani artışa yol açıyor; oysa faturalar kendini açıklayan ve doğru olmalı.
- Olmayan: paket değişikliği yapmayan müşteriler `[VARSAYIM — kayıt örneğiyle doğrula]`.
- Kanıt: ay başı haftası başına faturalama kaydı sayısı `[BİLİNMİYOR]` – gereken: son 3 ayın kategori bazında kayıt sayısı.
