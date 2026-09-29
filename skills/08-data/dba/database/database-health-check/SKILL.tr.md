---
name: database-health-check
description: "Kullanıcının sağladığı metrikler, görünümler ve ayarlar üzerinden bir veritabanı instance'ının yapılandırılmış sağlık kontrolünü yapar: bekleme profili, en çok kaynak tüketen sorgular, kilitlenme ve bloklanma, depolama büyümesi ve şişkinlik/parçalanma, indeks ve istatistik sağlığı, yapılandırma, replikasyon, yedekler ve temel güvenlik; ardından bulguları kanıt ve çözümleriyle önceliklendirir. Periyodik veritabanı incelemelerinde, yoğun sezon veya geçiş öncesinde, veritabanı genel olarak yavaş hissettirdiğinde ya da tanınmayan bir veritabanı devralındığında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: dba
  area: database
  title: "Veritabanı sağlık kontrolü"
  related: "query-optimization, index-recommendation, backup-restore-plan, capacity-planning, alert-design"
  prompt: "Üretimdeki SQL veritabanımızın sağlık kontrolünü yap. En yüksek beklemeleri, CPU'ya göre ilk 10 sorguyu, dosya boyutlarını ve yapılandırma ayarlarını yapıştırdım."
---

# Veritabanı Sağlık Kontrolü

## Amaç
Bir veritabanı instance'ının sağlığına dair açık, kanıta dayalı bir tablo ve önceliklendirilmiş bir düzeltme listesi vermek; böylece ekip uzun bir genel iyi uygulama listesi yerine gerçekten önemli olan birkaç konuya odaklanır.

## Ne zaman kullanılır
- Bir üretim veritabanının periyodik (ör. çeyreklik) incelemesinde.
- Yoğun sezon, büyük bir sürüm, bir geçiş veya donanım/katman değişikliği öncesinde.
- Veritabanı genel olarak yavaşsa ve sorumlu bilinmiyorsa ya da bir ekip tanımadığı bir veritabanını devralıyorsa.

## Ne zaman kullanılmaz
- Bilinen tek bir sorgu yavaşsa `query-optimization` kullanılır.
- Amaç gelecekteki boyutlandırma ve büyüme tahminiyse `capacity-planning` kullanılır.
- Yalnızca yedekleme ve kurtarma tasarımı söz konusuysa `backup-restore-plan` kullanılır.

## Girdiler
Zorunlu:
- Veritabanı motoru ve dağıtım modeli.
- En az bir kanıt seti: bekleme istatistikleri veya eşdeğeri, kaynak tüketimine göre en önemli sorgular ya da temsili bir döneme ait kaynak metrikleri (CPU, bellek, IO, depolama).

İsteğe bağlı:
- Yapılandırma ayarları, depolama/dosya boyutları ve büyüme geçmişi, indeks ve istatistik metadata'sı, bloklanma/deadlock geçmişi, replikasyon durumu, yedek geçmişi, kullanıcı ve yetki listesi, hata logu alıntıları, donanım/katman özellikleri.

Hiç kanıt verilmediyse tahmin yürütmek yerine kullanıcıya motora uygun, toplanacakların kısa bir listesini (en fazla 5 madde) ver. Kanıtla kapsanmayan alanları `[DEĞERLENDİRİLMEDİ]` olarak işaretle.

