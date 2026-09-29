---
description: "Bir gereksinim dokümanını veya hikaye setini onaydan önce kontrol listesine dayalı, yapılandırılmış bir incelemeden geçirir: yapı, tekil gereksinim kalitesi (ISO/IEC/IEEE 29148 özellikleri), set düzeyinde bütünlük ve tutarlılık, NFR'ler, izlenebilirlik ve onaya hazırlık. Bulguları ve geçer/geçmez önerisini döndürür. Bir BRD, FRD, SRS veya backlog dilimi temel sürüme alınmadan, tedarikçiye verilmeden veya onaylanmadan önce kullanılır."
related: "ambiguity-detection, requirements-gap-analysis, requirements-consistency-check, requirements-sign-off, document-review"
prompt: "Bu FRD'yi iş birimine onaya göndermeden önce incele. Düzgün bir kontrol listesi kullan ve hazır olup olmadığını söyle."
---

# Gereksinim Gözden Geçirme

## Amaç
Onaylayana bir gereksinim paketinin temel sürüme alınmaya uygun olduğu konusunda güven vermek. İnceleme tutarlı bir kontrol listesi uygular, bulguları önem derecesine göre kaydeder ve net bir hazır olma kararı ile oraya ulaşmak için gereken düzeltmelerle biter.

## Ne zaman kullanılır
- Bir BRD, FRD, SRS veya hikaye seti onaylanmak ya da temel sürüme alınmak üzereyken.
- Gereksinimler bir tedarikçiye, başka bir ekibe veya sabit fiyatlı tahmine verilirken.
- Bir akran incelemesi veya kalite kapısı, incelemenin belgelenmesini gerektiriyorsa.

## Ne zaman kullanılmaz
- Yalnızca ifade netliği gerekiyorsa `ambiguity-detection` kullanılır.
- Onay paketinin kendisi gerekiyorsa `requirements-sign-off` kullanılır.
- Doküman bir gereksinim dokümanı değilse (ör. tasarım, politika) `document-review` kullanılır.

## Girdiler
Zorunlu:
- Gereksinim dokümanı veya hikaye seti.

İsteğe bağlı, kaliteyi artırır:
- Talep dokümanı veya iş hedefleri.
- Kurum şablonu veya zorunlu bölümler.
- İstenen inceleme derinliği (hızlı tarama veya tam inceleme) ve dokümanın hedef kitlesi.

İnceleme derinliği verilmediyse tam inceleme yap ve bunu belirt.

## Süreç
1. Yapı kontrolü: gerekli bölümler var mı (amaç, kapsam, paydaşlar, sözlük, varsayım/kısıtlar, fonksiyonel, NFR, veri, arayüzler, geçiş, açık konular), sürüm ve değişiklik geçmişi, sahip.
2. Tekil gereksinim kontrolü, ISO/IEC/IEEE 29148 özelliklerine göre: gerekli, uygun (doğru soyutlama, tasarım içermiyor), tek anlamlı, eksiksiz, tekil, yapılabilir, doğrulanabilir, doğru, standarda uygun. ~50'den az gereksinim varsa hepsini; fazlaysa tüm yüksek öncelikliler ile belirtilen bir örneklemi incele.
3. Set düzeyi kontrol: hedeflere göre eksiksiz, tutarlı (çelişki/tekrar yok), kısıtlar içinde yapılabilir, hedef kitlesi için anlaşılır, sınırlı (kapsam ve kapsam dışı açık).
4. NFR kontrolü: performans, erişilebilirlik (availability), güvenlik, gizlilik (kişisel veri varsa KVKK/GDPR), UI için erişilebilirlik (WCAG 2.2), denetlenebilirlik, işletilebilirlik; her biri ölçülebilir.
5. Veri ve arayüz kontrolü: ana varlıklar, doğrulama kuralları, saklama süresi, arayüz tarafları, hata yönetimi.
6. İzlenebilirlik kontrolü: her gereksinimin ID'si, önceliği ve kaynağı var; hedefler gereksinimlere bağlanıyor.
7. Hazırlık kontrolü: açık konuların sorumlusu ve tarihi var; varsayımlar listelenmiş; onaylayanlar adlandırılmış.
8. Bulguları konum, kontrol maddesi, önem derecesi (Kritik / Büyük / Küçük / Yazım) ve önerilen düzeltmeyle kaydet.
9. Karar ver: Hazır / Koşullu hazır (koşulları listele) / Hazır değil. Kritik bulgu her zaman Hazır değil demektir.
10. Kullanıcı devam etmek isterse karar Hazır ise `requirements-sign-off`, bulguları kapatmak için ise `requirements-gap-analysis` / `ambiguity-detection` öner.

## Çıktı formatı
```markdown
# Gereksinim İncelemesi: <doküman> v<sürüm>
İnceleyen: <ad/rol veya yapay zekâ destekli> · Tarih: <tarih> · Derinlik: <tam / örneklem: hangileri>

## Karar
<Hazır / Koşullu hazır / Hazır değil> – <tek satırlık gerekçe>
Koşullar: <varsa liste>

## Kontrol Listesi Sonuçları
| Alan | Madde | Sonuç (Geçti / Kaldı / N/A) | Not |
|---|---|---|---|

## Bulgular
| # | Konum | Kontrol maddesi | Önem | Bulgu | Önerilen düzeltme |
|---|---|---|---|---|---|

## İstatistik
Kritik n · Büyük n · Küçük n · Yazım n
```

## Kalite kontrol listesi
- [ ] Her kontrol alanı değerlendirildi veya gerekçesiyle N/A işaretlendi.
- [ ] Her gereksinim okunmadıysa örnekleme yaklaşımı belirtildi.
- [ ] Bulgular tam konumu gösteriyor ve uygulanabilir.
- [ ] Karar genel izlenime göre değil, önem derecesi kurallarına göre verildi.
- [ ] Yazım sorunları esasa ilişkin bulgularla karıştırılmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca dile bakıp bütün alanların (NFR, göç, raporlama) eksik olduğunu kaçırmak.
- Kritik bulguları onlarca yazım yorumunun arasında kaybetmek. Yazım maddelerini grupla ve en sona koy.
- Son tarih yakın diye açık Kritik maddelerle "Hazır" demek. "Koşullu hazır"ı yalnızca kritik olmayan maddeler için kullan.

## Örnek
Girdi: Hasar portalı için FRD v0.9, 64 gereksinim, NFR bölümü yok.

Çıktıdan bir bölüm:
Karar: Hazır değil – NFR bölümü yok; 3 gereksinim doğrulanamıyor.
| # | Konum | Kontrol maddesi | Önem | Bulgu | Önerilen düzeltme |
|---|---|---|---|---|---|
| B1 | Tüm doküman | NFR mevcut | Kritik | Performans, erişilebilirlik veya güvenlik gereksinimi yok | NFR bölümü ekle; bkz. `nfr-specification` |
| B2 | FR-17 | Doğrulanabilir | Büyük | "Hasarlar hızlıca işlenir" | Hedef süreyi `[TBD]` ve ölçüm noktasını tanımla |
