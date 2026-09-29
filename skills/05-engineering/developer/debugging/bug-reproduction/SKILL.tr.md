---
description: Belirsiz bir hata bildirimini; kesin adımlar, ortam, veri ön koşulları, beklenen ve gerçekleşen sonuç ile tekrar oranı içeren minimal ve deterministik bir yeniden üretime dönüştürür, mümkünse başarısız olan otomatik bir testle bitirir. Bir hata zor üretilebilir, aralıklı, ortama özgü olduğunda veya yalnızca kullanıcı diliyle anlatıldığında ve düzeltmeye başlamadan önce kullanılır.
related: bug-report, debugging-hypotheses, log-analysis, unit-test-writing, flaky-test-analysis
prompt: Kullanıcılar dışa aktarımın bazen boş dosya ürettiğini söylüyor. Güvenilir bir yeniden üretim kurmama yardım et.
---

# Hatayı Yeniden Üretme

## Amaç
Her seferinde (veya bilinen bir oranda) en az adım ve değişkenle başarısız olan bir yeniden üretim kurmak. Bu olmadan düzeltmeler tahmindir ve doğrulama imkânsızdır; bununla düzeltme kanıtlanabilir ve bir regresyon testiyle korunabilir.

## Ne zaman kullanılır
- Hata bildiriminde adımlar eksikse veya geliştirici hatayı tetikleyemiyorsa.
- Hata aralıklıysa veya yalnızca bazı ortam, tenant veya cihazlarda görünüyorsa.
- Düzeltmeden önce hatayı başarısız bir test olarak yakalamak için.

## Ne zaman kullanılmaz
- Yeniden üretim biliniyor ve neden aranıyorsa `debugging-hypotheses` veya `stack-trace-analysis` kullanılır.
- Takip için hata kaydı yazmak için `bug-report` kullanılır.
- Kod değişmeden bazen geçip bazen kalan bir testteki hata için `flaky-test-analysis` kullanılır.

## Girdiler
Zorunlu:
- Hata açıklaması: ne gözlemlendi ve nerede.

İsteğe bağlı, kaliteyi artırır:
- Ortam ve sürüm, gerçekleşme zamanı, etkilenen kullanıcı veya tenant'lar, cihaz/tarayıcı.
- Loglar, hata kimlikleri, correlation/trace ID'ler, ekran görüntüleri.
- Son değişiklikler (dağıtımlar, yapılandırma, veri migration'ları, feature flag'ler).

Hangi sistemin veya özelliğin etkilendiğini bilmiyorsan sor. Paylaşılan log veya örnek kayıtlardaki kişisel verileri maskele.

