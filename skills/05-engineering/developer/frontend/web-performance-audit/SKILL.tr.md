---
description: Bir web sayfasını veya front-end uygulamasını Core Web Vitals (LCP, INP, CLS) ve destekleyici metriklerle yükleme ve çalışma zamanı performansı açısından denetler; her sorunu kritik render yolu, JavaScript, görseller, fontlar veya üçüncü taraf kodlardaki nedenine bağlar ve beklenen etkisi ile doğrulama yöntemi belirtilmiş öncelikli düzeltmeler verir. Bir sayfa yavaş hissettirdiğinde, saha verisinde Core Web Vitals kaldığında, performans bütçesi aşıldığında veya bir lab raporu ya da trace'in yorumlanması gerektiğinde kullanılır.
related: performance-optimization, performance-test-plan, observability-plan, slo-definition, component-design
prompt: Ürün listeleme sayfamızda mobilde LCP 4,8 sn, INP 350 ms civarında. Lab raporu ve sayfanın head bölümü ekte. Önce neyi düzeltmeliyiz?
---

# Web Performans Denetimi

## Amaç
Performans ölçümlerini kullanıcıya dönük metrikleri gerçekten iyileştiren kısa ve kanıta dayalı bir düzeltme listesine dönüştürmek. Denetim saha gerçeğini lab teşhislerinden ayırır ve her öneriyi bir metriğe, bir nedene ve bir doğrulama adımına bağlar.

## Ne zaman kullanılır
- Saha verisi (gerçek kullanıcı izleme veya açık saha veri setleri) Core Web Vitals'ı "iyileştirme gerekli" veya "zayıf" aralığında gösterdiğinde.
- Bir lab raporu, performans trace'i veya waterfall yorumlanıp iş kalemlerine dönüştürülmesi gerektiğinde.
- Bir sürüm kabul edilmiş performans bütçesini aşmak üzereyken veya yeniden tasarım yayından önce kontrol edilmeliyse.

## Ne zaman kullanılmaz
- Profiler ile bulunan sunucu tarafı veya algoritmik darboğazlar için `performance-optimization` kullanılır.
- Back-end kapasitesi için yük veya stres testi planlamak için `performance-test-plan` kullanılır.
- Üretimde performans hedefleri ve alarm tanımlamak için `slo-definition` veya `observability-plan` kullanılır.

## Girdiler
Zorunlu:
- Sayfa veya route ve en az bir ölçüm: saha metrikleri, lab raporu, trace, waterfall ya da ilgili HTML, kaynak listesi ve bundle boyutları.

İsteğe bağlı, kaliteyi artırır:
- Gerçek kullanıcıların cihaz ve ağ profili, hedef yüzdelik (varsayılan p75), mevcut performans bütçesi.
- Framework ve render modu (sunucu tarafı, statik, istemci tarafı, hibrit), CDN ve önbellek kurgusu.
- Üçüncü taraf script envanteri ve iş sahipleri.

Hiç ölçüm yoksa iste; ölçüm olmadan yalnızca `[VARSAYIM]` olarak işaretli olası nedenler listesi ve bir ölçüm planı ver.

## Süreç
1. Başlangıç değerlerini belirle: LCP, INP ve CLS'in p75 değerleri, cihaz sınıfı ve sayfa türüne göre ayrılmış; her sayının saha mı lab mı olduğunu belirt. Ekibin kendi bütçesi yoksa yaygın eşikleri kullan ("iyi" için LCP 2,5 sn, INP 200 ms, CLS 0,1).
2. LCP elemanını bul ve süresini alt parçalara ayır: ilk bayta kadar geçen süre (TTFB), kaynak yükleme gecikmesi, kaynak yükleme süresi, eleman render gecikmesi. Önce en büyük alt parçayı düzelt.
3. TTFB için yönlendirmeleri, sunucu yanıtını, önbellek başlıklarını, CDN isabetlerini ve HTML'in önbelleklenebilir ya da stream edilen bir yapıda olup olmadığını kontrol et.
4. Yükleme gecikmesi ve süresi için LCP kaynağının HTML'de keşfedilebilirliğini (script ile eklenmemiş, lazy-load edilmemiş), öncelik ipuçlarını, preload/preconnect'i, görsel formatını ve duyarlı boyutları, sıkıştırmayı kontrol et.
5. Render gecikmesi için render'ı engelleyen CSS ve script'leri, web font yükleme stratejisini, içerik boyanmadan önce bitmesi gereken istemci tarafı render veya hydration'ı listele.
6. INP için uzun görevleri ve onları tetikleyen etkileşimleri bul: ağır olay işleyicileri, büyük yeniden render'lar, senkron layout, ana thread'deki üçüncü taraflar. İşi bölmeyi, ana thread'e sıra vermeyi (yield), acil olmayan güncellemeleri ertelemeyi ve hydration maliyetini azaltmayı öner.
7. CLS için kayan elemanları ve nedenlerini bul: boyutu verilmemiş görsel veya gömülü içerikler, geç eklenen banner'lar, font değişimleri, layout özelliklerinin animasyonu.
8. JavaScript ve üçüncü tarafları incele: route başına bundle boyutu, kullanılmayan kod, tekrarlanan kütüphaneler, tag manager'lar ve widget'lar; her üçüncü tarafa bir sahip ve tut, ertele veya kaldır önerisi ver.
9. Düzeltmeleri beklenen metrik etkisi, güven ve eforla önceliklendir; ölçülmediyse etkiyi `[VARSAYIM]` olarak etiketle.
10. Her düzeltme için doğrulamayı tanımla: hangi metrik, hangi araç veya pano ve sonuçların saha verisinde görünmesi için gereken gecikme. CI'da uygulanan bir performans bütçesi öner veya mevcut bütçeyi güncelle.
11. Kullanıcı devam ederse back-end kaynaklı TTFB için `performance-optimization`, hedefleri resmîleştirmek için `slo-definition`, gerçek kullanıcı izleme eklemek için `observability-plan` öner.

