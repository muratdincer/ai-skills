---
description: Sonuçları özgün hedefler ve temel planlarla karşılaştıran, kapsam, takvim, maliyet ve kalite sapmalarını açıklayan, kabulü ve operasyona devri teyit eden, açık maddeleri sahipleriyle listeleyen, öğrenilen dersleri kaydeden ve fayda takibini kuran bir proje kapanış raporu yazar. Bir proje veya faz sona ererken, sponsorun resmî bir kapanış kararına ihtiyacı olduğunda ya da iptal edilen bir projenin düzenli biçimde kapatılması gerektiğinde kullanılır.
related: acceptance-certificate, handover-document, lessons-learned, benefits-realization, earned-value-analysis
prompt: CRM taşıma projemiz geçen ay canlıya çıktı. Proje başlatma belgesi, son durum raporu ve gerçekleşen bütçeden kapanış raporunu yaz.
---

# Proje Kapanış Raporu

## Amaç
Bir projeyi veya fazı, söz verilene karşı neyin teslim edildiğinin, neyin kaldığının ve kimin sahiplendiğinin dürüst bir dökümüyle resmî olarak kapatmak. Böylece sponsor ekibi ve bütçeyi serbest bırakabilir, kurum da bu deneyimden öğrenir.

## Ne zaman kullanılır
- Son teslimatlar kabul edildiğinde ve proje veya faz sona ererken.
- Bir proje iptal edildiğinde veya durdurulduğunda ve düzenli bir kapanış gerektiğinde.
- Sponsor veya PMO bir kapanış kapısı kararı istediğinde.

## Ne zaman kullanılmaz
- Yalnızca öğrenilen dersler oturumu yapılacaksa `lessons-learned` kullanılır.
- Yalnızca bir sistem desteğe devredilecekse `handover-document` kullanılır.
- Kapanıştan çok sonra faydalar ölçülecekse `benefits-realization` kullanılır.

## Girdiler
Zorunlu:
- Özgün hedefler ve temel planlar (proje başlatma belgesi, kapsam tanımı, takvim, bütçe) ya da temel rakamları.
- Nihai gerçekleşenler: teslim edilen kapsam, tarihler, maliyetler, kabul durumu.

İsteğe bağlı, kaliteyi artırır:
- Son durum raporu, RAID kaydı, değişiklik kaydı, kabul belgeleri, devir kayıtları.
- Öğrenilen ders notları, paydaş geri bildirimi, fayda hipotezleri.

Hedefler veya nihai gerçekleşenler yoksa iste. Sapmaları asla tahminle doldurma.

## Süreç
1. Kapanış türünü (tamamlandı, istisnalarla tamamlandı, iptal edildi, durduruldu) ve kapanış tarihini belirt.
2. Her özgün hedefi ve başarı kriterini, ulaşılan sonuç ve kanıtla listele; henüz ölçülemeyen sonuçları `[TBD – <tarih> itibarıyla ölçülecek]` olarak işaretle.
3. Kapsamı karşılaştır: teslim edilen, kapsamdan çıkarılan (CR referansıyla), eklenen (CR referansıyla) ve teslim edilmeyen.
4. Takvimi ve maliyeti hem özgün hem de son onaylı temel planla karşılaştır; ikisini birlikte göster ki onaylı değişiklikler aşımlardan ayrılsın.
5. Kaliteyi özetle: teslimat bazında kabul durumu, önem derecesine göre açık hatalar, iş biriminin kabul ettiği bilinen kısıtlar.
6. Operasyona devri teyit et: destek modeli, dokümantasyon, erişim, garanti veya hypercare (yoğun destek) dönemi ve bitiş tarihi.
7. Açık maddeleri (sorunlar, riskler, aksiyonlar, hatalar) proje ekibi dışından bir sahip ve bitiş tarihiyle listele; sahipsizleri işaretle.
8. İdari kapanışı tamamla: sözleşmeler ve satınalma siparişleri, lisanslar, ortamlar, erişim hakları, kayıtların arşivlenmesi; bilinmeyen durumları işaretle.
9. Öğrenilen dersleri, benimsemesi gereken sahibiyle birlikte uygulanabilir öneriler olarak özetle.
10. Fayda takibini tanımla: kapanış sonrası hangi fayda, metrik, başlangıç değeri, hedef, ölçüm tarihi ve sahip.
11. İmza satırlarıyla kapanış kararını talep et; kullanıcının hedefi devam ediyorsa `lessons-learned`, `handover-document` veya `benefits-realization` öner.

## Çıktı formatı
```markdown
# Proje Kapanış Raporu: <proje>
Kapanış türü: <...> | Kapanış tarihi: <...> | Sponsor: <...> | PM: <...>

## Yönetici Özeti
## Hedefler ve Sonuçlar
| Hedef / başarı kriteri | Hedef değer | Ulaşılan | Kanıt |
## Kapsam
| Madde | Durum (Teslim edildi/Çıkarıldı/Eklendi/Teslim edilmedi) | CR ref |
## Takvim ve Maliyet
| Ölçü | Özgün temel | Son temel | Gerçekleşen | Son temele göre sapma | Ana nedenler |
## Kalite ve Kabul
## Operasyona Devir
## Devredilen Açık Maddeler
| Madde | Tür | Yeni sahip | Bitiş |
## İdari Kapanış
## Öğrenilen Dersler
| Ders | Öneri | Benimseyecek sahip |
## Fayda Takibi
| Fayda | Metrik | Başlangıç | Hedef | Ölçüm tarihi | Sahip |
## Kapanış Onayı
| Rol | Ad | Karar | Tarih |
```

## Kalite kontrol listesi
- [ ] Kaçırılanlar dahil her özgün hedef raporlandı.
- [ ] Sapmalar onaylı değişiklikleri aşımlardan ayırıyor.
- [ ] Her açık maddenin dağılan proje ekibi dışından bir sahibi var.
- [ ] Devir ve hypercare bitiş tarihleri açık ya da `[TBD]` olarak işaretli.
- [ ] Dersler şikâyet veya suçlama değil, uygulanabilir öneriler.
- [ ] Hiçbir rakam uydurulmadı; boşluklar işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca son yeniden temellenmiş planla karşılaştırmak; gerçek hikâye gizlenir. Özgün planı da göster.
- Açık maddeleri ayrılmakta olan kişilere bırakarak kapatmak. Sahipliği açıkça devret.
- İş sonuçları henüz ölçülemezken yalnızca teslimata bakarak başarı ilan etmek. Fayda ölçüm tarihleri belirle.

## Örnek
Girdi: "CRM taşıma ayın 3'ünde canlıya çıktı. Bütçe 800 bin, gerçekleşen 910 bin (onaylı CR +70 bin). Planlanan canlıya geçiş önceki ayın 1'iydi. 12 küçük hata açık."

Çıktıdan bir bölüm:
- Maliyet: Özgün 800 bin, son temel 870 bin, gerçekleşen 910 bin → son temele göre +40 bin (özgüne göre +110 bin, bunun 70 bini onaylı).
- Takvim: canlıya geçiş özgün plandan yaklaşık bir ay geç `[kesin gün sayısını ve nedeni teyit et]`.
- Açık maddeler: 12 küçük hata → uygulama destek ekibi `[sahip adı TBD]`, hypercare içinde `[bitiş tarihi TBD]`.
