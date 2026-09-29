---
description: Belirti ve kanıtlardan sıralı bir hata ayıklama hipotezleri listesi üretir ve her birini en ucuz ayırt edici testle eşleştirir; böylece araştırma dağılmak yerine sonuca yaklaşır. Bir hatanın nedeni bilinmediğinde, birkaç açıklama makul göründüğünde, hata ayıklama oturumu kısır döngüye girdiğinde veya ekip araştırma işini bölüşmek istediğinde kullanılır.
related: bug-reproduction, stack-trace-analysis, log-analysis, five-whys, fishbone-analysis
prompt: Son dağıtımdan sonra API isteklerinin yaklaşık %2'si 5 saniyeyi aşıyor, yalnızca bazı pod'larda. Sıralı hipotezler ve her birinin nasıl test edileceğini ver.
---

# Hata Ayıklama Hipotezleri

## Amaç
Deneme yanılmayı disiplinli bir aramayla değiştirmek: olasılığa ve test maliyetine göre sıralanmış açık hipotezler ve her biri için sonucu hipotezi eleyen veya doğrulayan bir test. Bu, kök nedene ulaşma süresini kısaltır ve ekibin belirtileri düzeltmesini engeller.

## Ne zaman kullanılır
- Belirti bilinip neden bilinmediğinde.
- Birkaç makul açıklama yarıştığında veya ekip takıldığında.
- Araştırmanın kişiler arasında paralelleştirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Hatayı tetiklemenin güvenilir bir yolu henüz yoksa ve kurmak ucuzsa önce `bug-reproduction` kullanılır.
- Bir olay sonrası süreç veya organizasyon kaynaklı kök neden analizi için `five-whys` veya `postmortem` kullanılır.

## Girdiler
Zorunlu:
- Belirti: yanlış olan ne, nerede ve nasıl gözlemlendi.

İsteğe bağlı, kaliteyi artırır:
- Şimdiye kadar bilinen olgular: ne zaman başladı, kapsam (kullanıcılar, pod'lar, bölgeler, sürümler), sıklık, son değişiklikler.
- Toplanmış kanıt: loglar, metrikler, trace'ler, stack trace'ler, denenen ve elenenler.
- Mimari bağlam ve bağımlılıklar.

Kapsam veya başlangıç zamanı bilinmiyorsa tahmin etme; bunları belirlemeyi ilk ucuz testler olarak listele.

## Süreç
1. Belirtiyi kapsam ve sıklıkla birlikte net biçimde yaz; olguları inançlardan ayrı listele.
2. Ayırt edici soruları sor: Ne değişti (kod, yapılandırma, veri, trafik, bağımlılıklar, altyapı)? Başarısız ve çalışan durumlar arasındaki fark ne? Hata deterministik mi?
3. Hiçbir alan atlanmasın diye hipotezleri kategoriler boyunca üret: kod değişikliği, yapılandırma/feature flag, veri şekli veya hacmi, bağımlılık veya üçüncü taraf davranışı, altyapı/kaynaklar, eşzamanlılık/zamanlama, ortam/zaman (saat, yaz saati, sertifikalar, kotalar).
4. Her hipotez için mekanizmayı tek cümleyle yaz (tam olarak bu belirtiye nasıl yol açar) ve lehine ve aleyhine kanıtı belirt.
5. Bilinen olgularla çelişen hipotezleri ele; nedenini not et.
6. Olasılığı kanıta göre (Yüksek/Orta/Düşük) ve test maliyetini (dakika, saat, gün, canlı ortam erişimi gerekir) tahmin et.
7. Her biri için en ucuz ayırt edici testi tasarla: hipotez doğruysa farklı sonuç verecek bir gözlem veya deney (sorgu, metrik kırılımı, log alanı, flag açıp kapama, tek bir pod'u geri alma, bir isteği yeniden oynatma).
8. Planı olasılık/maliyet oranına göre sırala; paralel çalışabilecek testleri grupla ve ekip varsa sorumlu ata.
9. Durma koşulunu tanımla: hangi sonuç kök nedeni doğrular (hata, o faktör değiştirilerek açılıp kapanabiliyor) ve tüm hipotezler elenirse ne yapılacak (kapsamı genişlet, ölçümleme ekle).

## Çıktı formatı
```markdown
# Hata Ayıklama Hipotezleri: <belirti>
## Olgular
- ...
## Önce Belirlenmesi Gereken Bilinmeyenler
- ...

## Hipotezler
| # | Hipotez | Mekanizma | Lehine / aleyhine kanıt | Olasılık | En ucuz test | Maliyet | Doğruysa beklenen sonuç |
|---|---|---|---|---|---|---|---|

## Elenenler
- <hipotez> — <olgu> ile çelişiyor

## Test Planı
1. <test> — sorumlu [TBD] — #... ile paralel

## Kök Neden Doğrulama Kriterleri
- ...
```

## Kalite kontrol listesi
- [ ] Hipotezler yalnızca ilk akla geleni değil, birden fazla kategoriyi kapsıyor.
- [ ] Her hipotez, kapsamı ve sıklığı dahil somut belirtiyi açıklıyor.
- [ ] Her test ayırt edici: sonucu inancını değiştirebilir.
- [ ] Plan merakla değil, olasılık ve maliyetle sıralanmış.
- [ ] Olgularla çelişen hipotezler açıkça elenmiş.
- [ ] Doğrulama yalnızca korelasyon değil, hatanın açılıp kapatılabilmesini gerektiriyor.

## Sık yapılan hatalar
- Son dağıtıma takılıp aynı penceredeki veri veya trafik değişikliklerini göz ardı etmek.
- Başarısız olamayacak testler çalıştırmak (ör. servisin ayakta olduğunu kontrol etmek). Her test bir şeyi eleyebilmeli.
- İlk makul nedende durmak. Kök neden ilan etmeden önce faktörü açıp kapatarak doğrula.

## Örnek
Girdi: v4.12 dağıtımından sonra isteklerin ~%2'si 5 sn'yi aşıyor, yalnızca bazı pod'larda; CPU normal.

Çıktıdan bir bölüm:
- H1 (Yüksek, 10 dk): Yeni pod'lar, değişen yapılandırma varsayılanı nedeniyle daha küçük bir DB bağlantı havuzuyla çalışıyor. Test: yavaş ve hızlı pod'lar arasında havuz ayarlarını ve bekleme süresi metriklerini karşılaştır. Doğruysa: yalnızca yavaş pod'larda havuz bekleme > 0.
- H2 (Orta, 30 dk): Yavaş pod'lar gürültülü komşusu olan node'larda. Test: yavaş pod'ları node'lara eşle; doğruysa yavaşlık sürümü değil node'u takip eder.
- Elenen: GC duraklamaları — yavaş pod'larda CPU ve GC metrikleri düz.
