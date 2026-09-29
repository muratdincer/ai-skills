---
description: "Şartname, kullanım kılavuzu, prosedür, sözleşme, mevzuat, form ve rapor gibi mevcut dokümanlardan gereksinim çıkarır; kaynağa izlenebilen aday gereksinimler, iş kuralları, veri öğeleri ve çelişkiler listesi üretir. Eski sistem dokümanları, bir mevzuat veya sözleşme görüşmelerden önce taranacaksa ya da 'bu dokümanlardan hangi gereksinimleri çıkarabiliriz?' diye sorulduğunda kullanılır."
related: "business-rules-catalog, interview-question-set, requirements-consistency-check, traceability-matrix, glossary-builder"
prompt: "Mevcut hasar sistemimizin 20 sayfalık operasyon kılavuzundan ve yeni yönetmelik metninden gereksinimleri çıkar, nerede çeliştiklerini göster."
---

# Mevcut Dokümanlardan Gereksinim Çıkarma

## Amaç
Mevcut dokümanları izlenebilir aday gereksinimlere, kurallara ve sorulara dönüştürmek. Böylece görüşmeler kanıttan başlar, paydaşların zamanı da dokümanların cevaplayamadığı konulara harcanır.

## Ne zaman kullanılır
- Eski bir sistem değiştiriliyor ve ana bilgi kaynağı onun kılavuzları, şartnameleri veya prosedürleriyse.
- Bir mevzuat, standart veya sözleşme gereksinime dönüşmesi gereken yükümlülükler getiriyorsa.
- Görüşme veya çalıştaylardan önce hipotez hazırlamak ve zaten yazılı olanı sormamak için.

## Ne zaman kullanılmaz
- Girdi görüşme veya toplantı notlarıysa `interview-notes-analysis` kullanılır.
- Girdi eksikleri kontrol edilecek hazır bir gereksinim setiyse `requirements-gap-analysis` kullanılır.
- Yalnızca iş kurallarının standartlaştırılması gerekiyorsa `business-rules-catalog` kullanılır.

## Girdiler
Zorunlu:
- Doküman metni veya alıntılar; adı ve biliniyorsa sürümü ve tarihi.
- Analizin hizmet ettiği kapsam veya soru (ör. "yeni sistem için hasar kaydı").

İsteğe bağlı, kaliteyi artırır:
- Doküman sahibi ve durumu (güncel, taslak, yürürlükten kalkmış).
- Sözlük veya bilinen alan terimleri.
- Mükerrerliği önlemek için zaten bilinenlerin listesi.

Doküman metni yoksa iste. Kapsam yoksa bunun için tek bir soru sor; aksi halde her cümle aday gereksinime dönüşür.

## Süreç
1. Kaynakların envanterini çıkar: başlık, tür (mevzuat, sözleşme, kılavuz, prosedür, şartname, form, rapor), sürüm, tarih, sahip, bağlayıcılık düzeyi (bağlayıcı / tanımlayıcı / gayriresmi). Eskimiş veya yerine yenisi gelmiş kaynakları işaretle.
2. Örneklerde, formlarda veya ekran görüntülerinde bulunan kişisel verileri maskele; yalnızca alan adlarını ve formatları tut.
3. Kapsama göre oku ve yükümlülük, yetenek, kural, kısıt, veri öğesi, hesaplama, istisna veya kalite beklentisi ifade eden cümleleri çıkar. Tam yerini (bölüm, sayfa, madde) kaydet.
4. Her çıkarımı sınıflandır: Yükümlülük (yasal/sözleşmesel), Fonksiyonel, İş kuralı, Veri, NFR, Arayüz, Rapor, Süreç adımı, Terim.
5. Dokümanın söylediğini, mevcut sistemin bunu nasıl yaptığından ayır. Kılavuzdaki bir ekran düzeni bugünkü çözümü anlatır, gereksinim değildir; `Mevcut davranış` olarak işaretle.
6. Her maddeyi kaynaktaki bağlayıcılık gücünü koruyarak (zorunlu vs. önerilir vs. olabilir) tarafsız bir aday gereksinim olarak yeniden yaz. Metnin ötesine geçen her yorumu `[VARSAYIM]` olarak etiketle.
7. Kaynaklar arası çelişkileri ve örtüşmeleri (ör. kılavuz 30 gün, yönetmelik 15 gün diyor) ve dokümanın bariz bir durum hakkında sessiz kaldığı boşlukları bul.
8. Alan terimlerini ve veri öğelerini kaynaktaki tanımıyla küçük bir sözlüğe çıkar.
9. Her madde için güven düzeyi ver: Yüksek (bağlayıcı, güncel kaynak), Orta (tanımlayıcı, güncel), Düşük (eski, gayriresmi veya tek geçen). Düşük maddeler teyit ister.
10. Paydaşlara yalnızca çelişkiler, boşluklar ve düşük güvenli maddeler için, muhtemel muhatabıyla birlikte soru üret.
11. Hedef devam ediyorsa kurallar için `business-rules-catalog`, açık noktaları teyit için `interview-question-set`, kaynak bağlantılarını korumak için `traceability-matrix` öner.

