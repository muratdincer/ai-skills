---
name: secure-code-review
description: "Kaynak kodu veya bir diff'i güvenlik zafiyetleri açısından inceler; bulguları OWASP Top 10 kategorileri ve CWE numaralarıyla eşler, güvenilmeyen girdiyi kaynaktan hedefe (sink) izler ve her bulgu için önem derecesi, kanıt ve somut düzeltme verir. Bir pull request kimlik doğrulama, yetkilendirme, girdi işleme, kriptografi, dosya veya ağ erişimine dokunduğunda ya da kodun zafiyet açısından kontrol edilmesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: security-engineer
  area: assessment
  title: "Güvenli kod incelemesi"
  related: "code-review, security-finding-report, vulnerability-triage, security-requirements, threat-model"
  prompt: "Merge etmeden önce bu ASP.NET Core controller'ı ve repository sınıfını güvenlik açısından incele."
---

# Güvenli Kod İncelemesi

## Amaç
Sürümden önce koddaki istismar edilebilir zayıflıkları bulmak ve geliştiricilere teorik gürültüye boğmadan, doğrulanabilir ve kesin düzeltmeler sunmak.

## Ne zaman kullanılır
- Bir değişiklik kimlik doğrulama, oturum, yetkilendirme, girdi ayrıştırma, sorgular, dosya işleme, deserialization, kriptografi veya dış çağrılara dokunduğunda.
- Bir SAST aracının ürettiği bulguların insan tarafından doğrulanması gerektiğinde.
- Kod sızma testi, denetim veya internete açılma öncesinde hazırlanırken.

## Ne zaman kullanılmaz
- Genel okunabilirlik veya tasarım incelemesi için `code-review` ya da `clean-code-review` kullanılır.
- Bulgular üçüncü taraf paketlerdeyse `dependency-vulnerability-review` kullanılır.
- Doğrulanmış tek bir bulgu resmi olarak yazılacaksa `security-finding-report` kullanılır.

## Girdiler
Zorunlu:
- İncelenecek kod veya diff, dil ve framework bilgisiyle.

İsteğe bağlı, kaliteyi artırır:
- Koda nasıl erişildiği (açık endpoint, iç iş, yalnızca yönetici) ve çağıranların güven düzeyi.
- İlgili yapılandırma, middleware, ORM ve doğrulama katmanları.
- Güvenlik gereksinimleri veya ASVS seviyesi, SAST çıktısı.

Kod yoksa iste. Giriş noktası belirsizse maruziyet hakkındaki varsayımını yaz.

## Süreç
1. Giriş noktalarını (kaynak) belirle: HTTP parametreleri, header'lar, cookie'ler, mesaj içerikleri, dosyalar, ortam değişkenleri, kullanıcıların yazdığı veritabanı değerleri.
2. Hedefleri (sink) belirle: SQL/NoSQL sorguları, işletim sistemi komutları, dosya yolları, şablon/HTML çıktısı, deserializer'lar, yönlendirmeler, dış URL'ler (SSRF), LDAP/XPath, loglama.
3. Her kaynağı her hedefe kadar izle; yol üzerindeki doğrulama, kodlama veya parametrelemeyi not et. Kesintisiz kirli (tainted) yollar aday bulgudur.
4. Her işlemde erişim kontrolünü kontrol et: kimlik doğrulama zorunlu mu, rol veya scope kontrol ediliyor mu, nesne sahipliği doğrulanıyor mu (IDOR), kiracı filtresi uygulanıyor mu.
5. Kriptografi ve gizli bilgileri kontrol et: koda gömülü secret'lar, zayıf algoritma veya modlar, tahmin edilebilir rastgelelik, eksik TLS doğrulaması, parola hash'leme (yeterli maliyetle Argon2id, bcrypt, PBKDF2).
6. Hata yönetimi ve loglamayı kontrol et: sızan stack trace veya iç detaylar, loglara yazılan hassas veya kişisel veriler, eksik denetim olayları.
7. Framework'e özgü tuzakları kontrol et: mass assignment/over-posting, CSRF koruması, CORS yapılandırması, güvensiz deserialization ayarları, devre dışı güvenlik header'ları.
8. Her bulgu için kaydet: konum, OWASP Top 10 kategorisi, CWE numarası, istismar senaryosu, önem derecesi (gerekçesiyle veya ekip kullanıyorsa CVSS), güven düzeyi ve kod düzeyinde düzeltme.
9. Doğrulanmış bulguları, çalışma zamanında doğrulanması gereken şüpheli kalıplardan ayır.
10. Özetle: önem derecesine göre sayılar, merge'i engelleyen konular ve gözlemlenen olumlu kontroller.
11. Devret: her Kritik veya Yüksek bulguyu `security-finding-report` ile yaz, önem derecesi tartışmalı olanları `vulnerability-triage`'a yönlendir, tekrar eden eksikleri `security-requirements`'a aktar.

