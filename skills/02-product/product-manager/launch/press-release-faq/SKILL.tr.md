---
name: press-release-faq
description: "Bir ürün fikrinin, hiçbir şey geliştirilmeden önce ilgi çekici, anlaşılır ve yapılabilir olup olmadığını sınamak için gelecekteki bir lansman tarihli tersine çalışma basın bülteni, müşteri SSS'si ve iç SSS yazar; dokümanın ortaya çıkardığı açık sorular ve risklerle biter. Yeni bir ürün veya büyük bir özellik önerildiğinde, ekibin tasarımdan önce müşteri sonucunda uzlaşması gerektiğinde ya da \"PR/FAQ\", \"working backwards\" dokümanı veya \"gelecekteki basın bülteni\" istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: launch
  title: "Tersine çalışma basın bülteni ve SSS"
  related: "product-vision, prd-writing, value-proposition-canvas, positioning-statement, pre-mortem"
  prompt: "B2B müşterilerimizin portala giriş yapmadan WhatsApp üzerinden teslimat tahmini (ETA) alabildiği bir özellik için tersine çalışma PR/FAQ yaz."
---

# Tersine Çalışma Basın Bülteni ve SSS

## Amaç
Müşteriden ve lansman gününden başlayıp geriye doğru çalışmak: basın bülteni ilgi çekici değilse ve SSS zor sorulara cevap veremiyorsa fikir geliştirilmeye hazır değildir. Doküman pazarlama metni değil, bir düşünme ve karar aracıdır.

## Ne zaman kullanılır
- Yeni bir ürün, hizmet veya büyük bir özellik yatırım için önerildiğinde.
- Paydaşlar ürünün ne için veya kimin için olduğu konusunda anlaşamadığında.
- PRD veya tasarım çalışmasından önce müşteri sonucunda ve sınırlarda uzlaşmak için.

## Ne zaman kullanılmaz
- Ürün zaten var ve gerçek bir lansman duyurusu gerekiyorsa `release-announcement` kullanılır.
- Geliştirme için ayrıntılı gereksinimler gerekiyorsa PR/FAQ kabul edildikten sonra `prd-writing` kullanılır.
- Yalnızca uzun vadeli yön gerekiyorsa `product-vision` kullanılır.

## Girdiler
Zorunlu:
- Fikir: hedef müşteri, problem ve önerilen çözüm, birkaç cümleyle.

İsteğe bağlı, kaliteyi artırır:
- Müşteri kanıtları, rakip alternatifler, kısıtlar, iş hedefleri, lansman ufku, fiyat fikri.

Hedef müşteri veya problem eksikse her seferinde tek soru sorarak iste. Müşteri alıntılarını gerçekmiş gibi uydurma: bunları temsili olarak yaz ve `[TEMSİLİ]` olarak etiketle. Pazar rakamı asla uydurma.

## Süreç
1. Başlığı ve alt başlığı müşterinin dilinde yaz: kim hangi faydayı elde ediyor. Kurum içi jargon yok; müşteri önemsemiyorsa teknoloji adı yok.
2. Kullanıcının verdiği gelecekteki lansman tarihiyle veya `[TBD]` ile tarih satırını ve ürünü ile faydayı özetleyen ilk paragrafı yaz.
3. Problem paragrafı: müşterinin bugünkü sıkıntısını, müşterinin anlatacağı biçimde somut olarak yaz.
4. Çözüm paragrafı: ürünün problemi nasıl çözdüğünü mimariye değil deneyime odaklanarak yaz.
5. Temsili bir yönetici alıntısı (neden geliştirdik) ve temsili bir müşteri alıntısı (elde ettiği sonuç) ekle; ikisi de `[TEMSİLİ]` etiketli.
6. "Nasıl başlanır" ve erişilebilirlik bilgisini bir iki cümleyle ekle; bülteni yaklaşık bir sayfada tut.
7. Müşteri SSS: gerçek bir müşterinin soracağı 6-10 soru (fiyat, erişilebilirlik, kurulum, veri, sınırlamalar, eski yönteme ne olacağı).
8. İç SSS: karar vericiler için 6-12 zor soru: hedef segmentin büyüklüğü ve kanıtı, neden şimdi, başarı metrikleri, iş modeli, maliyet ve ekip, bağımlılıklar, hukuk/gizlilik, en önemli riskler ve yanıldığımızı nasıl anlarız, neyi yapmayacağız. Kanıtla cevapla ya da `[BİLİNMİYOR]` olarak işaretle.
9. Öz eleştiri yap: Fayda başlıkta net mi? Hedef müşteri önemser mi? Hangi SSS cevapları zayıf veya `[BİLİNMİYOR]`? Bunları sahipleriyle birlikte açık soru ve risk olarak listele.
10. Gerekçeleriyle bir karar öner (devam / iyileştir / durdur) ve sonraki beceriyi öner: tanımlamak için `prd-writing`, riskleri zorlamak için `pre-mortem` veya müşteri değeri belirsizse `value-proposition-canvas`.

