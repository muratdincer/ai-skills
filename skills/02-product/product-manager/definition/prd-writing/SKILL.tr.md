---
description: Problem ve kanıtları, hedefleri ve başarı metriklerini, hedef kullanıcıları, kapsam ve hedef dışı konuları, kabul kriterleriyle önceliklendirilmiş gereksinimleri, kullanıcı deneyimini, fonksiyonel olmayan ihtiyaçları, bağımlılıkları, riskleri, yayın planını ve açık soruları kapsayan bir Ürün Gereksinim Dokümanı (PRD) yazar. Bir ürün girişiminin geliştirme öncesinde mühendislik, tasarım ve paydaşlar arasında hizalanması gerektiğinde, PRD veya ürün spesifikasyonu istendiğinde ya da mevcut bir PRD'nin eksikler açısından gözden geçirilmesi gerektiğinde kullanılır.
related: feature-brief, mvp-scoping, epic-breakdown, nfr-specification, acceptance-criteria
prompt: B2B müşterilerin belirli bir tutarın üzerindeki satın alma siparişleri için onay akışı tanımlayabilmesi için bir PRD yaz.
---

# Ürün Gereksinim Dokümanı (PRD) Yazma

## Amaç
Bir girişimin neden önemli olduğunu, hangi sonucu elde etmesi gerektiğini ve ürünün ne yapması gerektiğini açıklayan; mühendislik ve tasarımın planlama yapabileceği kadar kesin, kapsam dışı ve henüz bilinmeyen konularda net tek bir doğruluk kaynağı oluşturmak.

## Ne zaman kullanılır
- Birden çok iterasyon sürecek bir girişim veya önemli bir özellik, geliştirme öncesinde ekipler arası hizalama gerektirdiğinde.
- Yönetim veya iş ortakları hedefleri, kapsamı ve riskleri olan, gözden geçirilebilir bir spesifikasyon istediğinde.
- Mevcut bir PRD eksik bölümler, belirsiz gereksinimler veya test edilemeyen hedefler açısından kontrol edilecekse.

## Ne zaman kullanılmaz
- Küçük bir özellik için tek sayfalık bir hizalama notu yeterliyse `feature-brief` kullanılır.
- Sözleşmeye bağlı veya regülasyona tabi bir proje için resmî iş ya da fonksiyonel gereksinimler gerekiyorsa `brd-writing` veya `frd-writing` kullanılır.
- Kapsam hâlâ çok büyükse ve önce daraltılması gerekiyorsa `mvp-scoping` kullanılır.

## Girdiler
Zorunlu:
- Problem veya fırsat ve hedef kullanıcılar.
- Hedeflenen çözüm yönü hakkında bilinenler.

İsteğe bağlı, kaliteyi artırır:
- Kanıtlar: araştırma, geri bildirim temaları, analitik, satış/destek verisi.
- Strateji/OKR bağlantısı, kısıtlar (tarihler, uyum, platformlar), bağımlılıklar.
- Tasarımlar, teknik notlar, önceki kararlar.

Problem veya hedef kullanıcılar eksikse sor (tek seferde en fazla 5 soru). Bilinmeyen diğer her şey açık sorularda `[TBD]` olur; metrik, tarih veya müşteri adı uydurma.

