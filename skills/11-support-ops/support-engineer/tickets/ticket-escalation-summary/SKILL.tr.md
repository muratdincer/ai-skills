---
name: ticket-escalation-summary
description: "Bir destek kaydını ve geçmişini bir sonraki destek seviyesi, yazılım ekibi veya tedarikçi için eskalasyon özetine dönüştürür: iş etkisi, kesin belirti, ortam, zaman çizelgesi, denenenler ve sonuçları, kanıtlar ve net talep. Kayıt L1'den L2/L3'e, ürün ekibine veya üçüncü tarafa geçeceğinde, uzun bir kayıt yazışması için devir notu gerektiğinde veya müşteri eskalasyon için baskı yaptığında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Eskalasyon için kayıt özeti"
  related: "ticket-triage, ticket-response, log-analysis, bug-report, problem-management"
  prompt: "30 mesajlık bu kaydı L3 için özetle: kullanıcılar salıdan beri web portalında birkaç dakikada bir 'oturum süresi doldu' hatası alıyor; önbellekleri temizledik, parolaları sıfırladık, değişen bir şey yok."
---

# Eskalasyon İçin Kayıt Özeti

## Amaç
Devralan seviyeye, müşteriye yeniden soru sormadan ve yapılmış teşhisleri tekrarlamadan harekete geçmesi için gereken her şeyi tek okumada vermek. Böylece eskalasyon çözüm süresini sıfırlamak yerine kısaltır.

## Ne zaman kullanılır
- Kayıt mevcut seviyenin bilgi, yetki veya süre sınırını aştığında.
- Kayıt bir yazılım veya ürün ekibine ya da tedarikçinin desteğine geçeceğinde.
- Uzun ve dağınık bir kayıt yazışmasının vardiyalar veya sahipler arasında temiz bir devir notuna ihtiyacı olduğunda.

## Ne zaman kullanılmaz
- Kayıt henüz sınıflandırılmamış veya önceliklendirilmemişse `ticket-triage` kullanılır.
- Amaç müşteriye yanıt vermekse `ticket-response` kullanılır.
- Doğrulanmış, tekrarlanabilir bir ürün hatası için backlog kaydı gerekiyorsa `bug-report` kullanılır.

## Girdiler
Zorunlu:
- Kayıt içeriği ve geçmişi (mesajlar, notlar, yapılan işlemler).

İsteğe bağlı, kaliteyi artırır:
- Öncelik, SLA ve kalan süre; müşteri seviyesi ve sözleşme yükümlülükleri.
- Loglar, hata metinleri, tarif edilen ekran görüntüleri, korelasyon veya istek ID'leri.
- Devralan ekibin eskalasyon şablonu veya zorunlu alanları.

Kayıt geçmişi yoksa iste. İsteğe bağlı bilgileri baştan sorma; "Eksik kanıt" altında listele. Kişisel verileri (son kullanıcı adları, T.C. kimlik numarası, kart numarası, sağlık bilgisi) maskele; parola, token veya oturum çerezlerini özete asla kopyalama, müşteri yapıştırdıysa değiştirilmeleri için işaretle.

## Süreç
1. Tüm yazışmayı oku ve olguları kaynaklarıyla (müşteri, destek uzmanı, log) çıkar. Gözlenen olguları destek uzmanının hipotezlerinden ayır; hipotezleri `[VARSAYIM]` olarak işaretle.
2. Belirtiyi kesin yaz: hata metninin tamamı, nerede göründüğü, etkilenen işlev, neyin "çalıştığı" ve neyin "çalışmadığı". Belirsiz ifadeleri ("yavaş", "bozuk") ölçülebilir gözlemlerle değiştir veya `[BİLİNMİYOR]` olarak işaretle.
3. Kapsamı ve iş etkisini sayısallaştır: etkilenen kullanıcı/lokasyon, engellenen süreç, geçici çözüm ve maliyeti, yasal veya finansal maruziyet, kalan SLA süresi.
4. Ortamı yaz: ürün/sürüm, tenant veya instance, tarayıcı/işletim sistemi/cihaz, ağ yolu, ilgili entegrasyonlar ve başka müşterilerde aynı belirtinin olup olmadığı.
5. UTC veya belirtilmiş bir saat diliminde zaman çizelgesi oluştur: ilk görülme, son değişiklikler (sürüm, yapılandırma, sertifika, tedarikçi değişikliği), bildirimler, yapılan işlemler.
6. Her sorun giderme adımını, olumsuz sonuçlar dahil sonucuyla birlikte listele; bildirilen ama doğrulanmayan adımları işaretle.
7. Kanıtları ekle veya referans ver: zaman damgalı log parçaları, istek/korelasyon ID'leri, tekrar adımları ve oranı (örneğin 5 denemenin 3'ü). Parçalardan kişisel verileri çıkar.
8. Devralan seviyeden net talebi yaz: teşhis, düzeltme, geçici çözüm, veri düzeltme onayı veya hatanın teyidi. Son tarihi ve nedenini ekle.
9. Müşteri iletişim durumunu kaydet: müşteriye ne söylendi, bir sonraki güncelleme için verilen söz ve hassasiyetler (üst yönetim ilgisi, sözleşme anlaşmazlığı).
10. Devret: müşteriyi güncellemek için `ticket-response`, devralan ekip hatayı doğrularsa `bug-report`, kayıt tekrarlayan bir örüntüye uyuyorsa `problem-management` öner.

