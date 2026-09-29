---
description: "Kodu mevcut testleriyle karşılaştırarak test edilmemiş yolları bulur: dalları, sınırları, hata işleyicilerini, durum geçişlerini ve gereksinim kurallarını sıralar, her birini kapsayan testlerle eşler, boşlukları ve zayıf testleri (assertion'sız, aşırı mock'lu, yalnızca mutlu yol) işaretler ve eklenecek somut testle birlikte riske göre sıralar. Testlerde neyin eksik olduğu sorulduğunda, kapsam anlamlı biçimde artırılmak istendiğinde, bir pull request'in testleri incelendiğinde ya da elde bir kapsam raporu olup hangi boşlukların önemli olduğu bilinmek istendiğinde kullanılır."
related: "unit-test-writing, integration-test-writing, code-review, regression-selection, risk-based-testing"
prompt: "InvoiceService ve test sınıfı burada. Hangi yollar test edilmemiş ve hangi boşluklar en önemli?"
---

# Test Edilmemiş Yolları Bulma

## Amaç
Bir kod parçasının hangi davranışlarının testlerle korunmadığını ve hangi mevcut testlerin yanıltıcı bir güven verdiğini riske göre sıralı ve kesin biçimde göstermek. Böylece ekip bir kapsam yüzdesinin peşinden koşmak yerine önemli olan birkaç testi ekler.

## Ne zaman kullanılır
- Bir pull request kod ekliyor veya değiştiriyorsa ve testlerin yeterliliği kontrol edilmeliyse.
- Bir kapsam raporu var ama ekip kapsanmayan satırlardan hangilerinin önemli olduğunu bilmiyorsa.
- Kod refactor edilmek üzereyse ya da sık hata çıkan bir kaynaksa.

## Ne zaman kullanılmaz
- Bilinen bir davranış için testler hemen yazılacaksa `unit-test-writing` veya `integration-test-writing` kullanılır.
- Soru bir değişiklik için hangi mevcut testlerin koşturulacağıysa `regression-selection` kullanılır.
- Değişikliğin tam incelemesi (tasarım, güvenlik, okunabilirlik) gerekiyorsa `code-review` kullanılır.

## Girdiler
Zorunlu:
- İncelenecek kod ve mevcut testleri (ya da test olmadığı bilgisi).

İsteğe bağlı, kaliteyi artırır:
- Gereksinimler veya kabul kriterleri, satır/dal kapsam raporu, hata geçmişi, değişiklik sıklığı, bilinen kritik yollar.

Testler verilmemişse iste; testler olmadan aday testleri listele ama kapsam durumunu `[BİLİNMİYOR]` olarak belirt. Kapsam yüzdeleri kod okunarak asla tahmin edilmez.

## Süreç
1. Kodun göstermesi gereken davranışları sırala: verilmişse gereksinimlerden, ayrıca kodun kendisinden (her dal, döngü sınırı, koruma koşulu, catch bloğu, erken dönüş, durum geçişi, yapılandırma anahtarı). Koddan çıkarılan davranışları niyet açısından `[VARSAYIM]` olarak etiketle.
2. Satır kapsamının kaçırdığı gizli yolları listele: kısa devre koşulları (`a && b` içinde her terimin belirleyici olduğu durumlar), varsayılan ve fall-through durumları, null/boş koleksiyonlar, işbirlikçilerin fırlattığı istisnalar, yeniden denemeler ve zaman aşımları, eşzamanlılık ve sıralama, zamana bağlı mantık (ay sonu, artık gün, saat dilimi, yaz saati).
3. Her davranışı onu çalıştıran ve sonucunu gerçekten doğrulayan mevcut testlerle eşle. Bir yolu çalıştırıp sonucunu doğrulamayan test onu kapsamaz.
4. Mevcut testleri yanıltıcı güven açısından değerlendir: eksik veya önemsiz assertion'lar, sonuç yerine mock'lar üzerinde doğrulama, çıktıdan kopyalanmış beklentiler, devre dışı bırakılmış veya atlanan testler, paylaşılan durum, yalnızca mutlu yol girdileri.
5. Her davranışı kanıtıyla (test adı veya satır referansı) sınıflandır: KAPSANDI, ZAYIF (çalıştırılıyor ama doğru doğrulanmıyor ya da sınırın yalnızca bir tarafı test ediliyor) veya BOŞLUK (hiç çalıştırılmıyor).
6. Boşlukları riske göre sırala: yanlış olursa etki (para, veri bütünlüğü, güvenlik, uyum, kullanıcıya görünürlük), olasılık (karmaşıklık, değişiklik sıklığı, hata geçmişi) ve başka yerde yakalanabilirlik. Satır sayısına göre sıralama.
7. Her yüksek ve orta boşluk için somut bir test öner: ad, girdi, beklenen sonuç, seviye (birim veya entegrasyon). Doğru sonuç gereksinimlerden anlaşılmıyorsa tahmin etmek yerine açık soru olarak yaz.
8. Test edilmesi zor kodu (gizli bağımlılıklar, statik zaman, global durum) ve onu test edilebilir kılacak en küçük dikiş noktasını (seam) not et.
9. Eşleme sırasında bulunan ölü veya erişilemeyen kodu test edilecek değil, kaldırılacak aday olarak işaretle.
10. Özetle: sınıf başına sayılar, en önemli boşluklar ve değişikliğin birleştirme için yeterince test edilip edilmediği.
11. Hedef devam ediyorsa önerilen testleri yazmak için `unit-test-writing` veya `integration-test-writing`, bulguları bir pull request incelemesine katmak için `code-review` öner.

