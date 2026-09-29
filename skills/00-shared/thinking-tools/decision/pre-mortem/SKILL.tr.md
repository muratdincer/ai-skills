---
description: Bir plan, proje, lansman veya karar için başarısızlığın zaten gerçekleştiğini varsayarak geriye doğru çalışır; en olası nedenleri, erken uyarı sinyallerini ve önlemleri ortaya çıkarır. Bir plan, lansman, geçiş veya büyük karar kesinleşmeden önce, ekip aşırı iyimser göründüğünde ya da "ne ters gidebilir?" veya "pre-mortem yapalım" dendiğinde kullanılır.
related: risk-register, assumption-mapping, bias-check, raid-log, technical-risk-review
prompt: Faturalama veritabanını mart ayında tek bir hafta sonunda yeni bir bulut bölgesine taşıma planımız için pre-mortem yap.
---

# Pre-Mortem

## Amaç
Ekibin bildiği ama dile getirmediği riskleri, başarısızlığı bir ihtimal değil öncül olarak ele alarak yüzeye çıkarmak. Sonuç; sahipleri, tetik sinyalleri ve önlemleriyle sıralanmış başarısızlık senaryolarıdır ve plan hâlâ ucuza değiştirilebilirken üretilir.

## Ne zaman kullanılır
- Bir plan, lansman, geçiş, sözleşme veya işe alım kararı kesinleşmek üzereyken.
- Ekipte sorgulanmamış bir iyimserlik veya uzlaşı varken.
- Bir risk kaydı var ama genel ifadelerden ("kapsam kayması", "kaynak eksikliği") oluşuyorsa.

## Ne zaman kullanılmaz
- Bir şey zaten başarısız olduysa ve nedenleri aranıyorsa `postmortem` veya `five-whys` kullanılır.
- Tek seferlik bir çalışma yerine sürekli güncellenen bir risk kaydı gerekiyorsa `risk-register` veya `raid-log` kullanılır.
- Tek bir analizin akıl yürütmesi yanlılık açısından sınanacaksa `bias-check` kullanılır.

## Girdiler
Zorunlu:
- Plan veya karar: hedef, kapsam, zaman çizelgesi ve temel adımlar (kısa bir tarif yeterli).

İsteğe bağlı, kaliteyi artırır:
- Başarı kriterleri ve başarının değerlendirileceği tarih.
- Ekip, bağımlılıklar, kısıtlar, benzer önceki çalışmalar ve sonuçları.
- Mevcut risk listesi; böylece pre-mortem tekrar etmek yerine ekleme yapar.

Plan tarifi yoksa iste. Başarı kriteri yoksa bir tane öner ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Planı iki satırda yeniden ifade et ve "başarısızlık tarihini" belirle: sonucun değerlendirileceği somut bir an (örneğin "canlıya geçişten 8 hafta sonra"). O anda başarısızlığın ne anlama geldiğini gözlemlenebilir biçimde tanımla.
2. Öncülü yaz: "Tarih <başarısızlık tarihi>. Plan kötü şekilde başarısız oldu." Başarısızlığı kesin kabul et; olup olmayacağını tartışma.
3. Listenin tek taraflı olmaması için başarısızlık senaryolarını farklı merceklerden üret: insan ve yetkinlik, bağımlılıklar ve tedarikçiler, teknoloji ve veri, süreç ve kararlar, müşteri ve pazar, mevzuat ve güvenlik, zamanlama ve sıralama. Her biri neden ve sonuç içeren tek cümlelik 10-20 senaryo hedefle.
4. Bir grupla çalışılıyorsa herkesin senaryolarını önce sessizce yazmasını, sonra sırayla birer birer paylaşmasını iste; bu, en kıdemli sesin listeye çıpa atmasını önler.
5. Olguyu çıkarımdan ayır: her senaryoyu kullanıcının söylediği veya gözlemlediği bir şeye dayanan ya da `[VARSAYIM]` olarak işaretle. Olay, isim veya sayı uydurma.
6. Tekrarları birleştir ve senaryoları olasılık ve etkiye göre (her biri Yüksek/Orta/Düşük) tek satırlık gerekçeyle sırala. "Sessiz katilleri", yani şu an sahibi olmayan yüksek etkili maddeleri işaretle.
7. İlk 5-7 senaryo için şunları yaz: başladığını gösterecek erken uyarı sinyali (tetik), önleyici aksiyon, yine de gerçekleşirse B planı ve sahibi (yoksa `[TBD]`).
8. Sıralamanın gerektirdiği plan değişikliklerini belirle: kapsam kesme, ek kontrol noktası, sıra değişikliği, go/no-go kapısı veya durma kararı. Değişiklik gerekmiyorsa bunu ve nedenini açıkça yaz.
9. Açık soruları ve planın dayandığı, kimsenin doğrulamadığı varsayımları listele.
10. Çıktı şablonunu doldur ve yaklaşık bir sayfada tut.
11. Hedef devam ediyorsa sonraki beceriyi öner: riskleri izlemek için `risk-register` veya `raid-log`, en riskli varsayımları sınamak için `assumption-mapping`, kararın kendisi aşırı özgüvenli görünüyorsa `bias-check`.

