---
description: Kullanıcıya dönük hata, doğrulama ve uyarı mesajlarını ne olduğunu, yardımcı olacaksa nedenini ve şimdi ne yapılacağını söyleyecek şekilde; suçlama, jargon veya iç detay sızdırmadan, doğru konum, önem derecesi ve erişilebilirlik davranışıyla yazar. Hata durumları için metin gerektiğinde, mevcut mesajlar belirsiz ("Bir şeyler ters gitti") veya teknik olduğunda ya da bir hata kataloğu kullanıcıya dönük metne çevrilecekse kullanılır.
related: microcopy, voice-and-tone-guide, error-scenario-catalog, error-handling-review, design-handoff
prompt: Bu beş ödeme hata mesajını kullanıcı ne olduğunu ve ne yapacağını anlayacak şekilde yeniden yaz; şu an sadece API hata kodlarını gösteriyorlar.
---

# Hata Mesajı Yazma

## Amaç
Kullanıcıya ne olduğunu, sorunun kendi eyleminden mi sistemden mi kaynaklandığını ve somut sonraki adımı ürünün sesiyle anlatarak bir hatadan hızlı ve güvenle toparlanmasını sağlamak.

## Ne zaman kullanılır
- Bir ekran, form veya akışa hata, doğrulama, uyarı veya başarısızlık metni gerektiğinde.
- Mevcut mesajlar genel, teknik, suçlayıcı olduğunda ya da hata kodlarını ve yığın ayrıntılarını gösterdiğinde.
- Teknik hata durumlarından oluşan bir liste (API'den veya hata kataloğundan) kullanıcıya dönük mesajlara eşlenecekse.

## Ne zaman kullanılmaz
- Metin bir hatayla ilgili değilse (etiketler, boş durumlar, onaylar) `microcopy` kullanılır.
- Önce hangi hataların oluşabileceği çıkarılacaksa `error-scenario-catalog` kullanılır.
- Kodun hataları nasıl ele aldığı inceleniyorsa `error-handling-review` kullanılır.

## Girdiler
Zorunlu:
- Hata durumları: mevcut mesajlar, hata kodları veya neyin ne zaman başarısız olduğunun tarifi.

İsteğe bağlı, kaliteyi artırır:
- Sistemin o anda bildikleri (hangi alan, yeniden deneme mümkün mü, veri kaydedildi mi kayboldu mu).
- Ses ve ton rehberi, terim sözlüğü, uzunluk sınırları, diller.
- Destek kanalı ve referans numarası formatı.

Hata durumları yoksa iste. Bir durumun nedeni veya toparlanma yolu bilinmiyorsa tahmin etme, `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Her durum için neden sınıfını belirle: kullanıcı girdisi, kullanıcı yetkisi veya durumu, sistem/servis hatası, bağlantı ya da iş kuralı. Sınıf, bir sonraki adımı kimin atacağını belirler.
2. Kullanıcının ne yapabileceğini belirle: girdiyi düzeltmek, yeniden denemek, beklemek, ayar değiştirmek, birine başvurmak veya hiçbir şey. Verinin kaydedildiğini, kaybolduğunu ya da kısmen işlendiğini teyit et; garanti olmayan bir güvenceyi asla ima etme.
3. Önem derecesini ve konumu seç: alan içi doğrulama, form düzeyinde özet, banner, toast, pencere veya tam sayfa. Engelleyici pencereyi yalnızca kullanıcının karar vermesi gerekiyorsa kullan.
4. Mesajı yaz: ne olduğunu sade bir dille, nedeni yalnızca kullanıcının harekete geçmesine yardım ediyorsa, sonraki adımı bir talimat veya eylem butonu olarak. Nesneyi somut tut ("girdi" değil "kart numarası").
5. Suçlamayı, jargonu ve iç detayları çıkar: ana metinde "geçersiz", "yasadışı", "kritik hata", HTTP kodları veya exception adları olmasın. Destek ihtiyacı olabilecekse referans numarasını ikincil metne koy.
6. Tonu riske göre ayarla: ciddi hatalarda sakin ve nötr; hata mesajlarında mizah ve ünlem yok; yalnızca kusur sistemdeyse ve yalnızca bir kez özür dile.
7. Doğrulamada kullanıcının karşılaması gereken kuralı belirt, doğru anda doğrula (her tuş vuruşunda değil, odaktan çıkınca veya gönderimde), girilen değeri koru ve birden fazla hata varsa alanlara bağlantı veren bir özet listele.
8. Erişilebilirliği WCAG 2.2'ye göre kontrol et: hatalar metinle belirtiliyor (yalnızca renkle değil), alanla ilişkilendiriliyor, yardımcı teknolojiye duyuruluyor ve gönderimde odak özete veya ilk hataya taşınıyor.
9. Güvenlik ve gizliliği kontrol et: bir hesabın var olup olmadığını, iç sistem adlarını veya başkalarının kişisel verisini açığa çıkarma; kimlik doğrulama hatalarındaki mesajları bilinçli olarak genel tut.
10. Uzunluk sınırlarını ve yerelleştirmeyi doğrula (parça birleştirme yok, dinamik değerler için yer tutucular ve çoğul/ek uyumu desteği) ve neden veya toparlanmaya dair her varsayımı `[VARSAYIM]` olarak etiketle.
11. Hedef devam ediyorsa karşılanmamış hataları bulmak için `error-scenario-catalog`, çevredeki arayüz metinleri için `microcopy` veya mesajları durumlara bağlamak için `design-handoff` öner.

## Çıktı formatı
```markdown
# Hata Mesajları: <özellik / akış>

| No / kod | Neden sınıfı | Konum | Mesaj (başlık + gövde) | Eylem | Veri durumu | Not |
|---|---|---|---|---|---|---|
| ... | kullanıcı girdisi | alan içi | ... | ... | korundu | ... |

## Uygulanan Kurallar
- Doğrulama zamanı: ...  - Odak ve duyuru: ...  - Referans numarası: ...

## Önce / Sonra
| Mevcut | Önerilen | Neden |

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
- [BİLİNMİYOR] <kod> için toparlanma yolu — sorumlu: ...
```

## Kalite kontrol listesi
- [ ] Her mesaj ne olduğunu söylüyor ve somut bir sonraki adım veriyor ya da adım gerekmediğini belirtiyor.
- [ ] Ana metinde suçlama, jargon, iç kod veya exception adı yok.
- [ ] Kaydedilen veya kaybolan veriye dair ifadeler girdiyle destekleniyor ya da `[BİLİNMİYOR]` olarak işaretli.
- [ ] Doğrulama mesajları kuralı belirtiyor ve kullanıcının girdisini koruyor.
- [ ] Hatalar metinle belirtiliyor, alanla ilişkili ve duyuruluyor; yalnızca renkle gösterilmiyor.
- [ ] Kimlik doğrulama ve yetki mesajları hesap veya sistem ayrıntısı sızdırmıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Bir şeyler ters gitti." Ne neden ne eylem verir; en azından yeniden denenip denenmeyeceğini ve işin kaydedilip kaydedilmediğini söyle.
- Her teknik koda bir mesaj yazmak. Kullanıcının her toparlanma yolu için bir mesaja ihtiyacı vardır; aynı eyleme çıkan kodları birleştir.
- Hata anında formu temizlemek. Girdiyi koru ve tam olarak hangi alan olduğunu göster.

## Örnek
Girdi: "Ödeme `CARD_DECLINED_51` (yetersiz bakiye) ile başarısız oluyor. Mevcut mesaj: 'Hata 51: İşlem başarısız.'"

Zayıf: "Hata 51: İşlem başarısız. Lütfen tekrar deneyin."

Güçlü: Başlık "Ödeme gerçekleşmedi" · Gövde "Bankanız kartı onaylamadı. Kartınızdan ücret alınmadı. Başka bir kart deneyin veya bankanızla görüşün." · Eylem [Başka kart kullan] · Konum: form düzeyinde banner, odak banner'a taşınır.
