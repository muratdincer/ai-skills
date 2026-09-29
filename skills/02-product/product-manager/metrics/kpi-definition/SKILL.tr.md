---
description: Ürün KPI'larını ad, amaç, formül, dahil etme kuralları, veri kaynağı, başlangıç değeri, hedef, eşikler, sahip, periyot ve her KPI'nın beslediği kararı içeren, belirsizliği olmayan bir KPI tablosu olarak tanımlar. Bir ürün, özellik veya ekip için KPI seti gerektiğinde, mevcut KPI'lar belirsiz veya tartışmalıysa ya da biri "hangi KPI'ları izlemeliyiz ve tam olarak nasıl hesaplanıyor" diye sorduğunda kullanılır.
related: north-star-metric, metric-definition, okr-definition, dashboard-spec, feature-adoption-review
prompt: Otellerdeki yeni mobil self check-in özelliğimiz için KPI'ları tanımla.
---

# KPI Tanımlama

## Amaç
Herkesin aynı şekilde hesapladığı, bir sahibi ve gözden geçirme ritmi olan, her biri bilinen bir kararı yönlendiren küçük bir KPI seti üretmek. Böylece değerlendirme toplantıları kimin sayısının doğru olduğunu değil, ne yapılacağını tartışır.

## Ne zaman kullanılır
- Bir ürün, özellik veya ekip yayına çıkıyor ve üzerinde uzlaşılmış performans göstergelerine ihtiyaç var.
- Mevcut KPI'lar tartışmalı ("hangi aktif kullanıcı?"), izlenmiyor ya da sahipsiz.
- Bir gösterge paneli veya yönetim raporu tanımlanacak ve arkasındaki KPI'lar belirsiz.

## Ne zaman kullanılmaz
- Ürünün henüz ortak bir değer metriği yoksa önce `north-star-metric` kullanılır.
- İddia seviyesi olan, zamana bağlı hedefler gerekiyorsa `okr-definition` kullanılır.
- Bir veri mühendisi tek bir metriğin olay/SQL seviyesinde tam tanımına ihtiyaç duyuyorsa `metric-definition` kullanılır.

## Girdiler
Zorunlu:
- Ürün/özellik/ekip ve hedefi ya da KPI'ların desteklemesi gereken kararlar.

İsteğe bağlı, kaliteyi artırır:
- Mevcut metrikler, analitik olaylar ve veri kaynakları; Kuzey Yıldızı veya OKR'lar.
- Başlangıç değerleri, kıyaslamalar, SLA'lar veya sözleşmesel hedefler; rapor hedef kitlesi.

Hedef yoksa sor. Başlangıç değeri veya hedef uydurma; nasıl elde edileceğini belirterek `[TBD]` olarak işaretle.

## Süreç
1. KPI'ların beslemesi gereken kararları (ör. "daha fazla otele yaygınlaştır", "onboarding'e yatırım yap") ve hedef kitleyi listele; hiçbir karara hizmet etmeyen KPI çıkarılır veya teşhis metriklerine taşınır.
2. Değer zincirini 4-8 KPI'lık dengeli bir setle kapsa: sonuç (değer/iş), davranış (benimsenme, etkileşim), kalite/sağlık (hata, gecikme, destek yükü) ve en az bir koruma metriği.
3. Her KPI için kesin tanım yaz: pay ve paydasıyla formül, birim, dahil etme/hariç tutma kuralları (test hesapları, iç kullanıcılar, iptaller), zaman penceresi ve toplama biçimi (günlük, 28 günlük kayan).
4. Veri kaynağını ve olayı/alanı belirt ya da `[TBD]` olarak işaretleyip gereken ölçümlemeyi not et. Kişisel veri gerektiren KPI'ları işaretle ve veriyi en aza indir (toplulaştır, takma adla; KVKK/GDPR).
5. Her KPI'yı öncü veya gecikmeli olarak sınıflandır ve aralarındaki beklenen ilişkiyi hipotez olarak not et.
6. Başlangıç değerini (verilmişse ya da ölçüm planıyla `[TBD]`), hedefi (verilmişse ya da `[TBD]`) ve her durumun tetiklediği aksiyonla kırmızı/sarı/yeşil eşikleri kaydet.
7. Her KPI'ya tek bir hesap verebilir sahip (rol) ve ne kadar hızlı değişebildiğine uygun bir gözden geçirme sıklığı ata.
8. Seti çatışma ve manipülasyon açısından kontrol et: hangi KPI bir diğerine zarar verirken iyileştirilebilir? Gerekirse karşı metrik ekle veya eşleştir.
9. Çıkarım yapılan her tanımı veya ilişkiyi `[VARSAYIM]` olarak işaretle ve veri sahipleri için açık soruları listele.
10. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: seti görselleştirmek için `dashboard-spec`, veri seviyesinde tanım için `metric-definition`, zamana bağlı hedefler için `okr-definition`.

