---
description: Mevcut durumu, iş, veri, uygulama ve teknoloji görünümlerinde hedef durumu, aralarındaki farkları ve bağımlılıklar ile karar noktaları içeren ara durumlardan oluşan bir geçiş yol haritasını tanımlayarak hedef mimariyi ortaya koyar. Bir dönüşüm, platform birleştirme veya çok yıllı program, mimarinin nereye gitmesi gerektiği ve oraya nasıl varılacağı konusunda ortak bir resme ihtiyaç duyduğunda kullanılır.
related: capability-map, architecture-principles, migration-strategy, application-portfolio-assessment, roadmap
prompt: Monolitik sipariş yönetimimizi ve gece çalışan toplu entegrasyonlarımızı üç yıl içinde olay akışı kullanan alan servislerine taşımak için hedef mimariyi tanımla.
---

# Hedef Mimari Tanımlama

## Amaç
Sponsorlara ve teslimat ekiplerine mevcut durum, hedef ve aralarındaki sıralı geçişler için tek ve üzerinde uzlaşılmış bir tanım vermek; böylece yatırımlar ve projeler sistem envanterini aynı yöne taşır.

## Ne zaman kullanılır
- Çok yıllı bir dönüşüm veya program, projeler başlamadan önce yön belirlemeye ihtiyaç duyduğunda.
- Birden fazla girişim aynı yapıyı değiştiriyor ve bunların birleşmesi gerektiğinde.
- Bir stratejinin (bulut, veri, API öncelikli) mimariye çevrilmesi gerektiğinde.
- Bir fonlama kararı fark analizi ve aşamalı yol haritası gerektirdiğinde.

## Ne zaman kullanılmaz
- Yalnızca tek bir sistem tasarlanıyorsa `solution-architecture-document` kullanılır.
- Soru belirli bir sistemin nasıl devreye alınacağıysa `migration-strategy` kullanılır.
- Yol gösterici kurallar hiç yoksa önce `architecture-principles` kullanılır.

## Girdiler
Zorunlu:
- Kapsam ve iş hedefleri (ne değişmeli ve neden).
- Mevcut durum tanımı: ana uygulamalar, entegrasyonlar, veri depoları, platformlar (liste yeterli).

İsteğe bağlı:
- Yetkinlik haritası, uygulama portföyü değerlendirmesi, ilkeler, standartlar.
- Kısıtlar: bütçe zarfı, yasal tarihler, sözleşmeler, yetkinlikler.
- Program takvimi veya fonlama dönemleri.

Hedefler veya mevcut durum yoksa sor. Tarih veya bütçe uydurma.

## Süreç
1. Hedefleri ölçülebilir hedef sonuçlar olarak yaz (ör. "alan başına sürüm teslim süresi", "gerçek zamanlı sipariş durumu", "sözleşme bitiminde veri merkezinden çıkış").
2. Mevcut durumu dört görünümde (iş, veri, uygulama, teknoloji) aynı soyutlama düzeyinde tanımla; her görünümdeki bilinen sorunları not et.
3. Hedef durumu aynı dört görünümde, ilkelerden ve hedeflerden türeterek tanımla. Kararın henüz verilmediği yerlerde teknolojiden bağımsız kal ve `[KARAR BEKLİYOR]` olarak işaretle.
4. Fark analizi yap: her öğe için mevcut → hedef ve aksiyon (koru, değiştir, yeni, kaldır).
5. Farkları iş paketlerinde grupla; bağımlılıkları belirle (alandan önce platform, rapordan önce veri).
6. 2-4 geçiş mimarisi (ara durum) tanımla; her biri tek başına değer üreten, tutarlı ve işletilebilir bir durum olmalı.
7. Her ara durum için giriş kriterlerini, canlıya alınanları, kaldırılanları, geçici entegrasyonları ve riskleri listele.
8. Mimari kararları ve en geç verilmeleri gereken tarihi belirle; ADR'lere bağla.
9. Hedefe ulaşıldığını doğrulayacak ölçüleri tanımla (fitness function'lar, hedef başına KPI'lar).
10. Varsayımları, kısıtları ve yönlendirme kurulu için açık soruları kaydet.
11. Hedef devam ediyorsa her geçiş için `migration-strategy`, zamanlama için `roadmap` veya temel hedef kararlar için `adr` öner.

## Çıktı formatı
```markdown
# Hedef Mimari – <kapsam>
Ufuk: <ör. 3 yıl> · Durum: Taslak

## Hedefler ve Hedef Sonuçlar
| Hedef | Hedef sonuç | Ölçü |

## Mevcut Durum (İş / Veri / Uygulama / Teknoloji)
## Hedef Durum (İş / Veri / Uygulama / Teknoloji)
## Fark Analizi
| Görünüm | Öğe | Mevcut | Hedef | Aksiyon | İş paketi |

## Geçiş Mimarileri
### Ara Durum 1 – <ad>
- Canlıda: ... · Kaldırılan: ... · Geçici entegrasyonlar: ... · Giriş kriterleri: ... · Riskler: ...

## Bekleyen Kararlar
| Karar | Seçenekler | En geç karar tarihi | Sorumlu |

## Ölçüler, Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Mevcut ve hedef durum aynı görünümleri ve soyutlama düzeyini kullanıyor.
- [ ] Her farkın bir aksiyonu var ve bir iş paketine ait.
- [ ] Her ara durum işletilebilir ve tek başına değer üretiyor; geçici entegrasyonlar açıkça yazılı.
- [ ] Verilmemiş teknoloji kararları varsayılmadı, işaretlendi.
- [ ] Her hedefin ilerlemeyi izleyecek bir ölçüsü var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca hedefi çizmek. Mevcut durum ve ara durumlar olmadan plan yoktur, yalnızca resim vardır.
- Ara durumları yok saymak. Geçici entegrasyonlar ve paralel çalışma maliyeti çoğu zaman en büyük risktir.
- Hedefi araç düzeyinde dondurmak. Yetkinlikleri ve desenleri belirt; ürünleri kararlarla seç.

## Örnek
Girdi: "Monolitik sipariş yönetimi, ERP ve depoya gece toplu aktarım; hedef: gerçek zamanlı sipariş durumu."

Çıktıdan bir bölüm:
| Görünüm | Öğe | Mevcut | Hedef | Aksiyon |
|---|---|---|---|---|
| Uygulama | Sipariş yönetimi | Monolit | Sipariş, Karşılama, Faturalama alan servisleri | Değiştir |
| Veri | Depoya sipariş durumu | Gece dosyası | Akış platformunda sipariş olayları `[KARAR BEKLİYOR: platform]` | Yeni |
- Ara Durum 1: Sipariş olayları monolitten CDC ile yayınlanır; depo olayları tüketir; gece dosyası yalnızca depo için kaldırılır.
