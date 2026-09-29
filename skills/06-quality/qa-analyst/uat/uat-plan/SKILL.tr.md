---
name: uat-plan
description: "Kullanıcı kabul testini planlar: hedefler, iş tarafı katılımcıları ve rolleri, senaryo kapsamı, ortam ve veri hazırlığı, takvim, hata yönetimi, giriş/çıkış kriterleri ve resmî onay yolu. Bir sürüm, proje aşaması veya tedarikçi teslimatı iş birimi kabulü gerektirdiğinde, UAT'nin nasıl organize edileceği sorulduğunda ya da iş kullanıcılarının canlıya geçmeden önce çözümün gerçek işlerini desteklediğini teyit etmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: uat
  title: "Kullanıcı kabul testi planı"
  related: "uat-scenarios, test-plan, acceptance-certificate, requirements-sign-off, release-quality-gate"
  prompt: "Yeni faturalama modülü için UAT planla: finans ve satış kullanıcıları canlıya geçişten önce iki hafta test edecek."
---

# Kullanıcı Kabul Testi Planı

## Amaç
İş kullanıcılarına iyi hazırlanmış, süresi belli, sorumlulukları ve kriterleri net bir kabul penceresi sunmak. Böylece kabul kararı aceleye getirilmiş ikinci bir sistem testini değil gerçek iş akışını yansıtır ve resmî olarak kayda geçer.

## Ne zaman kullanılır
- Bir çözüm veya sürüm canlıya çıkmak üzereyken ve iş sahiplerinin kabul vermesi gerektiğinde.
- Bir tedarikçi veya sözleşme teslimatı, ödeme ya da devir öncesinde resmî kabul gerektirdiğinde.
- Önceki UAT turları dağınık geçtiğinde (hazırlıksız kullanıcılar, bozuk veri, belirsiz onay) ve yapıya ihtiyaç olduğunda.

## Ne zaman kullanılmaz
- İş senaryolarının kendisi gerekiyorsa `uat-scenarios` kullanılır.
- QA ekibinin yürüttüğü sistem veya entegrasyon testi planlanıyorsa `test-plan` kullanılır.
- Çıkış kriterlerine göre yayına alınır/alınmaz değerlendirmesi gerekiyorsa `release-quality-gate` kullanılır.

## Girdiler
Zorunlu:
- Kabul edilecek kapsam (özellikler, süreçler, sürüm) ve hedef canlıya geçiş veya kabul tarihi.
- Etkilenen iş alanları.

İsteğe bağlı, kaliteyi artırır:
- İsimleriyle iş sahipleri ve kilit kullanıcılar, müsaitlikleri, sözleşmedeki kabul şartları.
- Test ortamı durumu, veri kaynakları, sistem testi sonuçları, bilinen açık hatalar.

Kapsam veya hedef tarih yoksa iste. Elinde olmayan katılımcı isimlerini `[TBD]` olarak yaz; asla kişi veya tarih uydurma.

