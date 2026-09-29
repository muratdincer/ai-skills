---
name: requirements-interview
description: "Kullanıcıyla her seferinde tek soru sorarak ve her soruyu önceki cevaba göre uyarlayarak (teşhis et, daralt, teyit et) görüşme yapar; güncel bir spesifikasyonu görünür tutar, hazır olma kontrol listesi karşılandığında durur ve yapılandırılmış bir gereksinim özetiyle bitirir. Bir ihtiyaç belirsiz olduğunda (\"bir dashboard lazım\", \"onayları otomatikleştirelim\"), kullanıcı \"bana soru sor\", \"bunu netleştirmeme yardım et\" dediğinde veya zayıf bir girdiden story ya da PRD yazılmadan önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: elicitation
  title: "Etkileşimli gereksinim görüşmesi"
  related: "request-clarification-questions, requirements-gap-analysis, user-story, acceptance-criteria, edge-case-elicitation"
  prompt: "Geliştirilebilecek netliğe gelene kadar benimle görüş: tedarikçilerin faturalarını e-postayla göndermek yerine kendilerinin yüklemesini istiyoruz."
---

# Etkileşimli Gereksinim Görüşmesi

## Amaç
Belirsiz bir ihtiyacı, kullanıcıya uzun bir soru listesi vermek yerine en az sayıda ve en isabetli soruyu tek tek sorarak ekibin geliştirip test edebileceği bir spesifikasyona dönüştürmek.

## Ne zaman kullanılır
- Kullanıcının bir fikri veya problemi var ama spesifikasyonu yok ve şu anda cevap verebilecek durumda.
- Talep; story, kabul kriteri veya PRD yazmak için fazla zayıf.
- Kullanıcı açıkça kendisiyle görüşülmesini veya soru sorulmasını istiyor.

## Ne zaman kullanılmaz
- Talep sahibine şu anda ulaşılamıyorsa ve sorular tek seferde gönderilecekse `request-clarification-questions` kullanılır.
- Yazılı bir spesifikasyon var ve boşlukları kontrol edilecekse `requirements-gap-analysis` kullanılır.
- Üçüncü kişilerle yapılacak bir paydaş görüşmesi planlanacaksa `interview-question-set` kullanılır.

## Girdiler
Zorunlu:
- İhtiyacın ilk ifadesi, tek cümle bile olsa.

İsteğe bağlı, kaliteyi artırır:
- Mevcut dokümanlar, ekran görüntüleri, bugünkü süreç, kısıtlar, son tarih.
- Kullanıcıların kim olduğu ve kararı kimin verdiği.

İlk ifade yoksa ilk soru olarak "Ne elde etmek istiyorsun ve kimin için?" diye sor. Kullanıcının zaten söylediği bir şeyi asla yeniden sorma.

## Süreç
1. İhtiyacın tek satırlık yeniden ifadesi ve taslak bir güncel spesifikasyonla (aşağıdaki bölümler, çoğu `[BİLİNMİYOR]`) başla. Kullanıcıya istediği an "geç" veya "bilmiyorum" diyebileceğini söyle.
2. Teşhis et: önce asıl hedefi ve tetikleyiciyi sor (neden şimdi, bugün ne oluyor, ne ters gidiyor). Kelimesi kelimesine istenenle asıl ihtiyacı ayır.
3. Sonraki soruyu tek bir kurala göre seç: en çok başka kararı engelleyen bilinmeyen. Her turda tam olarak TEK soru sor, işe yarıyorsa 2-4 olası seçenek sun ve neden sorduğunu kısaca belirt.
4. Daralt: her cevaptan sonra spesifikasyonu güncelle, yeni olguları `[teyitli]`, kendi çıkarımlarını `[çıkarım]` olarak işaretle; ardından şu öncelikle derinleş: aktörler, ana akış, veri, kurallar, yetkiler, istisnalar ve fonksiyonel olmayan ihtiyaçlar.
5. Cevaplardaki çelişkileri veya belirsiz ifadeleri ("hızlı", "hepsi", "genelde") yakala ve devam etmeden önce ölçülebilir hâle getirmek için tek bir takip sorusu sor.
6. Her 4-5 soruda bir, kullanıcının düzeltebilmesi için özet spesifikasyonu göster.
7. Teyit et: hazır olma listesi karşılanmış görünüyorsa temel kararları 3-6 maddeyle geri oku ve kullanıcıdan teyit veya düzeltme iste. "Geç"/"bilmiyorum" cevaplarını, hazır olma listesini engellemedikleri sürece engel değil sahibi belli açık soru olarak ele al.
8. Hazır olma listesi karşılandığında veya kullanıcı durmak istediğinde dur; olsa iyi olur türünden ayrıntıları sorma.
9. Zorunlu ihtiyaçlar, başarı kriterleri, kesin istenmeyenler (açıkça istemedikleri), açık sorular ve varsayımlarla nihai yapılandırılmış özeti üret.
10. Sonraki beceriyi öner: özeti backlog öğelerine çevirmek için `user-story` veya `acceptance-criteria`, akışı zorlamak için `edge-case-elicitation`, resmi bir bütünlük kontrolü için `requirements-gap-analysis`.

