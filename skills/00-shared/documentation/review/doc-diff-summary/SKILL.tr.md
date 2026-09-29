---
name: doc-diff-summary
description: "Bir dokümanın (sözleşme, şartname, politika, runbook, gereksinimler) iki sürümünü karşılaştırır; esaslı değişiklikleri, her paydaşa etkilerini ve doğurdukları soruları, anlam değişikliklerini biçimsel olanlardan ayırarak kategorize edilmiş bir özet hâlinde sunar. Bir dokümanın yeni sürümü geldiğinde, yeniden onay veya imza öncesinde, tedarikçi ya da müşteri revize taslak gönderdiğinde veya iki sürüm arasında neyin değiştiği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: documentation
  area: review
  title: "Doküman değişikliklerini özetleme"
  related: "change-request-analysis, impact-analysis, document-review, changelog-entry, requirements-sign-off"
  prompt: "Tedarikçiden gelen entegrasyon şartnamesinin v1.3 ve v1.4 sürümleri burada. Ne değişti ve bizim için ne anlama geliyor?"
---

# Doküman Değişikliklerini Özetleme

## Amaç
İnceleyenlerin, dokümanın tamamını yeniden okumadan iki sürüm arasında gerçekte neyin değiştiğini ve bunun neden önemli olduğunu anlamasını sağlamak; yükümlülük, kapsam, sayı veya tarihlerdeki sessiz bir değişikliğin onaydan kaçmasını önlemek.

## Ne zaman kullanılır
- Revize bir şartname, sözleşme, politika veya planın yeniden onaylanması gerektiğinde.
- Bir tedarikçi, müşteri veya başka bir ekip yeni sürüm gönderip yalnızca küçük düzeltmeler yapıldığını söylediğinde.
- Bir doküman için değişiklik kaydı veya sürüm geçmişi maddesi yazılacaksa.

## Ne zaman kullanılmaz
- Değişiklik, karar gerektiren ve üzerinde anlaşılmış gereksinimlere yönelik bir değişiklik önerisiyse `change-request-analysis` kullanılır.
- Bir değişikliğin sistemler ve süreçler üzerindeki geniş etkisi değerlendirilecekse `impact-analysis` kullanılır.
- Tek bir sürüm var ve kalite geri bildirimi gerekiyorsa `document-review` kullanılır.

## Girdiler
Zorunlu:
- Eski ve yeni olarak etiketlenmiş iki sürüm (tam metin veya açıkça işaretlenmiş bölümler).

İsteğe bağlı, kaliteyi artırır:
- Okuyucunun rolü ve ilgi alanı (ör. entegre eden taraf olarak bizim ekibimiz).
- Gerçek farkla karşılaştırmak için yazarın değişiklik notları veya ön yazısı.
- Özellikle önemli alanlar (fiyat, SLA, veri alanları, son tarihler).

Sürümlerden biri eksikse iste. Yalnızca beyan edilen değişiklik listesi varsa analizin bu beyana dayandığını ve beyan edilmemiş değişiklikleri tespit edemeyeceğini belirt.

