---
name: positioning-statement
description: "Bir ürün veya özellik için belirli bir hedef segmente, gerçek bir alternatife ve kanıtlanabilir bir farka dayanan konumlandırma cümlesini Kimin için/Kim/Nedir/Ne yapar/Rakiplerden farkı formatında yazar; ardından kanıt noktalarını ve mesaj sınırlarını çıkarır. Bir ürün veya büyük bir özellik lansmana hazırlanırken, satış ve pazarlama ürünü farklı anlatırken ya da \"bunu nasıl konumlandıralım\", \"bizi farklı kılan ne\" diye sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: launch
  title: "Konumlandırma cümlesi"
  related: "value-proposition-canvas, competitor-analysis, persona, go-to-market-plan, elevator-pitch"
  prompt: "Orta ölçekli üreticilerin finans ekiplerine yönelik yeni fatura eşleştirme modülümüz için konumlandırma cümlesi yaz."
---

# Konumlandırma Cümlesi

## Amaç
Ürünün kimin için olduğunu, hangi problemi çözdüğünü, hangi kategoride rekabet ettiğini ve müşterinin aksi halde seçeceği alternatiften neden daha iyi olduğunu anlatan kısa ve sınanabilir bir cümle üretmek. Böylece her lansman mesajı, satış konuşması ve yol haritası tartışması aynı iddiadan başlar.

## Ne zaman kullanılır
- Yeni bir ürün, modül veya büyük bir özellik lansmana hazırlanırken.
- Satış, pazarlama ve ürün ekipleri teklifi farklı anlatıyor ve bu karışıklık yüzünden fırsatlar kaybediliyorsa.
- Ürün yeni bir segment için ya da bir rakip hamlesinden sonra yeniden konumlandırılırken.

## Ne zaman kullanılmaz
- Müşterinin işleri, acıları ve kazanımları henüz anlaşılmadıysa önce `value-proposition-canvas` veya `jobs-to-be-done` kullanılır.
- İhtiyaç tam lansman planıysa (kanallar, zamanlama, hazırlık) `go-to-market-plan` kullanılır.
- 30 saniyelik sözlü bir tanıtım gerekiyorsa bu cümleyi girdi olarak vererek `elevator-pitch` kullanılır.

## Girdiler
Zorunlu:
- Ürün veya özellik ve ne yaptığı.
- Hedeflenen müşteri veya segment (kaba da olsa).

İsteğe bağlı, kaliteyi artırır:
- Müşteri araştırması, kazanma/kaybetme notları, yorumlar, destek temaları.
- Başlıca rakipler veya mevcut geçici çözüm (tablolar, elle yapılan iş, hiçbir şey yapmamak).
- Kanıtlar: metrikler, müşteri sonuçları, sertifikalar, kıyaslamalar.
- Marka veya mesaj kılavuzları.

Ürün veya hedef segment eksikse sor. Alternatif bilinmiyorsa adayları `[VARSAYIM]` olarak öner ve açık soru olarak listele.

## Süreç
1. Hedefi daralt: demografi ya da "herkes" değil; rol, bağlam ve tetikleyici durumla tanımlanan tek bir segment seç (ör. "ay sonu kapanışını üçlü eşleştirmeyle yapan orta ölçekli üreticilerin finans ekipleri"). Birden fazla segment varsa her biri için ayrı cümle yaz.
2. İhtiyacı müşterinin diliyle yaz: segmentin sık yaşadığı ve maliyetli olan problem ya da iş. Girdilerdeki kanıtları kullan; çıkarımları `[VARSAYIM]` olarak işaretle.
3. Müşterinin zaten tanıdığı referans çerçevesini (pazar kategorisini) seç. Kategori beklentiyi ve rakip kümesini belirlediği için bilinçli seç; yeni bir kategori yaratıyorsan bunu ve nedenini not et.
4. Müşterinin bunun yerine kullanacağı gerçek alternatifi belirle: adı konmuş bir rakip, komşu bir araç, kurum içi geliştirme, elle yapılan iş veya hiçbir şey yapmamak.
5. Aday farklılaştırıcıları listele ve yalnızca segment için önemli olan, o alternatife göre benzersiz ya da açıkça daha iyi olan ve kanıtlanabilen farkları tut. Denk (parity) özellikleri çıkar.
6. Tutulan her farka kanıt noktası ekle. Kanıt yoksa sayı uydurmak yerine `[KANIT GEREKLİ]` olarak işaretle.
7. Cümleyi kur: <hedef> için, <ihtiyaç> yaşayanlara, <ürün> bir <kategori>dir ve <ana fayda> sağlar. <alternatif>ten farklı olarak ürünümüz <ana fark>.
8. Mesaj sınırlarını türet: üç mesaj ayağı, kullanılacak ve kaçınılacak kelimeler, kanıt olmadan kullanılamayacak iddialar.
9. Stres testi yap: Bir rakip aynı cümleyi imzalayabilir mi? Hedef müşteri kendi problemini tanır mı? Fayda bir özellik değil de bir sonuç mu? Her cevap cümleyi destekleyene kadar düzelt.
10. Varsayımları ve açık soruları listele; nasıl doğrulanacağını öner (müşteri görüşmeleri, mesaj testi, kazanma/kaybetme incelemesi).
11. Hedef devam ediyorsa lansman planı için `go-to-market-plan`, sözlü biçim için `elevator-pitch` veya lansman mesajı için `release-announcement` öner.

