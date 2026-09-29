---
description: "Değişiklik onayı veya değişiklik danışma kurulu (CAB) için hazır bir BT değişiklik talebi (RFC) yazar: gerekçe, kapsam ve etkilenen konfigürasyon öğeleri, değişiklik türü, risk ve etki değerlendirmesi, uygulama planı, test kanıtları, tetikleyicisiyle geri alma planı, takvim, iletişim ve doğrulama. Altyapı, uygulama, yapılandırma veya veride bir üretim değişikliği onay gerektirdiğinde, CAB'a sunum yapılacağında veya acil bir değişikliğin belgelenmesi gerektiğinde kullanılır."
related: "rollback-plan, deployment-checklist, deployment-strategy, technical-risk-review, problem-management"
prompt: "Üretimdeki PostgreSQL kümesini bu cumartesi gecesi 14'ten 16'ya yükseltmek için RFC yaz; 3 uygulama buna bağlı, geçen hafta staging'de test ettik."
---

# Değişiklik Talebi (RFC) Yazma

## Amaç
Onaylayanlara hızlı karar verecek kadar kanıt, uygulayıcılara da güvenle uygulayıp geri alabilecekleri bir plan vermek. Böylece değişiklikler ilk seferde başarılı olur, başarısız olanlar olaya dönüşmeden geri alınır.

## Ne zaman kullanılır
- Üretimde normal bir değişiklik (altyapı, uygulama, yapılandırma, erişim, veri) onay gerektirdiğinde.
- Değişiklik, risk görünümüne ihtiyaç duyan bir CAB'a veya onaylayana gideceğinde.
- Acil bir değişiklik yapıldığında veya yapılması gerektiğinde ve belgelenip sonradan onaylanması gerektiğinde.

## Ne zaman kullanılmaz
- Şablonu mevcut, önceden onaylı standart bir değişiklik için o şablon veya `runbook` kullanılır.
- Proje kapsamı, bütçesi veya takviminde değişiklik için `change-control` kullanılır.
- Yalnızca teknik geri alma prosedürü gerekiyorsa `rollback-plan` kullanılır.

## Girdiler
Zorunlu:
- Neyin, nerede (ortam, sistemler) ve neden değişeceği.
- Planlanan tarih/saat veya bunu belirleyen kısıt.

İsteğe bağlı, kaliteyi artırır:
- Etkilenen konfigürasyon öğeleri ve bağımlılıklar, test sonuçları, önceki benzer değişiklikler ve sonuçları.
- Kurumun RFC şablonu, risk matrisi, değişiklik pencereleri ve dondurma dönemleri.
- Uygulayıcı, onaylayanlar, iş sahibi, tedarikçi katılımı.

Ne, nerede veya neden eksikse tek mesajla sor. Risk derecesini, kesinti süresini veya test sonuçlarını kanıt olmadan doldurma; `[BİLİNMİYOR]` veya `[VARSAYIM]` olarak işaretle. RFC'ye asla kimlik bilgisi, anahtar veya bağlantı cümlesi (connection string) koyma.

## Süreç
1. Değişikliği ve gerekçesini iş ve teknik sonuç olarak yaz (örneğin desteği biten sürüm, güvenlik düzeltmesi, kapasite, PRB-... problemi) ve yapılmamasının riskini belirt.
2. Değişiklik türünü kurumun tanımlarına göre sınıflandır (standart, normal, acil); acil durumu açıkça gerekçelendir.
3. Etkilenen konfigürasyon öğelerini, yukarı ve aşağı yönlü bağımlılıkları, kullanıcıları ve hizmetleri listele; değişiklik takviminde çakışma ve dondurma dönemlerini kontrol et.
4. Etkiyi değerlendir: beklenen kesinti veya performans düşüşü, veri taşıma veya şema etkileri, performans, güvenlik ve uyum etkileri (örneğin KVKK/GDPR kapsamında kişisel veri işleme, denetim logları).
5. Riski olasılık x etki ile derecelendir (kurumun matrisini, yoksa `[VARSAYIM]` ile işaretli 3x3 bir ölçek kullan) ve başlıca riskleri önlemleriyle listele.
6. Uygulama planını sahibi ve kontrol noktası olan, zamanlanmış, numaralı adımlar olarak yaz; ön kontrolleri (yedeklerin doğrulanması, kapasite, erişim) ve devam/dur (go/no-go) noktasını ekle.
7. Test kanıtlarını belgele: ortam, neyin test edildiği, sonuçlar ve güveni sınırlayan üretimden farklar.
8. Geri alma planını yaz: ölçülebilir tetikleyici (örneğin 10 dakika boyunca eşiği aşan hata oranı veya X adımının başarısız olması), adımlar, gereken süre, veri etkileri ve varsa dönüşü olmayan nokta.
9. Uygulama sonrası doğrulamayı tanımla: teknik kontroller, iş smoke testleri, ne kadar süre hangi izlemenin takip edileceği ve başarıyı kimin onaylayacağı.
10. İletişimi planla: önce, sırasında ve sonra kimin bilgilendirileceği (kullanıcılar, destek, paydaşlar) ve servis masasının hazırlığı.
11. Devret: ayrıntılı geri alma için `rollback-plan`, uygulama için `deployment-checklist`, yüksek riskli bir değişiklik için `technical-risk-review` öner.

