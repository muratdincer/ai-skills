---
name: sla-breach-analysis
description: "Bir dönemdeki SLA ihlallerini analiz eder: veriyi ve süre sayım kurallarını doğrular, ihlal oranlarını öncelik, kategori, ekip, zaman ve müşteri bazında ölçer, örüntüleri ve kök nedenleri (süreç, kapasite, yönlendirme, bağımlılık, ölçüm) bulur ve sahipli, hedef metrikli, önceliklendirilmiş iyileştirme aksiyonları önerir. SLA performansı düştüğünde, bir hizmet değerlendirmesi veya sözleşme görüşmesi öncesinde, ceza veya iade söz konusu olduğunda ya da bir ekip kayıtların neden hedefi kaçırdığını anlamak istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 11-support-ops
  role: it-service-management
  area: itsm
  title: "SLA ihlal analizi"
  related: "problem-management, ticket-triage, slo-definition, kpi-definition, dashboard-spec"
  prompt: "Geçen çeyreğin SLA ihlallerini analiz et: P2 çözüm hedefi 8 iş saati, %90 hedefe karşı %71 tutturduk; kayıt dökümü ekte."
---

# SLA İhlal Analizi

## Amaç
Hizmet seviyelerinin neden kaçırıldığını kanıtla açıklamak, gerçek hizmet sorunlarını ölçüm kaynaklı sapmalardan ayırmak ve bulguları, hedefe ulaşmayı ölçülebilir biçimde artıracak birkaç aksiyona dönüştürmek.

## Ne zaman kullanılır
- Bir öncelik, hizmet veya müşteri için SLA başarı oranı hedefin altına düştüğünde.
- Bir hizmet değerlendirmesi, sözleşme yenileme veya ceza/iade görüşmesi yaklaştığında.
- Bir destek ekibi yanıt veya çözüm hedeflerini sürekli kaçırdığında ve neden tartışmalı olduğunda.

## Ne zaman kullanılmaz
- Yeni hizmet seviyesi hedefleri veya hata bütçeleri tanımlanacaksa `slo-definition` kullanılır.
- Tek bir kayıt ihlal edildi ve hemen eskalasyon gerekiyorsa `ticket-escalation-summary` kullanılır.
- Bilinen neden tekrarlayan teknik olaylarsa `problem-management` kullanılır.

## Girdiler
Zorunlu:
- Döneme ait kayıt veya olay verisi (en az numara, öncelik, kategori, açılış, ilk yanıt, çözüm, durum geçmişi veya bekletme süreleri, atanan grup) ya da toplu bir ihlal raporu.
- SLA tanımları: öncelik başına hedefler, çalışma saatleri/takvim, bekletme kuralları.

İsteğe bağlı, kaliteyi artırır:
- Personel ve vardiya verileri, birikim eğilimi, dönem içindeki değişiklikler (sürümler, yeniden yapılanma, araç değişikliği).
- Müşteri sözleşme şartları, ceza veya iade maddeleri.
- Karşılaştırma için önceki dönem sonuçları.

Veri veya SLA tanımları eksikse iste; varsayılan hedeflerle oran hesaplama. Toplulaştırılmış veya takma adlandırılmış veriyle çalış: analizden önce kayıt metinlerindeki müşteri iletişim bilgilerini ve kişisel verileri çıkar.

## Süreç
1. Ölçümü doğrula: süre sayım kurallarını (çalışma saatleri, tatiller, saat dilimleri, "müşteri bekleniyor" durumunda bekletme) teyit et; eksik zaman damgalarını, yeniden açılan kayıtları, yaşam döngüsü ortasında değişen öncelikleri ve çözülmeden kapatılan kayıtları kontrol et. Veri kalitesi sorunlarını ve etkilerini kaydet.
2. Her SLA metriği (yanıt, çözüm) için öncelik bazında dönem başarı oranını ve önceki dönemlere göre durumu hesapla; yalnızca yüzde değil, sayıları da göster.
3. İhlalleri kategori/hizmet, atanan grup, kanal, müşteri, günün/haftanın zamanı ve kayıt yaşına göre dilimle; ihlallerin nerede yoğunlaştığını vurgula (örneğin ihlallerin %80'ine yol açan kategorilerin %20'si).
4. İhlal edilen kayıtların zaman çizelgelerini incele: atamadan önce kuyrukta geçen süre, yeniden atamalar (ping-pong), üçüncü taraf beklemesi, bekletmede geçen süre ve çalışma süresi. Süreyi hangi bölümün tükettiğini belirle.
5. Nedenleri sınıflandır: talep artışı, kapasite/vardiya kapsaması, yönlendirme ve sınıflandırma hataları, yetkinlik eksikleri, başka bir ekibe veya tedarikçiye bağımlılık, süreç tasarımı (onaylar), araçlar, ölçüm kaynaklı sapmalar. Her nedeni kanıta dayalı veya `[VARSAYIM]` olarak etiketle.
6. Manipülasyon veya çarpıtmayı kontrol et: ihlale yakın öncelik düşürme, erken kapatma, bekletmenin kötüye kullanımı, bölünmüş kayıtlar. Bunları tarafsız biçimde ölçüm riski olarak raporla.
7. Sözleşmesel maruziyeti yalnızca verilen sözleşme şartlarından hesapla; aksi hâlde `[BİLİNMİYOR]` yaz.
8. Aksiyonları beklenen etki ve efora göre sırala; her birini bir nedene bağla, sahibini, tarihini ve iyileşmeyi gösterecek metriği ve hedefi yaz.
9. İzleme öner: öncü göstergeler (ihlale yaklaşan kayıtlar, kuyruk yaşı, yeniden atama sayısı) ve değerlendirme sıklığı.
10. Devret: teknik kök nedenler için `problem-management`, izleme panosu için `dashboard-spec`, hedeflerin kendisi gerçekçi görünmüyorsa `slo-definition` öner.