## Çıktı formatı
```markdown
# Doküman Analizi: <kapsam>

## Kaynaklar
| ID | Doküman | Tür | Sürüm / tarih | Bağlayıcılık | Durum |
|---|---|---|---|---|---|
| K1 | ... | Mevzuat | ... | Bağlayıcı | Güncel |

## Aday Gereksinimler
| ID | İfade (tarafsız) | Kategori | Kaynak (doküman, bölüm) | Güç | Güven | Not |
|---|---|---|---|---|---|---|
| DG-01 | ... | Yükümlülük | K1 §4.2 | Zorunlu | Yüksek | |

## Mevcut Davranış (gereksinim değil)
- ...

## Çelişkiler ve Boşluklar
| # | Konu | Kaynak A | Kaynak B / sessizlik | Etki | Soru | Sahibi |

## Sözlük Çıkarımı
- <terim>: <tanım> (K#)

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Her madde bir kaynak ve yer gösteriyor; izlenemeyen madde yok.
- [ ] Mevcut uygulama ayrıntıları gereksinimlerden ayrı tutuldu.
- [ ] Bağlayıcılık gücü kaynakla uyumlu; "önerilir" "zorunlu"ya yükseltilmedi.
- [ ] Kaynaklar arası çelişkiler sessizce çözülmedi, gösterildi.
- [ ] Yürürlükten kalkmış veya tarihsiz kaynaklar işaretlendi, maddeleri Düşük güvenle derecelendirildi.
- [ ] Örneklerdeki kişisel veriler maskelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Eski sistemi yenisine kopyalamak. Her mevcut davranış maddesi için ihtiyacın hâlâ geçerli olup olmadığını sor.
- Bir mevzuat özetini mevzuatın kendisi sanmak. Bağlayıcı metne atıf yap, ikincil kaynakları işaretle.
- Her şeyi çıkarmak. Kapsama göre filtrele; yoksa liste gözden geçirilemez hale gelir.

## Örnek
Girdi: Hasar kılavuzu v3 (2019) §5: "Memur hasarı 30 gün içinde girer ve K-12 formunu yazdırır." Yönetmelik §4.2: "Hasarlar ihbardan itibaren 15 gün içinde kayda alınır."

Çıktıdan bir bölüm:
| ID | İfade | Kategori | Kaynak | Güç | Güven |
|---|---|---|---|---|---|
| DG-01 | Hasar, ihbardan itibaren 15 gün içinde kayda alınmalıdır. | Yükümlülük | K2 §4.2 | Zorunlu | Yüksek |
| DG-02 | K-12 formunun yazdırılması | Mevcut davranış | K1 §5 | – | Düşük |

Çelişki: K1 30 gün, K2 15 gün diyor. Yönetmelik bağlayıcıdır; kılavuzun güncelliğini Uyum birimiyle teyit et.
