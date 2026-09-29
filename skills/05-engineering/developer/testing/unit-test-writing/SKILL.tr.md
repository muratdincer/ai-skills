---
description: "Bir fonksiyonun, sınıfın veya modülün gözlemlenebilir davranışını Arrange-Act-Assert yapısında sabitleyen birim testleri yazar; mutlu yolu, denklik sınıflarını, sınır değerleri, hata yollarını ve durum geçişlerini kapsar, test dublörlerini yalnızca gerçek sınırlarda kullanır ve test adlarını birer şartname gibi yazar. Birim testi yazma, ekleme veya iyileştirme, belirli bir kodun kapsamını artırma ya da değişiklikten önce kodu güvence altına alma istendiğinde kullanılır."
related: "tdd-cycle, test-gap-finder, integration-test-writing, equivalence-boundary-analysis, refactoring"
prompt: "Bu ShippingCostCalculator sınıfı için birim testleri yaz; ağırlık kademeleri, belli tutarın üzerinde ücretsiz kargo ve ekspres ek ücreti kuralları var."
---

# Birim Testi Yazma

## Amaç
Kodun ne yaptığını çağıranın bakış açısından tarif eden hızlı ve deterministik birim testleri üretmek. Böylece regresyonlar anlaşılır bir mesajla açıkça kırılır ve kod, testler yeniden yazılmadan refactor edilebilir.

## Ne zaman kullanılır
- Yeni veya mevcut kodun davranışı, kuralları ve uç durumları için test gerektiğinde.
- Bir değişiklik veya refactoring planlandığında ve mevcut davranışın önce güvence altına alınması gerektiğinde.
- Bir hata düzeltildiğinde ve düzeltme olmadan kırılan bir regresyon testi gerektiğinde.

## Ne zaman kullanılmaz
- Davranış gerçek altyapıyı (veritabanı, mesaj kuyruğu, HTTP) aşıyorsa `integration-test-writing` kullanılır.
- Kod henüz yoksa ve testlerle yönlendirilmesi isteniyorsa `tdd-cycle` kullanılır.
- Soru testlerin yazılması değil, hangi yolların test edilmediğiyse `test-gap-finder` kullanılır.

## Girdiler
Zorunlu:
- Test edilecek kod (veya imzası ve beklenen davranışı).

İsteğe bağlı, kaliteyi artırır:
- Kullanılan dil, test çatısı ve mock kütüphanesi; mevcut test kuralları ve yardımcıları.
- Gereksinimler veya kabul kriterleri; bilinen hatalar; kapsam raporu.

Kod yoksa iste. Test çatısı belirtilmemişse kodun dilinden ve ekosisteminden çıkar ve `[VARSAYIM]` olarak işaretle; örnek verildiyse mevcut test stiline uy.

## Süreç
1. Birimin genel sözleşmesini belirle: girdiler, çıktılar, fırlatılan hatalar, gözlemlenebilir durum değişiklikleri ve sözleşmenin parçası olan işbirlikçi çağrıları (ör. "olay yayınlar"). Private metotları doğrudan test etme.
2. Metotları değil davranışları listele: her kural için bir satır ("ücretsiz kargo eşiğini aşan siparişler sıfır öder"). Belirtilmiş gereksinimleri koddan çıkarılan davranıştan ayır ve ikincileri `[VARSAYIM]` olarak etiketle; kod yanlış görünüyorsa bunu assert etmek yerine şüpheli hata olarak kaydet.
3. Her davranış için durumları çıkar: tipik değer, denklik sınıfları, sınırlar (min, maks, hemen altı/üstü, boş, null, sıfır, negatif, maksimum uzunluk), geçersiz girdiler, hata yolları ve durumlu birimler için durum dizileri.
4. Test dublörlerine karar ver: yalnızca deterministik olmayan veya yavaş sınırları (saat, rastgelelik, ağ, dosya sistemi, dış servisler) değiştir. Sorgular için fake veya stub, yalnızca çağrının kendisi davranış olan komutlar için mock tercih et; birimin kendisini veya değer nesnelerini asla mock'lama.
5. Testleri deterministik yap: saat, rastgele tohum, saat dilimi, yerel ayar ve kültür dışarıdan verilsin; sleep yok, paylaşılan değişken durum yok, test sırasına bağımlılık yok.
6. Her testi Arrange-Act-Assert yapısında, test başına tek davranış ve tek Act ile yaz. Proje kuralına uyarak adı şartname gibi koy (`<koşul>_<beklenen sonuç>` veya bir cümle).
7. Aynı kuralı birçok girdiyle sınamak için veri güdümlü (parametreli) testler kullan; kırılma doğrudan kuralı göstersin diye her ayrı kural için ayrı test tut.
8. Sonuçları kesin biçimde doğrula: tam değerler, istisna türü ve mesajın ilgili kısmı, yayınlanan olaylar; tesadüfi ayrıntıları (log metni, sözleşmenin parçası olmayan çağrı sayıları) doğrulama.
9. Her testin kırılabildiğini kontrol et: kodu zihnen (veya gerçekten) boz ya da beklenen değeri tersine çevir ve testin okunabilir bir mesajla kırmızıya döndüğünü gör. Regresyon testinin düzeltilmemiş kodda, hatanın tarif ettiği nedenle kırıldığı görülmelidir.
10. Test kodunu temiz tut: karmaşık hazırlık için builder veya factory yardımcıları, test gövdesinde mantık (döngü, koşul) yok, üç tekrarı aşan kopyala-yapıştır arrange blokları yok.
11. Hangi davranışların kapsandığını, hangi durumların bilinçli olarak dışarıda bırakıldığını ve bulunan şüpheli hataları raporla.
12. Hedef devam ediyorsa kalan test edilmemiş dallar için `test-gap-finder`, sınır davranışı için `integration-test-writing` veya davranış güvenceye alındığına göre `refactoring` öner.

