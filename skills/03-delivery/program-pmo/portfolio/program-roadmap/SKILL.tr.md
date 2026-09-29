---
name: program-roadmap
description: "Birden fazla ekibin veya projenin işini ortak sonuçlara doğru sıralayan; ekipler arası kilometre taşlarını, entegrasyon noktalarını, karar kapılarını ve kritik yolu sahte kesinlik yerine güven düzeyleriyle gösteren bir program yol haritası oluşturur. Program birden fazla ekibe veya tedarikçiye yayıldığında, yönetim paralel iş akışlarının nasıl birleştiğini tek görünümde görmek istediğinde ya da program düzeyinde plan, zaman çizelgesi veya bütünleşik yol haritası istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: program-pmo
  area: portfolio
  title: "Program yol haritası"
  related: "cross-team-dependency-board, portfolio-prioritization, roadmap, release-planning, schedule-plan"
  prompt: "Çekirdek bankacılık geçişimiz için program yol haritası oluştur: 5 ekip, bir tedarikçi ve 4. çeyrekte yasal zorunlu canlıya geçiş var."
---

# Program Yol Haritası

## Amaç
Sponsorlara ve ekip liderlerine birden fazla iş akışının program sonucuna doğru nasıl ilerlediğini gösteren tek ve dürüst bir görünüm sunmak: her biri neyi ne zaman teslim ediyor, nerede buluşmaları gerekiyor, hangi kapılar devam kararını veriyor ve tarihlere ne kadar güveniliyor.

## Ne zaman kullanılır
- Program birlikte teslim etmesi gereken birden fazla ekibe, projeye veya tedarikçiye yayıldığında.
- Sabit bir dış tarih (mevzuat, sözleşme, pazar olayı) birleşen iş akışlarıyla karşılanmak zorunda olduğunda.
- Yönetim veya yönlendirme kurulu ayrı ekip planları yerine tek bir bütünleşik zaman çizelgesi istediğinde.

## Ne zaman kullanılmaz
- Tek bir ürün ekibi kendi sürümlerini planlıyorsa `roadmap` veya `release-planning` kullanılır.
- Tek bir proje için ayrıntılı görev takvimi gerekiyorsa `schedule-plan` kullanılır.
- Asıl ihtiyaç belirli bağımlılıkları müzakere edip izlemekse `cross-team-dependency-board` kullanılır.

## Girdiler
Zorunlu:
- Program hedefi veya sonucu ve varsa sabit tarihler.
- İlgili iş akışları veya ekipler ve her birinden beklenen teslimatlar.

İsteğe bağlı, kaliteyi artırır:
- Ekip planları, kapasite, tahminler veya verim verisi.
- Bilinen bağımlılıklar, ortak ortamlar, tedarikçi sözleşmeleri ve temin süreleri.
- Yönetişim kapıları, sürüm pencereleri, dondurma dönemleri, iş takvimleri.
- Daha önce kaydedilmiş riskler ve varsayımlar.

Hedef veya iş akışları eksikse sor. Bilinmeyen tarihler `[TBD]` olarak kalır; asla uydurulmaz.

## Süreç
1. Program sonucunu ve başarı ölçütlerini, sabit kısıtlarla birlikte (dış son tarihler, dondurma dönemleri, bütçe ufukları) yaz. Çıkarım olanları `[VARSAYIM]` olarak etiketle.
2. İş akışlarını (kulvarları) ve sahiplerini tanımla. Her iş akışının teslimatları etkinlik listesi değil, sonuç odaklı artımlar olmalı.
3. Kesinliğe uygun zaman ayrıntısını seç: uzak ufuk için ay veya çeyrek, yakın dönem için iterasyon veya hafta. Tarihler gerçekten belirsizse Şimdi/Sonra/Daha Sonra bantlarını kullan.
4. Her iş akışının ana teslimatlarını güven düzeyi (Yüksek/Orta/Düşük) ve tarihin dayanağıyla (ekip tahmini, tedarikçi taahhüdü, kestirim, hedef) yerleştir.
5. Entegrasyon noktalarını belirle: bir iş akışının çıktısının diğerinin girdisi olduğu yerler, ortak ortamlar, uçtan uca testler, veri göçleri, geçiş provaları. Her birine ID, tarih ve iki tarafın sahibini ver.
6. Program kilometre taşlarını ve karar kapılarını (ör. tasarım tamam, entegrasyon testine giriş, go/no-go) açık giriş kriterleriyle tanımla.
7. Bağımlılıklar ve entegrasyon noktaları üzerinden sabit tarihe giden kritik yolu çıkar; bolluğu hesapla veya tahmin et ve bolluğun olmadığı yerleri adlandır.
8. Kapasite ve takvimlere karşı stres testi yap: ortak ekiplerde çakışan yoğunluklar, tatil ve dondurma dönemleri, tedarikçi temin süreleri. Çakışmaları gizlemek yerine kaydet.
9. Yol haritasına yönelik başlıca riskleri sahibi ve azaltma önlemiyle, tarihlerin dayandığı varsayımlarla birlikte listele.
10. Güncelleme ritmini ve sahipliği belirle: hangi kulvarı kim, ne sıklıkla günceller ve hangi değişiklik kurul onayı gerektirir.
11. Hedef devam ediyorsa bağımlılıkları yönetmek için `cross-team-dependency-board`, sunmak için `steering-committee-pack` veya kapıları tanımlamak için `governance-framework` öner.

