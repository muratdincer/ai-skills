---
name: invest-check
description: "Kullanıcı hikayelerini INVEST kriterlerine (Bağımsız, Tartışılabilir, Değerli, Tahmin Edilebilir, Küçük, Test Edilebilir) göre değerlendirir, her kriteri kanıtıyla puanlar ve bölme, yeniden yazma veya eksik kabul kriteri gibi somut düzeltmeler önerir. Backlog iyileştirmesi sırasında, hikayeler bir iterasyona veya taahhüde girmeden önce ya da bir hikaye sürekli yeniden tahmin edilip devrediliyorsa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: quality
  title: "INVEST kontrolü"
  related: "user-story, acceptance-criteria, story-splitting, definition-of-ready, backlog-refinement"
  prompt: "Ödeme epiğindeki bu 8 hikayeye INVEST kontrolü yap, hangileri hazır değil söyle."
---

# INVEST Kontrolü

## Amaç
Ekibe her hikaye için planlanıp geliştirilmeye hazır olup olmadığını ve değilse tam olarak neyin değişmesi gerektiğini söylemek. Çıktı, genel bir INVEST anlatımı değil; kanıtlı ve uygulanabilir düzeltmeler içeren puanlı bir tablodur.

## Ne zaman kullanılır
- Backlog iyileştirmesi (refinement) sırasında veya bir planlama oturumundan önce.
- Bir hikaye tekrar tekrar devrediliyor, yeniden tahmin ediliyor veya tartışılıyorsa.
- Yeni bir ekip veya paydaş hikaye yazıyor ve hızlı geri bildirim istiyorsa.

## Ne zaman kullanılmaz
- Hikayeler sıfırdan yazılacaksa `user-story` kullanılır.
- Hikaye iyi ama çok büyükse ve bölme seçenekleri gerekiyorsa `story-splitting` kullanılır.
- Yalnızca INVEST değil ekibin tüm hazır olma kriterleri isteniyorsa `definition-of-ready` kullanılır.

## Girdiler
Zorunlu:
- Bir veya daha fazla hikaye: başlık, anlatı ve varsa kabul kriterleri.

İsteğe bağlı, kaliteyi artırır:
- Epik veya hedef bağlamı, ilişkili hikayeler, bilinen bağımlılıklar.
- Ekibin tipik hikaye büyüklüğü veya iterasyon uzunluğu ("Küçük" için).
- Ekibin hazır olma tanımı (definition of ready).

Kabul kriteri yoksa yine değerlendir, ancak Test Edilebilir'i başarısız işaretle.

## Süreç
1. Her hikayeyi tek satırda yeniden ifade et: kullanıcı, yetenek, fayda. Fayda yoksa, teknikse ("API çağrılsın diye") ya da isteği tekrar ediyorsa Değerli için not al. Genel personaları ("bir kullanıcı olarak") ve hikaye gibi yazılmış teknik görevleri işaretle; teknik görevler hikaye listesine değil iş kırılımına aittir.
2. Bağımsız: diğer hikayelere, ekiplere veya sistemlere bağımlılıkları listele. Sert (başlanamaz) ile yumuşak (sıralama tercihi) bağımlılığı ayır. Yeniden sıralama, taklit (stub) veya birleştirme öner.
3. Tartışılabilir: hikayenin açık kalması gereken UI veya teknik çözüm ayrıntılarını dayatıp dayatmadığını kontrol et. Aşırı tanımlamayı işaretle.
4. Değerli: sonucun bir kullanıcı veya iş paydaşı tarafından fark edilip edilmeyeceğini kontrol et. Yalnızca teknik hikayeler sağladığı sonucu belirtmeli veya bir değer hikayesine bağlanmalı.
5. Tahmin Edilebilir: tahmini engelleyen bilinmeyenleri (alan, teknik, dış) belirle. Her biri için bir spike veya soru öner.
6. Küçük: ekibin tipik büyüklüğüne göre değerlendir; bilinmiyorsa çok sayıda kabul kriteri, birden fazla rol, birden fazla iş akışı veya başlıkta "ve" olan hikayeleri işaretle. Bir bölme kalıbı adlandır (iş akışı adımı, iş kuralı, veri çeşitliliği, mutlu/mutsuz yol, arayüz).
7. Test Edilebilir: kabul kriterlerinde gözlemlenebilir sonuçlar, veri koşulları ve hata durumları var mı kontrol et. Eksik kriterleri Given/When/Then veya kural biçiminde öner; birden fazla When veya Then içeren senaryo bölme adayıdır.
8. Her harfi Geçti / Kısmi / Kaldı olarak tek satırlık kanıtla puanla; genel karar: Hazır / İyileştirilmeli / Hazır değil.
9. Ekip iyileştirme oturumunda harekete geçebilsin diye düzeltmeleri efor/etki oranına göre sırala.
10. Kullanıcı devam etmek isterse Small kriterinden kalan hikayeler için `story-splitting`, Testable kriterinden kalanlar için `acceptance-criteria` veya tam hazırlık kapısı için `definition-of-ready` öner.

