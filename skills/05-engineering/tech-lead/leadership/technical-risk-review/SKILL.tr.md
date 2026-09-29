---
name: technical-risk-review
description: "Bir özellik, proje veya sürüm planı için yapılandırılmış bir teknik risk incelemesi yapar: mimari, bağımlılıklar, teknoloji yeniliği, veri, entegrasyon, performans, güvenlik, işletilebilirlik, yetkinlik ve takvim boyunca teslimat ve kalite risklerini belirler, olasılık ve etkiyi puanlar, erken uyarı sinyallerini adlandırır, sorumlularıyla azaltma aksiyonlarını ve riski en ucuza düşüren deneyleri önerir. Başlangıçta veya bir plana taahhüt vermeden önce, büyük bir sürümden önce, proje uyarı işaretleri gösterdiğinde veya paydaşlar teknik olarak neyin ters gidebileceğini sorduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: tech-lead
  area: leadership
  title: "Teknik risk incelemesi"
  related: "risk-register, technical-estimation, spike-report, threat-model, architecture-review"
  prompt: "Fatura üretimini olay güdümlü bir servise taşıyacağımız 3 aylık bir projeye başlıyoruz. Plana taahhüt vermeden önce teknik riskleri incele."
---

# Teknik Risk İncelemesi

## Amaç
Teslimatı veya kaliteyi raydan çıkarabilecek teknik riskleri, harekete geçmek için hâlâ zaman varken görünür kılmak ve her birini somut bir azaltma aksiyonuna, erken uyarı sinyaline ve sorumluya dönüştürmek. İnceleme bir kenara kaldırılacak bir liste değil, şimdi alınacak kararlarla ilgilidir.

## Ne zaman kullanılır
- Proje veya özellik başlangıcında, kapsam ve tarihler taahhüt edilmeden önce.
- Büyük bir sürüm, taşıma veya mimari değişiklikten önce.
- Süren bir proje belirti gösterdiğinde: kayan tahminler, tekrarlayan olaylar, belirsiz entegrasyon durumu.

## Ne zaman kullanılmaz
- Amaç projenin tüm kategorilerdeki genel risk kaydını sürdürmekse `risk-register` kullanılır.
- Bir tasarımın güvenlik tehditleri derinlemesine modellenecekse `threat-model` kullanılır.
- Mimarinin kendisi kalite nitelikleri açısından değerlendirilecekse `architecture-review` kullanılır.

## Girdiler
Zorunlu:
- İşin tanımı: hedef, kapsam, ana bileşenler ve teknolojiler, takvim veya kilometre taşı.

İsteğe bağlı, kaliteyi artırır:
- Mimari taslak, bağımlılık listesi, ekip yapısı ve deneyimi, tahmin ve varsayımları.
- Bilinen sorunlar, olay geçmişi, kısıtlar (uyum, değişiklik dondurma pencereleri, tedarikçi sözleşmeleri).

Kapsam veya ana bileşenler bilinmiyorsa sor. En fazla beş soru sor; geri kalan her şey varsayım veya açık soru olur.

## Süreç
1. Hedefi ve başarısızlığın neye benzeyeceğini (gecikme, bütçe aşımı, düşük kalite, üretimde olay) yeniden yaz; etki puanları buna dayanır.
2. Risk kaynaklarını sistematik olarak gez: mimari ve tasarım, teknoloji yeniliği, dış ve ekipler arası bağımlılıklar, veri (taşıma, kalite, hacim), entegrasyon ve sözleşmeler, performans ve ölçeklenebilirlik, güvenlik ve gizlilik, işletilebilirlik (izleme, rollback), test ve ortamlar, insan ve yetkinlik (kilit kişi, müsaitlik), takvim ve kapsam.
3. Her riski neden → olay → sonuç biçiminde yaz ("iş ortağı API'sinin sandbox'ı olmadığı için entegrasyon hataları geç bulunabilir ve sürüm gecikir"). Riskleri, şu anda yaşanmakta olan sorunlardan ayır.
4. Olasılığı ve etkiyi (Düşük/Orta/Yüksek) tek satırlık gerekçeyle puanla; girdiyle desteklenmeyen puanları `[VARSAYIM]` olarak işaretle.
5. Her Orta/Yüksek risk için bir erken uyarı sinyali (ölçülebilir tetikleyici) ve bir yanıt tanımla: kaçın, azalt, devret veya kabul et.
6. Önce riski en ucuza azaltan aksiyonları tercih et: süre sınırlı spike'lar, uçtan uca walking skeleton, sözleşme testleri, kritik yolun yük testi, erken üretime benzer ortam, feature flag'ler ve rollback provası.
7. Planı, en riskli varsayımlar en erken doğrulanacak şekilde sırala; bir risk gerçekleşirse tahmine etkisini belirt.
8. Her azaltma aksiyonuna bir sorumlu rolü ve gözden geçirme tarihi ata; asla isim uydurma.
9. En önemli üç riski ve şimdi gereken kararı özetle (ör. bir spike ile başla, kapsamı değiştir, bağımlılık kilometre taşı ekle).
10. Hedef devam ediyorsa riskleri zaman içinde izlemek için `risk-register`, en büyük bilinmeyen için `spike-report`, planı yeniden baz almak için `technical-estimation` öner.

