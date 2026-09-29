---
description: "Müşteri diliyle bir hizmet kataloğu kaydı yazar: hizmetin ne olduğu ve ne olmadığı, kimlerin kullanabileceği, talep seçenekleri ve nasıl talep edileceği, onaylar, karşılama adımları, hizmet seviyeleri ve destek saatleri, ücretliyse maliyetler, bağımlılıklar, sorumluluklar ve sahiplik. Yeni bir BT veya iç hizmet devreye alındığında, mevcut bir kayıt eskidiğinde veya belirsizleştiğinde, talep edenler bir şeyi nasıl alacaklarını sürekli sorduğunda ya da hizmet seviyelerinin kullanıcılara duyurulması gerektiğinde kullanılır."
related: "slo-definition, sla-breach-analysis, raci-matrix, user-guide, faq-builder"
prompt: "'Geliştirici VM' hizmetimiz için katalog kaydı yaz: geliştiriciler 8 vCPU/32 GB Linux VM talep ediyor, yönetici onayı gerekiyor, 2 iş gününde teslim ediliyor, uzatılmazsa 90 gün sonra siliniyor."
---

# Hizmet Kataloğu Kaydı

## Amaç
Kullanıcıların ne alabileceklerini, nasıl talep edeceklerini ve ne bekleyeceklerini anlamalarını, hizmet sağlayıcının da hizmeti tutarlı biçimde karşılayıp ölçebilmesini sağlamak. Böylece talepler eksiksiz gelir, beklentiler hizmetin gerçekte sunduğuyla örtüşür.

## Ne zaman kullanılır
- Yeni bir BT, platform veya iç ortak hizmet devreye alındığında.
- Mevcut bir kayıt tekrar tekrar "... nasıl alırım" sorularına veya eksik taleplere yol açtığında.
- Hizmet seviyeleri, destek saatleri veya maliyetler değiştiğinde ve duyurulması gerektiğinde.

## Ne zaman kullanılmaz
- Hizmetin arkasındaki iç SLO hedefleri ve hata bütçeleri tanımlanacaksa `slo-definition` kullanılır.
- Hizmet teslim edildikten sonraki adım adım kullanım talimatları için `user-guide` kullanılır.
- Çok sayıda ekip arasında ayrıntılı sorumluluk dağılımı için `raci-matrix` kullanılır.

## Girdiler
Zorunlu:
- Hizmetin adı ve neyi, kimin için sağladığının tanımı.

İsteğe bağlı, kaliteyi artırır:
- Talep seçenekleri ve opsiyonlar, uygunluk, onay kuralları, karşılama adımları ve teslim süreleri.
- Üzerinde anlaşılmış hizmet seviyeleri, destek saatleri ve kanalları, maliyet veya iç faturalama modeli.
- Sahip, sağlayıcı ekip, bağımlılıklar, güvenlik ve veri işleme kuralları, kurumun katalog şablonu.

Hizmet tanımı yoksa iste. Hizmet seviyelerini, teslim sürelerini veya fiyatları uydurma; `[TBD]` olarak işaretle ve hizmet sahibinin vermesi gereken kararlar olarak listele.

## Süreç
1. Hizmet tanımını talep edenin diliyle yaz: kullanılan teknoloji değil, elde ettikleri sonuç. Kimin için olduğunu ve tek satırlık bir "şu durumda kullanın" ifadesini ekle.
2. Açık kapsam dışılıkları yaz ("bu hizmete dahil olmayanlar") ve sık karıştırılan her durum için doğru hizmete yönlendir.
3. Uygunluğu tanımla: kimler talep edebilir (roller, departmanlar, lokasyonlar), ön koşullar (eğitim, lisans, masraf merkezi).
4. Talep seçeneklerini (örneğin yeni, değişiklik, uzatma, kaldırma) opsiyon ve sınırlarıyla listele; taleplerin eksiksiz gelmesi için her birinde talep edenin vermesi gereken alanları yaz.
5. Talep ve onay akışını anlat: kanal, seçenek başına onaylayanlar, otomatik veya manuel karşılama, tamamlandığında talep edenin ne alacağı.
6. Seçenek başına hizmet seviyelerini yayımla: karşılama süresi, erişilebilirlik, destek saatleri, öncelik başına ilk yanıt ve çözüm hedefleri ve bir olayın nasıl bildirileceği. Yalnızca üzerinde anlaşılmış değerleri kullan; aksi hâlde `[TBD]`.
7. Varsa maliyetleri ve faturalama modelini, yaşam döngüsü kurallarını (yenileme, süre sonu, hizmetten kaldırma, veri saklama ve silme) belirt.
8. Güvenlik ve uyum yükümlülüklerini ekle: hizmette izin verilen veri sınıfı, erişim kontrolleri, kabul edilebilir kullanım, hizmet kişisel veri işliyorsa KVKK/GDPR kapsamında kişisel verilerin ele alınışı.
9. Sahiplik ve bağımlılıkları kaydet: hizmet sahibi, sağlayıcı ekip, eskalasyon irtibatı, altta yatan hizmetler ve tedarikçiler, gözden geçirme tarihi.
10. Gerçek veya olası talep eden sorularından üç ila beş SSS ekle; gerçek kayıtlardan gelmiyorsa `[VARSAYIM]` olarak etiketle.
11. Devret: yayımlanan seviyelerin arkasına ölçülebilir hedefler koymak için `slo-definition`, SSS'yi genişletmek için `faq-builder`, performans verisi oluştuğunda `sla-breach-analysis` öner.

