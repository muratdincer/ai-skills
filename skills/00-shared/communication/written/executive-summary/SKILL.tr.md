---
name: executive-summary
description: "Bir dokümanı, analizi, teklifi veya tartışmayı; önce sonucu ve talebi, ardından destekleyici noktaları, seçenekleri, riskleri ve sonraki adımları veren tek sayfalık, karar odaklı bir yönetici özetine indirger. Üst düzey bir okuyucunun uzun veya teknik bir içeriği hızla anlayıp harekete geçmesi gerektiğinde ya da \"kısaca\", \"yönetici özeti\", \"yönetim için tek sayfa\" istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: communication
  area: written
  title: "Yönetici özeti yazma"
  related: "status-update, steering-committee-pack, document-simplify, decision-matrix, presentation-outline"
  prompt: "Bu 20 sayfalık tedarikçi değerlendirmesini, gelecek hafta kısa listedeki iki tedarikçi arasında seçim yapacak CIO için yönetici özetine dönüştür."
---

# Yönetici Özeti Yazma

## Amaç
Üst düzey okuyucuya sonucu, arkasındaki gerekçeyi ve gereken kararı tek sayfada vermek. Böylece okuyucu kaynağı okumadan harekete geçebilir ve önemli hiçbir şeyin atlanmadığına güvenebilir.

## Ne zaman kullanılır
- Uzun bir rapor, analiz, iş gerekçesi veya teklif yöneticilere ya da yönlendirme komitesine gidiyorsa.
- Bir karar verici teknik bir konunun kısa sürümünü istiyorsa.
- Bir ön okumanın iki dakikada gözden geçirilebilir olması gerekiyorsa.

## Ne zaman kullanılmaz
- Düzenli ilerleme raporlanıyorsa `status-update` kullanılır.
- Tam bir yönlendirme komitesi sunumu hazırlanıyorsa `steering-committee-pack` kullanılır.
- Doküman hedef kitlesi değişmeden kısaltılıp sadeleştirilecekse `document-simplify` kullanılır.

## Girdiler
Zorunlu:
- Kaynak içerik (metin, notlar veya ana bulgular).
- Okuyucu ve onun neye karar vermesi veya neyi bilmesi gerektiği.

İsteğe bağlı:
- Karar için son tarih, kurumsal kısıtlar, tercih edilen öneri, format sınırları (kelime sayısı, tek slayt).

Okuyucu veya amaç eksikse bir kez sor: "Bunu kim okuyacak ve okuduktan sonra ne yapmalı?" Kaynağın desteklemediği bir öneri ekleme; kaynakta öneri yoksa seçenekleri tarafsızca sun ve bunu belirt.

## Süreç
1. Okuyucunun cevaplanmasını istediği tek soruyu tanımla (karar ver, onayla, bilgilen, engeli kaldır).
2. Kaynaktan çıkar: sonuç/öneri, onu destekleyen 3-5 bulgu, değerlendirilen seçenekler, maliyetler, riskler ve hiçbir şey yapılmazsa ne olacağı.
3. Önce sonucu yaz (BLUF): sonucu ve talebi içeren bir veya iki cümle.
4. Destekleyici noktaları kaynağın sırasına göre değil, karar için önemine göre sırala. Her nokta rakamı veya kanıtıyla tek cümle olsun.
5. Bir seçim varsa seçenekleri, her birinin ödünleşimini gösteren kısa bir tabloda sun ve önerileni işaretle.
6. Temel riskleri ve gecikmenin veya hareketsizliğin maliyetini, yalnızca kaynak destekliyorsa yaz.
7. Talebi net yaz: kim neye, ne zamana kadar karar verecek ve karardan sonra ne olacak.
8. Jargonu iş etkisine (maliyet, risk, süre, müşteri, uyum) çevir; teknik bir terimi yalnızca okuyucu kullanıyorsa bırak.
9. Kaynakta olmayan her şeyi `[VARSAYIM]` olarak işaretle; önemli eksikleri üstünü örtmek yerine açık soru olarak listele.
10. Tek sayfaya (yaklaşık 250-400 kelime) indir; ayrıntı için kaynağa bağlantı ver.
11. Kullanıcının hedefi devam ediyorsa sunum sürümü için `steering-committee-pack`, seçeneklerin yapılandırılmış puanlanması gerekiyorsa `decision-matrix` öner.

## Çıktı formatı
```markdown
# Yönetici Özeti: <konu>
**Kime:** <okuyucu / kurul>   **Karar için son tarih:** <tarih veya [TBD]>

**Sonuç:** <1-2 cümlede sonuç ve talep>

**Gerekçe**
- <kanıtlı/rakamlı bulgu 1>
- <bulgu 2>
- <bulgu 3>

**Seçenekler**
| Seçenek | Fayda | Maliyet / risk | |
|---|---|---|---|
| A | ... | ... | Önerilen |

**Riskler ve hareketsizliğin maliyeti**
- ...

**Talep ve sonraki adımlar**
- <kim>, <ne> konusunda <tarih>'e kadar karar verir; ardından <sonraki adım>.

**Varsayımlar / açık sorular**
- ...
Kaynak: <bağlantı veya doküman adı>
```

## Kalite kontrol listesi
- [ ] İlk iki cümle tek başına sonucu ve talebi veriyor.
- [ ] Her rakam ve iddia kaynağa dayanıyor; ekleme yapılmadı.
- [ ] Seçenekler yalnızca önerilenin faydalarını değil, ödünleşimlerini de içeriyor.
- [ ] Dil iş etkisi odaklı; açıklanmamış jargon yok.
- [ ] En fazla bir sayfa.
- [ ] Varsayımlar ve eksikler gizlenmedi, listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Dokümanın sonuçlarını değil yapısını özetlemek ("2. bölüm ... konusunu ele alıyor").
- Öneriyi sona saklayan hikâye kurgusu. Yöneticiler erken bırakır; öneriyle başla.
- Öneri daha temiz görünsün diye rahatsız edici riski çıkarmak. Toplantıda mutlaka gündeme gelir ve güveni zedeler.

## Örnek
Girdi: 20 sayfalık tedarikçi değerlendirmesi, CIO gelecek hafta iki tedarikçi arasında seçim yapacak.

Zayıf: "Bu doküman RFP, demolar ve referans kontrollerinden oluşan değerlendirme sürecini özetlemektedir. Birçok kriter dikkate alınmıştır..."

Güçlü (bölüm):
**Sonuç:** B tedarikçisini seçin; tüm zorunlu gereksinimleri karşılıyor ve 3 yıllık maliyeti daha düşük `[rakam kaynağın 5. bölümünden]`. 1. çeyrek başlangıcını korumak için kararın `[tarih]` tarihli yönlendirme toplantısında verilmesi gerekiyor.
**Gerekçe:** A tedarikçisi veri yerleşimi gereksinimini karşılamıyor; B tüm referans kontrollerini geçti.
