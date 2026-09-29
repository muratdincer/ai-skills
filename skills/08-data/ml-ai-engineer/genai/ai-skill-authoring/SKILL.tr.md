---
name: ai-skill-authoring
description: "Bu kütüphanenin yazım rehberine uyan yeni, taşınabilir ve iki dilli bir skill (İngilizce SKILL.md ve Türkçe SKILL.tr.md) yazar; katalog satırını, üç alanlı frontmatter'ı, sabit dokuz bölümü, yapısal sınırları ve içerik kurallarını kapsar. Kütüphaneye yeni bir skill eklenmek istendiğinde, tekrarlanan bir görev veya kontrol listesi skill'e dönüştürülecekken ya da bir skill taslağı kurallara uygunluk açısından incelenecekken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: ml-ai-engineer
  area: genai
  title: "Yeni YZ skill'i yazma"
  related: "prompt-design, llm-eval-set, document-review, technical-translation, style-guide-check"
  prompt: "Kütüphanemiz için destek mühendisinin müşteriye kesinti bildirimi yazmasına yardım eden yeni bir skill yaz; katalog satırını ve iki dil dosyasını ver."
---

# Yeni YZ Skill'i Yazma

## Amaç
Herhangi bir sohbet modelinin yalnızca konuşmayı girdi alarak izleyebileceği, isabetli açıklaması sayesinde doğru anda yüklenen ve kütüphanenin yapısal kontrolünden iki dilde de ilk denemede geçen bir skill üretmek.

## Ne zaman kullanılır
- Bir ekibin standartlaştırmaya değer, tekrarlanan bir görevi (doküman, analiz veya inceleme) olduğunda.
- Bir skill taslağının birleştirilmeden önce yazım rehberine göre kontrol edilmesi gerektiğinde.
- Mevcut bir prompt veya kontrol listesi kütüphanenin skill formatına dönüştürülecekse.

## Ne zaman kullanılmaz
- Tek bir özellik için tek seferlik bir talimatsa `prompt-design` kullanılır.
- Yapı değişmeden yalnızca Türkçe veya İngilizce metnin iyileştirilmesi gerekiyorsa `technical-translation` veya `document-review` kullanılır.

## Girdiler
Zorunlu:
- Skill'in yaptığı görev, hedef rol ve kullanıldığı 2-3 gerçek durum.
- Skill'in ürettiği çıktı (doküman, tablo, mesaj, inceleme).

İsteğe bağlı, kaliteyi artırır:
- Çıktının iyi bir gerçek örneği, uygulayıcıların sık yaptığı hatalar, ilgili standartlar.
- Katalogda hedeflenen kategori, rol ve alan; ilgili mevcut skill ID'leri.

Görev veya çıktı belirsizse her seferinde tek soru sor (bir grupta en fazla 5). İsteğe bağlı girdileri sorma; açık soru olarak listele.

