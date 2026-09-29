---
description: Analiz sonuçlarını, sorgu çıktılarını veya grafikleri kısa bir "ne anlama geliyor" içgörü özetine dönüştürür; ana bulgu, kanıt, güven düzeyi, etkiler ve önerilen aksiyon. Rakamlar hazır olduğunda ama kitlenin ne anlama geldiğini ve ne yapılacağını bilmesi gerektiğinde kullanılır; örneğin bir analizden, aylık gözden geçirmeden veya dashboard'daki bir anomaliden sonra.
related: analysis-plan, executive-summary, ab-test-analysis, dashboard-spec, presentation-outline
prompt: Şu sonuçlardan içgörü özeti yaz: Q3'te müşteri kaybı %3,1'den %4,0'a çıktı, çoğunlukla aylık plandaki KOBİ segmentinde.
---

# İçgörü Özeti Yazma

## Amaç
Veri sonuçlarını, ne olduğunu, neden önemli olduğunu, ne kadar emin olunduğunu ve sonra ne yapılacağını anlatan karar odaklı bir anlatıya çevirmek. Böylece paydaşlar analizi yeniden istemek yerine bulguya göre harekete geçer.

## Ne zaman kullanılır
- Bir analiz tamamlandığında ve analist olmayanlara aktarılması gerektiğinde.
- Düzenli bir gözden geçirmede (haftalık/aylık) grafiklerin ötesinde yorum gerektiğinde.
- Bir dashboard anomali gösterdiğinde ve yönetim "ne oluyor?" diye sorduğunda.

## Ne zaman kullanılmaz
- Analiz henüz kapsamlandırılmamış veya yapılmamışsa `analysis-plan` kullanılır.
- Sonuçlar yayına alma kararı gerektiren kontrollü bir deneyden geliyorsa `ab-test-analysis` kullanılır.
- İhtiyaç veri dışı içeriğin genel bir yönetici özetiyse `executive-summary` kullanılır.

## Girdiler
Zorunlu:
- Sonuçlar: sayılar, tablolar, grafik açıklamaları veya analist notları.

İsteğe bağlı, kaliteyi artırır:
- Orijinal soru ve hedef kitle.
- Metrik tanımları, zaman pencereleri, veri uyarıları.
- İş bağlamı (lansmanlar, olaylar, mevsimsellik).

Sonuçlar yoksa iste. Girdide olmayan hiçbir sayıyı doldurma.

## Süreç
1. Hedef kitleyi ve sahip olduğu kararı belirle; o karar için yaz.
2. En önemli tek bulguyu çıkar ve yön, büyüklük ve kapsam içeren bir başlık cümlesi olarak yaz ("KOBİ kaybı Q3'te 0,9 puan arttı ve toplam artışın %80'ini oluşturdu").
3. Gözlemi (verinin gösterdiği) yorumdan (neden) ayır; yorumları kanıt düzeyiyle etiketle: doğrulanmış, muhtemel, hipotez.
4. Büyüklüğü bağlamla kontrol et: mutlak ve göreli değişim, taban büyüklüğü, olağan dalgalanma, mevsimsellik, geçen yılla karşılaştırma.
5. Girdi destekliyorsa değişimi ayrıştır (karma ve oran etkisi, segment katkısı); desteklemiyorsa takip analizi olarak not et.
6. Sonucu değiştirebilecek uyarıları yaz: veri boşlukları, tanım değişiklikleri, küçük örneklemler, izleme sorunları.
7. Etkilere çevir: gelir, maliyet, müşteri veya risk üzerindeki etki; rakam verilmediyse nitel olarak.
8. Sorumlularıyla 1-3 aksiyon öner; güven düşükse sonraki analizleri öner.
9. Tek ekrana sığdır; destekleyici tabloları eke koy.

## Çıktı formatı
```markdown
# İçgörü: <başlık cümlesi>
**Kitle:** <rol> | **Dönem:** <pencere> | **Güven:** Yüksek / Orta / Düşük

## Ne oldu
- <girdideki sayılarla gözlem>

## Neden (kanıt düzeyi)
- <etken> – doğrulanmış / muhtemel / hipotez – <kanıt>

## Ne anlama geliyor
- <karara etkisi>

## Önerilen aksiyonlar
1. <aksiyon> – <sorumlu veya [BİLİNMİYOR]> – <ne zamana>

## Uyarılar
- ...

## Sonraki sorular
- ...
```

## Kalite kontrol listesi
- [ ] Başlık tek cümlede yön, büyüklük ve kapsamı veriyor.
- [ ] Her sayı girdiye dayanıyor; sessizce tahmin edilen bir şey yok.
- [ ] Yorumlar kanıt düzeyiyle etiketli.
- [ ] Mutlak ve göreli değişim karıştırılmadı (puan ve %).
- [ ] En az bir somut aksiyon önerildi.
- [ ] Sonucu tersine çevirebilecek uyarılar görünür.

## Sık yapılan hatalar
- Her grafiği tek tek anlatmak ("A metriği arttı, B azaldı"). Önemli olan tek bulguyla başla.
- Korelasyonu neden gibi sunmak. Nedensellik test edilmediyse "ile eş zamanlı" ifadesini kullan.
- Çok küçük bir tabandaki göreli değişimi ("+%200") mutlak sayılar olmadan vermek.

## Örnek
Girdi: "Q3'te müşteri kaybı %3,1'den %4,0'a çıktı, çoğunlukla aylık plandaki KOBİ'lerde. Aylık plan zammı temmuzda devreye girdi."

Çıktıdan bir bölüm:
- Başlık: Q3'te müşteri kaybı 0,9 puan arttı; artış aylık plandaki KOBİ müşterilerinde yoğunlaştı.
- Neden: Temmuzdaki aylık plan zammıyla eş zamanlı – muhtemel – zamanlama örtüşüyor; henüz ayrılış anketi verisi yok `[teyit et]`.
- Aksiyon: Elde tutma ekibi, aylık plandaki KOBİ'ler için yıllık plana geçiş teklifini test etsin – sorumlu `[BİLİNMİYOR]`.
