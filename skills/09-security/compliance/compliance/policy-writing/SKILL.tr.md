---
name: policy-writing
description: "Amaç, kapsam, uygulanabilir kurallar, roller, istisnalar, uyum ölçümü ve gözden geçirme döngüsü içeren bir güvenlik veya BT politikası yazar ya da revize eder; politikayı standart ve prosedürlerden ayırır. Bir politika eksik, güncelliğini yitirmiş veya denetimde bulgu almışsa ya da ISO 27001, SOC 2, KVKK veya iç yönetişim için gerekiyorsa (ör. kabul edilebilir kullanım, erişim kontrolü, parola, yedekleme, uzaktan çalışma, yapay zekâ kullanımı) kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: compliance
  area: compliance
  title: "Güvenlik/BT politikası yazma"
  related: "control-mapping, audit-preparation, it-risk-assessment, retention-policy, document-review"
  prompt: "Şirketimiz için erişim kontrol politikası yaz; ISO 27001'e hazırlanıyoruz, Entra ID ve GitHub kullanıyoruz."
---

# Güvenlik/BT Politikası Yazma

## Amaç
Neyin sağlanması gerektiğini, kimin hesap verdiğini ve uyumun nasıl ölçüleceğini belirten kısa ve uygulanabilir bir politika üretmek. Böylece çalışanlar politikaya uyabilir, denetçiler test edebilir ve istisnalar tutarlı biçimde yönetilir.

## Ne zaman kullanılır
- Gerekli bir politika yoksa (denetim bulgusu, sertifikasyon eksiği, müşteri şartı).
- Mevcut bir politika teknoloji, organizasyon veya mevzuat değişikliğinden sonra güncelliğini yitirdiyse.
- Kurallar yalnızca kişilerin bilgisinde veya dağınık wiki sayfalarında duruyor ve bağlayıcı bir dokümana ihtiyaç varsa.
- Yeni bir risk alanında hızla tutum belirlemek gerekiyorsa (ör. üretken yapay zekâ kullanımı, kişisel cihaz kullanımı).

## Ne zaman kullanılmaz
- Hangi kontrollerin bir standarda karşılık geldiğini kontrol etmeniz gerekiyorsa `control-mapping` kullanılır.
- Veri kategorisi bazında saklama süreleri gerekiyorsa `retention-policy` kullanılır.
- Adım adım operasyon talimatı gerekiyorsa `runbook` kullanılır.

## Girdiler
Zorunlu:
- Politikanın konusu ve kurum bağlamı (büyüklük, sektör, ana sistemler veya kapsamdaki mevzuat).

İsteğe bağlı, kaliteyi artırır:
- Mevcut politika, denetim bulguları veya karşılanacak kontrol gereksinimleri (ISO/IEC 27001 Ek A kontrol numaraları, SOC 2 kriterleri, KVKK teknik ve idari tedbirleri).
- Politika şablonu, doküman numaralandırması, onay makamı (ör. bilgi güvenliği komitesi).
- Bilinen istisnalar veya kısıtlar.

Konu veya bağlam yoksa iste (tek seferde en fazla 5 kısa soru). Geri kalan her şey `[TBD]` veya açık soru olur.

## Süreç
1. Politikanın hedefini, ele aldığı bir risk veya gereksinime bağlayarak bir iki cümleyle tanımla.
2. Kapsamı belirle: kişiler (çalışanlar, yükleniciler, üçüncü taraflar), varlıklar, lokasyonlar, sistemler; hariç tutulanları yaz.
3. Seviyeleri ayır: politika zorunlu ilkeleri belirtir ("-malıdır/-mamalıdır"); sık değişen teknik değerler (parola uzunluğu, araç adları, saklama günleri) atıf yapılan bir standarda veya prosedüre gider.
4. Kuralları "-malıdır", "-mamalıdır" veya "-melidir (önerilir)" kalıbıyla, her cümlede tek gereksinim olacak şekilde test edilebilir yaz. Her kural denetlenebilir olmalı: denetçi uyum veya uyumsuzluk kanıtı bulabilmeli.
5. Rolleri ve sorumlulukları tanımla: politika sahibi, onaylayanlar, uygulayanlar, tüm kullanıcılar. Üçten fazla rol varsa kısa bir RACI kullan.
6. İstisna sürecini tanımla: kim talep edebilir, kim onaylar, azami süre, telafi edici kontroller, istisna kaydı.
7. Uyum ve yaptırımı tanımla: uyumun nasıl ölçüldüğü (gözden geçirmeler, loglar, metrikler), ihlalin İK prosedürleriyle uyumlu sonuçları, bildirim kanalı.
8. Referansları ekle: ilgili politikalar, standartlar, prosedürler ve karşılanan gereksinimler (ISO 27001 kontrol numaraları, KVKK, SOC 2); ücretli standartlardan alıntı yapma.
9. Doküman kontrolünü ekle: sürüm, sahip, onay tarihi, gözden geçirme döngüsü (genellikle yıllık veya önemli değişiklikte), değişiklik geçmişi.
10. Okunabilirliği gözden geçir: sade dil, kuralların içinde gerekçe yazıları yok, hedef 2-4 sayfa; arka planı eke taşı.
11. Varsayılan kurum bağlamına dayanan her kuralı `[VARSAYIM]` olarak işaretle; kuralları kontrollere bağlamak için `control-mapping`, denetim yakınsa `audit-preparation` öner.

