---
description: Gereksinimlerden ve tasarım notlarından arc42 yapısında bir çözüm mimarisi dokümanı yazar - hedefler ve kalite gereksinimleri, kısıtlar, bağlam ve kapsam, çözüm stratejisi, yapı taşları, çalışma zamanı senaryoları, dağıtım, kesişen kavramlar, kararlar, riskler ve sözlük. Bir çözümün inceleme, devir, onay veya denetim için belgelenmesi gerektiğinde ya da mevcut tasarım yalnızca slaytlarda ve kişilerin kafasında olduğunda kullanılır.
related: c4-model, adr, nfr-to-architecture, architecture-review, technical-design-doc
prompt: Yeni kredi başvuru platformumuz için çözüm mimarisi dokümanı yaz; gereksinimler, entegrasyon listesi ve beyaz tahta notlarımız ekte.
---

# Çözüm Mimarisi Dokümanı

## Amaç
Neyin inşa edildiğini, neden bu şekilde tasarlandığını ve nasıl çalıştığını mimari kurullar, teslimat ekipleri ve operasyon için gereken düzeyde anlatan, tek ve incelenebilir bir çözüm tanımı üretmek.

## Ne zaman kullanılır
- Yeni bir çözüm veya büyük bir değişiklik mimari kurul onayı gerektirdiğinde.
- Tasarım yalnızca slaytlarda, beyaz tahtada veya kişilerin kafasında olup devredilmesi gerektiğinde.
- Denetçiler, güvenlik veya operasyon bir referans tanıma ihtiyaç duyduğunda.
- Tedarikçinin teslim ettiği bir çözümün müşteri için belgelenmesi gerektiğinde.

## Ne zaman kullanılmaz
- Geliştiriciler için tek bir özellik veya bileşen tasarımıysa `technical-design-doc` kullanılır.
- Yalnızca bir karar kaydedilecekse `adr` kullanılır.
- Yalnızca diyagram gerekiyorsa `c4-model` kullanılır.

## Girdiler
Zorunlu:
- Çözümün iş hedefi ve kapsamı.
- Fonksiyonel gereksinimler veya ana kullanım senaryoları ve bilinen kalite gereksinimleri (NFR).

İsteğe bağlı:
- Mevcut sistemler ve entegrasyonlar, kısıtlar (standartlar, platformlar, mevzuat, bütçe).
- Tasarım notları, diyagramlar, alınmış kararlar.
- Organizasyon bağlamı: ekipler, işletim modeli, barındırma.

Hedef veya gereksinimler yoksa sor. Girdisi olmayan bölümler dokümanda `[TBD]` ve bir açık soruyla kalır.

## Süreç
1. Bölüm 1 Giriş ve hedefler: en önemli 3-5 gereksinim, ölçülebilir hedefleriyle en önemli 3 kalite hedefi, paydaşlar ve beklentileri.
2. Bölüm 2 Kısıtlar: teknik, organizasyonel, yasal (ör. KVKK/GDPR, sektör düzenlemeleri), gelenekler.
3. Bölüm 3 Bağlam ve kapsam: iş bağlamı (aktörler, dış sistemler, alışverişi yapılan veri) ve teknik bağlam (kanallar, protokoller). Kod olarak bir C4 sistem bağlam diyagramı ekle.
4. Bölüm 4 Çözüm stratejisi: birkaç temel karar (mimari stil, ana teknolojiler, ayrıştırma yaklaşımı, en önemli kalite hedeflerine nasıl ulaşıldığı) ve ADR bağlantıları.
5. Bölüm 5 Yapı taşı görünümü: sorumlulukları ve arayüzleriyle seviye 1 konteynerler; seviye 2 yalnızca karmaşık parçalar için.
6. Bölüm 6 Çalışma zamanı görünümü: mimari açıdan önemli 2-4 senaryo (kritik yol, hata yolu, toplu işlem) sıralı akış olarak.
7. Bölüm 7 Dağıtım görünümü: ortamlar, düğümler, ağ bölgeleri, ölçekleme birimleri, konteynerlerin altyapıya eşlenmesi.
8. Bölüm 8 Kesişen kavramlar: güvenlik (kimlik doğrulama/yetkilendirme, gizli bilgiler, veri koruma), gözlemlenebilirlik, hata yönetimi, kalıcılık, entegrasyon, yapılandırma.
9. Bölüm 9-11: karar dizini, kalite senaryoları (uyaran/yanıt/ölçü), riskler ve teknik borç ile azaltım önlemleri.
10. Bölüm 12 Sözlük. Tutarlılık kontrolü yap: bölüm 5'teki her konteyner 7'de yer alıyor; bölüm 1'deki her kalite hedefi 4, 8 veya 10'da karşılanıyor.
11. Hedef devam ediyorsa onaydan önce `architecture-review`, zayıf kalite bölümleri için `nfr-to-architecture`, bileşen düzeyi tasarım için `technical-design-doc` öner.

## Çıktı formatı
```markdown
# Çözüm Mimarisi – <çözüm adı>
Sürüm · Durum · Yazarlar · İnceleyenler

1. Giriş ve Hedefler (gereksinim özeti, kalite hedefleri tablosu, paydaşlar)
2. Kısıtlar
3. Bağlam ve Kapsam (iş bağlamı tablosu, teknik bağlam, bağlam diyagramı)
4. Çözüm Stratejisi
5. Yapı Taşı Görünümü (konteyner tablosu: ad, sorumluluk, teknoloji, arayüzler, sahip)
6. Çalışma Zamanı Görünümü (senaryolar)
7. Dağıtım Görünümü
8. Kesişen Kavramlar
9. Mimari Kararlar (ADR dizini)
10. Kalite Gereksinimleri (kalite ağacı, senaryolar)
11. Riskler ve Teknik Borç (risk, etki, azaltım, sorumlu)
12. Sözlük
Açık Sorular
```

## Kalite kontrol listesi
- [ ] Kalite hedefleri ölçülebilir ve strateji, kavramlar veya senaryolarla izlenebilir.
- [ ] Bağlamdaki her dış sistemin protokolü ve verisiyle bir arayüzü var.
- [ ] Her konteynerin tek ve net bir sorumluluğu ve sahibi var.
- [ ] Çalışma zamanı görünümünde en az bir hata senaryosu var.
- [ ] Kişisel veri akışları ve korunmaları açıkça yazılı.
- [ ] Bilinmeyenler uydurulmadı; açık soruyla birlikte `[TBD]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Gerekçe yerine teknoloji listesi yazmak. Bölüm 4 "neden"i anlatmalı.
- Yalnızca mutlu yolu anlatmak. İnceleyenler hata, yeniden deneme ve kurtarma davranışını görmek ister.
- Açıklaması olmayan diyagramlar veya görünümler arasında tutarsız adlar.

## Örnek
Girdi: "Kredi başvurusu: web ve şube kanalları, kredi bürosu entegrasyonu, kullandırım için ana bankacılık, hedef %99,9 erişilebilirlik."

Çıktıdan bir bölüm:
| Kalite hedefi | Senaryo | Hedef |
|---|---|---|
| Erişilebilirlik | Başvuru sırasında kredi bürosu zaman aşımına uğrar | Başvuru kaydedilir, kullanıcı bilgilendirilir, asenkron yeniden denenir; başvuru gönderimi için aylık %99,9 `[SLO'yu teyit et]` |
| Güvenlik | Şube kullanıcısı başka bir şubenin başvurusuna erişir | Reddedilir ve denetim kaydına yazılır; veri şube bilgisine göre kapsamlanır |
