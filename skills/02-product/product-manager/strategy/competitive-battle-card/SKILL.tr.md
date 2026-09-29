---
name: competitive-battle-card
description: "Satış ve ön satış ekipleri için adı belli bir rakibe karşı tek sayfalık rekabet kartı hazırlar; ne zaman kazanıp ne zaman kaybettiğimizi, iki tarafın güçlü ve zayıf yönlerini, keşif ve tuzak sorularını, kanıtlı itiraz yanıtlarını ve kısa savuşturma cümlelerini içerir. Satış ekibi anlaşmalarda bir rakiple karşılaştığında, rekabetçi bir sunum veya RFP öncesinde, kazanma/kaybetme notları sahaya yönelik rehbere dönüştürülecekse ya da \"battle card\", \"rakibi nasıl yeneriz\" istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: strategy
  title: "Rekabet kartı hazırlama"
  related: "competitor-analysis, positioning-statement, pricing-analysis, rfp-response, elevator-pitch"
  prompt: "Satış ekibimiz için VendorX'e karşı bir rekabet kartı hazırla; orta ölçekli anlaşmaları fiyat yüzünden onlara kaybediyoruz ama entegrasyon önemli olduğunda kazanıyoruz."
---

# Rekabet Kartı Hazırlama

## Amaç
Bir satış temsilcisine veya ön satış mühendisine tek bir rakibe karşı canlı bir görüşmede ihtiyaç duyduğu her şeyi tek sayfada vermek: konuşmayı nereye yönlendireceği, ne soracağı, itirazlara nasıl cevap vereceği ve neyi iddia etmemesi gerektiği.

## Ne zaman kullanılır
- Bir rakip anlaşmalarda veya RFP'lerde sürekli karşımıza çıkıyorsa.
- Kazanma/kaybetme bulguları veya analist notları sahada kullanılabilir rehbere dönüştürülecekse.
- Yeni bir rakip, sürüm veya fiyat değişikliği satış mesajlarının hızla güncellenmesini gerektiriyorsa.

## Ne zaman kullanılmaz
- Birçok rakibin pazar düzeyinde geniş bir karşılaştırması gerekiyorsa `competitor-analysis` kullanılır.
- Ürünün temel konumlandırması henüz tanımlı değilse önce `positioning-statement` kullanılır.
- Belirli bir ihaleye resmi yanıt gerekiyorsa `rfp-response` kullanılır.

## Girdiler
Zorunlu:
- Rakibin adı ve bizim ürünümüz/teklifimiz.
- Onlara karşı anlaşmalar hakkında en azından bir miktar kanıt (kazanma/kaybetme notları, satış geri bildirimi, kullanıcının sağladığı kamuya açık materyal).

İsteğe bağlı, kaliteyi artırır:
- Hedef segment ve tipik alıcı rolleri, fiyat bilgisi, müşteri referansları, rakibin son sürümleri.

Hiç kanıt yoksa bunu belirt, kartı her iddiası `[DOĞRULANMADI]` işaretli bir hipotez taslağı olarak hazırla ve toplanacak kanıtları listele. Rakip özelliği, fiyatı veya müşteri adı asla uydurma.

## Süreç
1. Bağlamı sabitle: segment, anlaşma büyüklüğü, alıcı rolleri ve rakibin genellikle ortaya çıktığı aşama.
2. Rakibi 2-3 satırda özetle: konumlandırması, tipik satış söylemi ve en iyi kime sattığı.
3. Kanıttan yola çıkarak "şu durumda kazanıyoruz" ve "şu durumda kaybediyoruz" koşullarını listele (özellik değil, anlaşma örüntüleri). Kartın tamamını bunlar yönlendirir.
4. Alıcı için önemli olan 3-5 farklılaştırıcımızı, her biri için bir kanıtla (referans, demo, metrik, sertifika) ya da `[KANIT GEREKLİ]` ile listele.
5. Rakibin gerçek güçlü yönlerini dürüstçe listele ve her birinin nasıl yeniden çerçeveleneceğini veya etkisizleştirileceğini yaz; zayıf yönlerini kanıtı ve doğrulama tarihi veya kaynağıyla listele.
6. Keşif ve tuzak soruları yaz: alıcının bizim güçlü olduğumuz gereksinimleri kendisinin keşfetmesini sağlayan tarafsız sorular (örneğin "Mevzuat değiştiğinde e-fatura entegrasyonunuzun güncellemelerini nasıl yöneteceksiniz?").
7. En sık 4-6 itiraz için yanıt yaz: kabul et, yeniden çerçevele, kanıtla ve kısa bir savuşturma cümlesi ekle.
8. Fiyat rehberini yalnızca sağlanan verilerden yaz: destekleyemeyeceğin indirim taktikleri değil, toplam maliyetin nasıl konumlanacağı.
9. "Söyleme" kurallarını ekle: doğrulanamayan iddialar, kötüleme, hukuki/gizli bilgi, eskimiş özellik karşılaştırmaları.
10. Güncellik satırı ekle (sorumlu, kaynaklar, kullanıcının verdiği son gözden geçirme tarihi veya `[TBD]`), ardından daha derin pazar görünümü için `competitor-analysis`, kayıplar fiyat kaynaklıysa `pricing-analysis` veya konuşma metinleri için `elevator-pitch` öner.

