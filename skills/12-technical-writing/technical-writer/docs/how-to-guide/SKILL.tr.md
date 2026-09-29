---
description: Diátaxis anlamında hedef odaklı bir nasıl yapılır rehberi yazar; temel bilgiye sahip okuru belirli bir başlangıç noktasından tek bir gerçek sonuca götüren, ön koşulları, numaralı eylem adımları, karar noktaları, doğrulama ve sorun giderme içeren, öğretim ya da arka plan sapması barındırmayan odaklı bir tarif sunar. Kullanıcılar "... nasıl yapılır" diye sorduğunda, bir destek kaydı veya tekrarlayan soru dokümansız bir görevi ortaya çıkardığında ya da mevcut dokümanlar pratik bir görev için eğitim, referans ve açıklamayı karıştırdığında kullanılır.
related: tutorial, user-guide, docs-information-architecture, style-guide-check, runbook
prompt: Entegrasyon geliştiricileri için platformumuzda API imzalama anahtarını kesinti olmadan yenilemeyi anlatan bir nasıl yapılır rehberi yaz.
---

# Nasıl Yapılır Rehberi

## Amaç
Yetkin bir okurun belirli, gerçek bir görevi hızlı ve güvenli biçimde tamamlamasını sağlamak. Rehber yalnızca gereken adımları, koşulları ve kontrolleri verir, başka bir şey vermez; böylece zaman baskısı altında da izlenebilir.

## Ne zaman kullanılır
- Kullanıcılar veya geliştiriciler belirli bir görevi nasıl yapacaklarını tekrar tekrar sorduğunda.
- Bir destek kaydı, olay veya sürüm dokümanı olmayan yeni bir görev ortaya çıkardığında.
- Mevcut bir sayfa kavramları, referans tablolarını ve görev adımlarını karıştırıyor ve görevin kendi sayfası olması gerektiğinde.

## Ne zaman kullanılmaz
- Okur yeniyse ve ilk yönlendirilmiş başarıya ihtiyaç duyuyorsa `tutorial` kullanılır.
- Bir özelliğin veya ürünün tüm görevleri son kullanıcı için belgelenecekse `user-guide` kullanılır.
- Nöbetçi ekip veya canlı ortam desteği için alarm ve eskalasyon içeren bir operasyon prosedürüyse `runbook` kullanılır.

## Girdiler
Zorunlu:
- Okurun ifade edeceği biçimde hedef ("imzalama anahtarını yenile", "faturaları CSV'ye aktar").
- Hedef kitle ve bildikleri ya da erişebildikleri.
- Gerçek adımlar veya bunların güvenilir kaynağı (uzman notları, kayıt çözümü, kod, ekran üzerinden gösterim).

İsteğe bağlı, kaliteyi artırır:
- Ürün sürümü veya edisyonu, ortam farkları (işletim sistemi, bulut, paket seviyesi).
- Bilinen hata durumları, ilgili referans sayfaları, stil rehberi.

Hedef veya adımların kaynağı yoksa iste (her seferinde tek soru). Komut, parametre, menü etiketi veya çıktı asla uydurma; doğrulayamadıklarını `[TBD – doğrula]` olarak işaretle.

## Süreç
1. Hedefi, okurun kelimeleriyle ve fiille başlayan bir görev başlığı olarak yeniden yaz ("API imzalama anahtarını yenileme"); talep birden fazla hedef içeriyorsa ayrı rehberlere böl ve bunu belirt.
2. Başlangıç noktasını ve son durumu tanımla: okurun 1. adımdan önce elinde ne olduğu ve son adımdan sonra neyin doğru olduğu.
3. Ön koşulları listele: yetki veya roller, sürümler, gereken veri, yedekler, bakım pencereleri; yıkıcı veya geri alınamaz her şeyi adımların içine değil, adımlardan önce bir uyarıya koy.
4. Kaynağın söylediğini kendi çıkarımından ayır; çıkarımla yazdığın adımları `[VARSAYIM]` olarak etiketle ve uzman onayı için listele.
5. Numaralı adımlar yaz: her adımda tek eylem, emir kipi, birebir arayüz etiketi, komut veya değer; koşulu eylemden önce yaz ("SSO kullanıyorsanız ... seçin").
6. Gerçek farklılıkları açık karar noktalarıyla veya varyant başına kısa sekmelerle (işletim sistemi, kurulum tipi) ele al; sonucu değiştirmeyen seçenekler için dallanma yapma.
7. Doğrulama ekle: okurun başarıyı nasıl teyit edeceği (beklenen çıktı, durum, ekran görünümü); hem sonda hem riskli her adımdan sonra.
8. En olası 2-4 hata için belirti, neden, çözüm biçiminde sorun giderme ekle; görev canlı ortamın durumunu değiştiriyorsa geri alma adımlarını ekle.
9. Öğretimi ve arka planı en fazla bir cümlelik bağlama indir; yerine açıklama ve referans sayfalarına bağlantı ver.
10. Rehberi hedef kitleye göre kontrol et: hiçbir adım okurun sahip olmadığı bir bilgiyi varsaymamalı, zaten bildiğini de açıklamamalı.
11. Her `[TBD – doğrula]` ve `[VARSAYIM]` öğesini olası doğrulayıcısıyla birlikte "Doğrulanacaklar" altında listele.
12. Kullanıcının hedefi devam ediyorsa yayından önce `style-guide-check`, rehberi yerleştirmek için `docs-information-architecture` ya da okurların yeni başlayan olduğu anlaşılırsa `tutorial` öner.

