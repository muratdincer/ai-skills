---
name: heuristic-evaluation
description: "Bir ürünü, akışı veya ekranları Nielsen'in 10 kullanılabilirlik ilkesine göre değerlendirir; ihlal edilen ilke, kanıt, 0-4 önem derecesi ve somut öneriyle konumlandırılmış bulgular ile önceliklendirilmiş bir özet üretir. Kullanıcı testinden önce veya onun yerine hızlı bir uzman kullanılabilirlik incelemesi gerektiğinde, \"bu arayüzde ne yanlış\" sorulduğunda ya da ekran görüntüleri, prototipler veya canlı bir akış denetlenecekse kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 10-design
  role: ux-ui-designer
  area: design
  title: "Sezgisel değerlendirme"
  related: "usability-test-script, accessibility-audit, design-critique, research-synthesis, user-flow"
  prompt: "Masraf girişi akışımız için sezgisel değerlendirme yap; 4 ekranın görüntüleri ekte."
---

# Sezgisel Değerlendirme

## Amaç
Arayüzü yerleşik ilkelere göre inceleyerek kullanılabilirlik sorunlarını hızlı ve düşük maliyetle bulmak ve önem derecesine göre sıralamak. Böylece ekip, teste veya yayına yatırım yapmadan önce kullanıcıyı en çok zorlayan sorunları düzeltir.

## Ne zaman kullanılır
- Bir prototip veya canlı akışın kullanıcı testinden ya da yayından önce uzman incelemesine ihtiyacı olduğunda.
- Kullanıcı araştırması için bütçe veya zaman yok, yine de yapılandırılmış bir inceleme gerektiğinde.
- Bir rakip veya eski ürün kullanılabilirlik sorunları açısından kıyaslanacaksa.

## Ne zaman kullanılmaz
- Amaç erişilebilirlik standartlarına uygunluksa `accessibility-audit` kullanılır.
- Devam eden bir tasarım için ekip incelemesinde hedeflere göre geri bildirim isteniyorsa `design-critique` kullanılır.
- Karar için gerçek kullanıcılardan kanıt gerekiyorsa `usability-test-script` kullanılır.

## Girdiler
Zorunlu:
- Değerlendirilecek arayüz (ekran görüntüleri, prototip tarifi, ekran listesi veya canlı akış tarifi), birincil kullanıcıları ve görevleri.

İsteğe bağlı, kaliteyi artırır:
- Kullanıcı akışı, bilinen şikâyetler veya analitik, platform alışkanlıkları, tasarım sistemi, kapsam sınırları.

Arayüz veya ana görevler yoksa iste. Akışın yalnızca bir kısmı görünüyorsa görüneni değerlendir, gerisini değerlendirilmedi olarak listele.

## Süreç
1. Kapsamı tanımla: kullanıcılar, 3-5 temel görev, kapsamdaki ekranlar ve durumlar, platform; hariç tutulanları belirt.
2. Her görevi hedef kullanıcı gözüyle adım adım yürü; her tereddüt, şaşkınlık veya fazladan çaba noktasını not et. Yalnızca görüneni veya tarif edileni değerlendir; çıkarılan davranışı `[VARSAYIM]` olarak işaretle.
3. 10 ilkeye göre incele: sistem durumunun görünürlüğü; sistemle gerçek dünyanın uyumu; kullanıcı kontrolü ve özgürlüğü; tutarlılık ve standartlar; hata önleme; hatırlamak yerine tanıma; esneklik ve verimlilik; estetik ve sade tasarım; hataları tanıma, teşhis ve kurtarmada yardım; yardım ve dokümantasyon.
4. Her bulguyu bir kez, bulunduğu yerde kaydet: ihlal edilen ilke(ler), ne olduğu, görev için neden önemli olduğu ve kanıt (ekran, öğe, etiket alıntısı).
5. Sıklık, etki ve kalıcılığa göre 0-4 önem derecesi ver (0 sorun değil, 1 kozmetik, 2 küçük, 3 büyük, 4 felaket/engelleyici); derecelendirmeyi tek satırla açıkla.
6. Her bulgu için somut bir öneri yaz (yalnızca "anlaşılırlığı artır" değil, neyin değişeceği); tahmin edilebiliyorsa eforu K/O/B olarak belirt.
7. Düzeltmeler bozmasın diye korunması gereken olumlu bulguları kaydet.
8. Tekrarları birleştir, bulguları görev veya ekrana göre grupla ve önem derecesine göre sırala.
9. Sınırları belirt: tek değerlendirici yanlılığı (kapsam için 3-5 değerlendirici öner), gerçek kullanıcı verisi olmaması, görülmeyen durumlar.
10. En önemli sorunları özetle; büyük bulguları kullanıcılarla doğrulamak için `usability-test-script`, WCAG kapsamı için `accessibility-audit` öner.

## Çıktı formatı
```markdown
# Sezgisel Değerlendirme: <ürün / akış>
Kapsam: <görevler, ekranlar, platform> · Değerlendirici(ler): <...> · Kapsam dışı: <...>

## Özet
- Bulgular: <n> (4: x, 3: y, 2: z, 1: w)
- En önemli sorunlar: 1) ... 2) ... 3) ...

## Bulgular
| # | Konum | İlke | Sorun | Kanıt | Önem (0-4) | Öneri | Efor |
|---|---|---|---|---|---|---|---|

## Korunacak Güçlü Yönler
- ...

## Sınırlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her bulgunun konumu, ilkesi, kanıtı ve somut önerisi var.
- [ ] Önem dereceleri 0-4 ölçeğine uyuyor ve her biri gerekçelendirildi.
- [ ] Bulgular kişisel zevkle değil, kullanıcıların görev başarısıyla ilgili.
- [ ] Tekrarlar birleştirildi ve liste önem derecesine göre sıralandı.
- [ ] Görülmeyen ekranlar veya durumlar tahmin edilmedi, değerlendirilmedi olarak listelendi.
- [ ] Sınırlar (değerlendirici sayısı, kullanıcı verisi yokluğu) belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İhlalleri öneri olmadan listelemek. Her bulgu neyin değişeceğini söylemeli.
- Her şeyi büyük sorun olarak derecelendirmek. Ayırt etmek için sıklık, etki ve kalıcılığı kullan.
- Değerlendirmeyi kullanıcı kanıtı gibi sunmak. Uzman görüşü olarak sun ve büyük sorunları kullanıcılarla doğrula.

## Örnek
Girdi: Bir masraf girişi akışının 4 ekran görüntüsü.

Zayıf bulgu: "Form kafa karıştırıcı. İlke 2. Önem 3."
Güçlü bulgu: "Ekran 2, 'Masraf merkezi' alanı: liste veya ipucu olmadan bir kod (ör. 4410) bekliyor; kullanıcı kodu başka bir sistemden hatırlamak zorunda. İlke: hatırlamak yerine tanıma. Önem 3: her girişte yaşanıyor, finans dışı çalışanları engelliyor. Öneri: ad + kod gösteren aranabilir açılır liste, varsayılan olarak kullanıcının kendi masraf merkezi. Efor: O."
