---
description: Bir ürün veya özellik kapsamını, en riskli değer varsayımını gerçek kullanıcılarla sınayan en küçük sürüme indirir; varsayım odaklı kesim, mutlaka/sonra/asla kapsam tablosu, açık bir kalite tabanı, öğrenme hedefleri ve çıkış kriterleri kullanır. Kapsam eldeki süreye göre çok büyükse, "MVP'miz ne" diye sorulduğunda ya da ekip ilk sürümden neyi dışarıda bırakacağına karar vermesi gerektiğinde kullanılır.
related: hypothesis-statement, story-mapping, prd-writing, assumption-mapping, release-planning
prompt: Saha servis planlama uygulaması için 8 haftamız ve 40 maddelik bir özellik listemiz var; MVP kapsamını belirlememe yardım et.
---

# MVP Kapsamını Belirleme

## Amaç
Belirli bir kullanıcıya gerçek değer sunan ve bir sonraki yatırım kararı için gereken öğrenmeyi sağlayan en küçük tutarlı sürümü tanımlamak; bilinçli olarak dışarıda bırakılanları ve nedenlerini açıkça listelemek.

## Ne zaman kullanılır
- İstek listesi süreyi, bütçeyi veya ekip kapasitesini açıkça aşıyorsa.
- Yeni bir ürün veya büyük bir özellik, talebi ya da değeri doğrulayan ilk bir sürüme ihtiyaç duyuyorsa.
- Paydaşlar ilk sürümün neleri içermesi gerektiği konusunda anlaşamıyorsa.

## Ne zaman kullanılmaz
- Ekip ürün geliştirmeden tek bir varsayımı sınamak istiyorsa `hypothesis-statement` ve `experiment-design` kullanılır.
- Kapsam üzerinde anlaşıldı ve kullanıcı yolculuğu boyunca sürüm dilimleri gerekiyorsa `story-mapping` veya `release-planning` kullanılır.
- Üzerinde anlaşılmış kapsamın gereksinimleri yazılacaksa `prd-writing` kullanılır.

## Girdiler
Zorunlu:
- Ürün veya özellik fikri, hedef kullanıcı segmenti ve aday özellik listesi (ya da listeyi çıkarmaya yetecek açıklama).

İsteğe bağlı, kaliteyi artırır:
- Süre/kapasite kısıtı, son tarihin nedeni, lansman kitlesi (iç, beta, herkese açık).
- Kanıtlar ve bilinen riskler; regülasyon veya sözleşmeden gelen zorunluluklar.
- Mevcut hikaye haritası veya PRD.

Hedef kullanıcı veya özellik listesi eksikse sor. Kapasite veya tahmin uydurma; `[TBD]` olarak işaretle.

## Süreç
1. Tek bir birincil kullanıcıyı ve MVP'nin baştan sona yaptırması gereken tek işi adlandır; iş onlarsız başarısız olmuyorsa ikincil kullanıcılar ertelenir.
2. En riskli varsayımları (değer, kullanılabilirlik, yapılabilirlik, sürdürülebilirlik) listele ve MVP'nin yanıtlaması gereken 1-3 tanesini seç; bunları öğrenme hedefi olarak yaz.
3. Bu iş için uçtan uca en küçük akışı çıkar (genellikle 4-8 adım); her adımın manuel de olsa (concierge, yönetim aracı, tablo) en azından temel bir çözümü olmalı.
4. Her aday maddeyi sınıflandır: Mutlaka (onsuz iş başarısız olur veya öğrenme hedefi ölçülemez), Sonra (iyileştirir ama öğrenmek için gerekmez), Asla/Şimdi değil (strateji dışı); her Mutlaka için tek satırlık gerekçe yaz.
5. Her Mutlaka maddesini sorgula: manuel yapılabilir mi, daraltılabilir mi (tek platform, tek bölge, tek entegrasyon), arka planda taklit edilebilir mi? İşi çalışır tutan en ucuz sürümle değiştir.
6. Pazarlık konusu olmayanları ayrı tut: güvenlik, gizlilik (kişisel veri varsa KVKK/GDPR), yasal gereklilikler, temel erişilebilirlik, veri bütünlüğü. Bunlar isteğe bağlı kapsam değil, kalite tabanıdır.
7. Öğrenme hedeflerini ölçmek için gereken ölçümlemeyi tanımla; ölçümü olmayan bir MVP sayılmaz.
8. Kapasiteye uyumu yalnızca ekibin verdiği tahminlerle kontrol et; Mutlaka listesi hâlâ sığmıyorsa kalite tabanını değil kapsamı daha da kes veya kitleyi daralt.
9. Çıkış kriterlerini belirle: ölçekle, yinele veya durdur anlamına gelen sinyaller ve kararın verileceği tarih ya da örneklem.
10. Açıkça dışarıda kalanları, kesimin risklerini ve madde kaybeden paydaşlar için iletişim noktalarını listele.
11. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: MVP'yi yayınlanabilir artımlara bölmek için `story-mapping`, spesifikasyonunu yazmak için `prd-writing`.

