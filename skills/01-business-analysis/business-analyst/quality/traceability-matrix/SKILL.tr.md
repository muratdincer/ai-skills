---
description: "İş hedeflerini ve kaynakları gereksinimlere, tasarım öğelerine, test senaryolarına ve sürümlere iki yönlü bağlayan bir gereksinim izlenebilirlik matrisi oluşturur; sahipsiz öğeleri, karşılanmamış gereksinimleri ve kapsam yüzdelerini raporlar. Denetim, düzenleyici kurum veya müşteri kapsam kanıtı istediğinde, sürüm veya UAT öncesinde ya da bir değişikliğin etkilediği öğeler araştırılırken kullanılır."
related: "requirements-gap-analysis, impact-analysis, test-scenarios-from-requirements, requirements-sign-off, release-quality-gate"
prompt: "Bu 30 gereksinim ve 55 test senaryosundan izlenebilirlik matrisi oluştur, nelerin karşılanmadığını göster."
---

# İzlenebilirlik Matrisi

## Amaç
Her gereksinimin meşru bir kaynaktan geldiğini, tasarlandığını, geliştirildiğini ve test edildiğini; gereksinimi olmayan hiçbir şeyin geliştirilmediğini veya test edilmediğini kanıtlamak. Matris denetimleri, değişiklik etkisini ve sürüm kararlarını destekler.

## Ne zaman kullanılır
- Kapsam kanıtı gerektiren düzenlemeye tabi veya sözleşmeli projelerde (ör. finans, sağlık, kamu).
- UAT veya sürüm kalite kapısından önce.
- Bir değişiklik talebi geldiğinde etkilenen test ve tasarımların hızla bulunması gerektiğinde.

## Ne zaman kullanılmaz
- Yalnızca tek bir değişikliğin etkisi gerekiyorsa `impact-analysis` kullanılır.
- Test senaryoları henüz yok ve türetilmesi gerekiyorsa `test-scenarios-from-requirements` kullanılır.
- Kapsam değil eksik gereksinim aranıyorsa `requirements-gap-analysis` kullanılır.

## Girdiler
Zorunlu:
- ID'li gereksinim listesi.
- ID'leriyle birlikte en az bir başka bağlanacak set: hedefler/kaynaklar, tasarımlar, test senaryoları veya sürümler.

İsteğe bağlı, kaliteyi artırır:
- Mevcut bağlantılar (ör. test senaryosundaki "kapsar" alanı, hikaye-epik bağları).
- Test koşum sonuçları ve hata ID'leri.
- Kurumun veya düzenleyicinin tanımladığı zorunlu izleme seviyeleri.

ID'ler yoksa bir ID şeması öner ve eşlemeye başlamadan önce kullanıcıdan onay al.

## Süreç
1. İzleme seviyelerini netleştir: ör. İş hedefi / Kaynak → Gereksinim → Tasarım öğesi → Test senaryosu → Test sonucu → Sürüm. Yalnızca verisi olan seviyeleri kullan; diğerlerini `[N/A]` veya `[TBD]` işaretle.
2. Her set için ID ve sürümleri normalleştir.
3. Önce açık bağlantıları (alanlar, referanslar) kullan. Metin benzerliğinden bağlantı çıkarımını yalnızca gerektiğinde yap ve teyit için `[ÇIKARIM]` olarak işaretle.
4. İleri izlenebilirliği kur: her gereksinimden tasarımına, testlerine, sonuçlarına ve sürümüne.
5. Geri izlenebilirliği kur: her test ve tasarım öğesinden bir gereksinime; her gereksinimden bir hedef veya kaynağa.
6. Sorunları belirle: testi olmayan gereksinimler, gereksinimi olmayan testler (sahipsiz), kaynağı olmayan gereksinimler, kapsamdaki gereksinimlerde başarısız veya koşulmamış testler, açık hatası olan gereksinimler.
7. Kapsamı hesapla: en az bir testi olan, en az bir başarılı testi olan gereksinimler; önceliğe göre kırılım.
8. Kapsamı zayıf yüksek öncelikli veya mevzuat kaynaklı gereksinimleri en başta vurgula.
9. Bakım kurallarını belirt: matrisi kim, ne zaman günceller (her değişiklik talebinde, her test döngüsünde).

## Çıktı formatı
```markdown
# İzlenebilirlik Matrisi: <kapsam> · Temel sürüm <sürüm> · Tarih <tarih>

## Kapsam Özeti
| Metrik | Değer |
|---|---|
| Toplam gereksinim | n |
| ≥1 test senaryosu olan | n (%x) |
| ≥1 başarılı testi olan | n (%x) |
| Sahipsiz test senaryosu | n |
| Kaynağı olmayan gereksinim | n |

## Matris
| Ger. ID | Öncelik | Kaynak / Hedef | Tasarım ref. | Test senaryosu ID'leri | Son sonuç | Açık hatalar | Sürüm | Durum |
|---|---|---|---|---|---|---|---|---|

## Sorunlar
| # | Tür | Öğe | Ayrıntı | Aksiyon | Sorumlu |
|---|---|---|---|---|---|

## Bakım
- Güncelleme tetikleyicisi: <değişiklik talebi / test döngüsü / sürüm>
- Sorumlu: <rol>
```

## Kalite kontrol listesi
- [ ] Hem ileri hem geri yön kontrol edildi.
- [ ] Çıkarımla kurulan bağlantılar `[ÇIKARIM]` olarak işaretli ve teyit için listelendi.
- [ ] Kapsam yüzdeleri tahmin değil, matristen hesaplandı.
- [ ] Eksiği olan yüksek öncelikli ve mevzuat kaynaklı gereksinimler en başta.
- [ ] Her sorunun bir aksiyonu ve sorumlu rolü var.

## Sık yapılan hatalar
- Test hiç koşulmadığı veya başarısız olduğu halde, test var diye gereksinimi karşılanmış saymak. "Test edildi" ile "geçti"yi ayrı raporla.
- Testleri gereksinimlere yalnızca epik düzeyinde bağlamak. Doğrulanan en alt gereksinim seviyesinde izle.
- Matrisi bir kez kurup hiç güncellememek. Güncellemeyi değişiklik kontrolüne ve test döngülerine bağla.

## Örnek
Girdi: REQ-01..REQ-05; TC-10 REQ-01'i, TC-11 REQ-01 ve REQ-03'ü kapsıyor, TC-12'nin referansı yok.

Çıktıdan bir bölüm:
| Ger. ID | Öncelik | Kaynak / Hedef | Tasarım ref. | Test senaryosu ID'leri | Son sonuç | Durum |
|---|---|---|---|---|---|---|
| REQ-01 | Yüksek | BRD 3.1 | [TBD] | TC-10, TC-11 | Geçti | Karşılandı |
| REQ-02 | Yüksek | Yönetmelik md. 5 | [TBD] | – | – | Karşılanmadı |

Sorunlar: REQ-02 (mevzuat) için test yok – test senaryosu oluştur, sorumlu QA lideri; TC-12 sahipsiz – bağla veya kaldır.
