---
description: "Bir girişimi etkileyen, ondan etkilenen veya hakkında karar veren herkesi, gizli ve dolaylı paydaşlar (uyum, operasyon, veri sahipleri, dış taraflar) dahil olmak üzere rolleri, ilgi alanları ve onlardan ne gerektiğiyle birlikte belirler. Bir talebin, projenin veya analizin başında ya da 'kimleri dahil etmemiz gerekiyor?' sorusu geldiğinde kullanılır."
related: "stakeholder-map, raci-matrix, stakeholder-register, request-intake-document, communication-plan"
prompt: "Kağıt tabanlı masraf onayını dijital iş akışıyla değiştirme projesinin paydaşları kimler?"
---

# Paydaşları Belirleme

## Amaç
Erken aşamada eksiksiz ve kategorilere ayrılmış bir paydaş listesi çıkarmak. Böylece hiçbir karar verici, etkilenen grup veya veto sahibi geç ortaya çıkıp yeniden işe yol açmaz.

## Ne zaman kullanılır
- Yeni bir talep, proje veya analiz başlarken.
- Gereksinimler toplanırken kimlerle görüşüleceği bilinmek istendiğinde.
- Bir değişiklik birden çok departmanı, sistemi veya dış tarafı etkilediğinde.

## Ne zaman kullanılmaz
- Paydaşlar biliniyor ve güç/ilgiye göre önceliklendirilmesi gerekiyorsa `stakeholder-map` kullanılır.
- Aktivite bazında sorumluluk atanacaksa `raci-matrix` kullanılır.
- İletişim ve katılım takibi olan bir proje yönetimi kaydı gerekiyorsa `stakeholder-register` kullanılır.

## Girdiler
Zorunlu:
- Girişimin veya talebin tanımı (kaba da olsa hedef ve kapsam).

İsteğe bağlı, kaliteyi artırır:
- Organizasyon şeması veya departman listesi, etkilenen sistemler, bilinen dış taraflar.
- Talep sahibinin zaten andığı kişiler.

Girişim tanımı yoksa iste. Kişiler bilinmiyorsa isim uydurma, rol kullan.

## Süreç
1. Analizi sabitlemek için girişimin kapsamını tek cümleyle yeniden yaz.
2. Değer zincirini izle: süreci kim tetikliyor, her adımı kim yapıyor, çıktıyı kim kullanıyor, kim ödüyor.
3. Sık atlanan gruplar listesini uygula: sponsor/bütçe sahibi, segmentlere göre son kullanıcılar, son kullanıcıların yöneticileri, operasyon/destek, etkilenen her sistemin BT sahibi, veri sahipleri/sorumluları, güvenlik, hukuk/uyum/KVKK irtibat kişisi, iç denetim, finans, İK/sendika (roller veya izleme değişiyorsa), satın alma, müşteriler, tedarikçiler/iş ortakları, düzenleyici kurumlar, eğitmenler.
4. Veriyi ve sistemleri izle: dokunulan her sistem ve veri seti bir sahip demektir.
5. Her paydaşı kategorilere ayır: Karar verir, Etkiler, Etkilenir, Bilgilendirilir; iç veya dış.
6. Her biri için ilgisini (ne kazanıyor veya neden endişe ediyor) ve ondan ne gerektiğini (onay, girdi, veri, test, imza) yaz.
7. Veto sahiplerini ve yokluğu risk olan paydaşları işaretle.
8. Eksikleri listele: kişisi bilinmeyen rolleri `[BİLİNMİYOR]` olarak işaretle ve kimin isim verebileceğini yaz.

## Çıktı formatı
```markdown
# Paydaşlar: <girişim>
Kapsam: <tek cümle>

| # | Paydaş (rol / grup) | Ad | İç/Dış | Kategori | İlgi / endişe | Ondan beklenen | Veto? |
|---|---|---|---|---|---|---|---|
| 1 | Sponsor | [BİLİNMİYOR] | İç | Karar verir | ... | Bütçe, öncelik kararları | Evet |

## Gizli veya kolay atlanan
- ...

## Çözülecek bilinmeyenler
- <rol> – kişiyi kim söyleyebilir: ...
```

## Kalite kontrol listesi
- [ ] Etkilenen her sistem ve veri setinin bir sahibi listelendi.
- [ ] Uyum, güvenlik, operasyon ve destek açıkça değerlendirildi.
- [ ] Dış taraflar (müşteriler, tedarikçiler, düzenleyiciler) değerlendirildi.
- [ ] İsim uydurulmadı; bilinmeyen kişiler `[BİLİNMİYOR]` işaretli roller olarak yazıldı.
- [ ] Her paydaşın somut bir "ondan beklenen" maddesi var.
- [ ] Veto sahipleri işaretlendi.

## Sık yapılan hatalar
- Yalnızca talep sahibinin departmanını listelemek. Süreci ve veriyi uçtan uca izle.
- "Kullanıcılar"ı tek grup saymak. Rol, kanal veya hacme göre ayır; ihtiyaçları farklıdır.
- Bir şey kaybedenleri (iş yükü, kontrol, kadro) görmezden gelmek. En güçlü direnç çoğu zaman onlardan gelir.

## Örnek
Girdi: "Kağıt tabanlı masraf onayını dijital bir iş akışıyla değiştirelim."

Çıktıdan bir bölüm:
| # | Paydaş | Kategori | İlgi / endişe | Ondan beklenen | Veto? |
|---|---|---|---|---|---|
| 1 | CFO (sponsor) | Karar verir | Daha hızlı kapanış, kontrol | Onay politikası kararları | Evet |
| 2 | Masraf giren çalışanlar | Etkilenir | Geri ödeme hızı, mobilde kolaylık | Kullanılabilirlik girdisi, UAT | Hayır |
| 3 | İç denetim | Etkiler | Kanıtların saklanması, görevler ayrılığı | Kontrol gereksinimleri | Evet |
| 4 | Bordro/ERP sistem sahibi | Etkiler | Entegrasyon yükü | Arayüz tanımı | Hayır |
