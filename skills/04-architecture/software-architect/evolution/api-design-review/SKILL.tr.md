---
name: api-design-review
description: "Bir API tasarımını (OpenAPI/AsyncAPI spesifikasyonu, gRPC/protobuf tanımı, GraphQL şeması veya yazılı öneri) kaynak modellemesi, isimlendirme tutarlılığı, sürümleme ve uyumluluk, hata modeli, sayfalama ve filtreleme, idempotency ve eşzamanlılık, güvenlik ve işletilebilirlik açısından inceler; derecelendirilmiş bulguları somut düzeltmelerle verir. Bir API uygulanmadan veya yayımlanmadan önce önerildiğinde ya da değiştiğinde, genel veya iş ortağı API'si yayına çıkmak üzereyken veya mevcut bir API'nin tutarlılık denetimi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: software-architect
  area: evolution
  title: "API tasarımı inceleme"
  related: "api-contract, api-deprecation-plan, api-test-design, threat-model, api-reference-docs"
  prompt: "Yeni sipariş API'mizin OpenAPI spesifikasyonunu iş ortaklarına yayımlamadan önce incele. Sürümleme, hatalar ve sayfalamaya odaklan."
---

# API Tasarımı İnceleme

## Amaç
Tasarım hatalarını düzeltmesi hâlâ ucuzken bulmak: tüketiciler entegre olduktan sonra her isimlendirme, hata veya uyumluluk hatası kırıcı bir değişikliğe ya da kalıcı bir geçici çözüme dönüşür. İnceleme, verilen spesifikasyona dayanan bir karar ve önceliklendirilmiş düzeltme listesi üretir.

## Ne zaman kullanılır
- Yeni bir API veya önemli bir değişiklik tanımlandı ve uygulamadan önce onay bekliyor.
- Genel, iş ortağı veya ekipler arası bir API yayımlanmak ya da yeni sürüme geçmek üzere.
- Mevcut bir API yüzeyi tutarsız görünüyor ve kurum rehberine göre denetlenmesi gerekiyor.

## Ne zaman kullanılmaz
- Sözleşme henüz yok ve yazılması gerekiyorsa `api-contract` kullanılır.
- Bir endpoint veya sürüm emekliye ayrılıyorsa `api-deprecation-plan` kullanılır.
- Amaç uygulanmış bir API için test senaryolarıysa `api-test-design` kullanılır.

## Girdiler
Zorunlu:
- API tanımı (spesifikasyon, şema, IDL veya endpoint/operasyon, payload ve hataları içeren bir öneri).

İsteğe bağlı, kaliteyi artırır:
- Tüketiciler (iç, iş ortağı, genel) ve entegrasyon biçimleri; beklenen hacimler.
- Kurumun API rehberi, tutarlı kalınması gereken mevcut API'ler, kimlik doğrulama modeli.
- Uyumluluk taahhüdü (semantik sürümleme, destek süresi).

Tanım verilmemişse iste. Tüketiciler bilinmiyorsa dış tüketici varsay `[VARSAYIM]` ve daha katı uyumluluk çıtasıyla incele.

