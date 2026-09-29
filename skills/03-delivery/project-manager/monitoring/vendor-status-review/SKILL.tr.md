---
description: Bir tedarikçinin teslimat performansını sözleşmeye veya iş tanımına (SOW) göre değerlendirir; teslimatlar ve kilometre taşları, SLA ve KPI sonuçları, kalite, kadro, faturalar ve her iki tarafın açık yükümlülüklerini inceler ve kanıta dayalı puanlı bir değerlendirme, sorunlar ve kararlaştırılan aksiyonlar üretir. Dönemsel tedarikçi yönetişim toplantısı öncesinde, bir tedarikçi geciktiğinde, bir fatura veya kilometre taşı ödemesi onaylanmadan önce ya da eskalasyon veya sözleşme yaptırımlarına karar verirken kullanılır.
related: statement-of-work, sla-breach-analysis, issue-management, acceptance-certificate, vendor-evaluation
prompt: SOW kilometre taşlarını, uygulama ortağımızın durum raporunu ve SLA raporumuzu kullanarak aylık performans değerlendirmesini hazırla.
---

# Tedarikçi Performans Değerlendirmesi

## Amaç
Tedarikçinin sözleşmesel taahhütlerini karşılayıp karşılamadığına, neyin risk altında olduğuna ve iki tarafın sırada ne yapması gerektiğine dair kanıta dayalı bir görünüm vermek. Böylece ödemeler, eskalasyonlar ve ilişki kararları olgulara dayanır.

## Ne zaman kullanılır
- Dönemsel (ör. aylık veya çeyreklik) tedarikçi yönetişim ya da hizmet değerlendirmesinde.
- Bir tedarikçi kilometre taşlarını, SLA hedeflerini veya kalite beklentilerini kaçırdığında.
- Bir kilometre taşı ödemesi veya fatura onaylanmadan önce.
- Yenileme, uzatma veya çıkış görüşmelerinden önce.

## Ne zaman kullanılmaz
- Yeni tedarikçi seçimi için `vendor-evaluation` kullanılır.
- Tek bir SLA ihlalinin ayrıntılı analizi için `sla-breach-analysis` kullanılır.
- Belirli bir teslimatın resmî kabulü için `acceptance-certificate` kullanılır.

## Girdiler
Zorunlu:
- Sözleşmesel temel: SOW, sözleşme yükümlülükleri, kilometre taşları, SLA/KPI tanımları (veya ilgili bölümleri).
- Döneme ait performans kanıtı: tedarikçi durum raporu, SLA/KPI ölçümleri, teslimat kayıtları.

İsteğe bağlı, kaliteyi artırır:
- Faturalar ve ödeme takvimi, değişiklik talepleri, önceki değerlendirmenin aksiyonları.
- İç ekip geri bildirimi, hata verileri, planlanan ve gerçekleşen kadro.

Sözleşmesel temel veya dönem kanıtı yoksa iste. Kanıtlanamayanı puanlama.

