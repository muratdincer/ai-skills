---
description: "Koddaki performans darboğazlarını tahminle değil ölçümle bulur ve giderir: hedef metriği tanımlar, profil, trace veya sorgu planlarını okur, darboğazları maliyet payına göre sıralar, beklenen kazanç ve ödünleşimlerle çözüm önerir ve iyileşmenin nasıl doğrulanacağını belirtir. Kod, bir uç nokta veya bir iş çok yavaş ya da çok kaynak tüketiyorsa veya optimize etme, hızlandırma ya da CPU, bellek veya gecikmeyi azaltma istendiğinde kullanılır."
related: "sql-query-writing, query-optimization, load-test-analysis, web-performance-audit, logging-instrumentation"
prompt: "Sipariş arama uç noktamızın normal yükte p95 değeri 2,4 sn. Handler kodu ve CPU profili burada, hızlandırmama yardım et."
---

# Performans İyileştirme

## Amaç
Gecikmeyi, throughput sınırlarını veya kaynak kullanımını önemli olduğu yerde ve ölçümlere dayanarak azaltmak. Böylece emek gerçek darboğaza gider ve her değişikliğin davranışı bozmadan fayda sağladığı gösterilebilir.

## Ne zaman kullanılır
- Bir uç nokta, iş veya fonksiyon gecikme, throughput ya da maliyet hedefini tutturamıyorsa.
- Yorumlanması gereken bir profil, trace, flame graph veya yavaş sorgu logu varsa.
- Kaynak kullanımı (CPU, bellek, allocation, bağlantı) yükten daha hızlı artıyorsa.

## Ne zaman kullanılmaz
- Tarayıcı sayfa hızı ve Core Web Vitals için `web-performance-audit` kullanılır.
- Planıyla birlikte tek bir yavaş SQL ifadesi için `query-optimization` veya `sql-query-writing` kullanılır.
- Tüm sistemin yük testi sonuçlarını analiz etmek için `load-test-analysis` kullanılır.

## Girdiler
Zorunlu:
- Kod veya bileşen ve sayıyla ifade edilmiş belirti (ör. p95 gecikme, süre, bellek tepe değeri).

İsteğe bağlı, kaliteyi artırır:
- Profiller, trace'ler, sorgu planları, metrik dashboard'ları, yük profili ve veri hacimleri.
- Hedef (SLO, bütçe) ve kısıtlar (yeni altyapı yok, API değişmemeli).

Hiç ölçüm yoksa darboğaz tahmin etme: önce bir ölçüm planı ver ve her şüpheyi `[HİPOTEZ]` olarak işaretle.

## Süreç
1. Hedefi metrik, yüzdelik ve yük koşuluyla yaz (ör. "50 istek/sn'de p95 < 500 ms"); yoksa bir hedef öner ve `[VARSAYIM]` olarak işaretle.
2. Bir başlangıç ölçümü belirle: nasıl ölçüldü, ortam, veri hacmi, sıcak ya da soğuk. Farklı koşullar arasındaki karşılaştırmaları reddet.
3. Kanıtları kullanarak zamanın veya kaynağın nereye gittiğini bul: duvar saati ve CPU süresi, I/O beklemeleri, kilit çekişmesi, GC veya allocation baskısı, N+1 çağrılar, serileştirme.
4. Darboğazları toplam maliyetteki paylarına göre sırala (Amdahl): zamanın %5'inde %50 kazanç çok az şey ifade eder.
5. Her önemli darboğaz için en ucuz etkili çözüm sınıfını seç: daha az iş yap (kaldır, toplu işle, sayfala), tekrarlanan işten kaçın (cache, memoize, önceden hesapla), işi veriye yakın yap (filtreyi veritabanına it, indeks ekle), eşzamanlı yap veya daha iyi bir algoritma ya da veri yapısı kullan.
6. Beklenen kazancı gerekçesiyle ve ödünleşimleri belirt: bellek, bayatlık, karmaşıklık, tutarlılık, maliyet.
7. Cache için anahtar, TTL, geçersiz kılma, boyut sınırı ve stampede korumasını; eşzamanlılık için sınırları ve back-pressure'ı tanımla.
8. Davranışı aynı tut: onu koruyan testleri adlandır, eksikleri kodu değiştirmeden önce ekle.
9. Doğrulamayı tanımla: aynı benchmark veya yük, aynı ortam, önce/sonra sayıları ve bir gerileme koruması (CI'da benchmark, alarm, SLO).
10. Ölçülmemiş her iddiayı `[HİPOTEZ]` olarak etiketle ve sıradaki ölçümleri listele.
11. Hedef devam ediyorsa veritabanı kaynaklı darboğazlar için `query-optimization`, sinyaller eksikse `logging-instrumentation` veya ölçekte doğrulamak için `load-test-analysis` öner.

## Çıktı formatı
```markdown
# Performans İyileştirme: <bileşen>
Hedef: <metrik, yüzdelik, yük> · Başlangıç: <değer, nasıl ölçüldü>

## Maliyet Nerede
| Sıra | Darboğaz | Kanıt | Maliyet payı |

## Önerilen Değişiklikler
| # | Değişiklik | Çözüm sınıfı | Beklenen kazanç | Ödünleşimler | Koruyan testler |

## Kod Değişiklikleri
<en önemli değişikliğin diff'i veya kodu>

## Doğrulama Planı
- Benchmark / yük: ...
- Gerileme koruması: ...

## Hipotezler ve Açık Sorular
- [HİPOTEZ] ...
```

## Kalite kontrol listesi
- [ ] Hedef yüzdelik ve yük koşulu olan bir sayı.
- [ ] Her darboğaz kanıta (profil, trace, plan, metrik) dayanıyor ya da `[HİPOTEZ]` olarak işaretli.
- [ ] Değişiklikler kolaylığa veya zevke göre değil maliyet payına göre sıralı.
- [ ] Her değişiklik ödünleşimlerini ve davranışı koruyan testleri belirtiyor.
- [ ] Önce/sonra ölçümü aynı koşulları kullanıyor.
- [ ] Hiçbir kazanç veya sayı uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- N+1 sorgu sürenin %70'ini alırken zamanın %2'sini alan kodu mikro optimize etmek. Önce sırala.
- Ortalamalar kuyruk gecikmesini gizler. Yüzdelik kullan ve en yavaş isteklerin trace'lerine bak.
- Geçersiz kılma kuralı olmayan bir cache ekleyip hız sorununu doğruluk sorununa çevirmek.
- Sıcak bir yerel döngüde benchmark alıp canlıda aynı kazancı beklemek.

## Örnek
Girdi: "Sipariş arama p95 2,4 sn. CPU profili JSON serileştirmede %18 gösteriyor; trace istek başına 40 DB çağrısı gösteriyor."

Çıktıdan bir bölüm:
| Sıra | Darboğaz | Kanıt | Maliyet payı |
|---|---|---|---|
| 1 | Her sipariş için satırları tek tek yükleyen N+1 | Trace: 40 ardışık DB span'i, ~1,6 sn | ~%65 |
| 2 | Tüm sipariş grafiğinin serileştirilmesi | Profil: %18 CPU | ~%15 `[HİPOTEZ: CPU payı ≠ duvar saati]` |

Değişiklik 1: satırları sipariş id'leriyle tek toplu sorguda yükle; p95'te kabaca DB span süresi kadar düşüş beklenir; mevcut arama sözleşme testleri ve 50 siparişli yeni bir testle korunur.
