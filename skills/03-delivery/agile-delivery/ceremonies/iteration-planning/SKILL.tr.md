---
name: iteration-planning
description: "Bir iterasyon/sprint planlama oturumunu baştan sona kolaylaştırır: gerçekçi kapasiteyi hesaplar, iterasyon hedefini teyit eder, kapasiteye sığan işi seçip görevlere böler, riskleri ve ortaya çıkan planı kaydeder. Ekip yeni bir iterasyona/sprint'e başlamak üzereyken, planlama gündemi veya kapasite hesabı istendiğinde ya da geçmiş planlar sürekli aşırı taahhütle bittiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "İterasyon planlaması kolaylaştırma"
  related: "iteration-goal, estimation-session, velocity-analysis, task-breakdown, definition-of-ready"
  prompt: "2 haftalık sprint için 6 geliştiricili sprint planlamasını yürütmeme yardım et; biri 3 gün izinli ve son gün sürüm dondurma var. En üstteki 12 backlog maddesi ekte."
---

# İterasyon Planlaması Kolaylaştırma

## Amaç
Ekibin gerçekten inandığı bir iterasyon/sprint planı üretmek: bir hedef, gerçek kapasiteye göre boyutlandırılmış bir seçim, ilk görev kırılımı ve görünür riskler. Böylece iterasyon bir istek listesiyle değil, ortak bir taahhütle başlar.

## Ne zaman kullanılır
- Ekip yeni bir iterasyona/sprint'e başlıyor ve bir gündem ile kapasiteye dayalı seçime ihtiyaç duyuyor.
- Son iterasyonlar büyük devir (carry-over) ile bitti ve planlamanın sıfırlanması gerekiyor.
- Yeni kurulan veya yeniden yapılanan bir ekip ilk iterasyonunu planlıyor.

## Ne zaman kullanılmaz
- Yalnızca tek cümlelik hedef gerekiyorsa `iteration-goal` kullanılır.
- Maddeler planlanamayacak kadar belirsiz veya büyükse önce `backlog-refinement` veya `story-splitting` kullanılır.
- Ekip iterasyonsuz, sürekli akışla çalışıyorsa taahhütler için `wip-policy` ve `monte-carlo-forecast` kullanılır.

## Girdiler
Zorunlu:
- Sıralanmış aday backlog maddeleri (ekip tahmin yapıyorsa boyutlarıyla).
- İterasyon için ekip üyeleri ve müsaitlikleri (süre, izinler, diğer görevler).

İsteğe bağlı, kaliteyi artırır:
- Son 3-6 iterasyonun verimi (throughput) veya hızı (velocity).
- Taslak iterasyon hedefi, ürün/sürüm hedefi.
- Bilinen olaylar: sürümler, dondurmalar, tatiller, nöbet rotasyonu, diğer ekiplere bağımlılıklar.
- Hazır Tanımı (DoR) ve Bitti Tanımı (DoD).

Adaylar veya müsaitlik eksikse sor (en fazla 5 odaklı soru). Diğer her şey açık soru olur.

## Süreç
1. İterasyon süresini, tarihlerini ve sabit olayları (dondurma, sürüm, tatil) teyit et. Teyit edilmemiş her tarihi `[TBD]` olarak işaretle.
2. Kişi başı kapasiteyi hesapla: çalışma günleri eksi izin eksi tekrarlayan yük (toplantı, destek, nöbet). Kullanılan odak katsayısını belirt; ekip vermediyse `[VARSAYIM]` olarak işaretle.
3. Kapasiteyi geçmişle karşılaştır: geçmiş verim/hız varsa son iterasyonların medyanını tavan olarak kullan ve iki görüş arasındaki farkı açıkla. Asla geçmiş rakam uydurma.
4. İterasyon hedefini ürün sahibiyle teyit et veya taslakla; yalnızca madde listesiyse sonuç odaklı bir hedef öner.
5. Her adayı Hazır Tanımı'na göre kontrol et; geçemeyen maddeleri eksik unsuruyla birlikte "hazır değil" listesine taşı.
6. Kapasite tavanına ulaşana kadar backlog sırasına göre madde seç; plansız iş için tampon bırak (yüzdeyi ve dayanağını belirt). Hedefe hizmet eden maddeleri ve bağımsız ama gerekli işleri ayrı işaretle.
7. Seçilen üst maddeleri en fazla yaklaşık bir günlük görevlere böl; her görev için sahip adayı ve açık bir "bitti" kontrolü yaz. Zaman kısaysa kalanını ilk günlere bırak.
8. Riskleri ve bağımlılıkları belirle: dış ekipler, ortamlar, tek kişide toplanmış yetkinlikler, belirsiz kabul kriterleri.
9. Güven oylaması yap (ör. beş parmak). Güven düşükse kapasiteyi zorlamak yerine kapsam çıkar ve çıkarılanı kaydet.
10. Planı çıktı formatında yaz; ekibin söylediğini kendi çıkarımından ayır.
11. Kullanıcının hedefi devam ediyorsa daha derin kırılım için `task-breakdown`, boyutlandırılmamış maddeler için `estimation-session` veya iterasyonun ilerleyen günlerinde `iteration-review-prep` öner.

