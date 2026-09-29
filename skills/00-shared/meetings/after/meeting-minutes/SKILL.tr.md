---
description: Toplantı bilgileri, katılım ve yeter sayı, sırasıyla gündem maddeleri, özlü görüşme kayıtları, oylama veya onay sonucuyla numaralandırılmış kararlar, aksiyonlar ve onay imzalarını içeren resmi toplantı tutanağı oluşturur. Yönlendirme komiteleri, yönetim kurulları, değişiklik danışma kurulları, denetimler, sözleşmesel veya tedarikçi toplantıları ya da kaydın kanıt olarak kullanılabileceği her durumda kullanılır.
related: meeting-notes, meeting-summary, decision-log, steering-committee-pack, audit-preparation
prompt: Dünkü proje yönlendirme komitesi için bu notlardan resmi tutanak yaz; iki değişiklik talebi onaylandı, biri ertelendi.
---

# Resmi Toplantı Tutanağı Yazma

## Amaç
Resmi bir toplantının kimlerin katıldığını, neyin görüşüldüğünü ve neye karar verildiğini gösteren doğru, tarafsız ve onaylanabilir kaydını oluşturmak. Böylece tutanak yönetişim veya sözleşme kanıtı olarak kullanılabilir.

## Ne zaman kullanılır
- Yönlendirme komitesi, yönetim kurulu, değişiklik danışma kurulu, tedarikçi veya sözleşme yönetişimi toplantılarında.
- Sonuçlarının denetlenebilir olması gereken toplantılarda (uyum, bütçe onayı, kabul).
- Kurum veya sözleşme imzalı ya da onaylı tutanak gerektiriyorsa.

## Ne zaman kullanılmaz
- Okunabilir bir kaydın yeterli olduğu iç çalışma toplantılarında `meeting-notes` kullanılır.
- Yöneticiler için kısa bir sonuç özeti gerekiyorsa `meeting-summary` kullanılır.

## Girdiler
Zorunlu:
- Toplantının notları, dökümü veya kayıt özeti.
- Toplantı türü ve tarihi.

İsteğe bağlı:
- Rolleriyle katılım listesi, yeter sayı kuralı, gündem, önceki tutanak, kurumun tutanak şablonu, karar numaralandırma şeması.

Katılım veya yeter sayı kuralları yoksa `[BİLİNMİYOR]` olarak kaydet ve dağıtımdan önce teyit edilecekler listesine ekle.

## Süreç
1. Başlığı doldur: kurul/toplantı adı, toplantı numarası, tarih, başlangıç ve bitiş saati, yer/ortam, başkan, raportör.
2. Katılımı üç grupta kaydet: katılanlar (rolüyle), mazeretli/katılmayanlar, belirli maddeler için davetliler. Kural varsa yeter sayı durumunu belirt.
3. Gündemde varsa önceki tutanağın onayını ve takip eden konuların durumunu kaydet.
4. Gündem sırasını izle. Her madde için: sunan kişi, görüşülen belgeler, tartışmanın 2-5 satırlık tarafsız özeti ve sonuç.
5. Sonuçları resmi ve açık ifade et: "Kurul ... onayladı", "Kurul ... koşuluyla ... erteledi", "Kurul ... bilgisine sunuldu". Uygunsa oyları veya muhalefet şerhini kaydet.
6. Kararları daha sonra atıf yapılabilecek şekilde numaralandır (ör. YK-2026-07/K1).
7. Beyan edilen çıkar çatışmalarını ve bir madde için toplantıdan ayrılan üyeleri kaydet.
8. Aksiyonları sorumlu ve tarihle listele; her birini ilgili gündem maddesine bağla.
9. Üçüncü şahıs ve tarafsız dil kullan; kurul gerektirmedikçe görüş, sıfat veya birebir argüman yazma.
10. Bir sonraki toplantı tarihini ve onay bölümünü (başkan imzası/onay tarihi) ekle.
11. Dağıtımdan önce teyit edilecekleri listele (isimlerin yazımı, rakamlar, karar metinleri).

## Çıktı formatı
```markdown
# Tutanak – <kurul/toplantı adı> No. <n>
Tarih: <tarih>  Saat: <başlangıç–bitiş>  Yer: <yer/çevrim içi>
Başkan: <isim>  Raportör: <isim>
Katılanlar: <isim – rol>; ...
Mazeretliler: <...>   Davetliler: <isim – madde>
Yeter sayı: <sağlandı / sağlanmadı / [BİLİNMİYOR]>

## 1. Önceki tutanak ve takip eden konular
<dağıtıldığı şekliyle / değişikliklerle onaylandı>

## 2. <Gündem maddesi>
Sunan: <isim>. Belgeler: <ref>.
Görüşme: <tarafsız özet>
Karar <No>: <Kurul> <onayladı/reddetti/erteledi/bilgi edindi> <...>. <Varsa oy/muhalefet şerhi>

## Aksiyonlar
| # | Aksiyon | Sorumlu | Tarih | Madde |
## Sonraki toplantı: <tarih veya [TBD]>
Başkan onayı: ____________  Tarih: ______
## Dağıtımdan önce teyit edilecekler
- ...
```

## Kalite kontrol listesi
- [ ] Katılım, mazeretler ve yeter sayı kaydedilmiş veya işaretlenmiş.
- [ ] Her gündem maddesinin açık bir sonucu var (onay, ret, erteleme, bilgi).
- [ ] Kararlar numaralı ve metinleri net.
- [ ] Dil tarafsız ve üçüncü şahıs; kişisel görüş yok.
- [ ] Rakamlar, tarihler ve isimler kaynakla uyumlu; boşluklar `[BİLİNMİYOR]` ile işaretli.
- [ ] Sonraki toplantı ve onay bölümü mevcut.

## Sık yapılan hatalar
- Döküm yazmak. Tutanak her argümanı değil, neye karar verildiğini ve temel gerekçeyi kaydeder.
- "Konu daha sonra görüşülecek" gibi muğlak sonuçlar. Her maddenin resmi bir durumu olmalı.
- Başkan onayı olmadan dağıtmak; hatalar resmi kayda dönüşür. Teyit listesini ekle.

## Örnek
Girdi: Yönlendirme komitesi notları: DT-14 ve DT-15 onaylandı, DT-16 maliyet tahminine kadar ertelendi.

Çıktıdan bir bölüm:
Karar YK-07/K2: Kurul, bütçe etkisinin mevcut yedek bütçe içinde karşılanması koşuluyla DT-15'i (SSO entegrasyonu) onayladı.
Karar YK-07/K3: Kurul, tedarikçiden maliyet tahmini gelene kadar DT-16'yı erteledi. `[tarih BİLİNMİYOR]`
