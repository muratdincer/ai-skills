---
name: experiment-design
description: "Bir hipotezden yola çıkarak ürün deneyi (A/B testi, sahte kapı, boyalı kapı, concierge veya prototip testi) tasarlar; varyantları, rastgeleleştirme birimini, birincil ve koruma metriklerini, tespit edilebilir en küçük etkiyi, örneklem büyüklüğünü ve süreyi, durdurma kurallarını ve önceden taahhüt edilmiş karar kuralını belirler. Ekip bir hipotezi gerçek kullanıcılarla doğrulamak istediğinde, A/B veya sahte kapı testinin nasıl kurulacağını sorduğunda ya da bir deney planının yayından önce kontrol edilmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: discovery
  title: "Ürün deneyi tasarlama"
  related: "hypothesis-statement, ab-test-analysis, assumption-mapping, metric-definition, funnel-analysis"
  prompt: "Yeni fiyatlandırma sayfası tasarımımız için bir A/B testi tasarla; haftada yaklaşık 40.000 ziyaretçimiz var ve deneme kaydı oranı %3,2."
---

# Ürün Deneyi Tasarlama

## Amaç
Hipotezi gerçekten yanıtlayabilecek bir deney planı üretmek: doğru test türü, yeterli istatistiksel güç, temiz ölçüm ve daha hiçbir veri görülmeden sabitlenmiş bir karar kuralı.

## Ne zaman kullanılır
- Yazılmış bir hipotezin mühendislik yatırımından veya yaygınlaştırmadan önce test edilmesi gerektiğinde.
- Ekip bir A/B testi planlıyor ve örneklem büyüklüğü, süre ve metriklerin doğru kurulması gerekiyorsa.
- Henüz geliştirilmemiş bir özelliğe talep ölçülmek isteniyorsa (sahte kapı, bekleme listesi, concierge).
- Mevcut bir deney planının yayından önce hatalara karşı gözden geçirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Henüz net bir hipotez yoksa önce `hypothesis-statement` kullanılır.
- Deney tamamlandı ve sonuçların yorumlanması gerekiyorsa `ab-test-analysis` kullanılır.
- Soru keşif amaçlıysa ("kullanıcılar neden ayrılıyor?") `problem-interview-script` veya `research-plan` kullanılır.

## Girdiler
Zorunlu:
- Hipotez (değişiklik, segment, beklenen davranış değişikliği) ya da bir hipotez yazmaya yetecek bilgi.
- Haftalık yaklaşık trafik veya uygun kullanıcı sayısı.

İsteğe bağlı, kaliteyi artırır:
- Birincil metriğin başlangıç oranı/ortalaması ve varyansı; aksiyon almaya değecek en küçük etki.
- Kısıtlar: yasal/rıza kuralları, fiyat adaleti, satış taahhütleri, mühendislik eforu.
- Mevcut deney platformu kuralları (gruplama, maruz kalma kaydı).

Hipotez veya trafik bilgisi yoksa sor. Başlangıç değeri asla uydurulmaz; bilinmiyorsa önce bir başlangıç ölçümü adımı planla.

