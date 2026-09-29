---
description: "Semantic Versioning 2.0.0 kurallarını bir değişiklik listesine uygulayarak sonraki sürüm numarasını belirler: her değişikliği public API'ye göre sınıflandırır, gizli kırıcı değişiklikleri yakalar, 0.x, pre-release ve build metadata durumlarını ele alır. Bir kütüphane, API, SDK, paket veya servis yayına çıkmak üzereyken hangi sürüm olması gerektiği ya da bir değişikliğin major artış gerektirip gerektirmediği sorulduğunda kullanılır."
related: "release-notes, changelog-entry, api-deprecation-plan, api-design-review, release-plan"
prompt: "Mevcut sürüm 2.4.1. Değişiklikler: isteğe bağlı 'locale' parametresi eklendi, INVALID_TOKEN hata kodu TOKEN_INVALID olarak değiştirildi, yuvarlama hatası düzeltildi. Sonraki sürüm ne olmalı?"
---

# Sürüm Numarası Belirleme

## Amaç
SemVer 2.0.0'ın gerektirdiği gibi her değişikliği tanımlı public API'ye göre sınıflandırarak, tüketicilere yükseltmenin güvenli olup olmadığını doğru anlatan bir sürüm numarası vermek.

## Ne zaman kullanılır
- Tüketicisi olan bir kütüphane, SDK, paket, API veya bileşen yayına çıkmak üzereyken.
- Ekip bir değişikliğin kırıcı olup olmadığı konusunda anlaşamadığında.
- Bir proje 0.x'ten 1.0.0'a geçerken veya pre-release'ler (alpha, beta, rc) getirirken.

## Ne zaman kullanılmaz
- Değişiklikleri kullanıcılara anlatan notlar gerekiyorsa `release-notes` veya `changelog-entry` kullanılır.
- Bir API'yi veya sürümü emekliye ayırma planı gerekiyorsa `api-deprecation-plan` kullanılır.
- Ürün uyumluluk vaadi olmayan takvim veya pazarlama sürümleri kullanıyorsa SemVer kuralları uygulanmaz; bunu belirt.

## Girdiler
Zorunlu:
- Mevcut sürüm.
- O sürümden bu yana yapılan değişikliklerin listesi (commit'ler, pull request'ler, changelog, diff özeti).

İsteğe bağlı, kaliteyi artırır:
- Public API tanımı (dışa açık tipler, endpoint'ler, CLI parametreleri, yapılandırma anahtarları, event şemaları, tüketicilerin okuduğu veritabanı view'ları).
- Desteklenen çalışma zamanı/platform sürümleri, pre-release niyeti, proje gelenekleri.

Mevcut sürüm veya değişiklik listesi yoksa sor. Public API tanımlı değilse varsayılan sınırı `[VARSAYIM]` olarak belirt.

## Süreç
1. Public API sınırını belirle; sınırın dışındaki değişiklikler (iç yapı, testler, build) tüketiciye görünür davranışı değiştirmedikçe numarayı etkilemez.
2. Her değişikliği sınıflandır: MAJOR (uyumsuz değişiklik), MINOR (geriye uyumlu yeni işlevsellik veya kullanımdan kaldırma bildirimi), PATCH (geriye uyumlu hata düzeltmesi), YOK (tüketiciye görünür etkisi yok).
3. Gizli kırıcı değişiklikleri ara: yeniden adlandırılan veya kaldırılan üyeler, yeni zorunlu parametre veya yapılandırma, değişen varsayılanlar, daraltılan kabul edilen girdi, katı istemcilerin reddettiği genişletilmiş çıktı (ör. yeni enum değeri), değişen hata kodları veya exception tipleri, değişen serileştirme, bırakılan platform veya çalışma zamanı desteği, sıkılaştırılmış doğrulama, API'de açığa çıkan geçişli bağımlılıkların major artışları.
4. Güvenilen davranışı değiştiren hata düzeltmelerini potansiyel kırıcı say; sessizce patch demek yerine karar için işaretle.
5. En yüksek sınıflandırmayı al: herhangi bir MAJOR → major'ı artır, minor ve patch'i sıfırla; yoksa herhangi bir MINOR → minor'ı artır, patch'i sıfırla; yoksa PATCH.
6. 0.x kurallarını uygula: 1.0.0'dan önce her şey değişebilir; proje 0.x'te kırıcı değişiklikler için minor artırma geleneğini izliyorsa bunu açıkça belirt.
7. Pre-release ve build metadata'yı ele al: pre-release (`-alpha.1`, `-rc.2`) yayından daha düşük önceliğe sahiptir; build metadata (`+build.5`) öncelik hesabında yok sayılır.
8. Major artış istenmiyorsa azaltma yolları öner: eski üyeyi deprecated olarak koru, yeniden adlandırmak yerine ekle, yeni parametreyi isteğe bağlı yap.
9. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa değişiklikleri belgelemek için `release-notes` veya `changelog-entry`, kaldırmalar planlanıyorsa `api-deprecation-plan` öner.

## Çıktı formatı
```markdown
# Sürüm Kararı: <bileşen>
Mevcut: <x.y.z> → **Önerilen: <x.y.z>**

## Public API Sınırı
<neyin public sayıldığı; verilmediyse [VARSAYIM]>

## Değişiklik Sınıflandırması
| Değişiklik | Sınıf | Gerekçe |
|---|---|---|

## Gerekçe
<en yüksek sınıf belirler; kilit kırıcı değişiklik(ler)>

## Major Artıştan Kaçınma Alternatifleri (gerekirse)
- ...

## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Public API sınırı belirtildi ya da varsayım olarak işaretlendi.
- [ ] Her değişiklik tüketici etkisine bağlı bir gerekçeyle sınıflandırıldı.
- [ ] Gizli kırıcı değişiklikler (hata kodları, varsayılanlar, enum'lar, platform desteği) kontrol edildi.
- [ ] Sıfırlama kuralları doğru uygulandı (major'da minor ve patch 0; minor'da patch 0).
- [ ] Pre-release ve build metadata SemVer 2.0.0 önceliğine uyuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bir yeniden adlandırmaya "refactoring" deyip patch olarak yayınlamak. Tüketiciler o isme referans veriyorsa kırıcıdır.
- Sürümü pazarlama aracı olarak görmek ("büyük sürüm, o yüzden 3.0"). Numara büyüklüğü değil uyumluluğu anlatır.
- Tüketicilerin kapsamlı eşleştirme veya katı deserialization kullanıp kullanmadığını kontrol etmeden minor'da enum değeri eklemek.

## Örnek
Girdi: "2.4.1 → isteğe bağlı 'locale' parametresi eklendi; INVALID_TOKEN hata kodu TOKEN_INVALID oldu; yuvarlama hatası düzeltildi."

Çıktıdan bir bölüm:
| Değişiklik | Sınıf | Gerekçe |
|---|---|---|
| İsteğe bağlı `locale` parametresi | MINOR | Geriye uyumlu yeni yetenek |
| Hata kodu yeniden adlandırma | MAJOR | `INVALID_TOKEN` ile eşleştirme yapan istemciler bozulur |
| Yuvarlama düzeltmesi | PATCH | `[TEYİT ET]` hiçbir tüketici eski yuvarlamaya güvenmiyor |

Önerilen: **3.0.0**. Alternatif: bir kullanımdan kaldırma dönemi boyunca iki kodu birlikte döndür ve **2.5.0** yayınla.
