---
name: code-explanation
description: "Bir kod parçasının ne yaptığını, muhtemelen neden böyle yazıldığını ve hangi riskleri taşıdığını okuyucunun ihtiyaç duyduğu derinlikte açıklar: tek paragraflık özet, kontrol ve veri akışının adım adım anlatımı, yan etkiler, varsayımlar, uç durumlar ve şüpheli noktalar. Biri kod yapıştırıp ne yaptığını, nasıl çalıştığını, neden belli bir şekilde davrandığını sorduğunda ya da kodu değiştirmeden veya incelemeden önce anlaması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: coding
  title: "Kodu açıklama"
  related: "legacy-code-comprehension, code-documentation, clean-code-review, regex-builder, technical-onboarding"
  prompt: "Bu fonksiyonun ne yaptığını açıkla ve içinde riskli görünen bir şey var mı söyle."
---

# Kodu Açıklama

## Amaç
Okuyucuya bir kod parçasının doğru bir zihinsel modelini hızla vermek: neyi başardığı, verinin içinden nasıl aktığı, dışarıda neye dokunduğu ve nerede kırılabileceği; kodun gösterdiğiyle çıkarım yapılanı net biçimde ayırarak.

## Ne zaman kullanılır
- Birinin bir fonksiyonu, sınıfı, sorguyu, script'i veya konfigürasyonu değiştirmeden önce anlaması gerektiğinde.
- Bir inceleyici veya yeni gelen "bu ne yapıyor?" ya da "bu neden X döndürüyor?" diye sorduğunda.
- Kod alışılmadık bir kalıp, kütüphane veya dil özelliği kullandığında.

## Ne zaman kullanılmaz
- Yabancı bir kod tabanının veya modül haritasının tamamı çıkarılacaksa `legacy-code-comprehension` kullanılır.
- Amaç bulgular içeren bir kalite değerlendirmesiyse `clean-code-review` veya `code-review` kullanılır.
- Çıktı kalıcı yorum veya docstring olacaksa `code-documentation` kullanılır.

## Girdiler
Zorunlu:
- Kod parçası veya dosya.

İsteğe bağlı, kaliteyi artırır:
- Dil/framework sürümü, çağıran kod veya bağlam, okuyucunun geçmişi, özel soru (ör. "neden yavaş", "neden null dönüyor").

Referans verilen bir fonksiyon, tip veya config sağlanmamışsa adından ve kullanımından yola çıkarak açıkla ve o kısmı `[İSİMDEN ÇIKARIM]` olarak işaretle.

## Süreç
1. Dili, framework'ü ve kodun türünü belirle (handler, domain mantığı, sorgu, script, config, test).
2. Alan terimleriyle tek paragraflık bir özet yaz: girdiler, çıktı, ana etki. Kullanıcı özel bir soru sorduysa önce onu yanıtla.
3. Kodu çalışma sırasıyla, satırları adımlar hâlinde gruplayarak anlat; alışılmadık olan sözdizimi değilse sözdizimini değil niyeti açıkla.
4. Veri akışını izle: her girdinin nereden geldiği, nasıl dönüştürüldüğü, neyin döndürüldüğü veya kalıcı hâle getirildiği.
5. Yan etkileri ve dış etkileşimleri listele: I/O, veritabanı yazmaları, ağ çağrıları, global veya paylaşılan durum, olaylar, loglama, zaman ve rastgelelik.
6. Örtük varsayımları ve sözleşmeleri belirt: null olabilirlik, sıralama, birimler, kodlama, saat dilimi, transaction sınırları, thread güvenliği.
7. Uç durumları gez: boş, null, çok büyük, mükerrer, eşzamanlı, her dış çağrının başarısız olması. Her birinde ne olduğunu söyle.
8. Riskleri ve tuhaflıkları önem derecesiyle (muhtemel hata, risk, kod kokusu) işaretle; her biri için satırı veya yapıyı ve nedenini ver; istenmedikçe kodu yeniden yazma.
9. Olguları çıkarımlardan ayır: "neden" veya görülmeyen kod hakkındaki her şey `[ÇIKARIM]` olarak etiketlenir.
10. Derinliği okuyucuya göre ayarla: önce kısa özet, altında ayrıntılar; kıdemli bir okuyucuya temel bilgileri anlatma.
11. Hedef devam ediyorsa açıklamayı kalıcı kılmak için `code-documentation`, iyileştirme bulguları için `clean-code-review` veya çevresindeki sistem de belirsizse `legacy-code-comprehension` öner.

## Çıktı formatı
```markdown
# Kod Açıklaması: <fonksiyon/dosya>
**Kısaca:** <tek paragraf>

## Adım Adım
1. <x-y satırları>: <ne ve neden>

## Veri Akışı
<girdi> → <dönüşüm> → <çıktı/kalıcılık>

## Yan Etkiler
- ...

## Varsayımlar ve Sözleşmeler
- ...

## Uç Durumlar
| Durum | Ne olur |

## Riskler ve Tuhaflıklar
| Önem | Nerede | Sorun | Neden önemli |

## Çıkarım / Doğrulanmamış
- [ÇIKARIM] ...
```

## Kalite kontrol listesi
- [ ] Özet, kullanıcının asıl sorusunu ilk satırlarda yanıtlıyor.
- [ ] Görülmeyen kod veya asıl niyet hakkındaki her iddia `[ÇIKARIM]` olarak etiketli.
- [ ] Tüm yan etkiler ve dış çağrılar listelendi.
- [ ] Uç durumlar "başarısız olabilir" değil somut sonuçlar belirtiyor.
- [ ] Açıklama derinliği okuyucuya uygun; satır satır sözdizimi anlatımı yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Niyeti ve akışı açıklamak yerine her satırı başka sözlerle tekrar etmek ("i'yi bir artırır").
- Kodun neden var olduğuna dair bir tahmini olgu gibi sunmak. Etiketle ve kimin veya neyin (geçmiş, kayıt) teyit edebileceğini öner.
- Lazy loading, örtük transaction veya varsayılan serileştirme gibi framework kurallarındaki gizli davranışı atlamak.

## Örnek
Girdi: ürünler üzerinde dönen, statik bir cache'ten `promo` okuyan ve `item.price` değerini değiştiren 25 satırlık `applyDiscount(cart)` fonksiyonu.

Zayıf: "Fonksiyon ürünler üzerinde döner ve fiyatlarını değiştirir."

Güçlü, bir bölüm:
- **Kısaca:** Aktif kampanyayı uygun sepet ürünlerine, her ürünün fiyatının üzerine yazarak uygular; bir şey döndürmez.
- Yan etki: `item.price` değerini değiştirir; iki kez çağrılırsa indirim iki kez uygulanır.
- Risk (muhtemel hata): yüzde tamsayı bölmesiyle hesaplanıyor; 999'un %15'i 149,85 değil 149 çıkar.
- [ÇIKARIM] Statik kampanya cache'i başka bir yerde yenileniyor; yenileme başarısız olursa bayat kampanyalar uygulanabilir.