## Çıktı formatı
````markdown
# <Fiille başlayan görev başlığı>
Geçerli olduğu: <ürün/sürüm/edisyon veya TBD> | Hedef kitle: <rol> | Süre: <~N dk veya TBD>

<Tek cümle: bu rehber neyi sağlar ve ne zaman gerekir.>

## Başlamadan Önce
- <yetki / sürüm / veri / yedek>
> Uyarı: <varsa geri alınamaz veya kesinti yaratan etki>

## Adımlar
1. <birebir etiket, komut veya değerle eylem>
   ```<dil>
   <komut>
   ```
2. <koşul> ise <eylem>. Değilse <eylem>.

## Doğrulama
<beklenen sonuç / çıktı / durum>

## Sorun Giderme
| Belirti | Olası neden | Çözüm |

## Geri Alma (gerekirse)
1. ...

## İlgili Sayfalar
- <referans sayfası> · <açıklama sayfası>

## Doğrulanacaklar
- [TBD – doğrula] <öğe> – <kim teyit edebilir>
````

## Kalite kontrol listesi
- [ ] Rehber tek bir hedefe hizmet ediyor ve başlık bu hedefi fiille adlandırıyor.
- [ ] Ön koşullar ve uyarılar, ihtiyaç duyulan adımlardan önce yer alıyor.
- [ ] Her adımda tek eylem var, koşullar eylemden önce geliyor; etiketler/komutlar birebir ya da `[TBD – doğrula]` olarak işaretli.
- [ ] Okur başarıyı doğrulayabiliyor ve riskli değişikliklerin geri alma yolu var.
- [ ] Bir cümleyi aşan eğitim tarzı anlatım veya kavram açıklaması yok; derinlik bağlantıyla veriliyor.
- [ ] Çıkarımla yazılan adımlar `[VARSAYIM]` olarak etiketli ve doğrulama için listelenmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Farkında olmadan eğitim yazmak: kavramları açıklamak, "önce şunu anlayalım ..." diye başlamak. Okuru görevde tut, derinlik için bağlantı ver.
- Uyarıyı okur 5. adımı çalıştırdıktan sonra 6. adımın içine gömmek. Uyarıları etkilenen ilk adımdan önceye taşı.
- "Eksiksiz olsun" diye her seçeneği anlatmak. Yalnızca sonucu değiştiren varyantları belgele; gerisini referansa bırak.

## Örnek
Girdi: "Nasıl yapılır: API imzalama anahtarını kesintisiz yenileme, entegrasyon geliştiricileri için. Uzman notları: yeni anahtar oluştur, eskisiyle birlikte dağıt, imzalamayı değiştir, 24 saat sonra eskiyi kaldır."

Çıktıdan bir bölüm:
- Zayıf: "Anahtarlar güvenliğin önemli bir parçasıdır. Anahtar yenilemede birkaç yaklaşım vardır ve şunları da düşünmek isteyebilirsiniz ..."
- Güçlü: "## Başlamadan Önce / - Entegrasyon projesinde Admin rolü. > Uyarı: tüm istemciler geçiş yapmadan eski anahtarı silmek imza doğrulamasını bozar. ## Adımlar / 1. **Ayarlar > İmzalama anahtarları** ekranında **Anahtar oluştur**'u seçin `[TBD – etiketi doğrula]`. 2. Yeni açık anahtarı doğrulayıcılarınıza eskisiyle birlikte dağıtın. ... ## Doğrulama / Yeni isteklerin imza başlığında `kid=<yeni anahtar kimliği>` görünür `[TBD – başlık adını doğrula]`."
- Doğrulanacaklar: "24 saatlik çakışma süresi yeterli" `[VARSAYIM]` – platform ekibi.
