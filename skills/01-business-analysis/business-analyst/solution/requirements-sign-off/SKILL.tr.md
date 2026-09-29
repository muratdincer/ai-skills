---
name: requirements-sign-off
description: "Gereksinim onay paketini hazırlar: onaylanan temel sürüm (dokümanlar, sürümler, gereksinim ID'leri), son incelemeden bu yana değişenler, açık konular ve kabul edilen riskler, koşullar, gereken onaycılar ve sonraki değişikliklerin nasıl kontrol edileceği. Gereksinimler incelenip temel sürüme bağlanmaya hazır olduğunda, sponsor 'tam olarak neyi imzalıyorum?' diye sorduğunda ya da tasarım, geliştirme veya bir sözleşme kilometre taşı başlamadan önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: solution
  title: "Gereksinim onayı hazırlama"
  related: "requirements-review-checklist, traceability-matrix, change-control, change-request-analysis, decision-log"
  prompt: "Hasar portalı FRD v1.3 için onay paketini hazırla; iş sahibi ve BT lideri bu hafta onaylayabilsin."
---

# Gereksinim Onayı Hazırlama

## Amaç
Onaycılara neyin temel sürüme bağlandığını, neyin hâlâ açık olduğunu ve onayın hangi koşullarla verildiğini net biçimde gösteren kısa bir paket sunmak. İyi bir paket imzayı anlamlı kılar ve değişiklik kontrolüne sabit bir referans noktası verir.

## Ne zaman kullanılır
- Gereksinimler incelemeden geçtiğinde ve tasarım, geliştirme veya satın alma başlamak üzereyken.
- Bir sözleşme kilometre taşı, bütçe kapısı veya tedarikçiye devir resmi olarak onaylanmış kapsam gerektirdiğinde.
- Onaylanan değişiklik talepleri sonrasında yeni bir temel sürüm gerektiğinde.

## Ne zaman kullanılmaz
- Gereksinimler henüz gözden geçirilmediyse önce `requirements-review-checklist` kullanılır.
- Onaylı temel sürümdeki tek bir değişiklik için karar gerekiyorsa `change-request-analysis` kullanılır.
- Değişiklik sürecinin kendisini tanımlamak gerekiyorsa `change-control` kullanılır.

## Girdiler
Zorunlu:
- Temel sürüme bağlanacak dokümanlar veya gereksinim seti, sürüm ya da tarihleriyle.
- Kimin onaylaması gerektiği (ad veya rol).

İsteğe bağlı, kaliteyi artırır:
- İnceleme bulguları ve durumları, izlenebilirlik matrisi, önceki temel sürüm.
- Kurumun onay politikası (kim neyi imzalar, vekâlet, elektronik onay kuralları).
- Onaya bağlı sözleşme veya yönetişim maddeleri.

Doküman seti veya onaycılar yoksa iste. Başka bir şeyi en başta sorma; eksikleri açık konu olarak kaydet.

## Süreç
1. Temel sürümü kesin tanımla: doküman adları, sürümler, tarihler ve gereksinim ID aralığı. Sürümü olmayan bir temel sürüm imzalanamaz; eksik sürümleri `[TBD]` olarak işaretle.
2. Önceki bir temel sürüm varsa farkı özetle: ID bazında eklenen, değişen ve çıkarılan gereksinimler ve bunlara yol açan değişiklik talepleri.
3. İncelemelerden ve diğer kaynaklardan gelen açık konuları listele. Her birini sınıflandır: Engelleyici (onay beklemeli), Koşullu (tarihli bir koşulla imzalanır) veya Ertelenen (sorumlusuyla birlikte açıkça sonraki sürüme taşınan).
4. Onaycıların kabul ettiği riskleri ve varsayımları kaydet; çıkarım olan maddeleri `[VARSAYIM]` etiketiyle tut ki onaycılar temel sürümün neye dayandığını görsün.
5. Hazırlık kanıtlarını kontrol et: inceleme tamamlandı mı, hedeflere izlenebilirlik var mı, NFR ve kabul kriterleri mevcut mu, kapsam dışı yazılmış mı. Her birini kanıt göstererek Evet / Kısmen / Hayır olarak raporla; göremediğin şeyi işaretleme.
6. Onaycı listesini oluştur: rol, ad, neyi onayladığı (iş içeriği, teknik yapılabilirlik, uyum, bütçe) ve onayın zorunlu mu danışma niteliğinde mi olduğu. Kişisel veri veya üretim ortamı değişikliği kapsamdaysa veri koruma, güvenlik ya da operasyon gibi eksik rolleri işaretle.
7. Onay sonrası değişiklik kontrol kuralını yaz: değişiklik nasıl talep edilir, kim karar verir, yeni temel sürümü ne tetikler.
8. Öneri ver: İmzaya hazır / Koşullu imza / Hazır değil; gerekçesi tek satır.
9. Talep sahibinin gönderebileceği kısa bir onay isteği mesajı taslağı yaz; son tarihi ve sessizliğin ne anlama geldiğini belirt (yönetişim aksini söylemedikçe sessizlik asla onay değildir).
10. Kullanıcı devam etmek isterse temel sürümü sabitlemek için `traceability-matrix`, onay sonrası süreç için `change-control` veya onayı kaydetmek için `decision-log` öner.

