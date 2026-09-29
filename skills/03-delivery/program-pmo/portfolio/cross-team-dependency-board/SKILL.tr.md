---
name: cross-team-dependency-board
description: "Ekipler arası bağımlılık planlamasını yürütür; ekipler arasındaki her bağımlılığı ortaya çıkarır, her birini açık hale getirir (sağlayan, tüketen, ne, gereken tarih), bir taahhüt ya da alternatif üzerinde müzakere eder ve eskalasyon kurallarıyla ortak bir panoda durumunu izler. Birden fazla ekip aynı dönemi birlikte planlarken, bir program ekipler arası beklemeler yüzünden sürekli kayarken veya ekipler arası bağımlılıkların haritalanması, müzakere edilmesi ya da izlenmesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: program-pmo
  area: portfolio
  title: "Ekipler arası bağımlılık planlaması"
  related: "dependency-map, program-roadmap, raid-log, escalation-message, negotiation-prep"
  prompt: "Önümüzdeki çeyreğin planlaması için bir bağımlılık panosu kur; 4 ekip var ve ödeme adımı ekibi neredeyse her şey için ödeme ve kimlik ekiplerine bağımlı."
---

# Ekipler Arası Bağımlılık Planlaması

## Amaç
Ekipler arası her bağımlılığı açık, üzerinde anlaşılmış ve görünür hale getirmek. Böylece ekipler umutlara değil gerçek taahhütlere göre plan yapar ve riskteki bağımlılıklar planı değiştirmeye yetecek kadar erken eskale edilir.

## Ne zaman kullanılır
- Birden fazla ekip aynı dönemi planlıyor ve işleri kesişiyorsa.
- Bir program, işler başka bir ekibi beklediği için tekrar tekrar kayıyorsa.
- Ortak bir planlama etkinliği bağımlılıklar için bir pano ve müzakere düzeni gerektiriyorsa.

## Ne zaman kullanılmaz
- Bağımlılıklar tek bir proje takvimi içindeyse `dependency-map` kullanılır.
- İhtiyaç programın genel zaman çizelgesi ve kilometre taşlarıysa `program-roadmap` kullanılır.
- Yalnızca engellenmiş tek bir iş için eskalasyon mesajı gerekiyorsa `escalation-message` kullanılır.

## Girdiler
Zorunlu:
- İlgili ekipler ve planlama ufku.
- Her ekibin bu ufuk için planladığı işler veya hedefler (liste yeterli).

İsteğe bağlı, kaliteyi artırır:
- Bilinen bağımlılıklar, ortak platformlar veya uzmanlar, tedarikçi girdileri.
- Ekip kapasitesi ve iterasyon takvimi.
- Mevcut eskalasyon yolları ve karar sahipleri.

Ekipler veya planlanan işler eksikse sor. Bilinmeyen tarihler veya taahhütler `[TBD]` olarak kalır ve teyitsiz gösterilir.

## Süreç
1. Her ekibin planladığı işleri şu sorularla bağımlılık için tara: başka birinden API, veri, ortam, karar, onay, uzman yetkinlik, ortak bileşen veya tedarikçi teslimatı gerekiyor mu? Tersini de sor: bu ekipten kim bir şey bekliyor? Çıkarım olan bağımlılıkları `[VARSAYIM]` olarak işaretle.
2. Her bağımlılığı bir kart olarak yaz: ID, tüketen ekip, sağlayan ekip, tam olarak ne gerektiği (doğrulanabilir teslimat), gereken tarih veya iterasyon, bu yüzden engellenen tüketici işi.
3. Türünü (geliştirme, karar, ortam, bilgi, dış) ve kritikliğini sınıflandır: bir program kilometre taşının veya kritik yolun üzerinde mi?
4. Her kartı sağlayan-tüketen eşleşmesinde müzakere et: sağlayan kapasitesini ve taahhüt ettiği tarihi teyit eder ya da bir alternatif önerir (daraltılmış kapsam, geçici stub veya sözleşme, yeniden sıralama, tüketicinin kendi kendine yapması). Sonucu Taahhüt edildi, Koşullu taahhüt edildi, Taahhüt edilmedi veya Yeniden tasarımla kaldırıldı olarak kaydet.
5. Taahhüt edilmeyen veya geç taahhüt edilen kartlar için en düşük maliyetli çözümü bul: tüketici işini yeniden sırala, bir sözleşme veya mock ile ayrıştır, kapasite kaydır ya da karar sahibine eskale et.
6. Kartları panoya yerleştir: satırlarda ekipler, sütunlarda iterasyonlar veya haftalar, sağlayanın teslimatından tüketicinin ihtiyacına bir çizgi. Teslimatın ihtiyaçtan sonra olduğu veya bir ekibin çok fazla gelen bağımlılık taşıdığı yerleri kırmızıyla işaretle.
7. Yoğunlaşma riskini belirle: en çok gelen bağımlılığı olan sağlayıcı ekipler ve tek hata noktaları (tek uzman, tek ortam). Azaltma önlemleri öner.
8. İzleme düzenini tanımla: durum değerleri (Başlamadı, Yolunda, Riskte, Gecikti, Tamam), güncelleme sıklığı, kimin güncellediği ve eskalasyon kuralları (ör. bir döngüden uzun Riskte kalan veya gereken tarihine iki haftadan az kalan kart program liderine gider).
9. Sağlayıcı sahibi olmayan açık bağımlılıkları ve gereken kararları, kimin karar vermesi gerektiği ve ne zamana kadar olduğuyla kaydet.
10. Hedef devam ediyorsa taahhüt edilen tarihleri yansıtmak için `program-roadmap`, riskli olanları izlemek için `raid-log` veya eskale edilmesi gerekenler için `escalation-message` öner.

