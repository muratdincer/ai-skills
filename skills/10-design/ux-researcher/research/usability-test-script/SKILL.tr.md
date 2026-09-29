---
description: Moderatörlü veya moderatörsüz bir kullanılabilirlik testi senaryosu yazar; giriş ve onay, ısınma, gerçekçi görev senaryoları, yönlendirmesiz sorular, gözlemlenebilir başarı kriterleri, görev sonrası ve test sonrası ölçümler ile kapanışı içerir. Bir prototip veya canlı ürün kullanıcılarla test edilecekse, "test görevleri" ya da "moderatör rehberi" istendiğinde veya bir kullanılabilirlik oturumu planlanmadan önce kullanılır.
related: research-plan, screener-survey, research-synthesis, heuristic-evaluation, interview-question-set
prompt: Yeni ödeme adımı prototipimiz için kullanılabilirlik testi senaryosu yaz; ilk kez alışveriş yapanların indirim kodu uygulayıp kartla ödeme yapabildiğini görmek istiyoruz.
---

# Kullanılabilirlik Testi Senaryosu

## Amaç
Moderatöre (veya moderatörsüz test aracına), tasarımın en riskli kısımlarını gerçekçi, yönlendirmesiz görevler ve gözlemlenebilir başarı kriterleriyle test eden bir senaryo vermek. Böylece sonuçlar katılımcılar arasında karşılaştırılabilir olur ve somut tasarım değişikliklerine işaret eder.

## Ne zaman kullanılır
- Bir prototip, beta veya canlı akışın temsilî kullanıcılarla değerlendirilmesi gerektiğinde.
- Araştırma planı hazır ve oturum rehberinin yazılması gerektiğinde.
- Yeniden tasarımın aynı görevlerle mevcut sürüme karşı kıyaslanması gerektiğinde.

## Ne zaman kullanılmaz
- Hedefler, yöntem ve katılımcılar henüz netleşmediyse `research-plan` kullanılır.
- Amaç bir tasarımı değerlendirmek değil, ihtiyaç ve davranışları keşfetmekse `interview-question-set` kullanılır.
- Kullanıcıya erişim yoksa ve uzman incelemesi yeterliyse `heuristic-evaluation` kullanılır.

## Girdiler
Zorunlu:
- Test edilen şey (akış, prototip veya ürün alanı) ve cevaplanması gereken araştırma soruları ya da riskler.

İsteğe bağlı, kaliteyi artırır:
- Araştırma planı, hedef segment, prototipin doğruluk seviyesi ve çıkmaz noktaları, oturum süresi, moderatörlü veya moderatörsüz format, yeniden kullanılacak kıyas metrikleri.

Test edilen akış veya araştırma soruları yoksa bunları kısa, numaralı tek bir soru grubuyla iste. Diğer eksikler senaryoda açık soru olarak yer alır.

