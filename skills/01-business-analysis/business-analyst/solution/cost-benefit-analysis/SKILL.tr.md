---
description: "Bir girişimin veya rakip seçeneklerin maliyet ve faydalarını belirli bir dönem boyunca sayısallaştırır; tek seferlik ve tekrarlayan kalemleri, somut ve soyut faydaları ayırır; net faydayı, ROI'yi, geri dönüş süresini ve istenirse NPV'yi temel varsayımlara duyarlılık analiziyle hesaplar. Bir iş gerekçesi, yatırım kararı veya seçenek karşılaştırması rakam gerektirdiğinde ya da 'değer mi?' veya 'ROI ne?' diye sorulduğunda kullanılır."
related: "feasibility-study, budget-proposal, cloud-cost-estimate, benefits-realization, decision-matrix"
prompt: "Fatura eşleştirme otomasyonu için maliyet-fayda analizi yap: lisans yıllık 40 bin, uygulama 120 bin, 3 FTE'lik manuel işi azaltması bekleniyor."
---

# Maliyet-Fayda Analizi

## Amaç
Bir girişimin maliyet ve faydalarını karşılaştırılabilir ve şeffaf tek bir temele oturtmak; karar vericilerin net değeri, geri dönüş süresini ve sonucun hangi varsayımlara dayandığını görmesini sağlamak.

## Ne zaman kullanılır
- Bir iş gerekçesi veya bütçe talebi finansal dayanak gerektirdiğinde.
- İki veya daha fazla seçenek yalnızca fiyatla değil değerle karşılaştırılacaksa.
- Sponsor onaydan önce ROI veya geri dönüş süresi istediğinde.

## Ne zaman kullanılmaz
- Finansal olmayan boyutlarda yapılabilirlik hâlâ belirsizse önce `feasibility-study` kullanılır.
- Yalnızca bir mimarinin bulut işletim maliyeti gerekiyorsa `cloud-cost-estimate` kullanılır.
- Faydalar gerçekleşmiş ve takip edilecekse `benefits-realization` kullanılır.

## Girdiler
Zorunlu:
- Girişim veya seçenekler ile kullanıcının elindeki maliyet ve fayda rakamları ya da sürücüleri (hacimler, birim fiyatlar, FTE, lisans fiyatları).
- Değerlendirme dönemi (ör. 3 veya 5 yıl); yoksa 3 yıl öner ve `[VARSAYIM]` olarak işaretle.

İsteğe bağlı, kaliteyi artırır:
- Finansın kullandığı iskonto veya asgari getiri oranı, para birimi, enflasyon varsayımı.
- FTE başına tam yüklü maliyet, başlangıç hacimleri, büyüme öngörüsü.
- Risk düzeltme politikası, vergi veya amortisman yaklaşımı (finansa bırak).

Asla fiyat, maaş veya hacim uydurma. Gereken bir rakam yoksa sor (bir seferde en fazla 5 soru) ya da adlandırılmış bir değişken olarak bırak.

