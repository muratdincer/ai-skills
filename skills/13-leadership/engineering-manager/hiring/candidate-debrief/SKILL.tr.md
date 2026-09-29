---
description: Mülakat değerlendirme formlarını yetkinlik kapsama matrisi, çelişen sinyaller, çözülen ve çözülmeyen sorular ile seviyesiyle birlikte belgelenmiş bir işe alım kararı içeren yapılandırılmış bir toplantı özetine dönüştürür. Aday değerlendirme toplantısı hazırlanırken veya yapılırken, mülakatçılar anlaşamadığında ya da kararın kanıtı ve gerekçesiyle kayda geçmesi gerektiğinde kullanılır.
related: interview-scorecard, interview-plan, decision-log, onboarding-plan-30-60-90, bias-check
prompt: Bu dört değerlendirme formundan B adayının toplantı özetini çıkar ve kıdemli seviye için karar taslağı hazırla.
---

# Aday Değerlendirme Toplantısı Özeti

## Amaç
Bağımsız değerlendirme formlarını kanıta dayalı tek bir karara dönüştürmek: hangi yetkinlikler kapsandı, sinyaller nerede çelişiyor, toplantıda ne netleşti ve nihai işe alım kararı ile seviye neden seçildi.

## Ne zaman kullanılır
- Adayın tüm formları gönderildi ve değerlendirme toplantısı yapılmak üzere ya da yeni yapıldı.
- Mülakatçılar ciddi şekilde anlaşamıyor veya aynı yetkinliği farklı puanladı.
- Karar ve seviyenin işe alım komitesi, adaya geri bildirim veya sonraki denetim için yazılı gerekçesi gerekiyor.

## Ne zaman kullanılmaz
- Tek tek formlarda hâlâ kanıt eksikse önce `interview-scorecard` kullanılır.
- Tekrarlayan zayıf sinyaller nedeniyle sürecin yeniden tasarlanması gerekiyorsa `interview-plan` kullanılır.

## Girdiler
Zorunlu:
- Adayın gönderilmiş tüm değerlendirme formları (puanlar, kanıtlar, öneriler) ve hedef seviye.

İsteğe bağlı, kaliteyi artırır:
- Süreç tasarımı (hangi aşama hangi yetkinlikten sorumlu), seviye tanımları, toplantı tartışma notları.
- İşe alım çıtası politikası (ör. tek bir kesin hayır engeller mi, kim karar verir).

Herhangi bir aşamanın formu eksikse eksikliği listele ve o aşamanın sonucunu tahmin etme.

## Süreç
1. Tüm formların tartışmadan önce gönderildiğini doğrula; toplantı başladıktan sonra yazılan veya değiştirilenleri işaretle.
2. Kapsama matrisi kur: yetkinlik × aşama, puan ve tek satırlık kanıtla; sinyali olmayan veya zayıf yetkinlikleri işaretle.
3. Çelişkileri (aynı yetkinlik, farklı puan) belirle ve mülakatçının kıdemini değil, her iki tarafın kanıtını yaz.
4. Kanıtı izlenimden ayır: Davranışa dayanmayan ifadeleri ve işle ilgisiz yorumları çıkar veya işaretle.
5. Tartışmada neyin netleştiğini (yeni kanıt, ölçeğin ortak yorumu) ve neyin açık kaldığını kaydet.
6. Adayı süreçteki diğer adaylara göre değil, seviye çıtasına göre değerlendir; kanıt başka bir seviyeye uyuyorsa hangisi olduğunu ve nedenini belirt.
7. Kurumun karar kuralını uygula (ör. işe alım yöneticisi karar verir, kesin hayır ancak karşı kanıtla aşılır); hangi kuralın kullanıldığını yaz.
8. Önyargı kontrolü yap: tek güçlü aşamadan doğan hale etkisi, benzerlik/yakınlık, okul/geçmiş prestiji, değerleri tanımlanmamış "kültüre uyum", ilk konuşandan sonra oluşan grup düşüncesi.
9. Kararı, seviyeyi, oryantasyon için koşul veya riskleri ve aday için olgusal, saygılı bir geri bildirim taslağını yaz.
10. Aday kişisel verisini en aza indir ve politikaya göre saklama süresini not et (KVKK/GDPR).
11. Kullanıcının hedefi devam ediyorsa işe alım olduysa `onboarding-plan-30-60-90`, kararı kaydetmek için `decision-log` veya süreçte boşluk çıktıysa `interview-plan` öner.

## Çıktı formatı
```markdown
# Değerlendirme Toplantısı: <aday no> – <rol> – <hedef seviye> – <tarih>
Karar kuralı: <kural> · Karar veren: <rol>

## Kapsama Matrisi
| Yetkinlik | Aşama / mülakatçı | Puan | Ana kanıt |
|---|---|---|---|

## Çelişen Sinyaller
- <yetkinlik>: <A tarafı kanıtı> ve <B tarafı kanıtı> → <çözüldü / açık>

## Sinyal Boşlukları
- ...

## Karar
İşe al / Alma – Seviye: <seviye> – Gerekçe: <kanıta bağlı 3-5 cümle>
Riskler / oryantasyon odağı: ...

## Aday Geri Bildirim Taslağı
- ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Süreçteki her yetkinlik matriste kanıtla ya da işaretlenmiş bir boşlukla yer alıyor.
- [ ] Çelişkiler yalnızca kıdem veya çoğunluk oyuyla değil, kanıtla çözüldü.
- [ ] Karar diğer adaylara göre değil, seviye çıtasına göre verildi.
- [ ] İşle ilgisiz yorum veya tanımsız "uyum" argümanı kalmadı.
- [ ] Karar kuralı ve karar veren belirtildi.
- [ ] Aday geri bildirimi olgusal; iç puanlama ayrıntısı veya kişisel yorum içermiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İlk veya en kıdemli konuşanın herkesi çapalamasına izin vermek. Önce formları sessizce okuyun, sonra tartışın.
- Puanların ortalamasını almak. Seviye tanımı aksini söylemiyorsa eksik bir zorunlu yetkinlik başka alandaki mükemmellikle telafi edilmez.
- Kanıtı olmadan "güvenli olsun" diye adayı alt seviyeden almak. Seçilen seviyenin kanıtını yaz.

## Örnek
Girdi: 4 form, hedef Kıdemli. Tasarım Kesin evet, kodlama Evet, iş birliği Evet, işletilebilirlik Hayır ("izlemeden bahsetmedi").

Çıktıdan bir bölüm:
- Çelişki: İşletilebilirlik Hayır (sistem tasarımı, ipucu gerekti) ve Evet (kodlama aşaması, istenmeden yapılandırılmış loglama ekledi) → kanıtlar karşılaştırılarak "Evet, boşlukla" olarak çözüldü.
- Zayıf gerekçe (kaçın): "Herkes çok sevdi, kesin alalım."
- Güçlü gerekçe: "Tasarım ve ödünleşimlerde Kıdemli çıtasını karşılıyor (hata analiziyle outbox seçimi); işletilebilirlik kanıtı karışık; oryantasyon odağı: ilk 30 günde nöbet gölgeleme."
