---
name: assumption-mapping
description: "Bir planın, ürün fikrinin, tahminin veya kararın arkasındaki varsayımları ortaya çıkarır, türlerine göre sınıflar (arzu edilebilirlik, kullanılabilirlik, fizibilite, ekonomik yapılabilirlik, etik/mevzuat, teslimat), önem ve kanıta göre konumlandırır ve en riskli olanları en ucuz testle birlikte test edilebilir ifadelere çevirir. Bütçe veya kapsam taahhüdünden önce, bir plan fazla iyimser göründüğünde ya da bunun işe yaraması için neyin doğru olması gerektiği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: thinking-tools
  area: problem
  title: "Varsayım haritalama"
  related: "hypothesis-statement, experiment-design, pre-mortem, risk-register, problem-statement"
  prompt: "KOBİ müşterileri için gelecek çeyrekte self-servis oryantasyon başlatma planımızın varsayımlarını haritala."
---

# Varsayım Haritalama

## Amaç
Bir planın başarılı olması için neyin doğru olması gerektiğini görünür kılmak ve doğrulama emeğini, pahalı sürprizlere dönüşmeden önce hem kritik hem de zayıf kanıtlı birkaç varsayıma odaklamak.

## Ne zaman kullanılır
- Yeni bir ürün, özellik, girişim veya iş gerekçesi onaylanmak ya da fonlanmak üzereyse.
- Bir plan, yol haritası veya tahmin kimsenin kontrol etmediği inançlara dayanıyorsa.
- Ekip anlaşmazlık içinde ve anlaşmazlık aslında dile getirilmemiş inançlarla ilgiliyse.

## Ne zaman kullanılmaz
- Amaç teslimatta ters gidebilecekleri listelemekse `pre-mortem` veya `risk-register` kullanılır.
- Tek bir varsayım zaten seçilmiş ve resmi bir teste ihtiyaç duyuyorsa `hypothesis-statement` ve `experiment-design` kullanılır.
- Problemin kendisi henüz tanımlanmamışsa `problem-statement` kullanılır.

## Girdiler
Zorunlu:
- Plan, fikir veya karar ve hedeflenen sonucu.

İsteğe bağlı, kaliteyi artırır:
- Hedef kullanıcılar veya müşteriler, iş modeli, zaman çizelgesi, bağımlılıklar.
- Mevcut kanıtlar (araştırma, veri, pilotlar, kıyaslamalar).
- Bilinen kısıtlar (bütçe, mevzuat, teknoloji).

Plan veya hedeflenen sonucu yoksa iste. Bir seferde en fazla beş odaklı soru sor; geri kalan her şey açık soru olur.

## Süreç
1. Planı ve hedeflenen sonucu birer cümleyle yeniden ifade et.
2. Varsayımları "Bunun işe yaraması için şunun doğru olması gerekir..." kalıbıyla çıkar. Belirtilenleri ve çıkarımla bulduğun örtük olanları dahil et; çıkarımla bulunanları `[ÇIKARIM]` olarak işaretle.
3. Her birini bir konu ("oryantasyon") olarak değil, tek ve yanlışlanabilir bir inanç olarak yaz ("KOBİ yöneticileri kurulumu telefon görüşmesi olmadan tamamlar").
4. Her birini sınıfla: arzu edilebilirlik (istiyorlar), kullanılabilirlik (kullanabiliyorlar), fizibilite (inşa edip işletebiliriz), ekonomik yapılabilirlik (karşılığını verir), etik/mevzuat (iznimiz var), teslimat (bu ekiple zamanında yapabiliriz).
5. Önemi puanla: yanlışsa plan çöker mi (Yüksek), zayıflar mı (Orta), yoksa pek değişmez mi (Düşük)?
6. Kanıtı puanla: Güçlü (gözlenmiş davranış, veri), Kısmi (beyan edilen niyet, benzetmeler, uzman görüşü), Yok (inanç).
7. Varsayımları 2x2 matrise yerleştir: yüksek önem / zayıf kanıt = önce test et; yüksek önem / güçlü kanıt = izle; düşük önem = park et.
8. "Önce test et" maddelerinin her biri için geçme eşiği olan test edilebilir bir ifade ve en ucuz güvenilir testi (veri sorgusu, görüşme, prototip, smoke test, spike, hukuki inceleme) yaz; sorumlu rolü ve süre sınırını ekle.
9. Bağımlılıkları not et: hangi varsayımlar yanlış çıkarsa diğerlerini geçersiz kılar.
10. Devam/dur kararını neyin değiştireceğini ve hangi varsayımların test edilmemiş kaldığını özetle.
11. Kullanıcının hedefi devam ediyorsa öncelikli maddeler için `hypothesis-statement` ve `experiment-design`, teslimatla ilgili olanları izlemek için `risk-register` öner.

