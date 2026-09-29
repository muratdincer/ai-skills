---
name: data-quality-rules
description: "Bir veri seti veya veri ürünü için bütünlük, geçerlilik, teklik, tutarlılık, referans bütünlüğü, güncellik ve hacim boyutlarında test edilebilir veri kalitesi kuralları tanımlar; her kural için eşik, önem derecesi, hata durumunda aksiyon ve sorumlu belirler. Bir veri setine kalite kontrolü gerektiğinde, veri sözleşmesinin kalite bölümü yazılırken, tekrarlayan veri sorunları önlenmek istendiğinde veya bir tabloya ya da veri hattına hangi kontrollerin konacağı sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-architect
  area: governance
  title: "Veri kalitesi kuralları"
  related: "data-contract, data-catalog-entry, pipeline-spec, business-rules-catalog, pipeline-failure-analysis"
  prompt: "Aylık gelir raporunu besleyen müşteri ve sipariş tabloları için veri kalitesi kurallarını tanımla."
---

# Veri Kalitesi Kuralları

## Amaç
"Veri doğru olmalı" gibi belirsiz beklentileri; eşiği, aksiyonu ve sahibi belli, çalıştırılabilir az sayıda kontrole dönüştürmek. Böylece hatalı veri kararlara ulaşmadan durdurulur veya işaretlenir.

## Ne zaman kullanılır
- Yeni bir veri seti, veri hattı veya veri ürünü canlıya alınacaksa.
- Tüketiciler sürekli hatalı, eksik, mükerrer veya geç veriyle karşılaşıyorsa.
- Bir veri sözleşmesi veya sertifikasyon açık kalite beklentileri istiyorsa.

## Ne zaman kullanılmaz
- Üretici-tüketici anlaşmasının tamamı (SLA, sürümleme) gerekiyorsa `data-contract` kullanılır.
- Hatalı veriyle ilgili belirli bir olay teşhis edilecekse `pipeline-failure-analysis` kullanılır.
- Veri kontrolü değil uygulamanın iş kuralları kataloglanıyorsa `business-rules-catalog` kullanılır.

## Girdiler
Zorunlu:
- Şeması veya alan listesiyle veri set(ler)i ve verinin hizmet etmesi gereken en az bir tüketici kullanım senaryosu.

İsteğe bağlı:
- Bilinen sorunlar ve geçmiş olaylar, veri hacmi ve yükleme deseni, iş kuralları, referans veri, mevcut kontroller, hassasiyet sınıfı.

Ne şema ne kullanım senaryosu verilmişse iste; kullanım senaryosu olmadan kurallar önceliklendirilemez.

## Süreç
1. Her veri setinin tanecik ve anahtarını, ayrıca kritik veri öğelerini (CDE) belirle: hatası bir kararı, finansal bir rakamı veya yasal bir raporu değiştiren alanlar.
2. Kullanım senaryosundan ve geçmişten hata modlarını çıkar: hatalı veri nasıl görünür ve maliyeti ne olur. Gözlenmemiş, çıkarım yaptığın hata modlarını `[VARSAYIM]` olarak işaretle.
3. CDE'lerden başlayarak boyut bazında kurallar yaz: bütünlük (boş olmama, zorunlu popülasyonlar), geçerlilik (tip, aralık, desen, izinli değerler), teklik (anahtar ve iş anahtarı), tutarlılık (alanlar ve veri setleri arası, ör. satır toplamı başlık toplamına eşit), referans bütünlüğü (yetim kayıtlar), güncellik (tazelik gecikmesi), hacim (referans döneme göre satır sayısı, dağılım kayması).
4. Her kuralı kesin, araçtan bağımsız bir yüklem veya SQL benzeri ifadeyle yaz ve çalıştığı popülasyonu belirt (tüm satırlar, günün bölümü, değişen satırlar).
5. Eşikleri belirle: mutlak (anahtarda sıfır mükerrer) veya toleranslı (boş oranı %x altında, hacim son dönem ortalamasının ±%y içinde). Bilinmeyen eşikler, geçmiş veriden kalibrasyon yöntemiyle birlikte `[TBD]` olur.
6. Önem derecesi ve aksiyon ata: Kritik yayını durdurur veya partiyi karantinaya alır; Majör uyarı ve kayıtla yayımlar; Minör eğilim için loglanır. Önem derecesini kural tipine değil tüketici etkisine bağla.
7. Her kuralın nerede çalışacağına karar ver: kaynakta/üreticide, alım kapısında, dönüşüm sonrasında veya kayıt sistemine karşı mutabakat olarak. Sorunu yakalayabilen en erken noktayı tercih et.
8. Sahipliği ata: veriyi kim düzeltir (üretici), kim bilgilendirilir (tüketiciler, veri sorumlusu) ve beklenen yanıt süresi.
9. Ölçüm ve raporlamayı tanımla: kural bazında geçme oranı, eğilim, gerekiyorsa veri seti kalite skoru ve istisnaların nasıl gözden geçirileceği.
10. Buda: kimsenin aksiyon almayacağı kuralları ve veritabanı şemasının zaten zorladığı kısıtların kopyalarını çıkar.
11. Varsayımları ve açık soruları listele. Hedef devam ediyorsa kuralları gömmek için `data-contract`, veri hattına bağlamak için `pipeline-spec` veya kalite durumunu yayımlamak için `data-catalog-entry` öner.

