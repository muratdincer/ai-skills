---
name: request-intake-document
description: "Ham bir iş talebini (e-posta, sohbet mesajı, toplantı notu, kayıt) hedef, kapsam, değer, paydaşlar, kısıtlar ve açık sorular içeren yapılandırılmış bir talep alma dokümanına dönüştürür. Yeni bir talep, fikir veya değişiklik isteği geldiğinde, analiz, tahmin ya da önceliklendirmeden önce kayıt altına alınması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: intake
  title: "Talep alma dokümanı oluşturma"
  related: "request-clarification-questions, request-completeness-check, request-triage, stakeholder-identification"
  prompt: "Bu talep için talep alma dokümanı oluştur: Satış ekibi denetim için ay sonuna kadar müşteri listesi ekranına Excel aktarımı istiyor."
---

# Talep Alma Dokümanı Oluşturma

## Amaç
Yeni bir talebi tutarlı ve karar verilebilir bir biçimde kaydetmek. Böylece talep, temel bilgiler için talep sahibine geri dönmeden sınıflandırılabilir, tahmin edilebilir ve önceliklendirilebilir.

## Ne zaman kullanılır
- Serbest metin olarak yeni bir özellik, değişiklik, rapor veya entegrasyon talebi geldiğinde.
- Talep backlog'a ya da talep/portföy panosuna girmek üzereyken.

## Ne zaman kullanılmaz
- Talep zaten ayrıntılı gereksinimlere dönüştürülmüşse `brd-writing` veya `frd-writing` kullanılır.
- Bir olay veya hata kaydıysa `bug-report` veya `ticket-triage` kullanılır.

## Girdiler
Zorunlu:
- Ham talep metni (herhangi bir formatta).

İsteğe bağlı, kaliteyi artırır:
- Talep sahibinin adı, rolü ve departmanı.
- İlgili sistemler, dokümanlar, önceki talepler.
- Kuruma özel talep şablonu veya zorunlu alanlar.

Ham talep yoksa iste. İsteğe bağlı girdileri en başta sorma; bunları açık sorular olarak listele.

## Süreç
1. Ham talebi oku. Talep sahibinin söylediği olgularla kendi yorumunu birbirinden ayır.
2. İhtiyacı tek cümlelik bir problem veya fırsat tanımı olarak yeniden yaz: kim, hangi problem, hangi etki.
3. İstenen sonucu ve başarının nasıl ölçüleceğini belirle. Belirtilmemişse ölçülebilir bir aday öner ve `[VARSAYIM]` olarak işaretle.
4. Talep türünü sınıflandır: yeni özellik, mevcut özellikte değişiklik, rapor/veri, entegrasyon, yasal/uyum, teknik/altyapı, diğer.
5. Kapsamı taslak olarak çıkar: kapsam içi, kapsam dışı ve açıkça bilinmeyenler.
6. Paydaşları listele: talep sahibi, sponsor/karar verici, etkilenen kullanıcılar, etkilenen ekipler/sistemler.
7. Kısıtları kaydet: son tarih ve gerekçesi, bütçe, mevzuat, teknoloji, bağımlılıklar.
8. İş değerini ve aciliyeti nitel olarak (Yüksek/Orta/Düşük) ve her biri için tek satırlık gerekçeyle tahmin et. Asla parasal rakam uydurma.
9. Riskleri ve varsayımları listele.
10. Açık soruları konuya göre grupla ve analizi ne kadar engellediklerine göre sırala.
11. Çıktı şablonunu doldur. Girdiyle desteklenmeyen her alanı `[BİLİNMİYOR]` veya `[VARSAYIM]` olarak işaretle.

## Çıktı formatı
```markdown
# Talep Kaydı: <kısa başlık>
| Alan | Değer |
|---|---|
| Talep No | <verildiyse, yoksa TBD> |
| Geliş tarihi | <tarih> |
| Talep sahibi | <ad, rol, departman> |
| Sponsor / karar verici | <ad veya [BİLİNMİYOR]> |
| Talep türü | <tür> |
| İş değeri | <Y/O/D> – <gerekçe> |
| Aciliyet | <Y/O/D> – <gerekçe> |
| Hedef tarih | <tarih ve gerekçe veya [BİLİNMİYOR]> |

## Problem / Fırsat
<tek cümlelik tanım + kısa bağlam>

## İstenen Sonuç ve Başarı Kriterleri
- <ölçülebilir sonuç>

## Kapsam
- Kapsam içi: ...
- Kapsam dışı: ...
- Bilinmeyen: ...

## Paydaşlar ve Etkilenen Taraflar
- ...

## Kısıtlar ve Bağımlılıklar
- ...

## Varsayımlar ve Riskler
- [VARSAYIM] ...
- [RİSK] ...

## Açık Sorular
1. <soru> — <neden önemli> — <kim cevaplayabilir>

## Önerilen Sonraki Adım
<netleştirme toplantısı / sınıflandırma / fizibilite / gerekçeli ret>
```

## Kalite kontrol listesi
- [ ] Problem tanımı bir çözümü tarif etmiyor.
- [ ] Her başarı kriteri ölçülebilir.
- [ ] Hiçbir şey uydurulmadı: desteklenmeyen alanlar `[BİLİNMİYOR]` veya `[VARSAYIM]` olarak işaretli.
- [ ] Kapsam dışı maddeler açıkça listelendi.
- [ ] Açık sorular somut ve her birinin muhtemel bir muhatabı var.
- [ ] Doküman yaklaşık bir sayfaya sığıyor.

## Sık yapılan hatalar
- Talep sahibinin önerdiği çözümü gereksinim olarak kopyalamak. Onu bağlam içinde "önerilen çözüm" olarak kaydet, problemi ayrı tut.
- "En kısa sürede" ifadesini son tarih kabul etmek. Tarihin arkasındaki gerçek olayı veya gerekçeyi sor.
- Her talebe Yüksek değer vermek. Her puanı gerekçelendir.

## Örnek
Girdi: "Satış ekibi müşteri listesi ekranına Excel'e aktarma istiyor, denetim için ay sonuna kadar lazım."

Çıktıdan bir bölüm:
- Problem: Satış ekibi müşteri listesi verisini denetçilere kullanılabilir bir formatta sunamıyor. Bu durum denetim bulgusu riski doğuruyor.
- Talep türü: Mevcut özellikte değişiklik (rapor/veri).
- Hedef tarih: Ay sonu – dış denetim `[kesin tarihi teyit et]`.
- Açık soru: Denetçiler hangi alanları ve filtreleri istiyor? Aktarılan veri maskelenmesi gereken kişisel veri içeriyor mu?
