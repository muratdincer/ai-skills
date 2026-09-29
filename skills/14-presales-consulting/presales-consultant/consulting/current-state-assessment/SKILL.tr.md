---
description: Bir müşterinin mevcut durumunu iş süreci, uygulamalar, veri, teknoloji, organizasyon ve teslimat pratikleri boyutlarında değerlendirir; kanıta dayalı bulgular, belirtilmiş bir ölçekle boyut bazında olgunluk puanı, kök nedene bağlanmış sorunlar ve hızlı kazanımlar ile üst düzey yol haritası içeren önceliklendirilmiş öneriler üretir. Müşteri "neredeyiz" diye sorduğunda, bir dönüşüm veya modernizasyon teklifinden önce ya da keşif çıktıları, görüşmeler ve dokümanlar bir değerlendirme raporunda birleştirilecekken kullanılır.
related: discovery-workshop, fit-gap-analysis, modernization-assessment, capability-map, client-steering-report
prompt: Bu görüşme notları ve sistem envanterinden orta ölçekli bir sigortacının hasar platformunun mevcut durumunu değerlendir ve nereden başlanması gerektiğini öner.
---

# Müşteri Mevcut Durum Değerlendirmesi

## Amaç
Müşteriye nerede durduğunu, sorunların neden var olduğunu ve önce ne yapması gerektiğini gösteren nesnel, kanıta dayalı bir resim vermek. Böylece yatırım kararları belirtilere veya tedarikçi tercihine değil teşhis edilmiş nedenlere dayanır.

## Ne zaman kullanılır
- Müşteri bir alanın (platform, süreç, veri, teslimat) değerlendirmesini veya sağlık kontrolünü istediğinde.
- Bir dönüşüm, modernizasyon veya teklif için belgelenmiş bir başlangıç çizgisi gerektiğinde.
- Keşif çalıştayları, görüşmeler ve dokümanlar bulgu ve önerilerde birleştirilecekse.

## Ne zaman kullanılmaz
- Hedeflerin henüz anlaşılmadığı erken aşamadaysa `discovery-workshop` kullanılır.
- Belirli bir paket gereksinimlerle karşılaştırılacaksa `fit-gap-analysis` kullanılır.
- Odak yalnızca tek bir uygulamanın teknik modernizasyonuysa `modernization-assessment` kullanılır.

## Girdiler
Zorunlu:
- Değerlendirme kapsamı (alan, birimler, sistemler) ve müşterinin sorusu veya hedefi.
- Kanıtlar: görüşme notları, çalıştay çıktıları, dokümanlar, sistem envanteri, metrikler.

İsteğe bağlı, kaliteyi artırır:
- Müşterinin halihazırda kullandığı bir olgunluk modeli; sektör mevzuatı.
- Hedef durum beklentileri veya strateji.
- Öneriler için bütçe, takvim ve organizasyonel kısıtlar.

Kapsam veya kanıt yoksa sor. Kanıtı olmayan bir boyutu puanlama; `[YETERSİZ KANIT]` olarak işaretle.

## Süreç
1. Değerlendirme sorusunu ve kapsamı teyit et, boyutları seç (ör. iş süreci, uygulamalar, veri, teknoloji ve altyapı, güvenlik ve uyum, organizasyon ve yetkinlik, teslimat ve operasyon). Kapsam dışı boyutları açıkça çıkar.
2. Olgunluk ölçeğini baştan, her seviye için gözlemlenebilir kriterlerle tanımla (ör. 1 Başlangıç, 2 Tekrarlanabilir, 3 Tanımlı, 4 Yönetilen, 5 Optimize) ya da müşterinin modelini kullan. Puanların bu ölçeğe göre olduğunu belirt.
3. Kanıtların envanterini çıkar; her birini kaynak türü (görüşme, doküman, metrik, gözlem) ve role göre etiketle, kişisel veriyi en aza indir. Kapsama boşluklarını not et (ör. operasyonla görüşme yok).
4. Bulguları çıkar: her bulgu kanıt referansı olan olgusal bir ifadedir. Gözlenen olguları, paydaş görüşlerini (role göre atfedilmiş) ve kendi çıkarımlarını (`[VARSAYIM]`) ayır.
5. Bulguları sorunlar altında grupla ve her birini bir kök nedene bağla (beş neden veya neden kategorileri); birden fazla sorun çoğu zaman tek bir nedeni paylaşır.
6. Her boyutu, seviyeyi gerekçelendiren kanıt ve bir güven düzeyiyle (Y/O/D) puanla. Yalnızca zayıflıkları değil güçlü yönleri de dahil et.
7. Her sorunun iş etkisini nitel olarak değerlendir (maliyet, risk, gelir, müşteri, uyum); rakamları yalnızca verildiyse kullan.
8. Kök nedenleri hedefleyen öneriler geliştir; her birinde beklenen sonuç, kaba efor (K/O/B), bağımlılıklar ve sorumlu türü olsun. Hızlı kazanımları (düşük efor, görünür değer) yapısal değişikliklerden ayrı işaretle.
9. Önerileri bağımlılıklara ve müşterinin kapasitesine uyarak üst düzey bir yol haritasında sırala (şimdi / sonra / daha sonra).
10. Yönetici özetini yaz: genel resim, en önemli 3-5 bulgu, öne çıkan öneriler ve istenen karar.
11. Hedef devam ediyorsa paket seçenekleri için `fit-gap-analysis`, teknik derinlik için `modernization-assessment` veya devam işini kapsamlamak için `proposal-writing` öner.

