---
description: Proje kapsamını numaralı bir iş paketi hiyerarşisine bölen, teslimat odaklı bir iş kırılım yapısı (WBS) ve açıklama, sahip, kabul ve bağımlılıkları içeren WBS sözlüğü oluşturur. Kapsam üzerinde anlaşıldığında ve tahmin, takvim, kaynak planlama ve ilerleme takibi için bölünmesi gerektiğinde kullanılır.
related: scope-statement, estimation-three-point, schedule-plan, resource-plan, task-breakdown
prompt: Bu kapsam tanımını kullanarak mobil bankacılık uygulaması yeniden tasarımı için WBS oluştur.
---

# İş Kırılım Yapısı (WBS)

## Amaç
Tüm proje kapsamını yönetilebilir, tahmin edilebilir ve atanabilir iş paketlerine bölmek; böylece kapsamdaki hiçbir şey atlanmaz ve kapsam dışı hiçbir iş planlanmaz.

## Ne zaman kullanılır
- Kapsam tanımı üzerinde anlaşıldıktan sonra, tahmin ve takvimden önce.
- Bir plan var ama işler belirsiz veya ekipler arasında çakışıyorsa.
- Teklif veya bütçe için aşağıdan yukarı tahmin hazırlanırken.

## Ne zaman kullanılmaz
- Tek bir kullanıcı hikayesini geliştirici görevlerine bölmek için `task-breakdown` kullanılır.
- Epic'leri backlog öğelerine bölmek için `epic-breakdown` kullanılır.
- Kapsam henüz netleşmemişse önce `scope-statement` kullanılır.

## Girdiler
Zorunlu:
- Kapsam tanımı, teslimat listesi veya eşdeğer bir açıklama.

İsteğe bağlı, kaliteyi artırır:
- Kurumsal WBS şablonları, standart fazlar, yaşam döngüsü modeli.
- Ekip yapısı, tedarikçiler, sözleşme sınırları.

Teslimat açıklaması yoksa iste.

## Süreç
1. 1. seviyeyi proje, 2. seviyeyi ana teslimatlar olarak kur (kurum gerektiriyorsa fazlara göre; her seviyede tek bir ilke kullan).
2. Her zaman bir Proje Yönetimi dalı (planlama, yönetişim, raporlama, kapanış) ve kesişen işleri (test, veri taşıma, eğitim, dağıtım, hypercare) ekle.
3. Her iş paketi bağımsız tahmin edilebilir, tek bir sahibe atanabilir ve bir raporlama dönemine sığar hale gelene kadar böl (kural: 8-80 saat veya en fazla bir iterasyon).
4. Öğeleri fiil değil isim/teslimat olarak adlandır.
5. %100 kuralını uygula: alt öğeler üst öğenin kapsamını tam olarak karşılar; kapsam dışı iş yoktur.
6. Öğeleri hiyerarşik numaralandır (1, 1.1, 1.1.1).
7. Her iş paketi için WBS sözlüğü girdisi yaz: açıklama, kabul, sahip rolü, temel bağımlılıklar, varsayımlar.
8. Belirsizliği yüksek paketleri üç noktalı tahmin için işaretle.
9. Her kapsam teslimatını en az bir iş paketine izle ve boşlukları listele.

## Çıktı formatı
```markdown
# WBS: <proje>
## Hiyerarşi
1 <Proje>
  1.1 Proje Yönetimi
    1.1.1 Planlama ve baz çizgisi
  1.2 <Teslimat A>
    1.2.1 <İş paketi>
## WBS Sözlüğü
| WBS No | Ad | Açıklama | Kabul | Sahip rolü | Bağımlılıklar | Belirsizlik |
## Kapsam İzlenebilirliği
| Kapsam teslimatı | WBS No'ları |
## Boşluklar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] %100 kuralı her seviyede sağlanıyor.
- [ ] Tüm öğeler isim; paket seviyesinde faaliyet fiili yok.
- [ ] Proje yönetimi, test, veri taşıma, eğitim ve dağıtım mevcut ya da açıkça hariç tutulmuş.
- [ ] Her iş paketinin tek bir sahip rolü ve kabulü var.
- [ ] Her kapsam teslimatı bir pakete izlenebiliyor.

## Sık yapılan hatalar
- Aynı seviyede organizasyon birimlerini, fazları ve teslimatları karıştırmak. Her seviyede tek bir bölme ilkesi seç.
- Fazla derine inip WBS'i görev listesine çevirmek. İş paketinde dur.
- Entegrasyon ve fonksiyonel olmayan işleri unutmak; bunlar sonradan plansız efor olarak ortaya çıkar.

## Örnek
Girdi: "Mobil bankacılık yeniden tasarımı: yeni giriş, gösterge paneli, transferler; erişilebilirlik uyumu."

Çıktıdan bir bölüm:
1.3 Transfer modülü
  1.3.1 Transfer arayüz tasarımları (onaylı)
  1.3.2 Transfer API uyarlamaları
  1.3.3 Transfer test paketi ve sonuçları
1.6 Erişilebilirlik uyumu (WCAG 2.2 AA denetim raporu)
- Boşluk: Uygulama mağazası sürüm yönetimi kapsamda mı?
