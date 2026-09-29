---
description: "Bir ekip sağlık kontrolünü tasarlar ve analiz eder: 8-12 boyut seçer (ör. değer teslimi, hız, kod tabanı sağlığı, öğrenme, misyon netliği, keyif, destek, psikolojik güvenlik), trafik ışığı veya 1-5 derecelendirme ifadeleri yazar, anonim yürütür, sonuçları ve boyut bazında trendleri okur, en düşük veya düşen alanları sahibi belli az sayıda takip aksiyonuna dönüştürür. Bir ekip veya yönetici ekibin nabzını ölçmek, önceki turla karşılaştırmak ya da bir sağlık kontrolü oturumu hazırlamak istediğinde kullanılır."
related: "retrospective-facilitation, working-agreement, agile-maturity-assessment, questionnaire-design, engineering-metrics-review"
prompt: "Geçen çeyrek ve bu çeyrek 10 boyuttaki sağlık kontrolü sonuçlarımız burada (kişi başı yeşil/sarı/kırmızı). Ne öne çıkıyor ve ne yapmalıyız?"
---

# Ekip Sağlık Kontrolü

## Amaç
Ekibe, kendisi için önemli boyutlarda nasıl olduğunu görebileceği güvenli ve tekrarlanabilir bir yol sunmak, trendleri erken yakalamak ve sonuçları bir performans puanına dönüştürmeden ekibin kendisinin sahiplendiği az sayıda iyileştirme seçmek.

## Ne zaman kullanılır
- Ekip, sağlığına dair dönemsel (ör. çeyreklik) bir nabız ölçümü istiyor.
- Önceki turun sonuçları var ve trendler ile aksiyonlar isteniyor.
- Yeni bir ekip lideri veya koç yapılandırılmış bir başlangıç konuşması yapmak istiyor.

## Ne zaman kullanılmaz
- Çevik pratikleri bir olgunluk modeline göre puanlamak için `agile-maturity-assessment` kullanılır.
- Örneklemeli, kurum çapında büyük bir anket tasarlamak için `questionnaire-design` kullanılır.
- Tek bir iterasyonun çalışma biçimini iyileştirmek için `retrospective-facilitation` kullanılır.

## Girdiler
Zorunlu:
- Ya amaç ve ekip bağlamı (yeni bir sağlık kontrolü tasarlamak için) ya da boyut bazında sonuçlar (mevcut olanı analiz etmek için).

İsteğe bağlı, kaliteyi artırır:
- Trendler için önceki turların sonuçları.
- Ekibin veya kurumun hâlihazırda kullandığı boyutlar.
- Dönem içindeki ekip olayları (yeniden yapılanma, olaylar, yeni üyeler).

Sonuçlar kişi adlarıyla verilmişse adları çıkar ve yalnızca toplulaştırılmış veriyle çalış; kimliği belirlenebilir yanıtların dürüstlüğü zedelediğini kullanıcıya hatırlat.