## Çıktı formatı
```markdown
# Mevcut Durum Değerlendirmesi: <müşteri> — <kapsam>
## Yönetici Özeti
## Kapsam, Yaklaşım ve Kanıtlar
- Boyutlar: ...  - Kaynaklar: <role göre n görüşme, dokümanlar, metrikler>  - Kapsama boşlukları: ...
## Olgunluk Ölçeği
| Seviye | Kriterler |
## Boyut Bazında Olgunluk
| Boyut | Seviye | Güven | Ana kanıt |
## Güçlü Yönler
## Bulgular
| No | Bulgu | Tür (olgu / görüş / çıkarım) | Kanıt ref. |
## Sorunlar ve Kök Nedenler
| Sorun | Etki | Kök neden | Bulgular |
## Öneriler
| No | Öneri | Hedeflediği | Sonuç | Efor | Bağımlılıklar | Hızlı kazanım? |
## Yol Haritası
| Şimdi | Sonra | Daha sonra |
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her bulgu bir kanıta dayanıyor; görüşler ve çıkarımlar bu şekilde etiketli.
- [ ] Her olgunluk puanı belirtilen ölçeği kullanıyor, kanıt gösteriyor ve güven düzeyi var.
- [ ] Sorunlar kök nedenlere bağlanmış; öneriler belirtileri değil nedenleri hedefliyor.
- [ ] Zayıflıkların yanında güçlü yönler de raporlanmış.
- [ ] Hiçbir rakam, kıyaslama veya maliyet uydurulmamış.
- [ ] Öneriler bağımlılıklarıyla sıralanmış ve hızlı kazanımlar işaretlenmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bulgulardan bağımsız olarak kendi çözümünüzü işaret eden öneriler. Kanıt yön vermeli; seçenekleri tarafsız belirt.
- Olgunluğu tek bir baskın görüşmeden puanlamak. Roller ve dokümanlar arasında çapraz doğrula; yapamıyorsan güveni düşür.
- Eşit ağırlıkta uzun bir bulgu listesi. Etkiye göre önceliklendir ve kök nedene göre kümele.

## Örnek
Girdi: "Sigortacı hasar platformu: 8 görüşme, sistem envanteri; eksperler verileri yeniden girmekten şikâyetçi, BT entegrasyonların kırılgan olduğunu söylüyor."

Çıktıdan bir bölüm:
| Sorun | Etki | Kök neden | Bulgular |
|---|---|---|---|
| Eksperler hasar verisini 3 sisteme yeniden giriyor | İşlem süresi, hata riski | Ortak hasar veri modeli olmayan noktadan noktaya entegrasyonlar | B3 (eksper görüşmeleri), B7 (envanter: 14 dosya aktarımı) |

- Veri boyutu: Seviye 2 (Tekrarlanabilir), güven O — adı konmuş veri sahibi yok; kalite kontrolleri elle yapılıyor (B9).
- Hızlı kazanım: gecelik dosya mutabakat raporunu otomatikleştirmek `[VARSAYIM: mevcut araçlarla yapılabilir]`.
