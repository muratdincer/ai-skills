---
description: "Bir sistem veya özellik için tehdit modeli oluşturur: sistemi veri akış diyagramına ayırır, her eleman ve güven sınırı için STRIDE uygular, tehditleri derecelendirir ve sorumlusuyla birlikte önlemler önerir. Yeni bir sistem tasarlanırken, entegrasyon eklenirken, güven sınırları veya veri akışları değişirken ya da güvenlik açısından neyin ters gidebileceği sorulduğunda kullanılır."
related: "security-requirements, authn-authz-design, solution-architecture-document, pentest-scope, it-risk-assessment"
prompt: "Yeni mobil bankacılık API'miz için tehdit modeli çıkar: mobil uygulama, API gateway, .NET backend, PostgreSQL ve üçüncü taraf bir KYC sağlayıcısı var."
---

# Tehdit Modeli Oluşturma

## Amaç
Bir sisteme yönelik gerçekçi tehditleri zafiyete dönüşmeden erken aşamada belirlemek ve her birini somut bir önleme, teste ya da açık bir risk kararına dönüştürmek.

## Ne zaman kullanılır
- Yeni bir sistem, servis veya büyük bir özellik tasarlanırken.
- Bir güven sınırı değiştiğinde: yeni dış entegrasyon, yeni kullanıcı tipi, buluta geçiş, yeni yönetim arayüzü.
- Hassas veya kişisel veri bir bileşenden ilk kez geçmeye başladığında.
- Mevcut tehdit modeli, anlattığı mimariden daha eski kaldığında.

## Ne zaman kullanılmaz
- Backlog için test edilebilir güvenlik kontrolleri listesi gerekiyorsa `security-requirements` kullanılır.
- Tek bir sistem değil, kurum genelinde varlık bazlı risk değerlendiriliyorsa `it-risk-assessment` kullanılır.
- Devam eden bir saldırı varsa `security-incident-response` kullanılır.

## Girdiler
Zorunlu:
- Sistemin tanımı: bileşenler, veri depoları, dış aktörler ve veri akışları (metin, diyagram veya mimari doküman).

İsteğe bağlı, kaliteyi artırır:
- Veri sınıflandırması (kişisel, özel nitelikli, ödeme, gizli anahtarlar).
- Dağıtım topolojisi, ağ bölgeleri, kimlik sağlayıcı.
- Mevcut güvenlik kontrolleri ve bilinen geçmiş olaylar.
- Uyum kapsamı (KVKK/GDPR, PCI DSS, BDDK, ISO 27001).

Sistem tanımı yoksa iste. Diğer her şey varsayım veya açık soru olarak kaydedilir.

## Süreç
1. Kapsamı yeniden yaz: modele neyin dahil olduğu, neyin açıkça hariç tutulduğu (ör. kurumsal ağ, CI/CD) ve kullanılan mimari sürümü.
2. Metin olarak veri akış diyagramı (DFD) çıkar: dış varlıklar, süreçler, veri depoları, veri akışları. Her elemanı numarala (E1, P1, D1, F1).
3. Güven sınırlarını belirle: internet/DMZ, service mesh, tenant sınırı, üçüncü taraf sınırı, yönetim düzlemi. Sınırı geçen akışlar en çok dikkati hak eder.
4. Varlıkları ve güvenlik hedeflerini (gizlilik, bütünlük, erişilebilirlik, mahremiyet) veri sınıflandırmasıyla birlikte listele.
5. Her eleman için STRIDE uygula: süreçlere altısı da; veri depolarına T, R, I, D; veri akışlarına T, I, D; dış varlıklara S, R.
6. Her tehdit için kategori adı değil somut bir saldırı senaryosu yaz (aktör, giriş noktası, teknik). Yararlıysa CWE veya MITRE ATT&CK referansı ver.
7. Mevcut kontrolleri kaydet, ardından kalan riski olasılık x etki (Yüksek/Orta/Düşük) ve tek satırlık gerekçeyle derecelendir. Ekibin kendi ölçeği varsa onu kullan.
8. Her tehdit için önleyici, tespit edici ve müdahale edici önlemler öner. Telafi edici kontroller yerine tasarım değişikliklerini tercih et.
9. Her önlemi izlenebilir bir kalemle eşle: güvenlik gereksinimi, backlog kalemi, test senaryosu veya sorumlusu belli kabul edilmiş risk.
10. Varsayımları, kapsam dışı alanları ve açık soruları listele; modelin ne zaman yeniden ele alınacağını yaz.
11. Sonraki beceriyi öner: önlemleri kontrollere dönüştürmek için `security-requirements`, en yüksek riskleri doğrulamak için `pentest-scope`, kurum düzeyinde kabul edilen riskler için `it-risk-assessment`.