## Çıktı formatı
```markdown
# Konumlandırma: <ürün / özellik> — <segment>

## Konumlandırma Cümlesi
Kimin için: <hedef segment>
Kim: <ihtiyaç / problem> yaşayanlar
Nedir: <ürün> bir <pazar kategorisi>
Ne yapar: <ana fayda (sonuç)>
Rakiplerden farkı: <ana alternatif>ten farklı olarak ürünümüz <ana fark>

## Yapı Taşları
| Öğe | İçerik | Kanıt / kaynak |
|---|---|---|
| Hedef | ... | ... |
| İhtiyaç | ... | ... |
| Kategori | ... | ... |
| Ana fayda | ... | ... |
| Alternatif | ... | ... |
| Fark | ... | <kanıt veya [KANIT GEREKLİ]> |

## Mesaj Ayakları
1. <ayak> — kanıt: ...
## Kullanılacak / Kaçınılacak Kelimeler
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
## Doğrulama Planı
```

## Kalite kontrol listesi
- [ ] Hedef, "işletmeler" veya "kullanıcılar" değil, durumu tanımlanmış belirli bir segment.
- [ ] Ana fayda bir özellik listesi değil, müşterinin değer verdiği bir sonuç.
- [ ] Alternatif, geçici çözüm veya hiçbir şey yapmamak dahil, müşterinin gerçekte başvuracağı yol.
- [ ] Bir rakip aynı cümleyi inandırıcı biçimde imzalayamaz.
- [ ] Her farkın bir kanıt noktası var ya da `[KANIT GEREKLİ]` olarak işaretli; uydurulmuş metrik yok.
- [ ] Çıkarımlar etiketli ve varsayımlarda listeleniyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kimseyi kaybetmemek için herkesi hedeflemek. Geniş konumlandırma faydayı sıradanlaştırır; en net kazandığın segmenti seç.
- Üstünlük sıfatlarını ("sınıfının en iyisi", "kesintisiz", "yapay zekâ destekli") fark olarak kullanmak. Bunları belirli ve doğrulanabilir bir farkla değiştir.
- Müşterinin tanımadığı bir kategori seçmek. Tanıdık olmayan kategori, fayda anlaşılmadan önce eğitim gerektirir.

## Örnek
Girdi: "Orta ölçekli üreticilerin finans ekipleri için fatura eşleştirme modülü."

Zayıf: "Verimlilik isteyen işletmeler için FaturaX, finansı kolaylaştıran yenilikçi, yapay zekâ destekli bir çözümdür. Diğerlerinden farklı olarak kullanımı kolaydır."

Güçlü (bölüm): "Her ay sonu tedarikçi faturalarını sipariş ve irsaliyelerle mutabık kılmak için günler kaybeden orta ölçekli üretici finans ekipleri için FaturaX, faturaları otomatik eşleştiren ve yalnızca istisnaları insanlara yönlendiren bir satınalma-ödeme otomasyon modülüdür. Tablo tabanlı eşleştirmeden farklı olarak ürünümüz mal kabul kayıtlarını doğrudan ERP'den okur; böylece uyuşmazlıklar kapanıştan önce ortaya çıkar `[KANIT GEREKLİ: pilottan eşleştirme oranı verisi]`."
