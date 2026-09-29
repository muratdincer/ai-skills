---
description: "Sonuçlara bağlı bir ürün yol haritası oluşturur; Şimdi/Sonra/Daha Sonra ya da güven seviyeli zaman çizelgesi biçiminde temaları, hedef sonuçları, ana girişimleri, bağımlılıkları, açıkça planlanmayanları ve yol haritasının nasıl güncelleneceğini gösterir. Ürün sahibi veya yöneticisinin yönü paydaşlara anlatması, önümüzdeki çeyrekler için ekipleri hizalaması ya da bir özellik listesini sonuç odaklı bir plana dönüştürmesi gerektiğinde kullanılır."
related: "product-vision, okr-definition, release-planning, backlog-prioritization, program-roadmap"
prompt: "İK self-servis uygulamamız için bu 25 özellik talebini Şimdi/Sonra/Daha Sonra yol haritasına dönüştür; bu yılki hedeflerimiz daha az İK talebi ve daha yüksek mobil kullanım."
---

# Ürün Yol Haritası

## Amaç
Ürünün nereye gittiğini ve nedenini, paydaşları sonuçlar ve sıralama konusunda hizalayan ama belirsizlik konusunda dürüst kalan bir biçimde anlatmak. İyi bir yol haritası bir teslimat sözleşmesi değil, niyet ve öncelik beyanıdır.

## Ne zaman kullanılır
- Önümüzdeki çeyrekler veya bir planlama dönemi planlanıp yönetime, satışa veya diğer ekiplere anlatılacaksa.
- Bir özellik listesinin veya backlog'un stratejik temalara çevrilmesi gerekiyorsa.
- Paydaşlar sürekli "X ne zaman gelecek?" diye soruyorsa ve cevabın tutarlı olması gerekiyorsa.
- Bir strateji değişikliğinden sonra neyin kaydığını ve neyin bırakıldığını göstermek için.

## Ne zaman kullanılmaz
- Belirli bir sürüm için kapsam ve tarih taahhüdü verilecekse `release-planning` kullanılır.
- Bir programdaki birçok ekibin kilometre taşları koordine edilecekse `program-roadmap` kullanılır.
- Uzun vadeli hedefin kendisi belirlenecekse `product-vision` kullanılır.

## Girdiler
Zorunlu:
- Ufuk için ürün hedefleri veya sonuçları (OKR'lar, strateji, vizyon). Yoksa sor; hedefsiz bir yol haritası sadece özellik listesidir.
- Aday girişimler veya özellikler.

İsteğe bağlı, kaliteyi artırır:
- Hedef kitle (yöneticiler, müşteriler, iç ekipler) ve ufuk (ör. 12 ay).
- Kapasite sinyalleri, bilinen taahhütler, yasal tarihler, bağımlılıklar.
- Tercih edilen format: Şimdi/Sonra/Daha Sonra veya zaman çizelgesi.

## Süreç
1. Hedef kitleyi ve ufku netleştir; bu, ayrıntı düzeyini ve tarih gösterilip gösterilmeyeceğini belirler. Dış kitlelere daha az tarih kesinliği verilir.
2. Formatı seç: belirsizlik yüksekse veya ekip sürekli akışla çalışıyorsa Şimdi/Sonra/Daha Sonra; planı dış tarihler, sözleşmeler veya mevzuat belirliyorsa çeyreklik zaman çizelgesi.
3. Aday maddeleri, her biri bir hedefe ve ölçülebilir bir sonuca bağlı 3-6 temada grupla.
4. Tema/girişimleri önceliğe, bağımlılıklara ve kapasiteye göre ufuklara yerleştir. Şimdi = taahhüt edilmiş ve devam ediyor; Sonra = planlanmış, iyileştiriliyor; Daha Sonra = yön, değişime açık.
5. Her yerleşime bir güven seviyesi (Yüksek/Orta/Düşük) ata ve arkasındaki ana varsayımı yaz.
6. Sabit tarihli maddeleri tarihin kaynağıyla (mevzuat, sözleşme, etkinlik) ayrıca işaretle.
7. Maddeleri ufuklar arasında kaydırabilecek ana bağımlılıkları ve riskleri kaydet.
8. Yol haritasında açıkça yer almayanları ve nedenini listele; bu, sessiz beklentileri önler.
9. Güncelleme sıklığını ve değişiklik kuralını tanımla (ör. aylık gözden geçirilir; Şimdi'deki değişiklikler paydaşlara bildirilir).
10. Sahibin sunumda kullanabileceği kısa bir anlatı (3-5 cümle) taslağı hazırla.
11. Kullanıcının hedefi devam ediyorsa Şimdi ufku için `release-planning`, sonuçların ölçüsü yoksa `okr-definition`, birden çok ekip varsa `program-roadmap` öner.

## Çıktı formatı
```markdown
# Ürün Yol Haritası: <ürün> – <ufuk>
Hedef kitle: <kitle> · Son güncelleme: <tarih> · Sonraki gözden geçirme: <tarih veya [TBD]>

## Hedefler
- H1: <hedef> – sonuç metriği: <metrik>

## Yol Haritası
| Tema (hedef) | Şimdi | Sonra | Daha Sonra |
|---|---|---|---|
| <tema> (H1) | <girişim> [Y] | <girişim> [O] | <girişim> [D] |

## Sabit Tarihli Taahhütler
- <madde> – <tarih> – <kaynak>

## Ana Varsayımlar, Bağımlılıklar ve Riskler
- <madde>

## Yol Haritasında Olmayanlar
- <madde> – <gerekçe>

## Bu Yol Haritası Nasıl Değişir
<sıklık, değişiklik kuralı, iletişim>

## Anlatı
<3-5 cümle>
```

## Kalite kontrol listesi
- [ ] Her madde bir hedefe ve bir sonuç metriğine bağlı.
- [ ] Her madde için güven seviyesi gösterilmiş; en düşüğü Daha Sonra'da.
- [ ] Tarihler yalnızca gerçek bir kaynakla gerekçelendirildiğinde var; aksi halde ufuklar kullanılmış.
- [ ] "Yol haritasında olmayanlar" bölümü var.
- [ ] Ayrıntı düzeyi hedef kitleye uygun (yöneticiler için kayıt seviyesinde madde yok).
- [ ] Kapasite, gelir veya tarih rakamı uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Daha Sonra'daki bir maddeyi tarihle sunmak. Paydaşlar bunu söz olarak algılar; tarihleri taahhüt edilmiş iş için sakla.
- Problemler/sonuçlar yerine özellik listelemek. Maddeleri "Bordro ekranı" yerine "Self-servis bordro ile maaş sorularını azalt" gibi çerçevele.
- Şimdi'yi aşırı doldurmak. Şimdi gerçek kapasiteyi aşarsa hiçbir şey ilerlemez; yalnızca gerçekten devam edenleri koy.

## Örnek
Girdi: "İK self-servis uygulaması. Hedefler: daha az İK talebi, daha yüksek mobil kullanım. 25 talep."

Çıktıdan bir bölüm:
| Self-servis yanıtlar (H1: İK talepleri -%20) | Bordro ve izin bakiyesi self-servis [Y] | En sık 20 soruyla politika araması [O] | Sohbet tabanlı İK asistanı [D] |
| Önce mobil (H2: mobil aylık aktif kullanıcı payı) | Mobil izin talebi [Y] | Onaylar için anlık bildirimler [O] | Çevrim dışı mod [D] |
- Yol haritasında olmayan: Özel rapor oluşturucu – az kullanıcıya hizmet ediyor, iki hedefle de bağı yok.
