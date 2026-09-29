---
name: stack-trace-analysis
description: "Bir stack trace'i veya çökme raporunu analiz ederek hatalı çerçeveyi, istisna zincirini ve kök neden adaylarını belirler; çözümler ve sonraki teşhis adımını önerir. Geliştirici herhangi bir dil veya runtime'dan bir istisna, stack trace, çökme logu, panic veya yakalanmamış hata yapıştırıp neyin yanlış gittiğini ya da nereye bakacağını sorduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: debugging
  title: "Stack trace analizi"
  related: "debugging-hypotheses, log-analysis, bug-reproduction, error-handling-review, code-explanation"
  prompt: "Bu stack trace'e ne sebep oluyor? OrderController.getOrder'dan çağrılan OrderMapper.toDto içinde NullPointerException."
---

# Stack Trace Analizi

## Amaç
Bir stack trace'i deneyimli bir mühendis gibi okumak: istisnanın yüzeye çıktığı yeri değil, kendi kodunun hata yaptığı çerçeveyi bulmak, neden zincirini açmak ve bunu somut çözüm ve kontrollerle sıralı neden adaylarına dönüştürmek.

## Ne zaman kullanılır
- Bir istisna, çökme, panic veya yakalanmamış promise reddi metin olarak elde olduğunda.
- Trace uzun, sarmalanmış veya asenkron olduğunda ve gerçek neden belirsiz kaldığında.
- Mobil veya masaüstü istemciden gelen bir çökme raporunun ilk teşhisi gerektiğinde.

## Ne zaman kullanılmaz
- Trace yoksa, yalnızca belirtiler varsa `debugging-hypotheses` veya `log-analysis` kullanılır.
- Hata tetiklenemiyorsa ve önce yeniden üretim gerekiyorsa `bug-reproduction` kullanılır.

## Girdiler
Zorunlu:
- Her "Caused by" / inner exception / zincirlenmiş bölüm ve mesaj metniyle birlikte tam stack trace.

İsteğe bağlı, kaliteyi artırır:
- Kendi kodundaki çerçevelerin kaynak kodu, dil/runtime ve framework sürümleri.
- Ne zaman oluştuğu (her zaman, yük altında, dağıtım sonrası) ve tetikleyen girdi veya istek.
- Zaman damgası ve correlation ID'leri olan çevre log satırları.

Trace kesilmişse ("... 42 more") ve eksik kısım önemliyse bunu belirt ve tam hâlini iste. Trace'teki token, kişisel veri ve bağlantı dizelerini maskele.

## Süreç
1. Runtime'ı ve formatı belirle (JVM, .NET, Python, Node.js, Go, Swift/Kotlin çökmesi, native). Çerçevelerin içten dışa mı dıştan içe mi sıralandığını not et.
2. İlk satırda durmadan trace'in tamamını oku; tüm "Caused by", inner, aggregate ve suppressed istisnalar dahil. İstisna zincirini aç: dıştan kök nedene doğru her istisna türünü ve mesajını listele. En derindeki neden genellikle en bilgilendirici olandır.
3. Çerçeveleri framework/kütüphane ve uygulama çerçeveleri olarak ayır; kök neden içindeki en üstteki uygulama çerçevesini bul — birincil şüpheli konum odur.
4. İstisna türünü kesin olarak yorumla (null erişimi, dizin taşması, timeout, deadlock tespiti, serileştirme, sınıf yükleme/sürüm uyuşmazlığı, bellek yetersizliği, iptal) ve oluşması için hangi durumun doğru olması gerektiğini belirt.
5. Asenkron veya reaktif trace'lerde mantıksal çağrı yolunu yeniden kur (continuation'lar, thread havuzu, event loop) ve bağlamın nerede kaybolduğunu not et.
6. Ortamsal imzalara bak: sürüm çakışmaları (method not found, aynı isimli sınıflar arası cast hatası), yapılandırma (eksik anahtar, hatalı URL), kaynak tükenmesi (havuz, dosya tanıtıcıları, bellek), yetkiler.
7. Sıralı neden adayları üret; her biri trace'ten kanıt, hızlı bir doğrulama (eklenecek log, incelenecek değer, yazılacak test) ve önerilen çözüm içersin.
8. Çözümü korumadan ayır: hatalı değeri veri akışı boyunca oluşturulduğu yere kadar geriye doğru izle ve geçersiz durumu kaynağında düzelt; savunmacı kontrolü yalnızca girdinin gerçekten güvenilmez olduğu yerde ekle.
9. Hatalı durumu yeniden üreten bir regresyon testi öner.
10. Adaylardan hiçbiri yalnızca trace'ten doğrulanamıyorsa `debugging-hypotheses` (kök neden doğrulanmadan düzeltme yok) veya çevresindeki olaylar için `log-analysis` öner; çözüm istisna yönetimi tasarımıyla ilgiliyse `error-handling-review` öner.

## Çıktı formatı
```markdown
# Stack Trace Analizi: <component> içinde <istisna türü>
**Runtime:** ...  **Kök neden istisnası:** <tür: mesaj>
**Birincil şüpheli çerçeve:** <sınıf/fonksiyon:satır>

## İstisna Zinciri
1. <dış> → 2. <iç> → 3. <kök neden>

## Trace'in Söyledikleri
- ...

## Neden Adayları
| # | Aday | Kanıt | Nasıl doğrulanır | Önerilen çözüm | Olasılık |
|---|---|---|---|---|---|

## Regresyon Testi
- ...

## Eksik Bilgiler
- ...
```

## Kalite kontrol listesi
- [ ] Yalnızca dış sarmalayıcı değil, kök neden istisnası belirlenmiş.
- [ ] Birincil şüpheli bir uygulama çerçevesi; framework çerçeveleri suçlanmıyor, açıklanıyor.
- [ ] Her aday trace'ten kanıt ve bir doğrulama adımı içeriyor.
- [ ] Çözümler istisnayı yakalamakla kalmıyor, geçersiz durumun kaynağına yöneliyor.
- [ ] Trace'teki gizli bilgiler ve kişisel veriler çıktıda tekrarlanmıyor.
- [ ] Görülmeyen koda dair varsayımlar `[VARSAYIM]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- En dıştaki istisnayı (ör. genel bir "request failed") teşhis edip iç içe nedeni göz ardı etmek.
- Üst çerçeveler framework'e ait diye framework'ü suçlamak. Hata neredeyse her zaman ilk uygulama çerçevesinde veya framework'e verilen veridedir.
- Null referansı, asıl hatayı gizleyen bir null kontrolüyle düzeltmek (neden null'dı?). Değeri, atanması gereken yere kadar geri izle.

## Örnek
Girdi: `NullPointerException: Cannot invoke "Customer.getName()" because "order.customer" is null at OrderMapper.toDto(OrderMapper.java:27) at OrderController.getOrder(OrderController.java:45)`.

Çıktıdan bir bölüm:
- Birincil şüpheli: `OrderMapper.toDto:27` — her siparişin yüklenmiş bir müşterisi olduğunu varsayıyor.
- Aday 1 (Yüksek): Müşteri ilişkisi lazy ve bu sorgu yolunda yüklenmiyor. Doğrulama: `getOrder`'ın kullandığı repository metodunu kontrol et. Çözüm: ilişkiyi bu sorguda yükle.
- Aday 2 (Orta): Misafir ödemesiyle oluşturulan siparişlerin tasarım gereği müşterisi yok. Doğrulama: customer_id'si null olan siparişleri sorgula. Çözüm: misafir siparişlerini açıkça modelle ve misafir DTO'su eşle; misafir siparişiyle test ekle.
