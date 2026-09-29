---
name: to-be-process
description: "Mevcut süreç tarifi, sorunlar ve hedeflerden iyileştirilmiş (to-be) bir iş süreci tasarlar: yeniden tasarım kaldıraçlarını (kaldır, sadeleştir, otomatikleştir, paralelleştir, kararı taşı, kontrol ekle) uygular, her değişikliği as-is'e göre gösterir, beklenen etkileri, varsayımları ve gereken sağlayıcıları belirtir. Bir süreç iyileştirilecek, dijitalleştirilecek veya yeniden yapılandırılacaksa ve gereksinim ya da sistem tasarımından önce hedef çalışma biçiminde uzlaşılması gerekiyorsa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: process
  title: "Hedef süreci (to-be) tasarlama"
  related: "as-is-process, process-gap-analysis, bpmn-model, value-stream-map, business-rules-catalog"
  prompt: "Bu mevcut fatura onay süreci ve sorunlarından yola çıkarak onay süresini yarıya indiren bir hedef süreç tasarla."
---

# Hedef Süreci (To-Be) Tasarlama

## Amaç
Sürecin gelecekte nasıl işlemesi gerektiğini, bugüne göre her değişikliği açık ve gerekçeli hâle getirerek tanımlamak. Böylece paydaşlar üzerinde uzlaşabilir, analistler de gereksinimleri ve geçiş işlerini buradan türetebilir.

## Ne zaman kullanılır
- As-is analizi sorunları ortaya koyduktan sonra veya yeni hedefler (maliyet, hız, uyum, müşteri deneyimi) değişiklik gerektirdiğinde.
- Süreci destekleyen yeni veya değişen bir sistemin gereksinimleri yazılmadan önce.
- Birimler, bölgeler veya şirketler arasında süreçler birleştirilirken veya standartlaştırılırken.

## Ne zaman kullanılmaz
- Mevcut süreç henüz anlaşılmadıysa önce `as-is-process` kullanılır.
- Yalnızca fark ve değişiklik aksiyonları listesi gerekiyorsa `process-gap-analysis` kullanılır.
- Gösterim düzeyinde modelleme gerekiyorsa `bpmn-model` kullanılır.

## Girdiler
Zorunlu:
- Mevcut süreç (veya mevcut adımların net bir tarifi).
- İyileştirme hedefleri veya çözülecek problemler. Verilmediyse sorunlardan aday hedefler türet ve teyit iste.

İsteğe bağlı, kaliteyi artırır:
- Kısıtlar: mevzuat, kontroller, değişemeyecek sistemler, bütçe, organizasyonel sınırlar.
- Hedef metrikler, kıyaslama veya referans süreç.

## Süreç
1. Hedefleri ölçülebilir hedef değerler olarak yeniden ifade et (ör. toplam süre, hata oranı, dokunma sayısı); bilinmeyen hedefler `[TBD]` olur.
2. Her as-is sorununa bir kök neden etiketi ver (bekleme, devir, yeniden iş, elle veri girişi, belirsiz kural, eksik bilgi, onay katmanlaşması).
3. Yeniden tasarım kaldıraçlarını adım adım uygula: değer katmayan adımları kaldır, aynı rolün yaptığı adımları birleştir, kararı bilginin olduğu yere taşı, bağımsız işleri paralelleştir, kural tabanlı adımları otomatikleştir, veriyi kaynağında bir kez topla, istisna yönetimli kesintisiz işleme (straight-through) ekle, varyantları standartlaştır.
4. Gerekli kontrolleri (görevler ayrılığı, onay limitleri, denetim izi) koru veya güçlendir; riski kimin kabul ettiğini belirtmeden hiçbir kontrolü kaldırma.
5. To-be adımlarını aktör, sistem, girdi, çıktı, kural ve hedef süreyle yaz; her birini as-is'e göre Yeni / Değişti / Değişmedi / Kaldırıldı olarak işaretle.
6. Otomasyon başarısız olduğunda ne olacağı dahil istisna ve eskalasyon yollarını tanımla.
7. Sağlayıcıları listele: sistem yetenekleri, veri, roller ve beceriler, politika değişiklikleri.
8. Her hedef için etkileri nitel olarak veya verilen veriden açık hesapla tahmin et; varsayımları işaretle.
9. Riskleri ve insanlar üzerindeki değişim etkisini (kaldırılan veya değişen roller, eğitim) not et.
10. Doğrulama öner: süreç sahibiyle üzerinden geçme, simülasyon veya pilot.
11. Kullanıcı devam etmek isterse değişiklikleri iş listesine çevirmek için `process-gap-analysis`, diyagram için `bpmn-model` veya yeni kurallar için `business-rules-catalog` öner.

## Çıktı formatı
```markdown
# Hedef Süreç: <ad>
Sahip: <rol> · Hedefler: <hedef değerler> · Dayandığı as-is: <sürüm/tarih>

## Uygulanan Tasarım İlkeleri
- <ör. veriyi bir kez topla, kaynağında karar ver, istisna bazlı onayla>

## Hedef Adımlar
| # | Adım | Aktör | Sistem | Kural/Karar | Hedef süre | As-is'e göre (Yeni/Değişti/Değişmedi) | Çözdüğü sorun |
|---|---|---|---|---|---|---|---|

## Kaldırılan Adımlar
| As-is adımı | Kaldırılma nedeni | Riski kabul eden |
|---|---|---|

## İstisnalar ve Eskalasyon
- ...

## Kontroller
| Kontrol | Nerede | Tür (önleyici/tespit edici) |
|---|---|---|

## Sağlayıcılar ve Bağımlılıklar
- ...

## Beklenen Etkiler
| Hedef | As-is | To-be (beklenen) | Dayanak |
|---|---|---|---|

## Riskler, İnsan Etkisi ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her değişiklik bir hedefe veya soruna bağlanıyor.
- [ ] Kaldırılan adım ve kontrollerin açık bir risk sahibi var.
- [ ] Her otomatik veya kesintisiz adım için istisna yolu var.
- [ ] Beklenen etkiler dayanağını gösteriyor; uydurulmuş tasarruf rakamı yok.
- [ ] Bir sistem verili kısıt değilse tasarım teknolojiden bağımsız.
- [ ] İnsan etkisi (roller, eğitim) belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Mevcut süreci olduğu gibi otomatikleştirmek. Otomatikleştirmeden önce her adımı sorgula.
- Yalnızca mutlu yolu tasarlamak; eforun çoğunu genellikle istisnalar belirler.
- Veri olmadan süre tasarrufu vaat etmek. Hesabı göster veya `[VARSAYIM]` olarak işaretle.

## Örnek
Girdi: Elle veri girişi ve e-posta onaylı mevcut fatura onayı; hedef: toplam süreyi yarıya indirmek.

Çıktıdan bir bölüm:
| # | Adım | Aktör | Sistem | Kural/Karar | As-is'e göre | Çözdüğü sorun |
|---|---|---|---|---|---|---|
| 1 | Fatura verisini yakala | Sistem | Fatura yakalama/OCR `[VARSAYIM]` | Tedarikçi ve siparişi doğrula | Değişti (elle idi) | Elle veri girişi |
| 2 | Eşleşen faturayı otomatik onayla | Sistem | ERP | Tolerans içinde üçlü eşleşme `[TBD]` | Yeni | Onay beklemesi |
| 3 | İstisnaları onayla | Bütçe sahibi | İş akışı kutusu | `[TBD]` gün sonra hatırlatma, vekile eskalasyon | Değişti | Telefonla takip |
