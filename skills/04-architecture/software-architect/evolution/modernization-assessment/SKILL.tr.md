---
description: Eski (legacy) bir sistemi iş uyumu, teknik sağlık, operasyonel risk ve değişim etkenleri açısından değerlendirir; ardından 7R seçeneklerini (emekliye ayır, olduğu gibi tut, yeniden barındır, yer değiştir, platform değiştir, hazır ürün al, yeniden yapılandır/yeniden mimarile) göreli efor, değer ve riskle karşılaştırır, karar kriterleri ve ilk adımlarla bir yol önerir. Eski bir uygulama baskı altındayken (destek sonu, maliyet, yetkinlik, ölçeklenebilirlik, uyum), yönetim "X sistemiyle ne yapmalıyız?" diye sorduğunda veya bir taşıma ya da yeniden yazıma bütçe ayırmadan önce kullanılır.
related: legacy-code-comprehension, tech-debt-assessment, migration-strategy, build-vs-buy, application-portfolio-assessment
prompt: Şirket içinde çalışan 15 yıllık .NET Framework sipariş yönetimi monolitimizi değerlendir. İşletim sisteminin desteği seneye bitiyor ve sistemi yalnızca iki kişi biliyor. Seçeneklerimiz neler?
---

# Eski Sistem Modernizasyon Değerlendirmesi

## Amaç
Belirsiz bir "bu sistem eskidi" hissini savunulabilir bir modernizasyon kararına dönüştürmek: değişimin neden gerektiği, hangi 7R seçeneklerinin uygulanabilir olduğu, her birinin göreli maliyeti ve getirisi ve işe hangisiyle başlanacağı net olsun.

## Ne zaman kullanılır
- Sistem kesin bir etkenle karşı karşıya: üretici veya platform desteğinin bitmesi, kilit kişi riski, uyum açığı, artan maliyet, ölçeklenememe veya değiştirilememe.
- Yönetim, bütçeden önce tek bir eski uygulama için seçenekler istiyor.
- Bir yeniden yazım önerildi ve daha ucuz seçeneklerle sınanması gerekiyor.

## Ne zaman kullanılmaz
- Portföy kararı için çok sayıda uygulama sıralanacaksa `application-portfolio-assessment` kullanılır.
- Seçenek belirlendi ve taşımanın sıralanması gerekiyorsa `migration-strategy` kullanılır.
- Soru yalnızca hangi kod düzeyindeki borcun ödeneceğiyse `tech-debt-assessment` kullanılır.

## Girdiler
Zorunlu:
- Sistem tanımı: amacı, kullanıcıları, ana teknolojileri ve entegrasyonları ve değişim etkeni.

İsteğe bağlı, kaliteyi artırır:
- Mimari veya dağıtım diyagramları, kod metrikleri, olay ve değişiklik geçmişi, işletim maliyeti.
- Yetenek için iş yol haritası, hedef platform standartları, mevcut yetkinlikler ve bütçe zarfı.
- Veri hacimleri, mevzuat kısıtları, sözleşmeler ve lisanslar.

Değişim etkeni bilinmiyorsa sor; o olmadan hiçbir seçenek sıralanamaz. En fazla beş soru sor; kalanları açık soru olarak listele.

## Süreç
1. Etkenleri ve her birinin arkasındaki son tarihi yaz (ör. "işletim sistemi desteği 3. çeyrekte bitiyor" `[teyit et]`); kesin etkenleri (harekete geçmek zorunlu) yumuşak etkenlerden (olsa iyi olur) ayır.
2. İş uyumunu değerlendir: yeteneğin ne kadar kritik olduğu, farklılaştırıcı mı yoksa sıradan mı olduğu, beklenen değişim hızı ve standart bir ürünün olup olmadığı.
3. Teknik sağlığı değerlendir: platformun güncelliği, mimari (monolit sınırları, bağımlılık, paylaşılan veritabanı), kod kalitesi sinyalleri, test kapsamı, build ve deploy otomasyonu, dokümantasyon, kilit kişi bağımlılığı.
4. Operasyonel riski değerlendir: olaylar, güvenlik açıkları, ölçeklenebilirlik sınırları, kurtarma yeteneği, lisans ve destek riski.
5. Bağımlılıkları çıkar: yukarı/aşağı akış entegrasyonları, veri sahipliği, batch işler, raporlar ve veritabanının gizli tüketicileri.
6. Her 7R seçeneğini uygulanabilirlik açısından değerlendir; uygulanamayanları tek satırlık gerekçeyle ele. Uygulanabilir olanlar için göreli efor, değer, risk ve ilk faydaya kadar geçen süreyi (Düşük/Orta/Yüksek) puanla; asla maliyet uydurma.
7. Büyük patlama tarzı yeniden yazımlardan önce artımlı yolları (strangler fig, en sık değişen yeteneği önce ayırma) değerlendir; yeniden yazımın neden gerekçeli olduğunu ya da olmadığını açıkla.
8. Bir ana seçenek (ve bir yedek) öner; kararı değiştirecek kriterleri ve ön koşulları (yetkinlik, fon, değişiklik dondurma pencereleri) belirt.
9. Belirsizliği azaltan ilk adımları öner: süre sınırlı spike, bağımlılık keşfi, test güvenlik ağı, veri profilleme.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, riskleri ve açık soruları topla; hedef devam ediyorsa seçilen yolu planlamak için `migration-strategy`, hazır ürün uygulanabilirse `build-vs-buy`, bilgi riskini azaltmak için `legacy-code-comprehension` öner.

