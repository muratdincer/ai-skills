---
description: Maliyet yüklü bir temel plan ve ilerleme verisinden kazanılmış değer analizi yapar; PV, EV, AC, SV, CV, SPI, CPI, EAC, ETC, VAC ve TCPI değerlerini hesaplar, sapmaları yorumlar ve varsayımlarını belirterek tamamlanma maliyetini ve tarihini öngörür. Bütçe ve takvim temeli olan bir projede nesnel performans okuması, tamamlanmadaki maliyet tahmini ya da durum raporu veya yönlendirme kararı için kanıt gerektiğinde kullanılır.
related: budget-plan, schedule-plan, project-status-report, change-control, monte-carlo-forecast
prompt: İş paketi bazında temel planımız, bu ayın gerçekleşen maliyetleri ve tamamlanma yüzdeleri ekte. Kazanılmış değer analizi yap ve bütçe içinde bitirip bitiremeyeceğimizi söyle.
---

# Kazanılmış Değer Analizi

## Amaç
Onaylı temel plana göre takvim ve maliyet performansının nesnel, sayıya dayalı bir okumasını ve savunulabilir bir tamamlanma tahminini vermek. Böylece sponsorlar tamamlanma yüzdesi iyimserliğine değil olgulara göre karar verir.

## Ne zaman kullanılır
- Onaylı maliyet ve takvim temeli olan bir projenin dönemsel kontrolünde.
- Maliyet veya takvim sağlığı sorgulandığında, durum raporu ya da yönlendirme toplantısı öncesinde.
- Bir toparlanma planının gerçekçi olup olmadığını sınamak için (TCPI kontrolü).

## Ne zaman kullanılmaz
- Henüz maliyet yüklü bir temel plan yoksa önce `budget-plan` ve `schedule-plan` kullanılır.
- Bütçe temeli olmadan verimden tahmin yapan akış odaklı ekipler için `monte-carlo-forecast` kullanılır.
- Paydaşlara genel proje sağlığı raporlanacaksa `project-status-report` kullanılır ve bu sonuçlar oraya aktarılır.

## Girdiler
Zorunlu:
- Temel plan: tamamlanmadaki bütçe (BAC) ve dönem ya da iş paketi bazında planlanan değer.
- İlerleme: bir durum tarihi itibarıyla iş paketi başına kazanılmış değer veya ölçülebilir tamamlanma esası.
- Durum tarihine kadarki gerçekleşen maliyet (AC); temel planla aynı para birimi ve maliyet esasında.

İsteğe bağlı, kaliteyi artırır:
- Kullanılan kazanım kuralları (0/100, 50/50, ağırlıklı kilometre taşları, fiziksel tamamlanma yüzdesi).
- Onaylı değişiklikler ve yönetim yedeği hareketleri.
- Eğilim için önceki dönemlerin endeksleri.

BAC, planlanan değer veya gerçekleşen maliyet eksikse iste. AC'yi veya EV'yi anlatıdan asla tahmin etme.

