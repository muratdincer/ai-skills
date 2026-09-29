---
description: "Temel iş varlıklarını, tanımlarını ve aralarındaki ilişkileri teknolojiden bağımsız olarak iş dilinde ifade eden kavramsal veri modelini oluşturur. Yeni bir alan, platform veya entegrasyon başlarken, paydaşlar arasında ortak terminoloji kurulurken ya da varlık haritası, konu alanı modeli veya iş nesnesi modeli istendiğinde kullanılır."
related: "logical-data-model, glossary-builder, bounded-context-map, event-storming, data-requirements"
prompt: "Bu çalıştay notlarından B2B siparişten tahsilata alanımız için kavramsal veri modeli çıkar."
---

# Kavramsal Veri Modeli

## Amaç
İşin neyi yönettiğine dair ortak ve teknolojiden bağımsız bir resim kurmak: varlıklar, her birinin anlamı ve birbirleriyle ilişkisi. Mantıksal modeller, entegrasyon sözleşmeleri, yönetişim sahiplikleri ve sözlük bu modele dayanır.

## Ne zaman kullanılır
- Yeni bir alan, veri ürünü veya platform kapsamlanırken terimler tutarsız kullanılıyorsa.
- İki sistem veya ekip entegre edilecek ve aynı şeye farklı adlar veriyorlarsa.
- Ana veri, yönetişim veya data mesh girişimi konu alanlarına ve sahiplere ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- Nitelikler, anahtarlar ve normalizasyon gerekiyorsa `logical-data-model` kullanılır.
- Model olgu ve boyutlarla analitik sorgulama içinse `dimensional-model` kullanılır.
- İhtiyaç veri değil servis/alan sınırı haritasıysa `bounded-context-map` kullanılır.

## Girdiler
Zorunlu:
- Alan ve kapsamı (kapsanan süreçler veya yetkinlikler) ile eldeki kaynak materyal: çalıştay notları, süreç tanımları, gereksinimler, mevcut ekran veya raporlar.

İsteğe bağlı:
- Mevcut sözlük, kurumsal veri modeli veya konu alanı sınıflandırması.
- Bilinen kayıt sistemleri (system of record) ve veri sahipleri.
- Varlık kapsamını etkileyen mevzuat (KVKK/GDPR, sektör kuralları).

Kapsam yoksa sor; sınırı olmayan model anlamsızdır.

## Süreç
1. Sınırı belirle: kapsam içi ve dışı iş süreçlerini/yetkinlikleri listele.
2. Kaynaklardaki isimlerden aday varlıkları çıkar; nitelikleri, ekran gibi davranan rolleri, raporları ve sistem adlarını ele.
3. Eş ve sesteş anlamlıları çöz: her kavrama tek ad ver, diğer adları kaydet; farklı bağlamlarda iki şey ifade eden terimi böl (ör. ödeyen olarak "Müşteri" ile teslim alan olarak "Müşteri").
4. Her varlık için kimliği tanımlayan tek cümlelik iş tanımı yaz: iki örneği aynı kılan nedir?
5. Varlıkları sınıflandır: taraf/rol, ürün/kaynak, olay/işlem, anlaşma, lokasyon, referans/sınıflandırma. Ana veri adaylarını işaretle.
6. İlişkileri iki yönde iş fiilleriyle, kardinalite ve zorunlulukla (1:1, 1:N, M:N; zorunlu/isteğe bağlı) tanımla. İlişkinin kendisi iş anlamı taşımıyorsa M:N'yi bu seviyede bırak; taşıyorsa ayrı varlık olarak adlandır.
7. Aynı taraf birden çok rol oynuyorsa rolleri açıkça modelle (party-role örüntüsü); kişi/kurumları rol başına çoğaltma.
8. Varlıkları konu alanlarına grupla ve her konu alanı için iş sahibini, verilmediyse `[VARSAYIM]` olarak öner.
9. İşin önem verdiği zaman ve tarihçe anlamını (geçerlilik tarihleri, sürümler, yaşam döngüsü durumları) tasarlamadan not et.
10. Kişisel ve özel nitelikli veri içeren varlıkları sonraki sınıflandırma için işaretle.
11. Tanımlardaki açık soruları ve çelişkileri kaydet; sessizce birini seçme.
12. Modeli diagram-as-code bloğu ve varlık kataloğu olarak üret.
13. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa sonraki beceriyi öner: nitelik ve anahtar eklemek için `logical-data-model` veya iş terimlerini resmileştirmek için `glossary-builder`.

## Çıktı formatı
```markdown
# Kavramsal Veri Modeli: <alan>
Kapsam: <içi> | Kapsam dışı: <dışı> | Sürüm/tarih: <...>

## Diyagram
~~~mermaid
erDiagram
  MUSTERI ||--o{ SIPARIS : verir
~~~

## Varlık Kataloğu
| Varlık | Tanım (kimlik) | Tür | Diğer adlar | Konu alanı | Sahip | Kişisel veri |
|---|---|---|---|---|---|---|

## İlişkiler
| Kaynak | Fiil ifadesi | Hedef | Kardinalite | İş kuralı / not |
|---|---|---|---|---|

## Yaşam Döngüsü ve Tarihçe Notları
- <varlık>: <işin ihtiyaç duyduğu durumlar / geçerlilik tarihleri>

## Terminoloji Kararları
- <terim> <...> anlamına gelir; <...> ile karıştırılmamalı

## Açık Sorular
1. <soru> — <etki> — <kim karar verir>
```

## Kalite kontrol listesi
- [ ] Teknik öğe yok: vekil anahtar, veri tipi, tablo veya sistem adı varlık olarak yer almıyor.
- [ ] Her varlığın döngüsel olmayan, kimliği tanımlayan bir tanımı var.
- [ ] Her ilişki iki yönde kardinaliteyle iş cümlesi olarak okunuyor.
- [ ] Eş anlamlılar birleştirildi, sesteşler ayrıldı, diğer adlar kaydedildi.
- [ ] Kullanıcının vermediği sahipler `[VARSAYIM]` olarak işaretli.
- [ ] Kişisel veri taşıyan varlıklar işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Mevcut sistemin tablolarını modelleyip kavramsal model demek. Önce iş dilinden türet, sonra sistemlerle karşılaştır.
- Her taraf rolü için tek dev "Müşteri" varlığı. Kimlik ile rolü ayırmak için party-role kullan.
- Aşırı ayrıntı: çalıştay kitlesine 60 varlık. İşin adlandırıp savunabileceği varlıklarla sınırlı kal, alan başına genellikle 10-30.

## Örnek
Girdi: "Satış müşterilerden sipariş alıyor; faturalar genel müdürlüğe, teslimatlar şubelere gidiyor."

Çıktıdan bir bölüm:
- Taraf (kurum) Sipariş Veren, Fatura Alan, Teslim Alan rollerini oynar; `[VARSAYIM]` şube, "bağlıdır" ilişkisiyle genel müdürlüğüne bağlı bir Taraftır.
- İlişki: Sipariş tam olarak bir Fatura Alan role "faturalanır"; bir Fatura Alan rolü sıfır veya çok Sipariş için "faturalanır".
- Açık soru: Bir sipariş birden çok şubeye teslim edilebilir mi? — Sipariş/Teslimat kardinalitesini değiştirir — Satış operasyonları.
