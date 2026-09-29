---
description: "Tedarikçiden bağımsız bir veri platformu mimarisi tasarlar: alım (ingestion), depolama ve işleme katmanları, sunum örüntüleri, yönetişim, güvenlik, işletim modeli ve warehouse, lakehouse, mesh ya da hibrit arasındaki seçim; kararlar gereksinimlere izlenir. Hedef veri platformu tanımlanırken, eski bir veri ambarı modernize edilirken ya da lakehouse, data mesh veya referans veri mimarisi istendiğinde kullanılır."
related: "target-state-architecture, technology-selection, adr, data-contract, cloud-cost-estimate"
prompt: "SAP, MES ve IoT kaynakları, BI ve ML tüketicileri ve küçük bir merkezi veri ekibi olan bir üretici için hedef veri platformu tasarla."
---

# Veri Platformu Tasarlama

## Amaç
Verinin nasıl alınacağı, saklanacağı, işleneceği, yönetileceği ve sunulacağına dair, her büyük kararı gereksinim ve kısıtlarla gerekçelendirilmiş bir hedef mimari üretmek. Böylece teknoloji seçimi, yol haritası ve ekip tasarımı mimariyi yönlendirmez, mimariden türer.

## Ne zaman kullanılır
- Yeni veya hedef durum veri platformu tanımlanacaksa.
- Eski bir veri ambarı ya da parçalı bir veri gölü modernize edilecek veya birleştirilecekse.
- Yönetim lakehouse, data mesh veya hibrit yaklaşımın benimsenip benimsenmeyeceğini ve ne anlama geldiğini soruyorsa.

## Ne zaman kullanılmaz
- Yalnızca adaylar arasından ürün seçilecekse `technology-selection` kullanılır.
- Tek bir veri hattı tanımlanıyorsa `pipeline-spec` kullanılır.
- Yalnızca veri değil tüm kurumsal hedef durum gerekiyorsa `target-state-architecture` kullanılır.

## Girdiler
Zorunlu:
- İş sürücüleri ve ana tüketiciler (BI, operasyonel analitik, ML/YZ, veri paylaşımı, yasal raporlama).
- Kaynak ortamı (sistemler, türleri: OLTP, SaaS, dosyalar, olaylar/IoT) ve kaba hacim/gecikme ihtiyaçları.

İsteğe bağlı:
- Mevcut mimari ve sorunlar, bulut/on-prem kısıtları, veri yerelliği (KVKK/GDPR), ekip büyüklüğü ve yetkinlikleri, bütçe çerçevesi, mevcut sözleşmeler.

Sürücüler veya kaynaklar yoksa sor; aksi halde tasarım seçimlerini `[VARSAYIM]` olarak işaretle.

