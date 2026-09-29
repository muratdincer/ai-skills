---
description: Fiyat modellerini (sabit, kademeli, kullanıcı başı, kullanım bazlı, freemium, hibrit) değer metriği, hizmet maliyeti, rakip çıpaları ve ödeme isteği sinyallerine göre karşılaştırır; fiyat testi seçenekleriyle bir model önerir. Bir ürün yayına alınırken, ücretli bir paket eklenirken, fiyatlar yeniden ele alınırken ya da bir ürünün nasıl fiyatlanacağı veya paketleneceği sorulduğunda kullanılır.
related: market-analysis, competitor-analysis, business-model-canvas, experiment-design, persona
prompt: API izleme aracımız için fiyatlandırma seçeneklerini analiz et; şu an aylık sabit 49 USD.
---

# Fiyatlandırma Analizi

## Amaç
Müşterinin önemsediği değer metriğine, hizmet maliyetine ve gerçek ödeme isteği kanıtlarına dayanan bir fiyat modeli ve paketleme önermek; karar vermeden önce gereken riskleri ve testleri ortaya koymak.

## Ne zaman kullanılır
- Yeni bir ürün veya yeni bir ücretli paket/eklenti fiyatlanırken.
- Müşteri kaybı, düşük dönüşüm veya marj sorunları fiyatların ya da paketlemenin yanlış olduğunu düşündürdüğünde.
- Modeller arası geçişte, örneğin kullanıcı başından kullanım bazlıya.

## Ne zaman kullanılmaz
- Genel pazar büyüklüğü gerekiyorsa `market-analysis` kullanılır.
- Fiyat testinin mekaniğini tasarlamak gerekiyorsa `experiment-design` kullanılır.
- Müşteriye yönelik fiyat duyurusu gerekiyorsa `release-announcement` veya `announcement` kullanılır.

## Girdiler
Zorunlu:
- Ürün, hedef segmentler ve mevcut fiyatlandırma (veya "henüz yok").

İsteğe bağlı, kaliteyi artırır:
- Hizmet maliyeti itici değişkenleri, kullanım dağılımı, dönüşüm ve kayıp verisi.
- Rakip fiyatları, kazanma/kaybetme nedenleri, ödeme isteği araştırması (Van Westendorp, Gabor-Granger, conjoint, satış indirim verisi).
- Kısıtlar: sözleşmeler, mevzuat, para birimi, vergiler, kanal ortakları.

Ürün veya segment yoksa sor. Fiyat, esneklik veya ödeme isteği asla uydurma; `[BİLİNMİYOR]` olarak işaretle ve nasıl ölçüleceğini öner.

## Süreç
1. Değer metriğini belirle: müşteri değeriyle birlikte büyüyen birim (kullanıcı, işlem, izlenen uç nokta, işlenen ciro). Sına: anlaşılır mı, alıcı için öngörülebilir mi, değerle ölçekleniyor mu, ölçülebilir mi.
2. Segmentleri aldıkları değer ve ödeme isteği sinyallerine göre haritala; mevcut fiyatlamada kimin fazla, kimin az hizmet aldığını not et.
3. Aday modelleri listele ve her birini değer uyumu, gelir öngörülebilirliği, satış sürtünmesi, maliyet karşılama ve büyüme potansiyeli açısından değerlendir.
4. Fiyat koridorunu belirle: taban hizmet maliyeti ve hedef marjdan, tavan sunulan değer ve alternatiflerden, çıpalar rakiplerden (kaynaklı, tarihli).
5. Paketlemeyi tasarla: segmentin işine göre paketler, giriş paketini sakatlamadan paketleri ayıran sınırlar (limitler veya özellikler).
6. Mevcut müşterilere geçiş etkisini değerlendir: kim daha çok veya az ödeyecek, eski fiyatın korunması (grandfathering), iletişim.
7. Dayandığı varsayımlarla birlikte bir model ve paketleme öner.
8. Doğrulama öner: ödeme isteği anketi, satış liderliğinde fiyat testi, yalnızca yeni müşterilere uygulama veya etik ve yasal olduğu durumda A/B testi.
9. İzlenecek metrikleri tanımla: dönüşüm, hesap başına ortalama gelir (ARPA), büyüme, kayıp, indirim oranı.
10. Girdide yazmayan, senin çıkardığın her noktayı `[VARSAYIM]` olarak işaretle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: tercih edilen seçeneği yaygınlaştırmadan önce doğrulamak için `experiment-design`, rakip fiyatları doğrulanmamışsa `competitor-analysis`.

## Çıktı formatı
```markdown
# Fiyatlandırma Analizi: <ürün>
## Mevcut Durum ve Problem
...
## Değer Metriği
Seçilen: <metrik> — gerekçe; reddedilen alternatifler
## Model Karşılaştırması
| Model | Değer uyumu | Öngörülebilirlik | Sürtünme | Maliyet karşılama | Büyüme |
|---|---|---|---|---|---|
## Fiyat Koridoru
Taban: ... · Tavan: ... · Çıpalar (kaynak, tarih): ...
## Önerilen Paketleme
| Paket | Hedef segment | İçerik | Sınır | Fiyat |
|---|---|---|---|---|
## Geçiş Etkisi
...
## Doğrulama Planı ve Metrikler
...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Bir değer metriği seçildi ve dört kritere göre sınandı.
- [ ] Her fiyat veya ödeme isteği rakamının kaynağı var ya da `[VARSAYIM]`/`[TBD]` olarak işaretli.
- [ ] Mevcut müşteri etkisi ve eski fiyatın korunması ele alındı.
- [ ] Paket sınırları keyfi özellik gizlemeye değil, segment ihtiyaçlarına dayanıyor.
- [ ] Tam yaygınlaştırmadan önce bir doğrulama adımı var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca maliyet artı marjla fiyatlamak. Maliyet tabanı, değer tavanı belirler.
- Çok fazla paket veya eklenti. Alıcı paketini saniyeler içinde seçebilmeli.
- Müşteriye doğrudan "X öder misiniz?" diye sormak. Yapılandırılmış ödeme isteği yöntemlerini veya davranış verisini kullan.

## Örnek
Girdi: "API izleme aracı, tüm müşterilere aylık sabit 49 USD."

Çıktıdan bir bölüm:
- Değer metriği: izlenen uç nokta sayısı; yoğun kullanıcılar (>200 uç nokta) en çok değeri alıyor ama aynı fiyatı ödüyor `[kullanım dağılımını teyit et]`.
- Öneri: uç nokta sayısına göre aşım ücretli üç paket; mevcut müşteriler için sabit fiyat 12 ay korunur `[VARSAYIM]`.
- Doğrulama: 6 hafta boyunca yalnızca yeni kayıtlara uygula; denemeden ücretliye dönüşümü ve ARPA'yı izle.
