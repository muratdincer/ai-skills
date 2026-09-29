---
description: "Geniş veya dağınık bir kitle için yanlılıksız bir gereksinim anketi tasarlar: bilgi hedefleri, hedef kitle, yönlendirici veya çift konulu olmayan soru tipleri ve ifadeleri, dallanma mantığı, pilot planı, aydınlatma metni ve analiz planı. Çok sayıda kullanıcıya veya lokasyona aynı sorular sorulacaksa ya da 'gereksinim toplamak için bir anket hazırla' dendiğinde kullanılır."
related: "interview-question-set, screener-survey, feedback-synthesis, research-plan, data-classification"
prompt: "Mevcut kredi başvuru ekranında en çok zaman alan adımları bulmak için 400 şube çalışanına yönelik bir anket tasarla."
---

# Anket Tasarlama

## Amaç
Çok sayıda kişiden düşük maliyetle karşılaştırılabilir gereksinim kanıtı toplamak; soruların analizin gerçekten ihtiyaç duyduğu şeyi ölçmesini ve cevapları yönlendirmemesini sağlamak.

## Ne zaman kullanılır
- Çok sayıda kullanıcı, şube veya lokasyon etkileniyor ve görüşmelerle hepsine ulaşılamıyorsa.
- Bir sorunun, uygulamanın veya ihtiyacın ne kadar yaygın olduğunu sayısallaştırmak gerekiyorsa.
- Görüşme bulgularını geniş ölçekte doğrulamak isteniyorsa.

## Ne zaman kullanılmaz
- Az sayıda kişiden derinlik, hikâye ve gerekçe gerekiyorsa `interview-question-set` kullanılır.
- Kullanıcı araştırması için katılımcı seçiliyorsa `screener-survey` kullanılır.

## Girdiler
Zorunlu:
- Anketin desteklediği karar veya analiz sorusu.
- Hedef kitle.

İsteğe bağlı, kaliteyi artırır:
- Test edilecek görüşme bulguları veya hipotezler, anket aracının kısıtları, diller, son tarih.

Anketin desteklediği karar belirtilmemişse sor; aksi halde sorular "bilsek iyi olur" alanına kayar.

## Süreç
1. 2-5 bilgi hedefi yaz ve her biri için cevabın nasıl kullanılacağını belirt (karar, eşik, karşılaştırma).
2. Kitleyi ve karşılaştırılacak segmentleri (rol, lokasyon, deneyim) tanımla; yalnızca bu karşılaştırmalara hizmet eden demografik soruları ekle.
3. Her hedef için soruları taslak olarak yaz. Görüş ve varsayımsal sorular yerine davranış ve sıklık sorularını tercih et ("Geçen hafta kaç kez...").
4. Soru tiplerini bilinçli seç: "Diğer (belirtiniz)" ve "Uygulanamaz" seçenekli tekli/çoklu seçim, noktaları etiketli derecelendirme ölçekleri, sıralama (en fazla 5-7 madde), az sayıda açık metin alanı.
5. Yanlılığı temizle: yönlendirici veya yüklü ifade yok, her soruda tek konu, dengeli ölçekler, tarafsız sıra, jargon yok; mantıklıysa seçenek sırasını rastgele yap.
6. Huni (piramit) düzeninde sırala: önce kolay ve genel davranış soruları, sonra özel ve hassas sorular, demografik sorular en sonda; katılımcıların yalnızca ilgili soruları görmesi için dallanma ekle; tamamlama süresini yaklaşık 5-10 dakikada tut.
7. Giriş metnini yaz: amaç, gereken süre, anonim olup olmadığı, verinin kullanımı ve saklanması (KVKK/GDPR aydınlatma metni); ihtiyaç duyulmayan hiçbir kişisel veriyi toplama.
8. Göndermeden önce kitleden 3-5 kişiyle pilot yap: anlaşılırlığı, süreyi ve dallanmayı kontrol et, sonra düzelt. Pilotu yapılmamış anketi yayına alma.
9. Analiz planını tanımla: soru başına metrikler, segment kırılımları, güvenilir sonuç için gereken asgari cevap sayısı `[üzerinde anlaşılana kadar VARSAYIM]`. Görüşmelerden taşınan hipotezler bulgu gibi değil, hipotez olarak etiketlenir.
10. Hedef devam ediyorsa cevapları analiz etmek için `feedback-synthesis`, şaşırtıcı sonuçları derinlemesine incelemek için `interview-question-set` öner.

## Çıktı formatı
```markdown
# Anket: <konu>
Kitle: <hedef kitle> · Hedef süre: <dk> · Anonim: <evet/hayır>

## Hedefler
| # | Bilgi hedefi | Ne için kullanılacak |

## Giriş metni
...

## Sorular
| # | Hedef | Soru | Tip | Seçenekler / ölçek | Dallanma |
|---|---|---|---|---|---|

## Pilot planı
- ...

## Analiz planı
- ...
```

## Kalite kontrol listesi
- [ ] Her soru bir hedefe bağlı; hiçbiri "bilsek iyi olur" değil.
- [ ] Yönlendirici, yüklü veya çift konulu soru yok.
- [ ] Ölçekler dengeli ve etiketli; gereken yerde "Uygulanamaz" seçeneği var.
- [ ] Tahmini tamamlama süresi 10 dakika veya daha az.
- [ ] Aydınlatma metni mevcut ve kişisel veri en aza indirilmiş.
- [ ] Pilot ve analiz planı tanımlı.
- [ ] Sorular genelden özele huni düzeninde, demografik sorular sonda.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kullanıcılardan çözümü tasarlamalarını istemek ("Hangi özellikleri istersiniz?"). Bunun yerine görevleri, sıklığı ve sorunları sor.
- Düşük katılım oranını temsil edici saymak. Katılım oranını segment bazında raporla.
- Yayından sonra soruları değiştirmek. Önce pilot yap; değişiklikler karşılaştırılabilirliği bozar.

## Örnek
Girdi: "400 şube çalışanı; kredi başvuru ekranında hangi adımlar en çok zaman alıyor."

Çıktıdan bir bölüm:
| # | Hedef | Soru | Tip | Seçenekler / ölçek |
|---|---|---|---|---|
| 3 | Süre etkenleri | Son 5 kredi başvurunuzda en uzun süren adım hangisiydi? | Tekli seçim | Müşteri arama / Gelir girişi / Doküman yükleme / Kredi kontrolü / Diğer (belirtiniz) |
| 4 | Sıklık | Başka bir sistemde zaten bulunan veriyi ne sıklıkla yeniden giriyorsunuz? | Ölçek | Hiçbir zaman / Nadiren / Bazen / Sık sık / Her başvuruda |
