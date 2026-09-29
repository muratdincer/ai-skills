---
name: ml-monitoring-plan
description: "Bir makine öğrenmesi modeli için veri ve tahmin kayması, gecikmeli etiketlerle performans düşüşü, veri kalitesi, operasyonel sağlık, alarm eşikleri, sorumlular ve yeniden eğitim tetikleyicilerini kapsayan üretim izleme planı hazırlar. Model canlıya çıkmak üzereyken, sessiz model bozulmasının yol açtığı bir olaydan sonra veya modelin hâlâ çalışıp çalışmadığının nasıl anlaşılacağı sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: ml-ai-engineer
  area: ml
  title: "Model izleme planı"
  related: "model-evaluation-report, model-card, alert-design, observability-plan, feature-engineering-plan"
  prompt: "Churn modelimiz için izleme planı yaz; tüm müşterileri her gece skorluyor ve gerçek churn'ü ancak 60 gün sonra öğreniyoruz."
---

# Model İzleme Planı

## Amaç
Neyin, ne sıklıkla, hangi referansa göre ölçüleceğini ve kimin aksiyon alacağını tanımlamak. Böylece model bozulması iş tarafı fark etmeden yakalanır, yeniden eğitim de keyfe göre değil bir gerekçeyle yapılır.

## Ne zaman kullanılır
- Model üretime ya da gölge moddan canlı trafiğe geçerken.
- Bir model sessizce kötüleştiğinde ve ekip tespit mekanizması kurmak istediğinde.
- Yeniden eğitim sabit takvimle yapılıyor ve ekip kanıta dayalı tetikleyiciler istiyorsa.

## Ne zaman kullanılmaz
- Model henüz çevrimdışı değerlendirilmediyse önce `model-evaluation-report` kullanılır.
- İhtiyaç model boyutu olmayan altyapı/servis izlemesiyse `observability-plan` veya `alert-design` kullanılır.

## Girdiler
Zorunlu:
- Modelin amacı, tahmin türü (sınıf, skor, sıralama, regresyon, üretken) ve sunum şekli (batch, online, streaming).
- Gerçek etiketlerin (ground truth) ne zaman ve nasıl oluştuğu (ya da hiç oluşmadığı).

İsteğe bağlı, kaliteyi artırır:
- Çevrimdışı değerlendirme sonuçları ve eğitim verisi dönemi (referans taban).
- Önemli öznitelikler ve dilimler, modelin etkilediği iş KPI'ı, sunum yolunun SLO'ları.
- Mevcut izleme altyapısı ve nöbet (on-call) yapısı.

Etiketlerin ne zaman oluştuğu bilinmiyorsa sor; tüm tasarımı bu belirler. Geri kalan her şey açık soru olur.

## Süreç
1. Sunum bağlamını tanımla: hacim, sıklık, gecikme bütçesi, tahminleri kullananlar ve tahmine göre alınan aksiyonlar.
2. Referans tabanı sabitle: eğitim veya doğrulama dönemi ve her öznitelik ile tahminler için saklanacak istatistikler.
3. Girişte veri kalitesi kontrollerini tanımla: şema, boş oranı, değer aralığı, kategori sayısı, güncellik; her birini engelleyici veya uyarı olarak belirle.
4. Kayma izleyicilerini tanımla: öznitelik bazında dağılım kayması (PSI, KS veya Jensen-Shannon; kategorikler için ki-kare) ve tahmin dağılımı kayması; küçük özniteliklerin gürültüsü kimseyi uyandırmasın diye öznitelik önemine göre önceliklendir.
5. Etiket bazlı performans izleyicilerini tanımla: çevrimdışı metrik, dilim bazında, etiket gecikmesi belirtilerek. Etiketler gecikmeliyse öncü göstergeler ekle (tahmin kayması, iş göstergesi, insanla etiketlenmiş küçük örneklem).
6. İş ve adillik izleyicilerini ekle: modelin etkilediği KPI ve korunan ya da kritik segmentler arasındaki metrik farkları.
7. Operasyonel izleyicileri ekle: gecikme yüzdelikleri, hata ve zaman aşımı oranı, fallback oranı, işlem hacmi, tahmin başına maliyet.
8. Her izleyici için uyarı ve kritik seviyeli eşik ve pencere belirle; doğrulanmamış eşikleri `[VARSAYIM]` olarak işaretle ve bir kalibrasyon dönemi planla.
9. Her alarmı bir sorumluya ve runbook aksiyonuna bağla: incele, önceki modele geri dön, kural tabanlı fallback'e geç veya yeniden eğit.
10. Yeniden eğitim tetikleyicilerini (performansın alt sınırın altına düşmesi, süreklilik gösteren kayma, azami model yaşıyla planlı yenileme) ve yeniden eğitilen modelin terfi için geçmesi gereken kapıyı tanımla.
11. Panoları, gözden geçirme sıklığını ve log saklama süresini belirle; loglanan öznitelik ve tahminlerdeki kişisel verileri maskele.
12. Her çıkarımı `[VARSAYIM]` olarak işaretle ve açık soruları listele. Kullanıcının hedefi devam ediyorsa alarmları ayarlamak için `alert-design` veya izleme taahhütlerini belgelemek için `model-card` öner.

