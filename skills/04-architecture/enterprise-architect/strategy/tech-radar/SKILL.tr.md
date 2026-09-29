---
description: Teknolojileri çeyrekler (teknikler, platformlar, araçlar, diller ve framework'ler) boyunca Benimse, Dene, Değerlendir ve Beklet halkalarına yerleştiren bir teknoloji radarı oluşturur veya günceller; kanıta dayalı gerekçe, önceki sürüme göre hareket ve ekipler için yönlendirme içerir. Teknoloji yelpazesini standartlaştırırken, dönemsel bir radar yayınlarken veya bir ekibin yeni bir teknolojiyi kullanıp kullanamayacağına karar verirken kullanılır.
related: technology-selection, architecture-principles, technology-strategy, adr, dependency-upgrade
prompt: Teknoloji radarımızı şu önerilerle güncelle: gRPC'yi Değerlendir'den Dene'ye taşı, AngularJS'i Beklet'e al ve OpenTelemetry'yi ekle.
---

# Teknoloji Radarı

## Amaç
Kurumun hangi teknolojileri benimsediğini, denediğini, değerlendirdiğini veya kaçındığını gösteren kısa ve kanıta dayalı bir görünüm yayınlamak. Böylece ekipler sınırlar içinde seçim yapar, mimari birim de tek tek onay vermeden teknoloji yelpazesini yönlendirir.

## Ne zaman kullanılır
- Dönemsel (ör. altı aylık) bir radar sürümü hazırlanırken.
- Bir ekip yeni bir dil, framework, platform veya teknik önerdiğinde.
- Teknoloji yelpazesi dağıldığında ve birleştirme sinyallerine ihtiyaç olduğunda.
- Destek sonu veya güvenlik sorunları nedeniyle öğelerin Beklet'e alınması gerektiğinde.

## Ne zaman kullanılmaz
- Bir proje için tek ve kritik bir teknoloji kararı gerekiyorsa `technology-selection` kullanılır.
- Bir kod tabanında tek bir bağımlılık güncelleniyorsa `dependency-upgrade` kullanılır.
- Yönetim için çok yıllı teknoloji yönü belirleniyorsa `technology-strategy` kullanılır.

## Girdiler
Zorunlu:
- Önerilen öğeler veya mevcut radar; her öğe için çeyrek ve önerilen halka.
- Öğe başına kanıt: kim, nerede kullandı, sonuç ne oldu.

İsteğe bağlı:
- Mimari ilkeler ve standartlar.
- Kullanım envanteri (repo taramaları, lisans verisi), olay veya güvenlik geçmişi.
- Destek ve lisans durumu, kurum içi yetkinlik.

Bir öğe için kanıt yoksa onu Değerlendir'de tut veya `[KANIT GEREKLİ]` olarak işaretle; popülerliğe bakarak yükseltme.

## Süreç
1. Çeyrekleri (Teknikler; Platformlar; Araçlar; Diller ve Framework'ler) ve halka tanımlarını sabitle: Benimse = varsayılan seçim, burada üretimde kanıtlanmış; Dene = sponsoru ve çıkış planı olan bir üretim projesinde kullan; Değerlendir = spike'larla keşfet, üretimde değil; Beklet = yeni işe başlama, çıkışı planla.
2. Önerileri ve mevcut öğeleri topla; tekrarları ayıkla, adları ve sürümleri normalleştir.
3. Her öğe için kanıt topla: üretimde kullanım sayısı, sonuçlar, olaylar, topluluk/üretici sağlığı, lisans, güvenlik durumu, kurum içi yetkinlik, ilkelerle uyum.
4. Halka giriş kriterlerini uygula: Benimse için burada en az iki başarılı üretim kullanımı gerekir `[kurum politikasına göre ayarla]`; Dene için sorumlu ekip, başarı kriterleri ve gözden geçirme tarihi gerekir.
5. Hareketi (yeni, yukarı, aşağı, değişmedi) ve taşınan veya yeni her öğe için 2-4 cümlelik gerekçeyi kaydet.
6. Çakışmaları kontrol et: aynı problemi çözen iki Benimse öğesi için net bir kullanım sınırı gerekir, yoksa biri Beklet'e gider.
7. Her Beklet öğesi için geçiş yönlendirmesini ve çıkışın sorumlusunu yaz.
8. Yönetişim etkilerini belirt: ekiplerin onaysız yapabilecekleri (Benimse), bildirim gerektirenler (Dene), ADR gerektirenler (Beklet istisnaları).
9. Radar tablosunu ve ekipler için kısa bir "ne değişti" özetini üret.

## Çıktı formatı
```markdown
# Teknoloji Radarı – <sürüm/tarih>
Halka tanımları: <tanımlandığı şekliyle Benimse / Dene / Değerlendir / Beklet>

## Ne Değişti
- <öğe>: <eski halka> → <yeni halka> – <tek satır gerekçe>

## Radar
| Çeyrek | Öğe | Halka | Hareket | Gerekçe | Kanıt | Sahibi | Gözden geçirme tarihi |
|---|---|---|---|---|---|---|---|

## Beklet Öğeleri – Çıkış Yönlendirmesi
| Öğe | Yerine | Son tarih veya tetikleyici | Sorumlu |

## Çözülen Çakışmalar
## Yönetişim Notları ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her halka yerleşimi yalnızca sektördeki popülerliğe değil, kurum içi kanıta dayanıyor.
- [ ] Dene öğelerinin ekibi, başarı kriterleri ve gözden geçirme tarihi var.
- [ ] Beklet öğelerinin yerine geçecek seçenek ve sorumlusu var.
- [ ] Hiçbir iki Benimse öğesi belirtilmiş bir sınır olmadan çakışmıyor.
- [ ] Adlar, sürümler ve lisans durumu doğru veya `[BİLİNMİYOR]` olarak işaretli.

## Sık yapılan hatalar
- Radarı istek listesi olarak kullanmak. Kurum içi kanıtı olmayan öğeler Değerlendir'de kalır.
- Hiç öğe çıkarmamak. Eskimiş kayıtlar güveni zedeler; artık yönlendirme gerektirmeyen öğeleri kaldır.
- Çıkış yolu olmadan Beklet. Yerine geçecek seçenek veya son tarih yoksa ekipler Beklet'i yok sayar.

## Örnek
Girdi: "gRPC'yi Dene'ye taşı (ödeme ekibi dahili kullandı), AngularJS'i Beklet'e al, OpenTelemetry'yi ekle."

Çıktıdan bir bölüm:
| Çeyrek | Öğe | Halka | Hareket | Gerekçe |
|---|---|---|---|---|
| Diller ve Framework'ler | gRPC | Dene | Yukarı | Ödemede bir dahili servisler arası kullanım var; Benimse öncesi ikinci ekip ve şema yönetişimi gerekli. |
| Diller ve Framework'ler | AngularJS | Beklet | Aşağı | Üretici desteği bitti; ön yüzleri bir sonraki büyük değişiklikte taşı `[sorumlu TBD]`. |
| Teknikler | OpenTelemetry ölçümleme | Değerlendir | Yeni | Henüz üretim kullanımı yok `[KANIT GEREKLİ]`; platform ekibiyle spike yap. |
