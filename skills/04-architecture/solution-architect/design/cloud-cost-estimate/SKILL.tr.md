---
description: Bir çözüm tasarımının her bileşenini (hesaplama, depolama, veritabanı, ağ çıkışı, yönetilen servisler, gözlemlenebilirlik, lisanslar) iş yükü sürücülerinden boyutlandırır ve aralıkları, varsayımları ve maliyet düşürme kaldıraçlarıyla şeffaf bir aylık işletim maliyeti tahmini üretir. Bir tasarımın onay için maliyet rakamına ihtiyacı olduğunda, mimari seçenekler maliyetle karşılaştırılırken veya geliştirme öncesinde bulut bütçesi belirlenirken kullanılır.
related: finops-review, capacity-planning, build-vs-buy, solution-architecture-document, budget-proposal
prompt: Bu tasarımın aylık bulut maliyetini tahmin et: 6 konteynerli servis, yönetilen PostgreSQL, Redis, 5 TB doküman için nesne depolama ve ayda yaklaşık 20 milyon API çağrısı.
---

# Tasarımın Bulut Maliyet Tahmini

## Amaç
Karar vericilere, satır satır iş yükü sürücülerine ve varsayımlara izlenebilen aylık bir işletim maliyeti tahmini sunmak. Böylece tahmin sorgulanabilir, iyileştirilebilir ve sonradan gerçek harcamayla karşılaştırılabilir.

## Ne zaman kullanılır
- Bir çözüm tasarımı onay veya iş gerekçesi için işletim maliyeti rakamına ihtiyaç duyduğunda.
- İki mimari seçenek maliyet açısından karşılaştırılacaksa.
- Geliştirme veya göç öncesinde bütçe ya da maliyet sınırı belirlenecekse.

## Ne zaman kullanılmaz
- Çalışan bir sistemin gerçek harcaması analiz edilip optimize edilecekse `finops-review` kullanılır.
- Soru zaman içinde ne kadar kapasite gerektiğiyse önce `capacity-planning` kullanılır, sonra burada fiyatlandırılır.
- Geliştirme eforu dahil tam bir kaynak seçimi kararı için `build-vs-buy` kullanılır.

## Girdiler
Zorunlu:
- Mimari bileşenler (konteynerler, veri depoları, yönetilen servisler) ve hedef bulut veya barındırma modeli.
- İş yükü sürücüleri: kullanıcı/istek, veri hacmi ve büyüme ya da bunların `[VARSAYIM]` olarak belirtilmesine izin.

İsteğe bağlı:
- Bölge, erişilebilirlik hedefleri (çoklu AZ, çoklu bölge, DR), ortamlar (dev/test/stage/prod).
- Fiyatlandırma modeli kısıtları (talebe bağlı, taahhütler, kurumsal indirimler), mevcut ortak platform maliyetleri.
- Para birimi ve kur varsayımı.

Bileşenler veya iş yükü sürücüleri yoksa sor. Birim fiyatları asla hafızadan olgu gibi verme: kullanıcının verdiği fiyatları veya sağlayıcının fiyat hesaplayıcısını kullan, doğrulanmamış fiyatları `[DOĞRULANACAK]` olarak işaretle.