## Süreç
1. Amacı netleştir: ekibin öz değerlendirmesi (varsayılan) mi, yönetime girdi mi? Sonuçları yönetim görecekse yalnızca toplulaştırılmış veriyi ve ekibin onayladığı temaları paylaşmayı öner.
2. 8-12 boyut seç ve her biri için olumlu ve olumsuz bir çapa ifadesi yaz (ör. Kod tabanı sağlığı – "Kodumuzu güvenle değiştirmek kolay" / "Her değişiklik riskli geliyor"). Trendler karşılaştırılabilir kalsın diye mevcut boyutları yeniden kullan.
3. Ölçeği seç: trafik ışığı (yeşil/sarı/kırmızı) ve trend oku (iyileşiyor/sabit/kötüleşiyor) ya da 1-5. Turlar arasında aynı ölçeği koru.
4. Yürütmeyi planla: önce anonim bireysel oylama, sonra toplu sonucun gösterilmesi, ardından tartışma. Yaklaşık 60-90 dakikalık süre ayır; uzaktan ekiplerde anonim oylama ve ortak bir pano kullan.
5. Sonuçları boyut bazında topla: dağılım (renk başına sayı ya da 1-5 için ortalama ve yayılım) ve önceki tura göre trend. Yüksek yayılım başlı başına bir bulgudur; deneyimlerin farklı olduğunu gösterir.
6. Sinyalleri belirle: kırmızı/düşük, 2+ turdur düşen veya belirgin biçimde bölünmüş boyutlar. Bunları yalnızca puana göre değil, ekibin algıladığı öneme göre sırala.
7. İlk 1-3 sinyal için tartışma soruları çerçevele ("Yeşil nasıl görünürdü?", "Geçen seferden bu yana ne değişti?") ve ekibin açıklamalarını kaydet; kendi hipotezlerini `[ÇIKARIM]` olarak etiketle.
8. Bunları en fazla 3 aksiyona dönüştür; her birinin ekip içinden bir sorumlusu, ilk adımı ve kontrol tarihi olsun. Yalnızca ekibin değiştiremeyeceği şeyleri eskale et ve yönetime talep olarak adlandır.
9. Başlangıç değerini ve sonraki turun tarihini kaydet; bir aksiyonu derinlemesine çalışmak için `retrospective-facilitation`, bulgular normlarla ilgiliyse `working-agreement` öner.

## Çıktı formatı
```markdown
# Ekip Sağlık Kontrolü – <ekip>, <tur/tarih>
Katılımcı: <m kişiden n> · Ölçek: <trafik ışığı + trend / 1-5> · Önceki tur: <tarih veya yok>

| Boyut | Yeşil | Sarı | Kırmızı | Öncekine göre trend | Yayılım | Sinyal |
|---|---|---|---|---|---|---|

## Öne Çıkan Sinyaller
1. <boyut> – <kanıt> – ekibin açıklaması / [ÇIKARIM]

## Aksiyonlar (en fazla 3)
| Aksiyon | Sorumlu | İlk adım | Kontrol tarihi |
|---|---|---|---|

## Ekibin Kontrolü Dışındaki Talepler
- ...

## Sonraki Tur
<tarih> · aynı boyutlar ve ölçek
```

## Kalite kontrol listesi
- [ ] Bireysel yanıtlar anonim ve çıktıda hiçbir kişi tanınabilir değil.
- [ ] Boyutlar ve ölçek önceki turlarla aynı ya da karşılaştırılabilirlikteki kırılma belirtildi.
- [ ] Yalnızca ortalamalar değil, yayılım da raporlandı.
- [ ] Açıklamalar ekipten geliyor; kendi hipotezler `[ÇIKARIM]` olarak etiketli.
- [ ] En fazla 3 aksiyon var; her birinin sorumlusu, ilk adımı ve kontrol tarihi belli.
- [ ] Sonuçlar performans puanı olarak sunulmadı ve ekipler arasında karşılaştırılmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sağlık kontrolü sonuçlarını ekipleri sıralamak için kullanmak. Puanlar siyasallaşır, dürüstlük kaybolur.
- Her turda boyutları değiştirmek. Asıl değer olan trendler kaybolur.
- Çok aksiyon toplayıp hiçbirini bitirmemek. Az sayıda seç ve bir sonraki turda kontrol et.

## Örnek
Girdi: 10 boyut, 7 katılımcı, iki tur; "Kod tabanı sağlığı" 4 yeşil/3 sarıdan 1 yeşil/3 sarı/3 kırmızıya indi.

Çıktıdan bir bölüm:
| Boyut | Yeşil | Sarı | Kırmızı | Trend | Sinyal |
|---|---|---|---|---|---|
| Kod tabanı sağlığı | 1 | 3 | 3 | Kötüleşiyor | Başlıca sinyal |
| Keyif | 5 | 2 | 0 | Sabit | – |
- Hipotez `[ÇIKARIM]`: yeni ödeme modülü sürüm baskısı; tartışmada teyit edin.
- Aksiyon: en riskli iki modülün test kapsamı için kapasite ayır – sorumlu: teknik lider – bir sonraki turda kontrol.