## Çıktı formatı
```markdown
# MVP Kapsamı: <ürün/özellik>
Birincil kullanıcı: <segment> · İş: <iş ifadesi> · Kitle: <iç/beta/herkese açık>

## Öğrenme Hedefleri
1. <varsayım> – ölçüm: <metrik/sinyal>

## Uçtan Uca En Küçük Akış
| Adım | MVP çözümü | Manuel / daraltılmış mı? |
|---|---|---|

## Kapsam Kararları
| Madde | Karar (Mutlaka/Sonra/Asla) | Gerekçe |
|---|---|---|

## Kalite Tabanı (pazarlık dışı)
- ...

## Ölçümleme
- ...

## Çıkış Kriterleri
| Sinyal | Eşik | Karar |
|---|---|---|

## Kapsam Dışı, Riskler ve Paydaş Notları
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Tek bir birincil kullanıcı ve tek bir iş adlandırıldı; akış bu işi uçtan uca kapsıyor.
- [ ] Her Mutlaka maddesinin işe veya bir öğrenme hedefine bağlı gerekçesi var.
- [ ] Öğrenme hedefleri ölçülebilir ve ölçümleme planlandı.
- [ ] Güvenlik, gizlilik, yasal ve veri bütünlüğü maddeleri kesilmedi, kalite tabanında.
- [ ] Çıkış kriterleri ölçekle / yinele / durdur kararlarını tanımlıyor.
- [ ] Kapasite uyumu yalnızca verilen tahminlere dayanıyor; eksik olanlar `[TBD]`.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Katman katman geliştirmek (tüm backend, kullanılabilir akış yok). Yatayda ince, dikeyde eksiksiz kes.
- MVP'yi "daha az özellikli sürüm 1" sanıp öğrenme hedeflerini atlamak. Yanıtlanacak bir soru yoksa aksiyon alınacak bir sinyal de yoktur.
- Kapsam yerine kaliteyi kesmek. Hatalı bir MVP değer hipotezini değil, hatalara tahammülü test eder.

## Örnek
Girdi: "8 hafta, saha servis planlama uygulaması için 40 maddelik liste."

Çıktıdan bir bölüm:
- Birincil kullanıcı: 10-30 teknisyenli bir firmadaki planlamacı. İş: yarının işlerini teknisyenlere atamak ve teknisyenlerin günlerini görmesini sağlamak.
- Öğrenme hedefi: Planlamacılar art arda 4 hafta boyunca ertesi günü beyaz tahta yerine araçta planlıyor.
| Madde | Karar | Gerekçe |
|---|---|---|
| Rota optimizasyonu | Sonra | Planlamacı bugün işleri elle sıralıyor; öğrenmek için gerekmiyor |
| Teknisyen mobil gün görünümü | Mutlaka | Teknisyenler atamaları göremezse iş başarısız olur |
| Faturalama | Asla (şimdi) | Farklı bir iş; mevcut muhasebe aracı kullanılıyor |
