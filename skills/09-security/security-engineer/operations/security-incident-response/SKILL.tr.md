---
name: security-incident-response
description: "Şüpheli veya doğrulanmış bir güvenlik olayına müdahaleyi ilk değerlendirme, sınırlandırma, kanıtların korunması, temizleme, kurtarma ve bildirim adımlarıyla yönetir; KVKK ve GDPR kişisel veri ihlali yükümlülüklerini içerir, olay kaydı ve aksiyon planı üretir. Sızma belirtisi, kimlik bilgisi sızıntısı, zararlı yazılım, veri kaçırma veya yetkisiz erişim işaretleri olduğunda ve ekibin yapılandırılmış, savunma odaklı bir müdahaleye ihtiyacı olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: security-engineer
  area: operations
  title: "Güvenlik olayına müdahale"
  related: "incident-response, incident-communication, postmortem, vulnerability-triage, security-finding-report"
  prompt: "CI kullanıcımızın AWS erişim anahtarını herkese açık bir GitHub reposunda bulduk ve CloudTrail bilinmeyen bir IP'den çağrılar gösteriyor. Müdahale etmemize yardım et."
---

# Güvenlik Olayına Müdahale

## Amaç
Bir güvenlik olayının verdiği zararı sınırlamak, kanıtları korumak, güvenilir işleyişi geri getirmek ve yasal bildirim yükümlülüklerini karşılamak; bu sırada kararların net bir kaydını tutmak.

## Ne zaman kullanılır
- Sızma belirtileri olduğunda: şüpheli girişler, sızmış kimlik bilgileri, zararlı yazılım alarmları, olağandışı veri transferleri, sayfa tahrifatı, fidye notları.
- Üçüncü bir taraf (müşteri, araştırmacı, tedarikçi, otorite) ihlal veya ihlal şüphesi bildirdiğinde.
- Bir zafiyetin istismar edildiği anlaşıldığında.

## Ne zaman kullanılmaz
- Güvenlik kaynaklı olmayan bir erişilebilirlik olayı için `incident-response` kullanılır.
- İstismar belirtisi olmayan bir zafiyet için `vulnerability-triage` kullanılır.
- Olay kapanmışsa ve öğrenme incelemesi gerekiyorsa `postmortem` kullanılır.

## Girdiler
Zorunlu:
- Ne gözlemlendi, ne zaman, nerede (sistemler, hesaplar, veriler) ve kim tespit etti.

İsteğe bağlı, kaliteyi artırır:
- Loglar, alarmlar, şu ana kadarki zaman çizelgesi, alınmış aksiyonlar.
- Kurumun olay müdahale planı, önem seviyeleri, iletişim listesi, hukuk/kişisel veri irtibatları.
- Etkilenen sistemlerin veri sınıflandırması.

Gözlem yoksa sor. İsteğe bağlı detaylar için sınırlandırma önerisini geciktirme; bunları açık soru olarak kaydet.

## Süreç
1. İlk değerlendirme: bunun bir güvenlik olayı olduğunu teyit et, kurumun ölçeğine göre önem ata, bir olay lideri ve bir kayıt tutucu belirle, UTC zaman damgalı bir olay kaydı aç.
2. İlk hipotezlerle kapsamı çiz: etkilenen varlıklar, kimlikler, veri türleri, giriş vektörü, saldırganın hâlâ aktif olup olmadığı.
3. Yıkıcı adımlardan önce kanıtı koru: disk veya instance snapshot'ı al, logları dışa aktar, delil zinciri notları tut; zararı durdurmak için gerekmedikçe ele geçirilmiş host'ları yeniden başlatma veya silme.
4. Kısa vadede sınırlandır: ifşa olmuş kimlik bilgilerini ve oturumları iptal et veya döndür, ele geçirilmiş hesapları kapat, host'ları veya ağ segmentlerini izole et, göstergeleri (IP, alan adı, hash) engelle, etkilenen entegrasyonları durdur.
5. İncele: loglardan (kimlik, bulut kontrol düzlemi, uç nokta, ağ, uygulama) saldırı zaman çizelgesini çıkar, hangi verilere erişildiğini veya hangilerinin dışarı çıkarıldığını belirle, kalıcılık izlerini ara (yeni kullanıcılar, anahtarlar, zamanlanmış görevler, arka kapılar).
6. Temizle: kalıcılık mekanizmalarını ve zararlı yazılımı kaldır, istismar edilen zayıflığı yamala, bütünlüğünden şüphe edilen sistemleri güvenilir image'lardan yeniden kur.
7. Kurtar: servisleri artırılmış izleme ile aşamalı olarak geri aç, veri ve yapılandırma bütünlüğünü doğrula, normale dönüş kriterlerini tanımla.
8. Kişisel veri ihlalini değerlendir: kişisel veri etkilenmiş olabilirse veri sorumlusunun kişisel veri sorumlusunu/DPO'sunu ve hukuku dahil et. GDPR'da, ihlal risk doğurmayacak nitelikte değilse farkına varılmasından itibaren 72 saat içinde denetim otoritesine bildirim yapılır; KVKK'da ihlal Kişisel Verileri Koruma Kurulu'na en kısa sürede (Kurul kararı 72 saat öngörür) bildirilir ve ilgili kişilere bilgi verilir. Kararı hukuk verir; bu beceri yalnızca olguları hazırlar.
9. İletişim kur: iç paydaşlara sabit aralıklarla, müşteri ve iş ortaklarına yönetim ve hukukun kararına göre; açıklamaları olgusal ve onaylı tut.
10. Kapat: sınırlandırma ve temizliğin tamamlandığını teyit et, takip aksiyonlarını sorumlularıyla listele, bir postmortem planla.
11. Devret: paydaş güncellemeleri için `incident-communication`, suçlamasız değerlendirme için `postmortem`, istismar edilen her zafiyet için `security-finding-report`.

