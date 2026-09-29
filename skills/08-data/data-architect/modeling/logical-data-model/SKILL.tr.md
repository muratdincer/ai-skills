---
description: "Kavramsal modeli veya gereksinimleri; varlıklar, nitelikler, değer alanları, birincil/alternatif/yabancı anahtarlar, kısıtlar ve tarihçe yönetimi içeren, veritabanı ürününden bağımsız normalize bir mantıksal veri modeline dönüştürür. Fiziksel şema tasarımına hazırlanırken, gereksinimleri veriyle doğrularken ya da ERD, 3NF model veya nitelik düzeyinde model istendiğinde kullanılır."
related: "conceptual-data-model, database-schema-design, data-requirements, business-rules-catalog, data-classification"
prompt: "Hasar alanı için bu kavramsal modelden ve ekteki alan listesinden 3NF mantıksal veri modeli çıkar."
---

# Mantıksal Veri Modeli

## Amaç
Hangi verinin tutulduğunu nitelik düzeyinde, bütünlüğü güvenceye alan anahtar ve kurallarla kesin olarak tanımlamak. Böylece fiziksel tasarım, entegrasyon eşlemeleri ve kalite kuralları işi yeniden yorumlamadan türetilebilir.

## Ne zaman kullanılır
- Kavramsal model hazır ve sırada uygulama veya entegrasyon tasarımı varsa.
- Gereksinim, ekran veya raporlar eksik ya da çelişen veri açısından kontrol edilecekse.
- Mevcut bir şema temiz ve incelenebilir bir modele tersine mühendislikle çevrilecekse.

## Ne zaman kullanılmaz
- İş terminolojisi ve kapsam henüz netleşmediyse önce `conceptual-data-model` kullanılır.
- Motora özel tablo, indeks, bölümlendirme ve tipler gerekiyorsa `database-schema-design` kullanılır.
- Model analitik yıldız şema içinse `dimensional-model` kullanılır.

## Girdiler
Zorunlu:
- Kapsam için kavramsal model veya varlık listesi ve nitelik kaynakları (gereksinimler, alan listeleri, ekranlar, mevcut şemalar).

İsteğe bağlı:
- İsimlendirme standartları, değer alanı (veri tipi sınıfı) kataloğu, kurumsal referans veriler.
- İş kuralları kataloğu, hacimler, yasal saklama ve gizlilik kısıtları.

Varlık listesi ve nitelik kaynağı yoksa iste.

## Süreç
1. Varlık ve ilişkileri kavramsal modelden taşı; iş anlamı taşıyan M:N ilişkileri ilişkilendirme varlıklarına çevir.
2. Nitelikleri, kimliğini tanımladıkları varlığa ata; saklanan bir olgu değilse türetilmiş veya yalnızca rapora ait değerleri reddet (türetmeleri ayrıca işaretle).
3. Nitelik değer alanlarını tanımla (tanımlayıcı, kod, ad, tutar+para birimi, miktar+birim, tarih, saat dilimli zaman damgası, bayrak, serbest metin); uzunluk/hassasiyet ve izinli değerlerle.
4. Doğal/iş anahtarlarını ve alternatif anahtarları belirle; vekil anahtarı yalnızca mantıksal kolaylık olarak öner, hiçbir zaman beyan edilmiş iş anahtarının yerine koyma.
5. 3NF'ye (maliyeti düşükse BCNF'ye) normalize et: tekrarlayan grupları, kısmi ve geçişli bağımlılıkları kaldır. Bilinçli denormalizasyonu gerekçesiyle belgele.
6. Uygun yerde örüntü uygula: party-role, üst tip/alt tip (dışlayıcı/kapsayıcı, tam/eksik belirt), referans/kod tabloları, hiyerarşiler (komşuluk listesi veya köprü tablo).
7. Her varlık için zaman yönetimine karar ver: yalnızca güncel, geçerlilik tarihli (valid from/to), bitemporal (geçerlilik + işlem zamanı) veya olay kaydı. Her seçimi belirtilmiş bir iş veya denetim ihtiyacına bağla.
8. Referans bütünlüğünü zorunluluk ve silme davranışı niyetiyle (kısıtla, zincirleme, mantıksal silme), iş kısıtlarını (teklik, aralık, nitelikler arası kurallar) tanımla.
9. Nitelikleri hassasiyetle (kişisel, özel nitelikli, gizli) etiketle; maskeleme veya veri minimizasyonu adaylarını işaretle.
10. Her niteliği kaynak gereksinimine veya alanına izle; niteliği olmayan gereksinimleri ve gereksinimi olmayan nitelikleri listele.
11. Açık konuları ve varsayımları kaydet.
12. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa sonraki beceriyi öner: fiziksel tasarım için `database-schema-design` veya kişisel veri taşıyan nitelikler için `data-classification`.

## Çıktı formatı
```markdown
# Mantıksal Veri Modeli: <kapsam> (v<x>)
## Diyagram
<crow's foot gösterimli, diagram-as-code ERD>

## Varlık: <Ad>
Tanım: <...> | İş anahtarı: <nitelikler> | Zaman: <güncel / geçerlilik tarihli / bitemporal / olay>
| Nitelik | Değer alanı | Boş olabilir mi? | Anahtar | İzinli değer / kural | Hassasiyet | Kaynak |
|---|---|---|---|---|---|---|

## İlişkiler ve Bütünlük
| Ebeveyn | Çocuk | Kardinalite | FK | Silmede | Kural |
|---|---|---|---|---|---|

## Denormalizasyon ve Örüntü Kararları
- <karar> — <gerekçe>

## İzlenebilirlik Boşlukları
- Niteliği olmayan gereksinimler: ...
- Gereksinimi olmayan nitelikler: ...

## Açık Sorular / Varsayımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her varlığın yalnızca vekil anahtar değil, beyan edilmiş bir iş anahtarı var.
- [ ] Bilinçli olarak belgelenmedikçe geçişli veya kısmi bağımlılık kalmadı.
- [ ] Tutarlar para birimiyle, miktarlar birimle birlikte; zaman damgalarının saat dilimi anlamı belirtilmiş.
- [ ] Zaman yönetimi her varlık için kararlaştırılmış ve gerekçelendirilmiş.
- [ ] Hassas nitelikler etiketli.
- [ ] Her nitelik bir kaynağa izlenebiliyor; boşluklar listelenmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Modelleme kararlarından kaçmak için genel EAV "nitelik/değer" tabloları. Bilinen nitelikleri modelle; EAV'yi gerçekten kullanıcı tanımlı uzantılarla sınırla.
- Belirsiz kardinaliteyi gizlemek için boş geçilebilir yabancı anahtar. Kuralı netleştir ya da açık soru olarak kaydet.
- Denetim tarihçe isterken durumu yalnızca güncel değer olarak tutmak. Zaman ihtiyacını açıkça kararlaştır.

## Örnek
Girdi: "Poliçenin sigorta ettireni, sigortalıları, limitli teminatları var; hasarlar bir poliçe ve teminata bağlı."

Çıktıdan bir bölüm:
- Teminat varlığı: iş anahtarı (Poliçe No, Teminat Kodu, Geçerlilik Başlangıcı); Zaman: zeyillerde limitler değiştiği için geçerlilik tarihli.
- Hasar → Teminat: zorunlu, N:1; silmede kısıtla.
- Sigortalı.TC Kimlik No: değer alanı tanımlayıcı, hassasiyet kişisel, hasar işlemleri dışında maskele.
- Açık soru: Bir hasar iki teminatı kapsayabilir mi? Evetse Hasar Teminatı ilişkilendirme varlığı eklenir.