## Çıktı formatı
```markdown
# Pre-Mortem: <plan adı>
Başarısızlık tarihi: <tarih/an> · Başarısızlık demek: <gözlemlenebilir tanım>

## Başarısızlık Senaryoları (sıralı)
| # | Senaryo (neden → sonuç) | Mercek | Olasılık | Etki | Dayanak |
|---|---|---|---|---|---|
| 1 | ... | Bağımlılıklar | Y | Y | Belirtildi / [VARSAYIM] |

## Öncelikli Riskler: Sinyaller ve Yanıtlar
| # | Erken uyarı sinyali | Önleyici aksiyon | B planı | Sahibi |
|---|---|---|---|---|

## Önerilen Plan Değişiklikleri
- ...

## Doğrulanmamış Varsayımlar ve Açık Sorular
1. <soru> — <neden önemli> — <kim cevaplayabilir>
```

## Kalite kontrol listesi
- [ ] Başarısızlık, somut bir zamanda gözlemlenebilir biçimde tanımlanmış.
- [ ] Senaryolar yalnızca teknolojiyi değil, en az dört farklı merceği kapsıyor.
- [ ] Her öncelikli riskin "yakından izle"den öte, ölçülebilir bir erken uyarı sinyali var.
- [ ] Olgular ve çıkarımlar ayrılmış; hiçbir şey uydurulmamış.
- [ ] En az bir somut plan değişikliği önerilmiş ya da önerilmemesi gerekçelendirilmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Ne ters gidebilir?" diye sormak, "başarısız oldu, neden?" diye sormamak. Varsayımsal çerçeve savunmacı ve genel cevaplar getirir; başarısızlık öncülünü koru.
- Plan değişikliği olmadan bir listeyle bitirmek. Hiçbir şeyi değiştirmeyen pre-mortem yalnızca bir ritüeldir.
- Belirsiz riskler ("iletişim sorunları"). Her birini sonucu olan belirli bir neden olarak yeniden yaz.

## Örnek
Girdi: "Faturalama veritabanını mart ayında tek bir hafta sonunda yeni bir bölgeye taşıyacağız."

Zayıf senaryo: "Geçişte teknik sorunlar çıkabilir."
Güçlü senaryo: "Replikasyon gecikmesi ay sonu yükü altında ölçülmedi; geçiş 30 saat sürdü ve faturalar geç gönderildi." Dayanak: `[VARSAYIM]` (yük testinden söz edilmemiş).
- Erken uyarı sinyali: prova çalıştırmasında replikasyon gecikmesinin kabul edilen eşiği aşması.
- Önleyici aksiyon: iki hafta önce üretim boyutunda veriyle tam prova; cuma öğlen go/no-go kapısı.
- B planı: eski bölgeye 2 saat içinde dokümante edilmiş rollback `[TBD: DBA ile teyit et]`.
