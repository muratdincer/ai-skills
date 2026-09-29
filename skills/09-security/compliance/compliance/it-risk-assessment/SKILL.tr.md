---
name: it-risk-assessment
description: "Bir varlık veya hizmet kapsamı için BT ve bilgi güvenliği riskini değerlendirir: varlıkları, tehditleri ve zafiyetleri belirler, mevcut kontrollerle olasılık ve etkiyi puanlar, işleme seçeneğine (azaltma, transfer, kaçınma, kabul) karar verir ve her risk için bir risk kaydı üretir. ISO 27001 risk değerlendirmesi kurulurken veya yenilenirken, yeni bir tedarikçi, sistem ya da değişiklik değerlendirilirken, risk kabulü hazırlanırken veya yönetim bir şeyin ne kadar riskli olduğunu sorduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: compliance
  area: compliance
  title: "BT risk değerlendirmesi"
  related: "threat-model, risk-register, control-mapping, vulnerability-triage, privacy-impact-assessment"
  prompt: "Şirket içi ERP'mizi barındırılan bir bulut sağlayıcıya taşımanın BT riskini, tedarikçi ve veri riskleri dahil değerlendir."
---

# BT Risk Değerlendirmesi

## Amaç
Karar vericilere hangi bilgi risklerinin en önemli olduğunu, nedenini ve önerilen işleme yöntemini şeffaf ve tekrarlanabilir biçimde göstermek. Böylece kaynaklar en büyük risklere gider ve kalan risk, hesap veren bir sahip tarafından bilinçli olarak kabul edilir.

## Ne zaman kullanılır
- Bir BGYS risk değerlendirmesi kurulurken veya yenilenirken (ISO/IEC 27001 madde 6.1.2, ISO/IEC 27005 ile uyumlu yöntem).
- Yeni bir sistem, tedarikçi, dış kaynak kullanımı veya büyük bir değişiklik onaydan önce değerlendirilirken.
- Bir zafiyet veya kontrol eksiği zamanında giderilemiyor ve resmi risk kabulü gerekiyorsa.
- Yönetim veya denetçi güvenlik önceliklerinin gerekçesini sorduğunda.

## Ne zaman kullanılmaz
- Tek bir sistemin bileşen bazında tasarım tehditleri gerekiyorsa `threat-model` kullanılır.
- Risk bir proje teslim riskiyse (takvim, bütçe, kapsam) `risk-register` kullanılır.
- Konu tek bir zafiyetin önem derecesi ve düzeltme takvimiyse `vulnerability-triage` kullanılır.

## Girdiler
Zorunlu:
- Kapsam: değerlendirilen varlıklar, hizmetler, süreçler veya değişiklik.

İsteğe bağlı, kaliteyi artırır:
- Kurumun risk metodolojisi (ölçekler, risk iştahı, kabul yetkisi).
- Sahipleri ve sınıflandırmasıyla varlık envanteri, mevcut kontroller, olay geçmişi, denetim bulguları.
- İş etkisi bilgisi (kritik süreçler, RTO/RPO, KVKK veya BDDK gibi yasal yükümlülükler).

Kapsam yoksa iste. Metodoloji yoksa 5x5 veya 3x3 olasılık-etki ölçeği öner ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Kapsamı ve bağlamı teyit et: iş hedefleri, iç ve dış etkenler, yasal yükümlülükler, risk iştahı ve hangi risk seviyesini kimin kabul edebileceği.
2. Puanlama ölçeklerini tanımla veya benimse: olasılık (sıklık veya maruziyet çapalarıyla) ve gizlilik, bütünlük, erişilebilirlik, finansal, yasal, itibar ve ilgili kişiye zarar boyutlarında etki. Puanların tekrarlanabilir olması için çapaları yaz.
3. Kapsamdaki varlıkları (bilgi, uygulamalar, altyapı, insanlar, tedarikçiler) sahibi ve sınıflandırmasıyla belirle.
4. Her varlık veya varlık grubu için gerçekçi tehdit-zafiyet çiftlerini belirle. Tek kelimeler yerine senaryo kullan ("yamasız VPN cihazı üzerinden fidye yazılımı ERP veritabanını şifreler").
5. Mevcut kontrolleri kaydet ve etkinliklerini kanıta dayanarak değerlendir; planlanan veya belgelenmemiş kontrolleri hesaba katma.
6. Doğal (isteğe bağlı) ve mevcut riski puanla: olasılık x etki, her puan için tek satırlık gerekçe.
7. Risk iştahıyla karşılaştır. İştahın üzerindeki riskler için işleme yöntemini seç: azalt (sorumlu ve tarihli kontroller), transfer et (sigorta, sözleşme), kaçın (faaliyeti durdur) veya kabul et (sahip, gerekçe, bitiş tarihi, gözden geçirme tarihi).
8. İşleme sonrası hedef kalan riski puanla ve işleme aksiyonlarını kontrollere (gerekirse ISO 27001 Ek A numaraları) ve Uygulanabilirlik Bildirgesi'ne bağla.
9. Kişisel veri risklerini belirle ve ayrıca kişisel veri etki değerlendirmesi gereken yerleri işaretle.
10. Risk kaydını, ısı haritası özetini ve yönetim için en önemli riskleri gereken kararlarla birlikte üret.
11. Varsayılan olgulara dayanan her puanı `[VARSAYIM]` olarak işaretle; sonra derinlemesine inceleme için `threat-model`, işleme aksiyonlarını bir standarda hizalamak için `control-mapping` veya ilgili kişi riskleri için `privacy-impact-assessment` öner.

