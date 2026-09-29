---
name: deployment-checklist
description: "Sistemin bileşenlerine, veri değişikliklerine ve dağıtım mekanizmasına göre uyarlanmış, her biri sorumlu, beklenen sonuç ve durdurma koşulu içeren dağıtım öncesi, sırası ve sonrası kontrollerden oluşan bir dağıtım kontrol listesi hazırlar. Bir üretim dağıtımı planlandığında, dağıtımlar unutulan adımlar yüzünden başarısız olduğunda ya da geçiş veya dağıtım günü kontrol listesi istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Dağıtım kontrol listesi"
  related: "release-plan, rollback-plan, go-no-go, runbook, deployment-strategy"
  prompt: "Bu geceki sürüm için dağıtım kontrol listesi hazırla: Kubernetes üzerinde iki API servisi, bir SQL migration'ı ve gateway'de bir yapılandırma değişikliği var."
---

# Dağıtım Kontrol Listesi

## Amaç
Dağıtımı, sorumluları ve açık durdurma noktaları olan doğrulanabilir kontroller dizisine dönüştürmek. Böylece zaman baskısı altında hiçbir şey unutulmaz ve başarısız giden bir dağıtım kullanıcılara veya veriye zarar vermeden durdurulur.

## Ne zaman kullanılır
- Bir üretim (veya başka bir paylaşılan ortam) dağıtımı planlandığında ve adım listesi gerektiğinde.
- Önceki dağıtımlar unutulan adımlar, yapılandırma sapması veya doğrulanmamış sonuçlar yüzünden başarısız olduğunda.
- Manuel veya yarı otomatik bir geçiş birden fazla kişiyi içerdiğinde.

## Ne zaman kullanılmaz
- Sürümün genel takvimi, içeriği ve iletişimi gerekiyorsa `release-plan` kullanılır.
- Dağıtımı geri almanın ayrıntılı prosedürü gerekiyorsa `rollback-plan` kullanılır.
- Bir alarm için tekrar kullanılabilir operasyonel prosedür gerekiyorsa `runbook` kullanılır.