## Süreç
1. Temel durumu (hiçbir şey yapmamak / mevcut durum) ve her seçeneği tanımla; tüm rakamlar temel duruma göre artımsaldır.
2. Maliyetleri listele: tek seferlik (lisans, uygulama, taşıma, eğitim, iç efor, paralel çalışma) ve tekrarlayan (abonelik, destek, altyapı, ek personel, bakım). Kapatma ve çıkış maliyetlerini de ekle.
3. Faydaları listele: somut tasarruflar (kaçınılan maliyet, serbest kalan FTE saatleri, kapatılan lisanslar), gelir etkileri, risk azaltımı (kaçınılan beklenen kayıp) ve soyut faydalar (nitel olarak tutulur).
4. Serbest kalan kapasiteyi nakit tasarruftan ayır: boşalan saatler ancak kadro, fazla mesai veya dış kaynak harcaması gerçekten azalırsa nakittir. Hangisinin geçerli olduğunu işaretle.
5. Dönem tablosu kur (yıl 0..N): maliyet, fayda, net, kümülatif net. Her satırın formülünü veya sürücüsünü göster.
6. Hesapla: toplam net fayda, ROI = (toplam fayda − toplam maliyet) ÷ toplam maliyet, geri dönüş süresi (kümülatif netin pozitife döndüğü an) ve iskonto oranı verildiyse NPV.
7. En büyük etkiye sahip 2-3 varsayım için duyarlılık analizi yap (ör. benimsenme oranı, kalem başına tasarruf, uygulama maliyeti +%30): en iyi, beklenen ve en kötü durumu göster.
8. Finansal olmayan faktörleri ekle: stratejik uyum, uyum/mevzuat, müşteri deneyimi, rakamların yakalamadığı riskler.
9. Sonucu koşullarıyla birlikte yaz ("benimsenme %X'i aşarsa pozitif") ve finansın doğrulaması gereken varsayımları listele.
10. Kullanıcı devam etmek isterse bütçe istemek için `budget-proposal`, finansal ve finansal olmayan kriterleri tartmak için `decision-matrix` veya vaat edilen faydaları izlemek için `benefits-realization` öner.

## Çıktı formatı
```markdown
# Maliyet-Fayda Analizi: <girişim>
Dönem: <N yıl> · Para birimi: <...> · İskonto oranı: <%x veya uygulanmadı> · Temel durum: <...>

## Maliyetler
| Kalem | Tür (tek seferlik/tekrarlayan) | Sürücü / formül | Y0 | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|---|

## Faydalar
| Kalem | Tür (nakit / kapasite / risk / soyut) | Sürücü / formül | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|

## Sonuç
| Metrik | Beklenen | En kötü | En iyi |
|---|---|---|---|
| Net fayda | | | |
| ROI | | | |
| Geri dönüş süresi | | | |
| NPV (oran verildiyse) | | | |

## Finansal Olmayan Faktörler
- ...

## Sonuç ve Koşullar
...

## Doğrulanacak Varsayımlar
- [VARSAYIM] ... — doğrulama: ...
```

## Kalite kontrol listesi
- [ ] Her rakam girdiye veya belirtilmiş bir sürücüye dayanıyor; hiçbir şey uydurulmadı.
- [ ] İç efor ve çıkış maliyetleri dahil hem tek seferlik hem tekrarlayan maliyetler var.
- [ ] Kapasite faydaları, tasarruf gerçekleşmedikçe nakit sayılmadı.
- [ ] Aritmetik doğru: toplamlar, ROI ve geri dönüş süresi dönem tablosuyla örtüşüyor.
- [ ] Duyarlılık analizi sonucu tersine çevirebilecek varsayımları kapsıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kimse ayrılmadığı veya başka işe kaydırılmadığı halde boşalan FTE saatlerini tasarruf saymak. Bunu kapasite olarak etiketle ve nasıl kullanılacağını belirt.
- İç eforu, paralel çalışmayı ve benimsenme rampasını unutmak; bu, ilk yılı gerçekçi olmayan biçimde iyi gösterir.
- Duyarlılık analizi olmadan tek bir rakam sunmak. Hangi varsayımın gerekçeyi bozduğunu göster.

## Örnek
Girdi: "Lisans yıllık 40 bin, uygulama 120 bin, 3 FTE'lik manuel eşleştirme işini azaltıyor."

Çıktıdan bir bölüm:
| Metrik | Beklenen |
|---|---|
| 3 yıllık maliyet | 120 bin + 3 × 40 bin = 240 bin |
| 3 yıllık fayda | 3 FTE × tam yüklü maliyet `[BİLİNMİYOR]` × 3 yıl – FTE maliyetini finanstan iste |
| Başabaş koşulu | 3 yılda fayda ≥ 240 bin, yani FTE başına tam yüklü maliyet ≥ ~26,7 bin/yıl; 3 FTE gerçekten serbest kalıyorsa |
