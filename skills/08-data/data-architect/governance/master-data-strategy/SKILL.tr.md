---
description: "Bir veya daha fazla alan (müşteri, ürün, tedarikçi, lokasyon vb.) için ana veri yönetimi yaklaşımını tanımlar: nitelik bazında kayıt sistemi, altın kayıt ve hayatta kalma kuralları, eşleştirme/birleştirme mantığı, uygulama stili, veri sorumluluğu rolleri ve iş akışları, tüketen sistemlere dağıtım. Aynı varlık sistemler arasında tutarsız bulunduğunda, mükerrer kayıtlar operasyona veya raporlamaya zarar verdiğinde ya da bir ana veri veya altın kayıt girişimi kapsamlandırılırken kullanılır."
related: "data-quality-rules, logical-data-model, data-lineage-doc, raci-matrix, data-classification"
prompt: "CRM, ERP ve e-ticaret platformunda bulunan müşteri verisi için bir ana veri yaklaşımı tanımla."
---

# Ana Veri Yönetimi Tanımlama

## Amaç
Temel iş varlıklarının tek, güvenilir ve yönetişimi yapılan bir sürümünü ve bu güveni koruyan kuralları ve rolleri oluşturmak. Böylece operasyon ve analitik, birbiriyle çelişen kopyaları uzlaştırmakla uğraşmaz.

## Ne zaman kullanılır
- Aynı müşteri, ürün veya tedarikçi sistemlerde farklı kimlik ve niteliklerle yer alıyorsa.
- Mükerrer veya çelişen nitelikler operasyonel hatalara (yanlış sevkiyat, çift faturalama) ya da güvenilmez raporlamaya yol açıyorsa.
- Bir altın kayıt, MDM hub'ı veya veri yönetişimi programı kapsamlandırılıyorsa.

## Ne zaman kullanılmaz
- Tek bir veri seti için kontroller yeterliyse `data-quality-rules` kullanılır.
- Yalnızca varlığın yapısı tasarlanıyorsa `logical-data-model` kullanılır.
- Yalnızca verinin sistemler arası akışı belgelenecekse `data-lineage-doc` kullanılır.

## Girdiler
Zorunlu:
- Ana veri alan(lar)ı ve bu veriyi oluşturan veya tutan sistemler.

İsteğe bağlı:
- Sistem bazında nitelik listeleri, bilinen mükerrer oranları, kayıt oluşturan/değiştiren iş süreçleri, sorunlu noktalar, mevzuat gereksinimleri, sahiplik için organizasyon yapısı.

Alanı tutan sistemler bilinmiyorsa iste; onlar olmadan hayatta kalma kuralları tanımlanamaz.

