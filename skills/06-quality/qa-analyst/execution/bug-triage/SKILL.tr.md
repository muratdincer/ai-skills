---
name: bug-triage
description: "Bir grup hatayı; bütünlüğünü doğrulayarak, mükerrerleri bularak, önem derecesini (etki) öncelikten (düzeltme sırası) ayırarak, sorumlu ve hedef atayarak ve sürümü engelleyenleri işaretleyerek önceliklendirir; bir karar tablosu ve takip listesi üretir. Yeni veya birikmiş hatalar bir önceliklendirme toplantısında gözden geçirilecekse, sürüm yaklaşırken açık hatalar için engelleyici kararı gerekiyorsa ya da önce hangi hataların düzeltileceği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: execution
  title: "Hata önceliklendirme"
  related: "bug-report, release-quality-gate, defect-trend-analysis, risk-based-testing, ticket-triage"
  prompt: "Cuma günkü sürüm öncesi bu 14 açık hatayı önceliklendir: önem, öncelik, mükerrerler ve hangilerinin sürümü engellediğine karar ver."
---

# Hata Önceliklendirme

## Amaç
Sırasız bir hata kaydı kümesini net ve gerekçeli kararlara dönüştürmek: ne düzeltilecek, kim tarafından, hangi sürümde ve yayını ne engelliyor.

## Ne zaman kullanılır
- Düzenli bir önceliklendirme oturumunda yeni bildirilen hatalar gözden geçiriliyor.
- Bir sürüm adayında açık hatalar var ve engelleyici/engelleyici değil kararı gerekiyor.
- Hata backlog'u büyüdü ve temizlenmesi gerekiyor (mükerrer, eskimiş, reddedilen).

## Ne zaman kullanılmaz
- Tek bir hatanın hâlâ düzgün yazılması gerekiyorsa `bug-report` kullanılır.
- Zaman içindeki istatistikler ve kök neden örüntüleri gerekiyorsa `defect-trend-analysis` kullanılır.
- Bir sürüm için genel yayına alınır/alınmaz kararı gerekiyorsa `release-quality-gate` kullanılır.

## Girdiler
Zorunlu:
- En az başlık, açıklama ve mevcut durumu içeren hata listesi.

İsteğe bağlı, kaliteyi artırır:
- Ekibin kullandığı önem ve öncelik tanımları, sürüm tarihi ve kapsamı, bileşen sorumluları.
- Kullanım verisi, müşteri bildirimleri, SLA taahhütleri, bilinen geçici çözümler.

Hata listesi yoksa iste. Ekibin önem/öncelik ölçeği yoksa aşağıdaki varsayılanı kullan ve `[VARSAYIM]` ile işaretle.

## Süreç
1. Ölçekleri netleştir. Varsayılan önem: Kritik (veri kaybı, güvenlik, kesinti, geçici çözüm yok), Majör (temel işlev bozuk, zor geçici çözüm), Minör (sınırlı işlev, kolay geçici çözüm), Önemsiz (kozmetik). Varsayılan öncelik: P1 hemen düzelt, P2 bu sürümde, P3 sonraki sürümde, P4 backlog.
2. Her kaydı doğrula: tekrarlanabilir adımlar, ortam, beklenen sonuç. Eksik olanları eksik kalemi ve sorulacak kişiyi belirterek "Bilgi gerekli" olarak işaretle.
3. Mükerrerleri ve kümeleri belirti, bileşen ve kök neden işaretlerine göre bul; en eksiksiz kaydı birincil tut, diğerlerini bağla.
4. Her kalemi sınıfla: hata, değişiklik talebi/yeni gereksinim, tasarım gereği çalışıyor, ortam/veri sorunu, tekrarlanamadı. Yalnızca hatalar devam eder.
5. Önem derecesini, kimin bildirdiğinden bağımsız olarak teknik etkiye göre değerlendir.
6. Önceliği, önem derecesini iş etkenleriyle birleştirerek değerlendir: etkilenen kullanıcılar ve sıklık, görünürlük, uyum veya sözleşme riski, geçici çözüm maliyeti, düzeltme riski ve eforu, sürüm zamanlaması. Önceliğin önemden farklı olduğu her durumu açıkla.
7. Sürüm çıkış kriterlerine göre sürümü engelleyenleri işaretle; engelleyiciler sorumlusu belli P1/P2 olmalı.
8. Sorumlu (ekip veya bileşen) ve hedef sürüm veya iterasyon ata; verilmedikçe kişi adı yazma.
9. Toplantıda olmayan paydaşlar da izleyebilsin diye her hata için kararı ve gerekçeyi tek satırda kaydet.
10. Özetle: karara göre sayılar, engelleyiciler, bilgi bekleyen kalemler ve ertelemeyle kabul edilen riskler.
11. Kullanıcı devam ederse yayın kararı için `release-quality-gate`, kümeler sistemik sorunlara işaret ediyorsa `defect-trend-analysis` öner.