## Çıktı formatı
```markdown
# Test Boşluğu Analizi: <birim veya değişiklik>
Girdiler: <kod, testler, kapsam raporu?, gereksinimler?> · Varsayımlar: <liste veya yok>
Özet: KAPSANDI <n> · ZAYIF <n> · BOŞLUK <n> · Karar: <yeterli / birleştirmeden önce test ekle>

## Davranış Haritası
| # | Davranış / yol | Kaynak | Durum | Kanıt | Risk |
|---|---|---|---|---|---|
| 1 | İndirim en fazla %50 | KK-3 | BOŞLUK | tavan dalına giren test yok (S42) | Yüksek |

## Önerilen Testler (riske göre)
| # | Test adı | Girdi | Beklenen | Seviye |

## Zayıf Testler
- <test> — <sorun> — <düzeltme>

## Test Edilebilirlik Sorunları ve Ölü Kod
- ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Koddaki her dal, hata işleyici ve sınır davranış haritasında yer alıyor.
- [ ] Her durumun kanıtı var; çalıştırılıp doğrulanmayan yollar KAPSANDI değil ZAYIF.
- [ ] Boşluklar satır sayısına göre değil etki ve olasılığa göre sıralandı.
- [ ] Önerilen her testin somut girdisi ve beklenen sonucu var ya da kuralın belirsiz olduğu yerde açık soru yazıldı.
- [ ] Kapsam rakamı veya amaçlanan davranış uydurulmadı; çıkarımlar `[VARSAYIM]` olarak etiketlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Satır kapsamını davranış kapsamı saymak; assertion'sız bir testin geçtiği satır hiçbir şey kanıtlamaz.
- Yuvarlama veya yetkilendirme dalı test edilmeden kalırken yüzdeyi artırmak için getter'lara ve önemsiz eşlemelere test önermek.
- Boşluklar için beklenen değerleri mevcut koddan yazmak; tek kaynak kodsa beklenti teyit edilmesi gereken bir varsayımdır.

## Örnek
Girdi: İndirim, vergi ve para birimi yuvarlaması içeren `InvoiceService.calculateTotal`; testler tek bir standart faturayı kapsıyor.

Çıktıdan bir bölüm:
- BOŞLUK (Yüksek): %50 indirim tavanı dalına hiç girilmiyor. Test `tavani_asan_indirim_yuzde_50_ile_sinirlanir`: %70 indirim → %50 uygulanır.
- ZAYIF (Yüksek): `calculates_total` yalnızca `total != null` doğruluyor. Düzeltme: vergi dahil tam tutarı doğrula.
- BOŞLUK (Orta): ondalıksız para birimi yuvarlama yolu. Beklenen yuvarlama modu `[BİLİNMİYOR]` → finansa açık soru.
- Ölü kod: zaten istisna fırlatan bir korumadan sonra gelen `if (items == null)`; test etmek yerine kaldır.
