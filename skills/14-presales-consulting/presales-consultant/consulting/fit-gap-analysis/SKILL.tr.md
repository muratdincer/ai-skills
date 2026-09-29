---
description: Gereksinimleri bir paketin, platformun veya referans sürecin standart yetenekleriyle karşılaştıran bir fit-gap analizi yapar; her gereksinimi uygun (fit), konfigürasyonla uygun, boşluk (gap) veya uygulanamaz olarak sınıflandırır, her boşluk için efor bandı ve riskiyle bir çözüm önerir (süreç değişikliği, konfigürasyon, genişletme, entegrasyon, üçüncü taraf, geçici çözüm, erteleme) ve uyum oranını ve gereken kararları özetler. Bir ERP, CRM, SaaS veya başka bir paket çözüm değerlendirilirken ya da uygulanırken, müşteri paketin ne kadar özelleştirme gerektireceğini sorduğunda veya gereksinimler standart bir sürece hizalanacakken kullanılır.
related: requirements-gap-analysis, build-vs-buy, vendor-evaluation, current-state-assessment, effort-estimate-for-bid
prompt: Bu 40 siparişten tahsilata (order-to-cash) gereksinimini standart bir bulut ERP satış modülüyle karşılaştıran fit-gap analizi yap ve özelleştirmenin kaçınılmaz olduğu yerleri söyle.
---

# Fit-Gap Analizi

## Amaç
Gereksinim gereksinim, paketin kutudan çıktığı gibi neyi yaptığını, neyin konfigürasyon gerektirdiğini ve neyin uymadığını her boşluk için gerekçeli bir çözümle göstermek. Böylece müşteri sürecini mi ürünü mü ne kadar uyarlayacağına ve bunun efor ve risk olarak maliyetine karar verebilir.

## Ne zaman kullanılır
- Bir paket çözüm (ERP, CRM, İK, SaaS platformu) seçilirken, teklif edilirken veya uygulanırken.
- Müşteri paketin ne kadar özelleştirme, genişletme veya entegrasyon gerektireceğini sorduğunda.
- Gereksinimler tasarımdan önce standart veya referans bir sürece hizalanacaksa.

## Ne zaman kullanılmaz
- Bir gereksinim seti ürüne göre değil kendi eksikleri açısından kontrol ediliyorsa `requirements-gap-analysis` kullanılır.
- Birden fazla tedarikçi ağırlıklı puanlamayla karşılaştırılıyorsa `vendor-evaluation` kullanılır.
- Geliştirmek mi satın almak mı kararı veriliyorsa `build-vs-buy` kullanılır.

## Girdiler
Zorunlu:
- Gereksinim listesi (no, açıklama, biliniyorsa öncelik) veya kapsamdaki iş süreçleri.
- Karşılaştırılacak paket, platform veya referans süreç; gerekiyorsa sürümü/kapsamı.

İsteğe bağlı, kaliteyi artırır:
- Yetenek kanıtı olarak ürün dokümantasyonu, demo notları veya tedarikçi yanıtları.
- Müşteri önceliği (olmalı/olsa iyi/olabilir) ve mevzuat ya da yerelleştirme ihtiyaçları.
- Özelleştirme politikası (ör. "clean core", standart nesnelerde kod değişikliği yok).

Gereksinimler veya hedef paket yoksa sor. Kanıtı olmadan bir ürün yeteneğini asla iddia etme; `[TEDARİKÇİYLE DOĞRULA]` olarak işaretle.

