---
description: "Net başlık, ortam ve build, ön koşullar, en az sayıda numaralı adım, beklenen ve gerçekleşen sonuç, tekrarlanma oranı, kanıt, etki ve önerilen önem derecesi içeren, tekrarlanabilir ve önceliklendirmeye hazır bir hata raporu yazar. Bir test uzmanı, geliştirici veya kullanıcı bir hata bulduğunda ve kaydedilmesi gerektiğinde, mevcut rapor belirsiz ya da tekrarlanamıyorsa veya biri gözlemlerini yapıştırıp hata kaydına dönüştürülmesini istediğinde kullanılır."
related: bug-triage, bug-reproduction, log-analysis, test-case-writing, ticket-triage
prompt: "Hata raporu yaz: iOS uygulamasında ödeme adımında teslimat adresi değiştirildikten sonra kargo ücreti hâlâ eski şehre göre hesaplanıyor. Çoğu zaman oluyor, staging'de build 4.12.0."
---

# Hata Raporu Yazma

## Amaç
Geliştiricilere ve önceliklendirme yapanlara, bir hatayı raporlayana geri dönmeden tek okumada tekrarlamak, anlamak ve önceliklendirmek için gereken her şeyi vermek.

## Ne zaman kullanılır
- Test, UAT veya üretim kullanımı sırasında bir hata gözlendi ve kaydedilmeli.
- Mevcut bir kayıt "çalışmıyor" diyor veya "tekrarlanamadı" diye kapatılmış.
- Ham notlar, ekran görüntüleri veya sohbet mesajları yapılandırılmış bir kayda dönüşmeli.

## Ne zaman kullanılmaz
- Nedeni hâlâ kodda araştırıyorsan `bug-reproduction` veya `debugging-hypotheses` kullanılır.
- Çok sayıda mevcut hatayı sıralamak veya atamak gerekiyorsa `bug-triage` kullanılır.
- Doğrulanmış bir hata olmayan kullanıcı destek talebiyse `ticket-triage` kullanılır.

## Girdiler
Zorunlu:
- Ne yapıldığı ve ne olduğu (gözlem), herhangi bir biçimde.

İsteğe bağlı, kaliteyi artırır:
- Ortam, build/versiyon, cihaz/tarayıcı, kullanılan hesap veya rol, oluş zamanı.
- Ekran görüntüleri, kayıtlar, loglar, request ID'ler, correlation ID'ler.
- Beklenen davranışı tanımlayan gereksinim veya kabul kriteri.

Gözlem yoksa iste. Engelleyici boşluklar için (ortam, tam adımlar, beklenen davranış) en fazla üç odaklı soru sor; geri kalan her şey `[BİLİNMİYOR]` olur.

## Süreç
1. Raporlayanın gözlemlediğini, neden hakkındaki yorum veya tahminlerinden ayır; tahminleri adımlara koyma, "Notlar" altına yaz.
2. Başlığı "<bileşen>: <koşul> olduğunda <ne yanlış gidiyor>" biçiminde yaz. Mükerrerleri fark ettirecek kadar spesifik olmalı.
3. Ortamı kaydet: ortam adı, build/versiyon, platform, cihaz/tarayıcı, dil ayarı, feature flag'ler, kullanıcı rolü. Şifre veya token asla yazma.
4. Ön koşulları ve veriyi (maskeli) belirt: hesap durumu, sepet içeriği, konfigürasyon.
5. Adımları, sorunu tekrarlayan en kısa numaralı diziye indir; adım başına bir işlem.
6. Beklenen sonucu kaynağıyla yaz (gereksinim, kriter, önceki davranış ya da yalnızca sağduyuya dayanıyorsa `[VARSAYIM]`).
7. Gerçekleşen sonucu olgusal yaz: tam mesaj, yanlış değer, HTTP durumu, zaman. Tekrarlanma oranını ekle (ör. 5 denemede 4).
8. Kanıtı ekle veya referans ver: hata alanı işaretlenmiş ekran görüntüleri, zaman damgalı log kesiti, request/correlation ID'ler. Kişisel verileri maskele.
9. Etkiyi anlat: kim etkileniyor, ne sıklıkla, geçici çözüm var mı, veri veya para riski.
10. Önem derecesini (teknik etki) öner, ekip süreci aksini söylemiyorsa önceliği önceliklendirmeye bırak; tek satırla gerekçelendir.
11. Kullanıcı sağlayabiliyorsa olası mükerrer veya ilişkili kayıtları kontrol et; kullanıcı devam ederse önceliklendirme için `bug-triage`, tekrarlanma oranı düşükse `bug-reproduction` öner.

