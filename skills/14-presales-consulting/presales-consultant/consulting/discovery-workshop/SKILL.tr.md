---
name: discovery-workshop
description: "Erken aşamadaki bir müşteri işi için keşif çalıştayı tasarlar ve belgeler; hedefler, katılımcı karışımı, ön hazırlık, süreleri belli bir gündem, konu bazlı soru bankası, grup çalışması ve not-yaz-oyla (note-and-vote) yakınsama mekaniği ile yapılandırılmış bir çıktı (hedefler, sorunlar, mevcut yapı, gereksinim temaları, kısıtlar, riskler, sonraki adımlar) içerir. Yeni bir müşteri işi veya ön satış fırsatı başlarken, belirsiz bir müşteri ihtiyacı kapsama dönüştürülecekken ya da çalıştay notları bir keşif özetine çevrilecekken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 14-presales-consulting
  role: presales-consultant
  area: consulting
  title: "Müşteri keşif çalıştayı"
  related: "workshop-plan, facilitation-guide, current-state-assessment, stakeholder-map, interview-question-set"
  prompt: "E-ticaret platformunu \"modernize etmek\" isteyen ve ayrıntı paylaşmamış bir perakende müşterisiyle bir günlük keşif çalıştayı planla."
---

# Müşteri Keşif Çalıştayı

## Amaç
Erken aşamadaki ve gevşek tanımlı bir müşteri ihtiyacını hedefler, sorunlar, mevcut yapı ve kısıtlar hakkında ortak bir anlayışa dönüştürmek. Böylece sonraki adım (değerlendirme, teklif veya tahmin) varsayımlara değil müşteriyle birlikte toplanan kanıtlara dayanır.

## Ne zaman kullanılır
- Yeni bir iş veya fırsat başladığında ve müşterinin ihtiyacı hâlâ genel olduğunda.
- Müşteri tarafında birden fazla paydaşın farklı görüşleri ortaya çıkarılıp hizalanması gerektiğinde.
- Ham çalıştay notlarının müşteri için bir keşif özetine dönüştürülmesi gerektiğinde.

## Ne zaman kullanılmaz
- Genel bir iç çalıştay planlanıyorsa `workshop-plan` kullanılır.
- Müşteri mevcut sistemlerinin ve olgunluğunun resmi bir değerlendirmesini istiyorsa `current-state-assessment` kullanılır.
- İhtiyaç zaten netse ve bir paket gereksinimlerle karşılaştırılacaksa `fit-gap-analysis` kullanılır.

## Girdiler
Zorunlu:
- Müşterinin belirttiği ihtiyaç veya işin tetikleyicisi ile çalıştay formatı (süre, yüz yüze/uzaktan).

İsteğe bağlı, kaliteyi artırır:
- Müşterinin sektörü, büyüklüğü, bilinen sistemleri, önceki dokümanlar.
- Beklenen katılımcılar ve rolleri.
- İşin neye varması beklendiği (teklif, yol haritası, değerlendirme).
- Çalıştay yapıldıysa ham notlar veya döküm.

İhtiyaç veya format yoksa sor. Yalnızca sentez yapılacaksa notları iste. Diğer boşluklar ön hazırlık sorusu olur.

