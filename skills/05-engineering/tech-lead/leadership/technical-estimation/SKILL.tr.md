---
name: technical-estimation
description: "Teknik bir işi bağımlılık ve riske göre sıralanmış, doğrulanabilir küçük görevlere böler; her görevi aralık olarak tahmin eder, varsayımları ve bilinmeyenleri açık yazar, entegrasyon, test ve sürüm eforunu ekler, güven düzeyini ve rakamı neyin değiştireceğini belirtir. Teknik lidere \"bu ne kadar sürer?\" sorulduğunda, bir özellik, taşıma veya teknik girişimin planlama ya da taahhüt için boyutlandırılması gerektiğinde veya mevcut bir tahminin sorgulanıp yeniden baz alınması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: tech-lead
  area: leadership
  title: "Teknik iş tahmini"
  related: "task-breakdown, estimation-three-point, spike-report, technical-risk-review, monte-carlo-forecast"
  prompt: "Ürün ekibi web uygulamamıza kurumsal kimlik sağlayıcımızla SSO eklemenin ne kadar süreceğini soruyor. Aralıklar ve varsayımlarla bir tahmin ver."
---

# Teknik İş Tahmini

## Amaç
Karar vericilere planlama yapabilecekleri bir tahmin sunmak: güven düzeyi belirtilmiş bir aralık, dayandığı varsayımlar ve onu oynatabilecek bilinmeyenler. İyi bir tahmin bir tarih sözü değil, risk hakkında bir iletişim aracıdır.

## Ne zaman kullanılır
- Bir özelliğin, taşımanın, entegrasyonun veya refactoring'in ne kadar süreceği sorulduğunda.
- İşin yol haritası, iterasyon veya bütçe planlaması için boyutlandırılması gerektiğinde.
- Önceki bir tahmin yanlış göründüğünde ve yeni bilgiyle yeniden baz alınması gerektiğinde.

## Ne zaman kullanılmaz
- Bütünü boyutlandırmadan tek bir story'yi uygulama görevlerine bölmek için `task-breakdown` kullanılır.
- Çok sayıda iş paketinde üç noktalı hesapla resmi proje takvimi için `estimation-three-point` kullanılır.
- Ekibin geçmiş verimine dayanarak bitiş tahmini için `monte-carlo-forecast` kullanılır.

## Girdiler
Zorunlu:
- İşin tanımı (özellik, epic, teknik girişim) ve "bitti"nin ne anlama geldiği.

İsteğe bağlı, kaliteyi artırır:
- İlgili kod, mimari ve kısıtlar; ekip büyüklüğü, deneyimi ve müsaitliği.
- Benzer işlerin geçmiş verisi (gerçekleşen süreler, verim).
- Son tarihler, sabit kapsam veya sabit tarih kısıtları, diğer ekiplere bağımlılıklar.

"Bitti" belirsizse (ör. veri taşıma, dokümantasyon, üretime çıkış dahil mi) sor. En fazla beş soru sor; geri kalan her şey açık bir varsayım olur.

## Süreç
1. Kapsamı ve bitti tanımını, kodlama dışı işler dahil yeniden yaz: testler, güvenlik incelemesi, dokümantasyon, deployment, veri taşıma, izleme, stabilizasyon.
2. İşi doğrulanabilir küçük görevlere böl (hedef: her biri birkaç günlük efora sığsın); her görevin bitti kriteri ve nasıl doğrulanacağı olsun. Belirsizlik boyuttan baskın hale geldiği yerde bölmeyi durdur.
3. Görevleri bağımlılık ve riske göre sırala: en riskli veya en belirsiz kalemler önce; diğer ekiplere veya dış taraflara bağlı görevleri işaretle.
4. Her görevin belirsizliğini sınıflandır: bilinen (daha önce yapıldı), bilinen bilinmeyen (araştırma gerekir), bilinmeyen (yeni teknoloji veya belirsiz gereksinim). Tahmin edilemeyecek kadar belirsiz kalemler için süre sınırlı bir spike öner.
5. Her görevi efor olarak bir aralıkla tahmin et (iyimser / olası / kötümser veya alt / üst); asla tek sayı verme. Varsa referans görevleri veya geçmiş veriyi kullan ve bunu belirt.
6. Sıkça unutulan işleri açıkça ekle: entegrasyon ve uçtan uca test, code review döngüleri, ortam kurulumu, sürüm ve yaygınlaştırma, ilk kullanım sonrası hata düzeltme.
7. Efor'u, belirtilen müsaitliği (odak katsayısı, paralel işler, nöbet, tatiller) kullanarak takvim süresine çevir; verilmemişse `[VARSAYIM]` olarak işaretle. Paralelleştirmenin nerede mümkün olup olmadığını göster.
8. Toplamı makul biçimde birleştir (tüm kötümser değerleri toplayıp "olası" toplam diye sunma) ve genel aralık için bir güven düzeyi belirt.
9. Varsayımları, bağımlılıkları ve en önemli riskleri tahmine etkileriyle listele ("kimlik sağlayıcı özel claim eşlemesi gerektirirse 3-5 gün ekle").
10. Aralığı neyin daraltacağını (spike, prototip, başka bir ekipten gelecek cevap) ve tahminin ne zaman yeniden gözden geçirilmesi gerektiğini belirt.
11. Kullanıcı devam ederse ayrıntılı story'ler için `task-breakdown`, en büyük bilinmeyeni çözmek için `spike-report`, planı tehdit eden riskler için `technical-risk-review` öner.

