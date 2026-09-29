---
description: "Sistem davranışını fonksiyon bazında tanımlayan bir Fonksiyonel Gereksinim Dokümanı (FRD) yazar: aktörler ve yetkiler, tetikleyiciler, doğrulamalarıyla girdiler, işleme ve iş kuralları, çıktılar, durumlar, hata yönetimi ve arayüzler; her gereksinim benzersiz ID'li, test edilebilir ve bir iş ihtiyacına izlenebilir. İş gereksinimleri uzlaşılmışsa ve geliştirme ekibi veya tedarikçi belirsizlik içermeyen bir davranış tanımına ihtiyaç duyuyorsa ya da 'FRD yaz' dendiğinde kullanılır."
related: "brd-writing, use-case-spec, business-rules-catalog, nfr-specification, traceability-matrix"
prompt: "Bu BRD'ye dayanarak tedarikçi self-servis kayıt ve doküman doğrulama fonksiyonları için FRD yaz."
---

# Fonksiyonel Gereksinim Dokümanı (FRD) Yazma

## Amaç
Sistemin ne yapması gerektiğini, geliştiricilerin tahmin yürütmeden geliştirebileceği ve test uzmanlarının doğrulayabileceği kesinlikte tanımlamak; bunu yaparken karşıladığı iş gereksinimlerine izlenebilirliği korumak.

## Ne zaman kullanılır
- İş gereksinimleri uzlaşılmış ve sistem davranışına çevrilmesi gerekiyorsa.
- Bir tedarikçi, dış kaynak ekip veya paket konfigürasyonu sözleşmeye esas fonksiyonel bir temel istiyorsa.
- Birden çok ekip aynı yeteneğin parçalarını geliştiriyor ve tek bir davranış referansına ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- İş ihtiyacı ve hedefler henüz uzlaşılmamışsa `brd-writing` kullanılır.
- Tam bir ISO/IEC/IEEE 29148 tarzı sistem şartnamesi gerekiyorsa `srs-writing` kullanılır.
- Ekip backlog maddelerinden küçük artımlarla çalışıyorsa `user-story` ile `acceptance-criteria` kullanılır.

## Girdiler
Zorunlu:
- İş gereksinimleri (BRD, özellik özeti veya eşdeğeri) ve kapsamdaki fonksiyonlar.

İsteğe bağlı, kaliteyi artırır:
- Süreç modelleri, iş kuralları, veri modeli, ekran taslakları, arayüz tarifleri, mevcut sistem davranışı.
- Numaralandırma kuralları ve kurumun FRD şablonu.

İş gereksinimleri yoksa bunları veya fonksiyonların tarifini iste; davranışı yalnızca bir çözüm fikrinden türetme. Bir seferde en fazla 5 engelleyici soru sor.

## Süreç
1. Kapsamdaki fonksiyonları fiil + nesne olarak listele ("Tedarikçi kaydet", "Doküman doğrula") ve her birini hizmet ettiği iş gereksinimlerine eşle.
2. Aktörleri ve rolleri, bir de yetki matrisini tanımla: her fonksiyonda hangi rol görüntüleyebilir, oluşturabilir, değiştirebilir, onaylayabilir, silebilir.
3. Her fonksiyon için belirle: tetikleyici, ön koşullar, ana davranış, alternatif davranış, son koşullar (başarı ve hata).
4. Girdileri tanımla: alanlar, tip, format, zorunlu/isteğe bağlı, varsayılan değer, doğrulama kuralı ve kesin hata davranışı. Varlıkları yeniden tanımlamak yerine veri sözlüğüne atıf yap.
5. İşlemeyi tanımla: hesaplamalar, kural atıfları (BR-ID), durum değişiklikleri, idempotency ve mükerrer kayıt veya eşzamanlı düzenlemede ne olacağı.
6. Çıktıları tanımla: ekranlar veya mesajlar, dokümanlar, bildirimler (alıcı, tetikleyici, içerik), yazılan kayıtlar, denetim kayıtları.
7. Dokunulan arayüzleri tanımla: sistem, yön, veri, zamanlama ve karşı sistem erişilemezken davranış.
8. Her gereksinimi "Sistem ... yapmalıdır" biçiminde yaz; benzersiz ID, cümle başına tek davranış, öncelik ve kaynak bağlantısı ver. Muğlak terimlerden ("kullanıcı dostu", "hızlı", "vb.") kaçın.
9. İlgili NFR'leri (performans, güvenlik, erişilebilirlik) fonksiyonel cümlelere karıştırmadan atıfla ekle.
10. Her boşluğu `[TBD]`, her yorumu `[VARSAYIM]` olarak işaretle; bunları sahibiyle birlikte açık sorularda topla.
11. İzlenebilirlik tablosunu kur: iş gereksinimi → fonksiyonel gereksinimler → (sonra) test senaryoları.
12. Hedef devam ediyorsa karmaşık akışlar için `use-case-spec`, kalite nitelikleri için `nfr-specification`, testleri bağlamak için `traceability-matrix` öner.

