---
description: "Girdi alanlarına, parametrelere ve iş kurallarına denklik sınıfı bölümleme ve sınır değer analizi uygular; geçerli ve geçersiz sınıfları, sınır değerlerini (iki veya üç değerli) ve beklenen sonuçlarıyla en küçük test değeri setini üretir. Bir girdide aralık, uzunluk, format, tarih veya sabit liste olduğunda ya da bir alan veya kural için hangi değerlerin test edileceği sorulduğunda kullanılır."
related: test-case-writing, decision-table-testing, pairwise-testing, test-data-design, test-scenarios-from-requirements
prompt: "Kredi başvurusuna sınır değer analizi uygula: tutar 1.000-50.000, vade 6-60 ay, başvuru sahibinin kredi bitişindeki yaşı 18-70."
---

# Denklik Sınıfı ve Sınır Değer Analizi

## Amaç
Neredeyse sonsuz girdi uzayını, her davranış sınıfını bir kez ve bir-eksik/bir-fazla ile karşılaştırma hatalarının yoğunlaştığı her kenarı çalıştıran, savunulabilir küçük bir test değeri setine indirmek.

## Ne zaman kullanılır
- Alanlarda veya parametrelerde sayısal aralık, uzunluk, format, tarih, sabit liste veya adet kısıtı var.
- İş kuralları eşik içeriyor (indirim kademeleri, yaş sınırları, kesim saatleri).
- Test uzmanı, seçilen değer setinin neden yeterli olduğunu gerekçelendirmek zorunda.

## Ne zaman kullanılmaz
- Davranış birden fazla koşulun kombinasyonuna bağlıysa `decision-table-testing` kullanılır.
- Çok sayıda bağımsız parametre verimli biçimde birleştirilecekse `pairwise-testing` kullanılır.
- Davranış geçmişe veya duruma bağlıysa `state-transition-testing` kullanılır.

## Girdiler
Zorunlu:
- Belirtilmiş kısıtlarıyla birlikte alanlar, parametreler veya kurallar.

İsteğe bağlı, kaliteyi artırır:
- Veri tipleri ve saklama sınırları (ör. kolon uzunluğu, tamsayı boyutu), formatlar, yerel ayar kuralları.
- Sınırların dahil mi hariç mi olduğu; yuvarlama ve hassasiyet kuralları.

Bir kısıt belirtilmemişse varsayma. Açık soru olarak listele ve aday değerleri `[VARSAYIM]` ile işaretle.

## Süreç
1. Her girdiyi tip, birim, hassasiyet ve belirtilmiş kısıtlarıyla listele. Sınırların dahil olup olmadığını not et.
2. Geçerli sınıfları (her farklı beklenen davranış için bir tane, ör. her indirim kademesi) ve geçersiz sınıfları (minimumun altı, maksimumun üstü, yanlış tip, yanlış format, boş, null) belirle.
3. Gizli sınıfları ekle: teknik sınırlar (alan uzunluğu, tamsayı taşması), özel değerler (0, negatif, boşluk, baştaki sıfırlar, Unicode, yerel ayara göre ondalık ayırıcı), tarih özel durumları (artık gün, ay sonu, yaz saati geçişi).
4. Sıralı her sınıf sınırı için değer seç: varsayılan olarak iki değer yöntemi (sınır ve en yakın geçersiz komşu); yüksek riskli kurallar için üç değer yöntemi (altı, üstü, kendisi).
5. Hassasiyete göre en küçük anlamlı adımı kullan (tamsayı için 1, para için 0,01, zaman için 1 saniye veya 1 gün).
6. Bağımlı veya hesaplanan sınırlarda (kredi bitişindeki yaş = bugünkü yaş + vade) yalnızca ham girdilerde değil, hesaplanan değer üzerinde de sınır türet.
7. Sınır olmayan her sınıf için bir temsilci seç.
8. Her değere beklenen sonucu ata; geçersiz değerler için biliniyorsa tam ret davranışını, bilinmiyorsa `[BİLİNMİYOR]` yaz.
9. Birleştir: geçerli değerleri mümkünse birlikte test et; hatalar ayırt edilebilsin diye her geçersiz değeri tek başına test et.
10. Sınıf tablosunu, değer tablosunu ve açık soruları çıktı olarak ver.

## Çıktı formatı
```markdown
# Denklik Sınıfı ve Sınır Değer Analizi: <özellik>
## Sınıflar
| Girdi | Sınıf ID | Tanım | Geçerli mi? | Beklenen davranış |
## Test Değerleri
| TD | Girdi | Değer | Sınıf | Sınır mı? | Beklenen sonuç |
## Birleşik Test Seti
| Case | Değerler | Beklenen |
## Açık Sorular
- <dahil/hariç, hassasiyet, hata metni>
```

## Kalite kontrol listesi
- [ ] Her sınıfın en az bir değeri, sıralı her sınırın sınır ve komşu değerleri var.
- [ ] Geçersiz değerler tek tek test ediliyor.
- [ ] Adım büyüklüğü veri hassasiyetiyle uyumlu.
- [ ] Hesaplanan ve alanlar arası sınırlar dikkate alındı.
- [ ] Belirtilmemiş sınırlar olgu gibi sunulan varsayımlar değil, soru olarak yazıldı.

## Sık yapılan hatalar
- Yalnızca gereksinimdeki sınırları test edip teknik sınırları (veritabanındaki maksimum uzunluk, tamsayı boyutu) yok saymak.
- Daha ince hassasiyetli para veya zaman alanlarında 1'lik adım kullanmak.
- Tek case'te birden fazla geçersiz değeri karıştırıp hangi doğrulamanın başarısız olduğunu gizlemek.

## Örnek
Girdi: "Tutar 1.000-50.000, vade 6-60 ay, kredi bitişinde yaş 18-70."

Çıktıdan bir bölüm:
| TD-1 | Tutar | 999,99 | Minimum altı | Evet | Reddedilir |
| TD-2 | Tutar | 1.000,00 | Geçerli | Evet | Kabul edilir |
| TD-3 | Tutar | 50.000,00 | Geçerli | Evet | Kabul edilir |
| TD-4 | Tutar | 50.000,01 | Maksimum üstü | Evet | Reddedilir |
| TD-9 | Bitişteki yaş | 70 yıl 0 gün (yaş 65 + 60 ay) | Geçerli | Evet | Kabul edilir `[VARSAYIM: 70 dahil]` |
- Açık soru: "Kredi bitişinde 70 yaş" dahil mi ve yaş tam doğum tarihine göre mi hesaplanıyor?