## Süreç
1. Alanı kapsamlandır: varlık tanımı, neyin ana veri, neyin işlem verisi veya referans veri olduğu ve kapsamdaki nitelikler (süreçleri ve raporlamayı yönlendirenlerden başla).
2. Kaynakların envanterini çıkar: her sistem için hangi nitelikleri oluşturduğu, güncellediği veya yalnızca okuduğu, yerel tanımlayıcısı ve bilinen kalitesi.
3. Kayıt sistemini varlık bazında değil nitelik (veya nitelik grubu) bazında ata; farklı sistemler farklı niteliklerin meşru sahibi olabilir.
4. Bir uygulama stili seç ve gerekçelendir: registry (çapraz referans dizini), consolidation (analitik için altın kayıt), coexistence (altın kaydın kaynaklara geri senkronize edilmesi), centralized (kayıt yalnızca hub'da oluşturulur). Müdahalecilik ile kontrol arasındaki dengeyi belirt.
5. Eşleştirmeyi tanımla: blocking anahtarları, normalizasyonlu eşleştirme nitelikleri (büyük/küçük harf, boşluk, harf çevirisi, adres standardizasyonu, telefon formatları), önce deterministik kurallar, sonra otomatik birleştirme, inceleme ve eşleşmeme eşikleriyle olasılıksal puanlama `[TBD, örneklemle kalibre et]`.
6. Nitelik bazında hayatta kalma kurallarını tanımla: kaynak önceliği, en güncel, en dolu, en sık veya veri sorumlusunun belirlediği değer; ayrıca birleştirmeyi geri alma ve kaynak çapraz referanslarını koruma kuralları.
7. Tanımlayıcıları tanımla: global ana kimlik, çapraz referans tablosu ve tüketicilerin yerel kimlikleri nasıl çözeceği.
8. Veri sorumluluğunu tanımla: veri sahibi (hesap verebilir), veri sorumluları (operasyonel), eşleşme incelemesi, istisna kuyrukları, oluşturma/değiştirme talepleri için iş akışları ve çözüm için hizmet seviyeleri.
9. Dağıtımı tanımla: altın kaydın tüketicilere nasıl ulaştığı (olaylar, API'ler, toplu aktarım), gecikme ihtiyaçları ve çelişen yerel düzenlemelerin nasıl ele alındığı.
10. Kalite ve başarı metriklerini tanımla: mükerrer oranı, etiketli örneklem üzerinde eşleşme kesinliği/duyarlılığı, kritik niteliklerin doluluğu, veri sorumluluğu iş birikiminin yaşı; ölçülene kadar başlangıç değerleri `[BİLİNMİYOR]` olur.
11. Gizliliği ele al: alandaki kişisel veriler, açık rıza ve hukuki dayanak, tüm kopyalara iletilen silme talepleri, en aza indirilmiş nitelikler.
12. Riskler ve açık sorularla aşamalı bir yol haritası öner (önce tek alan ve az kaynak). Hedef devam ediyorsa kritik nitelikler için `data-quality-rules`, veri sorumluluğu rolleri için `raci-matrix` veya altın kayıt yapısı için `logical-data-model` öner.

## Çıktı formatı
```markdown
# Ana Veri Stratejisi: <alan>
Stil: <registry/consolidation/coexistence/centralized> — <gerekçe>

## Kapsam ve Tanım
<varlık tanımı, kapsamdaki nitelikler, hariç tutulanlar>

## Kayıt Sistemi Matrisi
| Nitelik grubu | Oluşturulduğu yer | Güncellendiği yer | Kayıt sistemi | Hayatta kalma kuralı |
|---|---|---|---|---|

## Eşleştirme
Blocking: <...> | Normalizasyon: <...> | Kurallar: <deterministik, olasılıksal> | Eşikler: otomatik <...> / inceleme <...>

## Tanımlayıcılar ve Dağıtım
<ana kimlik, çapraz referans, iletim mekanizması, gecikme>

## Veri Sorumluluğu
| Rol | Kim | Sorumluluklar | Hizmet seviyesi |
|---|---|---|---|

## Metrikler
| Metrik | Başlangıç | Hedef |
|---|---|---|

## Gizlilik
- ...

## Yol Haritası, Riskler ve Açık Sorular
- Aşama 1: ...
- [RİSK] ... | [TBD] ...
```

## Kalite kontrol listesi
- [ ] Kayıt sistemi yalnızca varlık bazında değil, nitelik grubu bazında tanımlandı.
- [ ] Uygulama stili kurumun kısıtlarına göre gerekçelendirildi.
- [ ] Eşleşme eşikleri kalibre edildi veya `[TBD]` olarak işaretlendi; birleştirme geri alınabiliyor.
- [ ] Her veri sorumluluğu iş akışının sahibi ve hizmet seviyesi var.
- [ ] Silme ve rıza, kişisel verinin tüm kopyalarına iletiliyor.
- [ ] Başlangıç değerleri ve hedefler uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- MDM'i bir araç satın alımı olarak görmek. Veri sorumluluğu rolleri ve bunlara ayrılmış zaman olmadan altın kayıt bozulur.
- Tüm alanları ve kaynakları kapsayan tek seferde geçiş. Değeri, mükerrer sorunu en acı olan tek alanda kanıtla.
- Agresif otomatik birleştirme. Yanlış birleştirmeler (iki gerçek kişiyi tek kişi yapmak) kaçırılan eşleşmelerden çok daha maliyetlidir; temkinli başla ve incele.

## Örnek
Girdi: "Müşteri verisi CRM, ERP ve e-ticarette duruyor; mükerrer müşteriler çift faturaya yol açıyor."

Çıktıdan bir bölüm:
- Stil: coexistence — faturalama için müşteriyi ERP oluşturmaya devam etmeli; altın kayıt olaylarla kaynaklara geri senkronize edilir.
- Hayatta kalma: fatura adresi ERP'den (kayıt sistemi); e-posta ve pazarlama izni e-ticaretten, en güncel olan kazanır.
- Eşleştirme: normalize posta kodu + soyadı ile blocking; otomatik birleştirme yalnızca vergi numarası birebir eşleştiğinde; bulanık ad/adres puanları veri sorumlusu incelemesine gider.
