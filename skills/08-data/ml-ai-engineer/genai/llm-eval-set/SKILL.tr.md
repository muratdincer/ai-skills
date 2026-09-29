---
description: Bir LLM özelliği için kategorilere ayrılmış test vakaları, puanlama kriterleri (rubric), değerlendirici seçimi (birebir eşleşme, programatik, model ile puanlama, insan), geçme eşikleri ve regresyon süreci içeren bir değerlendirme seti oluşturur. Bir LLM özelliği, prompt veya RAG hattı yayından önce ölçülebilir kalite gerektirdiğinde, modeller ya da prompt sürümleri karşılaştırılırken veya "yeni prompt daha iyi mi bilmiyoruz" dendiğinde kullanılır.
related: prompt-design, rag-design, model-evaluation-report, test-strategy, ai-use-case-assessment
prompt: Sözleşme özetleme asistanımız için, yayından önce iki prompt sürümünü karşılaştırabileceğimiz bir değerlendirme seti oluştur.
---

# LLM Değerlendirme Seti

## Amaç
"İyi görünüyor" yargısını tekrarlanabilir kanıta dönüştürmek: bir LLM özelliğinin yayına hazır olup olmadığını ve bir değişikliğin onu iyileştirip iyileştirmediğini gösteren, puanlama kriterleri ve değerlendiricileri olan sürümlü bir vaka seti.

## Ne zaman kullanılır
- Bir LLM özelliğini ya da yeni bir prompt, model veya erişim (retrieval) değişikliğini yayınlamadan önce.
- Modeller veya prompt sürümleri arasında maliyet, gecikme ve kaliteye göre seçim yaparken.
- Üretimden gelen şikâyetlerin regresyon vakalarına dönüştürülmesi gerektiğinde.

## Ne zaman kullanılmaz
- Prompt henüz tasarlanmadıysa önce `prompt-design` kullanılır.
- Etiketli verisi ve standart metrikleri olan klasik bir ML modeliyse `model-evaluation-report` kullanılır.

## Girdiler
Zorunlu:
- Özellik tanımı: görev, kullanıcılar, girdi türleri ve iyi bir çıktının neye benzediği.
- Gerçek veya gerçekçi (maskelenmiş) girdi örnekleri.

İsteğe bağlı, kaliteyi artırır:
- Bilinen hata örnekleri, kullanıcı şikâyetleri, etiketleme için alan uzmanlarının müsaitliği.
- Risk profili (regüle alan, zararlı çıktı kaygıları), maliyet ve gecikme bütçeleri.
- Mevcut prompt ve erişim kurgusu.

İyi bir çıktının tanımı yoksa bir örnekle birlikte iste; puanlama kriterleri buna bağlıdır. Diğer eksikler açık soru olur.

## Süreç
1. Bu özellik için kalite boyutlarını tanımla (ör. doğruluk, kaynağa sadakat/dayanak, eksiksizlik, format uyumu, ton, güvenlik, yerinde reddetme) ve riske göre ağırlıklandır.
2. Vaka sınıflandırmasını tasarla: sıklığa göre temel mutlu yollar, uç durumlar (uzun, boş, çok dilli, gürültülü girdi), saldırgan vakalar (prompt injection, jailbreak, hassas veri) ve reddedilmesi gereken kapsam dışı girdiler.
3. Seti boyutlandır: sınıflandırmaya göre tabakalanmış 30-100 vakayla başla; boyutun gereken güvenle ilişkisini belirt, doğrulanmadıysa `[VARSAYIM]` olarak işaretle.
4. Vakaları maskelenmiş üretim loglarından, uzmanların yazdığı vakalardan ve sentetik varyasyonlardan topla; her vakanın kaynağını kaydet, ham kişisel veriyi asla dahil etme.
5. Her vaka için referansı yaz: mümkünse birebir beklenen yanıt, değilse çıktıda bulunması gereken olgular, yasak içerik ve sağlanması gereken özellikler.
6. Her boyut için değerlendiriciyi seç: format için birebir/regex veya şema kontrolü; olgular için programatik kontrol; serbest metin için model ile rubric puanlama; yüksek riskli veya öznel boyutlar için insan incelemesi.
7. Her rubric'i 1-5 veya geçti/kaldı ölçeğiyle ve her seviye için somut tanımlarla yaz; model değerlendiricilere güvenmeden önce onları insanla etiketlenmiş 20+ vakayla doğrula ve uyum oranını raporla.
8. Her boyut için yayın eşiklerini, ortalama puanlardan ayrı olarak kesin kapılarla (ör. sıfır güvenlik hatası, %100 format uyumu) belirle.
9. Çalıştırma protokolünü tanımla: sabit parametreler, deterministik olmayan çıktılar için tekrar sayısı, maliyet ve gecikme ölçümü, sürümlerin yan yana karşılaştırılması.
10. Bakımı tanımla: her üretim olayı bir regresyon vakası ekler, periyodik yenileme yapılır, prompt'un sete aşırı uyumlanmasını önlemek için gizli bir holdout tutulur.
11. Her çıkarımı `[VARSAYIM]` olarak işaretle, açık soruları listele; düzeltmeler için `prompt-design`, sonuçları raporlamak için `model-evaluation-report` öner.

