---
name: problem-management
description: "Tekrarlayan veya büyük olaylar için problem yönetimi yürütür: ilişkili olayları gruplar, problemi tanımlar, kanıta dayalı kök neden analizini yönetir, geçici çözümüyle birlikte bilinen hata kaydı oluşturur ve doğrulama kriterleriyle kalıcı çözümleri değişiklik kontrolü üzerinden önerir. Aynı olay türü tekrarladığında, büyük bir olaydan sonra, olay eğilimleri altta yatan bir nedene işaret ettiğinde veya bir problem kaydı açılacağında, ilerletileceğinde ya da kapatılacağında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 11-support-ops
  role: it-service-management
  area: itsm
  title: "Problem yönetimi"
  related: "known-error-article, five-whys, fishbone-analysis, change-request-rfc, postmortem"
  prompt: "Problem kaydı aç: 3 haftada gece batch'inin uzayıp sabah raporlarının geciktiği 7 olay yaşadık; her birinde job yeniden başlatılarak çözüldü."
---

# Problem Yönetimi

## Amaç
Hizmeti tekrar tekrar ayağa kaldırmak yerine olayların altta yatan nedenini bulup ortadan kaldırmak. Böylece olay sayısı, kesinti süresi ve destek eforu ölçülebilir biçimde düşer.

## Ne zaman kullanılır
- Birden çok olay ortak bir belirti, bileşen veya zaman örüntüsü paylaştığında.
- Büyük bir olay geçici çözümle kapatıldığında ve kök neden hâlâ açık olduğunda.
- Eğilim analizi (kategori, CI, değişiklik, zaman bazında) incelenmeye değer bir sıcak nokta gösterdiğinde.

## Ne zaman kullanılmaz
- Hizmet şu anda kesik ve geri getirilmesi gerekiyorsa `incident-response` kullanılır.
- Tek bir olayın suçlamasız yazılı analizi isteniyorsa `postmortem` kullanılır.
- Yalnızca doğrulanmış bir neden için bilgi bankası makalesi gerekiyorsa `known-error-article` kullanılır.

## Girdiler
Zorunlu:
- Olaylar (kayıt numaraları, belirtiler, zamanlar, çözümler) veya problemi tetikleyen örüntü.

İsteğe bağlı, kaliteyi artırır:
- İlgili konfigürasyon öğeleri, son değişiklikler, izleme verileri, loglar, tedarikçi bilgileri.
- Olay başına iş etkisi (kesinti süresi, kullanıcı, biliniyorsa maliyet).
- Kurumun problem kaydı şablonu, öncelik şeması ve tercih ettiği kök neden analizi yöntemi.

Olay verisi yoksa en azından tarih ve çözümleriyle olay listesini iste. Maliyet veya kesinti süresini asla tahmin etme; eksik değerleri `[BİLİNMİYOR]` olarak işaretle. Olay alıntılarındaki kişisel verileri maskele.

## Süreç
1. Olayları grupla: kayıt numaraları, ilk/son görülme, sıklık, etkilenen konfigürasyon öğeleri, uygulanan çözüm; ortak bir belirti paylaştıklarını doğrula. Aykırı olanları gerekçesiyle dışarıda bırak.
2. Problem tanımını yaz: ne başarısız, nerede, ne sıklıkla, ne zamandan beri ve toplam etki. Tanım varsayılan bir nedeni değil, belirti örüntüsünü anlatır.
3. Problemi toplam etki, tekrar sıklığı ve büyüme riskine göre önceliklendir; bir problem sahibi ve kök neden analizi için hedef tarih ata.
4. Bir zaman çizelgesi oluştur ve değişikliklerle (sürümler, yapılandırma, kapasite, veri hacmi, tedarikçi güncellemeleri) ve dış olaylarla ilişkilendir; her korelasyon test edilene kadar bir hipotezdir.
5. Kök neden analizini açık bir yöntemle yürüt (örneğin doğrusal bir zincir için beş neden, çok etkenli durumlar için balık kılçığı, karşılaştırmalar için hata ağacı veya Kepner-Tregoe "öyle/öyle değil" analizi). Her hipotez için lehte ve aleyhte kanıtları kaydet.
6. Hipotezleri her seferinde tek değişkenle test et (test ortamında tekrar üretme, kontrollü yapılandırma değişikliği, ek loglama). Kanıt olmadan kök neden ilan etme; önerilen üç çözüm başarısız olursa bir sonraki yamayı değil, varsayımları ve tasarımı sorgula.
7. Neden veya güvenilir bir geçici çözüm doğrulandığında bilinen hata kaydını oluştur; geçici çözümü (hizmeti geri getirir) kalıcı çözümden (nedeni ortadan kaldırır) ayır.
8. Maliyet, risk ve eforlarıyla kalıcı çözüm seçeneklerini öner ve seçilen seçenek için değişiklik kontrolü üzerinden bir değişiklik talebi aç.
9. Doğrulamayı tanımla: çözümün işe yaradığını kanıtlayan metrik ve gözlem süresi (örneğin art arda 30 çalıştırmada sıfır gecikme) ve tekrarı yakalayacak izleme.
10. Problemi yalnızca doğrulamadan sonra kapat; çıkarılan dersleri, katkıda bulunan etkenleri (süreç, izleme, kapasite) ve sahipli takip aksiyonlarını kaydet.
11. Devret: bilgi bankası için `known-error-article`, kalıcı çözüm için `change-request-rfc`, daha derin bir kök neden oturumu için `five-whys` / `fishbone-analysis` öner.

