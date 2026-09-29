---
name: opportunity-solution-tree
description: "Tek bir ölçülebilir hedef sonucu araştırmadan gelen müşteri fırsatlarına (ihtiyaçlar, sorunlar, istekler), hedef fırsat başına birden fazla aday çözüme ve varsayım testlerine bağlayan bir fırsat-çözüm ağacı oluşturur. Bir ekibin bir sonucu etkilemek için neye odaklanacağını seçmesi gerektiğinde, keşif çalışması yapıdan yoksun olduğunda ya da bir hedefi fikirlere ve deneylere bağlamak istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: discovery
  title: "Fırsat-çözüm ağacı"
  related: "okr-definition, jobs-to-be-done, hypothesis-statement, experiment-design, assumption-mapping"
  prompt: "Yeni mobil bankacılık kullanıcılarının 30 günlük elde tutma oranını artırmak için bir fırsat-çözüm ağacı oluştur."
---

# Fırsat-Çözüm Ağacı

## Amaç
Bir iş sonucundan ekibin geliştirdiği şeye giden yolu açık ve sınanabilir kılmak. Böylece ekip ilk fikre bağlanmak yerine seçenekleri karşılaştırır ve hangi varsayımların geçerli olduğunu hızla öğrenir.

## Ne zaman kullanılır
- Bir ekibin bir hedef sonucu (OKR, Kuzey Yıldızı girdisi) var ve nereye odaklanacağına karar vermesi gerekiyorsa.
- Keşif bulguları karar için bir yapı olmadan birikiyorsa.
- Paydaşlar çözüm dayatıyor ve ekibin alternatifleri ve gerekçeyi göstermesi gerekiyorsa.

## Ne zaman kullanılmaz
- Henüz üzerinde anlaşılmış bir sonuç yoksa `okr-definition` veya `north-star-metric` kullanılır.
- Yalnızca bir hipotez yazılacaksa `hypothesis-statement` kullanılır.
- Tek bir deneyin ayrıntılı tasarımı gerekiyorsa `experiment-design` kullanılır.

## Girdiler
Zorunlu:
- Ekibin etkileyebileceği tek bir ölçülebilir sonuç.

İsteğe bağlı, kaliteyi artırır:
- Araştırma: görüşmeler, yolculuk haritaları, geri bildirim temaları, analitik.
- Masadaki çözüm fikirleri, ekip kısıtları.

Sonuç yoksa ya da bir çıktıysa ("X'i yayınla"), bir sonuç iste veya öner. Kanıtı olmayan fırsatlar `[VARSAYIM]` olarak işaretlenir.

## Süreç
1. Kökü, ekibin etkileyebileceği bir metrik olarak ifade edilmiş sonuca koy (gecikmeli iş metriği değil, ürün sonucu).
2. Fırsatları araştırmadan türet: müşteri ihtiyaçları, sorunları veya istekleri; müşterinin bakış açısıyla ifade edilmiş, asla çözüm olarak değil.
3. Fırsatları hiyerarşik yapılandır: geniş üst fırsatlar, ardından ele alınabilecek kadar küçük, özgül alt fırsatlar.
4. Her alt fırsatı büyüklük (kaç kişi, ne sıklıkla), müşteri için önem, stratejiyle uyum ve kanıt gücü açısından değerlendir. Bir hedef fırsat seç.
5. Hedef fırsat için yazılım dışı bir seçenek dahil en az üç farklı çözüm üret.
6. Her çözüm için ana varsayımları türüne göre listele: arzu edilebilirlik, yaşayabilirlik (iş), yapılabilirlik, kullanılabilirlik, etik.
7. En riskli varsayımları seç ve her biri başarı eşiğine sahip küçük testler tanımla (prototip, sahte kapı, tek soruluk anket, veri kontrolü).
8. Ağacı iç içe liste veya diyagram olarak sun; karar kaydını ve sonraki testleri ekle.
9. Girdide yazmayan, senin çıkardığın her noktayı `[VARSAYIM]` olarak işaretle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: öne çıkan çözüm için `hypothesis-statement` ve `experiment-design`, en riskli varsayımları sıralamak için `assumption-mapping`.

## Çıktı formatı
```markdown
# Fırsat-Çözüm Ağacı: <sonuç>
- **Sonuç:** <metrik, başlangıç, hedef>
  - Fırsat A: "<müşteri ihtiyacı/sorunu>" (kanıt)
    - A1: "..." ← hedef (büyüklük, önem, kanıt)
      - Çözüm 1: ...
        - Varsayım: ... → Test: ... → Eşik: ...
      - Çözüm 2: ...
      - Çözüm 3: ...
    - A2: "..."
  - Fırsat B: ...

## Neden Bu Hedef Fırsat
...
## Sonraki Testler
| Test | Varsayım | Yöntem | Eşik | Sorumlu | Süre |
|---|---|---|---|---|---|
```

## Kalite kontrol listesi
- [ ] Kök tek bir ölçülebilir ürün sonucu.
- [ ] Fırsatlar kılık değiştirmiş çözümler değil, müşteri ihtiyaçları veya sorunları.
- [ ] Hedef fırsat için en az üç çözüm var.
- [ ] Her testin başarı eşiği test çalıştırılmadan önce tanımlandı.
- [ ] Fırsatların kanıt gücü görünür.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çözümleri fırsat olarak yazmak ("chatbot lazım"). Müşterinin bakış açısıyla yeniden ifade et.
- Aynı anda birçok fırsat üzerinde çalışmak. Tek bir hedefe odaklan, çözümleri onun içinde kıyasla.
- Varsayımlar yerine fikirlerin tamamını test etmek. En riskli varsayımı ucuza test et.

## Örnek
Girdi: "Yeni mobil bankacılık kullanıcılarının 30 günlük elde tutma oranını artır."

Çıktıdan bir bölüm:
- Sonuç: ilk 30 günde 3+ oturum açan yeni kullanıcı oranı, başlangıç `[BİLİNMİYOR]`.
- Fırsat: "Maaşım başka bankaya yatıyorsa uygulamayı neden açayım ki" (görüşmeler 7/12).
- Çözümler: maaş taşıma teşviki; fatura ödeme hatırlatmaları; şube personeliyle kurulum oturumu.
- Test: sahte kapı "maaşını taşı" bandı, eşik ≥%5 tıklama oranı `[VARSAYIM]`.
