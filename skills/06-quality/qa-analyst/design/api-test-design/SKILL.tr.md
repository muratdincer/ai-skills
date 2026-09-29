---
name: api-test-design
description: "Her endpoint için sözleşme ve şema, durum kodları, kimlik doğrulama ve yetkilendirme, girdi doğrulama, iş kuralları, idempotency, sayfalama, eşzamanlılık ve hata formatını; negatif ve güvenlik odaklı durumlarla birlikte kapsayan API testleri tasarlar. Bir API sözleşmesi (OpenAPI, GraphQL şeması, gRPC proto veya gayriresmî tanım) için test tasarımı gerektiğinde, API testleri otomatikleştirilmeden önce ya da mevcut API testlerinin yeterliliği incelenirken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: design
  title: "API testi tasarlama"
  related: "api-contract, api-design-review, test-automation-script, security-requirements, integration-test-writing"
  prompt: "POST /orders ve GET /orders/{id} için API testleri tasarla: JWT ile kimlik doğrulama, müşteriler yalnızca kendi siparişlerini görür, Idempotency-Key başlığı, doğrulama hatalarında 422."
---

# API Testi Tasarlama

## Amaç
Her endpoint'in sözleşmesini, iş davranışını ve güvenlik sınırlarını doğrulayan, önceliklendirilmiş ve otomasyona hazır eksiksiz bir API test tasarımı üretmek.

## Ne zaman kullanılır
- Yeni veya değişen bir endpoint'in sözleşmesi var ve geliştirme öncesinde ya da sırasında test gerekiyor.
- API otomasyonu başlamak üzere ve bir case envanteri gerekiyor.
- Tüketiciler entegrasyon hataları bildiriyor ve mevcut API test setinin kapsamından şüphe ediliyor.

## Ne zaman kullanılmaz
- Sözleşmenin tasarım kalitesinin incelenmesi gerekiyorsa `api-design-review` kullanılır.
- Otomasyon kodu gerekiyorsa `test-automation-script` kullanılır.
- Tam bir güvenlik değerlendirmesi veya sızma testi kapsamı gerekiyorsa `pentest-scope` ya da `threat-model` kullanılır.

