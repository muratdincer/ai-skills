---
name: review-comment-writing
description: "Kod inceleme yorumlarını somut, nazik ve uygulanabilir olacak şekilde yazar veya yeniden yazar; her yorumu önem ve niyetine göre etiketler (Critical, Required, Nit, Optional, FYI; ayrıca soru ve takdir) ve gerekçe ile önerilen değişiklikle destekler. İnceleyenin bir pull request üzerinde ham gözlemleri veya sert taslak yorumları olduğunda ve bunları net ifade etmek istediğinde ya da inceleme yazışmaları gerginleştiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: collaboration
  title: "İnceleme yorumu yazma"
  related: "code-review, feedback-sbi, tone-rewrite, coding-standards, conflict-resolution"
  prompt: "İnceleme yorumlarımı sert olmadan ama net olacak şekilde yeniden yaz. İlki şu: 'bu yanlış, neden döngü içinde sorgu atıyorsun?'"
---

# İnceleme Yorumu Yazma

## Amaç
İnceleme gözlemlerini, yazarın önem derecesini tahmin etmek zorunda kalmadan ve kendini saldırı altında hissetmeden uygulayabileceği yorumlara dönüştürmek. Net etiketler ve gerekçeler gidip gelmeleri azaltır, incelemeyi kod üzerinde tutar ve merge'ü neyin engellediğini açık hâle getirir.

## Ne zaman kullanılır
- İnceleyenin bulguları var ve bunları PR yorumu olarak yazmak istiyor.
- Taslak yorumlar kısa, iğneleyici veya engelleyici olup olmadıkları konusunda belirsiz.
- Bir inceleme yazışması tartışmaya dönmüş ve yapıcı bir yanıt gerekiyor.

## Ne zaman kullanılmaz
- Sorunları bulmak için `code-review` kullanılır.
- Kod yerine bir kişinin davranışı veya performansı hakkında geri bildirim için `feedback-sbi` kullanılır.

## Girdiler
Zorunlu:
- Gözlemler veya taslak yorumlar; her biri ilgili kodla (veya kodun açıklamasıyla) birlikte.

İsteğe bağlı, kaliteyi artırır:
- Ekibin yorum etiketi kuralı ve kodlama standartları.
- İlişki bağlamı (yeni katılan, başka ekipten katkı veren, kıdemli meslektaş).
- Bir yazışmaya yanıt veriliyorsa yazarın cevabı.

Bir yorumun kod bağlamı eksikse ve yorum teknik bir iddia içeriyorsa kod parçasını iste veya iddiayı soru olarak bırak.

## Süreç
1. Her gözlem için etiketi seç: `Critical` (merge'ü engeller, riski belirt), Required (varsayılan, önek yok: merge öncesi ele alınmalı), `Nit` (önemsiz, yazar görmezden gelebilir), `Optional` (daha iyi alternatif, karar yazarın), `FYI` (bilgi, aksiyon gerekmez), `question` (henüz bilmiyorsun), `praise` (somut ve samimi). Bu PR'ın dışında kalan geçerli noktalar "takip işi" notuyla `Optional` olur.
2. İddianın doğru ve somut olduğunu kontrol et. Görünen koddan kanıtlayamıyorsan soruya çevir.
3. Gözlemi kişiye değil koda yönelt: "sorgu atıyorsun" yerine "bu döngü her öğe için bir sorgu çalıştırıyor".
4. Sonucu veya gerekçeyi yaz: hata, risk, maliyet, ihlal edilen standart (varsa kurala bağlantı ver).
5. Yalnızca sorunu değil somut düzeltmeyi öner: kod parçası, kullanılacak API veya kalıp; birden fazla geçerli çözüm varsa seçenek olarak sun.
6. Kısa tut: yorum başına tek konu, iki ila dört cümle; retorik soru, iğneleme, "sadece" veya "tabii ki" yok.
7. Tekrarlanan sorunları birleştir: bir kez yorum yap ve "aynısı X, Y satırları için de geçerli" de.
8. Tartışmalı yazışmalarda: yazarın görüşünü adil biçimde yeniden ifade et, asıl anlaşmazlığı adlandır, bir karar kuralı öner (standart, veri, teknik liderin kararı) veya konuyu yüz yüze görüşmeye taşı.
9. Gerçekten iyi yapılmış bir şey varsa en az bir somut takdir yorumu ekle.
10. Gözlemlerin kendisi eksik veya doğrulanmamışsa önce `code-review` çalıştırılmasını öner; kod yerine davranışla ilgili geri bildirim için `feedback-sbi` öner.

## Çıktı formatı
```markdown
**[<etiket>]** <konumuyla birlikte kod hakkındaki gözlem>
<gerekçe / sonuç, bir iki cümle>
<önerilen değişiklik veya kod parçası>   (isteğe bağlı: "Aynısı <konumlar> için de geçerli.")
```
Yeniden yazımlarda her orijinal yorumu yeni hâliyle yan yana tabloda göster:
| # | Orijinal | Yeniden yazılmış | Etiket |
|---|---|---|---|

## Kalite kontrol listesi
- [ ] Her yorumun önemi net (tek etiket veya Required anlamına gelen öneksiz yorum) ve Critical yorumlar riski açıklıyor.
- [ ] Hiçbir yorum kişiye yönelmiyor ("hep böyle yapıyorsun", "neden böyle yaptın").
- [ ] Soru olmayan her yorum somut bir değişiklik öneriyor.
- [ ] Koddan doğrulanamayan iddialar soru olarak ifade edilmiş.
- [ ] Tekrarlanan sorunlar birleştirilmiş.
- [ ] Nit'ler az; tekrarlıyorsa bir linter veya formatter kuralı öneriliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Etiketsiz yorumlar: yazar her yorumu engelleyici sanar ve inceleme tıkanır. Her şeyi etiketle.
- Gerçek bir Critical sorunu belirsiz bir "belki düşünebilirsin"e yumuşatmak. Nazik ama net ol: engellediğini ve nedenini söyle.
- Aslında eleştiri olan yönlendirici sorular ("Bunu test ettin mi?"). Gerçek soru sor veya endişeyi açıkça yaz.

## Örnek
Girdi: `for (id in ids) repo.findById(id)` satırına "bu yanlış, neden döngü içinde sorgu atıyorsun?" yorumu.

Zayıf (orijinal): "bu yanlış, neden döngü içinde sorgu atıyorsun?" — önem belirsiz, kişiye yönelik, düzeltme yok.

Güçlü (yeniden yazılmış):
**[Critical]** `OrderLoader.kt:31` her sipariş ID'si için ayrı bir veritabanı sorgusu çalıştırıyor. 500 ürünlük bir sepette bu, ödeme akışında 500 gidiş-dönüş demek.
Bunları tek çağrıda, örneğin `repo.findAllById(ids)` ile alıp sonuçları ID'ye göre eşleyebilir miyiz? Aynı kalıp `InvoiceLoader.kt:58` içinde de var.
