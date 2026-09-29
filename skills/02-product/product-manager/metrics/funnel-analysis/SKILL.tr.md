---
description: Bir dönüşüm hunisini adım adım analiz eder; adım ve kümülatif dönüşümü hesaplar, en büyük mutlak kayıpları bulur, bunları segmentlere ayırır, veri kaynaklı sapmaları gerçek davranıştan ayırır ve bulguları sıralanmış, test edilebilir iyileştirme hipotezlerine dönüştürür. Kayıt, onboarding, ödeme veya aktivasyon için huni sayıları ya da olay verisi verildiğinde veya biri "kullanıcıları nerede kaybediyoruz ve neden" diye sorduğunda kullanılır.
related: experiment-design, hypothesis-statement, customer-journey-map, north-star-metric, data-exploration
prompt: Geçen ayın adım ve cihaz bazında kayıt hunisi sayıları burada; kullanıcıları nerede kaybettiğimizi ve ne denememiz gerektiğini bul.
---

# Huni Analizi

## Amaç
Kullanıcıların tanımlı bir yolculuktan nerede ve hangi segmentte düştüğünü bulmak, gerçek davranışı ölçüm sorunlarından ayırmak ve karar içermeyen bir grafik yerine kısa, sıralanmış, test edilebilir bir hipotez listesi üretmek.

## Ne zaman kullanılır
- Kayıt, onboarding, aktivasyon, ödeme veya paket yükseltme için adım sayıları ya da olay verisi varsa.
- Bir dönüşüm KPI'ı düştüyse veya yerinde sayıyorsa ve ekip nereye bakacağını bilmek istiyorsa.
- Bir akış üzerinde hangi deneyin yapılacağı seçilmeden önce.

## Ne zaman kullanılmaz
- Henüz veri yoksa ve ekip nitel deneyimi anlamak istiyorsa `customer-journey-map` veya `research-synthesis` kullanılır.
- Bir deney sonucu değerlendirilecekse `ab-test-analysis` kullanılır.
- Veri tanınmıyorsa ve önce profillenmesi gerekiyorsa `data-exploration` kullanılır.

## Girdiler
Zorunlu:
- Huni tanımı (sıralı adımlar ve her adımı işaretleyen olay) ve bir dönem için adım başına sayılar ya da bunları türetecek ham veri.

İsteğe bağlı, kaliteyi artırır:
- Segment kırılımları (cihaz, kanal, ülke, yeni/geri dönen, paket), önceki dönemler.
- Adımlar arası süre, nitel geri bildirim, yakın zamandaki sürümler veya kampanyalar.

Adım tanımları veya sayılar yoksa sor. Asla sayı uydurma; yalnızca verilen veriden hesapla ve hesabı göster.

## Süreç
1. Huni tanımını teyit et: giriş olayı, her adımın olayı, sıralama (katı veya serbest), dönüşüm penceresi ve birim (kullanıcı, oturum, hesap). Kullanıcı ve oturum seviyesi adımlar karışmışsa not et.
2. Yorumlamadan önce veriyi doğrula: sayılar huni boyunca artmamalı (adımlar sırasız değilse), dönem ve filtreler eşleşmeli, bot/test trafiği hariç tutulmalı, dönem civarındaki ölçüm değişiklikleri kontrol edilmeli. Şüpheli sapmaları ayrı işaretle.
3. Adım dönüşümünü (adım n ÷ adım n-1), kümülatif dönüşümü (adım n ÷ giriş) ve adım başına kaybedilen mutlak kullanıcıyı hesapla. Aritmetiği göster.
4. Kayıpları kaybedilen mutlak kullanıcıya ve varsa verilen kıyaslama veya önceki döneme uzaklığa göre sırala; en büyük yüzde düşüş her zaman en büyük fırsat değildir.
5. İlk 2-3 kaybı segmentlere ayır (cihaz, kanal, yeni/geri dönen, coğrafya, paket). Dönüşümü çok daha kötü olan segmentleri veya büyük hacim kaymalarını (karışım etkisi) ara.
6. Zamanlama verisi varsa dönüşüm süresini incele: uzun aralıklar sürtünmeye veya dış bağımlılıklara (e-posta doğrulama, belge yükleme, onay) işaret eder.
7. Verildiyse nitel sinyallerle (geri bildirim, oturum notları, destek kayıtları) birleştir; kanıtla desteklenmeyen her nedensel açıklamayı `[VARSAYIM]` olarak işaretle.
8. Her kayıp için hipotez yaz: "<kanıt> nedeniyle, <segment> için <değişiklik> yapılmasının <adım dönüşümünü> artıracağına inanıyoruz". Etki (etkilenen kullanıcı × makul artış), güven ve efora göre sırala.
9. Sonraki aksiyonları öner: veri şüpheliyse önce ölçüm düzeltmeleri, ardından her biri için başarı metriği ve koruma metriğiyle ilk 1-3 deney veya hızlı düzeltme.
10. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: en üstteki hipotezi keskinleştirmek için `hypothesis-statement`, test etmek için `experiment-design`, nitel araştırma için `customer-journey-map`.

