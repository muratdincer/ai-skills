---
description: Bir çözüm veya yazılım mimarisini iş sürücüleri, kalite niteliği gereksinimleri, mimari ilkeler, bilinen riskler ve yaygın anti-desenlere göre gözden geçirir; somut önerilerle önem derecelendirilmiş bulgular ve bir inceleme kararı üretir. Bir tasarım dokümanı, diyagram seti veya ADR'ler mimari kurul onayına sunulduğunda, büyük bir geliştirme ya da canlıya geçiş öncesinde veya bir sistemde tekrarlayan yapısal sorunlar görüldüğünde kullanılır.
related: architecture-principles, nfr-to-architecture, atam-evaluation, resilience-review, scalability-review
prompt: Gelecek haftaki mimari kurul öncesinde yeni kredi başvuru platformumuzun çözüm mimarisi dokümanını gözden geçir.
---

# Mimari Gözden Geçirme

## Amaç
Bir mimarinin amacına uygun olup olmadığını ve kabul edilmiş ilkelere uyup uymadığını kanıta dayalı olarak değerlendirmek; tasarım ekibinin harekete geçebileceği bulgular ve onay makamı için net bir karar üretmek.

## Ne zaman kullanılır
- Bir çözüm mimarisi dokümanı, C4 diyagramları veya ADR seti onaya sunulduğunda.
- Büyük bir geliştirme, satın alma veya canlıya geçiş kilometre taşı mimari geçiş kapısı gerektirdiğinde.
- Çalışan bir sistemde yapısal bir nedenden şüphelenilen tekrarlayan olaylar, teslim yavaşlığı veya maliyet aşımları görüldüğünde.

## Ne zaman kullanılmaz
- Kalite ödünleşimleri üzerine yapılandırılmış bir paydaş çalıştayı gerekiyorsa `atam-evaluation` kullanılır.
- Yalnızca tek bir kalite niteliği söz konusuysa `resilience-review`, `scalability-review` veya `threat-model` kullanılır.
- Bir değişikliğin kod düzeyinde incelemesi için `code-review` kullanılır.

