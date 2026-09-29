---
name: technical-onboarding
description: "Ekibe katılan bir geliştirici için teknik oryantasyon planı hazırlar: doğrulama adımlı ortam kurulumu, rehberli kod tabanı ve mimari turu, çalışma biçimi, giderek zorlaşan ilk işler, kilit kişiler ve kontrol noktaları; hepsini kişinin deneyimine ve rolüne göre uyarlar. Yeni veya başka ekipten gelen bir geliştirici başladığında, teknik liderin yeni gelen için ilk haftaları hazırlaması gerektiğinde ya da mevcut oryantasyon çok yavaş olduğu için yeniden yapılandırılacağında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: tech-lead
  area: leadership
  title: "Geliştirici oryantasyonu"
  related: "onboarding-plan-30-60-90, readme-writing, legacy-code-comprehension, coding-standards, onboarding-guide"
  prompt: "Pazartesi ödeme ekibimize orta seviye bir backend geliştirici katılıyor. Kurulum ve ilk işler dahil ilk iki hafta için teknik oryantasyon planı hazırla."
---

# Geliştirici Oryantasyonu

## Amaç
Yeni geliştiricinin hızlı ve güvenli biçimde, gözden geçirilmiş ilk anlamlı değişikliğini üretime çıkarmasını sağlamak ve bağımsız çalışması için gereken sistem zihinsel modelini kurmak. İyi bir oryantasyon verimliliğe ulaşma süresini ve ekibin geri kalanının yükünü azaltır.

## Ne zaman kullanılır
- Dışarıdan veya başka bir ekipten bir geliştirici ekibe katıldığında.
- Teknik liderin ilk bir-iki hafta için somut bir plana ihtiyacı olduğunda.
- Oryantasyon geri bildirimi, kurulumun günler sürdüğünü veya yeni gelenlerin uzun süre bağımlı kaldığını söylüyorsa.

## Ne zaman kullanılmaz
- Plan, teknik olmayan hedefler dahil üç aylık tüm rolü kapsıyorsa `onboarding-plan-30-60-90` kullanılır.
- İhtiyaç repository için genel dokümantasyonsa `readme-writing` kullanılır.
- Konu kurum genelindeki oryantasyon rehberiyse (İK, araçlar, politikalar) `onboarding-guide` kullanılır.

## Girdiler
Zorunlu:
- Ekip ve sistem bağlamı (ekibin sahip olduğu alanlar, ana teknolojiler) ve yeni gelenin rolü ile deneyim düzeyi.

İsteğe bağlı, kaliteyi artırır:
- Repository'ler, mimari dokümanlar, kurulum talimatları, kodlama standartları, bitti tanımı.
- Aday ilk işler, buddy/mentor, erişim talep süreci, güvenlik eğitimi gereklilikleri.
- Başlangıç tarihi ve planlı izinler.

Ekip bağlamı veya yeni gelenin seviyesi eksikse sor. En fazla beş soru sor; geri kalan her şey planda `[TBD]` olarak işaretlenir.

