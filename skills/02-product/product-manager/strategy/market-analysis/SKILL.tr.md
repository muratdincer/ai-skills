---
name: market-analysis
description: "TAM/SAM/SOM büyüklük hesabı (yukarıdan aşağı ve aşağıdan yukarı, her rakam kaynaklı ya da varsayım olarak işaretli), segmentler, trendler, itici güçler ve engellerle yapılandırılmış bir pazar analizi hazırlar. Yeni bir pazar, ürün fikri veya genişleme değerlendirilirken, iş gerekçesi pazar büyüklüğüne ihtiyaç duyduğunda ya da pazarın ne kadar büyük olduğu veya hangi segmentin hedefleneceği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: strategy
  title: "Pazar analizi"
  related: "competitor-analysis, business-model-canvas, product-strategy-one-pager, persona, pricing-analysis"
  prompt: "Türkiye'deki bağımsız fizyoterapi klinikleri için randevu planlama SaaS ürününün pazar analizini yap."
---

# Pazar Analizi

## Amaç
Karar vericilere bir pazarın büyüklüğü, yapısı ve dinamikleri hakkında şeffaf bir tablo sunarak nerede ve oynanıp oynanmayacağına karar vermelerini sağlamak. Kaynakların ve varsayımların şeffaflığı büyük bir rakamdan daha önemlidir.

## Ne zaman kullanılır
- Yeni bir ürün, pazara giriş veya coğrafi genişleme değerlendirilirken.
- Bir iş gerekçesi, strateji veya yatırım kararı pazar büyüklüğüne ihtiyaç duyduğunda.
- Birden fazla aday arasından ilk odak (beachhead) segment seçilirken.

## Ne zaman kullanılmaz
- Soru belirli rakiplerin nasıl kıyaslandığıysa `competitor-analysis` kullanılır.
- Tek bir fikrin iş modeli mantığı gerekiyorsa `business-model-canvas` kullanılır.
- Fiyat seviyeleri ve modelleri gerekiyorsa `pricing-analysis` kullanılır.

## Girdiler
Zorunlu:
- Ürün veya teklif ve analiz edilecek pazar/coğrafya.

İsteğe bağlı, kaliteyi artırır:
- Mevcut veriler: sektör raporları, resmi istatistikler, iç satış verisi, müşteri sayıları.
- Hedef fiyat veya müşteri başına gelir, iş modeli.
- Analizin desteklediği karar.

Ürün veya coğrafya yoksa sor. Eksik veriyi asla uydurma rakamla doldurma; `[BİLİNMİYOR]` olarak işaretle ve nasıl elde edileceğini yaz.

## Süreç
1. Pazar sınırını tanımla: müşteri, ihtiyaç ve coğrafya; kapsam dışını listele.
2. Pazarı yalnızca demografiyle değil, satın alma davranışını değiştiren niteliklerle (ölçek, sektör, olgunluk, kanal, mevzuat) segmentlere ayır.
3. TAM'ı mümkünse aşağıdan yukarı hesapla: potansiyel müşteri sayısı x müşteri başına yıllık değer. Formülü göster ve her girdinin kaynağını belirt.
4. Yayımlanmış bir kaynaktan yukarıdan aşağı tahminle çapraz kontrol yap; ~2 kattan büyük farkları açıkla.
5. SAM'ı (mevcut ürün, kanal, dil ve mevzuatla erişilebilen) ve SOM'u (kapasite ve benzer benimsenme oranlarına göre dönem içinde gerçekçi olarak kazanılabilecek) türet. Her çarpanı etiketle.
6. Trendleri ve itici güçleri (teknoloji, mevzuat, davranış, ekonomi) ve engelleri (geçiş maliyeti, yerleşik oyuncular, uyum) anlat.
7. Aday segmentleri çekicilik (büyüklük, büyüme, acı, ödeme isteği, erişilebilirlik) ve uyum (yetkinlik, avantaj) açısından puanla.
8. Her rakam için güven düzeyini (Yüksek/Orta/Düşük) ve ana duyarlılığı (sonucu en çok hangi girdinin oynattığını) belirt.
9. Bir odak segment öner ve hâlâ gereken kanıtları yaz.
10. Girdide yazmayan, senin çıkardığın her noktayı `[VARSAYIM]` olarak işaretle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: seçilen segment için `competitor-analysis`, nerede oynanacağına karar vermek için `product-strategy-one-pager`.

## Çıktı formatı
```markdown
# Pazar Analizi: <teklif> — <coğrafya>
## Pazar Tanımı
<müşteri, ihtiyaç, coğrafya; kapsam dışı>

## Büyüklük
| Seviye | Formül | Girdiler (kaynak) | Değer | Güven |
|---|---|---|---|---|
| TAM | ... | ... | ... | Y/O/D |
| SAM | ... | ... | ... | ... |
| SOM | ... | ... | ... | ... |
Yukarıdan aşağı çapraz kontrol: ...
Ana duyarlılık: ...

## Segmentler
| Segment | Çekicilik | Uyum | Notlar |
|---|---|---|---|

## Trendler, İtici Güçler ve Engeller
- ...

## Öneri ve Kanıt Boşlukları
- ...
```

## Kalite kontrol listesi
- [ ] Her rakamın kaynağı var ya da `[VARSAYIM]`/`[BİLİNMİYOR]` olarak işaretli.
- [ ] Yalnızca sonuçlar değil, hesap formülleri de gösteriliyor.
- [ ] Aşağıdan yukarı ve yukarıdan aşağı tahminler karşılaştırıldı.
- [ ] SOM "TAM'ın %1'i" değil, gerçekçi kapasite ve benimsenmeyi yansıtıyor.
- [ ] Segmentler satın alma davranışına göre tanımlandı.
- [ ] Net bir öneri ve kalan kanıt boşlukları belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bir rapordaki yukarıdan aşağı TAM'ı fırsat olarak sunmak. Erişilemeyen veya hizmet verilemeyen alıcılar sizin pazarınız değildir.
- Kaynaklar arasında para birimi, yıl veya birimleri karıştırmak. Normalize et ve baz yılı belirt.
- Varsayımları bir tabloya gömmek. İtici değişkenleri dokümanın içine yaz.

## Örnek
Girdi: "Türkiye'deki bağımsız fizyoterapi klinikleri için randevu planlama SaaS'ı."

Çıktıdan bir bölüm:
- TAM formülü: bağımsız fizyoterapi kliniği sayısı `[BİLİNMİYOR – kaynak: bakanlık/dernek kayıtları]` x yıllık abonelik `[VARSAYIM: fiyat testinden]`.
- SAM: online randevuya hazır ve Türkçe destek alabilen klinikler; hastane zincirleri hariç.
- Ana duyarlılık: klinik sayısı; kayıt verisi elde edilene kadar güven Düşük.
