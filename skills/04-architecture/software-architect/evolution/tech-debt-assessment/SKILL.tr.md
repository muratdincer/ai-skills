---
description: Kod, mimari, testler, altyapı, bağımlılıklar ve dokümantasyondaki borç öğelerinin envanterini çıkararak, bunları sınıflandırarak (bilinçli/farkında olmadan, tedbirli/pervasız), anaparayı (düzeltme maliyeti) ve faizi (süregelen maliyet ve risk) tahmin ederek ve iş etkisine bağlı bir geri ödeme planında önceliklendirerek bir teknik borç kaydı oluşturur. Ekip kod tabanı yüzünden yavaşladığını hissettiğinde, yönetim ne kadar borç olduğunu ve önce neyin düzeltileceğini sorduğunda ya da borcun planlamada gerekçelendirilmesi gerektiğinde kullanılır.
related: code-quality-report, refactoring, modernization-assessment, dependency-upgrade, technical-risk-review
prompt: Faturalama platformumuzdaki teknik borcu değerlendir; sürümler iki hafta sürüyor, test kapsamı %30 ve hâlâ desteği bitmiş bir framework sürümü kullanıyoruz.
---

# Teknik Borç Değerlendirmesi

## Amaç
"Eski sistem" ve "borç" hakkındaki belirsiz şikâyetleri, her öğenin bugün neye mal olduğunu, düzeltmenin neye mal olacağını ve hangi sırayla ödeneceğini gösteren, önceliklendirilmiş ve kanıta dayalı bir kayda dönüştürmek.

## Ne zaman kullanılır
- Teslimat yavaşlıyor, olay veya hata oranları artıyor ve ekip kod tabanından ya da platformdan şüpheleniyorsa.
- Yönetim veya ürün, yatırım kararı için borç genel görünümü istiyorsa.
- Planlamada borç ödemesi için gerekçeli bir kapasite payı gerekiyorsa.

## Ne zaman kullanılmaz
- Tek bir kod tabanının metrik anlık görüntüsü (karmaşıklık, kapsam, tekrar) yeterliyse `code-quality-report` kullanılır.
- Asıl soru sistemin tamamının geleceğiyse (koru, platform değiştir, yenisiyle değiştir) `modernization-assessment` kullanılır.
- Bilinen tek bir öğe için somut düzeltme gerekiyorsa `refactoring` veya `dependency-upgrade` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki sistem veya alan ve gözlemlenen belirtiler (yavaş değişiklikler, olaylar, işe alıştırma zorluğu, denetim bulguları).

İsteğe bağlı:
- Statik analiz sonuçları, test kapsamı, bağımlılık ve destek sonu (end-of-life) listeleri, olay ve hata geçmişi, teslim süresi (lead time) ve değişiklik hata oranı.
- Ekip görüşmeleri veya anket sonuçları, mimari dokümanlar, yaklaşan yol haritası öğeleri.

