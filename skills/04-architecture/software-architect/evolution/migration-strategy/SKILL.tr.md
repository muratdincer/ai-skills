---
name: migration-strategy
description: "Mevcut bir sistemden veya platformdan hedefe geçişi; strangler fig, paralel çalıştırma, aşamalı ve tek seferde geçiş yaklaşımlarını karşılaştırarak, dilimleri ve sıralarını, veri taşıma ve senkronizasyonu, birlikte çalışma ve yönlendirmeyi, her adım için doğrulama ve geri dönüşü ve geçiş (cutover) kriterlerini tanımlayarak planlar. Bir sistem değiştirilirken veya platform değiştirirken, monolitten servis ayrılırken, yeni bir veritabanına ya da buluta geçilirken veya bir göç planının risk incelemesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: software-architect
  area: evolution
  title: "Göç stratejisi planlama"
  related: "target-state-architecture, service-decomposition, modernization-assessment, rollback-plan, schema-migration-plan"
  prompt: "Şirket içindeki sipariş yönetimi monolitimizin yeni bulut tabanlı sipariş servislerine, satış sezonunda kesinti olmadan göçünü planla."
---

# Göç Stratejisi Planlama

## Amaç
Her adımın bir değer ürettiği veya riski azalttığı, doğrulanabildiği ve geri alınabildiği adım adım bir göç planı üretmek. Böylece eskiden yeniye geçiş tek bir yüksek riskli geçiş anına bağlı kalmaz.

## Ne zaman kullanılır
- Hedef mimari belli ve mevcut durumdan oraya giden yol planlanacaksa.
- Bir monolit bölünüyor, ayırma sırası ve birlikte çalışma tasarlanacaksa.
- İş devam ederken verinin yeni bir depoya veya platforma taşınması gerekiyorsa.
- Mevcut bir göç planı tek bir büyük geçişe dayanıyor ve sorgulanması gerekiyorsa.

## Ne zaman kullanılmaz
- Modernize edilip edilmeyeceği ve nasıl (koru, yeniden barındır, yeniden yapılandır, değiştir) kararı hâlâ açıksa `modernization-assessment` kullanılır.
- Hedef durumun kendisi tanımsızsa `target-state-architecture` kullanılır.
- Yalnızca tek bir sürümün geri alma adımları gerekiyorsa `rollback-plan` kullanılır.

## Girdiler
Zorunlu:
- En az blok düzeyinde mevcut ve hedef durum (sistemler, veri depoları, arayüzler).
- İş kısıtları: izin verilen kesinti, yasak dönemler (blackout), son tarihler ve gerekçeleri.

İsteğe bağlı:
- Veri hacimleri ve değişim hızları, entegrasyon envanteri, tüketici listesi, ekip kapasitesi, yasal kısıtlar (veri yerelliği, denetim izi).

