---
name: release-quality-gate
description: "Sürüm hazırlığını üzerinde anlaşılmış çıkış kriterlerine (testler, hatalar, kapsam, fonksiyonel olmayan sonuçlar, operasyonel hazırlık, onaylar) göre değerlendirir; her kriteri kanıtıyla sağlandı, sağlanmadı veya muaf tutuldu olarak derecelendirir ve koşullar ile kabul edilen risklerle birlikte yayına al, koşullu yayına al veya yayına alma önerisi üretir. Bir üretim sürümü veya büyük bir dağıtım öncesinde, bir go/no-go toplantısında ya da bir build'in yayına hazır olup olmadığı sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: execution
  title: "Sürüm kalite kapısı değerlendirmesi"
  related: "test-summary-report, bug-triage, go-no-go, deployment-checklist, rollback-plan"
  prompt: "5.2 sürümünü çıkış kriterlerimize göre değerlendir: açık kritik/majör hata yok, %95 geçme oranı, regresyon tamam, performans p95 800 ms altında, güvenlik taraması temiz."
---

# Sürüm Kalite Kapısı Değerlendirmesi

## Amaç
Sürüm kararının kalite kısmını açık ve denetlenebilir kılmak: her çıkış kriteri kanıta göre değerlendirilir, her istisna görünür olur ve öneri veriye izlenebilir.

## Ne zaman kullanılır
- Bir sürüm adayı hazır ve bir kalite kapısı veya go/no-go toplantısı planlanmış.
- Resmî kriterleri olmayan bir ekip yapılandırılmış bir hazırlık kontrolüne ihtiyaç duyuyor.
- Açık sorunlara rağmen bir sürüm yayına zorlanıyor ve kabul edilen risklerin kaydedilmesi gerekiyor.

## Ne zaman kullanılmaz
- Bir test döngüsünün anlatımsal kalite raporu gerekiyorsa `test-summary-report` kullanılır.
- Fonksiyonlar arası tam go/no-go (destek, pazarlama, operasyon) gerekiyorsa `go-no-go` kullanılır.
- Dağıtım adımları veya geri alma prosedürü gerekiyorsa `deployment-checklist` ya da `rollback-plan` kullanılır.

## Girdiler
Zorunlu:
- Çıkış kriterleri (veya varsayılan önerme izni) ve mevcut kanıt: test sonuçları ve açık hatalar.

İsteğe bağlı, kaliteyi artırır:
- Fonksiyonel olmayan sonuçlar (performans, güvenlik, erişilebilirlik), kapsam verisi, değişiklik büyüklüğü.
- Operasyonel hazırlık: izleme, rollback planı, runbook'lar, destek bilgilendirmesi.
- Onaylayıcılar ve muafiyet politikası.

Kriter yoksa `[VARSAYIM]` ile işaretli varsayılan bir set öner ve puanlamadan önce kullanıcıdan onay iste. Bir kriterin kanıtı yoksa onu asla "Sağlandı" değil "Kanıtlanmadı" olarak derecelendir.

