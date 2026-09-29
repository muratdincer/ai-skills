---
name: bad-news-delivery
description: "Bir gecikmeyi, iptali, kapsam daralmasını, başarısız teslimatı, reddedilen talebi veya tutulamayan bir taahhüdü; haberi en başta, nedeni suçlamadan, okuyucuya etkisini, yapılanları, seçenekleri ve bir sonraki güncellemeyi belirterek şeffaf biçimde iletir. Bir müşteriye, sponsora, yöneticiye veya ekibe bir şeyin söz verildiği ya da beklendiği gibi olmayacağını yazılı olarak ya da bir görüşme için konuşma notlarıyla söylemek gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: communication
  area: written
  title: "Kötü haber iletme"
  related: "tone-rewrite, escalation-message, stakeholder-email, status-update, customer-outage-notice"
  prompt: "Sponsora, ayın 20'sinde planlanan raporlama sürümünün veri sağlayıcısının API'si değiştiği için üç hafta kayacağını ve bunun yerine ne önerdiğimizi söylememe yardım et."
---

# Kötü Haber İletme

## Amaç
İstenmeyen haberi erken ve açıkça, sahiplenerek, etkisiyle ve bir çıkış yoluyla iletmek. Böylece okuyucu planlarını ayarlayabilir; güven sürprizle veya süslemeyle aşınmak yerine korunur ya da yeniden kurulur.

## Ne zaman kullanılır
- Taahhüt edilmiş bir tarih, kapsam veya sonuç tutturulamayacaksa.
- Bir talep, teklif veya bütçe reddediliyorsa.
- Bir proje, özellik veya hizmet iptal ediliyor ya da önemli ölçüde değişiyorsa.
- Haber yüz yüze verilmeden önce konuşma notları hazırlanıyorsa.

## Ne zaman kullanılmaz
- Süren güncellemeleri olan canlı bir olay veya kesinti için `incident-communication` ya da `customer-outage-notice` kullanılır.
- Sorunu çözmek için üst seviyeden karar gerekiyorsa `escalation-message` kullanılır.
- Haber bir kişinin performansıyla ilgiliyse `feedback-sbi` kullanılır.

## Girdiler
Zorunlu:
- Haberin kendisi (neyin beklendiği gibi olmayacağı).
- Alıcı ve onun bu konudaki çıkarı.

İsteğe bağlı:
- Neden, yeni tarih veya seçenekler, şu an yapılanlar, sunulan telafi, ilişki geçmişi, kanal.

Yeni tarih veya toparlanma planı bilinmiyorsa uydurma: kesin tarihin ne zaman verileceğini söyle. Nedeni yalnızca etkiyi açıklamak için gerekiyorsa sor; bilinmeyen nedenler "inceleniyor" olarak yazılır.

## Süreç
1. Kanalı seç: kilit bir paydaş için önemli haber önce canlı (telefon/toplantı), sonra yazılı verilir; yazılı sürüm yine de tek başına anlaşılır olmalı.
2. Haberi ilk cümlede sade bir dille ver. Isınma paragrafı yok, gömülü haber yok.
3. Gönderenin rolüne uygun sahiplen: ekibin taahhütleri için "biz" de; neden olsalar bile tedarikçileri veya kişileri suçlama; nedenleri olgu olarak yaz.
4. Nedeni bir veya iki cümlede, yalnızca okuyucunun ihtiyaç duyduğu derinlikte açıkla; bilineni hâlâ incelenenden ayır.
5. Etkiyi okuyucunun gözünden yaz: neyi kaybediyor, neyi değiştirmesi gerekiyor, hangi tarihleri kayıyor.
6. Etkiyi sınırlamak için şu an yapılanları ve yapılacakları anlat.
7. Mümkünse seçenekleri ödünleşimleriyle sun (kısmi teslimat, zamanında daraltılmış kapsam, sonradan tam teslimat) ve okuyucudan seçmesini veya onaylamasını iste.
8. Bir sonraki güncellemeyi taahhüt et: tarihi ve içereceği bilgi; kesin tarihi yalnızca kullanıcı verdiyse yaz.
9. Bir taahhüt bozulduysa bir kez, samimi ve somut biçimde özür dile; tekrarlanan veya genel özür yok.
10. Çıkarım olan her nedeni, etkiyi veya tarihi `[VARSAYIM]` ya da `[TBD]` olarak işaretle ve gönderenin teyidi için listele.
11. Kullanıcının hedefi devam ediyorsa belirli bir okuyucuya göre üslubu ayarlamak için `tone-rewrite`, değişikliği düzenli raporlamaya yansıtmak için `status-update` öner.

## Çıktı formatı
```markdown
Konu: <Konu>: <sade bir dille haber>

<İsim>, <tek cümlede haber>.

**Neden:** <1-2 cümlede neden; bilinen ve incelenen ayrımı>
**Sizin için anlamı:** <okuyucunun diliyle etki>
**Yaptıklarımız:** <süren aksiyonlar>
**Seçenekler:**
1. <seçenek> – <ödünleşim>
2. <seçenek> – <ödünleşim>
**Sizden ihtiyacımız:** <tarih>'e kadar <seçim/onay>
**Sonraki güncelleme:** <tarih>, <içerik>

<taahhüt bozulduysa tek ve somut bir özür>

Konuşma notları (canlı iletilecekse): <aynı sırayla 3-5 madde>
Gönderen için notlar: <varsayımlar, [TBD] maddeler>
```

## Kalite kontrol listesi
- [ ] Kötü haber bağlamdan sonra değil, ilk cümlede.
- [ ] Neden, kişileri veya üçüncü tarafları suçlamadan olgusal olarak yazıldı.
- [ ] Etki okuyucunun bakış açısından anlatıldı.
- [ ] En az bir seçenek veya somut bir toparlanma aksiyonu ve bir sonraki güncelleme tarihi var.
- [ ] Uydurulmuş tarih, rakam veya neden yok; bilinmeyenler işaretli.
- [ ] En fazla bir özür var ve somut.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Haberi iltifatların arasına sıkıştırmak; okuyucu ya kaçırır ya da manipüle edildiğini hisseder. Haberle başla.
- Darbeyi yumuşatmak için yeni bir tarih vaat edip onu da kaçırmak. Tarihi ancak inandırıcıysa ver; değilse ne zaman bileceğini taahhüt et.
- "Bir çözümümüz olana kadar bekleyelim" diye haberi geç vermek. Dürüst bir planla gelen erken haber, cilalı bir planla gelen geç haberden iyidir.

## Örnek
Girdi: 20'sindeki raporlama sürümü, veri sağlayıcısının API'si değiştiği için üç hafta kayıyor.

Zayıf: "Merhaba, kısa bir güncelleme. Ekip çok sıkı çalıştı ve harika ilerleme kaydetti. Ancak bazı dış etkenler nedeniyle takvimde ufak bir ayarlama olabilir..."

Güçlü (bölüm):
Konu: Raporlama sürümü: 20'sinden `[yeni tarih]` tarihine kayıyor
"Emre Bey, raporlama sürümü 20'sinde yayına alınamayacak; mevcut tahminimiz üç hafta sonrası.
Neden: veri sağlayıcısı `[tarih]` tarihinde API'sini değiştirdi; entegrasyonumuzun yeniden yazılması gerekiyor.
Seçenekler: 1) sağlayıcı verisini kullanmayan 4 raporu 20'sinde yayına almak; 2) hepsini birlikte üç hafta sonra yayına almak."
