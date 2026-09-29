---
name: epic-breakdown
description: "Bir epic'i belirli bir persona, gerçek bir sonuç ve ilk dilim olarak uçtan uca bir iskelet (walking skeleton) içeren, değer, risk ve bağımlılığa göre sıralanmış ince, dikey ve bağımsız değer üreten hikayelere böler. Bir epic, girişim veya büyük özellik backlog maddelerine dönüşecekse, hikayeler katman (UI/API/DB) ya da teknik görev olarak çıkıyorsa veya ekip \"bu epic'i nasıl bölelim\" diye soruyorsa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: definition
  title: "Epic'i hikayelere bölme"
  related: "story-splitting, user-story, acceptance-criteria, story-mapping, invest-check"
  prompt: "Bu epic'i hikayelere böl: \"KOBİ müşterileri için müşteri portalında self-servis sözleşme yenileme\"."
---

# Epic'i Hikayelere Bölme

## Amaç
Bir epic'i, her biri adı belli bir kullanıcıya gözlemlenebilir değer sunan ince dikey dilimlere dönüştürmek. Böylece ekip her şeyi sonda birleştirmek yerine erken teslim eder, öğrenir ve sırayı yeniden düzenleyebilir.

## Ne zaman kullanılır
- Onaylanmış bir epic veya girişim backlog'a üzerinde çalışılabilir maddeler olarak girecekse.
- Mevcut bölümleme yataysa (önyüz hikayesi, arka uç hikayesi, veritabanı hikayesi) ya da çoğunlukla teknik görevlerden oluşuyorsa.
- Bir sürüm için uçtan uca yolu erkenden kanıtlayan ilk dilim gerekiyorsa.

## Ne zaman kullanılmaz
- Tek bir hikaye çok büyükse ve yalnızca bölünmesi gerekiyorsa `story-splitting` kullanılır.
- Birden çok epic için tüm kullanıcı yolculuğu ve sürüm dilimleri çıkarılacaksa `story-mapping` kullanılır.
- Tek tek hikayelerin ayrıntılı kabul koşulları yazılacaksa `acceptance-criteria` kullanılır.

## Girdiler
Zorunlu:
- Epic: hedefi, hedef kullanıcıları ve etkilemesi beklenen sonuç (ya da bunları içeren bir PRD/özellik özeti).

İsteğe bağlı, kaliteyi artırır:
- İş kuralları, akışlar, ekranlar, entegrasyonlar, fonksiyonel olmayan gereksinimler (NFR), bilinen kısıtlar.
- Ekibin hikaye formatı ve boyut kuralları; ilgili mevcut hikayeler.

Epic'in kullanıcıları veya hedefi yoksa sor (en fazla 3 odaklı soru). İş kuralı uydurma; bunları açık soru olarak listele.

## Süreç
1. Epic'i sonuç + birincil persona + kapsam sınırı olarak yeniden ifade et. Personayı somut adlandır (ör. "KOBİ hesap yöneticisi"), asla "kullanıcı" deme; persona verilmemişse bir öneri yap ve `[VARSAYIM]` olarak işaretle.
2. Epic'in mümkün kıldığı uçtan uca akışı (tetikleyici, adımlar, tamamlanma) yürü; her adımda dokunulan iş kurallarını, veriyi ve entegrasyonları not et.
3. Uçtan uca iskeleti tanımla: gerçek bir personanın tamamlayabileceği, her adımdan geçen en ince yol; en basit kural, tek veri çeşidi ve mutlu yol.
4. İskeletten dilimleri şu bölme eksenleriyle büyüt: iş akışı adımları, kural çeşitleri, veri çeşitleri, arayüz/kanallar, hata ve uç durum yolları, performans/kalite seviyeleri. Her dilim gerekli tüm katmanları kesmeli.
5. Her hikayeyi "<somut persona> olarak, <yetenek> istiyorum, böylece <gerçek sonuç>" biçiminde yaz. "Böylece" kısmı isteği tekrar etmez, bir fayda söyler.
6. Teknik işi ayır: saf teknik görevler (kuyruk kurmak, şema taşımak) kullanıcı hikayesi değildir; bir hikayenin altında görev ya da gerekçesi yazılmış bir enabler olur. Tahmini engelleyecek kadar büyük bilinmeyenler süre sınırlı spike'a dönüşür.
7. Her hikaye için Given/When/Then biçiminde 2-4 kabul senaryosu taslağı çıkar; her senaryoda tek When ve tek Then olsun. Bir hikaye çok sayıda When veya Then gerektiriyorsa böl.
8. Her hikayeyi INVEST'e göre kontrol et; bağımlılıkları açıkça işaretle ve bağlamak yerine yeniden sıralamayı veya bölmeyi tercih et.
9. Hikayeleri sırala: önce iskelet, sonra en yüksek değer veya en çok risk azaltan, zorunlu bağımlılıklara uyarak. Birlikte yayınlanabilir artım oluşturan hikayeleri işaretle.
10. Kapsamayı kontrol et: 2. adımdaki her kural, veri çeşidi ve NFR bir hikayeye, açık bir "kapsam dışı"na veya açık soruya düşmeli. Çıkarım yapılan kuralları `[VARSAYIM]` olarak etiketle.
11. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: hikayeleri detaylandırmak için `acceptance-criteria`, hâlâ büyük kalan maddeler için `story-splitting`, epic'ler arası sürüm planı için `story-mapping`.