## Çıktı formatı
```markdown
# Güvenlik Olayı <ID> – <kısa başlık>
| Alan | Değer |
|---|---|
| Önem | ... | Durum | İnceleniyor / Sınırlandırıldı / Temizlendi / Kurtarıldı / Kapandı |
| Tespit | <UTC zaman>, <kaynak> | Olay lideri | ... |
| Etkilenen varlıklar / kimlikler | ... |
| Kişisel veri etkisi | Evet / Hayır / [BİLİNMİYOR] – kategoriler, yaklaşık kişi sayısı [BİLİNMİYOR] |
## Zaman Çizelgesi (UTC)
| Zaman | Olay / aksiyon | Yapan | Kanıt ref |
## Sınırlandırma Aksiyonları
- [ ] ...
## İnceleme Bulguları
## Temizleme ve Kurtarma Planı
## Bildirim Değerlendirmesi
- GDPR / KVKK: karar sahibi, son tarih, durum
## İletişim Kaydı
## Açık Sorular ve Sonraki Güncelleme
```

## Kalite kontrol listesi
- [ ] Sınırlandırma adımları önce geliyor ve somut (hangi anahtar, hangi hesap, hangi host).
- [ ] Kanıtlar yıkıcı aksiyonlardan önce korunuyor.
- [ ] Zaman çizelgesi tek bir saat dilimi kullanıyor ve her kayıt için kanıt gösteriyor.
- [ ] Kişisel veri etkisi ve bildirim süreleri değerlendirildi, hukuk/kişisel veri sorumlusuna atandı.
- [ ] Kimlik bilgileri, token'lar ve kişisel veriler kayıtta maskelendi.
- [ ] Kanıt olmadan saldırgan kimliği veya veri hacmi belirtilmedi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sızan bir anahtarı döndürüp onun oluşturduğu oturumları, token'ları ve türetilmiş kimlik bilgilerini atlamak.
- Bir host'u hemen silip neyin çalındığını anlamak için gereken kanıtı yok etmek.
- Bildirim kararının sahibi olmadığı için yasal süreyi kaçırmak.
- İnceleme desteklemeden kök nedeni veya saldırganın kimliğini duyurmak.

## Örnek
Girdi: "CI kullanıcısının bulut erişim anahtarı açık bir repoda bulundu; kontrol düzlemi logları bilinmeyen bir IP'den çağrılar gösteriyor."

Çıktıdan bir bölüm:
- [ ] Sızan anahtarı hemen devre dışı bırak, ardından secrets manager üzerinden CI için yeni anahtar oluştur; loglar dışa aktarılana kadar eski anahtarı silme.
- [ ] Commit tarihinden bu yana bu anahtarla yapılan tüm işlemler için kontrol düzlemi loglarını sorgula: yeni kullanıcılar, anahtarlar, roller, instance'lar, depolama okumaları.
- Bildirim değerlendirmesi: anahtarın erişebildiği depolama alanlarında müşteri dışa aktarımları var [VARSAYIM: teyit et]; KVKK/GDPR bildirimine kişisel veri sorumlusu karar verecek, 72 saatlik süre <farkına varma UTC zamanı> itibarıyla başladı.
