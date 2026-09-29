---
description: "Parametre değerlerinin her ikilisini (kritik parametreler için daha yüksek dereceyi) değerler arası kısıtlara uyarak kapsayan azaltılmış bir test kombinasyonu seti üretir; azaltmayı ve kalan riski açıklar. Çok sayıda parametre veya yapılandırma (tarayıcı, cihaz, rol, ayar, ürün seçeneği) birleşince tümünü test etmek mümkün olmadığında kullanılır."
related: equivalence-boundary-analysis, decision-table-testing, test-case-writing, risk-based-testing, test-data-design
prompt: "Ödeme adımı için ikili kombinasyonlar üret: 4 tarayıcı, 3 ödeme yöntemi, 2 kullanıcı tipi, 3 teslimat seçeneği, kupon var/yok. Apple Pay yalnızca Safari'de."
---

# İkili Kombinasyon Testi

## Amaç
Etkileşim hatalarının çoğu bir veya iki parametre tarafından tetiklendiği için, parametreler arasındaki tüm ikili etkileşimleri toplam kombinasyon sayısının küçük bir kısmıyla kapsamak; bunu yaparken kısıtları geçerli tutmak ve kalan riski görünür kılmak.

## Ne zaman kullanılır
- Ortamlar, cihazlar, yerel ayarlar veya ayarlar arasında yapılandırma veya uyumluluk testi.
- Çok sayıda bağımsız seçeneği olan özellikler (ürün yapılandırıcılar, arama filtreleri, feature flag'ler).
- Tüm kombinasyonların sayısı mevcut süreyi aşıyor.

## Ne zaman kullanılmaz
- Sonuçlar kombinasyon bazında açık kurallarla belirleniyorsa `decision-table-testing` kullanılır.
- Tek bir parametrenin aralıkları önemliyse önce değerleri seçmek için `equivalence-boundary-analysis` kullanılır.
- Parametreler bağımsız değil, sıralıysa (iş akışı) `state-transition-testing` kullanılır.

## Girdiler
Zorunlu:
- Parametreler ve değerleri.

İsteğe bağlı, kaliteyi artırır:
- Kısıtlar (geçersiz veya zorunlu kombinasyonlar), değer bazında kullanım payı, bilinen riskli etkileşimler.
- İstenen derece (varsayılan ikili; kritik parametre grupları için üçlü).

Parametreler veya değerler eksikse iste. Değerler aralık ise önce sınıflara indir.

## Süreç
1. Parametreleri ve değerleri listele; değerlerin davranışsal olarak farklı olması için her değer setini denklik sınıflarıyla azalt.
2. Kısıtları açık kurallar olarak yaz (ör. Ödeme = Apple Pay ⇒ Tarayıcı = Safari; Misafir ⇒ kayıtlı kart yok).
3. Toplam kombinasyon sayısını ve teorik ikili alt sınırı (en büyük iki değer sayısının çarpımı) hesapla.
4. Kapsayan diziyi kur: en büyük iki parametreyi temel ızgara olarak al, kalan parametreleri satır satır, en çok kapsanmamış ikiliyi kapsayan ve kısıtları sağlayan değerlerle doldur. Büyük modellerde bir ikili kombinasyon üretecinin kullanılması gerektiğini belirt ve modeli araçtan bağımsız bir metin formatında ver.
5. Kapsamı doğrula: her değer ikilisini listele ve en az bir geçerli satırda yer aldığını teyit et; kısıt nedeniyle dışlanan ikilileri uygulanamaz olarak listele.
6. Tohum satırlar ekle: ikili olarak zaten kapsansa bile en çok kullanılan yapılandırmalar (en yaygın tarayıcı + ödeme) ve bilinen riskli kombinasyonlar.
7. Kapasite izin veriyorsa yüksek riskli parametre alt kümeleri için (ör. ödeme x para birimi x ülke) dereceyi üçlüye çıkar.
8. "Fark etmez" hücrelerini en sık kullanılan değerle doldur.
9. Azaltmayı, kalan riski (test edilmeyen yüksek dereceli etkileşimler) ve satırların test case'lere nasıl eşleneceğini raporla.

## Çıktı formatı
```markdown
# İkili Kombinasyonlar: <özellik>
Parametreler: <P1 (n değer), P2 (n değer), ...>
Kısıtlar: <liste>
Tüm kombinasyonlar: <n> · İkili satır: <n> · Derece: ikili (+ <alt küme> için üçlü)

| Satır | P1 | P2 | P3 | ... | Not (tohum / riskli) |
|---|---|---|---|---|---|

## Kapsam Kontrolü
- Tüm geçerli ikililer kapsandı: <Evet / eksiklerin listesi>
- Kısıtla dışlanan ikililer: <liste>

## Kalan Risk
- <kapsanmayan yüksek dereceli etkileşimler>
```

## Kalite kontrol listesi
- [ ] Her geçerli değer ikilisi en az bir satırda yer alıyor.
- [ ] Hiçbir satır bir kısıtı ihlal etmiyor.
- [ ] Yüksek kullanımlı ve bilinen riskli kombinasyonlar açıkça dahil.
- [ ] Parametre değerleri rastgele örnekler değil, davranışsal olarak farklı sınıflar.
- [ ] Kalan risk belirtildi.

## Sık yapılan hatalar
- Kısıtları unutup koşturulamayacak satırlar üretmek.
- Sonuç kurallarının açık olduğu yerde ikili kombinasyon kullanmak; tam kural kombinasyonu kaçabilir.
- İkili kombinasyonu eksiksiz test sanmak. İkilileri kapsar, her üçlü etkileşimi değil.

## Örnek
Girdi: "4 tarayıcı, 3 ödeme, 2 kullanıcı tipi, 3 teslimat seçeneği, kupon var/yok; Apple Pay yalnızca Safari'de."

Çıktıdan bir bölüm:
Tüm kombinasyonlar: 144 · İkili satır: 13 (alt sınır 12, kısıt nedeniyle +1)
| 1 | Chrome | Kart | Üye | Standart | Var | tohum (en yüksek kullanım) |
| 5 | Safari | Apple Pay | Misafir | Ekspres | Yok | |
- Dışlanan ikililer: Apple Pay ile Chrome, Firefox, Edge.
