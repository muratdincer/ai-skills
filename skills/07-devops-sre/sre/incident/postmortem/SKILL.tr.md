---
description: Olay notlarından, sohbet loglarından, alarmlardan ve zaman çizelgelerinden suçlamasız bir olay sonrası analiz (postmortem) yazar: özet, müşteri ve iş etkisi, zaman damgalı zaman çizelgesi, tespit ve müdahale analizi, tetikleyicinin ötesine izlenen katkıda bulunan etkenler ve kök nedenler, iyi gidenler ve sorumlu ile tarihleri belli önceliklendirilmiş düzeltici aksiyonlar. Bir olay çözüldükten sonra, bir SLO ihlali veya kıl payı atlatılan bir durum resmi incelemeyi gerektirdiğinde ya da taslak bir postmortem'in suçlamasız ve uygulanabilir hale getirilmesi gerektiğinde kullanılır.
related: incident-response, incident-communication, runbook, error-budget-policy, alert-design
prompt: Dün geceki ödeme kesintisinin sohbet logu ve alarm geçmişi ekte. Zaman çizelgesi, kök nedenler ve aksiyon maddeleriyle suçlamasız bir postmortem yaz.
---

# Suçlamasız Olay Sonrası Analiz

## Amaç
Bir olayı kalıcı bir öğrenmeye dönüştürmek: ne olduğunun doğru bir anlatımı, sistemin buna neden izin verdiği ve tekrarı daha az olası ya da daha az zararlı kılan, sahibi belli az sayıda aksiyon. Suçlamasız olmak, kimin hata yaptığına değil, koşullara ve kararların o anki bağlamına odaklanmak demektir.

## Ne zaman kullanılır
- Olay hafifletildi ve ekibin inceleme dokümanına ihtiyacı var.
- Bir SLO ihlal edildi, hata bütçesi tüketildi veya kıl payı atlatılan bir durumdan ders çıkarılmalı.
- Taslak bir postmortem kişileri suçluyor veya uygulanabilir takip aksiyonları içermiyor ve yeniden yazılmalı.

## Ne zaman kullanılmaz
- Olay hâlâ sürüyorsa `incident-response` kullanılır.
- İhtiyaç olay sırasında müşterilere veya paydaşlara durum güncellemesiyse `incident-communication` kullanılır.
- Olay değil genel bir proje değerlendirmesiyse `lessons-learned` veya `retrospective-facilitation` kullanılır.

## Girdiler
Zorunlu:
- Olay materyali: zaman çizelgesi notları, sohbet veya köprü (bridge) logu, alarmlar ya da ne olduğunu ve nasıl çözüldüğünü anlatan yazılı bir açıklama.

İsteğe bağlı, kaliteyi artırır:
- Metrikler ve panolar, deployment ve değişiklik geçmişi, müşteri etki verisi (etkilenen kullanıcılar, başarısız işlemler), SLO ve hata bütçesi verisi.
- Mevcut aksiyon maddeleri, önem derecesi tanımları, kurumun postmortem şablonu.

Olay materyali yoksa iste. Eksik zaman damgaları veya sayılar `[BİLİNMİYOR]` olarak işaretlenir, asla olgu gibi tahmin edilmez.

## Süreç
1. Olgusal bir özet yaz: ne bozuldu, kimi etkiledi, ne kadar sürdü, nasıl hafifletildi; kurumun ölçeğine göre önem derecesi.
2. Etkiyi yalnızca veriden sayısallaştır: süre (başlangıç, tespit, hafifletme, çözüm), etkilenen kullanıcılar veya istekler, başarısız işlemler, tüketilen SLO ve hata bütçesi, veri kaybı, sözleşmesel veya yasal sonuçlar. Bilinmeyenleri işaretle.
3. Zaman dilimini belirterek zaman damgalı zaman çizelgesini kur: ilk tetikleyici, ilk belirti, tespit, eskalasyon, önemli kararlar, hafifletme, toparlanma, olayın kapanışı. Her kaydı kaynağıyla etiketle.
4. Müdahale metriklerini hesapla ve yorumla: tespit süresi, devreye girme süresi, hafifletme süresi, çözüm süresi; zamanın nerede kaybedildiğini belirle.
5. Nedenleri tetikleyicinin ötesinde analiz et: değişiklik veya koşul neden zarara yol açtı, neden daha erken yakalanmadı (testler, review, canary), tespit neden bu kadar sürdü, toparlanma neden yavaştı. Yapılandırılmış bir yöntem kullan (ör. her dal için beş neden veya katkıda bulunan etkenler ağacı); tek bir kök neden değil, birden çok katkıda bulunan etken bekle.
6. Suçlayıcı her ifadeyi sistem terimleriyle yeniden yaz ("X hatalı yapılandırma gönderdi" yerine "deploy aracı doğrulama olmadan yapılandırma değişikliğine izin verdi"). Anlatımdan isimleri çıkar; rollere atıf yap.
7. İyi gidenleri ve ekibin şanslı olduğu yerleri kaydet; şans gizli bir risktir.
8. Düzeltici aksiyonları kategorilere göre tanımla: önleme, tespit, hafifletme, süreç. Her biri somut olsun; sorumlu rolü, önceliği, verilmemişse `[TBD]` olarak bitiş tarihi ve tamamlandığını doğrulama yolu bulunsun. Çok sayıda küçük aksiyon yerine az sayıda yüksek etkili aksiyonu tercih et.
9. Açık soruları ve takip incelemelerini listele; doğrulanmış olguları `[VARSAYIM]` olarak etiketlenen çıkarımlardan ayır.
10. Hedef devam ediyorsa hafifletmeyi belgelemek için `runbook`, tespit açıkları için `alert-design`, SLO sonuçları bir karar gerektiriyorsa `error-budget-policy` öner.