## Çıktı formatı
```markdown
# Tahmin: <iş kalemi>
Bitti tanımı: ...
Genel: <alt>–<üst> <birim> efor · <alt>–<üst> takvim haftası · Güven: <düşük/orta/yüksek>

## Görev Kırılımı
| # | Görev | Bitti koşulu / doğrulama | Bağımlılık | Belirsizlik | Tahmin (alt–olası–üst) |
|---|---|---|---|---|---|

## Takvim Varsayımları
- Ekip: ... · Müsaitlik: ... [VARSAYIM] · Paralellik: ...

## Varsayımlar
- [VARSAYIM] ...

## Riskler ve Etkileri
| Risk | Tahmine etkisi | Azaltma |
|---|---|---|

## Aralığı Daraltmak İçin
- ...
```

## Kalite kontrol listesi
- [ ] Her tahmin bir aralık ve genel aralığın belirtilmiş bir güven düzeyi var.
- [ ] Görevler küçük; her birinin bitti kriteri ve doğrulama adımı var, bağımlılık ve riske göre sıralı.
- [ ] Kodlama dışı işler (test, review, sürüm, taşıma, stabilizasyon) dahil edildi.
- [ ] Her varsayım etiketli ve hiçbir rakam dayanağı belirtilmeden uydurulmadı.
- [ ] Riskler yalnızca listelenmedi, tahmine etkileriyle sayısallaştırıldı.
- [ ] Efor ve takvim süresi ayrı gösterildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Baskı altında tek sayı vermek; bu sayı taahhüde dönüşür. Bir aralık ve onu sınırlayan varsayımları ver.
- Yalnızca kodlamayı tahmin etmek. Entegrasyon, review, sürüm ve stabilizasyon çoğu zaman kod yazmak kadar sürer.
- Toplantıları, destek görevini ve diğer projeleri yok sayıp eforu %100 müsaitlikle tarihe çevirmek.

## Örnek
Girdi: "Web uygulamamıza kurumsal kimlik sağlayıcıyla SSO ekleyin."

Zayıf: "Yaklaşık iki hafta."

Güçlü örnekten bir bölüm:
| # | Görev | Bitti koşulu / doğrulama | Bağımlılık | Belirsizlik | Tahmin (gün) |
|---|---|---|---|---|---|
| 1 | Spike: protokolü, claim'leri ve test tenant erişimini doğrula | Test tenant'a giriş başarılı | IdP yönetici ekibi | Bilinmeyen | 1–2–3 (süre sınırlı) |
| 2 | Standart protokol kütüphanesiyle giriş/çıkış akışını uygula | Entegrasyon testi geçiyor | 1 | Bilinen bilinmeyen | 2–3–5 |
| 3 | IdP claim'lerini uygulama rollerine eşle; mevcut hesapları taşı | Mevcut kullanıcılar staging'de aynı yetkilerle giriş yapıyor | 1 | Bilinen bilinmeyen | 2–4–7 |

Genel: 10–18 gün efor, %60 müsaitlikle `[VARSAYIM]` 3–5 takvim haftası, güven orta. En büyük etken: mevcut kullanıcılar için hesap eşleme.
