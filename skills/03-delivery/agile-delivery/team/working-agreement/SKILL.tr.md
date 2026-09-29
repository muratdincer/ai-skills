---
description: "Ekip çalışma sözleşmesini kolaylaştırır ve yazar: iletişim kanalları ve yanıt süreleri, erişilebilirlik ve ortak çalışma saatleri, kod incelemesi ve eşli çalışma, toplantılar, karar alma, nöbet ve çatışma yönetimine dair normları toplar, bunları somut ve gözlemlenebilir taahhütlere dönüştürür, sözleşmenin nasıl gözden geçirilip uygulanacağını belirler. Ekip kurulduğunda veya değiştiğinde, tekrarlayan sürtünmeler (yavaş incelemeler, toplantı yükü, mesai dışı mesajlar) görüldüğünde ya da ekip tüzüğü veya temel kurallar istendiğinde kullanılır."
related: "wip-policy, team-health-check, retrospective-facilitation, definition-of-done, conflict-resolution"
prompt: "Ekibimiz artık İstanbul ve Berlin arasında bölünmüş durumda, incelemeler günlerce bekliyor ve insanlara gece mesaj atılıyor. Bir çalışma sözleşmesi taslağı hazırlamamıza yardım et."
---

# Ekip Çalışma Sözleşmesi

## Amaç
Ekibin örtük beklentilerini herkesin üzerinde uzlaştığı kısa ve açık bir norm setine dönüştürmek. Böylece sürtünme bir kişiyi değil, ortak sözleşmeyi işaret ederek ele alınır.

## Ne zaman kullanılır
- Ekip yeni kurulduğunda, birleştiğinde ya da yeni üyeler veya lokasyonlar eklendiğinde.
- Tekrarlayan sürtünmeler olduğunda: yavaş incelemeler, belirsiz erişilebilirlik, toplantı yükü, mesai dışı mesajlar.
- Bir retrospektiften yazıya dökülmesi gereken normlarla ilgili aksiyonlar çıktığında.

## Ne zaman kullanılmaz
- Pano kolonları, WIP limitleri ve çekme kuralları için `wip-policy` kullanılır.
- Bitmiş işin kalite çıtası için `definition-of-done` kullanılır.
- Belirli bir kişilerarası çatışma için `conflict-resolution` kullanılır.

## Girdiler
Zorunlu:
- Ekip bağlamı: büyüklük, roller, lokasyonlar/saat dilimleri ve sözleşmeyi tetikleyen sorunlar veya hedefler (ya da bir ekip oturumundan ham girdiler).

İsteğe bağlı, kaliteyi artırır:
- Varsa mevcut sözleşme.
- Ekibi bağlayan kurumsal politikalar (çalışma saatleri, nöbet ücretlendirmesi, güvenlik kuralları).
- Kullanılan araç kategorileri (sohbet, görüntülü görüşme, iş takip sistemi); ürün adı gerekmez.

Tetikleyen sorunlar bilinmiyorsa kullanıcıdan en önemli 3 sürtünmeyi iste; sözleşme gerçek sorunlara yanıt vermeli. Ekip oturumu olmadan taslak hazırlanıyorsa her normu `[TASLAK – EKİP ONAYLAYACAK]` olarak işaretle.