## Süreç
1. Hatayı beklenen ve gerçekleşen davranış olarak birer cümleyle yeniden yaz; gözlemleri bildirenin yorumundan ayır.
2. Önemli olabilecek değişkenleri çıkar: sürüm/build, ortam, yapılandırma ve feature flag'ler, veri şekli ve hacmi, kullanıcı rolü/yetkileri, dil/saat dilimi/saat, eşzamanlılık ve zamanlama, ağ koşulları, istemci cihazı/tarayıcı.
3. Başarısız bir durumu çalışan bir durumla karşılaştır ve farkları listele; bilinen son sağlıklı an ile ilk hatalı an arasındaki son değişiklikleri (commit'ler, yapılandırma, veri, bağımlılıklar) de ekle. Her fark aday bir değişkendir.
4. İlk yeniden üretimi bildirilen koşullara olabildiğince yakın kur (aynı sürüm, benzer veri, aynı rol). Başarısız olup olmadığını ve ne sıklıkta olduğunu kaydet (ör. 20 çalıştırmada 3).
5. Küçült: her seferinde tek bir değişkeni kaldır veya sabitle ve yeniden çalıştır; bir değişkeni yalnızca kaldırınca hata kayboluyorsa tut. Olasılık uzayı büyükse veri setleri, commit'ler veya yapılandırma üzerinde ikiye bölme (bisection) kullan.
6. Aralıklı hatalarda şüpheli koşulu zorla: sabit seed, dondurulmuş saat, enjekte edilmiş gecikme, küçültülmüş havuz boyutları, paralel çalıştırma, büyük veri hacmi. Öncesi ve sonrası tekrar oranını raporla.
7. Yeniden üretim kararlı olduğunda onu olabilecek en düşük seviyede ifade et: önce birim veya entegrasyon testi, sonra API çağrı dizisi, en son UI adımları.
8. Ön koşulları ve test verisini sentetik veya maskelenmiş veriyle açıkça belgele.
9. Yeniden üretemezsen denenenleri, elenen değişkenleri ve gereken ek kanıtı (log alanları, trace, dump, müşteri veri örneği) tam olarak belgele.
10. Devret: kararlı bir yeniden üretim varsa kök nedeni bulmak için `debugging-hypotheses` (doğrulanmadan düzeltme yok) ve başarısız testi kalıcı kılmak için `unit-test-writing` öner; hata kaydının kendisi eksikse `bug-report` öner.

## Çıktı formatı
```markdown
# Yeniden Üretim: <hata başlığı>
**Durum:** Üretildi (<m> çalıştırmada <n>) | Henüz üretilemedi
**Beklenen:** ...
**Gerçekleşen:** ...

## Ortam
| Öğe | Değer |
|---|---|
| Sürüm / build | ... |
| Ortam | ... |
| Yapılandırma / flag'ler | ... |
| İstemci | ... |

## Ön Koşullar ve Test Verisi
- ...

## Minimal Adımlar
1. ...

## Elenen Değişkenler
- <değişken> — <nasıl test edildi>

## Otomatik Yeniden Üretim
<başarısız test adı ve taslağı veya TBD>

## Üretilemediyse: Gereken Kanıt
- ...
```

## Kalite kontrol listesi
- [ ] Beklenen ve gerçekleşen sonuçlar ayrı ve kesin biçimde yazılmış.
- [ ] Her adım ve ön koşul gerekli; herhangi biri kaldırılınca hata kayboluyor.
- [ ] Deterministik olmayan hatalarda tekrar oranı belirtilmiş.
- [ ] Test verisi sentetik veya maskelenmiş.
- [ ] Başarısız bir otomatik test önerilmiş veya neden olmadığı açıklanmış.
- [ ] Doğrulanmamış ortam bilgileri `[BİLİNMİYOR]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bildirilen sürüm yerine en güncel kodda denemek ve "üretilemiyor" demek. Önce sürümü sabitle.
- Küçültme sırasında birden fazla değişkeni aynı anda değiştirmek. Hangisinin önemli olduğunu söyleyemez hâle gelirsin.
- Yeniden üretim güvenilir hâle gelmeden düzeltmeye başlamak ("şimdilik hızlı bir düzeltme"). Kararlı bir yeniden üretim olmadan düzeltmenin işe yaradığını kanıtlayamazsın.
- Zamanı göz ardı etmek: saat dilimleri, yaz saati geçişleri, ay sonları ve cache süre dolumları tamamen deterministik olan "rastgele" hatalar üretir.

## Örnek
Girdi: "Dışa aktarım bazen boş CSV dosyası üretiyor."

Çıktıdan bir bölüm:
- Değişkenler: dosya boyutu, aynı kullanıcının eşzamanlı dışa aktarımları, depolama gecikmesi, günün saati.
- Küçültme: tek dışa aktarımda 20'de 0; aynı kullanıcı için 1 sn içinde iki dışa aktarım başlatıldığında 20'de 6.
- Minimal adımlar: 1) 1.000'den fazla siparişi olan bir kullanıcıyla giriş yap. 2) İki dışa aktarımı paralel başlat. 3) İlk dosyayı indir: 0 bayt.
- Sonraki adım: iki işin kullanıcı ID'sine bağlı aynı geçici dosya adını paylaştığı hipotezi — `debugging-hypotheses` ile devam.
