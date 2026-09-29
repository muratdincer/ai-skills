---
name: source-to-target-mapping
description: "Bir veri yüklemesi için sütun düzeyinde kaynak-hedef eşleme (STTM) dokümanı yazar: tip ve boş olabilirlikle hedef sütunlar, kaynak sütunlar, dönüşüm ve iş kuralları, lookup'lar, varsayılanlar, anahtar üretimi, filtreler, join koşulları, reddedilen kayıtların ele alınışı ve test senaryoları. Bir veri hattı, veri göçü veya entegrasyon yüklemesi kurulacak ya da gözden geçirilecekse, türetilmiş alanların iş kuralları netleştirilecekse veya iki şema arasında eşleme tablosu istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-engineer
  area: pipelines
  title: "Kaynak-hedef eşleme dokümanı"
  related: "pipeline-spec, field-mapping, data-lineage-doc, dimensional-model, test-data-design"
  prompt: "CRM müşteri ve adres tablolarından dim_customer tablomuza kaynak-hedef eşleme dokümanı oluştur."
---

# Kaynak-Hedef Eşleme Dokümanı

## Amaç
Her hedef sütunun nasıl doldurulduğunu kesin olarak tanımlamak. Böylece geliştiriciler analistlerin kastettiği mantığı kurar, test uzmanları senaryo türetebilir ve herkes bir hedef değeri kaynağına kadar izleyebilir.

## Ne zaman kullanılır
- İki şema arasında veri ambarı yüklemesi, veri göçü veya entegrasyon beslemesi kuruluyorsa.
- Mantığı yalnızca kodda yaşayan mevcut bir yükleme gözden geçiriliyorsa.
- Türetilmiş sütunların (durum, segment, tutar) iş kuralları üzerinde uzlaşılıp onaylanması gerekiyorsa.

## Ne zaman kullanılmaz
- İş analizi bağlamında uygulama ekranları, API'ler veya mesajlar arasında alan eşlemesi yapılıyorsa `field-mapping` kullanılır.
- Konu veri hattının zamanlaması, SLA'ları ve operasyonuysa `pipeline-spec` kullanılır.
- Denetim veya etki için çok adımlı uçtan uca akış gerekiyorsa `data-lineage-doc` kullanılır.

## Girdiler
Zorunlu:
- Hedef şema (veya hedef model) ve kaynak şema(lar) ya da örnek veriler.

İsteğe bağlı:
- İş kuralları, kod listeleri ve referans veri, mevcut SQL, veri profilleme sonuçları, bilinen veri sorunları, anahtar stratejisi (surrogate/doğal), SCD gereksinimleri.

Hedef yapı yoksa iste ya da önce `dimensional-model` / `logical-data-model` öner; tanımsız bir hedefe eşleme yapmak yeniden işe yol açar.

## Süreç
1. Hedef taneciği ve sürücü kaynağı (satırları hedef satırları üreten tablo) tanımla; diğer kaynaklara giden join yolunu ve join tiplerini kardinaliteleriyle birlikte belirt.
2. Veri seti düzeyindeki kuralları belirt: filtreler (hangi kaynak satırları neden dahil/hariç), tekilleştirme kuralı, artımlı seçim kriteri.
3. Her hedef sütun için kaynak tablo.sütun'u (veya "türetilmiş"/"sabit"/"üretilmiş") ve dönüşümü kaydet: tip dönüşümü, trim, harf düzeni, bölme/birleştirme, lookup, hesaplama, koşullu mantık, birim/para birimi/saat dilimi dönüşümü.
4. Dönüşüm mantığını sözde SQL veya CASE ifadeleriyle tek anlamlı yaz; boş değer yönetimi ve eşleşmeyen lookup'lar için varsayılan dahil (ör. bilinmeyen üye anahtarı -1).
5. Anahtar yönetimini tanımla: doğal/iş anahtarı, surrogate anahtar üretimi ve boyutlar için nitelik bazında SCD tipi ile geçerlilik tarihi mantığı.
6. Kaynak ve hedef arasındaki tip ve uzunluk uyumsuzluklarını (kesilme, hassasiyet kaybı, karakter kodlaması) işaretle ve çözümünü belirt.
7. Reddedilen kayıtları tanımla: hangi koşulların satırı reddettiği veya karantinaya aldığı, hangilerinde varsayılanla yüklendiği ve reddedilenlerin nereye gittiği.
8. Kişisel veri sütunlarını ve hedefte gereken maskeleme veya dışlamayı işaretle.
9. Önemsiz olmayan her kural için test senaryosu ekle: girdi değerleri ve beklenen çıktı; boş değerler, sınır değerler ve eşleşmeyen lookup'lar dahil.
10. Her eşleme satırının durumunu (iş tarafınca teyitli, `[VARSAYIM]`, `[TBD]`) ve açık soruları kaydet. Hedef devam ediyorsa yüklemeyi işletmek için `pipeline-spec` veya daha kapsamlı test verisi için `test-data-design` öner.

