---
name: value-proposition-canvas
description: "Tek bir müşteri segmenti için değer önerisi kanvasını doldurur; müşteri işlerini, sorunlarını ve kazanımlarını ürün ve hizmetlerle, sorun gidericilerle ve kazanım yaratıcılarla eşler, bunları önem sırasına koyar, problem-çözüm uyumunu kontrol eder ve sınanacak varsayımları listeler. Bir değer önerisi tanımlanırken veya keskinleştirilirken, bir ürün fikrinin gerçek sorunlara dokunup dokunmadığı kontrol edilirken, konumlandırma veya keşif çalışması hazırlanırken ya da \"değer önerisi kanvası\" veya \"uyum\" analizi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: discovery
  title: "Değer önerisi kanvası"
  related: "jobs-to-be-done, persona, positioning-statement, business-model-canvas, hypothesis-statement"
  prompt: "Orta ölçekli distribütörlerdeki saha satış temsilcileri için masraf uygulamamızın değer önerisi kanvasını doldur."
---

# Değer Önerisi Kanvası

## Amaç
Bir ürünün hangi müşteri işlerini, sorunlarını ve kazanımlarını nasıl karşıladığını açık hâle getirmek; böylece ekip uyumun nerede güçlü olduğunu, nerede iddia edilip kanıtlanmadığını ve sırada neyin sınanacağını görebilir.

## Ne zaman kullanılır
- Yeni bir ürün veya özellik fikri belirli bir segment için net bir değer önerisine ihtiyaç duyuyorsa.
- Mevcut bir ürünün mesajları özellik odaklıysa ve müşteri sonuçlarına bağlanması gerekiyorsa.
- Keşif bulguları (görüşmeler, destek kayıtları) ürün kararlarına bağlanacaksa.

## Ne zaman kullanılmaz
- Müşterinin yapmaya çalıştığı işler henüz anlaşılmamışsa önce `jobs-to-be-done` kullanılır.
- İşin tamamı (kanallar, gelir, maliyet) tasarlanacaksa `business-model-canvas` kullanılır.
- Tek cümlelik bir pazar konumlandırması gerekiyorsa `positioning-statement` kullanılır.

## Girdiler
Zorunlu:
- Tek bir müşteri segmenti (belirli rol ve bağlam) ve ürün ya da fikir.

İsteğe bağlı, kaliteyi artırır:
- Araştırma kanıtları: görüşme notları, anket sonuçları, destek verileri, kazanma/kaybetme notları, analitik.
- Segmentin bugün kullandığı rakip alternatifler.

Birden fazla segment verilmişse hangisiyle başlanacağını sor; her segment için ayrı kanvas hazırla. Araştırma kanıtı yoksa kanvası hipotez olarak hazırla ve her maddeyi `[VARSAYIM]` olarak etiketle.

## Süreç
1. Segmenti (rol, bağlam, durum) ve incelenen ürün kapsamını kesin tanımla.
2. Müşteri işleri: işlevsel, sosyal ve duygusal işleri, ayrıca destekleyici işleri (satın alma, öğrenme, bakım) listele. Her birini ürünü anmadan fiil + nesne + bağlam olarak yaz.
3. Sorunlar: işlerin etrafındaki istenmeyen sonuçlar, engeller ve riskler. Belirsiz ("yavaş") değil somut yaz ("temsilciler fişleri gece yeniden yazıyor, haftada ~30 dk `[VARSAYIM]`").
4. Kazanımlar: gerekli, beklenen, arzu edilen ve beklenmedik sonuçlar. Mümkünse ölçülebilir yaz.
5. İşleri, sorunları ve kazanımları bu segment için önem ve şiddete göre sırala ve her birini kanıtla etiketle: `[KANIT: kaynak]` veya `[VARSAYIM]`.
6. Ürün ve hizmetler: teklifin neleri içerdiğini (özellikler, hizmet, destek, entegrasyonlar) pazarlama dili kullanmadan listele.
7. Sorun gidericiler: sıralamanın üstündeki her sorun için teklifin onu nasıl giderdiğini yaz; kazanım yaratıcılar: üst sıradaki her kazanım için onu nasıl yarattığını yaz. Bağlantıları açıkça kur (sorun ↔ giderici, kazanım ↔ yaratıcı).
8. Uyumu değerlendir: üst sıradaki her sorun/kazanımı karşılanıyor, kısmen karşılanıyor veya karşılanmıyor olarak işaretle; hiçbir iş, sorun veya kazanıma bağlanmayan özellikleri belirt.
9. Mevcut alternatifle (hiçbir şey yapmamak dahil) karşılaştır: segment neden geçiş yapsın?
10. Uyumun dayandığı en riskli varsayımları her biri için ucuz bir testle listele, tek cümlelik bir değer önerisi yaz ve testleri biçimlendirmek için `hypothesis-statement`, mesajlar için `positioning-statement` veya geniş model için `business-model-canvas` öner.

