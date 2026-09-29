---
name: service-decomposition
description: "İş yetkinliklerini, sınırlı bağlamları, veri sahipliğini, değişim ve ölçekleme etkenlerini ve ekip yapısını birleştirerek bir sistemi veya monoliti servis ya da modül sınırlarına ayrıştırır; her adayı bağımlılık, geveze iletişim (chattiness) ve dağıtık işlem riski açısından değerlendirir ve servisler gerekçelendirilemiyorsa modüler monolit dahil bir ayrıntı düzeyi önerir. Bir monolit bölünürken, yeni bir servis yapısı tasarlanırken veya mevcut servislerin çok ince ya da çok kaba olup olmadığı incelenirken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: software-architect
  area: domain
  title: "Servislere ayrıştırma"
  related: "bounded-context-map, event-storming, migration-strategy, team-topology, database-schema-design"
  prompt: "400 bin satırlık sigorta monolitimizi servislere bölmek istiyoruz; poliçe, hasar, faturalama ve müşteri için sınırları ve veri sahipliğini bulmamıza yardım et."
---

# Servislere Ayrıştırma

## Amaç
Ekiplerin sistemin parçalarını bağımsız olarak değiştirip dağıtabileceği ve ölçekleyebileceği, veri sahipliği net servis veya modül sınırlarını bulmak; bunu yaparken dağıtık monolitten kaçınmak.

## Ne zaman kullanılır
- Bir monolit bölünürken ya da sıfırdan bir sistem için servis yapısı gerektiğinde.
- Servisler çoğu sürümde birlikte değişiyor, birbirini sık sık çağırıyor veya tabloları paylaşıyorsa.
- Ekip mikroservisler ile modüler monolit arasında karar vermek zorundaysa.

## Ne zaman kullanılmaz
- Alanın sınırları ve dili henüz anlaşılmamışsa önce `event-storming` ve `bounded-context-map` kullanılır.
- Asıl soru eski yapıdan yenisine geçişin sırası ve riskiyse `migration-strategy` kullanılır.
- Yalnızca tek bir servisin iç yapısı sorgulanıyorsa `technical-design-doc` kullanılır.

## Girdiler
Zorunlu:
- Sistemin yetkinliklerinin veya modüllerinin ve ana iş akışlarının tanımı.

İsteğe bağlı:
- Sınırlı bağlam haritası, veri modeli veya tablo listesi, değişiklik geçmişi (hangi modüller birlikte değişiyor), fonksiyon bazında yük profili.
- Ekip yapısı ve büyüklüğü, dağıtım ve operasyon olgunluğu (CI/CD, gözlemlenebilirlik, nöbet).

Yalnızca sistem adı verilmişse ana yetkinliklerini ve akışlarını sor. Bilinmeyen etkenleri `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Ayrıştırma etkenlerini listele ve kullanıcıyla ağırlıklandır: bağımsız dağıtılabilirlik, ekip özerkliği, farklı ölçekleme veya erişilebilirlik ihtiyaçları, güvenlik ya da uyum izolasyonu, teknoloji çeşitliliği. Hiçbiri güçlü değilse modüler monolit öner.
2. Teknik katmanlardan veya varlıklardan değil, sınırlı bağlamlardan ya da iş yetkinliklerinden başla; bir bağlam, bir servis için varsayılan üst sınırdır.
3. Veri sahipliğini ata: her varlığın veya tablonun tam olarak bir sahip aday servisi olur; diğer servisler API, olay veya çoğaltılmış okuma modelleri üzerinden okur.
4. Değişim bağımlılığını kanıt olarak kullan: iş öğelerinin çoğunda birlikte değişen modüller bir arada durmalıdır `[geçmiş yoksa VARSAYIM]`.
5. Her ana akış için adaylar arası çağrıları izle; senkron atlama (hop) sayısını ve servisler arası işlemleri say. Kullanıcıya dönük bir yolda ikiden fazla senkron atlama veya zorunlu servisler arası ACID işlemi sınır kokusudur.
6. Bütünlüğü ve boyutu kontrol et: bir aday tek bir ekip tarafından sahiplenilebilmeli ve diğerleri olmadan anlamlı olmalıdır; tek başına iş göremeyen adayları (nano servisler) birleştir.
7. Sık değişen kısımları kararlı olanlardan ayır; farklı fonksiyonel olmayan ihtiyaçları olan bileşenleri izole et (ör. yüksek yüklü fiyatlama motoru, PCI kapsamındaki ödeme bileşeni).
8. Her adayı bir tabloda değerlendir: sorumluluk, sahip olunan veri, bağımlılıklar, senkron/asenkron etkileşimler, ekip, ölçekleme profili, riskler.
9. Önerilen servis sayısı için operasyonel hazırlığı kontrol et: pipeline'lar, gözlemlenebilirlik, nöbet ve platform kapasitesi. Olgunluk düşükse sayıyı azalt veya aşamalandır.
10. Hedef ayrıştırmayı gerekçesi, reddedilen alternatifler ve ilk ayrılacak adayla (yüksek değer, düşük bağımlılık) birlikte öner. Çıkarımları etiketle.
11. Hedef devam ediyorsa ayırma yolu için `migration-strategy`, sahiplik için `team-topology` veya ayrıntı düzeyi kararı için `adr` öner.

## Çıktı formatı
```markdown
# Servis Ayrıştırması: <sistem>