## Çıktı formatı
```markdown
# Varsayım Haritası: <plan>

**Plan:** <tek cümle> **Hedeflenen sonuç:** <tek cümle>

| # | Varsayım (yanlışlanabilir) | Tür | Önem | Kanıt | Bölge | Kaynak |
|---|---|---|---|---|---|---|
| V1 | ... | Arzu edilebilirlik | Y | Yok | Önce test et | Belirtilen / [ÇIKARIM] |

## Önce Test Et
| # | Test edilebilir ifade | Geçme eşiği | En ucuz test | Sorumlu (rol) | Süre sınırı |
|---|---|---|---|---|---|
| V1 | İnanıyoruz ki ... | <eşik veya [TBD]> | ... | ... | ... |

## İzle
- ...

## Park Edilenler
- ...

## Bağımlılıklar ve Karara Etkisi
- V1 yanlışsa ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her varsayım bir konu değil, tek ve yanlışlanabilir bir cümle.
- [ ] Altı türün tamamı değerlendirildi; boş kalan türler bilinçli bir sonuç.
- [ ] Çıkarımla bulunan varsayımlar `[ÇIKARIM]` olarak işaretli; kaynağı olmadan hiçbir şey kanıt olarak sunulmamış.
- [ ] Her "önce test et" maddesinin bir eşiği, testi ve sorumlu rolü var.
- [ ] Kullanıcının vermediği eşik ve sayılar uydurulmamış, `[TBD]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Teknik ekipler için rahat olduğundan yalnızca fizibilite varsayımlarını listelemek. Planları çoğunlukla arzu edilebilirlik ve ekonomik yapılabilirlik öldürür.
- Paydaşların inancını kanıt saymak. Görüş en iyi ihtimalle "Kısmi"dir.
- Önce pahalı testler tasarlamak. Varsayımı yanlışlayabilecek en ucuz testle başla.

## Örnek
Girdi: "KOBİ müşterileri için gelecek çeyrekte self-servis oryantasyon başlatmayı planlıyoruz."

Çıktıdan bir bölüm:
| # | Varsayım | Tür | Önem | Kanıt | Bölge |
|---|---|---|---|---|---|
| V1 | KOBİ yöneticileri kurulumu destek hattını aramadan bitirebilir. | Kullanılabilirlik | Y | Yok | Önce test et |
| V2 | Self-servis, oryantasyon maliyetini geliştirme maliyetini karşılayacak kadar düşürür. | Ekonomik yapılabilirlik | Y | Kısmi – oryantasyon başı maliyet biliniyor, efor [TBD] | Önce test et |
| V3 | Kimlik doğrulama mevcut mevzuat altında çevrim içi yapılabilir. | Mevzuat | Y | Yok `[ÇIKARIM]` | Önce test et |

V1 testi: 5-8 KOBİ yöneticisiyle moderatörsüz prototip testi; [TBD — eşik üzerinde uzlaşın] kişi yardımsız kurulumu tamamlarsa geçer.
