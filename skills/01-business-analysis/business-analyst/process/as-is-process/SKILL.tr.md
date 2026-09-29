---
name: as-is-process
description: "Mevcut (as-is) iş sürecini görüşme ve gözlem notları, prosedürler veya sistem kayıtlarından belgeler: tetikleyici, adımlar, aktörler, sistemler, girdi/çıktılar, karar noktaları, süreler, hacimler, sorunlar ve geçici çözümler. Bir süreç iyileştirilecek, otomatikleştirilecek veya değiştirilecekse ve ekibin önce işin bugün gerçekte nasıl yapıldığına dair ortak, kanıta dayalı bir resme ihtiyacı varsa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: process
  title: "Mevcut süreci (as-is) belgeleme"
  related: "to-be-process, bpmn-model, value-stream-map, observation-notes, interview-notes-analysis"
  prompt: "Muhasebe ve iki departman yöneticisiyle yapılan görüşme notlarından tedarikçi fatura onayı için mevcut süreci belgele."
---

# Mevcut Süreci (As-Is) Belgeleme

## Amaç
Sürecin bugün gerçekte nasıl işlediğinin, gayriresmî kısımları da dahil, olgulara dayalı ve ortak bir tarifini oluşturmak. Böylece iyileştirme ve otomasyon kararları resmî prosedüre değil kanıta dayanır.

## Ne zaman kullanılır
- Hedef süreç, otomasyon veya sistem değişikliği tasarlanmadan önce.
- Paydaşlar aynı süreci farklı anlattığında.
- Süreçle ilgili bilinen şikâyetler (gecikme, hata, yeniden iş) var ama nedenleri net değilse.

## Ne zaman kullanılmaz
- Amaç gelecekteki süreci tasarlamaksa `to-be-process` kullanılır.
- Resmî BPMN gösterimi gerekiyorsa `bpmn-model` kullanılır (bu skill'den sonra veya birlikte).
- Uçtan uca israf ve akış sürelerini sayısallaştırmak gerekiyorsa `value-stream-map` kullanılır.

## Girdiler
Zorunlu:
- Mevcut süreci anlatan en az bir kaynak: görüşme veya çalıştay notları, gözlem notları, prosedür dokümanları ya da sistem/kayıt verisi.
- Süreç sınırı: hangi tetikleyiciyle başlar, hangi sonuçla biter. Yoksa bir sınır öner ve `[VARSAYIM]` olarak işaretle.

İsteğe bağlı, kaliteyi artırır:
- Hacimler, döngü süreleri, hata veya yeniden iş oranları.
- Organizasyon şeması, sistem listesi, kullanılan form ve şablonlar.

## Süreç
1. Sınırı sabitle: ad, tetikleyici, bitiş durum(lar)ı, kapsam içi/dışı varyantlar, süreç sahibi.
2. Kaynakları ayır: hangi ifadelerin prosedürden (tasarlandığı gibi), hangilerinin uygulayıcılardan veya veriden (yapıldığı gibi) geldiğini not et. Farklılık varsa modelde uygulanan hâl esas alınır, fark not edilir.
3. Aktörleri (isim değil rol) ve sistemleri, tablolar, e-posta ve kâğıt dahil, listele.
4. Adımları fiil + nesne biçiminde ("Sipariş eşleşmesini kontrol et") sırala; her birinde aktör, sistem, girdi, çıktı ve uygulanan iş kuralı olsun.
5. Karar noktalarını koşulları ve her çıkış yoluyla işaretle; yalnızca ana yolu değil, yeniden iş döngülerini ve istisnaları da dahil et.
6. Aktörler veya sistemler arası devir teslimleri kaydet; her devir gecikme ve hata adayıdır.
7. Biliniyorsa süre ve hacimleri kaydet: işlem süresi, bekleme süresi, sıklık, yoğun dönemler. Bilinmeyen değerler `[BİLİNMİYOR]` olur, olgu gibi tahmin edilmez.
8. Adım bazında sorunları ve geçici çözümleri kanıtıyla (kim söyledi, veri noktası), kontrolleri de (onaylar, mutabakatlar, denetim noktaları) kaydet.
9. Her adımda işlenen kişisel veya hassas veriyi not et; kaynak notlardaki gerçek isimleri veya müşteri verilerini maskele.
10. Kaynaklar arasındaki farklılıkları ve doğrulama sorularını listele; uygulayıcılarla bir üzerinden geçme (walkthrough) oturumu öner.
11. Kullanıcı devam etmek isterse iyileştirmeyi tasarlamak için `to-be-process`, biçimsel diyagram için `bpmn-model` veya israfı sayısallaştırmak için `value-stream-map` öner.

## Çıktı formatı
```markdown
# Mevcut Süreç: <ad>
Sahip: <rol> · Tetikleyici: <olay> · Bitiş durum(lar)ı: <sonuçlar> · Kaynaklar: <liste> · Sürüm/tarih

## Kapsam
İçinde: ... · Dışında: ... · Varyantlar: ...

## Aktörler ve Sistemler
| Aktör (rol) | Sorumluluk | Kullanılan sistem/araçlar |
|---|---|---|

## Süreç Adımları
| # | Adım (fiil + nesne) | Aktör | Sistem | Girdi | Çıktı | Kural/Karar | Süre (işlem/bekleme) | Sorun / geçici çözüm |
|---|---|---|---|---|---|---|---|---|

## Karar Noktaları ve İstisnalar
- K1 <koşul> → evet: adım x, hayır: adım y

## Metrikler (bilinen)
Hacim: ... · Toplam süre: ... · Yeniden iş oranı: ...

## Sorun Özeti
| # | Sorun | Adımlar | Kanıt | Etki |
|---|---|---|---|---|

## Farklılıklar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Sınır (tetikleyici ve bitiş durumu) açık.
- [ ] Her adımın bir aktörü ve çıktısı var; devir teslimler görünür.
- [ ] Yalnızca mutlu yol değil, istisnalar ve yeniden iş döngüleri de belgelendi.
- [ ] Sorunlar kanıta dayanıyor; hiçbir sayı uydurulmadı.
- [ ] Prosedür ile uygulama arasındaki farklar kaydedildi.
- [ ] As-is tarifine iyileştirme fikirleri karıştırılmadı (ayrı bir listede tutuldu).
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Gerçeklik yerine prosedür el kitabını belgelemek. İşi yapan kişilerle doğrula.
- Haritalarken çözüm tasarlamak. Modelin dışında bir "iyileştirme fikirleri" listesi tut.
- Aktör olarak kişi isimleri kullanmak. Rol kullan; isimler değişir ve kişisel veri olabilir.

## Örnek
Girdi: "Muhasebe uzmanı faturayı e-postayla alır, ERP'ye girer, onay için departman yöneticisine e-posta atar, bir hafta yanıt gelmezse telefonla takip eder."

Çıktıdan bir bölüm:
| # | Adım | Aktör | Sistem | Çıktı | Süre (işlem/bekleme) | Sorun / geçici çözüm |
|---|---|---|---|---|---|---|
| 1 | Faturayı al | Muhasebe uzmanı | Ortak posta kutusu | Fatura PDF | [BİLİNMİYOR] | Birden fazla adrese mükerrer faturalar geliyor |
| 2 | Fatura verisini gir | Muhasebe uzmanı | ERP | Taslak fatura | [BİLİNMİYOR] | Elle veri girişi |
| 3 | Onay iste | Muhasebe uzmanı | E-posta | Onay e-postası | 1 haftaya kadar bekleme | Telefonla takip (geçici çözüm) |
