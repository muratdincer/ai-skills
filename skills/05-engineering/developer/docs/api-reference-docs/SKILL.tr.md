---
description: HTTP, RPC veya mesaj tabanlı API'ler için kimlik doğrulamayı, her uç noktayı veya işlemi parametreleriyle, istek ve yanıt örneklerini, hata kodlarını, sayfalamayı, hız sınırlarını ve sürümlemeyi kapsayan API referans dokümantasyonunu bir sözleşmeden, koddan veya notlardan yazar. Bir API'nin tüketicilere yönelik referans dokümanına ihtiyacı olduğunda, mevcut doküman uygulamadan saptığında veya şartname olduğu hâlde açıklama ve örnek içermediğinde kullanılır.
related: api-contract, api-design-review, readme-writing, error-message-writing, changelog-entry
prompt: Bu OpenAPI dosyasından sipariş API'miz için referans doküman yaz. Tüketiciler hata kodlarının ne anlama geldiğini ve sayfalamanın nasıl çalıştığını sürekli soruyor.
---

# API Referans Dokümanı

## Amaç
Entegrasyon yapan geliştiricinin kaynak kodu okumadan veya ekibe sormadan API'yi ilk denemede doğru çağırabilmesini sağlamak: her işlem, alan, hata ve sınır çalışan bir örnekle anlatılır. Kesin bir referans dokümanı destek yükünü ve entegrasyon hatalarını azaltır.

## Ne zaman kullanılır
- Bir API başka ekiplere, iş ortaklarına veya kamuya açılırken.
- Bir sözleşme (OpenAPI, AsyncAPI, protobuf, GraphQL şeması) var ama açıklamaları boş ve örnek içermiyorsa.
- Tüketiciler hatalar, sayfalama, idempotency veya kimlik doğrulama konusunda kafa karışıklığı bildiriyorsa.

## Ne zaman kullanılmaz
- Sözleşmenin kendisini tasarlamak için `api-contract` kullanılır.
- API tasarımının iyi olup olmadığını değerlendirmek için `api-design-review` kullanılır.
- Ürünün bütünü için başlangıç veya eğitim içeriği için `readme-writing` veya `tutorial` kullanılır.

## Girdiler
Zorunlu:
- API yüzeyi için bir doğru kaynak: sözleşme dosyası, route tanımları veya handler kodu ya da işlemlerin kesin bir tarifi.

İsteğe bağlı, kaliteyi artırır:
- Kimlik doğrulama yöntemi, ortamlar ve base URL'ler.
- Hata modeli, hız sınırları, sayfalama ve sürümleme politikası.
- Gerçek (temizlenmiş) istek ve yanıt örnekleri, tüketicilerden gelen bilinen sorular.

API yüzeyine dair bir kaynak verilmediyse iste. Girdide olmayan bir uç noktayı, alanı veya hatayı asla belgeleme; şüphelenilen boşlukları açık soru olarak listele.

## Süreç
1. Kaynaktan yüzeyin envanterini çıkar: işlemler, path'ler veya topic'ler, metotlar, şemalar ve hangilerinin public, hangilerinin dahili olduğu. Yalnızca public olması amaçlanan yüzeyi belgele.
2. Genel bakışı bir kez yaz: ortam başına base URL'ler (bilinmiyorsa yer tutucu), kimlik doğrulama ve yetkilendirme (işlem başına scope veya rol), içerik türleri, sürümleme şeması ve kurallar (harf düzeni, tarih-saat formatı ve saat dilimi, para ve ondalık gösterimi, ID formatı).
3. Kesişen davranışları bir kez anlat ve onlara bağlantı ver: tam hata kodu listesiyle hata modeli, sayfalama (cursor veya offset, sınırlar, sıralama garantileri), filtreleme ve sıralama sözdizimi, idempotency anahtarları, hız sınırları ve bunları bildiren header'lar, yeniden deneme rehberi.
4. Her işlem için yaz: tüketici diliyle tek satırlık amaç, metot ve path, gereken yetki, path, query ve header parametreleri, istek gövdesi alanları ve durum kodu başına yanıt alanları.
5. Her alan için türü, zorunlu veya isteğe bağlı olduğunu, null olabilirliği, izin verilen değerleri veya formatı, kısıtları (uzunluk, aralık, desen) ve varsayılanı belirt; yalnızca adı değil anlamı anlat.
6. Her işlem için ana başarı durumunun ve en az bir hata durumunun eksiksiz istek ve yanıt örneğini, şemaya uyan sentetik veriyle ekle.
7. İşleme özgü hataları belgele: durum kodu, hata kodu, ne zaman oluştuğu ve tüketicinin ne yapması gerektiği (girdiyi düzelt, backoff ile yeniden dene, destekle iletişime geç).
8. Tüketicilerin güvendiği davranış garantilerini not et: idempotency, tutarlılık (nihai veya anlık), sıralama, yayılan olaylar veya e-postalar gibi yan etkiler ve yerine geçen işlemle birlikte kullanımdan kalkma durumu.
9. Örnekleri şemayla karşılaştır; sözleşme ile uygulama arasındaki her uyumsuzluğu sessizce birini seçmek yerine açık soru olarak işaretle.
10. Bilinmeyen değerleri `[BİLİNMİYOR]`, çıkarılan davranışları `[VARSAYIM]` olarak işaretle ve API sahibi için açık sorularda topla. Kullanıcı devam ederse belgeleme sırasında bulunan tasarım sorunları için `api-design-review`, API değişikliklerini yayımlamak için `changelog-entry` öner.

