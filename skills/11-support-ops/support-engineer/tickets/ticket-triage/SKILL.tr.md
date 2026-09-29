---
name: ticket-triage
description: "Gelen bir destek kaydını sınıflandırır: türünü belirler (olay, hizmet talebi, soru, hata, güvenlik veya kişisel veri bildirimi), etki ve aciliyetten önceliği çıkarır, mükerrer kayıt veya süren bir kesinti olup olmadığını kontrol eder, eksik bilgileri belirler ve doğru kuyruğa veya seviyeye yönlendirir. Destek kuyruğuna yeni bir kayıt, e-posta veya sohbet talebi geldiğinde, sınıflandırılmamış kayıt birikimi ayıklanacağında veya öncelik tartışmalı olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Destek kaydı sınıflandırma"
  related: "ticket-response, ticket-escalation-summary, known-error-article, incident-response, bug-report"
  prompt: "Bu kaydı sınıflandır: 'Bu sabahtan beri 40 şube kullanıcımızın hiçbiri POS'tan fatura yazdıramıyor, elle yazıyoruz.'"
---

# Destek Kaydı Sınıflandırma

## Amaç
Bir kaydın ne olduğuna, ne kadar acil olduğuna, kimin ele alması gerektiğine ve neyin eksik olduğuna dakikalar içinde karar vermek. Böylece kritik sorunlar hızla doğru kişilere ulaşır, rutin talepler üst destek seviyelerini tıkamaz.

## Ne zaman kullanılır
- Destek kuyruğuna yeni bir kayıt, e-posta, sohbet veya telefon notu geldiğinde.
- Sınıflandırılmamış veya yanlış yönlendirilmiş bir grup kaydın ayıklanması gerektiğinde.
- Öncelik müşteri, destek ve yazılım ekibi arasında tartışmalı olduğunda.

## Ne zaman kullanılmaz
- Kayıt sınıflandırılmış ve müşteriye yanıt gerekiyorsa `ticket-response` kullanılır.
- Kaydın tüm bağlamıyla bir üst seviyeye devredilmesi gerekiyorsa `ticket-escalation-summary` kullanılır.
- Büyük bir olay ilan edilmiş ve koordinasyon gerekiyorsa `incident-response` kullanılır.

## Girdiler
Zorunlu:
- Kayıt metni (konu, açıklama, belirtilen ekler veya loglar).

İsteğe bağlı, kaliteyi artırır:
- Müşteri veya kullanıcı kimliği, sözleşme seviyesi ve SLA, etkilenen hizmet veya ürün.
- Kurumun öncelik matrisi, kategorileri ve yönlendirme kuralları.
- Mevcut bilinen hatalar, süren olaylar, son değişiklikler veya sürümler.

Kayıt metni yoksa iste. Sınıflandırmayı isteğe bağlı girdiler için bekletme; bunları `[BİLİNMİYOR]` olarak işaretle ve hangisinin önceliği değiştireceğini not et. Kayıt içeriğini tekrarlarken kişisel verileri (T.C. kimlik numarası, kart numarası, parola, sağlık bilgisi) maskele ve kullanıcının yapıştırdığı kimlik bilgilerini değiştirilmesi için işaretle.

