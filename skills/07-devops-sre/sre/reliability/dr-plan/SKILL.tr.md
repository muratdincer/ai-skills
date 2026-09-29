---
description: "Bir sistem için felaket kurtarma planı yazar: servis katmanına göre iş gereksinimine dayalı RTO/RPO, felaket senaryoları, kurtarma stratejisi ve bağımlılık sırası, adım adım failover ve failback prosedürleri, roller ve felaket ilan yetkisi, iletişim ve kanıtlı bir test takvimi. Sistemde DR planı yoksa, RTO/RPO hedefleri belirlenmeli veya doğrulanmalıysa, bir denetim öncesinde ya da bir DR testi veya olay eksikleri ortaya çıkardıktan sonra kullanılır."
related: "backup-restore-plan, runbook, chaos-experiment, incident-communication, resilience-review"
prompt: "Çekirdek bankacılık API'miz ve PostgreSQL veritabanı için DR planı yaz. İş birimi RTO 1 saat ve RPO 5 dakika istiyor; tek bölgede çalışıyoruz ve gecelik yedek alıyoruz."
---

# Felaket Kurtarma Planı

## Amaç
Büyük bir kesintiden sonra bir sistemin, üzerinde anlaşılmış kurtarma süresi ve veri kaybı sınırları içinde nasıl geri getirileceğini tanımlamak. Prosedürler stres altında uygulanabilecek kadar kesin olmalı, testler de hedeflerin tutturulabildiğini kanıtlamalı.

## Ne zaman kullanılır
- Kritik bir sistemin DR planı yok ya da plan hiç test edilmemiş.
- RTO/RPO hedefleri iş birimiyle kararlaştırılmalı veya mevcut mimariye karşı kontrol edilmeli.
- Bir denetim, düzenleyici kurum veya müşteri belgelenmiş ve test edilmiş kurtarma yeteneği istiyor.

## Ne zaman kullanılmaz
- Kapsam yalnızca veritabanı yedekleri ve geri yüklemeyse `backup-restore-plan` kullanılır.
- Tek bir hata modu için müdahale prosedürü gerekiyorsa `runbook` kullanılır.
- Felaket şu an yaşanıyorsa `incident-response` kullanılır; varsa bu planın prosedürleri ardından uygulanır.

## Girdiler
Zorunlu:
- Kapsamdaki sistem, bileşenleri ve nerede çalıştıkları.
- Kesinti ve veri kaybının iş etkisi ya da iş biriminin belirttiği hedefler.

İsteğe bağlı, kaliteyi artırır:
- Mevcut yedekleme, replikasyon ve kod olarak altyapı kurulumu; üçüncü taraflar dahil bağımlılık haritası.
- Yasal veya sözleşmesel yükümlülükler (örn. ISO 22301 veya sektör kuralları kapsamındaki iş sürekliliği gereksinimleri).
- Önceki DR testleri ve olaylar; bütçe kısıtları.

İş etkisi veya hedefler bilinmiyorsa bunların sahibini sor; RTO/RPO'yu onlar adına belirleme. Önerilen değerler `[ÖNERİ]` olarak işaretlenir ve iş biriminin onayını gerektirir.