## Süreç
1. Bağlamı kaydet: motor, sürüm ailesi, dağıtım modeli, iş yükü tipi (OLTP, raporlama, karma), boyut, iş kritikliği, kanıtın kapsadığı dönem. Çıkarımları `[VARSAYIM]` ile işaretle.
2. Bekleme profilini analiz et: baskın bekleme sınıfları (CPU, IO, kilitler, bellek tahsisi, log yazma, ağ/istemci, paralellik) ve her birinin ne anlama geldiği; zararsız boşta bekleme türlerini dikkate alma.
3. Toplam CPU, okuma ve süreye göre en önemli sorguları incele: maliyete hâkim olan birkaç sorguyu, plan kötüleşmelerini, düşük maliyetli ama çok sık çalışan sorguları (geveze uygulama) ve eksik parametreleştirmeyi işaretle.
4. Eşzamanlılığı kontrol et: bloklanma zincirleri, uzun süren ve işlem içinde boşta bekleyen oturumlar, deadlock sıklığı ve desenleri, izolasyon seviyesi seçimleri.
5. Depolamayı kontrol et: veri ve log büyüme hızı, boş alan, otomatik büyüme ayarları, taramaları gerçekten etkilediği yerde tablo/indeks şişkinliği veya parçalanması, geçici alan kullanımı, log'un yeniden kullanımını engelleyenler.
6. İndeksleri ve istatistikleri kontrol et: kullanılmayan ve mükerrer indeksler, eksik indeks sinyalleri, büyük veya hızlı değişen tablolarda istatistik bayatlığı, bakım işlerinin sonuçları.
7. Yapılandırmayı iş yüküne göre kontrol et: bellek tahsisi, paralellik eşikleri, bağlantı sınırları ve havuzlama, checkpoint/log ayarları, ilgili motora özgü seçenekler; kulaktan dolma kurallardan sapmaları değil iş yüküne uygun olmayan varsayılanları işaretle.
8. Dayanıklılığı ve düzeni kontrol et: replikasyon/HA gecikmesi ve sağlığı, son başarılı yedek ve son geri yükleme testi, tutarlılık kontrolü sonuçları, hata logu sorunları, yama güncelliği, fazla yetkiler ve paylaşılan yönetici hesapları (rapora kimlik bilgisi kopyalanmaz).
9. Her bulguyu önem derecesine göre değerlendir (Kritik: kesinti veya veri kaybı riski; Yüksek: kullanıcıya görünen performans veya yakın vadeli kapasite; Orta; Düşük); kanıtı, somut çözümü, eforu ve biliniyorsa sorumluyu ekle.
10. Genel sağlık durumunu ve ilk 3 aksiyonu özetle. Hedef devam ediyorsa baskın sorgular için `query-optimization`, indeks bulguları için `index-recommendation`, kurtarma boşlukları için `backup-restore-plan` veya bulunan riskleri izlemek için `alert-design` öner.

## Çıktı formatı
```markdown
# Veritabanı Sağlık Kontrolü: <instance> – <tarih>
Motor / model: <...> | İş yükü: <...> | Kanıt dönemi: <...> | Genel durum: <Sağlıklı / Riskli / Kritik>

## İlk 3 Aksiyon
1. ...

## Bulgular
| # | Alan | Bulgu | Kanıt | Önem | Çözüm | Efor |
|---|---|---|---|---|---|---|

## Alan Özeti
| Alan | Durum | Notlar |
|---|---|---|
| Beklemeler | | |
| En önemli sorgular | | |
| Eşzamanlılık | | |
| Depolama | | |
| İndeksler / istatistikler | | |
| Yapılandırma | | |
| HA / yedekler / bütünlük | | |
| Temel güvenlik | | |

## Değerlendirilmeyenler / Toplanacak Veriler
- ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her bulgu girdilerden belirli bir kanıta dayanıyor; kanıtsız genel iyi uygulamalar çıkarılmış.
- [ ] Kanıtı olmayan alanlar sağlıklı sayılmak yerine `[DEĞERLENDİRİLMEDİ]` olarak işaretlenmiş.
- [ ] Önem derecesi önce kesinti/veri kaybı riskini, sonra kullanıcıya görünen etkiyi yansıtıyor.
- [ ] Her bulgunun somut bir çözümü var; riskli olanlarda güvenli uygulama notu eklenmiş.
- [ ] Raporda kimlik bilgisi, bağlantı dizesi veya kişisel veri yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Asıl sorun test edilmemiş bir yedek veya bir bloklanma zinciriyken parçalanma yüzdelerini manşete taşımak.
- Yapılandırmayı gözlenen bekleme profili ve iş yükü yerine genel kulaktan dolma kurallara göre ayarlamak.
- Tek bir anlık görüntüyü temsili saymak; yoğun saatler, batch pencereleri ve ay sonu çoğu zaman farklı bir tablo gösterir.

## Örnek
Girdi: "OLTP veritabanı, beklemeler: %45 kilit, %25 log yazma; en önemli sorgu saatte 1,2M kez çalışıyor; log dosyası 180 GB, %5'i kullanılıyor; son geri yükleme testi bilinmiyor."

Çıktıdan bir bölüm:
- Genel durum: Riskli.
- Bulgu 1 (Yüksek): kilit beklemeleri baskın; bloklanma zincirlerinin başında kilitleri dakikalarca tutan bir toplu güncelleme var `[VARSAYIM: bloklanma geçmişiyle doğrula]`. Çözüm: güncellemeyi parçalara böl, işlemleri kısalt.
- Bulgu 2 (Kritik): geri yükleme testine dair kanıt yok; kurtarma kabiliyeti bilinmiyor. Çözüm: 2 hafta içinde geri yükleme testi, ardından çeyreklik.
- Bulgu 3 (Orta): tek satırlık bir aramanın saatte 1,2M kez çalışması uygulamadan N+1 erişime işaret ediyor; kodda veya önbellekle çöz.