Belirti veya kanıt verilmemişse talebi tetikleyen iki üç sıkıntıyı sor. Metrik uydurma; boşlukları `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Sonuçlara dayan: belirtileri, varsa teslimat ve operasyon ölçümlerine (teslim süresi, değişiklik hata oranı, kurtarma süresi, işe alıştırma süresi, kaçan hata) bağla.
2. Borç öğelerinin envanterini kategoriye göre çıkar: kod, mimari/tasarım, testler, build ve pipeline, altyapı, bağımlılıklar ve desteği biten bileşenler, veri, dokümantasyon ve bilgi (tek kişiye bağlı uzmanlık).
3. Her öğe için kanıtı (metrik, olay, sık değişen dosya, görüşme alıntısı) kaydet; yalnızca görüşe dayanan öğeleri `[VARSAYIM]` olarak etiketle.
4. Nedeni teknik borç dörtlüsüyle (bilinçli/farkında olmadan × tedbirli/pervasız) sınıflandır; böylece bilinçli ödünleşimleri, sürekli yeni borç üretecek süreç sorunlarından ayır.
5. Anaparayı efor aralığı olarak (ör. kişi-gün), faizi ise tekrarlayan maliyet olarak tahmin et: değişiklik başına ek efor, olay saatleri, risk maruziyeti (güvenlik, uyum, destek sonu). Aralık kullan ve dayanağını belirt.
6. Faizi sıcak noktaya (hotspot) göre ağırlıklandır: sık değişen veya kritik yoldaki koddaki borç, kararlı ve nadiren dokunulan alanlardakinden pahalıdır.
7. Her öğeyi faiz, risk ve yaklaşan yol haritası işiyle uyum açısından puanla; önce yüksek faizli ve riskli ama anaparası düşük öğeleri ve yol haritasının üzerindeki öğeleri önceliklendir.
8. Her öğe için bir yöntem seç: hemen düzelt, ilgili özellik işiyle birlikte düzelt, ayrı iş öğesi olarak planla, sınırla (bir arayüzün arkasına izole et) veya kabul et ve belgele.
9. Borcun yeniden büyümemesi için kök neden süreç düzeltmelerini belirle (eksik definition of done maddeleri, gözden geçirme yokluğu, bağımlılık güncelleme rutininin olmaması).
10. Geri ödeme planını oluştur: iterasyon veya çeyrek başına kapasite payı ya da ayrı iş öğeleri, sahipler ve iyileşmeyi gösterecek ölçümler.
11. Hedef devam ediyorsa öncelikli öğeler için `refactoring` veya `dependency-upgrade`, borç sistemikse `modernization-assessment`, risk öğeleri için `technical-risk-review` öner.

## Çıktı formatı
```markdown
# Teknik Borç Değerlendirmesi: <sistem>
Kapsam: ... · Kanıt kaynakları: ... · Başlangıç ölçümleri: <teslim süresi, CFR, ... veya [BİLİNMİYOR]>

## Borç Kaydı
| No | Öğe | Kategori | Dörtlü | Kanıt | Anapara (aralık) | Faiz (ay/değişiklik başına) | Risk | Sıcak nokta | Öncelik | Yöntem |
|---|---|---|---|---|---|---|---|---|---|---|

## Öncelikler
1. <öğe> — neden şimdi — beklenen etki

## Kök Nedenler ve Süreç Düzeltmeleri
- ...

## Geri Ödeme Planı
| Dönem | Öğeler | Kapasite | Sahip | Başarı ölçütü |
|---|---|---|---|---|

## Kabul Edilen Borç
- <öğe> — gerekçe — gözden geçirme tarihi

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her öğenin kanıtı var veya `[VARSAYIM]` olarak etiketli.
- [ ] Anapara ve faiz, dayanağı belirtilmiş aralıklar; uydurma kesinlik veya parasal rakam yok.
- [ ] Önceliklendirme yalnızca büyüklük veya önem derecesine değil, faize ve sıcak noktalara dayanıyor.
- [ ] Her öğenin bir yöntemi var; uygun yerlerde açık kabul dahil.
- [ ] Borcun yeniden büyümemesi için süreç nedenleri ele alınmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tarayıcının bulduğu her kod kokusunu listelemek. Teslimatı ölçülebilir biçimde yavaşlatan veya risk yaratan öğeleri tut, gerisini topla.
- İş bağlantısı olmadan "borç sprint'i" istemek. Her öğeyi teslim süresine, olaylara veya yol haritası işine bağla.
- Desteği biten bağımlılıkları sıradan borç saymak. Bunlar tarihe bağlı güvenlik ve destek riski taşır; o tarihe göre önceliklendir.

## Örnek
Girdi: "Faturalama platformu: sürümler iki hafta sürüyor, %30 kapsam, desteği bitmiş framework sürümü."

Çıktıdan bir bölüm:
- TD-01 Desteği bitmiş framework (bağımlılıklar, bilinçli/tedbirli): güvenlik yaması yok; anapara 20–40 kişi-gün `[VARSAYIM: benzer yükseltmelere dayanarak]`; faiz: açık güvenlik maruziyeti; öncelik 1, yöntem: bu çeyrek planla.
- TD-02 Fatura hesaplaması etrafında eksik testler (testler, farkında olmadan/pervasız): sürümlerin %70'inde değişen sıcak nokta `[geçmişle teyit et]`; faiz: manuel regresyon her sürüme ~3 gün ekliyor; yöntem: bir sonraki fiyatlama değişikliğiyle birlikte karakterizasyon testleri ekle.
- Süreç düzeltmesi: definition of done'a "değişen mantık için testler" maddesini ekle.
