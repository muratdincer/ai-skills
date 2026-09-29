---
description: Amacı, beklenen çıktıyı, gündem özetini, her katılımcının neden davet edildiğini ve gereken hazırlığı net biçimde belirten bir toplantı daveti yazar. Takvim daveti veya toplantı talebi e-postası gönderilirken, alıcıların katılıp katılmayacağına karar verebilmesi ve hazırlıklı gelmesi gerektiğinde kullanılır.
related: meeting-agenda, meeting-necessity-check
prompt: Önümüzdeki salı ödeme servisinin yeniden tasarımı için 45 dakikalık bir mimari inceleme toplantısı daveti yaz.
---

# Toplantı Daveti Yazma

## Amaç
Alıcıların toplantının neden yapıldığını, neden davet edildiklerini ve ne hazırlamaları gerektiğini 10 saniyede anlamasını sağlamak. Böylece katılım ve hazırlık kalitesi artar.

## Ne zaman kullanılır
- Takvim daveti veya toplantı talebi e-postası gönderilirken.
- Kapsam veya gündem değiştikten sonra davet yeniden gönderilirken.

## Ne zaman kullanılmaz
- Gündemin kendisi henüz tasarlanmadıysa önce `meeting-agenda` kullanılır.
- Toplantının gerekli olup olmadığı belirsizse önce `meeting-necessity-check` kullanılır.

## Girdiler
Zorunlu:
- Toplantı konusu ve hedefi.
- Tarih, saat, süre, yer veya bağlantı.

İsteğe bağlı:
- Gündem, rolleriyle katılımcı listesi, ön okumalar, alınması gereken kararlar.

Zorunlu bir girdi eksikse sor. Tarih veya bağlantı verilmediyse davet taslağında `[TBD]` bırak, uydurma.

## Süreç
1. Konu satırını `<Tür>: <konu> – <çıktı>` biçiminde yaz (ör. "Karar: Ödeme yeniden tasarımı – hedef mimarinin onayı").
2. Amacı ve beklenen çıktıyı belirten tek bir cümleyle başla.
3. 3-5 maddelik bir gündem özeti ekle.
4. Her katılımcının neyi hazırlaması gerektiğini bağlantılarıyla yaz. Somut ol ("3. bölümü oku", "maliyet tahminini getir").
5. Zorunlu ve isteğe bağlı katılımcıları ayır; kilit kişilerin neden davet edildiği açık değilse bir satırla belirt.
6. Lojistiği ekle: saat dilimi, bağlantı, telefonla katılım, salon.
7. Katılamayacaklar için bir satır ekle: görüşlerini nasıl iletecekleri veya kimi yerine gönderecekleri.
8. Davetin tamamını yaklaşık 150 kelimenin altında tut.
9. Kullanıcının hedefi devam ediyorsa ve süreleri belli bir gündem henüz yoksa `meeting-agenda`, katılımcılar toplantının gerekliliğini sorgulayabilecekse `meeting-necessity-check` öner.

## Çıktı formatı
```markdown
Konu: <Tür>: <konu> – <çıktı>

Amaç: <tek cümle>. Toplantı sonunda <çıktı> elimizde olacak.

Gündem
- <madde> (<dakika>)
- ...

Lütfen hazırlanın
- <kişi/herkes>: <somut eylem> <bağlantı>

Zorunlu: <isimler>   İsteğe bağlı: <isimler>
Ne zaman/Nerede: <tarih, saat, saat dilimi, bağlantı/salon>
Katılamıyor musunuz? <görüş iletme veya yetki devri yolu>
```

## Kalite kontrol listesi
- [ ] Konu satırı toplantı türünü ve çıktıyı gösteriyor.
- [ ] Amaç tek cümleye sığıyor.
- [ ] Hazırlık somut ve bağlantılı.
- [ ] Zorunlu ve isteğe bağlı katılımcılar ayrılmış.
- [ ] Yaklaşık 150 kelimenin altında.
- [ ] Girdide söylenmeyen her şey `[VARSAYIM]` olarak işaretlendi veya açık soru olarak listelendi; olgu gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca başlık içeren davetler; alıcılar toplantının kendileriyle ilgisini değerlendiremez.
- Neye bakılacağını söylemeden "ekteki dokümanı inceleyiniz" demek.
- Dağıtık ekiplerde saat dilimini yazmayı unutmak.

## Örnek
Konu: Karar: Ödeme servisi yeniden tasarımı – hedef mimarinin onayı
Amaç: Önerilen mimariyi gözden geçirip PoC'ye geçip geçmeyeceğimize karar vermek. Toplantı sonunda bir devam/dur kararı ve açık risklerin listesi elimizde olacak.