## Çıktı formatı
```markdown
# BT Risk Değerlendirmesi: <kapsam> (<tarih>, yöntem: <ad / [VARSAYIM]>)
## Bağlam ve Kriterler
- Risk iştahı: ... / Kabul yetkisi: ... / Ölçekler: olasılık 1-5, etki 1-5, çapalarıyla
## Varlık Envanteri (kapsam içi)
| Varlık | Sahibi | Sınıflandırma |
## Risk Kaydı
| No | Varlık | Tehdit senaryosu | Zafiyet | Mevcut kontroller | O | E | Mevcut risk | İşleme | Aksiyon / kontrol | Sorumlu | Tarih | Hedef kalan risk |
## Isı Haritası Özeti
- Yüksek: R3, R7 / Orta: ... / Düşük: ...
## Gereken Kararlar
- R3: kabul / azaltmayı finanse et – karar sahibi
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Puanlama ölçeklerinin yazılı çapaları var ve tutarlı uygulandı.
- [ ] Her risk bir varlığa, tehdide ve zafiyete bağlı somut bir senaryo.
- [ ] Mevcut kontroller yalnızca kanıtla hesaba katıldı; planlanan kontroller sayılmadı.
- [ ] İştahın üzerindeki her riskin sorumlu ve tarihli bir işleme aksiyonu ya da yetkili ve süreli bir kabulü var.
- [ ] Kişisel veri riskleri gerektiğinde kişisel veri etki değerlendirmesi için işaretlendi.
- [ ] Parasal tutarlar ve olasılıklar uydurulmadı; bilinmeyenler `[BİLİNMİYOR]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tehditleri tek başına puanlamak ("hackerlar: Yüksek"). Senaryoyu her zaman belirli bir varlık ve zafiyete karşı puanla.
- Riskleri süresiz kabul etmek. Her kabulün bir bitiş tarihi ve gözden geçirme tetikleyicisi olmalı.
- Puanları en yüksek sesle konuşan paydaşa bırakmak. Yazılı çapaları kullan ve gerekçeyi kaydet.
- Raporlamada doğal ve kalan riski karıştırmak; bu, kontrol yatırımını görünmez kılar.

## Örnek
Girdi: "Şirket içi ERP'yi barındırılan bir bulut sağlayıcıya taşıma."

Çıktıdan bir bölüm:
| R4 | ERP verisi | Sağlayıcı yönetici kötüye kullanımı veya ihlali müşteri ve bordro verisini ifşa eder | Paylaşılan sorumluluk belirsiz, müşteri yönetimli anahtar yok | Sağlayıcının ISO 27001 sertifikası [VARSAYIM: SoA incelenmedi] | 3 | 5 | Yüksek | Azalt | Üzerinde anlaşılan süre içinde ihlal bildirimi için sözleşme maddesi, müşteri yönetimli şifreleme anahtarları, sağlayıcının SOC 2 raporunun incelenmesi | BT Direktörü | [TBD] | Orta |
| R6 | ERP verisi | Çalışan kişisel verilerinin geçerli bir KVKK md. 9 mekanizması olmadan yurt dışına aktarılması | Barındırma bölgesi sabit değil | Yok | 4 | 4 | Yüksek | Azalt | Bölgeyi sabitle veya aktarım mekanizmasını kur; kişisel veri etki değerlendirmesi yap | Veri koruma sorumlusu | [TBD] | Düşük |
