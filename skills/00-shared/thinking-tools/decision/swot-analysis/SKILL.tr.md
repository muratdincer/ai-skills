---
name: swot-analysis
description: "Sınırları belirli bir konu (ürün, ekip, platform, girişim, iş birimi) için belirtilen bir hedefe göre SWOT analizi yapar; iç güçlü ve zayıf yönleri dış fırsat ve tehditlerden ayrı tutar, her maddeyi kanıtla destekler ve sonucu TOWS stratejilerine ve önceliklendirilmiş aksiyonlara dönüştürür. Strateji veya planlama oturumlarında, büyük bir yatırımdan önce, yeni bir pazara girerken ya da SWOT istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: thinking-tools
  area: decision
  title: "SWOT analizi"
  related: "competitor-analysis, product-strategy-one-pager, technology-strategy, assumption-mapping, risk-register"
  prompt: "Gelecek yılın planlaması öncesinde kurum içi veri platformu ekibimiz için SWOT analizi yap."
---

# SWOT Analizi

## Amaç
Karar vericilere, konunun hedefine göre nerede durduğunu kanıta dayalı olarak göstermek ve bu tabloyu, kimsenin üzerinde aksiyon almadığı dört liste yerine somut stratejik seçeneklere dönüştürmek.

## Ne zaman kullanılır
- Bir ürün, platform, ekip veya iş birimi için yıllık ya da stratejik planlamada.
- Bir yatırım, pazara giriş, yeniden yapılanma veya büyük değişiklik öncesinde hazır olma durumu değerlendirilirken.
- Paydaşların bir yön seçmeden önce ortak bir başlangıç noktasına ihtiyacı varsa.

## Ne zaman kullanılmaz
- Seçenekler arasında belirli bir tercih gerekiyorsa `decision-matrix` veya `trade-off-analysis` kullanılır.
- Odak yalnızca rakiplerse `competitor-analysis` kullanılır.
- Odak yalnızca mevcut bir planın teslimat riskleriyse `pre-mortem` veya `risk-register` kullanılır.

## Girdiler
Zorunlu:
- Konu ve SWOT'un hizmet ettiği hedef (ör. "gelecek yıl self-servis analitik kullanımını artırmak").

İsteğe bağlı, kaliteyi artırır:
- Performans verileri, müşteri veya kullanıcı geri bildirimi, yetkinlik envanteri, maliyetler.
- Pazar, teknoloji, mevzuat veya organizasyon eğilimleri.
- Önceki SWOT veya strateji dokümanları.

Hedef yoksa iste; hedefi olmayan bir SWOT genel geçer listeler üretir.

## Süreç
1. Kapsamı ve hedefi birer satırla, zaman ufkunu da belirterek tanımla.
2. Güçlü yönler: konunun kontrol ettiği ve hedefe ulaşmaya yardım eden iç özellikler; tercihen başkalarının kolayca kopyalayamayacakları.
3. Zayıf yönler: hedefi engelleyen iç özellikler; yetkinlik, süreç, teknik borç ve maliyet durumu dahil.
4. Fırsatlar: konunun yararlanabileceği dış koşullar (pazar, kullanıcılar, teknoloji, mevzuat, konunun kontrolü dışındaki organizasyon).
5. Tehditler: konunun ne yaptığından bağımsız olarak ona zarar verebilecek dış koşullar.
6. Yerleşimi test et: konu doğrudan değiştirebiliyorsa içtir (G/Z); değiştiremiyorsa dıştır (F/T). Yanlış yerdeki maddeleri taşı.
7. Her maddeyi somut ve kanıtlı yaz ("yavaş" değil, "ortak kümede medyan sorgu süresi 40 sn"); desteklenmeyen maddeleri `[VARSAYIM]` olarak işaretle.
8. Her çeyreği hedef açısından en önemli 3-6 maddeyle sınırla ve sırala.
9. TOWS matrisi kur: GF (güçlü yönlerle fırsatları yakala), ZF (fırsatları yakalamak için zayıf yönleri gider), GT (güçlü yönlerle tehditleri azalt), ZT (tehditlerden kaçınmak için zayıf yönleri en aza indir).
10. Sorumlu rolü, zaman ufku ve başarı sinyali olan 3-5 öncelikli aksiyon seç; önce neyin doğrulanması gerektiğini not et.
11. Kullanıcının hedefi devam ediyorsa aksiyonları stratejiye dönüştürmek için `product-strategy-one-pager` veya `technology-strategy`, kilit maddeleri doğrulamak için `assumption-mapping` öner.

## Çıktı formatı
```markdown
# SWOT: <konu>
**Hedef:** ... **Zaman ufku:** ...

| | Yardımcı | Zararlı |
|---|---|---|
| **İç** | **Güçlü yönler** 1. <madde – kanıt> | **Zayıf yönler** 1. ... |
| **Dış** | **Fırsatlar** 1. ... | **Tehditler** 1. ... |

## TOWS Stratejileri
| | Fırsatlar | Tehditler |
|---|---|---|
| **Güçlü yönler** | GF: ... | GT: ... |
| **Zayıf yönler** | ZF: ... | ZT: ... |

## Öncelikli Aksiyonlar
| # | Aksiyon | Strateji türü | Sorumlu (rol) | Zaman ufku | Başarı sinyali |
|---|---|---|---|---|---|

## Varsayımlar ve Doğrulanacak Maddeler
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Hedef belirtilmiş ve her madde onunla ilgili.
- [ ] İç ve dış maddeler doğru yerleştirilmiş (kontrol edilebilir = iç).
- [ ] Maddeler somut ve kanıtlı ya da `[VARSAYIM]` olarak işaretli.
- [ ] Her çeyrek sıralanmış ve önemli olanlarla sınırlanmış.
- [ ] TOWS stratejileri sorumlusu ve başarı sinyali olan aksiyonlara bağlanıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ekibin yapmak istediklerini fırsat olarak yazmak ("yeni bir API geliştirmek"). Bunlar aksiyondur; fırsatlar dış koşullardır.
- Belirsiz maddeler ("iyi ekip", "rekabet"). Ekibi neyin iyi yaptığını ve hangi rakibin ne yaptığını yaz.
- Dört çeyrekte durmak. Değer TOWS stratejilerinde ve aksiyonlardadır.

## Örnek
Girdi: "Gelecek yılın planlaması öncesinde kurum içi veri platformu ekibimiz için SWOT."

Çıktıdan bir bölüm:
- Hedef: 12 ay içinde self-servis analitik kullanan iş ekibi sayısını ikiye katlamak.
- Güçlü yön: kontrolörlerin zaten güvendiği, düzenlenmiş finans ve satış veri setleri `[VARSAYIM — kullanım verisiyle teyit et]`.
- Zayıf yön: ortak kümede medyan sorgu süresi yaklaşık 40 sn (izleme verisi).
- Fırsat: gelecek yıl için şirket genelinde zorunlu kılınan raporlama konsolidasyonu.
- Tehdit: iş birimlerinin kendi BI araçlarını satın alıp gölge veri depoları kurması.
- ZF aksiyonu: konsolidasyon başlamadan self-servis iş yükleri için küme ayrıştırmasını finanse et; başarı sinyali: medyan sorgu süresi [TBD] saniyenin altında.
