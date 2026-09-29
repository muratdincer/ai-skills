---
name: impact-analysis
description: "Önerilen bir değişikliğin süreçler, sistemler, arayüzler, veri, raporlar, kullanıcılar, dokümanlar, kontroller ve testler üzerindeki etkisini doğrudan ve dolaylı bağımlılıkları izleyerek analiz eder; her etkiyi kanıt ve güven düzeyiyle puanlar. Yeni bir gereksinim, değişiklik talebi, kural değişikliği veya sistem değişikliği önerildiğinde ve ekibin tahmin, onay veya yayın öncesinde başka neyin etkilendiğini bilmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: solution
  title: "Etki analizi"
  related: "change-request-analysis, traceability-matrix, process-gap-analysis, regression-selection, dependency-map"
  prompt: "Ana bankacılık sistemimizde müşteri numarasını sayısaldan alfanümeriğe çevirmenin etkisi ne olur?"
---

# Etki Analizi

## Amaç
Bir değişikliğin yayılan etkisini tahmin veya onaydan önce görünür kılmak; böylece sonraki halkalarda hiçbir şey sessizce bozulmaz ve efor, test kapsamı ve iletişim tam resme dayanır.

## Ne zaman kullanılır
- Bir değişiklik talebi, yeni kural veya mevzuat değişikliği mevcut bir sistemi veya süreci etkilediğinde.
- Bir alan, kod listesi, hesaplama veya arayüz değiştirildiğinde.
- Test ekibinin neyin regresyon testinden geçeceğini bilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Değişikliği kabul, erteleme veya ret önerisi gerekiyorsa `change-request-analysis` kullanılır (bu analizi girdi olarak kullanır).
- As-is'ten to-be'ye tüm geçiş planlanıyorsa `process-gap-analysis` kullanılır.
- Bilinen bir etki listesinden yalnızca test seçimi yapılacaksa `regression-selection` kullanılır.

## Girdiler
Zorunlu:
- Değişikliğin kesin tarifi (ne değişiyor, neden neye).

İsteğe bağlı, kaliteyi artırır:
- İzlenebilirlik matrisi, sistem haritası veya arayüz listesi, veri sözlüğü.
- Süreç modelleri, rapor envanteri, sonraki tüketicilerin listesi.
- Her sistemi bilen kişilere erişim (etkileri teyit etmek için).

Değişiklik tarifi muğlaksa ("müşteri ekranını iyileştir") önce somut değişikliği sor. Eksik sistem bilgisi tahmin değil "teyit edilecek" madde olur.

## Süreç
1. Değişikliği kesin bir fark olarak yeniden ifade et: nesne, nitelik veya kural, eski davranış, yeni davranış, yürürlük tarihi.
2. Değişikliğin başlangıç noktasını belirle (değişikliğin olduğu sistem, tablo, kural veya süreç adımı).
3. Birinci derece etkileri katman katman izle: iş süreçleri ve adımları; kullanıcı rolleri ve ekranlar; iş kuralları ve hesaplamalar; veri (tablolar, alanlar, formatlar, referans veri, geçmiş veri); arayüzler ve API'ler (üretenler ve tüketenler); raporlar, panolar ve veri çıktıları; batch işler.
4. İkinci derece etkileri izle: etkilenen arayüz ve raporların tüketicileri, arşiv verisi, veri ambarı ve analitik, iş ortağı sistemleri, doküman ve eğitim materyali, kontroller ve denetim izleri.
5. Yatay konuları kontrol et: güvenlik ve yetkiler, kişisel veri (KVKK/GDPR), performans ve hacim, mevcut kayıtların taşınması, geriye uyumluluk ve sürümleme.
6. Her etki için kaydet: alan, kalem, değişikliğin niteliği (yok / konfigürasyon / kod / veri / doküman / süreç), puan (Yüksek/Orta/Düşük), kanıt, güven (Teyitli / Muhtemel / Teyit edilecek) ve kimin teyit edebileceği.
7. Kapsamı sınırlamak için açıkça etkilenmeyenleri ve nedenini belirt.
8. Sonuçları çıkar: efor sürücüleri (verilmedikçe rakam değil), test kapsamı, taşıma ihtiyacı, iletişim ve eğitim, yayın sıralaması.
9. Riskleri ve açık soruları, tahmini ne kadar değiştirebileceklerine göre sıralayarak listele.
10. Kullanıcı devam etmek isterse karar için `change-request-analysis`, test kapsamı için `regression-selection` veya bağlantıları güncel tutmak için `traceability-matrix` öner.

## Çıktı formatı
```markdown
# Etki Analizi: <değişiklik>
Değişiklik: <eski → yeni> · Başlangıç noktası: <sistem/süreç> · Yürürlük: <tarih veya [BİLİNMİYOR]>

## Özet
<3-5 satır: etkinin genişliği, başlıca riskler, güven düzeyi>

## Etki Kaydı
| # | Alan | Kalem | Değişikliğin niteliği | Puan | Kanıt | Güven | Teyit edecek |
|---|---|---|---|---|---|---|---|

## Etkilenmeyenler (ve nedeni)
- ...

## Sonuçlar
- Efor sürücüleri: ...
- Test kapsamı: ...
- Veri taşıma: ...
- İletişim / eğitim: ...

## Riskler ve Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Değişiklik kesin bir eski → yeni farkı olarak ifade edildi.
- [ ] Tüm katmanlar kontrol edildi: süreç, kullanıcılar, kurallar, veri, arayüzler, raporlar, batch, dokümanlar, kontroller.
- [ ] Yalnızca başlangıç sistemi değil, sonraki tüketiciler (ikinci derece etkiler) de listelendi.
- [ ] Her etkinin kanıtı ve güven düzeyi var; teyitsiz kalemlerde kimin teyit edeceği yazıyor.
- [ ] Kişisel veri, güvenlik ve mevcut verinin taşınması açıkça değerlendirildi.
- [ ] Çıkarımla bulunan etkiler Muhtemel veya Teyit edilecek olarak etiketli, asla Teyitli değil.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Değişen sistemde durmak. Olayların çoğu bilinmeyen tüketicilerden gelir: veri çıktıları, raporlar, iş ortağı dosyaları.
- Geçmiş veriyi unutmak. Yeni bir format veya kural, mevcut kayıtlara ne olacağını söylemelidir.
- "Kod değişikliği yok"u "etki yok" saymak. Konfigürasyon, dokümanlar, eğitim ve testler yine değişir.

## Örnek
Girdi: "Müşteri numarası 10 haneli sayısaldan 12 karakterli alfanümeriğe değişiyor."

Çıktıdan bir bölüm:
| # | Alan | Kalem | Nitelik | Puan | Güven | Teyit edecek |
|---|---|---|---|---|---|---|
| 1 | Veri | CUSTOMER.ID kolon tipi ve tüm yabancı anahtarlar | Kod + veri | Yüksek | Teyitli | DBA |
| 2 | Arayüz | Kart sistemi günlük dosyası (sabit uzunluk, 10 karakter) | Kod | Yüksek | Muhtemel | Kart sistemi sahibi |
| 3 | Rapor | Yasal rapor sayısal numaraya göre sıralıyor | Kod | Orta | Teyit edilecek | Yasal raporlama |
| 4 | Kullanıcılar | Çağrı merkezi araması yalnızca rakam kabul ediyor | Konfigürasyon | Orta | Muhtemel | Kanal ekibi |
