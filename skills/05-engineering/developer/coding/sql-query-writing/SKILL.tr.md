---
description: "Belirtilen bir soru için hedef veritabanı lehçesinde doğru, okunabilir ve indeks dostu bir SQL sorgusu yazar: sonuç taneciğini (grain) ve join kardinalitesini netleştirir, NULL'ları, mükerrer kayıtları ve saat dilimlerini ele alır, sargable koşullar ve parametreler kullanır, dayandığı indeksleri ve sonuçların nasıl doğrulanacağını belirtir. Bir rapor, özellik, veri düzeltme veya inceleme için sorgu gerektiğinde, bir sorunun SQL'e çevrilmesi istendiğinde ya da mevcut bir sorgunun doğruluk veya okunabilirlik için yeniden yazılması istendiğinde kullanılır."
related: "query-optimization, index-recommendation, database-schema-design, metric-definition, performance-optimization"
prompt: "Siparişi olmayanlar dahil her müşteri için son 90 gündeki sipariş sayısını ve toplam cirosunu döndüren bir PostgreSQL sorgusu yaz."
---

# SQL Sorgusu Yazma

## Amaç
Bir veri sorusunu doğru satırları doğru taneciklikte döndüren, kolay okunan, gerçekçi hacimlerde verimli çalışan ve uygulama koduna güvenle gömülebilen bir sorguya dönüştürmek.

## Ne zaman kullanılır
- Bir rapor, özellik, API veya inceleme ilişkisel veritabanından veri gerektirdiğinde.
- Bir iş sorusunun SQL'e çevrilmesi gerektiğinde.
- Mevcut bir sorgu yanlış sayılar veya mükerrer kayıt döndürdüğünde ya da okunması zor olduğunda.

## Ne zaman kullanılmaz
- Sorgu doğru ama yavaşsa ve bir çalıştırma planı varsa `query-optimization` kullanılır.
- İhtiyaç bir iş yükü için indeks seçmekse `index-recommendation` kullanılır.
- Metriğin kendisi henüz tanımlı değilse önce `metric-definition` kullanılır.

## Girdiler
Zorunlu:
- Sonucun yanıtlaması gereken soru.
- Kolonları ve anahtarlarıyla ilgili tablolar (DDL veya açıklama) ve veritabanı motoru.

İsteğe bağlı, kaliteyi artırır:
- Satır hacimleri, mevcut indeksler, örnek veri, sorgunun nasıl çağrılacağı (anlık, rapor, parametreli uygulama), saat dilimi ve para birimi kuralları.

Şema verilmemişse iste; tablo veya kolon adı uydurma. Kısmi ise sorguyu yaz ve varsayılan adları `[VARSAYILAN KOLON]` olarak işaretle.

## Süreç
1. Sonuç taneciğini tanımla: her satır neyi temsil ediyor? Çıktı kolonlarını tanımları ve birimleriyle listele.
2. Kaynak tabloları ve join yollarını belirle; her join için kardinaliteyi (1:1, 1:N, N:M) ve satırları çoğaltıp çoğaltamayacağını yaz.
3. Join türlerini sorudan seç: "olması gereken" için inner, "olmayanlar dahil" için left; eşleşmeyen satırları elememesi gereken dış tablo filtrelerini `ON` içine koy.
4. Doğru seviyede topla: fan-out kaynaklı çift saymayı önlemek için çok tarafını join'den önce bir CTE veya alt sorguda topla; nedenini bilmeden mükerrerleri `DISTINCT` ile düzeltme.
5. NULL'ları açıkça ele al: gösterim için `COALESCE`, `COUNT(kolon)` ile `COUNT(*)` farkı, null olabilen alt sorgularla `NOT IN` (`NOT EXISTS` tercih et).
6. Zaman: yarı açık aralıklar kullan (`>= başlangıç AND < bitiş`), saat dilimini belirt, koşullarda indeksli kolonlara fonksiyon uygulama (sargability).
7. Okunabilirlik için yaz: anlamlı isimli CTE'ler, satır başına bir ifade, açık kolon listeleri (uygulama kodunda `SELECT *` yok), tutarlı alias'lar.
8. Her dış değeri parametre yap; SQL'i asla string birleştirerek oluşturma.
9. Sorgunun dayandığı indeksleri ve beklenen erişim yolunu belirt; büyük taramaları, sıralamaları ve büyük kümeler üzerindeki window fonksiyonlarını işaretle.
10. Doğrulama sorguları ver: tanecikte satır sayısı, bilinen bir rakamla mutabakat toplamı, uç satırların (siparişi olmayan, sınır tarihler) örnek kontrolü.
11. Hedef devam ediyorsa gerçek çalıştırma planıyla `query-optimization` veya destekleyici indeksler eksikse `index-recommendation` öner.

## Çıktı formatı
````markdown
# SQL Sorgusu: <soru>
Motor: <lehçe> · Tanecik: her satır bir <...> · Parametreler: <liste>

```sql
<sorgu>
```

## Mantık Notları
- Join'ler ve kardinalite: ...
- NULL / saat dilimi işleme: ...

## İndeks Varsayımları
- ...

## Doğrulama
```sql
<kontrol sorguları>
```

## Varsayımlar ve Açık Sorular
- ...
````

## Kalite kontrol listesi
- [ ] Tanecik belirtildi ve her join satır çoğaltmaya karşı kontrol edildi.
- [ ] Dış join'li tablolardaki filtreler join'i sessizce inner join'e çevirmiyor.
- [ ] NULL davranışı ve zaman aralıkları açık ve yarı açık.
- [ ] Koşullar sargable ve tüm dış değerler parametre.
- [ ] Hiçbir tablo veya kolon adı uydurulmadı; varsayımlar işaretli.
- [ ] Doğrulama sorguları verildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Siparişleri ve sipariş satırlarını join'leyip sipariş toplamlarını toplamak; ciro satır sayısıyla çarpılır.
- `LEFT JOIN orders` sonrasında `WHERE o.created_at >= ...` yazmak; siparişi olmayan müşteriler düşer.
- Timestamp üzerinde `BETWEEN '2024-01-01' AND '2024-01-31'` kullanmak; son günün neredeyse tamamı dışarıda kalır.
- `WHERE YEAR(created_at) = 2024` yazmak; indeks kullanımını engeller.

## Örnek
Girdi: "Siparişi olmayanlar dahil müşteri başına son 90 günün sipariş sayısı ve cirosu. PostgreSQL. customers(id, name), orders(id, customer_id, total_amount, created_at)."

Zayıf: `SELECT c.name, COUNT(*), SUM(o.total_amount) FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.created_at > now() - interval '90 days' GROUP BY c.name;` (siparişi olmayan müşterileri düşürür, onlar için 1 sayar, benzersiz olmayan isme göre gruplar).

Güçlü, bir bölüm:
```sql
WITH recent AS (
  SELECT customer_id, COUNT(*) AS order_count, SUM(total_amount) AS revenue
  FROM orders
  WHERE created_at >= now() - interval '90 days'
  GROUP BY customer_id
)
SELECT c.id, c.name, COALESCE(r.order_count, 0) AS order_count, COALESCE(r.revenue, 0) AS revenue
FROM customers c
LEFT JOIN recent r ON r.customer_id = c.id;
```
İndeks varsayımı: seçiciliğe göre `orders(created_at, customer_id)` veya `orders(customer_id, created_at)` `[planla DOĞRULA]`.
