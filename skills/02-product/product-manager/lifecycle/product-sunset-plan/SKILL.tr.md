---
description: Bir ürünün, paketin veya özelliğin kullanımdan kaldırılmasını; açık karar kriterleri, etkilenen müşteri segmentleri, geçiş yolları, aşamalı iletişim sırası, takvim kapıları ve veri saklama/silme yükümlülükleriyle planlar. Bir ürün veya özellik emekliye ayrılırken, yenisiyle değiştirilirken ya da birleştirilirken veya "müşteri ve güven kaybetmeden bunu nasıl kapatırız" sorusu sorulduğunda kullanılır.
related: communication-plan, migration-strategy, api-deprecation-plan, impact-analysis, kpi-definition
prompt: Eski raporlama modülümüzü gelecek yıl kapatıp herkesi yeni analitik panoya taşımak istiyoruz. Kullanımdan kaldırma planını hazırla.
---

# Ürün/Özellik Kullanımdan Kaldırma Planı

## Amaç
Bir ürünü veya özelliği bilinçli biçimde emekliye ayırmak: savunulabilir bir karar, etkilenen her segment için bir geçiş yolu, müşterilerin harekete geçebileceği bir iletişim sırası ve kaybın kazançtan büyük olacağı durumda kapatmayı durduran kapılar.

## Ne zaman kullanılır
- Bir ürün, paket veya özelliğin kullanımı düşük, bakım maliyeti yüksek ya da daha yeni bir teklifle değiştirilmiş olduğunda.
- Birleşme veya yeniden platformlama sonrası örtüşen iki ürün tek ürüne indirilirken.
- Yönetim bir pazar segmentinden çıkma kararı aldığında ve uygulanabilir bir plan gerektiğinde.

## Ne zaman kullanılmaz
- Kaldırılan şey herkese açık veya iş ortağına yönelik bir API sözleşmesiyse `api-deprecation-plan` kullanılır (ürün kapatma bir API içeriyorsa ikisi birlikte kullanılır).
- Müşteriye yansıyan bir değişiklik olmadan yapılan teknik bir platform geçişiyse `migration-strategy` kullanılır.
- Onaylanmış bir plan için yalnızca duyuru metni gerekiyorsa `communication-plan` veya `release-announcement` kullanılır.

## Girdiler
Zorunlu:
- Neyin kaldırıldığı (ürün, özellik, paket) ve gerekçesi veya tetikleyicisi.

İsteğe bağlı, kaliteyi artırır:
- Segment bazında kullanım verisi, bağlı gelir, sözleşmesel taahhütler (SLA, bildirim süreleri, dönem sonu tarihleri).
- Varsa yerine geçen ürün veya alternatif ve özellik açıkları.
- Sürdürmenin iç maliyeti (destek, altyapı, güvenlik yamaları).
- Veri saklama ve dışa aktarma ile ilgili mevzuat kısıtları (KVKK/GDPR, sektör kuralları).

Kaldırılan öğe veya gerekçe yoksa sor. Diğer her şey `[BİLİNMİYOR]` ya da açık soru olur.

## Süreç
1. Kapatma kapsamını kesin olarak belirt (ne duruyor: satış, yeni kayıt, özellik, destek, veri erişimi) ve belirtilen gerekçeyi yaz; kendi çıkardığın gerekçeyi `[VARSAYIM]` olarak etiketle.
2. Kararı açık kriterlere göre sına: kullanım eğilimi, gelir ve sözleşme riski, sürdürme maliyeti, stratejik uyum, güvenlik/uyum riski ve alternatifin varlığı. Hangi kriterlerin kanıtlı, hangilerinin `[BİLİNMİYOR]` olduğunu kaydet; gerekçe zayıfsa yine de planlamak yerine bunu açıkça söyle.
3. Etkilenen müşterileri segmentlere ayır (ör. yoğun kullanıcılar, hafif kullanıcılar, stratejik/sözleşmeli hesaplar, entegrasyon yapanlar, iç ekipler) ve her segmentin etkisini nitel olarak tahmin et. Asla sayı veya gelir uydurma.
4. Her segment için geçiş yolunu tanımla: yerine geçen ürün, özellik açığı için geçici çözümler, veri dışa/içe aktarma, destekli geçiş, ticari teşvik veya düzgün çıkış. Uygulanabilir yolu olmayan segmentleri risk olarak işaretle.
5. Yükümlülükleri kontrol et: sözleşmesel bildirim süreleri, taahhüt edilen SLA'lar, imzalanmış yenilemeler, iadeler ve veri saklama/silme görevleri. Kişisel veri KVKK/GDPR'a göre müşteriye aktarılmalı veya silinmeli; örneklerde kişisel veriyi maskele.
6. Takvimi kapılı aşamalar olarak kur: duyuru, yeni satışın durdurulması, özellik dondurma, geçiş penceresi, salt okunur, kapatma, veri silme. Her kapının bir giriş koşulu (ör. taşınan aktif hesap oranı, stratejik hesaplardan açık P1 kaydı olmaması) ve sorumlusu olur.
7. Hedef kitle bazında iletişim sırasını hazırla: önce iç ekipler (satış, destek, müşteri başarısı, iş ortakları), sonra segment bazında müşteriler; kanal, kapatmaya göre zamanlama (T-eksi) ve harekete geçirme çağrısıyla. Tarih yaklaştıkça hatırlatmalar sıklaşır.
8. İç hazırlığı planla: destek SSS'si ve hazır yanıtlar, satış yönlendirmesi (neyin satılmayacağı), faturalama değişiklikleri, doküman bantları, ürün içi bildirimler ve kalan kullanımın izlenmesi.
9. Başarı ve durdurma metriklerini tanımla: geçiş oranı, kapatmaya bağlı kayıp (churn), destek kaydı hacmi, kapatma anındaki kalan kullanım. Kayıp üzerinde anlaşılan eşiği `[TBD]` aşarsa erteleme veya geri alma tetikleyicisi ekle.
10. Riskleri, varsayımları ve açık soruları listele, ardından şablonu doldur.
11. Sonraki becerileri öner: ayrıntılı mesajlar için `communication-plan`, teknik taşıma için `migration-strategy`, kapsamda API varsa `api-deprecation-plan`, bağlı sistemler için `impact-analysis`.

