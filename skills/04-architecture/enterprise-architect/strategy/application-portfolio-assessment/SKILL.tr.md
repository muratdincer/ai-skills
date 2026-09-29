---
name: application-portfolio-assessment
description: "Uygulama portföyünü iş uygunluğu ve teknik uygunluk açısından değerlendirir; her uygulamaya gerekçe, maliyet ve risk sinyalleriyle bir TIME kararı (Tolere et, Yatırım yap, Taşı, Kaldır) ve sıralanmış bir sadeleştirme planı atar. Uygulama sadeleştirmesinde, bütçe döneminde, bulut veya ERP programlarının planlanmasında ya da birleşme sonrası çakışan sistemler olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: enterprise-architect
  area: strategy
  title: "Uygulama portföyü değerlendirmesi"
  related: "capability-map, modernization-assessment, tech-debt-assessment, build-vs-buy, target-state-architecture"
  prompt: "Sahipleri, maliyetleri ve kullanıcı sayılarıyla 40 uygulamalık listemiz ekte; bunları TIME ile sınıflandır ve önce hangilerini kaldırmamız gerektiğini öner."
---

# Uygulama Portföyü Değerlendirmesi

## Amaç
Her uygulama için kanıta dayalı bir karar üreterek yönetimin harcamayı mükerrer veya zayıf sistemlerden işi farklılaştıran sistemlere kaydırmasını sağlamak.

## Ne zaman kullanılır
- Bütçe planlaması veya maliyet düşürme hedefleri uygulama işletim maliyetini hedef aldığında.
- Birleşme, bölünme ya da ERP/bulut programı çakışan uygulamalar bıraktığında.
- Güvenlik veya destek sonu riskinin tüm envanter genelinde ölçülmesi gerektiğinde.
- Yetkinlik haritası mükerrerlik gösterdiğinde ve uygulama düzeyinde karar gerektiğinde.

## Ne zaman kullanılmaz
- Tek bir eski sistem için ayrıntılı modernizasyon yolu gerekiyorsa `modernization-assessment` kullanılır.
- Soru tek bir değiştirme kararıysa `build-vs-buy` kullanılır.
- Tek sistem içindeki kod düzeyinde borç için `tech-debt-assessment` kullanılır.

## Girdiler
Zorunlu:
- Uygulama envanteri: ad, amaç, sahip, desteklediği yetkinlik veya süreç.
- İş değeri veya kullanım için bir ölçü (kullanıcı, işlem, kritiklik).

İsteğe bağlı:
- Yıllık işletim maliyeti (lisans, altyapı, destek), olay sayıları, değişiklik sıklığı.
- Teknoloji yığını, üretici destek tarihleri, güvenlik bulguları.
- Yetkinlik haritası ve stratejik öncelikler.

Envanter yoksa iste. Maliyet veya tarih uydurma; `[BİLİNMİYOR]` olarak işaretle ve güven düzeyini düşür.

## Süreç
1. Envanteri normalleştir: dağıtılabilir her uygulama için bir satır; takma adları birleştir; gölge BT'yi ve SaaS'ı açıkça işaretle.
2. Puanlamadan önce ağırlıklı ölçütleri tanımla. İş uygunluğu: yetkinlik kapsamı, kullanıcı memnuniyeti, stratejik uyum, yasal gereklilik. Teknik uygunluk: desteklenebilirlik (destek sonu tarihleri), mimari kalite, güvenlik durumu, işletilebilirlik, yetkinlik bulunabilirliği.
3. Her uygulamayı ölçüt başına 1-5 puanla; kanıtı ve güven düzeyini (Yüksek/Orta/Düşük) kaydet.
4. TIME dörtlüsüne yerleştir: yüksek iş/yüksek teknik = Yatırım; yüksek iş/düşük teknik = Taşı; düşük iş/yüksek teknik = Tolere et; düşük/düşük = Kaldır.
5. Maliyet ve riski ekle: düşük değerli yüksek maliyet, 18 ay içinde destek sonu, kritik açıklar, tek kişiye bağlı bilgi.
6. Mükerrerleri görmek için yetkinliğe göre grupla; her mükerrer küme için gerekçesiyle kalacak uygulamayı seç.
7. Her Kaldır veya Taşı kararından önce bağımlılıkları ve veri sahipliğini kontrol et: arayüzler, raporlar, arşivler ve saklama yükümlülükleri.
8. Planı dalgalara böl: hızlı kazanımlar (az bağımlı kaldırmalar), risk kaynaklı taşımalar, stratejik yatırımlar.
9. Etkiyi yalnızca nitel olarak ya da verilen rakamlarla tahmin et; tasarruf uydurma.
10. Sahiplerden beklenen kararları ve güveni düşüren veri boşluklarını listele.
11. Sahiplerden gelen verilerle kendi çıkarımlarını ayır, her çıkarımsal puanı `[VARSAYIM]` olarak işaretle; hedef devam ediyorsa Taşı adayları için `modernization-assessment`, yenileme için `build-vs-buy` veya `target-state-architecture` öner.

## Çıktı formatı
```markdown
# Uygulama Portföyü Değerlendirmesi – <kapsam>
Ölçütler ve ağırlıklar: <tablo> · Veri tarihi: <tarih>

## Portföy Özeti
| Karar | Adet | Bilinen işletim maliyetindeki payı |

## Uygulama Değerlendirmeleri
| Uygulama | Yetkinlik | Sahip | İş uygunluğu | Teknik uygunluk | TIME | Ana risk | Güven | Gerekçe |
|---|---|---|---|---|---|---|---|---|

## Mükerrer Kümeler
| Yetkinlik | Uygulamalar | Kalacak uygulama | Neden |

## Sadeleştirme Yol Haritası
| Dalga | Uygulamalar | Aksiyon | Bağımlılıklar | Sorumlu |

## Veri Boşlukları ve Beklenen Kararlar
```

## Kalite kontrol listesi
- [ ] Ölçütler ve ağırlıklar puanlamadan önce sabitlendi.
- [ ] Her puanın kanıtı veya güven işareti var.
- [ ] Her Kaldır/Taşı kararında bağımlılıklar, veri saklama ve arşiv ihtiyacı kontrol edildi.
- [ ] Mükerrer kümelerde kalacak uygulama ve gerekçesi belirtildi.
- [ ] Hiçbir maliyet, tasarruf veya tarih uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- En yüksek sesli sahibin kendi sistemini yeniden puanlamasına izin vermek. Kanıt ve sabit bir ölçek kullan.
- Veriyi unutmak. Arşiv veya saklama planı olmadan uygulama kaldırmak uyum riski yaratır.
- TIME'ı plan sanmak. TIME bir karardır; yol haritası bağımlılık ve dalga ister.

## Örnek
Girdi: "İK'da iki izin sistemi ve desteklenmeyen bir veritabanı üzerinde eski bir bordro aracı var."

Çıktıdan bir bölüm:
| Uygulama | İş uygunluğu | Teknik uygunluk | TIME | Ana risk | Gerekçe |
|---|---|---|---|---|---|
| LeaveTrack | 2 | 2 | Kaldır | Mükerrer | İK paketinin izin modülü karşılıyor `[özellik eşdeğerliğini teyit et]` |
| PayrollLegacy | 5 | 1 | Taşı | Veritabanı destek sonu `[BİLİNMİYOR tarih]` | Kritik süreç desteklenmeyen yığında |
