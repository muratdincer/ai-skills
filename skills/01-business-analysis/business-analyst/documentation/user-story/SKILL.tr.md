---
description: "Kullanıcı hikayelerini somut bir persona, gerçek bir sonuç, bağlam, iş kuralları, bağımlılıklar ve kabul kriteri başlıklarıyla \"... olarak ... istiyorum ki ...\" kalıbında yazar; aslında teknik görev olan veya bölünmesi gereken maddeleri işaretler. Bir ihtiyaç, gereksinim veya özelliğin backlog maddelerine dönüşmesi gerektiğinde ya da 'hikaye yaz', 'bunu user story'ye çevir' veya zayıf hikayeleri yeniden yaz dendiğinde kullanılır."
related: "acceptance-criteria, invest-check, story-splitting, persona, epic-breakdown"
prompt: "Mağaza müdürlerinin personel vardiya değişimlerini telefondan onaylayabilmesi için kullanıcı hikayeleri yaz."
---

# Kullanıcı Hikayesi Yazma

## Amaç
Bir ihtiyacı; kimin fayda sağladığını, ne yapabildiğini ve bunun neden önemli olduğunu söyleyen, küçük ve değerli backlog maddelerine çevirmek. Böylece ekip her birini bağımsız olarak konuşabilir, tahminleyebilir ve doğrulayabilir.

## Ne zaman kullanılır
- Bir özellik, gereksinim veya talep kaydının backlog maddelerine dönüşmesi gerektiğinde.
- Mevcut hikayeler muğlaksa ("Kullanıcı olarak bir buton istiyorum") ve yeniden yazılmaları gerektiğinde.
- Bir refinement oturumunda tartışılacak taslak hikayelere ihtiyaç olduğunda.

## Ne zaman kullanılmaz
- İş hâlâ büyük ve şekillenmemiş bir yetkinlikse önce `epic-breakdown` veya `story-mapping` kullanılır.
- Mevcut bir hikaye için yalnızca tamamlanma koşulları gerekiyorsa `acceptance-criteria` kullanılır.
- Var olan bir hikaye daha küçük parçalara bölünecekse `story-splitting` kullanılır.

## Girdiler
Zorunlu:
- Hikayeye dönüştürülecek ihtiyaç, özellik tarifi veya gereksinim.

İsteğe bağlı, kaliteyi artırır:
- Personalar veya kullanıcı rolleri, iş kuralları, süreç modeli, ekran taslakları, ekibin hikaye şablonu ve Definition of Ready.

İhtiyaç yoksa iste. Kullanıcı rolleri belirsizse işi kimin yaptığına dair tek bir soru sor; aksi hâlde hikayeleri yaz ve eksikleri açık soru olarak listele.

## Süreç
1. Girdiden aktörleri belirle. "Kullanıcı" değil, somut bir persona veya rol kullan ("mağaza müdürü", "ilk kez başvuran aday"); rol çıkarımsa `[VARSAYIM]` olarak işaretle.
2. Her aktör için kullanıcı hedeflerini fiil + nesne olarak listele. Talep sahibinin söylediğini kendi çıkarımından ayır.
3. Her hikayeyi yaz: "<somut persona> olarak, <sonuç> için <yetkinlik> istiyorum." "Ki/için" kısmı isteği tekrar etmemeli; gerçek bir fayda (kazanılan zaman, önlenen risk, mümkün kılınan karar) söylemeli.
4. Hikaye kılığındaki teknik görevleri yakala ("Geliştirici olarak veritabanını taşımak istiyorum"). Bunları mümkün kıldıkları kullanıcı değerine göre yeniden çerçevele veya hikaye seti dışında teknik iş maddesi olarak işaretle.
5. Boyutu kontrol et: hikayede "ve", birden fazla rol, akış veya veri çeşidi varsa bölmeyi öner ve bölme kalıbını adlandır (akış adımı, kural varyasyonu, veri tipi, mutlu/mutsuz yol).
6. Her hikayeye bağlam ekle: iş kuralları (katalog varsa ID ile), ilgili veri, bağımlılıklar ve kapsam dışı notları.
7. Her hikaye için 2-5 kabul kriteri başlığı taslağı yaz (kural biçiminde, her biri tek sonuç); ayrıntılı Given/When/Then'i `acceptance-criteria`'ya bırak.
8. Hikayeleri, ilki uçtan uca ince bir dilim teslim edecek şekilde sırala; bağımlılıkları açıkça yaz.
9. Varsayımları ve açık soruları muhtemel muhataplarıyla topla; kural, limit veya sayı uydurma.
10. Hedef devam ediyorsa ayrıntılı kriterler için `acceptance-criteria`, kalite incelemesi için `invest-check`, büyük hikayeler için `story-splitting` öner.

