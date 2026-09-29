---
description: Projenin iç ve dış bağımlılıklarını haritalar; neyin, kimden, ne zamana kadar gerektiğini, sağlayan ve alan sahipleri, taahhüt durumunu, kritikliği ve bağımlılık kayarsa geri dönüş planını belirtir. Proje başka ekiplere, tedarikçilere, platformlara veya kararlara dayandığında ya da kaçırılan devirler kilometre taşlarını tehdit ettiğinde kullanılır.
related: schedule-plan, raid-log, cross-team-dependency-board, risk-register, integration-requirements
prompt: Sadakat programı lansmanımızın tüm bağımlılıklarını haritala: pazarlama, POS tedarikçisi, veri ekibi ve hukuk incelemesi.
---

# Bağımlılık Haritası

## Amaç
Projenin dayandığı her devri açık, sahipli ve tarihli hale getirmek; böylece taahhüt boşlukları ve takvim riski gecikmeye yol açmadan görünür olur ve müzakere edilir.

## Ne zaman kullanılır
- Planlama sırasında, takvim baz çizgisi üzerinde anlaşılmadan önce.
- Proje başka taraflardan teslimat, karar veya ortam beklediğinde.
- Bir bağımlılık kaydığında ve etkisinin değerlendirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Çok sayıda ekip arasında ortak bir oturumda program düzeyinde bağımlılık planlaması için `cross-team-dependency-board` kullanılır.
- Proje içi faaliyet sıralaması için `schedule-plan` kullanılır.
- Teknik arayüz spesifikasyonları için `integration-requirements` kullanılır.

## Girdiler
Zorunlu:
- Proje kapsamı veya plan özeti ve dahil olan taraflar.

İsteğe bağlı, kaliteyi artırır:
- Takvim ve kilometre taşları, sağlayıcılarla sözleşmeler/SLA'lar, organizasyon şemaları.

Taraflar veya plan bilinmiyorsa iste; şüphelenilen bağımlılıkları `[VARSAYIM]` olarak listele.

## Süreç
1. Bağımlılık türlerini tara: diğer ekiplerden teslimatlar, tedarikçi temini, platform/ortam hazırlığı, veri erişimi, kararlar/onaylar, mevzuat veya hukuk incelemeleri, paylaşılan kişiler.
2. Yönü sınıfla: gelen (bizim ihtiyacımız) ve giden (başkalarının bizden ihtiyacı).
3. Her biri için tam öğeyi, sağlayan sahibi, alan sahibi, gereken tarihi ve beslediği kilometre taşını kaydet.
4. Taahhüt durumunu kaydet: Talep edilmedi, Talep edildi, Mutabık, Riskte, Teslim edildi. "Mutabık" yalnızca sağlayıcı teyit ettiyse.
5. Kritikliği değerlendir: kritik yolda mı, ne kadar bolluk var.
6. Geri dönüş planını veya geçici çözümü ve ona geçmek için en geç karar tarihini tanımla.
7. Bağımlılık zincirlerini ve döngüsel bağımlılıkları belirle; tek sağlayıcıda toplanan kümeleri işaretle.
8. Sağlayıcı başına eskalasyon yolunu ve gözden geçirme sıklığını ekle.
9. Riskteki bağımlılıkları risk kaydına veya RAID kaydına aktar.

## Çıktı formatı
```markdown
# Bağımlılık Haritası: <proje>
| No | Yön | Gereken öğe | Sağlayan (sahip) | Alan (sahip) | Gereken tarih | Beslediği kilometre taşı | Durum | Kritik yol? | Geri dönüş | Karar tarihi |
|---|---|---|---|---|---|---|---|---|---|---|
## Kritik ve Riskteki Bağımlılıklar
## Sağlayıcı Yoğunlaşması
| Sağlayıcı | Bağımlılık sayısı | Eskalasyon muhatabı |
## Diyagram (isteğe bağlı)
<sağlayıcılar → teslimatlar → kilometre taşları için metin veya Mermaid akış şeması>
## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her bağımlılık "X ekibinden destek" değil, somut bir öğe adlandırıyor.
- [ ] "Mutabık" durumu yalnızca sağlayıcının teyit ettiği yerlerde.
- [ ] Her kritik bağımlılığın geri dönüş planı ve karar tarihi var.
- [ ] Giden bağımlılıklar da dahil.
- [ ] İsimler ve tarihler uydurulmadı; boşluklar işaretli.

## Sık yapılan hatalar
- Bağımlılıkları sağlayıcının haberi olmadan kaydetmek. Yazılı olarak teyit al.
- Gereken tarihi kullanım tarihine eşit koymak; entegrasyon için tampon kalmaz.
- Karar bağımlılıklarını (onaylar, hukuk onayı) göz ardı etmek; bunlar çoğu zaman en uzun temin süreleridir.

## Örnek
Girdi: "Sadakat lansmanı için POS tedarikçisi güncellemesi, veri ekibinden müşteri verisi ve koşulların hukuk onayı gerekiyor."

Çıktıdan bir bölüm:
| B-01 | Gelen | Sadakat API v2'li POS sürümü | POS tedarikçisi (müşteri yöneticisi) | Entegrasyon sorumlusu | `[TBD]` | UAT başlangıcı | Talep edildi | Evet | 4 hafta boyunca arka ofiste manuel puan girişi | UAT'den 3 hafta önce |