## Çıktı formatı
```markdown
# INVEST Kontrolü: <epik / set>

## Genel Bakış
| Hikaye | I | N | V | E | S | T | Karar |
|---|---|---|---|---|---|---|---|
| S1 <başlık> | Geçti | Kısmi | Geçti | Kaldı | Geçti | Kısmi | İyileştirilmeli |

## Hikaye Ayrıntıları
### S1 <başlık>
- Kanıt: I … / N … / V … / E … / S … / T …
- Düzeltmeler:
  1. <somut değişiklik>
  2. <Given/When/Then biçiminde eksik kabul kriteri>
- Sorular: <tahmini ne engelliyor, kim cevaplar>
```

## Kalite kontrol listesi
- [ ] Her puanın hikayeden alıntılanan veya gösterilen bir kanıtı var.
- [ ] Her Kaldı veya Kısmi için en az bir somut düzeltme var.
- [ ] Bölme önerileri bir bölme kalıbı adlandırıyor ve dikey kesilmiş, değerli hikayeler üretiyor.
- [ ] Önerilen kabul kriterleri kararlaştırılmış kapsam olarak değil, öneri olarak işaretli.
- [ ] Ekibin ölçeği verilmediyse story point cinsinden büyüklük yargısı yapılmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Teknik katmana göre bölmek (UI hikayesi, API hikayesi, DB hikayesi). Bu Değerli ve Bağımsız'ı bozar; davranışa göre böl.
- Bağımsız'ı mutlak saymak. Bir miktar sıralama normaldir; yalnızca paralel çalışmayı veya planlamayı engelleyen bağımlılıkları işaretle.
- Meşru kısıtlar (mevzuat, sözleşme) yüzünden Tartışılabilir'i başarısız saymak. Bunları kısıt olarak işaretle.

## Örnek
Girdi: "S3: Kullanıcı olarak kart ve PayPal ile ödeme yapmak ve kartımı kaydetmek istiyorum ki ödeme daha kolay olsun." Kabul kriteri yok.

Çıktıdan bir bölüm:
| Hikaye | I | N | V | E | S | T | Karar |
|---|---|---|---|---|---|---|---|
| S3 | Kısmi | Geçti | Geçti | Kısmi | Kaldı | Kaldı | Hazır değil |

Düzeltmeler: ödeme yöntemine ve "kartı kaydet"e göre böl (iş kuralı çeşitliliği); reddedilen kart ve 3-D Secure hatası için kriter ekle; kart saklamanın ödeme sağlayıcısı tarafından token'lanıp token'lanmadığını Güvenlik ekibine sor `[BİLİNMİYOR]`.


Zayıf yeniden yazım: "Bir kullanıcı olarak kolayca ödemek istiyorum ki ödeyebileyim." (genel persona, fayda isteği tekrar ediyor)
Güçlü yeniden yazım: "Tekrar gelen bir müşteri olarak kayıtlı kartımla ödemek istiyorum ki kart bilgilerimi yeniden girmeden alışverişi tamamlayabileyim."
