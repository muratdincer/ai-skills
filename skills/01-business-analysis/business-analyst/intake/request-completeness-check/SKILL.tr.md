---
name: request-completeness-check
description: "Bir talebi veya talep alma dokümanını eksik kontrol listesine (iş, kullanıcılar, veri, entegrasyon, NFR, yasal, operasyon, raporlama, geçiş) göre inceler; eksik, belirsiz veya çelişkili noktaları önem derecesiyle raporlar ve hazır/hazır değil kararı verir. Talep analize, tahmine veya sprint/backlog'a girmeden önce ya da 'bu talep başlamak için yeterince eksiksiz mi?' sorusu geldiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: intake
  title: "Talep eksiklik kontrolü"
  related: "request-intake-document, request-clarification-questions, ambiguity-detection, requirements-gap-analysis, definition-of-ready"
  prompt: "Bu talep analize başlamak için yeterince eksiksiz mi kontrol et: 'Belli bir limitin üstündeki siparişlere indirim onay adımı ekleyelim, yöneticiler e-postayla onaylasın.'"
---

# Talep Eksiklik Kontrolü

## Amaç
Bir talebin analize veya tahmine geçip geçemeyeceği konusunda açık bir karar vermek ve önce kapatılması gereken eksikleri tek tek listelemek. Böylece yeniden yapılacak bir talep üzerinde çalışmaya başlanmaz.

## Ne zaman kullanılır
- Talep analize, tahmine, talep panosuna veya backlog'a girmeden önce.
- Taslak bir talep alma dokümanının kalite kapısından geçmesi gerektiğinde.
- Talepler yarım tanımlı geldiği için tahminler sürekli değişiyorsa.

## Ne zaman kullanılmaz
- Yalnızca talep sahibine gönderilecek sorular gerekiyorsa `request-clarification-questions` kullanılır.
- Girdi zaten ayrıntılı bir gereksinim setiyse `requirements-gap-analysis` veya `ambiguity-detection` kullanılır.

## Girdiler
Zorunlu:
- Talep metni veya talep alma dokümanı.

İsteğe bağlı, kaliteyi artırır:
- Talebin gideceği aşama (sınıflandırma, analiz, tahmin, geliştirme); çıtayı bu belirler.
- Kurumun zorunlu talep alanları veya "hazır" tanımı (definition of ready).
- İş alanı bağlamı (düzenlemeye tabi sektör, ilgili sistemler).

Talep yoksa iste. Hedef aşama bilinmiyorsa "analize hazır" çıtasını varsay ve bunu belirt.

## Süreç
1. Çıtayı belirle: "sınıflandırmaya hazır" için hedef, talep sahibi ve tür yeterlidir; "analize hazır" için kapsam, paydaşlar ve kısıtlar eklenir; "tahmine hazır" için kurallar, veri, entegrasyonlar ve NFR hedefleri de gerekir.
2. Aşağıdaki eksik kontrol listesini uygula. Her madde için karar ver: VAR, ZAYIF (bahsedilmiş ama muğlak veya test edilemez), YOK (hiç bahsedilmemiş), ERTELENDİ (bilinçli olarak sonraya bırakılmış, sahibi ve aşamasıyla), ÇELİŞKİLİ veya UYGULANAMAZ (gerekçesiyle). Her biri için kanıt kaydet: alıntılanan ifade veya "bahsedilmemiş".
3. Belirsizliğin üstünü örtme: ZAYIF bir maddeyi kendin netleştirip yeniden yazma. İfadeyi alıntıla ("hızlı", "tüm kullanıcılar", "eski sistemdeki gibi", "vb.", "en kısa sürede") ve yerine ne gerektiğini yaz; eklediğin her yorumu `[VARSAYIM]` olarak etiketle.
4. Çelişkileri tespit et (örneğin "kişisel veri yok" ama "müşteri iletişim listesini dışa aktar").
5. Her eksiği derecelendir: Engelleyici (bu aşamada ilerlenemez), Büyük (yeniden işe yol açar), Küçük (sonra kapatılabilir).
6. Her Engelleyici ve Büyük eksik için onu kapatacak soruyu ve kimin cevaplaması gerektiğini yaz.
7. Kararı ver: Hazır, Koşullu hazır (koşulları listele) veya Hazır değil.
8. Basit bir kapsama göstergesi hesapla: uygulanabilir maddelerden kaçı Var / toplam uygulanabilir madde. Bunu bir kalite puanı gibi sunma.
9. Hedef devam ediyorsa eksikleri mesaja çevirmek için `request-clarification-questions`, ayrıntılı gereksinimler oluştuğunda `requirements-gap-analysis` öner.