## Çıktı formatı
```markdown
# <Başlık: müşteri faydası>
## <Alt başlık: kim, ne, neden önemli>
**<Şehir>, <gelecekteki lansman tarihi veya TBD>** – <özet paragraf>

<Problem paragrafı>
<Çözüm paragrafı>
"<Yönetici alıntısı>" – <rol> [TEMSİLİ]
<Nasıl çalışır / deneyim>
"<Müşteri alıntısı>" – <müşteri tipi> [TEMSİLİ]
<Nasıl başlanır, erişilebilirlik>

---
## Müşteri SSS
**S:** ... **C:** ...

## İç SSS
**S:** Müşteri tam olarak kim ve kaç tane? **C:** ... [KANIT / BİLİNMİYOR]
**S:** Başarıyı nasıl ölçeceğiz? **C:** ...
**S:** Açıkça neyi yapmıyoruz? **C:** ...

## Açık Sorular ve Riskler
| # | Soru / risk | Neden önemli | Sahibi |
|---|---|---|---|

## Öneri
<Devam / İyileştir / Durdur> – <gerekçeler>
```

## Kalite kontrol listesi
- [ ] Başlık, uzman olmayan birinin anlayacağı bir müşteri faydası ifade ediyor.
- [ ] Basın bülteni yaklaşık bir sayfaya sığıyor ve kurum içi jargon ya da mimari içermiyor.
- [ ] Alıntılar ve tarihler temsili veya TBD olarak etiketli; rakam uydurulmadı.
- [ ] İç SSS zor soruları dürüstçe cevaplıyor, boşluklar `[BİLİNMİYOR]` olarak işaretli.
- [ ] Kapsam dışı maddeler ve başarı metrikleri açık.
- [ ] Açık soruların ve risklerin sahipleri var ve bir öneri verilmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Basın bülteni diye özellik listesi yazmak. Müşteri sonucuyla başla; özellikler gerekirse sonra gelir.
- Kolay sorulardan oluşan iç SSS. Değer rahatsız edici sorulardadır; her cevap olumluysa SSS işini yapmıyordur.
- Taslağı taahhüt gibi görmek. PR/FAQ'yu fikir netleşene kadar yinele ya da fikri durdur.

## Örnek
Girdi: "B2B müşteriler portala girmeden WhatsApp'tan teslimat ETA'sı alsın."

Zayıf başlık: "Şirket, gerçek zamanlı ETA motoruyla WhatsApp entegrasyonunu başlattı."
Güçlü başlık: "Teslimatınızın ne zaman geleceğini giriş yapmadan öğrenin: tahmini varış saati artık zaten kullandığınız sohbete geliyor."
İç SSS'den bir bölüm:
**S:** İşe yaradığını nasıl anlayacağız? **C:** Hizmet masasına gelen "teslimatım nerede" aramalarının azalmasıyla `[başlangıç değeri BİLİNMİYOR – sahibi: hizmet masası sorumlusu]`.
**S:** Neyi yapmıyoruz? **C:** İlk sürümde sohbet üzerinden çift yönlü sipariş yok.
