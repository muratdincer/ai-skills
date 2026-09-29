---
description: RFP/RFI/ihale gereksinimlerine uyumlu ve fayda odaklı yanıtlar yazar; her gereksinim için önce uyum düzeyini, ardından çözümün onu nasıl karşıladığını, kanıtı ve müşteriye faydayı, müşterinin formatında ve sınırlar içinde verir. Bir RFP soru listesine veya uyum tablosuna yanıt taslaklanırken ya da iyileştirilirken, yanıtlar fazla genel veya özellik odaklı kaldığında ya da kısmi uyumun dürüstçe belirtilmesi gerektiğinde kullanılır.
related: rfp-analysis, proposal-writing, effort-estimate-for-bid, statement-of-work, traceability-matrix
prompt: Bu RFP'deki R-10 ile R-25 arası gereksinimlere yanıtlarımızı yaz; ürünümüz çoğunu karşılıyor, ikisi özelleştirme gerektiriyor.
---

# RFP Yanıtı Yazma

## Amaç
Değerlendiricilere hızla puanlayabilecekleri ve güvenebilecekleri yanıtlar vermek: Her gereksinim doğrudan ve istenen formatta, dürüst bir uyum düzeyi, somut kanıt ve bu müşteriye sağlanan faydayla yanıtlanır.

## Ne zaman kullanılır
- Bir RFP/RFI soru listesi, uyum tablosu veya teknik yanıt bölümü yanıtlanırken.
- Mevcut taslak yanıtlar genel, kopyala-yapıştır veya ürün broşürü gibi okunuyorsa.
- Bazı gereksinimler yalnızca kısmen karşılanıyor ve sapmanın değerlendirmeyi kaybetmeden belirtilmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Teklif verip vermemeye karar vermek veya RFP'yi anlamak için `rfp-analysis` kullanılır.
- Serbest formatlı teklif anlatısı (anlayış, yaklaşım, ekip) için `proposal-writing` kullanılır.
- İhale sonrası sözleşmesel kapsam ve kabul koşulları için `statement-of-work` kullanılır.

## Girdiler
Zorunlu:
- Yanıtlanacak gereksinimler (metin ve referans numaraları) ve sunulan çözüm veya hizmetle ilgili bilgiler.

İsteğe bağlı, kaliteyi artırır:
- RFP analizi: değerlendirme kriterleri, ağırlıklar, müşterinin sıkıntıları, format ve uzunluk sınırları.
- Yeniden kullanılabilir içerik (önceki yanıtlar, ürün dokümantasyonu, sertifikalar, vaka çalışmaları).
- Bu teklif için kararlaştırılan kazanma temaları ve dolaylı olarak karşıtlık kurulacak rakip zayıflıkları.

Bir gereksinim için çözüm bilgisi yoksa tahmin etme; yanıt iskeletini `[TBD – <rol> ile teyit et]` ile yaz. Kullanıcının teyit etmediği sertifika, referans, özellik veya rakamı asla iddia etme.