## Çıktı formatı
```markdown
# Problem: <PRB no> – <belirti örüntüsü>
| Alan | Değer |
|---|---|
| Durum | yeni / inceleniyor / bilinen hata / değişiklikte / doğrulandı / kapandı |
| Sahip / Analiz hedef tarihi | <...> |
| Öncelik | <P> – <toplam etki ve tekrar sıklığı> |
| İlişkili olaylar | <numaralar, sayı, dönem> |
| Konfigürasyon öğeleri | <...> |

## Problem Tanımı
<ne, nerede, ne sıklıkla, ne zamandan beri, etki>
## Zaman Çizelgesi ve Korelasyonlar
| Tarih | Olay | Kaynak | İlişkili mi? |
|---|---|---|---|
## Kök Neden Analizi (<yöntem>)
| Hipotez | Lehte kanıt | Aleyhte kanıt | Test / sonuç |
|---|---|---|---|
- Kök neden: <doğrulanmış ifade> veya [BİLİNMİYOR – inceleme sürüyor]
- Katkıda bulunan etkenler: ...
## Bilinen Hata
- Geçici çözüm: ... Bilinen hata makalesi: <no / yazılacak>
## Kalıcı Çözüm
| Seçenek | Efor | Risk | Seçildi mi? | Değişiklik no |
|---|---|---|---|---|
## Doğrulama
- Başarı metriği: ... Gözlem süresi: ... İzleme: ...
## Aksiyonlar
| Aksiyon | Sahip | Tarih |
|---|---|---|
```

## Kalite kontrol listesi
- [ ] Problem tanımı varsayılan bir nedeni değil, belirti örüntüsünü ve etkiyi anlatıyor.
- [ ] İlişkilendirilen her olay belirtiyi paylaşıyor; dışarıda bırakılanların gerekçesi var.
- [ ] Kök neden kanıtla destekleniyor; test edilmemiş fikirler hipotez veya `[BİLİNMİYOR]` olarak kalıyor.
- [ ] Geçici çözüm ile kalıcı çözüm ayrılmış, kalıcı çözüm değişiklik kontrolünden geçiyor.
- [ ] Kapanış ölçülebilir bir doğrulama süresine bağlı.
- [ ] Uydurulmuş sayı yok; eksik kesinti süresi veya maliyet `[BİLİNMİYOR]`.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Geçici çözüm belgelenince problemi kapatmak. Bilinen hata bir ara hedeftir, son değil.
- "İnsan hatası" veya "job'da hata" noktasında durmak. Sürecin veya izlemenin buna neden izin verdiğini sor.
- En son değişiklikle korelasyon kurup test etmeden onu neden ilan etmek.
- Kök neden analizini suçlu arama egzersizine çevirmek; insanlar bilgi saklar ve gerçek neden gizli kalır.

## Örnek
Girdi: "3 haftada gece batch'inin uzayıp sabah raporlarının geciktiği 7 olay; her biri yeniden başlatmayla çözüldü."

Çıktıdan bir bölüm:
- Problem tanımı: Gece mutabakat batch'i 21 günde 7 kez 06:00 tamamlanma penceresini aştı (INC-...); her seferinde sabah raporları gecikti. Tek çözüm yeniden başlatma oldu.
- Korelasyon [VARSAYIM]: gecikmeler ay sonu veri hacmi artışından sonra başladı; ayrıca veritabanı indeks bakımının 02:00'ye taşınmasıyla (CHG-...) çakışıyor.
- Test: batch'i staging'de üretim hacmiyle, eş zamanlı indeks bakımı açıkken ve kapalıyken çalıştır.
- Doğrulama: 05:00'te alarm kurulu olarak art arda 30 çalıştırmanın 05:30'dan önce tamamlanması.
