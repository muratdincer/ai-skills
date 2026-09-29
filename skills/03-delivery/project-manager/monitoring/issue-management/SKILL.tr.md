---
name: issue-management
description: "Tek bir proje sorununu kayıttan kapanışa kadar yönetir; sorunu net biçimde tanımlar, etkisini ve aciliyetini değerlendirir, nedenini bulur, sahip ve tarihlerle çözüm planı kurar, eskalasyon tetikleyicilerini ve kapanış kriterlerini belirler ve doğrulanmış çözüme kadar izler. Engellenen bir ekip, aksayan bir bağımlılık, tedarikçi gecikmesi veya gerçekleşmiş bir risk gibi, şu anda ters giden ve kapsamı, takvimi, maliyeti ya da kaliteyi etkileyen bir durum olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: monitoring
  title: "Sorun yönetimi"
  related: "raid-log, escalation-message, five-whys, change-control, decision-log"
  prompt: "Test ortamımız 4 gündür çalışmıyor ve tedarikçi sürekli erteliyor. Bunu bir sorun olarak kaydedip eskalasyon yoluyla yönetmeme yardım et."
---

# Sorun Yönetimi

## Amaç
Canlı bir problemi, etkisi ve eskalasyon kuralları görünür, sahibi net ve süreye bağlı bir çözüm yoluna dönüştürmek. Böylece sorun, projeye sessizce zarar vermeden çözülür ya da karara bağlanır.

## Ne zaman kullanılır
- Bir risk gerçekleştiğinde veya beklenmedik bir problem işi şu anda engellediğinde.
- Bir sorun çok uzun süredir açıksa, ekipler arasında gidip geliyorsa ya da sahibi yoksa.
- Sponsor "sorun tam olarak ne ve ne yapıyoruz?" diye sorduğunda.

## Ne zaman kullanılmaz
- Çok sayıda risk, varsayım, sorun ve bağımlılık birlikte izlenecekse `raid-log` kullanılır.
- Henüz gerçekleşmemiş, olabilecek bir durumsa `risk-register` kullanılır.
- Canlı kullanıcıları etkileyen bir üretim olayıysa `incident-response` kullanılır.

## Girdiler
Zorunlu:
- Ne olduğunun ve ne zamandan beri sürdüğünün açıklaması.

İsteğe bağlı, kaliteyi artırır:
- Etkilenen teslimatlar, kilometre taşları veya ekipler; denenmiş aksiyonlar.
- Eskalasyon matrisi, sözleşme veya SLA koşulları, RAID kayıt numaraları.

Açıklama yoksa iste. Etki değerlendirmesini engelleyen konularda bir seferde en fazla bir odaklı soru sor.

## Süreç
1. Sorun tanımını gözlemlenebilir olgular olarak yaz: ne oluyor, nerede, ne zamandan beri, kanıt. Yorumları ayrı tut ve `[VARSAYIM]` olarak işaretle.
2. Kapsam, takvim (kritik yolda mı), maliyet, kalite ve kişiler üzerindeki etkiyi değerlendir; yalnızca verilen veriyle sayısallaştır, aksi halde nitel seviyeler kullan.
3. Önceliği etki ve aciliyetten belirle; verildiyse "her gecikme gününün maliyetini" sözle veya sayıyla belirt.
4. Nedeni belirle: belirtiyi, doğrudan nedeni ve kök nedeni ayır; bilinmiyorsa tahmin yürütmek yerine ilgili kişilerle kısa bir teşhis planla (ör. beş neden).
5. Harekete geçme yetkisi olan tek bir hesap verebilir sahip ata; katkı verenleri ayrı listele.
6. Sınırlama (hasarı şimdi durdur) ve çözüm (nedeni gider) aksiyonlarını her biri sahip ve bitiş tarihiyle tanımla.
7. Eskalasyon tetikleyicilerini tanımla: ilerlemesiz geçen süre, etki eşiği veya kaçırılan aksiyon tarihi; bir sonraki eskalasyon seviyesi ve kanalı.
8. Doğrulanabilir kapanış kriterleri tanımla ("çözüldü" değil, ör. "ortam 3 iş günü kesintisiz çalıştı").
9. Sonuçları bağla: temel plan etkileniyorsa değişiklik talebi aç, RAID kayıtlarını güncelle, kararları kaydet.
10. Durum güncellemelerini tarih, değişen şey ve sonraki kontrolle izle; kısa bir kapanış notu ve derslerle kapat.
11. Kullanıcının hedefi devam ediyorsa eskalasyon için `escalation-message`, temel plan değişecekse `change-control` ya da geniş kayıtta tutmak için `raid-log` öner.

## Çıktı formatı
```markdown
# Sorun I-<no>: <kısa başlık>
| Alan | Değer |
|---|---|
| Bildiren / tarih | <...> |
| Sahip (hesap verebilir) | <ad/rol veya [BİLİNMİYOR]> |
| Öncelik | <Kritik/Yüksek/Orta/Düşük> – <gerekçe> |
| Durum | Açık / Devam ediyor / Eskale edildi / Çözüldü / Kapandı |
| Bağlı kayıtlar | <risk, bağımlılık, CR numaraları> |

## Sorun Tanımı (olgular)
## Etki
| Boyut | Etki | Kanıt |
## Neden
- Belirti / doğrudan neden / kök neden (veya teşhis planı)
## Aksiyonlar
| # | Tür (sınırlama/çözüm) | Aksiyon | Sahip | Bitiş | Durum |
## Eskalasyon Tetikleyicileri
- <tarih> itibarıyla <koşul> ise → <kanal> ile <seviye>'ye eskale et
## Kapanış Kriterleri
## Durum Geçmişi
| Tarih | Güncelleme | Sonraki kontrol |
```

## Kalite kontrol listesi
- [ ] Tanım suçlama veya çözüm değil, olgu ve kanıt içeriyor.
- [ ] Yetkili tek bir hesap verebilir sahip belirtildi ya da `[BİLİNMİYOR]` olarak işaretlendi.
- [ ] Sınırlama ve çözüm aksiyonları ayrıldı, her birinin sahibi ve tarihi var.
- [ ] Eskalasyon tetikleyicileri somut ve süreye bağlı.
- [ ] Kapanış kriterleri doğrulanabilir.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sahip olarak bir ekibi veya "tedarikçi"yi yazmak; kimse harekete geçmez. Yetkili bir kişi veya rol yaz.
- Neden ortadan kalkmadan geçici çözümle kapatmak. Bir çözüm aksiyonu bırak ya da kalan riski kaydet.
- Eskalasyonu başarısızlık gibi hissettirdiği için geciktirmek. Tetikleyicileri baştan kararlaştır ki eskalasyon olağan olsun.

## Örnek
Girdi: "Test ortamı 4 gündür kapalı; tedarikçi düzeltmeyi sürekli erteliyor."

Çıktıdan bir bölüm:
- Tanım: Entegrasyon test ortamı `[tarih]`ten beri erişilemez (4 iş günü); tedarikçinin verdiği 2 düzeltme tarihi kaçırıldı.
- Etki: Sistem testi engellendi; kritik yolda; her gün UAT başlangıcını bir gün geciktiriyor `[VARSAYIM: bolluk yok]`.
- Sınırlama: API testlerini mock'lara karşı çalıştır – Sahip QA lideri – Bitiş `[tarih]`.
- Eskalasyon: `[tarih]`e kadar düzelmezse önce tedarikçi müşteri yöneticisine, sonra SLA uyarınca sözleşme sahibine eskale et.
