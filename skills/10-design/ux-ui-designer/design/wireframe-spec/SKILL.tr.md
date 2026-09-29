---
name: wireframe-spec
description: "Tek bir ekran veya görünüm için wireframe'i metinle tarif eder; amaç, yerleşim bölgeleri, bileşenler, içerik önceliği, etkileşimler, tüm durumlar (varsayılan, yükleniyor, boş, hata, kısmi, yetki), duyarlı davranış ve erişilebilirlik notlarını kapsar. Bir ekranın görsel maketten önce veya onun yerine tanımlanması gerektiğinde, \"bu ekranda ne olacak\" sorulduğunda ya da wireframe'in ürün ve yazılım ekiplerince metin üzerinden incelenmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 10-design
  role: ux-ui-designer
  area: design
  title: "Wireframe tarifi"
  related: "user-flow, information-architecture, screen-requirements, design-handoff, microcopy"
  prompt: "E-ticaret web uygulamamızın sipariş geçmişi ekranı için boş ve hata durumları dahil wireframe tarifi yaz."
---

# Wireframe Tarifi

## Amaç
Bir ekranın neleri, hangi öncelikle ve hangi durumlarda içerdiğini görsel stil olmadan tanımlamak. Böylece paydaşlar yapı ve davranış üzerinde erkenden uzlaşır, tasarımcılar ve geliştiriciler aynı şeyi üretir.

## Ne zaman kullanılır
- Kullanıcı akışında uzlaşıldıysa ve her ekranın artık yapıya ihtiyacı varsa.
- Bir ekranın metin üzerinden (doküman, kayıt, eşzamansız inceleme) tartışılması veya incelenmesi gerektiğinde.
- Mevcut bir ekran yeniden tasarlanıyor ve içerik önceliği baştan belirlenmeliyse.

## Ne zaman kullanılmaz
- Ekranlar arası adım sırası henüz tanımlı değilse `user-flow` kullanılır.
- İhtiyaç geliştiriciler için alan bazında işlevsel gereksinimlerse `screen-requirements` kullanılır.
- Tasarım son hâlini aldıysa ve geliştirme için ölçüler gerekiyorsa `design-handoff` kullanılır.

## Girdiler
Zorunlu:
- Ekranın amacı: hangi kullanıcı, akıştaki hangi görev veya adım.

İsteğe bağlı, kaliteyi artırır:
- Kullanıcı akışı, ekranda mevcut veriler, iş kuralları, tasarım sistemi bileşenleri, platformlar ve kırılım noktaları, mevcut ekran ve analitiği.

Ekranın kullanıcısı ve görevi yoksa iste. Bilinmeyen veri alanları veya kurallar `[VARSAYIM]` ya da açık soru olur.

## Süreç
1. Ekranın kullanıcısını, birincil görevini, giriş noktalarını ve en önemli tek aksiyonu (birincil CTA) yaz.
2. İçerik ve aksiyonları göreve göre önceliklendir (ilk görülmesi gereken, ikincil, istek üzerine); ilk üçü gerekçelendir.
3. Yerleşim bölgelerini (üst bilgi, navigasyon, ana alan, yan alan, alt bilgi) tanımla ve içeriği öncelik ve okuma sırasına göre yerleştir; ızgaradan ve stilden bağımsız tut.
4. Her bölge için bileşenleri (tercihen tasarım sistemindeki adlarıyla), içeriklerini ve veri kaynaklarını, etiketleri veya `[metin TBD]` notunu listele.
5. Etkileşimleri tarif et: her kontrolün ne yaptığı, geri bildirim, gidilen hedefler, doğrulamanın zamanı, geri alınamaz aksiyonlarda onay.
6. Durumları tanımla: varsayılan, yükleniyor (iskelet veya dönen gösterge), boş (ilk kullanım, sonuç yok, temizlendi), hata (tam sayfa veya satır içi), kısmi veri, yetkiyle kısıtlı, çevrimdışı, uzun içerik ve kırpma.
7. Her kırılım noktası için duyarlı davranışı tanımla: ne yeniden akar, daralır, gizlenir veya yer değiştirir; mobilde dokunma alanları.
8. Erişilebilirlik notlarını ekle: başlık yapısı, odak sırası, sayfa bölgeleri (landmark), ikon düğmelerin etiketleri, hata duyurusu, kontrast ihtiyaçları; uygun yerlerde WCAG 2.2 AA'ya atıf yap.
9. Faydalıysa varsayılan durumun düşük doğruluklu metin veya ASCII taslağını çiz ve temsilî olduğunu belirt.
10. Varsayımları ve açık soruları listele; metinler için `microcopy`, görseller kesinleşince `design-handoff` öner.

## Çıktı formatı
```markdown
# Wireframe: <ekran adı>
Kullanıcı: <...> · Görev: <...> · Giriş: <...> · Birincil aksiyon: <...>

## İçerik Önceliği
1. <öğe> — neden
2. ...

## Yerleşim
| Bölge | Bileşenler | İçerik / veri | Notlar |
|---|---|---|---|

## Etkileşimler
| Öğe | Aksiyon | Sonuç / geri bildirim |
|---|---|---|

## Durumlar
| Durum | Tetikleyici | Kullanıcının gördüğü | Sunulan aksiyon |
|---|---|---|---|
| Yükleniyor | ... | ... | ... |
| Boş (ilk kullanım) | ... | ... | ... |
| Hata | ... | ... | ... |

## Duyarlı Davranış
- <kırılım noktası>: ...

## Erişilebilirlik Notları
- ...

## Taslak (temsilî)
<ASCII veya metin taslak>

## Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Ekranın tek ve net bir birincil aksiyonu ve gerekçeli bir içerik önceliği var.
- [ ] Her veri öğesinin bir kaynağı var ya da `[VARSAYIM]` olarak işaretli.
- [ ] Yükleniyor, boş, hata, kısmi ve yetki durumları tanımlandı.
- [ ] Her hedef kırılım noktası için duyarlı değişiklikler tanımlandı.
- [ ] Odak sırası, başlıklar ve metin olmayan kontrollerin etiketleri ele alındı.
- [ ] Tarif, yapı dışında görsel stil kararı (renk, yazı tipi) içermiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca "tüm veriler dolu" durumunu tanımlamak. Kullanıcılar boş ve hata durumlarında takılır.
- Her öğeye eşit ağırlık vermek. Sıralamayı zorla; ekranın yalnızca bir birincil aksiyonu olabilir.
- Lorem ipsum yer tutucu kullanmak. Kırpma sorunlarını görmek için gerçekçi içerik uzunlukları kullan veya metni `[TBD]` olarak işaretle.

## Örnek
Girdi: "E-ticaret web uygulamamızın sipariş geçmişi ekranı, boş ve hata durumlarıyla."

Çıktıdan bir bölüm:
- Birincil aksiyon: takip veya iade için bir siparişi açmak.
- Öncelik: 1) durumlarıyla son siparişler, 2) tarihe ve duruma göre arama/filtre, 3) tekrar sipariş ver.
- Boş (ilk kullanım): "Henüz siparişin yok" + alışverişe devam bağlantısı. Boş (sonuç yok): "Bu filtrelere uyan sipariş yok" + filtreleri temizle.
- Hata: satır içi uyarı "Siparişlerini yükleyemedik" + tekrar dene; varsa önbellekteki liste gösterilir `[VARSAYIM]`.
