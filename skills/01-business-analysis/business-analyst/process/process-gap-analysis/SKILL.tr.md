---
name: process-gap-analysis
description: "Mevcut (as-is) süreci hedef (to-be) süreçle adım adım karşılaştırır; her farkı insan, süreç, teknoloji, veri veya politika boyutunda gereken bir değişiklik olarak, etkisi, bağımlılıkları ve sorumlusuyla listeler. Hedef süreç tasarlandıktan sonra oraya ulaşmak için değişiklik listesi, iş paketleri veya geçiş planı gerektiğinde ya da 'as-is'ten to-be'ye geçmek için ne değişmeli?' sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: process
  title: "As-is/to-be fark analizi"
  related: "as-is-process, to-be-process, impact-analysis, fit-gap-analysis, raci-matrix"
  prompt: "Fatura onay sürecimizin as-is ve to-be hallerini paylaşıyorum. Fark analizini ve nelerin değişmesi gerektiğini çıkar."
---

# As-Is/To-Be Fark Analizi

## Amaç
Mevcut süreç ile hedef süreç arasındaki farkı somut ve sahipli bir değişiklik listesine dönüştürmek; böylece geçiş planlanabilir, tahmin edilebilir ve takip edilebilir. Bu liste olmadan to-be modeli yalnızca bir çizim olarak kalır.

## Ne zaman kullanılır
- Hem as-is hem to-be süreç mevcutsa ve geçişin planlanması gerekiyorsa.
- Bir süreç yeniden tasarımının BT, operasyon, İK ve uyum arasında iş paketlerine bölünmesi gerekiyorsa.
- Paydaşlar onay vermeden önce kendi rolleri için neyin değiştiğini görmek istiyorsa.

## Ne zaman kullanılmaz
- Hazır bir ürünün gereksinimleri karşılayıp karşılamadığı kontrol edilecekse `fit-gap-analysis` kullanılır.
- Bir gereksinim dokümanındaki eksik içerik aranıyorsa `requirements-gap-analysis` kullanılır.
- Tek bir değişikliğin mevcut sistemlere yayılan etkisi değerlendirilecekse `impact-analysis` kullanılır.

## Girdiler
Zorunlu:
- As-is süreç (adımlar, aktörler, sistemler).
- To-be süreç (adımlar, aktörler, sistemler).

İsteğe bağlı, kaliteyi artırır:
- As-is sorun noktaları ve KPI'ları; to-be hedef KPI'ları.
- Organizasyon şeması, sistem haritası, geçerli politika ve mevzuat.
- Kısıtlar: bütçe zarfı, son tarih, dondurma (freeze) dönemleri.

İki süreçten biri yoksa iste ya da önce `as-is-process` / `to-be-process` öner. Eksik tarafı uydurma.

