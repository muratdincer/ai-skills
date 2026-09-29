---
name: performance-review
description: "Bir mühendis veya ekip üyesi için kanıta dayalı, yetkinliklerle uyumlu ve dengeli bir performans değerlendirmesi yazar; kalibre edilmiş puan gerekçesi, güçlü yönler, gelişim alanları ve sonraki dönem odağını içerir. Değerlendirme dönemi geldiğinde, birebir notları, ekip arkadaşı geri bildirimleri ve teslimat kanıtları yazılı bir değerlendirmeye dönüştürülürken veya taslak bir değerlendirme önyargı ve dayanaksız iddialar açısından kontrol edilirken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: people
  title: "Performans değerlendirmesi yazma"
  related: "career-ladder, goal-setting, one-on-one-notes, career-development-plan, feedback-sbi"
  prompt: "Bu notlardan, ekip arkadaşı geri bildirimlerinden ve hedeflerinden Can'ın yıllık değerlendirmesinin taslağını çıkar. Kariyer basamağımızdaki seviyesi Kıdemli Mühendis."
---

# Performans Değerlendirmesi Yazma

## Amaç
Kişinin adil bulacağı bir değerlendirme üretmek: her ifade tüm döneme ait kanıtla desteklenir, kurumun yetkinliklerine ve seviyesine eşlenir ve sonraki dönem için net bir yön verir.

## Ne zaman kullanılır
- Ara dönem veya yıllık değerlendirme yazılacak ya da tamamlanacaksa.
- Dağınık kanıtlar (birebir notları, hedef sonuçları, geri bildirimler, olaylar, teslim edilen işler) tek ve tutarlı bir değerlendirmeye dönüştürülecekse.
- Taslak değerlendirme kalibrasyondan önce önyargı ve kanıt kontrolünden geçecekse.

## Ne zaman kullanılmaz
- Resmi plan gerektiren süregelen performans açığı için `underperformance-plan` kullanılır.
- Sonraki dönem hedeflerini ayrıntılı belirlemek için `goal-setting` kullanılır.
- Seviye beklentilerinin kendisini tanımlamak için `career-ladder` kullanılır.

## Girdiler
Zorunlu:
- Kişinin rolü ve seviyesi, değerlendirme dönemi ve o döneme ait kanıtlar (notlar, hedef sonuçları, geri bildirim, iş örnekleri).

İsteğe bağlı, kaliteyi artırır:
- Yetkinlik çerçevesi veya kariyer basamakları ve tanımlarıyla puanlama ölçeği.
- Öz değerlendirme, ekip arkadaşı ve paydaş geri bildirimi, önceki değerlendirme.
- Bağlam: rol değişikliği, izin, yeniden yapılanma, nöbet yükü, iptal edilen projeler.

Puan ölçeği veya yetkinlik çerçevesi yoksa genel boyutları (etki, ustalık, iş birliği, sahiplenme, gelişim) kullan ve `[VARSAYIM]` olarak işaretle. Kanıt zayıfsa bunu açıkça söyle; boşluğu izlenimlerle doldurma.

## Süreç
1. Kanıt tablosu oluştur: tarih, gözlem, kaynak, yetkinlik. Yalnızca son haftaları değil tüm dönemi kapsa (yakınlık önyargısı).
2. Duyuma dayalı, kişiliğe dair veya korunan özelliklerle, izinle ya da kişisel koşullarla ilgili kanıtları çıkar veya işaretle.
3. Kanıtları yetkinliklere eşle ve ekip arkadaşlarıyla ya da yöneticinin kendi tarzıyla değil, seviyenin beklentileriyle karşılaştır.
4. Hedefler için sonucu hedefle karşılaştır ve sonucu değiştiren bağlamı (kapsam kesintisi, bağımlılıklar) yaz.
5. Güçlü yönleri somut örnekler ve ekibe, ürüne veya müşteriye etkileriyle yaz.
6. Gelişim alanlarını davranış olarak, her biri için en az bir örnekle ve bu seviyede "iyi"nin neye benzediğiyle yaz.
7. Ölçek tanımlarına bağlı bir puan ve kısa gerekçe öner; en güçlü karşı kanıtı da belirt.
8. Önyargı taraması yap: yakınlık, hale/boynuz etkisi, benzerlik, atıf (bireysel ve ekip katkısı), cinsiyetçi veya kodlanmış dil ("sert", "agresif" / "kararlı"), esnek çalışma veya izin nedeniyle cezalandırma.
9. Gelişim alanları ve kariyer hedefleriyle bağlantılı 2-4 sonraki dönem odağı belirle.
10. Kanıtsız her iddiayı `[KANIT GEREKLİ]` olarak işaretle ve yönetici için açık soruları listele.
11. Kullanıcının hedefi devam ediyorsa sonraki dönem hedefleri için `goal-setting` veya gelişim alanları için `career-development-plan` öner.

