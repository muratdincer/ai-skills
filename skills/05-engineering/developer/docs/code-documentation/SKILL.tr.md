---
name: code-documentation
description: "Docstring'leri, API yorumlarını ve satır içi yorumları, kodun ne yaptığını tekrar etmek yerine sözleşmeyi, niyeti, kısıtları ve açık olmayan gerekçeleri (neden) anlatacak şekilde yazar veya iyileştirir; yanlış, eskimiş veya koda dönüşmesi gereken yorumları işaretler. Bir geliştirici bir fonksiyonun, sınıfın, modülün veya public API'nin belgelenmesini, mevcut yorumların gözden geçirilmesini ya da kodun devre hazırlanmasını istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: docs
  title: "Kod dokümantasyonu"
  related: "readme-writing, api-reference-docs, clean-code-review, code-explanation, legacy-code-comprehension"
  prompt: "Bu fiyatlandırma modülüne düzgün dokümantasyon ekle. İşe yarar olsun; kodu tekrar eden yorumlar istemiyorum."
---

# Kod Dokümantasyonu

## Amaç
Kodun kendi başına söyleyemediklerini belgeleyerek kodu güvenle kullanılabilir ve değiştirilebilir kılmak: çağıranın güvendiği sözleşme, kısıtlar ve değişmezler, şaşırtıcı kararların arkasındaki gerekçeler. Az sayıda kesin yorum, kodu tekrar eden ve zamanla bozulan çok sayıda yorumdan iyidir.

## Ne zaman kullanılır
- Public bir fonksiyon, sınıf, modül veya kütüphane API'sinin doküman yorumu yoksa ya da zayıfsa.
- Mevcut yorumlar eskimiş, yanıltıcı veya kodu tekrar ediyorsa.
- Gizli iş kuralları, geçici çözümler veya performans hileleri içeren kod devredilmek üzereyse.

## Ne zaman kullanılmaz
- Proje düzeyinde kurulum ve kullanım için `readme-writing` kullanılır.
- HTTP veya mesaj API'leri için uç nokta düzeyinde referans için `api-reference-docs` kullanılır.
- Belgelemeden önce yabancı kodu anlamak için önce `code-explanation` veya `legacy-code-comprehension` kullanılır.

## Girdiler
Zorunlu:
- Belgelenecek kod; dili ve çağıranları anlamaya yetecek bağlamla.

İsteğe bağlı, kaliteyi artırır:
- Ekibin doküman yorumu kuralı (ör. dilin standart docstring veya doc-comment stili) ve dokümanların yorumlardan üretilip üretilmediği.
- Açık olmayan kodun arkasındaki iş kuralları, kayıtlar veya olaylar hakkında arka plan.
- Hedef kitle: dahili bakımcılar veya harici kütüphane kullanıcıları.

Açık olmayan bir kararın gerekçesi koddan çıkarılamıyorsa uydurma: `TODO(sahip): nedenini açıkla ...` yaz veya açık soru olarak listele.