## Süreç
1. Bağlamı belirle: API stili (REST, gRPC, GraphQL, olay), tüketiciler ve uygulanan rehber. Rehber verilmemişse kullandığın temel çizgiyi (ör. kurumun kendi rehberi veya yaygın REST kuralları) `[VARSAYIM]` olarak belirt.
2. Kaynak ve operasyon modeli: kaynaklar tablolara veya ekranlara değil alan kavramlarına karşılık gelir; iyi gerekçelendirilmiş aksiyonlar dışında REST yollarında fiil yok; her operasyonun tek sorumluluğu var; N+1 çağrıya zorlayan geveze kalıplar yok.
3. İsimlendirme ve tutarlılık: yüzey başına tek harf düzeni, tutarlı çoğul kullanım, tanımlayıcılar, zaman damgaları (ofsetli ISO 8601), para (tutar + para birimi), belgelenmiş ve genişletilebilir enum'lar.
4. Sürümleme ve uyumluluk: açık bir sürümleme şeması; her değişikliği eklemeli veya kırıcı olarak sınıflandır; toleranslı okuyucu beklentisi belirtilmiş; istemciler bilinmeyen enum değerlerini ele alıyor.
5. Hata modeli: tek yapılandırılmış hata formatı (ör. RFC 9457 problem details), doğru durum kodları (400 ile 422, 401 ile 403, 404 ile 410, 409, 429), makinece okunabilir hata kodları, stack trace veya iç ayrıntı yok.
6. Koleksiyonlar: sınırsız her listede sayfalama (büyük veya değişken kümelerde cursor tercih edilir), azami sayfa boyutu, kararlı sıralama, filtreleme ve alan seçimi kuralları.
7. Idempotency ve eşzamanlılık: POST için idempotency anahtarıyla güvenli yeniden deneme, PUT/DELETE idempotent, iyimser eşzamanlılık (ETag/If-Match veya sürüm alanı), uzun süren operasyonlar açıkça modellenmiş.
8. Güvenlik: kimlik doğrulama şeması, nesne düzeyinde yetkilendirme (BOLA), operasyon başına kapsamlar, URL'de hassas veri yok, girdi sınırları, rate limit; OWASP API Security Top 10'a göre kontrol et. Payload'lardaki kişisel veriyi işaretle ve en aza indirmeyi öner.
9. İşletilebilirlik: korelasyon/trace ID'leri, rate limit başlıkları, kullanımdan kaldırma sinyali, önbellek başlıkları, taahhüt edildiyse belgelenmiş SLA'lar.
10. Her bulguyu Critical (yayını engeller), Required, Nit, Optional veya FYI olarak derecelendir; yalnızca sorunu değil somut düzeltmeyi (değişen yol, alan veya şema parçası) ver. Çıkarımları `[VARSAYIM]` olarak etiketle.
11. Karar ver ve hedef devam ediyorsa spesifikasyonu yeniden yazmak için `api-contract`, güvenlik ağırlıklı bulgular için `threat-model`, üzerinde anlaşılan davranışı kapsamak için `api-test-design` öner.

## Çıktı formatı
```markdown
# API Tasarım İncelemesi: <API adı / sürüm>
Stil: <REST/gRPC/GraphQL/olay> · Tüketiciler: <...> · Temel çizgi: <rehber>
Karar: Onay / Değişikliklerle onay / Yeniden tasarım

## Özet
- Güçlü yanlar: ...
- En önemli riskler: ...

## Bulgular
| # | Önem | Alan | Konum (yol/operasyon/alan) | Bulgu | Önerilen düzeltme |
|---|---|---|---|---|---|

## Uyumluluk Değerlendirmesi
| Değişiklik | Eklemeli / Kırıcı | Tüketici etkisi | Azaltma |
|---|---|---|---|

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her bulgu verilen tanımda somut bir konuma işaret ediyor ve önerilen bir düzeltmesi var.
- [ ] Hata modeli, sayfalama, idempotency ve sürümleme sorun bulunmasa bile ayrı ayrı değerlendirildi.
- [ ] Nesne düzeyinde yetkilendirme ve hassas veri ifşası kontrol edildi.
- [ ] Kırıcı değişiklikler belirlendi ve eklemeli olanlardan ayrıldı.
- [ ] Önem etiketleri tutarlı; kararı yalnızca Critical maddeler engelliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Stili incelerken anlamı kaçırmak: isimlendirme kusursuz ama yeniden denemede iki kez ücret çeken bir POST. Önce idempotency ve eşzamanlılığı kontrol et.
- Büyük ve sık değişen koleksiyonlarda offset sayfalama; kayıtlar atlanır veya tekrarlanır. Cursor öner.
- Hata gövdesiyle 200 döndürmek; istemcinin yeniden deneme ve izleme mantığını bozar.

## Örnek
Girdi: `POST /createOrder` şunu döndürüyor: `200 {"success": false, "msg": "Stok hatası"}`; `GET /orders` sayfalama olmadan tüm siparişleri döndürüyor.

Zayıf: "Endpoint'ler daha RESTful olabilir."

Güçlü örnekten bir bölüm:
| # | Önem | Alan | Konum | Bulgu | Önerilen düzeltme |
|---|---|---|---|---|---|
| 1 | Critical | Hatalar | POST /createOrder | Hata, serbest metinli mesajla 200 olarak dönüyor | `POST /orders`; problem details ile 409 döndür `{type, title, status, code: "OUT_OF_STOCK"}` |
| 2 | Critical | Koleksiyonlar | GET /orders | Sınırsız liste | `limit` (en fazla 100) ve `cursor` ekle; `next_cursor` döndür |
| 3 | Required | Idempotency | POST /orders | Yeniden deneme mükerrer sipariş oluşturabilir | `Idempotency-Key` başlığını kabul et; saklanan yanıtı yeniden döndür |
