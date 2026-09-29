---
description: "Bir değişiklik listesinden, commit'lerden veya iş kalemlerinden; yeni özellikler, iyileştirmeler, düzeltmeler, kırıcı değişiklikler, kullanımdan kaldırmalar ve bilinen sorunlar olarak gruplanmış ve belirli bir hedef kitle (son kullanıcılar, yöneticiler, API tüketicileri veya iç ekipler) için yazılmış sürüm notları hazırlar. Bir sürüm yayına çıkmak üzereyken kullanıcıların, müşterilerin veya desteğin neyin değiştiğini ve ne yapmaları gerektiğini bilmesi gerektiğinde kullanılır."
related: "changelog-entry, semantic-versioning, release-announcement, app-store-release-notes, release-plan"
prompt: "Birleştirilmiş şu 23 kaydı 3.8 sürümü için müşterilerimizin sistem yöneticilerine yönelik sürüm notlarına dönüştür."
---

# Sürüm Notları Yazma

## Amaç
Belirli bir hedef kitleye sürümde neyin değiştiğini, bunun onlar için ne anlama geldiğini ve hangi aksiyonu almaları gerektiğini anlatmak. Böylece yükseltmeler güvenli olur ve destek ekibi önlenebilir sorularla dolmaz.

## Ne zaman kullanılır
- Bir sürüm yayına çıkmak üzereyken ve ham bir değişiklik listesi (kayıtlar, commit'ler, pull request başlıkları) varken.
- Sürüm, kullanıcıların aksiyon alması gereken kırıcı değişiklikler, migration'lar veya kullanımdan kaldırmalar içerdiğinde.
- Aynı sürümden farklı hedef kitleler (müşteriler, yöneticiler, API tüketicileri, destek) için farklı notlar gerektiğinde.

## Ne zaman kullanılmaz
- Depoda geliştiricilere yönelik, değişiklik bazlı bir kayıt gerekiyorsa `changelog-entry` kullanılır.
- Pazarlama tarzında bir lansman mesajı gerekiyorsa `release-announcement` kullanılır.
- Mobil uygulama için mağaza metni gerekiyorsa `app-store-release-notes` kullanılır.

## Girdiler
Zorunlu:
- Değişiklik listesi (kayıtlar, commit'ler, pull request'ler veya bir özet).
- Hedef kitle.

İsteğe bağlı, kaliteyi artırır:
- Sürüm numarası ve yayın tarihi.
- Bilinen sorunlar ve geçici çözümler, yükseltme veya migration adımları, kullanımdan kaldırma takvimleri.
- Stil rehberi, ton ve format için önceki sürüm notları.

Değişiklik listesi veya hedef kitle yoksa sor. Bir değişikliğin etkisini yalnızca kayıt başlığından tahmin etme; `[TEYİT ET]` olarak işaretle ve açık soru olarak listele.

## Süreç
1. Değişiklik listesini hedef kitleye göre süz: görünür bir etkisi (performans, güvenlik, uyumluluk) yoksa iç refactor, test ve build değişikliklerini çıkar.
2. Kalan her değişikliği sınıflandır: Yeni, İyileştirildi, Düzeltildi, Kırıcı, Kullanımdan kaldırıldı, Güvenlik, Bilinen sorun.
3. Kırıcı değişiklikleri titizlikle belirle: kaldırılan veya yeniden adlandırılan alanlar, endpoint'ler, ayarlar; değişen varsayılanlar; değişen davranış; yeni zorunlu yapılandırma; minimum sürüm değişiklikleri.
4. Her maddeyi okuyucunun bakış açısından yeniden yaz: ekibin içeride ne yaptığını değil, okuyucunun artık ne yapabildiğini veya neyin artık olmadığını anlat.
5. Her kırıcı veya kullanımdan kaldırılan madde için gereken aksiyonu, son tarihi ve geçiş yolunu belirt.
6. Güvenlik düzeltmelerinde etkilenen sürümleri ve önerilen aksiyonu belirt; kullanıcılar yama yapmadan istismar ayrıntısı verme.
7. Bilinen sorunları geçici çözüm ve beklenen düzeltme durumuyla yalnızca teyit edilmişse ekle; verilmemiş tarihleri asla vaat etme.
8. Bölümleri okuyucunun önce aksiyon alması gerekene göre sırala: kırıcı ve güvenlik, sonra yeni ve iyileştirilmiş, sonra düzeltmeler, sonra bilinen sorunlar.
9. Sürüm numarasının değişiklik türleriyle tutarlı olduğunu kontrol et; minor veya patch sürümünde kırıcı değişiklik varsa işaretle.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa numarayı doğrulamak için `semantic-versioning`, depo kaydı için `changelog-entry` veya pazarlama mesajı için `release-announcement` öner.

## Çıktı formatı
```markdown
# <Ürün> <sürüm> Sürüm Notları
Yayın tarihi: <tarih veya [TBD]> · Hedef kitle: <kitle>

## Aksiyon Gerekli
- **Kırıcı:** <değişiklik> – <kim etkileniyor> – <ne yapılmalı> – <ne zamana kadar>
- **Kullanımdan kaldırıldı:** <özellik> – <sürüm/tarih veya [TBD]> itibarıyla kaldırılması planlanıyor – <alternatif>

## Güvenlik
- <bileşen> içinde <sorun sınıfı> düzeltildi; <sürümler> etkileniyor. Yükseltme önerilir.

## Yeni
- <kullanıcının bakış açısından yetenek>

## İyileştirildi
- ...

## Düzeltildi
- <koşul> durumunda kullanıcının gördüğü <belirti> artık oluşmuyor.

## Bilinen Sorunlar
- <sorun> – geçici çözüm: <...>

## Yükseltme Notları
<adımlar, uyumluluk, minimum sürümler>
```

## Kalite kontrol listesi
- [ ] Her madde iç kayıt jargonuyla değil, okuyucunun diliyle yazıldı.
- [ ] Tüm kırıcı değişikliklerin ve kullanımdan kaldırmaların somut bir gerekli aksiyonu var.
- [ ] Yalnızca içeriye ait değişiklik, kişisel veri, müşteri adı veya istismar ayrıntısı sızmadı.
- [ ] Etkisi belirsiz maddeler tahmin edilmedi, `[TEYİT ET]` olarak işaretlendi.
- [ ] Sürüm numarası kırıcı değişikliklerin varlığıyla tutarlı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kırıcı bir değişikliği "İyileştirildi" listesine gömmek. Okuyucular göz gezdirir; onu en üstte Aksiyon Gerekli altında ver.
- Kayıt başlıklarını kopyalamak ("OrderMapper'da NPE düzeltildi"). Kullanıcının yaşadığı belirtiyi anlat.
- Her commit'i listelemek. Notlar seçilmiş içeriktir; süzülmemiş uzun liste önemli olanı gizler.

## Örnek
Girdi: "PAY-812 Eski /v1/refund endpoint'ini kaldır; PAY-790 Para birimi eksikken fatura dışa aktarımında null pointer düzelt; PAY-801 Logging kütüphanesini yükselt."

Zayıf: "/v1/refund kaldırıldı. Fatura aktarımında NPE düzeltildi. Logging kütüphanesi güncellendi."

Güçlü:
- **Kırıcı:** `/v1/refund` endpoint'i kaldırıldı. Hâlâ bu endpoint'i çağıran entegrasyonlar hata alacaktır; yükseltmeden önce `/v2/refunds` endpoint'ine geçin (bkz. geçiş rehberi).
- **Düzeltildi:** Para birimi değeri olmayan faturalarda dışa aktarım artık hata vermiyor.
- (Logging kütüphanesi güncellemesi çıkarıldı: kullanıcıya görünür etkisi yok `[VARSAYIM]`.)