## Süreç
1. Bildirenin söylediklerini (belirti, kapsam, zaman) kendi yorumundan (olası neden, etkilenen bileşen) ayır. Yorumları `[VARSAYIM]` olarak işaretle.
2. Kayıt türünü sınıflandır: olay (hizmet yavaşladı veya durdu), hizmet talebi (standart karşılama), soru/nasıl yapılır, hata (anlık kesinti olmayan, tekrarlanabilir ürün hatası), değişiklik talebi, güvenlik veya kişisel veri bildirimi, şikâyet.
3. Güvenlik ve kişisel veri bildirimlerini, önceliğinden bağımsız olarak hemen tanımlı kanala (güvenlik ekibi, veri koruma sorumlusu) yönlendir; olası kişisel veri ihlallerinin KVKK ve GDPR kapsamında yasal bildirim süreleri vardır.
4. Etkiyi değerlendir: etkilenen kullanıcı, şube veya müşteri sayısı, engellenen iş süreci, geçici çözüm var mı, risk altındaki veri, yasal veya finansal maruziyet.
5. Aciliyeti değerlendir: durum kötüleşiyor mu, zamana bağlı bir son tarih var mı, şimdi mi engelliyor yoksa daha sonra mı.
6. Önceliği etki x aciliyet matrisinden çıkar (verildiyse kurumun matrisini, yoksa P1-P4'e eşlenen ve `[VARSAYIM]` ile işaretlenen 3x3 bir matris kullan). Gerekçeyi tek satırda yaz.
7. Aynı belirtiye sahip mükerrer kayıt, süren olay veya bilinen hata olup olmadığını kontrol et; varsa paralel bir inceleme açmak yerine ilişkilendir.
8. Teşhisi engelleyen eksik bilgileri (hata metni, zaman, etkilenen kullanıcı örneği, ortam, adımlar, ekran görüntüleri) listele ve tek bir mesajda iste.
9. Yönlendirme kurallarına göre kuyruğa veya seviyeye (L1, L2, L3, tedarikçi, ürün ekibi) yönlendir; SLA'dan beklenen ilk yanıt ve çözüm hedeflerini belirt.
10. Devret: bilgilendirme yanıtı için `ticket-response`, üst seviyeye yönlendirirken `ticket-escalation-summary`, P1 için `incident-response`, doğrulanmış bir hata için `bug-report` öner.

## Çıktı formatı
```markdown
# Sınıflandırma: <kayıt no> – <kısa başlık>
| Alan | Değer |
|---|---|
| Tür | olay / hizmet talebi / soru / hata / değişiklik / güvenlik-kişisel veri / şikâyet |
| Kategori | <hizmet> > <bileşen> |
| Etki | <kim ve kaç kişi, geçici çözüm var/yok> |
| Aciliyet | <gerekçe> |
| Öncelik | P1-P4 – <tek satırlık gerekçe> |
| İlişkili | <olay / bilinen hata / mükerrer kayıt no veya bulunamadı> |
| Yönlendirme | <kuyruk / seviye / ekip> |
| SLA hedefleri | ilk yanıt <...>, çözüm <...> veya [BİLİNMİYOR] |

## Söylenen ve Çıkarılan
- Söylenen: ...
- [VARSAYIM] ...
## Eksik Bilgi (bildirene sorulacak)
1. ...
## Sonraki Adım
<bilgilendir / eskale et / olay ilan et / bilgi iste>
```

## Kalite kontrol listesi
- [ ] Öncelik, bildirenin üslubundan veya kıdeminden değil, belirtilen etki ve aciliyetten çıkarıldı.
- [ ] Güvenlik ve kişisel veri bildirimleri öncelikten bağımsız olarak kendi kanalına yönlendirildi.
- [ ] Mükerrer kayıtlar, süren olaylar ve bilinen hatalar kontrol edilip ilişkilendirildi.
- [ ] Eksik bilgiler tek ve somut bir mesajla istendi.
- [ ] Kişisel veriler ve yapıştırılmış kimlik bilgileri sınıflandırma notunda maskelendi.
- [ ] Çıkarımlar `[VARSAYIM]`, verilmeyen SLA hedefleri `[BİLİNMİYOR]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Önceliği bildirenin ne kadar kızgın veya kıdemli olduğuna göre belirlemek. Matrisi kullan ve gerekçeyi yaz.
- Birbirine benzeyen çok sayıda kaydı ayrı sorunlar gibi ele almak. Ortak nedeni ara ve kayıtları tek bir olaya bağla.
- Geçici çözümün ölçekte uygulanabilir olup olmadığını kontrol etmeden, geçici çözüm var diye önceliği düşürmek.
- Kaydı kuyruklar arasında gidip getirmek. Açık bir gerekçeyle bir kez yönlendir; sahip belirsizse eskale et.

## Örnek
Girdi: "Bu sabahtan beri 40 şube kullanıcımızın hiçbiri POS'tan fatura yazdıramıyor, elle yazıyoruz."

Çıktıdan bir bölüm:
| Tür | Olay |
| Etki | Tüm şubelerde 40 kullanıcı [VARSAYIM: tek müşterinin tüm şubeleri], faturalama engellendi; elle geçici çözüm var ama vergi uyumu riski doğuruyor |
| Öncelik | P2 – yüksek etki, geçici çözüm var ama sürdürülebilir değil; başka müşteriler de bildirirse P1'e yükselt |
| İlişkili | Dün gece POS yazdırma servisine çıkılan sürümü kontrol et [VARSAYIM] |
Eksik bilgi: ekrandaki hata metninin tamamı, etkilenen bir terminal numarası, ilk hatanın saati.
