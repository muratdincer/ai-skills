---
name: observation-notes
description: "Ham iş gölgeleme (job shadowing) veya bağlamsal gözlem notlarını süreleri, kullanılan araçları, sorunları, geçici çözümleri, kesintileri ve yazılı süreç ile gerçek süreç arasındaki farkı gösteren bir görev dizisine dönüştürür. Kullanıcılar işbaşında gözlemlendikten sonra, saha notları dağınık olduğunda veya 'ekibi izlerken ne öğrendik?' diye sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Gözlem notlarını yapılandırma"
  related: "as-is-process, interview-notes-analysis, value-stream-map, customer-journey-map, research-synthesis"
  prompt: "İki çağrı merkezi temsilcisini üç saat gölgelediğim notlar bunlar. Görev, sorun ve geçici çözümler olarak yapılandır."
---

# Gözlem Notlarını Yapılandırma

## Amaç
Ham gözlem notlarını işin gerçekte nasıl yapıldığına dair kanıta dönüştürmek. Böylece gereksinimler dokümanlarda veya görüşmelerde anlatılan süreci değil, gerçek görevleri, geçici çözümleri ve sürtünmeleri hedefler.

## Ne zaman kullanılır
- İş gölgeleme, bağlamsal sorgulama veya "beni takip et" oturumundan sonra.
- Görüşmeler ile prosedürler çeliştiğinde ve gerçek iş gözlemlendiğinde.
- As-is süreç modellemesinden önce, modeli insanların gerçekte yaptığına dayandırmak için.

## Ne zaman kullanılmaz
- Notlar soru-cevap şeklindeki bir görüşmeden geliyorsa `interview-notes-analysis` kullanılır.
- Kulvarları ve süreleri olan resmi bir as-is süreç modeli gerekiyorsa `as-is-process` kullanılır (bu çıktıyı girdi olarak alabilir).
- Gözlemler bir prototipin kullanılabilirlik testinden geliyorsa `research-synthesis` kullanılır.

## Girdiler
Zorunlu:
- Gözlem notları (ham metin, mümkünse zaman damgalı).

İsteğe bağlı, kaliteyi artırır:
- Gözlemlenen kişi (rol, deneyim düzeyi, lokasyon), tarih, süre ve işi neyin tetiklediği.
- Karşılaştırma için yazılı prosedür.
- Kullanılan ekran, form, yapışkan not ve tabloların fotoğrafı veya tarifi.

Not verilmemişse iste. Rol ve bağlam eksikse devam et ve bunları açık soru olarak listele.

## Süreç
1. Anonimleştir: gözlemlenen kişilere rol ve kodla (Temsilci A) atıf yap, notlardaki müşteri veya iş arkadaşı verilerini maskele.
2. Gözlemi yorumdan ayır: görülen veya duyulan ("Excel'e geçti, poliçe numarasını kopyaladı") ile bunun ne anlama geldiğini düşündüğün. Her yorumu `[VARSAYIM]` olarak etiketle.
3. Her oturum için görev dizisini yeniden kur: tetikleyici, adımlar, sistemler/araçlar, devirler, bitiş durumu. Notta varsa zaman damgalarını veya süreleri koru; eksik olanları asla tahmin etme.
4. Her olayı etiketle: Görev adımı, Araç/sistem değişimi, Bekleme, Kesinti, Hata/yeniden iş, Geçici çözüm, Yazısız kural ("... ise hep önce ararız"), Yan araç (gölge tablo, kâğıt liste, not), Alıntı.
5. Geçici çözümleri ve gölge araçları açıkça çıkar; her biri karşılanmamış bir ihtiyacın işaretidir. Karşıladığı ihtiyacı yaz.
6. Sorunları kanıtıyla belirle: oturumda görülme sıklığı, ölçüldüyse kaybedilen süre, sonucu (hata, gecikme, müşteri etkisi).
7. Verildiyse yazılı prosedürle karşılaştır: atlanan, eklenen, sırası değişen, başka araçta yapılan adımlar.
8. Gözlemlenen kişiler veya lokasyonlar arasında karşılaştır: ortak örüntüler ile kişisel alışkanlıklar. Bir örüntü en az iki gözlem gerektirir; tekil gözlemler `[TEK GÖZLEM]` olarak işaretlenir.
9. Aday ihtiyaçları ve gereksinim hipotezlerini problem biçiminde çıkar; her birini destekleyen gözlem ID'lerine bağla.
10. Gözlemlenen kişilerle veya yöneticileriyle doğrulanacak açık soruları listele (neden böyle yapıyorlar, oturum dışında ne sıklıkta oluyor).
11. Hedef devam ediyorsa akışı modellemek için `as-is-process`, bekleme ve yeniden işi görmek için `value-stream-map`, takip görüşmeleri yapılırsa `interview-notes-analysis` öner.

## Çıktı formatı
```markdown
# Gözlem Özeti: <süreç / ekip>
Oturumlar: <rol kodları, lokasyon, tarih, süre> · Gözlemci: <rol>

## Görev Dizisi (oturum <kod>)
| # | Saat | Adım | Araç / sistem | Etiket | Not |
|---|---|---|---|---|---|

## Geçici Çözümler ve Gölge Araçlar
| # | Geçici çözüm | Karşıladığı ihtiyaç | Görüldüğü yer | Risk |

## Sorunlar
| # | Sorun | Kanıt (gözlem ID, sıklık, süre) | Sonuç |

## Yazılı ve Gerçek Süreç
- ...

## Aday İhtiyaçlar
- İ1: <problem biçiminde ihtiyaç> (gözlem 3, 7, 12)

## Yorumlar [VARSAYIM] ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Gözlemler ve yorumlar ayrıldı; her yorum etiketli.
- [ ] Hiçbir süre veya sıklık uydurulmadı.
- [ ] Her geçici çözümün arkasındaki ihtiyaç yazıldı.
- [ ] Örüntüler en az iki gözleme dayanıyor ya da `[TEK GÖZLEM]` olarak işaretli.
- [ ] Kişi ve müşteri verileri anonimleştirildi.
- [ ] Aday ihtiyaçlar özellik değil problem ifadesi ve gözlemlere atıf yapıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Geçici çözümü kötü uygulama diye yargılamak. Genellikle sistem gerçek bir ihtiyacı karşılamadığı için vardır; önce ihtiyacı kaydet.
- Tek bir uzman kullanıcıdan genelleme yapmak. Uzmanlar, yeni başlayanların ihtiyaç duyduğu adımları atlar; deneyim düzeyini not et.
- Yalnızca ana akışı kaydetmek. Kesintiler, beklemeler ve yeniden işler en değerli bulgulardır.

## Örnek
Girdi: "10:02 A CRM'i açıyor, müşteriyi arıyor. 10:04 kendi Excel'ine geçiyor, poliçe no kopyalıyor. 'Eski poliçelerde CRM araması çok yavaş.' 10:09 telefon çalıyor, arayanı beklemeye alıyor."

Çıktıdan bir bölüm:
| # | Saat | Adım | Araç | Etiket | Not |
|---|---|---|---|---|---|
| 1 | 10:02 | Müşteri arama | CRM | Görev adımı | |
| 2 | 10:04 | Poliçe no'yu kişisel listede bulma | Excel | Geçici çözüm | Alıntı: "eski poliçelerde çok yavaş" |

Aday ihtiyaç İ1: Temsilciler eski poliçeleri kişisel bir listeye başvurmadan çağrı içinde bulabilmeli (gözlem 2). Neden `[VARSAYIM]`: eski verilerde CRM arama performansı.
