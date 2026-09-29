---
description: "Belirli bir servis için risk, durum tutma, veritabanı değişiklikleri, trafik kontrolü, maliyet ve geri dönüş hızını tartarak bir dağıtım stratejisi (recreate, rolling, blue-green, canary, shadow, feature flag veya bunların birleşimi) önerir. Bir sürümün kullanıcıya nasıl ulaşacağına karar verilirken ya da mevcut sürümler kesintiye veya riskli toplu geçişlere yol açıyorsa kullanılır."
related: "pipeline-design, rollback-plan, release-plan, schema-migration-plan, slo-definition"
prompt: "Ödeme servisimizi 20 dakikalık bakım penceresiyle dağıtıyoruz. Kesintisiz dağıtım için hangi stratejiye geçmeliyiz?"
---

# Dağıtım Stratejisi Seçme

## Amaç
Servisin risk ve kısıtlarına uyan, açık terfi kriterleri ve geri dönüş yolu olan bir yayılım mekanizması seçmek; böylece sürümler ya hep ya hiç olayları olmaktan çıkar.

## Ne zaman kullanılır
- Bir servis bakım pencerelerinden kesintisiz sürümlere geçerken.
- Yüksek riskli bir değişikliğin kademeli olarak açılması gerektiğinde.
- Ekip blue-green, canary ve feature flag arasında karar veremiyorsa.

## Ne zaman kullanılmaz
- Tüm hattın tasarlanması gerekiyorsa `pipeline-design` kullanılır.
- Belirli bir sürümün nasıl geri alınacağı soruluyorsa `rollback-plan` kullanılır.
- Çok ekipli bir sürümün sıralaması konuşuluyorsa `release-plan` kullanılır.

## Girdiler
Zorunlu:
- Servis tanımı: çalışma platformu, durum tutma, trafik girişi (load balancer, gateway, mesh, istemci uygulamalar), veritabanı bağımlılığı.
- İş toleransı: sürüm sırasında kabul edilebilir kesinti ve kullanıcıya görünen hata payı.

İsteğe bağlı, kaliteyi artırır:
- Trafik hacmi (canary'nin istatistiksel anlamı için gerekli), SLO'lar, mevcut metrikler.
- Altyapı bütçesi (blue-green kapasiteyi geçici olarak iki katına çıkarır).
- Mevcut feature flag altyapısı, oturum yönetimi, API ve şemanın geriye uyumluluğu.

Platform veya kesinti toleransı bilinmiyorsa sor. Diğer eksikler açık soru olur.

## Süreç
1. Kısıtları netleştir: iki sürüm aynı anda çalışabilir mi? API ve veritabanı şeması geriye uyumlu mu? Yapışkan oturumlar, uzun ömürlü bağlantılar, arka plan tüketicileri veya tekil işler var mı?
2. İki sürüm bir arada çalışamıyorsa önce şema ve API değişiklikleri için expand-and-contract planla; aksi halde yalnızca recreate güvenlidir.
3. Adayları şu ölçütlerle değerlendir: kesinti, etki alanı, geri dönüş süresi, altyapı maliyeti, trafik kontrolü ihtiyacı, gözlemlenebilirlik ihtiyacı, operasyonel karmaşıklık.
4. Canary uygulanabilirliğini kontrol et: adım süresi içinde bir gerilemeyi yakalayacak kadar trafik var mı; sürüm bazında metrik alınabiliyor mu.
5. Dağıtımı yayından ayır: kullanıcı erişimini binary'lerden bağımsız olarak feature flag'lerle yönetip yönetmeyeceğine karar ver.
6. Terfi adımlarını (ör. %1 → %10 → %50 → %100) süre ve otomatik analiz kriterleriyle (hata oranı, gecikme yüzdelikleri, doygunluk, iş KPI'ı) tanımla.
7. Her strateji için durdurma kriterlerini ve rollback mekanizmasını (trafik geçişi, rollout geri alma, flag kapatma) tanımla.
8. Durum tutan parçaları ele al: kuyruk tüketicileri, zamanlanmış işler, önbellekler, migration'lar; iki sürümün birlikte çalıştığı sürede bunları kimin çalıştıracağını yaz.
9. Gerekçesi ve kurulması gereken ön koşullarıyla tek bir strateji (veya birleşim) öner.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa ayrıntılı geri dönüş yolu için `rollback-plan`, sürümün sıralaması için `release-plan` veya terfi kriterlerinde üzerinde anlaşılmış SLO yoksa `slo-definition` öner.

## Çıktı formatı
```markdown
# Dağıtım Stratejisi: <servis>
## Kısıtlar
- Sürümlerin bir arada çalışması: evet/hayır – gerekçe
- Şema/API uyumluluğu: ...
## Karşılaştırılan Seçenekler
| Strateji | Kesinti | Etki alanı | Geri dönüş süresi | Ek maliyet | Ön koşullar | Uygunluk |
## Öneri
<strateji>, çünkü ...
## Yayılım Adımları
| Adım | Açılma oranı | Süre | Terfi koşulu | Durdurma koşulu |
## Rollback Mekanizması
## Bir Arada Çalışma Süresince Durum Tutan Bileşenler
## Ön Koşullar / Açık Sorular
```

## Kalite kontrol listesi
- [ ] Recreate dışı bir strateji önerilmeden önce sürüm birlikteliği ve şema uyumluluğu kontrol edildi.
- [ ] Terfi ve durdurma kriterleri eşikli ya da `[TBD]` işaretli metriklere dayanıyor.
- [ ] Canary yalnızca trafik anlamlı karşılaştırmaya izin veriyorsa önerildi.
- [ ] Yalnızca HTTP trafiği değil, arka plan işleri ve tüketiciler de ele alındı.
- [ ] Çift kapasitenin maliyet etkisi uydurma rakam olmadan nitel olarak belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kırıcı bir migration ile tek bir veritabanını paylaşırken blue-green seçmek. Önce expand-and-contract uygula.
- %1'in birkaç istek anlamına geldiği düşük trafikte canary. Daha uzun adımlar veya sentetik trafik kullan.
- Feature flag veya veri migration'ı durumu değiştirmişken yalnızca binary'yi geri almak. İkisini birlikte planla.

## Örnek
Girdi: "Ingress arkasında Kubernetes üzerinde ödeme API'si, ~300 rps, bugün 20 dakikalık bakım penceresi, birkaç sürümde bir şema değişikliği."

Çıktıdan bir bölüm:
- Öneri: ağırlıklı yönlendirme ile canary; expand-and-contract migration'lar ve yeni ödeme yöntemleri için feature flag'lerle birlikte.
- Adım 1: 15 dk boyunca %5; canary'nin 5xx oranı ve p99 gecikmesi stable'dan `[TBD]` fazlasıyla kötü değilse terfi et; herhangi bir ödeme yetkilendirme hatası sıçramasında durdur.