## Çıktı formatı
```markdown
# Kullanıcı Hikayeleri: <özellik>
Personalar: <liste> · Kaynak: <gereksinim / talep ID>

## US-01 <kısa başlık>
<somut persona> olarak, <sonuç> için <yetkinlik> istiyorum.
- Bağlam / kurallar: <BR-xx, notlar>
- Kabul kriterleri (başlıklar):
  1. ...
- Bağımlılıklar: ...
- Kapsam dışı: ...
- Bölme önerisi: <yok / kalıp + önerilen hikayeler>

## Teknik iş maddeleri (kullanıcı hikayesi değil)
- ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
1. <soru> — <muhatap>
```

## Kalite kontrol listesi
- [ ] Her hikaye somut bir persona adlandırıyor; hiçbiri "kullanıcı olarak" veya "sistem olarak" demiyor.
- [ ] Her hikayenin fayda kısmı, istenen yetkinlikten farklı bir sonuç söylüyor.
- [ ] Teknik görevler kullanıcı hikayelerinden ayrıldı.
- [ ] Her hikaye tek bir yetkinlik tarif ediyor; bileşik hikayelerde bölme önerisi var.
- [ ] Her hikayenin, her biri tek sonuçlu kabul kriteri başlıkları var.
- [ ] Kural, limit veya sayı uydurulmadı; çıkarımlar etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
| Hata | Düzeltme |
|---|---|
| "Kullanıcı olarak..." | Hedef kimin ise o rolü adlandır; farklı roller genellikle farklı hikayeler demektir. |
| "Özelliği kullanabilmek için" | Bir iş veya kullanıcı sonucu ortaya çıkana kadar "bu neden önemli?" diye sor. |
| Hikaye arayüzü tarif ediyor ("bir açılır liste") | Yetkinliği tarif et; kontrol seçimini tasarıma bırak. |
| Katmana göre bölünmüş hikayeler (UI hikayesi, API hikayesi) | Her hikaye tek başına kullanılabilir olsun diye dikey dilimle. |

## Örnek
Girdi: "Mağaza müdürleri vardiya değişimlerini mobilden onaylasın."

Zayıf: "Kullanıcı olarak, değişimleri onaylayabilmek için bir değişim onay ekranı istiyorum."

Güçlü:
US-01 Mağaza müdürü olarak, arka ofiste olmadan personel açığını vardiya başlamadan kapatabilmek için bekleyen bir vardiya değişimini telefonumdan onaylamak veya reddetmek istiyorum.
- Kurallar: değişim yalnızca aynı yetkinliğe sahip personel arasında yapılabilir `[VARSAYIM – İK ile teyit et]`.
- Kabul kriteri başlıkları: 1. Onaylanan değişim iki çalışanın çizelgesini de günceller. 2. Ret, iki çalışana gerekçesiyle bildirilir. 3. Başlamış bir vardiya için değişim onaylanamaz.
- Açık soru: Vardiya başlangıcından ne kadar önce değişimler kilitleniyor? — Operasyon