## Çıktı formatı
```markdown
# Değer Önerisi Kanvası: <segment> için <ürün>

## Müşteri Profili
| Tür | Madde | Sıra | Kanıt |
|---|---|---|---|
| İş (işlevsel) | ... | 1 | [KANIT: 8 görüşmenin 6'sı] |
| Sorun | ... | 1 | [VARSAYIM] |
| Kazanım | ... | 2 | ... |

## Değer Haritası
| Ürün ve hizmetler | Sorun gidericiler (→ sorun) | Kazanım yaratıcılar (→ kazanım) |
|---|---|---|

## Uyum Değerlendirmesi
| Üst sıradaki sorun / kazanım | Karşılanıyor mu? (Evet / Kısmen / Hayır) | Nasıl | Boşluk |
|---|---|---|---|
- Bağlantısız özellikler: ...
- Mevcut alternatiften neden geçilsin: ...

## Değer Önerisi (tek cümle)
<iş>'i yapan <segment> için <ürün>, <alternatif>'ten farklı olarak <en önemli sorunu giderir / en önemli kazanımı yaratır>.

## En Riskli Varsayımlar ve Testler
| Varsayım | Test | Başarı sinyali |
|---|---|---|
```

## Kalite kontrol listesi
- [ ] Kanvas tam olarak tek ve belirli bir segmenti kapsıyor.
- [ ] İşler, sorunlar ve kazanımlar müşterinin bakışından yazılmış ve ürünü anmıyor.
- [ ] Her madde kanıtla veya `[VARSAYIM]` ile etiketli ve maddeler sıralanmış.
- [ ] Üst sıradaki her sorun ve kazanımın açık bir bağlantısı var ya da boşluk olarak işaretli; bağlantısız özellikler belirtilmiş.
- [ ] En riskli varsayımların her birinin somut ve ucuz bir testi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Değer haritasından başlayıp sorunları özelliklere uyacak şekilde tersine türetmek. Önce müşteri profilini doldur.
- Genel sorunlar ("verimlilik istiyor"). Belirli durumu, sıklığı ve sonucu yaz.
- Segmentleri karıştırmak; bir finans direktörü ile bir saha temsilcisinin işleri farklıdır. Her segment için bir kanvas.

## Örnek
Girdi: "Orta ölçekli distribütörlerdeki saha satış temsilcileri için masraf uygulaması."

Çıktıdan bir bölüm:
Zayıf sorun: "Masraf raporlamak can sıkıcı."
Güçlü sorun: "Temsilci çok günlü rotalarda kâğıt yakıt fişlerini kaybediyor ve geri ödenemeyince cebinden ödüyor" – Sıra 1 – `[VARSAYIM: 5 temsilci görüşmesinde doğrula]`.
| Üst sıradaki sorun / kazanım | Karşılanıyor mu? | Nasıl | Boşluk |
|---|---|---|---|
| Kaybolan fiş → geri ödenmeyen masraf | Evet | Pompada fotoğraf çekme, çevrimdışı eşitleme | OCR termal kâğıtta çalışırsa yok `[test et]` |
| Bir hafta içinde geri ödeme | Kısmen | Daha hızlı gönderim | Onay hızı uygulamaya değil yöneticilere bağlı |
