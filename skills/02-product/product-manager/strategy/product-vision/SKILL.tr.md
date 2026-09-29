---
name: product-vision
description: "Hedef kitle, ihtiyaçlar, ürün ve iş hedeflerini kapsayan, ilham veren ve sınanabilir bir ürün vizyonu cümlesi ile vizyon panosu yazar. Yeni bir ürün veya büyük bir yön değişikliği ortak bir yöne ihtiyaç duyduğunda, ekipler ürünün ne için var olduğunda anlaşamadığında ya da vizyon cümlesi veya vizyon panosu istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: strategy
  title: "Ürün vizyonu yazma"
  related: "product-strategy-one-pager, positioning-statement, north-star-metric, persona, okr-definition"
  prompt: "Küçük işletme müşterilerimize yönelik self-servis fatura portalı için ürün vizyonu ve vizyon panosu yaz."
---

# Ürün Vizyonu Yazma

## Amaç
Ürünün kime hizmet ettiğini, hangi ihtiyacı karşıladığını ve nasıl bir değişim yarattığını anlatan kısa bir vizyon cümlesi ve vizyon panosu üretmek. İyi bir vizyon yıllarca sabit kalır, ödünleşimlere yön verir ve strateji, yol haritası ile OKR'ların ona göre sınanmasını sağlar.

## Ne zaman kullanılır
- Yeni bir ürün, ürün hattı veya büyük bir yön değişikliği başlarken ekiplerin tek bir ortak yöne ihtiyacı olduğunda.
- Paydaşlar ürünü birbiriyle çelişen biçimlerde tarif ettiğinde ya da yol haritası amaçsız bir özellik listesine dönüştüğünde.
- Mevcut vizyon karar almaya yardım etmeyen bir slogandan ibaretse ve yeniden yazılması gerekiyorsa.

## Ne zaman kullanılmaz
- Önümüzdeki 12-24 ay için nerede oynanacağı ve nasıl kazanılacağı seçimleri gerekiyorsa `product-strategy-one-pager` kullanılır.
- Pazara dönük farklılaşma metni gerekiyorsa `positioning-statement` kullanılır.
- Ölçülebilir çeyreklik hedefler gerekiyorsa `okr-definition` kullanılır.

## Girdiler
Zorunlu:
- Ürün veya ürün fikri ve ele aldığı problem alanı.

İsteğe bağlı, kaliteyi artırır:
- Hedef kullanıcılar/müşteriler ve araştırma kanıtları (görüşmeler, personalar, veri).
- Şirket misyonu ve stratejisi, iş hedefleri, ürünün mevcut durumu.
- Kullanıcıların bugün başvurduğu rakipler veya alternatifler.

Ürün veya problem alanı yoksa iste. Geri kalan her şey varsayım ya da açık soru olarak kaydedilir.

## Süreç
1. Problem alanını tek satırda yeniden yaz: kimin hayatı veya işi, hangi durumda iyileşiyor.
2. Vizyonu (dünyada kalıcı değişim), ürünü (bir araç) ve hedefleri (iş faydası) birbirinden ayır. Vizyon cümlesine özellik koyma.
3. Hedef kitleyi belirle: önce birincil segment, ikincil segmentleri yalnızca ürün gerçekten onlara hizmet ediyorsa ekle. Desteklenmeyen segmentleri `[VARSAYIM]` olarak işaretle.
4. Ürünün karşıladığı en önemli 1-3 ihtiyacı veya işi adlandır; kanıta dayalı ihtiyaçları tercih et ve kaynağını belirt.
5. Ürünü özellik listesiyle değil, 3-5 farklılaştırıcı nitelikle tarif et.
6. Vizyonun mümkün kıldığı iş hedeflerini (gelir, elde tutma, maliyet, stratejik konum) nitel olarak yaz; asla rakam uydurma.
7. 2-3 alternatif vizyon cümlesi taslağı çıkar (tek cümle, ~25 kelimeden kısa, sade dil) ve kontrol listesini en iyi geçeni seç.
8. Cümleyi sına: Bir rakip de aynısını söyleyebilir mi? 3-5 yıl sonra da geçerli olur mu? Bir şeye "hayır" demeye yardım ediyor mu? Cevaplar hayır/evet/evet olana kadar düzelt.
9. Ödünleşimleri açık hale getirmek için "bu vizyonun dışarıda bıraktıkları" listesini ekle.
10. Doğrulanacak varsayımları ve sorumlusu belli açık soruları listele.
11. Girdide yazmayan, senin çıkardığın her noktayı `[VARSAYIM]` olarak işaretle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: vizyona nasıl ulaşılacağına karar vermek için `product-strategy-one-pager`, ilerlemeyi ölçmek için `north-star-metric`.

## Çıktı formatı
```markdown
# Ürün Vizyonu: <ürün>
**Vizyon cümlesi:** <tek cümle>

## Vizyon Panosu
| Hedef kitle | İhtiyaçlar | Ürün | İş hedefleri |
|---|---|---|---|
| <birincil / ikincil segment> | <kanıtıyla en önemli ihtiyaçlar> | <3-5 farklılaştırıcı nitelik> | <nitel hedefler> |

## Bu Vizyonun Dışarıda Bıraktıkları
- ...

## Değerlendirilen Alternatifler
1. <cümle> — <neden seçilmedi>

## Doğrulanacak Varsayımlar
- [VARSAYIM] ... — <nasıl doğrulanacak>

## Açık Sorular
1. <soru> — <sorumlu>
```

## Kalite kontrol listesi
- [ ] Cümle tek cümle, jargonsuz ve özellik adı içermiyor.
- [ ] Hedef kitle ve ihtiyaç birilerini dışarıda bırakacak kadar somut.
- [ ] İhtiyaçlar bir kanıta dayanıyor ya da `[VARSAYIM]` olarak işaretli.
- [ ] İş hedefleri nitel veya kaynaklı; uydurma rakam yok.
- [ ] "Dışarıda bıraktıkları" listesinde en az iki gerçek ödünleşim var.
- [ ] Vizyon 15 saniyeden kısa sürede sesli okunabiliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tüm şirketin misyonunu veya bir pazarlama sloganını yazmak. Bu ürünün kullanıcılarına ve yarattığı değişime odaklan.
- Her paydaşın isteğini cümleye doldurmak. Her şeyi kapsayan vizyon hiçbir şeye yön vermez.
- Vizyona zamana bağlı hedef ("2027'ye kadar 1 milyon kullanıcı") eklemek. Hedefleri OKR'lara veya stratejiye taşı.

## Örnek
Girdi: "Küçük işletme müşterileri için self-servis fatura portalı; bugün fatura kopyası almak ve itiraz etmek için çağrı merkezini arıyorlar."

Çıktıdan bir bölüm:
- Vizyon cümlesi: Küçük işletme sahipleri her faturayı bizi aramaya gerek kalmadan kendi başlarına anlar ve kapatır.
- İhtiyaçlar: Geçmiş faturaları hızla bulmak; beklenmedik kalemleri anlamak; hatta beklemeden itiraz etmek (çağrı kayıtları `[hacmi teyit et]`).
- Dışarıda bıraktıkları: Genel bir muhasebe aracına dönüşmek; kurumsal satın alma süreçlerine hizmet etmek.