## Süreç
1. Gereksinimleri normalize et: satır başına tek yetenek, sabit numaralar, öncelik ve süreç alanı. Bileşik gereksinimleri böl; belirsiz olanları puanlamak yerine `[BELİRSİZ]` olarak işaretle.
2. Kelimesi kelimesine gereksinimi asıl iş ihtiyacından ayır; eski çalışma biçimi yerine ihtiyaç karşılaştırıldığında görünen boşlukların çoğu ortadan kalkar.
3. Her gereksinim için karşılanma durumunu kanıt kaynağıyla belirle: Uygun (standart), Konfigürasyonla uygun (kod olmadan ayar, iş akışı, alan), Boşluk veya Uygulanamaz. Kanıt türünü kaydet (dokümantasyon, demo, tedarikçi beyanı, varsayım).
4. Her boşluk için çözüm seçeneklerini tercih sırasıyla belirle: standart süreci benimseme (süreç değişikliği), konfigürasyon, desteklenen mekanizmalarla genişletme, başka bir sistemle entegrasyon, üçüncü taraf eklenti, elle geçici çözüm veya erteleme. Sürüm yükseltmeyi güvenli tutan seçenekleri tercih et.
5. Her boşluğun efor bandını (K/O/B), yükseltme ve destek riskini ve iş kritikliğini puanla; bunları gerekçeli bir önerilen çözümde birleştir.
6. Müşteriye ait kararları işaretle: süreç değişikliğinin kabulü, özelleştirme politikasından sapma, olmazsa olmaz maddelerin ertelenmesi. Karar sahibinin türünü belirt.
7. Sık atlanan fonksiyonel olmayan ve kesişen alanları kontrol et: roller ve yetkiler, raporlama, yerelleştirme ve yasal gereksinimler (ör. e-fatura, vergi), veri taşıma, entegrasyonlar, denetim izi, performans, KVKK/GDPR.
8. Özetle: genel ve süreç alanı bazında kategori sayıları ve yüzdeleri, olmazsa olmaz boşluklar, boşlukların toplam efor bandı ve en önemli riskler.
9. Tedarikçi teyidi veya müşteri netleştirmesi gereken açık maddeleri sorumlusuyla listele.
10. Her çıkarımı ve kanıtla desteklenmeyen her yetenek iddiasını etiketle.
11. Hedef devam ediyorsa boşluk çözümlerini maliyetlendirmek için `effort-estimate-for-bid`, birden fazla paket karşılaştırılıyorsa `vendor-evaluation` veya üzerinde uzlaşılan kapsamı sabitlemek için `statement-of-work` öner.

## Çıktı formatı
```markdown
# Fit-Gap Analizi: <paket / kapsam>
## Özet
| Süreç alanı | Uygun | Konfig. ile uygun | Boşluk | Uyg. değil | Olmazsa olmaz boşluklar |
- Genel uyum oranı: ...  - Boşluk efor bandı: ...  - Öne çıkan riskler: ...

## Ayrıntılı Değerlendirme
| Ger. No | Gereksinim (ihtiyaç) | Öncelik | Sınıf | Kanıt | Çözüm | Efor | Yükseltme riski | Karar sahibi |

## Müşteri Kararı Gerektiren Boşluklar
| Ger. No | Seçenekler | Öneri | Ödünleşim |

## Kesişen Alan Kontrolleri
- Yetkiler / raporlama / yerelleştirme / taşıma / entegrasyonlar / denetim / gizlilik

## Açık Maddeler
| Madde | Kimden gerekli (tedarikçi / müşteri) | Sorumlu |

## Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Her gereksinimin tek bir sınıfı ve kanıt türü var; belirsiz olanlar puanlanmamış, `[BELİRSİZ]` olarak işaretli.
- [ ] Kanıtsız hiçbir yetenek iddiası yok; doğrulanmamış olanlar `[TEDARİKÇİYLE DOĞRULA]` olarak işaretli.
- [ ] Her boşluğun çözüm seçenekleri, önerisi, efor bandı ve yükseltme riski var.
- [ ] Genişletmelerden önce süreç değişikliği seçenekleri değerlendirilmiş.
- [ ] Müşteri kararları karar sahibi türüyle ayrı listelenmiş.
- [ ] Kesişen alanlar (yetkiler, yerelleştirme, taşıma, raporlama) kapsanmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İş ihtiyacı yerine eski sistemin davranışıyla karşılaştırmak. Boşlukları ve özelleştirmeyi şişirir.
- Satış demosunu kanıt saymak. Kanıt türünü kaydet ve kritik uyumları dokümantasyonla veya bir kavram kanıtıyla (PoC) doğrula.
- Yalnızca uyum yüzdesini raporlamak. Yüksek bir oran, maliyet ve riske hâkim olan birkaç olmazsa olmaz boşluğu gizleyebilir.

## Örnek
Girdi: "Gereksinim OTC-17: Kredi limiti kontrolü limiti aşan siparişleri durdurmalı ve bölge finans yöneticisine SMS ile bildirmeli."

Çıktıdan bir bölüm:
| Ger. No | Gereksinim (ihtiyaç) | Sınıf | Kanıt | Çözüm | Efor | Yükseltme riski |
|---|---|---|---|---|---|---|
| OTC-17a | Kredi limitini aşan siparişi durdur | Konfig. ile uygun | Ürün dokümanı `[TEDARİKÇİYLE DOĞRULA: sürüm]` | Kredi yönetimini konfigüre et | K | Düşük |
| OTC-17b | Finans yöneticisine SMS ile bildir | Boşluk | Yerleşik SMS yok `[VARSAYIM]` | Standart e-posta/iş akışı bildirimi (süreç değişikliği) veya SMS ağ geçidi entegrasyonu | K / O | Düşük / Orta |

- Müşteri kararı: SMS yerine e-posta bildirimi kabul edilir mi? Sahibi: finans süreç sahibi.
