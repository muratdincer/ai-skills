---
name: api-deprecation-plan
description: "Bir API'nin, sürümün, endpoint'in, alanın veya olayın kullanımdan kaldırılmasını; tüketici envanteri, sürümleme stratejisi, makinece okunabilir Deprecation/Sunset sinyalleri, geçiş rehberi, brownout'lar ve ölçülebilir kaldırma kapılarıyla planlar. Kırıcı bir değişiklik, yeni bir API sürümü veya kaldırılan bir endpoint, iç ekiplere, iş ortaklarına ya da herkese açık tüketicilere sürpriz kesinti yaşatmadan ulaştırılacağı zaman kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: software-architect
  area: evolution
  title: "API kullanımdan kaldırma planı"
  related: "api-design-review, api-contract, migration-strategy, api-reference-docs, product-sunset-plan"
  prompt: "/v1/orders yerine /v2/orders geliyor (yeni sayfalama ve para formatı). İş ortaklarımız ve iç uygulamalarımız için v1'in kullanımdan kaldırma planını hazırla."
---

# API Kullanımdan Kaldırma Planı

## Amaç
Bir API yüzeyini güvenle kaldırmak: her tüketici bilinir, hem API yanıtları içinden hem dış kanallardan bilgilendirilir, test edilmiş bir geçiş yolu alır ve kaldırma ancak trafik verisi bunun güvenli olduğunu kanıtladığında yapılır.

## Ne zaman kullanılır
- Yeni bir ana sürüm eskisinin yerini aldığında veya bir endpoint, alan, parametre, olay ya da şema kaldırılırken.
- Kırıcı bir davranış değişikliği (hata formatı, sayfalama, kimlik doğrulama şeması) mevcut tüketicilere yayılacağında.
- Bir entegrasyon platformu veya gateway emekliye ayrılırken ve üzerindeki API'ler taşınacağında.

## Ne zaman kullanılmaz
- Müşteriye yönelik ürünün veya özelliğin tamamı kaldırılıyorsa `product-sunset-plan` kullanılır (API kısmı için bu beceri de kullanılır).
- Yeni API'nin kendisi henüz tasarım incelemesi bekliyorsa önce `api-design-review` veya `api-contract` kullanılır.
- Tüketiciye yansıyan sözleşme değişikliği olmayan bir veri veya platform geçişiyse `migration-strategy` kullanılır.

## Girdiler
Zorunlu:
- Kullanımdan kaldırılan API yüzeyi ve yerine geçen (veya "yerine geçen yok").

İsteğe bağlı, kaliteyi artırır:
- Tüketici listesi veya trafik verisi (API anahtarları, client ID'ler, user agent'lar, gateway logları) ve tüketici türleri (iç, iş ortağı, herkese açık, güncelleme döngüsü yavaş mobil uygulamalar).
- Sözleşmede veya yayımlanmış politikada yer alan kullanımdan kaldırma kuralları (asgari bildirim süresi, destek penceresi).
- Protokol ve stil: REST/HTTP, GraphQL, gRPC, asenkron olaylar.
- Hedef tarihler ve tetikleyici (güvenlik açığı, maliyet, platformun ömrünün sonu).

Kaldırılan yüzey belirsizse sor. Bilinmeyen tüketiciler, tarihler ve politikalar `[BİLİNMİYOR]`/`[TBD]` ve açık soru olur.

## Süreç
1. Değişikliği kesin olarak tanımla: eski yüzey, yerine geçen, alan alan kırıcı farklar ve kırıcı olmayan bir yolun (eklemeli değişiklik, adaptör, varsayılan değer) kullanımdan kaldırmayı tamamen gereksiz kılıp kılmayacağı. Çıkarımla bulunan farkları `[VARSAYIM]` olarak etiketle.
2. Tüketici envanterini hafızadan değil trafik kanıtından çıkar: tüketici ID'si, sahibi/iletişim, tür, çağrı hacmi, kullanılan endpoint'ler, son görülme, istemci sürüm döngüsü. Sahibi belirlenemeyen tüketiciler risktir; istemci kimliği yoksa zorunlu hale getirmeyi planla. API anahtarlarını ve kişisel veriyi maskele.
3. Sürümleme ve birlikte çalışma yaklaşımını seç (URI, header veya media-type sürümü; alan düzeyinde kaldırma; GraphQL `@deprecated`; protobuf `deprecated` seçeneği; yeni olay türü/topic) ve ikisinin ne kadar süre paralel çalışacağını belirle.
4. Politikayı ve takvimi belirle: duyuru tarihi, kullanımdan kaldırma tarihi, brownout pencereleri, sunset (kaldırma) tarihi. Bildirim süresi en az yayımlanmış politika veya sözleşmedeki asgari süre kadardır ve en yavaş tüketicinin (ör. mobil uygulamalar) sürüm döngüsüne yetecek uzunlukta olur.
5. Yanıt içi sinyalleri ekle: `Deprecation` yanıt header'ı (RFC 9745) ve `Sunset` header'ı (RFC 8594), geçiş rehberine giden `Link` ile (`rel="deprecation"`/`rel="sunset"`); API referansında uyarılar ve SDK'da derleme zamanı kullanımdan kaldırma işaretleri. Header değerlerini tam olarak belirt `[TBD tarihler]`.
6. Geçiş rehberinin taslağını yaz: önce/sonra istek ve yanıt örnekleri, alan eşleme tablosu, davranış farkları (hatalar, sayfalama, yuvarlama, saat dilimleri), SDK sürümleri, test sandbox'ı ve SSS.
7. Dış kanal iletişimini planla: changelog, geliştirici portalı duyurusu, envanterdeki her sahibe doğrudan e-posta, yüksek hacimli tüketiciler için iş ortağı hesap yöneticileri ve sabit T-eksi noktalarında hatırlatmalar.
8. Brownout'ları tasarla: bilinmeyen tüketicileri ortaya çıkarmak için eski yüzeyin dokümante edilmiş hatayı (ör. 410 Gone veya açık bir hata kodu) döndürdüğü planlı, duyurulmuş, süreli pencereler; süreyi kademeli artır, bir tüketicinin bilinen yoğun saatine denk getirme ve anında geri açma anahtarı bulundur.
9. Kaldırma kapılarını tanımla: eski yüzeydeki trafik N ardışık gün boyunca anlaşılan eşiğin `[TBD]` altında, adı bilinen tüm tüketiciler geçişi onaylamış veya açıkça kabul etmiş, açık geçiş engeli yok, destek ve nöbetçi ekip bilgilendirilmiş, geri alma (yeniden açma) test edilmiş. Her kapıyı bir sorumlu onaylar.
10. Kaldırmayı ve temizliği planla: sunset sonrası nihai yanıt davranışı (bağlantılı 410 veya 404), ilk günler için izleme ve alarm, ardından kodun, route'ların, dokümanların, SDK metotlarının ve gateway yapılandırmasının kaldırılması.
11. Riskleri, varsayımları ve açık soruları listele, ardından şablonu doldur. Sonraki becerileri öner: geçiş rehberi için `api-reference-docs`, yerine geçen sözleşme için `api-contract`, müşteriler işlev kaybediyorsa `product-sunset-plan`.