## Süreç
1. Sürümleri bölüm bazında hizala; eklenen, çıkarılan, taşınan veya yeniden numaralanan bölümleri not et.
2. Değişiklikleri yalnızca paragraf değil madde düzeyinde tespit et: sayılar, tarihler, birimler, kiplik ifadeleri (-malıdır'dan -malıdır (önerilir)'e), koşullar, istisnalar, taraflar, tanımlar ve referanslar.
3. Her değişikliği sınıflandır: Esaslı (anlamı, yükümlülüğü, kapsamı, değeri, davranışı değiştirir), Açıklama (anlam aynı, daha net), Biçimsel (biçim, yazım hatası, yeniden numaralama).
4. Tanım değişikliklerine ve yeniden numaralanan referanslara özellikle dikkat et; değişen bir tanım onu kullanan her maddeyi sessizce değiştirir.
5. Her esaslı değişiklik için eski ve yeni ifadeyi kısaca, pratikte ne anlama geldiğini ve kimi etkilediğini yaz.
6. Her değişikliğin etkisini okuyucunun bakış açısından tek satırlık gerekçeyle derecelendir (Yüksek/Orta/Düşük).
7. Yazarın beyan ettiği değişiklik notlarıyla karşılaştır; beyan edilmemiş esaslı değişiklikleri ayrıca listele.
8. Belirsiz, aleyhte veya açıklanmamış değişiklikler için sorular veya müzakere noktaları oluştur.
9. En üste karar vericiler için 3-5 maddelik bir özet yaz.
10. Metnin söylediğini etkisine dair kendi yorumundan ayır: çıkarımla belirlediğin her etkiyi veya niyeti `[VARSAYIM]` olarak işaretle ve doküman sahibinin teyidi için listele.
11. Kullanıcının hedefi devam ediyorsa önemli değişiklikler için `impact-analysis` veya `change-request-analysis`, özeti yayımlamak için `changelog-entry` öner.

## Çıktı formatı
```markdown
# Değişiklikler: <doküman> <eski sürüm> → <yeni sürüm>
Okuyucu bakış açısı: <...> | Karşılaştırılan: <tam metin / bölümler>

## Özet
- <n> esaslı, <n> açıklama, <n> biçimsel değişiklik
- En önemlisi: <...>
- Beyan edilmemiş esaslı değişiklikler: <sayı veya yok>

## Esaslı Değişiklikler
| # | Konum (yeni) | Eski | Yeni | Pratik anlamı | Etkilenen | Etki |
|---|---|---|---|---|---|---|

## Açıklamalar
- <konum>: <kısa açıklama>

## Biçimsel
- <gruplanmış açıklama>

## Yapısal Değişiklikler
- Eklenen / çıkarılan / taşınan bölümler: <...>

## Sorular ve Gündeme Getirilecek Noktalar
1. <soru> — <değişiklik #> — <kime>
```

## Kalite kontrol listesi
- [ ] Her sayı, tarih, kiplik ve koşul değişikliği yakalanmış.
- [ ] Tanım değişiklikleri etkiledikleri maddelere kadar izlenmiş.
- [ ] Esaslı ve biçimsel değişiklikler açıkça ayrılmış.
- [ ] Beyan edilmemiş esaslı değişiklikler vurgulanmış.
- [ ] Etki, okuyucunun bakış açısından gerekçesiyle belirtilmiş.
- [ ] İki ifade de gösterilmeden hiçbir şey değişmiş olarak raporlanmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yazarın ön yazısına güvenmek. Her zaman metinlerin kendisini karşılaştır.
- "-malıdır"ın "-abilir"e ya da "5 iş günü içinde"nin "5 gün içinde"ye dönüşmesini kaçırmak. Küçük kelime, büyük etki.
- Yeniden numaralamayı onlarca değişiklik olarak raporlamak. Tek bir yapısal notta topla ve eski-yeni numaraları eşle.

## Örnek
Girdi: Tedarikçiden entegrasyon şartnamesi v1.3 ve v1.4; okuyucu: bizim entegrasyon ekibimiz.

Çıktıdan bir bölüm:
- Özet: 4 esaslı, 6 açıklama, §5-§7'de biçimsel yeniden numaralama. Beyan edilmemiş: 1.
- | 1 | §3.2 | Yeniden deneme: "tedarikçi 3 kez yeniden denemelidir" | "istemci yeniden denemelidir (önerilir)" | Yeniden deneme sorumluluğu bize geçiyor | Entegrasyon ekibi | Yüksek |
- | 2 | §6.1 (eski §5.1) | Hız sınırı 100 istek/sn | 50 istek/sn | Toplu senkronizasyon yoğun saatte sınırı aşabilir `[kendi tepe değerimizi doğrula]` | Operasyon | Yüksek |
- Soru: Yeniden deneme sorumluluğu neden taşındı ve bu SLA'ya yansıtıldı mı? — değişiklik 1 — tedarikçi müşteri temsilcisi.