## Girdiler
Zorunlu:
- API sözleşmesi veya tanımı (endpoint'ler, metotlar, istek/yanıt yapıları).

İsteğe bağlı, kaliteyi artırır:
- Yetki modeli (scope'lar, roller, tenant'lar), iş kuralları, hız limitleri, hata formatı standardı (ör. RFC 9457 problem details).
- Tüketici listesi, versiyonlama politikası, idempotency ve sayfalama kuralları, alt sistem bağımlılıkları.

Sözleşme veya örnek yoksa iste. Dokümante edilmemiş davranış varsayılan bir durum kodu değil, `[BİLİNMİYOR]` ve açık soru olur.

## Süreç
1. Endpoint ve operasyonların envanterini çıkar; her biri için kaynağı, metodu, yetki gereksinimini, yan etkilerini ve HTTP semantiğine göre güvenli/idempotent olup olmadığını not et.
2. Sözleşme testleri: yanıt şeması, zorunlu/isteğe bağlı alanlar, tipler, formatlar, enum değerleri, content type, başlıklar (önbellek, location, correlation ID) ve önceki versiyonla geriye dönük uyumluluk.
3. Fonksiyonel pozitif testler: operasyon başına ana başarı yolu; kalıcı durum ve yayımlanan olay veya mesajlar dahil.
4. Girdi doğrulama: eksik zorunlu alanlar, yanlış tipler, sınırlar, aşırı uzun metinler, geçersiz formatlar, bilinmeyen alanlar, boş gövde, bozuk JSON; dokümante edilmiş 4xx ve hata gövdesi beklenir.
5. Kimlik doğrulama: token yok, süresi dolmuş, bozuk, yanlış audience/issuer, iptal edilmiş. Yetkilendirme: yanlış rol, yanlış scope, başka tenant'ın veya kullanıcının kaynağı (BOLA/IDOR), korunan alanların toplu atanması (bkz. OWASP API Security Top 10).
6. İş kuralları ve durum: kaynağın mevcut durumunda geçersiz operasyonlar, çakışmalar (409), bulunamadı ile yasak ayrımı, ön koşul başlıkları (ETag/If-Match).
7. Güvenilirlik semantiği: idempotency anahtarları ve yeniden denemeler, mükerrer gönderimler, eşzamanlı güncellemeler, sayfalama/sıralama/filtreleme kararlılığı, hız sınırı (429 ve retry başlıkları), bağımlılık zaman aşımları.
8. Hata formatı tutarlılığı: aynı yapı, stack trace veya iç ayrıntı yok, correlation ID mevcut.
9. Her case'i riske göre önceliklendir (önce güvenlik ve veri bütünlüğü) ve hangisinin smoke, commit başına ve gece setinde koşacağını işaretle.
10. Veri ve ortam ihtiyaçlarını tanımla: test tenant'ları, rol başına token'lar, bağımlılık stub'ları veya sözleşme mock'ları.
11. Dokümante edilmemiş kodlar veya kurallar için açık soruları listele; kullanıcı devam ederse seti uygulamak için `test-automation-script`, sözleşmede boşluk varsa `api-design-review` öner.

## Çıktı formatı
```markdown
# API Test Tasarımı: <API / versiyon>
## Endpoint Envanteri
| Endpoint | Metot | Yetki | Idempotent | Yan etkiler |
|---|---|---|---|---|

## Test Case'leri
| ID | Endpoint | Kategori | Koşul | İstek özü | Beklenen durum | Beklenen gövde / etki | Öncelik | Set |
|---|---|---|---|---|---|---|---|---|

Kategoriler: Sözleşme, Pozitif, Doğrulama, AuthN, AuthZ, Durum/Kural, Güvenilirlik, Hata formatı.

## Test Verisi ve Ortam
- Token'lar / roller: ...
- Stub'lar / mock'lar: ...

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Her endpoint'in sözleşme, pozitif, doğrulama ve yetkilendirme case'leri var.
- [ ] Path veya gövdedeki her kaynak ID'si için kullanıcılar ve tenant'lar arası erişim (BOLA) test ediliyor.
- [ ] Beklenen durum kodları sözleşmeden geliyor; dokümante edilmemiş olanlar `[BİLİNMİYOR]` ve soru olarak yazılmış.
- [ ] API'nin vaat ettiği yerlerde idempotency, eşzamanlılık ve sayfalama kapsanmış.
- [ ] Hata yanıtları tutarlı yapı ve iç ayrıntı sızmaması açısından kontrol ediliyor.
- [ ] Test verisi yalnızca sentetik kimlikler ve token'lar kullanıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca durum kodunu doğrulamak. Yanlış gövdeli bir 200 veya eksik bir olay da hatadır; şemayı, değerleri ve yan etkileri doğrula.
- Yetkilendirmeyi yalnızca "token yok" ile test etmek. Gerçek ihlallerin çoğu, başkasının kaynağı için geçerli bir token kullanır.
- Uygulama ne dönüyorsa onu beklenen kabul etmek. Beklentileri sözleşmeden türet; uyumsuzluklar bulgudur.

## Örnek
Girdi: "POST /orders, GET /orders/{id}; JWT; müşteriler yalnızca kendi siparişlerini görür; Idempotency-Key başlığı; doğrulamada 422."

Çıktıdan bir bölüm:
| ID | Endpoint | Kategori | Koşul | Beklenen durum | Beklenen gövde / etki | Öncelik |
|---|---|---|---|---|---|---|
| API-07 | GET /orders/{id} | AuthZ | B müşterisinin geçerli token'ı, A müşterisinin siparişi | 404 veya 403 `[BİLİNMİYOR: hangisi]` | Sipariş verisi sızmaz | Yüksek |
| API-12 | POST /orders | Güvenilirlik | Aynı Idempotency-Key aynı gövdeyle iki kez | 201, ardından aynı yanıt tekrar döner `[VARSAYIM]` | Tam olarak bir sipariş kaydedilir | Yüksek |
| API-13 | POST /orders | Güvenilirlik | Aynı anahtar, farklı gövde | 422 veya 409 `[BİLİNMİYOR]` | Yeni sipariş oluşmaz | Orta |