## Çıktı formatı
```markdown
# API Kullanımdan Kaldırma Planı: <yüzey> → <yerine geçen>
| Alan | Değer |
|---|---|
| Kaldırılan yüzey | <endpoint'ler / alanlar / olaylar> |
| Yerine geçen | <yüzey veya yok> |
| Kırıcı farklar | <liste> |
| Politika / asgari bildirim | <politika veya [BİLİNMİYOR]> |
| Sorumlu | <ekip veya [BİLİNMİYOR]> |

## Tüketici Envanteri
| Tüketici | Sahibi / iletişim | Tür | Hacim | Kullanılan endpoint'ler | Son görülme | Durum |
|---|---|---|---|---|---|---|

## Takvim
| Kilometre taşı | Tarih | Sinyal / aksiyon |
|---|---|---|
| Duyuru | [TBD] | changelog, e-posta, portal |
| Kullanımdan kaldırıldı | [TBD] | `Deprecation` + `Sunset` + `Link` header'ları |
| Brownout 1..n | [TBD] | <süre, dönen hata> |
| Sunset | [TBD] | <410 / 404 davranışı> |

## Geçiş Rehberi Taslağı
- Alan eşleme / önce-sonra örnekleri / davranış değişiklikleri / SDK / sandbox / SSS

## Kaldırma Kapıları
- [ ] <ölçülebilir koşul> — <sorumlu>

## Riskler, Varsayımlar, Açık Sorular
- [RİSK] ... / [VARSAYIM] ... / 1. <soru> — <sorumlu>
```

## Kalite kontrol listesi
- [ ] Tüketici envanteri trafik kanıtına dayanıyor ve kimliği belirsiz tüketiciler açıkça ele alınıyor.
- [ ] Her kırıcı fark geçiş eşlemesiyle birlikte listelendi.
- [ ] Hem yanıt içi (header, doküman, SDK) hem dış kanal (doğrudan temas, changelog) sinyalleri planlandı.
- [ ] Brownout'lar duyurulmuş, süreli ve geri alınabilir.
- [ ] Kaldırma kapıları ölçülebilir ve sahipli; tarih tek başına kapı değil.
- [ ] Hiçbir tarih, hacim veya tüketici adı uydurulmadı; bilinmeyenler işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca changelog girdisine güvenmek. Tüketicilerin çoğu onu okumaz; envanterdeki sahiplere doğrudan ulaş ve her yanıtta sinyal ver.
- Trafiğe bakmadan duyurulan tarihte kaldırmak. Tarih hedeftir; kararı kapılar verir.
- Yavaş hareket eden istemcileri unutmak (mobil uygulamalar, kurum içi kurulumlar, aylık çalışan batch işleri). Trafiğin bittiğine karar vermeden önce "son görülme"yi tam bir iş döngüsü boyunca kontrol et.
- Aynı sürüm içinde davranışı sessizce değiştirmek. Her kırıcı değişiklik ya yeni bir sürüm ya da bu planı gerektirir.

## Örnek
Girdi: "/v1/orders yerine /v2/orders geliyor (cursor sayfalama, para birimi küçük birim + döviz kodu). İş ortakları ve iç uygulamalar v1 kullanıyor."

Çıktıdan bir bölüm:
- Kırıcı farklar: offset → cursor sayfalama; `amount: 12.5` → `amount: {value: 1250, currency: "TRY"}` `[VARSAYIM – döviz kaynağını teyit et]`.
- Envanter: gateway loglarından 3 iç uygulama belirlendi; client ID'siz iş ortağı trafiği `[sahibi BİLİNMİYOR]` → kullanımdan kaldırma tarihinden itibaren `client_id` zorunlu.
- Sinyal: `Deprecation: @<unix-zamanı>`, `Sunset: <HTTP-tarihi>`, `Link: <https://.../migrate-v2>; rel="deprecation"` `[TBD tarihler]`.
- Kaldırma kapısı: v1 trafiği bir ay sonunu da kapsayan 30 ardışık gün boyunca günlük `[TBD]` isteğin altında ve her iş ortağı geçişi yazılı olarak onaylamış.
