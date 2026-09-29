---
name: bpmn-model
description: "Bir süreç tarifini BPMN 2.0 modeline dönüştürür: havuzlar ve kulvarlar, olaylar, görevler, geçitler, mesaj akışları ve veri nesneleri; çıktıyı yapılandırılmış bir öğe listesi ile çizilebilir veya içe aktarılabilir diyagram kodu olarak verir. Bir sürecin biçimsel olarak çizilmesi gerektiğinde, metin olarak yazılmış bir as-is veya to-be süreç diyagrama çevrilecekse ya da BPMN, kulvar diyagramı veya süreç diyagramı kodu istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: process
  title: "BPMN süreç modeli"
  related: "as-is-process, to-be-process, diagram-as-code, business-rules-catalog, use-case-spec"
  prompt: "Bu satın alma onay sürecini BPMN ile modelle: çalışan talep girer, yönetici 10 bine kadar onaylar, üstünde finans da onaylar, sonra satın alma sipariş verir."
---

# BPMN Süreç Modeli

## Amaç
Anlamsal olarak doğru (doğru olay, görev ve geçit türleri) ve hem iş birimleri hem de BT tarafından okunabilen bir BPMN 2.0 modeli üretmek. Böylece süreç doğrulanabilir, otomasyona alınabilir ya da gereksinimlere temel olabilir.

## Ne zaman kullanılır
- Metin olarak yazılmış bir as-is veya to-be sürecin biçimsel bir diyagrama ihtiyacı olduğunda.
- Bir iş akışı motoru veya süreç otomasyonu girişimi temiz bir başlangıç modeline ihtiyaç duyduğunda.
- Departmanlar veya sistemler arası devir teslimlerin görünür kılınması gerektiğinde (havuz, kulvar, mesaj akışı).

## Ne zaman kullanılmaz
- Süreç henüz kayıt altına alınmamışsa önce `as-is-process` veya `to-be-process` kullanılır.
- İş süreci değil sistemden sisteme çağrı sırası gerekiyorsa `sequence-flow` kullanılır.
- Tek bir nesnenin yaşam döngüsü (sipariş durumları) gerekiyorsa `state-model` kullanılır.

## Girdiler
Zorunlu:
- Süreç tarifi: adımlar, aktörler, kararlar (metin, notlar veya mevcut as-is/to-be dokümanı).

İsteğe bağlı, kaliteyi artırır:
- Hedef seviye: tanımlayıcı (üst düzey), analitik (istisnalarla) veya çalıştırılabilir.
- Tercih edilen çıktı gösterimi: BPMN XML, Mermaid flowchart, PlantUML veya araçtan bağımsız öğe listesi.
- Kararların arkasındaki iş kuralları, SLA'lar ve zamanlayıcılar.

Tarif yoksa iste. Seviye verilmediyse varsayılan olarak analitik seviyeyi seç ve bunu belirt.

## Süreç
1. Kapsamı belirle: süreç adı, tetikleyici (başlangıç olayı), bitiş durumları (her ayrı iş sonucu için bir bitiş olayı), ayrıntı seviyesi.
2. Katılımcıları belirle: her kurum veya dış taraf için bir havuz, kendi kurumundaki her rol veya iç sistem için bir kulvar. Adımları önemli değilse dış taraflar kara kutu havuz olarak kalır.
3. Aktiviteleri fiil-nesne biçiminde listele ("Talebi onayla"). Her birinin türünü belirle: kullanıcı, servis, manuel, gönderme, alma, iş kuralı veya script görevi; yeniden kullanılan alt süreçler için call activity kullan.
4. Kararları doğru geçitle modelle: tek yol için dışlayıcı (XOR), eşzamanlı yollar için paralel (AND), bir veya daha fazlası için kapsayıcı (OR), "hangisi önce olursa" için olay tabanlı geçit. Çıkan akışları koşullarla etiketle; varsayılan akış ekle.
5. Her ayrılmayı aynı türde bir birleşmeyle kapat; ayrı bitiş olaylarına giden XOR yolları hariç.
6. Olayları ekle: zamanlayıcılar (son tarih, hatırlatma), havuzlar arası mesajlar, hata verebilecek aktiviteye sınır olayı olarak hata ve eskalasyon, tamamlanmış bir adımın geri alınması gerekiyorsa telafi (compensation).
7. Sıralı akışı (sequence flow) yalnızca havuz içinde, mesaj akışını yalnızca havuzlar arasında kullan. Akışı yönlendiren doküman veya sistem kaydı varsa veri nesnesi ya da veri deposu ekle.
8. Doğrula: çıkmaz yol yok, gelen/giden akışı olmayan aktivite yok, örtük birleşme yok, her döngünün çıkış koşulu var, her kulvarda iş var.
9. Diyagram kodunu istenen gösterimde ve modelin çizilmeden incelenebilmesi için bir öğe tablosuyla üret.
10. Varsayımları (geçit koşulları, zamanlayıcılar, çıkarım yaptığın roller) ve süreç sahibine yönelik açık soruları listele.
11. Kullanıcı devam etmek isterse geçit kuralları için `business-rules-catalog`, sistem destekli görevler için `use-case-spec` veya model iyileştirme ihtiyacı gösteriyorsa `to-be-process` öner.

