---
name: impediment-tracking
description: "Bir engel kaydı oluşturur ve sürdürür: her engeli bloke ettiği iş, etkisi, sorumlusu ve sonraki aksiyonuyla kaydeder, kaldırmak için neye ihtiyaç duyulduğuna göre (ekip, başka ekip, yönetim, dış taraf) sınıflandırır, süre eşikleriyle bir eskalasyon basamağı uygular ve tekrarlayan sistemik nedenleri ortaya çıkarır. Ekip günlük senkronda engel bildirdiğinde, iş başkalarını beklerken takıldığında ya da açık engellerin düzenlenmesi, eskale edilmesi veya raporlanması istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "Engel takibi"
  related: "daily-sync-summary, escalation-message, cross-team-dependency-board, raid-log, retrospective-facilitation"
  prompt: "Bu haftaki senkronlardan çıkan engeller: test ortamı salıdan beri çalışmıyor, güvenlik ekibinin firewall kuralı onayını bekliyoruz, product owner iade kurallarına dönmedi. Düzenle ve neyi eskale etmem gerektiğini söyle."
---

# Engel Takibi

## Amaç
Her engeli net bir sorumlu ve sonraki aksiyonla görünür kılmak, iterasyonu sessizce tüketmeden doğru seviyede eskale etmek ve tekrarlayan engelleri sürekli yangın söndürme yerine sistemik iyileştirmelere dönüştürmek.

## Ne zaman kullanılır
- Engeller günlük senkronlarda veya yazışmalarda ortaya çıkıyor ve tutarlı biçimde kaydedilmesi gerekiyor.
- İş maddeleri başka bir ekibi, bir kararı veya dış bir tarafı bekliyor.
- Haftalık ya da iterasyon düzeyinde engel raporu veya eskalasyon gerekiyor.

## Ne zaman kullanılmaz
- Bağımlılıkları iş başlamadan önce planlamak ve müzakere etmek için `cross-team-dependency-board` kullanılır.
- Yönetişim için proje düzeyinde risk, varsayım ve sorun kaydı için `raid-log` kullanılır.
- Eskalasyon mesajının kendisini yazmak için, bu beceri neyin eskale edileceğine karar verdikten sonra `escalation-message` kullanılır.

## Girdiler
Zorunlu:
- Engellerin anlatıldığı haliyle listesi (senkron notları, mesajlar veya liste), biliniyorsa bloke ettikleri işle birlikte.

İsteğe bağlı, kaliteyi artırır:
- Her engelin bildirildiği tarih, mevcut engel kaydı.
- Etkiyi değerlendirmek için iterasyon hedefi veya sürüm kilometre taşları.
- Eskalasyon yolları ve muhataplar (ekip lideri, diğer ekip liderleri, yönetim, tedarikçi yöneticisi).

Bloke edilen iş veya bildirim tarihi belirtilmemişse `[BİLİNMİYOR]` yaz ve açık sorulara ekle; tahmin etme.

