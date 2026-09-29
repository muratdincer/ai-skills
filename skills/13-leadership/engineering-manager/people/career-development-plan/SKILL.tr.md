---
name: career-development-plan
description: "Kişinin mevcut seviyesini hedef seviye veya kariyer yoluyla karşılaştıran, yetkinlik bazında kanıta dayalı eksikleri belirleyen ve gelişim aksiyonlarını, fırsatları, desteği ve kontrol noktalarını tanımlayan bir kariyer gelişim planı oluşturur. Biri terfi veya yol değişikliği (uzman ya da yönetici, uzmanlaşma) sorduğunda, bir değerlendirmeden sonra veya yöneticinin yapılandırılmış bir gelişim konuşmasına ihtiyacı olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: people
  title: "Kariyer gelişim planı"
  related: "career-ladder, goal-setting, performance-review, one-on-one-prep, onboarding-plan-30-60-90"
  prompt: "18 ay içinde Staff seviyesine geçmek isteyen Kıdemli Mühendis Burak için gelişim planı oluştur."
---

# Kariyer Gelişim Planı

## Amaç
Gelişimi somutlaştırmak: kişi bugün nerede, nereye gitmek istiyor, ikisini tam olarak ne ayırıyor ve hangi deneyimler ve destek bu farkı kapatacak.

## Ne zaman kullanılır
- Bir kişi terfi veya farklı bir yol için neye ihtiyacı olduğunu sorduğunda.
- Değerlendirme sonrasında gelişim alanlarını uzun vadeli bir plana dönüştürmek için.
- Rol değişikliği (teknik lider, yönetici, mimar, alan uzmanı) değerlendirilirken.

## Ne zaman kullanılmaz
- Yalnızca tek bir değerlendirme döneminin hedefleri için `goal-setting` kullanılır.
- Düşük performans için iyileştirme planı gerekiyorsa `underperformance-plan` kullanılır.
- Kurum için seviye beklentilerini tanımlamak için `career-ladder` kullanılır.

## Girdiler
Zorunlu:
- Mevcut rol ve seviye, kişinin kendi ifadesiyle hedef seviye veya yol ve kariyer basamakları ya da yetkinlik beklentileri (veya genel beklentilerin kullanılmasına izin).

İsteğe bağlı, kaliteyi artırır:
- Son değerlendirme, öz değerlendirme, ekip arkadaşı geri bildirimi, iş örnekleri.
- İş bağlamı: yaklaşan projeler, ekip ihtiyaçları, terfi süreci ve zamanlaması.
- Kısıtlar: ayrılabilecek zaman, eğitim bütçesi, lokasyon, çalışma düzeni.

Hedef yalnızca yöneticiden geliyorsa önce kişinin kendi beklentisini teyit et. Kariyer basamağı yoksa genel boyutları kullan ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Kişinin hedefini kendi sözleriyle ve arkasındaki motivasyonla yeniden yaz.
2. Her yetkinlik için mevcut kanıtı ve hedef seviye beklentisini yan yana kaydet.
3. Her eksiği (yok / küçük / belirgin) kanıtla derecelendir; izlenime göre derecelendirme.
4. Hedef için en yüksek kaldıraca sahip 2-3 öncelikli eksik seç; gerisini beklet.
5. Her öncelikli eksik için 70-20-10 karışımını planla: gerçek işte zorlayıcı deneyimler, koçluk veya mentorluk ve resmi eğitim.
6. Somut fırsatları (projeler, sahiplik alanları, liderlik edilecek incelemeler) belirle ve bunların görünür birkaç kişiye ayrılmadığını, ekip içinde adil dağıtıldığını kontrol et.
7. Eksiğin kapandığını gösterecek gözlemlenebilir kanıtı tanımla.
8. Yönetici taahhütlerini listele: sponsorluk, görünürlük, zaman, bütçe, tanıştırmalar.
9. Kontrol noktaları belirle ve planın neyi garanti etmediğini açıkça yaz (terfi; sürece, iş ihtiyacına ve gösterilen kanıta bağlıdır).
10. Onaylanmamış maddeleri `[VARSAYIM]` veya `[TBD]` olarak işaretle.
11. Kullanıcının hedefi devam ediyorsa aksiyonları dönem hedeflerine çevirmek için `goal-setting` veya ilerleme görüşmelerini planlamak için `one-on-one-prep` öner.

## Çıktı formatı
```markdown
# Kariyer Gelişim Planı: <ad>
Mevcut: <rol, seviye> · Hedef: <seviye / yol> · Süre: <ay> · Güncelleme: <tarih>

## Hedef (kendi sözleriyle)

## Eksik Analizi
| Yetkinlik | Mevcut kanıt | Hedef beklenti | Eksik |
|---|---|---|---|

## Öncelikli Eksikler ve Aksiyonlar
| Eksik | Deneyim (iş başında) | Koçluk / mentor | Eğitim | İlerleme kanıtı | Tarih |
|---|---|---|---|---|---|

## Yönetici Taahhütleri
- ...

## Kontrol Noktaları
- <tarih>: <neyi gözden geçireceğiz>

## Bu Planın Garanti Etmedikleri
- ...

## Açık Noktalar
- [TBD] ...
```

## Kalite kontrol listesi
- [ ] Hedef varsayılmadı; kişiye ait ve teyit edildi.
- [ ] Her eksik, belirtilmiş bir beklentiye karşı kanıtla destekleniyor.
- [ ] En fazla üç öncelikli eksik var.
- [ ] Aksiyonların çoğu yalnızca kurs değil, iş başında deneyim.
- [ ] Yönetici taahhütleri ve kontrol noktaları açık.
- [ ] Terfi zamanlamasına dair beklentiler gerçekçi ve söz verilmedi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tamamen eğitim ve sertifikalardan oluşan planlar. Kıdemli seviyelerde gelişim kapsam ve sahiplikten gelir.
- Terfi tarihi vaat etmek. Sonuca değil, plana ve kanıta taahhüt ver.
- Herkesin yöneticilik istediğini varsaymak. Uzman ve yönetici yollarını eşit seçenekler olarak sun.

## Örnek
Girdi: "Burak, Kıdemli Mühendis, 18 ay içinde Staff olmak istiyor."

Çıktıdan bir bölüm:
| Ekipler arası teknik etki | Kendi ekibinde tasarımlara liderlik ediyor | 2+ ekibin kararlarını şekillendirir `[basamak ifadesini teyit et]` | Belirgin |
- Aksiyon: Sipariş ve faturalama ekipleri arasında event şema yönetişimi önerisini sahiplenmek; mentor: principal mühendis; kanıt: önerinin iki ekip tarafından benimsenmesi.
- Garanti etmez: Staff terfisi kalibrasyona ve açık bir iş ihtiyacına bağlıdır.
