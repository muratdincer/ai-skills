---
description: "Geçmiş verim (throughput) verisinden Monte Carlo simülasyonuyla olasılıksal teslim öngörüsü üretir: 'N madde ne zaman biter?' veya 'D tarihine kadar kaç madde biter?' sorularını güven seviyeleriyle (%50/85/95) yanıtlar, backlog büyümesini ve bölünmeyi hesaba katar, yöntemi ve uyarıları açıklar. Haftalık veya iterasyon başına verim paylaşılıp sürüm tarihi, bir son tarih için kapsam öngörüsü ya da bir taahhüdü tutturma olasılığı sorulduğunda kullanılır."
related: "velocity-analysis, cycle-time-analysis, release-planning, burndown-analysis, schedule-plan"
prompt: "Son 12 haftadaki haftalık verimimiz: 3, 5, 4, 0, 6, 4, 5, 3, 7, 4, 2, 5. 38 madde kaldı. %85 güvenle ne zaman bitiririz?"
---

# Monte Carlo ile Teslim Tahmini

## Amaç
Tek noktalı tarihlerin yerine ekibin kendi teslim geçmişinden türetilen dürüst, olasılığa dayalı yanıtlar koymak. Böylece paydaşlar taahhüt seviyesini bilerek seçer ve kapsam büyümesinin tabloyu nasıl değiştirdiğini görür.

## Ne zaman kullanılır
- Bir sürüm tarihi veya son tarihteki kapsam için açık güven seviyeli öngörü gerekiyor.
- Paydaşlar "D tarihini tutturma olasılığımız ne?" diye soruyor.
- Puan tahminlerine güvenilmiyor veya yok, ama dönem başına madde sayıları mevcut.

## Ne zaman kullanılmaz
- Geçmiş teslimatın trendini ve değişkenliğini anlamak için `velocity-analysis` kullanılır.
- Tek bir maddenin süresini öngörmek için `cycle-time-analysis` yüzdelikleri kullanılır.
- Bağımlılıklarla görev düzeyinde takvim oluşturmak için `schedule-plan` kullanılır.

## Girdiler
Zorunlu:
- Verim geçmişi: hafta (veya iterasyon) başına biten madde, en az ~8 dönem; ekibi ve süreci geleceğe benzeyen bir dönemden.
- Soru: kalan madde sayısı ("ne zaman" için) veya hedef tarih ("kaç tane" için).

İsteğe bağlı, kaliteyi artırır:
- Beklenen backlog büyümesi veya bölünme oranı (ör. maddeler başlandıktan sonra tipik olarak 1,3 parçaya bölünüyor).
- Öngörü penceresindeki planlı kapasite değişiklikleri (tatiller, ekip değişiklikleri).
- Öngörünün başlangıç tarihi.

~8'den az dönem varsa yine öngörü yap ama sonucu `[DÜŞÜK GÜVEN]` olarak etiketle. Asla verim değeri uydurma; veri eksikse sor.

