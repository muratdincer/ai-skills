---
description: Bir toplantı veya çalıştay için dakika dakika akış planı, açılış ve kapanış metni, gündem maddesi başına yönlendirici sorular, karar kuralı ve baskınlık, sessizlik, konudan sapma ve çatışma için taktikler içeren kolaylaştırıcı metni hazırlar. Birisi bir toplantıyı yönetecek ve özellikle karar, uyum veya ekipler arası oturumları güvenle yürütmek istiyorsa kullanılır.
related: meeting-agenda, conflict-resolution, retrospective-facilitation, workshop-plan, decision-matrix
prompt: Ürün, satış ve mühendislikle 3. çeyrek önceliklerinde anlaşmak için 90 dakikalık bir oturumu kolaylaştıracağım. Bana bir kolaylaştırma rehberi ver.
---

# Toplantı Kolaylaştırma

## Amaç
Kolaylaştırıcıya hazır bir metin vermek; böylece grup hedeflenen çıktıya zamanında ulaşır, herkes katkı verir ve görüş ayrılıkları oturumu raydan çıkarmak yerine açıkça çözülür veya park edilir.

## Ne zaman kullanılır
- Birden fazla tarafla karar, önceliklendirme, uyum veya problem çözme toplantısı yönetilecekse.
- Tartışmalı bir konu veya üst düzey katılımcılar doğaçlamayı riskli kılıyorsa.
- Yeni bir kolaylaştırıcının hazır metne ve yedek hamlelere ihtiyacı varsa.

## Ne zaman kullanılmaz
- Gündem henüz tasarlanmadıysa önce `meeting-agenda` kullanılır.
- Toplantı bir retrospektifse `retrospective-facilitation` kullanılır.
- Egzersizler içeren çok oturumlu bir keşif çalıştayıysa `workshop-plan` kullanılır.

## Girdiler
Zorunlu:
- Toplantı hedefi ve beklenen çıktı.
- Süre ve katılımcılar (roller; isimler bilinmiyorsa sayı).

İsteğe bağlı:
- Gündem, bilinen gerilimler veya pozisyonlar, karar verici ve karar kuralı, uzaktan/yüz yüze düzen, materyaller.

Karar toplantısında karar verici bilinmiyorsa bunu rehberde engelleyici olarak işaretle; birini varsayma.

## Süreç
1. Çıktıyı bir tamamlanma testi olarak yeniden yaz ("X'in onayladığı, sıralanmış 5 öncelikle çıkıyoruz").
2. Karar kuralını baştan seç: danışma sonrası karar verici, rıza (gerekçeli itiraz yok), oy çokluğu veya konsensüs. Açılışta ilan et.
3. Süre kutuları zamanın %90'ını dolduran bir akış planı kur; %10 tampon ve kapanış için 5 dakika ayır.
4. 60 saniyelik bir açılış yaz: amaç, çıktı, karar kuralı, gündem, temel kurallar (tek konuşma, park alanı, uzaktansa kameralar).
5. Her gündem maddesi için uygun tekniği seç: sessiz yazma sonra sırayla paylaşım (ıraksama), nokta oylama veya sıralama (yakınsama), 1-2-4-hepsi (çok ses), beş parmak (rıza kontrolü).
6. Her madde için 2-3 açık uçlu soru ve bir yakınsama sorusu yaz ("A'yı seçmek için neye inanmamız gerekir?").
7. Şu durumlar için müdahaleler hazırla: baskın bir ses, sessiz katılımcılar, konudan sapma, argümanların tekrarı, tartışmayı kapatan en kıdemli kişinin görüşü (HiPPO), açık çatışma.
8. Park alanı kuralını tanımla: oraya ne gider ve nasıl takip edilir.
9. Kapanışı yaz: kararları ve aksiyonları sorumlularıyla oku, karar kuralına uyulduğunu teyit et, kısa çıkış turu, özeti kimin göndereceği.
10. Gerekiyorsa uzaktan/hibrit notu ekle: sohbet takibi, söz sırası, ortak pano.

## Çıktı formatı
```markdown
# Kolaylaştırma Rehberi: <toplantı>
Tamamlanma testi: <...>   Karar kuralı: <...>   Karar verici: <isim veya [BİLİNMİYOR] – engelleyici>

## Akış Planı
| Zaman | Madde | Teknik | Çıktı | Soru |
|---|---|---|---|---|

## Açılış (metin)
"<...>"

## Madde Soruları
### <Madde>
- Iraksama: ...
- Yakınsama: ...

## Müdahaleler
| Durum | Hamle | Kullanılacak ifade |
|---|---|---|

## Park Alanı Kuralı
## Kapanış (metin)
```

## Kalite kontrol listesi
- [ ] Tamamlanma testi toplantı sonunda gözlemlenebilir.
- [ ] Karar kuralı ve karar verici belirtilmiş ya da eksik olduğu işaretlenmiş.
- [ ] Süre kutuları tampon ve kapanış süresi içeriyor.
- [ ] Her maddenin hem ıraksama hem yakınsama sorusu var.
- [ ] Müdahaleler yalnızca tavsiye değil, somut ifadeler içeriyor.

## Sık yapılan hatalar
- Karar kuralını tartışmadan sonra seçmek; kaybeden taraf süreci sorgular. Açılışta ilan et.
- Kolaylaştırıcının da bir pozisyonu savunması. Katkı vermen gerekiyorsa "kolaylaştırıcı şapkamı çıkarıyorum" de ve kısa tut.
- Tüm süreyi ıraksamaya harcamak. Akış planında yakınsama süresini koru.

## Örnek
Girdi: 90 dk, ürün/satış/mühendislik, 3. çeyrek öncelikleri, kararı CPO veriyor.

Çıktıdan bir bölüm:
| 0:10-0:25 | Aday listesi | Sessiz yazma, sonra sırayla paylaşım | Tekilleştirilmiş liste | "Bu çeyreğin başarılı sayılması için çeyrek sonunda ne doğru olmalı?" |
Müdahale – baskın ses: "Teşekkürler Ali, gayet net. Devam etmeden önce mühendislikten dinleyelim. Deniz?"
