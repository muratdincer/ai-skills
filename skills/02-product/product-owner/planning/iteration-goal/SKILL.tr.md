---
description: "Ekibin taahhüt ettiği sonucu, bunun neden önemli olduğunu ve başarının nasıl gözlemleneceğini belirten tek ve tutarlı bir iterasyon/sprint hedefi yazar; aday maddelerden hangilerinin hedefe hizmet ettiğini, hangilerinin etmediğini kontrol eder. İterasyon/sprint planlamasına hazırlanırken, taslak hedef sadece bir kayıt listesiyse ya da sprint hedefi veya iterasyon amacı istendiğinde kullanılır."
related: "iteration-planning, backlog-prioritization, roadmap, okr-definition, iteration-review-prep"
prompt: "Sonraki sprint adaylarımız: SSO girişi, parola sıfırlama e-postası düzeltmesi, denetim logu dışa aktarma ve iki teknik borç maddesi. Bir sprint hedefi yaz."
---

# İterasyon Hedefi Yazma

## Amaç
Ekibe iterasyon/sprint için, döngü boyunca ödünleşimlere yön veren, taahhüt sabit kalırken kapsamın esnemesine izin veren ve değerlendirme toplantısını anlamlı kılan tek bir odak sonucu vermek.

## Ne zaman kullanılır
- İterasyon/sprint planlamasından önce veya planlama sırasında.
- Önerilen hedef "101-108 numaralı kayıtları bitir" gibi okunuyorsa.
- Aday maddeler farklı yönlere çekiyorsa ve odak gerekiyorsa.
- Paydaşların "bu iterasyon ne hakkında?" sorusuna tek satırlık bir cevaba ihtiyacı varsa.

## Ne zaman kullanılmaz
- Ekip iterasyonsuz sürekli akışla çalışıyorsa; `okr-definition` ile bir hizmet veya çeyrek hedefi ya da `wip-policy` içinde bir akış hedefi kullanılır.
- Kapasite ve görev kırılımıyla tam planlama oturumu yürütülecekse `iteration-planning` kullanılır.
- Çeyrekler boyunca ürün hedefleri belirlenecekse `roadmap` veya `okr-definition` kullanılır.

## Girdiler
Zorunlu:
- İterasyon için aday backlog maddeleri ya da iterasyonun ilerletmesi gereken ürün hedefi. İkisi de yoksa sor.

İsteğe bağlı, kaliteyi artırır:
- Güncel ürün/sürüm hedefi veya OKR.
- Ekip kapasite sinyali ve bilinen kısıtlar (tatiller, olaylar).
- İterasyon içindeki paydaş beklentileri veya son tarihler.

## Süreç
1. İterasyonun ilerletmesi gereken üst seviye amacı (sürüm hedefi, OKR, yol haritası teması) belirle.
2. Aday maddeleri katkı verdikleri sonuca göre kümele; o amaç için en yüksek değer veya öğrenmeyi sağlayan kümeyi bul.
3. Hedefi tek cümlelik bir sonuç olarak yaz: "<kim> <ne yapabilir/ne deneyimler>, böylece <fayda>" ya da "<varsayımı> <kanıtla> doğrula". Madde listeleme.
4. 1-3 gözlemlenebilir sinyal içeren bir "hedefe ulaşıldığını şuradan anlarız" satırı ekle (demo senaryosu, metrik, test sonucu).
5. Her aday maddeyi eşle: hedefi destekliyor / bağımsız ama gerekli (hatalar, bakım, taahhütler) / uymuyor. Kapasite darsa neyin çıkarılacağını veya erteleneceğini öner.
6. Bağımsız işi görünür ama ikincil tut; yaygın bir yaklaşım hedefle ilgili işin kapasitenin çoğunu kullanmasıdır `[VARSAYIM: ekip normuna göre ayarla]`.
7. Hedefi şu ölçütlerle kontrol et: tek sonuç, iterasyon içinde ulaşılabilir, paydaşlar için anlamlı, ekibe kapsam pazarlığı için alan bırakıyor.
8. Odak tartışmalıysa her birinin ödünleşimiyle birlikte 2 alternatif ifade öner.

## Çıktı formatı
```markdown
# İterasyon Hedefi: <iterasyon adı/numarası>
İlerlettiği: <sürüm hedefi / OKR / tema>

**Hedef:** <tek cümle>
**Hedefe ulaşıldığını şuradan anlarız:**
- <sinyal>

## Madde Uyumu
| Madde | Hedefi destekliyor | Bağımsız ama gerekli | Uymuyor |
|---|---|---|---|

## Öneri
- Kalsın: ...
- Ertele/çıkar: ... – <gerekçe>

## Alternatif Hedefler (odak tartışmalıysa)
1. <hedef> – <ödünleşim>
```

## Kalite kontrol listesi
- [ ] Hedef, madde listesi değil bir sonucu tarif eden tek cümle.
- [ ] Başarı sinyalleri değerlendirme toplantısında gözlemlenebilir.
- [ ] Her aday madde hedefe göre sınıflandırılmış.
- [ ] Hedef kapsam pazarlığına izin veriyor (hedefe ulaşmak için tüm maddeler şart değil).
- [ ] Üst seviye amaçla bağ belirtilmiş veya `[BİLİNMİYOR]` olarak işaretli.

## Sık yapılan hatalar
- Hedef olarak "planlanan tüm hikayeleri tamamla" yazmak. Ödünleşimlere yön vermez; bunun yerine sonucu adlandır.
- "ve" ile bağlanmış birleşik hedefler. İki hedef odak yok demektir; birini seç, gerisini bağımsız iş olarak ele al.
- Ekip dışında kimsenin anlamadığı bir hedef. Bir paydaşın tekrar edebileceği biçimde yaz.

## Örnek
Girdi: "Adaylar: SSO girişi, parola sıfırlama e-postası düzeltmesi, denetim logu dışa aktarma, iki teknik borç maddesi. Sürüm hedefi: kurumsal hazırlık."

Çıktıdan bir bölüm:
**Hedef:** Kurumsal pilot kullanıcılar kurumsal kimlikleriyle oturum açabilir, böylece onboarding artık elle parola kurulumu gerektirmez.
**Hedefe ulaşıldığını şuradan anlarız:** Değerlendirme demosunda bir pilot kullanıcı staging ortamında SSO ile oturum açar.
| SSO girişi | ✓ | | |
| Parola sıfırlama e-postası düzeltmesi | | ✓ (canlı hata) | |
| Denetim logu dışa aktarma | | | ✓ sonraki iterasyona ertele |
