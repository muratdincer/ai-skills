---
description: "Bir tablo veya akış için artımlı yükleme tasarlar: değişiklik tespit yöntemi (log tabanlı CDC, zaman damgası veya sıra numarası watermark'ı, snapshot karşılaştırma), watermark yönetimi, idempotent merge, silmelerin iletimi, geç ve sırasız gelen verinin ele alınışı, mutabakat ve tam yeniden yükleme yedeği. Tam yüklemeler çok yavaş veya maliyetli hale geldiğinde, bir kaynağın düşük gecikmeyle çoğaltılması gerektiğinde ya da yalnızca değişen verinin güvenle nasıl yükleneceği sorulduğunda kullanılır."
related: "pipeline-spec, source-to-target-mapping, data-vault-model, schema-evolution-plan, pipeline-failure-analysis"
prompt: "Tam yüklemesi 6 saat süren 400 milyon satırlık işlem tablosu için artımlı yükleme tasarla."
---

# Artımlı Yükleme Tasarımı

## Amaç
Veriyi kaybetmeden, çoğaltmadan veya sırasını bozmadan yalnızca değişeni yüklemek. Böylece veri hatları tazelik ve maliyet hedeflerini tutturur ve herhangi bir hatadan sonra güvenle yeniden çalıştırılabilir.

## Ne zaman kullanılır
- Tam yüklemeler batch penceresini, kaynak yük sınırlarını veya maliyet bütçesini aşıyorsa.
- Tüketiciler tam yenilemenin sağlayabileceğinden daha düşük gecikme istiyorsa.
- Mevcut bir artımlı yükleme satır kaybediyor veya çoğaltıyorsa ve yeniden tasarlanması gerekiyorsa.

## Ne zaman kullanılmaz
- Veri hattının tamamı (takvim, SLA, operasyon) tanımlanacaksa `pipeline-spec` kullanılır.
- Belirli bir artımlı yükleme hata verdi ve teşhis gerekiyorsa `pipeline-failure-analysis` kullanılır.
- Sorun kaynak veya hedef şemadaki yapısal bir değişiklikse `schema-evolution-plan` kullanılır.

## Girdiler
Zorunlu:
- Anahtarıyla kaynak nesne, satırların nasıl değiştiği (yalnızca ekleme, güncelleme, silme) ve istenen tarihçe davranışıyla hedef (güncel durum, tam tarihçe, ekleme logu).

İsteğe bağlı:
- Hacim ve değişim oranı, mevcut değişiklik sütunları veya değişiklik logları, kaynak kısıtları, gecikme hedefi, kaynağın saat/saat dilimi davranışı, mevcut yükleme kodu.

Kaynağın satırları güncelleyip güncellemediği veya silip silmediği bilinmiyorsa sor; yöntem buna bağlıdır.

## Süreç
1. Kaynağın değişim desenini belirle: yalnızca ekleme, yerinde güncelleme, kalıcı silme, mantıksal silme, geriye tarihli düzeltmeler; güvenilir bir değişiklik göstergesi olup olmadığı.
2. Değişiklik tespit yöntemini seç ve gerekçelendir: log tabanlı CDC (silmeleri ve her değişikliği yakalar, log erişimi gerekir), monoton sıra/ID watermark'ı (yalnızca ekleme), son değişiklik zaman damgası watermark'ı (her değişiklikte güncellenen, güvenilir ve indeksli bir sütun gerekir), snapshot karşılaştırma/hash farkı (gösterge yoksa, maliyeti yüksek).
3. Watermark'ı tanımla: sütun, saklandığı yer, yalnızca hedef commit'i başarılı olduktan sonra güncellenmesi ve saat kaymasını ve uzun süren kaynak işlemlerini telafi eden örtüşme penceresi (geriye bakış).
4. Çekmeyi tanımla: yüklem (`> son watermark − örtüşme` ve `<= çalışma üst sınırı`), hareketli hedefi önlemek için çalışma başına sabit üst sınır ve kaynak tarafı maliyet (indeks kullanımı, okuma replikası).
5. Idempotent uygulamayı tanımla: deterministik sıralamayla iş anahtarı üzerinden merge/upsert (sıra numarası veya commit konumuna göre en son değişiklik kazanır) ya da bölüm üzerine yazma; örtüşmeden gelen mükerrerler zararsız olmalı.
6. Silmelerin iletimini tanımla: CDC silme olayları, tombstone'lar, mantıksal silme bayrağı veya kaynak log olmadan kalıcı silme yapıyorsa periyodik anahtar mutabakatı.
7. Geç ve sırasız gelen veriyi tanımla: olay zamanı ve işlem zamanı, izin verilen gecikme, geç kayıtların toplamları veya tarihçeyi (SCD geçerlilik tarihleri) nasıl güncellediği ve bir bölümün ne zaman kesinleşmiş sayıldığı.
8. Hedefteki tarihçe davranışını tanımla: güncel olanın üzerine yazma, SCD2 sürümleri veya işlem tipiyle ekleme şeklinde değişiklik logu.
9. Mutabakatı tanımla: bölüm veya anahtar aralığı bazında kaynağa karşı periyodik satır sayısı ve checksum karşılaştırması ve hedefli yeniden senkronizasyonun tetikleyicisi.
10. İlk yüklemeyi ve tam yeniden yükleme yedeğini tanımla: boşluk bırakmadan tutarlı snapshot ile değişiklik konumu devri ve tam yeniden yüklemenin ne zaman zorunlu olduğu (şema kırılması, tespit edilen sapma).
11. Hata senaryolarını ve beklenen davranışı listele (yazmadan sonra watermark güncellenmeden çökme, kaynağın geri yüklenmesi, saat değişikliği) ve varsayımları ekle. Hedef devam ediyorsa işin tamamı için `pipeline-spec` veya kaynak değişiklikleri için `schema-evolution-plan` öner.