## Çıktı formatı
```markdown
# <Hizmet Adı>
| Alan | Değer |
|---|---|
| Özet | <tek cümlelik sonuç> |
| Kimin için | <kim> |
| Hizmet sahibi / Sağlayıcı | <rol veya ad> / <ekip> |
| Durum | yayında / pilot / kaldırılıyor |
| Gözden geçirme tarihi | <tarih> |

## Ne Alırsınız
...
## Dahil Olmayanlar
- ... → <diğer hizmet> kullanın
## Kimler Talep Edebilir
- Uygunluk: ... Ön koşullar: ...
## Talep Seçenekleri
| Seçenek | Opsiyonlar / sınırlar | Vermeniz gereken bilgi | Onay | Teslim süresi |
|---|---|---|---|---|
## Nasıl Talep Edilir
1. ...
## Hizmet Seviyeleri ve Destek
| Kalem | Hedef |
|---|---|
| Erişilebilirlik | <... veya [TBD]> |
| Destek saatleri / kanal | ... |
| Olay yanıtı / çözümü (öncelik başına) | ... |
## Maliyet ve Yaşam Döngüsü
- Maliyet: ... Yenileme/süre sonu: ... Veri saklama ve silme: ...
## Güvenlik ve Uyum
- ...
## Bağımlılıklar
- ...
## SSS
- S: ... C: ...
## Hizmet Sahibinden Beklenen Kararlar
- [TBD] ...
```

## Kalite kontrol listesi
- [ ] Tanım, uygulama ayrıntılarını değil kullanıcının elde ettiği sonucu sade bir dille anlatıyor.
- [ ] Kapsam dışılıklar açık ve doğru hizmete yönlendiriyor.
- [ ] Her seçenek, talep edenin vermesi gereken bilgileri ve onay yolunu listeliyor.
- [ ] Hizmet seviyeleri, teslim süreleri ve maliyetler üzerinde anlaşılmış değerler veya `[TBD]`; asla uydurulmamış.
- [ ] Yaşam döngüsü, veri saklama ve güvenlik kuralları belirtilmiş.
- [ ] Sahip, eskalasyon irtibatı ve gözden geçirme tarihi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kullanıcının ne aldığı yerine altyapıyı anlatmak ("Ceph'li KVM kümesi"). Sonuçla başla.
- Sağlayıcının karşılayamayacağı iddialı hizmet seviyeleri yayımlamak; bu anında SLA ihlalleri doğurur.
- Süre sonu ve silme kurallarını atlamak; kaynak yığılmasına ve verilerin amacın ötesinde saklanmasına yol açar.
- Kayıtları eskimeye bırakmak; güncel olmayan bir katalog talepleri yeniden e-posta ve sohbete iter.

## Örnek
Girdi: "Geliştirici VM: 8 vCPU/32 GB Linux VM, yönetici onayı, 2 iş günü, uzatılmazsa 90 gün sonra silinir."

Çıktıdan bir bölüm:
- Özet: Geliştirme ve test için 2 iş günü içinde hazır, kişisel bir Linux sanal makinesi.
- Dahil olmayanlar: üretim iş yükleri veya müşteri verisi → "Uygulama Barındırma" hizmetini kullanın.
- Seçenekler: Yeni VM (8 vCPU / 32 GB, daha büyük boyutlar [TBD]) – talep eden proje kodu ve gerekçe verir – onay: bağlı yönetici – teslim: 2 iş günü.
- Yaşam döngüsü: uzatılmazsa teslimden 90 gün sonra silinir; silmeden önce hatırlatma gönderilir [VARSAYIM: 7 gün].
- Güvenlik: geliştirici VM'lerinde kişisel veya üretim verisi bulunmaz [VARSAYIM: veri sınıflandırma politikasıyla teyit et].