## Süreç
1. UAT hedeflerini iş diliyle yaz: hangi süreçlerin uçtan uca çalıştığı kanıtlanmalı ve onay hangi kararın önünü açıyor (canlıya geçiş, ödeme, devir).
2. Kapsamı tanımla: kapsamdaki iş süreçleri ve roller, kapsam dışı olanlar ve başka yerde zaten kabul edilmiş maddeler. Sistem testinden geçmemiş kapsamı risk olarak işaretle.
3. Katılımcıları belirle: kabul sahibi (imzalayan), iş süreci sahipleri, rol başına kilit kullanıcılar, UAT koordinatörü, hata yönetimi için QA/geliştirme desteği. Kapsamdaki her rolde en az bir gerçek kullanıcı olduğunu kontrol et.
4. Giriş kriterlerini koy: sistem testi çıkışı sağlanmış, kapsamda açık Kritik hata yok, ortama sürüm adayı kurulmuş, test verisi ve kullanıcı hesapları hazır, senaryolar iş tarafınca gözden geçirilmiş, katılımcılar bilgilendirilmiş.
5. Ortamı ve veriyi planla: canlıya benzer konfigürasyon, entegrasyonlar (gerçek mi stub mı, açıkça belirtilmiş), maskelenmiş veya sentetik kişisel veri, rol bazında hesap ve yetki kurulumu.
6. Takvimi oluştur: açılış ve eğitim, süreç alanı bazında koşum pencereleri, günlük hata gözden geçirmesi, yeniden test aralıkları, tampon, onay toplantısı. Kullanıcıların iş takvimine (ay sonu, yoğun sezon) saygı göster.
7. Hata yönetimini tanımla: kullanıcıların nasıl bildireceği (asgari alanlar), iş dilinde önem ölçeği, sınıflandırma sıklığı, şimdi düzelt / geçici çözümle kabul et / ertele kararını kimin vereceği.
8. Çıkış kriterlerini ve onay kuralını belirle: gerekli senaryo geçme oranı, kabul edilmiş geçici çözümü olmayan açık Kritik/Yüksek hata olmaması, sorumlusuyla listelenmiş ertelenen maddeler, kimin hangi biçimde imzalayacağı.
9. Riskleri (kullanıcı müsaitliği, veri hazırlığı, kararsız ortam, UAT'de "yeni gereksinim" olarak gelen kapsam kayması) önlemleriyle listele; yeni gereksinimleri hata listesine değil değişiklik kontrolüne yönlendir.
10. Kullanıcı devam ederse senaryoları yazmak için `uat-scenarios`, onay dokümanı için `acceptance-certificate`, sürüm kararı için `release-quality-gate` öner.

## Çıktı formatı
```markdown
# UAT Planı: <çözüm/sürüm>
| Alan | Değer |
|---|---|
| Kabul sahibi | <ad/rol veya [TBD]> |
| UAT penceresi | <başlangıç–bitiş veya [TBD]> |
| Canlıya geçiş / kabul tarihi | <tarih> |
| Ortam | <ad, build> |

## Hedefler
- ...
## Kapsam
| İş süreci | Roller | İçinde/Dışında | Notlar |
|---|---|---|---|
## Katılımcılar ve Sorumluluklar
| Rol | Kişi | Sorumluluk | Müsaitlik |
|---|---|---|---|
## Giriş Kriterleri
- [ ] ...
## Ortam ve Veri
- ...
## Takvim
| Gün/Tarih | Aktivite | Katılımcılar |
|---|---|---|
## Hata Yönetimi
- Bildirim alanları / önem ölçeği / sınıflandırma sıklığı / karar sahibi
## Çıkış Kriterleri ve Onay
- ...
## Riskler ve Önlemler
| Risk | Olasılık | Etki | Önlem |
|---|---|---|---|
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Hedefler ve çıkış kriterleri iş dilinde ve onayın hangi kararı sağladığını söylüyor.
- [ ] Kapsamdaki her rolün QA personeli değil, isimle veya `[TBD]` olarak belirtilmiş gerçek bir iş katılımcısı var.
- [ ] Giriş kriterleri test edilmemiş veya kararsız bir build üzerinde UAT başlatılmasını engelliyor.
- [ ] UAT ortamındaki kişisel veri maskelenmiş veya sentetik; değilse eksik işaretlendi.
- [ ] Onay sahibi ve biçimi açık.
- [ ] UAT sırasında gelen yeni gereksinimler değişiklik kontrolüne yönlendiriliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- UAT'yi ilk gerçek test olarak kullanmak. Sistem testi çıkışını giriş kriteri yap; yoksa kullanıcılar pencereyi temel hataları bulmakla geçirir.
- QA'nın iş kullanıcıları "adına" koşum yapması. Kabul, işin sahibi olan kişilerden gelmelidir.
- UAT'yi iş biriminin en yoğun dönemine planlamak. Tarihleri kesinleştirmeden önce iş takvimini kontrol et.

## Örnek
Girdi: "Yeni faturalama modülü için UAT; finans ve satış; ayın 1'indeki canlıya geçişten önce iki hafta."

Çıktıdan bir bölüm:
- Hedef: finansın faturayı uçtan uca kesebildiğini, düzeltebildiğini ve iptal edebildiğini, satışın siparişlerde doğru fatura durumunu gördüğünü kanıtlamak; onay canlıya geçişin önünü açar.
- Giriş kriteri: sistem testi çıkışı sağlandı; faturalamada açık Kritik hata yok; müşteri verisi maskelendi.
- Risk: pencere ay sonu kapanışıyla çakışıyor (Yüksek etki) — önlem: finans senaryolarını 1. haftada koş `[kapanış tarihlerini teyit et]`.