## Süreç
1. Bileşenleri ve bağımlılıkları (işlem gücü, veri depoları, kuyruklar, DNS, kimlik, secret'lar, sertifikalar, üçüncü taraf API'ler) envanterle ve her servisi iş kritikliğine göre katmanlandır.
2. Katman başına RTO ve RPO'yu iş sahibiyle kararlaştır; onaylayanı kaydet, onaysız hedefleri işaretle.
3. Felaket senaryolarını tanımla: bölge içi zone kaybı, bölge kaybı, veri bozulması veya yanlışlıkla silme, fidye yazılımı veya ele geçirilmiş hesap, kritik üçüncü taraf kesintisi, kilit kişi veya erişim kaybı.
4. Senaryo başına mevcut yeteneği değerlendir: bugünkü yedekler, replikasyon ve otomasyonla ulaşılabilen RTO/RPO; hedeflere karşı eksikleri listele.
5. Katman başına bir kurtarma stratejisi seç (yedekten geri yükleme, pilot light, warm standby, active-active) ve maliyet, karmaşıklık ve hedefler arasındaki ödünleşimi göster.
6. Kurtarma sırasını bağımlılıklardan çıkar: önce temeller (ağ, kimlik, secret'lar, DNS), sonra veri, sonra servisler, en son trafik geçişi.
7. Adım başına beklenen süre, sahip ve doğrulama içeren adım adım failover prosedürlerini yaz; veri tutarlılığı kontrollerini ve yarıda kalan işlemlerin nasıl ele alınacağını dahil et.
8. Failback prosedürlerini ve birincil siteye dönüş kriterlerini yaz; failback çoğu zaman failover'dan daha risklidir.
9. Rolleri ve felaket ilanını tanımla: kim felaket ilan edebilir, karar kriterleri, eskalasyon kişileri ve birincil kimlik sağlayıcı çöktüğünde ekibin nasıl erişim sağlayacağı (güvenli saklanan break-glass hesaplar).
10. İletişimi tanımla: iç ekipler, müşteriler, düzenleyiciler; şablonlar ve zamanlamayla birlikte.
11. Test programını tanımla: masa başı tatbikat, bileşen geri yükleme, tam failover; sıklık, başarı kriterleri (ölçülen RTO/RPO) ve saklanan kanıtlar.
12. Her çıkarımı `[VARSAYIM]` olarak etiketle, açık soruları listele ve sonraki becerileri öner: veri ayrıntıları için `backup-restore-plan`, her prosedür için `runbook`, bileşen testleri için `chaos-experiment`, şablonlar için `incident-communication`.

## Çıktı formatı
```markdown
# Felaket Kurtarma Planı: <sistem>
Sahip: <ad> · İş onaylayıcısı: <ad veya [BİLİNMİYOR]> · Son test: <tarih veya hiç>

## Kapsam ve Servis Katmanları
| Servis | Katman | RTO | RPO | Onaylayan |

## Bağımlılıklar ve Kurtarma Sırası
## Senaryolar ve Mevcut Yetenek
| Senaryo | Bugün ulaşılabilen RTO/RPO | Eksik | Strateji |

## Failover Prosedürü
| # | Adım | Sahip | Beklenen süre | Doğrulama |

## Failback Prosedürü ve Kriterleri
## Roller, Felaket İlanı ve Erişim
## İletişim Planı
## Test Programı
| Test türü | Sıklık | Başarı kriteri | Kanıt |

## Varsayımlar, Riskler ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her RTO/RPO'nun adı belli bir iş onaylayıcısı var ya da `[ÖNERİ]` olarak işaretli.
- [ ] Mevcut yetenek hedeflerle karşılaştırıldı ve eksikler açık.
- [ ] Kurtarma sırası kimlik, secret'lar ve DNS dahil bağımlılıkları izliyor.
- [ ] Her prosedür adımının sahibi, beklenen süresi ve doğrulaması var.
- [ ] Yalnızca altyapı kaybı değil, veri bozulması ve ele geçirilmiş hesap senaryoları da kapsanıyor.
- [ ] Ölçülebilir başarı kriterleri ve kanıtlarla bir test programı tanımlandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Replikasyonu yedek saymak. Replikasyon bozulmayı ve silmeleri anında kopyalar; zamana nokta geri dönüş (point-in-time recovery) veya değiştirilemez yedekler gerekir.
- Çöken bölgenin araçlarına (kimlik, secret kasası, CI/CD, runbook wiki'si) bağımlı bir plan. Kurtarma erişimini bağımsız tut.
- RTO'yu arızadan itibaren sayıp tespit ve felaket ilanı süresini yok saymak. İkisini de dahil et.

## Örnek
Girdi: "Çekirdek bankacılık API'si + PostgreSQL, hedef RTO 1 sa / RPO 5 dk, tek bölge, gecelik yedek."

Çıktıdan bir bölüm:
| Senaryo | Bugün ulaşılabilen | Eksik | Strateji |
|---|---|---|---|
| Bölge kaybı | RTO `[BİLİNMİYOR]` (hiç test edilmedi), RPO 24 saate kadar | RPO 5 dakikalık hedefi karşılamıyor | Bölgeler arası streaming replikasyon + point-in-time recovery ile warm standby |
| Veri bozulması | RPO 24 saate kadar | Aynı | Değiştirilemez depolamaya sürekli WAL arşivleme |

Açık soru: İş biriminde RTO 1 sa / RPO 5 dk hedefini kim onayladı ve standby maliyeti kabul ediliyor mu?
