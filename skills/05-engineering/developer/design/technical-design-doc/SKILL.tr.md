---
name: technical-design-doc
description: "Değişikliğin büyüklüğüne uygun olarak problem, hedefler ve hedef dışı konular, önerilen tasarım, alternatifler, yayına alma, riskler ve açık soruları kapsayan bir teknik tasarım dokümanı (RFC) yazar. Bir özellik veya değişiklik kodlamadan önce incelenmesi gerekecek kadar büyük, riskli ya da ekipler arası olduğunda veya RFC, tasarım dokümanı ya da teknik öneri istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: design
  title: "Teknik tasarım dokümanı (RFC)"
  related: "adr, solution-architecture-document, task-breakdown, api-contract, trade-off-analysis"
  prompt: "Sipariş onay e-postalarını checkout isteği içinde senkron göndermek yerine outbox ve arka plan worker'ı ile göndermek için bir tasarım dokümanı yaz."
---

# Teknik Tasarım Dokümanı (RFC)

## Amaç
Kod yazılmadan önce ekip arkadaşlarının yaklaşımı sorgulayabileceği, incelenebilir bir tasarım dokümanı üretmek. Böylece pahalı hatalar (yanlış veri modeli, güvensiz yayına alma, gözden kaçan bağımlılık) üretimde değil kâğıt üzerinde yakalanır.

## Ne zaman kullanılır
- Değişiklik birden fazla bileşeni, ekibi, veri deposunu veya dışa açık sözleşmeyi etkiliyorsa.
- Değişikliğin geri alınması zorsa: şema değişikliği, veri taşıma, yeni dış bağımlılık, protokol değişikliği.
- İnceleyenler veya liderler "bunun tasarımı var mı?" diye soruyorsa ya da bir RFC süreci varsa.
- İki veya daha fazla uygulanabilir yaklaşım varsa ve seçimin yazılı gerekçesi gerekiyorsa.

## Ne zaman kullanılmaz
- Tek bir mimari kararın kaydı gerekiyorsa `adr` kullanılır.
- Bütün bir çözüm veya program için sistem düzeyinde mimari gerekiyorsa `solution-architecture-document` kullanılır.
- Bir bilinmeyenin süre sınırlı araştırması gerekiyorsa önce `spike-report`, ardından bu skill kullanılır.

## Girdiler
Zorunlu:
- Problem veya gereksinim (hikaye, kayıt, olay, talep) ve sistemin etkilenen bölümü.

İsteğe bağlı, kaliteyi artırır:
- Mevcut mimari notları, ilgili kod veya şemalar, trafik ve veri hacimleri.
- Kısıtlar: son tarih, ekip büyüklüğü, platform standartları, uyum kuralları.
- Bilinen alternatifler veya tercih edilen yaklaşım.

Problem tanımı yoksa iste. Diğer her şey `[BİLİNMİYOR]` ya da açık soru olarak yazılır.

## Süreç
1. Problemi 2-4 cümlede yeniden ifade et; neden şimdi yapılması gerektiğini ve hiçbir şey yapmamanın maliyetini ekle.
2. Hedefleri ve açıkça hedef dışı olanları yaz. Hedef dışı maddeler incelemede kapsamın kaymasını önler.
3. Mevcut durumu kısaca anlat: bileşenler, veri akışı, sorunlu noktalar. Boşlukları `[BİLİNMİYOR]` olarak işaretle.
4. Önerilen tasarımı anlat: bileşenler ve sorumlulukları, veri modeli değişiklikleri, arayüzler/sözleşmeler, ana akışın ve ana hata akışının sırası.
5. Geçerli olan kesişen konuları ele al: tutarlılık ve idempotency, eşzamanlılık, güvenlik ve yetkilendirme, gizlilik (kişisel veriyi maskele/azalt), gözlemlenebilirlik, performans ve kapasite, maliyet.
6. "Hiçbir şey yapmamak" veya "asgari değişiklik" dahil en az iki alternatifi, neden reddedildikleriyle birlikte listele.
7. Yayına almayı planla: feature flag'ler, taşıma sırası (şemalar için expand-migrate-contract), geriye dönük uyumluluk, rollback yolu ve rollback kısmi kalırsa veri onarımı.
8. Başarının nasıl doğrulanacağını tanımla: testler, metrikler, SLO etkisi, yayın sonrası kabul sinyalleri.
9. Riskleri olasılık/etki ve azaltma önlemiyle, ardından açık soruları sorumlusuyla listele.
10. Dokümanı değişikliğe göre ölçekle: orta büyüklükte bir değişiklik için bir-iki sayfa; gerçekten geçerli olmayan bölümleri tek satırla belirterek atla.
11. Hedef devam ediyorsa her önemli karar için `adr`, yeni arayüzler için `api-contract` ve uygulamayı planlamak için `task-breakdown` öner.

