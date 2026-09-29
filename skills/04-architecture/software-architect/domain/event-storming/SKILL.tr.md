---
name: event-storming
description: "Genel resim (big picture) veya tasarım düzeyinde bir event storming oturumunu planlar ya da yürütür ve sonucu alan olayları, komutlar, aktörler, politikalar, okuma modelleri, dış sistemler, aggregate'ler ve sıcak noktalardan oluşan yapılandırılmış bir modele dönüştürür. Bir ekip bir iş akışını ortak şekilde anlamak, sınırlı bağlamları veya aggregate'leri keşfetmek ya da dağınık bir yapışkan not duvarını toparlamak istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: software-architect
  area: domain
  title: "Event storming"
  related: "bounded-context-map, aggregate-design, event-driven-design, workshop-plan, glossary-builder"
  prompt: "Sipariş-teslimat akışımız için tasarım düzeyinde bir event storming yürütmeme yardım et ve dünkü oturumun notlarını yapılandır."
---

# Event Storming

## Amaç
Bir alanda neler olduğunu, alan olayları ve bunların etrafındaki komutlar, aktörler, politikalar ve verilerle zaman çizelgesine göre sıralanmış ortak bir model olarak ortaya koymak. Böylece sınırlar, aggregate'ler ve açık çatışmalar tasarım başlamadan görünür hale gelir.

## Ne zaman kullanılır
- Yeni bir alanın veya büyük bir özelliğin iş ve mühendislik tarafından birlikte anlaşılması gerektiğinde.
- Servis veya modül sınırları tartışmalıysa ve iş akışından kanıt gerekiyorsa.
- Oturum yapılmış ve ham notların (fotoğraf dökümü, liste) bir modele dönüştürülmesi gerekiyorsa.
- `aggregate-design` veya `event-driven-design` öncesinde, bunları yönlendiren olayları ve değişmezleri bulmak için.

## Ne zaman kullanılmaz
- Akış zaten modellenmişse ve yalnızca resmi bir süreç diyagramı gerekiyorsa `bpmn-model` veya `as-is-process` kullanılır.
- Bağlamlar biliniyor, yalnızca aralarındaki ilişkiler belirsizse `bounded-context-map` kullanılır.
- Asıl ihtiyaç oturum lojistiği (salon, gündem, davet) ise `workshop-plan` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki alan veya akış, başlangıç ve bitiş olaylarıyla (ör. "sipariş verildi"den "sipariş teslim edildi"ye).
- Planlanan oturum düzeni ya da oturumun ham çıktısı (not listesi, döküm, fotoğraf notları).

