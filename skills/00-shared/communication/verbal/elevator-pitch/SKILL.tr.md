---
name: elevator-pitch
description: "Bir fikir, proje, ürün veya talep için tek bir dinleyiciye göre uyarlanmış; dikkat çekici bir giriş, problem, öneri, kanıt ve tek bir somut talep içeren 30-60 saniyelik sözlü bir konuşma yazar. Birinin meşgul bir kişiyi bir sonraki adımı atacak kadar ilgilendirmek için kısa bir fırsatı (koridor, görüşme açılışı, toplantıda tanıtım, bütçe veya sponsorluk talebi) olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: communication
  area: verbal
  title: "Asansör konuşması hazırlama"
  related: "presentation-outline, executive-summary, value-proposition-canvas, problem-statement, stakeholder-map"
  prompt: "CTO'muzu mikroservislerimiz arasında otomatik kontrat testi pilotuna sponsor olmaya ikna edecek 45 saniyelik bir konuşma hazırla."
---

# Asansör Konuşması Hazırlama

## Amaç
Bir fikri, belirli bir dinleyiciyi önemsemeye, inandırıcı bulmaya ve küçük bir sonraki adımı kabul etmeye yönelten 80-150 sözcüklük sözlü bir metne indirmek; böylece kısa bir fırsat bir toplantıya, bir sponsora veya bir karara dönüşür.

## Ne zaman kullanılır
- Kıdemli birinden sponsorluk, bütçe, zaman veya toplantı istenecekse.
- Bir toplantının ya da etkinliğin başında proje veya ürün tanıtılacaksa.
- Ekibinizin işini dışarıdan birine bir dakikadan kısa sürede anlatmaya hazırlanıyorsanız.

## Ne zaman kullanılmaz
- Dinleyicinin yazılı ve kendi başına anlaşılır bir özete ihtiyacı varsa. `executive-summary` kullanın.
- Tam bir sunum süresi varsa. `presentation-outline` kullanın.
- Problemin kendisi hâlâ net değilse. Önce `problem-statement` kullanın.

## Girdiler
Zorunlu:
- Fikir veya talep ve dinleyicinin kim olduğu (rolü, neyi önemsediği).
- Talep: dinleyicinin bir sonraki adımda ne yapmasını istediğiniz.

İsteğe bağlı:
- Kanıtlar (rakamlar, müşteri görüşleri, pilot sonuçları), kısıtlar, ortam ve süre sınırı, dinleyicinin bilinen itirazları.

Dinleyici veya talep eksikse sorun; hedef dinleyicisi olmayan bir konuşma slogandan ibarettir. Asla metrik veya sonuç uydurmayın; kullanıcının dolduracağı `[TBD: rakam]` yer tutucuları kullanın.

## Süreç
1. Dinleyiciyi ve en önemli kaygısını belirleyin (maliyet, risk, büyüme, müşteri, ekip hızı, uyum). Çıkarımsa `[VARSAYIM]` olarak işaretleyin.
2. Kabul etmesi kolay, küçük tek bir talep tanımlayın (30 dakikalık toplantı, pilot, tanıştırma); programın tamamını değil.
3. Girişi yazın: dinleyicinin kaygısına somut bir olgu, soru veya sonuçla bağlanan tek cümle. Dinleyicinin kullanmadığı jargon ve kısaltmalardan kaçının.
4. Problemi onun diliyle söyleyin: kim etkileniyor, ne kadar, ne sıklıkla. Tek cümle.
5. Öneriyi tek cümleyle söyleyin: ne yapacağınızı; iç işleyişini değil.
6. Kanıt ekleyin: bir rakam, pilot sonucu, müşteri sinyali veya emsal. Doğrulanmamış kanıtı `[TBD]` olarak işaretleyin.
7. Neden şimdi ve neden siz: zamanlama tetikleyicisi ve güvenilirliğiniz, en fazla birer cümle.
8. Talep ve sonraki adımla kapatın; "evet" demeye davet eden bir soru olarak kurun.
9. Süreye göre kısaltın: konuşmada dakikada yaklaşık 130 sözcük; sıfatları ve dinleyicinin bir başkasına aktarmayacağı her şeyi çıkarın.
10. En olası iki itiraza tek cümlelik cevaplar ve 15 saniyelik kısa bir sürüm hazırlayın.
11. Kullanıcının hedefi devam ediyorsa takip toplantısı için `presentation-outline`, geride bırakılacak yazılı özet için `executive-summary` öner.

## Çıktı formatı
```markdown
# Asansör Konuşması: <konu>
Dinleyici: <rol> – en önemli kaygısı: <...> | Süre: <saniye> (~<sözcük> sözcük)
Talep: <küçük tek bir sonraki adım>

## Konuşma (sözlü)
<Giriş.> <Onun diliyle problem.> <Öneri.> <Kanıt.> <Neden şimdi / neden biz.> <Soru olarak talep.>

## 15 saniyelik sürüm
<...>

## Olası itirazlar
- "<itiraz>" -> <tek cümlelik cevap>

Doldurulacak yer tutucular: [TBD] ... | Varsayımlar: [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Adı belli tek bir dinleyici ve onun kaygısı için yazılmış.
- [ ] Tam olarak bir talep var ve anında kabul edilebilecek kadar küçük.
- [ ] Sesli okunduğunda süreye sığıyor (dakikada yaklaşık 130 sözcük).
- [ ] Dinleyicinin kullanmayacağı jargon ve uydurma rakam yok.
- [ ] Dinleyici ana mesajı tek cümleyle tekrarlayabilir.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çözümün teknolojisiyle başlamak. Dinleyicinin problemiyle başlayın.
- Her şeyi bir anda istemek (bütçe, ekip, yol haritası). Yalnızca sonraki adımı isteyin.
- Ezberlenmiş metni senaryo okur gibi söylemek. Sözlü kullanılacaksa madde madde ipuçları olarak tutun.

## Örnek
Girdi: CTO, mikroservisler arası otomatik kontrat testi pilotuna sponsorluk, 45 saniye.

Zayıf: "Bir broker ve CI entegrasyonuyla consumer-driven contract testing getirmek istiyoruz çünkü best practice ve kaliteyi artırıyor."

Güçlü (alıntı): "Geçen çeyrek canlı ortam olaylarımızın `[TBD: n]` tanesi, bir servisin başka bir servisin bağımlı olduğu API'yi değiştirmesinden çıktı. Bunları bugün ancak sürümden sonra yakalıyoruz. Ödeme akışının arkasındaki iki ekiple altı haftalık bir pilot yapmak istiyorum: her API değişikliği merge'den önce tüketicilerine karşı kontrol edilecek. Bu olayları azaltırsa yaygınlaştırırız, azaltmazsa durdururuz. Sponsor olur ve başarı ölçütünü belirlemek için gelecek hafta 30 dakika ayırır mısınız?"
