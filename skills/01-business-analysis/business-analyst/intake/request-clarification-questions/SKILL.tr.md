---
description: "Yeni bir talep için talep sahibine sorulacak netleştirme sorularını konu başlıklarına (iş, kullanıcılar, veri, entegrasyon, NFR, yasal, operasyon, raporlama, geçiş) göre gruplar ve cevabın analizi ne kadar engellediğine göre önceliklendirir. Talep belirsizse, netleştirme toplantısı veya e-postası öncesinde ya da 'iş birimine bununla ilgili ne sormalıyım?' sorusu geldiğinde kullanılır."
related: "request-intake-document, request-completeness-check, interview-question-set, open-questions-tracker"
prompt: "Bu talep için talep sahibine ne sormalıyım: 'Müşteriler adreslerini mobil uygulamadan kendileri güncelleyebilsin.'"
---

# Talep Netleştirme Soruları

## Amaç
Analiz ve tahmini engelleyen belirsizlikleri gideren kısa ve önceliklendirilmiş bir soru seti üretmek. Böylece beş tur yerine tek bir netleştirme turu yeterli olur.

## Ne zaman kullanılır
- Yeni talep muğlak, doğrudan çözümle başlıyor ya da bariz bilgiler eksik olduğunda.
- Talep sahibiyle yapılacak netleştirme toplantısı, e-postası veya yazışması öncesinde.
- Talep alma dokümanında sahibi belirlenmesi gereken çok sayıda `[BİLİNMİYOR]` alan olduğunda.

## Ne zaman kullanılmaz
- Soru değil, önem derecesi belirtilmiş bir eksik listesi gerekiyorsa `request-completeness-check` kullanılır.
- Bir paydaş grubuyla kapsamlı gereksinim görüşmesi hazırlanıyorsa `interview-question-set` kullanılır.

## Girdiler
Zorunlu:
- Talep metni veya talep alma dokümanı.

İsteğe bağlı, kaliteyi artırır:
- Soruların kime gideceği (talep sahibi, sponsor, BT, uyum) ve kanal (toplantı, e-posta).
- Bilinen bağlam: etkilenen sistemler, iş alanı, mevzuat ortamı, son tarih.
- Önceki turlarda alınmış cevaplar.

Talep metni yoksa iste. Talebin zaten cevapladığı hiçbir şeyi sorma.

## Süreç
1. Talebi oku; bilinenleri (olgular), ima edilenleri (yorum) ve eksik olanları ayrı ayrı listele.
2. Aşağıdaki soru bankasındaki her kategoriyi gözden geçir. Yalnızca cevabı talepte olmayan ve kapsamı, tasarımı, tahmini veya riski değiştirecek soruları tut.
3. Kalan her soruyu bu talebe özel hale getir (ekranın, varlığın, kullanıcı grubunun, tarihin adını ver). Genel ifadeleri çıkar.
4. Mümkün olduğunda kapalı veya seçenekli sorular tercih et ("A mı B mi?", "X, Y veya başka bir şey mi?"); cevaplar hızlanır.
5. Her soruya öncelik ver: P1 analizi/tahmini engeller, P2 tasarımı etkiler, P3 detaylı analize kadar bekleyebilir.
6. Neden önemli olduğunu (kısa bir ifade) ve muhtemel cevap sahibini ekle.
7. İlk turu yaklaşık 10-15 soruyla sınırla; kalanları "sonra" listesine taşı.
8. Kanala göre sırala: toplantıda hedeften ayrıntıya doğal akış; e-postada numaralı, P1 önce, yazılı cevaplanabilir sorular.

