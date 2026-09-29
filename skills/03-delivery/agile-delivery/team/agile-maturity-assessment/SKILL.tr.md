---
description: "Bir ekibin veya birimin çeviklik olgunluğunu metodolojiden bağımsız biçimde değerlendirir: pratik alanlarını (müşteri değeri ve ürün sahipliği, planlama ve öngörü, akış ve teslimat, teknik pratikler, kalite, sürekli iyileştirme, ekip özerkliği, paydaş iş birliği) kanıta dayalı 1-5 ölçeğinde puanlar, ortalama almak yerine kısıtı belirler ve gözlemlenebilir sonuçlarla sonraki 2-3 iyileştirmeyi önerir. Bir lider veya koç ekibin gerçekte ne kadar çevik olduğunu sorduğunda, bir dönüşüm öncesi başlangıç değeri gerektiğinde ya da sırada neyin iyileştirileceğine karar verilmek istendiğinde kullanılır."
related: "team-health-check, retrospective-facilitation, wip-policy, engineering-metrics-review, current-state-assessment"
prompt: "Ekibimizin çeviklik olgunluğunu değerlendir. İki haftalık iterasyonlarla çalışıyoruz, sürümler üç ayda bir çıkıyor, product owner yarı zamanlı ve test otomasyonu yok."
---

# Çeviklik Olgunluk Değerlendirmesi

## Amaç
Bir ekibin çalışma biçiminin değeri ne kadar sık, güvenli ve uyarlanabilir biçimde teslim ettiğine dair kanıta dayalı bir tablo sunmak ve bir tören kontrol listesi veya gösteriş puanı yerine en çok kilidi açacak az sayıdaki iyileştirmeyi işaret etmek.

## Ne zaman kullanılır
- Çevik dönüşüm öncesinde veya sırasında bir başlangıç değeri gerektiğinde.
- Bir lider veya koç bir ekip ya da ekip grubu için "neredeyiz, sırada ne var?" diye sorduğunda.
- İyileştirmelerin yerleşip yerleşmediğini görmek için dönemsel yeniden değerlendirmede.

## Ne zaman kullanılmaz
- Ekip moralini ve algılanan sağlığı ölçmek için `team-health-check` kullanılır.
- Teslimat metriklerini derinlemesine analiz etmek için `engineering-metrics-review` kullanılır.
- Danışmanlık bağlamında bir müşterinin tüm BT organizasyonunu değerlendirmek için `current-state-assessment` kullanılır.

## Girdiler
Zorunlu:
- Ekibin bugün nasıl çalıştığının anlatımı (planlama, teslimat ve sürüm sıklığı, roller, kalite pratikleri, geri bildirim döngüleri) ya da bir değerlendirme anketinin yanıtları.

İsteğe bağlı, kaliteyi artırır:
- Metrikler: deployment sıklığı, değişiklik teslim süresi, değişiklik hata oranı, toparlanma süresi (DORA), döngü süresi, üretime kaçan hatalar.
- Eserler: backlog, pano görüntüsü, bitti tanımı, retrospektif aksiyonları.
- Değerlendirmenin hedefleri ve kurumun hâlihazırda kullandığı bir olgunluk modeli varsa o.

Anlatım zayıfsa en fazla 5 hedefli soru sor (sürüm sıklığı, öncelikleri kimin belirlediği, kalitenin nasıl güvenceye alındığı, kullanıcıların ne sıklıkla geri bildirim verdiği, son retrospektiften sonra ne değiştiği). Yanıtlanmayan alanları `[YETERSİZ KANIT]` olarak puanla, asla tahmin etme.