## Çıktı formatı
```markdown
# Birim Testleri: <birim>
Çatı: <çatı> · Dublörler: <hangi işbirlikçiler ve neden> · Varsayımlar: <liste veya yok>

## Davranış Haritası
| # | Davranış | Kaynak (gereksinim / çıkarım) | Test(ler) |
|---|---|---|---|
| D1 | <kural> | <KK no veya [VARSAYIM]> | <test adı> |

## Testler
<davranışa göre gruplanmış test kodu>

## Kapsanmayanlar ve Nedeni
- <durum> — <neden: entegrasyon testi gerekir / kapsam dışı / kural belirsiz>

## Şüpheli Hatalar
- <girdi> → <gerçekleşen> ve <kurala göre beklenen> — [teyit edilene kadar VARSAYIM]
```

## Kalite kontrol listesi
- [ ] Her test genel sözleşme üzerinden tek bir davranışı doğruluyor ve tek bir Act içeriyor.
- [ ] Yalnızca mutlu yol değil; sınırlar, geçersiz girdiler ve hata yolları da kapsandı.
- [ ] Testler deterministik: gerçek saat, rastgelelik, ağ, dosya sistemi veya sıra bağımlılığı yok.
- [ ] Mock yalnızca etkileşimin kendisinin davranış olduğu yerlerde kullanıldı.
- [ ] Her test doğru nedenle kırılabiliyor ve adı beklenen davranışı söylüyor.
- [ ] Çıkarılan davranış `[VARSAYIM]` olarak etiketlendi; şüpheli hatalar assert ile sabitlenmedi, raporlandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Gerçekleştirimi test etmek: mock'lar üzerinde çağrı sırası doğrulamak her refactoring'de testleri kırar. Bunun yerine sonuçları doğrula.
- Hataları betona gömmek: kodu çalıştırıp çıktısını beklenen değer olarak kopyalamak. Beklentiyi kuraldan türet.
- Metot başına çok sayıda assert içeren tek dev test; ilk kırılma diğerlerini gizler. Davranış başına böl.

## Örnek
Girdi: "ShippingCostCalculator: 0-1 kg = 5, 1-5 kg = 9, >5 kg = 15; 100 üzeri ücretsiz; ekspres +10."

Zayıf test:
```
test_calculate() { assert calc.cost(order(2kg, 50)) == 9; assert calc.cost(order(2kg, 150)) == 0 }
```
Güçlü testler (bölüm):
- `agirlik_tam_1kg_ilk_kademeyi_kullanir` → 5 (sınır; kademe sınırının dahil olup olmadığı `[VARSAYIM]`, ürün sahibine açık soru).
- `siparis_tutari_tam_100_ucretsiz_degildir` → 9 (kural "100 üzeri" diyor).
- `ucretsiz_kargolu_siparise_ekspres_yalnizca_ek_ucret_yansitir` → 10 `[VARSAYIM]`: kod 0 döndürüyor, şüpheli hata olarak işaretlendi.
- `negatif_agirlik_InvalidWeight_firlatir`.
