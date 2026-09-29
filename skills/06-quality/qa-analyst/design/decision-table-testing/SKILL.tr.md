---
name: decision-table-testing
description: "İş kurallarından koşulları ve aksiyonları listeleyerek karar tabloları kurar, kombinasyonları çıkarır, ilgisiz olanları daraltır ve her kural sütunu için bir test türetir; bu sırada eksik ve çelişkili kuralları ortaya çıkarır. Davranış koşul kombinasyonlarına bağlı olduğunda (uygunluk, fiyatlama, onaylar, indirimler, yönlendirme) ya da bir eğer-ise kural setinin test edilmesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: design
  title: "Karar tablosu testi"
  related: "equivalence-boundary-analysis, business-rules-catalog, test-case-writing, pairwise-testing, state-transition-testing"
  prompt: "Kargo ücreti için karar tablosu kur: 200 TL üzeri üyelere ücretsiz, standart 29 TL, ekspres +40 TL, adalara +50 TL, üyelere ekspres yarı fiyat."
---

# Karar Tablosu Testi

## Amaç
Kural koşullarının her kombinasyonunu açık hale getirerek her farklı sonucun bir kez test edilmesini sağlamak; kurallardaki boşlukları ve çelişkileri üretim hatasına dönüşmeden bulmak.

## Ne zaman kullanılır
- Bir sonuç iki veya daha fazla koşula bağlı (müşteri tipi, tutar, kanal, bölge, bayraklar).
- Kurallar düz metin paragraflar halinde yazılmış ve uç kombinasyonlarda görüş ayrılığı var.
- Fiyatlama, uygunluk, onay yönlendirme veya ücret mantığı değişiyor.

## Ne zaman kullanılmaz
- Sonucu aralıkları olan tek bir girdi belirliyorsa `equivalence-boundary-analysis` kullanılır.
- Davranış önceki olaylara veya duruma bağlıysa `state-transition-testing` kullanılır.
- Çok sayıda parametre bağımsızsa ve yalnızca kombinasyon kapsamı gerekiyorsa `pairwise-testing` kullanılır.

## Girdiler
Zorunlu:
- İş kuralları (metin, spesifikasyon alıntısı, mevcut kural kataloğu).

İsteğe bağlı, kaliteyi artırır:
- Kuralların önceliği/üstünlüğü, yuvarlama kuralları, iş biriminden örnekler.
- Karşılaştırma için mevcut uygulamanın davranışı.

Kurallar yoksa iste. Kural metni bir sonucu belirlemiyorsa hücreyi `[BİLİNMİYOR]` ile işaretle ve soru olarak yükselt.

## Süreç
1. Koşulları çıkar ve her birini boolean ya da küçük bir sınıf kümesi yap (ör. Tutar: <200, >=200). Aralık varsa sınıfları sınır değer analizinden al.
2. Aksiyonları/sonuçları çıkar (ücret tutarı, onay seviyesi, mesaj, atanan bayrak).
3. Toplam kombinasyon sayısını hesapla; yaklaşık 32'nin altındaysa hepsini çıkar, değilse koşulları grupla veya alt tablolara böl.
4. Her sütunu (kuralı) kural metnindeki beklenen aksiyonlarla doldur; sonucu belirtilmemiş hücreleri `[BİLİNMİYOR]` ile işaretle.
5. İmkânsız kombinasyonları (ör. üye değil VE üye indirimi) gerekçesiyle işaretle.
6. Sonucu bir koşula bağlı olmayan sütunları "-" (fark etmez) ile daralt ve daraltmanın bir farkı gizlemediğini doğrula.
7. Anomalileri bul: eksik kurallar (sonucu olmayan kombinasyonlar), çelişkiler (farklı sonuç veren iki kural), gereksiz kurallar.
8. Kalan her sütun için, tam olarak o sütunu sağlayan somut veriyle bir test case türet; aralık bazlı koşullar için sınır değerleri ekle.
9. Sütunları iş etkisine ve sıklığa göre önceliklendir.
10. Tabloyu, testleri ve ürün sahibi için kural boşlukları listesini çıktı olarak ver.
11. Çıkarımla eklenen her kuralı veya sonucu `[VARSAYIM]` ile işaretle; kullanıcı devam ederse kuralları case'e çevirmek için `test-case-writing`, koşullar patlıyorsa `pairwise-testing` öner.

## Çıktı formatı
```markdown
# Karar Tablosu: <kural seti>
| | K1 | K2 | K3 | ... |
|---|---|---|---|---|
| C1: <koşul> | E | E | H | |
| C2: <koşul> | E | H | - | |
| A1: <aksiyon> | X | | X | |
| A2: <aksiyon / değer> | | 29 TL | | |

İmkânsız kombinasyonlar: <liste ve gerekçe>
## Kural Boşlukları ve Çelişkiler
| Sütunlar | Sorun | Soru |
## Türetilen Testler
| Test | Kural sütunu | Veri | Beklenen |
```

## Kalite kontrol listesi
- [ ] Her koşul kombinasyonu ya test ediliyor, ya imkânsız olarak işaretli, ya da gerekçeli "-" ile daraltılmış.
- [ ] Her sütunun tam olarak bir beklenen sonucu var veya `[BİLİNMİYOR]` ile işaretli.
- [ ] Çelişkiler ve boşluklar sessizce çözülmedi, soru olarak listelendi.
- [ ] Test verisi sütunu, aralıklar için sınır değerler dahil, tam olarak sağlıyor.
- [ ] Kural önceliği (hangi kuralın kazandığı) belirtildi veya soruldu.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sütunları erken daraltıp bir etkileşimi kaçırmak (ör. ekspres + ada + üye).
- Aralıkları eşiklerde sınır testi olmadan boolean olarak kodlamak.
- Belirsiz kuralları kendi başına çözmek. Seçenekleri sun ve kural sahibine sor.

## Örnek
Girdi: "200 TL üzeri üyelere ücretsiz kargo, standart 29 TL, ekspres +40 TL, adalar +50 TL, üyelere ekspres yarı fiyat."

Çıktıdan bir bölüm:
| C1 Üye | E | E | H | H |
| C2 Sepet >= 200 | E | E | E | H |
| C3 Ekspres | H | E | E | H |
| A Ücret | 0 | 20 | 69 | 29 |
- Boşluk: Ada ek ücreti ücretsiz kargolu siparişlere de uygulanıyor mu? `[BİLİNMİYOR]`
- Soru: "Ekspres yarı fiyat", ücretsiz kargonun üstüne 20 TL mi, yoksa 69 TL'nin yarısı mı?