## Çıktı formatı
```markdown
# SLA İhlal Analizi: <hizmet / dönem>
## Özet
- Başarı oranı: <metrik, öncelik>: <%x (n/N)>, hedef <%y>; önceki dönem <%z>
- Ana etkenler: 1. ... 2. ... 3. ...
- Öncelikli aksiyonlar: ...
## Veri ve Ölçüm Notları
- Uygulanan süre kuralları: ... Veri kalitesi sorunları: ... Etkisi: ...
## Başarı Oranı
| Metrik | Öncelik | Karşılanan | İhlal | Başarı | Hedef | Önceki |
|---|---|---|---|---|---|---|
## İhlal Yoğunlaşması
| Boyut | Dilim | İhlal | Pay | Not |
|---|---|---|---|---|
## Süre Nereye Gitti (ihlal edilen kayıtlar)
| Bölüm | Medyan süre | Geçen sürenin payı |
|---|---|---|
## Nedenler
| Neden | Kanıt | Güven (kanıt / [VARSAYIM]) |
|---|---|---|
## Sözleşmesel Maruziyet
<verilen şartlardan veya [BİLİNMİYOR]>
## Aksiyonlar
| # | Aksiyon | Ele aldığı neden | Sahip | Tarih | Başarı metriği |
|---|---|---|---|---|---|
## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Herhangi bir oran raporlanmadan önce SLA süre kuralları ve veri kalitesi sorunları belirtildi.
- [ ] Oranlar sayılarla birlikte, hedef ve önceki dönemle karşılaştırmalı gösterildi.
- [ ] Her neden veriyle destekleniyor veya `[VARSAYIM]` olarak etiketli.
- [ ] Her aksiyon bir nedene bağlı; sahibi ve başarı metriği var.
- [ ] Ceza veya iadeler yalnızca verilen sözleşme şartlarından hesaplandı.
- [ ] Kayıt metinlerindeki kişisel veriler çıkarıldı veya takma adlandırıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- SLA iş saatiyle tanımlıyken ihlalleri takvim saatiyle hesaplayıp ihlal sayısını şişirmek.
- Sürenin nerede harcandığını göstermeden "yeterli kişi yok" demek; çoğu zaman kuyruk beklemesi veya yeniden atamalar baskındır.
- Ortalama raporlamak; birkaç çok eski kayıt ortalamayı bozar. Medyan ve yüzdelik değerler kullan.
- On aksiyon önermek; en büyük ihlal yoğunlaşmalarını ele alan birkaç aksiyonu seç.

## Örnek
Girdi: "P2 çözüm hedefi 8 iş saati; geçen çeyrek %90 hedefe karşı %71; kayıt dökümü ekte."

Çıktıdan bir bölüm:
- Başarı oranı: P2 çözüm %71 (412/580), hedef %90; önceki çeyrek %84 (n/N [BİLİNMİYOR]).
- Yoğunlaşma: P2 ihlallerinin %58'i "Entegrasyonlar" kategorisinde; ihlal edilen kayıtların %64'ü 2 veya daha fazla kez yeniden atanmış.
- Süre nereye gitti: ilk atamadan önce kuyrukta medyan 3,1 iş saati.
- Neden (kanıt): 2. ayda devreye giren yeni iş ortağı API hataları için yönlendirme kuralı yok. Neden [VARSAYIM]: akşam vardiyasında L2 entegrasyon yetkinliği eksik.
- Aksiyon: entegrasyon hataları için yönlendirme kuralı ve sınıflandırma kontrol listesi ekle – sahip: Destek Lideri – başarı: gelecek çeyrekte P2 entegrasyon başarı oranı ≥ %88.
