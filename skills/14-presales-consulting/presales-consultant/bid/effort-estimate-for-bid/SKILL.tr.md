---
description: Bir teklif için efor tahmini oluşturur; iş kırılımından gelen aşağıdan-yukarı tahmini yukarıdan-aşağı veya benzetme kontrolüyle birleştirir, her varsayımı ve kapsam dışını açık yazar, riske dayalı yedek pay ekler ve eforu rol bazlı bir kadro profiline çevirir. Ön satış ekibinin sabit fiyatlı veya zaman-malzeme teklifi fiyatlaması gerektiğinde, bir RFP efor veya ekip büyüklüğü istediğinde ya da mevcut bir teklif tahmininin sağlamasının yapılması gerektiğinde kullanılır.
related: rfp-analysis, proposal-writing, statement-of-work, estimation-three-point, wbs
prompt: SSO, sipariş takibi ve ERP entegrasyonu olan bir B2B müşteri portalı teklifimiz için efor tahmini yap; müşteri sabit fiyat istiyor.
---

# Teklif İçin Efor Tahmini

## Amaç
Bir teklif için savunulabilir, varsayımlara dayanan bir efor rakamı ve kadro profili üretmek. Böylece ticari ekip fiyatlayabilir, teslimat ekibi de daha sonra bu sınırlar içinde teslim edebilir.

## Ne zaman kullanılır
- Bir RFP, ihale veya müşteri talebi efor, ekip büyüklüğü ya da fiyat dayanağı istediğinde.
- Sabit fiyatlı bir teklifin kapsamlanması ve varsayımlar ile yedek payla korunması gerektiğinde.
- Satıştan gelen bir rakamın gönderim öncesi bağımsız bir aşağıdan-yukarı kontrolü gerektiğinde.

## Ne zaman kullanılmaz
- Proje kazanıldıysa ve iş kalemi bazında teslimat tahmini gerekiyorsa `estimation-three-point` veya `technical-estimation` kullanılır.
- Teklif verilip verilmeyeceğine hâlâ karar veriliyorsa `rfp-analysis` kullanılır.
- Efor değil bulut işletim maliyeti fiyatlanıyorsa `cloud-cost-estimate` kullanılır.

## Girdiler
Zorunlu:
- Kapsam tanımı: RFP, gereksinim listesi veya müşteri talebi.
- Ticari model: sabit fiyat, zaman-malzeme, tavanlı veya bilinmiyor.

İsteğe bağlı, kaliteyi artırır:
- Benzer projelerin gerçekleşen değerleri; ekip verimlilik normları.
- Teslimat modeli (yerinde/uzaktan karışımı), roller ve ücret tabloları (verilmedikçe ücretler ticari ekipte kalır).
- Müşteri kısıtları: son tarih, zorunlu teknolojiler, müşteri tarafı sorumluluklar.

