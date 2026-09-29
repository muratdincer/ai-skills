---
description: Teşhisi, nerede oynanacağını, nasıl kazanılacağını, az sayıdaki stratejik bahsi ve açık hedef dışı konuları vizyon ve sonuç metriklerine bağlayarak tek sayfalık bir ürün stratejisi yazar. Bir ürünün önümüzdeki 12-24 ay için stratejiye ihtiyacı olduğunda, yol haritasının gerekçesi olmadığında ya da yönetim "ürün stratejimiz ne" diye sorduğunda kullanılır.
related: product-vision, market-analysis, competitor-analysis, okr-definition, roadmap
prompt: B2B saha servis uygulamamız için önümüzdeki 18 aya yönelik tek sayfalık ürün stratejisi taslağı hazırla.
---

# Tek Sayfalık Ürün Stratejisi

## Amaç
Ürünün stratejik seçimlerini tek sayfaya sığdırmak: hangi zorlukla karşı karşıya olduğu, nerede rekabet edeceği, orada neden kazanacağı, hangi bahislere gireceği ve bilerek neleri yapmayacağı. Bu, ekiplere yol haritası ve önceliklendirme kararları için bir süzgeç sağlar.

## Ne zaman kullanılır
- Yıllık veya altı aylık planlamada ya da yol haritası oluşturmadan önce.
- Bir yol haritası var ama neden başka maddeler değil de bunların seçildiğini kimse açıklayamıyorsa.
- Yeni bir yönetici, pazar değişimi veya rakip hamlesi stratejinin yeniden ifade edilmesini gerektirdiğinde.

## Ne zaman kullanılmaz
- Uzun vadeli amacın kendisi belirsizse önce `product-vision` kullanılır.
- Bu stratejiden ölçülebilir çeyreklik hedefler çıkarılacaksa `okr-definition` kullanılır.
- Girişimlerin sıralı planı gerekiyorsa `roadmap` kullanılır.

## Girdiler
Zorunlu:
- Ürün, mevcut durumu (kullanıcılar, çekiş, ana sorunlar) ve stratejinin zaman ufku.

İsteğe bağlı, kaliteyi artırır:
- Vizyon, şirket stratejisi ve kısıtlar (bütçe, kadro, mevzuat).
- Pazar ve rakip analizi, müşteri araştırması, temel metrikler.
- Önceki strateji ve ne sonuç verdiği.

Ürünün durumu veya zaman ufku yoksa iste.

## Süreç
1. Teşhisi yaz: kanıta dayanan bir veya iki kritik zorluk ya da fırsat. Teşhissiz strateji bir dilek listesidir.
2. Nerede oynanacağını tanımla: hedef segmentler, kullanım senaryoları, coğrafyalar ve kanallar; dışarıda bırakılanları da yaz.
3. Nasıl kazanılacağını tanımla: kopyalanması zor avantaj (veri, dağıtım, entegrasyon derinliği, maliyet, deneyim). Rakiplere karşı sına.
4. 2-4 stratejik bahis seç: her birinin gerekçesi, etkilemesi beklenen sonuç ve bahsin yanlış olduğunu gösterecek sinyal olsun.
5. Hedef dışı konuları yaz: bu dönemde yapılmayacak cazip şeyler ve nedenleri.
6. Her bahsi bir sonuç metriğine (Kuzey Yıldızı veya girdi metriği) bağla; üzerinde anlaşılmamış hedefleri `[TBD]` olarak işaretle.
7. Gerekli yetkinlikleri veya yatırımları (ekip becerileri, platform işi, ortaklıklar) ve ana riskleri listele.
8. Tutarlılığı kontrol et: bahisler nasıl kazanılacağını destekliyor, hedef dışı konular bahislerle çelişmiyor, bütün mevcut kapasiteye sığıyor.
9. Tek sayfada tut; ayrıntıları eklere veya bağlantılı dokümanlara taşı.

## Çıktı formatı
```markdown
# Ürün Stratejisi: <ürün> (<zaman ufku>)
**Vizyon bağlantısı:** <tek satır>

## Teşhis
<kanıtıyla kritik zorluk/fırsat>

## Nerede Oynayacağız
- Odak: ...
- Dışarıda bırakılan: ...

## Nasıl Kazanacağız
<farklılaştırıcı avantaj ve neden savunulabilir olduğu>

## Stratejik Bahisler
| Bahis | Gerekçe | Sonuç metriği | Vazgeçme sinyali |
|---|---|---|---|

## Hedef Dışı Konular
- <konu> — <neden şimdi değil>

## Gerekli Yetkinlikler ve Riskler
- ...

## Açık Sorular
1. <soru> — <sorumlu>
```

## Kalite kontrol listesi
- [ ] Teşhis gerçek bir zorluğu adlandırıyor ve kanıt gösteriyor ya da `[VARSAYIM]` ile işaretli.
- [ ] "Nerede oynayacağız" en az bir cazip segmenti veya senaryoyu açıkça dışarıda bırakıyor.
- [ ] Her bahsin bir sonuç metriği ve vazgeçme sinyali var.
- [ ] Hedef dışı konular birilerinin gerçekten istediği şeyler, uydurma örnekler değil.
- [ ] Uydurma pazar büyüklüğü, gelir veya hedef yok.
- [ ] Tek sayfaya sığıyor.

## Sık yapılan hatalar
- Hedefleri ("geliri %30 artır") listeleyip strateji demek. Strateji, bir teşhise dayanarak "nasıl" sorusuna verilen seçimdir.
- Özellikleri bahis olarak yazmak. Bahis, değer ve avantaj hakkında bir hipotezdir; özellikler sonra gelir.
- Hedef dışı bölümünü boş bırakmak. Bu bölüm olmadan ekipler "hayır" diyemez.

## Örnek
Girdi: "B2B saha servis uygulaması, orta ölçekli klima firmalarında güçlü, hepsi bir arada paketlere karşı satış kaybediyor, 18 aylık ufuk."

Çıktıdan bir bölüm:
- Teşhis: Alıcılar araçlarını giderek birleştiriyor; finans ve CRM paket halinde sunulduğunda bağımsız planlama ürünümüz kaybediyor `[kazanma/kaybetme verisini teyit et]`.
- Nerede oynayacağız: Orta ölçekli teknik servis firmaları (klima, tesisat); dışarıda: kurumsal enerji dağıtım şirketleri.
- Bahis: Kendi faturalamamızı yazmak yerine derin muhasebe entegrasyonları — sonuç: paketlere karşı kazanma oranı — vazgeçme sinyali: iki çeyrek sonra kazanma oranında değişim yoksa.
