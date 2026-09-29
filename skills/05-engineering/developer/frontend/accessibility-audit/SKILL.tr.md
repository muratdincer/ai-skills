---
description: Bir web veya mobil arayüzü (sayfa, akış, bileşen ya da işaretleme kodu) WCAG 2.2 A ve AA başarı kriterlerine göre denetler; her bulguyu kriter, etkilenen kullanıcılar, kanıt ve önem derecesiyle kaydeder, somut kod veya tasarım düzeltmeleri önerir. Bir ekran veya bileşenin yayın öncesi erişilebilirlik kontrolü gerektiğinde, bir şikâyet ya da yasal talep sonrasında veya "bu erişilebilir mi?", "WCAG'ye göre kontrol et" dendiğinde kullanılır.
related: component-design, heuristic-evaluation, design-handoff, microcopy, test-case-writing
prompt: Bu ödeme formu işaretlemesini WCAG 2.2 AA'ya göre denetle ve önce neyi düzeltmem gerektiğini söyle.
---

# Erişilebilirlik Denetimi (WCAG)

## Amaç
Engelli kullanıcıların bir işi tamamlamasını engelleyen bariyerleri bulmak, her birini bir WCAG 2.2 başarı kriterine bağlamak ve geliştiricilere önceliklendirilmiş, düzeltilebilir bir liste vermek. Çıktı, iş kalemlerine dönüştürülebilen ve düzeltmelerden sonra yeniden kontrol edilebilen bir denetim raporudur.

## Ne zaman kullanılır
- Bir sayfa, akış veya bileşen yayına çıkmak üzereyken A/AA uygunluk kontrolü gerektiğinde.
- Bir kullanıcı şikâyeti, müşteri gereksinimi veya yasal yükümlülük erişilebilirlik incelemesi istediğinde.
- Bir tasarım sistemi bileşeni diğer ekipler kullanmadan önce doğrulanmalıysa.

## Ne zaman kullanılmaz
- Kod yazılmadan önce yeni bir bileşenin erişilebilirlik sözleşmesini tasarlamak için `component-design` kullanılır.
- WCAG değil, sezgisel ilkelere göre genel kullanılabilirlik incelemesi için `heuristic-evaluation` kullanılır.
- Yalnızca erişilebilirlik regresyon test senaryoları yazmak için `test-case-writing` kullanılır.

## Girdiler
Zorunlu:
- Denetlenecek arayüz: işaretleme veya kod, ekran görüntüleriyle bir URL tarifi ya da akışın ayrıntılı açıklaması ve kritik kullanıcı görevi.

İsteğe bağlı, kaliteyi artırır:
- Hedef seviye (varsayılan AA) ve varsa yasal veya sözleşmesel gereklilik.
- Otomatik denetleyici sonuçları, ekran okuyucu veya klavye test notları.
- Desteklenen platformlar, tarayıcılar ve yardımcı teknolojiler; tasarım token'ları (renkler, odak stilleri).

Arayüzün kendisi yoksa iste. Yalnızca ekran görüntüsü verildiyse semantik, erişilebilir adlar ve klavye davranışının `[BİLİNMİYOR]` olduğunu ve doğrulanamadığını belirt.

## Süreç
1. Kapsamı tanımla: sayfalar veya ekranlar, durumlar (varsayılan, hata, yükleniyor, modal açık), kritik kullanıcı görevi, hedef seviye ve eldeki kanıt (kod, ekran görüntüsü, test notu). Kontrol edilemeyenleri kaydet.
2. Görevi yalnızca klavyeyle yürüt: her kontrole erişilebilirlik, mantıklı odak sırası, yapışkan içerik altında kalmayan görünür odak göstergesi (2.4.7, 2.4.11), klavye tuzağı olmaması (2.1.2), diyaloglarda ve sayfa geçişlerinde odak yönetimi.
3. Semantiği ve adları kontrol et: başlıklar ve landmark'lar, ARIA'dan önce yerel elemanlar, her kontrolün görünür etiketini içeren bir erişilebilir adı olması (4.1.2, 2.5.3), form alanlarının programatik etiket ve yönergeleri (1.3.1, 3.3.2).
4. Algılanabilir içeriği kontrol et: anlamlı görsel ve ikonlar için metin alternatifleri (1.1.1), metin kontrastı 4.5:1, büyük metinde 3:1 (1.4.3), kontrol ve odak için metin dışı kontrast 3:1 (1.4.11), bilginin yalnızca renkle verilmemesi (1.4.1), 320 CSS px'te yeniden akış ve %200 metin büyütme (1.4.10, 1.4.4).
5. Etkileşim ve girdiyi kontrol et: en az 24x24 CSS px hedef boyutu veya yeterli boşluk (2.5.8), sürükleme alternatifleri (2.5.7), zaman tuzağı olmaması (2.2.1), hareket ve otomatik oynatma kontrolleri (2.2.2; AAA kapsamdaysa 2.3.3).
6. Hataları ve yardımı kontrol et: hataların metinle belirtilip alana bağlanması (3.3.1), öneriler (3.3.3), yasal veya finansal gönderimlerde onay veya geri alma (3.3.4), tekrarlı veri girişinden kaçınma (3.3.7), bilişsel test gerektirmeyen erişilebilir kimlik doğrulama (3.3.8), tutarlı yardım (3.2.6).
7. Dinamik içeriği kontrol et: odağı taşımadan duyurulan durum mesajları (4.1.3), live region'ların ölçülü kullanımı, üzerine gelince veya odakta açılan içeriğin kapatılabilir ve kalıcı olması (1.4.13).
8. Her bulgu için kaydet: konum, kriter numarası ve adı, kimin etkilendiği, kanıt (kod parçası veya gözlenen davranış) ve Doğrulandı mı yoksa `[VARSAYIM]` mı (ekran görüntüsünden veya eksik koddan çıkarım).
9. Önem derecesini göreve etkisine göre ver: Engelleyici (görev tamamlanamıyor), Yüksek (büyük çabayla tamamlanıyor), Orta, Düşük. Kritik yoldaki bir A seviyesi hatası en az Yüksek'tir.
10. Her bulgu için somut bir düzeltme öner: düzeltilmiş işaretleme, öznitelik, token veya davranış; ARIA yerine yerel HTML veya platform kontrollerini tercih et.
11. Kontrol edilen her kriter için uygunluk özetini çıkar (Geçti, Kaldı, Uygulanamaz, Test edilmedi) ve yardımcı teknolojiyle manuel test gerektirenleri listele.
12. Kullanıcı devam ederse bir bileşen sözleşmesini kaynağında düzeltmek için `component-design`, regresyon kontrolleri eklemek için `test-case-writing`, etiket ve hata metinleri için `microcopy` öner.

