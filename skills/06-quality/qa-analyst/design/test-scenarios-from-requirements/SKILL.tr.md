---
name: test-scenarios-from-requirements
description: "Gereksinimlerden, user story'lerden, use case'lerden veya kabul kriterlerinden kaynağa izlenebilir ve öncelikli üst düzey test senaryoları (pozitif, negatif, uç, yetki, entegrasyon, fonksiyonel olmayan) çıkarır. Bir özellik için test tasarımı başladığında, bir story'nin kapsamı kontrol edilirken ya da bir gereksinim için neyin test edilmesi gerektiği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: design
  title: "Gereksinimden test senaryosu çıkarma"
  related: "test-case-writing, testability-review, equivalence-boundary-analysis, traceability-matrix, bdd-feature-file"
  prompt: "Bu story için test senaryolarını çıkar: müşteri siparişini kargoya verilene kadar iptal edebilir ve ödemesi orijinal ödeme yöntemine iade edilir."
---

# Gereksinimden Test Senaryosu Çıkarma

## Amaç
Ayrıntılı test case'ler yazılmadan önce bir gereksinim için neyin doğrulanması gerektiğini senaryo düzeyinde, eksiksiz ve izlenebilir bir liste olarak üretmek. Senaryolar kapsam boşluklarını görünür kılar ve ürün sahibiyle ucuz biçimde gözden geçirilebilir.

## Ne zaman kullanılır
- Bir story, use case veya gereksinim seti test tasarımına hazır.
- Ekip, ayrıntılı case'leri yazmadan önce kapsamı iş birimiyle gözden geçirmek istiyor.
- Kabul kriterleri var ama yalnızca mutlu yolu anlatıyor.

## Ne zaman kullanılmaz
- Veri ve beklenen sonuç içeren adım adım case'ler gerekiyorsa `test-case-writing` kullanılır.
- Gereksinimler hâlâ belirsizse önce `testability-review` yapılır.
- Koşturulabilir Gherkin gerekiyorsa `bdd-feature-file` kullanılır.

## Girdiler
Zorunlu:
- Gereksinim, story, use case veya kabul kriterleri.

İsteğe bağlı, kaliteyi artırır:
- İş kuralları, arayüz tasarımları, API sözleşmeleri, roller ve yetkiler, ilgili fonksiyonel olmayan gereksinimler.
- Bu alandaki bilinen hatalar veya olaylar.

Gereksinim yoksa iste. Belirsiz davranış uydurulmuş bir beklenti değil, açık soru olur.

## Süreç
1. Test edilebilir koşulları çıkar: belirtilen veya ima edilen her iş kuralı, girdi, durum, rol, çıktı ve entegrasyon.
2. Her kabul kriterini en az bir kez kapsayan ana başarı senaryolarını yaz.
3. Alternatif akışları ekle: geçerli varyasyonlar (farklı ödeme türleri, isteğe bağlı alanlar, diğer roller).
4. Negatif senaryoları ekle: geçersiz girdi, kural ihlali, yetkisiz erişim, yanlış durum (ör. son tarihten veya durum değişikliğinden sonra yapılan işlem).
5. Uç senaryoları ekle: sınırlar, boş/maksimum değerler, zaman (kesim saatleri, saat dilimleri, ay sonu), eşzamanlılık (iki kullanıcı, çift gönderim), idempotency.
6. Entegrasyon senaryolarını ekle: bağlı sistem hatası, zaman aşımı, kısmi başarı, yeniden denemeler, mesaj tekrarı.
7. İlgili fonksiyonel olmayan senaryoları ekle: denetim kaydı, bildirimler, yeni arayüzün erişilebilirliği, ağır işlemlerin performansı, veri gizliliği.
8. Her senaryoya bir ID, kaynak referansı (kriter, kural) ve öncelik (riske göre Yüksek/Orta/Düşük) ver.
9. Kapsamı kontrol et: her kabul kriteri ve iş kuralı en az bir senaryoya eşleniyor; kapsanmayanları listele.
10. Beklenen davranışın tanımlı olmadığı yerler için açık soruları listele.
11. Çıkarımla eklenen davranışları `[VARSAYIM]` ile işaretle; kullanıcı devam ederse ayrıntılı case'ler için `test-case-writing`, Gherkin için `bdd-feature-file` öner.

## Çıktı formatı
```markdown
# Test Senaryoları: <özellik / story ID>
| ID | Senaryo | Tür | Kaynak | Öncelik |
|---|---|---|---|---|
| TS-01 | <... durumunda ... olduğunu doğrula> | Pozitif / Negatif / Uç / Yetki / Entegrasyon / NFR | AC-1, BR-2 | Y |

## Kapsam
| Kaynak öğe | Senaryolar |
Kapsanmayan: <öğeler veya "yok">

## Açık Sorular
1. <tanımsız davranış> — <etkilenen senaryo>
```

## Kalite kontrol listesi
- [ ] Her kabul kriteri ve iş kuralı en az bir senaryoyla kapsanıyor.
- [ ] Yüksek riskli özelliklerde negatif ve uç senaryolar en az mutlu yol senaryoları kadar.
- [ ] Her senaryo adım değil, tek bir amaç ve koşul içeriyor.
- [ ] Hiçbir beklenen davranış uydurulmadı; belirsiz olanlar açık soru.
- [ ] Öncelikler yazılış sırasını değil riski yansıtıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Senaryo yerine test case yazmak. Tek satırlık amaçla sınırlı tut; ayrıntılar `test-case-writing` işidir.
- Yalnızca arayüz yollarını kapsamak. Durum değişikliklerini, entegrasyonları ve asenkron etkileri (e-posta, iade, olaylar) dahil et.
- Kesim saatleri ve durum geçişleri gibi zamana bağlı kuralları unutmak.

## Örnek
Girdi: "Müşteri siparişi kargoya verilene kadar iptal edebilir; iade orijinal ödeme yöntemine yapılır."

Çıktıdan bir bölüm:
| TS-01 | Kargoya verilmemiş, kartla ödenmiş siparişi iptal et → sipariş iptal, tutarın tamamı karta iade | Pozitif | AC-1 | Y |
| TS-04 | Kargoya verilmiş siparişi iptal et → iptal mesajla reddedilir | Negatif | AC-1 | Y |
| TS-07 | Kargo durumu aynı anda değişirken iptal et | Uç | AC-1 | O |
| TS-09 | İade sağlayıcısı zaman aşımına düşer → sipariş durumu ve yeniden deneme davranışı | Entegrasyon | AC-2 | Y |
- Açık soru: Kısmen kargolanmış siparişlerde kalan kalemler mi iptal edilir, yoksa iptal reddedilir mi?
