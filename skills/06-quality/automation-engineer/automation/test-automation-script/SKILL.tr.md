---
description: "Ekibin dili ve framework'ünde page object veya API istemcileri, bağımsız test verisi, koşula dayalı açık beklemeler ve kesin doğrulamalar kullanan bakımı kolay bir otomatik test yazar; önce testin doğru nedenle kaldığını gösterir. Manuel bir test case, senaryo veya Gherkin adımı otomatik test koduna dönüştürülecekken, bir UI veya API testi yazılması istendiğinde ya da mevcut bir otomatik test güvenilir olacak şekilde yeniden yazılacakken kullanılır."
related: automation-candidate-selection, automation-framework-design, test-case-writing, bdd-feature-file, flaky-test-analysis
prompt: "Bu test case'i TypeScript setimizde API testi olarak otomatikleştir: süresi dolmuş kuponla sipariş oluşturmak 422 dönmeli ve stok ayırmamalı."
---

# Otomatik Test Yazma

## Amaç
Yalnızca davranış bozulduğunda kalan, kaldığında kendini açıklayan ve UI ile veri değişikliklerinden etkilenmeyen otomatik test kodu üretmek. Böylece sete güven sürer ve bakımı ucuz kalır.

## Ne zaman kullanılır
- Bir test case, senaryo veya feature dosyası adımı otomasyon için seçildiğinde.
- Yeni bir UI yolculuğu veya API endpoint'i için kararlaştırılan seviyede otomatik kontrol gerektiğinde.
- Mevcut bir otomatik test okunaksız veya kırılgan olduğunda ve yeniden yazılması gerektiğinde.

## Ne zaman kullanılmaz
- Neyin otomatikleştirilmeye değer olduğuna hâlâ karar verilecekse `automation-candidate-selection` kullanılır.
- Setin henüz bir yapısı (katmanlar, koşucular, raporlama) yoksa `automation-framework-design` kullanılır.
- Üretim kodunun yanında geliştirici seviyesinde unit test yazılıyorsa `unit-test-writing` kullanılır.

## Girdiler
Zorunlu:
- Beklenen sonucuyla birlikte test edilecek davranış (test case, senaryo, story veya Gherkin).
- Test seviyesi (UI veya API) ve setin kullandığı dil/framework.

İsteğe bağlı, kaliteyi artırır:
- Mevcut page object'ler, API istemcileri, fixture'lar, yardımcılar ve isimlendirme kuralları.
- Seçiciler veya API sözleşmesi, kimlik doğrulama yaklaşımı, test verisi kurulum mekanizmaları, CI kısıtları.

Davranış, beklenen sonuç veya framework yoksa iste (tek seferde en fazla 3 soru). Seçici, endpoint veya alan adı uydurma; bunları açıkça işaretlenmiş `[TBD]` yer tutucuları olarak yaz ve açık soru olarak listele.

## Süreç
1. Davranışı tek bir test niyeti olarak yeniden yaz: "<durum> verildiğinde, <aksiyon> yapılınca, <gözlemlenebilir sonuç>". Birden fazla When veya Then varsa ayrı testlere böl.
2. Mevcut page object'leri, API istemcilerini ve fixture'ları yeniden kullan; yalnızca eksik metotları, ham tıklamalar değil kullanıcı veya iş aksiyonları olarak ekle (`checkout.applyCoupon(code)`).
3. Veriyi bağımsız hazırla: testin ihtiyacını API veya fixture ile benzersiz tanımlayıcılarla oluştur; asla başka bir teste veya paylaşılan değiştirilebilir kayıtlara bağlı olma. Temizlik veya yalıtımı planla.
4. Sağlam konum belirleyiciler veya sözleşme alanları seç: UI için özel test ID'leri veya erişilebilir rol/etiketler; API için şema alanları ve durum kodları. Konuma veya stile dayalı seçicilerden kaçın.
5. Sabit beklemeleri (sleep) üst sınırı belli, açık koşullara dayalı beklemelerle değiştir (eleman durumu, yanıtın gelmesi, olayın gözlemlenmesi).
6. Doğrulamaları iş tarafından görülebilen sonuçlar ve yan etkiler üzerine yaz (durum, gövde alanları, kalıcı durum, yayınlanan olay); mesajlar neyin beklendiğini söylesin. Önemli olduğu yerde olumsuz yan etkiyi de doğrula (stok ayrılmadı).
7. Önce testin doğru nedenle kaldığını göster: bilinen hatalı bir build'e karşı, geçici olarak ters çevrilmiş bir beklentiyle veya değiştirilmiş bir girdiyle; hata mesajının kuruluma değil davranışa işaret ettiğini teyit et.
8. Doğru build'e karşı geçmesini sağla ve deterministik olduğunu doğrulamak için tekrar tekrar (set paralel koşuyorsa paralel olarak da) koş.
9. Testi etiketle (seviye, özellik, risk) ve izlenebilirlik için gereksinim veya test case numarasına bağla.
10. Yer tutucuları, varsayımları ve hazırlık işlerini (eksik test ID'leri, veri besleme endpoint'leri) listele; kullanıcı devam ederse test kararsızsa `flaky-test-analysis`, paylaşılan yardımcılar eksikse `automation-framework-design` öner.

