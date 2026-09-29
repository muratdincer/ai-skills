---
description: "İki sistem veya mesaj arasında kaynak-hedef alan eşlemesi üretir: her hedef alan için kaynak, dönüşüm, varsayılan değer, doğrulama, kod değeri çevirisi, boş ve hatalı değer yönetimi; ayrıca iki taraftaki eşlenmeyen alanlar ve açık kararlar. Bir entegrasyon, API adaptörü, veri değişim dosyası veya sistem değişimi yapılırken, iki sistemin kayıt alışverişi gerektiğinde ya da 'hangi alan nereye gidiyor, nasıl dönüştürülüyor?' sorusu sorulduğunda kullanılır."
related: "integration-requirements, api-contract, source-to-target-mapping, data-quality-rules, error-scenario-catalog"
prompt: "CRM dışa aktarımındaki müşteri alanlarını yeni faturalama sisteminin müşteri API'sine kod dönüşümleri dahil eşle."
---

# Sistemler Arası Alan Eşleme

## Amaç
Her hedef değerin nereden geldiğini, nasıl dönüştürüldüğünü ve kaynak boş ya da hatalıysa ne olacağını alan alan belirterek sistem entegrasyonundaki tahmin payını ortadan kaldırmak. Geliştiriciler bunun üzerine inşa eder, test uzmanları buna göre doğrular.