Hazır olma listesi: hedef ve başarı ölçütü; birincil kullanıcılar/aktörler; tetikleyici ve ana akış; temel girdi/çıktı verisi; iş kuralları ve yetkiler; ana istisnalar; önemli NFR'ler (hacim, güvenlik, erişilebilirlik süresi); kapsam dışı; karar sahibi.

## Çıktı formatı
```markdown
<!-- Görüşme sırasında her tur: -->
**S<n> (<konu>):** <tek soru> — *neden:* <tek satır>
Seçenekler: a) ... b) ... c) diğer

<!-- Nihai özet -->
# Gereksinim Özeti: <başlık>
**İhtiyaç (kelimesi kelimesine):** ... **Asıl hedef:** ...
**Başarı kriterleri:** <ölçülebilir>
## Aktörler ve Yetkiler
## Ana Akış
1. ...
## Veri (girdi / çıktı / saklanan)
## İş Kuralları
## İstisnalar ve Uç Durumlar
## Fonksiyonel Olmayan Gereksinimler
## Kapsam Dışı / Kesin İstenmeyenler
## Varsayımlar ([çıkarım])
## Açık Sorular – <sahibi>
## Hazır olma: <karşılanan madde> / 9 – <hâlâ eksik olan>
```

## Kalite kontrol listesi
- [ ] Her turda tam olarak bir soru soruldu (açıkça istenirse en fazla 5'lik grup) ve bilinen hiçbir bilgi yeniden sorulmadı.
- [ ] Özetteki her madde bir cevaba dayanıyor ya da `[çıkarım]`/`[VARSAYIM]` olarak etiketli.
- [ ] Belirsiz ifadeler ölçülebilir hâle getirildi veya açık soru olarak listelendi.
- [ ] Hazır olma listesi açıkça değerlendirildi ve eksikler adıyla belirtildi.
- [ ] Yalnızca özellikler değil, kesin istenmeyenler ve kapsam dışı maddeler de kaydedildi.
- [ ] Cevaplarda geçen kişisel veriler özette en aza indirildi veya maskelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tek seferde 20 soru yığmak. Kullanıcı kolay olanları cevaplar, kritik olanlar açık kalır.
- Hedef ve akış netleşmeden arayüz ayrıntılarını sormak. Öncelik sırasını izle.
- Hiç durmamak. Hazır olma noktasında dur; kalan ayrıntılar açık soru olur.
- Boşlukları sessizce kendi tasarımınla doldurmak. Seçenek sun, seçimi kullanıcı yapsın.

## Örnek
Girdi: "Tedarikçiler faturalarını e-postayla göndermek yerine kendileri yüklesin."

Zayıf ilk tur: "Lütfen cevaplayın: 1) kullanıcılar? 2) formatlar? 3) hacim? 4) ERP? 5) onay? ... 15) SLA?"
Güçlü ilk tur:
**S1 (hedef):** Bugün e-postayla ilgili asıl sorun ne: elle veri girişi yükü mü, kaybolan faturalar mı, geciken ödemeler mi, başka bir şey mi? — *neden:* "bitti"nin ne anlama geldiğini bu belirler.
Seçenekler: a) giriş yükü b) kayıp/mükerrer fatura c) ödeme gecikmesi d) diğer

Özetten bir bölüm: Başarı kriteri: yüklenen faturalarda elle girişin azalması `[hedef değer muhasebe sorumlusuyla TBD]`. Kesin istenmeyen: "tedarikçiler başka tedarikçilerin belgelerini görmemeli" `[teyitli]`.
