---
name: value-stream-map
description: "Müşteri talebinden teslim edilen değere kadar bir değer akışını haritalar; her adımda işlem süresini bekleme süresinden ayırır, adımları değer katan, gerekli ama değer katmayan veya israf olarak sınıflandırır ve toplam süre (lead time), işlem süresi, akış verimliliği ve yeniden işleme oranlarını hesaplar. Bir süreç veya teslimat akışı yavaş geldiğinde, toplam sürenin kısaltılması gerektiğinde ya da israfın, beklemenin veya darboğazın nerede olduğu sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: process
  title: "Değer akışı haritalama"
  related: "as-is-process, to-be-process, cycle-time-analysis, five-whys, process-gap-analysis"
  prompt: "Müşteri kazanım sürecimizin değer akışını çıkar: başvurudan aktif hesaba yaklaşık 12 gün sürüyor, zamanın nereye gittiğini görmek istiyoruz."
---

# Değer Akışı Haritalama

## Amaç
Müşteri talebi ile teslim edilen değer arasında zamanın nereye gittiğini göstermek. Böylece iyileştirme, pek fark yaratmayan adımları hızlandırmak yerine en büyük beklemelere ve israflara odaklanır.

## Ne zaman kullanılır
- Toplam süre uzun veya öngörülemez ve nedeni belli değilse.
- Bir to-be tasarımı sayısal bir başlangıç değerine ve hedefe ihtiyaç duyuyorsa.
- Uçtan uca bir akış birkaç ekibe yayılıyor ve bütünün sahibi yoksa.

## Ne zaman kullanılmaz
- Sürelere gerek olmadan yalnızca adım adım tarif gerekiyorsa `as-is-process` kullanılır.
- Bir teslimat ekibinin iş kalemi akışı takip aracı verisinden analiz ediliyorsa `cycle-time-analysis` kullanılır.
- Belirli bir gecikmenin kök nedeni aranıyorsa `five-whys` kullanılır.

## Girdiler
Zorunlu:
- Akışın başlangıç tetikleyicisi ve bitiş noktası ("değer teslim edildi"nin anlamı).
- Ana adımlar ve her adım için en azından yaklaşık işlem süresi ile bekleme süresi ya da bunların türetilebileceği veri.

İsteğe bağlı, kaliteyi artırır:
- Hacim (günlük/haftalık adet), parti büyüklükleri, adım başına kişi sayısı.
- Adım başına tam ve doğru oranı (%C&A) veya yeniden işleme oranı.
- Bir sistem günlüğünden veya takip aracından zaman damgaları.

Süreler yoksa adım adım sor (bir seferde en fazla 5 soru). Yalnızca tahmin varsa kullan ve `[VARSAYIM]` olarak işaretle; asla rakam uydurma.

## Süreç
1. Sınırları sabitle: müşteri, tetikleyici, bitiş durumu ve akış birimi (bir başvuru, bir sipariş, bir değişiklik).
2. Adımları sırayla, yapan ekip/sistem ve devir teslimlerle listele; kuyrukları, onayları ve batch işleri açık adım veya bekleme olarak ekle.
3. Her adım için kaydet: işlem süresi (fiilen çalışılan), sonraki adımdan önceki bekleme, %C&A ve biliniyorsa parti/hacim. En iyi durumu değil medyanı kullan; dağılım büyükse not düş.
4. Her adımı sınıflandır: Değer katan (müşteri bunun için öder), Gerekli ama değer katmayan (mevzuat, kontrol), İsraf. İsraf türünü etiketle: bekleme, yeniden işleme/hata, aşırı işlem, devir/taşıma, hareket, stok/kuyruk, kullanılmayan yetenek.
5. Toplam süreyi (işlem + bekleme), toplam işlem süresini, akış verimliliğini (işlem ÷ toplam süre) ve zincirleme %C&A'yı (adım %C&A'larının çarpımı) hesapla.
6. Darboğazı (en uzun bekleme veya en düşük kapasiteli adım) ve kaybettirdiği süreye göre ilk 3 israf kaynağını belirle.
7. Haritayı metin zaman çizelgesi veya diyagram kodu olarak çiz; işlem ve beklemeyi gösteren bir zaman merdiveni ekle.
8. Her israf için iyileştirme fikri öner (kaldır, birleştir, paralelleştir, otomatikleştir, parti büyüklüğünü azalt, kaliteyi başa taşı); her birinin tahmini etkisini `[VARSAYIM]` olarak işaretle.
9. Gelecek durum metriklerini (hedef toplam süre, akış verimliliği) yalnızca fikirlerden türetilmiş olarak taslakla; hangi verinin bunları doğrulayacağını belirt.
10. Kullanıcı devam etmek isterse akışı yeniden tasarlamak için `to-be-process`, darboğaz için `five-whys` veya değişiklikleri planlamak için `process-gap-analysis` öner.

