---
description: "Yabancı veya eski (legacy) bir kodun çalışılabilir haritasını çıkarır: giriş noktaları, modüller ve sorumlulukları, ana çalışma akışları, veri depoları, dış entegrasyonlar, gizli iş kuralları, ölü veya riskli alanlar ve güvenle değiştirilebilecek yerler; her sonucu koddaki bir kanıta bağlar. Bir geliştirici bir sistemi devraldığında, kimsenin tam anlamadığı kodu değiştirmesi gerektiğinde, bir modernizasyon planlandığında veya eski bir kod tabanının nasıl çalıştığı sorulduğunda kullanılır."
related: "code-explanation, refactoring, tech-debt-assessment, modernization-assessment, business-rules-catalog"
prompt: "Dokümantasyonu olmayan bu faturalama modülünü devraldım. Klasör yapısı ve ana sınıflar burada; bir faturanın nasıl oluşturulduğunu anlamama yardım et."
---

# Eski Kodu Anlama

## Amaç
Yabancı bir kod tabanını geliştiricinin üzerinde aksiyon alabileceği bir haritaya dönüştürmek: işler nerede oluyor, hangi kural nerede yaşıyor, neye dokunmak tehlikeli ve nereden başlanmalı; kodda görülenle hâlâ tahmin olanı açıkça ayırarak.

## Ne zaman kullanılır
- Bir ekip güvenilir dokümantasyonu veya asıl yazarları olmayan bir sistemi ya da modülü devraldığında.
- Akışı ve kuralları anlaşılmamış bir kodda değişiklik yapılması gerektiğinde.
- Bir modernizasyon, taşıma veya yeniden yazım mevcut davranışın ve gizli kuralların envanterine ihtiyaç duyduğunda.

## Ne zaman kullanılmaz
- Tek bir fonksiyon veya dosyanın açıklanması gerekiyorsa `code-explanation` kullanılır.
- Amaç kod yapısını adım adım iyileştirmekse `refactoring` kullanılır.
- Amaç karar vericiler için önceliklendirilmiş bir borç envanteriyse `tech-debt-assessment` kullanılır.

## Girdiler
Zorunlu:
- Kod parçalarına erişim: klasör ağacı, giriş noktaları veya ilgilenilen alanın çevresindeki dosyalar.
- Keşfi yönlendiren soru veya değişiklik (ör. "bir fatura nasıl oluşturuluyor").

İsteğe bağlı, kaliteyi artırır:
- Build ve deployment dosyaları, veritabanı şeması, konfigürasyon, loglar, commit geçmişinden öne çıkanlar, mevcut kayıtlar, sistemi hatırlayan kişiler.

Kodun yalnızca bir kısmı varsa görüneni haritala, boşlukları `[GÖRÜLMEDİ]` olarak işaretle ve sıradaki en bilgilendirici dosyaları her seferinde küçük bir grup hâlinde iste.

## Süreç
1. Yönlendiren soruya tutun; hedefsiz anlama çabası sonsuza kadar genişler.
2. Teknoloji yığınını ve giriş noktalarını belirle: ana programlar, HTTP route'ları, zamanlanmış işler, mesaj tüketicileri, UI ekranları, stored procedure'lar ve trigger'lar.
3. Modül haritasını çıkar: her paket veya bileşen için isimlerden, bağımlılıklardan ve koddan çıkarılan tek satırlık sorumluluk ile gelen/giden bağımlılıklar.
4. Yönlendiren soru için ana akışı giriş noktasından kalıcılığa ve dış çağrılara kadar izle; her adımda dosya ve fonksiyon adlarını kaydet.
5. Veri envanteri çıkar: dokunulan tablolar veya dosyalar, onlara kimin yazdığı ve diğer sistemlerin doğrudan okuduğu veriler.
6. Gizli iş kurallarını çıkar: durum kodlarına bağlı koşullar, sihirli sayılar, tarih kesimleri, özel müşteriler, konfigürasyon bayrakları; her birini konumuyla kaydet.
7. Risk bölgelerini işaretle: testi olmayan, sık değişen veya karmaşık kod, reflection veya dinamik dağıtım, paylaşılan global durum, kopyala-yapıştır varyantlar, ölü görünen kod (silmeden önce kullanım araması veya loglarla teyit et).
8. Dikişleri (seam) belirle: davranışın test için gözlemlenebildiği veya değiştirilebildiği yerler (arayüzler, konfigürasyon, sınırlar) ve istenen değişikliğin yapılacağı en güvenli nokta.
9. Değişikliklerden önce mevcut davranışı sabitleyen karakterizasyon testleri öner.
10. Her sonucu `[<dosya> içinde GÖRÜLDÜ]` veya `[ÇIKARIM]` olarak etiketle; açık soruları kimin veya neyin (loglar, veritabanı, iş sahibi) yanıtlayabileceğiyle listele.
11. Hedef devam ediyorsa alanı güvenle iyileştirmek için `refactoring`, çıkarılan kuralları belgelemek için `business-rules-catalog` veya bulunan riskleri önceliklendirmek için `tech-debt-assessment` öner.

