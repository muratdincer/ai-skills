---
description: Bir teknoloji satın alımı için tedarikçileri veya ürünleri değerlendirir; gereksinimler ve eleme kriterlerinden, yanıtlar okunmadan önce sabitlenen ağırlıklı puanlama modeline, kanıta dayalı puanlamaya, toplam sahip olma maliyeti ve riske, oradan da belgelenmiş bir öneriye kadar ilerler. Bir yazılım ürünü, platform, bulut veya hizmet sağlayıcı seçilirken, RFP hazırlanır veya puanlanırken ya da tedarikçi seçiminin satın alma, denetim veya yönetim önünde savunulabilir olması gerektiğinde kullanılır.
related: decision-matrix, build-vs-buy, fit-gap-analysis, vendor-status-review, it-risk-assessment
prompt: API yönetim platformu RFP'mize 3 yanıt geldi; değerlendirme modelini kur ve bir tedarikçi öner.
---

# Tedarikçi Değerlendirme (RFP)

## Amaç
İzlenebilir ve adil bir tedarikçi kararına ulaşmak: Kriterler ve ağırlıklar kimse puan vermeden önce kararlaştırılır, her puan kanıta dayanır ve işlevselliğin yanında toplam maliyet ve risk de karşılaştırılır.

## Ne zaman kullanılır
- Bir ürün, platform, yönetilen hizmet veya uygulama ortağı seçilirken.
- Bir RFP'nin değerlendirme bölümü tasarlanırken veya gelen yanıtlar puanlanırken.
- Tercih edilen tedarikçinin satın alma, denetim, güvenlik veya yönetim kuruluna gerekçelendirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Satın almak mı geliştirmek mi kararı için önce `build-vs-buy` kullanılır.
- Tek bir paketin ayrıntılı gereksinimlere uygunluğunu kontrol etmek için `fit-gap-analysis` kullanılır.
- Mevcut bir tedarikçinin teslimat performansını incelemek için `vendor-status-review` kullanılır.

## Girdiler
Zorunlu:
- İhtiyaç veya gereksinimler ve aday tedarikçiler ya da (puanlama başladıysa) yanıtları.

İsteğe bağlı, kaliteyi artırır:
- Bütçe aralığı, sözleşme süresi, satın alma kuralları ve zorunlu maddeler.
- Mimari, güvenlik, veri yerleşimi ve uyum kısıtları (KVKK/GDPR, sektör kuralları).
- Demo, kavram kanıtı (PoC) veya referans görüşmesi notları.

Gereksinimler yoksa iste; onlar olmadan her puanlama bir görüştür. Tedarikçi yeteneği, fiyat veya referans uydurma; yalnızca yanıtların veya kullanıcının verdiklerini kullan.

## Süreç
1. Kararı tanımla: ne satın alınıyor, zaman ufku, karar sahibi ve kimlerin puanlayacağı; değerlendiriciler arasındaki çıkar çatışmalarını beyan ettir.
2. Eleme kriterlerini (zorunlu, geçer/geçmez) belirle: ör. veri yerleşimi, güvenlik sertifikası, belirli bir sistemle entegrasyon, destek saatleri. Birini karşılamayan tedarikçi gerekçesi kaydedilerek elenir.
3. Ağırlıklı kriterleri gruplar halinde kur: işlevsel uygunluk, işlevsel olmayan (performans, erişilebilirlik, güvenlik), entegrasyon ve mimari uyum, tedarikçi sürdürülebilirliği ve desteği, teslimat yaklaşımı, ticari/TCO. Ağırlıkları yanıtları okumadan önce kararlaştır.
4. Değerlendiricilerin aynı şekilde puan vermesi için çapalı bir puan ölçeği tanımla (ör. 0 = karşılanmıyor, 3 = geçici çözümle karşılanıyor, 5 = kanıtla birlikte yerleşik olarak karşılanıyor).
5. Her tedarikçiyi her kriterde tek satırlık bir kanıt referansıyla (yanıt bölümü, demo gözlemi, PoC sonucu) puanla; kanıtı olmayan iddiaları doğrulanmamış olarak işaretle, düşük puanla ya da doğrula.
6. Değerlendiricilerin önce bağımsız puanlamasını sağla, ardından büyük farkları kıdemle değil kanıtla uzlaştır.
7. Sözleşme ufku boyunca toplam sahip olma maliyetini (TCO) hesapla: lisans/abonelik, uygulama, entegrasyon, altyapı, iç personel, eğitim, çıkış/geçiş maliyeti; tahminleri `[VARSAYIM]` olarak işaretle.
8. Riskleri değerlendir: bağımlılık (lock-in) ve çıkış seçenekleri, tedarikçinin finansal ve yol haritası riski, güvenlik ve gizlilik, kilit kişi bağımlılığı, sözleşme boşlukları.
9. Duyarlılık kontrolü yap: makul ağırlık değişimleriyle sıralama değişir mi? Kazananın ne kadar sağlam olduğunu belirt.
10. Öneriyi koşullarıyla (sözleşme maddeleri, PoC kapıları, pazarlık noktaları) ve yedek olarak ikinci sıradaki tedarikçiyle yaz.
11. Kullanıcının hedefi devam ediyorsa kararı kaydetmek için `decision-log`, daha derin risk incelemesi için `it-risk-assessment` veya tedarikçiyle çalışma başladığında `vendor-status-review` öner.

