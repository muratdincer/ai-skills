---
name: authn-authz-design
description: "Bir uygulama veya API için kimlik doğrulama ve yetkilendirme tasarlar: kimlik sağlayıcı ve protokol seçimi (OIDC, OAuth 2.x, SAML), giriş ve token akışları, token süreleri ve saklama, roller, claim'ler veya öznitelikler ve en az yetki uygulama noktaları. Yeni uygulama veya API geliştirilirken, SSO ya da MFA eklenirken, API'ler iş ortaklarına veya makine istemcilerine açılırken ya da rol modeli yeniden tasarlanırken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: security-engineer
  area: design
  title: "Kimlik doğrulama ve yetkilendirme tasarımı"
  related: "security-requirements, threat-model, access-review, api-design-review, secrets-management-plan"
  prompt: "B2B SaaS ürünümüz için kimlik doğrulama ve yetkilendirme tasarla: web SPA, iş ortakları için açık REST API, çok kiracılı yapı; müşteriler kendi Entra ID veya Okta'ları ile SSO istiyor."
---

# Kimlik Doğrulama ve Yetkilendirme Tasarımı

## Amaç
Kimin, nasıl, hangi token'larla kimlik doğrulayabileceğini ve her kimliğin ne yapabileceğini belirten bir kimlik ve erişim tasarımı üretmek. Böylece uygulama tutarlı olur ve en az yetki ilkesi tasarım yoluyla uygulanır.

## Ne zaman kullanılır
- Yeni bir uygulama, API veya kiracı (tenant) modeli tasarlanırken.
- SSO, MFA, parolasız giriş ya da iş ortağı/makine erişimi eklenirken.
- Rol modeli plansız büyüdüğünde ve yeniden tasarlanması gerektiğinde.

## Ne zaman kullanılmaz
- Kimin hangi erişime sahip olduğunun gözden geçirilmesi gerekiyorsa `access-review` kullanılır.
- Yalnızca kimlik değil, tüm güvenlik kontrolleri gerekiyorsa `security-requirements` kullanılır.
- Gizli anahtarların saklanması ve rotasyonu planlanıyorsa `secrets-management-plan` kullanılır.

## Girdiler
Zorunlu:
- İstemci tipleri (tarayıcı SPA, sunucu taraflı web uygulaması, mobil, servis, CLI, iş ortağı) ve eriştikleri kaynaklar.

İsteğe bağlı, kaliteyi artırır:
- Mevcut kimlik sağlayıcı, dizin, kiracı modeli.
- Kullanıcı grupları (çalışan, müşteri, iş ortağı, yönetici) ve mevzuat ihtiyaçları (güçlü müşteri doğrulaması, KVKK/GDPR).
- Mevcut rol listesi, hassas işlemler, denetim gereksinimleri.

İstemci tipleri veya kaynaklar eksikse sor. Diğer boşluklar varsayım olarak kaydedilir.

