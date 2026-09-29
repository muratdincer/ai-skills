---
name: sequence-flow
description: "Uçtan uca tek bir senaryoda sistemlerin, servislerin ve aktörlerin nasıl etkileştiğini tarif eder: katılımcılar, sıralı mesajlar, senkron veya asenkron yapı, temel yük alanları, yanıtlar, zaman aşımları, yeniden denemeler ve alternatif ya da hata yolları; çıktı bir adım tablosu ve sıralama diyagramı kodudur. Bir senaryo birden çok sistemi kestiğinde, entegrasyon davranışı ekipler arasında netleştirilmesi gerektiğinde ya da 'ne neyi, hangi sırayla çağırıyor, hata olursa ne oluyor?' sorusu sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: system-analyst
  area: specification
  title: "Sistem etkileşim akışı"
  related: "integration-requirements, api-contract, error-scenario-catalog, state-model, diagram-as-code"
  prompt: "Online sipariş için akışı tarif et: web mağaza, sipariş servisi, ödeme geçidi, stok servisi ve bildirim; ödeme zaman aşımı dahil."
---

# Sistem Etkileşim Akışı

## Amaç
Belirli bir senaryo için kimin kiminle, hangi sırayla, hangi sözleşme ve hata davranışıyla konuştuğunu tasarımcılar, geliştiriciler ve test uzmanları için tek ve üzerinde anlaşılmış bir resimde toplamak. Bu, fonksiyonel gereksinimlerle arayüz veya API tasarımı arasındaki boşluğu kapatır.

## Ne zaman kullanılır
- Bir kullanıcı veya iş senaryosu iki ya da daha fazla sistemi, servisi veya dış paydaşı kapsıyorsa.
- Farklı sistemlerin sahibi olan ekiplerin çağrı sırası, senkron/asenkron yapı ve hata yönetimi üzerinde anlaşması gerekiyorsa.
- Bir olay veya değişiklik, yeniden tasarımdan önce mevcut etkileşimin belgelenmesini gerektiriyorsa.