## Çıktı formatı
```markdown
**Başlık:** <bileşen>: <koşul> olduğunda <belirti>

| Alan | Değer |
|---|---|
| Ortam / build | <ortam, versiyon> |
| Platform | <OS, cihaz, tarayıcı, dil> |
| Rol / hesap | <rol, maskeli hesap> |
| Tekrarlanma oranı | <n/m> |
| Önem (önerilen) | <Kritik/Majör/Minör/Önemsiz> – <gerekçe> |
| İlgili gereksinim | <ID veya [BİLİNMİYOR]> |

**Ön koşullar:** ...
**Tekrarlama adımları:**
1. ...
**Beklenen sonuç:** ... (kaynak: ...)
**Gerçekleşen sonuç:** ...
**Kanıt:** <ekran görüntüsü / log / request ID>
**Etki ve geçici çözüm:** ...
**Notlar (raporlayanın doğrulanmamış hipotezleri):** ...
```

## Kalite kontrol listesi
- [ ] Başlık tek başına neyin yanlış olduğunu ve hangi koşulda olduğunu söylüyor.
- [ ] Adımlar en kısa hâlinde, numaralı ve belirtilmiş bir ön koşuldan başlıyor.
- [ ] Beklenen ve gerçekleşen sonuç spesifik; beklenen sonuç kaynağını belirtiyor.
- [ ] Ortam, build ve tekrarlanma oranı var ya da `[BİLİNMİYOR]` olarak işaretli.
- [ ] Kanıtta maskelenmemiş kişisel veri, şifre veya token yok.
- [ ] Neden hakkındaki tahminler gözlenen olgulardan ayrılmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Birden fazla sorun için tek kayıt. Ayır; her hatanın kendi yaşam döngüsü olmalı.
- Dikkat çekmek için şişirilmiş önem derecesi. Etkiye bağla, önceliği önceliklendirme belirlesin.
- "Giriş yap ve sayfaya git" ile başlayıp hatayı asıl tetikleyen veri durumunu atlayan adımlar.

## Örnek
Girdi: "iOS uygulaması: ödemede teslimat adresi değişince kargo ücreti eski şehre göre kalıyor. Çoğunlukla oluyor, 4.12.0, staging."

Zayıf: "iOS'ta kargo ücreti yanlış. Acil düzeltin."

Güçlü (bölüm):
- Başlık: Ödeme (iOS): teslimat adresi başka şehre değiştirildiğinde kargo ücreti yeniden hesaplanmıyor
- Tekrarlanma oranı: `[BİLİNMİYOR: n/m]`, raporlayan "çoğu zaman" diyor
- Adımlar: 1. Ankara adresiyle sepete bir ürün ekle. 2. Ödemeyi aç; ücreti not et. 3. Teslimat adresini bir İzmir adresiyle değiştir. 4. Sipariş özetine dön.
- Beklenen: Ücret İzmir için yeniden hesaplanır (kaynak: `[BİLİNMİYOR: fiyat kuralı ID]`). Gerçekleşen: Ücret hâlâ Ankara tutarını gösteriyor; sipariş bu tutarla verilebiliyor.
- Etki: Şehirler arası her adres değişikliğinde olası gelir kaybı veya fazla tahsilat; geçici çözüm: ürünü çıkarıp yeniden eklemek.