## Girdiler
Zorunlu:
- Neyin dağıtılacağı: bileşenler, artefaktlar veya sürümler ve hedef ortam.
- En azından üst düzeyde dağıtım mekanizması (pipeline, manuel adımlar, script'ler).

İsteğe bağlı, kaliteyi artırır:
- Veritabanı veya veri migration'ları, yapılandırma ve secret değişiklikleri, altyapı değişiklikleri.
- İzleme panoları ve kilit metrikler, mevcut smoke testler.
- Kurumun değişiklik yönetimi kuralları, bakım penceresi, ekip üyeleri.

Bileşenler veya hedef ortam bilinmiyorsa sor. Bilinmeyen sorumlular `[TBD]` olur; bilinmeyen komutlar uydurulmaz, niyet olarak tarif edilir.

## Süreç
1. Değişen her şeyi listele: artefaktlar ve sürümler, yapılandırma, secret'lar, şema/veri, altyapı, dış bağımlılıklar, feature flag'ler.
2. Dağıtım öncesi kontroller: onaylı değişiklik kaydı, staging'den terfi etmiş doğru artefakt (sürüm, digest veya checksum), alınmış ve geri yüklenebilir yedek veya snapshot, kapasite ve kota payı, bağımlı ekipler bilgilendirildi, nöbetçi haberdar, geri dönüş planı gözden geçirildi.
3. Ortamın hazır olduğunu doğrula: mevcut sağlık referansı (hata oranı, gecikme, doygunluk) kaydedildi, aktif olay yok, çakışan başka değişiklik sürmüyor.
4. Uygulama adımlarını bağımlılık sırasıyla yaz; her birinde sorumlu, beklenen sonuç ve doğrulama (işe yaradığını nasıl anlarsın) olsun.
5. Riskli adımlardan sonra durdurma koşulları ekle: eşik değeri veya `[TBD]` ile açık "X olursa dur ve geri dönüşü başlat" ifadesi.
6. Geri dönüşsüz noktayı işaretle ve ondan önce açık bir devam kararı iste.
7. Dağıtım sonrası doğrulama: smoke testler, kilit kullanıcı akışları, referansla karşılaştırılan metrikler, yeni hata sınıfları için loglar, boşalan arka plan işleri ve kuyruklar, veri migration'ı için satır sayıları veya kontroller.
8. Kapanış: planlandıysa flag'leri aç, değişiklik kaydını ve durum kanallarını güncelle, izleme penceresini ve hypercare sorumlusunu teyit et, sapmaları retrospektif için kaydet.
9. Her maddeyi doğrulanabilir evet/hayır ifadesi olarak tut; açıklamaları notlara taşı.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa geri alma prosedürü için `rollback-plan`, karar kapısı için `go-no-go` veya tekrarlanan adımları yeniden kullanılabilir bir prosedüre dönüştürmek için `runbook` öner.

## Çıktı formatı
```markdown
# Dağıtım Kontrol Listesi: <sürüm/sistem> – <ortam> – <tarih>
Dağıtım lideri: <ad veya [TBD]> · Geri dönüş planı: <bağlantı veya [TBD]>

## Dağıtım Öncesi
| # | Kontrol | Sorumlu | Beklenen sonuç | Tamam |
|---|---|---|---|---|

## Uygulama
| # | Adım | Sorumlu | Doğrulama | Şu olursa dur | Tamam |
|---|---|---|---|---|---|
| ⚠ | GERİ DÖNÜŞSÜZ NOKTA – devam kararı gerekli | | | | |

## Dağıtım Sonrası Doğrulama
| # | Kontrol | Sorumlu | Referansa göre | Tamam |

## Kapanış
- [ ] Değişiklik kaydı güncellendi
- [ ] Paydaşlara sonuç bildirildi
- [ ] Hypercare sorumlusu ve süresi teyit edildi

## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her adımın bir sorumlusu ve doğrulanabilir beklenen sonucu var.
- [ ] Dağıtımdan önce referans değerler kaydediliyor, sonraki kontroller bunlarla karşılaştırılıyor.
- [ ] Riskli adımlardan sonra geri dönüşe bağlı açık durdurma koşulları var.
- [ ] Veri değişikliklerinde yalnızca "migration çalıştı" değil, yedek ve doğrulama kontrolü (sayılar, bütünlük) var.
- [ ] Yalnızca HTTP endpoint'leri değil, arka plan işleri, kuyruklar ve cache'ler de kapsanıyor.
- [ ] Hiçbir komut, eşik veya isim uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Adım olarak "logları kontrol et" yazmak. Neye bakılacağını ve neyin hata sayılacağını belirt.
- Yedek alıp geri yüklemeyi hiç test etmemek. Bir geri yükleme doğrulaması ekle veya son test edilen geri yüklemeyi belirt.
- Dağıtım biter bitmez başarı ilan etmek. İzleme penceresini koru ve sorumlusunu adlandır.

## Örnek
Girdi: "Kubernetes'te iki API, bir ekleme yapan SQL migration'ı, gateway route değişikliği, bu gece 23:00."

Çıktıdan bir bölüm:
| # | Adım | Sorumlu | Doğrulama | Şu olursa dur |
|---|---|---|---|---|
| U1 | Ekleme yapan migration'ı çalıştır | DBA `[TBD]` | Yeni kolonlar var; satır sayısı değişmedi | Migration `[TBD]` dk'yı aşar veya tabloyu kilitlerse |
| U2 | API A'yı yayına al | Ekip A | Tüm pod'lar hazır; 5xx oranı referansta | 5xx oranı 5 dk boyunca referans + `[TBD]` üzerinde |
| U4 | Gateway route'unu değiştir | Platform | Yeni route'taki sentetik kontrol geçiyor | Yeni route'ta herhangi bir 404/502 |
