---
name: screen-requirements
description: "Ekran veya UI gereksinimlerini ekran bazında, görsel tasarımı dayatmadan tanımlar: amaç ve giriş noktaları, roller ve yetkiler; kaynağı, formatı, zorunluluk kuralı, varsayılanı ve mesaj davranışlı doğrulamalarıyla alanlar; aksiyonlar ve sonuçları; ekran durumları (boş, yükleniyor, hata, salt okunur, yetkisiz), gezinme, erişilebilirlik ve duyarlı tasarım ihtiyaçları. Tasarım ve geliştirme için bir ekran, form veya sayfanın tanımlanması gerektiğinde ya da 'bu ekran ne yapmalı' sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Ekran gereksinimi tanımlama"
  related: "wireframe-spec, error-message-writing, frd-writing, data-requirements, accessibility-audit"
  prompt: "Çağrı merkezi uygulamasındaki 'Müşteri adresini düzenle' formu için ekran gereksinimlerini yaz."
---

# Ekran Gereksinimi Tanımlama

## Amaç
Her ekranın her durumda neyi göstermesi, neyi kabul etmesi ve ne yapması gerektiğini tarif etmek; böylece tasarım yerleşim ve etkileşime odaklanır, geliştiriciler tutarlı davranış uygular ve test uzmanları neyi doğrulayacaklarını tam olarak bilir.

## Ne zaman kullanılır
- Yeni bir ekran, form, sayfa veya diyalog gerektiğinde ya da mevcut biri değiştiğinde.
- Tasarımcıların bir taslağı var ama alanlar, doğrulamalar ve durumlar tanımlanmamışsa.
- Davranış role veya duruma göre değişiyor ve geliştirmeden önce netleşmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Odak bir wireframe'in yerleşimi ve görsel hiyerarşisiyse `wireframe-spec` kullanılır.
- Yalnızca hata ve yardım metinleri yazılacaksa `error-message-writing` veya `microcopy` kullanılır.
- Tek tek ekranların ötesinde tüm sistem davranışı gerekiyorsa `frd-writing` kullanılır.

## Girdiler
Zorunlu:
- Ekranın amacı ve desteklediği süreç adımı veya hikaye.

İsteğe bağlı, kaliteyi artırır:
- Taslak veya eskiz, veri gereksinimleri, iş kuralları, rol matrisi, mevcut ekran, tasarım sistemi kuralları, erişilebilirlik hedefi.

Amaç veya desteklenen adım yoksa iste. Bir seferde en fazla 5 engelleyici soru sor; geri kalan her şey açık soru olur.

## Süreç
1. Ekranın amacını, kullanıcılarını/rollerini, giriş noktalarını (nereden ve hangi bağlamla) ve çıkış noktalarını belirt.
2. Rol bazında yetkileri tanımla: görüntüleme, düzenleme, aksiyonların kullanılabilirliği; yetkisi olmayan kullanıcının ne gördüğünü yaz.
3. Alanları mantıksal sırayla listele: etiket, iş anlamı, kaynak (veri öğesi veya hesaplama), düzenlenebilir veya salt okunur, format ve uzunluk, zorunluluk (her zaman veya koşullu), varsayılan ve izin verilen değerler.
4. Alan bazında ve alanlar arası doğrulamaları, ne zaman tetiklendiklerini (değişince, alandan çıkınca, kaydederken) ve mesaj davranışını yaz; iş kuralı ID'lerine referans ver.
5. Aksiyonları (butonlar, bağlantılar, toplu işlemler) ön koşulu, sonucu, onay ihtiyacı ve başarı, hata ve çift gönderimde ne olduğuyla listele.
6. Durumları tanımla: ilk açılış, boş (veri yok), yükleniyor, kısmi veri, doğrulama hatası, sistem hatası, salt okunur (ör. duruma göre), eşzamanlı değişiklik tespit edildi, yetkisiz.
7. Gezinmeyi ve kaydedilmemiş değişiklik davranışını, listeler için sayfalama/arama/sıralamayı ve ziyaretler arasında neyin hatırlandığını tanımla.
8. Erişilebilirliği (WCAG 2.2 AA: etiketler, klavye sırası, hata duyurusu, kontrast sorumlusu) ve cihaz/duyarlı tasarım ihtiyaçlarını belirt; görsel stili tasarıma bırak.
9. Ekranda gösterilen kişisel verileri ve maskeleme ihtiyaçlarını not et (ör. temsilciler için kısmen maskelenmiş telefon).
10. Varsayımları ve açık soruları muhataplarıyla listele; çıkarılan davranışı `[VARSAYIM]` olarak işaretle.
11. Hedef devam ediyorsa yerleşim için `wireframe-spec`, mesaj metinleri için `error-message-writing`, ekran geliştirildikten sonra `accessibility-audit` öner.