Kapsam yoksa iste. Geçmiş veri, ücret veya müşteri taahhüdü asla uydurma; bunları `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Girdideki kapsam kalemlerini teklif düzeyinde bir iş kırılım yapısına (WBS) çıkar: fazlar, iş akışları, özellikler, entegrasyonlar, veri taşıma, fonksiyonel olmayan işler. Her birine kaynak referansını ekle; senin eklediğin kalemler `[VARSAYIM]` olur.
2. Her kalemin kesinliğini sınıflandır: bilinen (net tanım), anlaşılmış (tipik, bazı belirsizlikler), belirsiz (muğlak, yeni, müşteriye bağımlı). Belirsiz kalemler tek rakam değil aralık ve açık varsayımlar alır.
3. Her kalemi üç noktalı (iyimser, en olası, kötümser) adam-gün olarak aşağıdan-yukarı tahmin et; beklenen eforu (O + 4M + P) / 6 ile hesapla ve yayılımı görünür tut.
4. Tekliflerde sık unutulan eforu ekle: proje yönetimi, mimari, ortamlar ve DevOps, test ve hata düzeltme, UAT desteği, veri taşıma, dokümantasyon, eğitim, canlı sonrası yoğun destek (hypercare), güvenlik ve performans testi, yönetişim toplantıları. Kullanılan oranı veya dayanağı belirt.
5. Yukarıdan-aşağı sağlama yap: toplamı ve faz dağılımını benzer bir projeyle veya belirtilmiş bir oranla (ör. testin geliştirmeye oranı) karşılaştır. Fark yaklaşık %20'yi aşıyorsa incele ve açıkla; körü körüne ortalama alma.
6. Varsayım kaydını yaz: rakamın dayandığı her varsayımı SOW'a kopyalanabilecek biçimde ifade et (müşteri X'i Y tarihine kadar sağlar; en fazla N entegrasyon; Z ortam) ve açık kapsam dışı maddeleri ekle.
7. Bir risk listesi çıkar ve yedek payı düz bir yüzde yerine buradan türet (risk bazlı maruziyet veya üç noktalı yayılım). Yedek payı (bilinen riskler, fiyatın içinde) yönetim rezervinden (bilinmeyen bilinmeyenler, ticari karar) ayır.
8. Eforu rol ve faz bazında bir kadro profiline çevir ve ortaya çıkan sürenin müşterinin son tarihine uyduğunu kontrol et; uymuyorsa sıkıştırma risklerini işaretle.
9. Tahmini önerilen bir rakam ve güven düzeyiyle birlikte aralık olarak, ticari modele göre sun: sabit fiyat daha sıkı varsayım ve daha yüksek yedek pay ister; zaman-malzeme net bir ücret dayanağı ve tavan mantığı ister.
10. Aralığı en çok daraltacak müşteri sorularını efor etkisine göre sıralayarak listele.
11. Hedef devam ediyorsa yaklaşımı sunmak için `proposal-writing`, varsayımları sözleşmeye bağlamak için `statement-of-work` veya gereksinim bazlı yanıtlar için `rfp-response` öner.

## Çıktı formatı
```markdown
# Teklif Efor Tahmini: <müşteri / fırsat>
| Alan | Değer |
|---|---|
| Ticari model | ... |
| Önerilen efor | <adam-gün> (aralık <alt>–<üst>, güven <Y/O/D>) |
| Süre / en yüksek ekip | ... |

## İş Kalemi Bazında Tahmin
| No | Kalem | Kaynak | Kesinlik | O | M | P | Beklenen | Varsayımlar |

## Destekleyici Efor
| Alan | Dayanak | Adam-gün |

## Yukarıdan-Aşağı Sağlama
- Benzetme / oran: ...  - Fark ve açıklaması: ...

## Yedek Pay
| Risk | Olasılık | Etki (AG) | Maruziyet |
- Yedek pay: ...  - Yönetim rezervi (ticari karar): ...

## Kadro Profili
| Rol | Faz 1 | Faz 2 | ... | Toplam AG |

## Varsayımlar ve Kapsam Dışı (SOW'a hazır)
- V1: ...
- Kapsam dışı: ...

## Aralığı Daraltacak Sorular
1. <soru> — <efor etkisi>
```

## Kalite kontrol listesi
- [ ] Her kapsam kalemi girdiye dayanıyor ya da `[VARSAYIM]` olarak etiketli.
- [ ] Destekleyici efor (PM, test, ortamlar, taşıma, hypercare) dayanağıyla dahil edilmiş.
- [ ] Aşağıdan-yukarı ve yukarıdan-aşağı rakamlar uzlaştırılmış, farklar açıklanmış.
- [ ] Yedek pay adı konmuş risklerden türetilmiş ve yönetim rezervi ayrılmış.
- [ ] Varsayımlar bir SOW'a kopyalanabilecek biçimde yazılmış.
- [ ] Hiçbir ücret, geçmiş rakam veya müşteri taahhüdü uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca geliştirme eforunu tahmin etmek. Geliştirme dışı işler çoğu zaman toplamın büyük bir bölümünü oluşturur; açıkça listele.
- Tahmini hedef fiyata göre tersine hesaplamak. Dürüst rakamı koru; indirim veya risk kabulüne ticari ekip karar versin.
- Varsayımları tahmin tablosuna gömmek. SOW'da yer almayan varsayım teklifi korumaz.

## Örnek
Girdi: "B2B portal: SSO, sipariş takibi, ERP entegrasyonu. Sabit fiyat. ERP hakkında ayrıntı yok."

Çıktıdan bir bölüm:
| No | Kalem | Kesinlik | O | M | P | Beklenen | Varsayımlar |
|---|---|---|---|---|---|---|---|
| 3 | ERP sipariş senkronizasyonu | belirsiz | 25 | 45 | 90 | 49,2 | V4: ERP dokümante API sunuyor; en fazla 3 varlık; müşteri 4. haftaya kadar test ERP ortamı sağlar |

- Aralığı daraltacak soru: "Hangi ERP ve sürümü, sipariş API'leri hazır mı?" — etki ±45 AG'ye kadar.