## Çıktı formatı
```markdown
# Artımlı Yükleme Tasarımı: <kaynak> → <hedef>
Değişim deseni: <...> | Yöntem: <CDC / sıra no / zaman damgası / fark> — <gerekçe>

## Watermark
Sütun: <...> | Saklandığı yer: <...> | Örtüşme: <...> | Güncelleme: hedef commit'inden sonra

## Çekme
Yüklem: <...> | Üst sınır: <...> | Kaynağa etkisi: <...>

## Uygulama
Mod: <merge/bölüm üzerine yazma/append> | Anahtar: <...> | Sıralama: <...> | Idempotency: <nasıl>

## Silmeler, Geç Veri ve Tarihçe
- Silmeler: <...>
- Geç/sırasız: <izin verilen gecikme, ele alınış>
- Tarihçe: <güncel/SCD2/değişiklik logu>

## Mutabakat ve Yedek Yol
- Mutabakat: <sıklık, yöntem> | Yeniden senkronizasyon tetikleyicisi: <...>
- İlk yükleme / tam yeniden yükleme: <...>

## Hata Senaryoları
| Senaryo | Beklenen davranış |
|---|---|

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Yöntem, silmeler ve geriye tarihli güncellemeler dahil değişim desenine uygun.
- [ ] Watermark yalnızca başarılı commit'ten sonra ilerliyor; bir örtüşme penceresi var.
- [ ] Herhangi bir pencerenin yeniden çalıştırılması idempotent; anahtar başına birden fazla değişikliğin sıralaması deterministik.
- [ ] Geç ve sırasız gelen veri için davranış tanımlı.
- [ ] Mutabakat sapmayı yakalıyor ve boşluksuz bir ilk/tam yeniden yükleme yolu var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bazı kod yollarının (toplu güncellemeler, trigger'lar, manuel düzeltmeler) güncellemediği bir son değişiklik sütununa güvenmek.
- Watermark'ta üst sınır veya örtüşme olmadan `>=` ya da `>` kullanmak: uzun işlemlerin geç commit ettiği satırlar sonsuza dek kaybolur.
- Silmeleri unutmak: zaman damgası watermark'ları kalıcı silinen satırları hiç görmez ve hedef sessizce sapar.

## Örnek
Girdi: "400 milyon satırlık işlem tablosu, güncelleme var, silme yok, tam yükleme 6 saat; last_updated sütunu mevcut."

Çıktıdan bir bölüm:
- Yöntem: last_updated üzerinde zaman damgası watermark'ı `[VARSAYIM: toplu düzeltmeler dahil her yazma yolunun bu sütunu güncellediğini doğrula]`; güncellemiyorsa CDC'ye geç.
- Çekme: last_updated > watermark − 15 dk AND <= run_start; örtüşmeden gelen mükerrerler txn_id üzerinden max(last_updated) tutularak merge ile elenir.
- Mutabakat: ay bölümleri bazında haftalık sayı + sum(amount) kaynakla karşılaştırılır; uyuşmazlık yalnızca o ayın yeniden senkronizasyonunu tetikler.
