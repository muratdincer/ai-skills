---
name: team-topology
description: "Değer akışları, bilişsel yük ve bağımlılıklara dayanarak akışa hizalı, platform, destekleyici ve karmaşık alt sistem ekip türleri ile etkileşim modlarını kullanan bir ekip topolojisi tasarlar veya inceler. Ekipler kurulurken veya bölünürken, devirler ve ekipler arası bağımlılıklar teslimatı yavaşlattığında, bir platform ekibi düşünüldüğünde ya da ekip sınırları mimariyle örtüşmediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: team
  title: "Ekip topolojisi tasarlama"
  related: "bounded-context-map, service-decomposition, role-definition, cross-team-dependency-board, org-change-communication"
  prompt: "5 ekibimiz ve 40 mühendisimiz var, her özellik 3 ekibe ihtiyaç duyuyor. E-ticaret platformumuz için bir ekip topolojisi öner."
---

# Ekip Topolojisi Tasarlama

## Amaç
Ekip sınırlarını değer akışları ve mimariyle hizalamak. Böylece işlerin çoğu tek bir ekipten akabilir, bilişsel yük sürdürülebilir olur ve geriye kalan ekipler arası etkileşimler bilinçli ve süreli olur.

## Ne zaman kullanılır
- Ekipler kuruluyor, bölünüyor veya birleşiyor ya da organizasyon hızla büyüyor.
- Özelliklerin çoğu birden fazla ekip gerektiriyor ve teslim süresinde devirler baskın.
- Bir platform, destekleyici veya uzman ekip öneriliyor ve görev tanımı belirsiz.
- Ekip sınırları ile servis/alan sınırları birbirinden uzaklaşmış.

## Ne zaman kullanılmaz
- İhtiyaç ekipler değil yalnızca alan sınırlarıysa `bounded-context-map` kullanılır.
- Tek bir rolün sorumluluklarını tanımlamak için `role-definition` kullanılır.
- Karar verilmiş bir değişikliği duyurmak için `org-change-communication` kullanılır.

## Girdiler
Zorunlu:
- Mevcut ekipler (büyüklük, yetkinlikler, neye sahip oldukları) ve ana ürünler veya değer akışları.

İsteğe bağlı, kaliteyi artırır:
- Mimari veya alan haritası, bağımlılık verisi (başka ekip yüzünden bekleyen işler), teslim süresi metrikleri.
- Kısıtlar: kadro, lokasyonlar ve saat dilimleri, bütçe, mevzuat kaynaklı görevler ayrılığı.

Mevcut sahiplik bilinmiyorsa ekiplerin ve neye sahip olduklarının listesini iste; mevcut durumu uydurma.

## Süreç
1. Değer akışlarını (müşteri yolculukları veya ürünler) ve her birinin dokunduğu sistemleri/alanları haritala.
2. Mevcut sahipliği ve bağımlılıkları haritala: Son işlerden bir örneklemde hangi ekipler gerekti ve iş nerede bekledi.
3. Ekip başına bilişsel yükü değerlendir (alan, sistem, teknoloji sayısı, nöbet yüzeyi); sürdürülebilir yükün üzerindeki ekipleri işaretle.
4. Önce akışa hizalı ekipleri öner: her değer akışı veya sınırlı bağlam (bounded context) için bir ekip, sürdürülebilir sahiplik için boyutlandırılmış (genellikle 5-9 kişi).
5. Birçok akışın ihtiyaç duyduğu ve onların yükünü azaltan yetenekleri belirle; ancak bundan sonra ürün bakışına ve net bir "en ince uygulanabilir platform" kapsamına sahip bir platform ekibi öner.
6. Karmaşık alt sistem ekiplerini yalnızca gerçekten uzmanlık gerektiren alanlarda (ör. fiyatlama motoru, video codec), destekleyici ekipleri ise kalıcı kapı bekçisi olarak değil, süreli koç olarak kullan.
7. Ekipler arası etkileşim modlarını (iş birliği, hizmet olarak sunma, kolaylaştırma) süre ve çıkış kriterleriyle tanımla.
8. Conway yasası uyumunu kontrol et: Hedef mimari ve ekip sınırları birbirini desteklemeli; topolojinin çalışması için mimarinin nerede değişmesi gerektiğini not et.
9. Geçişi sahiplik devri, nöbet değişiklikleri ve doğrulama ölçütleriyle (teslim süresi, ekipler arası bağımlılık, yük anketi) adım adım planla.
10. Kişilere etkileri İK ve yöneticiler için açık sorular olarak listele; isim atama ve tercihler hakkında varsayımda bulunma.
11. Çıkarım yaptığın bağımlılıkları ve yükleri `[VARSAYIM]` olarak işaretle.
12. Kullanıcının hedefi devam ediyorsa yeni roller için `role-definition`, alan sınırları için `bounded-context-map` veya değişikliği duyurmak için `org-change-communication` öner.

