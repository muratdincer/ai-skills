---
description: Ham toplantı notlarını, sohbet kayıtlarını veya bir dökümü; tartışma noktalarını, kararları, aksiyonları ve açık soruları ayıran, gerektiğinde konuşmacıyı belirten konu bazlı yapılandırılmış notlara dönüştürür. Dağınık notlar veya bir döküm paylaşılıp konuşulanların "toparlanması", "yapılandırılması" ya da "yazıya dökülmesi" istendiğinde kullanılır.
related: transcript-cleanup, meeting-summary, action-item-extraction, decision-log, open-questions-tracker
prompt: Platform ekibiyle bugünkü sprint planlamasından ham notlarım bunlar. Bunları yapılandırılmış toplantı notlarına çevir.
---

# Yapılandırılmış Toplantı Notu Tutma

## Amaç
Konuşulanların konuya göre gruplanmış, sadık ve hızla taranabilir bir kaydını üretmek. Böylece katılanlar ve katılamayanlar toplantıyı yeniden dinlemeden kararları, taahhütleri ve açık konuları bulabilir.

## Ne zaman kullanılır
- Ham madde notları, sohbet kayıtları veya otomatik oluşturulmuş bir döküm okunabilir notlara dönüştürülecekse.
- Notlar ekiple paylaşılacak veya bir projeyle birlikte saklanacaksa.
- Birden fazla not tutanın parçaları tek bir kayıtta birleştirilecekse.

## Ne zaman kullanılmaz
- Kısa, yönetime dönük bir özet gerekiyorsa `meeting-summary` kullanılır.
- Katılım ve kararları içeren resmi bir kayıt gerekiyorsa (yönetim kurulu, yönlendirme komitesi, denetim) `meeting-minutes` kullanılır.
- Dökümün kendisi kelimesi kelimesine korunarak temizlenecekse `transcript-cleanup` kullanılır.

## Girdiler
Zorunlu:
- Ham notlar veya döküm.

İsteğe bağlı:
- Toplantı başlığı, tarih, katılımcılar ve rolleri, gündem, önceki notlar, proje terimleri sözlüğü.

Ham içerik yoksa iste. Gündem yoksa konuları içerikten çıkar ve bunu belirt.

## Süreç
1. Girdinin tamamını bir kez tara ve ayrı konuları listele; gündem varsa gündem maddeleriyle eşleştir, yoksa konuşulma sırasına göre diz.
2. Her konu için özü yakalayan 2-6 madde yaz: alınan pozisyonlar, verilen veriler, dile getirilen kısıtlar. Başka sözcüklerle ifade et; sayıları, sistem adlarını ve tarihleri aynen koru.
3. Bir ifadeyi kişiye yalnızca sahiplik önemliyse (taahhüt, itiraz, uzman görüşü) atfet. Diğer durumlarda nötr yaz.
4. Maddeleri satır içinde etiketle: `KARAR`, `AKSİYON`, `SORU`, `RİSK`. Karar için girdide açık bir mutabakat olmalı; mutabakat olmayan öneri tartışma noktası olarak kalır.
5. Her AKSİYON için sorumlu ve tarih yaz; eksikse `[BİLİNMİYOR]` yaz, asla tahmin etme.
6. Etiketli tüm maddeleri sonda toplu bölümlerde yeniden listele ki takip araçlarına kopyalanabilsin.
7. Belirsiz bölümleri (duyulmayan, çelişkili, anlamı belirsiz kısaltma) düzeltmeye çalışmak yerine `[BELİRSİZ: ...]` olarak işaretle.
8. Sohbeti, tekrarları ve kayıt dışı ifadeleri çıkar; kayıt için gerekmeyen kişisel verileri (telefon, sağlık, İK konuları) maskele.
9. Toplantı bilgilerini içeren bir başlık ve atlanan gündem maddeleri için "Görüşülmeyen" satırı ekle.

## Çıktı formatı
```markdown
# <Toplantı başlığı> – Notlar
Tarih: <tarih>  |  Katılımcılar: <isim/rol veya [BİLİNMİYOR]>  |  Not tutan: <isim veya [BİLİNMİYOR]>
Gündem kapsamı: <görüşülenler> | Görüşülmeyen: <maddeler>

## 1. <Konu>
- <tartışma noktası>
- KARAR: <üzerinde anlaşılan>
- AKSİYON: <iş> — <sorumlu> — <tarih>
- SORU: <açık soru> — <kim cevaplayabilir>

## 2. <Konu>
- ...

## Kararlar
| # | Karar | Konu |
## Aksiyonlar
| # | Aksiyon | Sorumlu | Tarih | Durum |
## Açık Sorular ve Riskler
| # | Madde | Tür | Sorumlu |
```

## Kalite kontrol listesi
- [ ] Girdideki her konu yer alıyor; önemli hiçbir şey atlanmadı.
- [ ] Kararlar yalnızca girdide açıkça mutabık kalınanlar.
- [ ] Her aksiyonun sorumlusu ve tarihi ya da `[BİLİNMİYOR]` işareti var.
- [ ] Sayılar, tarihler ve sistem adları kaynakla birebir aynı.
- [ ] Belirsiz kısımlar tahmin edilmedi, işaretlendi.
- [ ] Hassas kişisel veriler maskelendi veya çıkarıldı.

## Sık yapılan hatalar
- "Galiba şunu yapmalıyız..." ifadesini karara çevirmek. Tartışma noktası veya SORU olarak bırak.
- Kimin ne dediğini sırayla yazan kronolojik tutanak üretmek. Konuya göre grupla, kişi atfını yalnızca taahhütlerde kullan.
- Muhalefeti kaybetmek. Bir karara itiraz eden olduysa kısaca kaydet; ileride önem kazanır.

## Örnek
Girdi: "altyapı maliyeti %18 artmış ... Ayşe: reserved instance lazım mı? ... tamam prod db için 1 yıllık RI, Mehmet cumaya kadar finansla teyit edecek ... staging hâlâ açık"

Çıktıdan bir bölüm:
## 1. Altyapı maliyeti
- Aylık altyapı maliyeti %18 arttı.
- KARAR: Üretim veritabanı için 1 yıllık reserved instance kullanılacak.
- AKSİYON: Bütçe onayını Finans ile teyit et — Mehmet — Cuma `[tarihi teyit et]`.
- SORU: Staging ortamı da ayrılmış kapasiteye geçmeli mi? — [BİLİNMİYOR]