## Ne zaman kullanılmaz
- Tek bir arayüzün tam tanımı (alanlar, formatlar, SLA'lar) gerekiyorsa `integration-requirements` veya `api-contract` kullanılır.
- Tek bir varlığın yaşam döngüsü gerekiyorsa `state-model` kullanılır.
- Roller arası insan iş süreci gerekiyorsa `bpmn-model` kullanılır.

## Girdiler
Zorunlu:
- Senaryo (tetikleyici, hedef, bitiş durumu) ve dahil olan sistemler veya aktörler.

İsteğe bağlı, kaliteyi artırır:
- Arayüz listesi veya API tanımları, mimari bağlam (örn. C4 container görünümü).
- Fonksiyonel olmayan beklentiler: gecikme, karşı sistemlerin erişilebilirliği, hacimler.
- Bilinen hata olayları veya kısıtlar (toplu iş pencereleri, istek sınırları).

Senaryo veya katılan sistemler bilinmiyorsa, her seferinde bir soru sorarak iste. Geri kalan her şey `[TBD]` ya da açık soru olur.

## Süreç
1. Senaryoyu yaz: tetikleyici, ön koşullar, başarılı bitiş durumu ve iş sonucu. Her akışta tek senaryo olsun; varyantları ayrı listele.
2. Katılımcıları çağrı sırasına göre soldan sağa listele: aktör, ön yüz, servisler, önemli veri depoları, dış paydaşlar, mesaj aracısı (broker). Her birinin sahibini işaretle.
3. Ana başarı yolunu numaralı mesajlarla yaz: gönderen, alıcı, işlem veya olay adı, senkron (istek/yanıt) ya da asenkron (olay/kuyruk), temel yük alanları ve yanıt.
4. İşlem ve tutarlılık sınırlarını işaretle: verinin nerede kalıcılaştığı, nihai tutarlılığın (eventual consistency) nerede başladığı ve sonraki bir adım başarısız olursa neyin telafi edildiği (örn. stoğu serbest bırakma, iade).
5. Her senkron çağrı için zaman aşımı, yeniden deneme politikası ve idempotency anahtarını; her asenkron mesaj için teslim garantisini, sıralama ihtiyacını ve tekrar yönetimini tanımla. Bilinmeyen değerler `[TBD]` olur.
6. Alternatif ve hata yollarını ekle: karşı sistem kapalı, zaman aşımı, iş kuralı reddi, kısmi başarı, tekrarlanan istek, zaman aşımından sonra gelen geç yanıt. Her birinde kullanıcının ne gördüğünü yaz.
7. Güvenlik ve veri noktalarını not et: sistemler arası kimlik doğrulama, sınır geçen kişisel veri (maskele veya azalt), denetim ya da log kayıtları.
8. Girdide belirtilmeyen her davranışı `[VARSAYIM]` olarak etiketle ve açık soruları sahibi olan ekiple listele.
9. Tabloyla eşleşen alt/opt bloklarıyla sıralama diyagramı kodu üret (Mermaid sequenceDiagram veya PlantUML).
10. Kullanıcı devam etmek isterse her arayüz için `integration-requirements` veya `api-contract`, hata yolları için `error-scenario-catalog`, akış boyunca durumu değişen varlıklar için `state-model` öner.

## Çıktı formatı
```markdown
# Akış: <senaryo>
Tetikleyici: <...> · Ön koşullar: <...> · Başarılı bitiş: <...>

## Katılımcılar
| Katılımcı | Tür (aktör / servis / depo / dış paydaş / broker) | Sahibi |
|---|---|---|

## Ana Akış
| # | Kimden → Kime | Mesaj / işlem | Yapı (senkron / asenkron) | Temel veri | Yanıt / sonuç |
|---|---|---|---|---|---|

## Güvenilirlik Kuralları
| Adım | Zaman aşımı | Yeniden deneme | Idempotency / tekrar | Telafi |
|---|---|---|---|---|

## Alternatif ve Hata Yolları
| Ref | Koşul | Davranış | Kullanıcı ne görür |
|---|---|---|---|

## Diyagram
<Mermaid sequenceDiagram veya PlantUML kodu>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ... — sorumlu ekip
```

## Kalite kontrol listesi
- [ ] Akış, net bir tetikleyici ve bitiş durumuyla tam olarak tek bir senaryoyu kapsıyor.
- [ ] Her mesajın göndereni, alıcısı, yapısı ve yanıtı ya da onayı var.
- [ ] Her dış veya uzak çağrı için zaman aşımı, yeniden deneme ve tekrar yönetimi tanımlı ya da `[TBD]` olarak işaretli.
- [ ] Veri kalıcılaştıktan sonra başarısız olabilecek her adımın bir telafisi ya da açıkça "yok" ifadesi var.
- [ ] Tablo ve diyagram aynı mesajları aynı sırayla içeriyor.
- [ ] Çıkarım olan davranışlar `[VARSAYIM]` etiketli; sınır geçen kişisel veri işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca mutlu yolu çizmek. Akışın değeri, ekiplerin anlaşamadığı zaman aşımı, yeniden deneme ve telafi noktalarındadır.
- Ödeme tahsilatı gibi idempotent olmayan çağrıları yeniden denemek. Yeniden denemeden önce idempotency anahtarı veya durum sorgusu şart koş.
- Birden çok senaryoyu iç içe alt bloklarıyla kimsenin okuyamayacağı hâle getirmek. Ayrı akışlara böl.

## Örnek
Girdi: "Müşteri sipariş verir: web mağaza sipariş servisini çağırır, sipariş servisi ödeme geçidinden tahsil eder, stok ayırır, onay e-postası gönderir."

Çıktıdan bir bölüm:
| # | Kimden → Kime | Mesaj | Yapı | Temel veri | Yanıt |
|---|---|---|---|---|---|
| 1 | Web mağaza → Sipariş servisi | createOrder | senkron | sepet, customerId, idempotencyKey | orderId, durum Beklemede |
| 2 | Sipariş servisi → Ödeme geçidi | authorize | senkron | orderId, tutar | authCode veya ret |
| 3 | Sipariş servisi → Broker | OrderConfirmed | asenkron | orderId, satırlar | ack |

Hata yolu F1: ödeme geçidi `[TBD]` sn sonra zaman aşımına uğrar. Körlemesine yeniden deneme yapma; orderId ile ödeme durumunu sorgula, siparişi Beklemede tut ve "Ödemeniz doğrulanıyor" göster. `[VARSAYIM]`: stok yalnızca provizyon sonrası ayrılır.
