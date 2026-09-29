---
description: "Başarısız bir CI/CD çalıştırmasını logları ve bağlamı üzerinden analiz eder; hatayı sınıflandırır (kod, test, kararsız test, bağımlılık, altyapı, yapılandırma, kimlik bilgisi), en olası nedeni kanıtıyla belirler, çözüm ve önleme adımı önerir. Build, test, tarama veya dağıtım işi başarısız olduğunda ve log ya da hata metni paylaşıldığında kullanılır."
related: "pipeline-design, flaky-test-analysis, log-analysis, stack-trace-analysis, dependency-upgrade"
prompt: "Main branch hattımız bu sabahtan beri Docker build adımında kırılıyor, log ekte. Sorun ne ve nasıl düzeltiriz?"
---

# Hat Hatası Analizi

## Amaç
Logdaki gürültüyü gerçek nedenden ayırarak kırmızı hattı hızla yeşile döndürmek ve aynı hatanın tekrarlanmasını önleyen bir düzeltme bırakmak.

## Ne zaman kullanılır
- Build, test, tarama, paketleme veya dağıtım işi başarısız olduğunda ve log mevcut olduğunda.
- Hat aralıklı olarak kırılıyor ve ekip kararsızlıktan veya altyapıdan şüpheleniyorsa.
- Bir bağımlılık, runner imajı veya yapılandırma değişikliğinden sonra hat bozulduysa.

## Ne zaman kullanılmaz
- Tek bir hata değil, genel olarak kararsız bir test paketi söz konusuysa `flaky-test-analysis` kullanılır.
- Hata hatta değil, üretimde uygulamadaysa `log-analysis` veya `incident-response` kullanılır.
- Hattın yeniden tasarlanması gerekiyorsa `pipeline-design` kullanılır.

## Girdiler
Zorunlu:
- Başarısız işin logu (en azından ilk hatadan sona kadar) veya tam hata metni.

İsteğe bağlı, kaliteyi artırır:
- Başarısız aşamanın hat tanımı, son yeşil çalıştırma ve o zamandan beri değişenler (commit'ler, bağımlılık güncellemeleri, runner imajı, secret rotasyonu).
- Hatanın yeniden denemede veya yerelde tekrarlanıp tekrarlanmadığı.

Log veya hata metni yoksa iste. Yalnızca iş adından tahmin yürütme.

## Süreç
1. Son satırı değil, ilk gerçek hatayı bul. Zincirleme hataları ve genel "exit code 1" sarmalayıcısını atla.
2. Hatayı sınıflandır: derleme/kod, test doğrulaması, kararsız/zamanlama, bağımlılık çözümleme, ağ/registry, altyapı/runner (disk, bellek, zaman aşımı), yapılandırma/değişkenler, kimlik bilgisi/yetki, kota/rate limit, politika kapısı (tarama, kapsam).
3. Değişiklikle ilişkilendir: son yeşil çalıştırmayla karşılaştır. Farkları listele (commit'ler, lockfile, base image tag'i, runner sürümü, secret'lar, dış servis).
4. Olasılığa göre sıralı 1-3 hipotez kur; her biri için destekleyen log kanıtını ve onu neyin çürüteceğini yaz.
5. En güçlü hipotez için en ucuz ayırt edici kontrolü öner (debug log ile yeniden çalıştırma, önceki sürümü sabitleme, aynı imajla yerelde çalıştırma, kimlik bilgisinin süresini kontrol etme).
6. Çözümü öner: anında blokaj kaldırma (revert, sabitleme, gerekçeli yeniden deneme) ve kalıcı çözüm (kod, yapılandırma, bağımlılık değişikliği).
7. Yeniden deneme kararını ver: yalnızca sınıf geçiciyse ve kanıt bunu gösteriyorsa kabul edilir. Aksi halde yeniden denemeyi çözüm olarak önerme.
8. Önleme öner: sabitleme, önbellek, yeni bir kontrol, kararsız testi kayıt açarak karantinaya alma, kimlik bilgisi süre dolumu için alarm.
9. Güvenlik konularını not et: log bir secret'ı açığa çıkarıyorsa rotasyon ve log maskelemesi öner.

## Çıktı formatı
```markdown
# Hat Hatası Analizi: <hat / iş / çalıştırma>
- Başarısız adım: <adım>
- İlk hata: `<alıntılanan satır>`
- Sınıf: <sınıf>
- Son yeşilden bu yana değişenler: <liste veya [BİLİNMİYOR]>

## Hipotezler
| # | Hipotez | Kanıt | Doğrulama kontrolü | Olasılık |

## Çözüm
- Şimdi blokajı kaldır: ...
- Kalıcı çözüm: ...
## Önleme
- ...
## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Alıntılanan ilk hata verilen logda gerçekten var.
- [ ] Hipotezler kanıta dayanıyor; hiçbiri kanıtsız olgu gibi sunulmadı.
- [ ] Deterministik bir hata için yeniden deneme çözüm olarak önerilmedi.
- [ ] Çözüm, anlık blokaj kaldırmayı kalıcı çözümden ayırıyor.
- [ ] Açığa çıkan her secret rotasyon için işaretlendi.

## Sık yapılan hatalar
- Genellikle bir sonuç olan son hata satırını okumak. İlk hatayı bulmak için yukarı doğru ara.
- Kanıt olmadan kararsızlığı suçlamak. Tekrarlanıp tekrarlanmadığını, zamanlama veya sıralamanın etkisini kontrol et.
- Her şeyi aynı anda güncelleyerek veya sabitlemeyi kaldırarak düzeltmeye çalışmak. Tek seferde tek değişkeni değiştir.

## Örnek
Girdi: Log, imaj build sırasında `failed to solve: node:20: failed to resolve source metadata ... toomanyrequests` gösteriyor; son yeşil çalıştırma dün.

Çıktıdan bir bölüm:
- Sınıf: ağ/registry (rate limit).
- Hipotez 1: runner havuzu büyütüldükten sonra genel registry'den anonim çekmeler rate limit'e takıldı. Kanıt: `toomanyrequests`. Kontrol: kimlik doğrulamalı çekme yapan bir runner'da yeniden çalıştır.
- Kalıcı çözüm: base image'ları iç ayna/önbellek üzerinden çek ve digest ile sabitle.