## Çıktı formatı
```markdown
# Teknik Risk İncelemesi: <proje/özellik>
Hedef: ... · Ufuk: <kilometre taşı/tarih> · Katılan roller: <roller>

## En Önemli Riskler ve Gereken Karar
1. ...
Şimdi gereken karar: ...

## Risk Tablosu
| # | Risk (neden → olay → sonuç) | Kaynak | O | E | Erken uyarı sinyali | Yanıt | Azaltma aksiyonu | Sorumlu rol | Gözden geçirme tarihi |
|---|---|---|---|---|---|---|---|---|---|

## Mevcut Sorunlar (şu anda yaşananlar)
- ...

## Riski Azaltan Deneyler
| Deney | Ele alınan risk | Süre sınırı | Başarı kriteri |
|---|---|---|---|

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] 2. adımdaki tüm risk kaynakları ele alındı; boş olanlar "önemli risk bulunmadı" olarak belirtildi.
- [ ] Her risk neden → olay → sonuç biçiminde yazıldı ve sorunlar risklerden ayrıldı.
- [ ] Her Orta/Yüksek riskin erken uyarı sinyali, azaltma aksiyonu ve sorumlu rolü var.
- [ ] Girdiyle desteklenmeyen puanlar `[VARSAYIM]` olarak etiketli; hiçbir isim veya tarih uydurulmadı.
- [ ] En önemli riskler şimdi alınacak somut bir karara veya deneye bağlanıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Karmaşıklık" veya "sıkışık takvim" gibi belirsiz riskler. Nedeni ve sonucu adlandır ki azaltma aksiyonu kendiliğinden belirginleşsin.
- Yalnızca "yakından izle" diyen azaltma aksiyonları. Sinyali ve sinyal tetiklendiğinde yapılacak aksiyonu tanımla.
- Her şeyi Yüksek puanlamak. Ekibin ilk haftaları nereye harcayacağını bilmesi için sıralamayı zorla.

## Örnek
Girdi: "Fatura üretimini 3 ayda gece batch'inden olay güdümlü servise taşı; ekip mesaj kuyruğunda yeni."

Zayıf: "Risk: yeni teknoloji. Azaltma: dikkatli olmak."

Güçlü örnekten bir bölüm:
| # | Risk | Kaynak | O | E | Erken uyarı sinyali | Yanıt | Azaltma aksiyonu | Sorumlu rol |
|---|---|---|---|---|---|---|---|---|
| 1 | Ekip mesaj kuyruğunda yeni olduğu için mesaj sıralaması ve mükerrer işleme yanlış tasarlanabilir ve çift fatura oluşur | Teknoloji yeniliği | O | Y | Entegrasyon testlerinde mükerrer olaylar | Azalt | 1 haftalık spike: idempotent tüketici + sıralama testi | Teknik lider |
| 2 | Finans raporları batch tablolarını okuduğu için batch'i kapatmak ay sonu raporlarını bozabilir | Veri/bağımlılık | O `[VARSAYIM]` | Y | Veritabanı denetiminde bilinmeyen tüketiciler bulunması | Kaçın | Tasarım dondurulmadan önce tablo tüketicilerinin envanterini çıkar | Mimar |
