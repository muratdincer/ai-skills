---
description: "Test edilen ve edilmeyen kapsamı, koşum sonuçlarını, gereksinim ve risklere göre kapsamı, önem derecesine göre açık hataları, plandan sapmaları, kalan riski ve net bir öneriyi belirten, ISO/IEC/IEEE 29119-3 içeriğiyle uyumlu bir test özet (tamamlama) raporu yazar. Bir test seviyesi, iterasyon veya sürüm döngüsünün sonunda, paydaşların karar vermeye hazır bir kalite durumuna ihtiyacı olduğunda ya da ham koşum sayılarının rapora dönüşmesi gerektiğinde kullanılır."
related: test-plan, release-quality-gate, bug-triage, defect-trend-analysis, executive-summary
prompt: "Şu sayılarla 3.4 sürümünün test özet raporunu yaz: 412 case, 389 geçti, 11 kaldı, 12 bloke, 7 açık hata (1 kritik), performans testi koşulmadı."
---

# Test Özet Raporu

## Amaç
Bir test çalışmasının sonunda karar vericilere, test edilmeyenler dahil ürün kalitesinin dürüst ve kanıta dayalı bir resmini sunmak; böylece kalan riski bilinçli olarak kabul edebilsinler.

## Ne zaman kullanılır
- Bir test seviyesi (sistem, entegrasyon, UAT) veya sürüm döngüsü bitiyor.
- Yönetim veya sürüm kurulu "hazır mıyız?" diye soruyor ve yazılı bir dayanak gerekiyor.
- Bir iterasyon kapanıyor ve kalite durumu kayda geçmeli.

## Ne zaman kullanılmaz
- Çıkış kriterlerine göre resmî yayına alınır/alınmaz değerlendirmesi gerekiyorsa `release-quality-gate` kullanılır (bu raporu girdi olarak kullanabilir).
- Sürümler arası trend ve kök neden analizi gerekiyorsa `defect-trend-analysis` kullanılır.
- Devam eden günlük durum gerekiyorsa `status-update` kullanılır.

## Girdiler
Zorunlu:
- Kapsam için koşum sonuçları (sayılar veya listeler) ve açık hatalar.

İsteğe bağlı, kaliteyi artırır:
- Kapsam, çıkış kriterleri ve takvim içeren test planı; gereksinim/risk kapsam verisi.
- Ortam sorunları, sapmalar, kaybedilen süre, koşulmayan test türleri.
- Hedef kitle (ekip, yönetim, müşteri) ve sürüm karar tarihi.

Sonuçlar yoksa iste. Verilmemiş sayılardan asla yüzde türetme; boşlukları `[BİLİNMİYOR]` ile işaretle.

## Süreç
1. Hedef kitleyi ve raporun desteklediği kararı belirle; yönetim için öneriyi en başa koy.
2. Kapsamı belirt: test edilen build/versiyonlar, ortamlar, koşulan test seviyeleri ve türleri, dönem.
3. Test edilmeyen veya kısmen test edilenleri nedeniyle (kapsamdan çıkarıldı, bloke, ortam, süre) açıkça belirt.
4. Koşumu özetle: planlanan, koşulan, geçen, kalan, bloke, koşulmayan; yüzdeleri yalnızca verilen sayılardan hesapla ve paydayı göster.
5. Gereksinimlere ve belirlenmiş ürün risklerine göre kapsamı raporla; kapsamı düşük yüksek riskli alanları vurgula.
6. Hataları özetle: dönemde bulunan ve düzeltilen, önem ve önceliğe göre açık olanlar, engelleyiciler, geçici çözümüyle birlikte dikkat çeken kabul edilmiş/ertelenmiş hatalar.
7. Plandan sapmaları listele: takvim kaymaları, sağlanmayan giriş kriterleri, ortam kesintileri, kapsam değişiklikleri ve güvene etkileri.
8. Sonuçları plandaki çıkış kriterleriyle kriter kriter karşılaştır (sağlandı / sağlanmadı / ölçülemedi).
9. Kalan riski iş diliyle değerlendir: üretimde ne ters gidebilir, olasılık ve etki, azaltımlar (izleme, feature flag, hotfix hazırlığı).
10. Koşulları ve sorumlularıyla net bir öneri ver (yayına al / koşullu yayına al / yayına alma / teste devam); olguları test uzmanının yargısından ayır.
11. Kullanıcı devam ederse resmî karar için `release-quality-gate`, geriye dönük bakış için `defect-trend-analysis` öner.

## Çıktı formatı
```markdown
# Test Özet Raporu: <ürün / sürüm / seviye>
**Öneri:** <yayına al / koşullu / yayına alma / devam> – <tek satır gerekçe>

## Kapsam
- Test edilen: <build, ortamlar, seviyeler, türler, dönem>
- Test edilmeyen / kısmi: <kalem – neden>

## Koşum Sonuçları
| Planlanan | Koşulan | Geçen | Kalan | Bloke | Koşulmayan |
|---|---|---|---|---|---|

## Kapsam Analizi
| Gereksinim / risk alanı | Kapsam | Sonuç | Not |
|---|---|---|---|

## Hatalar
| Önem | Bulunan | Düzeltilen | Açık | Engelleyici |
|---|---|---|---|---|
Dikkat çeken açık hatalar: ...

## Çıkış Kriterleri
| Kriter | Durum | Kanıt |
|---|---|---|

## Plandan Sapmalar
- ...

## Kalan Risk ve Azaltımlar
- ...

## Koşullar ve Sonraki Adımlar
- <koşul> – <sorumlu> – <tarih>
```

## Kalite kontrol listesi
- [ ] Öneri en başta ve çıkış kriterlerinin durumuyla tutarlı.
- [ ] Test edilmeyen alanlar nedenleriyle açıkça listelenmiş.
- [ ] Her yüzde paydasını gösteriyor ve verilen sayılardan geliyor.
- [ ] Kalan risk iş diliyle ve azaltımlarıyla yazılmış.
- [ ] Olgular ile test uzmanının yargısı açıkça ayrılmış; bilinmeyenler `[BİLİNMİYOR]`.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bloke ve koşulmayan testler test edilmemiş riski gizlerken yüksek geçme oranı raporlamak. Tüm durumları göster.
- Kapsamdan çıkarılan test türlerini (performans, güvenlik, erişilebilirlik) atlamak. Yoklukları dipnot değil kalan risktir.
- Takvimi memnun etmek için veriyle çelişen bir öneri. Bunun yerine "koşullu yayına al" de ve koşulları listele.

## Örnek
Girdi: "3.4 sürümü: 412 case, 389 geçti, 11 kaldı, 12 bloke, 7 açık hata (1 kritik), performans testi koşulmadı."

Çıktıdan bir bölüm:
**Öneri:** Kritik hata düzeltilip doğrulanana kadar yayına alma; sonrasında koşullu yayına al.
| Planlanan | Koşulan | Geçen | Kalan | Bloke | Koşulmayan |
|---|---|---|---|---|---|
| 412 | 400 | 389 (koşulanların %97,3'ü) | 11 | 12 | `[BİLİNMİYOR]` |

- Test edilmeyen: Performans testi – koşulmadı `[BİLİNMİYOR: neden]`. Kalan risk: yoğun saat yanıt süreleri doğrulanmadı; azaltım: güçlendirilmiş izleme ve hazır rollback planı.
