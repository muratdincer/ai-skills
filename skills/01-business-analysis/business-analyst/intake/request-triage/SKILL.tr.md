---
description: "Gelen bir veya birden çok iş talebini tür, aciliyet, değer, efor sınıfı ve riske göre sınıflandırır, mükerrerleri bulur ve her birini doğru yola (hızlı yol, analiz, fizibilite, proje, destek, ret) yönlendirir. Yeni taleplerden oluşan bir kuyruk sıralanacağında, talep değerlendirme toplantısında veya 'bu talepler nereye gitmeli, önce hangisi?' sorusu geldiğinde kullanılır."
related: "request-intake-document, request-completeness-check, ticket-triage, backlog-prioritization, change-request-analysis"
prompt: "Bu haftaki gelen kutusundaki 8 talebi sınıflandır; hangileri analize gider, hangileri destek kaydı, hangilerini reddetmeliyiz söyle."
---

# Gelen Talepleri Sınıflandırma

## Amaç
Sıralanmamış talep akışını yönlendirilmiş ve gerekçelendirilmiş bir listeye dönüştürmek. Böylece kapasite doğru işe gider, talep sahipleri de hızlı ve açıklanabilir bir cevap alır.

## Ne zaman kullanılır
- Bir gelen kutusunda, formda veya talep panosunda yeni talepler biriktiğinde.
- Haftalık talep değerlendirme toplantısı öncesinde.
- Çok farklı boyut ve türde talepler aynı kanaldan geldiğinde.

## Ne zaman kullanılmaz
- Tek bir talebin önce düzgünce yazılması gerekiyorsa `request-intake-document` kullanılır.
- Kayıtlar olay veya servis masası talebiyse `ticket-triage` kullanılır.
- Olgunlaştırılmış backlog maddeleri sıralanacaksa `backlog-prioritization` kullanılır.

## Girdiler
Zorunlu:
- Talepler (metin, liste veya talep alma dokümanları).

İsteğe bağlı, kaliteyi artırır:
- Kurumda mevcut yönlendirme yolları (ör. küçük değişiklik yolu, proje kapısı, servis masası).
- Güncel stratejik hedefler veya OKR'ler, kapasite kısıtları, dondurma (freeze) dönemleri.
- Kullanılan sınıflandırma kriterleri veya puanlama modeli.

Talep verilmemişse iste. Yönlendirme yolları bilinmiyorsa aşağıdaki varsayılan seti kullan ve bunu belirt.

## Süreç
1. Her talebi tek satıra indir: talep sahibi, ihtiyaç, belirtilen tarih. Numarası yoksa geçici bir ID ver.
2. Mükerrer ve örtüşen talepleri bul; birleştir veya ilişkilendir, ilgili talep sahiplerini not et.
3. Türü sınıflandır: yeni özellik, mevcut özellikte değişiklik, rapor/veri, entegrasyon, yasal/uyum, teknik/altyapı, hata/olay (yanlış kanal), soru/yetki talebi (yanlış kanal).
4. Aciliyeti bir olaya bağlı gerekçeyle puanla: yasal tarih, sözleşme tarihi, dönemsel gelir/maliyet etkisi, operasyonel risk. Tek başına "en kısa sürede" zayıf bir kanıttır.
5. Değeri belirtilen hedeflere göre (Y/O/D) puanla; efor sınıfını yalnızca kaba bir aralık olarak T-shirt boyutuyla (XS-XL) ver ve `[VARSAYIM]` olarak işaretle.
6. Risk işaretlerini belirt: kişisel veri, finansal hesaplama, dış taraflar, birden çok sistem, geri alınamaz değişiklikler.
7. Hazırlığı kontrol et: yönlendirmeye yetecek bilgi var mı? Yoksa 2-3 engelleyici soruyla "netleştir" yoluna yönlendir.
8. Her talebi yönlendir. Varsayılan yollar: Hızlı yol (XS/S, düşük risk, net), Analiz, Fizibilite/tahmin, Proje/portföy kapısı, Servis masası/destek, Netleştir, Ret/beklet (saygılı bir gerekçeyle).
9. Yönlendirilen maddeler için aciliyet ve değere dayalı bir sıra öner; gizli bir puan değil, gerekçeyi göster.
10. Her talep sahibine gidecek tek satırlık cevabı taslak olarak yaz.

## Çıktı formatı
```markdown
# Talep Sınıflandırma – <tarih / parti adı>

| ID | Talep (tek satır) | Tür | Aciliyet | Değer | Efor aralığı | Risk işaretleri | Yol | Gerekçe |
|---|---|---|---|---|---|---|---|---|
| T1 | ... | ... | Y – yasal tarih | O | S [VARSAYIM] | Kişisel veri | Analiz | ... |

## Mükerrer / birleştirilen
- T3 + T6: ...

## Netleştirme gerekenler
- T4: <engelleyici sorular>

## Önerilen sıra
1. T1 – ...

## Talep sahiplerine mesajlar
- T5 (ret/beklet): ...
```

## Kalite kontrol listesi
- [ ] Her talebin tam olarak bir yolu ve bir gerekçesi var.
- [ ] Aciliyet puanları talep sahibinin üslubuna değil, somut bir olay veya etkiye dayanıyor.
- [ ] Efor aralıkları varsayım olarak işaretli; saat veya para uydurulmadı.
- [ ] Yanlış kanaldan gelen olaylar ve yetki talepleri analize değil, desteğe gönderildi.
- [ ] Reddedilen veya bekletilen maddelerin saygılı ve somut bir gerekçesi var.
- [ ] Mükerrerler ilişkilendirildi, hiçbir talep sahibi unutulmadı.

## Sık yapılan hatalar
- En yüksek sesle isteyene veya kıdeme göre sıralamak. Belirtilen hedeflere ve olay tarihlerine dayan.
- Her şeyi analize göndermek. Küçük, net ve düşük riskli değişiklikler için hızlı yol, analistleri gerçek problemlere ayırır.
- Talepleri sessizce bekletmek. Her talep sahibi bir cevap ve bir sonraki adım almalı.

## Örnek
Girdi: "T1 Finans: KDV oranı değişikliği 1 Ocak'tan itibaren faturalara yansımalı. T2 Pazarlama: yeni bir pano 'olsa iyi olur'. T3 Kullanıcı portala giriş yapamıyor."

Çıktıdan bir bölüm:
| ID | Tür | Aciliyet | Değer | Yol | Gerekçe |
|---|---|---|---|---|---|
| T1 | Yasal | Y – yasal yürürlük tarihi | Y | Analiz (öncelikli) | Vergi hesabı, faturalar, muhtemelen raporlar etkileniyor |
| T2 | Rapor/veri | D – tarih yok | [BİLİNMİYOR] | Netleştir | Panonun hedefi ve desteklediği kararlar belirtilmemiş |
| T3 | Olay (yanlış kanal) | – | – | Servis masası | Erişim sorunu, değişiklik talebi değil |
