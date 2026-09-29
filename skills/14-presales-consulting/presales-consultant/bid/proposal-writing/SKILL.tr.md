---
description: Müşteri odaklı bir teklif dokümanı yazar; yönetici özeti, müşterinin durumu ve hedeflerine dair anlayış, önerilen çözüm, teslimat yaklaşımı, plan ve kilometre taşları, ekip, varsayımlar ve ticari özeti müşterinin kendi önceliklerine bağlanmış kazanma temaları ve kanıtlarla içerir. Bir müşteri talebine veya RFP'ye anlatı biçiminde teklifle yanıt verilirken, bir çözüm satın alma kararı için sunulacakken ya da taslak teklif genel bir yetkinlik broşürü gibi okunuyorsa kullanılır.
related: rfp-analysis, rfp-response, effort-estimate-for-bid, statement-of-work, executive-summary
prompt: Bir lojistik firmasının eski sevkiyat sistemini modernize etmek için teklif dokümanı yaz; keşif notları ve efor tahminimiz ekte.
---

# Teklif Dokümanı Yazma

## Amaç
Müşterinin karar vericilerini problemlerini anladığınıza, inandırıcı bir çözümünüz ve planınız olduğuna ve en düşük riskli iş ortağı olduğunuza ikna etmek; bunu değerlendirmesi kolay, efor tahmini ve SOW ile tutarlı bir dokümanla yapmak.

## Ne zaman kullanılır
- Müşteri keşif sonrası teklif istediğinde veya bir RFP anlatı biçiminde yanıt beklediğinde.
- Kurum içinde bir çözüm ve tahmin hazır olduğunda ve satın alma kararı için paketlenmesi gerektiğinde.
- Taslak teklif özellik odaklı veya genel kaldığında ve müşteriye özgü hâle getirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- RFP gereksinim bazında uyum yanıtları istiyorsa `rfp-response` kullanılır.
- Sözleşmeye girecek kapsam ve kabul koşulları gerekiyorsa `statement-of-work` kullanılır.
- Teklif verilip verilmeyeceğine hâlâ karar veriliyorsa `rfp-analysis` kullanılır.

## Girdiler
Zorunlu:
- Müşterinin talebi, RFP veya keşif notları (durumu, hedefleri, kısıtları).
- Önerilen çözümün ana hatları ya da onu `[VARSAYIM]` olarak taslaklama izni.

İsteğe bağlı, kaliteyi artırır:
- Efor tahmini, plan ve ticari model; fiyat (yalnızca ticari ekipten).
- Değerlendirme kriterleri ve karar vericiler; rekabetteki firmalar.
- Referans projeler, vaka çalışmaları, sertifikalar, ekip özgeçmişleri.
- Zorunlu yapı, sayfa sınırları ve gönderim formatı.

Müşteri bağlamı yoksa iste. Referans, müşteri adı, metrik, fiyat veya sertifika asla uydurma; `[TBD: referans]` yer tutucuları kullan.

