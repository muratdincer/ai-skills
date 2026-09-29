---
name: dependency-upgrade
description: "Bir kütüphane, framework veya çalışma ortamı güncellemesini planlar ve uygular: mevcut ve hedef sürüm arasındaki sürüm notlarını ve geçiş kılavuzlarını okur, kod tabanını gerçekten etkileyen kırıcı değişiklikleri listeler, geçiş adımlarını sıralar, geçişli bağımlılık çakışmalarını ele alır, doğrulama ve geri dönüşü tanımlar. Güvenlik, destek sonu veya ihtiyaç duyulan bir özellik nedeniyle bağımlılık güncellenmesi gerektiğinde, otomatik güncelleme pull request'i başarısız olduğunda veya X sürümünden Y'ye nasıl geçileceği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: coding
  title: "Bağımlılık güncelleme"
  related: "dependency-vulnerability-review, semantic-versioning, refactoring, changelog-entry, pull-request-description"
  prompt: "Web framework'ümüzü 6. ana sürümden 8'e yükseltmeyi planla; bağımlılık manifesti ve kullandığımız özelliklerin listesi burada."
---

# Bağımlılık Güncelleme

## Amaç
Bir bağımlılığı etkisi bilinen ve sınırlı olacak şekilde hedef sürüme taşımak: ilgili her kırıcı değişiklik ele alınmış, her adımda build ve testler yeşil ve canlı ortam aksini söylerse geri dönüş yolu hazır.

## Ne zaman kullanılır
- Bir güvenlik açığı, destek sonu veya gereken bir özellik güncellemeyi zorunlu kıldığında.
- Otomatik bir bağımlılık güncellemesi build'i bozduğunda veya testleri kırdığında.
- Ana sürüm atlaması (framework, ORM, çalışma ortamı, SDK) bir geçiş planı gerektirdiğinde.

## Ne zaman kullanılmaz
- Bildirilen bir açığın istismar edilebilir ve acil olup olmadığına karar vermek için `dependency-vulnerability-review` kullanılır.
- Farklı kütüphaneler arasında seçim yapmak için `technology-selection` kullanılır.
- Sürüm değişikliği olmadan kodu yeniden yapılandırmak için `refactoring` kullanılır.

## Girdiler
Zorunlu:
- Bağımlılık adı, mevcut sürüm, hedef sürüm (veya "desteklenen en güncel").
- Bağımlılık manifesti veya lock dosyası ya da bağımlılığın nasıl kullanıldığının açıklaması.

İsteğe bağlı, kaliteyi artırır:
- Kullanıcının yapıştırabileceği sürüm notları ve geçiş kılavuzları, build ve test çıktısı, çalışma ortamı ve platform sürümleri, onu sabitleyen diğer bağımlılıklar.

Kırıcı değişiklikleri hafızadan olgu gibi sayma. Kullanıcıdan ilgili sürüm notlarını yapıştırmasını iste veya hatırlanan her değişikliği `[sürüm notlarından DOĞRULA]` olarak işaretle.