## Çıktı formatı
```markdown
# RFC: <no> – <kısa başlık>
| Alan | Değer |
|---|---|
| Tür | standart / normal / acil – <gerekçe> |
| Talep eden / Uygulayan / İş sahibi | <...> |
| Planlanan pencere | <başlangıç–bitiş, saat dilimi>; çakışma kontrolü: evet/hayır |
| Etkilenen CI'lar ve hizmetler | <...> |
| Beklenen kesinti | <süre veya yok veya [BİLİNMİYOR]> |
| Risk | <Düşük/Orta/Yüksek> – <olasılık x etki gerekçesi> |

## Gerekçe ve Fayda
<neden şimdi; değiştirmemenin riski>
## Etki Değerlendirmesi
- Kullanıcılar/hizmetler: ... Veri: ... Güvenlik/uyum: ...
## Riskler ve Önlemler
| Risk | Olasılık | Etki | Önlem |
|---|---|---|---|
## Uygulama Planı
| # | Zaman | Adım | Sahip | Kontrol noktası |
|---|---|---|---|---|
## Test Kanıtları
- Ortam / sonuç / üretime göre eksikler
## Geri Alma Planı
- Tetikleyici: ... Adımlar: ... Süre: ... Dönüşü olmayan nokta: ...
## Doğrulama
- Teknik: ... İş: ... İzleme: <ne, ne kadar süre> ... Onay: <kim>
## İletişim
- Önce / sırasında / sonra: ...
## Onaylayanlar İçin Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Gerekçe ve değiştirmemenin riski açıkça yazılı.
- [ ] Her uygulama adımının sahibi ve kontrol noktası var, bir go/no-go noktası tanımlı.
- [ ] Geri alma planının ölçülebilir tetikleyicisi, süresi ve dönüşü olmayan noktası var.
- [ ] Risk derecesi gerekçeli; üretime göre test eksikleri belirtilmiş.
- [ ] Diğer değişikliklerle çakışmalar ve dondurma dönemleri kontrol edildi.
- [ ] RFC'de kimlik bilgisi yok; eksik kanıt uydurulmadı, `[BİLİNMİYOR]` olarak işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Geri yükleme süresi veya test edilmiş bir yedek olmadan "Geri alma: yedekten dön" yazmak. Süreyi ve son geri yükleme testini belirt.
- Onaydan geçmek için her şeyi Düşük risk olarak işaretlemek. Onaylayanlar bir süre sonra derecelere güvenmez.
- Birbiriyle ilgisiz değişiklikleri tek RFC'de toplamak; geri almayı değerlendirmek imkânsızlaşır.
- İş doğrulaması ve izleme yapılmadan, kurulum bittiği anda başarı ilan etmek.

## Örnek
Girdi: "Üretimdeki PostgreSQL'i bu cumartesi gecesi 14'ten 16'ya yükselt; 3 uygulama bağlı; geçen hafta staging'de test edildi."

Çıktıdan bir bölüm:
- Gerekçe: 14 sürümünün topluluk desteğinin sonu yaklaşıyor [VARSAYIM: tarihi teyit et]; değişiklik yapılmazsa güvenlik yamaları alınamaz.
- Risk: Orta – yüksek etki (3 uygulama), staging testi olasılığı azaltıyor; staging veri hacmi üretimin %20'si [VARSAYIM], bu yüzden yükseltme süresi belirsiz.
- Geri alma tetikleyicisi: geçişten 15 dakika sonra herhangi bir uygulama sağlık kontrolünün başarısız olması veya pg_upgrade adımının başarısız olması. Geri alma: bağlantıyı dokunulmamış v14 primary'ye geri çevir; dönüşü olmayan nokta: v16'ya ilk yazma.
- Açık soru: 3 uygulamanın sürücüleri v16 için sertifikalı mı?