## Süreç
1. Girdideki sürtünmeleri ve hedefleri listele ve her birini bir sözleşme alanına eşle: iletişim, erişilebilirlik, kod incelemesi/eşli çalışma, toplantılar, kararlar, kalite/bitti, nöbet/destek, çatışma ve geri bildirim, oryantasyon.
2. Ekiple yürütülüyorsa bir oturum öner: "En iyi şu durumda çalışırım..." ve "Şu durum beni zorluyor..." cümlelerini herkes sessizce yazsın, notlar kümelensin, ardından en önemli 5-8 alan nokta oylamasıyla seçilsin. Notlar verildiyse onları kullan.
3. Seçilen her alan için, gerektiğinde sayılar içeren 1-3 normu somut ve gözlemlenebilir davranışlar olarak yaz (ör. "incelemeler 4 iş saati içinde üstlenilir", "ortak saatler İstanbul 10:00-13:00 / Berlin 09:00-12:00").
4. Her normu test et: Yeni gelen biri uyulup uyulmadığını anlayabilir mi? Kurumsal politikaya ve çalışma süresine ilişkin yerel mevzuata uyuyor mu? Ekipteki her lokasyon ve rol için işliyor mu? Geçemeyen normları yeniden yaz veya çıkar.
5. Normlar arasındaki çatışmaları (ör. hızlı yanıt ile odaklanma süresi) her birinin ne zaman geçerli olduğunu tanımlayarak çöz; örneğin acil kanal istisnası olan odak blokları.
6. Ekip için bir karar kuralı (ör. rıza: gerekçeli bir itiraz yoksa ilerlenir) ve bir anlaşmazlık yolu ekle.
7. Sözleşmenin nasıl canlı tutulacağını tanımla: nerede duracağı, herkesin bir ihlali nazikçe nasıl dile getirebileceği ve bir gözden geçirme tetikleyicisi (her N iterasyonda, üye değişiminde veya bir norm tekrar tekrar çiğnendiğinde).
8. Bir sayfada tut; ayrıntılı prosedürleri bağlantılı dokümanlara taşı.
9. Çıkarım olan normları `[TASLAK – EKİP ONAYLAYACAK]` olarak işaretle ve açık soruları listele; sonraki gözden geçirme için `retrospective-facilitation`, sürtünmenin azalıp azalmadığını görmek için `team-health-check` öner.

## Çıktı formatı
```markdown
# Ekip Çalışma Sözleşmesi – <ekip>
Uzlaşma tarihi: <tarih veya [TBD]> · Sonraki gözden geçirme: <tetikleyici/tarih> · Üyeler: <roller/lokasyonlar>

## İletişim
- ...
## Erişilebilirlik ve Ortak Saatler
- ...
## Kod İncelemesi ve İş Birliği
- ...
## Toplantılar
- ...
## Kararlar ve Anlaşmazlık
- ...
## Destek / Nöbet
- ...
## Geri Bildirim ve Çatışma
- ...

## Sözleşmeyi Canlı Tutmak
- İhlali dile getirme: ...
- Gözden geçirme tetikleyicisi: ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her norm belirtilen bir sürtünmeye veya hedefe yanıt veriyor.
- [ ] Normlar somut ve gözlemlenebilir; gerektiğinde sayı veya koşul içeriyor.
- [ ] Normlar ekipteki tüm lokasyonlar, saat dilimleri ve roller için işliyor.
- [ ] Hiçbir norm kurumsal politika veya çalışma süresi kurallarıyla çelişmiyor; çelişkiler işaretlendi.
- [ ] Ekibin onaylamadığı normlar `[TASLAK – EKİP ONAYLAYACAK]` olarak işaretli.
- [ ] Bir gözden geçirme tetikleyicisi ve ihlali dile getirme yolu var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Davranış yerine değer yazmak ("birbirimize saygı duyarız"). Bunu insanların gerçekten yapacağı şeyle değiştir.
- Sözleşmeyi bir yöneticinin dayatması. Yalnızca ekip şekillendirip onayladığında işe yarar.
- Bir kez yazıp unutmak. Ekip veya sürtünmeleri değiştiğinde gözden geçir.

## Örnek
Girdi: İstanbul ve Berlin'de üyeler; incelemeler günlerce bekliyor; gece mesajları.

Çıktıdan bir bölüm:
- Zayıf norm: "Hızlı yanıt verin." Güçlü norm: "Pull request'ler inceleyenin saat dilimine göre 4 iş saati içinde üstlenilir; mümkün değilse inceleyen bunu söyler ve başka birini önerir."
- Erişilebilirlik: ortak saatler İstanbul 10:00-13:00 (Berlin 09:00-12:00) `[TASLAK – EKİP ONAYLAYACAK]`; kişinin kendi mesaisi dışında mesajlar zamanlanmış gönderilir, acil kanal yalnızca üretim olayları için kullanılır.