## Süreç
1. Araştırma sorularını yeniden yaz ve her birini en az bir göreve bağla; hiçbir soruyu cevaplamayan görevleri çıkar.
2. 45-60 dakikalık moderatörlü bir oturum için 4-7 görev seç (moderatörsüzde daha az). Görevleri basitten karmaşığa sırala ve en riskli akışları, süre kısalırsa kesilmeyecek kadar öne al.
3. Her görevi hedef ve bağlam içeren bir senaryo olarak yaz; arayüz etiketleri veya adımlar kullanma ("E-postandaki kodla daha az ödemek istiyorsun", "Kupon uygula'ya tıkla" değil).
4. Her görev için başarıyı gözlemlenebilir biçimde tanımla: ulaşılan son durum, kritik hatalar, izin verilen yardım, süre sınırı. "Başarılı / zorlukla başarılı / başarısız" kurallarını oturumlardan önce belirle.
5. Yönlendirmesiz sorular (burada ne bekliyorsun, sonra ne yapardın) ve yasak ifadeler ekle; prototip çıkmazlarını ve yardım isteklerini nasıl ele alacağını planla.
6. Ölçümleri seç: görev tamamlama, görev süresi, hatalar, görev sonrası tek soruluk kolaylık sorusu ve kıyaslama yapılacaksa test sonrası standart bir anket (ör. SUS). İfadeleri turlar arasında aynı tut.
7. Girişi yaz: amaç, "sizi değil tasarımı test ediyoruz", sesli düşünme talimatı, kayıt ve veri minimizasyonuyla onay. Gerekenden fazla kişisel veri toplama.
8. Eleme profilini ve bağlamı doğrulayan ısınma soruları, ardından kapanış ekle: genel izlenim, en zor an, karşılanmayan beklentiler.
9. Zaman planını ve gözlemci not tablosunu (görev, gözlem, alıntı, önem) hazırla.
10. Her çıkarımı `[VARSAYIM]` olarak işaretle, açık soruları (prototip sınırları, test verisi, hesaplar) listele; katılımcı bulmak için `screener-survey`, oturumlardan sonra `research-synthesis` öner.

## Çıktı formatı
```markdown
# Kullanılabilirlik Testi Senaryosu: <ürün / akış>
Format: <uzaktan moderatörlü / yüz yüze / moderatörsüz> · Süre: <dk> · Prototip: <doğruluk, link TBD>

## Araştırma Soruları
- AS1 ... → Görevler: G1, G3

## Giriş (≈5 dk)
<amaç, sizi test etmiyoruz, sesli düşünme, kayıt ve onay>

## Isınma (≈5 dk)
1. ...

## Görevler
### G1 <kısa ad> (≈<dk>)
- Senaryo: "<hedef ve bağlam, arayüz etiketi yok>"
- Başlangıç noktası / test verisi: ...
- Başarı: <son durum> · Kritik hatalar: ... · Süre sınırı: ...
- Sorular: ...
- Görev sonrası: "Bu görev genel olarak ne kadar kolay veya zordu?" (1-7)

## Test Sonrası (≈5 dk)
<anket, kapanış soruları>

## Kapanış ve Teşekkür
<teşvik, sonraki adımlar>

## Gözlemci Tablosu
| Görev | Sonuç | Gözlem | Alıntı | Önem |
|---|---|---|---|---|

## Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her görev bir araştırma sorusuna, her araştırma sorusu en az bir göreve bağlı.
- [ ] Hiçbir görevde arayüz etiketi, adım ipucu veya yönlendirici ifade yok.
- [ ] Başarı ve başarısızlık kuralları her görev için oturumlardan önce tanımlandı.
- [ ] Süreler, pay bırakılarak oturum süresine sığıyor.
- [ ] Onay, kayıt ve kişisel veri işleme ele alındı.
- [ ] Prototip sınırları ve gereken test verileri listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Görev metninde katılımcıya nereye tıklayacağını söylemek. Hedefi anlat, yolu kendisi bulsun.
- Çok erken yardım etmek. Yardım politikasını önceden belirle ve yardımla tamamlananları ayrı say.
- Turlar arasında görev ifadesini değiştirip metrikleri karşılaştırmak. Kıyaslamada ifadeleri sabitle.

## Örnek
Girdi: "İlk kez alışveriş yapanlar indirim kodu uygulayıp kartla ödeyebiliyor mu, test edelim."

Zayıf görev: "'Kupon uygula'ya tıkla ve SAVE10 yaz."
Güçlü görev: "Hoş geldin e-postasında %10 indirim kodu aldın. Mavi sırt çantasını olabilecek en düşük fiyata al ve aşağıdaki test kartıyla öde."
- Başarı: indirim uygulanmış sipariş onayı görüldü, yardım alınmadı. Kritik hata: fark etmeden tam fiyat ödemek.
- Soru: "Buna bastığında ne olmasını bekliyordun?"
