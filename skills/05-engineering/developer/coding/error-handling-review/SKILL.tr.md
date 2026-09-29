---
name: error-handling-review
description: "Kodun hataları nasıl tespit ettiğini, ilettiğini, yeniden denediğini, yedek davranışa geçtiğini ve raporladığını inceler: istisna tasarımı, yutulan veya fazla geniş catch'ler, yeniden deneme ve zaman aşımı politikası, idempotency, kaynak temizliği, transaction tutarlılığı ve kullanıcıya gösterilen hata mesajları. Hatalar sessiz veya kafa karıştırıcı olduğunda, bir servis veya entegrasyon sağlamlaştırılmadan önce ya da kodun hata yönetimi, istisnaları veya dayanıklılığı incelenmek istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: coding
  title: "Hata yönetimi incelemesi"
  related: "resilience-review, logging-instrumentation, error-message-writing, code-review, error-scenario-catalog"
  prompt: "Bu ödeme istemcisindeki hata yönetimini incele: sağlayıcıyı HTTP ile çağırıyor, hata olursa yeniden deniyor ve sipariş durumunu güncelliyor."
---

# Hata Yönetimi İncelemesi

## Amaç
Hataların kaybolduğu, yanlış sınıflandırıldığı, güvensiz biçimde yeniden denendiği veya kötü gösterildiği yerleri bulmak ve somut düzeltmeler vermek. Böylece kod öngörülebilir biçimde hata verir, mümkün olduğunda toparlanır ve operasyon ekibine ve kullanıcılara doğru bilgiyi iletir.

## Ne zaman kullanılır
- Olaylar sessiz hataları, mükerrer yan etkileri veya yanıltıcı hata mesajlarını ortaya çıkardıysa.
- Kod dış sistemleri (HTTP, kuyruklar, veritabanları, dosyalar) çağırıyor ve üretime çıkmak üzereyse.
- İnceleyen kişi istisnalara, yeniden denemelere ve yedek davranışlara odaklı bir bakış istiyorsa.

## Ne zaman kullanılmaz
- Sistem düzeyinde dayanıklılık (bulkhead, failover, kapasite) gerekiyorsa `resilience-review` kullanılır.
- Yalnızca kullanıcıya gösterilen mesajların ifadesi gerekiyorsa `error-message-writing` kullanılır.
- Genel bir pull request incelemesi gerekiyorsa `code-review` kullanılır.

## Girdiler
Zorunlu:
- Hata yönetimi incelenecek kod ve dili.

İsteğe bağlı, kaliteyi artırır:
- Çağrılan servislerin hata sözleşmeleri ve idempotency garantileri, SLO'lar/zaman aşımları, ekibin hata yönetimi kuralları, yakın zamandaki olaylar.

Dış sözleşme bilinmiyorsa hangi bulguların ona bağlı olduğunu belirt ve `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Hata noktalarını listele: her dış çağrı, ayrıştırma, dönüştürme, kilit, kaynak edinimi ve kural kontrolü.
2. Her biri için hataları sınıflandır: beklenen iş sonucu (örn. yetersiz bakiye), geçici teknik (zaman aşımı, 503), kalıcı teknik (400, şema uyuşmazlığı), programlama hatası.
3. Tespiti kontrol et: her uzak çağrıda zaman aşımı var mı; durum kodları ve yanıt gövdeleri kontrol ediliyor mu; kısmi yanıtlar ele alınıyor mu.
4. İletimi kontrol et: boş veya logla-devam et catch'leri yok; sınırlar dışında temel istisna tipi yakalanmıyor; sarmalarken neden/bağlam korunuyor; iş sonuçları genel istisna olarak değil sonuç veya alan hatası olarak modelleniyor.
5. Yeniden denemeleri kontrol et: yalnızca geçici hatalar; üstel backoff ve jitter ile sınırlı deneme; toplam süre çağıranın zaman aşımı içinde; işlem idempotent (idempotency key) ya da yeniden deneme güvensiz.
6. Tutarlılığı kontrol et: hata sırasında yan etkiler (DB güncellendi ama çağrı başarısız ya da tersi); transaction'lar ve telafi işlemleri; "güncelle ve bildir" için outbox.
7. Temizliği kontrol et: kaynaklar tüm yollarda serbest bırakılıyor (finally/using/defer/with); kilitler bırakılıyor; yarım yazılmış dosya yok.
8. Yedek davranış ve circuit breaker'ı kontrol et: yedek davranış yalnızca "boş dön" değil, iş açısından doğru; kısıtlı çalışma modu görünür.
9. Raporlamayı kontrol et: hata başına doğru sınırda, correlation id'li, gizli bilgi veya kişisel veri içermeyen tek log kaydı; kullanıcı mesajları uygulanabilir ve iç ayrıntı sızdırmıyor; API hataları kararlı bir kod kullanıyor.
10. Bulguları önceliklendir (Kritik: veri kaybı/mükerrer para hareketi; Yüksek: sessiz hata; Orta: zayıf teşhis; Düşük: stil) ve kod düzeyinde düzeltmeler ver.
11. Hedef devam ediyorsa teşhis boşlukları için `logging-instrumentation`, sistem düzeyindeki arıza modları için `resilience-review` veya kullanıcıya gösterilen metinler için `error-message-writing` öner.

## Çıktı formatı
```markdown
# Hata Yönetimi İncelemesi: <birim>
## Hata Noktası Envanteri
| # | İşlem | Hata sınıfları | Mevcut ele alış |

## Bulgular
| # | Önem | Konum | Problem | Sonuç | Düzeltme |

## Önerilen Desen
<ana düzeltme için kısa kod taslağı>

## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her uzak çağrının bir zaman aşımı ve sınıflandırılmış bir hata yolu var.
- [ ] Yeniden denemeler geçici hatalar ve idempotent işlemlerle sınırlı.
- [ ] Hiçbir bulgu, sınır gerekçesi olmadan her şeyi yakalamayı önermiyor.
- [ ] Hata anında tutarlılık (DB ve dış yan etki) analiz edildi.
- [ ] Log önerileri mükerrer kayıt, gizli bilgi ve kişisel veri içermiyor.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve varsayım ya da açık soru olarak listeli; dayanağı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İdempotent olmayan çağrıları (ödeme, e-posta) yeniden deneyip mükerrerliğe yol açmak. Idempotency key iste ya da yeniden deneme.
- Her katmanda loglayıp tekrar fırlatmak ve tek hata için beş stack trace üretmek. Sınırda bir kez logla.
- İş sonuçlarını istisna, teknik hataları normal sonuç gibi ele almak; bu çağıranların ve metriklerin kafasını karıştırır.

## Örnek
Girdi: "PaymentClient: sağlayıcıyı çağır, Exception yakala, 5 kez yeniden dene, sonra siparişi FAILED yap."

Çıktıdan bir bölüm:
| # | Önem | Konum | Problem | Sonuç | Düzeltme |
|---|---|---|---|---|---|
| 1 | Kritik | `charge()` yeniden deneme döngüsü | Okuma zaman aşımında idempotency key olmadan yeniden deniyor | Müşteriden iki kez çekim yapılabilir | `Idempotency-Key = orderId` gönder; yalnızca bağlantı hatası/503'te yeniden dene |
| 2 | Yüksek | `catch (Exception)` | Kart reddi teknik hata gibi ele alınıyor | Sipariş FAILED işaretleniyor ve yeniden deneniyor | Reddi `PaymentDeclined` sonucuna eşle; yeniden deneme yok |
