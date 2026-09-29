---
name: data-lineage-doc
description: "Veri kökenini kaynak sistemlerden alım, dönüşüm ve depolama katmanları üzerinden raporlara, modellere ve diğer tüketicilere kadar, veri seti ve kritik sütun düzeyinde, dönüşüm mantığı, sahipler ve doğrulama durumuyla belgeler. Bir rakamın nereden geldiği sorulduğunda, değişiklik öncesi etki analizi için, denetim veya yasal izlenebilirlik gerektiğinde ya da ekibe tanımadığı bir veri akışı anlatılırken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-architect
  area: governance
  title: "Veri kökeni dokümantasyonu"
  related: "data-catalog-entry, source-to-target-mapping, impact-analysis, data-quality-rules, diagram-as-code"
  prompt: "Finans panosundaki 'net gelir' rakamının kaynak sistemlere kadar veri kökenini belgele."
---

# Veri Kökeni Dokümantasyonu

## Amaç
Bir veri setinin veya metriğin kaynaklarından nasıl üretildiğini doğrulanabilir biçimde göstermek. Böylece insanlar veriye güvenebilir, hataları kaynağına kadar izleyebilir ve değişikliklerin etkisini tüketicileri bozmadan önce değerlendirebilir.

## Ne zaman kullanılır
- Raporlanan bir rakam sorgulandığında ve nasıl türetildiği açıklanmak zorunda olduğunda.
- Bir kaynak, tablo veya sütun değişmek üzereyken alt akış etkisi gerektiğinde.
- Denetim veya mevzuat, raporlanan verinin izlenebilirliğini istediğinde (ör. finansal veya risk raporlaması).

## Ne zaman kullanılmaz
- Veri hattı inşası için sütun sütun ayrıntılı yükleme tanımı gerekiyorsa `source-to-target-mapping` kullanılır.
- Tek bir veri seti için keşif odaklı özet isteniyorsa `data-catalog-entry` kullanılır.
- Veri akışlarının ötesinde bir iş veya sistem değişikliğinin etkisi soruluyorsa `impact-analysis` kullanılır.

## Girdiler
Zorunlu:
- Köken hedefi (veri seti, sütun, metrik veya rapor) ve eldeki kanıtlar: SQL/dönüşüm kodu, veri hattı tanımları, iş listeleri, mimari notlar veya kişilerin anlatımı.

İsteğe bağlı:
- Kapsam yönü (yukarı akış, aşağı akış, ikisi), derinlik, sahipler, takvimler, bilinen sorunlar, verinin hassasiyeti.

Hiç kanıt yoksa kod, veri hattı adları veya akışı bilen bir kişi iste; tahminle kurulmuş köken, hiç olmamasından kötüdür.

## Süreç
1. Hedefi ve yönü sabitle: yukarı akış (nereden geliyor), aşağı akış (kim kullanıyor) veya ikisi; ayrıntı düzeyini belirle (veri seti düzeyi, kritik öğeler için sütun düzeyi).
2. Akışı kanıtlardan adım adım izle: kaynak sistem ve nesne, çekme yöntemi, landing/ham katman, her dönüşüm adımı, sunum katmanı, tüketici (rapor, model, dışa aktarım, API).
3. Her adım için kaydet: düğüm adı, katman, sahip, çalışma takvimi ve dönüşüm türü (doğrudan aktarım, filtre, join, toplama, türetme, lookup, tekilleştirme, manuel düzeltme).
4. Kritik sütunlar için türetimi formül veya sözde SQL olarak yaz; filtreler, join anahtarları, para birimi/birim dönüşümleri ve sabit kodlanmış değerler dahil.
5. Her adımın doğrulama durumunu işaretle: koddan doğrulandı, sistem metaverisinden doğrulandı, bir kişi tarafından söylendi veya `[ÇIKARIM]`. Çıkarım yapılan adımları asla doğrulanmış gibi sunma.
6. Kopuklukları ve riskleri işaretle: manuel adımlar (tablolar, dosya yüklemeleri), belgelenmemiş mantık, aynı olgu için birbiriyle yarışan kaynaklar, tek değişikliğin çok sayıda tüketiciyi etkilediği dağılım noktaları.
7. Kontrol noktalarını not et: yol boyunca veri kalitesi kontrollerinin, mutabakatların veya onayların yapıldığı yerler.
8. Hassas veri hareketini not et: kişisel verinin nereye girdiği, nerede maskelendiği veya kontrollü ortamdan nerede çıktığı.
9. Akışı soldan sağa bir diagram-as-code bloğu olarak çiz ve bir adım tablosuyla eşleştir.
10. Boşlukları, açık soruları ve bunları kapatabilecek kişileri listele. Hedef devam ediyorsa planlı bir değişiklik için `impact-analysis`, korumasız adımlar için `data-quality-rules` veya sonucu yayımlamak için `data-catalog-entry` öner.

## Çıktı formatı
```markdown
# Veri Kökeni: <hedef>
Yön: <yukarı/aşağı/ikisi> | Ayrıntı: <veri seti / sütun> | Tarih: <tarih> | Hazırlayan: <...>

## Diyagram
<diagram-as-code, kaynak → ... → tüketici>

## Adımlar
| # | Nereden | Nereye | Katman | Dönüşüm | Mantık (kritik sütunlar) | Sahip | Takvim | Doğrulama |
|---|---|---|---|---|---|---|---|---|

## Kontrol Noktaları
- <# numaralı adımdaki kontrol / mutabakat / onay>

## Riskler ve Kopukluklar
- <manuel adım, yarışan kaynak, dağılım noktası>

## Boşluklar ve Açık Sorular
- [ÇIKARIM] ... — <rol> ile teyit et
```

## Kalite kontrol listesi
- [ ] Her adım kanıt türünü belirtiyor; çıkarım yapılan adımlar `[ÇIKARIM]` olarak etiketli.
- [ ] Kritik sütunların filtreler ve dönüşümler dahil açık türetim mantığı var.
- [ ] Manuel adımlar ve yarışan kaynaklar örtbas edilmeden işaretlendi.
- [ ] Kişisel veri hareketi ve maskeleme noktaları gösterildi.
- [ ] Diyagram ile adım tablosu birbiriyle uyumlu.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Veri ambarında durmak. Rakamlar çoğu zaman ambar ile yönetim sunumu arasındaki tablo düzeltmesinde ayrışır.
- Yalnızca tablo düzeyinde köken. "Gelir siparişlerden gelir" ifadesi, iadeleri dışlayan filtreyi gizler.
- Araçla toplanan kökeni eksiksiz saymak; dinamik SQL, stored procedure'lar ve manuel yüklemeler sıkça gözden kaçar.

## Örnek
Girdi: "Finans panosundaki 'net gelir' nereden geliyor? Pano sorgusu ve mart SQL'i ekte."

Çıktıdan bir bölüm:
- Adım 3: stg_orders → fct_revenue, günlük toplama; net_revenue = sum(gross_amount − discount − refund), status <> 'cancelled', günlük kurla EUR'ya çevrilir. Koddan doğrulandı.
- Adım 5: fct_revenue → finans panosu, region ≠ 'internal' filtresi. Koddan doğrulandı.
- Adım 1: ERP → landing, gece çekimi `[ÇIKARIM: iş adından]` — ERP entegrasyon sahibiyle teyit et.
