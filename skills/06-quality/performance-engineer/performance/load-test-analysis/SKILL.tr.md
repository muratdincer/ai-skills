---
name: load-test-analysis
description: "Yük testi sonuçlarını analiz eder: test koşumunu doğrular, verimi, gecikme yüzdeliklerini ve hata oranlarını kabul kriterleriyle karşılaştırır, darboğazı bulmak için istemci tarafı sonuçları sunucu tarafı kaynak, havuz, kuyruk ve veritabanı metrikleriyle ilişkilendirir, kanıta dayalı düzeltmeler ve yeniden testler önerir. Bir yük, stres, ani yük veya dayanıklılık testi koşulduğunda ve raporu, metrikleri veya grafikleri yorumlanacağında ya da bir test sonucu tartışmalı olup ikinci bir görüş gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: performance-engineer
  area: performance
  title: "Yük testi sonuç analizi"
  related: "performance-test-plan, capacity-test-report, performance-optimization, query-optimization, observability-plan"
  prompt: "Dünkü checkout yük testinin sonuçları ekte: özet tablo, gecikme grafiği açıklaması ve veritabanı CPU'su. Geçtik mi, darboğaz nerede?"
---

# Yük Testi Sonuç Analizi

## Amaç
Üzerinde anlaşılmış kriterlere göre net bir geçti/kaldı kararı vermek; test başarısız olduğunda veya performans düştüğünde darboğazı kanıtıyla adlandırmak ve bir sonraki deneyi belirlemek. Analiz güvenilir olmalıdır: geçersiz bir test koşumu yorumlanmaz, geçersiz olarak raporlanır.

## Ne zaman kullanılır
- Bir yük, stres, ani yük veya dayanıklılık testi bitti ve sonuçlar yorumlanacak.
- Bir sonuç tartışmalı ("sorun test ortamındaydı") ve nesnel bir incelemeye ihtiyaç var.
- Bir düzeltme veya yapılandırma değişikliğinden sonra birden çok koşum karşılaştırılacak.

## Ne zaman kullanılmaz
- Test henüz tasarlanmadıysa `performance-test-plan` kullanılır.
- Soru planlama için sürdürülebilir maksimum yük ve paysa `capacity-test-report` kullanılır.
- Belirli bir yavaş sorgu veya kod yolu zaten belirlendiyse `query-optimization` veya `performance-optimization` kullanılır.

## Girdiler
Zorunlu:
- Test sonuçları: yük profiliyle birlikte, işlem başına veya genel olarak en azından verim, gecikme (tercihen yüzdelikler) ve hatalar.

İsteğe bağlı, kaliteyi artırır:
- Kabul kriterleri/SLO'lar, test planı, sunucu tarafı metrikler (CPU, bellek, GC, thread/bağlantı havuzları, kuyruk derinliği, veritabanı beklemeleri), izler, yük üreticisi metrikleri.
- Önceki koşumlar veya üretim temel çizgisi, son değişiklikler.

Sonuçlar yoksa iste. Kabul kriterleri yoksa davranışı analiz et ve kararı `[VARSAYIM: kriter verilmedi]` olarak işaretle.

