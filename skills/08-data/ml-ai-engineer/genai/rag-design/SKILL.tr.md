---
description: Doküman kümesi ve erişim kontrolü, veri alımı, parçalama, embedding, hibrit erişim, yeniden sıralama, kaynak gösteren dayanaklı yanıt üretimi, değerlendirme ve operasyonu kapsayan bir erişimle zenginleştirilmiş üretim (RAG) sistemi tasarlar. Bir LLM'in kurum dokümanlarından veya verisinden yanıt vermesi gerektiğinde, mevcut RAG yanlış ya da kaynaksız yanıtlar verdiğinde veya RAG, fine-tuning ve düz prompt arasında seçim yapılırken kullanılır.
related: prompt-design, llm-eval-set, ai-use-case-assessment, data-classification, solution-architecture-document
prompt: 3.000 İK politika PDF'i ve intranet sayfasından çalışan sorularını yanıtlayan, ülkeye özel erişim kurallarına uyan bir RAG asistanı tasarla.
---

# RAG Sistemi Tasarlama

## Amaç
Yanıtların doğru ve erişim izni olan kaynaklara dayandığı, erişim kalitesinin ölçülebildiği ve her tasarım tercihinin (parçalama, erişim, yeniden sıralama, prompt) varsayılanlarla değil doküman kümesi ve sorularla gerekçelendirildiği bir tasarım üretmek.

## Ne zaman kullanılır
- Bir asistan, arama veya destek özelliğinin kurum içi bilgiden yanıt vermesi gerektiğinde.
- Mevcut bir RAG uydurma yanıt verdiğinde, bariz dokümanları kaçırdığında veya yanlış kaynak gösterdiğinde.
- Ekibin probleme RAG, fine-tuning veya uzun bağlamlı prompt'tan hangisinin uyduğuna karar vermesi gerektiğinde.

## Ne zaman kullanılmaz
- Görev dış bilgi gerektirmiyor, sorun talimat kalitesindeyse `prompt-design` kullanılır.
- İş gerekçesi ve riskler henüz değerlendirilmediyse `ai-use-case-assessment` kullanılır.

## Girdiler
Zorunlu:
- Doküman kümesinin tanımı: doküman türleri, formatlar, hacim, diller, güncellenme sıklığı.
- Tipik kullanıcı soruları (mümkünse 10+ gerçek örnek) ve kullanıcıların kim olduğu.

İsteğe bağlı, kaliteyi artırır:
- Erişim kuralları ve veri sınıflandırması, gecikme ve maliyet hedefleri, mevcut arama veya vektör altyapısı.
- Mevcut sistemden bilinen hata örnekleri.

Örnek sorular yoksa iste; erişim tasarımı bunlara bağlıdır. Diğer eksikler açık soru olur.

