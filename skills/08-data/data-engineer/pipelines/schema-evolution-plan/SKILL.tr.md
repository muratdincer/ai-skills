---
name: schema-evolution-plan
description: "Bir veri hattında, olay akışında veya paylaşılan veri setinde şema değişikliğini planlar: her değişikliği geriye, ileriye, tam uyumlu veya kırıcı olarak sınıflar, evrim desenini (eklemeli, expand-contract, sürümlü veri seti veya topic, çift yazma) seçer ve üretici, veri hattı ve tüketici değişikliklerini backfill, doğrulama ve kullanımdan kaldırmayla sıralar. Bir kaynak alan eklediğinde, yeniden adlandırdığında, tipini değiştirdiğinde veya kaldırdığında, bir veri sözleşmesi değişmesi gerektiğinde ya da tüketiciler üst akıştaki şema kaymasıyla sürekli kırıldığında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-engineer
  area: pipelines
  title: "Şema evrimi planlama"
  related: "data-contract, schema-migration-plan, incremental-load-design, source-to-target-mapping, data-lineage-doc"
  prompt: "CRM ekibi gelecek ay customer_type alanını segment olarak yeniden adlandırıp serbest metinden enum'a çevirecek. Veri hattımız ve 6 alt akış tüketicisi için şema evrimini planla."
---

# Şema Evrimi Planlama

## Amaç
Başkalarının bağımlı olduğu verinin şeklini, tüketicileri kırmadan, tarihçeyi kaybetmeden ve üreticileri dondurmadan değiştirmek. Plan her değişikliğin uyumluluğunu açık hale getirir ve geçişi her ara durumun geçerli olacağı şekilde sıralar.

## Ne zaman kullanılır
- Bir kaynak sistem veya üretici alan ekleyecek, yeniden adlandıracak, tipini değiştirecek, bölecek veya kaldıracaksa.
- Paylaşılan bir veri seti, olay şeması veya veri sözleşmesi yeni bir sürüme ihtiyaç duyuyorsa.
- Duyurulmamış şema kaymaları veri hatlarını sürekli kırıyorsa ve kontrollü bir süreç gerekiyorsa.

## Ne zaman kullanılmaz
- Değişiklik tek bir operasyonel veritabanı içindeki bir DDL geçişiyse `schema-migration-plan` kullanılır.
- Üretici ile tüketici arasındaki anlaşmanın kendisi (anlam, SLA, sahiplik) yazılacaksa `data-contract` kullanılır.
- Bir veri hattı şema kayması yüzünden zaten kırıldıysa ve önce teşhis gerekiyorsa `pipeline-failure-analysis` kullanılır.

## Girdiler
Zorunlu:
- Mevcut şema ve planlanan değişiklik (alan düzeyinde: ekleme, yeniden adlandırma, tip değişikliği, null olabilirlik, anlam, kaldırma).
- Verinin nasıl aktığı: depolama formatı veya taşıma (tablo, dosya formatı, schema registry'li veya registry'siz olay/topic).

İsteğe bağlı:
- Köken bilgisinden tüketici listesi, veri sözleşmesi, kullanılan uyumluluk modu, tarihsel verinin saklanması, üretici ve tüketicilerin yayın tarihleri.

Tüketiciler bilinmiyorsa bunu belirt ve tüketici keşfini ilk adım yap; hiç tüketici olmadığını varsayma.