## Çıktı formatı
```markdown
# Eskalasyon: <kayıt no> – <tek satırlık belirti>
| Alan | Değer |
|---|---|
| Kimden / Kime | <L1 uzmanı> → <L2 / L3 / ekip / tedarikçi> |
| Öncelik / SLA | P<n> – <kalan süre veya [BİLİNMİYOR]> |
| Müşteri / seviye | <maskeli veya hesap no> |
| İş etkisi | <kim, kaç kişi, ne engellendi, geçici çözüm> |
| Talep | <teşhis / düzeltme / geçici çözüm / hata teyidi>, <zaman, neden> |

## Belirti
<hata metninin tamamı, nerede, ne zaman, tekrar oranı>
## Ortam
- ...
## Zaman Çizelgesi (<saat dilimi>)
| Zaman | Olay | Kaynak |
|---|---|---|
## Denenenler
| Adım | Sonuç | Doğrulandı mı? |
|---|---|---|
## Kanıtlar
- <log parçası / korelasyon ID / ekran görüntüsü referansı>
## Hipotezler
- [VARSAYIM] ... – destekleyen ve çelişen kanıt
## Eksik Kanıt
- ...
## Müşteri İletişimi
- Son söylenen: ... Söz verilen sonraki güncelleme: ...
```

## Kalite kontrol listesi
- [ ] Devralan ekip, daha önce verilmiş hiçbir bilgiyi müşteriye yeniden sormadan işe başlayabiliyor.
- [ ] Belirti yalnızca müşterinin anlatımıyla değil, hata metninin tamamı ve gözlemlerle yazıldı.
- [ ] Denenen her adımın sonucu var, doğrulanmayanlar işaretli.
- [ ] Hipotezler `[VARSAYIM]` ile işaretli ve olgulardan ayrı.
- [ ] Talep ve son tarihi açık.
- [ ] Kişisel veriler maskeli, özette hiçbir gizli bilgi yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ham yazışmayı "kontrol eder misiniz" notuyla iletmek. Özetle; yazışma devir notu değil, ektir.
- Olumsuz sonuçları atlamak. "Önbellek temizliği işe yaramadı" bilgisi bir sonraki seviyeye bir saat kazandırır.
- Ortam ve hata zamanı olmadan eskale etmek; bu, log korelasyonunu imkânsız kılar.
- Devralan ekip adına müşteriye çözüm zamanı vaat etmek. Bunun yerine bir sonraki güncelleme zamanını söz ver.

## Örnek
Girdi: 30 mesajlık yazışma; kullanıcılar salıdan beri portalda birkaç dakikada bir "oturum süresi doldu" hatası alıyor; önbellek temizlendi, parolalar sıfırlandı.

Zayıf: "Müşterinin giriş sorunu var, her şey denendi, acil lütfen."

Güçlü, çıktıdan bir bölüm:
- Belirti: 2-5 dakikalık kullanımdan sonra "Oturumunuzun süresi doldu", tüm tarayıcılarda, ACME-EU tenant'ında yaklaşık 60 kullanıcı [VARSAYIM: o tenant'ın tüm kullanıcıları].
- Zaman çizelgesi: ilk bildirim salı 09:10 CET; 4.12 sürümü pazartesi 22:00 CET'te yayına alındı (kaynak: sürüm takvimi).
- Denenenler: tarayıcı önbelleği temizliği – değişiklik yok (2 kullanıcıyla doğrulandı); parola sıfırlama – değişiklik yok.
- Hipotez [VARSAYIM]: 4.12 ile oturum token ömrü veya load balancer yapışkanlığı (stickiness) değişti.
- Talep: L3'ün 15:00 CET'e kadar 4.11 ile 4.12 arasındaki oturum yapılandırma farkını incelemesi (SLA ihlali 17:00'de).