## Çıktı formatı
```markdown
# Bağımlılık Panosu: <program / planlama dönemi>
Ekipler: <liste> · Ufuk: <iterasyonlar / tarihler> · Güncelleme: <tarih>

## Bağımlılık Kaydı
| ID | Tüketen | Sağlayan | Gereken (doğrulanabilir) | Gereken tarih | Taahhüt tarihi | Tür | Kritik yol | Durum | Not / alternatif |
|---|---|---|---|---|---|---|---|---|---|

## Pano Görünümü
| Ekip | <iter 1> | <iter 2> | <iter 3> | <iter 4> |
|---|---|---|---|---|
| <sağlayan ekip> | D-01 ▶ | | | |
| <tüketen ekip> | | ▶ D-01 gerekli | | |
Kırmızı bayraklar: <teslimat > ihtiyaç olan kartlar>

## Yoğunlaşma ve Tek Hata Noktaları
## İzleme ve Eskalasyon Kuralları
## Çözülmemiş Konular ve Gereken Kararlar
1. <konu> — <karar sahibi> — <ne zamana kadar>
## Varsayımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her bağımlılık tüketeni, sağlayanı, doğrulanabilir bir teslimatı ve gereken tarihi ya da `[TBD]` işaretini içeriyor.
- [ ] Her kartın müzakere edilmiş bir durumu var; teyit edilmemiş taahhütler taahhüt edilmiş gibi gösterilmiyor.
- [ ] Teslimatın ihtiyaçtan geç olduğu kartlar önerilen çözümle birlikte işaretli.
- [ ] Yoğunlaşma riski ve tek hata noktaları belirlendi.
- [ ] Eskalasyon kuralları tetikleyiciyi, yolu ve zamanlamayı belirtiyor.
- [ ] Çıkarım olan bağımlılıklar etiketli ve teyit için listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Ödeme ekibinin desteği gerekiyor" gibi muğlak kartlar. İki tarafın da tamamlandığını doğrulayabileceği bir teslimat tanımla.
- Sağlayan itiraz etmedi diye bağımlılığı taahhüt edilmiş kaydetmek. Yalnızca sağlayanın açık teyidi geçerlidir.
- Bağımlılıkları değişmez kabul etmek. Çoğu zaman en ucuz çözüm daha fazla koordinasyon değil, yeniden tasarımdır (stub, önce sözleşme, tüketicinin kendi kendine yapması).

## Örnek
Girdi: "4 ekip; ödeme adımı ekibi neredeyse her şey için ödeme ve kimlik ekiplerine bağımlı."

Çıktıdan bir bölüm:
| ID | Tüketen | Sağlayan | Gereken | Gereken tarih | Taahhüt | Durum |
|---|---|---|---|---|---|---|
| D-01 | Ödeme adımı | Ödemeler | Üzerinde anlaşılmış sözleşme v1 ile staging'de iade API'si | İter 2 | İter 3 | Riskte |
| D-02 | Ödeme adımı | Kimlik | Karar: misafir alışverişe izin var mı? | İter 1 | `[TBD]` | Taahhüt edilmedi |

- D-01 alternatifi: ödeme adımı ekibi iter 2'de sözleşme stub'ına karşı geliştirir; ödemeler gerçek API'yi iter 3'te teslim eder; entegrasyon testi iter 3'e alınır.
- Yoğunlaşma: 11 gelen bağımlılığın 7'si ödemeler ekibinde; her iterasyon başında ortak bir API sözleşmesi gözden geçirmesi öner.
