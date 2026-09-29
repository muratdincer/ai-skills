---
description: Her paydaşın rolünü, ilgisini, etkisini, mevcut ve hedeflenen katılımını, temel kaygılarını ve iletişim ihtiyaçlarını, grup bazında katılım stratejisiyle birlikte listeleyen proje paydaş kaydını oluşturur. Proje başladığında, yeni taraflar katıldığında ya da bir grubun direnci veya sessizliği katılımın bilinçli planlanması gerektiğini gösterdiğinde kullanılır.
related: stakeholder-identification, stakeholder-map, raci-matrix, communication-plan, project-charter
prompt: Üç fabrikaya ERP geçişimiz için paydaş kaydı oluştur; organizasyon şeması ve başlatma belgesi ekte.
---

# Paydaş Kaydı

## Amaç
Projeyi etkileyen veya projeden etkilenen herkesin, katılım açığı ve stratejisiyle birlikte tek ve uygulanabilir bir listesini tutmak; böylece destek oluşturulur ve direnç takvim riskine dönüşmeden yönetilir.

## Ne zaman kullanılır
- Başlatma aşamasında, başlatma belgesi sponsoru ve ana etkilenen grupları belirledikten sonra.
- Organizasyon değişiklikleri, yeni tedarikçiler veya yeni lokasyonlar projeye girdiğinde.
- Bir paydaş grubu ilgisiz veya dirençli olduğunda.

## Ne zaman kullanılmaz
- Yalnızca kimlerin dahil olabileceğine dair ilk beyin fırtınasıysa `stakeholder-identification` kullanılır.
- Çalıştay için görsel güç/ilgi matrisi gerekiyorsa `stakeholder-map` kullanılır.
- Görevlere sorumluluk atanacaksa `raci-matrix` kullanılır.

## Girdiler
Zorunlu:
- Proje özeti (başlatma belgesi veya kapsam) ve dahil olan tarafların listesi ya da tanımı.

İsteğe bağlı, kaliteyi artırır:
- Organizasyon şemaları, bu gruplarla önceki proje deneyimleri, bilinen çatışmalar.
- Sözleşme tarafları, düzenleyiciler, çalışan temsilcileri veya sendikalar.

Hiç taraf verilmemişse en azından sponsoru ve etkilenen birimleri iste.

## Süreç
1. Paydaşları doğru ayrıntıda listele: karar vericiler için kişi, büyük kullanıcı kitleleri için grup.
2. Her biri için projedeki rolünü ve organizasyondaki konumunu kaydet.
3. İlgiyi (ne kazanıyor, ne kaybediyor) ve biliniyorsa kendi ifadeleriyle temel kaygılarını yaz.
4. Etki ve ilgiyi (Yüksek/Orta/Düşük) tek satırlık gerekçeyle puanla.
5. Mevcut katılımı (Habersiz, Dirençli, Tarafsız, Destekleyici, Öncü) ve hedef düzeyi değerlendir.
6. Mevcut düzeyin hedefin altında olduğu ve etkinin Yüksek olduğu açıkları öne çıkar; bunlar önceliklidir.
7. Öncelikli her paydaş için katılım stratejisi tanımla: sahip, aksiyonlar, kanal, sıklık.
8. İletişim planını beslemek için iletişim ihtiyaçlarını (format, ayrıntı, dil, zamanlama) kaydet.
9. Hassas kişisel değerlendirmeleri iç kullanıma özel işaretle; yalnızca işle ilgili bilgiyi tut, kişisel veriyi en aza indir.
10. Kayıt için gözden geçirme sıklığını ve güncellemeyi tetikleyen olayları belirle.
11. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: belirlenen ihtiyaçları karşılamak için `communication-plan` ya da karar yetkilerini netleştirmek için `raci-matrix`.

## Çıktı formatı
```markdown
# Paydaş Kaydı: <proje>
Sürüm <x> | Sahip <PM> | Sonraki gözden geçirme <tarih veya [TBD]> | Sınıf: İç kullanım

| No | Paydaş | Rol / konum | İlgi ve kaygılar | Etki | İlgi | Mevcut | Hedef | Strateji ve sahip | İletişim ihtiyacı |
|---|---|---|---|---|---|---|---|---|---|

## Öncelikli Katılım Açıkları
| Paydaş | Açık | Aksiyonlar | Sahip | Tarih |

## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Etkisi Yüksek her paydaşın bir katılım stratejisi ve sahibi var.
- [ ] Her satırda mevcut ve hedef katılım belirtildi.
- [ ] Puanlar çıplak etiket değil, gerekçeli.
- [ ] Dolaylı paydaşlar (operasyon, destek, denetim, düzenleyiciler) değerlendirildi.
- [ ] Gereksiz kişisel veri veya yargılayıcı dil yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca destekleyen, görünür paydaşları listelemek. Değişiklikten bir şey kaybedenleri ara.
- Kaydı bir kez oluşturup hiç güncellememek. Güncellemeleri kilometre taşlarına ve organizasyon değişikliklerine bağla.
- Açık sözlü değerlendirmeleri geniş paylaşılan bir dokümana yazmak. Hassas notları erişimi kısıtlı tut.

## Örnek
Girdi: "3 fabrikaya ERP geçişi. Fabrika müdürleri şüpheci, finans zorluyor."

Çıktıdan bir bölüm:
| P-04 | Fabrika müdürleri (3) | Operasyon sahipleri | Geçiş sırasında üretim duruşundan endişeli | Y | O | Dirençli | Destekleyici | Ortak geçiş planlaması, fabrikaya özel go/no-go kriterleri – PM | Haftalık 15 dk bilgilendirme, fabrika KPI'ları |
