---
description: "Backlog maddelerini açık ve savunulabilir bir yöntemle (WSJF, RICE, değer/efor, MoSCoW veya gecikme maliyeti) sıralar; puanlar, gerekçeler, duyarlılık notları ve ertelenecek veya çıkarılacak maddelerle birlikte sıralı bir liste üretir. Ürün sahibinin sıradaki işe karar vermesi gerektiğinde, paydaşlar öncelikler konusunda anlaşamadığında ya da backlog sırasının puanlanması ve gerekçelendirilmesi istendiğinde kullanılır."
related: "backlog-refinement, requirements-prioritization, portfolio-prioritization, roadmap, decision-matrix"
prompt: "Bu 12 backlog maddesini WSJF ile önceliklendir; efor tahminleri tabloda, değer bilgisi satış ve destek geri bildirimlerinden geliyor."
---

# Backlog Önceliklendirme

## Amaç
Paydaşların görüşler üzerinden değil girdiler üzerinden inceleyip itiraz edebileceği bir backlog sırası üretmek. Çıktı hangi yöntemin neden kullanıldığını, her maddenin nasıl puanlandığını ve sıralamanın ne kadar kararlı olduğunu gösterir.

## Ne zaman kullanılır
- Sonraki iterasyon/sprint, sürüm veya çeyrek için kapasiteden fazla aday madde olduğunda.
- Birden fazla paydaş rakip talepler öne sürdüğünde ve ürün sahibinin şeffaf bir dayanağa ihtiyacı olduğunda.
- Sıranın yönetime veya ekibe açıklanması gerektiğinde.

## Ne zaman kullanılmaz
- Maddeler hâlâ belirsiz veya çok büyükse önce `backlog-refinement` kullanılır.
- Bir portföydeki projeler veya girişimler sıralanacaksa `portfolio-prioritization` kullanılır.
- Tek bir gereksinim dokümanı içindeki gereksinimler önceliklendirilecekse `requirements-prioritization` kullanılır.

## Girdiler
Zorunlu:
- Önceliklendirilecek maddelerin listesi.
- Sıralamanın hizmet edeceği hedef veya sonuç (iterasyon hedefi, OKR, sürüm teması). Yoksa sor; hedef olmadan puanlar keyfi olur.

İsteğe bağlı, kaliteyi artırır:
- Efor veya boyut tahminleri, erişim/kullanım verisi, gelir veya maliyet sinyalleri, son tarihler, risk notları.
- Tercih edilen yöntem veya kurum standardı.
- Sabit kısıtlar (yasal tarihler, sözleşme taahhütleri, bağımlılıklar).

## Süreç
1. Yöntemi seç ve nedenini yaz: gecikme maliyeti değişkense ve son tarihler önemliyse WSJF; erişim verisi varsa RICE; hızlı bir ilk eleme için değer/efor 2x2; sabit tarihli kapsam pazarlığı için MoSCoW. Kurumun bir yöntemi varsa onu kullan.
2. Her puanlama boyutunu ölçek ve referans noktalarıyla tanımla (ör. en küçük maddeye göre 1, 2, 3, 5, 8, 13), böylece puanlar karşılaştırılabilir olur.
3. Pazarlığa kapalı maddeleri (yasal son tarihler, sözleşmesel yükümlülükler, güvenlik düzeltmeleri, zorunlu bağımlılıklar) ayır ve etiketleyerek en başa koy; bunları puanlamaya katma.
4. Kalan maddeleri puanla. Her puanın dayandığı kanıtı belirt; kanıt yoksa geçici bir puan ver ve `[VARSAYIM]` olarak işaretle.
5. Sonucu hesapla (WSJF = gecikme maliyeti / iş büyüklüğü; RICE = erişim x etki x güven / efor) ve sırala.
6. Bağımlılıkları kontrol et: bir madde bağımlı olduğu maddenin üstünde yer alamaz; düzelt ve not düş.
7. Duyarlılık kontrolü yap: varsayılan bir puan bir adım değişirse hangi maddelerin sırası değişiyor? Bunları "sıraya duyarlı" olarak işaretle.
8. Ertelenecek veya çıkarılacak adayları belirle (en düşük puanlılar, hedefle bağı olmayanlar) ve yapılmamalarının sonucunu yaz.
9. Kapasite biliniyorsa listenin üst kısmını kapasiteyle karşılaştır; bilinmiyorsa kesme çizgisini `[TBD]` olarak göster.

## Çıktı formatı
```markdown
# Backlog Önceliklendirme: <ürün> – <tarih>
Hizmet edilen hedef: <hedef>
Yöntem: <yöntem> – <neden seçildi>
Ölçekler: <boyut: referans noktaları>

## Önce Taahhüt Edilenler (puanlanmadı)
- <madde> – <gerekçe: yasal/sözleşme/bağımlılık/güvenlik>

## Sıralı Maddeler
| Sıra | Madde | <boyut 1> | <boyut 2> | <boyut 3> | Boyut | Puan | Kanıt / varsayım | Sıraya duyarlı |
|---|---|---|---|---|---|---|---|---|

## Kesme Çizgisi
Kapasite: <değer veya [TBD]> → 1–<n> arası maddeler sığıyor.

## Ertele veya Çıkar
- <madde> – <yapılmamasının sonucu>

## Gereken Kararlar
- <karar> – <kim> – <ne zamana kadar>
```

## Kalite kontrol listesi
- [ ] Seçilen yöntem ve ölçek referans noktaları belirtildi.
- [ ] Her puanın kanıtı ya da `[VARSAYIM]` işareti var.
- [ ] Zorunlu maddeler puanların içine gizlenmedi, ayrı gösterildi.
- [ ] Hiçbir madde bağımlı olduğu maddenin üstünde değil.
- [ ] Sıraya duyarlı maddeler işaretlendi.
- [ ] Parasal veya kullanım rakamları yalnızca girdide verildiyse yer alıyor.

## Sık yapılan hatalar
- Sahte kesinlik: WSJF 4,33 ile 4,25 arasındaki farkı gerçek bir fark gibi sunmak. Yakın puanları eşit say ve hedefe uyuma göre karar ver.
- MoSCoW kapsamının %80'inin "Must" olması. Must oranını kapasitenin yaklaşık %60'ının altında tut, yoksa planda esneklik kalmaz.
- Gözde maddelere şişirilmiş değer verip yalnızca eforu bölen olarak kullanmak. Değer puanlarını paydaşların üzerinde anlaştığı bir referans maddeye göre sabitle.

## Örnek
Girdi: "A (dışa aktarma, boyut 3), B (SSO, boyut 8), C (KVKK silme, Q3'te yasal son tarih), D (karanlık mod, boyut 2). Hedef: kurumsal müşteri kaybını azaltmak."

Çıktıdan bir bölüm:
- Önce taahhüt edilen: C – yasal son tarih, puanlanmadı.
| 1 | B SSO | İD 8 | ZK 5 | RA 8 | 8 | 2,6 | Kurumsal kayıp görüşmeleri SSO'yu işaret ediyor | Evet |
| 2 | A Dışa aktarma | 3 | 2 | 3 | 3 | 2,7 | B (2,6) ile eşit; hedef uyumu nedeniyle B önde | Hayır |
- Ertele: D karanlık mod – kurumsal kayıp hedefiyle bağı yok.
