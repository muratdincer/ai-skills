---
name: rfp-analysis
description: "Bir müşteri RFP/RFQ/ihale dokümanını teklif veren tarafından analiz eder; zorunlu ve puanlanan gereksinimleri, değerlendirme kriterlerini, ticari ve hukuki koşulları, tarihleri, örtük beklentileri ve riskleri çıkarır, bir uyum matrisi ve gerekçeli bir teklif ver/verme önerisi üretir. Yeni bir RFP veya ihale geldiğinde, ön satış eforu harcamadan önce ya da ekip teklif verip vermeyeceğine ve nasıl vereceğine karar vermek zorunda olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 14-presales-consulting
  role: presales-consultant
  area: bid
  title: "RFP analizi"
  related: "rfp-response, effort-estimate-for-bid, proposal-writing, requirements-gap-analysis, risk-register"
  prompt: "Core banking entegrasyon projesi için gelen bu 80 sayfalık RFP'yi analiz et ve teklif verip vermememiz gerektiğini söyle."
---

# RFP Analizi

## Amaç
Müşterinin tam olarak ne istediğini, yanıtları nasıl değerlendireceğini ve teklif vereni neyin zora sokabileceğini anlamak. Böylece ekip bilinçli bir teklif ver/verme kararı alır ve uyumlu, rekabetçi bir yanıt planlar.

## Ne zaman kullanılır
- Yeni bir RFP, RFQ, RFI veya ihale dokümanı geldiğinde.
- Ekip bir teklife ön satış eforu yatırıp yatırmayacağına karar vermek zorundaysa.
- Yanıtı yazmadan önce uyum matrisini ve soru listesini oluşturmak için.

## Ne zaman kullanılmaz
- Asıl yanıtları yazmak için `rfp-response` kullanılır.
- Alıcı olarak tedarikçi yanıtlarını değerlendirmek için `vendor-evaluation` kullanılır.
- Çözümün eforunu tahmin etmek için `effort-estimate-for-bid` kullanılır.

## Girdiler
Zorunlu:
- RFP dokümanı veya ilgili bölümleri (gereksinimler, değerlendirme kriterleri, koşullar, zaman çizelgesi).

İsteğe bağlı, kaliteyi artırır:
- Müşteriyle ilişki geçmişi, bilinen rakipler, mevcut tedarikçi.
- Kendi yetenekler, referanslar, iş ortağı seçenekleri ve teslimat dönemi için kapasite.
- Şirketin teklif politikası (asgari marj, risk iştahı, kabul edilmeyen sözleşme koşulları).

RFP metni yoksa iste. Dokümanın belirtmediği gereksinim, ağırlık veya tarih uydurma; boşlukları `[BİLİNMİYOR]` olarak işaretle ve netleştirme sorularına dönüştür.

## Süreç
1. İdari çerçeveyi çıkar: ihaleyi açan, teslim tarihi ve formatı, soru son tarihi, geçerlilik süresi, zorunlu formlar, teminat veya garantiler, dil ve sayfa sınırları.
2. Her gereksinimi referans numarasıyla çıkar ve sınıflandır: zorunlu (geçer/geçmez), puanlanan, bilgi amaçlı; format taleplerini not et (ör. "evet/hayır ve açıklama ile yanıtlayın").
3. Değerlendirme modelini yakala: kriterler, ağırlıklar, teknik/ticari oranı, asgari teknik eşik, fiyat formülü; açıklanmamışsa `[BİLİNMİYOR]` olarak işaretle.
4. Satır aralarını oku: tekrar eden temalar, alışılmadık derecede spesifik gereksinimler (mevcut tedarikçiyi kayırıyor olabilir), arka plan bölümündeki sıkıntılar; bu yorumları `[VARSAYIM]` olarak etiketle.
5. Ticari ve hukuki koşulları incele: ödeme kilometre taşları, cezalar ve götürü tazminat, sorumluluk üst sınırları, fikri mülkiyet, kabul, garanti, veri koruma (KVKK/GDPR), alt yüklenici sınırları; kabul edilemez veya yüksek riskli maddeleri işaretle.
6. Uyum matrisini kur: gereksinim → uyumlu / kısmi / uyumsuz / netleştirme gerekli, planlanan kanıt veya yaklaşımla birlikte.
7. Müşteri için netleştirme sorularını çözüm, fiyat veya uygunluk üzerindeki etkisine göre sıralayarak ve soru son tarihine uyarak listele.
8. Kazanma faktörlerini değerlendir: gereksinimlere uyum, ilişki ve müşteri bilgisi, referanslar, fiyat rekabetçiliği, mevcut tedarikçi avantajı, ekip müsaitliği.
9. Riskleri değerlendir: kapsam belirsizliği, belirsiz kapsamda sabit fiyat, agresif zaman çizelgesi, cezalar, müşteriye veya üçüncü taraflara bağımlılık, teslimat kapasitesi.
10. Kazanma olasılığı ve riske göre düzeltilmiş cazibe üzerinden şeffaf şekilde puanlanmış bir teklif ver / verme / koşullu teklif ver önerisi yap ve karar sahibini belirt.
11. Kullanıcının hedefi devam ediyorsa boyutlandırma için `effort-estimate-for-bid`, yanıtları yazmak için `rfp-response` veya serbest formatlı bir teklif isteniyorsa `proposal-writing` öner.

