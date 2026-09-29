---
description: "Bir Bitti Tanımı (DoD) oluşturur veya revize eder: her artımın veya iş maddesinin tamamlanmış sayılması için geçmesi gereken ortak kalite kontrol listesini madde, sürüm ve kurum seviyelerine ayırır; her kriter için doğrulama yöntemini ve eksikleri kapatma planını verir. 'Bitti' herkes için farklı anlama geldiğinde, kalite sorunları canlıya sızdığında ya da DoD veya tamamlanma kriterleri istendiğinde kullanılır."
related: "definition-of-ready, release-quality-gate, acceptance-criteria, coding-standards, working-agreement"
prompt: "Mobil bankacılık ekibimiz için bir Bitti Tanımı taslağı hazırla; kod incelemesi ve birim testlerimiz var ama sürümler hâlâ erişilebilirlik ve güvenlik kontrollerinde sorun çıkarıyor."
---

# Bitti Tanımı (DoD) Oluşturma

## Amaç
"Bitti" kavramını tek ve şeffaf bir kalite taahhüdüne dönüştürmek; böylece tamamlanan iş gerçekten yayınlanabilir olur, gizli işler ertelenmez ve ilerleme rakamları gerçeği yansıtır.

## Ne zaman kullanılır
- Maddeler bitti olarak işaretleniyor ama hâlâ test, dokümantasyon veya dağıtım işi gerektiriyorsa.
- Hatalar, erişilebilirlik veya güvenlik sorunları sürekli canlıya sızıyorsa.
- Birden fazla ekip tek bir ürüne katkı veriyor ve ortak bir kalite çıtasına ihtiyaç duyuyorsa.
- Denetime tabi bir ortam kalite faaliyetlerinin kanıtını gerektiriyorsa.

## Ne zaman kullanılmaz
- İş başlamadan önceki giriş kriterleri için `definition-of-ready` kullanılır.
- Tek bir hikayenin çalıştığını kanıtlayan maddeye özel davranış için `acceptance-criteria` kullanılır.
- Belirli bir sürüm için yayın/yayınlamama kararı için `release-quality-gate` veya `go-no-go` kullanılır.

## Girdiler
Zorunlu:
- Ekibin ne teslim ettiği (ürün türü, platformlar) ve mevcut pratikleri veya sorunları. Yoksa sor; DoD ekibin gerçekten doğrulayabileceği şeyleri yansıtmalı.

İsteğe bağlı, kaliteyi artırır:
- Mevcut DoD, kurumsal veya yasal kalite gereksinimleri.
- Araç gerçekleri: otomatik testler, pipeline aşamaları, ortamlar.
- Bilinen canlıya sızan hatalar veya denetim bulguları.

## Süreç
1. Üç seviyeyi ayır: madde seviyesi (her hikaye/hata), artım/sürüm seviyesi (yayın öncesi sağlanması gerekenler) ve kurumsal temel (tüm ekiplere uygulanır).
2. Şu kalite boyutlarını ele al ve yalnızca geçerli olanları dahil et: kod kalitesi ve inceleme; otomatik testlerin (birim, entegrasyon) geçmesi; kabul kriterlerinin doğrulanması; fonksiyonel olmayan kontroller (performans, OWASP ASVS seviyesine göre güvenlik, WCAG 2.2 AA'ya göre erişilebilirlik); dokümantasyon (kullanıcı, API, operasyon); entegre bir ortama dağıtım; izleme/loglama; veri gizliliği (KVKK/GDPR) kontrolleri.
3. Her kriteri doğrulanabilir biçimde yaz ve kanıtını belirt (pipeline aşaması, kontrol listesi, gözden geçiren onayı).
4. Mevcut durumla karşılaştır. Ekibin henüz karşılayamadığı kriterleri karşılanıyormuş gibi göstermek yerine, eksik kapatma aksiyonuyla birlikte "hedef" olarak işaretle.
5. DoD'nin kabul kriterleriyle çelişmediğinden emin ol: DoD geneldir ve tüm maddelere uygulanır; kabul kriterleri maddeye özeldir.
6. Bir madde iterasyon/sprint sonunda veya sürümde DoD'yi geçemezse ne olacağını tanımla: bitmemiştir, backlog'a döner ve ilerlemeye sayılmaz.
7. Gözden geçirme sıklığını ve DoD'yi zamanla güçlendirme kuralını belirle (kapasite elverdiğinde bir hedef kriter ekle).
8. Ekip panosuna uygun tek sayfalık bir DoD üret.
9. Kullanıcının hedefi devam ediyorsa eşleşen giriş kriterleri için `definition-of-ready`, madde DoD'sinin ötesindeki sürüm seviyesi kontroller için `release-quality-gate` öner.

## Çıktı formatı
```markdown
# Bitti Tanımı – <ekip/ürün>
Sürüm: <n> · Anlaşma: <tarih veya [TBD]> · Kurumsal temelle birlikte uygulanır: <evet/hayır>

## Madde Seviyesi
| # | Kriter | Kanıt | Durum |
|---|---|---|---|
| 1 | Kod en az bir başka geliştirici tarafından incelendi | Pull request onayı | Karşılanıyor |

## Artım / Sürüm Seviyesi
| # | Kriter | Kanıt | Durum |
|---|---|---|---|

## Hedef Kriterler (henüz karşılanmıyor)
- <kriter> – eksik – aksiyon – sahip – tarih [TBD]

## Bitmemiş İşin Ele Alınması
<madde DoD'yi geçemezse ne olur>

## Gözden Geçirme
<sıklık ve DoD'nin nasıl güçlendirileceği>
```

## Kalite kontrol listesi
- [ ] Her kriter doğrulanabilir ve kanıtını belirtiyor.
- [ ] Madde seviyesi ile sürüm seviyesi ayrılmış.
- [ ] Fonksiyonel olmayan boyutlar (güvenlik, erişilebilirlik, performans, işletilebilirlik) açıkça ele alınmış.
- [ ] Karşılanmayan kriterler karşılanıyor gibi değil, aksiyonlu hedef olarak gösterilmiş.
- [ ] DoD'ye maddeye özel kabul kriterleri karışmamış.
- [ ] Standartlar tam adıyla verilmiş (ör. WCAG 2.2 AA, OWASP ASVS seviyesi).
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ekibin pratikte karşılayamayacağı bir DoD. Göz ardı edilir; ulaşılabilir olanla başla, hedefleri sonra ekle.
- "Bitti"nin "geliştirmede bitti" anlamına gelmesi. Entegrasyon ve dağıtılabilirliği dahil et, yoksa ilerleme rakamları kurgu olur.
- Sonuç yerine faaliyet listelemek ("test yapıldı" yerine "tüm otomatik testler pipeline'da geçiyor").

## Örnek
Girdi: "Mobil bankacılık ekibi, kod incelemesi ve birim testleri var, erişilebilirlik ve güvenlik kontrolleri sürekli bozuluyor."

Çıktıdan bir bölüm:
| 5 | Yeni veya değişen ekranlar kontrast, etiket ve odak sırası için WCAG 2.2 AA kontrollerini geçiyor | Maddeye eklenmiş erişilebilirlik kontrol listesi | Hedef |
| 6 | Bağımlılık ve statik güvenlik taramalarında yeni yüksek/kritik bulgu yok | Pipeline tarama aşaması | Karşılanıyor |
- Hedef: İki platformda ekran okuyucu duman testi – eksik: cihaz laboratuvarı yok – aksiyon: minimal manuel senaryo tanımla – sahip [TBD].