Soru bankası (uyarla, körü körüne yapıştırma):
- **İş ve hedef:** Bugün hangi problem, ne sıklıkta yaşanıyor? Tarihi ne belirliyor? İşe yaradığını nasıl anlarız (metrik, başlangıç değeri, hedef)? Hiçbir şey yapmazsak ne olur? Kim karar veriyor, bütçe kimden?
- **Kullanıcılar ve roller:** Hangi kullanıcı grupları, kaç kişi, iç mi dış mı? Kim bunu görmemeli veya yapmamalı? Kanallar ve cihazlar? Erişilebilirlik ihtiyacı?
- **Süreç ve kurallar:** Hangi süreç adımı değişiyor? İş kuralları, onaylar, istisnalar? Olumsuz senaryoda ne olur?
- **Veri:** Hangi varlıklar ve alanlar? Doğru kaynak (master) hangisi? Hacim ve büyüme? Veri kalitesi sorunları? Kişisel veya hassas veri? Saklama süresi?
- **Entegrasyon:** Hangi sistemler veri gönderiyor veya alıyor? Anlık mı toplu mu? Arayüzün sahibi kim? Hata ve yeniden deneme beklentisi?
- **Fonksiyonel olmayan:** Yanıt süresi, tepe yük, erişilebilirlik penceresi, güvenlik seviyesi, denetim izi, yerelleştirme?
- **Yasal ve uyum:** KVKK/GDPR, sektör mevzuatı, sözleşmesel yükümlülükler, açık rıza, denetim gereksinimleri?
- **Operasyon ve destek:** Canlıya geçişten sonra kim destek verecek? İzleme, alarm, manuel yedek süreç, eğitim, runbook?
- **Raporlama:** Hangi KPI'lar veya raporlar bu değişikliği yansıtmalı? Kim, hangi sıklıkta kullanıyor?
- **Geçiş (migration):** Taşınacak veya temizlenecek mevcut veri var mı? Geçiş kısıtları, paralel çalışma, geriye dönük uyumluluk?

## Çıktı formatı
```markdown
# Netleştirme Soruları: <talep başlığı>
Hedef kitle: <talep sahibi / sponsor / ...> · Kanal: <toplantı / e-posta>

## Anladığımız
<teyit veya düzeltme için 2-3 cümlelik yeniden ifade>

## Öncelik 1 – analizi engelliyor
| # | Konu | Soru | Neden önemli | Sahibi |
|---|---|---|---|---|
| 1 | İş | ... | ... | ... |

## Öncelik 2 – tasarımı etkiliyor
| # | Konu | Soru | Neden önemli | Sahibi |

## Sonra (detaylı analiz)
- ...

## Cevap gelmezse kullanacağımız varsayımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Hiçbir soru talepte zaten cevaplanmış değil.
- [ ] Her soru bu talebe özel, genel değil.
- [ ] Her soru tek bir şey soruyor.
- [ ] Sorular tarafsız ve bir çözüm dayatmıyor.
- [ ] P1 soruları 10 veya daha az ve her birinin sahibi var.
- [ ] Talep "sadece arayüz" gibi görünse bile veri, yasal ve NFR başlıkları değerlendirildi.

## Sık yapılan hatalar
- Tüm soru bankasını talep sahibine göndermek. Sıkı filtrele; cevapsız kalan uzun listeler güveni zedeler.
- "Gereksinimleriniz neler?" diye sormak. Bunun yerine problemi, durumu ve somut örnekleri sor.
- Talep sahibi dışındakileri unutmak: engelleyici cevaplar çoğu zaman uyum, operasyon ve veri sahiplerindedir.

## Örnek
Girdi: "Müşteriler adreslerini mobil uygulamadan kendileri güncelleyebilsin."

Çıktıdan bir bölüm:
| # | Konu | Soru | Neden önemli | Sahibi |
|---|---|---|---|---|
| 1 | İş | Bu bugün hangi problemi çözüyor: çağrı merkezi yükü mü, iade dönen posta mı, veri kalitesi mi? Başlangıç rakamı var mı? | Başarı metriğini belirler | Talep sahibi |
| 2 | Yasal | Adres değişikliği kimliğin yeniden doğrulanmasını veya bir yasal bildirimi gerektiriyor mu? | Ek güvenlik adımı getirebilir | Uyum |
| 3 | Entegrasyon | Adres hangi sistemlerde tutuluyor (CRM, faturalama, kargo) ve master hangisi? | Entegrasyon kapsamını belirler | BT / veri sahibi |
