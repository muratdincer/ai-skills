---
description: "Belirli bir hedef kitlenin bir ürün, değişiklik, politika veya proje hakkında soracağı olası soruları üretir ve bunları yalnızca verilen kaynak materyale dayanarak cevaplar, boşlukları işaretler. Bir lansman, geçiş, politika değişikliği, iç araç veya müşteri yardım sayfası için SSS hazırlanırken ya da destek veya sohbet kanallarına aynı sorular tekrar tekrar geldiğinde kullanılır."
related: "kb-article, announcement, org-change-communication, user-guide, ticket-response"
prompt: "Bu yaygınlaştırma planına göre, eski VPN'den yeni zero-trust erişim istemcisine geçiş hakkında çalışanlar için bir SSS hazırla."
---

# SSS Oluşturma

## Amaç
Hedef kitlenin gerçekten soracağı soruları öngörmek ve kaynak materyale dayanarak cevaplamak. Böylece destek yükü azalır, kişiler kendi başına yanıt bulur ve cevapsız kalan sorular yayından önce sorumlulara görünür olur.

## Ne zaman kullanılır
- Bir lansman, geçiş, politika veya organizasyon değişikliği öngörülebilir sorular doğuracaksa.
- Destek, sohbet veya e-posta kanallarında standart bir cevabı hak eden tekrarlayan sorular varsa.
- Uzun bir doküman var ama okuyucuların belirli kaygılarına hızlı cevap gerekiyorsa.

## Ne zaman kullanılmaz
- Tek bir konu için eksiksiz, adım adım bir makale gerekiyorsa `kb-article` veya `how-to-guide` kullanılır.
- Değişikliğin kendisi duyurulacaksa `announcement` veya `org-change-communication` kullanılır.
- Tek bir müşteri sorusu cevaplanacaksa `ticket-response` kullanılır.

## Girdiler
Zorunlu:
- Kaynak materyal: plan, şartname, politika, sürüm notları veya mevcut dokümantasyon.
- Hedef kitle (ör. son kullanıcılar, çalışanlar, müşteriler, iş ortakları, iç destek).

İsteğe bağlı, kaliteyi artırır:
- Hâlihazırda gelmiş gerçek sorular (kayıtlar, sohbet geçmişi, anket yorumları); kişisel verileri maskele.
- Ton kılavuzu, yayın kanalı ve uzunluk sınırı.
- Cevapsız sorular için iletişim veya eskalasyon kanalı.

Kaynak materyal veya hedef kitle eksikse iste. Genel bilgiyle cevap verme; eksik cevaplar sorumlu için `[TBD]` olur.

## Süreç
1. Hedef kitlenin durumunu belirle: onlar için ne değişiyor, ne yapmaları gerekiyor, neyi kaybetmekten korkuyorlar.
2. Önce gerçek soruları topla (kayıtlar, geçmişler, yorumlar). Tekrarları ayıkla, ifadeyi iç jargon yerine kullanıcının diline göre düzenle.
3. Öngörülen soruları farklı açılardan üret: ne/neden, kim etkileniyor, ne zaman/son tarihler, ne yapmalıyım, hiçbir şey yapmazsam ne olur, maliyet/etki, veri ve gizlilik, istisnalar, nereden yardım alırım.
4. Sıklığa ve yanlış anlaşılmanın sonucuna göre önceliklendir; yalnızca proje ekibinin soracağı soruları çıkar.
5. Her soruyu yalnızca kaynağa dayanarak cevapla. İlk cümlede doğrudan cevabı ver (evet/hayır/tarih/aksiyon), ardından gerekli ayrıntıyı ekle.
6. Kaynak sessiz veya çelişkiliyse cevap yerine `[TBD — sorumlu: <rol>]` yaz ve boşluk listesine ekle.
7. Soruları kitleye yönelik 3-7 başlık altında grupla, en sık sorulandan en aza doğru sırala.
8. Tutarlılığı kontrol et: tarihler, isimler ve sayılar cevaplar arasında ve kaynakla uyumlu olmalı.
9. Tam dokümantasyona bağlantı veya referans ekle; en sona destek kanalını içeren "Başka sorunuz mu var?" maddesini koy.

## Çıktı formatı
```markdown
# SSS: <konu>
Hedef kitle: <...> | Son güncelleme: <tarih> | Kaynak: <dokümanlar>

## <Grup 1, ör. Ne değişiyor>
**S: <kullanıcının ağzından soru>**
C: <önce doğrudan cevap>. <destekleyici ayrıntı>. Bkz: <referans>.

## <Grup 2 ...>
...

## Başka sorunuz mu var?
<kanal, sorumlu, saatler>

---
## Sorumlular İçin Boşluklar (yayınlanmaz)
| Soru | Neden cevapsız | Sorumlu | Gereken tarih |
|---|---|---|---|
```

## Kalite kontrol listesi
- [ ] Sorular hedef kitlenin soracağı biçimde ifade edilmiş.
- [ ] Her cevap doğrudan cevapla başlıyor.
- [ ] Hiçbir cevap kaynakta olmayan bilgi içermiyor; boşluklar `[TBD]`.
- [ ] Tarihler, isimler ve sayılar maddeler arasında tutarlı.
- [ ] "Hiçbir şey yapmazsam" ve "nereden yardım alırım" soruları kapsanmış.
- [ ] Boşluk listesi yayınlanacak içerikten ayrılmış.

## Sık yapılan hatalar
- Kimsenin sormadığı pazarlama soruları yazmak ("Yeni araç neden bu kadar harika?"). Gerçek ve öngörülen kaygıları kullan.
- Cevabı bağlamın altına gömmek. İlk cümle cevaplar, gerisi destekler.
- SSS'nin tek dokümantasyon hâline gelmesine izin vermek. Asıl dokümanlara bağlantı ver, cevapları kısa tut.

## Örnek
Girdi: VPN'den zero-trust erişime geçiş planı; hedef kitle: tüm çalışanlar.

Çıktıdan bir bölüm:
- **S: Geçişten önce bir şey yapmam gerekiyor mu?** C: Evet. Geçiş tarihinden `[TBD — sorumlu: BT]` önce yeni erişim istemcisini self-servis portalından kurun. Eski VPN bu tarihten sonra çalışmayacak.
- **S: İç sistemlere kişisel dizüstü bilgisayarımdan hâlâ erişebilecek miyim?** C: `[TBD — sorumlu: Güvenlik]` Plan, yönetilmeyen cihazlar için politikayı belirtmiyor.
- Boşluk: yönetilmeyen cihaz politikası — Güvenlik — duyurudan önce gerekli.