## Çıktı formatı
```markdown
# Tehdit Modeli: <sistem> (v<mimari sürümü>, <tarih>)
## Kapsam ve Varsayımlar
- Kapsam içi: ... / Kapsam dışı: ...
- [VARSAYIM] ...
## Veri Akış Diyagramı (metin)
| ID | Eleman | Tür | Güven bölgesi | Veri (sınıf) |
## Güven Sınırları
- TB1: <kaynak> -> <hedef>: F1, F3 akışları
## Tehditler
| ID | Eleman | STRIDE | Senaryo | Mevcut kontroller | Olasılık | Etki | Risk | Önlem | Sorumlu | Takip |
## Kabul Edilen Riskler
- <tehdit ID> – gerekçe – onaylayan – gözden geçirme tarihi
## Açık Sorular
1. ...
## Yeniden Ele Alma Tetikleyicileri
- Yeni dış entegrasyon, kimlik doğrulama değişikliği, yeni veri kategorisi
```

## Kalite kontrol listesi
- [ ] Güven sınırını geçen her akış için en az bir tehdit analiz edildi.
- [ ] Senaryolar, test yazılabilecek kadar somut.
- [ ] Her Yüksek riskin bir önlemi veya onaylayanı belli kabul edilmiş risk kaydı var.
- [ ] Kişisel veri akışları işaretlendi, mahremiyet tehditleri (ilişkilendirilebilirlik, fazla veri toplama) değerlendirildi.
- [ ] Girdide olmayan hiçbir kontrol var sayılmadı; bilinmeyenler `[BİLİNMİYOR]` ile işaretli.
- [ ] Önlemler gereksinim, backlog kalemi veya testlerle izlenebilir.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Genel tehditleri ("SQL injection") bir elemana ve giriş noktasına bağlamadan listelemek. Her tehdidi bir DFD elemanına bağla.
- Yönetim, destek ve CI/CD yollarını atlamak. Yetkili düzlemler çoğu zaman en zayıf sınırdır.
- Modeli tek seferlik doküman saymak. Yeniden ele alma tetikleyicilerini tanımla ve mimari sürümüne bağla.
- Her şeyi Yüksek olarak derecelendirmek. Olasılığı maruziyet ve saldırgan eforuyla gerekçelendir.

## Örnek
Girdi: "Mobil uygulama API gateway'i çağırıyor, o da bir .NET servisini çağırıyor; servis müşterileri PostgreSQL'de tutuyor ve dış bir KYC sağlayıcısını çağırıyor."

Çıktıdan bir bölüm:
| T4 | F3 servis -> KYC | Bilgi ifşası | Yanlış yapılandırılmış çıkış proxy'sindeki saldırgan KYC'ye giden T.C. kimlik numaralarını okur | TLS 1.2 [VARSAYIM] | O | Y | Yüksek | Sağlayıcıya TLS 1.3 ve sertifika sabitleme, yalnızca gerekli alanları gönderme, kimlik numarası içermeyen loglama | Backend lideri | SEC-REQ-07 |
