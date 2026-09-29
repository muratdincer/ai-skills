---
description: WBS ve maliyet kategorisine göre maliyet kırılımı, gerektiğinde capex/opex ayrımı, yedek pay ve yönetim rezervi ile maliyet baz çizgisini oluşturan zamana yayılmış nakit akışını içeren proje bütçesini hazırlar. Bir proje onay için bütçeye, izleme için maliyet baz çizgisine ya da kapsam veya takvim değişikliği sonrası yeniden tahmine ihtiyaç duyduğunda kullanılır.
related: wbs, resource-plan, estimation-three-point, earned-value-analysis, cloud-cost-estimate
prompt: Bu kaynak planı ve tedarikçi tekliflerinden yedek paylı ve aylık nakit akışlı bir proje bütçesi oluştur.
---

# Proje Bütçesi

## Amaç
Sponsorların onaylayabileceği ve projenin karşısında izlenebileceği, bilinen ve bilinmeyen riskler için açık rezervleri olan, izlenebilir ve zamana yayılmış bir bütçe üretmek.

## Ne zaman kullanılır
- Başlatma belgesi onayı veya yatırım kapısı için bütçe hazırlanırken.
- Kazanılmış değer takibi için maliyet baz çizgisi oluşturulurken.
- Bir değişiklik talebi veya büyük bir risk olayından sonra yeniden tahmin yapılırken.

## Ne zaman kullanılmaz
- Yatırımın değip değmeyeceğine karar vermek için `cost-benefit-analysis` kullanılır.
- Birim düzeyinde yıllık bütçe talepleri için `budget-proposal` kullanılır.
- Bir mimarinin bulut işletim maliyeti tahmini için `cloud-cost-estimate` kullanılır.

## Girdiler
Zorunlu:
- WBS veya kapsam ile kaynak planı ya da efor tahminleri.
- Ücretler veya maliyetler ya da bunların sağlanacağı teyidi (ücret asla varsayılmaz).

İsteğe bağlı, kaliteyi artırır:
- Tedarikçi teklifleri, lisans ve altyapı maliyetleri, seyahat, eğitim.
- Capex/opex için kurum kuralları, para birimi, enflasyon, yedek pay politikası.

Maliyet dayanağı verilmemişse yapıyı `[BİLİNMİYOR]` değerlerle üret ve gereken ücretlerin listesini ver.

## Süreç
1. Maliyet kategorilerini tanımla: iç işgücü, dış işgücü/tedarikçiler, yazılım lisansları, donanım/altyapı, bulut, eğitim, seyahat, diğer.
2. WBS paketi başına maliyeti tahmin et: işgücü için efor × ücret; satın almalar için teklifler. Her satırın formülünü veya kaynağını göster.
3. Gerekiyorsa her satırı kurum politikasına göre capex veya opex olarak sınıflandır; emin değilsen `[FİNANSLA TEYİT ET]` işaretle.
4. Temel tahmini topla.
5. Tanımlı riskler için yedek pay (contingency) ekle (risk kaydındaki beklenen parasal değerden veya üç noktalı aralıklardan). Yöntemi belirt.
6. Kurum politikası kullanıyorsa, bilinmeyen bilinmeyenler için yönetim rezervi ekle; bunun maliyet baz çizgisinin dışında olduğunu not et.
7. Takvim ve ödeme koşullarını kullanarak maliyetleri aylara yay; nakit akışını ve kümülatif baz çizgisini (S eğrisi verisi) üret.
8. Onay toplam sahip olma maliyeti gerektiriyorsa canlıya geçişte başlayan tekrarlayan maliyetleri proje maliyetinden açıkça ayırarak ekle.
9. Varsayımları, hariç tutulanları (ör. vergiler, iç genel giderler), para birimini ve fiyat baz tarihini listele.
10. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: gerçekleşenleri bu temele göre izlemek için `earned-value-analysis` ya da personel maliyetleri henüz açıksa `resource-plan`.

## Çıktı formatı
```markdown
# Proje Bütçesi: <proje>
Para birimi <x> | Fiyat baz tarihi <tarih> | Sürüm <x>
## Maliyet Kırılımı
| WBS No | Kalem | Kategori | Capex/Opex | Miktar × ücret / kaynak | Maliyet |
## Özet
| Satır | Tutar |
| Temel tahmin | |
| Yedek pay (yöntem) | |
| Maliyet baz çizgisi | |
| Yönetim rezervi (varsa) | |
| Toplam bütçe | |
## Nakit Akışı
| Ay | Planlanan harcama | Kümülatif |
## Canlı Sonrası Tekrarlayan Maliyetler (gerekiyorsa)
## Varsayımlar, Hariç Tutulanlar, Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her satırın formülü veya kaynağı var; açıklamasız sayı yok.
- [ ] Hiçbir ücret veya fiyat uydurulmadı; boşluklar `[BİLİNMİYOR]`.
- [ ] Yedek pay yöntemi belirtildi ve risklere veya aralıklara bağlandı.
- [ ] Nakit akışı toplamı maliyet baz çizgisine eşit.
- [ ] Proje maliyeti ile tekrarlayan işletim maliyeti ayrıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yedek payı kalemlerin içine gizlemek; bu, sapma analizini anlamsız kılar.
- Fatura olmadığı için iç işgücünü unutmak; sponsorlar toplam maliyeti düşük tahmin eder.
- Maliyeti takvimi ve ödeme kilometre taşlarını izlemek yerine eşit yaymak.

## Örnek
Girdi: "6 ay boyunca 3 geliştirici, iç ücret [sağlanacak], tedarikçi iki kilometre taşında 120 bin sabit fiyat."

Çıktıdan bir bölüm:
| 1.2 | Geliştirme (iç) | İç işgücü | Capex `[FİNANSLA TEYİT ET]` | 18 adam-ay × `[BİLİNMİYOR]` | `[BİLİNMİYOR]` |
| 1.3 | Tedarikçi entegrasyonu | Dış | Capex | Sabit fiyat teklifi | 120.000 |
- Nakit akışı: tedarikçiye %50 A3 kabulünde, %50 A6'da `[VARSAYIM: ödeme koşullarını teyit et]`.