## Çıktı formatı
```markdown
# İterasyon Planı: <iterasyon adı/no> (<başlangıç> – <bitiş>)
**Hedef:** <tek cümlelik sonuç>
**Güven:** <oylama sonucu veya [TBD]>

## Kapasite
| Üye | Müsait gün | Tekrarlayan yük | Net kapasite |
|---|---|---|---|
| Toplam | | | <n> – odak katsayısı <x> [VARSAYIM] |
Geçmiş referans: <medyan verim/hız veya [BİLİNMİYOR]>
Plansız iş tamponu: <%> – <dayanak>

## Seçilen Maddeler
| # | Madde | Boyut | Hedefe hizmet? | Sahip adayı | Risk |
|---|---|---|---|---|---|

## Seçilmeyen / Hazır Olmayan
- <madde> – <gerekçe: kapasite / DoR'u geçmiyor: eksik ...>

## Görev Kırılımı (üst maddeler)
- <madde>: <görev> – <bitti kontrolü>

## Riskler ve Bağımlılıklar
- [RİSK] ... – <önlem / sahip>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
- <soru> – <kim cevaplar>
```

## Kalite kontrol listesi
- [ ] Kapasite belirtilen müsaitlikten türetildi ve verilmeyen her katsayı `[VARSAYIM]` olarak işaretli.
- [ ] Seçim kapasite tavanını aşmıyor ve tampon açıkça belirtilmiş.
- [ ] Hedef bir sonuç ve her seçilen madde hedefe hizmet edip etmediğine göre işaretli.
- [ ] Hazır Tanımı'nı geçemeyen maddeler sessizce plana alınmadı.
- [ ] Her görevin doğrulanabilir bir bitti kontrolü var.
- [ ] Hiçbir geçmiş metrik, tarih veya isim uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- %100 kapasiteyle planlamak. Plansız iş her zaman gelir; ekibin son dönemdeki kesinti oranına göre tampon ayır.
- Hızı hedef olarak kullanmak. Hız bir planlama girdisidir; zorlamak çıktıyı değil tahminleri şişirir.
- Tüm görevleri baştan atamak. Yalnızca paralel yürümesi gerekenleri ata, kalanını ekip kendisi çeksin.
- Madde listesinden ibaret bir hedefi kabul etmek. İterasyon ortasında kapsam ödünleşiminin dayanağını ortadan kaldırır.

## Örnek
Girdi: "6 geliştirici, 10 günlük sprint, Ayşe 3 gün izinli, 10. gün sürüm dondurma, son hızlar 34, 28, 31. Üst maddeler ekte."

Çıktıdan bir bölüm:
- Kapasite: 57 kişi-gün eksi kişi başı ~1 gün toplantı ve destek = 51; odak katsayısı 0,7 `[VARSAYIM]` → ~36 ideal gün. Geçmiş medyan hız 31 puan → %10 tamponla yaklaşık 28-31 puan planla.
- Hazır değil: "Fatura PDF yeniden tasarımı" – kabul kriteri yok.
- [RİSK] 10. gün dondurma: deployment gerektiren her iş 9. güne kadar bitmeli.
