---
name: app-store-release-notes
description: "Bir changelog, iş kaydı listesi veya pull request başlıklarından mobil uygulama mağazaları için kısa, kullanıcıya dönük \"Yenilikler\" sürüm notları yazar; iç değişiklikleri ayıklar, her mağazanın karakter sınırına uyar ve yerelleştirilmiş varyantlar hazırlar. Bir mobil sürüm mağazaya gönderilmek üzereyken, ham bir changelog mağaza metnine dönüştürülecekken veya notların bir mağaza için yerelleştirilmesi ya da kısaltılması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: mobile
  title: "Uygulama mağazası sürüm notları"
  related: "release-notes, changelog-entry, mobile-release-checklist, microcopy, voice-and-tone-guide"
  prompt: "Bu sprintte merge edilen PR başlıklarını 5.3 sürümü için App Store ve Google Play sürüm notlarına çevir, İngilizce ve Türkçe."
---

# Uygulama Mağazası Sürüm Notları

## Amaç
Kullanıcıya bu sürümde kendisi için neyin iyileştiğini birkaç satırda, ürünün sesiyle ve mağaza sınırları içinde anlatmak. İyi mağaza notları puanları destekler, destek taleplerini azaltır ve hiçbir zaman iç ya da güvenlik ayrıntısı sızdırmaz.

## Ne zaman kullanılır
- Bir mobil build mağazaya gönderilmeye hazır olduğunda ve "Yenilikler" metni gerektiğinde.
- Mühendislik ekibinin changelog'u veya PR listesi kullanıcı diline çevrilecekse.
- Notların yerelleştirilmesi, kısaltılması veya farklı mağazalara uyarlanması gerektiğinde.

## Ne zaman kullanılmaz
- Müşteri, destek veya operasyon için ayrıntılı sürüm notları için `release-notes` kullanılır.
- Repodaki geliştiriciye dönük değişiklik geçmişi için `changelog-entry` kullanılır.
- Build'in gönderime hazır olup olmadığını kontrol etmek için `mobile-release-checklist` kullanılır.

## Girdiler
Zorunlu:
- Bu sürümdeki değişikliklerin listesi (changelog, iş kayıtları, PR başlıkları veya açıklama) ve sürüm numarası.

İsteğe bağlı, kaliteyi artırır:
- Hedef mağazalar ve diller; ürünün ses ve ton rehberi.
- Hangi değişikliklerin feature flag veya kademeli yayın arkasında olduğu, hangilerinin platforma özel olduğu.
- Ekibin kullandığı mağaza karakter sınırları ve üslup için önceki notlar.

Değişiklik listesi yoksa iste. Özellik uydurma; bir değişikliğin kullanıcı faydası net değilse `[VARSAYIM]` olarak işaretle veya sor.

