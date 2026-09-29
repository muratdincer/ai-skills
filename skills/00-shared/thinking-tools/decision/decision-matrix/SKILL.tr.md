---
name: decision-matrix
description: "Seçenekleri açık ağırlıklara, puanlama ölçeklerine ve eleyici zorunlu kurallara sahip, üzerinde uzlaşılmış ve birbirinden bağımsız kriterlere göre karşılaştıran ağırlıklı bir karar matrisi oluşturur; ardından sonucun ağırlıklara ve belirsiz puanlara ne kadar duyarlı olduğunu test eder. Üç veya daha fazla seçenek (tedarikçi, teknoloji, tasarım, yatırım adayı) arasında seçim yapılırken, kararın başkalarına savunulabilir olması gerektiğinde veya bir grubun uzlaşması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: thinking-tools
  area: decision
  title: "Ağırlıklı karar matrisi"
  related: "trade-off-analysis, pros-cons, vendor-evaluation, technology-selection, decision-log"
  prompt: "Sipariş platformumuz için üç mesaj kuyruğu (broker) arasında seçim yapmak üzere ağırlıklı bir karar matrisi oluştur."
---

# Ağırlıklı Karar Matrisi

## Amaç
Çok seçenekli bir tercihi şeffaf ve tekrarlanabilir bir karşılaştırmaya dönüştürmek; böylece karar, en iyi savunanın görüşüne değil, paydaşların sorgulayabileceği açık kriterlere ve ağırlıklara dayanır.

## Ne zaman kullanılır
- Üç veya daha fazla seçeneğin birkaç kritere göre karşılaştırılması gerekiyorsa.
- Karar daha sonra denetlenecek, incelenecek veya sorgulanacaksa.
- Paydaşlar farklı şeylere değer veriyor ve uzlaşmak için ortak bir çerçeveye ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- Yalnızca iki seçenek veya evet/hayır kararı için hızlı ve dengeli bir bakış gerekiyorsa `pros-cons` kullanılır.
- Asıl soru hangi seçeneğin en yüksek puanı aldığı değil, her seçeneğin neyi feda ettiğiyse `trade-off-analysis` kullanılır.
- Seçim, RFP puanlama kuralları olan resmi bir tedarikçi satın alma süreciyse `vendor-evaluation` kullanılır.

## Girdiler
Zorunlu:
- Verilecek karar ve seçenekler (en az iki; tercihen üç veya daha fazla).

İsteğe bağlı, kaliteyi artırır:
- Paydaşların önceden uzlaştığı kriterler ve ağırlıklar.
- Seçenek başına olgular (maliyet, yetenekler, referanslar, test sonuçları).
- Kesin kısıtlar (bütçe tavanı, mevzuat, uyumluluk).

Karar veya seçenekler yoksa iste. Kriterler yoksa öner ve `[ÖNERİ — teyit et]` olarak işaretle.

## Süreç
1. Kararı kapsamı ve karar sahibiyle birlikte bir soru olarak ifade et ("Sipariş platformu önümüzdeki 3+ yıl hangi broker'ı kullanacak?").
2. Zorunlu kısıtları eleyici kriterler (geçer/kalır) olarak listele. Kalan seçenekler puanlamadan önce gerekçesi kaydedilerek elenir.
3. Birbirinden bağımsız (çifte sayım yok), ölçülebilir ya da en azından tarif edilebilir ve hedefle ilgili 4-8 puanlama kriteri tanımla. Yalnızca özellikleri değil maliyeti, riski ve işletilebilirliği de dahil et.
4. Toplamı 100 olan ağırlıkları her biri için tek satırlık gerekçeyle ata. Ağırlıklar paydaşlardan gelir; önerilen ağırlıklar `[ÖNERİ]` olarak işaretlenir.
5. Puanlama ölçeğini (ör. 1-5) kriter başına çapalarla tanımla ("5 = SLA'lı yönetilen hizmet; 1 = kendi barındırdığımız, kurum içi yetkinlik yok").
6. Her seçeneği her kriterde kanıtını göstererek puanla. Bilinmeyen olgular temkinli bir puan alır ve `[DOĞRULANMADI]` olarak işaretlenir.
7. Ağırlıklı toplamları hesapla ve sırala; hesabı göster.
8. Duyarlılık kontrolü yap: en yüksek iki ağırlığın yerini değiştir, her `[DOĞRULANMADI]` puanını makul en iyi ve en kötü değerine çek; kazananın değişip değişmediğini not et.
9. Öneriyi, farkın büyüklüğünü, sıralamanın hangi koşullarda tersine döneceğini ve kazananın neyi feda ettiğini yaz.
10. Açık soruları ve belirsizliği en çok azaltacak olguları listele.
11. Kullanıcının hedefi devam ediyorsa kararı kaydetmek için `decision-log` veya `adr`, ilk seçenekler birbirine yakınsa `trade-off-analysis` öner.

