---
description: "Bir ekibin Hazır Tanımını (DoR) oluşturur veya revize eder: ekibin bir iş maddesini taahhüt etmeden veya başlatmadan önce aranan giriş kriterlerini madde türlerine göre uyarlar, her kriterin nasıl kontrol edileceğini ve hangi durumlarda istisna yapılabileceğini belirtir. Ekip belirsiz işlere başlayıp takıldığında, planlama eksik bilgi yüzünden durduğunda ya da DoR, hazır olma kriterleri veya giriş kontrol listesi istendiğinde kullanılır."
related: "definition-of-done, backlog-refinement, invest-check, acceptance-criteria, working-agreement"
prompt: "Ekibimiz için bir Hazır Tanımı yaz; B2B bir web portalı geliştiriyoruz ve sürekli eksik API sözleşmeleri ve UX tasarımları yüzünden takılıyoruz."
---

# Hazır Tanımı (DoR) Oluşturma

## Amaç
Ekibe, belirsiz veya engelli işlerin başlatılmasını önleyen, kısa ve üzerinde anlaşılmış bir giriş kriterleri seti vermek; bunu yaparken hazır olmayı bürokratik bir geçiş kapısına dönüştürmemek.

## Ne zaman kullanılır
- İş maddeleri başlarken eksik bilgi yüzünden sık sık engelleniyor veya yeniden yapılıyorsa.
- Yeni bir ekip çalışma sözleşmelerini oluşturuyorsa.
- İyileştirme veya planlama oturumları hep aynı eksik girdiler yüzünden tıkanıyorsa.
- Mevcut bir DoR göz ardı ediliyorsa veya fazla uzamışsa.

## Ne zaman kullanılmaz
- İşin ne zaman tamamlandığı tanımlanacaksa `definition-of-done` kullanılır.
- Tek bir hikayenin kalitesi kontrol edilecekse `invest-check` kullanılır.
- Daha geniş ekip normları üzerinde anlaşılacaksa `working-agreement` kullanılır.

## Girdiler
Zorunlu:
- Ekip bağlamı: ekibin ne geliştirdiği ve engellenen veya belirsiz işlerin tekrarlayan nedenleri. Yoksa en önemli 2-3 sorunu sor; çözeceği bir sorun olmayan DoR genel geçer kalır.

İsteğe bağlı, kaliteyi artırır:
- Mevcut DoR, DoD, iş maddesi türleri (hikaye, hata, spike, teknik madde).
- Diğer ekiplere bağımlılıklar (UX, API sağlayıcıları, veri, güvenlik).
- Yasal veya uyum ihtiyaçları (ör. KVKK/GDPR veri sınıflandırması).

## Süreç
1. Gözlemlenen hata biçimlerini listele (tasarım yüzünden engel, eksik API sözleşmesi, belirsiz kabul, test verisi yok) ve her birini bir aday kritere eşle.
2. Tüm maddelere uygulanan minimal bir çekirdekle başla: değer belirtilmiş, kabul kriterleri test edilebilir, bir iterasyona/sprint'e veya birkaç günlük akışa sığacak kadar küçük, bağımlılıklar belirlenmiş, engelleyici açık soru yok.
3. Türe özel kriterleri yalnızca hata yaşanan yerlere ekle (ör. hikaye: arayüz değişiyorsa UX hazır; entegrasyon: sözleşme üzerinde anlaşılmış; hata: tekrarlanabilir adımlar ve ortam; spike: soru ve süre sınırı).
4. Her kriteri evet/hayır kontrolü olarak yaz; kimin ne zaman doğrulayacağını belirt (iyileştirme, planlama öncesi, çekme anı).
5. Çekirdek listeyi 5-8 kriterde tut; olsa iyi olurları rehber bölümüne taşı.
6. İstisna kuralını tanımla: hazır olmayan bir madde hangi durumda yine de çekilebilir (ör. acil düzeltme, ürün sahibinin açıkça kabul ettiği risk) ve nasıl etiketlenir.
7. DoR'un nasıl gözden geçirileceğini (ör. retrospektiflerde, birkaç iterasyonda bir) ve çok katı olduğunu gösteren sinyali (maddelerin yalnızca hazır olma yüzünden uzun beklemesi) tanımla.
8. DoR'u ekibin panosuna veya wiki'sine yapıştırabileceği tek sayfalık bir belge olarak yaz.
9. Kullanıcının hedefi devam ediyorsa eşleşen çıkış kriterleri için `definition-of-done`, mevcut maddeleri yeni DoR'a göre sınamak için `invest-check` öner.

## Çıktı formatı
```markdown
# Hazır Tanımı – <ekip>
Sürüm: <n> · Anlaşma tarihi: <tarih veya [TBD]> · Gözden geçirme sıklığı: <sıklık>

## Çekirdek Kriterler (tüm maddeler)
| # | Kriter (evet/hayır) | Kontrol eden | Ne zaman |
|---|---|---|---|
| 1 | Değer ve hedef kullanıcı belirtilmiş | Ürün sahibi | İyileştirme |

## Türe Özel Kriterler
- Arayüz değişikliği içeren hikaye: <kriter>
- Entegrasyon/API: <kriter>
- Hata: <kriter>
- Spike: <kriter>

## İstisnalar
<hazır olmayan maddenin ne zaman başlayabileceği, riski kimin kabul ettiği, nasıl etiketlendiği>

## Bu DoR'un Çözdüğü Sorunlar
- <hata biçimi> → kriter <#>

## Gözden Geçirme
<DoR'un ne zaman ve nasıl ele alınacağı; çok katı olduğunun sinyali>
```

## Kalite kontrol listesi
- [ ] Her kriter doğrulanabilir bir evet/hayır ifadesi.
- [ ] Her kriter gerçek bir soruna veya açıkça gerekçelendirilmiş bir temele dayanıyor.
- [ ] Çekirdek listede en fazla 8 kriter var.
- [ ] DoR'un acil işi engellememesi için bir istisna kuralı var.
- [ ] Hiçbir kriter Bitti Tanımını tekrar etmiyor.
- [ ] Tarihler ve anlaşma durumu ekip onaylayana kadar `[TBD]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- DoR'u şelale tarzı bir geçiş kapısına çevirmek ("tüm spesifikasyon onaylandı"). Hazır olmak, her şeyin bilinmesi değil, güvenle başlamaya yetecek bilginin olmasıdır.
- Ekip tahmin yapmıyorken tahmini kriter olarak istemek. Bunun yerine "yeterince küçük" kullan.
- DoR'u ekiple birlikte değil ekip adına yazmak. Ekibin üzerinde anlaşacağı bir taslak olarak sun.

## Örnek
Girdi: "B2B portal ekibi, eksik API sözleşmeleri ve geç gelen UX tasarımları yüzünden takılıyor."

Çıktıdan bir bölüm:
| 4 | Başka bir ekibin API'sini kullanan maddelerde sözleşme (endpoint'ler, veri yapıları, hata kodları) üzerinde anlaşılmış ve sürümlenmiş | Geliştirici + sağlayıcı ekip | Planlama öncesi |
| 5 | Arayüzü değiştiren maddelerde tasarım hazır ve bir geliştiriciyle gözden geçirilmiş | Ürün sahibi + tasarımcı | İyileştirme |
- İstisnalar: Hazır olmayan bir madde yalnızca ürün sahibi kabul edilen riski madde üzerine yazıp "hazır-olmadan-başladı" etiketi eklerse başlayabilir.