## Süreç
1. Örtüşmeyi kontrol et: mevcut bir skill görevin çoğunu karşılıyorsa onu genişletmeyi öner; değilse küresel olarak benzersiz, küçük harfli, tireli, en fazla 64 karakterlik ve klasör adıyla aynı bir ID seç.
2. Katalog satırını taslak olarak yaz: `- <id> | <EN başlık> | <TR başlık> | <EN tek satır> | <TR tek satır>`; doğru `# kategori`, `## rol`, `### alan` altına yerleştir; klasör `skills/<category>/<role>/<area>/<id>/` olur.
3. Frontmatter'a yalnızca `description`, `related` ve `prompt` yaz (name, license ve metadata'yı araçlar ekler). Açıklama üçüncü şahıs ağzından yazılır, önce ne yaptığını sonra "... olduğunda kullanılır" ile tetikleyicileri söyler, XML etiketi içermez, en fazla 1024 karakterdir (hedef 250-450). `related` katalogda var olan 2-5 ID içerir ve iki dosyada birebir aynıdır. `prompt` gerçekçi tek bir kullanıcı isteğidir.
4. Gövdeyi, başlık düzeninde yazılmış katalog başlığına eşit bir H1 ile başlat, ardından dokuz bölümü sırasıyla yaz: Amaç, Ne zaman kullanılır, Ne zaman kullanılmaz, Girdiler, Süreç, Çıktı formatı, Kalite kontrol listesi, Sık yapılan hatalar, Örnek (İngilizce: Purpose, When to use, When not to use, Inputs, Process, Output format, Quality checklist, Common pitfalls, Example).
5. Amaç (sonuç ve neden önemli olduğu, 1-3 cümle), Ne zaman kullanılır (2-4 somut durum) ve Ne zaman kullanılmaz (her biri daha uygun skill'i ters tırnak içinde ID ile gösteren 1-3 durum) bölümlerini yaz.
6. Girdileri "Zorunlu:" ve "İsteğe bağlı:" listeleri olarak yaz; zorunlu girdi eksikse ne yapılacağını ekle: yalnızca ilerlemeyi engelleyeni sor, her seferinde tek odaklı soru sor, kullanıcının zaten verdiğini yeniden sorma.
7. Süreci 6-14 numaralı, somut, uzman seviyesinde adım olarak yaz; desteklenmeyen maddelerin `[BİLİNMİYOR]`, `[VARSAYIM]` veya `[TBD]` (İngilizce `[UNKNOWN]`, `[ASSUMPTION]`, `[TBD]`) ile işaretlenmesini, söylenen olgularla çıkarımların ayrılmasını, kişisel veri varsa maskelemeyi ve `related` içinden sonraki skill'i öneren son adımı dahil et.
8. Çıktı formatını yer tutuculu, çitli (fenced) bir markdown şablonu olarak; Kalite kontrol listesini son maddesi öz kontrol döngüsü olan ("Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.") 4-9 `- [ ]` maddesi olarak yaz.
9. 2-4 Sık yapılan hata (alan hatası ve nasıl önleneceği) ve kısa bir Örnek (girdi ve çıktıdan bir bölüm) yaz; kalitenin ince olduğu durumlarda güçlü sürümün yanında zayıf bir sürüm göster.
10. İçerik kurallarını uygula: YZ ürünü, araç çağrısı, dosya erişimi veya slash komutu yok; metodoloji varsayımı yok ("iterasyon/sprint", "backlog" de); standartlar tam adıyla anılır, asla birebir alıntılanmaz; zamana bağlı ifade yok; kıdemli okur, temel kavram anlatımı yok.
11. Türkçe dosyayı kelime kelime çeviri olarak değil, doğal ve profesyonel Türkçeyle yaz: aynı bölümler, aynı adım sayısı, aynı kontrol maddesi sayısı, aynı şablon alanları; ç, ğ, ı, İ, ö, ş, ü doğru kullanılır; Türk ekiplerinin kullandığı yaygın İngilizce sektör terimleri korunur.
12. Yapısal sözleşmeye göre doğrula (her dosya 40-200 satır, hedef 60-130; adım ve kontrol maddesi sayıları aynı; related ID'ler geçerli), açık soruları listele ve skill'i gerçekçi prompt'larla test etmek için `llm-eval-set` öner.

## Çıktı formatı
```markdown
Katalog satırı:
- <id> | <EN başlık> | <TR başlık> | <EN tek satır> | <TR tek satır>
Yol: skills/<category>/<role>/<area>/<id>/

--- SKILL.md ---
---
description: <what it does>. Use when <triggers>.
related: <id-1>, <id-2>, <id-3>
prompt: <realistic request>
---

# <EN Title In Title Case>
## Purpose
## When to use
## When not to use
## Inputs
## Process
## Output format
## Quality checklist
## Common pitfalls
## Example

--- SKILL.tr.md ---
<aynı frontmatter anahtarları Türkçe, `related` birebir aynı; Türkçe başlıklar>

Uygunluk notları: <EN/TR adım sayısı, EN/TR kontrol maddesi sayısı, satır sayıları, açık sorular>
```

## Kalite kontrol listesi
- [ ] Açıklama skill'in ne yaptığını ve ne zaman kullanılacağını üçüncü şahıs ağzından, en fazla 1024 karakterle söylüyor.
- [ ] Dokuz başlığın tamamı iki dosyada da rehberdeki birebir ifadeyle ve sırayla yer alıyor.
- [ ] Süreç 6-14 adım, kontrol listesi 4-9 madde ve sayılar iki dilde aynı.
- [ ] Tüm `related` ve "ne zaman kullanılmaz" ID'leri katalogda var; `related` iki dosyada birebir aynı.
- [ ] Araç adı, ürün adı, metodoloji varsayımı veya zamana bağlı iddia yok; eksik veri işaretli, asla uydurulmadı.
- [ ] Son süreç adımı ilgili bir skill'e devrediyor ve son kontrol maddesi öz kontrol döngüsü.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Belirsiz açıklama ("Dokümanlarla yardımcı olur"). Araçlar skill'i bu satıra göre yükler; çıktıyı ve somut tetikleyicileri adlandır.
- Genel adımlar ("Girdiyi analiz et", "Çıktıyı yaz"). Her adım, bir yeni başlayanın bilmeyeceği bir alan sezgisi içermeli.
- Türkçeyi kelime kelime çevirmek veya iki dosyanın yapısını birbirinden uzaklaştırmak. Yapıyı aynı, ifadeyi doğal tut.

## Örnek
Girdi: "Müşteriye kesinti bildirimi yazmak için skill."

Zayıf açıklama: "Kesinti bildirimi skill'i. Bildirim yazmaya yardım eder."

Güçlü açıklama: "Etkiyi, etkilenen hizmetleri, güncel durumu, sonraki güncelleme zamanını ve geçici çözümü içeren, iç jargondan arındırılmış sade dilde müşteriye yönelik kesinti bildirimi yazar. Bir olay müşterileri etkilediğinde ve ilk ya da takip bildiriminin yayımlanması gerektiğinde kullanılır."

Uygunluk notlarından bir bölüm: Süreç 9/9 adım, kontrol listesi 6/6 madde, related `incident-communication, incident-response, customer-outage-notice` katalogla karşılaştırıldı.