## Süreç
1. Her öğenin görünürlüğünü belirle (public API, paket içi, private). Public API tam sözleşme dokümanı alır; private kod yalnızca nedenin açık olmadığı yerde yorum alır.
2. Yorum yazmadan önce kod olması gerekenleri ara: belirsiz isimler, sihirli sayılar, uzun fonksiyonlar. Yeniden adlandırmayı veya ayırmayı öner ve onun yerini tutacak yorumu yazma.
3. Her public öğe için dilin kuralına uygun, çağırana ne sağladığını alan diliyle anlatan tek satırlık bir özet yaz.
4. Sözleşmeyi belgele: parametreler (anlam, birim, izin verilen aralık, null olabilirlik), dönüş değeri (boş ve bulunamadı durumları dahil), fırlatılan hatalar veya istisnalar ve ne zaman fırlatıldıkları, yan etkiler (I/O, durum, olaylar), ilgiliyse thread güvenliği ve idempotency.
5. Çağıranların veya bakımcıların koruması gereken kısıtları ve değişmezleri ekle (sıralama, hassasiyet, saat dilimi, yuvarlama, performans sınırları).
6. Açık olmayan uygulama tercihleri için tam ilgili satıra kısa bir neden yorumu ekle: iş kuralı, yasal gerekçe, referansıyla birlikte hata için geçici çözüm veya ölçülmüş performans ödünleşimi.
7. Doğru kullanımı açık olmayan public API'ler için kısa bir kullanım örneği ekle; ilke olarak derlenebilir olsun.
8. Kodu tekrar eden, yanlış olan veya artık var olmayan şeylere atıf yapan yorumları kaldır ya da yeniden yaz; kullanımdan kalkan öğeleri yerine geçen öğe ve kaldırma planıyla işaretle.
9. Koddan çıkardığın her gerekçeyi yanıtında `[VARSAYIM]` olarak etiketle ki yazar commit'lemeden önce doğrulayabilsin.
10. Sonucu belgelenmiş kod (veya diff) olarak sun, ardından önerilen kod değişikliklerinin ve açık soruların kısa listesini ver. Kullanıcı devam ederse harici API dokümanı için `api-reference-docs` veya isimlendirme ve yapı bulguları için `clean-code-review` öner.

## Çıktı formatı
```markdown
## Belgelenmiş Kod
<dilin kuralına uygun doküman yorumları ve neden yorumlarıyla kod>

## Yorum Yerine Önerilen Kod Değişiklikleri
- <yeniden adlandırma / sabit çıkarma / fonksiyon çıkarma> — <gerekçe>

## Kaldırılan veya Düzeltilen Yorumlar
- <konum>: <neyin yanlış veya gereksiz olduğu>

## Açık Sorular ve Varsayımlar
- [VARSAYIM] <çıkarılan gerekçe> — <sahip> ile doğrula
```

## Kalite kontrol listesi
- [ ] Her public öğe sözleşmesini belirtiyor: girdiler, çıktı, hatalar ve yan etkiler.
- [ ] Hiçbir yorum yalnızca bir sonraki kod satırının söylediğini tekrar etmiyor.
- [ ] Önemli olduğu her yerde birimler, aralıklar, null olabilirlik ve saat dilimleri açık.
- [ ] Her neden yorumu, bakımcının koddan çıkaramayacağı bir gerekçeyi açıklıyor ve varsa referans veriyor.
- [ ] Çıkarılan gerekçeler `[VARSAYIM]` olarak işaretli; kanıtı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Yorum stili dilin kuralına uyuyor, böylece dokümantasyon araçları onu işleyebiliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kodun ne yaptığını satır satır belgelemek. Bakım yükünü ikiye katlar ve bir sonraki değişiklikte yanlış olur; niyeti ve sözleşmeyi belgele.
- Kötü bir ismi yorumla örtmek. Bunun yerine yeniden adlandır.
- Hangi hataların, nasıl yüzeye çıktığını ve işlemin yeniden denenip denenmediğini söylemeden "hataları yönetir" yazmak.

## Örnek
Girdi: `def price(q, c): return round(q * c.base * (0.9 if q >= 100 else 1), 2)`

Zayıf: `# miktarı taban fiyatla çarpar ve indirim uygular`

Güçlü:
```python
BULK_THRESHOLD = 100   # öneri: sihirli sayının yerine
BULK_DISCOUNT = 0.10

def price(quantity: int, catalog_item: CatalogItem) -> Decimal:
    """Return the net line price in the item's currency, rounded to 2 decimals.

    Orders of BULK_THRESHOLD units or more get BULK_DISCOUNT.
    Quantity is expected to be >= 1; it is not validated here.
    """
```
- Açık soru: `quantity < 1` hata fırlatmalı mı? Mevcut kod sessizce 0 veya negatif fiyat döndürüyor.
- [VARSAYIM] %10 toplu alım kuralı ticari koşullardan geliyor; fiyatlandırma sahibiyle doğrula.
- Öneri: float `round` yerine decimal tip ve açık bir yuvarlama modu kullan.
