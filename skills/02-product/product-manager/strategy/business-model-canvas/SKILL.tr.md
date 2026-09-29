---
description: Bir ürün fikri için İş Modeli Kanvası veya Lean Kanvas'ı doldurur; kanıtı varsayımdan ayırır ve önce sınanacak en riskli varsayımları sıralar. Yeni bir fikir, girişim veya ürün hattının iş mantığının ortaya konması gerektiğinde, iş modeli seçenekleri karşılaştırılırken ya da iş modeli veya lean kanvas istendiğinde kullanılır.
related: market-analysis, pricing-analysis, assumption-mapping, hypothesis-statement, product-vision
prompt: Serbest çalışan mali müşavirleri küçük e-ticaret satıcılarıyla buluşturan bir pazaryeri için lean kanvas doldur.
---

# İş Modeli / Lean Kanvas

## Amaç
Bir fikrin nasıl değer yarattığını, ilettiğini ve yakaladığını tek sayfada ortaya koymak ve hangi blokların kanıta, hangilerinin tahmine dayandığını görünür kılmak. En riskli tahminler bir sonraki deneylere dönüşür.

## Ne zaman kullanılır
- Yeni bir ürün, girişim veya iç iş kolunun erken şekillendirilmesinde.
- Aynı fikir için iki veya daha fazla iş modeli seçeneği karşılaştırılırken.
- Pazar veya maliyet değişikliğinden sonra mevcut bir ürünün modeli gözden geçirilirken.

## Ne zaman kullanılmaz
- Ayrıntılı pazar büyüklüğü gerekiyorsa `market-analysis` kullanılır.
- Tam bir fiyat modeli karşılaştırması gerekiyorsa `pricing-analysis` kullanılır.
- Fikir zaten doğrulanmış ve gereksinimlere ihtiyaç varsa `prd-writing` kullanılır.

## Girdiler
Zorunlu:
- Fikir: kime hizmet ettiği ve ne sunduğu.

İsteğe bağlı, kaliteyi artırır:
- Kanvas tercihi (yerleşik veya ortak ağırlıklı modeller için İş Modeli Kanvası, erken aşama veya belirsiz problemler için Lean Kanvas).
- Araştırma, erken çekiş, maliyet verisi, ortak seçenekleri.

Fikir yoksa sor. Kanvas belirtilmemişse ürün-pazar uyumu öncesindeki fikirler için Lean Kanvas'ı seç ve nedenini yaz.

## Süreç
1. Kanvası seç ve gerekçesini yaz.
2. Önce müşteri segmentlerini doldur; erken benimseyenleri somut olarak adlandır.
3. Problemi (Lean) veya değer önerilerini (İMK) doldur: en önemli 3 problem ve mevcut alternatifler; değer önerisi bir probleme bağlanmalı.
4. Çözüm / ana faaliyetler, kanallar ve müşteri ilişkileri bloklarını doldur.
5. Gelir akışlarını ve maliyet yapısını uydurma rakamlarla değil, modeller ve itici değişkenlerle doldur. Fiyat noktaları için `[VARSAYIM]` kullan.
6. Ana metrikleri (Lean) veya ana kaynaklar ve ortakları (İMK) doldur; Lean'de haksız avantajı dürüstçe yaz, "henüz yok" geçerli bir cevaptır.
7. Her girdiyi K (kanıt, kaynağıyla) veya V (varsayım) olarak etiketle.
8. İç tutarlılığı kontrol et: kanal segmente, gelir modeli ilişki türüne uyuyor mu, maliyetler faaliyetleri destekliyor mu.
9. Varsayımları riske göre (yanlışsa etkisi x belirsizlik) sırala ve ilk 3 için ucuz bir test öner.

## Çıktı formatı
```markdown
# <Lean Kanvas | İş Modeli Kanvası>: <fikir>
Kanvas seçimi: <gerekçe>

| Blok | İçerik | K/V | Kaynak / not |
|---|---|---|---|
| Müşteri segmentleri (erken benimseyenler) | ... | ... | ... |
| Problem / mevcut alternatifler | ... | ... | ... |
| Benzersiz değer önerisi | ... | ... | ... |
| Çözüm | ... | ... | ... |
| Kanallar | ... | ... | ... |
| Gelir akışları | ... | ... | ... |
| Maliyet yapısı | ... | ... | ... |
| Ana metrikler | ... | ... | ... |
| Haksız avantaj | ... | ... | ... |

## Tutarlılık Notları
- ...

## En Riskli Varsayımlar ve Testler
| # | Varsayım | Risk | En ucuz test | Başarı sinyali |
|---|---|---|---|---|
```

## Kalite kontrol listesi
- [ ] Her blok kanıt veya varsayım olarak etiketlendi.
- [ ] Erken benimseyenler bulunup iletişime geçilebilecek kadar somut.
- [ ] Gelir ve maliyet blokları model ve itici değişken içeriyor, uydurma rakam yok.
- [ ] Değer önerisi belirtilen bir probleme karşılık geliyor.
- [ ] En riskli 3 varsayımın her birinin testi ve başarı sinyali var.

## Sık yapılan hatalar
- Her bloğu kendinden emin cümlelerle doldurmak. Varsayımları işaretlenmemiş bir kanvas riski gizler.
- Segment olarak "herkes" yazmak. İki taraflı pazarlarda iki taraf ayrı segmentler olarak ele alınmalı.
- Aslında bir özellik olan şeyi haksız avantaj diye yazmak. Özellikler kopyalanabilir.

## Örnek
Girdi: "Serbest mali müşavirleri küçük e-ticaret satıcılarıyla buluşturan pazaryeri."

Çıktıdan bir bölüm:
- Segmentler: 10'dan az çalışanı olan ve defterini kendisi tutan pazaryeri satıcıları (V); boş kapasitesi olan serbest mali müşavirler (V).
- Gelir: ilk yıl hizmet bedeli üzerinden komisyon `[VARSAYIM]` ya da satıcı aboneliği — test edilecek.
- En riskli varsayım: satıcılar platformun eşleştirdiği müşavire güvenir; test: 10 satıcıyla elle (concierge) eşleştirme, başarı = 6'sının sözleşme imzalaması.
