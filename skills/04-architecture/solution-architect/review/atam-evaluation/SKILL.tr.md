---
name: atam-evaluation
description: "Architecture Tradeoff Analysis Method (ATAM) örnek alınarak bir değerlendirmeyi planlar ve belgeler; iş sürücülerini, önceliklendirilmiş kalite niteliği fayda ağacını, mimari yaklaşımların öncelikli senaryolara göre analizini ve ortaya çıkan hassasiyet noktalarını, ödünleşim noktalarını, riskleri, risk olmayanları ve risk temalarını üretir. Önemli bir mimari taahhüt öncesinde paydaşlarla değerlendirilecekse, kalite hedefleri çelişiyorsa veya bağımsız, yapılandırılmış bir değerlendirme isteniyorsa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: solution-architect
  area: review
  title: "ATAM tarzı değerlendirme"
  related: "nfr-to-architecture, architecture-review, trade-off-analysis, workshop-plan, adr"
  prompt: "Olay güdümlü ödeme platformumuz için ATAM tarzı bir değerlendirme hazırla; temel kaygılar gecikme, iki veri merkezinde erişilebilirlik ve denetlenebilirlik."
---

# ATAM Tarzı Değerlendirme

## Amaç
Mimari kararların birbiriyle yarışan kalite hedeflerini nasıl etkilediğini ortaya çıkarmak. Böylece paydaşlar mimariyi, hassasiyet noktalarını, ödünleşimlerini ve risklerini canlıda keşfetmek yerine bilerek taahhüt eder.

## Ne zaman kullanılır
- Yüksek riskli bir mimari taahhüt edilmek üzereyken (fonlama, satın alma, geliştirme başlangıcı).
- Kalite hedefleri çeliştiğinde (ör. gecikme ve denetlenebilirlik, erişilebilirlik ve tutarlılık) ve paydaşlar anlaşamadığında.
- Bir kurul veya müşteri bağımsız, yapılandırılmış bir değerlendirme istediğinde.

## Ne zaman kullanılmaz
- Hızlı bir uyum ve eksiksizlik kontrolü yeterliyse `architecture-review` kullanılır.
- Kalite senaryoları henüz tanımlanmamış ve paydaşlar erişilebilir değilse önce `nfr-to-architecture` kullanılır.
- Seçenekler arasında yalnızca tek bir karar gerekiyorsa `trade-off-analysis` veya `adr` kullanılır.

## Girdiler
Zorunlu:
- Mimari tanımı (görünümler ve temel kararlar) veya sunum yapacak mimara erişim.
- İş sürücüleri veya bunları ifade edebilecek kişiler.

İsteğe bağlı:
- Mevcut kalite senaryoları/NFR'ler, paydaş listesi, kısıtlar, önceki değerlendirme çıktıları.
- Oturum formatı kısıtları (ayrılan gün sayısı, uzaktan/yüz yüze).

Canlı yürütülüyorsa her seferinde tek odaklı soru ya da en fazla beş soruluk kısa bir grup sor. Girdiler doküman olarak geldiyse sürücüleri ve yaklaşımları onlardan çıkar, çıkarım yaptığın her şeyi etiketle.