## Çıktı formatı
```markdown
# Huni Analizi: <huni> · <dönem> · birim: <kullanıcı/oturum/hesap>

## Veri Kontrolleri
- ... (işaretlenen sapmalar, uygulanan hariç tutmalar)

## Huni
| Adım | Sayı | Adım dönüşümü | Kümülatif | Kaybedilen kullanıcı |
|---|---|---|---|---|

## En Büyük Kayıplar
1. <adım> – <kaybedilen kullanıcı>, <önceki dönem/kıyaslamaya göre dönüşüm> – segmentler: <...>

## Segment Bulguları
| Segment | Adım | Dönüşüm | Genele göre | Hacim |
|---|---|---|---|---|

## Hipotezler (sıralı)
| # | Hipotez | Kanıt | Etki | Güven | Efor |
|---|---|---|---|---|---|

## Önerilen Sonraki Aksiyonlar
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Huni birimi, sıralaması ve dönüşüm penceresi belirtildi.
- [ ] Veri geçerlilik kontrolleri yapıldı ve sapmalar davranıştan ayrıldı.
- [ ] Tüm sayılar verilen veriden, görünür aritmetikle hesaplandı; hiçbir şey uydurulmadı.
- [ ] Kayıplar yalnızca yüzdeye göre değil, mutlak etkiye göre sıralandı.
- [ ] Her nedensel açıklama `[VARSAYIM]` olarak etiketli ya da gösterilen kanıtla destekli.
- [ ] Önerilen her aksiyonun bir başarı metriği ve koruma metriği var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Trafik karışımı farklı dönemleri karşılaştırıp bunu dönüşüm değişimi saymak. Sonuca varmadan önce segmentlere ayır.
- Adımlar arasında oturum ve kullanıcı sayılarını karıştırmak. Baştan sona tek birim kullan.
- Bir kayıptan doğrudan yeniden tasarıma atlamak. Çıktı test edilecek hipotezlerdir, hüküm değil.

## Örnek
Girdi: "Geçen ay kayıt hunisi: açılış sayfası 40.000 → form başlangıcı 12.000 → form gönderimi 7.200 → e-posta doğrulandı 4.300 → ilk proje 2.150; mobil/masaüstü kırılımı verildi."

Çıktıdan bir bölüm:
| Adım | Sayı | Adım dön. | Kümülatif | Kayıp |
|---|---|---|---|---|
| E-posta doğrulandı | 4.300 | %59,7 | %10,8 | 2.900 |
| İlk proje | 2.150 | %50,0 | %5,4 | 2.150 |
- Girişten sonraki en büyük kayıp açılış → form başlangıcı (28.000), ancak niyet farkını içeriyor; kontrol edilebilir en büyük kayıp gönderim → doğrulama (2.900).
- Hipotez `[VARSAYIM]`: mobil kullanıcılar e-postayı kontrol etmek için uygulamadan çıkıyor ve geri dönmüyor; mobilde doğrulamayı ertelemeye izin vermek gönderim → ilk proje dönüşümünü artırır.