## Çıktı formatı
```markdown
# Değer Akışı Haritası: <akış>
Tetikleyici: <...> · Bitiş: <...> · Birim: <...> · Zaman birimi: <saat/gün>

## Adımlar
| # | Adım | Sahibi | İşlem süresi | Sonraki bekleme | %C&A | Sınıf (DK / GDK / İsraf: tür) |
|---|---|---|---|---|---|---|

## Özet Metrikler
| Metrik | Değer |
|---|---|
| Toplam süre (lead time) | ... |
| İşlem süresi | ... |
| Akış verimliliği | ...% |
| Zincirleme %C&A | ...% |

## Zaman Çizelgesi
<metin merdiveni veya diyagram kodu>

## Darboğaz ve Başlıca İsraflar
1. <adım> – <kaybedilen süre> – <israf türü>

## İyileştirme Fikirleri
| Fikir | Hedeflediği | Beklenen etki | Güven |
|---|---|---|---|

## Veri Kalitesi ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her adımda işlem süresi ile bekleme süresi ayrıldı.
- [ ] Özet metrikler adım tablosuyla aritmetik olarak tutarlı.
- [ ] Her rakam girdiden geliyor ya da `[VARSAYIM]` olarak işaretli; hiçbir şey uydurulmadı.
- [ ] Her israfın türü belirtildi ve her fikir belirli bir israfa işaret ediyor.
- [ ] Mevzuatın zorunlu kıldığı kontroller kaldırılacak israf olarak değil GDK olarak sınıflandırıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Toplam sürenin %90'ı beklemeyken işlem süresini optimize etmek. Önce kuyruklara, devir teslimlere ve parti büyüklüğüne odaklan.
- Süreç sahibinin verdiği en iyi durum sürelerini kullanmak. Tipik ve en kötü durumu sor ya da gerçek zaman damgalarını kullan.
- Yeniden işleme döngülerini göz ardı etmek. Düşük %C&A'lı bir adım sonraki beklemeleri katlar; bunu göster.

## Örnek
Girdi: "Kazanım ~12 gün sürüyor: başvuru kontrolü 30 dk, sonra 3 gün bekliyor; KYC incelemesi 1 saat, belgeler için 5 gün bekliyor; hesap açılışı 20 dk, batch için 2 gün bekliyor; hoş geldin araması 15 dk."

Çıktıdan bir bölüm:
| Metrik | Değer |
|---|---|
| Toplam süre | ~10,1 gün (belirtilen 12 günün ~2 günü açıklanamıyor `[VARSAYIM]`: nerede olduğunu sor) |
| İşlem süresi | 2 sa 05 dk |
| Akış verimliliği | ~%0,9 (24 saatlik gün üzerinden) |

Başlıca israf: KYC sonrası müşteri belgelerini bekleme (5 gün) – fikir: belgeleri incelemeden sonra değil başvuru anında iste.