## Çıktı formatı
```markdown
# Kullanımdan Kaldırma Planı: <ürün / özellik>
| Alan | Değer |
|---|---|
| Kapsam | <ne duruyor> |
| Gerekçe | <gerekçe> |
| Yerine geçen | <ürün veya yok> |
| Karar sahibi | <ad veya [BİLİNMİYOR]> |
| Hedef kapatma | <tarih veya [TBD]> |

## Karar Kriterleri
| Kriter | Kanıt | Değerlendirme |
|---|---|---|

## Etkilenen Segmentler ve Geçiş Yolları
| Segment | Etki (Y/O/D) | Geçiş yolu | Açıklar / teşvik | Sorumlu |
|---|---|---|---|---|

## Yükümlülükler (sözleşme, SLA, veri)
- ...

## Takvim ve Kapılar
| Aşama | Hedef tarih | Giriş kapısı | Sorumlu |
|---|---|---|---|

## İletişim Sırası
| T-eksi | Hedef kitle | Kanal | Mesaj / harekete geçirme çağrısı |
|---|---|---|---|

## İç Hazırlık
- Destek / Satış / Faturalama / Doküman / Ürün içi: ...

## Metrikler ve Durdurma Tetikleyicileri
- ...

## Riskler, Varsayımlar, Açık Sorular
- [RİSK] ... / [VARSAYIM] ... / 1. <soru> — <sorumlu>
```

## Kalite kontrol listesi
- [ ] Karar kanıtlı kriterlere göre sınandı; zayıf kanıt gizlenmedi, açıkça belirtildi.
- [ ] Etkilenen her segmentin bir geçiş yolu var ya da yolu olmadığı açıkça işaretlendi.
- [ ] Sözleşmesel bildirim, SLA ve veri saklama/silme yükümlülükleri ele alındı.
- [ ] Her aşamanın ölçülebilir koşullu bir giriş kapısı ve sorumlusu var.
- [ ] İç ekipler müşterilerden önce bilgilendiriliyor.
- [ ] Hiçbir sayı, gelir veya tarih uydurulmadı; bilinmeyenler işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sözleşme koşullarına bakmadan tarih duyurmak. Önce bildirim sürelerini ve yenilemeleri envantere al; en geç biten yükümlülük en erken kapatma tarihini belirler.
- Tüm müşterilere tek mesaj göndermek. Stratejik ve entegrasyon yapan hesaplar daha erken, doğrudan temas ve destekli geçiş ister.
- Kapatmayı son adım saymak. Veri silme, faturalama temizliği, ölü kodun ve dokümanların kaldırılması da planın parçasıdır.
- Durdurma koşulu koymamak. Hangi kayıp veya eskalasyon seviyesinin kapatmayı erteleyeceğini önceden tanımla.

## Örnek
Girdi: "Eski raporlama modülünü gelecek yıl kapatıyoruz; herkes yeni analitik panoya geçecek."

Çıktıdan bir bölüm:
- Karar kriterleri: kullanım eğilimi `[BİLİNMİYOR – son 12 ayın aylık aktif hesap sayısını iste]`; alternatif var ama zamanlanmış e-posta dışa aktarımı yok `[VARSAYIM – açık listesini teyit et]`.
- "Zamanlanmış dışa aktarım kullananlar" segmenti: Etki Y; yol: dondurma kapısından önce yeni panoya zamanlanmış dışa aktarım ekle, olmazsa CSV API'si sun.
- "Salt okunur" kapısı: aktif hesapların en az `[TBD]`%'si pano oluşturmuş olmalı ve sözleşmeli hesaplardan açık eskalasyon bulunmamalı.
- İletişim: T-180 gün iç bilgilendirme; T-150 tüm kullanıcılara e-posta + ürün içi bant; T-60 stratejik hesaplara doğrudan temas; T-14 son hatırlatma.