## Süreç
1. Değerlendirmeyi planla: değerlendirme ekibi rolleri (lider, yazıcı, soru soran), paydaş grupları (mimarlar, geliştiriciler, operasyon, iş birimi, güvenlik), gündem ve çıktılar; metodolojiden bağımsız tut.
2. İş sürücülerini topla: hedefler, kısıtlar, temel kalite nitelikleri ve sponsor için "başarının" anlamı.
3. Mimariyi topla: ana görünümler ve kullanılan mimari yaklaşımlar (ör. event sourcing, aktif-aktif, CQRS, devre kesiciler).
4. Fayda ağacını kur: Fayda → kalite niteliği → ayrıntılandırma → somut senaryo; her biri (Y/O/D önem, Y/O/D zorluk) ile derecelendirilir.
5. Paydaşlarla ek senaryolar üret (kullanım, büyüme, keşif) ve oylamayla önceliklendir; fayda ağacıyla birleştir.
6. Öncelikli her senaryoyu analiz et: hangi yaklaşımlar yanıt veriyor, nasıl, hangi kanıtla; nitelik bazında sorgulayıcı sorular sor (ör. "ikincil site N saniye geride kalırsa ne olur?").
7. Her analiz için kaydet: hassasiyet noktaları (tek bir niteliği güçlü etkileyen parametreler), ödünleşim noktaları (birden çok niteliği zıt yönde etkileyenler), riskler ve risk olmayanlar (gerekçesiyle sağlam kararlar).
8. Riskleri risk temalarında grupla ve her temayı tehdit ettiği iş sürücüsüne bağla.
9. Sponsor için özetle: başlıca risk temaları, önerilen azaltımlar veya ek analiz ve ADR gerektiren kararlar.
10. Hedef devam ediyorsa alınan kararlar için `adr`, takip kontrolleri için `architecture-review` veya erişilebilirlikle ilgili risk temaları için `resilience-review` öner.

## Çıktı formatı
```markdown
# ATAM Tarzı Değerlendirme: <sistem> – <tarih>
## İş Sürücüleri
## Mimari Yaklaşımlar
## Fayda Ağacı
| Kalite niteliği | Ayrıntılandırma | Senaryo | Önem | Zorluk |
|---|---|---|---|---|
## Senaryo Analizleri
### <senaryo ID>: <senaryo>
- İlgili yaklaşımlar: ...
- Hassasiyet noktaları: ...
- Ödünleşim noktaları: ...
- Riskler: ...
- Risk olmayanlar: ...
## Risk Temaları
| Tema | Riskler | Etkilenen iş sürücüsü | Önerilen aksiyon |
|---|---|---|---|
## Açık Sorular ve Takip İşleri
```

## Kalite kontrol listesi
- [ ] Her senaryo somut (uyaran, ortam, ölçülebilir yanıt); bir kalite sıfatı değil.
- [ ] Öncelikli senaryoların (Y,Y ve Y,O) tamamı analiz edildi veya açıkça ertelendi.
- [ ] Hassasiyet ve ödünleşim noktaları parametreyi ve etkilenen nitelikleri adlandırıyor.
- [ ] Yalnızca riskler değil, risk olmayanlar da gerekçesiyle kaydedildi.
- [ ] Risk temaları iş sürücülerine bağlı.
- [ ] Paydaş ifadeleri değerlendirici çıkarımlarından ayırt edilebiliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Değerlendirmeyi tasarım oturumuna çevirmek. Sorunları kaydet ve ilerle; yeniden tasarım sonra gelir.
- Senaryoları yalnızca mimarlara yazdırmak. Operasyon ve iş senaryoları farklı riskleri ortaya çıkarır.
- Onlarca bağımsız risk listelemek. Sponsorun harekete geçebileceği temalarda grupla.

## Örnek
Girdi: "Olay güdümlü ödeme platformu; kaygılar: gecikme, iki veri merkezi, denetlenebilirlik."

Çıktıdan bir bölüm:
| Nitelik | Ayrıntılandırma | Senaryo | Önem | Zorluk |
|---|---|---|---|---|
| Erişilebilirlik | Site arızası | Birincil veri merkezi tepe yükte çöker; ödemeler ikincilden devam eder, yetkilendirilmiş ödeme kaybolmaz; RPO `[TBD]` | Y | Y |
| Denetlenebilirlik | İzlenebilirlik | Denetçi bir ödemenin tüm geçmişini ister; olay deposundan 1 saatten kısa sürede üretilir | Y | O |

Ödünleşim noktası: veri merkezleri arası asenkron replikasyon gecikmesi – yazma gecikmesini düşürür, failover'da olay kaybı riskini artırır (erişilebilirlik ve denetlenebilirlik).
