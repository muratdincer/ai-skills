---
name: go-no-go
description: "Bir sürüm veya geçiş için yayına alma (go/no-go) kararını hazırlar ve kaydeder: üzerinde anlaşılmış kriterler, kriter başına kanıt, sorumlusu belli açık riskler, koşullu onay koşulları ve onaylayıcıları içeren bir karar kaydı. Bir sürüm, migration veya lansman resmi bir karar gerektirdiğinde, go/no-go toplantı paketi veya kontrol listesi istendiğinde ya da ekibin neden yayına çıktığını veya ertelediğini belgelemesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Yayına alma kararı"
  related: "release-quality-gate, release-plan, rollback-plan, decision-log, test-summary-report"
  prompt: "Yarınki CRM migration geçişi için go/no-go hazırla. Test sonuçları, açık hatalar ve prova notları ekte."
---

# Yayına Alma Kararı

## Amaç
Sürüm kararını önceden anlaşılmış kriterlere karşı kanıta dayanarak vermek ve koşulları ile sorumlularıyla birlikte kaydetmek. Böylece karar savunulabilir olur, takvim baskısına veya en yüksek sese göre verilmez.

## Ne zaman kullanılır
- Bir sürüm, veri migration'ı, geçiş veya lansman resmi bir karar noktası gerektirdiğinde.
- Birden fazla tarafın (iş birimi, QA, operasyon, güvenlik) onay vermesi gerektiğinde.
- Kararın denetim veya değişiklik yönetimi için belgelenmesi gerektiğinde.

## Ne zaman kullanılmaz
- Yalnızca testten gelen kalite kanıtı gerekiyorsa `release-quality-gate` veya `test-summary-report` kullanılır.
- Sürüm takvimi ve içeriği hâlâ planlanıyorsa `release-plan` kullanılır.
- Bir sürüm kapısı değil, seçenekler arasında genel bir karar söz konusuysa `decision-matrix` kullanılır.

## Girdiler
Zorunlu:
- Neye karar verildiği (sürüm, migration, lansman) ve planlanan pencere.
- Mevcut kanıtlar: test sonuçları, açık hatalar, prova veya staging sonuçları, operasyon ve destek hazırlığı.

İsteğe bağlı, kaliteyi artırır:
- Önceden anlaşılmış go/no-go kriterleri, kurumun değişiklik politikası.
- Geri dönüş planı ve geri dönüşsüz nokta, ertelemeye ilişkin iş kısıtları.
- Onaylayıcıların listesi ve rolleri.

Hiç kanıt yoksa iste; kanıtsız bir go/no-go yalnızca durum toplantısıdır. Eksik kriterler önerilir ve onay için `[ÖNERİ]` olarak işaretlenir.

## Süreç
1. Kanıta bakmadan önce kriterleri sabitle: fonksiyonel kalite, önem derecesine göre açık hatalar, fonksiyonel olmayan sonuçlar (performans, güvenlik), veri migration mutabakatı, operasyonel hazırlık (izleme, runbook'lar, nöbet), destek ve kullanıcı hazırlığı, geri dönüş hazırlığı, iş birimi hazırlığı, dış bağımlılıklar.
2. Her kriter için geçme eşiğini ve zorunlu mu (herhangi bir başarısızlık = no-go) yoksa tartılabilir mi olduğunu belirle.
3. Her kanıtı bir kritere eşle ve Karşılandı / Kısmen karşılandı / Karşılanmadı / Kanıt yok olarak derecelendir; kaynağı (rapor, koşum, kişi) ve tarihini belirt.
4. "Kanıt yok" durumunu karşılanmadı say; zorunlu kriterlerde sözlü güvenceyi not düşmeden kabul etme.
5. Açık riskleri ve kabul edilen sapmaları sorumlu, azaltma önlemi ve geçerlilik süresiyle listele.
6. No-go'nun maliyetini de değerlendir: ertelemenin iş etkisi, sonraki uygun pencere; rakam uydurmadan belirt.
7. Öneriyi oluştur: Go, Koşullu go (her koşul için açık sorumlu ve son tarihle) veya No-go (neyin değişmesi gerektiği ve sonraki karar noktasıyla).
8. Kararı kaydet: kim karar verdi, kime danışıldı, karşı görüşler, saat ve pencere boyunca geri dönüş karar sahibi.
9. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa geri dönüş hazırlığı zayıfsa `rollback-plan`, no-go sonrası yeniden planlama için `release-plan` veya kaydı dosyalamak için `decision-log` öner.

## Çıktı formatı
```markdown
# Go/No-Go: <sürüm/geçiş> – <pencere>
Karar toplantısı: <tarih/saat> · Karar sahibi: <ad veya [TBD]>

## Kriterler ve Kanıtlar
| # | Kriter | Zorunlu | Eşik | Kanıt (kaynak, tarih) | Durum |
|---|---|---|---|---|---|

## Açık Riskler ve Kabul Edilen Sapmalar
| Risk/sapma | Etki | Azaltma | Sorumlu | Geçerlilik |

## Ertelemenin Maliyeti
<nitel etki, sonraki pencere>

## Öneri
Go / Koşullu go / No-go – <2-3 cümlelik gerekçe>
Koşullar: <koşul – sorumlu – son tarih>

## Karar Kaydı
- Karar: ... · Saat: ...
- Onaylayanlar: ... · Danışılanlar: ... · Karşı görüş: ...
- Pencere boyunca geri dönüş karar sahibi: ...
```

## Kalite kontrol listesi
- [ ] Kriterler ve eşikler kanıt derecelendirilmeden önce belirtildi.
- [ ] Her durum bir kaynağa dayanıyor; "kanıt yok" karşılandı sayılmadı.
- [ ] Karşılanmayan zorunlu kriterler no-go'ya ya da sorumlusu belli, açıkça kabul edilmiş bir sapmaya götürüyor.
- [ ] Koşullu go koşulları doğrulanabilir, sahipli ve süreli.
- [ ] Karşı görüşler ve geri dönüş karar sahibi kaydedildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tarihe uysun diye kriterleri toplantıda değiştirmek. Her kriter değişikliğini sorumlusu olan bir sapma olarak kaydet.
- Belirsiz koşullarla koşullu go ("yakından izle"). Metriği, sorumluyu ve geri dönüşü neyin tetikleyeceğini adlandır.
- Testler geçti diye operasyon ve destek hazırlığını göz ardı etmek. Sistemi işletmeye hazır olmak kapının parçasıdır.

## Örnek
Girdi: "CRM migration: raporlamada 2 açık yüksek önemli hata, provada mutabakat satırların %99,97'si eşleşti, destek henüz eğitilmedi."

Çıktıdan bir bölüm:
| # | Kriter | Zorunlu | Durum |
|---|---|---|---|
| 3 | Veri mutabakatı = kapsamdaki kayıtların %100'ü, farklar açıklanmış | Evet | Kısmen karşılandı: %0,03 açıklanamadı `[kaynak: prova 2 raporu]` |
| 6 | Destek yeni ekranlar konusunda eğitildi | Hayır | Karşılanmadı |

Öneri: Açıklanamayan %0,03 `[TBD]` tarihinden önce sınıflandırılmazsa No-go; kapsam dışı arşiv kayıtları olduğu açıklanırsa, destek eğitiminin mesai başlamadan tamamlanması koşuluyla Koşullu go.