## Süreç
1. Müşterinin hedeflerini, sorunlarını, başarı ölçütlerini, kısıtlarını ve değerlendirme kriterlerini kendi ifadeleriyle çıkar. Her karar vericinin ana kaygısını (iş, teknik, finansal, risk) not et.
2. 2-4 kazanma teması belirle: her biri bir müşteri önceliğini sizin farklılaştırıcınıza ve bir kanıta bağlar. Kanıtı olmayan tema `[KANIT GEREKLİ]` olarak işaretlenir.
3. Önce anlayış bölümünü müşterinin terimleriyle yaz: mevcut durum, neden şimdi değişim, istenen sonuç. Müşteri yazmış gibi okunmalı; henüz şirketinizden söz edilmez.
4. Çözümü sonuç üzerinden anlat: her müşteri hedefine nasıl ulaşıldığı, ana bileşenler, kullanıcılar için ne değiştiği ve değerlendirilen seçenekler ile seçim gerekçesi. Özellikleri faydalara eşle, tersini değil.
5. Teslimat yaklaşımını anlat: fazlar, müşterinin nasıl dahil olduğu, yönetişim, kalite ve risk yönetimi, değişim ve bilgi aktarımı. Müşteri zorunlu kılmadıkça metodoloji bağımsız kal.
6. Planı sun: teslimat ve karar noktalarıyla kilometre taşları, müşteriye kritik bağımlılıklar ve efor tahminiyle tutarlı süre.
7. Ekibi sun: roller, sorumluluklar ve ilgili deneyim; yalnızca verildiyse kişi adı kullan.
8. Varsayımları, müşteri sorumluluklarını ve kapsam dışı maddeleri tahminle tutarlı ve SOW'a taşınabilir biçimde yaz.
9. Ticari özeti yalnızca verildiği kadarıyla özetle (model, fiyat, ödeme kilometre taşları, geçerlilik); rakam verilmediyse `[TBD: ticari]` bırak.
10. Yönetici özetini en son yaz: tek sayfa; müşteri hedefi, önerilen sonuç, neden biz, yatırım ve sonraki adım. Başka hiçbir şey okumayan biri için tek başına yeterli olmalı.
11. Zorunlu yapıya ve sınırlara uyumu, bölümler arası rakam tutarlılığını ve her değerlendirme kriterinin görünür biçimde yanıtlandığını kontrol et. Desteklenmeyen iddiaları `[VARSAYIM]` olarak etiketle.
12. Hedef devam ediyorsa kapsamı resmileştirmek için `statement-of-work`, uyum matrisleri için `rfp-response` veya sözlü sunum için `presentation-outline` öner.

## Çıktı formatı
```markdown
# Teklif: <müşteri> — <girişim>
## 1. Yönetici Özeti
## 2. Anlayışımız
- Durum / Neden şimdi / İstenen sonuçlar / Başarı ölçütleri
## 3. Önerilen Çözüm
- Sonuç-çözüm eşlemesi | Değerlendirilen seçenekler
## 4. Teslimat Yaklaşımı
## 5. Plan ve Kilometre Taşları
| Kilometre taşı | Teslimatlar | Müşteri bağımlılığı | Hedef |
## 6. Ekip
| Rol | Sorumluluk | İlgili deneyim |
## 7. Neden Biz
| Kazanma teması | Müşteri önceliği | Kanıt |
## 8. Varsayımlar, Müşteri Sorumlulukları, Kapsam Dışı
## 9. Ticari Özet
## 10. Sonraki Adımlar
Ek: değerlendirme kriteri → bölüm eşlemesi
```

## Kalite kontrol listesi
- [ ] Anlayış bölümü müşterinin hedeflerini ve ifadelerini kullanıyor, bizden bahsetmiyor.
- [ ] Her kazanma temasının bir kanıtı var ya da `[KANIT GEREKLİ]` olarak işaretli.
- [ ] Her değerlendirme kriteri bir bölüme eşlenmiş.
- [ ] Plan, ekip, varsayımlar ve rakamlar tahminle tutarlı.
- [ ] Hiçbir referans, metrik, fiyat veya ad uydurulmamış.
- [ ] Yönetici özeti tek sayfada tek başına anlaşılır.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Şirket tarihçesiyle açmak. Değerlendiriciler önce kendi problemlerini arar; anlayış ve sonuçla başla.
- Faydasız özellikler. Her yetkinliği bir müşteri hedefine bağla, yoksa broşür gibi okunur.
- SOW ve tahminin karşılamadığı teklif vaatleri. Üçünde de tek bir varsayım listesi kullan.

## Örnek
Girdi: "Lojistik firması, sevkiyat sistemi 15 yıllık, sevkiyatçılar siparişleri yeniden giriyor, anlık takip istiyorlar; tahminimiz: 3 faz."

Zayıf açılış: "2005 yılında kurulan şirketimiz, dijital dönüşüm hizmetlerinde lider bir sağlayıcıdır..."

Güçlü açılış: "Sevkiyatçılarınız her siparişi, araçların nerede olduğunu gösteremeyen bir sisteme yeniden giriyor. Hedef, siparişten teslimata tek bir anlık görünüm; ilk depo erken fayda görsün diye üç fazda teslim ediliyor `[VARSAYIM: depo bazlı fazlama]`."
