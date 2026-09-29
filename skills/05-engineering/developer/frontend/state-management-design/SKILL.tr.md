---
name: state-management-design
description: "Front-end'deki her durum parçasının nerede tutulacağını (yerel bileşen, URL, form, paylaşılan istemci, sunucu önbelleği, kalıcı depolama) ve nasıl aktığını, eşitlendiğini, geçersiz kılındığını ve test edildiğini framework'ten bağımsız biçimde tasarlar; global store kullanımını gerekçelendirir. Bir front-end özelliği veya uygulaması başlarken, durum ekranlar arasında tekrarlandığında ya da tutarsızlaştığında, ekip global store eklemeyi veya kaldırmayı tartışırken ya da sunucu verisi önbellekleme ve iyimser güncelleme kararları verilecekken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: frontend
  title: "Durum yönetimi tasarımı"
  related: "component-design, technical-design-doc, api-contract, adr, web-performance-audit"
  prompt: "Sipariş yönetimi ekranlarımız düzenlemeden sonra eski veri gösteriyor ve her şey tek bir global store'da. Durum yönetimini yeniden tasarlamamıza yardım et."
---

# Durum Yönetimi Tasarımı

## Amaç
Her durum parçasını tüketicilerini karşılayan en dar yere koymak; tek bir doğruluk kaynağı ve eşitleme ile geçersiz kılma için açık kurallar belirlemek. Sonuç; eski veriyi, gereksiz yeniden render'ları ve istemeden oluşan bağımlılıkları azaltan bir durum envanteri ve karar setidir.

## Ne zaman kullanılır
- Yeni bir front-end uygulaması veya özelliği için durum mimarisine karar verilmesi gerektiğinde.
- Ekranlar eski veya tutarsız veri gösterdiğinde ya da aynı veri birden fazla store'a kopyalandığında.
- Ekip bir global durum kütüphanesini eklemeyi, değiştirmeyi veya kaldırmayı tartışırken.

## Ne zaman kullanılmaz
- Tek bir bileşenin API'si (prop'lar, olaylar, kontrollü durum) için `component-design` kullanılır.
- Veriyi sunan back-end API'sini tasarlamak için `api-contract` kullanılır.
- Zaten verilmiş tek bir kararı kaydetmek için `adr` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki özellik veya ekranlar ve gösterdikleri ya da düzenledikleri veri (açıklama, kullanıcı hikayeleri veya mevcut kod yapısı).

İsteğe bağlı, kaliteyi artırır:
- Framework, render modu (sunucu, istemci, hibrit) ve kullanılan kütüphaneler.
- API özellikleri: uç noktalar, sayfalama, gerçek zamanlı kanallar, tutarlılık ihtiyaçları.
- Mevcut sorunlar (eski veri, performans, hatalar) ve örnekleri.
- Çevrimdışı, çoklu sekme veya eşzamanlı çalışma gereksinimleri.

Veri ve ekranlar net değilse önce ana kullanıcı akışlarını sor. Çıkarım yapılan her gereksinimi (örneğin çevrimdışı destek) `[VARSAYIM]` olarak işaretle.

## Süreç
1. Durum envanterini çıkar: her veri parçasını veya arayüz koşulunu, kimin okuduğunu, kimin yazdığını, ömrünü ve bugün nerede tutulduğunu listele.
2. Her maddeyi sınıflandır: sunucu durumu (sahibi back-end, istemcide önbelleklenir), URL durumu (filtreler, sayfalama, seçili sekme, paylaşılabilir veya yer imine eklenebilir her şey), form durumu (taslak değerler, doğrulama), yerel UI durumu (açık, hover, odak), paylaşılan istemci durumu (oturum, tema, feature flag, ekranlar arası seçimler), kalıcı istemci durumu (tercihler, çevrimdışı taslaklar).
3. Saklamak yerine türet: diğerlerinden hesaplanabilen her maddeyi (toplamlar, filtrelenmiş listeler, bayraklar) kaldır ve türetme kuralını not et.
4. Her maddeyi tüm okuyucularına hizmet eden en alt seviyeye yerleştir; yalnızca en yakın ortak sahibe taşı. Global store yalnızca ağacın birbirinden uzak parçalarını gerçekten kesen paylaşılan istemci durumunu tutar.
5. Sunucu durumu için önbellek politikasını tanımla: önbellek anahtarı, tazelik süresi, yeniden çekme tetikleyicileri (odak, yeniden bağlanma, aralık, olay), mutation sonrası geçersiz kılma, sayfalama stratejisi ve istek tekilleştirme. Sunucu verisini asla ayrı bir istemci store'una kopyalama.
6. Mutation'ları tanımla: kötümser veya iyimser güncelleme, hata durumunda geri alma, çakışma yönetimi (sürüm veya ETag) ve hangi önbellek girdilerinin geçersiz kılınacağı ya da güncelleneceği.
7. Eşitleme sınırlarını tanımla: URL ↔ durum, çoklu sekme, gerçek zamanlı bildirimler, çevrimdışı kuyruk; çakışmada hangi tarafın kazandığını belirt.
8. Performansı kontrol et: bileşenlerin yalnızca kullandıkları dilim değiştiğinde yeniden render olmasını sağlayan abonelikler, memoize edilmiş selector'lar, büyük listeler ve birçok ekranın aynı kayıtları düzenlediği yerlerde normalize edilmiş varlıklar.
9. Test yaklaşımını tanımla: saf reducer ve selector'lar için birim testleri, taklit edilmiş ağ katmanıyla önbellek davranışı testleri, kritik akışlar (düzenle, ardından listenin yenilenmesi) için entegrasyon testleri.
10. Kararları gerekçesi ve reddedilen alternatiflerle kaydet; kütüphane seçiliyor veya değiştiriliyorsa varsayılan bir kazanan ilan etmek yerine kriterleri listele (ekip deneyimi, sunucu önbelleği desteği, geliştirici araçları, bundle boyutu, geçiş maliyeti).
11. Kullanıcı devam ederse ana kararı kaydetmek için `adr`, etkilenen bileşenler için `component-design`, değişiklik birden fazla ekibi kapsıyorsa `technical-design-doc` öner.

