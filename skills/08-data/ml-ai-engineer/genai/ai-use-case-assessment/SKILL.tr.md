---
name: ai-use-case-assessment
description: "Önerilen bir yapay zeka veya makine öğrenmesi kullanım senaryosunu iş değeri, teknik fizibilite, veri hazırlığı, risk (gizlilik, adillik, güvenlik, mevzuat) ve işletme maliyeti açısından değerlendirir; en küçük sonraki deneyle birlikte puanlı bir devam / pilot / dur önerisi verir. Birisi \"X için yapay zeka kullanalım\" dediğinde, bir YZ fikirleri portföyü önceliklendirilirken veya bir YZ pilotu finanse edilmeden önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: ml-ai-engineer
  area: genai
  title: "YZ kullanım senaryosu değerlendirmesi"
  related: "ml-problem-framing, rag-design, privacy-impact-assessment, cost-benefit-analysis, decision-matrix"
  prompt: "Bu fikri değerlendir: çağrı merkezi temsilcilerimiz için gelen tüm müşteri şikâyetlerine ilk yanıt taslağını bir LLM hazırlasın."
---

# YZ Kullanım Senaryosu Değerlendirmesi

## Amaç
Ekipler bütçe ve veri ayırmadan önce, bir YZ fikrinin yatırıma değip değmediğine, hangi biçimi alması gerektiğine (kurallar, klasik ML, üretken YZ veya YZ'siz çözüm) ve hangi risklerin kontrol altına alınması gerektiğine erken ve kanıta dayalı karar vermek.

## Ne zaman kullanılır
- Bir iş birimi bir YZ özelliği veya otomasyonu önerdiğinde.
- Birden çok YZ fikri aynı ekip veya bütçe için yarıştığında ve karşılaştırılabilir puanlar gerektiğinde.
- Bir pilot başlamak üzereyken ve açık başarı ve durdurma kriterlerine ihtiyaç duyulduğunda.

## Ne zaman kullanılmaz
- Senaryo onaylandıysa ve hedef, öznitelikler ve taban çizgisinin teknik olarak tanımlanması gerekiyorsa `ml-problem-framing` kullanılır.
- Tam bir finansal iş gerekçesi gerekiyorsa bu değerlendirmeden sonra `cost-benefit-analysis` kullanılır.
- Ana soru kişisel verinin işlenmesiyse `privacy-impact-assessment` kullanılır.

## Girdiler
Zorunlu:
- Öneren kişinin kendi ifadesiyle kullanım senaryosu: görev, kullanıcılar ve YZ'nin üreteceği karar veya çıktı.

İsteğe bağlı, kaliteyi artırır:
- Mevcut süreç, hacimler, hata oranları, maliyetler ve sıkıntılı noktalar.
- Mevcut veri (kaynaklar, etiketler, kalite, sahiplik), mevzuat bağlamı, risk iştahı.
- Bütçe, zaman planı ve ekip yetkinlikleri.

Görev veya etkilenen kullanıcılar belirsizse her seferinde tek soru sor. Geri kalan her şey açık soru olur; hacim veya tasarruf asla uydurulmaz.

## Süreç
1. Senaryoyu yeniden ifade et: söylenen istek ile altta yatan ihtiyaç, otomatikleştirilen veya desteklenen karar ve çıktıya göre kimin aksiyon aldığı.
2. YZ'nin gerekli olup olmadığını kontrol et: kurallar, arama, bir form değişikliği veya bir rapor işin çoğunu çözebilir mi? En basit alternatifi taban çizgisi olarak kaydet.
3. YZ örüntüsünü sınıflandır: sınıflandırma/skorlama, tahminleme, bilgi çıkarma, üretim/taslak yazma, erişimli soru-cevap, ajan/otomasyon; ve özerklik düzeyini belirle (öneri, insan onaylı, tam otomatik).
4. Değeri değerlendir: bugünkü sıkıntı (zaman, maliyet, hata, gelir, deneyim), kimin fayda sağladığı, nasıl ölçüleceği; yalnızca girdi destekliyorsa aralık olarak ifade et, değilse `[BİLİNMİYOR]` yaz.
5. Fizibiliteyi değerlendir: görevin mevcut teknikler için zorluğu, hata toleransı, gecikme ihtiyacı, entegrasyon noktaları, ekip yetkinlikleri.
6. Veri hazırlığını değerlendir: erişilebilirlik, hacim, etiketler veya gerçek değerler, kalite, temsil gücü, erişim hakları ve kullanımın hukuki dayanağı.
7. Riski değerlendir: yanlış bir çıktının insanlar üzerindeki etkisi, gizlilik (KVKK/GDPR), adillik, güvenlik ve zararlı içerik, siber güvenlik (prompt injection, veri sızıntısı), mevzuat sınıflandırması (ör. AB Yapay Zeka Yasası risk kategorisi), itibar riski.
8. İşletme konularını nitel olarak tahmin et: çıkarım (inference) maliyetinin sürücüleri, izleme ve insan inceleme eforu, tedarikçi bağımlılığı.
9. Değer, fizibilite, veri hazırlığı ve riski her biri için tek satırlık kanıtla 1-5 arası puanla; çıkarıma dayanan puanları `[VARSAYIM]` olarak işaretle.
10. Devam, pilot veya dur öner; pilot için kapsamı, başarı metriğini, durdurma kriterini, insan gözetimini ve en büyük belirsizliği azaltacak en küçük deneyi tanımla.
11. Açık soruları sorumlularıyla listele; devam/pilot için `ml-problem-framing` veya `rag-design`, kişisel veri söz konusuysa `privacy-impact-assessment` öner.

## Çıktı formatı
```markdown
# YZ Kullanım Senaryosu Değerlendirmesi: <ad>
Öneren: <ad/birim veya [BİLİNMİYOR]> · Örüntü: <tür> · Özerklik: <öneri / onay / otomatik>

## Kullanım Senaryosu
- Söylenen istek: ...
- Altta yatan ihtiyaç: ...
- YZ'siz taban çizgisi: ...

## Puan Kartı
| Boyut | Puan (1-5) | Kanıt | Güven |
|---|---|---|---|
| İş değeri | | | |
| Teknik fizibilite | | | |
| Veri hazırlığı | | | |
| Risk (5 = düşük) | | | |

## Temel Riskler ve Kontroller
| Risk | Etki | Kontrol | Sorumlu |
|---|---|---|---|

## Öneri
<Devam / Pilot / Dur> – <gerekçe>
Pilot: kapsam ..., başarı metriği ..., durdurma kriteri ..., insan gözetimi ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
1. <soru> — <sorumlu>
```

## Kalite kontrol listesi
- [ ] YZ'siz bir taban çizgisi ele alındı ve karşılaştırıldı.
- [ ] Özerklik düzeyi ve yanlış çıktının etkisi açıkça belirtildi.
- [ ] Veri hazırlığı etiketleri, kaliteyi, erişim haklarını ve hukuki dayanağı kapsıyor.
- [ ] Her puanın kanıtı var; çıkarıma dayalı puanlar işaretli.
- [ ] Uydurulmuş hacim, maliyet veya tasarruf yok.
- [ ] Pilot önerisinin başarı ve durdurma kriterleri var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çözümden başlamak ("bir LLM'e ihtiyacımız var"). Teknolojiden değil, karardan ve hata toleransından başla.
- İnsan incelemesinin maliyetini göz ardı etmek. Her çıktının kontrol edilmesi gerekiyorsa tasarruf kaybolabilir; inceleme eforunu tahmin et.
- Bir demoyu fizibilite kanıtı saymak. Birkaç iyi örnek, gerçek ve dağınık girdilerdeki hata oranı hakkında bir şey söylemez.

## Örnek
Girdi: "Çağrı merkezi temsilcileri için tüm müşteri şikâyetlerine ilk yanıt taslağını LLM hazırlasın."

Çıktıdan bir bölüm:
- Özerklik: öneri; temsilci düzenler ve gönderir. Yanlış çıktının etkisi: orta (ton, yanlış vaatler), insan incelemesiyle azaltılır.
- Veri hazırlığı 3: İki yıllık şikâyet ve yanıt verisi var; geçmiş yanıtların kalitesi bilinmiyor `[VARSAYIM]`; kişisel veri içeriyor, geliştirme için maskelenmeli.
- Öneri: Tek bir şikâyet kategorisiyle 4 haftalık pilot; başarı = memnuniyet puanı düşmeden medyan işlem süresinin azalması; müşteriye ulaşan tek bir yetkisiz tazminat vaadi olursa durdur.
