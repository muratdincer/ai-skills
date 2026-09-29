---
description: "Önerilen bir girişimin veya çözüm seçeneğinin teknik, operasyonel, ekonomik, zaman, yasal/uyum ve organizasyonel açıdan yapılabilir olup olmadığını değerlendirir; her boyutu kanıtla puanlar, koşulları ve engelleyicileri adlandırır, devam, koşullu devam veya durdurma önerir. Bir fikir veya talep yatırım öncesi değerlendirilecekse, çözüm seçenekleri üst düzeyde karşılaştırılacaksa ya da 'bunu gerçekten yapabilir miyiz?' diye sorulduğunda kullanılır."
related: "cost-benefit-analysis, build-vs-buy, pre-mortem, risk-register, technology-selection"
prompt: "Şirket içi CRM'imizi 6 ay içinde bir SaaS CRM ile değiştirmenin fizibilitesini değerlendir; 2 geliştiricimiz var ve KVKK gereksinimlerimiz sıkı."
---

# Fizibilite Değerlendirmesi

## Amaç
Karar vericilere, para ve insan kaynağı ayrılmadan önce bir girişimin gerçek kısıtlar altında başarılı olup olamayacağına dair kanıta dayalı bir görünüm sunmak; sağlanması gereken koşulları ve girişimi durduracak engelleyicileri açıkça göstermek.

## Ne zaman kullanılır
- Bir talep veya fikir sınıflandırmadan geçtiyse ve ayrıntılı analiz veya bütçe öncesinde devam/durdur kararı gerekiyorsa.
- İki üç çözüm seçeneği tam karşılaştırmadan önce elenecekse.
- Son tarih, bütçe veya ekip büyüklüğü sıkışık görünüyorsa ve birinin gerçekçi olup olmadığını söylemesi gerekiyorsa.

## Ne zaman kullanılmaz
- ROI ve geri dönüş süresiyle finansal gerekçe gerekiyorsa `cost-benefit-analysis` kullanılır.
- Belirli bir bileşen için geliştir, satın al veya yeniden kullan sorusu varsa `build-vs-buy` kullanılır.
- Seçenek belirlendiyse ve teslimat riskleri çıkarılacaksa `risk-register` veya `pre-mortem` kullanılır.

## Girdiler
Zorunlu:
- Girişimin veya değerlendirilecek seçeneklerin tarifi.
- Şu ana kadar bilinen temel kısıtlar (son tarih, bütçe zarfı, ekip, mevzuat) ya da bunların bilinmediği bilgisi.

İsteğe bağlı, kaliteyi artırır:
- Mevcut sistem haritası, entegrasyon noktaları, veri hacimleri.
- Mevcut yetkinlik ve kapasite, tedarikçi bilgisi, kurumun değişim geçmişi.
- Zorunlu politikalar (güvenlik, verinin tutulduğu yer, satın alma).

Girişim tarifi yoksa iste. Bilinmeyen kısıtlarda ilerle ve bunları açık soru olarak listele; doldurmaya çalışma.

