---
name: transcript-cleanup
description: "Ham veya otomatik oluşturulmuş bir toplantı dökümünü dolgu sözcüklerini, yarım cümleleri ve üst üste konuşmaları ayıklayarak, konuşmacı etiketlerini ve bariz tanıma hatalarını düzelterek, anlamı ve ifadeleri koruyarak temizler. Bir döküm özete dönüştürülmeden okunabilir, alıntılanabilir veya arşivlenebilir hâle getirilecekse kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: meetings
  area: during
  title: "Toplantı dökümünü temizleme"
  related: "meeting-notes, meeting-minutes, meeting-summary, glossary-builder"
  prompt: "Tedarikçi görüşmemizin otomatik dökümünü temizle. Konuşmacı 1 benim (Selin), Konuşmacı 2 tedarikçinin proje yöneticisi."
---

# Toplantı Dökümünü Temizleme

## Amaç
Kimin ne söylediğini ve ne kastettiğini koruyan, okunabilir ve doğru bir döküm üretmek. Böylece döküm alıntılanabilir, incelenebilir veya not ve tutanaklar için kaynak olarak kullanılabilir.

## Ne zaman kullanılır
- Otomatik döküm dolgu sözcükleri, kopuk cümleler ve genel konuşmacı etiketleri içeriyorsa.
- Bir görüşme (mülakat, tedarikçi görüşmesi, tasarım incelemesi) kelimesi kelimesine yakın arşivlenecekse.
- Bir rapor veya karar kaydı için dökümden alıntı yapılacaksa.

## Ne zaman kullanılmaz
- Kullanıcı diyalog yerine yapı veya sonuç istiyorsa `meeting-notes` veya `meeting-summary` kullanılır.
- Kararların resmi kaydı gerekiyorsa `meeting-minutes` kullanılır.

## Girdiler
Zorunlu:
- Döküm metni.

İsteğe bağlı:
- Konuşmacı eşleştirmesi (etiket - isim/rol), ürün adları, kısaltmalar ve kişi adları sözlüğü, istenen temizlik düzeyi (hafif "temiz birebir" veya daha yoğun "okunabilir").

Konuşmacı eşleştirmesi yoksa orijinal etiketleri koru; içerikten açıkça anlaşılıyorsa bir eşleştirmeyi `[VARSAYIM]` ile öner.

## Süreç
1. Temizlik düzeyini netleştir. Varsayılan temiz birebirdir: dolgu sözcüklerini çıkar, konuşmacının sözcüklerini ve sırasını koru.
2. Konuşmacı etiketlerini tutarlı biçimde isim veya role çevir; tanıma aracının böldüğü aynı konuşmacıya ait parçaları birleştir.
3. Dolgu sözcüklerini ("ıı", "eee", dolgu olarak kullanılan "şey", "yani", "işte", İngilizce "uh", "you know"), kekelemeleri, yarım başlangıçları ve tekrarlanan sözcükleri çıkar.
4. Bariz tanıma hatalarını bağlam ve sözlük yardımıyla düzelt (ürün adları, kısaltmalar, teknik terimler). Emin değilsen orijinali koru ve `[?]` ekle.
5. Noktalama ve paragraf araları ekle; farklı sözcüklerle yeniden ifade etme, argümanların sırasını değiştirme.
6. Anlamı değiştiren çekinceleri ve niteleyicileri koru ("bence", "muhtemelen", "3. çeyrekten önce değil"). Bunlar dolgu değil, içeriktir.
7. Duyulmayan veya üst üste konuşulan yerleri `[anlaşılmıyor ss:dd:sn]` veya `[üst üste konuşma]` olarak işaretle; asla doldurma.
8. Kaynakta zaman damgası varsa konuşma veya paragraf düzeyinde koru.
9. Amaç için gerekmeyen hassas kişisel verileri (telefon, kimlik bilgisi, sağlık ayrıntısı) `[GİZLENDİ]` olarak maskele.
10. Sona kısa bir değişiklik notu ekle: temizlik düzeyi, kullanılan konuşmacı eşleştirmesi, belirsiz nokta sayısı.
11. Kullanıcının hedefi devam ediyorsa temizlenmiş dökümü yapılandırmak için `meeting-notes`, kısa bir özet için `meeting-summary` öner.

## Çıktı formatı
```markdown
# Döküm: <toplantı başlığı> – <tarih>
Temizlik düzeyi: <temiz birebir / okunabilir>
Konuşmacılar: <etiket> = <isim, rol>; ...

[00:00:12] **<İsim>:** <temizlenmiş metin>

[00:01:05] **<İsim>:** <temizlenmiş metin> [?terim]

[00:02:40] [üst üste konuşma]

---
Temizlik notları
- Konuşmacı eşleştirmesi: <teyitli / [VARSAYIM]>
- Belirsiz terimler: <zaman damgalarıyla liste>
- Gizlemeler: <sayı ve tür>
```

## Kalite kontrol listesi
- [ ] Hiçbir cümle kaynağa göre anlam değiştirmedi.
- [ ] Çekinceler, sayılar, tarihler ve olumsuzluklar korundu.
- [ ] Konuşmacı etiketleri dökümün tamamında tutarlı.
- [ ] Belirsiz her sözcük tahmin edilmedi, `[?]` ile işaretlendi.
- [ ] Duyulmayan kısımlar uydurulmadı, işaretlendi.
- [ ] Hassas kişisel veriler gizlendi.
- [ ] Girdide söylenmeyen her şey `[VARSAYIM]` olarak işaretlendi veya açık soru olarak listelendi; olgu gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Özetlemeye kaymak. Temizlenmiş döküm içerik taşıyan her konuşmayı korur.
- Konuşmacının olgusal hatasını "düzeltmek". Söyleneni koru; gerekirse `[sic]` ekle.
- Dolgu temizlerken olumsuzlukları veya niteleyicileri düşürmek ("pek değil", "henüz değil"); bu anlamı tersine çevirir.

## Örnek
Girdi: "Konuşmacı 2: evet yani ıı biz biz API'yi belki şey mayıs sonuna kadar verebiliriz ama raporlama kısmını değil"

Çıktıdan bir bölüm:
[00:14:22] **Tedarikçi PY:** API'yi belki mayıs sonuna kadar verebiliriz, ama raporlama kısmını değil.