## Çıktı formatı
```markdown
# Model İzleme Planı: <model adı, sürüm>
Sunum: <batch/online> · Hacim: <n/dönem> · Etiket gecikmesi: <süre veya yok> · Sorumlu: <ekip>

## Referans Taban
<dönem, saklanan istatistikler>

## İzleyiciler
| # | Katman | Sinyal | Yöntem / metrik | Pencere | Uyarı | Kritik | Sorumlu | Aksiyon |
|---|---|---|---|---|---|---|---|---|
| 1 | Veri kalitesi | <öznitelik boş oranı> | <kural> | <günlük> | <x> | <y> | <ekip> | <batch'i durdur / alarm> |
| 2 | Kayma | <ilk k öznitelik> | <PSI> | <haftalık> | <0,1> | <0,25> | ... | ... |
| 3 | Performans | <dilim bazında metrik> | ... | ... | ... | ... | ... | ... |
| 4 | İş / adillik | ... | ... | ... | ... | ... | ... | ... |
| 5 | Operasyonel | <p95 gecikme> | ... | ... | ... | ... | ... | ... |

## Yeniden Eğitim Tetikleyicileri ve Terfi Kapısı
- Tetikleyiciler: ...
- Kapı: <çevrimdışı metrik ≥ mevcut model, dilim kontrolleri, gölge dönem>

## Fallback ve Geri Dönüş
<önceki sürüm / kural tabanlı fallback, kim karar verir>

## Gizlilik ve Saklama
<neler loglanıyor, maskeleme, saklama süresi>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Etiket gecikmesi belirtildi ve aradaki boşluğu öncü göstergeler kapatıyor.
- [ ] Her izleyicinin eşiği, penceresi, sorumlusu ve somut aksiyonu var.
- [ ] Kayma izleme tüm özniteliklere körü körüne değil, öznitelik önemine göre uygulanıyor.
- [ ] Performans ve adillik yalnızca toplamda değil, dilim bazında izleniyor.
- [ ] Yeniden eğitimin açık tetikleyicileri ve bir terfi kapısı var.
- [ ] Loglanan kişisel veri en aza indirildi veya maskelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca kaymaya alarm kurmak. Performansa etkisi olmayan kayma çoğu zaman aksiyon gerektirmez; performans veya iş sinyaliyle birlikte kullan.
- Kapı olmadan otomatik yeniden eğitim. Bozuk veriyle eğitilen model daha kötü olabilir; her zaman önce mevcut şampiyon modelle karşılaştır.
- Geri besleme döngülerini görmezden gelmek. Modelin aksiyonları gelecekteki etiketleri değiştiriyorsa (ör. elde tutma teklifleri) bunu not et ve bir kontrol grubu (holdout) tut.

## Örnek
Girdi: "Churn modeli, tüm müşteriler üzerinde gecelik batch, gerçek churn 60 gün sonra belli oluyor."

Çıktıdan bir bölüm:
- Performans: 60 gün önce skorlanan kohort üzerinde, aylık olarak, abonelik süresi dilimlerine göre AUC ve ilk %10'da precision.
- Öncü gösterge: Skor dağılımında haftalık PSI (uyarı 0,1, kritik 0,25 `[VARSAYIM: ilk 8 haftada kalibre edilecek]`).
- Geri besleme döngüsü: Elde tutma teklifi alan müşteriler etiket değerlendirmesinden çıkarılır; rastgele %5'lik bir holdout grubuna teklif yapılmaz `[VARSAYIM]`.
