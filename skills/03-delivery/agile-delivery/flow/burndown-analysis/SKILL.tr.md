---
description: "Bir iterasyon veya sürüm için burndown ve burnup grafiklerini ya da bunların günlük verisini yorumlar: grafiğin şeklini okur, ilerlemeyi kapsam değişikliğinden ayırır, geç düşüş, yatay çizgi ve kapsam kayması gibi örüntüleri tespit eder, riskleri önerilen aksiyonlarla işaretler. Biri burndown/burnup grafiği veya günlük kalan iş rakamlarını paylaştığında ya da iterasyonun veya sürümün yolunda olup olmadığını sorduğunda kullanılır."
related: "velocity-analysis, monte-carlo-forecast, daily-sync-summary, iteration-planning, project-status-report"
prompt: "Sprintin 10 gününden 7.'sindeyiz. Günlere göre kalan puan: 40, 40, 38, 38, 38, 35, 35. 4. gün iki hikâye eklendi. Yetişecek miyiz?"
---

# Burndown/Burnup Analizi

## Amaç
Bir burndown veya burnup grafiğinin iterasyon ya da sürüm hedefine ulaşma olasılığı hakkında gerçekte ne söylediğini açıklamak, gerçek ilerlemeyi kapsam hareketinden ayırmak ve bu okumayı işe yarayacak kadar erken somut aksiyonlara dönüştürmek.

## Ne zaman kullanılır
- İterasyon veya sürüm ortasında "yolunda mıyız?" kontrolü yapılırken.
- Grafiğin alışılmadık bir şekli (yatay, basamaklı, yükselen) var ve yorum isteniyor.
- Kanıta dayalı bir ilerleme cümlesi gerektiren durum mesajı hazırlanırken.

## Ne zaman kullanılmaz
- Birçok iterasyon boyunca teslim hızını analiz etmek için `velocity-analysis` kullanılır.
- Olasılıklarla bitiş tarihi öngörmek için `monte-carlo-forecast` kullanılır.
- Tek tek maddelerin neden uzun sürdüğünü teşhis etmek için `cycle-time-analysis` kullanılır.

## Girdiler
Zorunlu:
- Grafik ya da kalan işin (burndown) veya tamamlanan iş ile toplam kapsamın (burnup) günlük/dönemsel serisi, ayrıca dönem uzunluğu ve içinde bulunulan gün.

İsteğe bağlı, kaliteyi artırır:
- Tarihleriyle kapsam değişiklikleri, iterasyon/sürüm hedefi.
- Birim (puan, madde, saat) ve maddelerin yalnızca tamamen bitince sayılıp sayılmadığı.
- Bilinen olaylar (tatiller, olaylar, bloke maddeler).

Veri veya içinde bulunulan gün eksikse sor. Net göremediğin bir görselden değer okuma; rakamları iste.

## Süreç
1. Veriyi gün/dönem bazında tabloya dök: kalan (veya biten), toplam kapsam, ideal çizgi değeri. Birimi ve sayma kuralını not et.
2. Kapsam değişikliğini ilerlemeden ayır: her dönem için tamamlanan = önceki kalan − güncel kalan + eklenen kapsam. Kapsam değişikliklerini açıkça göster; kapsam oynuyorsa burnup görünümünü tercih et.
3. Gerçekleşeni idealle karşılaştır: içinde bulunulan gündeki farkı birim olarak ve ilk taahhüdün yüzdesi olarak ver.
4. Örüntüyü ve olağan nedenlerini belirle:
   - Birkaç gün yatay: iş bitmiyor, maddeler büyük, bloke iş var ya da pano güncellenmiyor.
   - Geç uçurum: maddeler çok büyük veya yalnızca sonda bitiyor; test toplu yapılıyor.
   - Yükselen çizgi: kapsam, tamamlanandan hızlı ekleniyor.
   - İstikrarlı ama idealin üstünde: fazla taahhüt veya düşük tahmin.
   - Başta idealin altında: olası eksik taahhüt veya önce kolay maddeler.
5. Bitişi projekte et: son birkaç dönemin ortalama tamamlanma hızıyla dönem sonunda kalacak işi tahmin et. Aralık olarak sun ve `[PROJEKSİYON]` olarak etiketle.
6. Hedef riskini değerlendir: tüm maddeler bitmese de hedef için kritik maddeler bitecek mi? Ölçüt toplam değil, hedeftir.
7. Kalan süreye uygun 2-4 aksiyon listele: en eski maddeye ekipçe odaklanmak, product owner ile kapsamı bölmek veya çıkarmak, bir engeli kaldırmak, yeni madde başlatmayı durdurmak.
8. Grafiği güvenilmez kılan veri kalitesi sorunlarını (her gün yeniden tahmin edilen saatler, kısmi puan, güncellenmeyen pano) not et.
9. Kullanıcının hedefi devam ediyorsa engelleri ekiple ele almak için `daily-sync-summary`, sürüm düzeyinde öngörü için `velocity-analysis` / `monte-carlo-forecast` öner.

## Çıktı formatı
```markdown
# Burndown Okuması – <iterasyon/sürüm>, <m> günün <n>. günü
Birim: <...> · Hedef: <hedef veya [BİLİNMİYOR]>

| Gün | Kalan | Kapsam | İdeal | O gün tamamlanan | Eklenen kapsam |
|---|---|---|---|---|---|

**Durum:** Yolunda / Riskli / Yolunda değil
**Örüntü:** <ad> – <kanıt>
**Dönem sonu projeksiyonu:** <aralık> kalan [PROJEKSİYON]
**Hedef riski:** <hedef için kritik hangi maddeler risk altında>

## Aksiyonlar
1. <aksiyon> – <sorumlu rol> – <ne zamana kadar>

## Veri Uyarıları
- ...
```

## Kalite kontrol listesi
- [ ] Kapsam değişikliği ve tamamlanan iş ayrı gösterildi.
- [ ] Durum, rakamlarıyla birlikte ideale olan farka ve projeksiyona dayanıyor.
- [ ] Örüntü kanıt ve olası nedenlerle adlandırıldı; çıkarım olan nedenler etiketlendi.
- [ ] Hedef riski toplam kapsamdan ayrı değerlendirildi.
- [ ] Aksiyonlar kalan sürede uygulanabilir.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yatay çizgiyi "hiç iş yapılmadı" diye okumak. Çoğu zaman iş sürüyor ama bitmiyordur; devam eden maddelere ve yaşlarına bak.
- Kapsam kaymasını burndown içinde gizlemek. Kapsam oynuyorsa görünür olması için burnup'a geç.
- İdeal çizgiyi hedef gibi görmek. O bir referanstır; sapma başarısızlık değil bilgidir.

## Örnek
Girdi: 10 günlük sprint, 7. gün; kalan 40, 40, 38, 38, 38, 35, 35; 4. gün iki hikâye (+5) eklendi.

Çıktıdan bir bölüm:
- Şu ana kadar tamamlanan: 40 + 5 − 35 = 7 günde 10 puan (~1,4/gün). 7. gün ideal kalan: 12.
- Örüntü: kapsam eklenmiş, büyük ölçüde yatay – iş bitmiyor ve kapsam kayıyor.
- Projeksiyon: 10. gün sonunda ~31 puan kalır `[PROJEKSİYON]` → Yolunda değil.
- Aksiyon: product owner ile bugün hedef için kritik hikâyelerde uzlaş, 4. gün eklenenleri sprint dışına al.