## Çıktı formatı
```markdown
# Karar Matrisi: <karar sorusu>
Karar sahibi: <rol veya [BİLİNMİYOR]> · Ölçek: 1-5 (çapalar aşağıda)

## Eleyici Kriterler
| Kısıt | Seçenek A | Seçenek B | Seçenek C |
|---|---|---|---|
| <zorunlu> | Geçer | Geçer | Kalır – <gerekçe> |

## Ağırlıklı Puanlar
| Kriter (ağırlık) | Seçenek A | Seçenek B |
|---|---|---|
| <kriter> (30) | 4 – <kanıt> | 3 – <kanıt> [DOĞRULANMADI] |
| **Ağırlıklı toplam** | **x.xx** | **x.xx** |

## Puanlama Çapaları
- <kriter>: 5 = ..., 3 = ..., 1 = ...

## Duyarlılık
- <değişiklik> -> kazanan <değişmez / B olur>

## Öneri
<seçenek>, çünkü ... Fark: ... Feda ettiği: ... Sıralama şu durumda değişir: ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Eleyici kriterler puanlamadan önce uygulanmış.
- [ ] Kriterler örtüşmüyor; maliyet, risk ve işletilebilirlik temsil ediliyor.
- [ ] Ağırlıkların toplamı 100 ve her birinin gerekçesi var; önerilen ağırlıklar işaretli.
- [ ] Her puan bir kanıta dayanıyor veya `[DOĞRULANMADI]` olarak işaretli; hiçbir olgu uydurulmamış.
- [ ] Duyarlılık analizi kazananın sağlam olup olmadığını belirtiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Gözde seçeneği haklı çıkarmak için ağırlıkları puanları gördükten sonra belirlemek. Ağırlıkları önce sabitle; değiştirildiyse belirt.
- Aynı faydayı iki kez saymak ("performans" ve "işlem hacmi"). Örtüşen kriterleri birleştir.
- 0,1'lik bir farkı açık bir galibiyet gibi sunmak. Buna beraberlik de ve kararı temel ödünleşime göre ver.
- Bilinmeyen yetenekleri iyimser puanlamak. Bilinmeyen bir risktir; temkinli puanla ve işaretle.

## Örnek
Girdi: "Sipariş platformumuz için üç mesaj kuyruğu arasında seçim yap."

Çıktıdan bir bölüm:
| Kriter (ağırlık) | Yönetilen broker A | Kendi barındırdığımız B | Akış platformu C |
|---|---|---|---|
| Sıralama ve teslim garantileri (25) | 4 | 4 | 5 |
| Mevcut ekiple işletilebilirlik (25) | 5 – yönetilen hizmet | 2 – kurum içi yetkinlik yok | 3 [DOĞRULANMADI] |
| 3 yıllık maliyet (20) | 3 [ÖNERİ, tahmin gerekli] | 4 | 2 |

Duyarlılık: işletilebilirlik ağırlığı 10'a düşerse C, A'yı geçer; öneri ekibin işletme kapasitesine bağlıdır.
