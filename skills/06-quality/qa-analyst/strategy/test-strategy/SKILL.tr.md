---
description: "Bir ürün, program veya kurum için test seviyelerini, test türlerini, ortamları, araç kategorilerini, veri yaklaşımını ve risk bazlı odağı tanımlayan bir test stratejisi yazar. Yeni bir ürün veya büyük bir girişim başladığında, ekipler arasında test yaklaşımı tutarsız olduğunda ya da bir sistemin genel olarak nasıl test edileceği sorulduğunda kullanılır."
related: test-plan, risk-based-testing, environment-strategy, automation-framework-design, nfr-specification
prompt: "Yeni müşteri kazanım platformumuz için test stratejisi yaz: web + mobil ön yüz, 12 mikroservis, core banking ve KYC sağlayıcısı entegrasyonları var."
---

# Test Stratejisi Yazma

## Amaç
Bir ürün veya program için uzun ömürlü test yaklaşımını tanımlamak. Böylece her ekip doğru seviyede, doğru risklere karşı, ortak ortam, veri ve kalite kriterleriyle test eder. Strateji "burada nasıl test ederiz" sorusunun cevabıdır; tekil test planları ondan türetilir.

## Ne zaman kullanılır
- Yeni bir ürün, platform veya büyük program başlıyor ve ortak bir test yaklaşımı yok.
- Ekipler tutarsız test ediyor (tekrarlanan uçtan uca setler, sözleşme testi yok, manuel regresyon darboğazı).
- Mimari ciddi biçimde değişiyor (monolitten servislere geçiş, yeni bulut platformu, yeni entegrasyon yapısı).
- Bir denetim veya müşteri, dokümante edilmiş test yaklaşımı istiyor.

## Ne zaman kullanılmaz
- Tek bir sürüm veya proje için kapsam, takvim ve giriş/çıkış kriterleri gerekiyorsa `test-plan` kullanılır.
- Yalnızca özellikleri veya modülleri riske göre sıralamak gerekiyorsa `risk-based-testing` kullanılır.
- Otomasyon kodunun mimarisi tasarlanıyorsa `automation-framework-design` kullanılır.

## Girdiler
Zorunlu:
- Sistemin tanımı: ana bileşenler, kullanıcılar, entegrasyonlar, dağıtım modeli.
- İş bağlamı: bir hatanın maliyeti (para, mevzuat, itibar, güvenlik).

İsteğe bağlı, kaliteyi artırır:
- Mimari diyagramlar, fonksiyonel olmayan gereksinimler, yasal yükümlülükler, geçmiş hata verisi.
- Ekip yapısı, sürüm sıklığı, mevcut araçlar ve ortamlar.
- Kurumsal kalite politikası veya zorunlu standartlar.

Sistem tanımı veya iş bağlamı yoksa iste. Diğer her şey açık soru olarak kalır.

## Süreç
1. Test edilen sistemi ve kalite sürücülerini özetle (ör. para hareketinin doğruluğu, erişilebilirlik süresi, veri gizliliği, kullanılabilirlik).
2. Ürün risk alanlarını kaba düzeyde belirle (bileşen, entegrasyon ve kalite özelliği bazında; kontrol listesi olarak ISO/IEC 25010) ve Y/O/D olarak derecelendir.
3. Test seviyelerini (birim, bileşen, sözleşme, entegrasyon, sistem, uçtan uca, kabul) sorumlu, hedef ve o seviyede özellikle test edilmeyenlerle birlikte tanımla. Sabit bir piramit değil, riske göre şekillenen bir test portföyü hedefle.
4. Risklere göre test türlerini tanımla: fonksiyonel, regresyon, API/sözleşme, performans, güvenlik, erişilebilirlik (WCAG 2.2), kullanılabilirlik, uyumluluk, dayanıklılık, veri göçü.
5. Ortamları belirt: amaç, veri, entegrasyonlar (gerçek, stub, sanallaştırılmış) ve her ortama dağıtımı kimin yönettiği.
6. Test verisi yaklaşımını tanımla: sentetik veya maskelenmiş üretim verisi, yenileme, gizlilik kısıtları (KVKK/GDPR), sahiplik.
7. Seviye bazında otomasyon yaklaşımını tanımla: neyin mutlaka otomatik olacağı, pipeline'ın neresinde koşacağı, hedef geri bildirim süresi. Kullanıcı belirtmediyse ürün değil araç kategorisi adı ver.
8. Hata yönetimini tanımla: önem skalası, triage sıklığı, zorunlu alanlar, önem derecesine göre düzeltme SLA'ları.
9. Kalite kapılarını ve metrikleri tanımla: seviye bazında giriş/çıkış kriterleri, kapsam beklentileri, kaçak hatalar, kararsız test oranı.
10. Rolleri ve sorumlulukları (geliştirici, QA, ürün, operasyon) ve testin, metodolojiden bağımsız olarak teslimat ritmine nasıl oturduğunu listele.
11. Varsayımları, kısıtları ve açık soruları kaydet. Desteklenmeyen içeriği `[VARSAYIM]` veya `[BİLİNMİYOR]` ile işaretle.

