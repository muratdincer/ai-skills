---
description: "Bir sistemin ortam yapısını tanımlar: hangi ortamların neden var olduğu, üretimle eşdeğerlik, test verisi politikası, erişim ve değişiklik yetkileri, yaşam döngüsü (kalıcı veya geçici) ve sahiplik. Ortamlar amaçsızca çoğaldığında, testler staging'de geçip üretimde kırıldığında ya da yeni bir platform için ortam modeli üzerinde uzlaşılması gerektiğinde kullanılır."
related: "pipeline-design, test-data-design, secrets-management-plan, finops-review, deployment-strategy"
prompt: "dev, test, uat, preprod ve prod ortamlarımız var ve hangisinin ne için kullanıldığını kimse bilmiyor. Bizim için bir ortam stratejisi tanımla."
---

# Ortam Stratejisi

## Amaç
Her ortama net bir amaç, sahip, veri politikası ve erişim modeli vermek; böylece testler anlamlı, maliyet gerekçeli olur ve üretime benzer doğrulama üretimden önce yapılır.

## Ne zaman kullanılır
- Yeni bir ürün veya platform için ortam modeli gerektiğinde.
- Ortamlar birbirinden uzaklaştıysa ve "staging'de çalışıyordu" hataları sıksa.
- Üretim dışı ortamların test verisi, erişimi veya maliyeti sorun olduğunda.
- Branch başına geçici ortamlar değerlendiriliyorsa.

## Ne zaman kullanılmaz
- Konu terfi akışı ve kapılarsa `pipeline-design` kullanılır.
- Konu test veri setlerinin tasarımıysa `test-data-design` kullanılır.
- Yalnızca üretim dışı maliyet sorgulanıyorsa `finops-review` kullanılır.

## Girdiler
Zorunlu:
- Mevcut veya planlanan ortamlar ile sistemin ana bileşenleri ve bağımlılıkları (veritabanları, kuyruklar, üçüncü taraf API'ler).

İsteğe bağlı, kaliteyi artırır:
- Her ortamı kimin kullandığı (geliştiriciler, QA, iş birimi UAT, performans, iş ortakları).
- Veriye ilişkin mevzuat kısıtları (KVKK/GDPR, PCI DSS, bankacılık düzenlemeleri).
- Ortam başına altyapı maliyeti, kurulum yöntemi (IaC veya manuel).

Bileşen listesi yoksa iste; diğer eksikler açık sorulara gider.

## Süreç
1. Her ortamı tek bir birincil amacı ve birincil kullanıcılarıyla listele. Ayrı bir amacı olmayan ortamları birleştir veya kaldır.
2. Her ortamın yaşam döngüsünü belirle: kalıcı, pull request başına geçici veya performans testleri için talep üzerine.
3. Üretimle eşdeğerliği boyut bazında tanımla: altyapı topolojisi, sürümler (OS, runtime, veritabanı motoru), yapılandırma, ağ/güvenlik kontrolleri, ölçek, veri hacmi. Kabul edilen farkları açıkça yaz.
4. Her ortam için dış bağımlılıkları tanımla: gerçek sandbox, sözleşme stub'ı, servis sanallaştırma.
5. Veri politikasını tanımla: sentetik, maskelenmiş üretim kopyası veya alt küme. Üretim dışında asla düz üretim kişisel verisi olmaz; KVKK/GDPR veri minimizasyonuna atıf yap.
6. Erişim ve değişiklik yetkilerini tanımla: kim dağıtabilir, kim yapılandırmayı değiştirebilir, kim veriyi okuyabilir; manuel değişikliğe izin var mı (ideal olarak dev dışında yok).
7. Kurulum ve sapma kontrolünü tanımla: tüm ortamlar aynı IaC modüllerinden ortam değişkenleriyle; sapma tespiti.
8. Yenileme ve sıfırlama sıklığını ve kararlılık pencerelerini (ör. kabul sırasında UAT dondurma) tanımla.
9. Sahiplik ve maliyet kontrollerini tanımla: ortam başına sahip, boştaki üretim dışı ortamları kapatma takvimleri, etiketleme.
10. Şablonu doldur, mevcut durumdan geçiş adımlarını ve farkları listele.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa ortamlar arası terfi için `pipeline-design`, ortam bazlı gizli bilgiler için `secrets-management-plan` veya üretim dışı veri için `test-data-design` öner.

## Çıktı formatı
```markdown
# Ortam Stratejisi: <sistem>
| Ortam | Amaç | Kullanıcılar | Yaşam döngüsü | Dağıtım tetikleyicisi | Veri | Erişim (dağıtım/yapılandırma/veri) | Sahip |
## Üretimle Eşdeğerlik
| Boyut | Dev | Test | Staging | Kabul edilen fark |
## Ortam Bazında Dış Bağımlılıklar
## Veri Politikası ve Maskeleme
## Kurulum ve Sapma Kontrolü
## Yenileme, Dondurma ve Çalışma Takvimleri
## Mevcut Durumdan Değişiklikler
## Açık Sorular / Varsayımlar
```

## Kalite kontrol listesi
- [ ] Her ortamın tam olarak bir birincil amacı ve bir sahibi var.
- [ ] Üretimle eşdeğerlik farkları, özellikle üretim öncesi son ortam için, açıkça yazıldı.
- [ ] Üretim dışında maskelenmemiş üretim kişisel verisi yok.
- [ ] Her ortam için manuel değişiklik kuralı ve dağıtım yetkisi tanımlı.
- [ ] Tüm ortamlar değişkenlerle aynı koddan kuruluyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Veritabanı motoru sürümü veya ağ politikası farklı olduğu için hiçbir şey kanıtlamayan bir staging. Eşdeğerlik farklarını kaydet ve kapat.
- Herkesin değiştirdiği paylaşılan uzun ömürlü test ortamları. Özellik doğrulaması için geçici ortamlar kullan.
- Kolaylık olsun diye üretim verisini kopyalamak. Maskele veya sentetik üret, hukuki dayanağı belgele.

## Örnek
Girdi: "dev, test, uat, preprod, prod; uat ve preprod'u iş birimi kullanıyor; test ortamında üretim kopyası var."

Çıktıdan bir bölüm:
| Ortam | Amaç | Yaşam döngüsü | Veri |
|---|---|---|---|
| pr-* | Pull request başına özellik doğrulaması | Geçici | Sentetik |
| test | Entegre sistem testleri, QA otomasyonu | Kalıcı | Sentetik + maskelenmiş alt küme |
| staging (uat+preprod birleşimi) | UAT ve sürüm doğrulaması, üretime benzer topoloji | Kalıcı, kabul sırasında dondurulur | Maskelenmiş üretim alt kümesi `[maskeleme kurallarını teyit et]` |