## Süreç
1. Her engeli tek bir kayda dönüştür: ne bloke (madde numaraları), onu ne bloke ediyor, ne zamandan beri ve gözlenen etki. Belirsiz kayıtları ("altyapıyı bekliyoruz") somutlaştır veya neyin eksik olduğunu işaretle.
2. Engelleri sıradan görevlerden ve risklerden ayır: engel taahhüt edilmiş işi zaten durduruyor veya yavaşlatıyordur; risk gelecekte bunu yapabilir (`raid-log`'a gönder); ekibin kendisinin yapabileceği bir görev sadece iştir.
3. Çözecek tarafa göre sınıflandır: ekip içi, başka ekip, ürün/iş kararı, yönetim/organizasyon, dış tedarikçi veya müşteri.
4. Etkiyi değerlendir: taahhüt edilmiş veya hedef için kritik hangi maddeler etkileniyor, şimdiye kadar kaybedilen gün ve engelin kritik hale geleceği tarih. Tek satırlık gerekçeyle Yüksek/Orta/Düşük olarak derecelendir.
5. Tek bir sorumlu (çözümü yürüten kişi veya rol; çözen taraf olması gerekmez) ve tarihli somut bir sonraki aksiyon ata.
6. Ekibin kendi kuralı yoksa eşikli eskalasyon basamağını uygula: aynı gün ekip içinde; 1 iş günü sonra diğer ekibin liderine; 2-3 iş günü sonra veya hedef için kritikse yönetime/sponsora `[varsayılan, ekip kuralına göre ayarla]`. Hangi kayıtların hemen eskale edilmesi gerektiğini işaretle.
7. Her eskalasyon için somut talebi (karar, kaynak, erişim, tarih) ve gecikmenin maliyetini belirt; mesajın yazımını `escalation-message`'a devret.
8. Geçici çözümleri ve bunların maliyetini veya riskini ayrı kaydet; geçici çözüm engeli kapatmaz.
9. Kayıtları yalnızca bloke iş ilerleyebildiğinde kapat; çözüm tarihini ve gerçekleşen kayıp günü kaydet.
10. Kayıtlar arasında örüntü ara (aynı ekip, aynı ortam, aynı tür karar) ve sistemik nedenleri bir sonraki retrospektif için aday olarak listele.
11. Sistemik nedenler için `retrospective-facilitation`, eskalasyonlar için `escalation-message`, kaydı güncel tutmak için `daily-sync-summary` öner.

## Çıktı formatı
```markdown
# Engel Kaydı – <ekip>, güncelleme <tarih>

| No | Bloke iş | Engel | Bildirim | Çözen tarafın türü | Etki (Y/O/D) | Sorumlu | Sonraki aksiyon – tarih | Eskalasyon seviyesi | Durum |
|---|---|---|---|---|---|---|---|---|---|

## Hemen Eskale Edilecekler
| No | Kime (rol) | Somut talep | Gecikmenin maliyeti |
|---|---|---|---|

## Uygulanan Geçici Çözümler
- <No>: <geçici çözüm> – <maliyet/risk>

## Son Güncellemeden Bu Yana Çözülenler
- <No>: <tarih> çözüldü, kaybedilen gün <n>

## Tekrarlayan Örüntüler (retrospektif için)
- ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her kayıt bloke işi, tek bir sorumluyu ve tarihli bir sonraki aksiyonu içeriyor.
- [ ] Riskler ve sıradan görevler engel olarak kaydedilmedi.
- [ ] Eskalasyon kararları belirtilen eşiklere uyuyor ve somut bir talep içeriyor.
- [ ] Etki taahhüt edilmiş veya hedef için kritik işe bağlandı; bilinmeyenler işaretli.
- [ ] Yalnızca tek tek engeller değil, tekrarlayan nedenler de belirlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Engeli sorumlusuz kaydetmek. "Ekip" hiçbir şeyin sahibi değildir; süreci yürüten bir kişi veya rol adı ver.
- Nezaket nedeniyle eskalasyonu çok geciktirmek. Net talepli eskalasyon suçlama değil, hizmettir.
- Geçici çözüm var diye engeli kapatmak. Geçici çözümün maliyetini izle, asıl engeli açık tut.

## Örnek
Girdi: test ortamı salıdan beri çalışmıyor; firewall kuralı güvenlik onayı bekliyor; product owner iade kurallarına dönmedi.

Çıktıdan bir bölüm:
| No | Bloke iş | Engel | Çözen tarafın türü | Etki | Sonraki aksiyon – tarih | Eskalasyon seviyesi |
|---|---|---|---|---|---|---|
| ENG-1 | Test'teki 3 hikâye | Test ortamı salıdan beri kapalı | Başka ekip (platform) | Yüksek – hedef için kritik | Sorumlu bugün platform liderini arar | Hemen yönetime (3 gün) |
| ENG-2 | PAY-44 | Firewall kuralı onay bekliyor | Başka ekip (güvenlik) | Orta | Perşembeye kadar karar tarihi iste | Diğer ekip lideri |
- Zayıf kayıt: "Altyapı sorunları." Güçlü kayıt: "Test ortamı salı 09:00'dan beri erişilemez; PAY-41/42/45 doğrulamasını bloke ediyor."
