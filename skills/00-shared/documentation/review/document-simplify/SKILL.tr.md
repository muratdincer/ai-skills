---
name: document-simplify
description: "Bir dokümanı veya metin parçasını; tüm yükümlülükleri, sayıları, koşulları ve kararları koruyarak tekrarları, jargonu, çekinceli ifadeleri ve isimleştirmeleri ayıklayıp hedef kitlesi için daha kısa ve kolay okunur hâle getirir. Bir metin okuyucusu için fazla uzun, yoğun veya teknikse, bir şeyin kısaltılması, sadeleştirilmesi veya sade dille yazılması istendiğinde ya da doküman bir uzunluk sınırına sığmalıysa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: documentation
  area: review
  title: "Dokümanı sadeleştirme"
  related: "document-review, executive-summary, tone-rewrite, microcopy, technical-translation"
  prompt: "Üç sayfalık bu veri saklama politikasını takım liderlerinin ne yapmaları gerektiğini anlayacağı şekilde sadeleştir; tüm yükümlülükleri koru."
---

# Dokümanı Sadeleştirme

## Amaç
Anlamı kaybetmeden okuma yükünü belirgin biçimde azaltmak; böylece hedef okuyucular içeriği ilk okumada anlar ve buna göre hareket eder.

## Ne zaman kullanılır
- Bir politika, rehber, şartname veya e-posta doğru ama hedef kitlesi için fazla uzun veya yoğunsa.
- Teknik bir metnin uzman olmayanlarca anlaşılması gerekiyorsa.
- Bir doküman sayfa, kelime veya karakter sınırına sığmalıysa.

## Ne zaman kullanılmaz
- Amaç, sadeleştirilmiş tam sürüm değil uzun bir metnin kısa ve karar odaklı özetiyse `executive-summary` kullanılır.
- Sorun uzunluk veya karmaşıklık değil ton ise (fazla sert, fazla gayriresmî) `tone-rewrite` kullanılır.
- İçeriğin kendisi eksik veya yanlışsa önce `document-review` kullanılır.

## Girdiler
Zorunlu:
- Sadeleştirilecek metin.

İsteğe bağlı, kaliteyi artırır:
- Hedef kitle ve uzmanlık düzeyi.
- Hedef uzunluk veya kısaltma oranı.
- Aynen kalması gereken terimler veya bölümler (hukuki ifadeler, tanımlı terimler, sözleşme maddeleri).

Metin yoksa iste. Hedef kitle bilinmiyorsa bilgili ama uzman olmayan bir okuyucu varsay ve bunu `[VARSAYIM]` olarak belirt.

## Süreç
1. Düzenlemeden önce taşıyıcı içeriğin envanterini çıkar: yükümlülükler (-malıdır/zorunludur), izinler, yasaklar, sayılar, tarihler, eşikler, koşullar, istisnalar, sorumlular ve kararlar. Bu liste değişmezdir.
2. Aynen kalacak bölgeleri (hukuki maddeler, tanımlı terimler, alıntılanan gereksinimler) belirle; dokunma veya referans ver.
3. Doküman düzeyinde kes: tekrarlanan bölümleri, okuyucunun aksiyon almak için ihtiyaç duymadığı arka planı ve kararları değiştirmeyen tarihçeyi çıkar; referans içeriği eke taşı.
4. Yeniden yapılandır: okuyucunun yapması veya bilmesi gerekenle başla; sıralı işleri numaralı adımlara, paralel koşulları tablolara veya listelere çevir.
5. Cümleleri sadeleştir: cümle başına tek fikir, eylemi yapanı belli etken çatı, isimleştirme yerine fiil ("değerlendirme yapılması" yerine "değerlendirmek"), ortalama 15-20 kelime hedefle.
6. Jargonu hedef kitle için sade kelimelerle değiştir; gerekli teknik terimleri koru ve bir kez tanımla.
7. Gerçek bir belirsizliği ifade etmiyorsa çekinceli ve dolgu ifadeleri çıkar ("belirtmek gerekir ki", "... amacıyla", "temelde").
8. Sonucu değişmez listeyle karşılaştır; her madde aynı bağlayıcılık ve değerle hâlâ yer almalı.
9. Kısalma oranını (yaklaşık önce/sonra kelime sayısı) ve bilinçli olarak çıkarılan veya taşınan içeriği raporla.
10. Kullanıcının hedefi devam ediyorsa kapsamlı kalite incelemesi için `document-review`, karar vericinin tek sayfalık sürüme ihtiyacı varsa `executive-summary` öner.

## Çıktı formatı
```markdown
## Sadeleştirilmiş Sürüm
<yeniden yazılmış metin>

## Değişiklik Notları
- Uzunluk: ~<önce> → ~<sonra> kelime
- Çıkarılan: <ne ve neden>
- Eke taşınan / referans verilen: <...>
- Aynen korunan: <...>
- Anlam kontrolü: <n> yükümlülük, sayı ve koşulun tümü korundu | sorunlar: <yok veya liste>
```

## Kalite kontrol listesi
- [ ] Kaynaktaki her yükümlülük, sayı, tarih, eşik, koşul ve istisna hâlâ mevcut.
- [ ] Kiplik gücü değişmemiş ("-malıdır" "-abilir"e dönüşmemiş).
- [ ] Aynen kalacak bölgelere dokunulmamış.
- [ ] Her cümlenin net bir öznesi ve tek ana fikri var.
- [ ] Yerinde bırakılan jargon bir kez tanımlanmış.
- [ ] Değişiklik notları çıkarılan her şeyi listeliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Koşulları ve istisnaları ("... olmadıkça", "yalnızca ... ise") sadeleştirirken kaybetmek; bu kuralı değiştirir. Onları değişmez listede koru.
- Metni belirsizleştirerek kısaltmak ("uygun şekilde"). Kısa ve kesin olmalı, kısa ve muğlak değil.
- Kesin terimleri, alanda farklı anlamı olan gündelik eş anlamlılarla değiştirmek.

## Örnek
Girdi (bölüm): "Belirtmek gerekir ki, kişisel verilerin ilk toplanma amacı doğrultusunda artık gerekli olmaması durumunda, söz konusu verilerin silinmesinin 30 günü aşmayacak bir süre içerisinde gerçekleştirilmesinin sağlanması veri sahibinin sorumluluğundadır."

Çıktıdan bir bölüm: "Kişisel veri, toplanma amacı için artık gerekli değilse veri sahibi bu veriyi 30 gün içinde silmelidir."
Değişiklik notu: 30 → 16 kelime; yükümlülük (-malıdır), sorumlu (veri sahibi) ve süre (30 gün) korundu.
