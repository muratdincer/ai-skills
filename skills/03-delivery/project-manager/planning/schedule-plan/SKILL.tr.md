---
name: schedule-plan
description: "İş paketlerini bağımlılık türleri ve gecikmeleriyle sıralayarak, süreleri atayarak, kilometre taşlarını belirleyerek, kritik yolu ve bolluğu hesaplayarak ve takvim tamponları ekleyerek proje takvimi oluşturur. WBS ve tahminler hazır olduğunda baz takvim, kritik yol veya gerçekçi bir bitiş tarihi üretilmesi ya da kontrol edilmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: planning
  title: "Proje takvimi oluşturma"
  related: "wbs, estimation-three-point, dependency-map, resource-plan, release-planning"
  prompt: "Bu iş paketleri ve sürelerden bir takvim oluştur ve Haziran canlıya geçişine giden kritik yolu göster."
---

# Proje Takvimi Oluşturma

## Amaç
Kritik yolu, bolluğu ve kilometre taşlarını gösteren, bağımlılıklara dayalı gerçekçi bir zaman çizelgesi üretmek; böylece bitiş tarihi temenniyle değil işin kendisinden türetilir.

## Ne zaman kullanılır
- WBS ve tahminler hazır olduktan sonra takvim baz çizgisini oluşturmak için.
- Sabit bir tarih verildiğinde ve fizibilitesinin test edilmesi gerektiğinde.
- Bir gecikme yaşandığında ve kilometre taşlarına etkisinin yeniden hesaplanması gerektiğinde.

## Ne zaman kullanılmaz
- İterasyonlar arasında sürüm içeriği planlaması için `release-planning` kullanılır.
- Verim verisinden olasılıksal tarih öngörüsü için `monte-carlo-forecast` kullanılır.
- Yalnızca kimin kime bağımlı olduğunu haritalamak için `dependency-map` kullanılır.

## Girdiler
Zorunlu:
- Süre tahminleriyle iş paketleri veya faaliyetler.
- Bilinen bağımlılıklar ya da bunları çıkarmaya yetecek açıklama (çıkarılanlar `[VARSAYIM]` olarak işaretlenir).

İsteğe bağlı, kaliteyi artırır:
- Başlangıç tarihi, takvimler ve tatiller, sabit kilometre taşları, kaynak kısıtları, üç noktalı tahminler.

Faaliyetler veya süreler eksikse iste. Süre uydurma.

## Süreç
1. İş paketlerini faaliyetlere dönüştür; her faaliyette tek bir sahip ve süre olsun.
2. Bağımlılıkları tür (FS, SS, FF, SF) ve öne alma/gecikme ile tanımla; FS'yi tercih et, diğerlerini gerekçelendir. Zorunlu mantığı (teknik) tercihe dayalı mantıktan ayır.
3. Kararlar, geçiş kapıları, dış teslimatlar ve canlıya geçiş için kilometre taşları (sıfır süreli) ekle.
4. Takvimleri uygula: iş günleri, tatiller, dondurma dönemleri, tedarikçi temin süreleri.
5. İleri ve geri geçiş yap; en erken/en geç başlangıç ve bitişi ile toplam bolluğu hesapla.
6. Kritik yolu (yolları) ve kritiğe yakın faaliyetleri (bolluk ≤ 5 iş günü, ayarlanabilir) belirle.
7. Kritik yoldaki kaynak çakışmalarını kontrol et; dengeleme gerekiyorsa tarih etkisini not et.
8. Her görevi şişirmek yerine tahmin belirsizliğine göre boyutlandırılmış açık tamponlar (proje veya besleme tamponu) ekle.
9. Hedef tarih kaçıyorsa sıkıştırma seçenekleri öner: hızlı izleme (fast-tracking, risk) ve kaynak ekleme (crashing, maliyet), ödünleşimleriyle.
10. Kilometre taşı tablosunu, kritik yol özetini ve temel takvim risklerini üret.
11. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: takvimi kapasiteyle sınamak için `resource-plan` ya da dış bağımlılıklar için `dependency-map`.

## Çıktı formatı
```markdown
# Proje Takvimi: <proje>
Başlangıç <tarih> | Takvim <iş günleri, tatiller> | Baz v<x>
## Faaliyetler
| No | Faaliyet | Sahip | Süre | Öncüller (tür+gecikme) | EB | EBit | GB | GBit | Bolluk |
## Kilometre Taşları
| Kilometre taşı | Planlanan tarih | Tür (kapı/dış/canlı) |
## Kritik Yol
<No → No → No>, toplam süre <x>
## Kritiğe Yakın Faaliyetler
## Tamponlar
## Sıkıştırma Seçenekleri (hedef kaçıyorsa)
| Seçenek | Faaliyetler | Kazanılan gün | Maliyet / risk |
## Takvim Riskleri ve Varsayımlar
```

## Kalite kontrol listesi
- [ ] Başlangıç/bitiş dışında her faaliyetin bir öncülü ve ardılı var (sarkan görev yok).
- [ ] Gerçek kısıtlar dışında sabit tarih yok; kısıtlar listelendi.
- [ ] Kritik yol gösterildi ve açıklandı.
- [ ] Çıkarılan bağımlılıklar ve süreler `[VARSAYIM]` olarak işaretli.
- [ ] Tamponlar faaliyet sürelerine gizlenmedi, açıkça gösterildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Dayatılan tarihten geriye doğru planlayıp buna plan demek. Tarihi türet, sonra karşılaştır.
- Kaynak kısıtlarını yok saymak; kritik yol olduğundan kısa görünür.
- Dış temin sürelerini unutmak (satın alma, güvenlik onayları, ortam hazırlığı).

## Örnek
Girdi: "Tasarım 10g, tasarımdan sonra geliştirme 25g, geliştirmeden sonra test 15g, geliştirmeyle birlikte başlayan veri taşıma 20g, test ve taşımadan sonra canlıya geçiş."

Çıktıdan bir bölüm:
- Kritik yol: Tasarım → Geliştirme → Test → Canlıya geçiş = 50 iş günü.
- Veri taşıma bolluğu: 20 gün (geliştirmeyle SS, canlıdan önce bitmeli).
- Risk: test ortamı hazırlık süresi `[BİLİNMİYOR]` kritik yol üzerinde.