## Çıktı formatı
```markdown
# BPMN Modeli: <süreç adı>
Seviye: <tanımlayıcı / analitik / çalıştırılabilir> · Tetikleyici: <başlangıç olayı> · Sonuçlar: <bitiş olayları>

## Katılımcılar
| Havuz | Kulvarlar | Notlar |
|---|---|---|

## Öğeler
| ID | Tür | Ad | Kulvar | Gelen | Giden / koşul |
|---|---|---|---|---|---|
| SE1 | Başlangıç olayı (mesaj) | Talep alındı | Çalışan | – | T1 |
| G1 | Dışlayıcı geçit | Tutar > limit? | Yönetici | T2 | evet: T3 / varsayılan: T4 |

## Diyagram Kodu
<BPMN XML / Mermaid / PlantUML>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
- S: ... — muhatap: ...
```

## Kalite kontrol listesi
- [ ] Her geçidin etiketli koşulları ve gereken yerde varsayılan akışı var; ayrılma ve birleşmeler eşleşiyor.
- [ ] Mesaj akışları yalnızca havuzlar arasında; sıralı akışlar havuz sınırını geçmiyor.
- [ ] Her bitiş olayı ayrı ve adlandırılmış bir iş sonucunu temsil ediyor.
- [ ] Girdideki istisnalar ve zamanlayıcılar görev adlarına gömülmeden sınır veya ara olay olarak modellendi.
- [ ] Çıkarımla eklenen koşullar, roller ve zamanlayıcılar `[VARSAYIM]` olarak işaretli.
- [ ] Diyagram kodu öğe tablosuyla birebir örtüşüyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kararı geçide verdirmek. Geçit yönlendirir; karar geçitten önceki bir görevdir (çoğunlukla iş kuralı görevi).
- Her iç departmanı ayrı havuz yapıp mesaj akışıyla bağlamak. İç roller tek havuzdaki kulvarlardır.
- "Onaylanırsa" ifadesini geçit yerine görev adına yazmak; bu, dallanmayı inceleyenlerden gizler.
- Sistemleri ve kişileri ayrım yapmadan aynı kulvara çizmek; otomasyon kapsamı belirsizleşir.

## Örnek
Girdi: "Çalışan satın alma talebi girer; yönetici 10 bine kadar onaylar; 10 bin üstünde finans da onaylar; satın alma sipariş verir; ret durumunda çalışan bilgilendirilir."

Çıktıdan bir bölüm:
| ID | Tür | Ad | Kulvar | Giden / koşul |
|---|---|---|---|---|
| T2 | Kullanıcı görevi | Talebi onayla | Yönetici | G1 |
| G1 | Dışlayıcı geçit | Karar? | Yönetici | ret: T5 / onay: G2 |
| G2 | Dışlayıcı geçit | Tutar > 10 bin? | Yönetici | evet: T3 / varsayılan: T4 |
| T3 | Kullanıcı görevi | Finans olarak onayla | Finans | G3 (ret: T5 / varsayılan: T4) |
| B1 | T2 üzerinde zamanlayıcı sınır olayı | 3 iş günü `[VARSAYIM]` | Yönetici | Vekile eskale et |