## Çıktı formatı
````markdown
# Otomatik Test: <test adı>
- Niyet: ... verildiğinde, ... yapılınca, ...
- Seviye: UI | API · İzlendiği yer: <gereksinim/test case no>
- Etiketler: ...

## Kod
```<dil>
<test kodu + yeni page object / API istemci metotları>
```

## Veri ve Yalıtım
- Kurulum: ... · Temizlik: ...

## Doğrulanmış Kalma
- Nasıl kaldırıldı: ... · Hata mesajı: ...

## Yer Tutucular ve Açık Sorular
- [TBD] <seçici/endpoint/alan> — kim teyit edebilir
- [VARSAYIM] ...
````

## Kalite kontrol listesi
- [ ] Test başına tek davranış; ad davranışı ve beklenen sonucu söylüyor.
- [ ] Sabit bekleme yok; tüm beklemeler üst sınırlı açık koşullara dayanıyor.
- [ ] Test verisi bağımsız oluşturuluyor ve test sırasına bağlı değil.
- [ ] Doğrulamalar iş tarafından görülebilen sonuçları ve ilgili olumsuz yan etkileri net mesajlarla kontrol ediyor.
- [ ] Test geçti ilan edilmeden önce doğru nedenle kaldığı gösterildi.
- [ ] Uydurma seçici, endpoint veya kimlik bilgisi yok; gizli bilgiler koddan değil konfigürasyondan geliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca "hata oluşmadı" diye doğrulamak. Kalamayan bir test hiçbir şey kanıtlamaz; belirli sonucu doğrula.
- Testleri zincirlemek (B testi A testinde oluşturulan siparişi kullanır). Paralel koşumu bozar ve asıl hatayı gizler.
- Konum belirleyicileri ve beklemeleri test gövdesine koymak. Bunları page object'lerde tut ki bir UI değişikliği tek yerde düzeltilsin.

## Örnek
Girdi: "Süresi dolmuş kuponla sipariş 422 dönmeli ve stok ayırmamalı" — API seviyesi, TypeScript.

Zayıf: `await post('/orders', body); expect(res.ok).toBe(false);` — herhangi bir hata (yetki, 500) testi geçirir.

Güçlü, bir bölüm:
```ts
test('süresi dolmuş kuponlu siparişi reddeder ve stok ayırmaz', async ({ api, data }) => {
  const product = await data.createProduct({ stock: 5 });
  const coupon = await data.createCoupon({ expiresAt: daysAgo(1) });
  const res = await api.orders.create({ productId: product.id, qty: 1, coupon: coupon.code });
  expect(res.status, 'süresi dolmuş kupon doğrulama hatası olmalı').toBe(422);
  expect(res.body.errors[0].field).toBe('coupon'); // [TBD] hata yapısını sözleşmeden teyit et
  expect((await api.products.get(product.id)).stock).toBe(5);
});
```