## Süreç
1. Her değişikliği alan düzeyinde listele ve sınıfla: geriye uyumlu (yeni okuyucular eski veriyi okur), ileriye uyumlu (eski okuyucular yeni veriyi okur), tam uyumlu veya kırıcı. Anlamsal değişiklikleri (birim, anlam, izin verilen değerler) tip aynı kalsa bile kırıcı say.
2. Tüketicileri ve nasıl okuduklarını belirle: pozisyonla veya adla, katı veya toleranslı ayrıştırıcı, okurken veya yazarken şema, önbelleğe alınmış şemalar, BI çıkarımları, ML öznitelikleri. Her tüketicinin sorumlusunu ve yayın sıklığını kaydet.
3. Her değişiklik için evrim desenini seç: varsayılan değerle ekleme (güvenli), expand-contract (yeniyi ekle, ikisini birden doldur, tüketicileri taşı, eskiyi kaldır), sürümlü veri seti/topic/view (`v2` yan yana) veya yeni şekli eskiye eşleyen bir uyumluluk view'ı.
4. Hedef şemayı ve eşleme kurallarını tanımla: eski-yeni alan eşlemesi, tip dönüşümü ve değer eşlemesi (enum'lar için eksiksiz bir tablo ve eşlenmeyen değerlerin ele alınışı), tarihsel satırlar için varsayılanlar, null anlamı.
5. Tarihçenin nasıl ele alınacağına karar ver: tarihsel bölümleri yeniden yaz/backfill et, okuma anında birleştirmeyle karışık şemaları koru veya eski veriyi eski sürümde dondur. Depolama formatı kısıtlarını not et (sütun sırası, tip genişletme veya daraltma, bölüm sütunu değişiklikleri).
6. Geçişi her adım kendi başına geçerli olacak şekilde sırala: registry/uyumluluk ayarı, veri hattının iki şekli de kabul etmesi, üreticinin yeni şekli (çift yazmada eskisini de) üretmesi, backfill, tüketicilerin tek tek geçişi, eski alanların önce kullanımdan kaldırılması sonra silinmesi.
7. Her adımda doğrulamayı tanımla: CI'da veya registry'de şema uyumluluk kontrolü, yeni ve eski alanların satır sayıları ve null oranları, değer eşleme kapsamı, tüketici duman testleri.
8. Her adım için geri dönüşü ve geri dönüşü olmayan noktayı (genellikle eski alanın kaldırılması veya eski sürümün silinmesi) tanımla.
9. Kullanımdan kaldırma politikasını belirle: duyuru, süre, eski alan veya sürümlerde kullanım izleme ve kaldırma kriteri (yalnızca tarih değil, tanımlı bir süre boyunca sıfır okuma).
10. Riskleri, varsayımları ve açık soruları listele; üretici, veri hattı ve her tüketici adımı için sorumluları belirt.
11. Çıktı şablonunu doldur. Hedef devam ediyorsa yeni sürümü resmileştirmek için `data-contract`, eşlemeleri güncellemek için `source-to-target-mapping` veya kökeni yenilemek için `data-lineage-doc` öner.

## Çıktı formatı
```markdown
# Şema Evrimi Planı: <veri seti/akış> v<eski> → v<yeni>
Desen: <eklemeli / expand-contract / sürümlü / uyumluluk view'ı>

## Değişiklikler
| Alan | Değişiklik | Uyumluluk | Desen | Notlar |
|---|---|---|---|---|

## Tüketiciler
| Tüketici | Sorumlu | Nasıl okur | Etki | Geçiş adımı |
|---|---|---|---|---|

## Eşleme Kuralları
- <eski> → <yeni>: <dönüşüm, değer eşlemesi, varsayılan, eşlenmeyenler>

## Tarihsel Veri
<backfill / coalesce ile karışık / dondurulmuş> – <gerekçe>

## Geçiş Sırası
| Adım | Aksiyon | Sorumlu | Doğrulama | Geri dönüş |
|---|---|---|---|---|
Geri dönüşü olmayan nokta: <adım>

## Kullanımdan Kaldırma
Duyuru: <...> | Süre: <...> | Kaldırma kriteri: <...>

## Riskler, Varsayımlar, Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her alan değişikliği sınıflandırılmış; anlamsal değişiklikler kırıcı sayılmış.
- [ ] Her geçiş adımı üreticileri, veri hattını ve tüm tüketicileri çalışır durumda bırakıyor.
- [ ] Değer eşlemeleri eksiksiz; eşlenmeyen değerlerin nasıl ele alınacağı tanımlı.
- [ ] Tarihsel verinin nasıl ele alınacağı açık.
- [ ] Kaldırma ölçülmüş sıfır kullanıma bağlı; geri dönüşü olmayan nokta belirtilmiş.
- [ ] Tüketiciler ve formatlarla ilgili çıkarımlar işaretli; hiçbir şey uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bir alanı yerinde yeniden adlandırmak: her okuyucu için bu bir kaldırma artı bir eklemedir ve hepsini aynı anda kırar. Expand-contract kullan.
- Yalnızca sözdizimsel uyumluluğu kontrol etmek; registry, birimi kuruştan avroya değişen bir alanı kabul eder.
- Köken grafiğinin dışındaki tüketicileri (tablolar, geçici dışa aktarımlar, önbellekteki BI çıkarımları) unutmak; kaldırmadan önce okumaları izle.

## Örnek
Girdi: "CRM gelecek ay customer_type'ı (serbest metin) segment (enum: RETAIL, SME, CORPORATE) olarak yeniden adlandırıyor; 6 tüketici var."

Çıktıdan bir bölüm:
- Değişiklik: yeniden adlandırma + tip değişikliği + anlamsal kısıt → kırıcı; desen expand-contract.
- Eşleme: 'retail', 'Retail ', 'bireysel' → RETAIL; eşlenmeyen değerler → UNKNOWN ve günlük sayılır `[VARSAYIM: CRM tam değer listesini doğrular]`.
- Geçiş: (1) veri hattı `segment` ekler, tarihçe için `customer_type`'tan türetir; (2) CRM iki alanı birden üretir; (3) tüketiciler geçer; (4) `customer_type`, 30 gün sıfır okumadan sonra kaldırılır.
