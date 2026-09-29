---
name: steering-committee-pack
description: "Gereken kararlarla başlayan, ardından baz plana göre kısa durum, başlıca riskler ve sorunlar, finansal durum (bütçe, gerçekleşen, tahmin) ve fayda görünümünü veren, her karar için seçenekler ve öneri içeren bir yönlendirme kurulu sunumu hazırlar. Bir yönlendirme kurulu, proje kurulu veya sponsor değerlendirmesi öncesinde, aylık program raporunun karar odaklı bir pakete dönüştürülmesi gerektiğinde ya da bir proje veya program için \"steerco sunumu\" veya \"kurul güncellemesi\" hazırlanması istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: program-pmo
  area: portfolio
  title: "Yönlendirme kurulu sunumu"
  related: "project-status-report, executive-summary, raid-log, decision-log, presentation-outline"
  prompt: "Gelecek perşembe için yönlendirme kurulu sunumunu hazırla: entegrasyon testinde 3 hafta gerideyiz, bütçeyi %8 aştık ve raporlama modülünün kapsamdan çıkarılması için karar gerekiyor."
---

# Yönlendirme Kurulu Sunumu

## Amaç
Yönlendirme kuruluna yönlendirme yapması için gerekeni vermek: bugün alması gereken kararları seçenekler ve öneriyle birlikte, bu kararları güvenle alabilmesine yetecek kadar durum, risk, finansal ve fayda bilgisiyle sunmak; yalnızca okunup geçilen bir ilerleme raporu değil.

## Ne zaman kullanılır
- Planlanmış bir yönlendirme kurulu, proje kurulu veya sponsor değerlendirmesi öncesinde.
- Bir programın düzenli raporunun karar odaklı bir pakete dönüştürülmesi gerektiğinde.
- Bir tolerans aşımının (zaman, maliyet, kapsam, kalite) kurula taşınması gerektiğinde.

## Ne zaman kullanılmaz
- Kitle yalnızca durum bilgisi isteyen ekip veya daha geniş paydaşlarsa `project-status-report` veya `status-update` kullanılır.
- Dış bir müşterinin yönlendirme raporu gerekiyorsa `client-steering-report` kullanılır.
- Tüm konuları kapsayan şirket düzeyinde bir yönetim kurulu güncellemesi gerekiyorsa `board-update` kullanılır.

## Girdiler
Zorunlu:
- Plana göre güncel durum (kilometre taşları, kapsam, kalite) ve gereken kararlar veya eskalasyonlar.
- Kurul bütçeyi denetliyorsa finansal durum (bütçe, gerçekleşen, tahmin) ya da denetlemediğinin açık teyidi.

İsteğe bağlı, kaliteyi artırır:
- Baz plan, kurulla anlaşılan toleranslar, önceki sunum ve aksiyonları.
- RAID kaydı, değişiklik talepleri, fayda planı.
- Kurul üyeleri ve kaygıları.

Durum veya gereken kararlar eksikse sor. Eksik rakamlar `[BİLİNMİYOR]` olarak kalır; dayanağı belirtilmeden asla parasal tahmin yapma.

## Süreç
1. Kurulun amacını ve üyelerini, belirlediği toleransları ve önceki toplantının aksiyonlarını belirle. Önceki her aksiyonu tamamlandı, devam ediyor veya gecikti olarak raporla.
2. Gereken kararları listele. Her biri için soruyu tek satırda, seçenekleri ("hiçbir şey yapmamak" dahil), her seçeneğin zaman, maliyet, kapsam, risk ve faydaya etkisini, gerekçeli öneriyi ve kararın değerini yitireceği son tarihi yaz.
3. Genel durumu her boyut için (takvim, maliyet, kapsam, kalite, risk, fayda) RAG ile özetle; her birini bir olgu ve eğilimle (iyileşiyor, sabit, kötüleşiyor) destekle. RAG eşiklerini toleranslara göre tanımla.
4. Kilometre taşlarını baz plana göre göster: planlanan, tahmin, sapma ve her sapmanın nedeni. Tahmini umuttan ayır; her tahminin dayanağını yaz.
5. Finansal durumu sun: bütçe, bugüne kadar gerçekleşen, taahhüt edilen, tamamlanmak için tahmini maliyet (ETC), tamamlandığındaki tahmini maliyet (EAC), sapma ve kalan yedek bütçe. Türetilmiş rakamları etiketle, eksikleri `[BİLİNMİYOR]` olarak işaretle.
6. Kurulun bilmesi veya aksiyon alması gereken başlıca riskleri ve sorunları seç (yaklaşık beşi geçmesin); sahibini, etkisini, azaltma önlemini ve kuruldan ne istendiğini yaz.
7. Fayda görünümünü raporla: planlanan faydalar hâlâ ulaşılabilir mi, büyüklüklerini veya zamanlamalarını ne değiştirdi?
8. Tek sayfalık yönetici özetini en son yaz: genel durum, gereken kararlar ve en önemli tek mesaj.
9. Ana paketi kısa tut (yaklaşık 5-8 sayfa veya slayt); ayrıntıyı eke taşı.
10. Paketi kurulun gözünden kontrol et: her üye eki okumadan karar verebilir mi? Burada sponsorla önceden konuşulması gereken bir sürpriz var mı? Toplantıdan önce kimin bilgilendirileceğini not et.
11. Hedef devam ediyorsa sonuçları kaydetmek için `decision-log`, riskleri güncellemek için `raid-log` veya paketi slayta dönüştürmek için `presentation-outline` öner.

