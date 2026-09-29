---
name: bdd-feature-file
description: "İş tarafının okuyabileceği özellik açıklaması, background, bildirimsel senaryolar ve örnek tablolu scenario outline'lar içeren, etiketli ve gereksinimlere izlenebilir Gherkin feature dosyaları yazar. Ekip davranış odaklı geliştirme veya örneklerle tanımlama uyguluyorsa, kabul kriterleri çalıştırılabilir tanımlara dönüşecekse ya da mevcut Gherkin emir kipinde, arayüze bağımlı veya bakımı zor ise kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: design
  title: "BDD feature dosyası yazma"
  related: "acceptance-criteria, user-story, test-scenarios-from-requirements, test-automation-script, equivalence-boundary-analysis"
  prompt: "Kupon kuralı için feature dosyası yaz: sipariş başına bir kupon, en az 250 TL sepet, kampanyalı fiyatlarla birleşmez, süresi dolmuş kupon reddedilir."
---

# BDD Feature Dosyası Yazma

## Amaç
Bir özelliğin beklenen davranışını, iş tarafının okuyup onaylayabileceği ve otomasyonun yeniden yazmadan bağlanabileceği kısa ve öz Gherkin olarak ifade etmek.

## Ne zaman kullanılır
- Kabul kriterleri üzerinde anlaşıldı ve ekip yaşayan, çalıştırılabilir tanımlar istiyor.
- Bir three amigos veya refinement oturumunda çıkan örneklerin yazıya dökülmesi gerekiyor.
- Mevcut feature dosyaları her arayüz değişikliğinde kırılan, tık tık ilerleyen uzun script'ler.

## Ne zaman kullanılmaz
- Davranışın kendisi henüz netleşmediyse önce kuralları oturtmak için `acceptance-criteria` kullanılır.
- Adım bazında beklenen sonuçlu ayrıntılı manuel adımlar gerekiyorsa `test-case-writing` kullanılır.
- Step definition veya otomasyon kodu gerekiyorsa `test-automation-script` kullanılır.

## Girdiler
Zorunlu:
- Tanımlanacak story, kabul kriterleri veya iş kuralları.

