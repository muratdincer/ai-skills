---
description: Proje açılış toplantısını hazırlar; ekip ve sponsorlar için hedefleri, kapsamı, ekip ve rolleri, plan ve kilometre taşlarını, çalışma biçimini, riskleri ve ilk adımları içeren süreli gündem ile slayt slayt içerik üretir. Bir proje başlamak üzereyken ya da yeni bir faz veya büyük ekip değişikliği ortak bir başlangıç gerektirdiğinde kullanılır.
related: project-charter, scope-statement, stakeholder-register, communication-plan, meeting-agenda
prompt: Veri ambarı modernizasyon projemizin açılış toplantısını hazırla: 20 kişi, sponsor ilk 30 dakikaya katılıyor.
---

# Proje Açılış Toplantısı Hazırlığı

## Amaç
Sponsorları ve teslimat ekibini projenin neden var olduğu, başarının neye benzediği, kimin ne yaptığı ve ekibin nasıl çalışacağı konusunda hizalamak; böylece ilk haftalar netleştirmeyle değil uygulamayla geçer.

## Ne zaman kullanılır
- Başlatma belgesi onaylandığında ve ekip kurulurken.
- Değişen ekip, tedarikçi veya kapsamla yeni bir faz başlarken.
- Sorunlu bir proje yeniden başlatılırken ve sıfırlama gerektiğinde.

## Ne zaman kullanılmaz
- Proje henüz yetkilendirilmemişse `project-charter` kullanılır.
- Yalnızca rutin bir ekip toplantısı gerekiyorsa `meeting-agenda` kullanılır.
- Gereksinimleri açık, müşteriye dönük bir keşif oturumuysa `discovery-workshop` kullanılır.

## Girdiler
Zorunlu:
- Başlatma belgesi veya eşdeğer özet (hedefler, kapsam, sponsor).
- Katılımcılar ve ayrılan süre.

İsteğe bağlı, kaliteyi artırır:
- Taslak plan, kilometre taşları, ekip listesi, RACI, araçlar ve toplantı ritimleri.
- Bilinen riskler, hassas konular, sponsor beklentileri.

Başlatma özeti veya katılımcı/süre bilgisi yoksa iste.

## Süreç
1. Açılışın 3 çıktısını tanımla (ör. hedeflerin ortak anlaşılması, rollerde mutabakat, ilk 2 haftanın planlanması).
2. Gündemi kitleye göre böl: önce sponsor bölümü (neden, başarı, beklentiler), sonra ekip bölümü (nasıl).
3. Her maddeye süre ve sunucu ata; en az %20'yi soru ve etkileşime ayır.
4. Slayt içeriğini hazırla: bağlam ve neden şimdi, hedefler ve başarı ölçütleri, kapsam içi/dışı, teslimatlar ve kilometre taşları, organizasyon ve RACI, yönetişim ve ritimler, çalışma biçimi (araçlar, tanımlar, karar süreci), öncelikli riskler ve bağımlılıklar, sonraki adımlar.
5. Verilmemiş her tarih, isim ve sayıyı `[TBD]` olarak işaretle.
6. Etkileşimli bir bölüm ekle: risk beyin fırtınası, varsayım kontrolü veya beklenti turu.
7. Ön okuma listesi ve kararlarla aksiyonları içeren bir takip mesajı hazırla.
8. PM'in toplantıdan önce çözmesi gereken soruları listele.

## Çıktı formatı
```markdown
# Açılış Toplantısı: <proje>
Tarih <tarih> | Süre <x dk> | Katılımcılar <gruplar>
## Açılışın Çıktıları
1. ...
## Gündem
| Saat | Madde | Sunan | Kitle | Çıktı |
## Slayt İskeleti
1. Neden bu proje, neden şimdi – <ana mesaj>
2. Hedefler ve başarı ölçütleri – ...
3. Kapsam içi / dışı – ...
4. Kilometre taşları – ...
5. Ekip, roller ve RACI – ...
6. Yönetişim ve ritimler – ...
7. Çalışma biçimi – ...
8. Öncelikli riskler ve bağımlılıklar – ...
9. İlk 2 hafta – ...
## Etkileşimli Bölüm
## Ön Okumalar
## Açılış Öncesi Açık Noktalar
```

## Kalite kontrol listesi
- [ ] Her slaytın bir konu etiketi değil, tek bir ana mesajı var.
- [ ] Sponsor zamanı araç ayrıntılarına değil nedenlere ve beklentilere ayrıldı.
- [ ] Sürenin en az %20'si etkileşim veya soru-cevap.
- [ ] Roller ve karar yetkileri açık.
- [ ] Sonraki adımların sahibi ve tarihi var ya da `[TBD]`.

## Sık yapılan hatalar
- Tek yönlü sunum maratonu. Yapılandırılmış etkileşim ekle.
- Ekip doğrulamadan ayrıntılı planı kesinmiş gibi sunmak. Taslak olarak etiketle.
- Çalışma biçimini atlamak; ilk sürtüşmelerin çoğu belirsiz karar ve iletişim kurallarından doğar.

## Örnek
Girdi: "Veri ambarı modernizasyonu açılışı, 20 kişi, 2 saat, sponsor ilk 30 dakikada."

Çıktıdan bir bölüm:
| 0:00-0:10 | Neden şimdi: lisans bitişi ve raporlama gecikmeleri | Sponsor | Tümü | Ortak aciliyet |
| 0:40-1:10 | Risk ve varsayım beyin fırtınası | PM | Ekip | İlk RAID kayıtları |
- Açık nokta: Tedarikçi ekibi katılıyor mu, sözleşmede hangi rolle?
