---
description: "Görev, hedef alanlar, kaynaklar, yoklanacak riskler, test sezgisel yöntemleri ve kâhinler (oracle), süre sınırı ve not, hata ve sorular için bir değerlendirme şablonu içeren oturum bazlı keşif testi görev tanımları yazar. Yeni veya değişen bir özellik için keşif testi gerektiğinde, senaryolu testler henüz yokken veya yetmediğinde ya da keşif testi fikirleri istendiğinde kullanılır."
related: test-scenarios-from-requirements, risk-based-testing, bug-report, heuristic-evaluation, test-summary-report
prompt: "CSV'den toplu ürün fiyatı içe aktarma özelliği için keşif testi görev tanımları yaz. Bir öğleden sonra için 2 test uzmanımız var."
---

# Keşif Testi Görev Tanımı

## Amaç
Keşif testine net bir görev ve sınırlar vermek. Böylece oturumlar riske odaklanır, sonuçlar raporlanabilir olur ve kapsam tartışılabilir; test uzmanının öğrenme ve uyum sağlama özgürlüğü de korunur.

## Ne zaman kullanılır
- Yeni veya ciddi biçimde değişmiş bir özellik, senaryolu testlerden önce veya onlarla birlikte hızlı geri bildirim istiyor.
- Gereksinimler zayıf ve ekibin ürünün gerçek davranışını öğrenmesi gerekiyor.
- Yüksek riskli alanlar, mevcut regresyon case'lerinden farklı bir bakış açısı istiyor.

## Ne zaman kullanılmaz
- Regresyon için tekrarlanabilir senaryolu case'ler gerekiyorsa `test-case-writing` kullanılır.
- Sezgisel ilkelere göre uzman kullanılabilirlik incelemesi gerekiyorsa `heuristic-evaluation` kullanılır.
- Sürüm genelinde önce neyin test edileceğine karar verilecekse `risk-based-testing` kullanılır.

## Girdiler
Zorunlu:
- Keşfedilecek özellik veya alan ve neyin değiştiği.

İsteğe bağlı, kaliteyi artırır:
- Mevcut kişiler ve süre, bilinen riskler, son hatalar, kullanıcı profilleri, ortam ve veri.
- Tekrarı önlemek için mevcut senaryolu kapsam.

Keşfedilecek alan bilinmiyorsa iste. Diğer her şey varsayılıp `[VARSAYIM]` ile işaretlenebilir.

## Süreç
1. Alan için önemli olan riskleri ve kalite özelliklerini belirle (veri bütünlüğü, hata yönetimi, hacimde performans, güvenlik, kullanılabilirlik).
2. Alanı her biri 45-120 dakikalık, her birinde tek görev olan görev tanımlarına böl; "<hedef>i <kaynaklar> ile keşfet ve <bilgi/risk>i ortaya çıkar" kalıbını kullan.
3. Her görev tanımı için odak alanlarını ve açıkça kapsam dışı olanları listele.
4. Fikirleri yönlendirecek sezgisel yöntemler seç; ör. SFDIPOT (yapı, fonksiyon, veri, arayüzler, platform, operasyonlar, zaman), CRUD, sınırlar, kesintiler, "goldilocks" (çok büyük, çok küçük, tam kararında), değişken veri (kodlamalar, yerel ayarlar), veriyi takip et.
5. Kâhinleri tanımla: test uzmanı bir sorunu nasıl tanır (spesifikasyon, benzer ürün, diğer ekranlarla tutarlılık, kullanıcı beklentileri, loglar, veritabanı durumu).
6. Kaynakları listele: test hesapları, örnek dosyalar, araç kategorileri (proxy, log görüntüleyici), veri setleri. Yalnızca sentetik veri kullan.
7. Görev tanımlarını beceri ve riske göre test uzmanlarına ata; riske göre sırala.
8. Oturum notu şablonu ver: zaman damgaları, test edilenler, fikirler, hatalar, sorular, görev içi / hazırlık / hata inceleme süre yüzdeleri.
9. Oturum sonrası değerlendirme soruları ver: ne kapsandı, ne kapsanmadı, hangi yeni riskler çıktı, takip görev tanımı gerekiyor mu.

## Çıktı formatı
```markdown
# Keşif Testi Görev Tanımları: <özellik>
| # | Görev (Keşfet / ile / ortaya çıkar) | Odak | Kapsam dışı | Sezgisel yöntemler | Kâhinler | Süre | Test uzmanı |
|---|---|---|---|---|---|---|---|

## Kaynaklar ve Veri
## Oturum Notu Şablonu
- Görev #, test uzmanı, başlangıç/bitiş
- Kapsanan / kapsanmayan alanlar
- Hatalar (ID'ler) · Sorunlar/sorular · Yeni görev fikirleri
- Süre dağılımı: hazırlık % / test % / hata inceleme %
## Değerlendirme Soruları
```

## Kalite kontrol listesi
- [ ] Her görev tanımının tek bir görevi var ve süre sınırına sığıyor.
- [ ] Görev tanımları riske göre sıralı ve senaryolu testlerin kapsamadığı alanları kapsıyor.
- [ ] Her görev tanımı en az bir sezgisel yöntem ve bir kâhin belirtiyor.
- [ ] Test verisi sentetik veya maskelenmiş.
- [ ] Değerlendirme, kapsamı ve yeni riskleri raporlanabilir kılıyor.

## Sık yapılan hatalar
- Çok geniş görev tanımları ("uygulamayı keşfet"). Bir hedefe ve bir riske daralt.
- Görev tanımlarını adım listesi olarak yazmak. Görev olarak tut; adımlar keşfi öldürür.
- Değerlendirmeyi atlamak; bulgular ve kapsam kaybolur.

## Örnek
Girdi: "CSV'den toplu ürün fiyatı içe aktarma; 2 test uzmanı, bir öğleden sonra."

Çıktıdan bir bölüm:
| 1 | CSV ayrıştırmayı bozuk ve uç dosyalarla keşfet ve veri bozulmasını veya sessizce atlanan satırları ortaya çıkar | kodlamalar (UTF-8 BOM, Windows-1254), ayırıcılar, tırnaklar, 0/negatif fiyatlar | Arayüz görünümü | Goldilocks, değişken veri | DB'deki fiyat dosyadaki değere eşit; içe aktarma özeti sayıları | 90 dk | Test uzmanı A |
| 2 | Kısmi hata ve yeniden içe aktarmayı keşfet ve tekrarlanan veya kaybolan fiyat güncellemelerini ortaya çıkar | 10.000 satırın 5.000'incisi hata verir, aynı dosya yeniden yüklenir | | Kesintiler, veriyi takip et | Denetim kaydı, fiyat geçmişi | 90 dk | Test uzmanı B |