## Çıktı formatı
```markdown
# Rekabet Kartı: <ürünümüz> - <rakip>
**Segment:** <...> | **Sorumlu:** <...> | **Son gözden geçirme:** <tarih veya TBD> | **Kaynaklar:** <...>

## Tek Cümlede
<bu segmentteki bir alıcının neden onlar yerine bizi seçmesi gerektiği>

## Kazandığımız / Kaybettiğimiz Durumlar
| Kazanıyoruz, eğer | Kaybediyoruz, eğer |
|---|---|

## Farklılaştırıcılarımız (kanıtıyla)
1. <farklılaştırıcı> – <kanıt veya [KANIT GEREKLİ]>

## Onların Güçlü Yönleri → Yanıtımız
| Güçlü yönleri | Nasıl yeniden çerçevelenir / etkisizleştirilir |
|---|---|

## Zayıf Yönleri (doğrulanmış)
- <zayıf yön> – <kanıt / kaynak>

## Keşif ve Tuzak Soruları
1. ...

## İtiraz Yanıtları
| İtiraz | Yanıt (kabul → yeniden çerçeve → kanıt) | Kısa savuşturma |
|---|---|---|

## Fiyat Rehberi
## Söyleme
```

## Kalite kontrol listesi
- [ ] Rakip hakkındaki her iddianın kaynağı var ya da `[DOĞRULANMADI]` olarak işaretli; hiçbir şey uydurulmadı.
- [ ] "Kazanıyoruz/kaybediyoruz" maddeleri özellik listesi değil, kanıttan türetilmiş anlaşma koşulları.
- [ ] Rakibin güçlü yönleri dürüstçe kabul edilmiş; kötüleyici veya hukuken riskli ifade yok.
- [ ] Tuzak soruları tarafsız ve alıcıya faydalı; saldırı gibi duran tuzaklar değil.
- [ ] Kart tek sayfaya sığıyor ve görüşme sırasında göz atılabilir.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her satırda bizim tik attığımız bir özellik tablosu. Alıcı ilk kontrol ettiğinde satış ekibi güvenilirliğini kaybeder.
- Eskimiş kartlar. Karta sorumlu, kaynak ve gözden geçirme tarihi koy; rakibin son sürümünden eski iddiaları çıkar.
- Fiyat itirazlarını yalnızca indirimle karşılamak. Sağlanan kanıtlarla toplam maliyet, risk ve değere ulaşma süresi üzerinden yeniden çerçevele.

## Örnek
Girdi: "Orta ölçekli anlaşmaları fiyat yüzünden VendorX'e kaybediyoruz ama entegrasyon önemli olduğunda kazanıyoruz."

Çıktıdan bir bölüm:
| Kazanıyoruz, eğer | Kaybediyoruz, eğer |
|---|---|
| Alıcının entegre edilecek 3+ sistemi var ve toplantıda bir BT paydaşı bulunuyor | Yalnızca departman alıcısı var, tek kullanım senaryosu, ilk filtre fiyat |

İtiraz: "VendorX %30 daha ucuz." `[satışın aktardığı rakam; doğrulanmalı]`
Zayıf yanıt: "Ucuzlar çünkü ürünleri kötü."
Güçlü yanıt: "Lisans fiyatı için haklısınız. Saydığınız üç entegrasyonun maliyetini karşılaştıralım; referanslarımızda bunlar bizimle [KANIT GEREKLİ: uygulama gün sayısı] sürdü." Kısa savuşturma: "Satın alması mı ucuz, işletmesi mi?"
