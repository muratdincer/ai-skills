---
name: integration-test-writing
description: "Kodu gerçek sınırlar (veritabanı, mesaj kuyruğu, HTTP API'leri, dosya deposu, önbellek) üzerinden çalıştıran entegrasyon testleri yazar; mümkün olduğunda geçici gerçek bağımlılıklar, yalnızca ekibin sahibi olmadığı sistemler için test dublörleri kullanır; eşleme, transaction, serileştirme, hata ve zaman aşımı davranışını izole veri ve deterministik hazırlıkla kapsar. Entegrasyon testi istendiğinde, bir repository, API uç noktası, tüketici veya dış istemcinin gerçek altyapıya karşı doğrulanması gerektiğinde ya da mock'lu birim testleri davranışı kanıtlayamadığında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: testing
  title: "Entegrasyon testi yazma"
  related: "unit-test-writing, api-test-design, test-data-design, flaky-test-analysis, test-gap-finder"
  prompt: "OrderRepository ve OrderPlaced tüketicisi için entegrasyon testleri yaz; ilişkisel veritabanı ve mesaj kuyruğu kullanıyoruz."
---

# Entegrasyon Testi Yazma

## Amaç
Bileşenlerin, mock'lu birim testlerinin doğrulayamadığı gerçek sınırlar (sorgular, eşlemeler, transaction'lar, serileştirme, protokol ve hata davranışı) üzerinden birlikte çalıştığını kanıtlamak; bunu yaparken testleri her değişiklikte koşturulabilecek kadar güvenilir tutmak.

## Ne zaman kullanılır
- Veri erişim kodu, ORM eşlemeleri, migration'lar veya sorgular gerçek bir veritabanı motoruna karşı doğrulanmalıysa.
- Bir API uç noktası, mesaj tüketicisi/üreticisi veya dış istemci tek bir servis içinde uçtan uca test edilmeliyse.
- Gerçek bağımlılık farklı davrandığı için bir hata mock'lu birim testlerinden kaçtıysa.

## Ne zaman kullanılmaz
- Mantık altyapı olmadan izole biçimde doğrulanabiliyorsa `unit-test-writing` kullanılır.
- Amaç bir API için tüketici tarafından test tasarımıysa (durum kodları, yetki matrisi) `api-test-design` kullanılır.
- Mevcut entegrasyon testleri ara ara kırılıyorsa `flaky-test-analysis` kullanılır.