Eksik kontrol listesi:
- **İş:** problem tanımı, istenen sonuç, ölçülebilir başarı kriterleri, iş değeri gerekçesi, sponsor/karar verici, gerekçeli son tarih, gecikmenin maliyeti.
- **Aktörler ve roller:** kullanıcı grupları ve sayıları, iç/dış kullanıcı, kanal/cihaz, erişilebilirlik, eğitim etkisi, aktör rolündeki sistemler.
- **Tetikleyiciler ve akışlar:** tetikleyici olay, ana akış, alternatif akışlar, onaylar, bugünkü manuel geçici çözümler.
- **Ön/son koşullar:** başlamadan önce neyin doğru olması gerektiği; başarı ve hata sonrasındaki durum.
- **Kurallar ve doğrulama:** iş kuralları ve kaynağı, eşikler ve limitler, hesaplamalar, alan doğrulamaları.
- **Veri:** varlıklar ve alanlar, doğru kaynak, veri kalitesi, hacim ve büyüme, kişisel/hassas veri, sınıflandırma, saklama ve imha.
- **Yetki ve güvenlik:** kim görebilir, oluşturabilir, değiştirebilir, onaylayabilir; görevler ayrılığı; hassas işlemler; kimlik doğrulama seviyesi.
- **Hata yönetimi:** hatalı girdi, zaman aşımı, mükerrer kayıt, kısmi hata, yeniden deneme, kullanıcı mesajları, çözümden kim sorumlu.
- **Entegrasyon:** giren ve çıkan sistemler, yön, sıklık (anlık/toplu), arayüz sahibi, hata yönetimi, üçüncü taraf bağımlılığı.
- **NFR:** performans hedefleri, tepe yük, erişilebilirlik ve destek saatleri, kurtarma, yerelleştirme, erişilebilirlik (ilgiliyse WCAG 2.2).
- **Yasal ve uyum:** KVKK/GDPR hukuki dayanak ve açık rıza, sektör mevzuatı, sözleşmeler, kayıt tutma.
- **Destek ve operasyon:** destek sahibi, izleme ve alarm, manuel yedek süreç, runbook, SLA etkisi, sürüm penceresi kısıtları.
- **Raporlama ve denetim:** etkilenen KPI'lar, raporlar ve panolar, kullanıcıları, sıklık, geçmişle karşılaştırılabilirlik, denetim izi (kim, ne, ne zaman).
- **Devreye alma, geçiş ve bakım:** taşınacak veya temizlenecek veri, geçiş planı (cut-over), paralel çalışma, aşamalı devreye alma, geriye dönük uyumluluk, eski sistemin kapatılması, uzun vadeli sahip.

## Çıktı formatı
```markdown
# Eksiklik Kontrolü: <talep başlığı>
Hedef aşama: <sınıflandırma / analiz / tahmin / geliştirme> · Karar: **<Hazır / Koşullu hazır / Hazır değil>**
Kapsama: <var>/<uygulanabilir> uygulanabilir madde mevcut

## Eksikler
| # | Alan | Madde | Durum | Önem | Kanıt / alıntılanan ifade | Kapatacak soru | Sahibi |
|---|---|---|---|---|---|---|---|
| 1 | İş | Başarı kriterleri | YOK | Engelleyici | bahsedilmemiş | ... | Sponsor |

## Çelişkiler
- "<alıntı A>" ile "<alıntı B>" – ...

## Ertelenenler (sahip, aşama)
- ...

## Uygulanamaz (gerekçesiyle)
- ...

## İlerleme koşulları
1. ...
```

## Kalite kontrol listesi
- [ ] Kontrol listesindeki her alan değerlendirildi veya gerekçesiyle uygulanamaz işaretlendi.
- [ ] Belirsiz maddeler talepteki ifadeyi birebir alıntılıyor.
- [ ] Önem derecesi genel bir ideale değil, hedef aşamaya göre verildi.
- [ ] Her Engelleyici eksiğin kapatacak bir sorusu ve sahibi var.
- [ ] Karar eksik listesiyle tutarlı (açık Engelleyici varken "Hazır" yok).
- [ ] Eksik bilgi tahminle doldurulmadı ve hiçbir ZAYIF madde sessizce netleştirilip yeniden yazılmadı.
- [ ] Her bulgu kanıtıyla birlikte YOK, ZAYIF veya ERTELENDİ (ya da VAR/ÇELİŞKİLİ/UYGULANAMAZ) olarak sınıflandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sınıflandırma aşamasında tahmin düzeyinde ayrıntı istemek. Çıtayı aşamaya göre ayarla, yoksa iyi talepler takılır.
- Talep sahibi bahsetmedi diye bir alanı "uygulanamaz" saymak. Veri, yasal ve operasyon eksikleri genellikle yok değil, sessizdir.
- Önerilen çözümü eksiksiz gereksinim sanmak. "E-postayla onay" bir mekanizmadır; kural (kim, hangi limit, reddedilirse ne olur) hâlâ eksiktir.

## Örnek
Girdi: "Belli bir limitin üstündeki siparişlere indirim onay adımı ekleyelim, yöneticiler e-postayla onaylasın."

Çıktıdan bir bölüm:
Hedef aşama: analiz · Karar: **Hazır değil**
| # | Alan | Madde | Durum | Önem | Kanıt | Kapatacak soru | Sahibi |
|---|---|---|---|---|---|---|---|
| 1 | Kurallar | Onay kuralı | ZAYIF | Engelleyici | "belli bir limitin üstündeki" | Limit tutar mı, indirim yüzdesi mi, ikisi mi? Sabit mi, bölgeye göre mi? | Satış operasyon |
| 2 | Hata yönetimi | Ret/zaman aşımı akışı | YOK | Engelleyici | bahsedilmemiş | Yönetici reddederse veya zamanında cevap vermezse ne olur? | Satış operasyon |
| 3 | Raporlama ve denetim | Denetim izi | YOK | Büyük | bahsedilmemiş | Onaylar denetlenebilir olmalı mı (kim, ne zaman, hangi değer)? | Finans / denetim |