## Süreç
1. Koşumu doğrula: yük üreticisi hedef hıza ulaştı mı, üreticiler doydu mu (CPU, ağ), ısınma yapıldı mı, hata türleri test kaynaklı hatalar (tükenen veri, script hataları) içeriyor mu? Koşum geçersizse dur ve neyin düzeltilmesi gerektiğini belirt.
2. Zaman çizelgesini bölümlere ayır: ramp-up, sabit durum, ramp-down; kabul için yalnızca sabit durumu analiz et, geçici etkileri ayrıca not et.
3. Her işlemi kriterlerle karşılaştır: ulaşılan verim ve hedef, p50/p95/p99 ve azami gecikme, türüne göre hata oranı (HTTP kodu, zaman aşımı, iş hatası). Her kriter için geçti/kaldı işaretle.
4. Doygunluk desenini ara: verimin artmayı bırakıp gecikmenin yükseldiği yük seviyesi (kırılma/diz noktası) veya hataların başladığı nokta.
5. O andaki sunucu tarafı metriklerle ilişkilendir: CPU, bellek ve GC duraklamaları, thread ve bağlantı havuzu tükenmesi, kuyruk derinliği, veritabanı beklemeleri ve kilitler, aşağı akış gecikmesi, otomatik ölçekleme olayları. Her kaynak için kullanım-doygunluk-hata görünümünü kullan.
6. Kanıta göre sıralanmış darboğaz hipotezleri kur; her biri için neyin desteklediğini ve neyin çürüteceğini yaz. İlişkilendirilmiş kanıt olmadan kök neden adlandırma; çıkarımları `[VARSAYIM]` olarak etiketle.
7. Dayanıklılık testlerinde zaman içindeki trendleri kontrol et: bellek artışı, bağlantı sızıntıları, kötüleşen gecikme, disk veya log büyümesi.
8. Varsa önceki koşumlar veya temel çizgiyle karşılaştır; değişimi sayısallaştır.
9. Düzeltmeleri ve her birini doğrulayacak yeniden testi öner (her yeniden koşumda tek değişken değiştir).
10. Sınırlamaları belirt: ortam farkları, veri hacmi, eksik metrikler.
11. Hedef devam ediyorsa sistem geçtiğinde `capacity-test-report`, belirlenen darboğaz için `performance-optimization` veya `query-optimization`, önemli metrikler eksikse `observability-plan` öner.

## Çıktı formatı
```markdown
# Yük Testi Analizi: <sistem / test / tarih>
Koşum geçerliliği: Geçerli / Geçersiz (gerekçe) · Test türü: ... · Yük profili: ...
Karar: Geçti / Kaldı / Risklerle geçti

## Kriterlere Göre Sonuçlar (sabit durum)
| İşlem | Hedef hız | Ulaşılan | p95 (hedef) | p99 (hedef) | Hata oranı (hedef) | Sonuç |
|---|---|---|---|---|---|---|

## Doygunluk ve Darboğaz
- Diz noktası: ...
| # | Hipotez | Kanıt | Şu durumda çürür | Güven |
|---|---|---|---|---|

## Temel Çizgiyle Karşılaştırma
## Öneriler ve Yeniden Testler
| Düzeltme | Beklenen etki | Doğrulama |
|---|---|---|
## Sınırlamalar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Herhangi bir yorumdan önce, yük üreticisi doygunluğu dahil koşum geçerliliği kontrol edildi.
- [ ] Kabul, ortalamalara veya ramp aşamalarına değil sabit durum yüzdeliklerine göre değerlendirildi.
- [ ] Alıntılanan her sayı verilen sonuçlardan geliyor; eksik olanlar `[BİLİNMİYOR]`.
- [ ] Darboğaz iddiası ilişkilendirilmiş istemci ve sunucu kanıtına dayanıyor ya da hipotez olarak etiketli.
- [ ] Her önerinin tek değişken değiştiren bir doğrulama yeniden testi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sonuç olarak ortalama yanıt süresini raporlamak. Kullanıcı deneyimini ve zaman aşımlarını kuyruk gecikmesi belirler.
- Yük üreticisi doyduğunda veya test verisi tükendiğinde uygulamayı suçlamak.
- Yalnızca yüksek CPU'ya bakıp "darboğaz veritabanı" demek. Aynı zaman damgasında beklemeleri, kilitleri ve bağlantı havuzu kullanımını kontrol et.

## Örnek
Girdi: Hedef 120 istek/sn; ulaşılan 95 istek/sn; 90 istek/sn'den sonra p95 300 ms'den 2,4 sn'ye çıkıyor; uygulama CPU %45; DB bağlantı havuzu 50/50 dolu; zaman aşımı %3.

Zayıf: "Performans kötü, daha fazla sunucu ekleyin."

Güçlü örnekten bir bölüm:
- Karar: Kaldı — verim 95/120 istek/sn, p95 2,4 sn (hedef ≤ 800 ms), hata oranı %3 (hedef < %0,5).
- Diz noktası ~90 istek/sn. Hipotez 1: bağlantı havuzu tükenmesi (gecikmenin arttığı anda havuz tam 50/50 dolu, uygulama CPU'su yalnızca %45). DB beklemeleri bunun yerine kilit çekişmesi gösterirse çürür.
- Yeniden test: havuzu DB azami bağlantı sayısına göre doğrulanmış bir boyuta çıkar, aynı profili yeniden koş; beklenen diz noktası 120 istek/sn'nin üzerinde.
