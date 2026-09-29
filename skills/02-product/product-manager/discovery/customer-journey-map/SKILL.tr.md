---
description: Bir persona ve senaryo için müşteri yolculuğunu aşamalar boyunca eylemler, düşünceler, duygular, temas noktaları, kanallar, sorunlar, kritik anlar ve arka plandaki sorumlularla haritalar; iyileştirme fırsatlarını sıralar. Uçtan uca bir deneyimin anlaşılması, müşterilerin nerede zorlandığının veya vazgeçtiğinin bulunması, kanallar arası ekiplerin hizalanması gerektiğinde ya da yolculuk haritası istendiğinde kullanılır.
related: persona, jobs-to-be-done, funnel-analysis, user-flow, as-is-process
prompt: Web sitemiz ve çağrı merkezimiz üzerinden ilk kez konut sigortası alan müşterinin yolculuğunu haritala.
---

# Müşteri Yolculuğu Haritası

## Amaç
Bir müşteri tipinin tek bir senaryodaki uçtan uca deneyimini, her aşamada ne yaptığı, ne düşündüğü ve ne hissettiğiyle birlikte göstermek. Böylece ekipler deneyimin nerede bozulduğunu ve düzeltmenin kime ait olduğunu görebilir.

## Ne zaman kullanılır
- Bir deneyim birden fazla kanala veya ekibe yayılıyor ve bütünü kimse görmüyorsa.
- Dönüşüm, memnuniyet veya şikâyet verisi bir sorun gösteriyor ama nereden kaynaklandığını göstermiyorsa.
- Yeni bir hizmet tasarlanırken veya mevcut bir hizmet yeniden tasarlanırken.

## Ne zaman kullanılmaz
- Ekran düzeyinde gezinme gerekiyorsa `user-flow` kullanılır.
- İç süreç adımları ve roller gerekiyorsa `as-is-process` kullanılır.
- Adım başına nicel kayıp gerekiyorsa `funnel-analysis` kullanılır.

## Girdiler
Zorunlu:
- Persona veya müşteri tipi ve senaryo (başlangıç ve bitiş noktası).

İsteğe bağlı, kaliteyi artırır:
- Araştırma bulguları, analitik, destek kayıtları, NPS/CSAT yorumları, kanal listesi, iç süreç bilgisi.
- Haritanın mevcut durum mu yoksa gelecek durum mu olduğu.

Persona veya senaryo yoksa sor. Kanıtla desteklenmeyen maddeler `[VARSAYIM]` olarak işaretlenir; yorumlardaki kişisel verileri çıkar.

## Süreç
1. Kapsamı sabitle: bir persona, bir senaryo, mevcut veya gelecek durum, başlangıç tetikleyicisi ve bitiş noktası.
2. Organizasyon şemanıza göre değil, müşterinin bakış açısından 5-8 aşama tanımla (ör. farkına var, değerlendir, satın al, başla, kullan, yardım al, yenile).
3. Her aşama için müşteri eylemlerini, düşünce/sorularını, duygusunu (-2 ile +2 arası), temas noktalarını ve kanalları kaydet.
4. Her aşamadaki sorunları ve kazanımları kanıtıyla (alıntı, metrik, kayıt kategorisi) kaydet.
5. Kritik anları işaretle: duygunun veya kararın elde tutmayı ya da vazgeçmeyi belirlediği aşamalar.
6. Arka planı ekle: her temas noktasının arkasındaki iç ekipler, sistemler, politikalar ve sorumlu.
7. Fırsatları belirle: her biri bir soruna bağlı, beklenen etki ve eforu (Y/O/D) ve sorumlusu belli olsun.
8. Fırsatları sırala; önce ele alınacak 2-3 fırsatı ve değişmesi gereken metrikleri öner.

## Çıktı formatı
```markdown
# Müşteri Yolculuğu: <persona> — <senaryo> (<mevcut/gelecek> durum)
Tetikleyici: ... · Bitiş: ... · Kanıt: <kaynaklar>

| | Aşama 1 | Aşama 2 | ... |
|---|---|---|---|
| Eylemler | | | |
| Düşünceler / sorular | | | |
| Duygu (-2..+2) | | | |
| Temas noktaları / kanallar | | | |
| Sorunlar | | | |
| Arka plan / sorumlu | | | |

## Kritik Anlar
- ...

## Fırsatlar
| # | Fırsat | Ele alınan sorun | Etki | Efor | Sorumlu | Metrik |
|---|---|---|---|---|---|---|

## Boşluklar ve Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Yalnızca bir persona ve bir senaryo var.
- [ ] Aşamalar müşterinin bakış açısından tanımlandı.
- [ ] Duygular ve sorunlar kanıta dayanıyor ya da `[VARSAYIM]` olarak işaretli.
- [ ] Her fırsat belirli bir soruna bağlı ve sorumlusu var.
- [ ] Bozuk temas noktaları için arka plan sorumluları adlandırıldı.

## Sık yapılan hatalar
- İdeal yolculuğu çizip mevcut durum demek. Gerçekte ne olduğuna dair kanıt kullan.
- Tüm personaları tek haritada toplamak. Farklı hedefler farklı yolculuklar üretir.
- Takibi olmayan bir poster üretmek. Önceliklendirilmiş fırsatlar ve sorumlularla bitir.

## Örnek
Girdi: "İlk kez konut sigortası alan müşteri, web sitesi ve çağrı merkezi."

Çıktıdan bir bölüm:
- "Teklif al" aşaması: Eylem: 4 sayfalık formu dolduruyor; Düşünce: "Neden daha şimdiden kimlik numaramı istiyorlar?"; Duygu: -1; Sorun: 3. adımda formu terk etme `[analitiği teyit et]`.
- Kritik an: teminatı teyit etmek için ilk arama; uzun bekleme süresi vazgeçmeye yol açıyor.
- Fırsat: kimlik verisi istemeden önce tahmini fiyat göster — sorumlu: Dijital Satış.