## Çıktı formatı
```markdown
# Test Stratejisi: <ürün / program>
Sürüm: <x.y> | Sahip: <ad veya [BİLİNMİYOR]> | Durum: Taslak

## 1. Bağlam ve Kalite Sürücüleri
## 2. Risk Özeti
| Alan | Risk | Olasılık | Etki | Test ağırlığı |
## 3. Test Seviyeleri
| Seviye | Hedef | Sorumlu | Kapsam içi | Kapsam dışı | Otomatik mi? |
## 4. Test Türleri
| Tür | Uygulandığı yer | Yaklaşım | Tetikleyici (her commit / gece / sürüm öncesi) |
## 5. Ortamlar
| Ortam | Amaç | Veri | Entegrasyonlar | Dağıtım kontrolü |
## 6. Test Verisi
## 7. Otomasyon ve Pipeline Entegrasyonu
## 8. Hata Yönetimi
## 9. Kalite Kapıları ve Metrikler
## 10. Roller ve Sorumluluklar
## 11. Varsayımlar, Kısıtlar, Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her yüksek risk alanı en az bir test seviyesi ve test türüyle eşleşiyor.
- [ ] Her seviye neyi kapsamadığını belirtiyor; tekrar önleniyor.
- [ ] Fonksiyonel olmayan testler (performans, güvenlik, erişilebilirlik) ele alınmış veya gerekçesiyle kapsam dışı bırakılmış.
- [ ] Test verisi yaklaşımı mevzuata uygun; üretim verisi maskelenmeden kullanılmıyor.
- [ ] Hiçbir araç, sayı veya sorumlu uydurulmadı; boşluklar işaretli.
- [ ] Strateji metodolojiden bağımsız ve birden fazla ekip tarafından kullanılabilir.

## Sık yapılan hatalar
- Tarih ve isim içeren bir test planı yazmak. Strateji kalıcı kalmalı; takvimler `test-plan` içine gider.
- Genel bir test piramidini kopyalamak. Portföyü mimariden ve risklerden türet (ör. çok sayıda servis entegrasyonu varsa sözleşme testleri).
- Üçüncü taraf entegrasyonlarını yok saymak. Stub/sanallaştırma yaklaşımını ve gerçek bağlantıyı kimin test edeceğini tanımla.

## Örnek
Girdi: "Müşteri kazanım platformu: web + mobil, 12 mikroservis, core banking ve KYC sağlayıcısı entegrasyonları."

Çıktıdan bir bölüm:
- Risk: KYC sağlayıcısının yanıt varyasyonları (olasılık Y, etki Y) → servis başına tüketici odaklı sözleşme testleri + sağlayıcı sandbox'ına karşı az sayıda uçtan uca test.
- "Uçtan uca" seviyesi: yalnızca 10-15 kritik yolculuk; iş kuralı kombinasyonları bileşen seviyesinde test edilir.
- "SIT" ortamı: KYC sağlayıcısı sanallaştırılmış `[VARSAYIM: sandbox'ta istek sınırı var]`.
