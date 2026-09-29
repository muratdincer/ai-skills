---
description: Bir pull request'i veya diff'i doğruluk, tasarım, testler, güvenlik, performans ve okunabilirlik açısından inceler; önceliklendirilmiş, uygulanabilir bulgular ve net bir karar sunar. Birisi merge öncesinde bir PR'ın, diff'in, yamanın veya kod parçasının incelenmesini istediğinde ya da bir değişiklik için ikinci görüş aradığında kullanılır.
related: review-comment-writing, clean-code-review, secure-code-review, error-handling-review, pull-request-description
prompt: Bu pull request diff'ini incele. Sipariş servisine indirim hesaplama endpoint'i ekliyor.
---

# Pull Request İnceleme

## Amaç
Hataları ve tasarım problemlerini merge öncesinde, değişikliğin riskiyle orantılı bir maliyetle yakalamak ve yazara hemen uygulayabileceği geri bildirim vermek. Çıktı satır satır stil yorumu değil, bir karar ve önceliklendirilmiş bulgu listesidir.

## Ne zaman kullanılır
- Bir PR veya diff incelemeye hazır olduğunda.
- Yazar, insan inceleyenleri çağırmadan önce ön inceleme istediğinde.
- Riskli bir değişikliğin (veri, güvenlik, eşzamanlılık, public sözleşme) odaklı bir ikinci bakışa ihtiyacı olduğunda.

## Ne zaman kullanılmaz
- Yalnızca tek bir boyutta derin inceleme için `secure-code-review`, `concurrency-review`, `error-handling-review` veya `clean-code-review` kullanılır.
- Elindeki yorumların dilini iyileştirmek için `review-comment-writing` kullanılır.
- Bir değişikliği değil bütün kod tabanını değerlendirmek için `code-quality-report` veya `tech-debt-assessment` kullanılır.

## Girdiler
Zorunlu:
- Diff veya değişen kod; anlaşılabilmesi için yeterli çevre bağlamıyla.

İsteğe bağlı, kaliteyi artırır:
- PR açıklaması ve bağlı iş kaydı / kabul kriterleri.
- Ekip kodlama standartları, mimari kısıtlar, test sonuçları.
- Dil/framework sürümleri ve çalışma bağlamı (servis, kütüphane, UI).

Yalnızca bir parça verildiyse ve doğruluk görülmeyen koda bağlıysa görünen kısmı incele; varsayımları `[VARSAYIM]` olarak ve açık soruları ayrıca listele.