## Çıktı formatı
```markdown
# Eski Kod Haritası: <sistem/modül>
Yönlendiren soru: <...> · Kapsam: <görülen / görülmeyen>

## Giriş Noktaları
| Tür | Ad | Konum |

## Modül Haritası
| Modül | Sorumluluk | Bağımlı olduğu | Kanıt |

## Ana Akış: <soru>
1. <adım> — <dosya:fonksiyon> — [GÖRÜLDÜ/ÇIKARIM]

## Dokunulan Veri
| Depo/tablo | Okuma/Yazma | Kim | Kiminle paylaşılıyor |

## Gizli İş Kuralları
| Kural | Konum | Kanıt | Kiminle teyit edilir |

## Risk Bölgeleri
## Dikişler ve Güvenli Değişiklik Noktası
## Eklenecek Karakterizasyon Testleri
## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Harita, yönlendiren soruyu izlenebilir bir akışla yanıtlıyor.
- [ ] Her ifade `[... içinde GÖRÜLDÜ]` veya `[ÇIKARIM]` olarak etiketli; görülmeyen alanlar `[GÖRÜLMEDİ]` olarak işaretli.
- [ ] Gizli iş kuralları konum ve teyit yolu içeriyor.
- [ ] "Ölü kod" yalnızca kanıtla iddia ediliyor ya da şüpheli olarak işaretleniyor.
- [ ] Somut bir güvenli değişiklik noktası ve karakterizasyon testleri öneriliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bir giriş noktasından tek bir akışı izlemek yerine her dosyayı baştan sona okumak.
- Davranış yerine isimlere ve yorumlara güvenmek; eski kodda isimler yıllar süren değişikliklerden sonra çoğu zaman yanıltıcıdır.
- Reflection, konfigürasyon, zamanlanmış işler veya veritabanını okuyan başka bir sistem üzerinden çağrılan "kullanılmayan" kodu silmek.
- Uygulamanın dışında yaşayan mantığı gözden kaçırmak: stored procedure'lar, trigger'lar, cron script'leri, ETL işleri.

## Örnek
Girdi: "Faturalama modülü, klasörler `jobs/`, `core/`, `db/procs/`. Bir fatura nasıl oluşturuluyor?"

Çıktıdan bir bölüm:
1. `jobs/NightlyBilling.run()`, `status IN (2,5)` olan sözleşmeleri seçiyor `[NightlyBilling.java içinde GÖRÜLDÜ]`
2. `sp_create_invoice` stored procedure'ını çağırıyor `[GÖRÜLDÜ]`; gövdesi `[GÖRÜLMEDİ]`, sıradaki istek `db/procs/sp_create_invoice.sql`.
- Gizli kural: `customer_type = 'K'` olan sözleşmeler KDV'yi atlıyor `[TaxCalc.java:88 içinde GÖRÜLDÜ]` — `'K'` değerinin anlamını finans sorumlusuyla teyit et.