## Süreç
1. Durum tarihini, para birimini, maliyet esasını (yalnızca işçilik mi, tam yüklü mü) ve temel planla gerçekleşenlerin aynı esası kullandığını teyit et; uyumsuzlukları engelleyici olarak işaretle.
2. Temel planın yalnızca onaylı değişiklikleri içerdiğini kontrol et; onaylanmamış değişiklikler ve yönetim yedeği PV dışında kalır.
3. İş paketi başına EV'yi belirtilen kazanım kuralıyla belirle. Yalnızca öznel tamamlanma yüzdesi varsa onu uygula ama EV'yi `[VARSAYIM: öznel ilerleme]` olarak işaretle.
4. PV, EV, AC ile SV = EV − PV ve CV = EV − AC sapmalarını kümülatif ve dönemlik hesapla.
5. SPI = EV/PV ve CPI = EV/AC hesapla; kümülatif ve dönemlik değerleri, verildiyse son dönemlerdeki eğilimle birlikte göster.
6. EAC'yi en az iki yöntemle tahmin et ve hangisinin ne zaman uygun olduğunu belirt: BAC/CPI (mevcut verimlilik sürer), AC + (BAC − EV) (sapma istisnaiydi), AC + (BAC − EV)/(CPI × SPI) (takvim baskısı maliyeti sürükler). ETC ve VAC'yi türet.
7. TCPI = (BAC − EV)/(BAC − AC) hesapla, revize bütçe onaylıysa EAC'ye göre de hesapla; yaklaşık 1,1'in üzerindeki TCPI'yı gerçekçi olmayan bir toparlanma varsayımı olarak işaretle.
8. Takvim görünümünü değerlendir: SPI'nın proje sonuna doğru 1,0'a yaklaştığını not et; kritik yol biliniyorsa onunla, dönem verisi elveriyorsa kazanılmış takvimle (SPI(t)) çapraz kontrol et.
9. En büyük negatif CV ve SV'yi üreten iş paketlerine in ve olası nedenleri yaz; girdide verilmeyen nedenleri `[VARSAYIM]` olarak etiketle.
10. Aksiyon veya karar öner (yeniden planlama, değişiklik talebi, yedek kullanımı, kapsam ödünleşimi) ve kararı verecek kişiyi belirt.
11. Kullanıcının hedefi devam ediyorsa sonucu raporlamak için `project-status-report`, temel plan değişikliği gerekiyorsa `change-control` öner.

## Çıktı formatı
```markdown
# Kazanılmış Değer Analizi: <proje> – durum tarihi <tarih>
Para birimi / maliyet esası: <...> | BAC: <...> | Kazanım kuralı: <...>

## Özet
<2-3 cümle: maliyet ve takvim durumu, tahmin, gereken karar>

## Metrikler
| Metrik | Dönem | Kümülatif | Eğilim |
|---|---|---|---|
| PV / EV / AC | | | |
| SV / CV | | | |
| SPI / CPI | | | |

## Tahmin
| Yöntem | EAC | ETC | VAC | Ne zaman uygun |
|---|---|---|---|---|
TCPI (BAC'ye göre): <değer> – <gerçekçi mi>

## Sapma Kaynakları
| İş paketi | SV | CV | Neden (belirtilen veya [VARSAYIM]) |

## Öneriler ve Gereken Kararlar
- <aksiyon> – <karar sahibi>

## Varsayımlar ve Veri Boşlukları
```

## Kalite kontrol listesi
- [ ] Temel plan ve gerçekleşenler aynı para birimi, maliyet esası ve durum tarihini kullanıyor.
- [ ] Formüller doğru uygulandı ve işaretler tutarlı yorumlandı (negatif = olumsuz).
- [ ] EAC birden fazla yöntemle verildi ve seçilen yöntem gerekçelendirildi.
- [ ] Öznel ilerleme ve çıkarılan nedenler varsayım olarak etiketlendi.
- [ ] Öneriler bir karar sahibi içeriyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Harcamayı ilerleme saymak (EV = AC). EV harcanan paradan değil, tamamlanan işten gelir.
- Projenin sonlarında yalnızca SPI'ya bakmak; proje gecikmiş olsa bile 1,0'a kayar. Kritik yolu veya kazanılmış takvimi kontrol et.
- Tek bir EAC'yi kesinmiş gibi sunmak. Yöntemler arasındaki aralığı göster.
- Tahakkuk gecikmesi: henüz kaydedilmemiş faturalar CPI'yı olduğundan iyi gösterir. Taahhüt edilmiş ama faturalanmamış maliyetleri sor.

## Örnek
Girdi: "BAC 1.200 bin. 5. ay durumu: PV 600 bin, EV 480 bin, AC 560 bin."

Çıktıdan bir bölüm:
- SV = −120 bin, SPI = 0,80; CV = −80 bin, CPI = 0,86.
- EAC (BAC/CPI) ≈ 1.400 bin; EAC (AC + BAC − EV) = 1.280 bin; VAC −80 bin ile −200 bin arasında.
- TCPI (BAC'ye göre) = 720/640 = 1,13: kapsam veya finansman değişikliği olmadan orijinal bütçe içinde toparlanmak gerçekçi değil. Karar sahibi: sponsor `[teyit et]`.
