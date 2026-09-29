---
description: Teknoloji üzerine kısa bir üst yönetim veya yönetim kurulu güncellemesi yazar: son güncellemeden bu yana ne değişti, hedeflere göre birkaç sonuç metriği, eğilim ve azaltım planıyla en önemli riskler ve açık talepler ya da gereken kararlar. Bir CTO, CIO veya teknoloji direktörü yönetim kuruluna, icra kuruluna veya yatırımcılara rapor verirken ya da uzun bir teknik durumun teknik olmayan üst düzey okuyucular için yoğunlaştırılması gerektiğinde kullanılır.
related: executive-summary, status-update, technology-strategy, budget-proposal, risk-register
prompt: Yönetim kurulu için çeyreklik teknoloji güncellememi yaz; bulut geçişi %60 tamamlandı, iki büyük kesinti yaşadık ve bir güvenlik yatırımı için onay almam gerekiyor.
---

# Yönetim Kurulu Güncellemesi

## Amaç
Yönetim kurulu üyelerine veya yöneticilere birkaç dakikalık okumayla teknoloji ilerlemesi, riskler ve vermeleri gereken kararlar hakkında dürüst bir görünüm sunmak; bunu iş diliyle ve eklerde saklanmış sürprizler olmadan yapmak.

## Ne zaman kullanılır
- Düzenli yönetim kurulu, icra kurulu veya yatırımcı teknoloji raporlamasında.
- Önemli bir olayın (büyük kesinti, güvenlik ihlali, program gecikmesi) üst kademeye raporlanması gerektiğinde.
- En üst düzeyden bir karar veya finansman onayı gerektiğinde.

## Ne zaman kullanılmaz
- Teslimat ekibine yönelik haftalık veya proje düzeyi durum için `status-update` veya `project-status-report` kullanılır.
- Tek bir dokümanı veya analizi özetlemek için `executive-summary` kullanılır.
- Çalışanlara bir organizasyon değişikliğini duyurmak için `org-change-communication` kullanılır.

## Girdiler
Zorunlu:
- Son güncellemeden bu yana ana gelişmeler ve gereken talepler veya kararlar (ya da olmadığının teyidi).

İsteğe bağlı, kaliteyi artırır:
- Önceki güncelleme ve orada verilen taahhütler.
- Hedef ve eğilimleriyle metrikler (erişilebilirlik, teslimat, maliyet, güvenlik durumu, program kilometre taşları).
- Risk kaydı, olay raporları, denetim bulguları; kurulun bilinen kaygıları.

Gelişmeler yoksa iste. Asla metrik, eğilim veya tarih uydurma; eksik değerler `[BİLİNMİYOR]` olarak yazılır. Kullanıcıya bu düzeyde gerekmeyen kişisel verileri ve gizli olay ayrıntılarını çıkarmasını hatırlat.

## Süreç
1. Hedef kitleyi (yönetim kurulu, icra kurulu, yatırımcılar), bilinen kaygılarını ve ayrılabilecek okuma süresini belirle; tonu teknoloji ayrıntısına değil iş etkisine göre ayarla.
2. Kötü haberler dahil en önemli üç mesajla başla; yalnızca bu bölümü okuyan bir kurul üyesi yanıltılmamalı.
3. İlerlemeyi geçen sefer taahhüt edilenlere göre raporla: yolunda, riskli veya sapmış ve nedeni; referans noktasını sessizce değiştirme.
4. İş hedeflerine bağlı 4-6 sonuç metriği seç; her birinin hedefi, güncel değeri ve eğilimi olsun. Belirgin şekilde değişen metriği tek satırda açıkla.
5. En önemli 3-5 riski eğilim (artan/sabit/azalan), iş diliyle etki, azaltım ve sorumlu rolle sun; güvenlik ve mevzuat riskini açıkça dahil et.
6. Önemli olayları olgusal olarak raporla: müşteri veya gelir etkisi, üst düzey kök neden, neyin değiştiği; suçlamadan kaçın.
7. Talepleri net yaz: gereken karar, onay, finansman veya destek, seçenekler, öneri ve karar için son tarih.
8. Jargon ve kısaltmaları çıkar ya da tanımla; teknik terimleri iş sonuçlarıyla değiştir.
9. Tahmin veya yorum olan her şeyi `[VARSAYIM]` olarak etiketle; destekleyici ayrıntıyı eke koy.
10. Uzunluğu kontrol et: ana gövde 1-2 sayfa veya birkaç slayt.
11. Kullanıcının hedefi devam ediyorsa finansman talebi için `budget-proposal`, riskin ayrıntısı için `risk-register` veya kısa bir ön okuma için `executive-summary` öner.

## Çıktı formatı
```markdown
# <Hedef kitle> için Teknoloji Güncellemesi – <dönem>

## Ana Mesajlar
1. ...
2. ...
3. ...

## Kararlar / Talepler
| Talep | Seçenekler | Öneri | Gereken tarih |
|---|---|---|---|

## Taahhütlere Göre İlerleme
| Taahhüt (önceki güncelleme) | Durum | Yorum |
|---|---|---|

## Sonuç Metrikleri
| Metrik | Hedef | Güncel | Eğilim | Not |
|---|---|---|---|---|

## En Önemli Riskler
| Risk | İş etkisi | Eğilim | Azaltım | Sorumlu (rol) |
|---|---|---|---|---|

## Önemli Olaylar
- <olay> – etki – neden (üst düzey) – ne değişti

## Ek
- ...
```

## Kalite kontrol listesi
- [ ] Varsa kötü haberler ana mesajlarda; önemli hiçbir şey eke gömülmemiş.
- [ ] İlerleme önceki taahhütlere göre raporlanmış, referans noktası sessizce değiştirilmemiş.
- [ ] Her metriğin hedefi ve eğilimi var ve bir iş sonucuna bağlı.
- [ ] Her talep seçenekleri, bir öneriyi ve karar son tarihini belirtiyor.
- [ ] Uydurulmuş metrik veya tarih yok; tahminler etiketli, gereksiz kişisel veya gizli veri yok.
- [ ] Ana gövde 1-2 sayfa ve açıklanmamış jargon içermiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca iyi haber içeren rapor. Kurul sorunları başka yerden öğrendiğinde güven kaybolur; önemli sorunla başla.
- Sonuç yerine faaliyet metrikleri (kapanan kayıt, story point). Erişilebilirlik, müşteri etkisi, maliyet ve kilometre taşı teslimini kullan.
- Belirsiz talep ("güvenlik için destek"). Kararı, tutarı veya seçeneği ve ne zaman gerektiğini adlandır.

## Örnek
Girdi: Bulut geçişi %60 tamam, iki büyük kesinti, bir güvenlik yatırımı için onay gerekiyor.

Çıktıdan bir bölüm:
- Ana mesaj 2: Bu çeyrekteki iki kesinti online satışları toplam `[BİLİNMİYOR]` saat etkiledi; ikisi de eski ağ segmentinden kaynaklandı ve geçiş bu segmenti `[tarihi teyit et]` itibarıyla kaldırıyor.
- Zayıf talep (kaçın): "Daha fazla güvenlik bütçesine ihtiyacımız var." Güçlü talep: "B seçeneğini (yönetilen tespit hizmeti, yıllık `[tekliften tutar]`) bir sonraki toplantıya kadar onaylayın; A seçeneği (şirket içi ekip) için kadro kurmak 9-12 ay sürer `[VARSAYIM]`."