## Çıktı formatı
```markdown
# Yönlendirme Kurulu: <proje / program> — <toplantı tarihi>
## 1. Yönetici Özeti
Genel: <RAG> (<eğilim>) · Ana mesaj: <tek cümle> · Gereken karar: <n>

## 2. Gereken Kararlar
### K1: <soru>
| Seçenek | Zaman | Maliyet | Kapsam | Risk | Fayda |
|---|---|---|---|---|---|
Öneri: <seçenek> — <gerekçe> · Son karar tarihi: <tarih>

## 3. Durum
| Boyut | RAG | Eğilim | Kanıt |
|---|---|---|---|
## 4. Baz Plana Göre Kilometre Taşları
| Kilometre taşı | Baz | Tahmin | Sapma | Neden | Tahmin dayanağı |
|---|---|---|---|---|---|
## 5. Finansal Durum
| Bütçe | Gerçekleşen | Taahhüt | ETC | EAC | Sapma | Kalan yedek |
|---|---|---|---|---|---|---|
## 6. Başlıca Riskler ve Sorunlar
| ID | Açıklama | Sahip | Etki | Azaltma | Kuruldan istenen |
|---|---|---|---|---|---|
## 7. Fayda Görünümü
## 8. Önceki Aksiyonlar
## Ek
## Varsayımlar ve Veri Boşlukları
- [VARSAYIM] / [BİLİNMİYOR] ...
```

## Kalite kontrol listesi
- [ ] Gereken kararlar en başta; her birinin seçenekleri, etkileri, önerisi ve son karar tarihi var.
- [ ] Her RAG değerlendirmesinin kanıtı, eğilimi ve anlaşılan toleranslara bağlı bir eşiği var.
- [ ] Kilometre taşı tahminleri dayanağını, sapmalar nedenini belirtiyor.
- [ ] Finansal rakamların kaynağı var ya da etiketli; hiçbir şey uydurulmadı.
- [ ] Gösterilen riskler kurulun bilmesi veya aksiyon alması gerekenlerle sınırlı.
- [ ] Ana paket ek okunmadan karar verilebilecek kadar kısa; çıkarımlar etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Karpuz raporlama (dışı yeşil, içi kırmızı). RAG'i toleranslara ve kanıta bağla, eğilimi göster.
- Kuruldan bir sorunu karar olmadan yalnızca "not etmesini" istemek. Seçeneklerle açık bir talep çerçevele.
- Sponsoru toplantıda şaşırtmak. Büyük kötü haberleri ve tartışmalı önerileri önceden paylaş.

## Örnek
Girdi: "Entegrasyon testinde 3 hafta gerideyiz, bütçe %8 aşıldı, raporlama modülünün kapsamdan çıkarılması için karar gerekiyor."

Çıktıdan bir bölüm:
- K1: Canlıya geçiş tarihini korumak için raporlama modülü 1. sürümden çıkarılsın mı?
  | Seçenek | Zaman | Maliyet | Kapsam | Risk |
  |---|---|---|---|---|
  | A. Kapsamı koru | +3 hafta `[VARSAYIM]` | +`[BİLİNMİYOR]` | Tam | Yasal tarih riskte |
  | B. Raporlamayı 2. sürüme taşı | Tarih korunur | Tolerans içinde `[TBD: finans kontrolü]` | Raporlama gecikir | Geçici elle raporlama gerekir |
  Öneri: B — sabit canlıya geçiş tarihini korur; geçici raporlama sahibi atanmalı. Son karar tarihi: bu toplantı.
- Maliyet: Sarı, kötüleşiyor — EAC, %10 toleransa karşı bütçenin %8 üzerinde.