## Girdiler
Zorunlu:
- Test edilecek bileşen(ler) ve aştıkları sınırlar (hangi veritabanı, kuyruk, API'ler).

İsteğe bağlı, kaliteyi artırır:
- Bileşenin kodu ve yapılandırması; mevcut test altyapısı (container'lar, bellek içi ikameler, ortak fixture'lar).
- Sözleşmeler (API şartnamesi, mesaj şeması), beklenen transaction ve yeniden deneme davranışı, CI kısıtları (süre bütçesi, container desteği).

Sınırlar belirtilmemişse koddan çıkar ve `[VARSAYIM]` olarak işaretle. Test altyapısı bilinmiyorsa geçici gerçek bağımlılıklar öner ve bunu açık soru olarak listele.

## Süreç
1. Test sınırını tanımla: hangi bileşenler gerçek (servis, veritabanı, kuyruk), hangileri değiştiriliyor (ekibin sahibi olmadığı üçüncü taraf sistemler). Her değiştirme için gerekçeyi yaz.
2. Gerçekçi bağımlılıklar seç: lehçesi, kilitleme veya kısıt davranışı farklı olan bellek içi ikameler yerine üretimle aynı motor ve ana sürümde geçici bir örneği tercih et; her farkı bilinen kısıt olarak işaretle.
3. Her sınır için entegrasyon risklerini listele: eşleme ve kolon tipleri, null ve varsayılan değerler, kısıtlar ve benzersizlik ihlalleri, transaction ve rollback, izolasyon ve eşzamanlı yazma, serileştirme ve şema evrimi, sayfalama ve sıralama, saat dilimi ve hassasiyet, zaman aşımı, yeniden deneme, idempotency, zehirli mesajlar.
4. Her riski gözlemlenebilir bir sonucu olan senaryoya çevir (satır durumu, yanıt, yayınlanan mesaj, dead-letter kaydı); belirtilmiş gereksinimleri koddan çıkarılan davranıştan ayır ve ikincileri `[VARSAYIM]` olarak etiketle.
5. Veri izolasyonunu tasarla: her test kendi verisini benzersiz anahtarlarla oluşturur ya da kod transaction'ı kendisi yönetmiyorsa geri alınan bir transaction içinde çalışır; başka testlerin bıraktığı veriye veya seed sırasına asla bağımlı olma.
6. Dış sistemleri hata, gecikme ve bozuk yük döndürebilen stub HTTP sunucuları veya sözleşmeye dayalı fake'lerle değiştir; davranışın parçasıysa servisin gönderdiği isteği doğrula.
7. Asenkronluğu sleep olmadan yönet: beklenen durumu veya mesajı zaman aşımıyla yokla; test son gözlenen durumu gösteren bir mesajla kırılsın.
8. Her testi bileşenin gerçek giriş noktası (repository metodu, HTTP çağrısı, yayınlanan mesaj) üzerinden Arrange-Act-Assert olarak yaz; iç çağrıları değil kalıcı durumu veya üretilen çıktıyı doğrula.
9. Maliyeti kontrol et: pahalı altyapıyı test koşumu başına paylaş, testler arasında durumu sıfırla, entegrasyon testlerini ayrı koşturulabilecek şekilde etiketle ve paketi belirtilen CI süre bütçesi içinde tut.
10. Her testin kırılabildiğini doğrula: bir eşlemeyi, kısıtı veya handler'ı boz ve testin anlaşılır bir mesajla kırmızıya döndüğünü gör.
11. Kapsanan riskleri, ortamın bilinen kısıtlarını ve açık soruları raporla.
12. Hedef devam ediyorsa daha zengin veri setleri için `test-data-design`, tüketiciye dönük API kapsamı için `api-test-design` veya kalan test edilmemiş yolları bulmak için `test-gap-finder` öner.

## Çıktı formatı
```markdown
# Entegrasyon Testleri: <bileşen>
Gerçek: <servis, VT motoru/sürümü, kuyruk> · Değiştirilen: <sistem → stub/fake, gerekçe> · Varsayımlar: <liste veya yok>

## Risk Kapsamı
| # | Sınır | Risk | Senaryo | Test |
|---|---|---|---|---|
| R1 | VT | Mükerrer sipariş numarasında benzersizlik ihlali | Aynı numara iki kez eklenir → alan hatası, yarım satır yok | <test adı> |

## Hazırlık ve İzolasyon
<altyapı yaşam döngüsü, veri stratejisi, sıfırlama yaklaşımı>

## Testler
<sınıra göre gruplanmış test kodu>

## Bilinen Kısıtlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Değiştirilen her bağımlılık ekibin sahibi olmadığı bir sistem ve gerekçesi yazılı.
- [ ] Veritabanı ve kuyruk davranışı üretim motorunda test ediliyor ya da fark listelendi.
- [ ] Testler izole: paylaşılan değişken veri yok, sıra bağımlılığı yok, sabit sleep yok.
- [ ] Hata yolları kapsandı: kısıt ihlalleri, zaman aşımları, bozuk yükler, yeniden denemeler veya dead-letter'lar.
- [ ] Doğrulamalar kalıcı durumu veya üretilen çıktıyı kontrol ediyor ve her testin doğru nedenle kırıldığı gösterildi.
- [ ] Çıkarılan davranış ve sınırlar `[VARSAYIM]` olarak etiketlendi; ortam boşlukları açık soru olarak listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Lehçesi farklı bellek içi veritabanı kullanmak; testler geçer ama üretimde sorgular kilitleme, collation veya tipler yüzünden kırılır. Gerçek motoru kullan ya da farkı belgele.
- "Entegrasyon" testinde veritabanını mock'lamak; bu fazladan hazırlığı olan bir birim testidir ve sınır hakkında hiçbir şey kanıtlamaz.
- Asenkron tüketiciler için `sleep(5)`; hem yavaş hem yine kararsız. Beklenen durumu zaman aşımıyla yokla.

## Örnek
Girdi: "OrderRepository'yi ve stok ayıran OrderPlaced tüketicisini test et."

Çıktıdan bir bölüm:
- Gerçek: servis, geçici container'da ilişkisel VT (üretimle aynı ana sürüm `[VARSAYIM]`), kuyruk container'ı. Değiştirilen: ödeme sağlayıcısı → HTTP stub.
- R3 (kuyruk): Aynı OrderPlaced mesajı iki kez teslim edilir → stok bir kez ayrılır (mesaj kimliğiyle idempotency anahtarı). Ayırma satırını en fazla 10 sn yokla.
- R5 (kuyruk): Bozuk yük → mesaj dead-letter kuyruğuna düşer, ayırma yapılmaz, hata mesaj kimliğiyle loglanır.
- Kısıt: Testlerdeki izolasyon seviyesi ancak bağlantı dizesi ayarlıyorsa üretimle aynıdır `[açık soru: VT yapılandırmasının sahibi]`.
