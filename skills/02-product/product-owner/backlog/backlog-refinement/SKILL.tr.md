---
description: "Bir grup backlog maddesini iyileştirme oturumuna hazırlar; bunları kabul kriterleri, açık sorular ve hazır olma kararı içeren, net, uygun boyutta, tahmine hazır ve sıralı iş maddelerine dönüştürür. Backlog düzenlenmesi gerektiğinde, maddeler iterasyon/sprint planlaması öncesinde belirsiz veya çok büyük olduğunda ya da hikayelerin hazırlanması istendiğinde kullanılır."
related: "story-splitting, definition-of-ready, acceptance-criteria, backlog-prioritization, estimation-session"
prompt: "Gelecek haftaki planlama için bu 8 backlog maddesini iyileştir; hangileri hazır, hangileri bölünmeli ve iş birimine daha neler sormalıyız söyle."
---

# Backlog İyileştirme

## Amaç
Backlog'un üst kısmını "fikir ve parçalar" halinden, ekibin sürprizsiz anlayıp boyutlandırabileceği ve çekebileceği maddelere taşımak. Sonuç, her madde için hazır olma kararı ve onu hâlâ neyin engellediğini gösteren kısa bir liste içeren iyileştirilmiş bir listedir.

## Ne zaman kullanılır
- İterasyon/sprint planlamasından ya da maddeler akış panosuna çekilmeden önce.
- Maddeler tek satırlık başlıklardan ibaret, kabul kriteri yok veya değeri belirsiz olduğunda.
- Yeni bir epic veya özellik parçalara ayrıldıktan sonra parçaların sıkılaştırılması gerektiğinde.
- Ekip eksik bilgiyi sürekli iş ortasında fark ediyorsa.

## Ne zaman kullanılmaz
- Görev yalnızca çok sayıda madde arasında sıra belirlemekse `backlog-prioritization` kullanılır.
- Tek bir madde açıkça çok büyükse ve dilimlenmesi gerekiyorsa `story-splitting` kullanılır.
- Tüm backlog'un bayat, tekrar eden veya sahipsiz maddeler için denetlenmesi gerekiyorsa `backlog-health-check` kullanılır.

## Girdiler
Zorunlu:
- İyileştirilecek backlog maddeleri (başlıklar ve varsa açıklamalar).

İsteğe bağlı, kaliteyi artırır:
- Ürün/iterasyon hedefi, yol haritası teması veya hedef sonuç.
- Ekibin Hazır Tanımı (DoR) ve Bitti Tanımı (DoD).
- Kullanılan tahmin ölçeği (puan, tişört bedeni, yok) ve son dönem verimi.
- Bilinen bağımlılıklar, alan kuralları, UX veya teknik notlar.

Madde verilmediyse iste. Eksik isteğe bağlı girdileri açık soru olarak ele al.

## Süreç
1. Kapsamı backlog'un üst kısmıyla sınırla: yaklaşık sonraki 1-2 iterasyonluk iş veya önümüzdeki birkaç haftalık akış. Gerisine dokunma.
2. Her madde için değeri tek satırda yeniden ifade et: kim fayda sağlar, onun için ne değişir, neden şimdi. Değeri ifade edilemeyen maddeleri işaretle.
3. Belirsiz başlıkları sonuç diliyle yeniden yaz. Kullanıcı hikayesi formatını yalnızca netlik katıyorsa kullan; teknik altyapı maddeleri "Y için X'i mümkün kıl" biçimini kullanabilir.
4. Her madde için 3-7 test edilebilir kabul kriteri yaz (kural bazlı veya Given/When/Then). Çıkarım yaptıklarını `[VARSAYIM]` olarak işaretle.
5. Boyutu ekibin normuna göre kontrol et: bir iterasyonda veya birkaç günlük akışta bitirilemeyecek maddeler için bölme öner ve bölme desenini adlandır (iş akışı adımı, iş kuralı, veri çeşitliliği, arayüz, spike).
6. Bağımlılıkları (diğer ekipler, tedarikçiler, veri, ortamlar, kararlar) ve çözülüp çözülmediklerini belirle.
7. Her madde için açık soruları ve cevaplayabilecek kişi ya da rolü listele.
8. Her maddeyi Hazır Tanımına göre değerlendir (yoksa varsayılan: değer net, kabul kriterleri test edilebilir, yeterince küçük, bağımlılıklar biliniyor, engelleyici soru yok).
9. İyileştirilen maddeler için tek satırlık gerekçeyle bir sıra öner; ayrıntılı puanlamayı `backlog-prioritization` becerisine bırak.
10. Çıktıyı ve yalnızca ekip tartışması gerektiren maddeleri kapsayan kısa bir iyileştirme oturumu gündemini üret.
11. Kullanıcının hedefi devam ediyorsa hâlâ büyük olan maddeler için `story-splitting`, kriteri eksik maddeler için `acceptance-criteria`, boyutlandırma için `estimation-session` öner.

