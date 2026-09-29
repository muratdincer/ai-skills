---
name: design-system-component-spec
description: "Yeniden kullanılabilir bir tasarım sistemi bileşenini amacı, anatomisi, varyantları, boyutları, durumları, tasarım token'ları, davranışı, içerik kuralları, erişilebilirlik gereksinimleri, yap/yapma kullanım kuralları ve geliştirme için API/prop'larıyla tanımlar. Tasarım sistemine yeni bir bileşen önerildiğinde, mevcut bir bileşenin dokümante edilmesi veya kırıcı bir değişiklik geçirmesi gerektiğinde ya da ekipler aynı kalıbın farklı sürümlerini geliştirdiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 10-design
  role: ux-ui-designer
  area: design
  title: "Tasarım sistemi bileşeni tanımlama"
  related: "design-handoff, wireframe-spec, component-design, accessibility-audit, microcopy"
  prompt: "Web ve mobil ekiplerin aynı şekilde geliştirebileceği bir Toast bildirim bileşeni için tasarım sistemi spesifikasyonu yaz."
---

# Tasarım Sistemi Bileşeni Tanımlama

## Amaç
Bir bileşeni bir kez ve yeterince kesin tanımlamak. Böylece tasarımcılar onu tutarlı kullanır, her platform ekibi aynı anatomi, durum, token ve erişilebilirlik davranışını geliştirir.

## Ne zaman kullanılır
- Yeni bir kalıp iki veya daha fazla üründe ortaya çıktığında ve ortak bileşene dönüşmesi gerektiğinde.
- Mevcut bir bileşen dokümante edilmemiş, tutarsız geliştirilmiş veya değişmek üzereyse.
- Tasarım sistemine yapılan bir katkının kabul öncesi gözden geçirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Tek bir özellik ekranı geliştirme için tanımlanıyorsa `design-handoff` kullanılır.
- Ön yüz bileşeninin kod düzeyindeki yapısı tasarlanıyorsa `component-design` kullanılır.
- Mevcut arayüzün erişilebilirlik denetimi gerekiyorsa `accessibility-audit` kullanılır.

## Girdiler
Zorunlu:
- Bileşen adı ve çözdüğü problem (veya göründüğü yerlerden örnekler).
- Hedef platformlar (web, iOS, Android, diğer).

İsteğe bağlı, kaliteyi artırır:
- Mevcut token seti ve adlandırma kuralı.
- Birbirinden farklılaşmış mevcut uygulamaların ekran görüntüleri veya tarifleri.
- Birlikte var olması veya yerini alması gereken ilgili bileşenler.
- Yerleşik içerik için marka sesi rehberi.

Ad, problem veya platformlar eksikse sor. Diğer boşluklar açık soru olur.

## Süreç
1. Bileşenin işini tek cümleyle yaz ve benzer bileşenler yerine ne zaman seçilmesi gerektiğini belirt (ör. Toast, Banner ve Dialog karşılaştırması). Mevcut bir bileşen ihtiyacı karşılıyorsa bileşeni reddet ve bu öneriyi kaydet.
2. Mevcut kullanımların veya örneklerin envanterini çıkar, nerede ayrıştıklarını not et; varyant setini zevk değil bu ayrışmalar belirler.
3. Anatomiyi tanımla: numaralı parçalar, hangilerinin zorunlu hangilerinin isteğe bağlı olduğu, iç içe kullanım kuralları.
4. Varyantları (anlamsal; ör. bilgi/başarı/uyarı/hata) ve boyutları tanımla. Her varyantı ayrı bir kullanımla gerekçelendir; dekoratif olanları çıkar.
5. Durumları tanımla: varsayılan, hover, focus-visible, basılı, pasif, yükleniyor, seçili, hata ve bileşene özgü durumlar (ör. kendiliğinden kapanan, kalıcı).
6. Her parçayı ve durumu tasarım token'larına eşle (renk, tipografi, boşluk, köşe yarıçapı, yükselti, hareket). Ekibin adlandırmasını kullan; token uydurma, gerekiyorsa `[ÖNERİLEN TOKEN]` olarak işaretle.
7. Davranışı tanımla: tetikleyiciler, kapatma, zamanlama, üst üste binme/kuyruk, taşma ve kesme, duyarlı ve RTL davranışı, azaltılmış hareket.
8. Erişilebilirliği WCAG 2.2 ve ilgili WAI-ARIA Authoring Practices kalıbına göre tanımla: rol, erişilebilir ad, klavye etkileşimi, odak yönetimi, duyurular, kontrast, hedef boyutu.
9. İçerik kurallarını yaz: uzunluk sınırları, ton, büyük/küçük harf kullanımı, bileşene asla konmayacaklar; `microcopy` becerisine bağla.
10. Kullanım rehberini eşli yap/yapma kuralları olarak yaz; varsayılanlarıyla geliştirme API'sini (prop, olay, slot) ve kırıcı değişiklikler için sürümleme notunu ekle.
11. Çıkarımları `[VARSAYIM]` olarak işaretle ve açık soruları sorumlularıyla listele.
12. Hedef devam ediyorsa kod geliştirmesi için `component-design`, bileşeni kullanan ilk özellik için `design-handoff` veya geliştirme sonrası `accessibility-audit` öner.