## Çıktı formatı
```markdown
# Kaynak-Hedef Eşleme: <kaynak> → <hedef>
Tanecik: <...> | Sürücü kaynak: <...> | Yükleme tipi: <tam/artımlı> | Sürüm: <...>

## Join'ler ve Filtreler
- <kaynak A> LEFT JOIN <kaynak B> ON <...> (1:n) — <gerekçe>
- Filtre: <...> | Tekilleştirme: <...>

## Sütun Eşlemesi
| # | Hedef sütun | Tip | Null | Kaynak (tablo.sütun) | Dönüşüm / kural | Varsayılan / eşleşmeyen | Kişisel veri | Durum |
|---|---|---|---|---|---|---|---|---|

## Anahtarlar ve Tarihçe
<iş anahtarı, surrogate anahtar, nitelik bazında SCD tipi>

## Reddedilen Kayıtlar
| Koşul | Aksiyon | Hedef yer |
|---|---|---|

## Test Senaryoları
| Kural # | Girdi | Beklenen çıktı |
|---|---|---|

## Açık Sorular
- [TBD] ...
```

## Kalite kontrol listesi
- [ ] Her hedef sütun eşlendi ya da açıkça türetilmiş/sabit/üretilmiş olarak işaretlendi.
- [ ] Tanecik, sürücü kaynak ve join kardinaliteleri belirtildi; satır çoğalması riskleri ele alındı.
- [ ] Her dönüşüm boş değerleri ve eşleşmeyen lookup'ları ele alıyor.
- [ ] Tip/uzunluk uyumsuzlukları çözümüyle birlikte işaretlendi.
- [ ] Kişisel veri sütunları maskeleme/dışlama bilgisiyle işaretlendi.
- [ ] Teyit edilmemiş kurallar `[VARSAYIM]` veya `[TBD]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her sütun için "doğrudan aktarım" yazmak. Hatalar sessiz tip dönüşümlerinde, trim'lerde ve saat dilimi kaymalarında saklanır; bunları açıkça yaz.
- Join kardinalitesini belirtmemek: adreslere 1:n join, hedefte müşterileri çoğaltır.
- İş kurallarını kesin yüklem olmadan düz metinle yazmak ("yalnızca aktif müşteriler").

## Örnek
Girdi: "CRM müşteri + adres verisi dim_customer'a (segment ve şehirde SCD2)."

Çıktıdan bir bölüm:
- Join: customer LEFT JOIN address ON customer_id AND address.type = 'BILLING' AND address.is_current = 1 (1:0..1) — satır çoğalmasını önler.
- segment: CASE WHEN annual_revenue >= [TBD eşik] THEN 'Enterprise' ELSE 'SMB' END; boş gelir → 'Unknown'. `[VARSAYIM: Satış Operasyonlarıyla teyit et]`
- email: trim, küçük harf; kişisel veri, canlı dışı hedeflerde maskelenir.