## Çıktı formatı
```markdown
# Hata Önceliklendirme: <kapsam / tarih>
Kullanılan ölçekler: <ekip ölçeği veya varsayılan [VARSAYIM]>

| Hata | Başlık | Sınıf | Önem | Öncelik | Engelleyici | Sorumlu | Hedef | Gerekçe |
|---|---|---|---|---|---|---|---|---|

## Mükerrerler ve Kümeler
- <birincil> ← <mükerrerler> – <ortak belirti>

## Bilgi Gerekli
- <hata>: <eksik kalem> – <rol>'e sor

## Özet
- Engelleyici: n (liste) · Bu sürümde düzeltilecek: n · Ertelenen: n · Reddedilen/Tasarım gereği: n
- Ertelemeyle kabul edilen riskler: ...
```

## Kalite kontrol listesi
- [ ] Önem ve öncelik ayrı değerlendirilmiş, farklılıklar açıklanmış.
- [ ] Her engelleyicinin sorumlusu ve hedefi var ve bir çıkış kriterine izlenebiliyor.
- [ ] Mükerrerler tek bir birincil kayda bağlanmış.
- [ ] Hata olmayanlar (değişiklik talepleri, tasarım gereği) gerekçeyle ayrılmış.
- [ ] Sorumlu adı, tarih veya kullanıcı sayısı uydurulmamış; bilinmeyenler `[BİLİNMİYOR]`.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Önem ile önceliği eşitlemek. Ödeme sayfasındaki kozmetik bir yazım hatası P1, kullanımdan kalkmış bir yönetim ekranındaki çökme P4 olabilir.
- Önceliği en yüksek sesli paydaşın belirlemesine izin vermek. Her hata için aynı etkenleri kullan ve gerekçeyi yaz.
- Aynı hatayı her sürümde ertelemek. İkiden fazla ertelenen kalemler açıkça kabul edilmeli veya kapatılmalı.

## Örnek
Girdi: "14 açık hata, sürüm cuma."

Çıktıdan bir bölüm:
| Hata | Başlık | Sınıf | Önem | Öncelik | Engelleyici | Gerekçe |
|---|---|---|---|---|---|---|
| B-102 | Çoklu KDV oranlı sepetlerde fatura PDF'i yanlış KDV toplamı gösteriyor | Hata | Kritik | P1 | Evet | Yasal belge hatalı; geçici çözüm yok |
| B-109 | Karanlık modda giriş sayfasında logo kaymış | Hata | Önemsiz | P3 | Hayır | Kozmetik, düşük görünürlük |
| B-111 | "Dışa aktarımda vergi numarası olmalı" | Değişiklik talebi | – | – | Hayır | Yeni gereksinim; backlog'a yönlendir |
| B-114 | B-102 ile aynı, mobilden bildirilmiş | Mükerrer | – | – | – | B-102'ye bağlandı |