## Süreç
1. Değerlendirme dönemini belirle ve bu dönemde vadesi gelen yükümlülükleri listele: teslimatlar, kilometre taşları, SLA/KPI hedefleri, kadro taahhütleri, raporlama görevleri.
2. Müşterinin kendi yükümlülüklerini de (erişim, kararlar, ortamlar, gözden geçirmeler) ve karşılanıp karşılanmadığını listele; müşteri bağımlılıklarından kaynaklanan tedarikçi gecikmeleri ayrılmalıdır.
3. Her yükümlülüğü kanıtla karşılaştır: karşılandı, kısmen karşılandı, karşılanmadı, ölçülemedi. Her biri için kaynak göster.
4. SLA/KPI sonuçlarını sözleşmedeki formüle göre değerlendir (ölçüm penceresi, istisnalar, hizmet kredileri); hedefleri yeniden tanımlama.
5. Kalite sinyallerini değerlendir: hata oranları, yeniden çalışma, kabul retleri, dokümantasyonun eksiksizliği.
6. Ticari durumu kontrol et: faturalanan ve kabul edilen teslimatlar, bekleyen değişiklik talepleri, doğan krediler; kabul edilmemiş iş için kesilen faturaları işaretle.
7. Her alanı belirtilen bir ölçekte (ör. 1-5) tek satırlık gerekçeyle puanla; iç ekip görüşlerini kanıt değil algı olarak etiketle.
8. Sorunları ve riskleri belirle; hangilerinin sözleşmesel eskalasyon, hangilerinin ilişki düzeyinde çözüm gerektirdiğine karar ver.
9. Her iki taraf için sahip ve tarihli aksiyonlar taslakla, son değerlendirmeden kalan açık aksiyonları taşı.
10. Kullanıcının hedefi devam ediyorsa belirli bir ihlal için `sla-breach-analysis`, tedarikçi sorunu için `issue-management` ya da teslim edilenleri kabul etmek için `acceptance-certificate` öner.

## Çıktı formatı
```markdown
# Tedarikçi Performans Değerlendirmesi: <tedarikçi> – <dönem>
Sözleşme / SOW ref: <...> | Değerlendirenler: <...>

## Özet
<genel puan, öne çıkan 3 nokta, gereken kararlar>

## Yükümlülükler ve Kanıtlar
| Yükümlülük | Vade | Sonuç (Karşılandı/Kısmen/Karşılanmadı/Ölçülemedi) | Kanıt |

## SLA / KPI Sonuçları
| Metrik | Hedef | Gerçekleşen | Durum | Kredi / yaptırım |

## Müşteri Tarafı Yükümlülükleri
| Yükümlülük | Karşılandı mı? | Tedarikçiye etkisi |

## Puan Kartı
| Alan | Puan (1-5) | Gerekçe |
| Teslimat / Kalite / SLA / Kadro / İletişim / Ticari |

## Ticari Durum
## Sorunlar, Riskler ve Eskalasyonlar
## Aksiyonlar
| # | Aksiyon | Taraf | Sahip | Bitiş | Durum |
```

## Kalite kontrol listesi
- [ ] Her puan izlenime değil, sözleşme koşullarına ve kanıta dayanıyor.
- [ ] Müşteri tarafı bağımlılıklar ayrı değerlendirildi.
- [ ] SLA sonuçları sözleşmenin formülünü ve istisnalarını kullanıyor.
- [ ] Faturalar kabul edilmiş teslimatlarla mutabakata sokuldu.
- [ ] Aksiyonların her iki tarafta da sahibi ve tarihi var.
- [ ] Tedarikçi personeline ait kişisel veri, değerlendirmenin gerektirdiği rollerle sınırlı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tedarikçinin kendi yeşil durum raporuna güvenmek. Bağımsız kanıtla doğrula.
- Müşteri kaynaklı gecikmeleri yok saymak; bu, sonraki talep veya yaptırımları zayıflatır.
- Her şeyi sözleşmesel olarak eskale etmek; resmî yaptırımları önemli veya tekrarlayan ihlallere sakla.

## Örnek
Girdi: "SOW kilometre taşı M3 (veri taşıma) ayın 15'inde; tedarikçi %90 tamam diyor. SLA P1 yanıt süresi 30 dk, 5 olaydan 2'si kaçırıldı."

Çıktıdan bir bölüm:
- M3 Veri taşıma – Vade 15'i – Karşılanmadı – tedarikçi raporu %90 diyor; henüz kabul edilmiş bir taşıma koşusu yok.
- P1 yanıt: 5 olayın 3'ü 30 dk içinde (%60), hedef `[sözleşme %]` – Karşılanmadı – `[madde ref]` uyarınca kredi doğrulanmalı.
- Müşteri tarafı: üretim veri çıktısı geç teslim edildi `[tarihi teyit et]` – M3 gecikmesinin bir kısmını açıklayabilir.