## Süreç
1. Çıkış kriterlerini ölçülebilir biçimde listele; belirsiz olanları ("kalite iyi") yeniden yaz ve onay için işaretle.
2. Kriterleri grupla: fonksiyonel test, hatalar, kapsam ve regresyon, fonksiyonel olmayan, güvenlik/uyum, operasyonel hazırlık, dokümantasyon ve onaylar.
3. Her kriter için kanıtı (rapor, pano, kayıt ID'leri) ve tarihini kaydet; karar verilen build'den eski kanıtı işaretle.
4. Her birini derecelendir: Sağlandı, Sağlanmadı, Kanıtlanmadı, Muaf (onaylayan ve gerekçeyle).
5. Sağlanmayan her kalem için açığı ve iş etkisini ölçülendir, düzelt veya kabul et seçeneklerini yaz.
6. Engelleyici hataları tek tek kontrol et: önem derecesini, geçici çözümü, etkilenen kullanıcıları ve düzeltmenin aday build'de olup olmadığını doğrula.
7. Operasyonel güvenlik ağlarını kontrol et: rollback test edildi mi, feature flag'ler, yeni işlevler için izleme ve alarmlar, nöbetçi ekibin haberdar olması.
8. Öneriye karar ver: Yayına al (hepsi sağlandı veya muaf), Koşullu yayına al (kritik olmayan açıklar, yayın öncesi veya sonrası için koşul ve sorumlularla), Yayına alma (kabul edilebilir azaltımı olmayan herhangi bir kritik açık).
9. Koşulları sorumlusu ve son tarihi olan doğrulanabilir kalemler olarak yaz; kabul edilen riskleri kabul eden rolle birlikte kaydet.
10. Karar sahibi olguları tartışmadan öneriye itiraz edebilsin diye olguları, derecelendirmeleri ve öneriyi ayrı tut.
11. Kullanıcı devam ederse fonksiyonlar arası karar için `go-no-go`, güvenlik ağı eksikse `rollback-plan` öner.

## Çıktı formatı
```markdown
# Sürüm Kalite Kapısı: <ürün> <sürüm>
**Öneri:** <Yayına al / Koşullu yayına al / Yayına alma> – <tek satır gerekçe>
Karar verilen build: <id> · Kanıt tarihi: <tarih>

| # | Kriter | Hedef | Gerçekleşen | Kanıt | Durum |
|---|---|---|---|---|---|

Durum: Sağlandı / Sağlanmadı / Kanıtlanmadı / Muaf

## Açıklar ve Seçenekler
- <kriter>: açık <...>, etki <...>, seçenekler <düzelt / kabul et / azalt>

## Engelleyici İncelemesi
| Hata | Önem | Geçici çözüm | Build'de düzeltildi mi? |
|---|---|---|---|

## Operasyonel Hazırlık
- Rollback: ... · İzleme: ... · Destek bilgilendirmesi: ...

## Koşullar
- <koşul> – <sorumlu> – <yayın öncesi/sonrası, tarih>

## Kabul Edilen Riskler
- <risk> – <rol> tarafından kabul edildi – <geçerlilik/gözden geçirme tarihi>
```

## Kalite kontrol listesi
- [ ] Her kriter ölçülebilir ve kanıtı karar verilen build'e bağlı.
- [ ] Eksik kanıt asla "Sağlandı" değil "Kanıtlanmadı" olarak derecelendirilmiş.
- [ ] Muafiyetler onaylayan rolü ve gerekçeyi belirtiyor.
- [ ] Öneri, derecelendirmelerden ve karar kuralından çıkıyor.
- [ ] Koşulların ve kabul edilen risklerin her birinin sorumlusu ve tarihi var ya da `[TBD]`.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Önceki bir build'in kanıtını kullanmak. Kanıt tarihinden sonraki her kod değişikliği, etkisi değerlendirilmedikçe kanıtı geçersiz kılar.
- Geçme oranını tek kriter saymak. Ödeme yolu test edilmemiş %99 geçme oranı hazır demek değildir.
- Kabul edilen riskleri yazmadan "Yayına al" kaydetmek. Bir sonraki olay incelemesi bunlara ihtiyaç duyacak.

## Örnek
Girdi: "5.2 sürümü: açık kritik/majör yok, %95 geçme, regresyon tamam, p95 < 800 ms, güvenlik taraması temiz."

Çıktıdan bir bölüm:
| # | Kriter | Hedef | Gerçekleşen | Kanıt | Durum |
|---|---|---|---|---|---|
| 1 | Açık kritik/majör hata | 0 | 1 majör (B-88) | 12'si önceliklendirme | Sağlanmadı |
| 2 | Geçme oranı | ≥%95 | %96,1 | Özet rapor | Sağlandı |
| 4 | p95 gecikme | <800 ms | `[BİLİNMİYOR]` | Önceki build'deki performans testi | Kanıtlanmadı |

**Öneri:** Koşullu yayına al – B-88'in dokümante edilmiş geçici çözümü var; koşullar: dağıtım öncesi performans testini 5.2.0-rc3 build'inde yeniden koş (sorumlu: performans mühendisi); B-88 düzeltmesi 5.2.1'de.