## Çıktı formatı
```markdown
# Bileşen: <Ad>
| Alan | Değer |
|---|---|
| Durum | Önerildi / Beta / Kararlı / Kullanımdan kalkıyor |
| Platformlar | ... |
| Yerini aldığı / ilgili | ... |

## Amaç ve Ne Zaman Kullanılır
- Şu durumda kullan: ...  - Bunun yerine: <bileşen>, şu durumda ...

## Anatomi
1. <parça> (zorunlu/isteğe bağlı) — ...

## Varyantlar ve Boyutlar
| Varyant | Kullanım | Not |

## Durumlar
| Durum | Görsel değişim | Token'lar | Davranış |

## Token'lar
| Parça | Özellik | Token |

## Davranış
- Tetikleyici / kapatma / zamanlama / kuyruk / taşma / RTL / azaltılmış hareket

## Erişilebilirlik
- Rol / ad / klavye / odak / duyuru / kontrast / hedef boyutu

## İçerik Kuralları
- ...

## Kullanım
| Yap | Yapma |

## API
| Prop / olay | Tip | Varsayılan | Açıklama |

## Açık Sorular ve Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Spesifikasyon, komşu bir bileşenin ne zaman tercih edilmesi gerektiğini belirtiyor.
- [ ] Her varyantın ayrı bir kullanımı, her durumun token eşlemesi var.
- [ ] Klavye, odak, rol ve duyuru davranışı tanımlı.
- [ ] Davranış taşma, kuyruk, RTL ve azaltılmış hareketi kapsıyor.
- [ ] API'nin varsayılanları var ve adları platformlar arasında tutarlı.
- [ ] Önerilen token'lar ve çıkarımlar etiketli; var olmayan hiçbir şey mevcutmuş gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca görseli tanımlamak. Bileşenler renkten değil davranıştan (zamanlama, odak, kuyruk) bozulur; önce davranışı tanımla.
- Varyant patlaması. Her varyant bakım yükünü katlar; ayrı bir kullanımı olmayanları birleştir.
- Bir platformun alışkanlıklarını tümüne dayatmak. Ortak anlamı koru, rehberlerin ayrıştığı yerde platforma özgü etkileşime izin ver ve bunu belgele.

## Örnek
Girdi: "Web ve mobil için Toast bileşeni; ekipler şu an kendi sürümlerini yapıyor."

Zayıf bölüm: "Toast: altta çıkan küçük pencere, birkaç saniye sonra kaybolur."

Güçlü bölüm:
- Şu durumda kullan: kullanıcı eyleminin kısa ve akışı bölmeyen onayı. Kalıcı sistem durumu için Banner, karar gerekiyorsa Dialog kullan.
- Davranış: eylem içermiyorsa `[TBD]` saniye sonra kendiliğinden kapanır; hover ve odakta sayaç durur; en fazla 1 görünür, diğerleri kuyruğa girer.
- Erişilebilirlik: `role="status"` (hata varyantında `role="alert"`); odağı asla taşımaz; eyleme klavyeyle erişilir.