## Süreç
1. Niyeti belirle: açıklamayı oku veya diff'ten çıkar. Niyet belirsizse bunu en başta söyle; doğruluk ancak niyete göre değerlendirilebilir.
2. Riski ve boyutu değerlendir: public sözleşmeler, kalıcı veri, para, yetkilendirme, eşzamanlılık ve migration'lar inceleme derinliğini artırır. Yaklaşık 100 satırlık değişiklik iyi incelenebilir; 1000 satıra yaklaşınca bağımsız merge edilebilir PR'lara bölünmesini öner (refactor, davranış değişikliği, temizlik).
3. Önce testler: beklenen davranışı öğrenmek için implementasyondan önce testleri oku. Değişiklik geri alınırsa testler kırılır mı? Uç durumlar ve hata yolları kapsanmış mı? Testler deterministik mi?
4. Doğruluk: ana akışı ve uç durumları izle (null/boş, sınırlar, saat dilimleri, yuvarlama, idempotency, yeniden denemeler, kısmi hata). Kabul kriterlerinin gerçekten karşılandığını kontrol et.
5. Mimari ve tasarım: sorumluluğun yeri, bağımlılık (coupling), katman ihlalleri, sızan soyutlamalar, mevcut kodla tekrar, sözleşmelerin geriye dönük uyumluluğu.
6. Güvenlik: girdi doğrulama, her yeni giriş noktasında yetkilendirme, injection, kodda gizli bilgi, loglarda hassas veri (referans: OWASP ASVS).
7. İşletilebilirlik ve performans: N+1 sorgular, sınırsız döngü veya veri boyutu, eksik timeout'lar, yeni yollarda log ve metrik, kaynakların serbest bırakılması.
8. Okunabilirlik: isimler, fonksiyon boyutu, nedeni açıklayan yorumlar; yalnızca linter'ın yakalamayacağı stil konularını yaz.
9. Her bulguyu etiketle: `Critical` (merge'ü engeller), Required (varsayılan, önek yok: merge öncesi ele alınmalı), `Nit` (önemsiz, yazar görmezden gelebilir), `Optional` (değerlendirmeye değer), `FYI` (yalnızca bilgi); gerçekten varsa `question` ve `praise` ekle. Her birini dosya ve satıra bağla ve yalnızca sorunu değil somut düzeltmeyi öner. Görülmeyen koda dair her çıkarımı `[VARSAYIM]` olarak işaretle.
10. Kararı ver: Onay, Yorumlarla onay, Değişiklik iste veya Tartışma gerekli; tek satırlık gerekçesiyle. Kusursuz olmasa da genel kod sağlığını iyileştiren değişikliği onayla; neyin kontrol edildiğini söylemeden asla onay verme (körlemesine LGTM yok).
11. Kullanıcı bulguları PR yorumu olarak yazmak isterse `review-comment-writing` ile devam et; tek bir boyutta derin inceleme için `secure-code-review` veya `error-handling-review` öner.

## Çıktı formatı
```markdown
# İnceleme: <PR başlığı>
**Karar:** <Onay | Yorumlarla onay | Değişiklik iste | Tartışma gerekli> — <gerekçe>
**Risk seviyesi:** <Yüksek/Orta/Düşük> — <neden>

## Özet
<2-3 cümle: değişiklik ne yapıyor ve genel değerlendirme>

## Bulgular
| # | Önem | Konum | Bulgu | Önerilen düzeltme |
|---|---|---|---|---|
| 1 | Critical | <dosya:satır> | <sorun ve sonucu> | <somut değişiklik> |

## Testler
- Kapsanan: ...
- Eksik: ...

## Yazara Sorular
- ...

## İyi Olanlar
- ...
```

## Kalite kontrol listesi
- [ ] Her Critical bulgu yalnızca bir ilkeyi değil, somut hata senaryosunu anlatıyor.
- [ ] Bulgular bir konuma bağlı ve önerilen düzeltme içeriyor.
- [ ] Önem dereceleri orantılı; Nit'ler Critical bulgularla karışmıyor.
- [ ] Görülmeyen koda dair varsayımlar `[VARSAYIM]` olarak işaretli.
- [ ] Testlerin bir regresyonu yakalayıp yakalamayacağı değerlendirildi.
- [ ] Karar bulgularla tutarlı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İncelemeyi biçimlendirmeye harcayıp eksik bir yetki kontrolünü kaçırmak. İncelemeyi risk sırasına göre yap.
- Yalnızca diff satırlarına bakmak. Hataların çoğu değişmeyen çağıranlarda veya diff'in değiştirmeyi unuttuğu yerlerde durur.
- PR aşamasında blocker seviyesinde gerekçe olmadan yeniden tasarım istemek. Bunun yerine takip işi öner.
- Büyük bir diff'e körlemesine onay ("LGTM") vermek. Neyin incelendiğini ve neyin incelenmediğini yaz; boyut gerçek bir incelemeyi engelliyorsa bölünmesini iste.

## Örnek
Girdi: `total * (1 - pct/100)` değerini `double` ile hesaplayıp kaydeden `POST /orders/{id}/discount` ekleyen diff.

Çıktıdan bir bölüm:
- Karar: Değişiklik iste — tutar kayan noktalı sayıyla hesaplanıyor ve endpoint'te sahiplik kontrolü yok.
- 1 | Critical | OrderController:42 | Kimliği doğrulanmış herhangi bir kullanıcı herhangi bir siparişe indirim uygulayabiliyor. | İndirimden önce sipariş sahipliğini veya personel rolünü doğrula.
- 2 | Critical | DiscountService:18 | `double` aritmetiği toplamlarda yuvarlama hatasına yol açar. | Decimal tip ve açık bir yuvarlama modu kullan.
- 3 | (Required) | DiscountServiceTest | pct > 100 veya negatif pct için test yok. | Sınır testleri ve doğrulama ekle.
