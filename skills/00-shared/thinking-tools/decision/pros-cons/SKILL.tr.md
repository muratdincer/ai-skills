---
name: pros-cons
description: "Tek bir öneri veya birkaç seçenek için dengeli bir artı ve eksi analizi yapar; her maddeyi etki ve olasılığa göre tartar, olguları görüşlerden ayırır, hiçbir şey yapmama durumunu da temel alır ve net, koşula bağlı bir öneriyle bitirir. Hızlı kararlar, evet/hayır önerileri veya bir yaklaşıma bağlanmadan önce avantajları ve dezavantajları sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: thinking-tools
  area: decision
  title: "Artı-eksi analizi"
  related: "decision-matrix, trade-off-analysis, bias-check, pre-mortem, decision-log"
  prompt: "Haftalık sürümden ihtiyaç anında sürüme geçmenin artılarını ve eksilerini çıkar, bir öneri ver."
---

# Artı-Eksi Analizi

## Amaç
Karar vericiye, bir seçeneğin mevcut duruma kıyasla ne getirip ne götürdüğüne dair dürüst ve ağırlıklandırılmış bir bakış ve neye bağlı olduğunu açıkça söyleyen bir öneri sunmak.

## Ne zaman kullanılır
- Bir evet/hayır önerisi ya da iki-üç seçenek arasındaki bir tercih hızlı ve adil bir değerlendirme gerektiriyorsa.
- Biri "şunu yapmalı mıyız?" diye soruyor ve cevap bağlama bağlıysa.
- Bir öneri ısrarla savunuluyor ve onaydan önce dengeleyici bir bakışa ihtiyaç varsa.

## Ne zaman kullanılmaz
- Çok sayıda seçeneğin birkaç kritere göre puanlanması gerekiyorsa `decision-matrix` kullanılır.
- İki nitelik arasındaki temel gerilimin (hız ve güvenlik gibi) açıkça ortaya konması gerekiyorsa `trade-off-analysis` kullanılır.
- Asıl endişe, kabul edilmiş bir planın nasıl başarısız olabileceğiyse `pre-mortem` kullanılır.

## Girdiler
Zorunlu:
- Öneri veya seçenekler ve kararın bağlamı (hizmet ettiği hedef veya çözdüğü problem).

İsteğe bağlı, kaliteyi artırır:
- Kısıtlar, paydaşlar, zaman çizelgesi, maliyet rakamları, geçmiş deneyimlerden veriler.
- Karar vericinin öncelikleri veya risk iştahı.

Önerinin arkasındaki hedef belirsizse bununla ilgili tek bir soru sor; hedef olmadan artı ve eksiler tartılamaz.

## Süreç
1. Kararı, hizmet ettiği hedefi ve temel durumu yeniden ifade et: hiçbir şey değişmezse ne olur.
2. Her seçeneğin artılarını temel duruma göre kullanıcılar, ekip, operasyon, finans ve risk/uyum bakış açılarından listele.
3. Eksileri aynı şekilde ve eşit emekle listele; geçiş maliyetlerini (taşıma, eğitim, paralel çalıştırma) ve fırsat maliyetini dahil et.
4. Her maddeyi bir etiket ("daha az risk") olarak değil somut bir etki olarak yeniden yaz ("sürüm başına daha az değişiklik, dolayısıyla daha küçük etki alanı").
5. Her maddeyi Olgu (kaynağıyla), Beklenti (gerekçeli) veya Görüş (biri söylemiş) olarak etiketle; kendi çıkarımlarını işaretle.
6. Her maddeyi tart: etki Yüksek/Orta/Düşük ve olasılık Yüksek/Orta/Düşük. Önemsiz ve tekrarlanan maddeleri çıkar veya birleştir.
7. En ağır eksiler için azaltma önlemlerini, temel artıları güçlendirecek koşulları belirle.
8. Dengeyi kontrol et: bir sütun çok daha uzunsa diğer tarafta eksik kalanı bilinçli olarak ara.
9. Öneriyi yaz: devam / dur / koşullu devam / <kanıt> gelene kadar ertele; kararı belirleyen iki-üç maddeyi belirt.
10. Açık soruları ve karardan sonra izlenecek sinyalleri listele.
11. Kullanıcının hedefi devam ediyorsa daha fazla seçenek çıkarsa `decision-matrix`, uygulamadan önce `pre-mortem`, sonucu kaydetmek için `decision-log` öner.

## Çıktı formatı
```markdown
# Artı-Eksi: <karar>
**Hedef:** ... **Temel durum (hiçbir şey yapmamak):** ...

## Seçenek: <ad>
| Artılar | Tür | Etki | Olasılık |
|---|---|---|---|
| <somut etki> | Olgu – <kaynak> / Beklenti / Görüş | Y/O/D | Y/O/D |

| Eksiler | Tür | Etki | Olasılık | Azaltma önlemi |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Öneri
<devam / dur / koşullu devam / ertele>, çünkü <belirleyici maddeler>.
Koşullar: ...

## İzlenecek Sinyaller
- ...

## Açık Sorular ve Varsayımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Hiçbir şey yapmama temel durumu belirtilmiş ve maddeler ona göre yazılmış.
- [ ] Artılara ve eksilere eşit emek verilmiş; geçiş ve fırsat maliyetleri dahil.
- [ ] Her madde tür etiketi olan somut bir etki; çıkarımlar işaretli.
- [ ] Öneri belirleyici maddeleri ve koşullarını adlandırıyor.
- [ ] Hiçbir rakam uydurulmamış; eksik olanlar `[BİLİNMİYOR]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Maddeleri tartmak yerine saymak. Yüksek etkili tek bir eksi beş küçük artıdan ağır basabilir.
- Öneriyi gerçek temel durumla değil idealleştirilmiş bir alternatifle karşılaştırmak.
- Geçici olduğu için geçiş maliyetini dışarıda bırakmak. Değişikliğin yapılıp yapılmayacağını çoğu zaman bu belirler.

## Örnek
Girdi: "Haftalık sürümden ihtiyaç anında sürüme geçmeli miyiz?"

Zayıf: "Artı: daha hızlı. Eksi: riskli. Öneri: yapalım."

Güçlü bir bölüm:
| Artılar | Tür | Etki | Olasılık |
|---|---|---|---|
| Düzeltmeler müşteriye 7 güne kadar değil, saatler içinde ulaşır. | Beklenti | Y | Y |
| Daha küçük değişiklik setleri rollback kararlarını basitleştirir. | Beklenti | O | Y |

| Eksiler | Tür | Etki | Olasılık | Azaltma önlemi |
|---|---|---|---|---|
| Manuel regresyon seti (koşu başına yaklaşık 2 gün) bu hıza yetişemez. | Olgu – ekip tahmini | Y | Y | Önce kritik yol setini otomatikleştir |

Öneri: koşullu devam; kritik yol regresyon seti otomatik çalışana kadar düzeltmeler için hızlandırılmış bir yol ile haftalık sürüme devam edilsin.
