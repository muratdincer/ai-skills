---
description: Diátaxis anlamında öğrenme odaklı bir eğitim (tutorial) yazar; yeni başlayan birinin somut bir şey inşa ettiği, tanımlı bir öğrenme çıktısı, ön koşulları, küçük ve doğrulanabilir adımları, her adımdan sonra görünür sonuçları olan ve sapma içermeyen tek bir yönlendirilmiş yol sunar. Yeni kullanıcıları veya geliştiricileri bir ürüne, API'ye, SDK'ya ya da platforma alıştırırken, bir "başlarken" veya ilk proje dersi gerektiğinde ya da mevcut başlangıç içeriği referans ve nasıl yapılır karışımı olduğunda kullanılır.
related: how-to-guide, user-guide, docs-information-architecture, technical-onboarding, readme-writing
prompt: Ödeme API'miz için, bir geliştiricinin yaklaşık 30 dakikada test ödemesi oluşturup webhook'u işlediği bir başlangıç eğitimi yaz.
---

# Eğitim (Tutorial) Yazma

## Amaç
Yeni başlayan birine somut tek bir proje üzerinden rehberlik ederek ürünle güvenli ve güvenilir bir ilk başarı yaşatmak. Böylece nasıl yapılır rehberlerine veya referansa ihtiyaç duymadan önce özgüven ve zihinsel model kazanır.

## Ne zaman kullanılır
- Yeni kullanıcıların veya geliştiricilerin ilk uygulamalı deneyime ihtiyacı olduğunda.
- "Başlarken" yolu eksikse ya da seçenekler ve teoriyle aşırı yüklenmişse.
- Yeni bir ürün, API veya platform yeteneği için alıştırma dersi gerektiğinde.

## Ne zaman kullanılmaz
- Okuyucular temelleri biliyor ve belirli bir hedefe ulaşmak istiyorsa `how-to-guide` kullanılır.
- Bir özelliğin tüm görevleri son kullanıcılar için belgelenecekse `user-guide` kullanılır.
- Kavramlar veya mimari derinlemesine açıklanacaksa bu açıklama içeriğidir; `docs-information-architecture` bölümüne bakılır.

## Girdiler
Zorunlu:
- Ürün veya teknoloji ve öğrenenin inşa edeceği ya da yapacağı somut şey.
- Öğrenen profili (rol, varsayılan ön bilgi).

İsteğe bağlı, kaliteyi artırır:
- Ortam ayrıntıları (sandbox, örnek veri, sabitlenecek sürümler), örnek kod, bilinen kurulum tuzakları.
- Hedef süre, stil rehberi.

Nihai sonuç veya öğrenen profili yoksa iste. Komut, API uç noktası, parametre veya çıktı uydurma; doğrulayamadıklarını `[TBD – doğrula]` olarak işaretle.

## Süreç
1. Tek bir öğrenme çıktısı ("Sonunda ... elde etmiş olacaksınız") ve gerçekçi bir süre tanımla; buna hizmet etmeyen her şeyi çıkar.
2. Anlamlı ama asgari bir proje seç; öğrenen oyuncak bir parça değil, çalışan bir sonuç görmeli.
3. Ön koşulları kesin olarak listele: hesaplar, araçlar, sürümler, ön bilgi; erişim eksikliğinden yol tıkanmasın diye sandbox veya örnek veri sun.
4. Yolu, her biri görünür ve kontrol edilebilir bir sonuçla biten ("Şimdi ... görmelisiniz") 4-8 bölüme ayır.
5. Adımları birebir komutlar, kod ve girdilerle doğrudan talimatlar olarak yaz; öğrenen hiçbir zaman seçenekler arasında seçim yapmak zorunda kalmamalı.
6. Her önemli adımdan sonra beklenen çıktıyı göster ki öğrenen doğru yolda olduğunu teyit edebilsin; öğrenenlerin sık takıldığı yerlere olası bir hata ve çözümünü ekle.
7. Açıklamayı asgari tut: en fazla bir cümlelik "neden", derinlik için açıklama sayfalarına bağlantı.
8. Yolu zihnen baştan sona test et (veya kullanıcıdan çalıştırmasını iste): her adım yalnızca önceki adımlara dayanmalı, sürümler sabitlenmiş olmalı.
9. Öğrenilenlerin kısa bir özeti ve nasıl yapılır rehberlerine ve referansa bağlanan 2-3 sonraki adımla bitir.
10. Doğrulanmamış tüm komutları, çıktıları ve arayüz etiketlerini `[TBD – doğrula]` olarak işaretle ve teknik gözden geçirme için listele.
11. Kullanıcının hedefi devam ediyorsa sonraki görevler için `how-to-guide` ya da eğitimi doküman setine yerleştirmek için `docs-information-architecture` öner.

## Çıktı formatı
````markdown
# Eğitim: <ne inşa edeceksiniz>
Süre: <~N dk> | Seviye: <başlangıç/...> | Test edilen sürümler: <sürümler veya TBD>

Bu eğitimde <öğrenme çıktısı>.

## Başlamadan Önce
- <hesap / araç / sürüm>
- <ön bilgi>

## Adım 1: <eylem odaklı başlık>
<tek cümlelik neden>
```<dil>
<birebir komut veya kod>
```
Şunu görmelisiniz:
```
<beklenen çıktı>
```
> `<hata>` görürseniz <çözüm>.

## Adım 2: ...

## Neler Öğrendiniz
- ...

## Sonraki Adımlar
- <nasıl yapılır rehberi bağlantısı>
- <referans bağlantısı>

## Doğrulanacak Maddeler
````

## Kalite kontrol listesi
- [ ] İsteğe bağlı dal veya "şunu da yapabilirsiniz" içermeyen tek bir yol var.
- [ ] Her bölüm görünür ve kontrol edilebilir bir sonuçla bitiyor.
- [ ] Komutlar, kod, çıktılar ve sürümler birebir ya da `[TBD – doğrula]` olarak işaretli.
- [ ] Açıklama asgari düzeyde ve derinlik için dışarı bağlantı veriyor.
- [ ] Ön koşullar ilk adımın ihtiyaç duyduğu her şeyi kapsıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her şeyi bir anda öğretmek: seçenekler, parametreler, alternatifler. Tek bir yol seç; seçimleri nasıl yapılır rehberlerine taşı.
- Yalnızca yazarın makinesinde çalışan adımlar. Sürümleri sabitle, örnek veri sağla, işletim sistemi farklarını belirt.
- Çalışan bir sonuç olmadan bitirmek; öğrenenin özgüvenini yok eder.

## Örnek
Girdi: "Ödeme API eğitimi: test ödemesi oluştur ve webhook'u al, 30 dakika, API'mizde yeni geliştiriciler."

Çıktıdan bir bölüm:
- Zayıf: "Ödemeler birkaç yolla oluşturulabilir (API, SDK, panel). Ayrıca idempotency anahtarlarını ve yeniden denemeleri yapılandırmak isteyebilirsiniz..."
- Güçlü: "## Adım 2: İlk test ödemenizi oluşturun / Aşağıdaki komutu sandbox anahtarınızla çalıştırın. `"status": "pending"` içeren bir yanıt görmelisiniz `[TBD – alan adlarını doğrula]`. Adım 3'te bunu teyit eden webhook'u alacaksınız."