## Çıktı formatı
```markdown
# Modernizasyon Değerlendirmesi: <sistem>
Etkenler: <kesin> / <yumuşak> · Son tarih: <tarih veya [BİLİNMİYOR]>

## Mevcut Durum
| Boyut | Bulgu | Puan (İyi/Orta/Zayıf) | Kanıt |
|---|---|---|---|
| İş uyumu | ... | | |
| Teknik sağlık | ... | | |
| Operasyonel risk | ... | | |
| Bağımlılıklar | ... | | |

## Seçenekler (7R)
| Seçenek | Uygulanabilir mi? | Efor | Değer | Risk | Faydaya süre | Notlar |
|---|---|---|---|---|---|---|

## Öneri
- Ana seçenek: ... çünkü ...
- Yedek: ...
- Şu durumda değişir: ...
- Ön koşullar: ...

## İlk Adımlar
1. ...

## Varsayımlar, Riskler ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her seçenek puanı girdideki bir kanıta bağlı veya `[VARSAYIM]` olarak etiketli; hiçbir maliyet rakamı uydurulmadı.
- [ ] Yedi seçeneğin hepsi değerlendirildi ve elenenlerin gerekçesi var.
- [ ] Önerinin zamanlamasını kesin etkenler ve son tarihleri belirliyor.
- [ ] Gizli bağımlılıklar (paylaşılan veritabanı, batch işler, raporlar) ele alındı veya açık soru olarak listelendi.
- [ ] Öneri, kendisini neyin değiştireceğini belirtiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kod hoş olmadığı için varsayılan olarak tam yeniden yazıma gitmek. Yeniden yazımlar koda gömülü iş kurallarını kaybettirir; önce platform değiştirme ve artımlı yeniden yapılandırmayla karşılaştır.
- Veriyi yok saymak: asıl monolit çoğu zaman raporların ve diğer sistemlerin paylaştığı veritabanıdır.
- Kilit kişi riskini yalnızca teknik bir konu saymak. Hangi seçenek seçilirse seçilsin başlamadan önce bilgiyi kayıt altına al.

## Örnek
Girdi: Windows Server üzerinde, desteği seneye biten .NET Framework sipariş monoliti; finans raporlarının da kullandığı paylaşılan SQL veritabanı; iki bakımcı.

Çıktıdan bir bölüm:
| Seçenek | Uygulanabilir mi? | Efor | Değer | Risk | Faydaya süre | Notlar |
|---|---|---|---|---|---|---|
| Yeniden barındır | Evet | Düşük | Düşük | Düşük | Kısa | Yalnızca işletim sistemi son tarihini kaldırır; borç kalır |
| Platform değiştir | Evet | Orta | Orta | Orta | Orta | Desteklenen runtime ve konteynerlere geçiş; önce test güvenlik ağı gerekli |
| Yeniden yapılandır (strangler) | Evet | Yüksek | Yüksek | Orta | Uzun | Önce fiyatlandırmayı ayır (en yüksek değişim hızı) `[VARSAYIM]` |

Ana seçenek: destek son tarihini karşılamak için şimdi yeniden barındır, ardından strangler ile yeniden yapılandır; gerekli akışların çoğunu karşılayan standart bir sipariş ürünü varsa karar değişir.
