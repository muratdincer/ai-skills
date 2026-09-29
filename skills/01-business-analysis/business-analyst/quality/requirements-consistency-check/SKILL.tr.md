---
name: requirements-consistency-check
description: "Gereksinimleri birbirleriyle ve iş kuralları, sözlük, veri ve NFR'lerle karşılaştırarak çelişkileri, tekrarları, örtüşmeleri, tutarsız terimleri ve çatışan değerleri bulur; her biri için bir çözüm yolu önerir. Aynı kapsamı birden fazla doküman, yazar veya sürüm tarif ettiğinde, farklı ekiplerin hikayeleri birleştirildiğinde ya da gereksinimler temel sürüme (baseline) alınmadan önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: quality
  title: "Gereksinim tutarlılık kontrolü"
  related: "ambiguity-detection, requirements-gap-analysis, business-rules-catalog, glossary-builder, traceability-matrix"
  prompt: "Aynı faturalama kapsamı için bir BRD, bir FRD ve 45 kullanıcı hikayemiz var. Çelişkileri ve tekrarları bul."
---

# Gereksinim Tutarlılık Kontrolü

## Amaç
Gereksinim setinin her şeyi bir kez ve tek anlamda söylemesini sağlamak. Çelişkiler ve benzer tekrarlar erkenden, kanıtıyla ve önerilen çözüm sorumlusuyla bulunur; böylece temel sürüme güvenilebilir.

## Ne zaman kullanılır
- Aynı kapsamı birden fazla kaynak (BRD, FRD, hikayeler, sözleşme eki, mevzuat) kapsıyorsa.
- Birden fazla analist veya ekip paralel olarak gereksinim yazdıysa.
- Yeni bir sürüm veya değişiklik talebi mevcut temel sürüme eklendiyse.

## Ne zaman kullanılmaz
- Tek tek ifadeler muğlaksa `ambiguity-detection` kullanılır.
- Sorun çelişki değil eksiklikse `requirements-gap-analysis` kullanılır.
- İş kuralları sıfırdan çıkarılıyorsa `business-rules-catalog` kullanılır.

## Girdiler
Zorunlu:
- Karşılaştırılacak gereksinimler, her birinin kaynağı ve ID'siyle.

İsteğe bağlı, kaliteyi artırır:
- Kaynakların öncelik sırası (ör. mevzuat > sözleşme > BRD > hikayeler).
- Sözlük, iş kuralları kataloğu, veri sözlüğü, NFR hedefleri.

Kaynaklarda ID yoksa `<kaynak>-<n>` biçiminde ID ata ve eşlemeyi belirt.

## Süreç
1. Normalleştir: her gereksinimi kaynak ID'sini koruyarak aktör + eylem + nesne + koşul + değer biçiminde yeniden ifade et.
2. Karşılaştırılabilir ifadeler yan yana gelsin diye gereksinimleri iş nesnesi, süreç adımı ve kalite özelliğine göre grupla.
3. Doğrudan çelişkileri bul: aynı koşul, farklı sonuç (ör. "otomatik onaylanır" ile "her zaman yönetici onayı gerekir").
4. Değer çatışmalarını bul: aynı şey için farklı sayı, limit, format, zaman aralığı, yuvarlama veya para birimi.
5. Kural/durum çatışmalarını bul: bir yerde izin verilen, başka yerde yasaklanan geçişler; çelişen zorunlu/isteğe bağlı alanlar.
6. NFR gerilimlerini bul: ör. saklama süresi ile silme hakkı, gerçek zamanlı ile batch, erişilebilirlik (availability) ile bakım pencereleri.
7. Terim tutarsızlığını bul: aynı kavram için farklı sözcükler veya farklı kavramlar için aynı sözcük.
8. Tekrar ve örtüşmeleri bul: aynı veya neredeyse aynı gereksinimler; zamanla birbirinden kopacak kısmi örtüşmeler.
9. Her bulgu için önem derecesi (Engelleyici / Büyük / Küçük) belirle, iki kaynağı da göster ve çözüm öner: belirtilen öncelik sırasına göre hangi kaynağın geçerli olduğu, birleştirme veya adı belli bir karar vericiye eskalasyon. Tahminle kazanan seçme.
10. Gereken kararları özetle ve çözümün net olduğu yerlerde birleştirilmiş ifade öner.
11. Kullanıcı devam etmek isterse çözülen kuralları birleştirmek için `business-rules-catalog`, çelişen terimler için `glossary-builder` veya birleştirilen ID'lerin izlenebilirliği için `traceability-matrix` öner.

## Çıktı formatı
```markdown
# Tutarlılık Kontrolü: <kapsam>
Kaynaklar: <sürümleriyle liste> · Öncelik: <sıra veya [BİLİNMİYOR]>

## Özet
<türe ve önem derecesine göre sayılar; gereken kararlar>

## Bulgular
| # | Tür | Gereksinim A (kaynak/ID) | Gereksinim B (kaynak/ID) | Çelişki | Önem | Önerilen çözüm | Karar sahibi |
|---|---|---|---|---|---|---|---|

## Terim Uyumu
| Kavram | Kullanılan terimler (nerede) | Önerilen tek terim |
|---|---|---|

## Birleştirilecek Tekrarlar
| Kalan | Kaldırılan | Not |
|---|---|---|
```

## Kalite kontrol listesi
- [ ] Her çelişkinin iki tarafı kaynak ve ID ile gösterildi.
- [ ] Çözümler belirtilen öncelik sırasına uyuyor veya eskale ediliyor, tahmin edilmiyor.
- [ ] Değer çatışmaları iki kaynaktaki sayı ve birimleri birebir aktarıyor.
- [ ] Her terim bulgusu tek bir önerilen terime bağlanıyor.
- [ ] Tekrarlarda hangi ID'nin kalacağı belli, izlenebilirlik kaybolmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Farklı ayrıntı düzeylerini çelişki saymak (bir BRD hedefi ile onu detaylandıran hikaye). Çelişki, ikisinin aynı anda doğru olamaması demektir.
- En yeni dokümanın lehine sessizce karar vermek. Ekip öyle kararlaştırmadıysa yenilik öncelik demek değildir.
- Yalnızca fonksiyonel ifadeleri karşılaştırıp NFR ve veri kurallarındaki çelişkileri kaçırmak.

## Örnek
Girdi: BRD-12 "Faturalar her ayın 1'inde kesilir." Hikaye ST-40 "Müşteri olarak faturamın sözleşme yıldönümü günümde kesilmesini istiyorum."

Çıktıdan bir bölüm:
| # | Tür | Gereksinim A | Gereksinim B | Çelişki | Önem | Önerilen çözüm | Karar sahibi |
|---|---|---|---|---|---|---|---|
| Ç1 | Çelişki | BRD-12 | ST-40 | Fatura tarihi: sabit 1'i ile yıldönümü | Engelleyici | Eskale et; ikisi de gerekiyorsa segment kuralı tanımla (ör. kurumsal ve bireysel) `[TBD]` | Faturalama ürün sahibi |