## Çıktı formatı
```markdown
# Güvenli Kod İncelemesi: <bileşen / PR>
Kapsam: <dosyalar> · Maruziyet: <açık/iç/yönetici> [çıkarımsa VARSAYIM]
## Özet
- Engelleyici: <n> · Yüksek: <n> · Orta: <n> · Düşük/Bilgi: <n>
## Bulgular
### SCR-01 <başlık>
- Konum: <dosya:satır>
- Kategori: OWASP A0x:<yıl> <ad> · CWE-<id>
- Önem / güven: <Yüksek/Orta/Düşük> / <Doğrulandı/Muhtemel/Doğrulama gerekli>
- Senaryo: <saldırgan nasıl istismar eder>
- Düzeltme: <somut değişiklik, kısa kod parçasıyla>
## Çalışma Zamanında Doğrulanacaklar
- ...
## Gözlemlenen İyi Uygulamalar
- ...
```

## Kalite kontrol listesi
- [ ] Her bulgunun konumu, CWE'si, istismar senaryosu ve somut düzeltmesi var.
- [ ] Önem derecesi yalnızca kalıbı değil, gerçek erişilebilirliği ve maruziyeti yansıtıyor.
- [ ] Her veri erişimi için nesne ve kiracı düzeyi yetkilendirme kontrol edildi.
- [ ] Kodda bulunan secret, token veya kişisel veriler maskelenerek raporlandı, asla tam haliyle tekrarlanmadı.
- [ ] Spekülatif konular doğrulama gerekli olarak etiketlendi.
- [ ] Merge'i engelleyen maddeler açıkça ayrıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her string birleştirmeyi injection olarak raporlamak. Değerin saldırgan kontrolünde olduğunu ve bir hedefe ulaştığını doğrula.
- Kod "temiz göründüğü" için yetkilendirme açıklarını kaçırmak. Bozuk erişim kontrolü nadiren tehlikeli bir fonksiyon çağrısı olarak görünür.
- Genel "girdiyi temizle" önerisi vermek. Kesin kontrolü adlandır: parametreli sorgu, izin listesi, bağlama duyarlı kodlama.

## Örnek
Girdi: yalnızca `[Authorize]` ile korunan ve `repo.Get(id)` çağıran `GET /orders/{id}` controller aksiyonu.

Çıktıdan bir bölüm:
### SCR-01 Sipariş sorgulamada sahiplik kontrolü eksik
- Kategori: OWASP A01:2021 Broken Access Control · CWE-639
- Senaryo: Kimliği doğrulanmış herhangi bir kullanıcı `id` değerini deneyerek adresler dahil diğer müşterilerin siparişlerini okur.
- Düzeltme: Doğrulanmış token'daki müşteri kimliğiyle filtrele: `repo.Get(id, User.GetCustomerId())`; eşleşmezse 404 dön.
