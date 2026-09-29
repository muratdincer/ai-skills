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
1. Talebi oku; bilinenleri (olgular), ima edilenleri (`[VARSAYIM]` etiketli yorum) ve eksik olanları ayrı ayrı listele. Gönderenin rolünü, karar gücünü ve çıkarını not et; sponsorun talebi ile son kullanıcının talebi farklı sorular gerektirir.
2. Birebir isteneni asıl ihtiyaçtan (yapılmak istenen iş) ayır. İkisi farklı olabilirse ilk soru ihtiyacı teyit eder. Olmazsa olmazların, başarı kriterlerinin ve kesin istenmeyenlerin (açıkça istemedikleri) bilinip bilinmediğine bak; bilinmeyen her biri bir soruya dönüşür.
3. Aşağıdaki soru bankasındaki her kategoriyi gözden geçir. Yalnızca cevabı talepte olmayan ve kapsamı, tasarımı, tahmini veya riski değiştirecek soruları tut.
4. Kalan her soruyu bu talebe özel hale getir (ekranın, varlığın, kullanıcı grubunun, tarihin adını ver). Genel ifadeleri çıkar.
5. Mümkün olduğunda kapalı veya seçenekli sorular tercih et ("A mı B mi?", "X, Y veya başka bir şey mi?"); cevaplar hızlanır.
6. Her soruya öncelik ver: P1 analizi/tahmini engeller, P2 tasarımı etkiler, P3 detaylı analize kadar bekleyebilir.
7. Neden önemli olduğunu (kısa bir ifade) ve muhtemel cevap sahibini ekle.
8. İlk turu yaklaşık 10-15 soruyla sınırla; kalanları "sonra" listesine taşı.
9. Kanala göre sırala: toplantıda hedeften ayrıntıya doğal akış; e-postada numaralı, P1 önce, yazılı cevaplanabilir sorular.
10. Cevaplar geldiğinde kayıt için `request-intake-document`, hazırlığı teyit için `request-completeness-check`, açık kalanlar için `open-questions-tracker` öner.

Soru bankası (uyarla, körü körüne yapıştırma):
- **İş ve hedef:** Bugün hangi problem, kimin başına, ne sıklıkta geliyor? Önerilen çözümün arkasındaki asıl ihtiyaç ne? Tarihi ne belirliyor, kayarsa ne olur? İşe yaradığını nasıl anlarız (metrik, başlangıç değeri, hedef)? Hiçbir şey yapmazsak ne olur? Kim karar veriyor, bütçe kimden?
- **Kapsam ve beklentiler:** Sonuç ilk gün neyi mutlaka içermeli? Neyin kesinlikle değişmemesi veya yapılmaması gerekiyor? Hangi ilgili girişimler veya önceki talepler örtüşüyor? Kısmi veya aşamalı teslim kabul edilir mi?
- **Kullanıcılar ve roller:** Hangi kullanıcı grupları, kaç kişi, iç mi dış mı? Kim bunu görmemeli veya yapmamalı? Kanallar ve cihazlar? Erişilebilirlik ihtiyacı? Hangi yetki veya görevler ayrılığı kuralları geçerli?
- **Süreç ve kurallar:** Hangi süreç adımı değişiyor? İş kuralları, onaylar, istisnalar? Olumsuz senaryoda (ret, zaman aşımı, hatalı girdi, mükerrer kayıt) ne olur? Hangi doğrulamalar geçerli, hatayı kim düzeltir? Bugün hangi manuel geçici çözüm kullanılıyor?
- **Veri:** Hangi varlıklar ve alanlar? Doğru kaynak (master) hangisi? Hacim ve büyüme? Veri kalitesi sorunları? Kişisel veya hassas veri? Saklama süresi?
- **Entegrasyon:** Hangi sistemler veri gönderiyor veya alıyor? Anlık mı toplu mu? Arayüzün sahibi kim? Hata ve yeniden deneme beklentisi?
- **Fonksiyonel olmayan:** Yanıt süresi, tepe yük ve ne zaman oluştuğu, erişilebilirlik penceresi, kurtarma beklentisi, güvenlik seviyesi, denetim izi (kim, ne, ne zaman), yerelleştirme, tarayıcı/cihaz desteği?
- **Yasal ve uyum:** KVKK/GDPR, sektör mevzuatı, sözleşmesel yükümlülükler, açık rıza, denetim gereksinimleri?
- **Operasyon ve destek:** Canlıya geçişten sonra kim destek verecek? İzleme, alarm, manuel yedek süreç, eğitim, runbook?
- **Raporlama:** Hangi KPI'lar veya raporlar bu değişikliği yansıtmalı? Kim, hangi sıklıkta kullanıyor? Önceki ve sonraki dönem karşılaştırılabilir kalmalı mı?
- **Geçiş (migration):** Taşınacak veya temizlenecek mevcut veri var mı? Geçiş (cut-over) kısıtları ve dondurma dönemleri, paralel çalışma, geriye dönük uyumluluk, geri alma beklentisi, neyin kapatılacağı?

## Çıktı formatı
```markdown
# Netleştirme Soruları: <talep başlığı>
Hedef kitle: <talep sahibi / sponsor / ...> · Kanal: <toplantı / e-posta>

## Anladığımız
- İstenen (birebir): <kendi ifadeleriyle>
- Asıl ihtiyaç [VARSAYIM]: <teyit veya düzeltme için>
- Bilinen olmazsa olmazlar / başarı kriterleri / kesin istenmeyenler: <veya [BİLİNMİYOR]>

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
- [ ] Birebir istenen ile asıl ihtiyaç ayrıldı; sorular olmazsa olmazları, başarı kriterlerini ve kesin istenmeyenleri kapsıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

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
