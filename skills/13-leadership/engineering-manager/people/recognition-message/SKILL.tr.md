---
description: Bir kişi veya ekip için somut davranışı, ortaya çıkardığı sonucu ve neden önemli olduğunu belirten, kanala (özel, ekip, şirket geneli) uygun, somut ve etki odaklı bir takdir mesajı yazar. Bir yönetici veya ekip arkadaşı birine emeği için teşekkür etmek, görünmeyen katkıları öne çıkarmak ya da bir lansmanı, olay müdahalesini veya mentorluk çabasını kutlamak istediğinde kullanılır.
related: feedback-sbi, announcement, tone-rewrite, performance-review
prompt: Hafta sonunu veri taşıma geri alma işini çözmeye harcayan ve temiz bir postmortem yazan Selin için ekip kanalına teşekkür mesajı yaz.
---

# Takdir Mesajı Yazma

## Amaç
Katkıları alıcının samimi bulacağı biçimde takdir etmek ve ne yapıldığını ve etkisini somut olarak söyleyerek ekibe hangi davranışların önemli olduğunu göstermek.

## Ne zaman kullanılır
- Biri takdiri hak eden bir iş yaptığında: teslimat, olay yönetimi, mentorluk, kalite veya görünmeyen emek.
- Bir lansman veya kilometre taşında daha az görünür roller dahil tüm katkı verenler anılmalıysa.
- Yönetici ekip değerleriyle uyumlu bir davranışı pekiştirmek istediğinde.

## Ne zaman kullanılmaz
- Gelişim odaklı veya düzeltici geri bildirim için `feedback-sbi` kullanılır.
- Resmi değerlendirme metinleri için `performance-review` kullanılır.
- Genel bir sürüm veya organizasyon duyurusu için `announcement` kullanılır.

## Girdiler
Zorunlu:
- Kimin takdir edildiği ve ne yaptığı (en az bir somut örnek).

İsteğe bağlı, kaliteyi artırır:
- Ölçülebilir veya gözlemlenebilir etki (kullanıcılar, kazanılan zaman, olay süresi, önlenen risk).
- Kanal ve hedef kitle: özel mesaj, ekip kanalı, genel toplantı, yöneticisine yazılı not.
- Biliniyorsa kişinin açık veya özel takdir tercihi.
- Bağlanabilecek ekip değerleri veya ilkeleri.

Somut bir örnek yoksa iste; genel övgünün değeri düşüktür.

## Süreç
1. Belirli davranışı (ne yaptı) belirle ve sonuçtan (bunun sayesinde ne değişti) ayır.
2. Etkiyi yalnızca kullanıcının verdiği sayılarla nicelleştir; yoksa nitel olarak anlat. Rakam uydurma.
3. Neden önemli olduğunu açıkla: kullanıcı, müşteri, ekip veya iş sonucu ya da gösterdiği bir değer.
4. Anlamlı katkı veren herkesi an; gözden kaçan katkıcıları kontrol et (inceleyenler, test edenler, nöbetçiler, destek, dokümantasyon).
5. Kanala uy: Özel notlar kişisel olabilir; açık mesajlar profesyonel kalır ve özel ayrıntı içermez.
6. Tercihlere saygı göster: Kişinin özel takdiri tercih ettiği biliniyorsa özel mesaj ve isteğe bağlı olarak yöneticisine bir not öner.
7. Kısa tut: 3-6 cümle, üst üste yığılmış abartılı sıfatlar yok, başkalarıyla karşılaştırma yok.
8. Aşırı çalışmayı ideal olarak yüceltme (ör. hafta sonu mesaisini övmek); gerekiyorsa sürdürülebilirliğe de değin.
9. Faydalıysa bir alternatif sürüm (daha kısa veya başka bir kanal için) sun.
10. Kullanıcının hedefi devam ediyorsa daha geniş bir kitle için `announcement` veya kanıtı değerlendirme dönemine kaydetmek için `performance-review` öner.

## Çıktı formatı
```markdown
**Kanal:** <özel / ekip / şirket / yöneticiye not>

<Açılış: kim ve ne, tek cümle>
<Somut ayrıntıyla belirli davranış>
<Etki ve neden önemli olduğu>
<Varsa katkı veren diğer kişilere teşekkür>
<Kapanış teşekkürü>

---
Alternatif (<kanal>): <kısa sürüm>
```

## Kalite kontrol listesi
- [ ] Yalnızca bir özellik ("harika iş") değil, en az bir somut davranış belirtiliyor.
- [ ] Etki gerçek: sayılar yalnızca verildiyse, yoksa nitel.
- [ ] Anlamlı katkı veren herkes anıldı.
- [ ] Ton kanala uygun; açık mesajlarda özel ayrıntı yok.
- [ ] Sürdürülemez çabayı yüceltmiyor.
- [ ] 3-6 cümle.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Herkese gönderilebilecek genel övgü ("süperstar", "muhteşem iş"). Eylemi adlandır.
- Bir olay veya lansmanda yalnızca görünür kahramanı takdir etmek. Başka kimin yardım ettiğini sor.
- Bazı kişileri sürekli açıkça takdir edip diğerlerini hiç anmamak. Takdiri zaman içinde ekip genelinde adil tut.

## Örnek
Girdi: "Selin hafta sonunu veri taşıma geri alma işini çözmeye harcadı ve temiz bir postmortem yazdı."

Çıktıdan bir bölüm (ekip kanalı):
"Selin, cumartesi günü veri taşıma geri alma işine liderlik ettiğin için teşekkürler. Veri yeniden tutarlı hale gelene kadar geri alma işini sürdürdün, ardından tüm ekibin ders çıkarabileceği kadar net bir postmortem yazdın. Sakin olay yönetimi ile dürüst takibin bu birleşimi, hatalardan öğrenme biçimimizin ta kendisi. `[Varsa yardım eden diğer kişileri ekle – girdide belirtilmemiş]` Selin, bu hafta o zamanı geri almayı unutma."