## Süreç
1. Sürücüleri mimariyi etkileyen gereksinimlere çevir: gecikme sınıfları (batch, micro-batch, streaming), tazelik SLA'ları, eşzamanlılık, saklama, yerellik, erişilebilirlik, maliyet tavanı, self-servis düzeyi.
2. Önce organizasyonel örüntüyü seç: merkezi platform, hub-and-spoke veya alan odaklı (mesh). Mesh, veri ürünlerine sahip olabilecek alan ekipleri gerektirir; yoksa ileride mesh'e geçilebilecek şekilde tasarla.
3. Kaynak sınıfı bazında alım örüntülerini tanımla: OLTP için CDC, SaaS için API/batch çekme, manifest ile dosya iniş alanı, IoT/uygulamalar için olay akışı. Sözleşme ve şema kayıt defteri (schema registry) kullanımını belirt.
4. Depolama katmanlarını net sözleşmelerle tanımla: ham/iniş (değişmez, kaynağa sadık), entegre/temizlenmiş (ortaklaştırılmış, tekilleştirilmiş), küratörlü/sunum (mart'lar, veri ürünleri, öznitelikler). Formatları genel ifadeyle (açık tablo formatı, sütunsal) ve katman bazında sahipliği belirt.
5. Katman bazında işleme stillerini seç: platform içinde ELT, akış işleme ve dönüşüm mantığının nerede yaşadığı (sürümlü, test edilmiş kod).
6. Sunumu tanımla: SQL warehouse/lakehouse uç noktaları, semantik katman ve metrik tanımları, operasyonel kullanım için API/reverse ETL, ML için feature store, dış taraflar için güvenli paylaşım.
7. Kesişen konuları tasarla: katalog ve köken, veri kalitesi ve gözlemlenebilirlik, erişim kontrolü (RBAC/ABAC, satır/sütun güvenliği, maskeleme), şifreleme ve anahtar yönetimi, saklama ve silme, alan bazında maliyet dağıtımı.
8. İşletim modelini tanımla: platform ekibi ve alan ekipleri, veri ürünü sahipliği, sözleşme ve değişiklik süreci, veri olayları için nöbet.
9. Seçenekleri (ör. warehouse merkezli, lakehouse, hibrit) gereksinimlere karşı bir ödünleşim tablosunda değerlendir; kritik seçimleri ADR adayı olarak kaydet.
10. Eski bir platform değiştiriliyorsa geçiş yaklaşımını ve fazlarını belirle (alan/tüketici bazında strangler, paralel koşum, mutabakat).
11. Riskleri, açık soruları ve vazgeçilmezleri listele.

## Çıktı formatı
```markdown
# Veri Platformu Mimarisi: <kurum/kapsam>
## Sürücüler ve Mimariyi Etkileyen Gereksinimler
| Gereksinim | Hedef | Kaynak/varsayım |
|---|---|---|

## Bağlam ve Katman Diyagramı
<diagram-as-code: kaynaklar → alım → ham → entegre → küratörlü → sunum → tüketiciler>

## Katman Tanımları
| Katman | Amaç | Format / saklama | Sahip | Sözleşme/kalite kapısı |
|---|---|---|---|---|

## Alım ve İşleme Örüntüleri
| Kaynak sınıfı | Örüntü | Gecikme | Notlar |
|---|---|---|---|

## Sunum ve Tüketim
- ...

## Yönetişim, Güvenlik ve Gizlilik
- ...

## İşletim Modeli
- ...

## Seçenekler ve Ödünleşimler
| Kriter | Seçenek A | Seçenek B | Seçenek C |
|---|---|---|---|

## Kararlar (ADR adayları)
- ...

## Geçiş Fazları, Riskler ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her katmanın belirtilmiş bir sözleşmesi, sahibi ve kalite kapısı var.
- [ ] Gecikme ve tazelik hedefleri tüketici sınıfı bazında açık.
- [ ] Gizlilik, yerellik, erişim kontrolü ve silme tasarlandı, ertelenmedi.
- [ ] Organizasyonel örüntü ekip yetkinliğiyle uyumlu.
- [ ] Seçenekler özellik listelerine değil gereksinimlere göre karşılaştırıldı; tasarım tedarikçiden bağımsız.
- [ ] Maliyet sürücüleri ve maliyet dağıtımı ele alındı.

## Sık yapılan hatalar
- Önce ürünleri seçip mimariyi onların etrafına çizmek. Yetkinlikleri gereksinimlerden türet, sonra seç.
- Alan sahipliği, finansman veya self-servis platform olmadan data mesh ilan etmek. Ön koşulları adıyla belirt.
- Ham veriyi sözleşmesiz birçok bölgeye kopyalayıp bataklık üretmek. Her katmanın giriş kriteri olmalı.
- Tüketiciler günlük veriye ihtiyaç duyarken her yeri streaming tasarlamak. Gecikmeyi gerçek ihtiyaca göre belirle.

## Örnek
Girdi: "Üretici; SAP ERP + MES + IoT sensörleri; BI ve kestirimci bakım; 5 kişilik veri ekibi; ERP on-prem."

Çıktıdan bir bölüm:
- Örüntü: alanlara hizalı küratörlü bölgelerle merkezi platform; mesh ertelendi `[VARSAYIM: ekip alan sahipliği için çok küçük]`.
- IoT: 30 günlük sıcak saklama ile ham katmana olay akışı; ML öznitelikleri için küratörlü katmanda seyreltilmiş özetler.
- Karar adayı: motor bağımlılığını önlemek için ham/entegre katmanda açık tablo formatı.
