---
description: Bir UI bileşeninin teknik API'sini geliştirme öncesinde framework'ten bağımsız biçimde tasarlar: sorumluluk, prop'lar veya girdiler, iç ve kontrollü durum, olaylar, slot'lar veya kompozisyon noktaları, varyantlar, görsel ve etkileşim durumları, erişilebilirlik semantiği ve klavye davranışı, test durumları. Bir geliştirici yeniden kullanılabilir bir bileşen yazmak veya yeniden düzenlemek üzereyken, bir tasarım teslimi bileşen sözleşmesine dönüştürülecekken ya da bir bileşenin prop sayısı kontrolden çıktığında kullanılır.
related: design-system-component-spec, accessibility-audit, state-management-design, unit-test-writing, design-handoff
prompt: Yönetim ekranlarımızda tekrar kullanacağımız aranabilir bir seçim kutusu (combobox) için bileşen API'si tasarla. Asenkron seçenekler ve çoklu seçim gerekiyor.
---

# UI Bileşeni Tasarlama

## Amaç
Kod yazılmadan önce bileşenin sözleşmesinde uzlaşmak; böylece bileşen yeniden kullanılabilir, erişilebilir ve test edilebilir olur, bir prop-bayrak yığınına dönüşmez. Çıktı, geliştiricilerin uygulayabileceği ve inceleyenlerin karşılaştırabileceği bir bileşen şartnamesidir.

## Ne zaman kullanılır
- Bir ürün veya tasarım sistemi için yeni, yeniden kullanılabilir bir bileşen yazılmak üzereyken.
- Tasarımcının teslimi bir bileşen gösteriyor ve geliştiricilerin onun teknik API'sine ihtiyacı varken.
- Mevcut bir bileşenin kullanımı zorlaşmışsa (çok sayıda boolean prop, belirsiz durum sahipliği) ve yeniden tasarım gerekiyorsa.

## Ne zaman kullanılmaz
- Tasarımcılar için görsel token'lar ve kullanım rehberiyle tasarım sistemi düzeyindeki şartname için `design-system-component-spec` kullanılır.
- Uygulama genelindeki veya sunucu verisinin nerede tutulacağına karar vermek için `state-management-design` kullanılır.
- Uygulanmış bir arayüzü WCAG'ye göre kontrol etmek için `accessibility-audit` kullanılır.

## Girdiler
Zorunlu:
- Bileşenin ne yapması gerektiği: bir tasarım, ekran görüntüsü tarifi, kullanıcı hikayesi veya kullanım durumları listesi.

İsteğe bağlı, kaliteyi artırır:
- UI framework'ü ve stil yaklaşımı, mevcut tasarım sistemi bileşenleri ve isimlendirme kuralları.
- Bilinen tüketiciler (ekranlar) ve farklılaşan ihtiyaçları.
- Tasarım token'ları, desteklenen diller, yazı yönü (LTR/RTL), tarayıcılar ve cihazlar.

Kullanım durumları eksikse bileşenin kullanılacağı iki üç ana ekranı sor. Tasarımdan çıkardığın her gereksinimi `[VARSAYIM]` olarak işaretle.

## Süreç
1. Tek sorumluluğu bir cümleyle yaz; desteklemesi gereken kullanım durumlarını ve kapsam kaymasını önlemek için bilerek desteklemediklerini listele.
2. Bileşenin izlemesi gereken mevcut bir native eleman, tasarım sistemi bileşeni veya bilinen bir ARIA Authoring Practices deseni (ör. combobox, dialog, tabs, disclosure) olup olmadığını kontrol et; deseni adlandır.
3. Bileşenin ayrı bölgeleri varsa (tetikleyici, liste, öğe, alt bilgi) kompozisyon parçalarına böl; tüketicilerin içeriği değiştirmesi gerekiyorsa yapılandırma bayrakları yerine kompozisyonu (children, slot, render fonksiyonu) tercih et.
4. Prop'ları veya girdileri tanımla: ad, tür, zorunlu veya isteğe bağlı, varsayılan ve kısıtlar. Boolean kümelerini tek bir numaralandırılmış variant veya size prop'uyla değiştir; imkânsız kombinasyonlar ifade edilemez olsun.
5. Durum sahipliğine karar ver: hangi durum içeride, hangisi üst bileşen tarafından kontrol edilebilir (value/on-change, open/on-open-change çiftleri), hangisi türetilmiş. Kontrollü ve kontrolsüz kullanımı yalnızca tüketicilerin ikisine de ihtiyacı varsa destekle.
6. Olayları veya callback'leri payload'ları ve zamanlamalarıyla tanımla (değişimde mi onayda mı, asenkron aramada debounce) ve eskimiş asenkron sonuçların iptalini belirt.
7. Görsel ve etkileşim durumlarını say: varsayılan, hover, focus-visible, active, disabled, read-only, yükleniyor, boş, hata ve taşma (uzun metin, çok öğe, dar genişlik, RTL).
8. Erişilebilirliği belirle: rol ve erişilebilir ad kaynağı, ilişkiler (labelled-by, described-by, controls, active-descendant), klavye etkileşim tablosu, açılış ve kapanışta odak yönetimi, asenkron değişikliklerin duyurulması, WCAG 2.2'ye göre hedef boyutu ve kontrast.
9. Performans ve dayanıklılığı not et: büyük listeler (verilmediyse sanallaştırma eşiği `[VARSAYIM]`), memoization sınırları, başarısız yüklemelerde hata gösterimi ve yükleme sırasında yerleşim kayması olmaması.
10. Test durumlarını yaz: kullanım durumu başına davranış testleri, yalnızca klavyeyle testler, ekran okuyucu adı ve durum kontrolleri, uç durumlar (boş, hata, yavaş ağ).
11. Tasarım ve ürün için açık soruları listele; ardından bileşen bir tasarım sistemine girecekse `design-system-component-spec`, durum ekranlar arasında paylaşılıyorsa `state-management-design`, testler için `unit-test-writing` öner.