## Süreç
1. Ortam bazında maliyet doğuran bileşenleri listele; tasarımlarda unutulanlar dahil: yük dengeleyiciler, NAT/ağ geçitleri, çıkış trafiği, log/metrik/trace, yedekler ve anlık görüntüler, secret/anahtar yönetimi, CI çalıştırıcıları, DR kopyaları.
2. İş yükü sürücülerini ve varsayımları tek tabloda tanımla: istek hızı (ortalama ve tepe), depolanan veri ve büyüme, dışarı aktarılan veri, üretim dışı ortamların aktif saatleri.
3. Her bileşeni boyutlandır: instance sınıfı ve sayısı (tepe yük, pay ve HA'ya göre), depolama katmanı ve hacmi, IOPS/throughput, yönetilen servis katmanları.
4. Her satırı miktar × birim fiyat olarak fiyatlandır; birim fiyatın kaynağı ve tarihi kullanıcıdan gelsin ya da `[DOĞRULANACAK]` olsun.
5. En belirsiz sürücüleri (genellikle trafik, çıkış, log hacmi) değiştirerek düşük / beklenen / yüksek tahminler üret.
6. Üretim dışı ortamları (küçültülmüş, mesai dışında kapatılan) ve DR duruşunun maliyetini açıkça ekle.
7. İlk 3-5 maliyet sürücüsünü ve duyarlılıklarını belirle (sürücü birimi başına maliyet, ör. milyon istek veya TB başına).
8. Maliyet kaldıraçlarını listele: taahhüt/rezerve kapasite, otomatik ölçekleme ve sıfıra ölçekleme, depolama yaşam döngüsü katmanları, log örnekleme/saklama, önbellek/CDN ile çıkıştan kaçınma, yük testi sonrası doğru boyutlandırma.
9. Hariç tutulanları (personel, destek planları, lisanslar, vergiler) ve sonradan izlenecek birim maliyet KPI'ını (ör. sipariş başı maliyet) belirt.
10. Hedef devam ediyorsa canlıya geçişten sonra `finops-review`, büyüme için `capacity-planning` veya fon talebi için `budget-proposal` öner.

## Çıktı formatı
```markdown
# Bulut Maliyet Tahmini: <çözüm> (<sağlayıcı/bölge>, <para birimi>/ay)
## İş Yükü Sürücüleri ve Varsayımlar
| Sürücü | Değer | Kaynak |
|---|---|---|
## Maliyet Satırları
| Ortam | Bileşen | Boyut | Miktar | Birim fiyat (kaynak) | Aylık |
|---|---|---|---|---|---|
## Özet
| Senaryo | Prod | Prod dışı | DR | Toplam |
|---|---|---|---|---|
| Düşük / Beklenen / Yüksek | | | | |
## Başlıca Maliyet Sürücüleri ve Duyarlılık
## Maliyet Kaldıraçları
## Hariç Tutulanlar
## Birim Maliyet KPI'ı
## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her maliyet satırı bir sürücüye ve bir boyutlandırma kararına izlenebiliyor.
- [ ] Birim fiyatlar kullanıcıdan geliyor veya `[DOĞRULANACAK]` olarak işaretli; hiçbiri hafızadan kesin bilgi gibi sunulmadı.
- [ ] Çıkış trafiği, gözlemlenebilirlik, yedekler ve üretim dışı ortamlar dahil edildi ya da açıkça hariç tutuldu.
- [ ] Tek ve kesin görünen bir rakam yerine aralık (düşük/beklenen/yüksek) verildi.
- [ ] Hariç tutulanlar ve birim maliyet KPI'ı belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ortalama yüke göre boyutlandırıp HA çiftlerini ve tepe payını unutmak.
- Konuşkan veya yoğun log üreten sistemlerde çoğu zaman hesaplamayla yarışan gözlemlenebilirlik ve çıkış maliyetini yok saymak.
- Sahte kesinlik: tahmini trafikle üretilmiş bir rakama iki ondalık basamak yazmak. Yuvarla ve aralığı göster.

## Örnek
Girdi: "6 konteyner servis, yönetilen PostgreSQL, Redis, 5 TB nesne depolama, ayda ~20M API çağrısı."

Çıktıdan bir bölüm:
| Ortam | Bileşen | Boyut | Aylık |
|---|---|---|---|
| Prod | Konteyner hesaplama | 6 servis × 2 replika, `[VARSAYIM: her biri 0,5 vCPU/1 GB]`, çoklu AZ | `[birim fiyat DOĞRULANACAK]` |
| Prod | Nesne depolama | 5 TB standart, `[VARSAYIM: %30'u 90 gün sonra seyrek erişim katmanına geçer]` | ... |
| Prod | Loglar | `[VARSAYIM: istek başı 2 KB]` × 20M = ayda ~40 GB alım | ... |

En büyük sürücü: yönetilen PostgreSQL HA instance'ı; duyarlılık: yük testi sonrası bir boy küçüğe geçmek toplamı `[fiyatlar doğrulandıktan sonra hesaplanacak]` kadar değiştirir.
