---
name: interview-plan
description: "Bir rol için yapılandırılmış bir mülakat süreci tasarlar; her yetkinliği onu ölçen aşamalara eşler, aşama formatlarını, sürelerini, mülakatçı profillerini, puanlama ölçütlerini, aday iletişimini ve önyargıyı azaltan karar kurallarını belirler. Bir rol açılırken, mevcut süreç yavaş, tutarsız veya teklif kabul oranı düşük olduğunda ya da mülakatçılar aynı şeyleri ölçüp bazı alanları atladığında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: hiring
  title: "Mülakat süreci tasarlama"
  related: "job-description, technical-interview-questions, interview-scorecard, candidate-debrief, career-ladder"
  prompt: "Orta seviye frontend mühendisi için bir mülakat süreci tasarla. Adaydan en fazla dört saat alabiliriz."
---

# Mülakat Süreci Tasarlama

## Amaç
Rolde başarıyı öngören yetkinlikleri her aday için tutarlı biçimde, en az aday zamanı ve mülakatçı tekrarıyla ve net bir karar kuralıyla ölçmek.

## Ne zaman kullanılır
- Yeni bir rol açıldığında veya bir rolün seviyesi değiştiğinde.
- Mevcut süreç tutarsız kararlar, uzun süreler veya kötü aday geri bildirimi üretiyorsa.
- İşe alım hacmi artıyor ve yeni mülakatçılar için standart bir yapı gerekiyorsa.

## Ne zaman kullanılmaz
- Teknik aşamanın sorularını ve puanlamasını yazmak için `technical-interview-questions` kullanılır.
- Mülakat sonrası kanıtı kaydetmek için `interview-scorecard` kullanılır.
- İlan metni için `job-description` kullanılır.

## Girdiler
Zorunlu:
- Rol, seviye ve önemli olan 4-7 yetkinlik (veya bunların çıkarılacağı iş ilanı).

İsteğe bağlı, kaliteyi artırır:
- Aday zaman bütçesi, uzaktan veya yüz yüze, müsait mülakatçılar ve eğitim durumları.
- Mevcut süreç ve sorunları; hukuki veya İK gereklilikleri; erişilebilirlik ihtiyaçları süreci.

Yetkinlikler yoksa iş ilanından bir öneri çıkar ve onay için `[VARSAYIM]` olarak işaretle.

## Süreç
1. Yetkinlikleri teyit et ve her biri için bu seviyede "çıtayı karşılar"ın ne olduğunu gözlemlenebilir biçimde tanımla.
2. Yetkinlik × aşama matrisi oluştur; her yetkinlik en az bir aşamada, kritik olanlar iki aşamada ölçülür ve hiçbir aşama üçten fazla yetkinlik ölçmez.
3. Gerçek işe benzeyen formatlar seç: eşli kodlama veya pratik alıştırma, sistem tasarımı tartışması, kod inceleme alıştırması, yapılandırılmış davranışsal mülakat. İşle ilgisiz bilgi yarışması ve bulmacalardan kaçın.
4. Ev ödevi ile canlı alıştırma arasında karar ver; ücretsiz ev ödevi eforunu sınırla (ör. 2-3 saat) ve kısıtı olan adaylar için alternatif sun.
5. Toplam aday süresini bütçe içinde tut; erken aşamalar olmazsa olmazları elesin.
6. Her aşama için mülakatçı profilini belirle (seviye, eğitimli, mümkünse çeşitli panel); işe alım yöneticisinin tek karar sesi olmasından kaçın.
7. Standartlaştır: aşama başına aynı temel sorular, seviye bazlı puanlama çapaları, herhangi bir tartışmadan önce bağımsız yazılı değerlendirme formları.
8. Karar kurallarını tanımla: Hangi puan kombinasyonu işe al / alma sonucuna götürür, kim karar verir, anlaşmazlıklar nasıl çözülür.
9. Aday deneyimini planla: önceden ne söylenecek, hangi düzenlemeler sunulacak, geri bildirim takvimi.
10. Süreç sağlığı metriklerini tanımla: karara kadar geçen süre, aşama başına geçiş oranı, teklif kabulü, mülakatçı kalibrasyon sapması.
11. Kullanıcının hedefi devam ediyorsa aşama soruları için `technical-interview-questions`, değerlendirme formu için `interview-scorecard` veya karar toplantısı için `candidate-debrief` öner.

## Çıktı formatı
```markdown
# Mülakat Süreci: <rol, seviye>
Aday süresi: <toplam> · Karar sahibi: <rol>

## Yetkinlikler ve Çıta
| Yetkinlik | Bu seviyede çıtayı karşılamak |
|---|---|

## Aşamalar
| # | Aşama | Format | Süre | Ölçülen yetkinlikler | Mülakatçı profili |
|---|---|---|---|---|---|

## Kapsama Matrisi
| Yetkinlik | Aşama 1 | Aşama 2 | Aşama 3 | Aşama 4 |
|---|---|---|---|---|

## Standartlaştırma ve Önyargı Kontrolleri
- ...

## Karar Kuralı
- ...

## Aday İletişimi
- ...

## Süreç Sağlığı Metrikleri
- ...
```

## Kalite kontrol listesi
- [ ] Her yetkinlik kapsanıyor; kritik olanlar iki kez; hiçbir aşama üçten fazla yetkinlik ölçmüyor.
- [ ] Formatlar gerçek işe benziyor; zekâ bulmacası yok.
- [ ] Toplam aday süresi bütçe içinde; ev ödevi eforu sınırlı.
- [ ] Değerlendirme formları ortak toplantıdan önce bağımsız yazılıyor.
- [ ] Karar kuralı ve sahibi açık.
- [ ] Makul düzenleme ve aday iletişimi planlandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ayrı bir "kültür uyumu" aşaması. Benzerlik önyargısını davet eder; bunun yerine belirli değerlere dayalı davranışları ölç.
- Beş mülakatçının da aynı projeyi sorması. Kapsama matrisiyle her birine ayrı odak alanı ver.
- Emin olunamadığında aşama eklemek. Fazla aşama tahmini nadiren iyileştirir ama işe alımı her zaman yavaşlatır.

## Örnek
Girdi: "Orta seviye frontend mühendisi, aday için en fazla dört saat."

Çıktıdan bir bölüm:
| 1 | İK ön görüşmesi | Telefon | 30 dk | Motivasyon, lojistik | İşe alım uzmanı |
| 2 | Pratik eşli çalışma | Adayın tercih ettiği framework'te küçük bir bileşen geliştirme | 75 dk | Frontend ustalığı, test | Eğitimli iki orta/kıdemli mühendis |
| 3 | Tasarım ve kod inceleme | Bir PR'ı inceleme, state ve performans ödünleşimlerini tartışma | 60 dk | Teknik muhakeme, iş birliği | Kıdemli mühendis |
| 4 | Davranışsal | Yapılandırılmış sorular | 45 dk | Sahiplenme, iletişim | İşe alım yöneticisi + fonksiyonlar arası paydaş |