## Çıktı formatı
```markdown
# Gereksinim Onayı: <proje / kapsam>
Temel sürüm ID: <örn. BL-2 veya TBD> · Hazırlanma: <tarih> · Öneri: <Hazır / Koşullu / Hazır değil>

## Temel Sürüm İçeriği
| Doküman | Sürüm | Tarih | Gereksinim ID'leri |
|---|---|---|---|

## Önceki Temel Sürümden Bu Yana Değişiklikler
| Gereksinim ID | Eklendi / Değişti / Çıkarıldı | Kaynak (CR, inceleme) |
|---|---|---|

## Hazırlık Kanıtları
| Kontrol | Durum | Kanıt |
|---|---|---|

## Açık Konular
| # | Konu | Sınıf (Engelleyici / Koşullu / Ertelenen) | Sorumlu | Tarih |
|---|---|---|---|---|

## Kabul Edilen Riskler ve Varsayımlar
- [VARSAYIM] ...

## Onaylar
| Rol | Ad | Onayladığı | Zorunlu | Karar | Tarih |
|---|---|---|---|---|---|

## Onay Sonrası Değişiklik Kontrolü
<nasıl, kim, yeni temel sürüm tetikleyicisi>

## Onay İsteği Mesajı
<kısa mesaj metni>
```

## Kalite kontrol listesi
- [ ] Temel sürümdeki her dokümanın sürümü veya tarihi var ya da `[TBD]` olarak işaretli ve öneri buna göre verilmiş.
- [ ] Engelleyici konular öneriyle tutarlı (engelleyici madde varken "Hazır" yok).
- [ ] Her koşullu onayın sorumlusu ve son tarihi var.
- [ ] Onaycı rolleri iş, teknik ve gerekiyorsa uyum ile veri korumayı kapsıyor.
- [ ] Hiçbir onay, ad veya tarih uydurulmadı; kararlar verilene kadar boş bırakıldı.
- [ ] Çıkarım olan riskler ve varsayımlar etiketli; onaycılar neyi kabul ettiğini biliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Onaycılardan sürüm belirtmeden "gereksinimleri" imzalamalarını istemek. Sabit bir referans olmadan sonraki anlaşmazlıklar çözülemez.
- İmzayı hızlandırmak için açık konuları gizlemek. Bunlar daha kötü bir zamanda değişiklik talebi olarak geri döner; sınıflandırarak göster.
- "Uygun görünüyor" gibi bir yanıtı onay saymak. Açık kararı, ilgili sürümü ve tarihi kaydet.

## Örnek
Girdi: "Hasar portalının FRD v1.3 ve NFR listesi v1.1 incelendi. İki bulgu açık: doküman yükleme boyut sınırı ve SMS bildirim metni. İş sahibi Ayşe K. ve BT lideri imzalayacak."

Çıktıdan bir bölüm:
- Temel sürüm: FRD v1.3 (FR-001–FR-086), NFR v1.1 (NFR-01–NFR-22).
- Açık konular: yükleme boyut sınırı, Koşullu, sorumlu BT lideri, tarih `[TBD]`; SMS metni, içerik incelemesine Ertelendi, sorumlu İş birimi.
- Eksik onaycı `[VARSAYIM]`: portal sağlık verisi işlediği için muhtemelen veri koruma onayı gerekiyor.
- Öneri: Koşullu imza.
