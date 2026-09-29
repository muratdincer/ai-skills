---
description: Mülakatçının ham notlarını yetkinlik başına birebir kanıt, ölçeğe dayalı puan ve gerekçeli, bağımsız bir işe alım önerisi içeren bir değerlendirme formuna dönüştürür. Mülakattan hemen sonra, notların değerlendirme toplantısından önce yazılması gerektiğinde ya da bir formu eksik kanıt, önyargı veya olgu gibi sunulan izlenimler açısından kontrol ederken kullanılır.
related: technical-interview-questions, candidate-debrief, interview-plan, bias-check
prompt: B adayıyla yaptığım sistem tasarımı mülakatının notları burada. Kıdemli seviye ölçeğimize göre değerlendirme formuna dönüştür.
---

# Mülakat Değerlendirme Formu

## Amaç
Adayın gerçekte ne söyleyip ne yaptığını, bu aşamanın sorumlu olduğu yetkinliklere eşleyerek kaydetmek. Böylece işe alım kararı mülakatçının genel izlenimine değil, karşılaştırılabilir kanıtlara dayanır.

## Ne zaman kullanılır
- Mülakat yeni bitti ve notlar değerlendirme toplantısından önce forma dönüşmeli.
- Gönderilmiş bir form yalnızca sıfatlar içeriyor ("zeki", "yeterince kıdemli değil") ve kanıta ihtiyaç var.
- İşe alım yöneticisi formların ölçekle tutarlılığını kontrol etmek istiyor.

## Ne zaman kullanılmaz
- Aşamanın soruları ve ölçeği henüz yoksa `technical-interview-questions` kullanılır.
- Birden fazla formu birleştirip karara bağlamak için `candidate-debrief` kullanılır.
- Hangi aşamanın hangi yetkinliği ölçeceğini tasarlamak için `interview-plan` kullanılır.

## Girdiler
Zorunlu:
- Mülakatçının notları (mümkün olduğunca birebir) ve bu aşamaya atanmış yetkinlikler.

İsteğe bağlı, kaliteyi artırır:
- Seviye dereceleriyle aşama ölçeği, hedef seviye, sorulan soru ve verilen ipuçları.
- Kurumun öneri ölçeği (ör. kesin hayırdan kesin evete).

Atanmış yetkinlikler yoksa sor. Ölçek yoksa genel derecelerle dört dereceli bir ölçek kullan ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Formu bağımsız yaz: Önce diğer mülakatçıların geri bildirimlerini veya değerlendirme kanalını okuma (çapalama etkisi).
2. Notlardan gözlemleri yaklaşık zamanıyla davranış ve alıntı olarak çıkar; adayın yaptığını mülakatçının yorumundan ayır.
3. Her gözlemi atanmış bir yetkinliğe eşle; başka aşamaların yetkinliklerine ait gözlemleri kısa bir "diğer sinyaller" satırına bırak.
4. Her yetkinliği en iyi uyan ölçek derecesine göre kanıtını belirterek puanla; kanıt yetersizse tahmin etme, "yeterli sinyal yok" yaz.
5. Verilen ipuçlarını ve aşamanın ipucu politikasına göre sonucu nasıl etkilediğini not et.
6. İşle ilgisiz içeriği çıkar veya işaretle: dış görünüş, aksan, yaş, aile, uyruk, okul/geçmiş prestiji, tanımı olmayan "kültüre uyum" ve heyecan/gerginlik yorumları.
7. Genel öneriyi kurumun ölçeğinde yaz; 2-4 cümlelik gerekçede en güçlü destekleyici ve en güçlü karşı kanıtı belirt.
8. Sonraki mülakatçıların veya değerlendirme toplantısının derinleştirmesi gerekenleri açık sorular olarak listele.
9. Kişisel veriyi en aza indir: Yalnızca kararın ihtiyaç duyduğunu tut ve aday verisinin saklama kurallarını (KVKK/GDPR) hatırlat.
10. Kullanıcının hedefi devam ediyorsa tüm formlar tamamlandığında `candidate-debrief` veya ifadelerin ikinci bir gözden geçirmesi için `bias-check` öner.

## Çıktı formatı
```markdown
# Değerlendirme Formu: <aday no> – <aşama> – <mülakatçı> – <tarih>
Hedef seviye: <seviye> · Soru: <başlık> · Verilen ipuçları: <liste veya yok>

## Yetkinlik Bazında Kanıt
| Yetkinlik | Kanıt (davranış / alıntı, zaman) | Ölçek derecesi | Puan |
|---|---|---|---|

## Diğer Sinyaller (burada puanlanmaz)
- ...

## Öneri
<Kesin hayır / Hayır / Evet / Kesin evet> – <en güçlü lehte ve aleyhte kanıtla gerekçe>

## Derinleştirilecekler
- ...

## Veri İşleme Notu
- Kişisel veri en aza indirildi; saklama süresi politikaya göre [TBD].
```

## Kalite kontrol listesi
- [ ] Her puan en az bir somut davranışa veya alıntıya dayanıyor.
- [ ] Yalnızca bu aşamaya atanmış yetkinlikler puanlandı; eksikler "yeterli sinyal yok" olarak belirtildi.
- [ ] Dış görünüş, aksan, yaş, aile, köken, okul prestiji veya tanımsız "uyum" referansı yok.
- [ ] Yorumlar yorum olarak etiketlendi ve gözlemlerden ayrıldı.
- [ ] Öneri gerekçesi karşı kanıtı da içeriyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Önce karar verip sonra kanıt seçmek. Puan veya öneriyi seçmeden önce kanıt sütununu doldur.
- Farklı ama geçerli bir yaklaşımı cezalandırmak. Mülakatçının kendi çözümüne göre değil, ölçeğe göre puanla.
- "Yeterli sinyal yok"u hayır saymak. Bunu değerlendirme toplantısı için işaretle.

## Örnek
Girdi notlar: "Gergin görünüyordu. Önce ölçeği sordu. Outbox desenini seçti, çift yazmaya göre nedenini açıkladı. İzlemeye ancak hatırlatınca değindi."

Çıktıdan bir bölüm:
- Zayıf kayıt (kaçın): "Gergin, fena olmayan tasarım, muhtemelen orta seviye."
- Güçlü kayıt: Ödünleşimler – "Outbox'ı çift yazmayla karşılaştırdı, iki yazma arasında çökme olursa olay kaybolacağı için outbox'ı seçti" (22. dk) – derece Evet.
- İşletilebilirlik – alarmı ancak 45. dakikadaki ipucundan sonra andı – derece Hayır (politikaya göre ipucu puanı düşürür).
- Çıkarıldı: "gergin görünüyordu" (işle ilgili değil).
