---
description: "Bir talebi veya talep alma dokümanını eksik kontrol listesine (iş, kullanıcılar, veri, entegrasyon, NFR, yasal, operasyon, raporlama, geçiş) göre inceler; eksik, belirsiz veya çelişkili noktaları önem derecesiyle raporlar ve hazır/hazır değil kararı verir. Talep analize, tahmine veya sprint/backlog'a girmeden önce ya da 'bu talep başlamak için yeterince eksiksiz mi?' sorusu geldiğinde kullanılır."
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
2. Aşağıdaki eksik kontrol listesini uygula. Her madde için karar ver: Var, Belirsiz, Eksik, Çelişkili veya Uygulanamaz (gerekçesiyle).
3. Belirsiz ifadeleri kesin olarak işaretle: ifadeyi alıntıla ("hızlı", "tüm kullanıcılar", "eski sistemdeki gibi", "vb.", "en kısa sürede") ve yerine ne gerektiğini yaz.
4. Çelişkileri tespit et (örneğin "kişisel veri yok" ama "müşteri iletişim listesini dışa aktar").
5. Her eksiği derecelendir: Engelleyici (bu aşamada ilerlenemez), Büyük (yeniden işe yol açar), Küçük (sonra kapatılabilir).
6. Her Engelleyici ve Büyük eksik için onu kapatacak soruyu ve kimin cevaplaması gerektiğini yaz.
7. Kararı ver: Hazır, Koşullu hazır (koşulları listele) veya Hazır değil.
8. Basit bir kapsama göstergesi hesapla: uygulanabilir maddelerden kaçı Var / toplam uygulanabilir madde. Bunu bir kalite puanı gibi sunma.

Eksik kontrol listesi:
- **İş:** problem tanımı, istenen sonuç, ölçülebilir başarı kriterleri, iş değeri gerekçesi, sponsor/karar verici, gerekçeli son tarih, gecikmenin maliyeti.
- **Kullanıcılar:** kullanıcı grupları ve sayıları, roller ve yetkiler, iç/dış kullanıcı, kanal/cihaz, erişilebilirlik, eğitim etkisi.
- **Süreç ve kurallar:** tetikleyici, ana akış, istisnalar, onaylar, iş kuralları ve kaynağı, bugünkü manuel geçici çözümler.
- **Veri:** varlıklar ve alanlar, doğru kaynak, veri kalitesi, hacim ve büyüme, kişisel/hassas veri, sınıflandırma, saklama ve imha.
- **Entegrasyon:** giren ve çıkan sistemler, yön, sıklık (anlık/toplu), arayüz sahibi, hata yönetimi, üçüncü taraf bağımlılığı.
- **NFR:** performans hedefleri, tepe yük, erişilebilirlik ve destek saatleri, güvenlik ve yetkilendirme, denetim izi, yerelleştirme, erişilebilirlik (ilgiliyse WCAG 2.2).
- **Yasal ve uyum:** KVKK/GDPR hukuki dayanak ve açık rıza, sektör mevzuatı, sözleşmeler, kayıt tutma, denetim ihtiyacı.
- **Operasyon:** destek sahibi, izleme ve alarm, manuel yedek süreç, runbook, SLA etkisi, sürüm penceresi kısıtları.
- **Raporlama:** etkilenen KPI'lar, raporlar ve panolar, kullanıcıları, sıklık, geçmişle karşılaştırılabilirlik.
- **Geçiş (migration):** taşınacak veya temizlenecek veri, geçiş planı (cut-over), paralel çalışma, geriye dönük uyumluluk, eski sistemin kapatılması.

## Çıktı formatı
```markdown
# Eksiklik Kontrolü: <talep başlığı>
Hedef aşama: <sınıflandırma / analiz / tahmin / geliştirme> · Karar: **<Hazır / Koşullu hazır / Hazır değil>**
Kapsama: <var>/<uygulanabilir> uygulanabilir madde mevcut

## Eksikler
| # | Alan | Madde | Durum | Önem | Kanıt / alıntılanan ifade | Kapatacak soru | Sahibi |
|---|---|---|---|---|---|---|---|
| 1 | İş | Başarı kriterleri | Eksik | Engelleyici | – | ... | Sponsor |

## Çelişkiler
- "<alıntı A>" ile "<alıntı B>" – ...

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
- [ ] Eksik bilgi tahminle doldurulmadı.

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
| 1 | Süreç | Onay kuralı | Belirsiz | Engelleyici | "belli bir limitin üstündeki" | Limit tutar mı, indirim yüzdesi mi, ikisi mi? Sabit mi, bölgeye göre mi? | Satış operasyon |
| 2 | Süreç | Ret/zaman aşımı akışı | Eksik | Engelleyici | – | Yönetici reddederse veya zamanında cevap vermezse ne olur? | Satış operasyon |
| 3 | NFR | Denetim izi | Eksik | Büyük | – | Onaylar denetlenebilir olmalı mı (kim, ne zaman, hangi değer)? | Finans / denetim |