## Süreç
1. Dönem hedefini tanımla: ör. "5. güne kadar gözden geçirilmiş ilk değişiklik merge edilip deploy edildi, 2. haftanın sonunda küçük bir özelliğin sahibi". Deneyim düzeyine ve alan karmaşıklığına göre uyarla.
2. İlk gün gereken erişim ve hesapları (kaynak kod, pipeline, ortamlar, gözlemlenebilirlik, iş takibi, sohbet kanalları), her birini kimin verdiğini ve hazırlanma süresini listele; başlangıçtan önce talep et. Plana asla kimlik bilgisi yazma.
3. Ortam kurulumunu doğrulanabilir adımlar olarak yaz: her adım bir kontrolle biter ("testler yerelde geçiyor", "servis health endpoint'inde yanıt veriyor"). Kurulumda bulunan eksikleri dokümantasyon düzeltmesi olarak kaydet.
4. Mimari turunu planla: sistemin bağlam ve konteyner görünümü (C4 seviye 1-2), ana veri akışları, en önemli alan kavramları ve sözlük, riskli veya eski alanların yeri.
5. Kod tabanı turunu planla: repository yapısı, bir isteğin kod içinde nasıl aktığı, test yaklaşımı, build ve sürüm yolu, feature flag'ler, loglama ve panolar.
6. Çalışma biçimini açıkla: branch ve review kuralları, bitti tanımı, nöbet beklentileri, toplantı ritmi, kararların nasıl kaydedildiği.
7. İlk işleri artan zorlukta seç: (a) bir dokümantasyon veya kurulum düzeltmesi, (b) testleriyle birlikte küçük ve sınırları net bir hata veya değişiklik, (c) sistemin daha fazla kısmına dokunan bir özellik dilimi. Her birinin bitti kriteri ve adı belli bir gözden geçireni olsun.
8. Bir buddy ata ve kilit kişileri (ürün, mimari, operasyon, güvenlik) kime ne sorulacağıyla birlikte listele.
9. Kontrol noktalarını planla (1. gün sonu, 1. hafta sonu, 2. hafta sonu); ilerlemeyi ölçmek ve planı ayarlamak için soruları yaz.
10. Araçlar, kişiler ve tarihlerle ilgili her varsayımı `[VARSAYIM]` veya `[TBD]` olarak işaretle; hedef devam ediyorsa uzun vade için `onboarding-plan-30-60-90`, bulunan kurulum eksikleri için `readme-writing`, karmaşık alanlar için `legacy-code-comprehension` öner.

## Çıktı formatı
```markdown
# Teknik Oryantasyon: <ad/rol> · <ekip>
Başlangıç: <tarih> · Buddy: <ad veya [TBD]> · Hedef: <dönem için ölçülebilir hedef>

## İlk Günden Önce (Erişim)
| Erişim | Veren | Hazırlanma süresi | Durum |
|---|---|---|---|

## Ortam Kurulumu
1. <adım> — Doğrula: <kontrol>

## Mimari ve Kod Tabanı Turu
| Oturum | İçerik | Materyal | Sunan |
|---|---|---|---|

## Çalışma Biçimi
- ...

## İlk İşler
| # | İş | Neden bu | Bitti koşulu | Gözden geçiren |
|---|---|---|---|---|

## Kişiler
| Konu | Kişi/rol |
|---|---|

## Kontrol Noktaları
| Ne zaman | Sorular | Şu durumda ayarla |
|---|---|---|
```

## Kalite kontrol listesi
- [ ] Planın ölçülebilir bir hedefi var (ör. belirli bir güne kadar ilk değişiklik merge edilip deploy edildi).
- [ ] Her kurulum adımı bir doğrulama kontrolüyle bitiyor.
- [ ] İlk işlerin zorluğu artıyor ve her birinin bitti kriteri ve gözden geçireni var.
- [ ] Erişim talepleri sorumlu ve hazırlanma süresiyle listelendi; planda kimlik bilgisi yok.
- [ ] Kullanıcının vermediği adlar, tarihler ve araçlar `[TBD]` veya `[VARSAYIM]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Koda dokunmadan önce günlerce doküman okutmak. Okumayı erken aşamada küçük ve gerçek bir değişiklikle eşleştir.
- Acil veya kritik yoldaki bir işi ilk iş olarak vermek; yeni gelen baskı altında takılır. Sınırları net, acil olmayan işler seç.
- Erişim taleplerini ilk güne bırakmak; ilk hafta bloke olur. Başlangıç tarihinden önce talep et.

## Örnek
Girdi: "Pazartesi ödeme ekibine orta seviye backend geliştirici katılıyor; .NET servisleri, mesaj kuyruğu, Kubernetes."

Çıktıdan bir bölüm:
- Hedef: 5. güne kadar gözden geçirilmiş ilk değişiklik üretimde; 2. haftanın sonunda küçük bir iade raporu özelliğinin sahibi.
| # | İş | Neden bu | Bitti koşulu | Gözden geçiren |
|---|---|---|---|---|
| 1 | Yerel kurulum rehberindeki eskimiş adımları düzelt | Kurulum zorluğunu girdi olarak kullanır | Rehber güncellendi ve merge edildi | Buddy |
| 2 | İade tutarı için eksik doğrulamayı testleriyle ekle | Küçük, API ve alan katmanına dokunuyor | Merge edildi, deploy edildi, 24 saat alarmsız | Teknik lider |
