---
name: change-request-analysis
description: "Bir değişiklik talebini üzerinde anlaşılmış temel sürüme (baseline) göre analiz eder: talebi sınıflandırır (yeni kapsam, değişiklik, netleştirme, kılık değiştirmiş hata), değer, kapsam, efor sürücüleri, zaman, maliyet ve risk etkisini değerlendirir, seçenekleri listeler ve değişiklik otoritesi için gerekçeli kabul, ödünleşimli kabul, erteleme veya ret önerir. Gereksinimler onaylandıktan sonra veya teslimat sırasında bir paydaş ekleme ya da değişiklik istediğinde veya bir değişiklik kontrol kurulu karar dokümanı beklediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: solution
  title: "Değişiklik talebi analizi"
  related: "impact-analysis, change-control, change-request-rfc, requirements-sign-off, trade-off-analysis"
  prompt: "Pazarlama, canlıya geçişe iki hafta kala sadakat sürümüne SMS bildirimi eklemek istiyor. Değişiklik talebini analiz et ve öneri ver."
---

# Değişiklik Talebi Analizi

## Amaç
Değişiklik otoritesine, istenen değişiklik için açık ve kanıta dayalı bir karar dokümanı sunmak: ne olduğu, neden önemli olduğu, kapsam, zaman ve risk açısından neye mal olduğu ve seçeneklerin neler olduğu. Böylece kapsam değişiklikleri sessizce değil bilinçli olarak yapılır.

## Ne zaman kullanılır
- Bir paydaş temel sürümden sonra bir gereksinim eklemek, değiştirmek veya çıkarmak istediğinde.
- Bir değişiklik kontrol kurulu veya sponsor bir değişiklik hakkında karar verecekse.
- Teslimatın sonlarında bir "küçük düzeltme" geldiğinde ve gerçek büyüklüğü belirsizse.

## Ne zaman kullanılmaz
- Değişiklik operasyoneldir (canlıya dağıtım, altyapı değişikliği); bu durumda `change-request-rfc` kullanılır.
- Karar olmadan yalnızca etkilenen kalemlerin listesi gerekiyorsa `impact-analysis` kullanılır.
- Projenin değişiklik kontrol prosedürü tanımlanıyorsa `change-control` kullanılır.

## Girdiler
Zorunlu:
- Değişiklik talebinin iletildiği hali (metin, kayıt, e-posta).
- Mevcut temel sürüm veya üzerinde anlaşılanların tarifi (kapsam, tarihler).

İsteğe bağlı, kaliteyi artırır:
- Etki analizi sonuçları, güncel plan ve kapasite, kalan yedek (contingency).
- Değişikliklere ilişkin sözleşme maddeleri (dış teslimatsa), karar yetkisi ve eşikler.

Temel sürüm bilinmiyorsa analizin değişikliği asıl kapsamdan ayıramayacağını belirt ve iste; varsayım yapma.

## Süreç
1. Talebi yeniden ifade et: talep sahibi, sözlü/yazılı istek, altta yatan ihtiyaç (arkasındaki problem) ve neden şimdi. Çıkarımları işaretle.
2. Sınıflandır: yeni kapsam, anlaşılmış kapsamda değişiklik, mevcut kapsamın netleştirilmesi (değişiklik yok), hata (temel sürüm karşılanmamış) veya yasal/zorunlu. Netleştirmeler ve hatalar yeni kapsam olarak değişiklik onayından geçmez.
3. Temel sürümle karşılaştır: etkilenen gereksinim ID'lerini veya kapsam kalemlerini belirt, eski ile istenen durumu yaz.
4. Değer ve aciliyeti değerlendir: hangi hedefe hizmet ettiği, yapmamanın maliyeti, şimdi yerine sonra yapmanın maliyeti.
5. Etkiyi değerlendir: bir etki analizini kullan veya özetle (süreçler, sistemler, veri, raporlar, testler, dokümanlar); efor sürücülerini adlandır. Yalnızca verilen tahminleri kullan; yoksa göreli büyüklüğü tarif et ve `[VARSAYIM]` olarak işaretle.
6. Zaman, maliyet ve kalite etkisini değerlendir: kritik yol ve yayın tarihine etkisi, bütçe veya yedek tüketimi, özellikle canlıya yakınken test ve stabilizasyon riski.
7. Yapmanın ve yapmamanın risklerini belirle.
8. Seçenekleri oluştur: olduğu gibi kabul; ödünleşimli kabul (eşit büyüklükte bir kalemi çıkar veya ertele); sonraki sürümde kabul; küçültülmüş sürümü kabul; ret.
9. Gerekçesi ve koşullarıyla tek bir seçenek öner; karar otoritesini ve kararın gerektiği tarihi belirt.
10. Onaylanırsa neyin güncellenmesi gerektiğini listele: temel sürüm, plan, izlenebilirlik, test kapsamı, sözleşme, iletişim.
11. Kullanıcı devam etmek isterse daha derin etki görünümü için `impact-analysis`, seçenekleri karşılaştırmak için `trade-off-analysis` veya onay sonrası yeni temel sürüm için `requirements-sign-off` öner.

