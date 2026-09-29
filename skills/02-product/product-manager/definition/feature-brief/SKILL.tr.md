---
name: feature-brief
description: "Ekibi tek bir özellik etrafında hizalayan tek sayfalık bir özellik özeti yazar: problem ve kimin yaşadığı, beklenen sonuç ve başarı sinyali, önerilen yaklaşım, kapsam sınırları, temel riskler ve hâlâ gereken kararlar. Özellik tam bir PRD gerektirmeyecek kadar küçükse, bir paydaş kickoff veya refinement öncesinde \"kısa bir yazı\" istediğinde ya da bir talebin yap/yapma görüşmesi için çerçevelenmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: definition
  title: "Özellik özeti yazma"
  related: "prd-writing, hypothesis-statement, mvp-scoping, epic-breakdown, problem-statement"
  prompt: "CRM'imize kişilerin toplu CSV ile içe aktarılması için bir özellik özeti yaz."
---

# Özellik Özeti Yazma

## Amaç
Bir özellikte yer alan herkese "neden bu, kimin için, bitmiş hali neye benziyor ve neleri yapmıyoruz" sorusuna aynı kısa yanıtı vermek; böylece refinement ve tasarım varsayımlardan değil ortak niyetten başlar.

## Ne zaman kullanılır
- Özellik kabaca bir ile birkaç iterasyona sığıyor ve tam bir spesifikasyon değil hizalama gerekiyorsa.
- Kickoff, tasarım oturumu veya backlog refinement öncesinde.
- Bir paydaşın yap/yapma veya önceliklendirme kararı için kısa bir dayanağa ihtiyacı olduğunda.

## Ne zaman kullanılmaz
- Girişim birçok ekibe veya iterasyona yayılıyor ya da uyum yükü taşıyorsa `prd-writing` kullanılır.
- Temel problem hâlâ belirsizse önce `problem-statement` kullanılır.
- Özellik üzerinde anlaşıldı ve hikayelere bölünmesi gerekiyorsa `epic-breakdown` kullanılır.

## Girdiler
Zorunlu:
- Özellik fikri veya talebi ve hedeflediği kullanıcı grubu.

İsteğe bağlı, kaliteyi artırır:
- Kanıtlar (kayıtlar, geri bildirim temaları, analitik), ilgili hedefler veya OKR'ler.
- Bilinen kısıtlar: son tarih ve nedeni, platformlar, bağımlılıklar.
- Kaba çözüm fikirleri veya tasarımlar.

Özellik veya kullanıcıları eksikse sor. Bilinmeyenleri baştan sormak yerine açık kararlarda `[TBD]` olarak tut.

## Süreç
1. Sözel talebi asıl ihtiyaçtan ayır; problemi çözüm içermeden 2-3 cümleyle (kim, durum, etki) yaz, kanıtı not et ya da `[VARSAYIM]` olarak işaretle.
2. Beklenen sonucu ve hedefli ya da `[TBD]` olan tek bir birincil başarı sinyalini yaz; özellik başka bir şeye zarar verebilecekse koruma metriği ekle.
3. Önerilen yaklaşımı uygulama düzeyinde değil, kullanıcıya görünen davranış düzeyinde anlat (3-6 adımlık ana akış).
4. Kapsam çizgilerini çiz: kapsam içi, açıkça kapsam dışı ve "sonra" fikirleri.
5. UX hususlarını not et: giriş noktaları, boş/hata durumları, yetkiler, erişilebilirlik.
6. Bağımlılıkları ve en önemli 3 riski (değer, kullanılabilirlik, yapılabilirlik, sürdürülebilirlik) her biri için bir önlem veya testle listele.
7. Kaba büyüklük sinyalini yalnızca ekip verdiyse yaz; aksi halde `[TBD – ekip tahmini]` olarak işaretle.
8. Açık kararları sorumlu ve gereken tarihle listele; başlamayı engellemeyen açık sorulardan ayır.
9. Tek sayfaya indir: ayrıntıları bağlantılara taşı.
10. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: hikaye oluşturmak için `epic-breakdown`, sonuç önce test edilecek kadar belirsizse `hypothesis-statement`, kapsam daha büyük çıkarsa `prd-writing`.

## Çıktı formatı
```markdown
# Özellik Özeti: <özellik adı>
Sahibi: <ad> · Durum: <taslak/üzerinde anlaşıldı> · Tarih: <tarih> · İlgili hedef: <OKR/hedef | [TBD]>

**Problem:** <kim, durum, etki> (kanıt: ...)
**Sonuç ve başarı sinyali:** <metrik, başlangıç -> hedef, zaman aralığı> · Koruma metriği: ...

**Önerilen yaklaşım**
1. ...

| Kapsam içi | Kapsam dışı | Sonra |
|---|---|---|
| ... | ... | ... |

**UX notları:** ...
**Bağımlılıklar:** ...
**Riskler:** <risk> – <önlem/test>
**Büyüklük sinyali:** <ekip tahmini | [TBD]>

**Açık kararlar**
| Karar | Sorumlu | Gereken tarih |
|---|---|---|
```

## Kalite kontrol listesi
- [ ] Problem çözüm içermeden yazıldı ve belirli bir kullanıcı grubunu adlandırıyor.
- [ ] Tek bir birincil başarı sinyali var; ölçülmüş ya da `[TBD]`, asla uydurulmamış.
- [ ] Kapsam dışı açıkça yazıldı ve boş değil.
- [ ] Yaklaşım uygulamayı değil davranışı anlatıyor.
- [ ] Özet tek sayfaya sığıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Özetin PRD'ye dönüşmesine izin vermek. Bir sayfadan fazlası gerekiyorsa özellik çok büyüktür ya da özet hikayelere ait ayrıntı taşıyordur.
- "Kapsam dışı"nı boş bırakmak. Her özelliğin cazip komşuları vardır; geri sızmasınlar diye adlarını yaz.
- Çıktıyı başarı sinyali olarak kullanmak ("özellik yayınlandı"). Değişmesi gereken davranışı adlandır.

## Örnek
Girdi: "CRM'imize kişilerin toplu CSV ile içe aktarılmasını ekleyelim."

Çıktıdan bir bölüm:
- Problem: Yeni katılan hesaplardaki satış operasyon yöneticileri, tablolardan geçiş yaparken yüzlerce kişiyi elle giriyor ve ilk kullanım günlerce gecikiyor `[VARSAYIM – onboarding kayıtlarını kontrol et]`.
- Başarı sinyali: Hesap açılışından 100 kişiye ulaşmaya kadar geçen medyan süre [TBD] seviyesinden 1 günün altına iner.
- Kapsam dışı: Harici CRM'lerle senkronizasyon; birebir e-posta eşleşmesinin ötesinde tekilleştirme.
- Risk (kullanılabilirlik): Sütun eşleştirme hataları – 5 yöneticiyle kendi gerçek dosyaları (anonimleştirilmiş) üzerinden test et.
