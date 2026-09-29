---
name: ab-test-analysis
description: "Bir A/B veya çok değişkenli testi baştan sona analiz eder; geçerlilik kontrolleri (örneklem oranı uyumsuzluğu, maruziyet, süre), güven aralığıyla birincil metrik etkisi, koruyucu metrikler, segmentler ve yayına al / iyileştir / durdur önerisi. Deney sonuçları geldiğinde ve karar gerektiğinde ya da bir test sonucunun anlamlı veya güvenilir olup olmadığı sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-analyst
  area: analytics
  title: "A/B testi analizi"
  related: "experiment-design, hypothesis-statement, metric-definition, insight-summary, analysis-plan"
  prompt: "Bu A/B testini analiz et: kontrol 48.210 kullanıcı %2,31 dönüşüm, varyant 48.950 kullanıcı %2,52 dönüşüm, 14 gün sürdü; koruyucu metrik iade oranı."
---

# A/B Testi Analizi

## Amaç
Bir değişikliğin yayına alınıp alınmayacağına tek bir p-değerine veya umut verici görünen bir grafiğe göre değil; geçerli bir test, dürüst bir etki tahmini ve koruyucu metrikler üzerinden karar vermek.

## Ne zaman kullanılır
- Bir deney bittiğinde (veya planlanan örnekleme ulaştığında) ve karar verilmesi gerektiğinde.
- Paydaşlar ara sonuçlara bakıp testi erken durdurmak istediğinde.
- Bir sonuç şaşırtıcı derecede büyük göründüğünde veya diğer kanıtlarla çeliştiğinde.

## Ne zaman kullanılmaz
- Test henüz tasarlanmadıysa `experiment-design` kullanılır.
- Rastgele atanmış bir kontrol grubu yoksa (önce/sonra, bölgesel dağıtım) yarı deneysel bir yöntemle `analysis-plan` kullanılır.
- Yalnızca üzerinde uzlaşılmış bir sonucun iletilmesi gerekiyorsa `insight-summary` kullanılır.

## Girdiler
Zorunlu:
- Her varyant için: atanan birim sayısı, analiz edilen birim sayısı ve birincil metrik değerleri (sayılar veya ortalama ve standart sapma).

İsteğe bağlı, kaliteyi artırır:
- Önceden kayda geçirilmiş hipotez, minimum tespit edilebilir etki, planlanan süre ve örneklem büyüklüğü.
- Koruyucu ve ikincil metrikler, segment kırılımları, günlük veri.

Varyant bazındaki sayılar yoksa iste. Varsayılan değerlerden istatistik hesaplama.

## Süreç
1. Hipotezi, birincil metriği, rastgeleleştirme birimini ve planlanan örneklemi/süreyi yeniden yaz. Bilinmeyen ön kaydı `[BİLİNMİYOR]` olarak işaretle.
2. Geçerlilik kontrolleri: örneklem oranı uyumsuzluğu (SRM; atama sayılarına planlanan oran üzerinden ki-kare), maruziyet/tetiklenme doğruluğu, tam iş döngülerinin kapsanması (en az tam haftalar), test sırasında değişiklik yapılmaması, günlük trendde yenilik veya alışkanlık etkileri.
3. Rastgeleleştirme birimi analiz biriminden farklıysa (ör. kullanıcı ve oturum) varyans sorununu not et; delta yöntemini veya rastgeleleştirme birimine toplulaştırmayı tercih et.
4. Birincil etkiyi hesapla: mutlak ve göreli fark, uygun testle güven aralığı ve p-değeri (oranlar için iki oranlı z-testi, ortalamalar için Welch t-testi; kalın kuyruklu metriklerde kırpma veya bootstrap düşün). Hesap girdilerini göster.
5. Sonucu yalnızca sıfırla değil, minimum tespit edilebilir / pratik olarak anlamlı etkiyle karşılaştır. Anlamlı değilse gücü (power) raporla.
6. Koruyucu metrikleri aşağı kalmama (non-inferiority) bakışıyla değerlendir; eşiği aşan herhangi bir koruyucu metrik, birincil sonuç ne olursa olsun yayını engeller.
7. Yalnızca önceden belirlenmiş segmentleri incele; plansız segment bulgularını hipotez olarak ele al ve çoklu karşılaştırma için düzeltme yap (ör. Holm veya Benjamini-Hochberg).
8. Ardışık (sequential) tasarım olmadan ara sonuçlara bakıldıysa hata oranının şiştiğini belirt.
9. Öneri ver: yayına al, bir alt kümeye yayına al, iyileştir, uzat (güç yetersizse ve gerekçeliyse) veya durdur. Öneriyi eşiklere bağla.
10. Deney kaydı için öğrenimleri not et.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Kullanıcının hedefi devam ediyorsa kararı aktarmak için `insight-summary` veya takip testi için `experiment-design` öner.

## Çıktı formatı
```markdown
# A/B Test Sonucu: <test adı>
| Alan | Değer |
|---|---|
| Hipotez | ... |
| Birincil metrik | ... |
| Rastgeleleştirme birimi / oran | ... |
| Tarihler / süre | ... |
| Karar | Yayına al / Alt kümeye al / İyileştir / Uzat / Durdur |

## Geçerlilik
| Kontrol | Sonuç | Durum |
|---|---|---|
| Örneklem oranı uyumsuzluğu | p = ... | Tamam / BAŞARISIZ |
| Tam haftalık döngüler | ... | ... |

## Birincil Sonuç
| Varyant | n | Metrik | Mutlak fark | Göreli fark | %95 GA | p |
|---|---|---|---|---|---|---|

## Koruyucu Metrikler
| Metrik | Kontrol | Varyant | Eşik | Durum |
|---|---|---|---|---|

## Segmentler (önceden belirlenmiş)
- ...

## Öneri ve Gerekçe
...

## Uyarılar ve Öğrenimler
- ...
```

## Kalite kontrol listesi
- [ ] Etki yorumlanmadan önce SRM ve maruziyet kontrolleri yapıldı.
- [ ] Etki güven aralığıyla, hem mutlak hem göreli olarak raporlandı.
- [ ] Seçilen test metrik tipine ve rastgeleleştirme birimine uygun.
- [ ] Koruyucu metrikler değerlendirildi ve kararı veto edebiliyor.
- [ ] Segment bulguları önceden belirlenmiş veya keşifsel olarak etiketlendi.
- [ ] Tüm sayılar girdiden hesaplandı; bilinmeyen değerler işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İlk anlamlı ara bakışta kazanan ilan etmek. Planlanan örneklemi veya ardışık bir yöntemi kullan.
- SRM'yi yok saymak; başarısız bir SRM, p-değeri ne olursa olsun sonucu geçersiz kılar.
- Gücü yetersiz bir testte "etki yok" demek. "Sonuçsuz" de ve tespit edilebilir etkiyi belirt.

## Örnek
Girdi: Kontrol 48.210 kullanıcı, %2,31 dönüşüm; varyant 48.950 kullanıcı, %2,52; 14 gün; planlanan oran 50/50; koruyucu metrik iade oranı.

Çıktıdan bir bölüm:
- SRM: 50/50 planda 48.210'a karşı 48.950, ki-kare p ≈ 0,018 – BAŞARISIZ; etkiye güvenmeden önce atama mekanizmasını incele.
- Birincil (yalnızca bilgi için): mutlak +0,21 puan, göreli +%9,1; %95 GA yaklaşık +0,02 ile +0,40 puan.
- Öneri: Henüz yayına alma; atama sorununu düzelt ve testi tekrarla. İade oranı koruyucu metriği `[veri verilmedi]`.