## Çıktı formatı
```markdown
# Durum Yönetimi Tasarımı: <özellik/uygulama>

## Durum Envanteri
| Durum | Kategori | Okuyanlar | Yazanlar | Ömür | Konum (hedef) | Notlar |
|---|---|---|---|---|---|---|

## Türetilen Değerler
- <değer> = <türetme>

## Sunucu Önbellek Politikası
| Kaynak (önbellek anahtarı) | Tazelik | Yeniden çekme tetikleyicileri | Geçersiz kılan | İyimser mi? |
|---|---|---|---|---|

## Eşitleme Kuralları
- URL: ... · Sekmeler: ... · Gerçek zamanlı: ... · Çevrimdışı: ...

## Kararlar
| Karar | Gerekçe | Reddedilen alternatifler |
|---|---|---|

## Geçiş Adımları (mevcut kod değişiyorsa)
1. ...

## Test Yaklaşımı
- ...

## Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her durum parçasının tam olarak bir doğruluk kaynağı ve bir kategorisi var.
- [ ] Sunucu verisi istemci store'unda tekrarlanmıyor; geçersiz kılma kuralları olan bir önbellek politikası var.
- [ ] Paylaşılabilir görünüm durumu (filtreler, sayfalar, sekmeler) gerekçesi belirtilmedikçe URL'de.
- [ ] Türetilen değerler saklanmıyor, hesaplanıyor.
- [ ] Her mutation için güncelleme stratejisi, geri alma ve geçersiz kılma tanımlı.
- [ ] Çıkarım yapılan gereksinimler `[VARSAYIM]` olarak etiketli ve açık sorularda listeli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Tutarlılık için" her şeyi global store'a koymak; bu sunucu verisini bayatlatır ve ilgisiz ekranları birbirine bağlar. Sunucu önbelleğini istemci durumundan ayır.
- Filtre ve sayfalamayı bellekte tutmak; yenileme, geri gitme ve paylaşılan linkler görünümü kaybeder.
- Geri alma veya çakışma yönetimi olmadan iyimser güncelleme yapmak; sunucunun reddettiği veri sessizce gösterilir.

## Örnek
Girdi: "Sipariş listesi ve sipariş detayı; detaydaki düzenlemeler listede görünmüyor; her şey uygulama açılışında çekilen tek bir global store'da."

Çıktıdan bir bölüm:
| Durum | Kategori | Okuyanlar | Yazanlar | Ömür | Konum (hedef) | Notlar |
|---|---|---|---|---|---|---|
| Sipariş sayfası | Sunucu | Liste | API | Önbellek, 30 sn taze `[VARSAYIM]` | `orders?status&page` anahtarlı sunucu önbelleği | Sipariş güncellemesiyle geçersiz kılınır |
| Sipariş detayı | Sunucu | Detay, liste satırı | Düzenleme formu | Önbellek | `order:{id}` anahtarlı sunucu önbelleği | Güncelleme liste girdisine de yazılır |
| Durum filtresi, sayfa | URL | Liste | Filtre çubuğu | Oturum | Query string | Paylaşılabilir link sağlar |
| Düzenleme taslağı | Form | Düzenleme formu | Kullanıcı | Kaydet veya iptale kadar | Form durumu | Sayfadan ayrılırken onayla atılır |

Karar: siparişleri global store'dan çıkar; orada yalnızca oturum ve feature flag'leri tut.