## Çıktı formatı
```markdown
# Postmortem: <olay başlığı> (<tarih>)
Önem: <seviye> · Durum: Taslak/İncelendi · Yazanlar: <roller> · Suçlamasız: evet

## Özet
<3-5 cümle>

## Etki
| Ölçü | Değer | Kaynak |
|---|---|---|
| Süre (başlangıç → çözüm) | | |
| Etkilenen kullanıcılar / istekler | | |
| Tüketilen SLO / hata bütçesi | | |

## Zaman Çizelgesi (<zaman dilimi>)
| Zaman | Olay | Kaynak |
|---|---|---|

## Müdahale Metrikleri
| Tespit süresi | Devreye girme süresi | Hafifletme süresi | Çözüm süresi |
|---|---|---|---|

## Katkıda Bulunan Etkenler ve Kök Nedenler
- Tetikleyici: ...
- Neden zarara yol açtı: ...
- Neden daha erken yakalanmadı: ...
- Tespit/toparlanma neden bu kadar sürdü: ...

## İyi Gidenler / Şanslı Olduğumuz Yerler
## Düzeltici Aksiyonlar
| # | Aksiyon | Kategori | Sorumlu rol | Öncelik | Bitiş | Doğrulama |
|---|---|---|---|---|---|---|

## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her zaman damgası ve etki sayısı verilen materyalden geliyor ya da `[BİLİNMİYOR]` olarak işaretli.
- [ ] Anlatım kişileri değil rolleri ve sistemleri adlandırıyor, suçlayıcı ifade içermiyor.
- [ ] Nedenler tetikleyicinin ötesine geçiyor; neden önlenmediğini, neden daha erken tespit edilmediğini ve neden daha hızlı toparlanılmadığını kapsıyor.
- [ ] Her düzeltici aksiyon somut, sahipli, önceliklendirilmiş ve doğrulanabilir; hiçbiri "daha dikkatli ol" değil.
- [ ] Olgular ve çıkarımlar ayrıldı; çıkarımlar `[VARSAYIM]` olarak etiketli.
- [ ] Loglardaki kişisel veya müşteri verileri maskelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "İnsan hatası"nda durmak. Hatayı neyin mümkün ve kolay kıldığını sor ve o koşulu düzelt.
- Hiç yapılmayacak uzun, düşük değerli aksiyon listeleri. En büyük katkıda bulunan etkenleri ele alan birkaç aksiyon seç.
- Zaman çizelgesini sonradan bilinenlerle yeniden yazmak. Müdahale edenlerin her an ne bildiğini kaydet; kararlarını bu açıklar.

## Örnek
Girdi: "22:10'da bir yapılandırma değişikliği ödeme ağ geçidi zaman aşımını 1 sn yaptı; hatalar arttı; 22:41'de alarm; 23:05'te rollback."

Zayıf: "Kök neden: mühendis yanlış zaman aşımı girdi. Aksiyon: yapılandırmalarda daha dikkatli olun."

Güçlü örnekten bir bölüm:
- Tetikleyici: bir yapılandırma değişikliği ağ geçidi zaman aşımını 1 sn'ye düşürdü.
- Neden zarara yol açtı: ağ geçidinin p99 gecikmesi zirvede 1 sn'nin üzerinde `[VARSAYIM: metriklerden teyit et]`, bu yüzden ödemelerin bir kısmı zaman aşımına uğradı.
- Neden yakalanmadı: yapılandırma değişiklikleri, kod deploy'larında kullanılan canary aşamasını atlıyor.
- Tespit neden 31 dk sürdü: alarm 15 dk boyunca %10 hata oranında tetikleniyor; hata oranı %6 civarında kaldı.
| # | Aksiyon | Kategori | Sorumlu rol | Öncelik | Doğrulama |
|---|---|---|---|---|---|
| 1 | Yapılandırma değişikliklerini kodla aynı canary ve otomatik rollback'ten geçir | Önleme | Platform lideri | Yüksek | Staging'de test değişikliği otomatik geri alındı |
| 2 | Ödeme başarı SLO'su için burn-rate alarmı ekle | Tespit | SRE | Yüksek | Bu olayın yeniden oynatımında alarm tetikleniyor |
