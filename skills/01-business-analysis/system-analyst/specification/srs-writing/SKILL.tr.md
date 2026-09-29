---
description: "ISO/IEC/IEEE 29148 ile uyumlu bir Yazılım Gereksinim Şartnamesi (SRS) yazar: amaç ve kapsam, sistem bağlamı ve arayüzler, fonksiyonel gereksinimler, kalite nitelikleri, veri, kısıtlar ve her gereksinim için doğrulama yöntemi; her gereksinim tekil ID'li ve izlenebilirdir. Bir sistem veya alt sistemin tasarım, geliştirme, tedarikçi ya da denetim için tanımlanması gerektiğinde veya iş gereksinimlerinin doğrulanabilir bir sistem şartnamesine dönüştürülmesi gerektiğinde kullanılır."
related: "frd-writing, nfr-specification, use-case-spec, integration-requirements, traceability-matrix"
prompt: "Bu FRD ve arayüz listesine göre ödeme mutabakat servisi için bir SRS yaz."
---

# Yazılım Gereksinim Şartnamesi (SRS) Yazma

## Amaç
Tasarımcıların, geliştiricilerin, test uzmanlarının ve tedarikçilerin iş dokümanlarını yeniden yorumlamadan üzerine inşa edip doğrulayabileceği sistem düzeyinde bir şartname üretmek. Her gereksinim tekil, doğrulanabilir, benzersiz ID'li ve kaynağına izlenebilir olur.

## Ne zaman kullanılır
- İş veya fonksiyonel gereksinimler var ve bir sistem ya da alt sistem için sistem gereksinimi olarak yeniden yazılması gerekiyorsa.
- İş dış kaynağa veriliyor, regülasyona tabi veya denetleniyor ve resmi, sürümlü bir şartname gerekiyorsa.
- Birden çok ekip veya tedarikçi tek bir sistemin parçalarını geliştiriyor ve ortak bir sözleşmeye ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- İhtiyaç hâlâ iş düzeyindeyse (işin neye ulaşması gerektiği) `brd-writing` veya `frd-writing` kullanılır.
- Yalnızca kalite nitelikleri eksikse `nfr-specification` kullanılır.
- Yalnızca tek bir arayüz veya API tanımlanacaksa `integration-requirements` veya `api-contract` kullanılır.

## Girdiler
Zorunlu:
- Kaynak gereksinimler (BRD, FRD, hikayeler, kullanım senaryoları) veya sistemin sorumluluklarının tarifi.
- Sistem sınırı: hangi sistemin tanımlandığı.

İsteğe bağlı, kaliteyi artırır:
- Bağlam diyagramı, arayüz listesi, veri modeli, mevcut mimari kararlar.
- Mevzuat ve kurum içi standartlar, kurumun SRS şablonu.
- Hedef kullanıcılar, ortamlar ve işletim kısıtları.

Kaynak materyal veya sistem sınırı yoksa iste. Geri kalan her şey dokümanda `[TBD]` ya da açık konu olur.

