---
name: design-handoff
description: "Bir ekran, akış veya özellik için geliştiriciye hazır bir tasarım teslimi hazırlar; yerleşim ve boşluk ölçüleri, tasarım token'ları, bileşen eşlemesi, etkileşimler ve hareket, tüm uç durumlar, duyarlı (responsive) kurallar, erişilebilirlik notları, içerik ve varlıklar ile açık kararları kapsar. Bir tasarım onaylanıp geliştirmeye geçerken, geliştiriciler \"bu tam olarak ne yapmalı\" diye sorduğunda veya maket ya da tasarım dosyasının yanına bir teslim notu gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 10-design
  role: ux-ui-designer
  area: design
  title: "Tasarım teslimi hazırlama"
  related: "wireframe-spec, design-system-component-spec, user-flow, microcopy, acceptance-criteria"
  prompt: "Web ekibi bir sonraki iterasyonda başlayabilsin diye yeni ödeme adımının (kart ile ödeme) tasarım teslimini hazırla."
---

# Tasarım Teslimi Hazırlama

## Amaç
Onaylanmış bir tasarımı eksiksiz ve yoruma yer bırakmayan bir geliştirme özetine dönüştürmek. Böylece geliştiriciler durumları, boşlukları, davranışı veya içeriği tahmin etmeden tasarlananı geliştirir, QA da doğrulayabilir.

## Ne zaman kullanılır
- Bir ekran, akış veya özellik tasarımı onaylanıp geliştirilmek üzereyken.
- Geliştiriciler makette görünmeyen davranış, durum veya ölçüleri tekrar tekrar sorduğunda.
- Tasarım mevcut bir bileşeni değiştiriyor ya da işaretlenmesi gereken yeni bir kalıp getiriyorsa.
- Dış kaynak veya dağıtık bir ekibin kendi başına yeterli bir spesifikasyona ihtiyacı olduğunda.

## Ne zaman kullanılmaz
- Ekranın yapısına hâlâ karar veriliyorsa `wireframe-spec` kullanılır.
- Tasarım sistemi için yeniden kullanılabilir bir bileşen tanımlanıyorsa `design-system-component-spec` kullanılır.
- Tasarım kalitesine geri bildirim isteniyorsa `design-critique` kullanılır.

## Girdiler
Zorunlu:
- Teslim edilecek tasarım: maket tarifi, tasarım dosyası dışa aktarımı, ekran görüntüleri veya ayrıntılı wireframe.
- Hedef platform(lar): web, iOS, Android, masaüstü.

İsteğe bağlı, kaliteyi artırır:
- Tasarım sistemi adı ve token seti; mevcut bileşen kütüphanesi.
- Tasarımın karşıladığı kullanıcı akışı, gereksinimler veya kullanıcı hikâyeleri.
- Kırılma noktaları (breakpoint), desteklenen cihaz ve tarayıcılar, yerelleştirme dilleri.
- İzlenecek analitik olaylar.

Tasarım veya platform yoksa iste. Diğer her şey açık soru olur.

## Süreç
1. Kapsamı yeniden ifade et: teslimin hangi ekranları, akış adımlarını ve platformları kapsadığını, her birinin hangi gereksinimi veya hikâyeyi karşıladığını yaz. Dışarıda kalanları kapsam dışı olarak listele.
2. Görünen her öğeyi mevcut bir tasarım sistemi bileşenine ve varyantına eşle. Her sapmayı veya yeni bileşeni gerekçesiyle `[YENİ]` ya da `[SAPMA]` olarak işaretle; bileşenleri sessizce çatallama.
3. Yerleşimi tanımla: grid, bölgeler, hizalama ve boşluklar; token varsa ham piksel yerine token kullan (ör. `space-300`). Yalnızca piksel değeri biliniyorsa onu ver ve `[TOKEN YOK]` olarak işaretle.
4. Her öğe için görsel token'ları belirt: renk, tipografi, gölge/yükselti, köşe yarıçapı, ikonografi. Token adı uydurma; token seti bilinmiyorsa `[BİLİNMİYOR]` yaz.
5. Her etkileşimli öğenin etkileşimini tarif et: tetikleyici, tepki, gidilen hedef, odak hareketi, pasif olma koşulları ve hareket (süre, easing, azaltılmış hareket alternatifi).
6. Her ekran ve bileşen için durumları sırala: varsayılan, hover, odak, aktif, pasif, yükleniyor, boş, kısmi, hata, başarı, çevrimdışı, yetki yok, uzun içerik ve kesme. Her durum ya tanımlanır ya da açıkça `[TBD]` olarak listelenir.
7. Her kırılma noktası için duyarlı davranışı tanımla: neyin yeniden aktığı, gizlendiği, alt alta dizildiği veya bileşen değiştirdiği.
8. WCAG 2.2'ye göre erişilebilirlik notları ekle: okuma ve odak sırası, erişilebilir ad ve roller, başlık seviyeleri, kontrast çiftleri, hedef boyutu, hata duyurusu, klavye yolları.
9. İçeriği topla: anahtarlarıyla birlikte nihai metinler, dinamik değerler ve sınırları, çoğul biçimler, yerelleştirmede metin uzaması. Bitmemiş metinleri `microcopy` veya `error-message-writing` becerisine yönlendir.
10. Varlıkları (ikon, illüstrasyon, görsel) format, boyut, yoğunluk varyantları ve alternatif metinleriyle; verildiyse analitik olaylarla birlikte listele.
11. Durum ve etkileşimlerden doğrulanabilir kabul kontrolleri çıkar, açık kararları sorumlusuyla listele. Tasarımın gösterdiğini senin çıkarımından ayır; çıkarımları `[VARSAYIM]` olarak etiketle.
12. Hedef devam ediyorsa kontrolleri resmileştirmek için `acceptance-criteria`, her `[YENİ]` bileşen için `design-system-component-spec` veya eksik metinler için `microcopy` öner.

