---
name: regression-selection
description: "Belirli bir değişiklik için neyin değiştiğini, doğrudan ve dolaylı etkisini (ortak kod, veri, entegrasyonlar, konfigürasyon), riski ve yakın dönem hata geçmişini analiz ederek regresyon test seti seçer; testleri zorunlu, önerilen ve isteğe bağlı olarak katmanlar ve kalan riski açıkça yazar. Bir sürüm, hotfix veya merge regresyon testi gerektirdiğinde ama tam set çok yavaş ya da pahalıysa veya bir değişiklikten sonra neyin yeniden test edilmesi gerektiği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: execution
  title: "Regresyon testi seçimi"
  related: "impact-analysis, risk-based-testing, test-summary-report, automation-candidate-selection, test-gap-finder"
  prompt: "İndirim hesaplama servisini değiştirdik ve PDF kütüphanesini yükselttik. Yarınki hotfix öncesi hangi regresyon testlerini koşmamız şart?"
---

# Regresyon Testi Seçimi

## Amaç
Belirli bir değişiklik için gerekçeli güven veren en küçük regresyon setini seçmek ve koşulmayanların riskini yayın kararını verenlere görünür kılmak.

## Ne zaman kullanılır
- Bir hotfix, yama veya özellik sürümü sınırlı sürede yeniden test edilmeli.
- Tam regresyon seti, sürüm penceresinin izin verdiğinden uzun sürüyor.
- Ortak bir bileşen, kütüphane veya konfigürasyon değişti ve etki alanı belirsiz.

## Ne zaman kullanılmaz
- Uzun vadede neyin otomatikleştirilmeye değer olduğuna karar verilecekse `automation-candidate-selection` kullanılır.
- Belirli bir değişiklik değil tüm ürün için test önceliklendirmesi gerekiyorsa `risk-based-testing` kullanılır.
- Koddaki eksik testleri bulmak gerekiyorsa `test-gap-finder` kullanılır.

## Girdiler
Zorunlu:
- Değişikliğin tanımı (story'ler, commit'ler, pull request'ler, konfigürasyon veya bağımlılık değişiklikleri).

İsteğe bağlı, kaliteyi artırır:
- Alan/etiket, otomasyon durumu ve süre bilgisi içeren mevcut test envanteri.
- Mimari veya bağımlılık haritası, yakın dönem hata ve olay geçmişi, kullanım analitiği.
- Test için zaman ve ortam bütçesi.

Değişiklik tanımı yoksa iste. Test envanteri yoksa test ID'leri yerine kapsanacak test alanlarını ve senaryo adlarını ver.

## Süreç
1. Her değişiklik kalemini listele ve sınıfla: kod mantığı, ortak kütüphane/bağımlılık, veri/şema, konfigürasyon/feature flag, altyapı, yalnızca arayüz.
2. Doğrudan etkiyi eşle: değişen kodu çağıran özellikler, API'ler, ekranlar ve batch işler.
3. Dolaylı etkiyi eşle: ortak bileşenlerin tüketicileri, değişikliğin okuduğu veya yazdığı veri, entegrasyonlar ve alt raporlar, güvenlik ve yetki yolları. Çıkarımla kurulan bağlantıları `[VARSAYIM]` ile işaretle.
4. Risk etkenlerini ekle: iş kritikliği, alandaki yakın dönem hata veya olaylar, değişiklik karmaşıklığı, bir bağımlılık yükseltmesinin ilk sürümü, düşük mevcut kapsam.
5. Testleri katmanlara ayırarak seç: Katman 1 zorunlu (değişikliğin kendisi ve yüksek riskli doğrudan etki), Katman 2 önerilen (dolaylı etki, yoğun kullanılan yolculuklar), Katman 3 isteğe bağlı (kalan ilişkili alanlar).
6. Değişiklikten bağımsız olarak kritik iş yolculuklarından oluşan bir smoke setini her zaman dahil et.
7. Varsa otomatik testleri tercih et; manuel testleri yalnızca otomasyonun riski kapsamadığı yerlerde listele.
8. Verilen sürelerden katman başına efor tahmin et ya da `[BİLİNMİYOR]` yaz; planı zaman bütçesine sığdır ve neyin kesildiğini belirt.
9. Kalan riski yaz: bilerek yeniden test edilmeyen alanlar ve riskin neden kabul edilebilir olduğu ya da onay gerektirdiği.
10. Kapsamı genişletme tetikleyicisini tanımla (ör. Katman 1'de herhangi bir başarısızlık, dolaylı alanlarda bulunan hatalar).
11. Kullanıcı devam ederse sonuçları raporlamak için `test-summary-report`, manuel Katman 1 testleri tekrar ediyorsa `automation-candidate-selection` öner.

## Çıktı formatı
```markdown
# Regresyon Seçimi: <sürüm / değişiklik>
## Değişiklik Kalemleri
| Değişiklik | Tür | Doğrudan etki | Dolaylı etki | Risk etkenleri |
|---|---|---|---|---|

## Seçilen Testler
| Katman | Test / alan | Gerekçe (değişiklik bağlantısı) | Otomatik/Manuel | Tahmini efor |
|---|---|---|---|---|

## Her Zaman Koşan Smoke Seti
- ...

## Seçilmeyenler ve Kalan Risk
- <alan>: <neden seçilmedi> – <risk düzeyi, onay gerekli mi?>

## Genişletme Tetikleyicileri
- ...
```

## Kalite kontrol listesi
- [ ] Her değişiklik kalemi en az bir seçili teste ya da açık bir "etkisi yok" gerekçesine bağlanıyor.
- [ ] Ortak kod, veri ve entegrasyonlar üzerinden dolaylı etkiler dikkate alınmış.
- [ ] Katmanlar belirtilen zaman bütçesine sığıyor ya da açık belirtilmiş.
- [ ] Kalan risk "geri kalan her şey" değil, somut alanları adlandırıyor.
- [ ] Çıkarımla kurulan bağımlılıklar `[VARSAYIM]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca değişen özelliği test etmek. Regresyonlar genellikle ortak kodun ve verinin tüketicilerinde ortaya çıkar.
- Bağımlılık yükseltmelerini düşük riskli saymak. Kütüphane yükseltmeleri serileştirme, tarih, PDF üretimi ve güvenlik varsayılanlarında davranışı değiştirir.
- Süreye yetişmek için testleri sessizce atlamak. Kesintiyi kaydet ve karar sahibini görünür kıl.

## Örnek
Girdi: "İndirim hesaplama servisi değişti; PDF kütüphanesi yükseltildi; hotfix yarın."

Çıktıdan bir bölüm:
| Katman | Test / alan | Gerekçe | Otomatik/Manuel |
|---|---|---|---|
| 1 | İndirim kuralları seti (yüzde, sabit, birleşik, üst limit) | Doğrudan değişiklik | Otomatik |
| 1 | Fatura ve iade faturası PDF üretimi, Türkçe karakterler, çok sayfa | Kütüphane yükseltmesi | Manuel |
| 2 | İndirimli alım sonrası iade tutarı | İndirim sonucunu kullanıyor | Otomatik |
| 2 | Aylık satış raporu toplamları | İndirimli tutarları okuyor `[VARSAYIM]` | Manuel |

Kalan risk: Sadakat puanı birikimi yeniden test edilmedi; net tutarları okuyor olabilir `[BİLİNMİYOR]`; ürün sahibi onayı gerekli.
