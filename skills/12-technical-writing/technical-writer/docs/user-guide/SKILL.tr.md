---
name: user-guide
description: "Bir ürün veya özellik için, kullanıcıların başarması gereken işler etrafında düzenlenmiş; ön koşullar, numaralı adımlar, beklenen sonuçlar, ekran görüntüsü yer tutucuları, sorun giderme ve çapraz bağlantılar içeren görev bazlı bir kullanıcı kılavuzu yazar. Son kullanıcıların veya yöneticilerin yeni ya da değişen bir özellik için dokümantasyona ihtiyaç duyduğunda, bir sürüm kullanıcıya yönelik doküman gerektirdiğinde veya mevcut kılavuz özellik odaklı olup zor takip edildiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 12-technical-writing
  role: technical-writer
  area: docs
  title: "Kullanıcı kılavuzu yazma"
  related: "how-to-guide, tutorial, docs-information-architecture, style-guide-check, faq-builder"
  prompt: "Bu spesifikasyonlara ve ekran adlarına göre finans onaylayıcıları için yeni fatura onay akışımızın kullanıcı kılavuzu bölümünü yaz."
---

# Kullanıcı Kılavuzu Yazma

## Amaç
Belirli bir hedef kitleye, ürünle gerçek işleri doğru ve güvenle tamamlamaları için ihtiyaç duydukları dokümantasyonu, ürünün menülerine göre değil onların hedeflerine göre düzenlenmiş olarak sunmak.

## Ne zaman kullanılır
- Yeni veya değişen bir özellik son kullanıcı ya da yönetici dokümantasyonu gerektirdiğinde.
- Mevcut kılavuz ekranları ve alanları anlatıyor ama işin nasıl yapılacağını anlatmıyorsa.
- Destek kayıtları kullanıcıların aynı görevlerde tekrar tekrar zorlandığını gösteriyorsa.

## Ne zaman kullanılmaz
- Yeni başlayan birine tek bir yönlendirilmiş öğrenme yolu sunulacaksa `tutorial` kullanılır.
- Deneyimli kullanıcılar için tek ve odaklı bir tarif gerekiyorsa `how-to-guide` kullanılır.
- Bütün bir doküman seti düzenlenecekse `docs-information-architecture` kullanılır.

## Girdiler
Zorunlu:
- Ürün veya özellik ve davranışı (spesifikasyonlar, hikâyeler, arayüz etiketleri, demo notları veya ekranların tarifleri).
- Hedef kitle (rol, deneyim seviyesi).

İsteğe bağlı, kaliteyi artırır:
- Stil rehberi ve terim listesi, mevcut dokümanlar, destek kaydı temaları.
- Yetkiler ve roller, bilinen kısıtlar, sürüm numarası.

Özelliğin davranışı veya hedef kitle bilinmiyorsa iste. Girdinin doğrulamadığı arayüz öğelerini veya davranışları anlatma.

## Süreç
1. Hedef kitleyi ve hedeflerini tanımla; özellikle yaptıkları başlıca görevleri sıklık ve önem sırasına göre listele.
2. Görev taslağını kur: genel bakış, ön koşullar (erişim, roller, veri), temel görevler, ileri görevler, sorun giderme, referans (alanlar, durumlar, sınırlar).
3. Her görev için ekranı değil hedefi adlandıran, emir kipinde bir başlık yaz ("Fatura onaylama" yerine "Faturayı onaylayın" gibi, stil rehberine uygun biçimde).
4. Bir iki cümlelik bağlam yaz: bu görev ne zaman ve neden yapılır.
5. Göreve özgü ön koşulları listele (yetkiler, önceki adımlar, gerekli veri).
6. Numaralı adımları yaz: adım başına tek eylem, kalın yazılmış birebir arayüz etiketleri ve kullanıcının yaşadığı sıra; önemli olduğu yerde sonucu adımın ardından ver ("Fatura Onaylandı durumuna geçer").
7. Ekran görüntüsü veya diyagram yer tutucularını yalnızca belirsizliği azalttığı yerlere, amacını anlatan alternatif metinle ekle: `[Ekran görüntüsü: <ne gösterdiği>]`.
8. Not, uyarı ve ipuçlarını az kullan ve ilgili adımdan önce yerleştir; uyarılar sonucu ve nasıl önleneceğini anlatır.
9. Sorun giderme maddelerini bilinen sorunlardan veya destek temalarından belirti → neden → çözüm olarak yaz; tahminleri gözden geçirme için `[VARSAYIM]` olarak işaretle.
10. Doğrulanmamış her davranışı, etiketi veya sınırı `[TBD – ürün ekibiyle teyit et]` olarak işaretle ve konu uzmanı için gözden geçirme soruları olarak listele.
11. Kullanıcının hedefi devam ediyorsa yayından önce `style-guide-check`, tekrarlayan sorular için `faq-builder` ya da kılavuzu doküman setine yerleştirmek için `docs-information-architecture` öner.