## Süreç
1. Hipotezi ve deneyin besleyeceği kararı yeniden yaz; hipotez belirsizse keskinleştir (segment, metrik, eşik) ve yaptığın değişiklikleri `[VARSAYIM]` olarak işaretle.
2. Test türünü en riskli varsayıma ve trafiğe göre seç: yeterli trafikli mevcut akışları iyileştirmek için A/B veya çok değişkenli test; talep için sahte kapı / boyalı kapı; değer sunumu için concierge veya Wizard-of-Oz; trafik çok düşükse moderasyonlu prototip testi.
3. Varyantları (kontrol ve en fazla 1-2 deney varyantı) ve farklılaşan tek değişkeni tanımla; aynı kalması gerekenleri listele.
4. Karışmayı önleyecek rastgeleleştirme birimini seç (kullanıcı, hesap, oturum, bölge); B2B ortak çalışma alanlarında ve ağ etkisi varsa hesap düzeyini kullan.
5. Birincil metriği (tek), ikincil metrikleri ve koruma metriklerini formül, kaynak ve maruz kalma tanımıyla ("deneyde" sayılan kim) belirle.
6. Örneklem büyüklüğünü başlangıç değeri, tespit edilebilir en küçük etki (MDE), anlamlılık düzeyi (genellikle alfa 0,05, çift yönlü) ve güçten (genellikle 0,8) hesapla; uygun trafikle süreye çevir ve haftalık döngüleri kapsamak için tam haftaya yuvarla. Süre kabul edilemeyecek kadar uzunsa MDE'yi büyüt, metriği değiştir veya test türünü değiştir.
7. Durdurma kurallarını belirle: sabit ufuk (ara bakış yok) ya da önceden ilan edilmiş sıralı (sequential) yöntem; erken durdurma yalnızca koruma metriği ihlali, hata veya örneklem oranı uyumsuzluğunda (SRM).
8. Karar kuralını önceden taahhüt et: "etkisiz" sonuç dahil her sonuç için yayınla / yinele / sonlandır.
9. Geçerlilik tehditlerini ve önlemleri listele: yenilik etkisi, mevsimsellik, SRM, bot trafiği, çakışan deneyler, ölçüm boşlukları; sahte kapıda kullanıcılara gösterilecek dürüst bilgilendirme mesajını planla.
10. Etik ve gizliliği ele al: rıza, ödeme yapan müşterilere yanıltıcı fiyat gösterilmemesi, olay kayıtlarında kişisel verinin en aza indirilmesi.
11. Planı sorumlularla, yayın kontrol listesiyle (varyant QA'i, olay doğrulaması, A/A veya SRM kontrolü) ve açık sorularla üret.
12. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: veri geldiğinde `ab-test-analysis`, birincil metrik henüz kesin tanımlı değilse `metric-definition`.

## Çıktı formatı
```markdown
# Deney Planı: <ad>
Hipotez: <tek cümle> · Karar sahibi: <ad | [BİLİNMİYOR]>

| Madde | Değer |
|---|---|
| Test türü | <A/B / sahte kapı / concierge / ...> – <neden> |
| Varyantlar | Kontrol: ... / Deney: ... |
| Rastgeleleştirme birimi | <birim> – <neden> |
| Uygun popülasyon | <segment, dahil/hariç> |
| Birincil metrik | <formül, kaynak, maruz kalma kuralı> |
| Koruma metrikleri | <metrik – eşik> |
| Başlangıç / MDE | <değer | [BİLİNMİYOR]> / <değer> |
| Alfa / güç | <değerler> |
| Varyant başına örneklem | <n> |
| Süre | <hafta> (<trafik varsayımı>) |
| Durdurma kuralları | ... |

## Karar Kuralı
| Sonuç | Karar |
|---|---|
| Anlamlı olumlu, koruma metrikleri sağlam | ... |
| Etkisiz / belirsiz | ... |
| Olumsuz veya koruma ihlali | ... |

## Geçerlilik Tehditleri ve Önlemler
- ...
## Yayın Kontrol Listesi
- [ ] Varyantlar test edildi  - [ ] Olaylar doğrulandı  - [ ] SRM kontrolü planlandı
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Kontrol ve deney varyantı arasında yalnızca tek değişken farklı.
- [ ] Örneklem büyüklüğü ve süre belirtilen girdilerden hesaplandı; verilmeyen girdiler `[BİLİNMİYOR]` veya `[VARSAYIM]` olarak işaretli.
- [ ] Süre en az bir tam haftalık döngüyü kapsıyor ve belirtilen trafikle uygulanabilir.
- [ ] Karar kuralı yayından önce olumlu, etkisiz ve olumsuz sonuçları kapsıyor.
- [ ] Koruma metrikleri ve durdurma kuralları var; ara bakış dışlandı ya da sıralı yöntem adlandırıldı.
- [ ] Gizlilik, rıza ve adalet riskleri ele alındı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çok az trafikle A/B testi yapıp gürültüyü sonuç sanmak. Önce gücü hesapla; hesap tutmuyorsa nitel teste geç.
- Testi anlamlı çıktığı gün durdurmak. Ufku sabitle veya önceden ilan edilmiş sıralı bir yöntem kullan.
- Kullanıcılar birçok kez geri dönerken oturum bazında rastgeleleştirmek. Değişikliği deneyimleyen birim üzerinden rastgeleleştir.
- Sahte kapı tıklamalarını ek bir adım olmadan satın alma niyeti saymak. İkinci bir taahhüt sinyali ekle (bekleme listesi, e-posta, ön sipariş).

## Örnek
Girdi: "Yeni fiyatlandırma sayfası tasarımı için A/B testi; haftada ~40.000 ziyaretçi, deneme kaydı %3,2."

Çıktıdan bir bölüm:
- Test türü: A/B, kullanıcı düzeyinde rastgeleleştirme (çerez + oturum açmış kullanıcı ID'si).
- Birincil metrik: deneme kayıtları / fiyat sayfasının tekil ziyaretçileri; koruma metriği: 14. günde denemeden ücretliye dönüşüm.
- Göreli %10 MDE (%3,2'den %3,52'ye), alfa 0,05 çift yönlü, güç 0,8: varyant başına yaklaşık 49.000, yani 2 varyantla yaklaşık 3 hafta.
- Karar kuralı: Etkisiz sonuç çıkarsa kontrol korunur, tasarıma yatırım durur; bunun yerine değer mesajı test edilir.
