---
description: "Canlı bir sistemde sıfır veya asgari kesintiyle veritabanı şema geçişi planlar: her DDL'in kilit ve yeniden yazma davranışını değerlendirir, kırıcı değişiklikleri uygulama sürümleriyle hizalı expand-migrate-contract adımlarına böler, parçalı backfill tasarlar ve doğrulama, geri dönüş ile geri dönüşü olmayan noktayı tanımlar. Üretim veritabanlarında sütun, tablo, kısıt veya indeks eklenirken, yeniden adlandırılırken, tipi değiştirilirken veya silinirken ya da bir geçiş betiği yayından önce güvenlik incelemesine ihtiyaç duyduğunda kullanılır."
related: "schema-evolution-plan, index-recommendation, backup-restore-plan, deployment-strategy, rollback-plan"
prompt: "90 milyon satırlık bir PostgreSQL tablosunda customers.full_name sütununu kesinti olmadan first_name ve last_name olarak bölmemiz gerekiyor. Geçiş planını yaz."
---

# Şema Geçiş Planı

## Amaç
Üretim veritabanı şemasını kesinti, veri kaybı veya engellenmiş bir yayın olmadan değiştirmek. Plan DDL, backfill ve uygulama dağıtımlarını her adımda hem eski hem yeni uygulama sürümünün çalışacağı şekilde sıralar ve nasıl geri dönüleceğini tam olarak söyler.

## Ne zaman kullanılır
- Canlı ve büyük bir tabloda bir sütun, tablo, kısıt, indeks veya veri tipi değişecekse.
- Uygulama trafiğe hizmet vermeye devam ederken yeniden adlandırma, bölme, birleştirme veya tip değişikliği yapılacaksa.
- Bir geçiş betiği yazılmışsa ve yayından önce kilit/süre/geri dönüş incelemesi gerekiyorsa.

## Ne zaman kullanılmaz
- Değişiklik başka ekiplerin tükettiği paylaşılan veri setlerini veya olay akışlarını etkiliyorsa `schema-evolution-plan` kullanılır.
- Yalnızca indeks seti yeniden tasarlanıyorsa `index-recommendation` kullanılır; uygulamak için ardından bu skill kullanılır.
- Yeni şemanın kendisi tasarlanıyorsa `database-schema-design` kullanılır.

## Girdiler
Zorunlu:
- Veritabanı motoru ve sürüm ailesi, etkilenen nesnelerin mevcut ve hedef şeması.
- Etkilenen tabloların boyutları ve trafik profili (satır sayısı, yazma oranı, yoğun saatler).

İsteğe bağlı:
- Kullanılan geçiş aracı, replikasyon/failover yapısı, uygulama yayın süreci, bakım pencereleri, yedek durumu, kilit zaman aşımı politikaları.

Motor bilinmiyorsa sor; DDL'lerin kilit davranışı motorlar ve sürümler arasında temelden farklıdır. Emin olmadığın motor davranışlarını `[VARSAYIM]` ile işaretle.

## Süreç
1. Her şema değişikliğini listele ve sınıfla: eklemeli (yeni null olabilen sütun, yeni tablo), kısıt/indeks, yeniden yazmaya yol açan (tip değişikliği, bazı varsayılanlar, sütun sırası) veya yıkıcı (silme, yeniden adlandırma, daraltma).
2. Her DDL için motor davranışını değerlendir: kilit seviyesi ve süresi, tam tablo yeniden yazma mı yoksa yalnızca metadata mı, online seçeneğin varlığı, replikasyon gecikmesine etkisi ve uzun süren işlemlerin arkasında bekleyip beklemediği (kilit kuyruğu yığılması).
3. Kırıcı değişiklikleri expand-migrate-contract adımlarına böl: yeni yapıyı ekle, uygulamadan (veya trigger ile) çift yaz, tarihçeyi backfill et, okumaları geçir, eski yapıya yazmayı durdur, sonraki bir sürümde sil.
4. Adımları uygulama sürümleriyle hizala: hangi uygulama sürümü hangi şema durumuyla uyumlu; her adım hem önceki hem sonraki uygulama sürümüyle çalışmalı.
5. Backfill'i tasarla: anahtar aralığına göre parçalı, parça boyutu ve bekleme, replikasyon gecikmesi ve yüke göre kısma, idempotent ve kaldığı yerden devam edebilir, yoğun olmayan saatlere planlı, ilerleme takibi olan.
6. Kısıtları güvenli hale getir: önce doğrulanmamış/geçersiz olarak ekle, sonra ayrıca doğrula; indeksleri online/concurrent seçeneklerle oluştur; DDL'in trafiği bloklamak yerine hızlı başarısız olması için kilit zaman aşımı ve yeniden deneme ayarla.
7. Her adım için doğrulamayı tanımla: satır sayıları, yeni sütunlarda null kontrolleri, örneklem ve toplamlar üzerinde eski-yeni değer karşılaştırması, kısıt doğrulaması, uygulama hata oranları ve gecikme.
8. Her adım için geri dönüşü ve geri dönüşü olmayan noktayı (genellikle eski yapıların silinmesi veya geri alınamaz veri dönüşümü) tanımla; öncesinde doğrulanmış bir yedek veya geri yükleme noktası şart koş.
9. Runbook'u yaz: sıra, sorumlu, beklenen süre, go/no-go kriterleri, uygulama sırasında izleme (kilitler, replikasyon gecikmesi, hatalar), iletişim.
10. Riskleri, varsayımları ve açık soruları listele. Hedef devam ediyorsa geri yükleme noktası için `backup-restore-plan`, uygulama tarafı için `deployment-strategy` veya `rollback-plan` öner.

