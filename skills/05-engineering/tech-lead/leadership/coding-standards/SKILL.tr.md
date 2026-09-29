---
description: Bir ekibin kodlama standartlarını kısa ve numaralı kurallar olarak yazar veya günceller; her kural gerekçe, iyi ve kötü örnek, önem derecesi (zorunlu veya önerilen) ve nasıl uygulatıldığıyla (formatter, linter, inceleme, test) birlikte gelir ve araçların çözemediği kararlara odaklanır. Bir ekip kurulurken veya birleşirken, incelemelerde aynı stil ya da tasarım konuları sürekli tartışıldığında, yeni bir dil veya framework benimsendiğinde ya da mevcut standartlar çok uzun, eskimiş veya uygulanmıyorsa kullanılır.
related: clean-code-review, code-review, review-comment-writing, working-agreement, adr
prompt: Backend ekibimiz için kodlama standartları yaz. İncelemelerde exception yönetimi, isimlendirme ve pull request'in ne kadar büyük olması gerektiği konusunda sürekli tartışıyoruz.
---

# Kodlama Standartları Yazma

## Amaç
Ekibe, kod incelemesindeki tekrarlayan tartışmaları ortadan kaldıran ve kodun tek bir ekipten çıkmış gibi görünmesini sağlayan küçük ve uygulatılabilir bir kurallar seti vermek. Her kural gerekçesini taşır; böylece insanlar kuralın öngörmediği durumlara da uygulayabilir.

## Ne zaman kullanılır
- Yeni bir ekip, repo veya dil için ortak kurallar gerektiğinde.
- İncelemelerde aynı konular (isimlendirme, hata yönetimi, test stili, PR boyutu) tekrar tekrar tartışıldığında.
- Mevcut standartlar uzun, eskimiş, kod tabanıyla çelişiyor veya uygulanmıyorsa.

## Ne zaman kullanılmaz
- Belirli bir değişikliği clean code ilkelerine göre incelemek için `clean-code-review` veya `code-review` kullanılır.
- Kod dışındaki ekip çalışma normları (toplantılar, erişilebilirlik saatleri, nöbet) için `working-agreement` kullanılır.
- Tek bir önemli mimari karar için `adr` kullanılır.

## Girdiler
Zorunlu:
- Dil(ler) ve kapsam (repo, servis, ekip) ile standartların çözmesi gereken sorunlar veya konular.

İsteğe bağlı, kaliteyi artırır:
- Mevcut standartlar, linter ve formatter yapılandırması, tartışmalı inceleme yazışmalarından örnekler.
- Mimari stil ve katman kuralları, test yaklaşımı, güvenlik gereksinimleri.
- Ekip büyüklüğü ve deneyim dağılımı, mevzuat veya müşteri kısıtları.

Dil veya kapsam yoksa sor. Tartışmalı konular hakkında en fazla beş odaklı soru sor; yanıtlanmayan her şeyi ekip tartışması için `[ÖNERİ]` olarak işaretli bir kural önerisine dönüştür.

