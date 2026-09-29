---
description: "Veri gereksinimlerini iş bakış açısıyla tanımlar: varlıklar ve ilişkileri; anlamı, tipi, formatı, zorunluluk kuralı, doğrulamaları ve izin verilen değerleriyle nitelikler; tanımlayıcılar, veri sahipliği, kaynaklar ve tüketiciler, hassasiyet sınıfı, kalite beklentileri, saklama ve silme. Bir özellik veya sistem veri oluşturduğunda ya da değiştirdiğinde, geliştirme veya taşıma için veri sözlüğü gerektiğinde ya da 'veriyi tanımla', 'hangi alanlar lazım' dendiğinde kullanılır."
related: "conceptual-data-model, data-classification, data-quality-rules, retention-policy, frd-writing"
prompt: "Tedarikçi kayıt özelliği için veri gereksinimlerini tanımla: tedarikçi, iletişim kişileri, banka bilgileri ve dokümanlar."
---

# Veri Gereksinimlerini Tanımlama

## Amaç
İş biriminin hangi veriye ihtiyaç duyduğunu, bu verinin ne anlama geldiğini, sahibinin kim olduğunu, ne kalitede olması ve ne kadar saklanabileceğini tanımlamak; böylece tasarım, entegrasyon, taşıma ve mahremiyet kararları üzerinde uzlaşılmış bir veri tanımına dayanır.

## Ne zaman kullanılır
- Yeni bir özellik veya sistem iş verisi oluşturduğunda, değiştirdiğinde veya tükettiğinde.
- Geliştiriciler, entegrasyon ekibi veya taşıma ekibi iş seviyesinde bir veri sözlüğüne ihtiyaç duyduğunda.
- Kişisel veya hassas veri söz konusuysa ve işleme kurallarına erkenden karar verilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Tüm bir alan için kavramsal veya mantıksal model gerekiyorsa `conceptual-data-model` veya `logical-data-model` kullanılır.
- Mevcut bir veri seti için yalnızca ölçülebilir veri kalitesi kuralları gerekiyorsa `data-quality-rules` kullanılır.
- İki sistem arasında alan alan eşleme gerekiyorsa `field-mapping` veya `source-to-target-mapping` kullanılır.

## Girdiler
Zorunlu:
- Özellik, süreç veya sistem kapsamı ve işlediği bilgiler (her biçimde: formlar, raporlar, notlar).

İsteğe bağlı, kaliteyi artırır:
- Mevcut veri sözlüğü veya şema, sözlük, iş kuralları, mevzuat (KVKK/GDPR, sektörel saklama kuralları), veri sahipleri, örnek kayıtlar (maskelenmiş).

Kapsam yoksa iste. Asla gerçek kişisel veri isteme; alan adları ve maskelenmiş örneklerle çalış.

## Süreç
1. Girdiden iş varlıklarını (kimliği ve yaşam döngüsü olan isimler) ve kardinaliteli ilişkileri çıkar ("bir tedarikçinin 1..n iletişim kişisi vardır").
2. Her varlık için sözlük terimleriyle tek cümlelik iş anlamını, tanımlayıcısını (doğal ve/veya sistem) ve yaşam döngüsü durumlarını tanımla.
3. Her varlığın niteliklerini iş tanımı, veri tipi, format/uzunluk, zorunluluk (her zaman, koşullu ve koşuluyla, isteğe bağlı), varsayılan değer, izin verilen değerler veya referans listesi, birim veya para birimiyle listele.
4. Nitelik bazında ve nitelikler arası doğrulama kurallarını yaz (ör. bitiş tarihi ≥ başlangıç tarihi); varsa iş kuralı ID'lerine referans ver.
5. Her niteliğin kaynağını (kullanıcı girişi, sistem, dış arayüz, formülle türetilmiş) ve tüketicilerini (ekranlar, raporlar, arayüzler) belirle.
6. Veri sahipliğini ata: iş sahibi (anlamı ve kaliteyi tanımlar) ve veri sorumlusu (data steward); bilinmeyen sahipleri `[BİLİNMİYOR]` olarak işaretle.
7. Her niteliğin hassasiyetini sınıfla (açık, iç, gizli, kişisel, özel nitelikli kişisel) ve KVKK/GDPR kapsamında maskeleme, erişim ve minimizasyon ihtiyaçlarını not et.
8. Kalite beklentilerini yaz: bütünlük, teklik, doğruluk kaynağı, güncellik; ve hatalı veri geldiğindeki davranış.
9. Saklama, arşivleme ve silme ya da anonimleştirme kurallarını yasal veya iş dayanağıyla belirt; bilinmeyen süreler `[TBD]` olur, asla tahmin edilmez.
10. Taşıma veya geçmiş ihtiyaçlarını (yüklenecek mevcut veri, denetim izi, sürümleme) not et; varsayımları ve açık soruları muhataplarıyla listele.
11. Hedef devam ediyorsa ayrıntılı sınıflandırma için `data-classification`, ölçülebilir kontroller için `data-quality-rules`, saklama kararları için `retention-policy` öner.

