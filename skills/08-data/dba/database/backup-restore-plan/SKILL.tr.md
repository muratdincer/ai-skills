---
description: "RPO ve RTO'dan türetilmiş bir veritabanı yedekleme ve geri yükleme planı tasarlar: yedek tipleri ve sıklığı (tam, fark/artımlı, log veya sürekli arşivleme, snapshot), saklama ve değiştirilemez/tesis dışı kopyalar, şifreleme ve erişim, her arıza senaryosu için geri yükleme prosedürleri ve kanıt üreten periyodik geri yükleme testi programı. Bir veritabanı için yedekleme kurulurken veya gözden geçirilirken, başarısız ya da yavaş bir geri yüklemeden sonra, denetim kanıtı için veya RPO/RTO hedefleri değiştiğinde kullanılır."
related: "dr-plan, retention-policy, database-health-check, schema-migration-plan, runbook"
prompt: "2 TB'lık sipariş veritabanımız için yedekleme ve geri yükleme planı tasarla: RPO 15 dakika, RTO 2 saat; denetim için aylık yedekleri 1 yıl saklamamız da gerekiyor."
---

# Yedekleme ve Geri Yükleme Planı

## Amaç
Her gerçekçi arızada verinin gereken noktaya ve gereken sürede geri yüklenebileceğini garanti etmek. Bir yedekleme planı başarılı yedek işleriyle değil test edilmiş geri yüklemelerle değerlendirilir.

## Ne zaman kullanılır
- Yeni bir veritabanı üretime çıkıyorsa veya mevcut bir veritabanının belgelenmiş yedekleme tasarımı yoksa.
- RPO/RTO hedefleri belirleniyor veya değişiyorsa ya da bir geri yükleme başarısız olduysa veya beklenenden uzun sürdüyse.
- Denetçiler veya güvenlik ekibi yedek kapsamı, değiştirilemezlik ve geri yükleme testleri için kanıt istiyorsa.

## Ne zaman kullanılmaz
- Hizmetin tamamı için tesis veya bölge failover'ı tasarlanıyorsa `dr-plan` kullanılır; bu skill veritabanı kısmını kapsar.
- Soru iş verisinin ne kadar süre saklanabileceği veya ne zaman silinmesi gerektiğiyse `retention-policy` kullanılır.
- Tek bir geri yükleme için adım adım operasyon prosedürü gerekiyorsa bu plan girdi olarak kullanılıp `runbook` hazırlanır.

## Girdiler
Zorunlu:
- Veritabanı motoru, dağıtım modeli (kendi yönetilen, yönetilen servis, container) ve boyut/büyüme.
- RPO ve RTO hedefleri ya da bunları belirleyebilecek iş sahibi.

İsteğe bağlı:
- Değişim oranı ve log hacmi, mevcut yedekleme araçları, depolama hedefleri, yasal saklama gereksinimleri, şifreleme/anahtar yönetimi, replikasyon topolojisi, bütçe kısıtları.

RPO/RTO bilinmiyorsa uydurma; `[VARSAYIM]` ile işaretli aday seviyeler öner ve karar sahibini açık soru olarak listele.

## Süreç
1. Hedefleri ve kapsamı kaydet: veritabanları, RPO, RTO, gereken geri yükleme ayrıntı düzeyi (tüm instance, tek veritabanı, tablo, zamana dayalı kurtarmayla satır düzeyi) ve veri sınıflandırması. Çıkarılan değerleri `[VARSAYIM]` ile işaretle.
2. Kapsanacak arıza senaryolarını listele: donanım/depolama kaybı, mantıksal bozulma veya hatalı dağıtım, yanlışlıkla silme/güncelleme, fidye yazılımı veya kötü niyetli yönetici, bölge/tesis kaybı, geç fark edilen sessiz bozulma.
3. RPO'yu karşılayan yedek yöntemlerini seç: tam + fark/artımlı sıklığı, transaction log veya WAL/binlog arşivleme sıklığı (dakika düzeyi RPO için sürekli), storage snapshot'ları (uygulama tutarlılığıyla), yönetilen zamana dayalı kurtarma. Replikaların yedek olmadığını not et.
4. RTO'nun karşılanabilirliğini kontrol et: geri yükleme süresini, varsa ölçülmüş hızları kullanarak temel geri yükleme + log uygulama + doğrulama + uygulamanın yeniden bağlanması olarak tahmin et; tahmin RTO'yu aşıyorsa tasarımı değiştir (daha sık tam/fark yedek, snapshot, sıcak yedek sunucu).
5. Saklama katmanlarını ve kopyaları tanımla: operasyonel (kısa, hızlı), uzun dönemli (denetim), en az bir tesis dışı/farklı hesap veya bölge kopyası ve bir değiştirilemez veya mantıksal olarak ayrık (air-gapped) kopya (sezgisel kural olarak 3-2-1-1-0).
6. Yedekleri güvenceye al: durağan ve aktarım halinde şifreleme, yedek depolamadan ayrı anahtar yönetimi, en az yetkili erişim, silme koruması ve yedek silinmesi veya politika değişikliğinde alarm. Kişisel veri içeren yedekler kaynakla aynı gizlilik ve saklama kurallarına tabidir.
7. İzlemeyi tanımla: iş başarısı, süre eğilimi, boyut anomalileri (ani düşüş veya artış), log arşivindeki boşluklar, geri yüklenebilir en son noktanın RPO'ya göre yaşı.
8. Her senaryo için geri yükleme prosedürlerini yaz: mantıksal hatalar için yan bir instance'a zamana dayalı geri yükleme, kayıp için tam geri yükleme, tek tablo kurtarma için kısmi çıkarım; kimin karar verdiğini ve kimin uyguladığını ekle.
9. Geri yükleme testi programını tanımla: katman başına sıklık, rastgele seçim, izole ortama tam geri yükleme, bütünlük kontrolleri (motorun tutarlılık kontrolü, satır sayıları, uygulama duman testi), RTO'ya karşı ölçülen süre ve kaydedilen kanıt.
10. Boşlukları, riskleri, varsayımları ve maliyet etkenlerini (depolama, veri çıkışı, yedek sunucu) listele. Hedef devam ediyorsa hizmetin geneli için `dr-plan`, uygulanabilir geri yükleme adımları için `runbook` veya yasal saklamayla uyum için `retention-policy` öner.