## Çıktı formatı
```markdown
# Ekran Gereksinimleri: <ekran adı> (SCR-<nn>)
Amaç: ... · Desteklediği: <hikaye / use case> · Roller: ...
Giriş noktaları: ... · Çıkış noktaları: ...

## Yetkiler
| Öğe / aksiyon | Rol A | Rol B |
## Alanlar
| # | Etiket | Anlam / kaynak | Düzenlenebilir | Format | Zorunlu | Varsayılan / değerler | Doğrulama (ne zaman) | Mesaj davranışı |
## Aksiyonlar
| Aksiyon | Ön koşul | Başarı sonucu | Hata sonucu | Onay |
## Durumlar
| Durum | Koşul | Kullanıcının gördüğü / yapabildiği |
## Gezinme ve Kalıcılık
## Erişilebilirlik ve Cihazlar
## Kişisel Veri ve Maskeleme
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her alanın kaynağı, düzenlenebilirliği, zorunluluk kuralı ve zamanlamasıyla doğrulaması var.
- [ ] Her aksiyonun ön koşulu, başarı ve hata sonuçları ve çift gönderim davranışı var.
- [ ] Boş, yükleniyor, hata, salt okunur ve yetkisiz durumları tanımlandı.
- [ ] Rol bazlı farklar açık.
- [ ] Erişilebilirlik hedefi ve kişisel veri maskelemesi ele alındı.
- [ ] Görsel stil dayatılmadı; çıkarılan davranış `[VARSAYIM]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca doldurulmuş mutlu durumu tanımlamak. Kullanıcılar boş, hata ve salt okunur durumlarda takılır; bunları tanımla.
- Yerleşimi davranışla karıştırmak ("alanın altında kırmızı yazı"). Mesajın tetikleyicisini ve içeriğini tanımla; sunuma tasarım karar verir.
- Uzun formlarda doğrulamayı yalnızca kaydetmede yapmak. Kullanıcı bir anda on hatayla karşılaşmasın diye zamanlamayı alan bazında belirle.

## Örnek
Girdi: "Çağrı merkezi temsilcileri müşteri adresini düzenler; açık teslimatı olan müşterilerin adresine dikkat edilmeli."

Çıktıdan bir bölüm:
| # | Etiket | Anlam / kaynak | Düzenlenebilir | Zorunlu | Doğrulama (ne zaman) |
|---|---|---|---|---|---|
| 3 | Posta kodu | Customer.address.postalCode | Evet | Evet | Seçili il için geçerli olmalı (alandan çıkınca) `[TBD: referans kaynağı]` |
| 4 | İlçe | Customer.address.district | Evet | Evet | Seçili ile ait olmalı (il değişince sıfırlanır) |

| Durum | Koşul | Kullanıcının gördüğü / yapabildiği |
|---|---|---|
| Açık teslimat | Müşterinin henüz sevk edilmemiş bir teslimatı var | Değişikliğin teslimatı etkileyeceği uyarısı; temsilci "teslimata uygula" veya "yalnızca sonrakiler" seçer `[VARSAYIM]` |
| Salt okunur | Düzenleme yetkisi olmayan temsilci rolü | Adres, telefon kısmen maskelenmiş olarak gösterilir; Kaydet aksiyonu yok |

Açık soru: Teslimat sevk edilmişken temsilci adresi değiştirebilir mi? — Lojistik