İsteğe bağlı, kaliteyi artırır:
- Alan sözlüğü ve mevcut step dağarcığı, etiketleme kuralları, dil ayarı (ekip Gherkin'i Türkçe yazıyorsa `# language: tr`).
- İş tarafıyla daha önce konuşulmuş sınırlar ve örnekler.

Hiç kural veya kriter verilmediyse iste. Sonucu belirsiz olan durumlar `@question` etiketli senaryo olur, açık nokta yorum satırına yazılır.

## Süreç
1. Girdiden kuralları çıkar; her kural bir `Rule:` bloğu veya senaryo grubu olur. Feature dosyasını ekran başına değil yetenek başına bir tane tut.
2. Feature başlığını yaz: ad ve iş değerini belirten kısa bir "In order to / As a / I want" ya da düz anlatım. Belirli bir rol kullan, asla "bir kullanıcı" deme.
3. `Background` içine yalnızca ortak ve vazgeçilmez bağlamı koy; yaklaşık üç adımdan uzunsa veya her senaryoya gerekmiyorsa senaryolara taşı.
4. Her kural için en az bir pozitif ve bir negatif senaryo yaz. Senaryo başlığını testi değil davranışı anlatacak şekilde koy ("Sepet asgari tutarın altındaysa kupon reddedilir").
5. Adımları alan dilinde ve bildirimsel yaz: Given = durum, When = tek bir iş aksiyonu, Then = gözlemlenebilir sonuç. Tıklama, seçici, URL veya teknik ID olmasın.
6. Senaryo başına bir When ve bir Then tut (Then altındaki And yalnızca aynı sonucun parçaları için); birden fazla aksiyon veya sonuç varsa senaryoyu böl.
7. Aynı davranışın veri varyasyonları için `Scenario Outline` ve `Examples` kullan, satırları denklik sınıfları ve sınırlardan seç; farklı davranışları gizlemek için outline kullanma.
8. Step definition'lar küçük kalsın diye verilmişse mevcut step ifadelerini yeniden kullan; ifadeleri tutarlı tut (aynı kavram için aynı isim).
9. Ekip kuralına göre izlenebilirlik ve koşum için etiket ekle (`@REQ-123`, `@smoke`, `@wip`, `@question`).
10. Çıkarımla eklenen kuralları yorum satırında `[VARSAYIM]` ile işaretle ve açık soruları dosyanın altında listele.
11. Kullanıcı devam ederse step definition'lar için `test-automation-script`, açık sorular kuralları değiştiriyorsa `acceptance-criteria` öner.

## Çıktı formatı
```gherkin
@<yetenek-etiketi> @<REQ-id>
Feature: <yetenek>
  <belirli bir rolle iş değeri anlatımı>

  Background:
    Given <ortak ve vazgeçilmez bağlam>

  Rule: <iş kuralı>

    Scenario: <tek cümlede davranış>
      Given <durum>
      When <tek iş aksiyonu>
      Then <gözlemlenebilir sonuç>

    Scenario Outline: <veriye göre değişen davranış>
      Given <<param> içeren durum>
      When <aksiyon>
      Then <<sonuc> içeren sonuç>

      Examples:
        | param | sonuc |
```
Açık sorular / varsayımlar: dosyanın altında numaralı liste.

## Kalite kontrol listesi
- [ ] Bir iş paydaşı her senaryoyu teknik bilgi olmadan okuyabiliyor.
- [ ] Her senaryoda tam olarak bir When ve bir Then sonucu var; Given aksiyon değil durum anlatıyor.
- [ ] Adımlarda arayüz mekaniği, seçici, URL veya veritabanı ayrıntısı yok.
- [ ] Her kuralın en az bir negatif senaryosu var; sınırlar Examples'ta yer alıyor.
- [ ] Senaryolar bağımsız ve davranışa göre adlandırılmış.
- [ ] Etiketler gereksinimlere izlenebilirlik sağlıyor ve çıkarımla eklenen kurallar `[VARSAYIM]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Emir kipinde script'ler ("When Uygula'ya tıklarım, And ... yazarım"). Arayüze bağlanır ve kuralı gizler; niyeti anlat.
- Her okurun kaydırarak geçmek zorunda kaldığı dev Background bölümleri. Yalnızca tüm senaryoların ihtiyacı olanı tut.
- Bir sütunu tamamen farklı davranışlar arasında geçiş yapan tek Scenario Outline. Ayrı senaryolara böl.
- Gherkin'i otomasyondan sonra test kodunun dokümanı olarak yazmak. Değer, geliştirmeden önce örneklerde anlaşmaktan gelir.

## Örnek
Girdi: "Sipariş başına bir kupon, en az 250 TL sepet, kampanyalı fiyatlarla birleşmez, süresi dolmuş kupon reddedilir."

Zayıf:
```gherkin
Scenario: kupon testi
  When sepet sayfasını açıp #coupon alanına "SAVE10" yazar ve Uygula'ya tıklarım
  Then bir mesaj görürüm ve toplam değişir ve ikinci kupon alanı pasif olur
```
Güçlü (bölüm):
```gherkin
Rule: Sepet asgari tutara ulaşmalıdır

  Scenario Outline: Kuponun kabulü sepet toplamına bağlıdır
    Given bir müşterinin sepet toplamı <toplam> TL
    When müşteri geçerli bir kupon uygular
    Then kupon <sonuc>

    Examples:
      | toplam | sonuc       |
      | 249.99 | reddedilir  |
      | 250.00 | kabul edilir |
```
Açık soru: Asgari tutar kampanya indiriminden önce mi sonra mı kontrol ediliyor? `[VARSAYIM: önce]`