## Süreç
1. Kapsamı (tek ekip, birkaç ekip, bir departman) ve amacı (başlangıç değeri, iyileştirme planlaması, yeniden değerlendirme) teyit et. Sonucun bir performans değerlendirmesi olmadığını belirt.
2. Herhangi bir çerçeveden bağımsız pratik alanları kullan: müşteri değeri ve ürün sahipliği; planlama ve öngörü; akış ve teslimat; teknik pratikler (entegrasyon, otomasyon, deployment); yerleşik kalite; sürekli iyileştirme; ekip özerkliği ve roller; paydaş iş birliği ve geri bildirim.
3. Her alan için gözlemlenebilir çapaları olan bir 1-5 ölçeği tanımla (1 = gelişigüzel, 3 = ekip içinde tutarlı, 5 = sürekli optimize ediliyor ve ölçülüyor). Çapaları puanlamadan önce yaz.
4. Her alanı yalnızca girdideki kanıta göre puanla ve kanıtı belirt. Kanıtsız iddiaları `[İDDİA]`, bilgi olmayan alanları `[YETERSİZ KANIT]` olarak işaretle.
5. Sonuçlarla çapraz kontrol yap: DORA veya akış metrikleri varsa pratik puanlarıyla karşılaştır; yüksek pratik puanı ile zayıf sonuçlar, pratiğin etkili değil ritüel olduğunu gösterir.
6. Kısıtı belirle: diğerlerini sınırlayan en düşük alan (ör. üç aylık sürümler, iterasyon planlaması ne olursa olsun geri bildirim döngüsünü kısıtlar). Alanların ortalamasını alarak tek bir manşet puan üretme.
7. Kısıtı hedefleyen sonraki 2-3 iyileştirmeyi öner; her birinin gözlemlenebilir bir sonucu, ilk deneyi ve kontrol aralığı olsun (ör. "3 ay içinde en az 2 haftada bir üretime deployment").
8. Henüz yapılmaması gerekenleri listele (önce kısıtın çözülmesine bağlı iyileştirmeler).
9. Yeniden değerlendirmenin nasıl yapılacağını tanımla: aynı alanlar ve çapalar, toplanacak kanıt, tarih. İnsan tarafı için `team-health-check`, seçilen iyileştirmeleri başlatmak için `wip-policy` veya `retrospective-facilitation` öner.

## Çıktı formatı
```markdown
# Çeviklik Olgunluk Değerlendirmesi – <ekip/birim>, <tarih>
Amaç: <...> · Kullanılan kanıt: <anlatım, metrikler, eserler>

| Pratik alanı | Puan (1-5) | Kanıt | Bir sonraki seviyeye fark |
|---|---|---|---|

Sonuç metrikleri (varsa): <deployment sıklığı, teslim süresi, değişiklik hata oranı, toparlanma süresi, döngü süresi>

## Ana Kısıt
<alan> – <diğerlerini neden sınırlıyor>

## Sonraki İyileştirmeler (2-3)
| İyileştirme | Gözlemlenebilir sonuç | İlk deney | Kontrol zamanı |
|---|---|---|---|

## Henüz Değil
- ...

## Kanıt Boşlukları ve Açık Sorular
- ...

## Yeniden Değerlendirme
<tarih, aynı çapalar>
```

## Kalite kontrol listesi
- [ ] Her puan bir kanıta dayanıyor ya da `[İDDİA]` / `[YETERSİZ KANIT]` olarak işaretli.
- [ ] Ölçek çapaları gözlemlenebilir ve puanlamadan önce yazıldı.
- [ ] Hedef durum olarak belirli bir çerçeve varsayılmadı.
- [ ] Metrik varsa pratikler sonuçlarla çapraz kontrol edildi.
- [ ] Ortalama bir genel puan yerine tek bir kısıt adlandırıldı.
- [ ] İyileştirmelerin gözlemlenebilir sonuçları ve kontrol aralıkları var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sonuçlar yerine törenleri puanlamak (hiçbir şey değişmiyorsa "retrospektif yapıyorlar" olgunluk değildir).
- Tam bir çerçeve kurulumunu önermek. Bunun yerine kısıtı küçük bir deneyle hedefle.
- Ekipleri puana göre karşılaştırmak. Bağlamlar farklıdır; puanları her ekibin kendi sonraki adımına yön vermek için kullan.

## Örnek
Girdi: iki haftalık iterasyonlar, üç ayda bir sürüm, yarı zamanlı product owner, test otomasyonu yok.

Çıktıdan bir bölüm:
| Pratik alanı | Puan | Kanıt |
|---|---|---|
| Planlama ve öngörü | 3 | İterasyonlar tutarlı planlanıyor [İDDİA] |
| Akış ve teslimat | 1 | Sürümler üç ayda bir |
| Teknik pratikler | 1 | Test otomasyonu yok |
- Ana kısıt: sürüm ve test otomasyonu – iterasyon sıklığı ne olursa olsun kullanıcı geri bildirimi üç ayda bir geliyor.
- İyileştirme: en önemli 5 kullanıcı yolculuğunun regresyonunu otomatikleştir ve 2 haftada bir pilot gruba sürüm çıkar; 3 ay sonra kontrol et.