## Çıktı formatı
```markdown
# <Özellik> Kullanıcı Kılavuzu
Hedef kitle: <rol> | Geçerli olduğu sürüm: <ürün/sürüm> | Son gözden geçirme: <tarih veya TBD>

## Genel Bakış
<özelliğin bu kitle için ne yaptığı, 2-3 cümle>

## Başlamadan Önce
- <erişim, rol, veri>

## <Görev 1: emir kipinde hedef>
<bağlam cümlesi>
**Ön koşullar:** ...
1. **<Menü>** > **<Sayfa>** bölümüne gidin.
2. **<Düğme>** seçeneğini seçin.
   <Nesne> açılır. [Ekran görüntüsü: <ne gösterdiği>]
3. ...
> **Uyarı:** <sonuç ve nasıl önleneceği>

**Sonuç:** <iş bittiğinde kullanıcının gördüğü>

## Sorun Giderme
| Belirti | Neden | Çözüm |

## Referans
| Alan / durum | Anlamı | İzin verilen değerler |

## Konu Uzmanı İçin Gözden Geçirme Soruları
```

## Kalite kontrol listesi
- [ ] Görevler ekranlara veya özelliklere göre değil, kullanıcı hedeflerine göre adlandırıldı.
- [ ] Her adımda tek eylem var ve birebir arayüz etiketleri kullanıldı.
- [ ] Her görev, kullanıcının başardığını anlaması için sonucunu belirtiyor.
- [ ] Davranış veya arayüzle ilgili hiçbir şey uydurulmadı; doğrulanmamış maddeler `[TBD]` olarak işaretli.
- [ ] Uyarılar riskli adımdan sonra değil, önce yer alıyor.
- [ ] Dil belirtilen hedef kitleye uygun ve verildiyse stil rehberine uyuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Arayüzü alan alan anlatmak ("Durum alanı durumu gösterir"). Kullanıcının ne yaptığını ve neden yaptığını anlat.
- Kavramsal açıklamayı adımların içine karıştırmak. Kavramları genel bakışta veya bağlantılı bir açıklamada tut.
- Her adıma ekran görüntüsü koymak; hızla eskir. Yalnızca metnin belirsiz kaldığı yerlerde kullan.

## Örnek
Girdi: "Finans onaylayıcıları 10 binin üzerindeki faturaları Onaylar kutusundan onaylayabilir veya reddedebilir; ret için gerekçe zorunlu."

Çıktıdan bir bölüm:
- Zayıf: "Onaylar ekranı: Bu ekranda Onayla ve Reddet düğmeleri vardır."
- Güçlü: "## Bir faturayı reddedin / 1. **Onaylar** bölümünde faturayı açın. 2. **Reddet**'i seçin. 3. Gerekçeyi **Ret gerekçesi** alanına girin (zorunlu). 4. **Onayla**'yı seçin. **Sonuç:** Fatura, gerekçenizle birlikte gönderene geri döner. `[TBD – gönderene e-posta bildirimi gidip gitmediğini teyit et]`"