## Süreç
1. Sistem sınırını sabitle: sistemi adlandır, dış aktörleri ve komşu sistemleri listele, açıkça dışarıda kalanı yaz. Bağlamı liste veya kod olarak diyagram şeklinde tarif et.
2. Kuralları belirle: gereksinim ID şeması (örn. SRS-FR-###, SRS-NFR-###, SRS-IF-###), öncelik ölçeği ve "-meli/-malı" (bağlayıcı), "-mesi beklenir" (arzu edilen), "-ebilir" (isteğe bağlı) ifadeleri.
3. Her kaynak maddeden fonksiyonel gereksinim türet. Her gereksinimde tek bir davranış yaz: "Sistem ... -malıdır"; tetikleyici, girdi, işleme kuralı ve gözlemlenebilir çıktı olsun. "ve/veya" içeren ifadeleri böl.
4. Dış arayüzleri tanımla: kullanıcı arayüzleri (roller, ana ekranlar, kullanıcılar insansa WCAG 2.2 erişilebilirliği), sistem arayüzleri (karşı taraf, yön, protokol, mesaj, sıklık, hata yönetimi) ve donanım ya da iletişim kısıtları.
5. Veri gereksinimlerini tanımla: ana varlıklar, kural taşıyan öznitelikler, saklama, arşivleme ve KVKK/GDPR kapsamında maskeleme veya veri minimizasyonu ihtiyacıyla kişisel veri sınıflandırması.
6. Kalite niteliklerini ölçülebilir kabul ölçütleriyle tanımla: performans, erişilebilirlik (availability), kurtarılabilirlik, güvenlik, denetlenebilirlik, işletilebilirlik, ölçeklenebilirlik. Sayı veya koşul olmadan sıfat kullanma; eksik sayılar sorumlusuyla birlikte `[TBD]` olur.
7. Tasarım ve uygulama kısıtlarını (zorunlu platformlar, standartlar, mevzuat) gereksinimlerden ayrı listele; varsayımları ve bağımlılıkları kaydet, çıkarım olanları `[VARSAYIM]` olarak etiketle.
8. Her gereksinime bir doğrulama yöntemi ata: Test, Gösterim, İnceleme veya Analiz.
9. Her gereksinimi kaynak ID'sine izle; sistem gereksinimi olmayan kaynak maddeleri (kapsama boşluğu) ve kaynağı olmayan sistem gereksinimlerini (fazladan kapsam veya eksik kaynak) işaretle.
10. Her gereksinimi ISO/IEC/IEEE 29148 niteliklerine göre kontrol et: gerekli, açık, eksiksiz, tekil, yapılabilir, doğrulanabilir, doğru, uyumlu.
11. Kullanıcı devam etmek isterse bağlantıları sürdürmek için `traceability-matrix`, kalite niteliklerini derinleştirmek için `nfr-specification` veya onay öncesi için `requirements-review-checklist` öner.

## Çıktı formatı
```markdown
# Yazılım Gereksinim Şartnamesi: <sistem>
Sürüm: <x.y> · Durum: <Taslak / İnceleme / Temel sürüm> · Sahibi: <ad veya [TBD]>

## 1. Giriş
Amaç · Kapsam (içi / dışı) · Tanımlar (sözlük bağlantısı) · Referanslar · Kurallar (ID şeması, bağlayıcılık ifadeleri)

## 2. Genel Tanım
Sistem bağlamı (aktörler, komşu sistemler) · Kullanıcı sınıfları · İşletim ortamı · Kısıtlar · Varsayımlar ve bağımlılıklar

## 3. Fonksiyonel Gereksinimler
| ID | Gereksinim ("Sistem ... -malıdır") | Kaynak | Öncelik | Doğrulama |
|---|---|---|---|---|

## 4. Dış Arayüz Gereksinimleri
### 4.1 Kullanıcı arayüzleri  ### 4.2 Sistem arayüzleri  ### 4.3 İletişim arayüzleri
| ID | Arayüz | Yön | Protokol / format | Sıklık | Hata yönetimi |

## 5. Veri Gereksinimleri
| Varlık | Ana kurallar | Saklama | Kişisel veri (E/H, sınıf) |

## 6. Kalite Nitelikleri
| ID | Nitelik | Kabul ölçütü | Doğrulama |

## 7. İzlenebilirlik ve Kapsama
Eşlenmemiş kaynak maddeler · Kaynağı olmayan gereksinimler

## 8. Açık Konular
| # | Konu | Sorumlu | Gereken tarih |
```

## Kalite kontrol listesi
- [ ] Her gereksinimin benzersiz ID'si, kaynağı, önceliği ve doğrulama yöntemi var.
- [ ] Her gereksinim tek bir davranış tanımlıyor ve sistem sınırında gözlemlenebilir.
- [ ] Hiçbir kalite niteliği ölçülebilir kabul ölçütü veya `[TBD]` olmadan sıfat kullanmıyor.
- [ ] Kısıtlar ve varsayımlar gereksinimlerden ayrı, çıkarımlar etiketli.
- [ ] İki yöndeki kapsama boşlukları sessizce doldurulmadan listelendi.
- [ ] Kişisel veri sınıflandırıldı ve geçtiği yerde maskeleme veya minimizasyon belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İş gereksinimlerini aynen kopyalamak. "Kullanıcılar ödemeleri eşleştirebilir" bir sistem gereksinimi değildir; tetikleyiciyi, kuralı ve çıktıyı yaz.
- Tasarımı gereksinim olarak yazmak ("X tablosunda sakla"). Gerçek bir kısıt değilse çözüm tercihlerini tasarım dokümanlarında tut.
- Arayüzleri yalnızca adıyla bırakmak. Entegrasyon ekiplerinin ihtiyacı yön, format, sıklık ve hata davranışıdır.

## Örnek
Girdi: "FR-12: Finans, eşleşmeyen banka hareketlerini günlük olarak görmek istiyor."

Zayıf: "Sistem eşleşmeyen hareketleri hızlıca göstermelidir."

Güçlü:
| ID | Gereksinim | Kaynak | Öncelik | Doğrulama |
|---|---|---|---|---|
| SRS-FR-031 | Sistem, her banka ekstresi aktarımı tamamlandığında, eşleşen muhasebe kaydı olmayan her hareketi "Eşleşmedi" olarak işaretlemelidir. | FR-12 | Must | Test |
| SRS-FR-032 | Sistem, Eşleşmedi hareketlerini Mutabakat rolündeki kullanıcılara valör tarihi ve hesaba göre filtrelenebilir biçimde listelemelidir. | FR-12 | Must | Gösterim |
| SRS-NFR-007 | Eşleşmedi listesi `[TBD]` hareket için `[TBD]` saniye içinde yüklenmelidir. | FR-12 | Should | Test |