## Süreç
1. Her değişikliği sınıflandır: kullanıcıya görünen özellik, iyileştirme, düzeltme, platforma özel, iç değişiklik (refactor, bağımlılık, araç, analitik) veya güvenlik.
2. İç değişiklikleri çıkar. Güvenlik düzeltmelerini açığı tarif etmeden genel olarak belirt ("güvenlik iyileştirmeleri").
3. Kapalı feature flag veya sınırlı yayın arkasındaki maddeleri, ekip bu build'in tüm kullanıcılarına göründüğünü teyit etmedikçe çıkar veya beklet.
4. Kalan her maddeyi kullanıcı faydasına çevir: kullanıcının artık ne yapabildiği veya neyin onu rahatsız etmeyi bıraktığı, sade bir dille; iş kaydı numarası, bileşen adı veya jargon yok.
5. Kullanıcı değerine göre sırala: önce öne çıkan özellik, sonra iyileştirmeler, ardından küçükse tek satırda gruplanmış düzeltmeler.
6. Mağaza sınırına sığdır: her mağaza için sınırı kullanıcıyla teyit et; bilinmiyorsa ana metni yaygın en katı sınıra (yaklaşık 500 karakter) göre kısa tut ve en önemli maddeyi ilk satıra koy, çünkü mağazalar önizlemeyi keser.
7. Ürün sesini uygula: tutarlı zaman ve kişi, abartı yok, gelecek sürümlerle ilgili vaat yok, rakip karşılaştırması yok ve mağaza içerik kurallarını ihlal eden hiçbir şey yok (örneğin diğer platformlara atıf veya ekibin onaylamadığı fiyat iddiaları).
8. Özellikler iOS ve Android arasında farklıysa platform varyantları, ayrıca kelimesi kelimesine değil, o dilde yazılmış yerelleştirilmiş varyantlar üret; çeviriden sonra uzunluğu yeniden kontrol et.
9. Yalnızca bakım içeren sürümlerde gerçek bir kullanıcı faydası (kararlılık, hız) varsa genel "hata düzeltmeleri" yerine onu yaz.
10. Varsayımları ve çıkarılan maddeleri gerekçesiyle listele ki sürüm sahibi teyit edebilsin.
11. Kullanıcı devam ederse gönderimin kendisi için `mobile-release-checklist`, daha kapsamlı müşteri notları için `release-notes`, ifadeleri iyileştirmek için `microcopy` öner.

## Çıktı formatı
```markdown
# Mağaza Sürüm Notları: v<sürüm>

## <Mağaza> · <dil> (<n>/<sınır> karakter)
<Öne çıkan fayda cümlesi.>
• <fayda>
• <fayda>
• Düzeltmeler: <kısa, gruplanmış satır>

## Çıkarılan veya Bekletilenler
| Madde | Neden (iç / flag / güvenlik / belirsiz) |
|---|---|

## Sürüm Sahibi İçin Varsayımlar ve Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her satır bir kullanıcı faydasını anlatıyor; iş kaydı numarası, iç ad veya jargon yok.
- [ ] Kapalı, flag arkasında veya bu build'de olmayan hiçbir özellikten söz edilmiyor.
- [ ] Güvenlik düzeltmeleri istismar edilebilecek ayrıntıda anlatılmıyor.
- [ ] Her varyant karakter sayısını belirtiyor ve teyit edilen ya da temkinli sınıra sığıyor.
- [ ] Yerelleştirilmiş metin doğal okunuyor ve çeviriden sonra uzunluğu kontrol edildi.
- [ ] Net olmayan faydalar `[VARSAYIM]` olarak işaretli ve teyit için listeli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Mühendislik changelog'unu yapıştırmak ("PaymentService refactor edildi, SDK güncellendi"). Kullanıcı bununla bir şey yapamaz; çevir veya çıkar.
- Hâlâ flag arkasında olan ya da %5'e açılmış bir özelliği duyurmak; bu destek talebi ve kötü yorum üretir.
- Anlatılacak gerçek bir fayda varken her sürümde yalnızca "Hata düzeltmeleri ve performans iyileştirmeleri" yazmak.

## Örnek
Girdi: "v5.3 PR'ları: feat: kayıtlı aramalar; fix: ödeme ekranında döndürünce çökme (Android); chore: analitik SDK güncellemesi; feat(flag kapalı): karanlık mod beta."

Zayıf: "v5.3: kayıtlı aramalar, Android ödeme döndürme çökmesi düzeltildi, analitik SDK güncellemesi, karanlık mod beta."

Güçlü (Google Play, tr, 198/500):
"Aramalarınızı kaydedin, Arama sekmesinden tek dokunuşla yeniden açın.
• Telefonu döndürdüğünüzde ödeme ekranı artık beklenmedik şekilde kapanmıyor.
• Küçük düzeltmeler ve kararlılık iyileştirmeleri."

Çıkarılanlar: analitik SDK güncellemesi (iç değişiklik); karanlık mod beta (flag kapalı).