## Çıktı formatı
```markdown
# Ekip Topolojisi: <organizasyon / alan>

## Değer Akışları ve Alanlar
| Değer akışı | Alanlar / sistemler | Dahil olan mevcut ekipler |
|---|---|---|

## Mevcut Sorunlar (kanıt)
- ...

## Önerilen Ekipler
| Ekip | Tür | Sahip olduğu | Büyüklük | Bilişsel yük notları |
|---|---|---|---|---|

## Etkileşim Modları
| Ekip A | Ekip B | Mod | Süre / çıkış kriteri |
|---|---|---|---|

## Gerekli Mimari Değişiklikler
- ...

## Geçiş Planı ve Başarı Ölçütleri
| Adım | Değişiklik | Ölçüt |
|---|---|---|

## Açık Sorular / Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Her akışa hizalı ekip, akışındaki işlerin çoğunu başkalarını beklemeden teslim edebiliyor.
- [ ] Platform ve destekleyici ekiplerin açık tüketicileri, kapsamı ve etkileşim modları var.
- [ ] Bilişsel yük yalnızca kişi sayısıyla değil, ekip bazında değerlendirildi.
- [ ] Ekip sınırları hedef mimariyle örtüşüyor ya da gereken mimari değişiklik belirtildi.
- [ ] İş birliği modları süreli ve çıkış kriterleri var.
- [ ] İsimle kişi ataması yok; kişilere etkiler açık soru olarak listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Teknolojiye göre bileşen ekiplerini (frontend ekibi, veritabanı ekibi) akışa hizalı diye etiketlemek. Gerçek işlerle test et.
- Kayıt kuyruğuna dönüşen bir platform ekibi. Self-servis arayüzler tanımla ve tüketici teslim süresini ölç.
- Mimariyi değiştirmeden yeniden organize olmak. Monolit paylaşılıyorsa yeni ekipler yine birbirini bekler.

## Örnek
Girdi: 5 ekip (web, mobil, backend, veri, operasyon), 40 mühendis; ödeme adımı değişiklikleri web, backend ve operasyon gerektiriyor.

Çıktıdan bir bölüm:
- Öneri: Checkout (akışa hizalı: web+mobil+backend yetkinlikleri), Katalog ve Arama (akışa hizalı), Sipariş Karşılama (akışa hizalı), Geliştirici Platformu (platform: CI/CD, çalışma ortamı, hizmet olarak gözlemlenebilirlik), Veri Destek (destekleyici, 2 çeyrek).
- Etkileşim: Checkout ↔ Geliştirici Platformu = hizmet olarak sunma; Veri Destek ↔ Checkout = olaylar self-servis yayınlanana kadar kolaylaştırma.
- `[VARSAYIM]` Checkout bugün iki repoya bölünmüş ödeme adaptörü koduna sahip; teyit edilmeli.