## Çıktı formatı
```markdown
# Şema Geçiş Planı: <değişiklik>
Motor: <...> | Tablolar: <ad – satır – yazma oranı> | Kesinti hedefi: <sıfır / pencere>

## Değişiklik Sınıflandırması
| Değişiklik | Tür | Kilit / yeniden yazma | Online seçenek | Risk |
|---|---|---|---|---|

## Adımlar
| # | Adım | Uygulama sürümü | Tahmini süre | Doğrulama | Geri dönüş |
|---|---|---|---|---|---|
Geri dönüşü olmayan nokta: adım <n> – ön koşul: <doğrulanmış yedek/geri yükleme noktası>

## Backfill
Parçalama: <anahtar aralığı, boyut, bekleme> | Kısma: <gecikme/yük eşiği> | Devam edebilirlik: <nasıl>

## Güvenlik Ayarları
Kilit zaman aşımı: <...> | Komut zaman aşımı: <...> | Yeniden deneme: <...>

## İzleme ve Go/No-Go
- İzle: <kilitler, replikasyon gecikmesi, hata oranı, gecikme>
- Şu durumda durdur: <...>

## Riskler, Varsayımlar, Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her DDL için belirtilen motorda kilit seviyesi, yeniden yazma davranışı ve süre riski yazılmış.
- [ ] Her adım hem önceki hem sonraki uygulama sürümüyle uyumlu.
- [ ] Backfill parçalı, kısılabilir, idempotent ve kaldığı yerden devam edebilir.
- [ ] Her adımın doğrulaması ve geri dönüşü var; geri dönüşü olmayan noktanın doğrulanmış bir geri yükleme noktası var.
- [ ] Kilit zaman aşımları, DDL'in uzun işlemlerin arkasında kuyruğa girip trafiği bloklamasını önlüyor.
- [ ] Doğrulanmamış motor davranışları `[VARSAYIM]` ile işaretli; süreler uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bir sütunu, onu kullanmayı bırakan sürümle aynı yayında yeniden adlandırmak veya silmek; eski sürümün çalışan örnekleri anında hata verir.
- "Hızlı" bir DDL'in uzun bir işlemin arkasında beklemesi ve tüm yeni sorguların onun arkasında kuyruğa girmesi; her zaman kilit zaman aşımı ayarla.
- Backfill'i tek işlemde yapmak: devasa undo/log hacmi, replikasyon gecikmesi ve güncelleme kadar uzun süren bir geri alma.

## Örnek
Girdi: "customers.full_name'i first_name, last_name olarak böl; PostgreSQL, 90M satır, saniyede 800 yazma."

Çıktıdan bir bölüm:
- Adım 1: `lock_timeout = 3s` ve yeniden denemeyle null olabilen `first_name`, `last_name` ekle (yalnızca metadata).
- Adım 2: uygulama v2 eski ve yeni sütunlara birlikte yazar; okumalar hâlâ `full_name`'den.
- Adım 3: 10 bin satırlık anahtar parçalarıyla backfill, replika gecikmesi > 5 sn olursa bekle; tek kelimelik isimler için bölme kuralı `[TBD: iş kararı]`.
- Adım 4: uygulama v3 yeni sütunları okur; Adım 5 (geri dönüşü olmayan nokta, doğrulanmış snapshot sonrası): `full_name` sonraki bir yayında silinir.