## Çıktı formatı
```markdown
# KPI Tablosu: <ürün / özellik / ekip>
Desteklenen kararlar: <...> · Hedef kitle: <...>

| KPI | Tür (sonuç/davranış/kalite/koruma) | Öncü/gecikmeli | Formül | Dahil etme kuralları | Pencere | Kaynak | Başlangıç | Hedef | K/S/Y eşikleri → aksiyon | Sahip | Periyot |
|---|---|---|---|---|---|---|---|---|---|---|---|

## KPI Ayrıntıları
### <KPI adı>
- Amaç / beslediği karar: ...
- Tanım notları ve uç durumlar: ...
- Veri ve gizlilik: ...

## Çatışmalar ve Karşı Metrikler
- ...

## Ölçümleme Eksikleri
- ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her KPI adı belli bir kararı besliyor ve tek bir hesap verebilir sahibi var.
- [ ] Her formül pay, payda, dahil etme kuralları ve zaman penceresini belirtiyor.
- [ ] Set sonuç, davranış ve kalite KPI'larını karıştırıyor ve en az bir koruma metriği içeriyor.
- [ ] Başlangıç değerleri ve hedefler verilmiş ya da elde etme yoluyla `[TBD]`; hiçbiri uydurulmadı.
- [ ] Kişisel veri kullanımı en aza indirildi ve işaretlendi.
- [ ] Eşikler somut aksiyonlara bağlandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Aktifliği tanımlamadan "aktif kullanıcı" demek. Niteleyen eylemi ve pencereyi belirt.
- Çok fazla KPI. Hedef kitle başına ~8'den fazlası dikkati dağıtır; gerisini teşhis metriklerine taşı.
- Başlangıç değeri olmadan hedef koymak. Önce ölç, sonra hedef koy ya da hedefi hipotez olarak belirt.

## Örnek
Girdi: "Otellerdeki yeni mobil self check-in özelliğimiz için KPI'lar."

Çıktıdan bir bölüm:
| KPI | Tür | Formül | Hedef | Sahip |
|---|---|---|---|---|
| Self check-in oranı | Sonuç | Haftalık uygulamadan check-in yapılan konaklamalar ÷ uygun konaklamalar (grup rezervasyonları hariç) | 4 haftalık başlangıç ölçümünden sonra `[TBD]` | Ürün yöneticisi, misafir uygulaması |
| Oda anahtarına medyan süre | Davranış | Varış coğrafi alanından dijital anahtarın verilmesine kadar geçen medyan dakika | `[TBD]` | Ürün yöneticisi |
| Check-in hata oranı | Kalite | Başarısız uygulama check-in'leri ÷ denemeler | Eşik üstü `[TBD]` kırmızı → olay incelemesi | Mühendislik lideri |
| Resepsiyon eskalasyonları | Koruma | Resepsiyon yardımı gereken uygulama check-in'leri ÷ uygulama check-in'leri | `[TBD]` | Otel operasyonları |
- Açık soru: Yabancı misafirler için yasal kimlik kontrolü uygulama içinde yapılabilir mi, yoksa resepsiyona gitmeyi zorunlu kılıyor mu?