## Süreç
1. Konuları topla: tartışmalı inceleme temaları, tekrarlayan hatalar, oryantasyon soruları. İnceleme süresine mal olma veya hataya yol açma sıklığına göre sırala.
2. Önce araçlara devret: formatter veya linter'ın uygulatabildiği her şey (biçimlendirme, import sırası, basit isimlendirme kalıpları, karmaşıklık sınırları) düzyazı yerine yapılandırmaya referans veren bir araç kuralı olur.
3. Sıfırdan türetmek yerine dil için yaygın kullanılan bir topluluk stil rehberini temel al; yalnızca ekibin sapmalarını ve eklemelerini listele.
4. Kalan kuralları muhakeme gerektiren konular için yaz: isimlendirme ve alan dili, hata yönetimi ve loglama, modül sınırları ve bağımlılıklar, null ve opsiyonel değer yönetimi, eşzamanlılık, test kuralları, yorum ve dokümantasyon, güvenlik açısından hassas kalıplar (girdi doğrulama, secret'lar, SQL), PR boyutu ve commit kuralları.
5. Her kurala bir kimlik, tek satırlık emir kipinde bir ifade, önem derecesi (Zorunlu: merge'ü engeller / Önerilen: varsayılan, gerekçeyle sapılabilir), bir iki cümlelik gerekçe ve ekibin dilinde kötü ve iyi birer örnek ver.
6. Her kural için uygulatma yolunu tanımla: formatter, linter kuralı, statik analiz, mimari testi, CI kontrolü veya inceleme. Yalnızca incelemeyle uygulatılan kurallar az olmalı.
7. Seti kendi içinde, mevcut kod tabanıyla (ne kadarı ihlal eder) ve kullanılan framework'lerle çelişki açısından kontrol et; toplu yeniden yazım istemek yerine bir geçiş notu ekle (yalnızca yeni kod veya dokunulan kodda izci kuralı).
8. Kısa tut: ekibin yaklaşık on dakikada okuyabileceği bir doküman hedefle; nadir ayrıntıları bağlantılı sayfalara taşı.
9. Değişiklik sürecini tanımla: kimin değişiklik önerebileceği, kararların nasıl verildiği ve istisnaların nasıl kaydedildiği (gerekçeli satır içi bastırma).
10. Çıkarım yapılan kuralları `[ÖNERİ]` olarak işaretle ve ekip için açık kararları listele. Kullanıcı devam ederse standartları resmî olarak benimsemek için `working-agreement`, kodu bunlara göre incelemek için `clean-code-review`, içlerindeki önemli kararlar için `adr` öner.

## Çıktı formatı
```markdown
# Kodlama Standartları: <ekip / repo>
Kapsam: <diller, repolar> · Temel: <topluluk stil rehberi> · Sahip: <ad veya [BİLİNMİYOR]> · Sürüm: <n>

## Araçlarla Uygulatılanlar
| Alan | Araç / yapılandırma | Notlar |
|---|---|---|

## Kurallar
### <Kimlik> <Emir kipinde kural ifadesi> (Zorunlu/Önerilen)
Neden: <gerekçe>
Kötü:
    <kod>
İyi:
    <kod>
Uygulatma: <linter kuralı / mimari testi / inceleme>

## Benimseme
- Uygulandığı yer: <yeni kod / dokunulan kod> · İstisnalar: <nasıl kaydedilir>

## Bu Standartların Değiştirilmesi
- ...

## Açık Kararlar
- [ÖNERİ] ...
```

## Kalite kontrol listesi
- [ ] Her kuralın kimliği, önem derecesi, gerekçesi ve kötü/iyi örneği var.
- [ ] Araçla uygulatılabilen her şey düzyazı yerine araca devredildi.
- [ ] Kurallar birbiriyle veya seçilen temel rehberle çelişmiyor.
- [ ] Her Zorunlu kuralın hafıza dışında bir uygulatma mekanizması var.
- [ ] Üzerinde uzlaşılmamış, çıkarım yapılmış kurallar `[ÖNERİ]` olarak işaretli ve açık kararlarda yer alıyor.
- [ ] Doküman yaklaşık on dakikada okunacak kadar kısa.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Biçimlendirme üzerine uzun bir stil kılavuzu yazmak. Formatter bunu bedavaya çözer; kelimeleri tasarım ve hata yönetimi kurallarına harca.
- Gerekçesiz kurallar ("X kullanma"). İnsanlar gerekçeleri takip eder ve gerekçeler öngörülmeyen durumlarda karar vermeye yardım eder.
- Mevcut kod tabanının her yerde ihlal ettiği ve benimseme planı olmayan standartlar; birkaç hafta içinde görmezden gelinir.

## Örnek
Girdi: "Backend ekibi, exception, isimlendirme ve PR boyutu tartışmaları."

Zayıf kural: "Exception'ları düzgün yönet."

Güçlü kural:
### ERR-2 Exception'ı ele alamıyor veya bağlam ekleyemiyorsan yakalama (Zorunlu)
Neden: yutulan veya bağlam eklenmeden yeniden sarılan exception'lar kök nedeni gizler ve alarmları bozar.
Kötü:
    try { charge(order) } catch (e) { log.warn("error") }
İyi:
    try { charge(order) } catch (e: GatewayTimeout) { throw PaymentFailed(orderId = order.id, cause = e) }
Uygulatma: boş veya yalnızca log yazan catch blokları için statik analiz kuralı; bağlam için inceleme.