## Çıktı formatı
```markdown
# Fonksiyonel Gereksinim Dokümanı: <sistem / sürüm>
Sürüm: <x.y> · Durum: Taslak · Dayanak: <BRD id/sürüm>

## 1. Kapsam ve Fonksiyonlar
| Fonksiyon | Açıklama | İş gereksinim(ler)i |
## 2. Aktörler ve Yetkiler
| Fonksiyon | Rol A | Rol B | ... |  (G/O/D/Ö/S)
## 3. Fonksiyonel Gereksinimler
### F-01 <fonksiyon>
- Tetikleyici / Ön koşullar / Son koşullar
| ID | Gereksinim ("Sistem … yapmalıdır") | Kural atfı | Öncelik | Kaynak |
- Girdiler ve doğrulamalar: | Alan | Tip | Zorunlu | Doğrulama | Hata davranışı |
- Çıktılar ve bildirimler
- Hatalar ve istisnalar
## 4. Arayüzler
## 5. Atıf Yapılan NFR'ler
## 6. İzlenebilirlik (İG → FG)
## 7. Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her fonksiyonel gereksinimin benzersiz ID'si, tek davranışı ve kaynak bağlantısı var.
- [ ] Her fonksiyonun ön koşulları, son koşulları ve hata davranışı var.
- [ ] Her girdi alanının doğrulama kuralı ve tanımlı hata davranışı var.
- [ ] Yetkiler rol ve fonksiyon bazında tanımlı.
- [ ] Muğlak terim kalmadı; her cümle test edilebilir.
- [ ] Kapsamdaki her iş gereksinimi en az bir fonksiyonel gereksinime eşleniyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca mutlu yolu anlatmak. Hataların çoğu ret, zaman aşımı, mükerrer kayıt ve kısmi hata durumlarından gelir; bunları tanımla.
- Arayüz tasarımını gömmek ("sağda mavi bir düğme"). Davranışı ve bilgiyi tanımla; yerleşimi ekran gereksinimlerine bırak.
- Birleşik gereksinimler ("doğrulamalı, kaydetmeli ve bildirmelidir"). Her biri test edilip izlenebilsin diye böl.

## Örnek
Girdi: İG-04 "Zorunlu dokümanlar doğrulanana kadar tedarikçi aktivasyonunu engelle."

Çıktıdan bir bölüm:
| ID | Gereksinim | Kural atfı | Öncelik | Kaynak |
|---|---|---|---|---|
| FG-4.1 | Sistem, zorunlu dokümanlardan biri eksik veya doğrulanmamışken tedarikçiyi "Doğrulama bekliyor" durumunda tutmalıdır. | BR-17 | Must | İG-04 |
| FG-4.2 | Sistem, "Doğrulama bekliyor" durumundaki bir tedarikçi için gelen aktivasyon isteğini reddetmeli ve doğrulanmamış dokümanların listesini göstermelidir. | BR-17 | Must | İG-04 |
| FG-4.3 | Sistem, her dokümanı kimin ve ne zaman doğruladığını kaydetmelidir. | – | Must | İG-04, denetim |

Açık soru: Tedarikçi tipine göre hangi dokümanlar zorunlu? `[TBD]` – Satın alma.
