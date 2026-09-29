---
description: "ID, başlık, ön koşullar, test verisi, numaralı adımlar, adım bazında beklenen sonuçlar, öncelik ve gereksinim izlenebilirliği içeren ayrıntılı ve koşturulabilir test case'ler yazar. Senaryoların tekrarlanabilir manuel case'lere dönüştürülmesi gerektiğinde, koşum veya otomasyon için case hazırlanırken ya da bir özellik veya story için test case yazılması istendiğinde kullanılır."
related: test-scenarios-from-requirements, equivalence-boundary-analysis, test-data-design, test-automation-script, traceability-matrix
prompt: "Şifre sıfırlama akışı için test case yaz: e-posta bağlantısı 30 dakika geçerli, yeni şifre politikaya uymalı, eski oturumlar kapatılıyor."
---

# Test Case Yazma

## Amaç
Senaryoları, herhangi bir test uzmanının (veya otomasyon mühendisinin) koşturup aynı geçti/kaldı kararına ulaşacağı, gereksinimlere açıkça bağlanan, net ve tekrarlanabilir test case'lere dönüştürmek.

## Ne zaman kullanılır
- Senaryolar üzerinde anlaşıldı ve koşum için ayrıntılı adımlar gerekiyor.
- Bir regresyon seti, UAT paketi veya otomasyon backlog'u için düzgün yapılandırılmış case'ler gerekiyor.
- Mevcut case'ler belirsiz ("çalıştığını kontrol et") ve yeniden yazılmalı.

## Ne zaman kullanılmaz
- Yalnızca neyin test edileceğinin listesi gerekiyorsa `test-scenarios-from-requirements` kullanılır.
- BDD araç zinciri için Gherkin gerekiyorsa `bdd-feature-file` kullanılır.
- Bir alanın yapılandırılmamış keşfi gerekiyorsa `exploratory-test-charter` kullanılır.

## Girdiler
Zorunlu:
- Kapsanacak gereksinim, story veya senaryolar.

İsteğe bağlı, kaliteyi artırır:
- Arayüz ekranları veya API sözleşmesi, alan kuralları, roller, ortam bilgileri.
- Ekibin test case şablonu veya zorunlu alanları; test yönetim kuralları.

Case türetilecek bir şey yoksa iste. Bilinmeyen alan kuralları beklenen sonuçta `[BİLİNMİYOR]` ve açık soru olarak yazılır.

## Süreç
1. Kapsanacak senaryoları listele; verilmediyse önce kısaca türet (pozitif, negatif, uç).
2. Girdilerin aralığı veya kuralı olan yerlerde tasarım tekniklerini uygula: denklik sınıfları ve sınırlar, karar tabloları, durum geçişleri.
3. Her case için listede okunabilir olacak biçimde "<işlem> <koşul> <beklenen sonuç>" kalıbında başlık yaz.
4. Ön koşulları belirt: kullanıcı/rol, sistem durumu, feature flag'ler, gereken mevcut veri.
5. Somut test verisi değerleri ("geçerli e-posta" değil) yaz veya adlandırılmış bir veri setine atıf yap. Yalnızca sentetik veya maskelenmiş veri kullan.
6. Adımları, fiille başlayan, satır başına bir tane olmak üzere tekil ve gözlemlenebilir kullanıcı veya sistem işlemleri olarak yaz.
7. Doğrulanabilir sonucu olan her adım için beklenen sonuç yaz; mesajları, durum değişikliklerini, kalıcı veriyi, yan etkileri (e-posta, denetim kaydı, olay) dahil et.
8. Case ortak veriyi değiştiriyorsa son koşulları veya temizlik adımlarını ekle.
9. Önceliği (riskten), türü (fonksiyonel, negatif, sınır...) ve izlenebilirliği (gereksinim/kriter ID'leri) belirle.
10. Otomasyona uygunluğu işaretle (Evet / Sonra / Hayır, gerekçesiyle).
11. Bağımsızlığı gözden geçir: her case başka bir case'in sonucuna dayanmadan tek başına koşabilmeli.
12. Çıkarımla yazılan beklenen sonuçları `[VARSAYIM]` ile işaretle; kullanıcı devam ederse otomasyona uygun case'ler için `test-automation-script`, gereksinim bağlantısı için `traceability-matrix` öner.

## Çıktı formatı
```markdown
### TC-<nnn>: <başlık>
| Alan | Değer |
|---|---|
| İzlendiği kaynak | <REQ / AC ID'leri> |
| Öncelik / Tür | <Y/O/D> / <tür> |
| Ön koşullar | <rol, durum, veri> |
| Test verisi | <somut değerler veya veri seti adı> |
| Otomasyon | <Evet / Sonra / Hayır – gerekçe> |

| # | Adım | Beklenen sonuç |
|---|---|---|
| 1 | <fiil + işlem> | <gözlemlenebilir sonuç> |

Son koşullar / temizlik: <...>
```

## Kalite kontrol listesi
- [ ] Her case tek bir amacı doğruluyor ve net bir geçti/kaldı kararı var.
- [ ] Beklenen sonuçlar somut (tam mesaj, değer, durum); asla "doğru çalışır" değil.
- [ ] Test verisi somut ve gerçek kişisel veri içermiyor.
- [ ] Yalnızca mutlu yollar değil, negatif ve sınır case'leri de var.
- [ ] Her case en az bir gereksinime veya kritere izlenebiliyor.
- [ ] Case'ler bağımsız ve ön koşullarını belirtiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Pek çok kontrolü tek uzun bir case'te birleştirmek. Hata sorunun yerini gösterecek biçimde böl.
- Süresi dolan verileri (tarihler, token'lar) sabit yazmak. Göreli veri ("bugün + 31 gün") veya hazırlık adımları kullan.
- Bildirim, denetim kaydı veya bağlı sistem mesajları gibi yan etki kontrollerini atlamak.

## Örnek
Girdi: "Şifre sıfırlama: bağlantı 30 dakika geçerli, politikaya uygun yeni şifre, eski oturumlar kapatılır."

Çıktıdan bir bölüm:
### TC-004: 30 dakikadan sonra kullanılan sıfırlama bağlantısı reddedilir
| Ön koşullar | Aktif kullanıcı `qa.user01`, sıfırlama T0 anında istendi |
| Test verisi | T0'da üretilen bağlantı; sistem saati ayarlanır veya T0 + 30 dk + 1 sn beklenir |

| 1 | Sıfırlama bağlantısını T0 + 30:01'de aç | "Bağlantının süresi doldu" mesajı gösterilir; şifre alanı yok `[BİLİNMİYOR: tam metin]` |
| 2 | Eski şifreyle giriş yapmayı dene | Giriş başarılı (şifre değişmedi) |
