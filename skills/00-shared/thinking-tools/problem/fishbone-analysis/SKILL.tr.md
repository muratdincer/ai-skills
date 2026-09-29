---
name: fishbone-analysis
description: "Açıkça tanımlanmış bir sonucun tüm makul nedenlerini alana uygun kategorilerde düzenleyen bir Ishikawa (balık kılçığı) diyagramı oluşturur, kanıtlı nedenleri hipotezlerden ayırır ve önce doğrulanmaya değer birkaç nedeni seçer. Bir problemin birden fazla etkileşen nedeni olabileceğinde, ekip nedenler üzerine beyin fırtınası yapıp yapıya ihtiyaç duyduğunda veya en umut verici dallarda 5 Neden çalıştırmadan önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: thinking-tools
  area: problem
  title: "Balık kılçığı analizi"
  related: "problem-statement, five-whys, postmortem, diagram-as-code, assumption-mapping"
  prompt: "Balık kılçığı analizi yap: sürüm teslim süremiz son iki çeyrekte 3 günden 2 haftaya çıktı."
---

# Balık Kılçığı Analizi

## Amaç
Nedenleri daraltmadan önce aramayı genişletmek; böylece ekip aklına gelen ilk nedeni düzeltmekle yetinmez ve sonunda doğrulanacak, kanıta göre sıralanmış kısa bir neden listesi elde eder.

## Ne zaman kullanılır
- Bir kalite, teslimat veya operasyon probleminin muhtemelen birden fazla katkı veren nedeni varsa.
- Nedenler üzerine yapılan grup beyin fırtınası uzun ve dağınık bir liste ürettiyse.
- Önceki tek nedenli düzeltmeler metriği değiştirmediyse.

## Ne zaman kullanılmaz
- Sonuç henüz üzerinde uzlaşılmış veya ölçülebilir değilse önce `problem-statement` kullanılır.
- Net kanıtı olan tek bir nedensel zincir zaten varsa `five-whys` kullanılır.
- Çalışan bir sistemdeki arıza ayıklanıyorsa `debugging-hypotheses` kullanılır.

## Girdiler
Zorunlu:
- Analiz edilecek sonuç (problem), tercihen ölçüsü ve zaman aralığıyla.

İsteğe bağlı, kaliteyi artırır:
- Veri: metrikler, hata veya kayıt kategorileri, zaman çizelgeleri, değişiklik geçmişi.
- Ekibin daha önce dile getirdiği aday nedenler.
- Kurumda kullanılan tercih edilen kategori seti.

Sonuç yoksa iste. Bir çözüm veya neden olarak ifade edilmişse gözlemlenebilir bir sonuç olarak yeniden yaz ve kullanıcıyla teyit et.

## Süreç
1. Sonucu balığın başına gözlemlenebilir, ölçülebilir ve zaman aralığı belli bir ifade olarak yaz ("sürüm teslim süresi 1.-2. çeyrekte 3 günden 14 güne çıktı").
2. Alana uygun 4-7 kategori seç: yazılım teslimatı için örneğin İnsan/Yetkinlik, Süreç, Araç/Platform, Kod/Mimari, Ortam/Altyapı, Gereksinim/Girdi, Ölçüm; hizmet veya üretim için 6M ya da 8P setleri. Kategorileri ekibin diline göre adlandır.
3. Her kategoriyi önce girdideki aday nedenlerle doldur, sonra çıkarımla eklediğin makul nedenleri `[HİPOTEZ]` olarak işaretleyerek ekle.
4. Alt nedenleri eklemek için her nedende bir-iki kez "bu neden oluyor?" diye sor; alt neden kendi analizini gerektirecek noktaya gelince dur.
5. Tekrarları çıkar ve başka kategoriye ait nedenleri taşı; her neden, değiştirilebileceği kategoride yalnızca bir kez yer alır.
6. Her nedenin kanıt durumunu işaretle: Kanıtlı (veri veya kayıt gösterilmiş), Bildirilen (biri söylemiş), Hipotez (çıkarım).
7. Her nedeni sonuca olası etkisi ve doğrulama kolaylığı açısından (Yüksek/Orta/Düşük) tek satırlık gerekçeyle puanla.
8. Önce doğrulanacak 3-5 nedeni seç: önce yüksek etki, sonra doğrulama kolaylığı; her birini neyin doğrulayacağını veya çürüteceğini (veri ya da test) not et.
9. Diyagramı iç içe liste olarak veya istenirse diyagram kodu olarak ver; tabloyu esas kaynak olarak tut.
10. Açık soruları ve gereken verileri listele; ekibin kontrolü dışındaki nedenleri ayrıca belirt.
11. Kullanıcının hedefi devam ediyorsa seçilen nedenler için `five-whys`, görsel için `diagram-as-code`, doğrulamayı planlamak için `assumption-mapping` öner.

## Çıktı formatı
```markdown
# Balık Kılçığı: <sonucun kısa başlığı>

**Sonuç:** <gözlemlenebilir, ölçülebilir, zaman aralığı belli ifade>

## Kategorilere Göre Nedenler
### <Kategori 1>
- <neden> [Kanıtlı | Bildirilen | Hipotez]
  - <alt neden>
### <Kategori 2>
- ...

## Doğrulanacak Öncelikli Nedenler
| # | Neden | Kategori | Kanıt durumu | Etki | Doğrulama kolaylığı | Nasıl doğrulanır |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | Y/O/D | Y/O/D | <veri veya test> |

## Kontrolümüz Dışında
- ...

## Açık Sorular ve Gereken Veriler
- ...
```

## Kalite kontrol listesi
- [ ] Sonuç gözlemlenebilir, ölçülebilir ve neden ya da çözüm içermiyor.
- [ ] Kategoriler alana uygun; gerekçesi belirtilmeden boş bırakılan kategori yok.
- [ ] Her nedenin kanıt durumu var; çıkarımla eklenen nedenler `[HİPOTEZ]` olarak işaretli.
- [ ] Hiçbir neden bir kişi değil; insanla ilgili nedenler yetkinlik, yük veya teşvikleri tarif ediyor.
- [ ] Öncelikli listede her neden için somut bir doğrulama yöntemi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Diyagramı sonuç sanmak. Diyagram adayları listeler; bir şeyi neden yapan yalnızca doğrulamadır.
- Klasik 6M kategorilerini yazılım işine zorla uygulamak. Ekibin aksiyon alabileceği kategoriler kullan.
- En yüksek sesin tek bir kılçığı doldurmasına izin vermek. Sıralamadan önce her kategoride en az bir aday ara.
- Çözümleri neden olarak yazmak ("otomatik test yok"). Durumu yaz ("regresyonlar yalnızca manuel UAT'de bulunuyor").

## Örnek
Girdi: "Sürüm teslim süremiz son iki çeyrekte 3 günden 2 haftaya çıktı."

Çıktıdan bir bölüm:
- Süreç: değişiklik onay kurulu haftalıktan iki haftada bire geçti [Bildirilen]
- Araç/Platform: ortak staging ortamı diğer ekiplerin testleri yüzünden bloke oluyor [Hipotez]
- Kod/Mimari: iki ekip aynı repoda çalışmaya başladıktan sonra merge çakışmaları arttı [Kanıtlı – merge request verisi]

| # | Neden | Etki | Kolaylık | Nasıl doğrulanır |
|---|---|---|---|---|
| 1 | İki haftada bir toplanan onay kurulu | Y | Y | Değişiklik öncesi ve sonrası sürüm başına onay bekleme süresini karşılaştır |
