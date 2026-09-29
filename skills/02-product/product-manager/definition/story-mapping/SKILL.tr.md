---
name: story-mapping
description: "Soldan sağa kullanıcı aktiviteleri ve adımlarından oluşan bir omurga, her adımın altında önceliğe göre dizilmiş hikayeler ve her biri kullanılabilir uçtan uca bir sonuç sunan yatay sürüm dilimleriyle kullanıcı hikaye haritası oluşturur. Bir ürün veya büyük özellik tüm kullanıcı yolculuğu boyunca planlanacaksa, düz backlog büyük resmi kaybettirdiyse ya da ekip ilk ve sonraki sürümlere ne gireceğinde uzlaşmalıysa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: definition
  title: "Kullanıcı hikaye haritası"
  related: "epic-breakdown, mvp-scoping, release-planning, customer-journey-map, roadmap"
  prompt: "B2B masraf yönetimi uygulamamız için, çalışanın fiş göndermesinden finansın ödemesine kadar bir hikaye haritası çıkar."
---

# Kullanıcı Hikaye Haritası

## Amaç
Kullanıcının yolculuğunu aktivite ve adımlardan oluşan bir omurga olarak dizmek, hikayeleri bunun altına yerleştirmek ve yatay sürüm dilimleri kesmek. Böylece her sürüm gerçek bir kullanıcının yolculuğu uçtan uca tamamlamasını sağlar ve ekip düz bir backlog'un gizlediği boşlukları görür.

## Ne zaman kullanılır
- Yeni bir ürün, büyük bir özellik veya platform değişikliği tüm kullanıcı yolculuğu boyunca planlanacaksa.
- Backlog uzun ve düz bir listeyse ve paydaşlar bir sürümün neyi mümkün kıldığını göremiyorsa.
- Ekip MVP'de ve sonraki sürüm dilimlerinde birlikte uzlaşmalıysa.

## Ne zaman kullanılmaz
- Yalnızca bir epic hikayelere bölünecekse `epic-breakdown` kullanılır.
- Amaç müşterinin mevcut deneyimini, duygularını ve sorunlarını anlamaksa `customer-journey-map` kullanılır.
- Kapsam belliyse ve tarih, bağımlılık ve güven seviyesi planlanacaksa `release-planning` kullanılır.

## Girdiler
Zorunlu:
- Ürün veya özellik, birincil kullanıcı(lar)ı ve yolculuğun hedefi (tetikleyiciden tamamlanmaya).

İsteğe bağlı, kaliteyi artırır:
- Mevcut backlog maddeleri, personalar, yolculuk haritası, araştırma bulguları.
- Sürüm hedefleri, zaman veya kapasite kısıtları, bilinen zorunluluklar (yasal, sözleşmesel).

Kullanıcılar veya yolculuk hedefi yoksa sor (en fazla 3 soru). Sürüm tarihi veya kapasite uydurma; `[TBD]` olarak işaretle.

## Süreç
1. Çerçeveyi sabitle: birincil persona(lar), yolculuğun tetikleyicisi ve tamamlanma tanımı, haritanın etkilemesi beklenen sonuç. Personaları somut adlandır; önerdiklerini `[VARSAYIM]` olarak işaretle.
2. Omurgayı kur: anlatı sırasına göre 4-8 kullanıcı aktivitesi (kullanıcı gözünden fiil öbekleri, ör. "Masraf gönder"), ardından her aktivitenin altındaki adımlar. Sistem bileşenlerini değil kullanıcıyı merkeze al.
3. Eksik veya yanlış sıralanmış adımları bulmak için omurgayı sesli bir hikaye gibi anlat ("Önce çalışan..., sonra..."); yolculuğun ayrıştığı yerlere diğer personaların adımlarını ekle.
4. Her adımın altına hikayeleri/seçenekleri kullanıcıya görünen yetenekler olarak, en temelden olsa iyi olura doğru dikey sırayla listele. Mevcut backlog maddelerini buraya yerleştir; hiçbir adıma oturmayanları çıkarılacak veya yeniden çerçevelenecek aday olarak işaretle.
5. Fonksiyonel olmayan ihtiyaçları (güvenlik, gizlilik/KVKK/GDPR, erişilebilirlik, performans) ve operasyon/destek adımlarını ayrı bir kolon olarak değil, ilgili adımlarda kart olarak işaretle.
6. Sürüm dilimlerini yatay kes: 1. dilim personanın tüm omurgayı tamamlamasını sağlayan en ince kümedir (uçtan uca iskelet / MVP); sonraki dilimler adımları derinleştirir. Her dilim yolculuğun gerektirdiği her aktiviteye dokunmalı.
7. Her dilime adı konmuş bir sonuç ve ölçülebilir bir sinyal ver ("çalışanlar fişlerin %80'ini uygulamadan gönderiyor" teyit edilecek hedef olarak; başlangıç değeri uydurulmaz).
8. Her dilimde boşluk kontrolü yap: bir dilimde kartı olmayan adım yolculuğu kırar; ya en basit seçeneği (manuel bile olsa) ekle ya da boşluğu gerekçesiyle açıkça kabul et.
9. Dilim başına bağımlılıkları, açık soruları ve riskleri not et; araştırma veya spike gerektiren kartları işaretle.
10. Çıkarım yapılan adımları ve öncelikleri `[VARSAYIM]` olarak etiketle. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: ayrıntılı hikayeler için `epic-breakdown`, 1. dilimi sorgulamak için `mvp-scoping`, dilimleri takvime oturtmak için `release-planning`.

