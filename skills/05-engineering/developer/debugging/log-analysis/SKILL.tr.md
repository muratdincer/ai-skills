---
description: Uygulama, altyapı veya erişim loglarını analiz ederek zaman çizelgesi oluşturur, olayları request veya trace ID ile servisler arasında ilişkilendirir, anomalileri ve hata kümelerini bulur; kanıtın neyi desteklediğini ve neyi desteklemediğini belirtir. Geliştirici bir olay, hata, yavaşlama veya tuhaf davranış çevresindeki log parçalarını ya da dökümlerini paylaşıp ne olduğunu, ne zaman başladığını veya hangi bileşenin sorumlu olduğunu sorduğunda kullanılır.
related: stack-trace-analysis, debugging-hypotheses, incident-response, postmortem, logging-instrumentation
prompt: 14:00 ile 14:20 arasındaki API gateway ve sipariş servisi logları burada. Ödeme akışı hata vermeye başladığında ne oldu?
---

# Log Analizi

## Amaç
Ham log satırlarını kanıta dayalı bir anlatıya dönüştürmek: neyin olduğunu gösteren bir zaman çizelgesi, önce hangi bileşenin bozulduğu, hatanın nasıl yayıldığı ve hangi sonuçların kanıtlanmış, hangilerinin çıkarım olduğu. Çıktı hata ayıklamayı, olay müdahalesini ve postmortem'leri besler.

## Ne zaman kullanılır
- Bir hata penceresi çevresinde bir veya birden fazla servisin logları elde olduğunda.
- Hata oranları veya gecikmeler değiştiğinde ve neden belirsiz olduğunda.
- Tek bir isteğin servisler boyunca izlenmesi gerektiğinde.

## Ne zaman kullanılmaz
- Elde yalnızca stack trace'li tek bir istisna varsa `stack-trace-analysis` kullanılır.
- İleride neyin loglanacağını tasarlamak için `logging-instrumentation` veya `observability-plan` kullanılır.
- Devam eden bir olayı koordine etmek için `incident-response` kullanılır.

## Girdiler
Zorunlu:
- Zaman penceresini kapsayan, zaman damgalı log satırları veya döküm.

İsteğe bağlı, kaliteyi artırır:
- Belirti ve ilk fark edildiği zaman; penceredeki dağıtım, yapılandırma veya trafik değişiklikleri.
- Log şeması (alanlar, seviyeler), her kaynağın saat dilimi, servis topolojisi.
- Karşılaştırma için sağlıklı bir döneme ait referans loglar.

Zaman damgaları veya saat dilimleri belirsizse zaman çizelgesini kurmadan önce varsayımı açıkça yaz. Alıntılanan her satırda kişisel verileri, token'ları ve bireylere ait IP'leri maskele.

## Süreç
1. Normalleştir: tüm zaman damgalarını tek bir saat dilimine (tercihen UTC) çevir, sunucular arası saat kayması riskini not et ve anahtar alanları belirle (seviye, servis, trace/correlation ID, kullanıcı/tenant ID, endpoint, durum kodu, gecikme).
2. Belirti penceresini belirle: hata imzasının ilk ve son görülmesi ve bilinen son sağlıklı an.
3. Mesajları imzaya göre kümele (değişken kısımları çıkarılmış mesaj şablonu) ve dakika başına say; pencerede yeni ortaya çıkan veya oranı değişen imzaları öne çıkar.
4. En erken anomaliyi bul: kullanıcıya görünen hatadan önceki ilk yeni imza, ilk gecikme sıçraması veya ilk kaynak uyarısı (havuz tükenmesi, GC, disk, yeniden denemeler).
5. Kaynakları trace/correlation ID ile veya sıkı zaman hizalamasıyla ilişkilendir; karşılaştırma için bir başarısız ve bir başarılı isteği uçtan uca izle.
6. Yayılımı haritala: yukarı akıştaki neden → aşağı akıştaki belirtiler (timeout'lar, yeniden denemeler, açılan circuit breaker'lar, kuyruk birikmesi). Yükü büyüten yeniden deneme fırtınalarına dikkat et.
7. Eşzamanlı değişiklikleri kontrol et: dağıtımlar, yapılandırma yeniden yüklemeleri, sertifika süre dolumu, zamanlanmış işler, trafik artışları.
8. Kök neden doğrulanmadan düzeltme önerme. Bulguları Doğrulanmış (loglarda doğrudan görülen), Çıkarım (loglarla tutarlı ama kanıtlanmamış) ve Bilinmeyen (kanıt eksik) olarak ayır.
9. Boşlukları listele: eksik alanlar, örneklenmiş veya düşürülmüş loglar, logu olmayan servisler ve sonra neyin toplanacağı.
10. Devret: Çıkarım bulgularını `debugging-hypotheses` ile teste dönüştür; canlı bir olaysa `incident-response`, sonrasında `postmortem` ile devam et; log boşlukları analizi engellediyse `logging-instrumentation` öner.