## Çıktı formatı
```markdown
# RFP Analizi: <müşteri> – <RFP adı/referansı>

## Temel Bilgiler
| Kalem | Değer |
|---|---|
| Teslim tarihi / formatı | ... |
| Soru son tarihi | ... |
| Değerlendirme modeli | <ağırlıklar, eşik, fiyat formülü veya [BİLİNMİYOR]> |
| Sözleşme türü / süresi | ... |

## Gereksinim Özeti
| Ref | Gereksinim (kısa) | Tür | Uyum | Kanıt / yaklaşım | Not |
|---|---|---|---|---|---|

## Ticari ve Hukuki Uyarılar
| Madde | Risk | Önerilen tutum |
|---|---|---|

## Örtük Beklentiler (yorum)
- [VARSAYIM] ...

## Netleştirme Soruları
1. <soru> – RFP ref – neden önemli

## Kazanma Faktörleri ve Riskler
| Faktör | Değerlendirme | Kanıt |
|---|---|---|

## Öneri
Teklif ver / Verme / Koşullu teklif ver – gerekçeler – koşullar – karar sahibi
```

## Kalite kontrol listesi
- [ ] Her zorunlu gereksinim referansı ve uyum durumuyla listelendi.
- [ ] Değerlendirme modeli ve tarihler dokümandan alındı veya `[BİLİNMİYOR]` olarak işaretlendi.
- [ ] Yüksek riskli ticari ve hukuki maddeler önerilen tutumla işaretlendi.
- [ ] Örtük beklentilere dair yorumlar `[VARSAYIM]` olarak etiketli.
- [ ] Netleştirme soruları RFP bölümlerine atıf yapıyor ve etkiye göre sıralı.
- [ ] Teklif ver/verme önerisi gerekçeleri, koşulları ve karar sahibini belirtiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her ihaleye teklif vermek. Düşük olasılıklı bir teklif, kazanılabilir biriyle aynı ön satış eforunu tüketir; kanıtla karar ver.
- Tek bir geçer/geçmez gereksinimi (bir form, bir sertifika, bir teminat) kaçırmak. Kalitesi ne olursa olsun tüm yanıtı diskalifiye eder.
- Belirsiz kapsamda sınırsız sorumluluk veya cezayı kabul etmek. Bunu netleştirme sorusu veya belirtilmiş bir sapma olarak gündeme getir.

## Örnek
Girdi: 80 sayfalık RFP, core banking entegrasyonu, sabit fiyat, 6 aylık süre.

Çıktıdan bir bölüm:
- Zorunlu: R-14 "Tedarikçi son 3 yılda <belirtilen core banking ürünü> ile 2 entegrasyon teslim etmiş olmalıdır" – referanslarımız: `[BİLİNMİYOR – teyit et]`; yoksa bu bir eleme kriteridir.
- Hukuki uyarı: üst sınırı olmayan günlük %1 gecikme cezası – %10 üst sınır ve müşteri kaynaklı gecikme istisnası öner.
- Öneri: Koşullu teklif ver – yalnızca R-14 referansları teyit edilir ve test ortamı müsaitliği sorusu yanıtlanırsa.