## Süreç
1. Yanıt listesini gereksinimlerden oluştur; müşterinin numaralandırmasını, sırasını ve istenen formatı (evet/hayır alanları, karakter sınırları, şablonlar) koru.
2. Her gereksinim için uyum düzeyine karar ver: Tam uyumlu (standart), Yapılandırmayla uyumlu, Özelleştirme/geliştirmeyle uyumlu, Kısmen uyumlu, Yol haritasında (tarih yalnızca teyit edildiyse), Uyumsuz. Daha iyi görünmek için düzeyi asla yükseltme.
3. Her yanıtı uyum beyanı ve tek cümlelik doğrudan bir cevapla aç; değerlendiriciler çoğu zaman yalnızca ilk satırı okur.
4. Nasıl karşılandığını açıkla: genel ürün iddiaları değil, belirli mekanizma, yapılandırma veya süreç; müşterinin terminolojisini kullan.
5. Kanıt ekle: referans proje, sertifika, ekran görüntüsü veya doküman referansı, ölçülmüş sonuç; eksik kanıtı `[TBD]` olarak işaretle.
6. Müşterinin belirttiği sıkıntıya veya hedefe (RFP arka planından) bağlı faydayı yaz; çıkarım yapılan sıkıntıları `[VARSAYIM]` olarak etiketle.
7. Kısmi uyum veya uyumsuzlukta açığı, alternatifi veya geçici çözümü, eforunu ve etkisini ve fiyatı ya da süreyi etkileyip etkilemediğini belirt.
8. 2-3 kazanma temasını ilgili yerlere işle; her yanıtta tekrarlama.
9. Yanıtlar arasında ve fiyat ile planla tutarlılığı kontrol et (ör. burada belirtilen bir özelleştirme tahminde de yer almalı); tutarsızlıkları listele.
10. Puanlama için düzenle: kısa paragraflar, etken çatı, pazarlama abartısı yok, uzunluk sınırları içinde.
11. Ürün, teslimat, hukuk veya iş ortaklarından teyit gereken maddelerin listesini çıkar.
12. Kullanıcının hedefi devam ediyorsa eforu belirtilen özelleştirmelerle hizalamak için `effort-estimate-for-bid`, anlatı bölümü için `proposal-writing` veya kapsamayı çapraz kontrol etmek için `traceability-matrix` öner.

## Çıktı formatı
```markdown
# RFP Yanıtı: <müşteri> – <RFP ref>

## R-<n>: <gereksinim kısa başlığı>
**Uyum:** <düzey>
**Yanıt:** <tek cümlelik doğrudan cevap>
**Nasıl karşılıyoruz:** ...
**Kanıt:** <referans / sertifika / doküman ref veya [TBD]>
**<Müşteri> için fayda:** ...
**Sapma (varsa):** <açık – alternatif – efor/etki>

## Teyit Edilecek Maddeler
| Gereksinim | Teyit edilecek konu | Sorumlu (rol) |
|---|---|---|

## Tutarlılık Notları
- ...
```

## Kalite kontrol listesi
- [ ] Her gereksinim müşterinin numaralandırması ve formatında, sınırlar içinde yanıtlandı.
- [ ] Her yanıt dürüst bir uyum düzeyi ve doğrudan bir cevapla başlıyor.
- [ ] İddialar kanıta dayanıyor veya `[TBD]` olarak işaretli; uydurulmuş referans, sertifika veya rakam yok.
- [ ] Kısmi uyum ve uyumsuzluklarda açık, alternatif ve etki belirtilmiş.
- [ ] Özelleştirmeler ve sapmalar tahmin ve planla tutarlı.
- [ ] Faydalar bu müşteriye özgü; çıkarım yapılan sıkıntılar etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sorulmasını istediğin soruyu yanıtlamak. Değerlendiriciler gereksinim metnine göre puanlar; önce onu harfiyen yanıtla.
- Özel geliştirme gerektiren iş için tam uyum beyan etmek. Demoda veya teslimatta ortaya çıkar, güveni ve marjı zedeler.
- Broşür dili ("sınıfının en iyisi, kusursuz"). Yerine mekanizma ve kanıt koy.

## Örnek
Girdi: R-17 "Çözüm, bankanın kimlik sağlayıcısıyla tek oturum açmayı (SSO) desteklemelidir."

Çıktıdan bir bölüm:
- Zayıf (kaçın): "Platformumuz dünya standartlarında, kusursuz güvenlik sunar ve tüm kimlik sağlayıcılarla entegre olur."
- Güçlü: "**Uyum:** Yapılandırmayla uyumlu. **Yanıt:** Evet, SAML 2.0 ve OpenID Connect ile. **Nasıl:** Bankanın kimlik sağlayıcısı güvenilen yayıncı olarak yapılandırılır; roller grup claim'lerinden eşlenir. **Kanıt:** `[TBD – aynı IdP ile referans proje]`. **Fayda:** Personel mevcut kimlik bilgilerini kullanır, çalışan ayrıldığında erişim merkezi olarak kaldırılır."