## Çıktı formatı
```markdown
# Yedekleme ve Geri Yükleme Planı: <veritabanı/sistem>
Motor / model: <...> | Boyut / büyüme: <...> | RPO: <...> | RTO: <...> | Sınıflandırma: <...>

## Arıza Senaryoları
| Senaryo | Kurtarma yöntemi | Ulaşılabilir RPO / RTO | Boşluk |
|---|---|---|---|

## Yedekleme Takvimi
| Tip | Sıklık | Pencere | Hedef depolama | Saklama | Değiştirilemez / tesis dışı |
|---|---|---|---|---|---|

## Güvenlik
Şifreleme: <...> | Anahtarlar: <...> | Erişim: <...> | Silme koruması: <...>

## İzleme ve Alarmlar
- <kontrol> – eşik – alıcı

## Geri Yükleme Prosedürleri
| Senaryo | Adımlar (özet) | Karar sahibi | Uygulayan | Tahmini süre |
|---|---|---|---|---|

## Geri Yükleme Testleri
Sıklık: <...> | Kapsam: <...> | Kontroller: <...> | Kanıt: <nerede kaydediliyor>

## Boşluklar, Riskler, Varsayımlar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Listelenen her arıza senaryosunun, RPO/RTO'su hedefle karşılaştırılmış bir kurtarma yöntemi var.
- [ ] RTO karşılanabilirliği yedek süresinden değil geri yükleme + log uygulama + doğrulamadan tahmin edilmiş.
- [ ] Ayrı anahtar ve erişimle en az bir tesis dışı ve bir değiştirilemez veya ayrık kopya var.
- [ ] Replikasyon yedek olarak sayılmamış.
- [ ] Geri yükleme testleri planlı, RTO'ya karşı ölçülüyor ve kanıt üretiyor.
- [ ] Kullanıcının vermediği RPO/RTO veya süreler işaretli; hiçbir şey uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yedek işlerinin başarısını izleyip hiç geri yükleme yapmamak: bozuk, eksik veya anahtarsız açılamayan yedekler ancak bir olay sırasında ortaya çıkar.
- Aynı hesaptaki replikalara veya snapshot'lara güvenmek: hatalı bir silme anında çoğalır, ele geçirilmiş bir yönetici ikisini birden siler.
- Yedekleri kaynak verinin saklama süresinin izin verdiğinden uzun tutmak ve yedekleri bir gizlilik yüküne dönüştürmek.

## Örnek
Girdi: "2 TB sipariş veritabanı, RPO 15 dk, RTO 2 saat, denetim için aylık yedekler 1 yıl saklanacak."

Çıktıdan bir bölüm:
- Yedekler: haftalık tam, günlük fark, 5 dakikada bir ayrı bir hesaba log arşivleme; aylık tam yedek 12 ay boyunca değiştirilemez depolamaya kopyalanır.
- RTO kontrolü: tam geri yükleme ~70 dk + fark ~15 dk + 24 saate kadar değişikliğin log uygulaması ~30 dk `[VARSAYIM: hızı ilk geri yükleme testinde ölç]` → 1 sa 55 dk, 2 saate fazla yakın; 12 saatte bir fark yedek veya sıcak yedek sunucu ekle.
- Geri yükleme testi: aylık olarak rastgele bir noktaya izole ortamda geri yükleme, tutarlılık kontrolü ve sipariş sayısı mutabakatı; süre RTO'ya karşı kaydedilir.