## Çıktı formatı
```markdown
# Log Analizi: <belirti> (<pencere, saat dilimi>)
## Özet
<3-4 cümle: ne oldu, ilk bozulan bileşen, etki>

## Zaman Çizelgesi
| Zaman (UTC) | Kaynak | Olay | Kanıt (maskelenmiş alıntı) |
|---|---|---|---|

## Hata İmzaları
| İmza | Adet | İlk görülme | Oran değişimi | Servisler |
|---|---|---|---|---|

## Yayılım
<neden> → <etki> → <kullanıcıya görünen belirti>

## Bulgular
- Doğrulanmış: ...
- Çıkarım: ...
- Bilinmeyen: ...

## Sonraki Adımlar ve Eksik Kanıt
- ...
```

## Kalite kontrol listesi
- [ ] Tüm zamanlar belirtilmiş tek bir saat diliminde ve saat kayması varsayımları not edilmiş.
- [ ] Yalnızca en gürültülü hata değil, en erken anomali belirlenmiş.
- [ ] En az bir istek uçtan uca izlenmiş veya correlation ID eksikliği belirtilmiş.
- [ ] Doğrulanmış, çıkarım ve bilinmeyen bulgular açıkça ayrılmış.
- [ ] Alıntılanan log satırlarında kişisel veri ve gizli bilgiler maskelenmiş.
- [ ] Eşzamanlı değişiklikler (dağıtımlar, işler, trafik) kontrol edilmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- En yüksek hacimli hatayı neden saymak. Aşağı akıştaki timeout'lar ve yeniden denemeler çoğu zaman yukarı akıştaki kök nedenden daha gürültülüdür.
- Yerel saat ile UTC zaman damgalarını karıştırmak; bu, zaman çizelgesinin sırasını bozar ve yanlış nedensellik ima eder.
- Örneklenmiş, seviyeye göre filtrelenmiş veya bir servisi eksik loglardan "hata yok" sonucuna varmak. Kapsamı belirt.

## Örnek
Girdi: Gateway ve sipariş servisi logları, 14:00-14:20 UTC; ödeme hataları 14:07'den itibaren bildirilmiş.

Çıktıdan bir bölüm:
- 14:05:12 order-service: ilk `connection pool exhausted (max=20)` uyarısı; pencerede dağıtım yok; gece rapor işi aynı veritabanında 14:05:00'te başladığını loglamış.
- 14:07:03 gateway: `POST /checkout` için 504'ler başlıyor; istek başına 3 yeniden deneme sipariş servisi yükünü üçe katlıyor.
- Doğrulanmış: havuz tükenmesi gateway 504'lerinden önce geliyor. Çıkarım: rapor işi bağlantıları tutuyor. Bilinmeyen: veritabanı tarafındaki kilitler (DB logları verilmedi).