## Çıktı formatı
```markdown
# Değişiklik Talebi Analizi: <DT No> <başlık>
Talep sahibi: <...> · Tarih: <tarih> · Karar otoritesi: <...> · Karar gereken tarih: <tarih veya [BİLİNMİYOR]>

## Talep
- İstenen: ...
- Altta yatan ihtiyaç: ... [çıkarım mı?]
- Sınıf: <yeni kapsam / değişiklik / netleştirme / hata / zorunlu>
- Etkilenen temel sürüm kalemleri: <ID'ler> (eski → istenen)

## Değerlendirme
| Boyut | Değerlendirme | Kanıt / dayanak |
|---|---|---|
| Değer ve aciliyet | | |
| Kapsam ve efor sürücüleri | | |
| Zaman | | |
| Maliyet / yedek | | |
| Kalite ve risk | | |

## Seçenekler
| Seçenek | Açıklama | Artıları | Eksileri |
|---|---|---|---|

## Öneri
<seçenek> – <gerekçe> – <koşullar>

## Onaylanırsa Güncellenecekler
- ...
```

## Kalite kontrol listesi
- [ ] Talep sınıflandırıldı; netleştirmeler veya hatalar yeni kapsam olarak ele alınmadı.
- [ ] Temel sürüm kalemlerine atıf yapıldı, fark açık.
- [ ] Efor, maliyet ve zaman rakamları girdiden geliyor ya da `[VARSAYIM]` olarak işaretli.
- [ ] Yalnızca kabul/ret değil, en az bir ödünleşim veya erteleme seçeneği sunuldu.
- [ ] Değişikliği yapmanın riskinin yanında yapmamanın riski de belirtildi.
- [ ] Karar otoritesi ve karar gereken tarih adlandırıldı ya da `[BİLİNMİYOR]` olarak işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Küçük" değişiklikleri analizsiz kabul etmek. Geç gelen değişikliklerin test ve stabilizasyon maliyeti geliştirme eforunun çok üstündedir.
- İhtiyacı değil istenen çözümü analiz etmek. Çoğu zaman daha ucuz bir seçenek aynı ihtiyacı karşılar.
- Ödünleşim olmadan öneri yapmak. Kapasite sabitse başka bir şeyin kayması gerekir; neyin kayacağını söyle.

## Örnek
Girdi: "Pazarlama, canlıya 2 hafta kala sadakat sürümüne SMS bildirimi istiyor."

Çıktıdan bir bölüm:
- Sınıf: Yeni kapsam (temel sürümde SMS gereksinimi yok; REQ-12 yalnızca e-postayı kapsıyor).
- Altta yatan ihtiyaç `[çıkarım]`: lansman kampanyasından önce e-posta izni olmayan üyelere ulaşmak.
- Zaman: SMS ağ geçidi entegrasyonu, izin yönetimi (KVKK/GDPR) ve regresyon gerektiriyor; kalan 2 haftayı aşıyor `[VARSAYIM]`.
- Öneri: Sonraki sürümde kabul; lansman için e-posta izni olmayan üyelere uygulama içi banner kullan.