## Çıktı formatı
```markdown
# Performans Değerlendirmesi: <ad> – <dönem>
Rol / seviye: <rol, seviye> · Değerlendiren: <yönetici> · Puan: <öneri> [taslak]

## Özet (3-4 cümle)

## Hedef Sonuçları
| Hedef | Hedeflenen | Gerçekleşen | Bağlam |
|---|---|---|---|

## Yetkinlik Değerlendirmesi
| Yetkinlik | Seviye beklentisi | Kanıt (tarih, kaynak) | Değerlendirme |
|---|---|---|---|

## Güçlü Yönler
- <davranış> – <örnek> – <etki>

## Gelişim Alanları
- <davranış> – <örnek> – <bu seviyede iyi olan>

## Puan Gerekçesi
<ölçek tanımına göre neden bu puan; en güçlü karşı kanıt>

## Sonraki Dönem Odağı
1. ...

## Açık Sorular / Kanıt Eksikleri
- [KANIT GEREKLİ] ...
```

## Kalite kontrol listesi
- [ ] Her güçlü yön ve gelişim alanının tarihli ve kaynaklı en az bir örneği var.
- [ ] Kanıtlar tüm dönemi kapsıyor.
- [ ] Değerlendirme başka kişilere göre değil, seviye beklentilerine göre yapıldı.
- [ ] Kişilik etiketleri, kodlanmış dil veya izin, sağlık, aile ya da diğer korunan özelliklere atıf yok.
- [ ] Dönem içinde geri bildirim verildiyse değerlendirmedeki hiçbir şey sürpriz olmaz.
- [ ] Notlardaki kişisel veriler değerlendirmenin ihtiyacı kadarına indirildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yakınlık önyargısı. Metni yazmadan önce tüm döneme ait kanıt tablosunu oluştur.
- Görünür işleri (lansmanlar) takdir edip görünmeyen emeği (mentorluk, kod incelemeleri, olay sonrası takipler) atlamak. Bunları açıkça sor.
- Belirsiz gelişim alanları ("daha stratejik ol"). Davranışı ve beklenen davranışın somut bir örneğini yaz.

## Örnek
Girdi: Kıdemli Mühendis, ilk yarı değerlendirmesi; notlarda önbellek yeniden tasarımına liderlik ettiği (p95 %40 düşüş), iki ekip arkadaşının kod incelemelerinin yavaş olduğunu söylediği, yeniden yapılanma nedeniyle bir hedefin kaçırıldığı yazıyor.

Çıktıdan bir bölüm:
- Güçlü yön: Teknik liderlik – önbellek yeniden tasarımına liderlik etti (Mart, tasarım dokümanı + devreye alma); ekip panosuna göre p95 gecikme %40 düştü.
- Gelişim alanı: İnceleme hızı – iki ekip arkadaşı PR'ların 2-3 gün beklediğini belirtiyor (geri bildirim, Mayıs); kıdemli seviyede incelemelerin başkalarının önünü bir gün içinde açması beklenir `[basamak ifadesini teyit et]`.
- Hedef bağlamı: "Raporlama servisinin taşınması" gerçekleşmedi; proje Nisan'daki yeniden yapılanmayla durduruldu, performansa bağlanamaz.