## Çıktı formatı
```markdown
# Web Performans Denetimi: <sayfa/route>
Veri: <saha / lab / ikisi> · Cihaz ve ağ: <profil> · Yüzdelik: p75

## Başlangıç Değerleri
| Metrik | Değer | Kaynak | Hedef | Durum |
|---|---|---|---|---|

## LCP Kırılımı
- Eleman: ... · TTFB: ... · Yükleme gecikmesi: ... · Yükleme süresi: ... · Render gecikmesi: ...

## Bulgular ve Düzeltmeler
| # | Metrik | Neden (kanıt) | Düzeltme | Beklenen etki | Efor | Güven |
|---|---|---|---|---|---|---|

## Üçüncü Taraf İncelemesi
| Script | Sahip | Maliyet | Öneri |
|---|---|---|---|

## Doğrulama ve Bütçe
- ...

## Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her metrik değerinin saha mı lab mı olduğu ve hangi yüzdelikte olduğu belirtildi.
- [ ] Her bulgu bir metriği, kanıtlı somut bir nedeni ve belirli bir düzeltmeyi birbirine bağlıyor.
- [ ] LCP elemanı belirlendi ve süresi alt parçalara ayrıldı.
- [ ] Ölçüme dayanmayan etki tahminleri `[VARSAYIM]` olarak işaretli.
- [ ] Her düzeltmenin bir doğrulama adımı ve etkilemesi beklenen metriği var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Gerçek kullanıcılar orta segment telefonlardayken hızlı bir masaüstünde lab skorunu optimize etmek. Öncelikleri gerçek cihaz dağılımının saha verisine göre belirle.
- LCP görselini lazy-load etmek veya script ile eklemek; bu en önemli boyamayı geciktirir.
- Toplam bundle boyutunu hedef saymak. INP, etkileşim sırasındaki ana thread işine bağlıdır; yalnızca kilobaytı değil uzun görevleri ölç.

## Örnek
Girdi: "Ürün listeleme, mobil p75 LCP 4,8 sn, INP 350 ms. Hero görseli bir carousel script'iyle yükleniyor; 3 tag manager var."

Çıktıdan bir bölüm:
| # | Metrik | Neden (kanıt) | Düzeltme | Beklenen etki | Efor | Güven |
|---|---|---|---|---|---|---|
| 1 | LCP | Hero görseli ancak carousel script'i çalışınca keşfediliyor (trace'te yükleme gecikmesi 2,1 sn) | İlk slaytı HTML'de yüksek fetch önceliği ve açık boyutla `<img>` olarak render et; carousel'i sonra başlat | LCP -1,5 ila -2 sn `[VARSAYIM]` | S | Yüksek |
| 2 | INP | Filtre tıklaması tüm ızgarayı yeniden render eden 280 ms'lik uzun görev tetikliyor | Yalnızca değişen kartları güncelle; analitik çağrısını ertele; sonuçları render etmeden önce yield et | INP 200 ms altına `[VARSAYIM]` | M | Orta |
| 3 | INP/LCP | Üç tag manager örtüşen tag'ler yüklüyor | Tek bir tanesinde birleştir; sahipleri pazarlama teyit etsin | TBD | M | Düşük |