## Süreç
1. Örneklemi doğrula: aynı ekip, aynı "bitti" tanımı, benzer nitelikte (uygun boyutlu, homojen olması gerekmez) maddeler. Bilinen tek seferlik olaylarla bozulan dönemleri yalnızca kullanıcı tekrarlanmayacağını teyit ederse çıkar; çıkarılanları belirt.
2. Kalan kapsamı ayarla: kalan × bölünme katsayısı + beklenen büyüme. Bilinmiyorsa öngörüyü hem ham sayı için hem de `[VARSAYIM]` bir büyüme bandı (ör. +%10-25) için göster.
3. Simülasyonu açıkla: her deneme, kalan kapsam tükenene ("ne zaman") veya tarihe ulaşılana ("kaç tane") kadar geçmişten rastgele (yerine koyarak) bir dönem çeker. Çok sayıda deneme çalıştır (ör. 10.000).
4. Kod çalıştıramıyorsan öngörüyü şeffaf bir yaklaşıklıkla üret: örneklenen toplamın yüzdeliklerini bootstrap mantığıyla hesapla ya da kullanıcının çalıştırması için hesabı küçük bir betik/tablo formülü olarak ver ve rakamları `[YAKLAŞIK]` olarak etiketle. Uydurulmuş simülasyon çıktısını asla çalıştırılmış gibi sunma.
5. "Ne zaman" sonuçlarını gereken dönem sayısının yüzdelikleri olarak raporla: %50, %85, %95. Dönemleri başlangıç tarihinden itibaren, bilinen kapasite boşluklarını hesaba katarak takvim tarihlerine çevir.
6. "Kaç tane" sonuçlarını tersinden raporla: en az %85 ve %95 olasılıkla ulaşılan sayı (alt kuyruk), ayrıca %50.
7. Bir makullük kontrolü ekle: kalan ÷ medyan verim, %50 sonucuna yakın olmalı; büyük farkları açıkla.
8. Duyarlılığı açıkla: tarihi en çok hangi etken kaydırıyor (büyüme, sıfır verimli haftalar, bölünme oranı) ve öngörüyü ne değiştirir.
9. Yenileme kuralını belirt: öngörüyü her dönem yeni veriyle yeniden çalıştır; öngörü bir anlık görüntüdür, taahhüt değildir.
10. Seçilen güven seviyesini plana dönüştürmek için `release-planning`, geçmiş istikrarsız görünüyorsa `velocity-analysis` öner.

## Çıktı formatı
```markdown
# Monte Carlo Öngörüsü – <ekip/sürüm>
Soru: <N madde ne zaman biter / D tarihine kadar kaç tane>
Geçmiş: <n dönem, tarihler>, verim <liste> · Deneme: <n> · Yöntem: <simülasyon / [YAKLAŞIK]>
Kullanılan kapsam: <ham> → <ayarlanmış> (<bölünme katsayısı, büyüme [VARSAYIM]>)

| Güven | Gereken dönem / Biten madde | Takvim tarihi |
|---|---|---|
| %50 | | |
| %85 | | |
| %95 | | |

Makullük kontrolü: <kalan ÷ medyan verim = ...>
Duyarlılık: <ana etkenler>
Uyarılar: <örneklem kalitesi, kapasite değişiklikleri, gerekirse [DÜŞÜK GÜVEN]>
Yenileme: <sıklık>
```

## Kalite kontrol listesi
- [ ] Yanıt tek bir tarih değil, bir güven seviyeleri kümesi.
- [ ] Geçmiş dönem ve temsil gücü belirtildi.
- [ ] Kapsam büyümesi veya bölünme ya dahil edildi ya da açıkça hariç tutuldu.
- [ ] Rakamların çalıştırılmış bir simülasyondan mı yaklaşıklıktan mı geldiği açık.
- [ ] "Kaç tane" sorularında yüksek güven için alt kuyruk kullanıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Kaç tane" dağılımını yanlış kuyruktan okumak. %85 güven, denemelerin %85'inde en az o kadar madde demektir; bu, medyandan küçük bir sayıdır.
- Backlog büyümeye devam ederken sabit kapsamla öngörü yapmak. Büyümeyi dahil et, yoksa tarih her hafta kayar.
- Farklı bir ekibin veya sürecin geçmişini kullanmak. Model, örneklemin geleceğe benzerliği kadar iyidir.

## Örnek
Girdi: haftalık verim 3, 5, 4, 0, 6, 4, 5, 3, 7, 4, 2, 5 (medyan 4); 38 madde kaldı; 1. haftanın pazartesisi başlangıç.

Çıktıdan bir bölüm:
- Makullük kontrolü: medyanla 38 ÷ 4 ≈ 9,5 hafta.
- %50: 10 hafta · %85: 11-12 hafta · %95: 13 hafta `[YAKLAŞIK]` (doğrulamak için betik verildi).
- +%20 büyümeyle `[VARSAYIM]` (46 madde): %85 değeri ~13-14 haftaya kayar.
- Zayıf ifade: "9 haftada biteriz." Güçlü ifade: "Kapsam 38 maddede kalırsa 12 hafta içinde bitme olasılığı %85."
