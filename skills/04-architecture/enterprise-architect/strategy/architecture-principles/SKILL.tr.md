---
description: Kurumsal veya alan düzeyinde az sayıda mimari ilke tanımlar; her ilke için TOGAF tarzında ifade, gerekçe ve etkileri, uyumun nasıl denetleneceğini ve istisnaların nasıl yönetileceğini belirler. Kurumun mimari kararlar için yol gösterici kurallara ihtiyacı olduğunda, ilkeler içi boş sloganlara dönüştüğünde veya tasarım incelemelerinde aynı ödünleşimler tekrar tekrar tartışıldığında kullanılır.
related: architecture-review, adr, target-state-architecture, technology-strategy, governance-framework
prompt: Bulut-yerel ve olay güdümlü sistemlere geçişimiz için 8-10 mimari ilke tanımla; hedeflerimiz daha hızlı teslimat, daha düşük işletim maliyeti ve KVKK uyumu.
---

# Mimari İlkeler Tanımlama

## Amaç
İş hedeflerini karar kurallarına dönüştüren kısa ve uygulanabilir bir mimari ilke seti üretmek. İyi ilkeler tekrar eden ödünleşimleri bir kez çözer; incelemeler ve ADR'ler yeniden tartışmak yerine ilkeye atıf yapar.

## Ne zaman kullanılır
- Yeni bir mimari pratiği, platform veya dönüşüm programı yol gösterici kurallara ihtiyaç duyduğunda.
- Mevcut ilkeler gerekçesi ve etkisi olmayan sloganlardan ibaret olduğunda ("en iyi pratikleri kullan").
- Tasarım incelemelerinde aynı ödünleşim sürekli tartışıldığında (yeniden kullanım mı hız mı, yap mı al mı, merkezi mi federe veri mi).
- Birleşme veya yeniden yapılanma sonrası iki ilke setinin uyumlaştırılması gerektiğinde.

## Ne zaman kullanılmaz
- Tek bir karar verilip kaydedilecekse `adr` kullanılır.
- Somut bir teknoloji seçimi gerekiyorsa `technology-selection` veya `tech-radar` kullanılır.
- Kodlama düzeyinde kurallar gerekiyorsa `coding-standards` kullanılır.

## Girdiler
Zorunlu:
- İş hedefleri ve strateji (amaçlar, kısıtlar, mevzuat bağlamı).
- İlkelerin kapsamı: kurum geneli, bir alan (veri, entegrasyon, güvenlik) veya bir program.

İsteğe bağlı:
- Mevcut ilkeler, standartlar ve politikalar.
- Tekrar eden çatışmaları gösteren son ADR'ler veya inceleme bulguları.
- Organizasyon bağlamı: ekip özerkliği modeli, tedarik stratejisi, risk iştahı.

Hedefler veya kapsam yoksa sor. Diğer her şey açık soru olur.

## Süreç
1. Her iş hedefini ölçülebilir bir kaygı olarak yeniden yaz (ör. "değişiklik teslim süresi", "işlem başına işletim maliyeti", "mevzuat riski").
2. Aday ilkeleri hedeflerden, mevcut politikalardan ve tekrar eden inceleme çatışmalarından topla. Toplamda 8-12 ilke hedefle; fazlası uygulanamaz.
3. Her adayı TOGAF kalite ölçütleriyle sına: anlaşılır, sağlam (zor durumlarda kullanılabilir), bütünlüklü, diğerleriyle tutarlı, yıllarca geçerli.
4. İlke olmayanları ele: kimsenin karşı çıkmayacağı genellemeler ("sistemler güvenli olmalı"), teknoloji seçimleri ("Kafka kullan") ve tek seferlik kararlar. İyi bir ilkenin, makul bir kurumun seçebileceği inandırıcı bir karşıtı vardır.
5. Her ilkeyi yaz: kısa emir kipinde ad, tek cümlelik ifade, bir hedefe bağlı gerekçe, etkiler (ekipler, maliyet, yetkinlik, süreç için ne değişir).
6. İlkeleri bir matriste hedeflerle eşle; her ilke en az bir hedefe bağlanmalı, her hedef karşılanmalı.
7. İlkeler arası gerilimleri belirle (ör. "satın almadan önce yeniden kullan" ile "ekip özerkliği") ve öncelik kuralını ya da karar mercisini yaz.
8. Uyumu tanımla: inceleyen ilkeyi nasıl denetler (inceleme sorusu, fitness function, metrik) ve sahibi kim.
9. İstisna sürecini tanımla: kim onaylar, ne kaydedilir (ADR), bitiş veya gözden geçirme tarihi.
10. Strateji ve organizasyonla ilgili her varsayımı `[VARSAYIM]` olarak işaretle, mimari kurul için açık soruları listele.

## Çıktı formatı
```markdown
# Mimari İlkeler – <kapsam>
Sürüm: <x.y> · Sahibi: <rol veya [BİLİNMİYOR]> · Gözden geçirme: <ör. yıllık>

## Hedefler
| No | Hedef | Ölçü |
|---|---|---|

## İlkeler
### İ<n>. <Emir kipinde ad>
- İfade: <tek cümle>
- Gerekçe: <neden; hedef numaraları>
- Etkiler: <ekipler, maliyet, yetkinlik, süreç>
- Uyum denetimi: <inceleme sorusu / fitness function / metrik>
- Öncelik / gerilimler: <şu durumda İ-x geçerli>

## Hedef–İlke Matrisi
| İlke | H1 | H2 | ... |

## İstisna Süreci
<onaylayan, kayıt (ADR), bitiş tarihi>

## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] 8-12 ilke var; her birinde ifade, gerekçe, etkiler ve uyum denetimi bulunuyor.
- [ ] Her ilkenin inandırıcı bir karşıtı var (genelleme değil) ve hiçbir ürün adı geçmiyor.
- [ ] Her ilke bir hedefe bağlı; her hedef karşılanıyor.
- [ ] Bilinen gerilimler için açık bir öncelik kuralı veya karar mercisi var.
- [ ] İstisna süreci tanımlı ve süreli.
- [ ] Organizasyonla ilgili hiçbir şey uydurulmadı; boşluklar işaretli.

## Sık yapılan hatalar
- 30 ilke yazmak. Kimse uygulamaz; birleştir ya da standart düzeyine indir.
- Etkileri yazmamak. Maliyet ve davranış sonucu olmayan ilkeler onaylanır ama uygulanmaz.
- İlkeleri kalıcı saymak. Hedeflere bağla ki strateji değişince yeniden ele alınsın.

## Örnek
Girdi: "Hedefler: daha hızlı teslimat, daha düşük işletim maliyeti, KVKK uyumu. Kapsam: kurum geneli."

Çıktıdan bir bölüm:
- İ3. Veri, Onu Üreten Alana Aittir
  - İfade: Her iş veri setinin tek bir sahip alanı vardır ve bu alan veriyi bir sözleşmeyle yayınlar; diğerleri ona yazmaz.
  - Gerekçe: Teslimatı yavaşlatan bağımlılığı azaltır (H1); KVKK sorumluluğunu netleştirir (H3).
  - Etkiler: Paylaşılan veritabanları aşamalı olarak kaldırılır; alanlar veri sözleşmesi ve yayınlama için bütçe ayırır.
  - Uyum denetimi: Her tasarım incelemesinde "Herhangi bir servis başka bir alanın veri deposuna yazıyor mu?" sorusu.