## Çıktı formatı
```markdown
# Hikaye Haritası: <ürün / yolculuk>
Persona(lar): <...> · Tetikleyici: <...> · Tamamlanma: <...> · Sonuç: <...>

## Omurga
| Aktivite | <Aktivite 1> | <Aktivite 2> | ... |
|---|---|---|---|
| Adımlar | <adım a>, <adım b> | <adım c> | ... |

## Harita (her adımın altında hikayeler, en üstte en temel olan)
| Dilim | <adım a> | <adım b> | <adım c> | ... |
|---|---|---|---|---|
| Sürüm 1 – <sonuç> | <kart> | <kart> | <kart (manuel)> | |
| Sürüm 2 – <sonuç> | <kart> | – | <kart> | |
| Daha sonra | ... | | | |

## Dilim Sonuçları ve Sinyaller
| Dilim | Sonuç | Sinyal / hedef | Kabul edilen boşluklar |
|---|---|---|---|

## Kesişen Kartlar (NFR, destek, uyum)
- ...

## Bağımlılıklar, Riskler ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Omurga aktiviteleri sistem modülleri değil, anlatı sırasına göre kullanıcı eylemleri.
- [ ] Sürüm 1, bazı adımlar manuel olsa bile personanın tüm yolculuğu tamamlamasını sağlıyor.
- [ ] Her dilimin adı konmuş bir sonucu ve ölçülebilir bir sinyali var; başlangıç değeri uydurulmadı.
- [ ] Her dilimdeki boşluklar dolduruldu ya da gerekçesiyle açıkça kabul edildi.
- [ ] NFR, gizlilik ve destek ihtiyaçları ilgili adımlarda kart olarak yer alıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Omurgayı ekranlardan veya servislerden kurmak ("Giriş sayfası", "Ödeme API'si"). Kullanıcının ne yapmaya çalıştığı olarak yeniden yaz.
- Aktiviteye göre dikey dilimlemek ("Sürüm 1 = gönderim, Sürüm 2 = onay"). Son sürüme kadar kimse yolculuğu bitiremez; yatay dilimle.
- Haritayı bir kerelik çıktı saymak. Her sürümden sonra geri bildirim ve benimsenme verisiyle yeniden gözden geçir.

## Örnek
Girdi: "B2B masraf uygulaması, çalışanın fiş göndermesinden finansın ödemesine kadar."

Çıktıdan bir bölüm:
| Dilim | Fişi yakala | Talebi gönder | Onayla | Öde |
|---|---|---|---|---|
| Sürüm 1 – çalışanlar kağıtsız geri ödeme alır | Fotoğraf yükleme | Tek para birimli talep formu | Yönetici e-posta bağlantısıyla onaylar | Finans onaylı talepleri mevcut bordroya aktarır (manuel) |
| Sürüm 2 – daha hızlı, daha az hata | OCR ile ön doldurma | Çoklu para birimi, politika uyarıları | Vekaletli uygulama içi onay | Doğrudan banka dosyası |
- Zayıf dilim: "Sürüm 1 = OCR'lı fiş yakalama, çoklu para birimi" (kimse geri ödeme alamıyor).
- Açık soru: Bordro aktarım formatı finans sistemi tarafından sabit mi?