## Çıktı formatı
```markdown
# <API adı> Referansı
## Genel Bakış
Base URL'ler · Kimlik doğrulama · Sürümleme · Kurallar (tarihler, para, ID'ler)

## Hatalar
| HTTP durumu | Hata kodu | Anlamı | Tüketicinin yapacağı |
|---|---|---|---|

## Sayfalama, Hız Sınırları, Idempotency
...

## <İşlem adı>
`<METOT> <path>` — <amaç>. Yetki: <scope/rol>
### Parametreler
| Ad | Konum | Tür | Zorunlu | Açıklama / kısıtlar |
|---|---|---|---|---|
### İstek Gövdesi / Yanıt (<durum>)
| Alan | Tür | Zorunlu | Null olabilir | Açıklama / kısıtlar |
|---|---|---|---|---|
### Örnekler
<istek> / <yanıt> / <hata yanıtı>
### Hatalar
| Durum | Kod | Ne zaman | Aksiyon |
|---|---|---|---|

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Belgelenen her işlem, alan ve hata kaynakta var; hiçbir şey uydurulmadı.
- [ ] Her alanın yalnızca adı değil türü, zorunluluğu, null olabilirliği ve kısıtları var.
- [ ] Her işlemin şemaya uyan bir başarı örneği ve en az bir hata örneği var.
- [ ] Her hata kodu tüketiciye sonra ne yapacağını söylüyor.
- [ ] Örneklerde yalnızca sentetik veri var; gerçek müşteri verisi, token veya dahili sunucu adı yok.
- [ ] Kesişen kurallar (kimlik doğrulama, hatalar, sayfalama, sınırlar) bir kez tanımlanıp referans veriliyor, tutarsız biçimde tekrarlanmıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Alan adını tekrar eden açıklamalar ("customerId: müşteri ID'si"). Anlamı, formatı ve kaynağı (tüketicinin değeri nereden aldığı) yaz.
- Yalnızca mutlu yolu belgelemek. Entegrasyon süresinin çoğu hatalara, sayfalama kenarlarına ve yeniden denemelere harcanır.
- Dokümanın sözleşmeden sessizce sapmasına izin vermek. Uyuşmadıklarında bunu dile getir; birini seçme.

## Örnek
Girdi: `GET /orders` (query `cursor`, `limit`) ve `{code, message}` hata şeması içeren, açıklamaları boş bir OpenAPI.

Zayıf: "`limit` — limit."

Güçlü bölüm:
- `limit` | query | integer | isteğe bağlı | Sayfa boyutu, 1-100, varsayılan 20 `[VARSAYIM: varsayılan şartnamede yok, doğrula]`.
- `cursor` | query | string | isteğe bağlı | Önceki sayfanın `next_cursor` değerinden gelen opak değer; ayrıştırmayın veya kendiniz üretmeyin.
- Hatalar: `400` | `INVALID_CURSOR` | cursor süresi dolmuş veya bozuk | `cursor` olmadan ilk sayfadan yeniden başlayın.
- Açık soru: Sayfalama sırasında yeni siparişler gelirse sayfalar arası sıralama kararlı kalıyor mu?
