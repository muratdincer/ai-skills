---
description: "Bir gizli bilgi yönetimi planı üretir: secret envanteri ve sınıflandırması, merkezi kasa seçim kriterleri, en az yetkiyle kimlik tabanlı erişim, iş yüklerine ve hatlara enjeksiyon, rotasyon ve iptal, denetim ve acil erişim (break-glass). Bir ekip secret'ları kodda, yapılandırma dosyalarında veya hat değişkenlerinde tutuyorsa, bir sızıntıdan sonra ya da yeni bir platform için secret yönetimi tasarlanırken kullanılır."
related: "iac-review, pipeline-design, authn-authz-design, security-requirements, kubernetes-manifest-review"
prompt: "Veritabanı şifrelerimiz ve API anahtarlarımız appsettings dosyalarında ve hat değişkenlerinde duruyor. Düzgün bir secret yönetimine geçiş planı yaz."
---

# Gizli Bilgi Yönetimi Planı

## Amaç
Her kimlik bilgisinin, anahtarın ve sertifikanın bir sahibi olmasını, kontrollü bir kasada durmasını, açığa çıkmadan iş yüklerine ulaşmasını, takvime göre döndürülmesini ve bir sızıntıdan sonra hızla iptal edilebilmesini sağlamak.

## Ne zaman kullanılır
- Repository'lerde, imajlarda, yapılandırma dosyalarında veya düz metin hat değişkenlerinde secret bulunduğunda.
- Bir sızıntı veya şüpheli açığa çıkma yapılandırılmış bir iyileştirme gerektirdiğinde.
- Yeni bir platform veya cluster için secret yönetimi tasarımı gerektiğinde.
- Bir denetim rotasyon ve erişim kanıtı istediğinde.

## Ne zaman kullanılmaz
- Son kullanıcı kimlik doğrulama veya yetkilendirmesi tasarlanıyorsa `authn-authz-design` kullanılır.
- Belirli bir IaC değişikliği secret sızıntısı açısından inceleniyorsa `iac-review` kullanılır.
- Aktif bir ihlal yönetiliyorsa önce `security-incident-response` kullanılır.

## Girdiler
Zorunlu:
- Kullanılan secret türleri ve şu an nerede durdukları (en azından kaba bir liste).
- Çalışma ve teslim platformları (VM, konteyner, serverless, CI sistemi türü).

İsteğe bağlı, kaliteyi artırır:
- Mevcut secret kasası veya anahtar yönetim servisi, kimlik sağlayıcı, uyum gereksinimleri (PCI DSS, ISO/IEC 27001 kontrolleri, KVKK/GDPR).
- Ekip yapısı ve nöbet modeli.

Gerçek secret değerlerini asla isteme veya tekrar etme. Kullanıcı bir değer yapıştırırsa, onu ele geçirilmiş kabul edip döndürmesini söyle.

## Süreç
1. Secret envanteri çıkar: tür (veritabanı kimlik bilgisi, API anahtarı, imzalama anahtarı, TLS sertifikası, token), tüketici, sahip, mevcut konum, son rotasyon, sızarsa etki alanı.
2. Kritikliği (Kritik/Yüksek/Orta) etki alanına ve açıklığa göre sınıflandır.
3. Secret'ı ortadan kaldırmayı tercih et: workload/managed identity, hatlar için federasyonlu kısa ömürlü token'lar, destekleniyorsa IAM tabanlı veritabanı kimlik doğrulaması.
4. Merkezi kasa gereksinimlerini tanımla: KMS/HSM'deki anahtarlarla şifreleme, ince taneli erişim politikaları, denetim logu, sürümleme, dinamik secret desteği, yüksek erişilebilirlik. Kullanıcının mevcut ürünü yoksa ürün bağımsız kal.
5. Erişim modelini tanımla: uygulama başına kimlik, ortam bazında ayrım, en az yetki, varsayılan olarak insanların üretim secret'larını okuyamaması, anlık (just-in-time) yetki yükseltme.
6. Enjeksiyonu tanımla: çalışma anında çekme veya mount edilen volume/CSI tarzı sürücü; asla imaja gömülmez veya commit edilmez; yerel geliştirmenin üretim dışı secret'ları nasıl alacağı.
7. Rotasyonu tanımla: sınıf başına sıklık, mümkün olduğunca otomatik, kesintiyi önlemek için çift secret örtüşmesi, sertifika süre dolumu izleme.
8. Sızıntı müdahalesini tanımla: tespit (repository ve hatlarda secret taraması, pre-commit hook'ları), iptal-döndür-doğrula runbook'u; geçmiş temizliği rotasyondan sonra gelir.
9. Denetim ve alarmları tanımla: saklanan erişim logları, olağandışı erişim alarmları, periyodik erişim gözden geçirmesi.
10. Acil erişimi (break-glass) tanımla: mühürlü acil erişim, kim, nasıl loglanır, kullanım sonrası rotasyon.
11. Mevcut durumdan aşamalı bir geçiş planı üret.
12. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa uygulamayı kodda doğrulamak için `iac-review`, iş yükü kimliği için `authn-authz-design` veya CI/CD kimlik bilgisi akışı için `pipeline-design` öner.

## Çıktı formatı
```markdown
# Gizli Bilgi Yönetimi Planı: <sistem/birim>
## Secret Envanteri
| Secret | Tür | Tüketici | Sahip | Mevcut konum | Kritiklik | Hedef mekanizma | Rotasyon |
## Hedef Mimari (kasa, kimlik, enjeksiyon)
## Erişim Modeli
## Rotasyon Politikası
| Sınıf | Sıklık | Otomatik mi? | Örtüşme stratejisi |
## Tespit ve Sızıntı Müdahalesi
## Denetim ve Acil Erişim
## Geçiş Aşamaları
| Aşama | Kapsam | Çıkış kriteri |
## Açık Sorular / Varsayımlar
```

## Kalite kontrol listesi
- [ ] Çıktının hiçbir yerinde secret değeri yok.
- [ ] Her secret'ın bir sahibi ve rotasyon kuralı var.
- [ ] Saklamadan önce workload identity ile secret'ı ortadan kaldırma değerlendirildi.
- [ ] Rotasyon stratejisi kesintiye yol açmıyor (örtüşme veya sürümleme).
- [ ] Sızıntı müdahalesi yalnızca geçmişten silmeyi değil, önce rotasyonu söylüyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Secret'ları kasaya taşıyıp her servise her şeyi okuma yetkisi vermek. Kimlik ve ortam bazında kapsamla.
- Git geçmişini temizleyip sızıntıyı çözülmüş saymak. Secret iptal edilmeli ve döndürülmeli.
- Tüketiciler hazır olmadan rotasyon yapıp kesintiye yol açmak. Geçiş sırasında iki geçerli sürümü destekle.

## Örnek
Girdi: "SQL şifreleri ve bir ödeme API anahtarı appsettings.json'da, hatta değişken olarak bir bulut yönetici anahtarı var."

Çıktıdan bir bölüm:
| Secret | Kritiklik | Hedef mekanizma | Rotasyon |
|---|---|---|---|
| Hat bulut yönetici anahtarı | Kritik | Ortam bazında kapsamlı, federasyonlu kısa ömürlü kimlikle değiştir | Ortadan kalktı |
| Ödeme API anahtarı | Kritik | Merkezi kasa, çalışma anında uygulama kimliğiyle çekilir | 90 gün `[sağlayıcıyla teyit et]` |
| SQL şifresi | Yüksek | Destekleniyorsa managed identity, değilse dinamik kimlik bilgisi | Kiralama süresi başına |