## Etkenler
| Etken | Ağırlık (Y/O/D) | Kanıt |
|---|---|---|

## Aday Servisler / Modüller
| Aday | Sorumluluk | Sahip olunan veri | Bağımlılıklar (senkron/asenkron) | Ekip | Ölçekleme / NFR profili | Riskler |
|---|---|---|---|---|---|---|

## Akış Kontrolü
| Akış | Atlama (senkron) | Servisler arası yazma | Değerlendirme |
|---|---|---|---|

## Veri Sahipliği
- <varlık/tablo> → <sahip>; tüketiciler <API | olaylar | okuma modeli> ile okur

## Öneri
- Hedef: <mikroservisler | modüler monolit | hibrit> — çünkü ...
- Reddedilen alternatifler: ...
- İlk ayrılacak: <aday> — çünkü ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her varlığın tam olarak bir sahip adayı var; yazılabilir paylaşılan tablo kalmadı.
- [ ] Sınırlar teknik katmanlara değil yetkinliklere veya bağlamlara göre çizilmiş.
- [ ] Hiçbir ana akış servisler arası ACID işlemi gerektirmiyor; istisnalar için saga veya birleştirme var.
- [ ] Her aday tek bir ekip tarafından sahiplenilebilir ve tek başına anlamlı.
- [ ] Önerilen sayı için operasyonel hazırlık ele alınmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Katmana göre bölmek (arayüz servisi, iş servisi, veri servisi); her değişiklik hepsinden geçmek zorunda kalır.
- Varlık başına bir servis (Müşteri servisi, Adres servisi); geveze CRUD çağrıları ve dağıtık monolit üretir.
- "Şimdilik" paylaşılan veritabanını korumak; bölünmenin kaldırmak istediği bağımlılığı olduğu gibi bırakır.

## Örnek
Girdi: "Sigorta monoliti: poliçe, hasar, faturalama, müşteri; hasar ve poliçe çoğu sürümde birlikte değişiyor."

Çıktıdan bir bölüm:
- Etkenler: hasar mevsimsel ölçekleme istiyor (Y); faturalama PCI-DSS kapsam izolasyonu gerektiriyor (Y); ekip özerkliği (O).
- Adaylar: Poliçe Yönetimi, Hasar, Faturalama, Taraf/Müşteri.
- Akış kontrolü: "Hasar bildir" teminatı Poliçe'ye karşı senkron doğrular (1 atlama): kabul edilebilir. Hasarın poliçe tablolarını doğrudan okuması: "Poliçe Değişti" olaylarıyla beslenen bir poliçe okuma modeline taşınmalı.
- `[VARSAYIM]` Hasar ile poliçe arasındaki değişim bağımlılığı ortak teminat kurallarından kaynaklanıyor; teminat açıkça modellenene kadar ikisini tek modülde tutmayı değerlendir.
- İlk ayrılacak: Faturalama — ayrı uyum kapsamı, az sayıda gelen bağımlılık.
