---
name: capability-map
description: "Olgunluk, stratejik önem ve ısı haritası içeren hiyerarşik bir iş yetkinlik haritası (seviye 1-3) oluşturur; uygulamaları ve sahipleri yetkinliklere eşler. Yatırım planlarken, uygulama sadeleştirmesi yaparken, bir dönüşümün kapsamını belirlerken veya BT'yi iş stratejisiyle hizalarken ya da organizasyon şemasından ve sistemlerden bağımsız olarak işin ne yaptığı sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: enterprise-architect
  area: strategy
  title: "İş yetkinlik haritası"
  related: "application-portfolio-assessment, target-state-architecture, value-stream-map, bounded-context-map, portfolio-prioritization"
  prompt: "Bireysel bankamız için olgunluk ve stratejik önem içeren seviye 2 yetkinlik haritası oluştur ve gelecek yıl nereye yatırım yapmamız gerektiğini vurgula."
---

# İş Yetkinlik Haritası

## Amaç
İşin ne yaptığını kararlı bir yetkinlik hiyerarşisi olarak tanımlamak, ardından olgunluk, önem ve uygulama kapsamını bunun üzerine koymak. Böylece yatırım ve sadeleştirme kararları organizasyon yapısından bağımsız, ortak bir görünüme dayanır.

## Ne zaman kullanılır
- Yıllık planlama veya bir dönüşüm, yatırım önceliklerini gösteren bir ısı haritası gerektirdiğinde.
- Uygulama sadeleştirmesinde çakışma ve boşluklar için iş tarafında bir referans gerektiğinde.
- Birleşme-satın alma veya yeniden yapılanmada organizasyondan bağımsız tarafsız bir model gerektiğinde.
- Alan veya servis sınırları çizilirken iş tarafında bir referans gerektiğinde.

## Ne zaman kullanılmaz
- Uçtan uca akış ve israf inceleniyorsa `value-stream-map` kullanılır.
- Yalnızca uygulama envanteri değerlendiriliyorsa `application-portfolio-assessment` kullanılır.
- Yazılım düzeyinde alan sınırları gerekiyorsa `bounded-context-map` kullanılır.

## Girdiler
Zorunlu:
- İş kapsamı (kurum, iş birimi, ürün hattı) ve sektör.
- Strateji ifadesi veya temel iş hedefleri.

İsteğe bağlı:
- Mevcut yetkinlik modelleri veya sektör referans modelleri (ör. bankacılık için BIAN, telekom için eTOM, APQC PCF).
- Sahipleriyle birlikte uygulama envanteri.
- İş paydaşlarından gelen sorunlar.

Kapsam veya hedefler yoksa sor. Olgunluk ve önem puanları paydaşlardan gelmelidir; aksi hâlde `[VARSAYIM]` olarak taslak yaz.

## Süreç
1. Kapsamı ve adlandırma kurallarını sabitle: yetkinlikler isim veya isim öbeğidir ("Müşteri Edinimi", "Kredi Riski Değerlendirme"); süreç, departman veya sistem değildir.
2. Seviye 1'i (7-12 yetkinlik) stratejik, çekirdek ve destek grupları olarak taslakla. Uygun bir sektör referans modeli varsa ondan başla, sonra uyarla.
3. Seviye 2'ye (yalnızca kararın gerektirdiği yerde seviye 3'e) ayrıştır. MECE uygula: çakışma yok, boşluk yok; her alt yetkinlik tek bir üst yetkinliğe aittir.
4. Kararlılığı doğrula: yetkinlik bir yeniden yapılanmadan ve sistem değişiminden sağ çıkmalıdır. Ekip veya ürün adı içerenleri yeniden adlandır.
5. Puanlamadan önce ölçekleri tanımla: süreç, insan, bilgi ve teknoloji boyutlarında olgunluk 1-5 (düzensiz → optimize); stratejik önem (farklılaştırıcı / çekirdek / sıradan).
6. Her S2 yetkinliğini kanıt kaynağıyla puanla; puanlanmayanlar `[TBD]` kalır.
7. Uygulamaları ve iş sahiplerini S2 yetkinliklere eşle. Mükerrerleri (yetkinlik başına çok uygulama) ve boşlukları (hiç yok) işaretle.
8. Isı haritasını oluştur: yüksek önem + düşük olgunluk = yatırım; sıradan + yüksek maliyet/mükerrerlik = sadeleştir veya satın al.
9. 3-7 yatırım teması çıkar; her birini yetkinliklere ve iş hedeflerine bağla.
10. Açık soruları ve iş sahipleriyle yapılması gereken doğrulama oturumlarını listele.
11. İş sahibi tarafından doğrulanmamış her olgunluk veya ısı puanını `[VARSAYIM]` olarak işaretle; hedef devam ediyorsa `application-portfolio-assessment` veya `target-state-architecture` öner.

## Çıktı formatı
```markdown
# Yetkinlik Haritası – <kapsam>
Ölçekler: Olgunluk 1-5 · Önem: Farklılaştırıcı / Çekirdek / Sıradan

## Seviye 1 Genel Görünüm
| Grup | S1 Yetkinlikler |
|---|---|

## Seviye 2 Ayrıntı
| S1 | S2 Yetkinlik | Açıklama (1 satır) | Sahibi | Olgunluk | Önem | Uygulamalar | Isı |
|---|---|---|---|---|---|---|---|

## Isı Haritası Bulguları
- Yatırım: <yetkinlik> – <neden>
- Sadeleştir: <yetkinlik> – <mükerrer uygulamalar>
- Boşluk: <desteklenmeyen yetkinlik>

## Yatırım Temaları
| Tema | Yetkinlikler | İş hedefi | Sonraki adım |

## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Adlar iş odaklı isimlerdir; departman, süreç fiili veya ürün adı yok.
- [ ] Her seviye MECE; S1'de 7-12 madde var.
- [ ] Ölçekler kullanılmadan önce tanımlandı; her puanın kaynağı veya `[VARSAYIM]` etiketi var.
- [ ] Uygulamalar ve sahipler eşlendi; mükerrerler ve boşluklar işaretlendi.
- [ ] Yatırım temaları hem yetkinliklere hem hedeflere bağlı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Organizasyon şemasını kopyalamak. İlk yeniden yapılanmada bozulur; "kim"i değil "ne"yi modelle.
- Her yerde seviye 4'e inmek. Yalnızca kararın gerektirdiği yerde ayrıntıya gir.
- Puanlamayı yalnızca mimarın yapması. İş tarafında doğrulanmamış olgunluk inandırıcı değildir.

## Örnek
Girdi: "Bireysel banka; hedefler: dijital müşteri edinimi ve daha düşük hizmet maliyeti."

Çıktıdan bir bölüm:
| S1 | S2 | Olgunluk | Önem | Uygulamalar | Isı |
|---|---|---|---|---|---|
| Müşteri Yönetimi | Müşteri Edinimi | 2 `[VARSAYIM]` | Farklılaştırıcı | 3 (şube uygulaması, web formu, CRM) | Yatırım + sadeleştirme |
| Ödemeler | Ödeme Gerçekleştirme | 4 `[VARSAYIM]` | Çekirdek | 1 | Sürdür |