## Çıktı formatı
```markdown
# Tasarım Teslimi: <özellik / ekran>
| Alan | Değer |
|---|---|
| Platformlar / kırılma noktaları | ... |
| Karşıladığı iş | <hikâye / gereksinim no> |
| Tasarım kaynağı | <dosya / sürüm / bağlantı veya [BİLİNMİYOR]> |
| Tasarım sistemi | <ad / sürüm veya [BİLİNMİYOR]> |

## Kapsam
- Kapsam içi: ...  - Kapsam dışı: ...

## Bileşen Eşlemesi
| Öğe | Bileşen / varyant | Durum (mevcut / [YENİ] / [SAPMA]) | Not |

## Yerleşim ve Token'lar
| Bölge / öğe | Boşluk | Renk | Tipografi | Diğer |

## Etkileşimler ve Hareket
| Öğe | Tetikleyici | Davranış | Odak / gezinme | Hareket |

## Durumlar
| Ekran / bileşen | Durum | Görsel değişim | İçerik | Davranış |

## Duyarlı Kurallar
| Kırılma noktası | Değişiklikler |

## Erişilebilirlik (WCAG 2.2)
- Odak sırası: ...  - Ad / rol: ...  - Kontrast: ...  - Duyurular: ...

## İçerik
| Anahtar | Metin | Azami uzunluk / dinamik değer | Not |

## Varlıklar ve Analitik
- ...

## Kabul Kontrolleri
- [ ] ...

## Açık Kararlar ve Varsayımlar
1. <karar> — <sorumlu> — <gereken tarih>
```

## Kalite kontrol listesi
- [ ] Her öğe bir bileşene eşlenmiş ya da `[YENİ]` / `[SAPMA]` olarak işaretlenmiş.
- [ ] Her ekranın yükleniyor, boş, hata ve uzun içerik durumları tanımlı veya `[TBD]` olarak işaretli.
- [ ] Değerler, varsa tasarım token'larıyla verilmiş; hiçbir token adı uydurulmamış.
- [ ] Her etkileşimli öğenin klavye, odak ve erişilebilir ad notu var.
- [ ] Kabul kontrolleri QA tarafından tasarımcıya sormadan gözlemlenebilir.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve açık kararların sorumlusu var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca mutlu yolu teslim etmek. Yeniden işin çoğu eksik hata, boş ve taşma durumlarından gelir; bunları ekran ekran sırala.
- Token varken ham piksel ölçüsü vermek. Temalandırmayı bozar ve sistemden sapar; token'a referans ver.
- Davranışı prototipin içinde örtük bırakmak. Yazıya dök; prototipler zamanlama, doğrulama ve odak kurallarını göstermez.

## Örnek
Girdi: "Ödeme adımı, yalnızca web, kart formu ve kayıtlı kartlar listesi, kendi tasarım sistemimizi kullanıyor."

Zayıf bölüm: "Kart formu maketteki gibi. Geçersizse hata göster."

Güçlü bölüm:
| Ekran / bileşen | Durum | Görsel değişim | İçerik | Davranış |
|---|---|---|---|---|
| Kart numarası alanı | hata | kenarlık `color-border-danger`, ikon | "Kart numarasını kontrol edin" `[metin TBD]` | Odaktan çıkınca doğrula, live region ile duyur, odak alanda kalır |
| Kayıtlı kartlar listesi | boş | liste gizli | — | Kart formu varsayılan olarak açık `[VARSAYIM]` |
| Öde düğmesi | yükleniyor | spinner, etiket korunur | — | Pasif, çift gönderimi engeller |
