---
name: implement-from-story
description: "Kabul kriterlerini davranışlara eşleyerek, mevcut kod kurallarını okuyarak, kodu ve testleri küçük doğrulanabilir adımlarla yazarak ve neyin geliştirildiğini, nasıl doğrulandığını ve neyin açık kaldığını raporlayarak bir kullanıcı hikayesinden özellik planlar ve geliştirir. Bir geliştirici verilen kabul kriterlerine göre bir hikaye, kayıt veya özelliğin geliştirilmesini istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: coding
  title: "Hikayeden özellik geliştirme"
  related: "task-breakdown, acceptance-criteria, tdd-cycle, unit-test-writing, pull-request-description"
  prompt: "Bu hikayeyi servisimizde geliştir: müşteri varsayılan teslimat adresi belirleyebilir; yalnızca bir adres varsayılan olabilir; varsayılan adres checkout'ta önceden seçili gelir."
---

# Hikayeden Özellik Geliştirme

## Amaç
Her kabul kriterini karşılayan, mevcut kod tabanının kurallarına uyan, testli ve çalışan kod teslim etmek; neyin doğrulandığını ve neyin varsayıldığını dürüstçe raporlamak.

## Ne zaman kullanılır
- Kabul kriterleri olan bir hikaye veya kayıt kodlanmaya hazırsa.
- Bir geliştirici ilgili kodu paylaşıp tarif edilen bir davranışın geliştirilmesini istiyorsa.
- Küçük bir özellik uçtan uca eklenecekse (sözleşme, mantık, kalıcılık, testler).

## Ne zaman kullanılmaz
- Hikaye doğrudan kodlanamayacak kadar büyük veya belirsizse önce `task-breakdown` veya `acceptance-criteria` kullanılır.
- Davranış değişikliği olmayan yapısal bir değişiklikse `refactoring` kullanılır.
- Ekipler arası veya geri alınması zor bir değişiklikse önce `technical-design-doc` kullanılır.

## Girdiler
Zorunlu:
- Kabul kriterleriyle birlikte hikaye ve ilgili mevcut kod (ya da teknoloji yığını ve yapının tarifi).

İsteğe bağlı, kaliteyi artırır:
- Kodlama standartları, test kuralları, mimari kurallar, feature flag politikası.
- İlgili sözleşmeler, şemalar, örnek alınacak benzer mevcut özellikler.

Kod veya teknoloji bilgisi verilmemişse iste; bir proje yapısı uydurup mevcutmuş gibi sunma.

## Süreç
1. Her kabul kriterini girdi, eylem ve beklenen sonuçla gözlemlenebilir bir davranış olarak yeniden yaz; belirsizlikleri listele, engellemeyenler için belgelenmiş bir `[VARSAYIM]` seç.
2. Değişikliğin dokunduğu mevcut kod yollarını oku: giriş noktası, alan mantığı, kalıcılık, hata yönetimi, testler. Uyulacak kuralları not et (isimlendirme, katmanlar, DI, hata tipleri).
3. Uyan en küçük tasarımı belirle: yeni mantık nereye ait, sözleşmede veya şemada ne değişiyor, neyin geriye dönük uyumlu kalması gerekiyor.
4. Adımları her biri yeşil bitecek şekilde planla: örn. şema genişletme → birim testli alan kuralı → entegrasyon testli uç nokta/arayüz → flag arkasında bağlama.
5. Her adımda testi koddan önce veya kodla birlikte yaz; kabul kriterini, uç durumlarını ve hata yolunu kapsa.
6. Kod tabanının deyimleriyle geliştir; girdiyi sınırlarda doğrula, alan kurallarını alan katmanında tut, kriter tekillik gerektiriyorsa eşzamanlılığı ele al.
7. Log/metrik yalnızca işletime katkı sağladığı yerde ve kişisel veri içermeden ekle.
8. Diff'i kendin incele: ölü kod, debug çıktısı, TODO'lar, isimlendirme, hata mesajları, güvenlik (her yeni giriş noktasında yetkilendirme).
9. Her kabul kriterini onu kanıtlayan testlere eşle.
10. Raporla: değişen dosyalar, testlerin nasıl çalıştırılacağı, varsayımlar ve takip işleri (dokümantasyon, flag kaldırma, migration'ın daraltma adımı).
11. Hedef devam ediyorsa değişikliği incelemeye açmak için `pull-request-description` veya test kapsamını derinleştirmek için `unit-test-writing` öner.

## Çıktı formatı
```markdown
# Geliştirme: <hikaye başlığı>
## Plan
1. <adım> — şu durumla biter: <yeşil test / doğrulanabilir durum>

## Değişiklikler
- `<yol>`: <ne ve neden>

## Kod
<dosya bazında diff veya kod blokları>

## Kabul Kriterlerinin Doğrulanması
| Kriter | Test(ler) | Durum |

## Varsayımlar ve Takip İşleri
- [VARSAYIM] ...
- Takip: ...
```

## Kalite kontrol listesi
- [ ] Her kabul kriterinin, değişiklik olmadan başarısız olacak en az bir testi var.
- [ ] Kod, paylaşılan kodda görülen mevcut kurallara uyuyor.
- [ ] Yeni giriş noktaları yetkilendirme uyguluyor ve girdiyi doğruluyor.
- [ ] Eşzamanlılık altında korunması gereken kurallar korunuyor (kısıt, kilit veya idempotency).
- [ ] Uydurulmuş dosya, API veya kütüphane fonksiyonu yok; emin olunmayan her şey işaretli.
- [ ] Varsayımlar ve takip işleri açıkça listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Mutlu yolu geliştirip kriterlerin ima ettiği uç durumları (boş, mükerrer, bulunamadı, yetkisiz) atlamak.
- Kod tabanında o iş için zaten bir desen veya kütüphane varken yenisini getirmek.
- "Yalnızca bir varsayılan" kuralını kodda oku-sonra-yaz ile zorlamak; eşzamanlı istekler iki varsayılan üretir. Kısıt veya transaction içinde takas kullan.

## Örnek
Girdi: "Müşteri varsayılan teslimat adresi belirler; yalnızca bir varsayılan; checkout'ta önceden seçili."

Çıktıdan bir bölüm:
- Plan adım 2: `Customer.setDefaultAddress(addressId)` tek transaction içinde önceki varsayılanı kaldırır ve yenisini atar; birim testleri: varsayılanı değiştirme, bilinmeyen adres → `AddressNotFound`, başka müşterinin adresi → yetkisiz.
- Kural: `(customer_id) WHERE is_default` üzerinde kısmi unique indeks artı transaction; entegrasyon testi iki eşzamanlı istek çalıştırıp tam olarak bir varsayılan olduğunu doğrular.
- `[VARSAYIM]` Varsayılan adres silinirse varsayılan kalmaz; checkout'ta önceden seçim olmaz. Ürün sahibiyle teyit et.