## Süreç
1. Soruları sınıflandır: olgu arama, prosedürel, karşılaştırma, dokümanlar arası toplama veya tablolar üzerinde akıl yürütme gerektiren; RAG'in yanıtlayamayacaklarını not et (ör. tüm kayıtlar üzerindeki sayımlar bir sorgu aracı gerektirir).
2. Doküman kümesinin sınırını ve erişim modelini tanımla: kaynaklar, sahipler, sınıflandırma ve yetkilerin erişim anında nasıl uygulandığı (doküman düzeyinde ACL filtresi; yalnızca üretim sonrası karartma asla yeterli değil).
3. Veri alımını tasarla: formata göre ayrıştırma (tablolar, taranmış PDF'ler, başlıklar), temizleme, tekilleştirme, metadata (kaynak, bölüm, tarih, dil, erişim etiketleri) ve silme işlemlerini de kapsayan artımlı yenileme.
4. Parçalamayı doküman yapısına göre seç: yanıt birimine göre boyutlandırılmış, bölüm veya başlık farkındalıklı parçalar; bağlam önemliyse örtüşme ve üst doküman (parent-document) ya da küçükten büyüğe (small-to-big) erişim; boyutu soru türlerine göre gerekçelendir.
5. Embedding modelini belirtilen kriterlere göre seç: kapsanan diller, alan terminolojisi, boyut ve maliyet; itibara göre seçmek yerine örnek sorular üzerinde çevrimdışı karşılaştırma planla.
6. Erişimi tasarla: hibrit sözcüksel (BM25) artı vektör arama, metadata filtreleri, top-k ve çok parçalı sorular için sorgu yeniden yazma veya ayrıştırma.
7. İlk birkaç sonuçta kesinlik önemliyse yeniden sıralama (cross-encoder veya model tabanlı) ekle; gecikme maliyetini belirt.
8. Yanıt üretimini tasarla: dayanak talimatları, iddia başına kaynak gösterme formatı, "kaynaklarda bulunamadı" davranışı, kaynaklar arası çelişkide kural (en yeni veya yetkili kaynak) ve bağlam penceresi bütçesi.
9. Değerlendirmeyi tanımla: erişim metriklerini (etiketli soru-pasaj seti üzerinde recall@k, MRR) yanıt metriklerinden (sadakat, yanıt ilgililiği, kaynak doğruluğu) ayrı tut; bir değerlendirme setine bağla.
10. Operasyon ve güvenliği planla: güncellik SLA'i, indeks yeniden oluşturma, yanıtsız ve düşük benzerlik oranlarının izlenmesi, geri bildirim toplama, dokümanlardan gelen prompt injection, loglardaki kişisel verinin maskelenmesi.
11. Temel kararları alternatifleriyle kaydet ve test edilmemiş tercihleri `[VARSAYIM]` olarak işaretle.
12. Açık soruları listele; değerlendirme setini kurmak için `llm-eval-set`, yanıt üretim prompt'u için `prompt-design` öner.

## Çıktı formatı
```markdown
# RAG Tasarımı: <sistem adı>
Kullanıcılar: <kim> · Doküman kümesi: <türler, hacim, diller> · Güncellik: <SLA>

## Soru Türleri
| Tür | Pay | Örnek | RAG'e uygun mu? |
|---|---|---|---|

## Mimari
<alım → indeks → erişim → yeniden sıralama → üretim → geri bildirim; diyagram isteğe bağlı>

## Tasarım Kararları
| Alan | Tercih | Gerekçe | Alternatif | Durum |
|---|---|---|---|---|
| Parçalama | ... | ... | ... | Test edilene kadar [VARSAYIM] |
| Embedding | ... | ... | ... | ... |
| Erişim | ... | ... | ... | ... |
| Yeniden sıralama | ... | ... | ... | ... |

## Erişim Kontrolü ve Gizlilik
<ACL uygulama noktası, sınıflandırma, log maskeleme>

## Yanıt Üretim Sözleşmesi
<dayanak kuralları, kaynak formatı, yanıtsız davranış, çelişki kuralı>

## Değerlendirme
- Erişim: <metrikler, etiketli set>
- Yanıt: <metrikler, değerlendirme seti bağlantısı>

## Operasyon
<yenileme, izleme sinyalleri, geri bildirim döngüsü>

## Riskler ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Erişim kontrolü, içerik modele ulaşmadan önce erişim aşamasında uygulanıyor.
- [ ] Parçalama ve erişim tercihleri soru türleri ve doküman yapısıyla gerekçelendirildi.
- [ ] Erişim kalitesi ve yanıt kalitesi ayrı ayrı değerlendiriliyor.
- [ ] Tanımlı bir "kaynaklarda bulunamadı" davranışı ve kaynak gösterme formatı var.
- [ ] RAG'in yanıtlayamayacağı soru türleri bir alternatifle birlikte belirlendi.
- [ ] Güncellik, silme ve dokümanlardan gelen injection ele alındı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sorun erişimdeyken prompt'u ayarlamak. Üretime dokunmadan önce doğru pasajın top-k içinde olup olmadığını kontrol et.
- Tabloları ve prosedürleri bölen sabit boyutlu parçalar. Dokümanın kendi yapısını kullan.
- Eskimiş veya silinmiş dokümanları küçük bir sorun saymak. Güncel olmayan politika yanıtları çoğu zaman hiç yanıt olmamasından kötüdür.

## Örnek
Girdi: "3.000 politika PDF'i ve intranet sayfası üzerinde İK asistanı, ülkeye özel erişim."

Çıktıdan bir bölüm:
- Erişim: Her parça `country` ve `employee_group` etiketleri taşır; erişim, aramadan önce kullanıcının yetki bilgilerine göre filtreler.
- Parçalama: Başlık farkındalıklı bölümler, tablolar bölünmeden tutulur; bağlam için üst bölüm döndürülür `[VARSAYIM: 50 etiketli soruyla doğrulanacak]`.
- RAG kapsamı dışında: "Kaç gün iznim kaldı?" doküman erişimiyle değil, İK sistemine bir çağrıyla yanıtlanmalı.