## Çıktı formatı
```markdown
# Veri Kalitesi Kuralları: <veri seti / ürün>
Tanecik: <...> | Anahtar: <...> | CDE'ler: <liste> | Sahip: <üretici ekip> | Veri sorumlusu: <...>

| No | Boyut | Alan(lar) | Kural (yüklem) | Popülasyon | Eşik | Önem | Hata durumunda | Çalıştığı yer | Sorumlu |
|---|---|---|---|---|---|---|---|---|---|
| DQ-01 | Teklik | order_id | count(*) = count(distinct order_id) | günlük bölüm | 0 ihlal | Kritik | partiyi karantinaya al | yükleme sonrası | Checkout ekibi |

## Mutabakat
- <kaynak ve hedef kontrol toplamları, sayılar, tutarlar>

## Raporlama
- Metrikler: <geçme oranı, eğilim> | Gözden geçirme: <sıklık, platform>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
- [TBD] ...
```

## Kalite kontrol listesi
- [ ] Her CDE'nin en az bir kuralı var; kritik olmayan alanlar gereğinden fazla test edilmiyor.
- [ ] Her kural, popülasyonu tanımlı ve tek anlamlı bir yüklem.
- [ ] Her kuralın eşiği (veya kalibrasyon yöntemiyle `[TBD]`), önem derecesi, aksiyonu ve sorumlusu var.
- [ ] Sessiz veri kaybını en az bir mutabakat veya hacim kontrolü yakalıyor.
- [ ] Güncellik, yükleme takvimine değil tüketicinin ihtiyacına göre kontrol ediliyor.
- [ ] Şema kısıtlarını tekrarlayan kurallar çıkarıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kimsenin okumadığı yüzlerce otomatik "boş olamaz" kontrolü. CDE'lerden ve hata modlarından başla; alarm yorgunluğu kalite programlarını öldürür.
- Mevsimsel veride sabit hacim eşikleri. Bunun yerine aynı haftanın günü veya kayan bir referans dönemle karşılaştır.
- Yalnızca alarm veren kontroller. Durdurma/karantina kararı ve sorumlu yoksa Kritik kurallar hiçbir şeyi değiştirmez.
- Yalnızca hedefi doğrulamak. Kaynak-hedef mutabakatı olmadan eksik satırlar görünmez.

## Örnek
Girdi: "Müşteri ve sipariş tabloları aylık gelir raporunu besliyor; geçen çeyrek mükerrer kayıtlar geliri şişirdi."

Çıktıdan bir bölüm:
- DQ-01 Teklik, orders.order_id, yükleme başına 0 mükerrer, Kritik, partiyi karantinaya al, yükleme sonrası, Checkout ekibi.
- DQ-04 Tutarlılık, sipariş bazında sum(order_lines.amount) = orders.total_amount, tolerans 0,01, Majör, uyarıyla yayımla.
- DQ-07 Hacim, günlük sipariş sayısı son 4 haftanın aynı günlerine göre ±%30 içinde `[VARSAYIM: geçmiş veriyle kalibre et]`.
