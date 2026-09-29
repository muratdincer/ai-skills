---
description: "Bir sürüm, proje veya özellik seti için test öğelerini, kapsamı, yaklaşımı, ortamları, takvimi, rolleri, giriş/çıkış ve askıya alma kriterlerini, teslimatları ve riskleri ISO/IEC/IEEE 29119-3 ile uyumlu biçimde ele alan bir test planı yazar. Bir sürüm veya proje için üzerinde anlaşılmış test kapsamı ve takvimi gerektiğinde ya da test planı dokümanı istendiğinde kullanılır."
related: test-strategy, risk-based-testing, release-quality-gate, test-summary-report, uat-plan
prompt: "Hasar portalının 4.2 sürümü için test planı hazırla: yeni doküman yükleme, revize onay akışı ve iki hata düzeltmesi var. Code freeze üç hafta sonra."
---

# Test Planı Yazma

## Amaç
Test başlamadan önce neyin, nasıl, nerede, kim tarafından, ne zaman test edileceği ve "bitti"nin ne anlama geldiği konusunda anlaşmak. İyi bir plan, kapsam ödünlerini ve kalan riski sürüm kararında değil, erken aşamada görünür kılar.

## Ne zaman kullanılır
- Bir sürüm, proje veya önemli bir özellik seti test hazırlığına giriyor.
- Birden fazla ekip veya bir tedarikçi testi paylaşıyor ve ortak bir kapsam ile takvime ihtiyaç var.
- Sözleşme, denetim veya düzenleyici dokümante edilmiş bir plan bekliyor (ISO/IEC/IEEE 29119-3 yapısı).

## Ne zaman kullanılmaz
- Kurum veya ürün genelindeki yaklaşım henüz tanımlı değilse önce `test-strategy` kullanılır.
- Yalnızca iş birimi katılımcılarıyla kullanıcı kabul planlaması gerekiyorsa `uat-plan` kullanılır.
- Yük/stres planlaması gerekiyorsa `performance-test-plan` kullanılır.

## Girdiler
Zorunlu:
- Teslim edilenler: sürüm kapsamı, özellikler, değişiklikler veya gereksinim listesi.
- Önemli tarihler veya kısıtlar (hedef sürüm tarihi, freeze, ortam erişilebilirliği) ya da bunların olmadığının teyidi.

İsteğe bağlı, kaliteyi artırır:
- Geçerli test stratejisi, risk değerlendirmesi, önceki test özet raporları.
- Ekip üyeleri ve müsaitlikleri, ortam ve veri durumu, diğer ekiplere bağımlılıklar.

Teslimat kapsamı yoksa iste. Eksik tarihler tahmin edilmez, `[TBD]` olarak yazılır.

## Süreç
1. Test öğelerini (bileşenler, sürümler, build'ler), test edilecek ve edilmeyecek özellikleri belirle; her kapsam dışı bırakma için gerekçe yaz.
2. Özellik bazında risk değerlendirmesini al veya hızlıca yap; derinliği (kapsamlı / standart / smoke) buna göre belirle. Ayrıntı gerekiyorsa `risk-based-testing`e atıf yap.
3. Özellik bazında yaklaşımı tanımla: test seviyeleri ve türleri, tasarım teknikleri, manuel/otomatik, regresyon kapsamı.
4. Gereken ortamları, test verisini ve entegrasyonları hazır olma tarihleri ve sorumlularıyla belirt.
5. Giriş kriterlerini (build dağıtıldı, smoke geçti, test verisi hazır, gereksinimler baz alındı) ve çıkış kriterlerini (koşum yüzdesi, kritik testlerde geçme oranı, açık Kritik/Yüksek hata olmaması ya da onaylı istisna, yüksek risklerin kapsanması) tanımla.
6. Askıya alma ve devam etme kriterlerini tanımla (ör. ana akışta engelleyici hata, ortamın yarım günden uzun kapalı kalması).
7. Takvimi sürüm tarihinden geriye doğru kur: hazırlık, koşum döngüleri, regresyon, düzeltme doğrulama, raporlama. Tampon ekle ve kritik yolu belirt.
8. Rolleri ata: test yöneticisi/lideri, test uzmanları, düzeltmeler için geliştiriciler, UAT için iş birimi, ortam sorumlusu.
9. Teslimatları listele: test case'ler, koşum kayıtları, hata raporları, günlük durum, test özet raporu.
10. Planlama risklerini (ürün riskleri değil) önlem ve B planıyla listele: geciken build'ler, paylaşılan ortamlar, kilit kişi bağımlılığı.
11. Bilinmeyenleri işaretle; açık soruları ve gereken onayları topla.

## Çıktı formatı
```markdown
# Test Planı: <sürüm / proje>
Sürüm: <x.y> | Hazırlayan: <ad> | Onaylayanlar: <adlar veya [TBD]>

## 1. Test Öğeleri ve Kapsam
| Özellik / öğe | Kapsamda mı | Derinlik | Kapsam dışıysa gerekçe |
## 2. Yaklaşım
| Özellik | Seviyeler | Türler | Teknikler | Manuel / Otomatik |
## 3. Ortamlar ve Test Verisi
| İhtiyaç | Sorumlu | Hazır olma tarihi | Durum |
## 4. Giriş, Çıkış, Askıya Alma ve Devam Kriterleri
## 5. Takvim
| Aktivite | Başlangıç | Bitiş | Sorumlu | Bağımlılık |
## 6. Roller ve Sorumluluklar
## 7. Teslimatlar ve Raporlama Sıklığı
## 8. Planlama Riskleri ve B Planları
| Risk | Olasılık | Etki | Önlem | B planı |
## 9. Açık Sorular ve Onaylar
```

## Kalite kontrol listesi
- [ ] Kapsamdaki her özelliğin yaklaşımı ve derinliği var; her kapsam dışı bırakmanın gerekçesi var.
- [ ] Çıkış kriterleri ölçülebilir ve sürüm kalite kapısıyla tutarlı.
- [ ] Takvimde en az bir regresyon döngüsü ve düzeltme doğrulama süresi var.
- [ ] Ortam ve veri hazırlığının sorumlusu ve tarihi var ya da `[TBD]` olarak işaretli.
- [ ] Hiçbir isim, tarih veya sayı uydurulmadı.
- [ ] Planlama riskleri ürün risklerinden ayrı.

## Sık yapılan hatalar
- "Tüm testler geçti" gibi çıkış kriterleri. Gerekçeli istisnalara izin ver ve karar sahibini belirt.
- Koşumu yalnızca bir kez planlamak. Düzeltme-yeniden test ve regresyon döngülerini planla.
- Değişen bileşenlerin fonksiyonel olmayan ihtiyaçlarını atlamak (yeni yüklemenin performansı, yeni ekranların erişilebilirliği).

## Örnek
Girdi: "Hasar portalı 4.2: doküman yükleme, revize onay akışı, iki hata düzeltmesi; code freeze üç hafta sonra."

Çıktıdan bir bölüm:
- Derinlik: Onay akışı = kapsamlı (durum geçişleri, yetkilendirme); doküman yükleme = kapsamlı (dosya türleri, boyut sınırları, zararlı yazılım taraması); hata düzeltmeleri = yeniden test + hedefli regresyon.
- Çıkış: Kritik testlerin %100'ü koşuldu, açık Kritik hata 0, Yüksek hatalar yalnızca ürün sahibi istisnasıyla.
- Planlama riski: Test ortamında tarama servisi teyit edilmedi `[TBD: ortam sorumlusu]`.
