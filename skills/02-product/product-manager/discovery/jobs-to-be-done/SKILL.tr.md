---
description: Çözümden bağımsız bir temel iş ifadesi, ilişkili ve duygusal/sosyal işler, iş adımları ile önem ve memnuniyete göre önceliklendirilebilecek ölçülebilir istenen sonuç ifadeleri yazarak Yapılacak İşler (JTBD) çerçevesini kurar. Müşterilerin neyi başarmaya çalıştığı tanımlanırken, inovasyon veya yol haritası çalışması çözümden bağımsız bir çerçeveye ihtiyaç duyduğunda ya da JTBD, iş hikâyeleri veya istenen sonuçlar istendiğinde kullanılır.
related: persona, opportunity-solution-tree, customer-journey-map, problem-interview-script, feedback-synthesis
prompt: Tedarikçi siparişlerini yöneten restoran sahipleri için yapılacak işleri (JTBD) çerçevele.
---

# Yapılacak İşler (JTBD)

## Amaç
Müşterilerin herhangi bir üründen bağımsız olarak sağlamak istediği ilerlemeyi tanımlamak. Böylece ekipler karşılanmamış ihtiyaçları bulabilir, çözümleri adil biçimde kıyaslayabilir ve müşterinin değer verdiği şeye göre önceliklendirebilir.

## Ne zaman kullanılır
- Bir problem alanında keşfe başlarken veya fikir üretiminden önce.
- Yol haritası özellik güdümlüyse ve müşteri ilerlemesi çerçevesine ihtiyaç varsa.
- Ürününüz, müşterilerin bugün "işe aldığı" belirgin olmayan alternatiflerle kıyaslanırken.

## Ne zaman kullanılmaz
- Bir kullanıcı grubunun davranış profili gerekiyorsa `persona` kullanılır.
- Sonuçları çözümlere ve deneylere bağlamak gerekiyorsa `opportunity-solution-tree` kullanılır.
- İş verisini toplamak için görüşme rehberi gerekiyorsa `problem-interview-script` kullanılır.

## Girdiler
Zorunlu:
- Hedef müşteri (işi yapan kişi) ve problem alanı veya durum.

İsteğe bağlı, kaliteyi artırır:
- Görüşme notları, geçiş hikâyeleri (müşterinin bir çözümden diğerine neden geçtiği), destek ve yorum verisi.

İşi yapan kişi veya durum yoksa sor. Araştırmayla desteklenmeyen ifadeler `[VARSAYIM]` olarak işaretlenir.

## Süreç
1. İşi yapan kişiyi ve diğer rolleri (satın alan, onaylayan, faydalanan) belirle.
2. Temel işlevsel işi "fiil + nesne + bağlam belirleyici" olarak, çözüm veya teknoloji kelimesi kullanmadan yaz ("mutfağı en az israfla malzemeyle donatılmış tutmak").
3. İlişkili işleri ve duygusal/sosyal işleri ekle ("kontrolde hissetmek", "personel tarafından güvenilir görülmek").
4. İş adımlarını evrensel iş haritasıyla çıkar: tanımla, bul, hazırla, teyit et, uygula, izle, düzelt, sonuçlandır.
5. Her adım için istenen sonuç ifadeleri yaz: "<adım bağlamında> <istenmeyen sonucun> süresini/olasılığını en aza indir". Ölçülebilir ve zaman içinde kalıcı olsunlar.
6. Yararlı olduğu yerde durumu/tetikleyiciyi iş hikâyeleriyle yakala: "<durum> olduğunda, <motivasyon> istiyorum, böylece <beklenen sonuç>".
7. Bugün işe alınan çözümleri ve eksiklerini listele; hiç çözüm kullanmamayı (non-consumption) da dahil et.
8. Sonuçların nasıl önceliklendirileceğini (önem-memnuniyet anketi) öner ve kanıtlara göre muhtemelen yeterince karşılanmayan sonuçları işaretle.
9. Girdide yazmayan, senin çıkardığın her noktayı `[VARSAYIM]` olarak işaretle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: yeterince karşılanmayan sonuçları fırsatlara çevirmek için `opportunity-solution-tree`, eksik kanıtı toplamak için `problem-interview-script`.

## Çıktı formatı
```markdown
# Yapılacak İşler: <işi yapan kişi> — <durum>
**Temel iş:** <fiil + nesne + bağlam belirleyici>
İlişkili işler: ... · Duygusal/sosyal işler: ...

## İş Haritası ve İstenen Sonuçlar
| Adım | İstenen sonuç ifadeleri | Kanıt |
|---|---|---|
| Tanımla | ... en aza indir | ... |

## İş Hikâyeleri
- ... olduğunda, ... istiyorum, böylece ...

## Mevcut Çözümler ve Eksikleri
- ...

## Muhtemelen Yeterince Karşılanmayan Sonuçlar
- ...

## Sonraki Araştırma
- Sonuçlar üzerinde önem/memnuniyet anketi ...
```

## Kalite kontrol listesi
- [ ] Temel iş ürün, özellik veya teknoloji içermiyor.
- [ ] Sonuç ifadeleri ölçülebilir (süre, olasılık, sayı) ve çözümden bağımsız.
- [ ] Duygusal ve sosyal işler değerlendirildi.
- [ ] Mevcut çözümler arasında çözümsüzlük ve geçici çözümler yer alıyor.
- [ ] Varsayıma dayalı maddeler `[VARSAYIM]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İşi yanlış seviyede yazmak ("dışa aktar'a tıkla"). Kalıcı bir hedefe ulaşana kadar "neden?" diye sor.
- İhtiyaçla çözümü karıştırmak ("yeniden sipariş için bir uygulama"). Çözümü çıkar, ilerlemeyi bırak.
- İş ifadesinde durmak. Asıl değer, önceliklendirmede kullanılan sonuç ifadelerindedir.

## Örnek
Girdi: "Tedarikçi siparişlerini yöneten restoran sahipleri."

Çıktıdan bir bölüm:
- Temel iş: Mutfağı yaklaşan servis için doğru malzemelerle, en az israfla donatılmış tutmak.
- Sonuç (İzle): Servis başladıktan sonra eksik bir malzemeyi fark etme olasılığını en aza indir.
- Mevcut çözümler: kâğıt üzerinde stok sayımı, tedarikçiyi telefonla aramak, tampon olarak fazla sipariş vermek.