## Çıktı formatı
```markdown
# Backlog İyileştirme: <ürün/ekip> – <tarih>
Hedef/tema: <hedef veya [BİLİNMİYOR]>

| # | Madde | Değer (tek satır) | Boyut sinyali | Hazır olma | Engel |
|---|---|---|---|---|---|
| 1 | <başlık> | <kim/ne/neden> | Uygun / Böl / Spike | Hazır / Neredeyse / Hazır değil | <soru veya bağımlılık> |

## Madde Ayrıntıları
### <#> <iyileştirilmiş başlık>
- Açıklama: <1-3 satır>
- Kabul kriterleri:
  1. <kriter>
- Bölme önerisi: <desen ve ortaya çıkan maddeler veya yok>
- Bağımlılıklar: <madde – sahip – durum>
- Açık sorular: <soru – kim cevaplar>

## Önerilen Sıra
1. <madde> – <gerekçe>

## İyileştirme Oturumu Gündemi
- <madde>: <ekibin karar vermesi/tahmin etmesi gereken konu> (<dakika>)
```

## Kalite kontrol listesi
- [ ] Her maddenin tek satırlık bir değer ifadesi var ya da bunun eksik olduğu işaretlendi.
- [ ] Kabul kriterleri test edilebilir ve uygulamayı değil davranışı tarif ediyor.
- [ ] Fazla büyük maddeler için sadece "böl" denmedi, bölme deseni adlandırıldı.
- [ ] Hazır olma kararları belirtilen Hazır Tanımı ile tutarlı.
- [ ] Hiçbir şey uydurulmadı: tahminler, tarihler ve sahipler girdiden geliyor ya da işaretli.
- [ ] Oturum gündemi yalnızca ortak tartışma gerektiren maddeleri içeriyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çok ileriyi iyileştirmek. Ayrıntı zamanla eskir; yalnızca yakında çekilecek maddeleri iyileştir.
- Ekip adına tahmin üretmek. Bu beceri maddeleri hazırlar; boyutlandırmayı ekip `estimation-session` ile yapar.
- Çözülmemiş bağımlılıkları "Hazır" etiketinin arkasına saklamak. Dış bir engel maddeyi Hazır değil yapar.
- Kullanıcıya görünen veya test edilebilir sonuçlar yerine görev yazmak ("tablo oluştur", "endpoint ekle").

## Örnek
Girdi: "Maddeler: 1) Rapor dışa aktarma, 2) SSO ile giriş, 3) Yavaş aramayı düzelt."

Çıktıdan bir bölüm:
| 2 | Kurumsal SSO ile oturum açma | Çalışanlar ayrı bir parola yönetmekten kurtulur | Böl | Hazır değil | Hangi kimlik sağlayıcı ve protokol? – BT güvenlik |
- Bölme önerisi (arayüz): (a) web için SSO girişi, (b) mobil için SSO, (c) harici kullanıcılar için alternatif giriş.
- Madde 3 açık soru: Bugün "yavaş" ne demek ve kabul edilebilir yanıt süresi nedir? `[BİLİNMİYOR]`