## Çıktı formatı
```markdown
# Epic Bölümlemesi: <epic adı>
Sonuç: <etkilenecek metrik/davranış> · Birincil persona: <persona> · Sınır: <içeride / dışarıda>

## Uçtan Uca Akış
<adım 1> → <adım 2> → ... (adım başına kurallar / veri / entegrasyonlar)

## Hikayeler
| # | Hikaye (olarak / istiyorum / böylece) | Dilim türü | Ana senaryolar | Bağımlı olduğu | Boyut sinyali |
|---|---|---|---|---|---|
| 1 | <uçtan uca iskelet> | İskelet | ... | – | S/M/L veya [TBD] |

## Enabler'lar, Görevler ve Spike'lar
| Madde | Tür | Gerekçe / bağlı hikaye | Süre sınırı |
|---|---|---|---|

## Önerilen Sıra ve Sürüm Artımları
- Artım 1: #1, #2 – <kullanıcı artık ne yapabiliyor>

## Kapsama ve Kapsam Dışı
- Karşılanan kurallar/NFR'ler: ... · Açıkça kapsam dışı: ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her hikaye somut bir persona ve gerçek bir sonucu anlatan bir "böylece" içeriyor.
- [ ] Her hikaye dikey (persona tarafından kullanılabilir); hiçbiri bir katman ya da saf teknik görev değil.
- [ ] İlk hikaye uçtan uca akışı tamamlayan bir iskelet.
- [ ] Her senaryoda tek When ve tek Then var; birden çok davranış içeren hikayeler bölündü.
- [ ] Akıştaki her kural, çeşit ve NFR bir hikayeye, kapsam dışına veya açık soruya eşlendi.
- [ ] Boyutlar ekipten geliyor ya da `[TBD]`; hiçbir şey uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
| Hata | Düzeltme |
|---|---|
| Katmana göre bölmek (UI, API, DB) | Her dilim katmanları kessin diye iş akışı, kural veya veriye göre böl |
| "Kullanıcı olarak..." | Davranışı değişen personayı adlandır |
| "böylece yenileyebilirim" (isteği tekrarlar) | Faydayı yaz: "böylece hizmet kesintiye uğramaz" |
| İlk dilimi süslemek | İskeleti mutlu yol, tek kural, tek çeşitle sınırla |

## Örnek
Girdi: "KOBİ müşterileri için müşteri portalında self-servis sözleşme yenileme."

Zayıf: "Kullanıcı olarak yenileme sayfası istiyorum, böylece yenileyebilirim." / "Yenileme API'si yaz."

Güçlü, bir bölüm:
| # | Hikaye | Dilim türü |
|---|---|---|
| 1 | KOBİ hesap yöneticisi olarak mevcut sözleşmemi tek onayla aynen yenilemek istiyorum, böylece satışı aramadan hizmet devam eder | İskelet |
| 2 | KOBİ hesap yöneticisi olarak yenileme sırasında kullanıcı sayısını değiştirmek istiyorum, böylece yalnızca aktif çalışanlar için öderim | Veri çeşidi |
| 3 | KOBİ hesap yöneticisi olarak vadesi geçmiş fatura yüzünden yenilemenin neden engellendiğini görmek istiyorum, böylece sorunu kendim çözebilirim | Kural / hata yolu |
- Enabler: sözleşme bitiş tarihlerini faturalama sisteminden portala açmak (#1'e bağlı).
- Açık soru: Yenilemede fiyat planı değiştirilebilir mi, yoksa yalnızca miktarlar mı?