İzin verilen kesinti veya yasak dönemler bilinmiyorsa sor; yaklaşımı bunlar belirler. Diğer boşlukları `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Mevcut ile hedef arasındaki farkı ve göç etkenlerini (destek sonu, maliyet, yetkinlik) özetle. Kullanıcılar için neyin değişmemesi gerektiğini yaz.
2. Yaklaşımları kısıtlara göre karşılaştır: strangler fig (işlevselliğin kademeli yönlendirilmesi), paralel çalıştırma (iki sistem de işler, çıktılar karşılaştırılır), kullanıcı grubu, bölge veya fonksiyona göre aşamalı geçiş ve tek seferde geçiş (big bang). Gerekçesiyle birini veya bir bileşimi öner; tek seferde geçişi yalnızca birlikte çalışma imkânsız veya daha ucuzsa ve risk açıkça kabul edilmişse öner.
3. Dilimleri tanımla: bağımsız taşınabilen ince dikey birimler (bir yetkinlik, bir akış, bir müşteri segmenti). Öğrenme değeri, risk ve bağımlılığa göre sırala; tüm yolu çalıştıran düşük riskli bir dilimle başla.
4. Birlikte çalışmayı tasarla: yönlendirme mekanizması (facade, API gateway, feature flag), eski ve yeni modeller arasında anticorruption layer ve kesişen konuların (kimlik doğrulama, kimlikler, raporlama) geçiş süresince nasıl işleyeceği.
5. Her dilim için veri taşımayı planla: birlikte çalışma sırasında sahiplik (tek yazan), ilk yükleme, süregelen senkronizasyon (CDC, outbox ile çift yazma, toplu iş), mutabakat kontrolleri ve çakışmaların nasıl çözüleceği.
6. Her adım için doğrulamayı tanımla: işlevsel eşdeğerlik testleri, paralel çalıştırmada çıktı karşılaştırması, performans başlangıç değerleri ve izlenecek iş KPI'ları.
7. Her adım için geri dönüşü tanımla: tetikleyici koşullar, mekanizma (geri yönlendirme, veriyi geriye senkronize etme) ve geri dönüşün artık mümkün olmadığı dönüşü olmayan nokta.
8. Geçiş ve kapatma kriterlerini belirle: hangi kanıtın tam geçişe izin verdiği ve eski bileşenin, verisinin ve lisanslarının ne zaman emekliye ayrılacağı.
9. Riskleri (veri kaybı, uzayan çift çalışma, ekip kapasitesi, tüketici hazırlığı) azaltma önlemleriyle eşle ve zaman çizelgesinde yasak dönemlere uy.
10. Kullanıcının vermediği her boyutlandırma, süre veya bağımlılığı `[VARSAYIM]` olarak etiketle; tarih uydurma.
11. Hedef devam ediyorsa veritabanı değişiklikleri için `schema-migration-plan`, tekil sürümler için `rollback-plan` veya seçilen yaklaşımı kaydetmek için `adr` öner.

## Çıktı formatı
```markdown
# Göç Stratejisi: <kaynak> → <hedef>
Kısıtlar: kesinti <...> · yasak dönem <...> · son tarih <... veya [BİLİNMİYOR]>

## Yaklaşım
- Seçilen: <strangler fig | paralel çalıştırma | aşamalı | tek seferde | bileşim> — çünkü ...
- Reddedilen: <yaklaşım> — çünkü ...

## Dilimler ve Sıra
| # | Dilim | Neden bu sırada | Bağımlılık | Birlikte çalışma / yönlendirme | Veri stratejisi | Doğrulama | Geri dönüş (dönüşü olmayan nokta) |
|---|---|---|---|---|---|---|---|

## Veri Taşıma
- Birlikte çalışma sırasında sahiplik: ...
- İlk yükleme / senkronizasyon / mutabakat: ...

## Geçiş ve Kapatma Kriterleri
- ...

## Riskler ve Önlemler
| Risk | Olasılık | Etki | Önlem | Sahip |
|---|---|---|---|---|

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Yaklaşım belirtilen kesinti, yasak dönem ve son tarih kısıtlarına göre gerekçelendirilmiş.
- [ ] Her dilimin doğrulaması, geri dönüş yolu ve belirtilmiş bir dönüşü olmayan noktası var.
- [ ] Birlikte çalışma boyunca her veri kümesinin herhangi bir anda tek bir yazanı var ya da çakışma çözümü tanımlı.
- [ ] Eski bileşenlerin kapatılması planlanmış, açık bırakılmamış.
- [ ] Hiçbir tarih, hacim veya süre uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Teknik katmanları taşımak (önce veritabanı, sonra backend, sonra arayüz); sona kadar hiçbir değer üretmez. Dikey dilimleri taşı.
- Outbox veya mutabakat olmadan uygulama kodundan çift yazma; sessizce birbirinden ayrışır.
- Hiç bitirmemek: strangler facade ve eski sistem sonsuza kadar yaşar. Kapatma kriterleri koy ve takip et.

## Örnek
Girdi: "Şirket içi sipariş yönetimini bulut sipariş servislerine taşı; satış sezonunda kesinti olmasın."

Çıktıdan bir bölüm:
- Yaklaşım: yönlendirme facade'ı ile strangler fig, ayrıca sipariş fiyatlaması için iki haftalık paralel çalıştırma; çünkü kesintiye izin yok ve fiyatlama hataları pahalı.
- Dilim 1: sipariş durum sorguları (salt okunur) — düşük risk, facade'ı, kimlik doğrulamayı ve veri senkronizasyonunu uçtan uca çalıştırır.
- Dilim 3: tek bir satış kanalı için sipariş verme; dönüşü olmayan nokta: yeni servisin sipariş başlıklarının tek yazanı olduğu an.
- Yasak dönem: satış sezonunda geçiş adımı yok `[kesin tarihler BİLİNMİYOR, satışla teyit et]`.