## Çıktı formatı
```markdown
# Tedarikçi Değerlendirmesi: <satın alım>
Karar sahibi: <rol> · Değerlendiriciler: <roller> · Beyan edilen çatışmalar: <yok/...>

## Eleme Kriterleri
| Kriter | Tedarikçi A | Tedarikçi B | Tedarikçi C |
|---|---|---|---|

## Ağırlıklı Puanlama (0-5 ölçek, çapalar ekte)
| Grup / kriter | Ağırlık | A | B | C | Kanıt referansları |
|---|---|---|---|---|---|
| Ağırlıklı toplam | %100 | | | | |

## Toplam Sahip Olma Maliyeti (<n> yıl)
| Maliyet kalemi | A | B | C | Dayanak |
|---|---|---|---|---|

## Riskler
| Risk | Tedarikçi | Olasılık | Etki | Azaltım |
|---|---|---|---|---|

## Duyarlılık
- ...

## Öneri
- Tercih edilen: <tedarikçi> – neden – koşullar
- Yedek: <tedarikçi>
- Açık sorular: ...
```

## Kalite kontrol listesi
- [ ] Eleme kriterleri, ağırlıklar ve ölçek çapaları yanıtlar puanlanmadan önce sabitlendi.
- [ ] Her puan bir kanıta dayanıyor; doğrulanmamış tedarikçi iddiaları işaretli.
- [ ] TCO iç efor ve çıkış maliyeti dahil tüm ufku kapsıyor.
- [ ] Bağımlılık, güvenlik ve tedarikçi sürdürülebilirliği riskleri değerlendirildi.
- [ ] Uydurulmuş yetenek, fiyat veya referans yok; varsayımlar etiketli.
- [ ] Öneri koşulları ve bir yedeği belirtiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ağırlıkları yanıtları gördükten sonra belirlemek. Bu, modeli bir favoriye doğru büker; ağırlıkları önce dondur.
- Yalnızca lisans fiyatını karşılaştırmak. Uygulama, entegrasyon ve iç personel çoğu zaman TCO'ya hakim olur.
- En iyi demoyu puanlamak. Parlak bir demo, kendi verin ve entegrasyonlarınla uyumun kanıtı değildir; kritik kriterler için PoC kullan.

## Örnek
Girdi: Bir API yönetim platformu için üç RFP yanıtı.

Çıktıdan bir bölüm:
- Eleme: şirket içi veya yurt içi veri düzlemi zorunlu `[teyit et]`; Tedarikçi C yalnızca yurt dışı bölgede SaaS sunuyor – elendi.
- Zayıf kanıt (kaçın): "Tedarikçi A'nın güvenliği iyi." Güçlü: "Tedarikçi A: mTLS ve OAuth 2.0 politikaları demoda gösterildi; bağımsız güvenlik sertifikasının kopyası verilmedi – doğrulanmadı, gelene kadar puan 3."
- TCO: Tedarikçi B'nin lisansı daha düşük ama kendi barındırması için 2 FTE `[VARSAYIM]` gerekiyor; 3 yıllık TCO'da ikinci sırada.