## Girdiler
Zorunlu:
- Mimari tanımı (doküman, diyagramlar, ADR'ler veya ayrıntılı sözlü açıklama).
- Çözümün iş hedefi veya sürücüsü.

İsteğe bağlı:
- NFR'ler/kalite senaryoları, mimari ilkeler ve standartlar, referans mimariler.
- Kısıtlar (bütçe, takvim, platformlar), önceki inceleme bulguları, olay geçmişi.

Tanım incelemeye yetmeyecek kadar zayıfsa tahmin yürütme; eksik görünümleri (bağlam, konteynerler, dağıtım, veri akışları) açıkça iste.

## Süreç
1. Sürücüleri yeniden ifade et: iş hedefleri, ölçüleriyle öncelikli kalite nitelikleri, temel kısıtlar. Eksik ölçüleri varsayım değil bulgu olarak işaretle.
2. Görünümlerin eksiksizliğini kontrol et: bağlam, konteynerler/yapı taşları, kritik akışlar için çalışma zamanı senaryoları, dağıtım, veri (sahiplik, akışlar, sınıflandırma), kesişen kavramlar.
3. Kalite hedeflerine uygunluğu değerlendir: öncelikli her kalite niteliği için onu karşılayan tasarım kararlarını bul; "karşılanmıyor" durumunu açıkça işaretle.
4. İlke ve standartlara göre kontrol et; her sapma ya bir ADR/istisna ile gerekçelendirilmiş olmalı ya da bulgu olur.
5. Anti-desenleri ara: dağıtık monolit, servisler arası paylaşılan veritabanı, kritik yolda senkron çağrı zincirleri, konuşkan arayüzler, her şeyi yapan servis (god service), yeniden denenen işlemlerde idempotency eksikliği, belirsiz veri sahipliği, tekil hata noktaları, yönetilmeyen üretici bağımlılığı.
6. Kesişen konuları kontrol et: güvenlik (kimlik, secret'lar, veri koruma, KVKK/GDPR), gözlemlenebilirlik, dağıtım ve rollback, yedekleme/DR, işletilebilirlik ve destek sahipliği.
7. Uygulanabilirliği kontrol et: ekip yetkinlikleri, teslim planı, göç ve geçiş durumları, bütçeye göre maliyet.
8. Her bulguyu derecelendir: Kritik (onayı engeller), Büyük (geliştirme/canlı öncesi çözülmeli), Küçük (iyileştir), Gözlem. Her bulgu için kanıtı (bölüm, diyagram, ADR) belirt; gözlenen olgularla çıkarımları ayır.
9. Her Kritik ve Büyük bulgu için somut bir düzeltme ve sorumlu rol öner.
10. Kararı ver: Onaylandı, Koşullu onaylandı (koşulları listele) veya Onaylanmadı (neyin değişmesi gerektiğini listele) ve tasarım ekibine soruları listele.
11. Hedef devam ediyorsa tartışmalı ödünleşimler için `atam-evaluation`, derinlemesine inceleme için `resilience-review` veya `scalability-review`, koşulları kaydetmek için `adr` öner.

## Çıktı formatı
```markdown
# Mimari Gözden Geçirme: <çözüm> – <tarih>
Karar: <Onaylandı | Koşullu onaylandı | Onaylanmadı>
## Kapsam ve İncelenen Girdiler
## Anlaşılan Sürücüler
## Özet
<3-5 cümle: güçlü yönler, başlıca riskler>
## Bulgular
| ID | Önem | Alan | Bulgu | Kanıt | Öneri | Sorumlu |
|---|---|---|---|---|---|---|
## Kalite Niteliği Kapsamı
| Nitelik | Hedef | Karşılayan | Durum (Tamam / Kısmi / Eksik) |
|---|---|---|---|
## İlke Uyumu ve İstisnalar
## Onay Koşulları
## Tasarım Ekibine Sorular
```

## Kalite kontrol listesi
- [ ] Her bulgu incelenen materyalden kanıt gösteriyor veya çıkarım olarak etiketli.
- [ ] Her Kritik/Büyük bulgunun somut, uygulanabilir bir önerisi var.
- [ ] Öncelikli her kalite niteliğinin açık bir kapsam durumu var.
- [ ] İlkelerden sapmalar ya bir istisna/ADR'ye bağlı ya da bulgu olarak yükseltildi.
- [ ] Karar bulgulardan çıkıyor ("Onaylandı" altında açık Kritik bulgu yok).
- [ ] Yalnızca sorunlar değil, güçlü yönler de belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sürücülere uygunluk yerine kişisel tercihleri incelemek ("ben Kafka kullanırdım"). Her bulguyu bir sürücüye, ilkeye veya riske bağla.
- Belirsiz bulgular ("ölçeklenebilirlik endişeleri"). Mekanizmayı, tetikleyiciyi ve etkiyi belirt.
- Yalnızca diyagramlara bakarak onaylamak. Kritik akışların çalışma zamanı ve dağıtım görünümlerini iste.

## Örnek
Girdi: Kredi başvuru platformu için SAD; hedef: 10 dakikadan kısa sürede karar; ilkeler arasında "API öncelikli" ve "paylaşılan veritabanı yok" var.

Çıktıdan bir bölüm:
| ID | Önem | Bulgu | Kanıt | Öneri |
|---|---|---|---|---|
| F1 | Kritik | Skorlama ve doküman servisleri aynı şemaya yazıyor; "paylaşılan veritabanı yok" ilkesine aykırı | Dağıtım görünümü, §7 | Skorlamaya kendi veri deposunu ver; `ApplicationScored` olayları yayınla; ya da çıkış tarihli bir istisna ADR'si yaz |
| F2 | Büyük | 10 dakikalık karar hedefinin çalışma zamanı görünümü yok; kredi bürosu çağrısı senkron ve zaman aşımı belirtilmemiş | §6 eksik, §8 | Çalışma zamanı senaryosu ekle, zaman aşımı + manuel kuyruğa geri düşme |