İsteğe bağlı:
- Katılımcılar ve rolleri (alan uzmanları vazgeçilmezdir).
- Mevcut sözlük, süreç dokümanları, bilinen sıkıntılar.
- Düzey: genel resim (tüm alan) veya süreç/tasarım düzeyi (tek akış, aggregate'lere kadar).

Kapsamın net bir başlangıcı ve bitişi yoksa önce bunları sor. Diğer tüm eksikleri açık soru olarak ele al.

## Süreç
1. Düzeyi ve kapsamı sabitle: bütün bir değer akışını keşfetmek için genel resim, aggregate ve politikaların bulunması gereken tek akış için tasarım düzeyi. Başlangıç ve bitiş olaylarını açıkça yaz.
2. Oturum planlanıyorsa lejantı tanımla (turuncu: alan olayı, mavi: komut, sarı: aktör, lila: politika, pembe: dış sistem, yeşil: okuma modeli, açık sarı: aggregate, kırmızı/macenta: sıcak nokta) ve süreyi belirle; her alt akış için en az bir alan uzmanı şart koş.
3. Alan olaylarını geçmiş zamanlı iş olguları olarak topla ("Ödeme Onaylandı"); kullanıcı arayüzü eylemleri veya teknik adımlar ("Butona Tıklandı", "Satır Eklendi") olay değildir. Bunları yeniden yaz veya çıkar.
4. Zaman çizelgesini uygula: olayları soldan sağa sırala, eş anlamlıları birleştir ve seçilen terimi sözlüğe yaz. Paralel ve alternatif yolları açıkça işaretle.
5. İş anlamının el değiştirdiği kilit olayları (pivotal event) belirle (ör. "Sipariş Onaylandı", "Sevkiyat Çıktı"); bunlar aday bağlam sınırlarıdır.
6. Her olay için tetikleyen komutu ve bu komutu veren aktörü ya da dış sistemi ekle; bir olayı sonraki komuta bağlayan politikaları ("X olduğunda Y yap") ekle.
7. Okuma modellerini ekle: aktörün bir komuta karar vermek için ihtiyaç duyduğu bilgi. Eksik okuma modelleri çoğu zaman eksik veri gereksinimlerini ortaya çıkarır.
8. Tasarım düzeyinde komutları ve olayları, tutarlı kalması gereken iş kuralı etrafında grupla; bu kümeleri aday aggregate olarak adlandır ve değişmez bir alan uzmanınca teyit edilene kadar `[VARSAYIM]` olarak etiketle.
9. Her anlaşmazlığı, bilinmeyeni veya sıkıntıyı soru, onu kimin gündeme getirdiği ve kimin çözebileceğiyle birlikte sıcak nokta olarak kaydet. Sıcak noktaları tahminle çözme.
10. Katılımcıların söylediklerini kendi çıkarımlarından (ör. adı konmamış bir politika, birleştirilmiş eş anlamlılar) ayır ve her çıkarımı etiketle.
11. Çıktı şablonunu zaman çizelgesine göre sıralı ve her kilit bölüm için ayrı kulvarla doldur.
12. Hedef devam ediyorsa bulunan sınırlar için `bounded-context-map`, aday aggregate'ler için `aggregate-design` veya entegrasyon olayları için `event-driven-design` öner.

## Çıktı formatı
```markdown
# Event Storming: <akış> (<genel resim | tasarım düzeyi>)
Kapsam: <başlangıç olayı> → <bitiş olayı> · Katılımcılar: <roller veya [BİLİNMİYOR]>

## Zaman Çizelgesi
| # | Bölüm | Aktör / Sistem | Komut | Alan Olayı | Politika | Okuma Modeli | Aggregate (aday) |
|---|---|---|---|---|---|---|---|

## Kilit Olaylar ve Aday Sınırlar
- <olay> — <bölüm A> ile <bölüm B>'yi ayırır

## Aday Aggregate'ler
- <ad> — değişmez: <kural> — olaylar: ... [teyit edilene kadar VARSAYIM]

## Sıcak Noktalar
| # | Soru / çatışma | Gündeme getiren | Çözebilecek | Engellediği |
|---|---|---|---|---|

## Sözlük Kararları
- <seçilen terim> (değil: <eş anlamlılar>) — anlamı

## Çıkarımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her alan olayı geçmiş zamanlı bir iş olgusu; arayüz veya teknik adım değil.
- [ ] Olaylar zaman sırasında; paralel ve alternatif yollar işaretli.
- [ ] Her komutu tetikleyen bir aktör, dış sistem veya politika var.
- [ ] Sıcak noktalar sessizce çözülmemiş, sahibi olan sorular olarak kaydedilmiş.
- [ ] Aday aggregate'ler adı konmuş bir değişmeze bağlı ve teyit edilene kadar etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Oturumu yalnızca mühendislerle yapmak. Alan uzmanı olmadan işi değil mevcut yazılımı modellersiniz.
- Genel resim oturumunda aggregate ve servislere atlamak. Önce zaman çizelgesini ve sıcak noktaları bitir.
- Gerçek iş olgularını gizleyen CRUD olayları ("Sipariş Güncellendi"). Gerçekte neyin, neden değiştiğini sor.

## Örnek
Girdi: "Notlar: Sepete ekle, Sipariş Oluşturuldu, Ödeme OK, Stok Ayrıldı, Fatura Satırı Eklendi, Sipariş Gönderildi, Müşteri Bilgilendirildi."

Çıktıdan bir bölüm:
- Yeniden yazılan olaylar: "Ürün Sepete Eklendi", "Sipariş Verildi", "Ödeme Onaylandı", "Stok Ayrıldı", "Fatura Kesildi" (önceki: "Fatura Satırı Eklendi", teknik), "Sevkiyat Çıktı".
- Kilit olay: "Sipariş Verildi", Alışveriş ile Karşılama (fulfilment) bölümlerini ayırır.
- Politika `[VARSAYIM]`: Ödeme Onaylandığında Stok Ayır.
- Sıcak nokta: Ön siparişlerde stok ödemeden önce mi sonra mı ayrılıyor? Gündeme getiren: depo sorumlusu. Çözebilecek: ürün sahibi.
