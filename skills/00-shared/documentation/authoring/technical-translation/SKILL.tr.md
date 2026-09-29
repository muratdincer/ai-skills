---
description: "Teknik içeriği (şartname, dokümantasyon, arayüz metni, hata mesajı, sürüm notu, runbook) İngilizce ile Türkçe arasında terminolojiyi, kodu, tanımlayıcıları, biçimi ve anlamı koruyarak çevirir; kaynaktaki belirsiz metni işaretler. Teknik bir doküman, mesaj veya arayüz diğer dilde teslim edilecekse ya da mevcut bir çevirinin terminolojisi hizalanacaksa kullanılır."
related: "glossary-builder, microcopy, error-message-writing, document-review, style-guide-check"
prompt: "Geliştirici rehberimizin API hata yönetimi bölümünü İngilizceden Türkçeye çevir; kodu ve HTTP terimlerini olduğu gibi bırak."
---

# Teknik Çeviri

## Amaç
Anadili hedef dil olan bir mühendisin veya kullanıcının kendi dilinde yazılmış gibi okuyacağı, terminolojisi tutarlı ve tüm teknik öğeleri (kod, tanımlayıcı, birim, yer tutucu) bozulmamış bir çeviri teslim etmek.

## Ne zaman kullanılır
- Şartname, rehber, runbook veya sürüm notları İngilizce ve Türkçe yayınlanacaksa.
- Arayüz metinleri, hata mesajları veya bildirimler yerelleştirilecekse.
- Bir müşteri veya düzenleyici kurum dokümanı diğer dilde istiyorsa.
- Mevcut bir çeviri tutarsızsa ve terminolojinin hizalanması gerekiyorsa.

## Ne zaman kullanılmaz
- Büyük veya uzun ömürlü bir içerik için üzerinde anlaşılmış terminoloji yoksa önce `glossary-builder`, sonra çeviri yapılır.
- Kaynak metnin kendisi belirsiz veya kötü yazılmışsa önce kaynağa `document-simplify` veya `document-review` uygulanır.
- Arayüz metni hedef kitle için çevrilmek yerine yeniden yazılmalıysa `microcopy` kullanılır.

## Girdiler
Zorunlu:
- Kaynak metin ve hedef dil (EN'den TR'ye veya TR'den EN'ye).

İsteğe bağlı, kaliteyi artırır:
- Sözlük veya terim bankası, stil kılavuzu, hitap düzeyi (Türkçede "siz" veya "sen").
- Hedef kitle (geliştiriciler, son kullanıcılar, denetçiler) ve yayın ortamı (arayüz, PDF, wiki).
- Arayüz metinleri için karakter sınırları.

Kaynak veya çeviri yönü eksikse iste. Birden fazla geçerli karşılığı olan alan terimlerini tahmin etme; teyit için listele.

## Süreç
1. Kaynağı tara ve çevrilmeyecek öğeleri dondur: kod blokları, satır içi kod, tanımlayıcılar, API yolları, yapılandırma anahtarları, yer tutucular (`{0}`, `%s`, `{{name}}`), URL'ler, ürün adları, birimler ve sürüm numaraları.
2. Terim listesi oluştur veya mevcut listeyi uygula: her terim için İngilizce hâlinin korunacağına (Türk mühendislerin yaygın kullandığı deployment, pipeline, cache gibi), çevrileceğine ya da ilk kullanımda parantez içinde İngilizcesiyle Türkçe verileceğine karar ver.
3. Belirsiz kaynak cümleleri tespit et ve tahmin etmek yerine işaretle; en olası okumayı `[VARSAYIM]` ile öner.
4. Cümle düzeyinde anlamı çevir, kelime sırasını hedef dilin normlarına göre yeniden kur (Türkçe yüklemi sona alır; İngilizce net özneli etken çatıyı tercih eder).
5. Kiplik gücünü koru: must/shall = "-malıdır/zorunludur", should = bağlama göre "-malıdır (önerilir)", may = "-abilir". Gereksinimin bağlayıcılığı değişmemeli.
6. Türkçe dil bilgisi ayrıntılarını uygula: kısaltma ve kod terimlerinden sonra kesme işaretiyle ek (`API'ye`, `JSON'da`), okunuşa göre ünlü uyumu, ç, ğ, ı, İ, ö, ş, ü karakterlerinin ve noktalı/noktasız i büyük-küçük harf dönüşümünün doğru kullanımı.
7. Metin son kullanıcıya yönelikse biçimleri yerelleştir (tarih, ondalık ayırıcı, para birimi); kod, log veya veri örneklerinin içinde asla yerelleştirme.
8. Kaynağın yapısını koru: başlıklar, listeler, tablolar, bağlantılar, vurgular ve numaralandırma.
9. Arayüz metinlerini uzunluk sınırlarına ve yer tutucu sırasına göre kontrol et; dil bilgisinin sıralamayı değiştirmeye zorladığı yerleri not et.
10. Çeviriyi ve terim kararlarını, belirsizlikleri ve teyit edilecek maddeleri listeleyen çevirmen notunu teslim et.

## Çıktı formatı
```markdown
## Çeviri (<kaynak> → <hedef>)
<orijinal biçimi korunmuş çevrilmiş içerik>

## Çevirmen Notları
| Kaynak terim | Seçilen karşılık | Gerekçe |
|---|---|---|

Belirsizlikler: <cümle / seçilen yorum / [VARSAYIM]>
Teyit edilecekler: <alan sorumlusu gerektiren terimler veya cümleler>
```

## Kalite kontrol listesi
- [ ] Tüm kod, tanımlayıcı, yer tutucu, URL ve sayılar değişmemiş.
- [ ] Her terim metin boyunca aynı biçimde karşılanmış.
- [ ] Gereksinim bağlayıcılığı (must/should/may) korunmuş.
- [ ] Türkçe ekler, kesme işaretleri ve özel karakterler doğru.
- [ ] Yapı ve biçim kaynakla eşleşiyor.
- [ ] Belirsizlikler sessizce çözülmemiş, işaretlenmiş.

## Sık yapılan hatalar
- Kullanıcıların arama yaptığı tanımlayıcıları veya log mesajlarını çevirmek. Bunları orijinal bırak, gerekirse düz metinde açıkla.
- Türk ekiplerin kullanmadığı yerleşik İngilizce terimleri aşırı çevirmek (pipeline için "konuşlandırma boru hattı"). Ekibin kelime dağarcığını izle.
- İngilizce cümle sırasını koruyan kelimesi kelimesine çeviri yapıp yapay bir Türkçe üretmek. Doğal akış için cümleyi yeniden kur.

## Örnek
Girdi (EN): "If the token has expired, the API returns `401 Unauthorized`. Clients should refresh the token and retry once."

Çıktıdan bir bölüm (TR): "Token'ın süresi dolmuşsa API `401 Unauthorized` döner. İstemciler token'ı yenilemeli ve isteği bir kez tekrar denemelidir."
Not: "should" "-meli" ile karşılandı (öneri gücü korundu); "token" ekip kullanımına göre İngilizce bırakıldı.