## Süreç
1. Sürüm aralığını ve nedeni (güvenlik, destek sonu, özellik) belirle; sürümleme şemasını (SemVer mi) ve ara ana sürümlerden adım adım geçilmesi gerekip gerekmediğini kontrol et.
2. Aralıktaki değişiklikleri topla: kırıcı değişiklikler, kullanımdan kaldırmalar, yeni minimum çalışma ortamı veya platform sürümleri, değişen varsayılanlar, kaldırılan geçişli bağımlılıklar.
3. Her değişikliği kod tabanına eşle: arama noktaları (API'ler, config anahtarları, annotation'lar, build eklentileri) ve her birini Etkilenir, Etkilenmez veya Bilinmiyor olarak işaretle.
4. Bağımlılık grafiğini kontrol et: peer veya geçişli çakışmalar, uyumlu sürüm isteyen diğer paketler, çözümleme sonrası mükerrer sürümler.
5. Geçişi sırala: ön koşul güncellemeleri (çalışma ortamı, build aracı), önce eski sürümde kullanımdan kaldırılanları düzelt, sonra sürümü yükselt, sonra kaldırılanlara uyum sağla, sonra yeni varsayılanları bilinçli olarak benimse.
6. Her adımı build edilebilir ve test edilebilir tut; birlikte hareket etmeleri gerekmedikçe commit başına tek bağımlılık yükselt.
7. Testlerin yakalamayabileceği davranış değişikliklerini belirle: varsayılan timeout'lar, serileştirme, tarih/saat işleme, güvenlik varsayılanları, log formatı, performans.
8. Doğrulamayı tanımla: tüm test paketi, etkilenen alanlar için hedefli testler, canlıya benzer ortamda smoke test, yayın sonrası temel metriklerin karşılaştırılması.
9. Geri dönüşü tanımla: commit'i geri al ve yeniden deploy et, lock dosyasını geri yükle, tek yönlü veri veya config geçişleri ve bunların nasıl ele alınacağı.
10. Takip işlerini listele: uyumluluk ara katmanlarını kaldır, yeni özellikleri sonra benimse, dokümantasyonu ve changelog'u güncelle.
11. Hedef devam ediyorsa değişikliği sunmak için `pull-request-description`, sürüm notları için `changelog-entry` veya tetikleyici bir açıksa `dependency-vulnerability-review` öner.

## Çıktı formatı
```markdown
# Bağımlılık Güncelleme: <ad> <mevcut> → <hedef>
Neden: <güvenlik/destek sonu/özellik> · Şema: <SemVer?> · Geçiş: <doğrudan / X üzerinden>

## Değişiklik Etkisi
| Değişiklik | Kaynak | Etkilenir mi? | Nerede | Aksiyon |

## Bağımlılık Grafiği Sorunları
- ...

## Geçiş Adımları
| # | Adım | Doğrulama | Commit |

## İzlenecek Davranış Değişiklikleri
- ...

## Geri Dönüş
- ...

## Takip İşleri ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her kırıcı değişiklik bir kaynağa (sürüm notu, kılavuz) dayanıyor ya da `[sürüm notlarından DOĞRULA]` olarak işaretli.
- [ ] Her değişiklik kod tabanına Etkilenir, Etkilenmez veya Bilinmiyor olarak eşlendi.
- [ ] Adımlar her birinden sonra build yeşil kalacak şekilde sıralı.
- [ ] Sessiz davranış değişiklikleri (varsayılanlar, serileştirme, zaman, güvenlik) listelendi.
- [ ] Geri dönüş tek yönlü geçişleri açıkça kapsıyor.
- [ ] Bilinmeyen etki güvenli varsayılmadı, açık soru olarak listelendi; her çıkarım `[VARSAYIM]` olarak etiketlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Birkaç ana sürümü tek seferde atlayıp hangi değişikliğin hangi hataya yol açtığını bilmeden bir yığın hatayla uğraşmak.
- Test paketi timeout veya JSON harf düzeni gibi değişen varsayılanları kapsamıyorken "testler geçiyor"a güvenmek.
- Kullanımdan kaldırılan çağrıları yerinde bırakarak yükseltmek ve bir sonraki ana sürümde tıkanmak.

## Örnek
Girdi: "HTTP istemci kütüphanesini 4.x'ten 5.x'e yükselt; 12 yerde kullanıyoruz, özel retry handler ve bağlantı havuzu ayarı var."

Çıktıdan bir bölüm:
| Değişiklik | Kaynak | Etkilenir mi? | Nerede | Aksiyon |
|---|---|---|---|---|
| Retry handler arayüzü değişti | `[sürüm notlarından DOĞRULA]` | Etkilenir | `RetryConfig.kt` | Yeni retry stratejisi API'sine taşı, deneme sayısını ve backoff'u koru |
| Varsayılan bağlantı timeout'u değişti | Geçiş kılavuzu, "Defaults" | Bilinmiyor | Tüm istemciler | Davranışı korumak için yükseltmeden önce timeout'ları açıkça ayarla |