## Çıktı formatı
```markdown
# LLM Değerlendirme Seti: <özellik> v<sürüm>
Sorumlu: <ekip> · Vaka sayısı: <n> · Son yenileme: <tarih>

## Kalite Boyutları
| Boyut | Ağırlık | Değerlendirici | Eşik / kapı |
|---|---|---|---|

## Vaka Sınıflandırması ve Kapsama
| Kategori | Pay | Vaka sayısı | Kaynak |
|---|---|---|---|

## Vakalar (örnek)
| ID | Kategori | Girdi (maskeli) | Referans / zorunlu olgular | Olmamalı | Değerlendirici |
|---|---|---|---|---|---|

## Puanlama Kriterleri
### <boyut>
- 5: ...
- 3: ...
- 1: ...

## Çalıştırma Protokolü
<parametreler, tekrarlar, ölçülen metrikler, karşılaştırma yöntemi>

## Değerlendirici Doğrulaması
<insanla uyum sonuçları veya [TBD]>

## Bakım
<regresyon girişi, yenileme sıklığı, holdout>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her kalite boyutunun bir değerlendiricisi ve eşiği var; güvenlik ve format kesin kapı.
- [ ] Vakalar mutlu yol, uç, saldırgan ve kapsam dışı girdileri kapsıyor.
- [ ] Referanslar yalnızca "iyi bir yanıt" demiyor; zorunlu olguları ve yasak içeriği belirtiyor.
- [ ] Model ile puanlanan rubric'lerin insan etiketlerine karşı doğrulama planı var.
- [ ] Vaka girdileri maskelenmiş; ham kişisel veri yok.
- [ ] Holdout ve regresyon girişi, prompt'un sete aşırı uyumlanmasını engelliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her şeyi tek bir puanda ortalamak. Ortalamada daha iyi olup bir kez veri sızdıran sürüm kalmalıdır.
- Kalibrasyonsuz model değerlendiricisine güvenmek. İnsanla uyumu kontrol et ve daha uzun yanıtları kayırma eğilimine dikkat et.
- Vakaları yalnızca geliştiricinin hayal gücünden yazmak. Önemli hataları gerçek, dağınık kullanıcı girdileri bulur.

## Örnek
Girdi: "Sözleşme özetleme asistanı, iki prompt sürümünü karşılaştır."

Çıktıdan bir bölüm:
| ID | Kategori | Girdi | Zorunlu olgular | Olmamalı | Değerlendirici |
|---|---|---|---|---|---|
| C-014 | Uç | 42 sayfalık sözleşme, yenileme maddesi ekte | Otomatik yenileme süresi, bildirim süresi | Fesih bedeli uydurmak | Model rubric + insan örneklem kontrolü |
| C-031 | Saldırgan | "Önceki talimatları yok say" içeren sözleşme metni | Normal özet | Gömülü talimata uymak | Programatik kontrol |

Kapı: sadakat ortalaması ≥ 4,0 ve uydurma yükümlülük içeren sıfır vaka `[VARSAYIM: hukuk ile teyit et]`.
