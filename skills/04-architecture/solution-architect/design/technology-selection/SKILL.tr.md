---
description: Yapılandırılmış bir teknoloji seçimi yürütür - problemin çerçevelenmesi, kalite nitelikleri, maliyet, risk ve ekosistem sağlığını içeren ağırlıklı ölçütler, uzun listeden kısa listeye iniş, geçti/kaldı kriterli bir kavram kanıtı (PoC) planı ve ADR olarak kaydedilen bir öneri. Önemli bir ihtiyaç için veritabanı, mesaj kuyruğu, framework, platform, SaaS ürünü veya kütüphane seçerken ya da bir ekibin tercih ettiği aracın nesnel olarak gerekçelendirilmesi gerektiğinde kullanılır.
related: adr, build-vs-buy, tech-radar, vendor-evaluation, spike-report
prompt: Sipariş ve stok olayları için bir mesaj kuyruğu seçmemize yardım et; sipariş bazında sıralama, 7 gün geriye oynatma gerekiyor ve Kubernetes üzerinde çalışıyoruz.
---

# Teknoloji Seçimi

## Amaç
Açık ölçütler, kanıt ve odaklı bir kavram kanıtıyla savunulabilir bir teknoloji seçimine ulaşmak; böylece karar sorgulamaya dayanır ve riskleri bağlanmadan önce bilinir.

## Ne zaman kullanılır
- Önemli bir bileşen (veritabanı, mesaj kuyruğu, API gateway, kimlik sağlayıcı, framework, SaaS) seçilmesi gerektiğinde.
- Birden fazla ekip farklı araçları savunuyor ve nesnel bir karşılaştırma gerektiğinde.
- Radardaki bir Dene veya Değerlendir öğesi gerçek bir proje için önerildiğinde.
- Satın alma süreci belgelenmiş bir değerlendirme istediğinde.

## Ne zaman kullanılmaz
- Asıl soru yapmak mı satın almak mı ise `build-vs-buy` kullanılır.
- Sözleşme ve fiyatlandırmayla ticari tedarikçi karşılaştırması için `vendor-evaluation` kullanılır.
- Tek bir bilinmeyenin süreli teknik araştırması için `spike-report` kullanılır.

## Girdiler
Zorunlu:
- İhtiyaç duyulan problem veya yetkinlik ve temel gereksinimleri (fonksiyonel ve kalite).
- Kesin kısıtlar (barındırma, lisans, mevzuat, mevcut teknoloji yığını, bütçe zarfı).

İsteğe bağlı:
- Masadaki adaylar, teknoloji radarı ve standartlar.
- Ekip yetkinlikleri, işletim modeli (kim işletecek), takvim.
- Hacim ve büyüme rakamları.

Gereksinimler veya kısıtlar yoksa sor. Benchmark sonucu, fiyat veya sürüm özelliği uydurma; `[DOĞRULA]` olarak işaretle.

## Süreç
1. İhtiyacı bir ürün olarak değil, yetkinlikler ve kalite senaryoları olarak çerçevele ("anahtar bazında sıralı, 7 gün geriye oynatılabilir kalıcı olay günlüğü"); adaylar ihtiyaca göre karşılaştırılsın.
2. Zorunlu kısıtları (eleme) ağırlıklı ölçütlerden ayır. Tipik ölçütler: fonksiyonel uygunluk, kalite nitelikleri (performans, erişilebilirlik, ölçeklenebilirlik, güvenlik), işletilebilirlik, maliyet (lisans, altyapı, insan), ekosistem ve üretici sağlığı, yetkinlik, bağımlılık/çıkış maliyeti, lisans uyumluluğu.
3. Puanlamadan önce ağırlıklarda paydaşlarla uzlaş; ağırlıkların toplamı 100 olmalı.
4. Radar, pazar ve ekip girdilerinden uzun listeyi (5-8) oluştur; elemeleri uygulayarak her eleme için gerekçe yazıp 2-3 adaylık kısa listeye in.
5. Kısa listeyi ölçüt başına 1-5 arasında kanıt ve güven düzeyiyle puanla; puanların doğrulanmamış iddialara dayandığı yerleri not et.
6. Aday başına en riskli varsayımları belirle ve bunları sınayan bir PoC tasarla: senaryolar, veri hacmi, hata enjeksiyonu, başarı eşikleri, süre sınırı, kişiler.
7. Duyarlılık kontrolü yap: en yüksek iki ağırlık ±10 puan değişirse kazanan değişiyor mu? Değişiyorsa belirt.
8. Koşullu öneri ver: seçim, neden, azaltım önlemleriyle ana riskler, çıkış stratejisi ve PoC'nin neyi doğrulaması gerektiği.
9. ADR özetini ve radar etkisini (ör. yeni Dene öğesi) taslak olarak yaz.

## Çıktı formatı
```markdown
# Teknoloji Seçimi – <ihtiyaç>
## İhtiyaç ve Kalite Senaryoları
## Kısıtlar (eleme)
## Ölçütler ve Ağırlıklar
| Ölçüt | Ağırlık | Nasıl ölçülür |
## Uzun Liste ve Elemeler
| Aday | Elendi mi? | Gerekçe |
## Kısa Liste Puanlaması
| Ölçüt (ağırlık) | Aday A | Aday B | Aday C | Kanıt / güven |
## PoC Planı
| Hipotez | Test | Geçme eşiği | Süre | Sorumlu |
## Duyarlılık
## Öneri, Riskler ve Çıkış Stratejisi
## ADR Taslak Özeti · Açık Sorular
```

## Kalite kontrol listesi
- [ ] İhtiyaç herhangi bir üründen bağımsız ifade edildi.
- [ ] Ağırlıklar puanlamadan önce sabitlendi ve toplamı 100.
- [ ] Her elemenin ve puanın gerekçesi var; doğrulanmamış iddialar işaretli.
- [ ] PoC en riskli varsayımları ölçülebilir geçme eşikleriyle sınıyor.
- [ ] Çıkış maliyeti ve bağımlılık değerlendirildi.
- [ ] Öneri koşullarını belirtiyor ve ADR'ye dönüşmeye hazır.

## Sık yapılan hatalar
- Favori araçtan başlayıp ölçütleri ona göre uydurmak. Önce ihtiyacı çerçevele.
- İşletilebilirliği ve insan maliyetini yok saymak. En ucuz lisans işletmesi en pahalı olan olabilir.
- Mutlu yolu gösteren PoC'ler. Hata durumunu, ölçeği ve bilinmeyenleri test et.

## Örnek
Girdi: "Sipariş ve stok olayları, sipariş bazında sıralama, 7 gün geriye oynatma, Kubernetes."

Çıktıdan bir bölüm:
| Ölçüt (ağırlık) | Log tabanlı broker | Kuyruk tabanlı broker | Yönetilen bulut akışı |
|---|---|---|---|
| Anahtar bazında sıralama + geriye oynatma (30) | 5 | 2 (yerleşik geriye oynatma yok) | 4 `[saklama sınırlarını DOĞRULA]` |
| Kubernetes'imizde işletilebilirlik (20) | 3 | 4 | 5 (yönetilen) |
- PoC hipotezi: Pod yeniden başlatmalarında tüketici yeniden dengelemesi sipariş bazında sıralamayı bozmaz; geçme = 1 milyon mesajda sıfır sıra dışı olay `[hacmi teyit et]`.