## Çıktı formatı
```markdown
# Veri Gereksinimleri: <özellik / sistem>
## Varlıklar ve İlişkiler
| Varlık | Tanım | Tanımlayıcı | Yaşam döngüsü durumları | İlişkiler |
## Nitelikler: <Varlık>
| Nitelik | Tanım | Tip / format | Zorunlu | İzin verilen değerler / varsayılan | Doğrulama | Kaynak | Tüketiciler | Hassasiyet |
## Sahiplik
| Varlık | İş sahibi | Veri sorumlusu |
## Kalite Beklentileri
## Saklama ve Silme
| Varlık / nitelik | Saklama süresi | Dayanak | Süre sonu işlemi |
## Taşıma ve Geçmiş İhtiyaçları
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her varlığın iş tanımı, tanımlayıcısı ve kardinaliteli ilişkileri var.
- [ ] Her niteliğin tanımı, tipi, zorunluluk kuralı ve kaynağı var.
- [ ] Hassasiyet nitelik bazında sınıflandı; kişisel veriler için mahremiyet işlemi belirtildi.
- [ ] Saklama ve silme dayanağıyla yazıldı veya `[TBD]` olarak işaretlendi.
- [ ] Her varlığın bir iş sahibi ya da kimin karar vereceğini söyleyen bir açık soru var.
- [ ] Gerçek kişisel veri yer almıyor; değer veya süre uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Veritabanı kolonlarını gereksinim olarak kopyalamak. İş anlamından başla; fiziksel tasarım sonra gelir.
- Türe veya duruma bağlı zorunluluğu koşulsuz bırakmak. Koşulu yaz ("tedarikçi tipi = yurt dışı ise zorunlu").
- Veriyi "ne olur ne olmaz" diye toplamak. Her kişisel niteliğin bir amacı olmalı; yoksa çıkar (veri minimizasyonu).

## Örnek
Girdi: "Tedarikçi kaydı: firma bilgileri, iletişim kişileri, banka hesabı, sertifikalar."

Çıktıdan bir bölüm:
| Nitelik | Tanım | Tip / format | Zorunlu | Doğrulama | Kaynak | Hassasiyet |
|---|---|---|---|---|---|---|
| Vergi numarası | Tedarikçi firmanın vergi kimlik numarası | Metin, 10 hane `[VARSAYIM: yurt içi]` | Evet, tedarikçi tipi = yurt içi ise | Vergi idaresi kuralına göre kontrol hanesi `[TBD]` | Tedarikçi girişi | İç |
| IBAN | Ödemeler için banka hesabı | Metin, IBAN formatı | Evet | Geçerli IBAN; hesap sahibi = firma unvanı | Tedarikçi girişi, Finans doğrular | Gizli |
| İletişim telefonu | İletişim kişisinin iş telefonu | Metin, E.164 | İsteğe bağlı | Geçerli format | Tedarikçi girişi | Kişisel |

Saklama: tedarikçi kayıtları ilişki bittikten sonra `[TBD – Hukuk'tan yasal dayanak]` süre saklanır, ardından anonimleştirilir.
