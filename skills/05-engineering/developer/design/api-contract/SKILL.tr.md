---
description: "Gereksinimlerden kaynaklar, operasyonlar, şemalar, hata modeli, güvenlik, sürümleme ve örnekler içeren OpenAPI (HTTP) veya AsyncAPI (olay/mesaj) şartnamesi biçiminde bir API sözleşmesi yazar. Yeni bir uç nokta, servis veya olayın uygulamadan önce üretici ve tüketiciler arasında mutabık kalınması gerektiğinde ya da OpenAPI/Swagger veya AsyncAPI şartnamesi istendiğinde kullanılır."
related: "api-design-review, api-reference-docs, integration-requirements, technical-design-doc, api-test-design"
prompt: "İş ortaklarının gönderi oluşturmasını, gönderi durumunu sorgulamasını ve teslim alınmadan önce gönderiyi iptal etmesini sağlayan bir servis için OpenAPI sözleşmesi yaz."
---

# API Sözleşmesi Yazma

## Amaç
Üretici ve tüketicilerin paralel olarak geliştirip test edebileceği, makinece okunabilir ve incelenebilir bir sözleşme üretmek. Bu sözleşme dokümantasyon, mock ve sözleşme testleri için tek doğru kaynak olarak kalır.

## Ne zaman kullanılır
- Yeni bir HTTP API'si veya olay akışı tasarlanıyor ve tüketiciler onu bekliyorsa.
- Mevcut bir API'nin yeni sürümü veya kırıcı değişikliği gerekiyor ve farkın açıkça yazılması gerekiyorsa.
- Entegrasyon gereksinimleri düz metin olarak var ve kesin bir şartnameye dönüşmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Önceden yazılmış bir API tasarımının incelenmesi gerekiyorsa `api-design-review` kullanılır.
- Mevcut bir şartnameden insanlara yönelik referans sayfaları gerekiyorsa `api-reference-docs` kullanılır.
- Entegrasyon ihtiyacı henüz net değilse önce `integration-requirements` kullanılır.

## Girdiler
Zorunlu:
- API'nin karşılaması gereken gereksinimler veya kullanım senaryoları ve etkileşimin istek/yanıt mı yoksa olay tabanlı mı olduğu.

İsteğe bağlı, kaliteyi artırır:
- Kurumun API kılavuzu (isimlendirme, sayfalama, hata formatı, sürümleme), kimlik doğrulama mekanizması, mevcut alan modeli.
- Tüketici listesi, beklenen hacimler, gecikme hedefleri, idempotency ihtiyaçları.

Etkileşim tarzı belirsizse sor. Eksik ayrıntılar şartnamede açıklamayla birlikte `[TBD]` olarak yazılır.

## Süreç
1. Tüketici kullanım senaryolarını listele ve bunlardan kaynakları (isimler) veya olay türlerini (geçmiş zamanlı olgular) türet; veritabanı tablolarını kopyalama.
2. HTTP için: doğru method semantiği, durum kodları, idempotency (güvensiz yeniden denemeler için `Idempotency-Key`) ve güncellemelerin çakıştığı yerlerde eşzamanlılık kontrolü (ETag / `If-Match`) ile operasyonları tanımla.
3. Olaylar için: kanalları/topic'leri, mesaj anahtarını (sıralama kapsamı), payload şemasını, başlıkları (event id, tür, zaman, correlation id), teslim semantiğini ve tüketicilerin mükerrer mesaj beklentisini tanımla.
4. Şemaları tür, format, zorunlu alan, enum, uzunluk ve desenlerle modelle; tarihler için ISO 8601, tutarlar için açık birim/para birimi kullan.
5. Tüm operasyonlar için tek bir hata modeli tanımla (kılavuz aksini söylemiyorsa HTTP için RFC 9457 problem details) ve makinece okunabilir, kararlı bir hata kodu listesi ver.
6. Koleksiyon davranışını tanımla: sayfalama (büyük veya değişen kümelerde cursor tercih edilir), filtreleme, sıralama, limitler.
7. Güvenlik şemalarını ve operasyon bazında scope'ları belirt; kişisel veri alanlarını işaretle ve en aza indir.
8. Sürümleme ve uyumluluk kurallarını yaz: hangi değişiklikler eklemeli sayılır, kırıcı değişiklikler nasıl getirilir ve nasıl kullanımdan kaldırılır.
9. Her operasyon için sahte verilerle en az bir gerçekçi istek/yanıt veya mesaj örneği ekle.
10. Şartnameyi her kullanım senaryosuna karşı zihnen doğrula ve açık soruları listele.
11. Hedef devam ediyorsa tüketici dokümantasyonu için `api-reference-docs`, resmi inceleme için `api-design-review` veya sözleşme testleri için `api-test-design` öner.

## Çıktı formatı
````markdown
# API Sözleşmesi: <ad> v<sürüm>
Tarz: HTTP (OpenAPI 3.1) | Olaylar (AsyncAPI 3.0) · Sahibi: <ekip> · Tüketiciler: <liste veya [TBD]>

## Kullanım Senaryosu - Operasyon Eşlemesi
| Kullanım senaryosu | Operasyon / olay |

## Şartname
```yaml
openapi: 3.1.0   # veya asyncapi: 3.0.0
info: { title: <ad>, version: <x.y.z> }
paths / channels: ...
components:
  schemas: ...
  securitySchemes: ...
```

## Hata Kodları
| Kod | HTTP durumu | Anlamı | İstemcinin yapacağı |

## Uyumluluk ve Sürümleme Kuralları
## Açık Sorular
````

## Kalite kontrol listesi
- [ ] Her kullanım senaryosu bir operasyona veya olaya eşleniyor, tersi de geçerli.
- [ ] Her operasyonun başarı ve hata yanıtları, güvenlik tanımı ve örneği var.
- [ ] İstemcinin yeniden deneyebileceği güvensiz operasyonlar idempotent ya da neden olmadığı yazılı.
- [ ] Alan adları, harf düzeni, tarih ve para formatları şartname boyunca tutarlı.
- [ ] Kişisel veri belirlendi ve yalnızca tüketicilerin ihtiyaç duyduğu alanlar açıldı.
- [ ] Şartname, belirtilen sürüm için sözdizimsel olarak makul bir YAML/JSON.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve varsayım ya da açık soru olarak listeli; dayanağı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Şemayı kilitleyen iç modelleri veya veritabanı kimliklerini dışarı açmak. Tüketici kullanım senaryolarından tasarla.
- Hata gövdesiyle `200` dönmek ya da her şey için genel `400` kullanmak. Kesin durum kodları ve kararlı hata kodları kullan.
- Yalnızca kimlik taşıyıp tüketiciyi geri çağrıya zorlayan ya da tüm aggregate'i döken olaylar. Bildirim ile durum aktarımı arasında bilinçli karar ver.
- "Bugün veri az" diye liste uç noktalarında sayfalama koymamak.

## Örnek
Girdi: "İş ortakları gönderi oluşturur, durum sorgular, teslim alınmadan önce iptal eder."

Çıktıdan bir bölüm:
- `POST /shipments` için `Idempotency-Key` zorunlu; `Location` ile `201` döner; `partnerReference` zaten varsa `409 SHIPMENT_DUPLICATE_REFERENCE`.
- `POST /shipments/{id}/cancellation` teslim alındıktan sonra `409 SHIPMENT_ALREADY_PICKED_UP` döner (`400` değil, durum çakışması).
- Açık soru: Durum ayrıca bir olay (`shipment.status-changed`) olarak mı yayınlanacak, yoksa yalnızca sorgulama mı? `[TBD]`