## Süreç
1. Kimlikleri listele: insan kullanıcı grupları, servis kimlikleri, iş ortağı sistemleri, yönetici/destek personeli. Her kimliğin yaşam döngüsünün (işe giriş, görev değişikliği, ayrılış) sahibini not et.
2. İstemci başına protokol seç: tarayıcı ve mobil için PKCE ile OIDC authorization code; servisler için client credentials veya workload identity; adına yapılan çağrılar için token exchange; SAML yalnızca federasyon ortağı zorunlu kılıyorsa. Implicit ve password grant kullanma.
3. Kimlik doğrulama gücünü tanımla: MFA politikası, hassas işlemler için step-up, oturum süresi, yeniden doğrulama, hesap kurtarma ve kilitleme davranışı.
4. Token'ları tanımla: access token formatı (JWT veya opaque), audience, scope'lar, kısa ömür, refresh token rotasyonu ve bağlama, istemci başına saklama (SPA'larda local storage'da token yok; backend-for-frontend tercih edilir), iptal.
5. Yetkilendirme modelini seç: kaba görevler için RBAC; kiracı, sahiplik veya veri düzeyi kurallar için ABAC/ReBAC. Yetki matrisini yaz: rol x kaynak x eylem.
6. Uygulama noktalarını belirle: gateway (kimlik doğrulama, scope), servis (iş yetkilendirmesi, IDOR'a karşı nesne düzeyi kontroller), veri katmanı (satır düzeyi veya kiracı filtreleri).
7. En az yetki ve görevler ayrılığını uygula: varsayılan ret, joker scope yok, yönetici rolleri bölünmüş, izlenen acil durum (break-glass) hesapları.
8. Denetim loglamasını tanımla: kimlik doğrulama olayları, yetki değişiklikleri, reddedilen erişimler; loglarda kişisel veriyi maskele.
9. Karşılanan tehditleri (token hırsızlığı, replay, confused deputy, yetki yükseltme) ve kalan riskleri listele.
10. Kararları ve açık soruları bir ADR için kaydet.
11. Sonraki beceriyi öner: tasarımı test edilebilir kontrollere dönüştürmek için `security-requirements`, akışlara saldırgan gözüyle bakmak için `threat-model`, rollerin periyodik gözden geçirilmesi için `access-review`.

## Çıktı formatı
```markdown
# Kimlik Doğrulama/Yetkilendirme Tasarımı: <sistem>
## Kimlikler ve Yaşam Döngüsü
| Kullanıcı grubu | Doğruluk kaynağı | Yaşam döngüsü sahibi | MFA |
## İstemci Başına Akışlar
| İstemci | Protokol / grant | Token saklama | Oturum / token süresi |
## Token Tasarımı
- Audience, scope'lar, claim'ler, imzalama, rotasyon, iptal
## Yetkilendirme Modeli
| Rol / öznitelik | Kaynak | Eylemler | Koşul (kiracı, sahiplik) |
## Uygulama Noktaları
- Gateway: ... / Servis: ... / Veri: ...
## Yönetici, Acil Durum ve Destek Erişimi
## Denetim Olayları
## Karşılanan Tehditler ve Kalan Riskler
## Kararlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her istemci tipinin açık ve güncel en iyi uygulamaya uygun bir akışı var; implicit veya password grant yok.
- [ ] Nesne düzeyi yetkilendirme yalnızca gateway'de değil, serviste de uygulanıyor.
- [ ] Çok kiracılı sistemlerde kiracı izolasyonu birden fazla katmanda uygulanıyor.
- [ ] Token süreleri, rotasyon ve iptal tanımlı.
- [ ] Yönetici ve destek erişimi en az yetki ilkesine uyuyor ve denetleniyor.
- [ ] Bilinmeyen IdP yetenekleri veya politikaları `[BİLİNMİYOR]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her yetkiyi bir rol olarak kodlayıp rol patlamasına yol açmak. Veri düzeyi kurallar için öznitelik veya ilişki kullan.
- İstemciden gelen claim'lere güvenmek ya da audience doğrulamasını atlamak. Her serviste issuer, audience, imza ve süreyi doğrula.
- İş ortaklarına uzun ömürlü API anahtarları vermek. Kısa token'lı ve iş ortağı başına scope'lu client credentials tercih et.

## Örnek
Girdi: "Çok kiracılı B2B SaaS, SPA ve iş ortağı API'si var, müşteriler kendi Entra ID veya Okta'larını getiriyor."

Çıktıdan bir bölüm:
- SPA: backend-for-frontend üzerinden OIDC code + PKCE; HTTP-only cookie oturumu, tarayıcıda token yok.
- İş ortağı API'si: client credentials, 10 dakikalık access token [VARSAYIM], `orders.read`, `orders.write` scope'ları, iş ortağı başına bir istemci.
- Kiracı kuralı: her sorgu doğrulanmış token'daki `tenant_id` ile filtrelenir, ayrıca veritabanında satır düzeyi güvenlik uygulanır.