## Süreç
1. İki süreci ortak bir adım listesinde hizala: her as-is adımını to-be karşılığıyla eşle ve Değişmedi, Değişti, Kaldırıldı, Yeni veya Birleştirildi olarak işaretle.
2. Değişmedi dışındaki her adım için farkı tek satırda "X'ten Y'ye" biçiminde yaz; to-be'nin söylediğinin ötesinde çözüm tasarlama.
3. Her farkı boyutuna göre sınıflandır: İnsan (roller, yetkinlik, kadro), Süreç (adımlar, kurallar, kontroller, SLA'lar), Teknoloji (sistemler, entegrasyonlar, otomasyon), Veri (yeni alanlar, kalite, taşıma), Politika/Uyum (onaylar, görevler ayrılığı, KVKK/GDPR).
4. Her fark için gereken değişikliği çıkar: ne geliştirilmeli, satın alınmalı, eğitilmeli, yeniden yazılmalı veya kaldırılmalı.
5. Kontrol etkisini incele: kaldırılan onaylar, değişen görevler ayrılığı veya denetim izleri açık bir uyum incelemesi gerektirir.
6. Her değişikliği etki (Yüksek/Orta/Düşük) ve karmaşıklık (Yüksek/Orta/Düşük) açısından tek satırlık gerekçeyle puanla. Verilmedikçe parasal rakam kullanma.
7. Değişiklikler arasındaki bağımlılıkları belirle (ör. eğitim sistem değişikliğine bağlı, veri taşıma canlıya geçişten önce).
8. Değişiklikleri iş paketlerinde grupla ve bir sıra öner (hızlı kazanımlar, ön koşullar, tek seferde mi aşamalı mı geçiş).
9. Her iş paketine sorumlu rol ata, açık soruları ve varsayımları listele; çıkarımla bulunan her farkı `[VARSAYIM]` olarak etiketle.
10. Kullanıcı devam etmek isterse etkilenen sistem ve raporlar için `impact-analysis`, geçişin sahipliği için `raci-matrix` veya iş gerekçesi için `cost-benefit-analysis` öner.

## Çıktı formatı
```markdown
# Süreç Fark Analizi: <süreç>
As-is kaynağı: <doküman/sürüm> · To-be kaynağı: <doküman/sürüm>

## Adım Hizalaması
| As-is adımı | To-be adımı | Durum (Değişmedi/Değişti/Kaldırıldı/Yeni/Birleştirildi) |
|---|---|---|

## Fark ve Değişiklik Listesi
| # | Fark (önce → sonra) | Boyut | Gereken değişiklik | Etki | Karmaşıklık | Bağımlılık | Sorumlu rol |
|---|---|---|---|---|---|---|---|

## Kontrol ve Uyum Etkisi
- ...

## İş Paketleri ve Sıralama
1. <paket> – <değişiklikler> – <neden bu sırada>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
- S: ... — muhatap: ...
```

## Kalite kontrol listesi
- [ ] Her as-is ve to-be adımı hizalama tablosunda yer alıyor; hiçbir şey sessizce düşmedi.
- [ ] Her fark bir boyut ve "X'i iyileştir" yerine somut bir değişiklik içeriyor.
- [ ] Kaldırılan veya değişen kontroller uyum incelemesi için belirtildi.
- [ ] Bağımlılıklar önerilen sıralamaya yansıtıldı.
- [ ] Yalnızca BT işi değil, insan tarafı değişiklikler (roller, eğitim, iletişim) de var.
- [ ] Çıkarımla bulunan farklar ve puanlar `[VARSAYIM]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca sistem değişikliklerini listelemek. Süreç yeniden tasarımlarının çoğu roller, eğitim ve teşvikler yüzünden başarısız olur; İnsan boyutunu kapsa.
- Kaldırılan adımları bedava saymak. Manuel bir kontrolün kaldırılması bir iç kontrolün de kalkması olabilir; denetim veya uyum ile teyit et.
- Fark analizini yeni bir to-be tasarımıyla karıştırmak. To-be'ye katılmıyorsan bunu açık soru olarak yaz.

## Örnek
Girdi: As-is: faturalar e-postayla gelir, muhasebe uzmanı sisteme elle girer, yönetici e-postayla onaylar. To-be: faturalar e-fatura entegrasyonuyla gelir, otomatik üçlü eşleştirme yapılır, istisnalar ERP'de yöneticiye düşer.

Çıktıdan bir bölüm:
| # | Fark (önce → sonra) | Boyut | Gereken değişiklik | Etki | Karmaşıklık | Sorumlu rol |
|---|---|---|---|---|---|---|
| 1 | Elle giriş → e-fatura alımı | Teknoloji | E-fatura entegrasyonu ve eşlemesini geliştir | Yüksek | Yüksek | BT entegrasyon |
| 2 | Uzman veri girer → uzman eşleştirme istisnalarını yönetir | İnsan | Muhasebe uzmanı rolünü yeniden tanımla, istisna kuyruğu eğitimi ver | Yüksek | Orta | Muhasebe yöneticisi |
| 3 | E-posta onayı → ERP iş akışı | Politika | ERP onay izinin denetimi karşıladığını teyit et `[VARSAYIM]` | Orta | Düşük | İç denetim |
