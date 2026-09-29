---
description: Mühendislik teslimat metriklerini DORA (dağıtım sıklığı, değişiklik teslim süresi, değişiklik hata oranı, geri yükleme süresi) ve SPACE boyutlarıyla inceler, eğilimleri bağlamıyla yorumlar, manipülasyonu ve veri kalitesi sorunlarını tespit eder ve iyileştirme deneyleri önerir. Bir ekip veya organizasyon için metrik incelemesi hazırlanırken, yönetim verimlilik rakamları istediğinde ya da metrikler bireyleri karşılaştırmak için yanlış kullanıldığında kullanılır.
related: cycle-time-analysis, team-health-check, kpi-definition, metric-definition, velocity-analysis
prompt: Dört ekibin son iki çeyreğe ait DORA rakamları burada. İncele ve ekiplerle neleri konuşmam gerektiğini söyle.
---

# Mühendislik Metrikleri İncelemesi (DORA/SPACE)

## Amaç
Teslimat metriklerini, manipüle edilen hedeflere veya kişi sıralamalarına dönüştürmeden, sistem performansına dair dengeli ve bağlamı gözeten bir tabloya çevirmek ve bu tablodan iyileştirme deneyleri çıkarmak.

## Ne zaman kullanılır
- Ekipler veya mühendislik organizasyonu için dönemsel metrik incelemesi yapılacak.
- Yönetim "mühendislik ne kadar verimli" diye soruyor ve sorumlu bir yanıta ihtiyaç var.
- Metrikler keskin şekilde değişti ya da ekipler haksız ölçüldüklerini düşünüyor.

## Ne zaman kullanılmaz
- Tek bir ekibin iş kalemlerinin ayrıntılı akış analizi için `cycle-time-analysis` kullanılır.
- Sıfırdan yeni bir metrik tanımlamak için `metric-definition` veya `kpi-definition` kullanılır.
- Yalnızca ekip morali ve iş birliği için `team-health-check` kullanılır.

## Girdiler
Zorunlu:
- Zaman dönemleri ve kapsadıkları ekipler/servislerle metrik değerleri.

İsteğe bağlı, kaliteyi artırır:
- Metrik tanımları ve veri kaynakları (dağıtım, hata ve geri yükleme olarak ne sayılıyor).
- Bağlam: olaylar, yeniden yapılanmalar, sürüm dondurmaları, taşımalar, kadro değişiklikleri.
- Geliştirici deneyimi anketi sonuçları veya diğer SPACE sinyalleri (memnuniyet, iş birliği).

Metrik tanımları bilinmiyorsa varsaydığın yaygın tanımları yaz ve `[VARSAYIM]` olarak işaretle; tanımları farklı olabilecek ekipleri karşılaştırma.

## Süreç
1. Her metriğin tanımını ve veri kalitesini doğrula (kaynak, hariç tutulanlar, örneklem büyüklüğü); ekipler arasında karşılaştırılamayan metrikleri işaretle.
2. Dört DORA metriğini ekip/servis bazında zaman içinde birlikte sun; hızı asla kararlılık olmadan yorumlama (tersi de geçerli).
3. Tek ortalamalara değil, eğilimlere ve dağılımlara (medyan ve p85/p90) bak; normal dalgalanmadan küçük değişimleri gürültü olarak işaretle.
4. Zaman çizelgesine bağlam olaylarını ekle ve değişimleri kanıtla açıkla; hipotezleri hipotez olarak etiketle.
5. Görünümü dengelemek için aktivitenin ötesinde en az bir SPACE boyutu ekle (memnuniyet/iyi oluş, iş birliği, verimlilik/akış).
6. Manipülasyon ve yan etkileri kontrol et: dağıtımları yapay bölmek, olayları yeniden sınıflandırmak, teslim süresini düşürmek için testleri atlamak, artan nöbet yükü.
7. Birey düzeyinde sıralamayı reddet: Metrikler sistemi anlatır; kişi bazında rakam istenirse riski açıkla ve ekip düzeyinde alternatifler sun.
8. Metrikleri en olası sınırlayan 2-3 darboğazı belirle (ör. manuel onay kapısı, uzun inceleme beklemesi, kararsız testler).
9. Sorumlu rol, beklenen etki, ölçüt ve gözden geçirme tarihiyle iyileştirme deneyleri öner.
10. Ekipler için suçlama değil merak odaklı tartışma soruları hazırla.
11. Kullanıcının hedefi devam ediyorsa bir darboğazı derinleştirmek için `cycle-time-analysis` veya insan tarafı için `team-health-check` öner.

## Çıktı formatı
```markdown
# Mühendislik Metrikleri İncelemesi: <kapsam> – <dönem>

## Tanımlar ve Veri Kalitesi
| Metrik | Kullanılan tanım | Kaynak | Uyarılar |
|---|---|---|---|

## DORA Genel Görünüm
| Ekip / servis | Dağıtım sıklığı | Teslim süresi (medyan/p85) | Değişiklik hata oranı | Geri yükleme süresi | Eğilim |
|---|---|---|---|---|---|

## Aktivitenin Ötesi (SPACE)
- ...

## Yorum
- Gözlem → kanıt → hipotez [etiket]

## Manipülasyon / Yan Etki Kontrolü
- ...

## Olası Darboğazlar
1. ...

## İyileştirme Deneyleri
| Deney | Sorumlu rol | Beklenen etki | Ölçüt | Gözden geçirme tarihi |
|---|---|---|---|---|

## Ekiplere Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Hız ve kararlılık metrikleri her zaman birlikte gösteriliyor.
- [ ] Tanımlar ve veri uyarıları belirtildi; karşılaştırılamayan veriler karşılaştırılmadı.
- [ ] Eğilimler tek nokta ortalamalarıyla değil, dağılım ve bağlamla değerlendirildi.
- [ ] Hipotezler etiketlendi ve kanıttan ayrıldı.
- [ ] Birey düzeyinde sıralama veya kişilere hedef yok.
- [ ] Her iyileştirme deneyinin ölçütü ve gözden geçirme tarihi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Metrikleri hedefe dönüştürmek ("3. çeyrekte günlük dağıtıma ulaş"). Darboğazları hedefle, metrikleri gözlemle.
- Mimarileri ve tanımları farklı ekipleri lig tablosu gibi karşılaştırmak. Her ekibi kendi geçmişiyle karşılaştır.
- Maliyet tarafını görmezden gelmek: Artan nöbet çağrılarıyla gelen hızlı dağıtım bir iyileşme değildir.

## Örnek
Girdi: A ekibinin teslim süresi medyanı iki çeyrekte 6 günden 2 güne, değişiklik hata oranı %8'den %21'e çıkmış.

Çıktıdan bir bölüm:
- Gözlem: Teslim süresi 3 kat iyileşirken değişiklik hata oranı iki katından fazla arttı.
- Hipotez [etiket]: Kaldırılan manuel test kapısının yerine otomatik kontroller konmadı; checkout servisindeki test kapsamı değişmedi (kanıt: pipeline yapılandırması, kapsam raporu).
- Zayıf sonuç (kaçın): "A ekibi artık en hızlı ekip." Güçlü sonuç: "Hız kazanımı gerçek ama henüz güvenli değil; deney: en çok hata veren 3 entegrasyon için sözleşme testleri ekle, hata oranını 6 hafta sonra gözden geçir."
