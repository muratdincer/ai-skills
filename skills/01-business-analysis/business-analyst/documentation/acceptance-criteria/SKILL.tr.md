---
description: "Bir kullanıcı hikayesi veya gereksinim için Given/When/Then senaryoları ya da kural biçiminde test edilebilir kabul kriterleri yazar; mutlu yolu, iş kuralı varyasyonlarını, doğrulamayı, yetkileri ve hata durumlarını senaryo başına tek tetikleyici ve tek sonuçla kapsar. Bir hikayenin tamamlanma koşulları gerektiğinde, kriterler muğlak veya test edilemez olduğunda ya da 'kabul kriteri', 'AC', 'Gherkin' veya 'Given/When/Then' istendiğinde kullanılır."
related: "user-story, invest-check, edge-case-elicitation, bdd-feature-file, test-scenarios-from-requirements"
prompt: "Şu hikaye için kabul kriterleri yaz: Mağaza müdürü olarak bekleyen bir vardiya değişimini telefonumdan onaylamak veya reddetmek istiyorum."
---

# Kabul Kriteri Yazma

## Amaç
Bir hikayenin veya gereksinimin tamamlanmış sayılması için neyin doğru olması gerektiğini, hem iş biriminin hem test ekibinin kabul edeceği terimlerle tanımlamak; böylece gözden geçirme anında yoruma yer kalmaz.

## Ne zaman kullanılır
- Bir hikaye veya gereksinim refinement'a hazır ama kriterleri yoksa.
- Mevcut kriterler muğlaksa ("doğru çalışır", "hızlı", "kullanıcı dostu").
- Test ekibi veya otomasyon, bir hikayeye izlenebilir senaryolara ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- Hikayenin kendisi belirsizse veya somut persona ve sonuç içermiyorsa önce `user-story` kullanılır.
- Bir otomasyon çatısı için çalıştırılabilir feature dosyaları gerekiyorsa `bdd-feature-file` kullanılır.
- Veri kombinasyonlarıyla tam bir test tasarımı gerekiyorsa `test-scenarios-from-requirements` kullanılır.

## Girdiler
Zorunlu:
- Kullanıcı hikayesi veya gereksinim cümlesi.

İsteğe bağlı, kaliteyi artırır:
- İş kuralları, veri tanımları, ekran veya API davranışı, yetkiler, bilinen uç durumlar, ekibin tercih ettiği kriter formatı.

Hikaye yoksa iste. Sonucu belirleyen bir kural (limit, durum, rol) bilinmiyorsa kısa tek bir soru grubu hâlinde sor; aksi hâlde kriterde `[TBD]` olarak işaretle.

## Süreç
1. Hikayenin sonucunu tek satırda yeniden ifade et ve dayandığı iş kurallarını listele. Çıkardığın her kuralı `[VARSAYIM]` olarak etiketle.
2. Formatı seç: durum ve sıra içeren davranış için Given/When/Then; basit kısıtlar için kural biçimi ("Vardiya başladıktan sonra değişim onaylanamaz"). Bir hikayede tek formatı tutarlı kullan.
3. Önce mutlu yol senaryosunu yaz.
4. Hikayeyle ilgili her kural varyasyonu, doğrulama hatası, yetki sınırı ve hata veya zaman aşımı durumu için bir senaryo ekle.
5. Senaryo başına tek When ve tek Then kuralını uygula. Birden fazla tetikleyici veya sonuç varsa birden fazla senaryo yaz; Then içindeki "And" yalnızca aynı sonucun parçaları için kullanılabilir.
6. Her Then'i gözlemlenebilir ve ölçülebilir yap: durum, mesaj, kayıt, bildirim veya sayı. Muğlak kelimeleri somut değerlerle, bilinmiyorsa `[TBD]` ile değiştir.
7. Given içinde soyut ifadeler yerine somut örnek veri kullan (adı konmuş bir durum, bir tutar, bir tarih ilişkisi); kişisel verileri maskele.
8. Kriterleri uygulamadan bağımsız tut: üzerinde anlaşılmış sözleşmenin parçası değilse UI kontrolü, tablo adı veya endpoint yazma.
9. Kapsamı hikayeye göre kontrol et: her kuralın ve fayda kısmındaki sonucun en az bir senaryosu olsun; başka bir hikayeye ait kapsam kaymasını işaretle.
10. Açık soruları ve varsayımları muhataplarıyla listele.
11. Hedef devam ediyorsa daha derin sınır durumları için `edge-case-elicitation`, hikaye kalitesi için `invest-check`, otomasyon için `bdd-feature-file` öner.

## Çıktı formatı
```markdown
# Kabul Kriterleri: <hikaye ID ve başlığı>
Referans kurallar: <BR-xx, ...>

### AC-1 <senaryo adı> (mutlu yol)
Given <somut veriyle bağlam>
When <tek tetikleyici>
Then <tek gözlemlenebilir sonuç>

### AC-2 <senaryo adı>
...

### Kural biçiminde kriterler (kullanıldıysa)
- R-1 <kısıt>

## Bu hikayenin kapsamı dışında
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
1. <soru> — <muhatap>
```

## Kalite kontrol listesi
- [ ] Her senaryoda tam olarak bir When ve bir Then sonucu var.
- [ ] Her Then gözlemlenebilir ve muğlak terim içermiyor.
- [ ] İlgili olduğu yerde mutlu yol, kural varyasyonları, doğrulama, yetki ve hata durumları kapsandı.
- [ ] Kriterler UI kontrolünü veya uygulamayı değil davranışı tarif ediyor.
- [ ] Her kural ve hikayenin sonucu en az bir kritere izlenebiliyor.
- [ ] Bilinmeyen değerler `[TBD]`, çıkarılan kurallar `[VARSAYIM]`; hiçbir şey uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
| Hata | Düzeltme |
|---|---|
| "Then sistem doğru çalışır" | Bunu kanıtlayan durumu, mesajı veya kaydı tam olarak adlandır. |
| Bir senaryoda iki When | İki senaryoya böl; her biri tek tetikleyiciyi test etsin. |
| Yalnızca mutlu yol | Ret, geçersiz girdi, yetkisizlik ve zaman aşımı senaryoları ekle. |
| Hikayeyi tekrar eden kriterler | Kriterler hikayenin söylemediği koşulları eklemeli. |

## Örnek
Girdi: "Mağaza müdürü olarak bekleyen bir vardiya değişimini telefonumdan onaylamak veya reddetmek istiyorum."

Zayıf: "Müdür değişimleri onaylayıp reddedebilir ve her şey güncellenir."

Güçlü:
### AC-1 Bekleyen değişimi onaylama
Given iki çalışan arasında durumu "Beklemede" olan bir değişim talebi
When mağaza müdürü talebi onaylar
Then iki çalışanın çizelgesinde değiştirilmiş vardiyalar görünür ve talebin durumu "Onaylandı" olur

### AC-2 Başlamış vardiya için değişim
Given vardiyası 10 dakika önce başlamış bir değişim talebi
When mağaza müdürü talebi onaylamaya çalışır
Then onay, vardiyanın başladığını belirten mesajla reddedilir

Açık soru: Ret için gerekçe zorunlu mu? `[TBD]` — Operasyon
