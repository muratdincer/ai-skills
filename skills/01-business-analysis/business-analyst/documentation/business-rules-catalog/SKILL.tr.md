---
name: business-rules-catalog
description: "Doküman, not, gereksinim veya kod tariflerinden iş kurallarını çıkarır ve ID, kural tipi (kısıt, hesaplama, çıkarım, aksiyon tetikleyici, olgu), atomik ve bildirimsel ifade, kaynak, sahip, geçerlilik tarihleri, istisnalar ve kuralı kullanan gereksinimlerle bir katalogda standartlaştırır. Kurallar dağınık veya süreç ve ekranlara gömülü olduğunda, kaynaklar arasında çeliştiğinde ya da 'iş kurallarını listele' veya kural kitabı oluştur dendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "İş kuralları kataloğu"
  related: "document-analysis, decision-table-testing, requirements-consistency-check, frd-writing, glossary-builder"
  prompt: "Bu kredi başvurusu prosedür notlarındaki iş kurallarını çıkar ve bir katalogda standartlaştır."
---

# İş Kuralları Kataloğu

## Amaç
Kurumun kurallarını açık, atomik ve izlenebilir biçimde tek yerde toplamak; böylece kurallar bir kez uygulanır, kesin olarak test edilir ve onları barındıran her doküman, ekran ve programı aramadan değiştirilebilir.

## Ne zaman kullanılır
- Kurallar prosedürlere, e-postalara, gereksinim dokümanlarına veya eski sistem davranışına gömülü olduğunda.
- Farklı kaynaklar aynı kuralı farklı ifade ettiğinde veya kurallar sık değiştiğinde (fiyat, uygunluk, onay).
- Gereksinimler, kullanım senaryoları veya testler referans verecek kalıcı kural ID'lerine ihtiyaç duyduğunda.

## Ne zaman kullanılmaz
- Kaynak dokümanlar henüz okunup taranmadıysa önce `document-analysis` kullanılır.
- Karmaşık bir kural setinden test senaryosu türetilecekse `decision-table-testing` kullanılır.
- Yalnızca terim tanımları gerekiyorsa `glossary-builder` kullanılır.

## Girdiler
Zorunlu:
- Kuralları içeren kaynak materyal (dokümanlar, notlar, gereksinimler, sistem davranışı tarifleri).

İsteğe bağlı, kaliteyi artırır:
- Mevcut kural kataloğu ve ID şeması, sözlük, kural sahipleri, mevzuat referansları, geçerlilik tarihleri.

Kaynak materyal verilmemişse iste; genel alan bilgisinden kural yazma. Okumayıp çıkardığın her kuralı `[VARSAYIM]` olarak işaretle.

## Süreç
1. Kaynaklarda kural işaretlerini tara: "zorunludur", "yalnızca ... ise", "yapılamaz", "en az", "... içinde", eşikler, hesaplamalar, onay seviyeleri, uygunluk ve durum koşulları.
2. Kuralları süreç adımlarından ve UI davranışından ayır: kural, onu kimin veya hangi sistemin uyguladığından bağımsız olarak geçerlidir.
3. Her kuralı sınıflandır: kısıt (olmalı/olmamalı), hesaplama (formül), çıkarım (koşullar sağlanırsa sonuç), aksiyon tetikleyici (koşul bir aksiyonu başlatır) veya olgu/tanım.
4. Her birini sözlük terimlerini kullanarak tek, atomik ve bildirimsel bir ifadeye çevir: tek koşul seti, tek sonuç. Bileşik kuralları böl; orijinal ifadeyi kaynak alıntısı olarak sakla.
5. Parametreleri (tutarlar, süreler, yüzdeler, roller) açık yaz ve kural mantığından ayır; böylece kural yeniden yazılmadan değiştirilebilir. Bilinmeyen değerler `[TBD]` olur.
6. Karmaşık koşul kombinasyonlarında kuralı bir karar tablosuyla ifade et ve bütünlüğünü (her kombinasyonun bir sonucu var) ve çakışmaları kontrol et.
7. Kaynağı (doküman, bölüm, kişi), sahibi (kimin değiştirebileceği), geçerlilik tarihini, istisnaları ve uygulama noktasını (manuel, sistem, ikisi) kaydet.
8. Kaynaklar arası tekrar ve çelişkileri bul; sessizce çözme, iki alıntıyla ve karar vermesi gereken sahiple birlikte listele.
9. Her kuralı onu uygulayan gereksinimlere, kullanım senaryolarına veya hikayelere bağla.
10. Varsayımları ve açık soruları muhataplarıyla topla.
11. Hedef devam ediyorsa test türetmek için `decision-table-testing`, daha geniş çelişkiler için `requirements-consistency-check`, tanımsız terimler için `glossary-builder` öner.

## Çıktı formatı
```markdown
# İş Kuralları Kataloğu: <alan>
Kaynaklar: <liste> · ID şeması: BR-<alan>-<nn>

| ID | Tip | Kural ifadesi | Parametreler | İstisnalar | Kaynak (alıntı) | Sahip | Geçerlilik | Uygulayan | Kullanıldığı yer |
|---|---|---|---|---|---|---|---|---|---|

## Karar Tabloları (karmaşık kurallar için)
## Tekrarlar ve Çelişkiler
| Kural A | Kural B | Çelişki | Karar sahibi |
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her kural atomik: tek koşul seti, tek sonuç.
- [ ] Kurallar süreç adımı, UI davranışı veya uygulama ayrıntısı içermiyor.
- [ ] Her kuralın tipi, kaynak alıntısı ve sahibi var (ya da `[BİLİNMİYOR]` sahip açık soru olarak yazıldı).
- [ ] Parametreler mantıktan ayrıldı; bilinmeyen değerler `[TBD]`.
- [ ] Karar tabloları eksiksiz ve çakışmasız.
- [ ] Çelişkiler tahminle çözülmedi, iki kaynağıyla listelendi; çıkarılan kurallar `[VARSAYIM]`.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Adımları kural olarak kataloglamak ("Memur kimliği kontrol eder"). Neyin doğru olması gerektiğini sor; kural "Bir başvuru doğrulanmış kimlik gerektirir" olur.
- Eşikleri ifadeye sabit yazmak. Mantıktan daha sık değiştikleri için parametreleştir.
- İki kaynak çeliştiğinde daha yeni görüneni seçmek. Karar yalnızca kural sahibinindir; çelişkiyi listele.

## Örnek
Girdi (prosedür notu): "250.000 üzerindeki başvurular bölge müdürü onayı ister, ama son 12 ayda gecikmesi olmayan mevcut müşterilerde şube onayı yeterli."

Çıktıdan bir bölüm:
| ID | Tip | Kural ifadesi | Parametreler | Kaynak | Sahip |
|---|---|---|---|---|---|
| BR-CR-01 | Kısıt | Tutarı bölge onay limitini aşan kredi başvurusu, BR-CR-02 geçerli değilse bölge müdürü onayı gerektirir. | Bölge limiti = 250.000 `[TBD: para birimi]` | Prosedür notu §3 | Kredi politikası `[BİLİNMİYOR]` |
| BR-CR-02 | Çıkarım | Son N ayda ödeme gecikmesi olmayan mevcut müşteri şube onayına uygundur. | N = 12 | Prosedür notu §3 | Kredi politikası |

Açık soru: "Gecikme" neyi kapsıyor (her gecikme günü mü, bir eşiğin üstü mü)? — Kredi risk
