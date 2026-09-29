---
description: Ham müşteri geri bildirimlerini (destek kayıtları, NPS/CSAT yorumları, uygulama mağazası değerlendirmeleri, satış notları, topluluk gönderileri) sıklık, önem derecesi, etkilenen segmentler, anonimleştirilmiş temsilî alıntılar ve her talebin arkasındaki asıl ihtiyaçla temalara ayırır. Birikmiş geri bildirimin önceliklendirilebilir içgörülere dönüştürülmesi gerektiğinde, "müşteriler bize ne söylüyor" sorulduğunda ya da yol haritası ve backlog görüşmelerinden önce kullanılır.
related: research-synthesis, jobs-to-be-done, opportunity-solution-tree, persona, backlog-prioritization
prompt: Geçen çeyreğin 120 NPS yorumu burada; bunları temalara ayır ve en önemli olanları söyle.
---

# Müşteri Geri Bildirimi Sentezi

## Amaç
Dağınık geri bildirimleri; müşterilerin neyle zorlandığını, ne sıklıkta, ne kadar ciddi ve kimin için olduğunu gösteren, kanıta dayalı az sayıda temaya dönüştürmek. Böylece ürün kararları en yüksek sese değil, örüntülere dayanır.

## Ne zaman kullanılır
- Bir veya daha fazla kanaldan gelen geri bildirim yığınının yapılandırılmış bir özete ihtiyacı olduğunda.
- Yol haritası planlaması, backlog önceliklendirmesi veya çeyreklik değerlendirmeden önce.
- Paydaşlar tekil şikâyetleri örnek gösteriyor ve ekibin bunların ne kadar temsilî olduğunu bilmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Girdi planlı bir araştırmanın görüşme dökümleriyse `research-synthesis` kullanılır.
- Tek bir kaydın ele alınması gerekiyorsa `ticket-triage` veya `ticket-response` kullanılır.
- Yayınlanmış bir özelliğin kullanım verisi değerlendirilecekse `feature-adoption-review` kullanılır.

## Girdiler
Zorunlu:
- Geri bildirim maddeleri (metin, dışa aktarım veya yapıştırılmış liste), mümkünse kanal ve tarihle.

İsteğe bağlı, kaliteyi artırır:
- Madde başına müşteri nitelikleri: segment, paket, hesap büyüklüğü, müşteri yaşı, NPS puanı.
- Eşleştirilecek ürün alanları veya mevcut bir tema sınıflandırması.
- Sentezin besleyeceği karar.

Geri bildirim verilmediyse iste. Alıntılanan metinlerdeki adları, e-postaları, telefon numaralarını ve hesap tanımlayıcılarını maskele.

## Süreç
1. Girdinin envanterini çıkar: kanal ve dönem bazında madde sayısını say, örneklem yanlılığını not et (ör. mağaza yorumları olumsuza, satış notları potansiyel müşterilere eğilimlidir, yalnızca kötüleyenler yorum yazmıştır).
2. Birden çok konu içeren maddeleri tekil gözlemlere böl; aksiyona dönüşmeyecek maddeleri ayıkla ve kaç tane olduğunu raporla.
3. Her gözlemde sözel talebi ("Excel'e aktarma ekleyin") asıl ihtiyaçtan ("rakamları denetçime kanıtlamak") ayır; ihtiyacı kaydet ve senin çıkardığın ihtiyaçları `[ÇIKARIM]` olarak işaretle.
4. Gözlemleri aşağıdan yukarıya, özellik değil müşteri problemi olarak adlandırılmış temalara kümele ("Raporları araç dışındaki kişilerle paylaşamıyorum", "Paylaşım özelliği" değil).
5. Her tema için sıklığı (adet ve pay), önem derecesini (engelleyici / önemli / küçük, kullanılan kuralla), etkilenen segmentleri, veri elveriyorsa önceki döneme göre eğilimi ve 1-2 temsilî alıntıyı kaydet.
6. Nitelikler varsa etkilenenlere göre ağırlıklandır: stratejik veya yüksek gelirli segmentlerde yoğunlaşan temaları ve müşteri kaybı ya da kötüleyen puanlarla bağlantılı temaları işaretle.
7. Hataları ve hizmet sorunlarını ürün boşluklarından ve övgülerden ayır; hataları tema listesine değil hata sürecine yönlendir.
8. Temaları sıklık x önem x segment önemi ile sırala; formülü ve nerede muhakeme kullandığını belirt.
9. Çıkarımları yaz: hangi temalar fırsata işaret ediyor, hangileri ek araştırma gerektiriyor, hangileri gürültü veya strateji dışı.
10. Sınırlılıkları (örneklem büyüklüğü, yanlılık, eksik nitelikler) ve açık soruları listele.
11. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: öne çıkan temaları fırsat olarak çerçevelemek için `opportunity-solution-tree` veya `jobs-to-be-done`, mevcut işlerle tartmak için `backlog-prioritization`.

