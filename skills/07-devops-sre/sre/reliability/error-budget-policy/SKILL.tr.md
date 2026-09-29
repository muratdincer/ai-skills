---
description: "Tanımlı bütçe tüketim eşiklerinde geliştirme ve operasyon ekiplerinin ne yapması gerektiğini (sürüm kısıtları, güvenilirlik çalışması, olay sonrası analiz gereksinimleri), istisnalara kimin karar verdiğini ve anlaşmazlıkların nasıl eskale edildiğini belirten bir hata bütçesi politikası yazar. SLO'lar var ama hiçbir sonucu yoksa, özellik baskısı sürekli güvenilirliği ezip geçiyorsa ya da hata bütçesi bittiğinde ne olacağı sorulduğunda kullanılır."
related: "slo-definition, alert-design, postmortem, release-quality-gate, go-no-go"
prompt: "Checkout SLO'muz 28 günde %99,9 ve bütçenin %80'ini ilk haftada harcadık. Ürün ve mühendislik liderlerinin imzalayabileceği bir hata bütçesi politikası yaz."
---

# Hata Bütçesi Politikası Yazma

## Amaç
SLO'ları, özellik hızı ile güvenilirlik arasında denge kuran ve ürün ile mühendislik tarafından önceden imzalanan bir karar kuralına dönüştürmek. Böylece kötü giden bir ayda konuşma politikayı müzakere etmek değil, uygulamak üzerine olur.

## Ne zaman kullanılır
- SLO'lar var ama kaçırıldıklarında kimse davranışını değiştirmiyorsa.
- Ürün ve mühendislik olaylardan sonra sürümleri dondurma konusunda sürekli tartışıyorsa.
- Bir servis, bütçe politikası gerektiren SRE veya platform desteğine alınırken.

## Ne zaman kullanılmaz
- SLI ve SLO'ların kendisi henüz tanımlanmadıysa `slo-definition` kullanılır.
- İhtiyaç hızlı tükenme için sayfalama kurallarıysa `alert-design` kullanılır.
- Soru belirli bir sürüm için tek seferlik yayına alma kararıysa `go-no-go` kullanılır.

## Girdiler
Zorunlu:
- Hedefleri ve pencereleriyle SLO'lar.
- İlgili ekipler: servis sahipleri, ürün sahibi, operasyon/SRE, karar vericiler.

İsteğe bağlı, kaliteyi artırır:
- Mevcut ve geçmiş bütçe tüketimi, yakın zamandaki olaylar.
- Sürüm sıklığı ve dağıtım mekanizması ("dondurma"nın pratikte ne anlama geldiğini değerlendirmek için).
- Kurumun eskalasyon yolu, mevcut değişiklik politikaları, bağımlılıkların SLO'ları.

SLO yoksa dur ve `slo-definition` öner. Eksik isimler veya roller `[TBD]` olur.

## Süreç
1. Politikanın amaçlarını ve kapsamını belirt: servisler, SLO'lar, pencere ve bütçenin değişiklik için harcanmak üzere var olduğu ilkesi.
2. Tüketim eşiklerini (ör. pencerede bütçenin %50'si, %75'i, %100'ü) ve bir hızlı tükenme koşulunu, her biri için zorunlu aksiyonlarla tanımla.
3. Her eşik için geliştirme (sürüm kısıtları, zorunlu incelemeler, yalnızca güvenilirlik veya güvenlik düzeltmeleri), operasyon (ek izleme, kapasite) ve ürün (backlog'u güvenilirlik maddelerine göre yeniden önceliklendirme) aksiyonlarını belirt.
4. "Sürüm dondurma"nın neye izin verdiğini tanımla: güvenlik yamaları, tükenmeyi azaltan düzeltmeler, yasal değişiklikler; istisnaları kimin onaylayacağını belirt.
5. Tüketimi ilişkilendir: ekibin kontrolü dışındaki bağımlılıkların, planlı bakımın veya yanlış yapılandırılmış SLI'ın tükettiği bütçeyi hariç tut veya ayrı ele al; ilişkilendirme anlaşmazlıklarının nasıl çözüleceğini belirt.
6. Olay sonrası analiz gereksinimini koy: tek başına bütçenin belirtilen bir payından `[TBD]` fazlasını tüketen her olay, aksiyonları sonraki iterasyonda önceliklendirilen bir postmortem gerektirir.
7. Kısıtlamaların çıkış kriterlerini (bütçe toparlandı, aksiyonlar tamamlandı) ve sürekli kullanılmayan bütçe durumunu (daha sıkı SLO veya daha hızlı sürümler düşün) tanımla.
8. Anlaşmazlık için eskalasyonu ve imzacıları tanımla; politikanın kendisi için gözden geçirme sıklığı belirle.
9. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa burn-rate sayfalaması için `alert-design`, bütçe tüketen olaylar için `postmortem` veya sürüm kısıtını kodlamak için `release-quality-gate` öner.

## Çıktı formatı
```markdown
# Hata Bütçesi Politikası: <servis(ler)>
Kapsanan SLO'lar: <liste> · Pencere: <N gün> · Yürürlük: <tarih> · Gözden geçirme: <sıklık>
İmzacılar: <ürün lideri>, <mühendislik lideri>, <SRE/operasyon lideri> (bilinmiyorsa [TBD])

## Amaçlar ve Kapsam
## Eşikler ve Aksiyonlar
| Tüketilen bütçe | Geliştirme | Operasyon | Ürün | İstisna onaylayıcısı |
|---|---|---|---|---|
| ≥ %50 | ... | ... | ... | ... |
| ≥ %75 | ... | ... | ... | ... |
| ≥ %100 | ... | ... | ... | ... |
| Hızlı tükenme | ... | ... | ... | ... |

## Dondurma Sırasında İzin Verilenler
## Tüketimin İlişkilendirilmesi ve Hariç Tutulanlar
## Olay Sonrası Analiz Gereksinimi
## Çıkış Kriterleri
## Eskalasyon ve Anlaşmazlıklar
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her eşikte her ekip için "dikkatli olun" değil, somut ve doğrulanabilir aksiyonlar var.
- [ ] Dondurma istisnaları ve onaylayıcıları tanımlandı.
- [ ] Bağımlılık kaynaklı tüketimin ilişkilendirilmesi ele alındı.
- [ ] Çıkış kriterleri ve kullanılmayan bütçe kuralı var.
- [ ] İmzacılar arasında hem ürün hem mühendislik karar vericileri var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Politikayı yalnızca SRE'nin yazması. Ürün onayı olmadan ilk son tarihte çiğnenir.
- Tek tetikleyici olarak %100'ü görmek. Daha erken eşikler ekibin dondurmadan önce harekete geçmesini sağlar.
- Cezalandırıcı çerçeve. Bütçe risk seçmek için bir araçtır; politika asla suç atamamalıdır.

## Örnek
Girdi: "Checkout %99,9 / 28 gün; iki kötü dağıtım sonrası ilk haftada %80 tükendi."

Çıktıdan bir bölüm:
| Tüketilen bütçe | Geliştirme | Ürün | İstisna onaylayıcısı |
|---|---|---|---|
| ≥ %75 | Yalnızca flag arkasında ve canary ile değişiklik; her sürüm için geri dönüş prova edilmiş | İki postmortem'in en önemli güvenilirlik maddeleri sonraki iterasyona girer | Mühendislik lideri |
| ≥ %100 | Bütçe toparlanana veya aksiyonlar tamamlanana kadar güvenlik ve tükenmeyi azaltan düzeltmeler dışında dondurma | Özellik taahhütleri yeniden planlanır | Ürün + mühendislik lideri birlikte |