## Çıktı formatı
```markdown
# Erişilebilirlik Denetimi: <kapsam>
Hedef: WCAG 2.2 Seviye <A/AA> · Kanıt: <kod / ekran görüntüsü / YT testi> · Tarih: <tarih>
Kontrol edilmeyen: <maddeler ve nedeni>

## Özet
- Engelleyici: <n> · Yüksek: <n> · Orta: <n> · Düşük: <n>
- İlk 3 düzeltme: ...

## Bulgular
| # | Konum | Kriter | Etkilenen kullanıcılar | Kanıt | Önem | Durum | Düzeltme |
|---|---|---|---|---|---|---|---|

## Uygunluk Özeti
| Kriter | Sonuç (Geçti/Kaldı/Uyg. değil/Test edilmedi) | Not |
|---|---|---|

## Manuel Test Gerekenler
- <ekran okuyucu / sesli kontrol / yakınlaştırma senaryosu>

## Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her bulgu belirli bir WCAG 2.2 kriter numarası ve adına ve kanıta dayanıyor.
- [ ] Her düzeltme somut (işaretleme, öznitelik, token veya davranış); "erişilebilir yap" değil.
- [ ] Önem derecesi yalnızca kriterin seviyesini değil, kritik göreve etkisini yansıtıyor.
- [ ] Kanıttan doğrulanamayan maddeler `[VARSAYIM]` veya "Test edilmedi" olarak işaretli.
- [ ] Önerilen düzeltmelerde ARIA yerine yerel elemanlar tercih edildi.
- [ ] Otomatik araç veya yalnızca ekran görüntüsü kanıtıyla tam uygunluk iddia edilmedi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Otomatik denetleyicinin temiz sonucunu uygunluk saymak. Otomatik araçlar hataların yalnızca bir kısmını yakalar; klavye, odak ve ad kontrolleri manuel inceleme ister.
- Yerel button, link ve input yerine genel kapsayıcılara ARIA rolü eklemek; bu klavye davranışını bozar.
- Kontrast sorunlarını yalnızca gövde metninde aramak; odak göstergelerini, ikonları ve input kenarlıklarını (1.4.11) atlamak.

## Örnek
Girdi: "Ödeme formu: `<div class="btn" onclick="pay()">Öde</div>`, yalnızca placeholder'lı alanlar, hatalar kırmızıyla gösteriliyor."

Çıktıdan bir bölüm:
| # | Konum | Kriter | Etkilenen kullanıcılar | Kanıt | Önem | Durum | Düzeltme |
|---|---|---|---|---|---|---|---|
| 1 | Öde düğmesi | 2.1.1 Klavye, 4.1.2 Ad, Rol, Değer | Klavye ve ekran okuyucu kullanıcıları | Tıklama işleyicili `div`, rol veya tabindex yok | Engelleyici | Doğrulandı | `<button type="submit">Öde</button>` kullan |
| 2 | Kart numarası alanı | 3.3.2 Etiketler veya Yönergeler | Ekran okuyucu, bilişsel | Yalnızca placeholder, yazınca kayboluyor | Yüksek | Doğrulandı | Görünür `<label for>` ekle; format ipucunu `aria-describedby` ile ver |
| 3 | Hata durumu | 1.4.1 Rengin Kullanımı, 3.3.1 Hata Tanımlama | Renk körü kullanıcılar | Yalnızca kırmızı kenarlık | Yüksek | Ekran görüntüsünden `[VARSAYIM]` | `aria-describedby` ile bağlı hata metni ve ikon ekle |