## Süreç
1. Problem ifadesini çözüm içermeden yaz: kim, hangi zorluk, ne zaman, etkisi, kanıtı. Çıkarım olan her şeyi `[VARSAYIM]` olarak etiketle.
2. Girişimi stratejiye veya bir hedefe bağla ve neden şimdi yapılması gerektiğini belirt.
3. Hedefleri başarı metrikleriyle (başlangıç değeri, hedef, zaman aralığı, kaynak) sonuç olarak tanımla; koruma metriklerini ve açık hedef dışı konuları ekle.
4. Hedef kullanıcıları ve ana senaryoları tanımla; varsa personalara veya işlere (JTBD) atıf yap.
5. Kapsamı belirle: kapsam içi, kapsam dışı (gerekçesiyle) ve sonraki fazlar.
6. Fonksiyonel gereksinimleri senaryolara bağlı, numaralı, test edilebilir ifadeler olarak yaz; her birine öncelik (Must/Should/Could veya eşdeğeri) ve 1-3 kabul kriteri ekle; gereksinimi önerilen uygulama biçiminden ayır.
7. UX notlarını (akışlar, durumlar, boş/hata durumları, WCAG 2.2'ye göre erişilebilirlik) yaz ve tasarımlara bağlantı ver.
8. Burada önemli olan fonksiyonel olmayan gereksinimleri listele: performans, erişilebilirlik süresi (availability), güvenlik/gizlilik (kişisel veri varsa KVKK/GDPR), denetlenebilirlik, yerelleştirme, ölçeklenebilirlik.
9. Bağımlılıkları, önlemleriyle riskleri ve doğrulanacak varsayımları kaydet.
10. Yayın planını çıkar: fazlar, feature flag'ler, veri taşıma, beta grubu, lansman kriterleri, destek ve dokümantasyon ihtiyaçları.
11. Açık soruları sorumlu ve gereken tarihle topla; karar kaydı ve değişiklik geçmişi ekle.
12. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: gereksinimleri backlog maddelerine dönüştürmek için `epic-breakdown` veya `story-mapping`, kalite gereksinimlerini derinleştirmek için `nfr-specification`.

## Çıktı formatı
```markdown
# PRD: <girişim adı>
Durum: Taslak · Sahibi: <PM> · Gözden geçirenler: <mühendislik, tasarım, ...> · Son güncelleme: <tarih>

## 1. Problem ve Kanıtlar
## 2. Stratejik Uyum ve Neden Şimdi
## 3. Hedefler, Başarı Metrikleri ve Hedef Dışı Konular
| Metrik | Başlangıç | Hedef | Zaman aralığı | Kaynak |
|---|---|---|---|---|
Koruma metrikleri: ... · Hedef dışı: ...
## 4. Kullanıcılar ve Ana Senaryolar
## 5. Kapsam
- İçinde: ... · Dışında (neden): ... · Sonra: ...
## 6. Gereksinimler
| ID | Gereksinim | Senaryo | Öncelik | Kabul kriterleri |
|---|---|---|---|---|
| G1 | Sistem ... yapmalıdır | S1 | Must | Given/When/Then ... |
## 7. Kullanıcı Deneyimi
## 8. Fonksiyonel Olmayan Gereksinimler
## 9. Bağımlılıklar, Riskler ve Varsayımlar
## 10. Yayın ve Lansman Kriterleri
## 11. Açık Sorular
| # | Soru | Sorumlu | Gereken tarih |
## 12. Karar Kaydı ve Değişiklik Geçmişi
```

## Kalite kontrol listesi
- [ ] Problem çözüm içermeden ifade edildi ve kanıta dayanıyor ya da `[VARSAYIM]` olarak işaretli.
- [ ] Her hedefin başlangıç, hedef ve zaman aralığı olan bir metriği var; bilinmeyen değerler uydurulmadı, `[TBD]`.
- [ ] Hedef dışı ve kapsam dışı maddeler açıkça yazıldı.
- [ ] Her gereksinim benzersiz numaralı, test edilebilir, önceliklendirilmiş ve kabul kriterli.
- [ ] İlgili fonksiyonel olmayan gereksinimler, gizlilik ve erişilebilirlik ele alındı ya da açıkça uygulanamaz olarak işaretlendi.
- [ ] Açık soruların sorumlusu ve tarihi, risklerin önlemi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- PRD'yi bir özellik listesi olarak yazmak. Her gereksinimi bir senaryoya ve hedefe bağla, bağlanamıyorsa çıkar.
- Uygulamayı belirlemek ("üç sekmeli bir modal kullan"). İhtiyacı ve kısıtları yaz; tasarım ve mimari seçimlerini sahiplerine bırak.
- PRD'yi dondurulmuş saymak. Gözden geçirenler neyin neden değiştiğini görebilsin diye değişiklik geçmişi ve karar kaydı tut.

## Örnek
Girdi: "B2B müşterilerin belirli tutarın üzerindeki satın alma siparişleri için onay akışına ihtiyacı var."

Çıktıdan bir bölüm:
- Problem: Orta ölçekli müşterilerdeki finans yöneticileri büyük tutarlı satın alma siparişlerini gönderilmeden önce durduramıyor; bu da sonradan iptallere yol açıyor `[VARSAYIM – destek verisiyle doğrula]`.
- Hedef: Eşiğin üzerindeki siparişlerden gönderildikten sonra iptal edilenlerin payı 2 çeyrek içinde [TBD – başlangıç değeri] seviyesinden %2'nin altına iner.
- G3 (Must): Sistem, hesap eşiğinin üzerindeki bir siparişi onaylayıcı onaylayana veya reddedene kadar "Onay bekliyor" durumunda tutmalıdır.
  - Given eşik 10.000 ve sipariş 12.000, When alıcı siparişi gönderir, Then durum "Onay bekliyor" olur ve onaylayıcılara bildirim gider.
- Hedef dışı: Çok seviyeli onay zincirleri (sonraki faz).