## Çıktı formatı
```markdown
# Bileşen: <Ad>
Sorumluluk: <tek cümle> · Desen: <native eleman / ARIA deseni>
Kapsam dışı: ...

## Anatomi / Kompozisyon
- <Parça> — <rol>

## API
| Prop / girdi | Tür | Varsayılan | Zorunlu | Notlar / kısıtlar |
|---|---|---|---|---|
| Olay | Payload | Ne zaman tetiklenir | Notlar |
|---|---|---|---|

## Durum Sahipliği
- İç: ... · Kontrol edilebilir: ... · Türetilmiş: ...

## Durumlar ve Varyantlar
| Durum / varyant | Görsel | Davranış |
|---|---|---|

## Erişilebilirlik
- Rol / ad: ... · Klavye: | Tuş | Aksiyon | · Odak: ... · Duyurular: ...

## Test Durumları
- ...

## Açık Sorular ve Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Bileşenin tek bir sorumluluğu ve açık bir kapsam dışı listesi var.
- [ ] Çelişkili kombinasyonlara izin veren boolean prop kümesi yok; varyantlar numaralandırılmış.
- [ ] Her durum parçasının sahipliği açık (iç, kontrol edilebilir, türetilmiş).
- [ ] Klavye etkileşimi, odak yönetimi ve erişilebilir adlar belirlenmiş ve adı verilen desene uyuyor.
- [ ] Yalnızca varsayılan değil; yükleniyor, boş, hata ve taşma durumları da tanımlı.
- [ ] Çıkarılan gereksinimler `[VARSAYIM]` olarak işaretli ve açık sorularda listelenmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her tüketici isteğine bir prop ekleyip bileşeni onlarca bayrağa boğmak. Bunun yerine kompozisyon ve varyant kullan.
- Native kontrolleri genel kapsayıcılar ve tıklama handler'larıyla yeniden yazmak. Native elemandan veya ARIA deseninden başla ve klavye davranışını koru.
- Yalnızca mutlu durumu tasarlamak. Asenkron bileşenler hata verir, yavaş yüklenir ve boş döner; önce bu durumları tasarla.

## Örnek
Girdi: "Yönetim ekranları için aranabilir seçim kutusu, asenkron seçenekler, çoklu seçim."

Zayıf: "Prop'lar: `isMulti`, `isAsync`, `isSearchable`, `isClearable`, `isLoading`, `options`, `onChange`."

Güçlü bölüm:
- Desen: listbox açılır penceresiyle ARIA combobox; çoklu seçimde seçilen öğeler kaldırılabilir chip olarak gösterilir.
- API: `value: Option[]` + `onValueChange(Option[])` (kontrol edilebilir); `loadOptions(query, signal) => Promise<Option[]>`; `selectionMode: "single" | "multiple"`.
- Davranış: arama debounce edilir `[VARSAYIM: 250 ms, tasarımla doğrula]`; eskimiş yanıtlar `signal` ile iptal edilir.
- Klavye: Aşağı ok listeyi açar ve aktif seçeneği taşır; Enter seçer; Escape kapatır ve odağı girişe döndürür; boş girişte Backspace son chip'i kaldırır.
- Durumlar: yükleniyor ("Aranıyor..." kibarca duyurulur), boş ("... için sonuç yok"), yeniden deneme seçeneğiyle hata.