## Çıktı formatı
```markdown
# Program Yol Haritası: <program> — v<n> (<tarih>)
Sonuç: <hedef + ölçütler> · Sabit tarihler: <liste>

## Zaman Çizelgesi
| İş akışı / sahip | <dönem 1> | <dönem 2> | <dönem 3> | <dönem 4> |
|---|---|---|---|---|
| <ekip A> | <teslimat> (Y) | ... | ... | ... |
| Program kilometre taşları | ◆ M1 <ad> | ... | ◆ Kapı G2 | ◆ Canlıya geçiş |

## Entegrasyon Noktaları
| ID | Kimden → Kime | Aktarılan / test edilen | Tarih | Sahipler | Güven |
|---|---|---|---|---|---|

## Kilometre Taşları ve Kapılar
| ID | Kilometre taşı / kapı | Giriş kriterleri | Tarih | Karar sahibi |
|---|---|---|---|---|

## Kritik Yol
<zincir> · Bolluk: <değer veya yok>

## Kapasite ve Takvim Çakışmaları
## Riskler ve Varsayımlar
- [RİSK] ... — sahip — azaltma
- [VARSAYIM] ...
## Güncelleme Ritmi ve Değişiklik Kontrolü
```

## Kalite kontrol listesi
- [ ] Her teslimatın ve entegrasyon noktasının sahibi, tarihi veya `[TBD]` işareti ve dayanağıyla birlikte güven düzeyi var.
- [ ] Entegrasyon noktaları iki tarafı ve neyin aktarıldığını ya da test edildiğini belirtiyor.
- [ ] Kapıların açık giriş kriterleri ve karar sahibi var.
- [ ] Her sabit tarihe giden kritik yol, bolluğu veya bolluğun yokluğuyla gösterildi.
- [ ] Kapasite ve takvim çakışmaları örtülmeden kaydedildi.
- [ ] Uydurulmuş tarih yok; çıkarımlar etiketli ve varsayım olarak listeleniyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ekip planlarını entegrasyon noktası olmadan yan yana dikmek. Programın riski ekiplerin arasında yaşar; her devri açık hale getir.
- Uzak gelecekteki tarihleri gelecek ayınkilerle aynı kesinlikte göstermek. İleriye gittikçe daha kaba bantlar ve güven düzeyleri kullan.
- Entegrasyonu ve uçtan uca testi en sona koymak. Sorunların bolluk varken ortaya çıkması için erken entegrasyon kilometre taşları planla.

## Örnek
Girdi: "Çekirdek bankacılık geçişi: 5 ekip + tedarikçi, 4. çeyrekte yasal zorunlu canlıya geçiş."

Çıktıdan bir bölüm:
| ID | Kimden → Kime | Aktarılan / test edilen | Tarih | Güven |
|---|---|---|---|---|
| IP-03 | Tedarikçi çekirdek → Ödemeler ekibi | Test ortamında ödeme API'si | 2. çeyrek sonu `[TBD]` | Düşük (tedarikçi taahhüdü imzalanmadı) |
| IP-05 | Veri ekibi → Tümü | 1 numaralı tam göç provası | 3. çeyrek ortası | Orta |

Kritik yol: tedarikçi API'si (IP-03) → ödeme entegrasyonu → uçtan uca test → go/no-go. Bolluk: yaklaşık 3 hafta `[VARSAYIM]`; tedarikçide bunu aşan her kayma yasal tarihi tehdit eder.
