---
name: open-questions-tracker
description: "Toplantılardan, dokümanlardan ve yazışmalardan çözülmemiş soruları; net soru, neden önemli olduğu, neyi engellediği, sorumlusu, gereken tarih, durum ve cevapla birlikte bir takip listesinde toplar ve engellediği işe göre önceliklendirir. Bir projede çok sayıda dağınık soru olduğunda, analiz veya tasarım cevap beklediğinde ya da \"hâlâ neyi bekliyoruz?\" sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: meetings
  area: after
  title: "Açık soruları takip etme"
  related: "action-item-extraction, meeting-notes, raid-log, request-clarification-questions, decision-log"
  prompt: "Bu üç toplantı notunu ve gereksinim dokümanını incele, sorumlu ve tarihleriyle bir açık sorular listesi oluştur."
---

# Açık Soruları Takip Etme

## Amaç
Çözülmemiş her soruyu görünür, sahipli ve zamana bağlı kılmak; böylece cevap bekleyen işlerin önü zamanında açılır ve cevaplar insanların bulacağı yerde kaydedilir.

## Ne zaman kullanılır
- Birden fazla toplantı veya doküman cevapsız sorular bıraktıysa.
- Analiz, tasarım, tahmin veya bir karar eksik bilgi yüzünden engelliyse.
- Mevcut bir soru listesi yeni cevaplar veya yeni sorularla güncellenecekse.

## Ne zaman kullanılmaz
- Maddeler birinin yapmayı üstlendiği işlerse `action-item-extraction` kullanılır.
- Tek bir yeni talep için netleştirme soruları hazırlanacaksa `request-clarification-questions` kullanılır.
- Riskler, varsayımlar, sorunlar ve bağımlılıklar birlikte takip edilecekse `raid-log` kullanılır.

## Girdiler
Zorunlu:
- Soru içeren kaynak materyal (notlar, dokümanlar, yazışmalar) veya mevcut liste.

İsteğe bağlı:
- Soruların etkilediği kilometre taşları veya tarihler, sorumluluk alanlarıyla paydaş listesi, güncellenecek mevcut takip listesi.

Kilometre taşı tarihleri verilmediyse "gereken tarih"i sorunun engellediği işten türet ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Soruları topla: açık "?", "emin değilim", "TBD", "teyit edilecek", "şuna bağlı", açık kalan anlaşmazlıklar ve dokümanlardaki `[BİLİNMİYOR]` işaretleri.
2. Her birini tek bir kişinin cevaplayabileceği kapalı veya somut bir soru olarak yeniden yaz ("Denetim aktarımı hangi alanları içermeli?", "aktarım detayları?" değil).
3. Tekrarları birleştir, bileşik soruları böl.
4. Her biri için neden önemli olduğunu ve neyi engellediğini yaz (bir iş kalemi, karar, tahmin veya kilometre taşı).
5. Cevabı verebilecek veya bulabilecek bir sorumlu ata; bilinmiyorsa `[SORUMLU BİLİNMİYOR]` yaz ve bir rol öner.
6. Gereken tarih = cevabın engellenen iş için hâlâ işe yarayacağı en geç tarih; keyfi bir tarih değil.
7. Önceliklendir: Ö1 kritik yolu veya bu haftaki bir kararı engelliyor; Ö2 planlı işi engelliyor; Ö3 bilinmesi iyi olur.
8. Durumu belirle: Açık, Soruldu (tarih), Cevaplandı, Kapandı-artık geçerli değil, Eskale edildi. Cevapları kaynak ve tarihle birebir kaydet.
9. Mevcut listeyi güncellerken cevaplanan soruları kapalı bölüme taşı ve hangi karar veya dokümanların güncellenmesi gerektiğini not et.
10. Gereken tarihi geçmiş soruları eskalasyon için işaretle.
11. Kullanıcının hedefi devam ediyorsa risk veya soruna dönüşmüş sorular için `raid-log`, bir kararı kesinleştiren cevapları kaydetmek için `decision-log` öner.

## Çıktı formatı
```markdown
# Açık Sorular – <proje/konu> (<tarih> itibarıyla)
| No | Soru | Neden önemli / neyi engelliyor | Öncelik | Sorumlu | Gereken tarih | Durum | Kaynak |
|---|---|---|---|---|---|---|---|
| S1 | ... | ... | Ö1 | ... | YYYY-AA-GG | Açık | <toplantı/doküman> |

Gecikmiş / eskale edilecek: <numaralar>

## Son güncellemeden bu yana cevaplananlar
| No | Cevap | Cevaplayan | Tarih | Güncellenecek yer |
|---|---|---|---|---|
```

## Kalite kontrol listesi
- [ ] Her soru somut ve tek bir kişi tarafından cevaplanabilir.
- [ ] Her soru neyi engellediğini belirtiyor.
- [ ] Her birinin sorumlusu ya da önerilen rolle `[SORUMLU BİLİNMİYOR]` işareti var.
- [ ] Gereken tarihler engellenen işten türetildi, varsayımlar işaretli.
- [ ] Cevaplanan maddeler cevabı, kaynağı ve gereken güncellemeleri içeriyor.
- [ ] Girdide söylenmeyen her şey `[VARSAYIM]` olarak işaretlendi veya açık soru olarak listelendi; olgu gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kimsenin cevaplayamayacağı muğlak sorular ("performans?"). Somut ve ölçülebilir hâle getir.
- Soruyu soranı sorumlu yazmak. Cevabı bilen veya bulabilecek kişiyi ata.
- Cevapların sohbette kalması. Kaydet ve etkilenen doküman veya kararı güncelle.

## Örnek
Girdi: Notlarda "loglar için saklama süresi? hukuk teyit edecek" ve "iş ortakları için SSO gerekli mi emin değiliz" geçiyor.

Çıktıdan bir bölüm:
| S1 | Kişisel veri içeren uygulama logları için hangi saklama süresi geçerli? | Loglama tasarımını ve depolama tahminini engelliyor | Ö1 | Hukuk/VSK `[ismi teyit et]` | [VARSAYIM] tasarım incelemesinden önce | Açık | Mimari toplantı 03/06 |
| S2 | İş ortağı kullanıcıları kurumsal SSO ile mi kimlik doğrulamalı? | Kimlik doğrulama kapsamını ve tahmini engelliyor | Ö2 | [SORUMLU BİLİNMİYOR] – ürün sahibi | [BİLİNMİYOR] | Açık | Başlangıç notları |
