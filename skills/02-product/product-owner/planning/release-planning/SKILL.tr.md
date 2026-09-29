---
description: "Bir sürümü planlar: hedef sonuç, taahhüt edilen ve esnek olarak ayrılmış aday kapsam, verim veya hız aralıklarına dayanarak kapsamın ne zaman bitebileceğine dair öngörü, bağımlılıklar, kilometre taşları, riskler, güven seviyesi ve kapsam-tarih ödünleşim seçenekleri. Ürün sahibinin bir sürümde ne olacağını ve ne zaman çıkacağını cevaplaması, sabit bir tarih için pazarlık yapması ya da paydaşlar için sürüm planı hazırlaması gerektiğinde kullanılır."
related: "roadmap, monte-carlo-forecast, velocity-analysis, release-plan, dependency-map"
prompt: "Yeni onboarding akışını 15 Mart'a kadar yayınlamak istiyoruz. Kalan 18 madde ve son 8 iterasyonun verimi burada. Mümkün mü, hangi kapsamı taahhüt etmeliyiz?"
---

# Sürüm Planlama

## Amaç
Paydaşlara kapsamı, tarihi ve güven seviyesi ekibin gerçek teslimat verisine dayanan, ödünleşimleri açık bir sürüm planı vermek; böylece taahhütler gerçekçi olur ve sürprizler erken ortaya çıkar.

## Ne zaman kullanılır
- Bir sürüm, lansman veya kilometre taşı birkaç iterasyon/sprint ya da haftalık akış boyunca planlanacaksa.
- Tarih dışarıdan sabitlenmişse ve kapsamın pazarlığı yapılacaksa.
- Kapsam sabitse ve paydaşlar ne zaman biteceğini soruyorsa.
- Kapsam veya kapasite değişikliğinden sonra mevcut bir sürüm planının yeniden öngörülmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Çeyrekler boyunca uzun vadeli yön için `roadmap` kullanılır.
- Teknik dağıtım adımları, geçiş ve geri alma için `release-plan` veya `deployment-checklist` kullanılır.
- Yalnızca istatistiksel öngörü gerekiyorsa `monte-carlo-forecast` kullanılır.

## Girdiler
Zorunlu:
- Sürüm hedefi ve aday kapsam (maddeler, tercihen boyutlandırılmış veya sayılabilir).
- Bir hedef tarih ya da "ne zaman?" sorusu.
- Geçmiş teslimat verisi (hafta/iterasyon başına verim veya hız). Yoksa sor; veri olmadan yalnızca açık `[VARSAYIM]` kapasite ve Düşük güvenle plan üret.

İsteğe bağlı, kaliteyi artırır:
- Ekip müsaitlik değişiklikleri (tatiller, yeni katılanlar, paylaşılan üyeler).
- Diğer ekiplere veya tedarikçilere bağımlılıklar, stabilizasyon ihtiyaçları, yayın pencereleri.

## Süreç
1. Sürüm hedefini bir kapsam listesi olarak değil, bir sonuç olarak ifade et.
2. Aday kapsamı taahhüt edilen (hedefin karşılanması için mutlaka olmalı) ve esnek (olsa iyi olur) olarak ayır. Taahhüt edileni hedefin gerçekten gerektirdiğiyle sınırlı tut.
3. Maddelerin karşılaştırılabilir ayrıntı düzeyinde olduğundan emin ol; büyük maddeler kaldıysa aynı birimle tahmin et veya böl (`story-splitting`).
4. Tek sayı yerine aralıklarla öngör: son dönemdeki en düşük, medyan ve en yüksek verimi/hızı (veya bir Monte Carlo sonucunu) kullanarak kötümser, olası ve iyimser tamamlanmayı hesapla. Bilinen kapasite değişikliklerine göre düzelt ve beklenen kapsam büyümesini ekle (varsa gözlenen geçmişi kullan, yoksa varsayım olarak işaretle).
5. Planlama sorusunu cevapla: sabit tarih için %85 güvenle hangi kapsam sığıyor; sabit kapsam için %50 ve %85 güvenle hangi tarihe ulaşılıyor.
6. Kilometre taşlarını yerleştir: özellik tamamlama, stabilizasyon, yayın hazırlık kararı, yayın. Bağımlılık tarihlerini dahil et.
7. Riskleri ve öngörüye etkilerini belirle; hafifletme öner.
8. Ödünleşim seçeneklerini (tarihi kaydırmak, esnek kapsamı kesmek, uyum süresi maliyetiyle kapasite eklemek) sonuçlarıyla sun.
9. Yeniden öngörü tetikleyicilerini ve sıklığını tanımla (ör. her iterasyonda veya haftalık, gerçekleşen verimle).
10. Kullanıcının hedefi devam ediyorsa olasılıksal tarih için `monte-carlo-forecast`, operasyonel sürüm ve deployment planı için `release-plan` öner.

## Çıktı formatı
```markdown
# Sürüm Planı: <sürüm adı>
Hedef: <sonuç> · Sahip: <ürün sahibi> · Plan tarihi: <tarih>

## Kapsam
| Madde | Boyut | Taahhüt / Esnek | Bağımlılık |
|---|---|---|---|

## Öngörü
Kullanılan veri: <verim/hız örneklemi, dönem>
| Senaryo | Oran | Tamamlanma (taahhüt) | Tamamlanma (tümü) |
|---|---|---|---|
| Kötümser | | | |
| Olası | | | |
| İyimser | | | |
<tarih> hedefi için güven: <Yüksek/Orta/Düşük> – <gerekçe>

## Kilometre Taşları
| Kilometre taşı | Hedef | Bağlı olduğu |
|---|---|---|

## Riskler ve Hafifletmeler
- <risk> – <öngörüye etkisi> – <hafifletme>

## Ödünleşim Seçenekleri
1. <seçenek> – <sonuç>

## Yeniden Öngörü
<tetikleyici ve sıklık>
```

## Kalite kontrol listesi
- [ ] Öngörü gerçek veriden bir aralık kullanıyor ya da varsayımları işaretli ve güven Düşük.
- [ ] Tarih sabitse taahhüt edilen kapsam kötümser kapasiteden küçük.
- [ ] Kapsam büyümesi ve müsaitlik değişiklikleri dikkate alınmış.
- [ ] Her kilometre taşının ve bağımlılığın bir tarihi ya da `[TBD]` işareti var.
- [ ] Ödünleşimler gizlenmemiş, karar için seçenek olarak sunulmuş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ortalama hızın %100'üyle planlamak. Ortalamalar zamanın ancak yarısında tutar; kötümser veya 85. yüzdelik orana göre taahhüt ver.
- Sonradan keşfedilen işi yok saymak. Backlog'lar sürüm boyunca genellikle büyür; gözlenen büyümeyi kullan veya açık bir tampon ekle.
- Planı sabit saymak. Her döngüde gerçekleşenle yeniden öngör ve değişiklikleri erken bildir.

## Örnek
Girdi: "Kalan 18 madde, son 8 haftanın verimi: haftada 3, 5, 4, 2, 6, 4, 3, 5 madde; hedef 15 Mart, 7 hafta sonra."

Çıktıdan bir bölüm:
| Kötümser | 2/hafta | Hedefe kadar 14 madde | – |
| Olası | 4/hafta | 18 madde ~4,5 haftada | – |
- Taahhüt: onboarding hedefi için zorunlu 12 madde; esnek: 6 madde. Taahhüt edilen kapsam için 15 Mart güveni: Yüksek.
- Varsayım: kapsam büyümesi verisi yok; %10 büyüme eklendi `[VARSAYIM]`.