## Süreç
1. Girişimi ve başarı kriterlerini iki üç satırda yeniden ifade et; birden fazla seçenek varsa S1, S2... diye adlandır.
2. Teknik: mevcut mimariyle uyum, entegrasyon karmaşıklığı, veri taşıma, gereken teknolojinin olgunluğu, NFR'ler (performans, güvenlik, erişilebilirlik), kurum içi yetkinlik.
3. Operasyonel: kullanıcılar ve operasyon bunu işletebilecek mi? Süreç değişiklikleri, destek modeli, eğitim yükü, yoğun dönemler.
4. Ekonomik: yalnızca büyüklük mertebesinde maliyet ve fayda sürücüleri; verilen rakamlara atıf yap, yoksa sürücüleri tarif et ve tahminleri `[VARSAYIM]` olarak işaretle.
5. Zaman: kritik yol kalemlerini (satın alma, güvenlik onayı, taşıma, dondurma dönemleri) hedef tarihle karşılaştır; tek bir tarih değil gerçekçi bir aralık ver.
6. Yasal/uyum: KVKK/GDPR (verinin yeri, yurt dışına aktarım, veri işleyen sözleşmeleri), sektör mevzuatı, sözleşmeler ve lisanslama.
7. Organizasyonel: sponsorluk, paydaş hazırlığı, rakip girişimler, değişim yorgunluğu.
8. Her boyutu Yapılabilir / Koşullu yapılabilir / Yapılamaz / Bilinmiyor olarak, kanıtıyla ve puanı değiştirecek koşulla değerlendir.
9. Engelleyicileri (herhangi biri tek başına durdurma demektir) ve önce doğrulanması gereken temel varsayımları, en ucuz kontrolden başlayarak listele (spike, tedarikçi demosu, hukuk görüşü).
10. Öneri ver: Devam, Koşullu devam, Durdur veya Daha fazla bilgi gerekli; öneriyi neyin değiştireceğini belirt.
11. Kullanıcı devam etmek isterse finansal gerekçe için `cost-benefit-analysis`, seçenek belirlemek için `build-vs-buy` veya `technology-selection`, teslimat riskleri için `risk-register` öner.

## Çıktı formatı
```markdown
# Fizibilite Değerlendirmesi: <girişim>
Seçenekler: <S1, S2 ... veya tek> · Hedef: <verildiği haliyle tarih / bütçe / kısıtlar>

## Özet ve Öneri
<Devam / Koşullu devam / Durdur / Daha fazla bilgi gerekli> – <2-3 satır gerekçe>

## Boyut Puanları
| Boyut | Puan | Kanıt | Koşul / neyin değiştireceği |
|---|---|---|---|
| Teknik | | | |
| Operasyonel | | | |
| Ekonomik | | | |
| Zaman | | | |
| Yasal / uyum | | | |
| Organizasyonel | | | |

## Engelleyiciler
- ...

## Önce Doğrulanacak Varsayımlar
| Varsayım | Doğrulama yöntemi | Sorumlu | Gereken tarih |
|---|---|---|---|

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Her boyutun bir puanı ve kanıtı var; kanıt yoksa tahmin değil Bilinmiyor yazıldı.
- [ ] Hiçbir maliyet, fayda veya tarih uydurulmadı; tahminler `[VARSAYIM]` işaretli aralıklar.
- [ ] Engelleyiciler sıradan risklerden ayrıldı.
- [ ] Öneri puanlardan çıkıyor ve onu neyin değiştireceğini belirtiyor.
- [ ] Kişisel veri söz konusuysa yasal ve veri koruma boyutu değerlendirildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Teknik olarak yapılabilir" deyip durmak. Girişimlerin çoğu teknolojiden değil zaman, operasyon veya organizasyon nedeniyle başarısız olur.
- Tek noktalı tarih vermek. Kritik yol sürücüleriyle bir aralık sun.
- Sponsorun hevesinin bilinmeyenleri doldurmasına izin vermek. Bilinmeyen, doğrulanana kadar Bilinmiyor olarak kalır.

## Örnek
Girdi: "Şirket içi CRM'i 6 ayda SaaS CRM ile değiştirmek; 2 geliştirici; sıkı KVKK gereksinimleri."

Çıktıdan bir bölüm:
| Boyut | Puan | Kanıt | Koşul |
|---|---|---|---|
| Yasal / uyum | Bilinmiyor | SaaS tedarikçisinin verinin tutulduğu yer bilgisi verilmedi | Veri onaylı bir konumda tutulursa veya geçerli bir aktarım mekanizması varsa yapılabilir |
| Zaman | Koşullu yapılabilir | 2 geliştiriciye karşı taşıma + 5 entegrasyon `[VARSAYIM]` | Yalnızca entegrasyonları tedarikçi veya bir iş ortağı üstlenirse geçerli |

Öneri: Daha fazla bilgi gerekli – taahhüt öncesi verinin tutulduğu yeri ve entegrasyon sayısını teyit et.