## Çıktı formatı
```markdown
# <Politika Adı>
| Doküman No | [TBD] | Sürüm | 1.0 | Sahibi | <rol> | Onaylayan | <makam> [TBD] | Onay tarihi | [TBD] | Sonraki gözden geçirme | [TBD] |

## 1. Amaç
## 2. Kapsam
- Uygulandığı alan: ... / Hariç: ...
## 3. Politika Hükümleri
3.1 <-malıdır / -mamalıdır içeren kural>
3.2 ...
## 4. Roller ve Sorumluluklar
| Rol | Sorumluluk |
## 5. İstisnalar
## 6. Uyum ve Yaptırım
## 7. İlgili Dokümanlar ve Gereksinimler
- ISO/IEC 27001:2022 A.x.y, KVKK ..., <iç standart>
## 8. Tanımlar
## 9. Değişiklik Geçmişi
| Sürüm | Tarih | Değişiklik | Hazırlayan |
```

## Kalite kontrol listesi
- [ ] Her kural tek ve test edilebilir bir "-malıdır/-mamalıdır/-melidir" ifadesi.
- [ ] Sık değişen teknik değerler kurala gömülmedi, bir standarda atıf yapıldı.
- [ ] Kapsam, sahip, istisna süreci ve gözden geçirme döngüsü mevcut.
- [ ] Roller isimli kişilere değil pozisyonlara atandı.
- [ ] Karşılanan gereksinimlere birebir alıntı yapılmadan numarayla atıf yapıldı.
- [ ] Verilmeyen kuruma özgü bilgiler `[TBD]` veya `[VARSAYIM]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kimsenin denetleyemeyeceği temenni cümleleri yazmak ("güvenlik herkesin sorumluluğudur"). Bunları somut yükümlülüklere çevir ya da sil.
- Prosedürleri politikaya gömmek; böylece her araç değişiminde yeniden onay gerekir. Politikayı sabit tut, "nasıl"ı prosedürlere koy.
- İstisna yolu tanımlamamak; insanlar politikayı sessizce atlar. Hafif ve süreli bir istisna süreci sağla.
- Başka bir şirketin politikasını, kurumun işletmediği kontrollerle birlikte kopyalamak; bu denetimde uygunsuzluk doğurur.

## Örnek
Girdi: "Erişim kontrol politikası, 300 çalışan, Entra ID ve GitHub, ISO 27001 hazırlığı."

Zayıf kural: "Erişimler uygun şekilde verilmeli ve düzenli olarak gözden geçirilmelidir."
Güçlü kurallar:
- 3.2 Üretim sistemlerine erişim yalnızca iş gerekçesini ve talep edenden farklı bir onaylayanı belirten onaylı bir talep üzerinden verilmelidir.
- 3.5 Ayrıcalıklı erişimde MFA ve kişiye özel hesaplar kullanılmalıdır; paylaşılan yönetici hesapları kullanılmamalıdır. (ISO/IEC 27001:2022 A.8.2, A.8.5)
- 3.7 Erişim hakları, Erişim Gözden Geçirme Prosedürü'ne göre ayrıcalıklı roller için en az çeyrekte bir, diğerleri için altı ayda bir gözden geçirilmelidir [VARSAYIM].