## Çıktı formatı
```markdown
# Geri Bildirim Sentezi: <kaynak(lar)>, <dönem>
Madde: <n> (<kanal dağılımı>) · Ayıklanan: <n> · Bilinen yanlılıklar: ...

## Öne Çıkan Temalar
| # | Tema (müşteri problemi) | Sıklık | Önem | Segmentler | Eğilim | Asıl ihtiyaç |
|---|---|---|---|---|---|---|
| 1 | ... | 23 (%19) | Önemli | ... | artıyor | ... |

## Tema Ayrıntıları
### 1. <tema>
- Kanıt: <adet, kanallar>
- Temsilî alıntılar: > "..." (anonim)
- Görülen sözel talepler: <özellik talepleri>
- Çıkarım: <fırsat / araştırma / göz ardı et> – <neden>

## Hatalar ve Hizmet Sorunları (ayrı yönlendir)
- ...
## Övgüler (korunması gerekenler)
- ...
## Sınırlılıklar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Temalar çözüm olarak değil, müşteri problemi olarak ifade edildi.
- [ ] Her temanın bir sayısı ve en az bir gerçek, anonim alıntısı var; hiçbir şey uydurulmadı.
- [ ] Sözel talepler ile asıl ihtiyaçlar ayrıldı; çıkarılan ihtiyaçlar etiketli.
- [ ] Sıralama mantığı açık, örneklem yanlılıkları belirtildi.
- [ ] Hatalar ürün boşluklarından ayrıldı.
- [ ] Alıntılardaki kişisel veriler maskelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Özellik taleplerini kelimesi kelimesine saymak. On farklı talep aynı ihtiyaçtan doğabilir, tek bir talep üç ihtiyacı gizleyebilir; ihtiyaca göre kümele.
- Sıklığı önem sanmak. Kilit bir segmentteki nadir bir engelleyici sorun, yaygın ama küçük bir rahatsızlıktan ağır basabilir.
- Bir kanalın yanlılığını tüm müşteri tabanının görüşü gibi sunmak. Örneklemde kimin olmadığını yaz.

## Örnek
Girdi: "Geçen çeyreğin 120 NPS yorumu."

Çıktıdan bir bölüm:
| # | Tema | Sıklık | Önem | Segmentler | Asıl ihtiyaç |
|---|---|---|---|---|---|
| 1 | Ay sonu raporlarını hazırlamak saatler sürüyor | 31 (%26) | Önemli | Finans yöneticileri, orta ölçek | Manuel kopyala-yapıştır olmadan ay sonunu kapatmak |
| 2 | Dış muhasebecileri davet etmek zor | 14 (%12) | 6'sı için engelleyici | Küçük firmalar | Dış danışmanlarla güvenli iş birliği |
- Yanlılık: Yorumların %70'i kötüleyenlerden geliyor; destekleyenler nadiren yorum yazmış.
- Tema 1 için sözel talepler: "Excel'e aktarma", "zamanlanmış PDF", "API" – tek ihtiyaç, üç çözüm.