## Ne zaman kullanılır
- İki sistem bir API, mesaj, dosya veya veritabanı bağlantısı üzerinden kayıt alışverişi yapıyorsa.
- Bir sistem değiştiriliyor ve verisinin ya da arayüzlerinin yeniden yönlendirilmesi gerekiyorsa.
- Mevcut bir arayüz yanlış veya eksik değer üretiyor ve eşlemenin açık hâle getirilmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Veri ambarı veya analitik veri hattı için kolon düzeyinde köken gerekiyorsa `source-to-target-mapping` kullanılır.
- Arayüzün kendisi (protokol, sıklık, SLA'lar) henüz netleşmediyse önce `integration-requirements` kullanılır.
- Mevcut bir API'ye eşleme yerine yeni bir API tasarımı gerekiyorsa `api-contract` kullanılır.

## Girdiler
Zorunlu:
- Kaynak ve hedef yapı: alan listeleri, şemalar, örnek yükler (payload) veya ekran alanları.
- Veri alışverişinin yönü ve amacı.

İsteğe bağlı, kaliteyi artırır:
- İki taraftaki kod listeleri ve referans veriler, örnek kayıtlar (maskelenmiş), iş kuralları.
- Hacimler, sıklık ve akışın yalnızca oluşturma mı yoksa oluşturma/güncelleme/silme mi olduğu.

Yapılardan biri yoksa iste. Alan adı uydurma; bilinmeyenler `[TBD]` olur.

## Süreç
1. Kapsamı teyit et: yön, varlık veya mesaj, işlem türleri (oluşturma, güncelleme, silme, upsert) ve kayıtları sistemler arasında eşleştirmek için kullanılan anahtar.
2. Neyin zorunlu olduğunu hedef sözleşme belirlediği için hedef alanları hedefteki sırayla listele. Her biri için tür, uzunluk, format, zorunluluk ve izinli değerleri not et.
3. Her hedef alan için kaynağı bul: doğrudan alan, birleştirilen birkaç alan, kuralla türetilen, sabit, referans veriden arama veya kaynak yok. Kaynak alan yolunu birebir yaz.
4. Dönüşümü kesin tanımla: tür ve format dönüşümü (tarih, saat dilimi, ondalık ayırıcı, para birimi, karakter kodlaması), kırpma, birleştirme veya bölme, birim dönüşümü, yuvarlama kuralı.
5. Her sayılı değer alanı (durum, ülke, ürün tipi) için kod değeri çeviri tablosu oluştur. Her kaynak değer ya tek bir hedef değere ya da açık bir hataya eşlenir; sessiz varsayılan yok.
6. Her alan için boş, eksik ve hatalı değer yönetimini tanımla: varsayılan değer, kaydı reddetme, alanı göndermeme veya manuel düzeltmeye yönlendirme. Güncellemelerde "boş" ile "gönderilmedi"yi ayır.
7. İki taraftaki eşlenmeyen alanları listele: kaybolacak kaynak veriler ve boş kalacak hedef alanlar. Her kaybın kabul edilebilir olduğunu veri sahibine teyit ettir.
8. Kişisel ve hassas alanları işaretle; maskeleme, minimizasyon veya şifrelemeyi belirt; hedefin ihtiyaç duymadığı kişisel veriyi eşleme.
9. Girdilerle desteklenmeyen her kuralı `[VARSAYIM]` olarak etiketle ve açık kararları sorumlusuyla (genellikle hedefin veri sahibi) listele.
10. Kullanıcı devam etmek isterse taşıma ve SLA'lar için `integration-requirements`, doğrulama için `data-quality-rules` veya reddedilen kayıtlar için `error-scenario-catalog` öner.

## Çıktı formatı
```markdown
# Alan Eşleme: <kaynak sistem> → <hedef sistem> (<varlık / mesaj>)
Yön: <...> · İşlemler: <oluşturma / güncelleme / silme> · Eşleşme anahtarı: <kaynak anahtar ↔ hedef anahtar>

## Eşleme
| # | Hedef alan | Tür / uzunluk | Zorunlu | Kaynak alan(lar) | Dönüşüm / kural | Boş / hatalı değer | Kişisel veri |
|---|---|---|---|---|---|---|---|

## Kod Değeri Çevirileri
### <alan>
| Kaynak değer | Hedef değer | Not |
|---|---|---|

## Eşlenmeyen Alanlar
| Taraf | Alan | Gerekçe | Teyit eden |
|---|---|---|---|

## Varsayımlar ve Açık Kararlar
- [VARSAYIM] ... — sorumlu
```

## Kalite kontrol listesi
- [ ] Her zorunlu hedef alanın bir kaynağı, sabiti veya açık bir ret kuralı var.
- [ ] Her sayılı değer alanının "bilinmeyen değer" kuralı dahil eksiksiz çeviri tablosu var.
- [ ] Tarih, saat dilimi, ondalık ve para birimi formatları iki taraf için de belirtildi.
- [ ] Güncelleme davranışı "değeri temizle" ile "alan gönderilmedi"yi ayırıyor.
- [ ] İki taraftaki eşlenmeyen alanlar listelendi ve hedefin ihtiyaç duymadığı kişisel veri dışarıda bırakıldı.
- [ ] Hiçbir alan adı, kod veya kural uydurulmadı; boşluklar `[TBD]` ya da `[VARSAYIM]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Alan adı benzerliğine göre eşlemek. "Durum" veya "Tip" iki sistemde nadiren aynı anlama gelir; anlamı örnek kayıtlarla doğrula.
- Saat dilimlerini ve yerel formatları yok saymak. Dilimi olmayan bir tarih gece yarısı kayıtlarında bir gün kayar; ondalık virgül ayrıştırmayı bozar.
- Başarısız aramalarda sessiz varsayılan uygulamak. Bu, veri kalitesi sorunlarını gizler; bunun yerine reddet veya düzeltmeye yönlendir.

## Örnek
Girdi: "CRM müşteri: FullName, Phone, SegmentCode (A/B/C), CreatedAt (yerel saat). Faturalama API: firstName*, lastName*, phoneE164, segment (RETAIL/SME/CORPORATE)*, createdUtc."

Çıktıdan bir bölüm:
| # | Hedef | Zorunlu | Kaynak | Dönüşüm | Boş / hatalı | Kişisel |
|---|---|---|---|---|---|---|
| 1 | firstName | E | FullName | Son boşluktan böl; son parça hariç tümü `[VARSAYIM]` | Boşsa reddet | E |
| 3 | phoneE164 | H | Phone | Varsayılan ülke `[TBD]` ile E.164'e normalize et | Hatalıysa alansız gönder, logla | E |
| 4 | segment | E | SegmentCode | A→RETAIL, B→SME, C→CORPORATE | Bilinmeyen kod → reddet | H |

Açık karar: birden çok parçalı soyadları nasıl bölünecek; sorumlu Faturalama veri sahibi.