## Çıktı formatı
```markdown
# RFC: <başlık>
Durum: Taslak | İncelemede | Kabul edildi | Reddedildi · Yazar: <ad> · İnceleyenler: <adlar veya [TBD]> · Tarih: <tarih>

## 1. Problem ve Bağlam
## 2. Hedefler / Hedef Dışı
## 3. Mevcut Durum
## 4. Önerilen Tasarım
### 4.1 Bileşenler ve Sorumluluklar
### 4.2 Veri Modeli Değişiklikleri
### 4.3 Arayüzler ve Sözleşmeler
### 4.4 Ana Akış ve Hata Akışı (sıralama)
## 5. Kesişen Konular (güvenlik, gizlilik, tutarlılık, gözlemlenebilirlik, performans, maliyet)
## 6. Değerlendirilen Alternatifler
| Seçenek | Artılar | Eksiler | Neden seçilmedi |
## 7. Yayına Alma, Taşıma ve Rollback
## 8. Doğrulama ve Başarı Metrikleri
## 9. Riskler
| Risk | Olasılık | Etki | Azaltma |
## 10. Açık Sorular
1. <soru> — <sorumlu> — <gereken tarih>
```

## Kalite kontrol listesi
- [ ] Problem ve hedefler seçilen çözüme atıf yapmadan yazıldı.
- [ ] En az iki gerçek alternatif red gerekçesiyle karşılaştırıldı.
- [ ] Yalnızca mutlu yol değil, hata yolu da tasarlandı (zaman aşımı, yeniden deneme, mükerrer mesaj, kısmi hata).
- [ ] Yayına alma geri alınabilir ya da geri alınamayan adım açıkça belirtildi.
- [ ] Hacim, SLA veya tarih uydurulmadı; bilinmeyenler `[BİLİNMİYOR]`, çıkarımlar `[VARSAYIM]` olarak işaretlendi.
- [ ] İnceleyen kişi onaylaması istenen kararı bir dakika içinde bulabiliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tasarım yerine kod turu yazmak. Sorumluluklar, sözleşmeler ve veri düzeyinde kal; kodu pull request'e bırak.
- Göstermelik alternatifler. Her alternatif yetkin bir mühendisin gerçekten seçebileceği bir seçenek olmalı.
- Mevcut verinin ve işlemdeki isteklerin taşınmasını yok saymak. Geçiş dönemini mutlaka anlat.
- İnceleme sonrası dokümanı sahipsiz bırakmak. Nihai durumu kaydet, ortaya çıkan ADR'lere bağlantı ver.

## Örnek
Girdi: "Checkout onay e-postasını istek içinde gönderiyor; SMTP zaman aşımları sipariş isteğini başarısız yapıyor."

Çıktıdan bir bölüm:
- Hedef: Sipariş oluşturmanın başarısı e-posta sağlayıcısının erişilebilirliğine bağlı olmamalı. Hedef dışı: e-posta şablonlarını değiştirmek.
- Önerilen tasarım: Siparişle aynı transaction içinde bir `outbox` satırı yazılır; worker bu satırı `order_id + template` idempotency anahtarıyla yayınlar ve gönderir.
- Reddedilen alternatif: Commit sonrası "gönder ve unut" async çağrı; süreç commit ile gönderim arasında çökerse mesaj kaybolur.
- Yayına alma: Tenant bazında `email.outbox` flag'i; rollback = flag kapatılır, worker kalan satırları boşaltır.
- Açık soru: Kabul edilebilir teslim gecikmesi nedir? `[BİLİNMİYOR]` — ürün sahibi.