## Süreç
1. Çıktı olarak ifade edilmiş 2-4 çalıştay hedefi belirle (ör. "ölçütleriyle üzerinde uzlaşılmış ilk 5 iş hedefi") ve çalıştayın neye karar vermeyeceğini yaz.
2. Katılımcı karışımını tanımla: yönetici sponsor (açılış ve kapanış), iş süreci sahipleri, BT/mimari, operasyon ve son kullanıcı temsilcileri. Aktif katılımcıyı 6-12 civarında tut; eksik rolleri risk olarak işaretle.
3. Ön hazırlığı tasarla: kısa bir anket ve doküman talebi (organizasyon şeması, sistem haritası, KPI'lar, önceki girişimler); böylece çalıştay süresi veri toplamaya değil tartışmaya gider.
4. Süreleri belli bir gündem kur: sponsorun "neden şimdi" açılışı; hedefler ve başarı ölçütleri; mevcut süreç ve sorunlar; sistem ve veri yapısı; kısıtlar (bütçe, mevzuat, takvim, yetkinlik); riskler ve fikirler; önceliklendirme; sonraki adımlarla kapanış. Yaklaşık her 90 dakikada bir mola ekle.
5. Her gündem bloğu için genelden özele (huni) sıralanmış bir soru bankası hazırla; "bugün … olduğunda ne oluyor", "ne sıklıkla…", "… olduğunda size maliyeti ne" gibi derinleştirme soruları ekle. Yönlendirici veya çözümle başlayan sorulardan kaçın.
6. Yakınsama mekaniğini planla: sessiz bireysel not yazma, temalara göre kümeleme, nokta oylaması veya etki/efor yerleşimi; aktif kişi sayısı 8'i aşarsa alan bazında gruplara bölünme ve her grubun sabit bir şablonla geri bildirimi.
7. Rolleri ata: kolaylaştırıcı, not tutucu, alan uzmanı, zaman tutucu; notların nasıl alınacağını ve örneklerdeki kişisel verinin nasıl en aza indirileceğini kararlaştır.
8. Çalıştaydan sonra sentezle: katılımcıların söylediklerini (role göre atfederek) kendi yorumundan (`[VARSAYIM]`) ayır; sorunları ve hedefleri kümele; paydaşlar arası çelişkileri ortalamak yerine açıkça not et.
9. Keşif özetini üret: ölçütleriyle hedefler, önceliklendirilmiş sorunlar, mevcut yapı taslağı, gereksinim temaları, kısıtlar, riskler, doğrulanacak hipotezler ve sorumlularıyla açık sorular.
10. Sonraki adımları yalnızca üzerinde uzlaşıldıysa sorumlu ve tarihle öner; aksi hâlde `[TBD]`.
11. Hedef devam ediyorsa daha derin teşhis için `current-state-assessment`, bir paket söz konusuysa `fit-gap-analysis` veya teklifi şekillendirmek için `proposal-writing` öner.

## Çıktı formatı
```markdown
# Keşif Çalıştayı: <müşteri> — <konu>
## Plan
- Hedefler (çıktılar): ...  - Kapsam dışı: ...
- Katılımcılar: | Rol | Ad / TBD | Neden gerekli |
- Ön hazırlık: anket maddeleri, istenen dokümanlar

## Gündem
| Saat | Blok | Hedef | Yöntem | Yürüten |

## Soru Bankası
### <Blok>
1. <genel soru> → derinleştirme: ...

## Keşif Özeti (çalıştay sonrası)
### Hedefler ve Başarı Ölçütleri
| Hedef | Ölçüt | Dile getiren (rol) | Öncelik (oy) |
### Sorunlar
| Sorun | Etki | Sıklık | Dile getiren | Kanıt / [VARSAYIM] |
### Mevcut Yapı
### Gereksinim Temaları
### Kısıtlar ve Riskler
### Paydaş Görüş Ayrılıkları
### Doğrulanacak Hipotezler
### Açık Sorular — sorumlu — gereken tarih
### Sonraki Adımlar
```

## Kalite kontrol listesi
- [ ] Hedefler somut çalıştay çıktıları olarak ifade edilmiş.
- [ ] Gündemin süreleri, molaları ve net bir yakınsama adımı var.
- [ ] Sorular açık uçlu, huni sıralı ve çözüme yönlendirmiyor.
- [ ] Söylenen ile çıkarılan ayrılmış; çıkarımlar `[VARSAYIM]` olarak etiketli.
- [ ] Paydaş çelişkileri ortalanıp kaybolmamış, kaydedilmiş.
- [ ] Her açık soru ve sonraki adımın sorumlusu var ya da `[TBD]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Keşif sırasında çözümü satmak. Müşteriyi çıpalar ve gerçek ihtiyaçları gizler; çözüm konuşmasını kapanışa sakla.
- Odada yalnızca üst düzey kişilerin olması. Süreci yaşandığı gibi değil tasarlandığı gibi anlatırlar; operasyon kullanıcılarını dahil et.
- Söylenen her şeyi sıralayan özetler. Müşterinin oylarıyla önceliklendir ve sorunları etkiye bağla.

## Örnek
Girdi: "Perakende müşterisi, 'e-ticareti modernize etmek', bir gün yüz yüze, katılımcılar belli değil."

Çıktıdan bir bölüm:
| Saat | Blok | Hedef | Yöntem |
|---|---|---|---|
| 09:00 | Neden şimdi (sponsor) | Ortak gerekçe ve başarı resmi | Sponsor konuşması + soru-cevap |
| 10:45 | Sorunlar | Etkisiyle birlikte öncelikli sorunlar | Sessiz not → kümeleme → nokta oylaması |

- Soru: "Müşterinin sipariş vermesinden siparişin depodan çıkmasına kadar bugün neler oluyor, adım adım anlatır mısınız?" Derinleştirme: "İnsanlar veriyi nerede elle yeniden giriyor veya kontrol ediyor?"
- Risk: Operasyon veya depo katılımcısı teyit edilmedi `[TBD]`.
