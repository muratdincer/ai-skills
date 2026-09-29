---
name: goal-setting
description: "Bir mühendis veya ekip üyesi için ekip sonuçlarını kişinin gelişimiyle birleştiren, ölçüt, ara hedef ve gereken destekle birlikte 3-5 SMART bireysel hedef taslağı hazırlar. Değerlendirme döneminin başında, terfi veya rol değişikliğinden sonra ya da hedefler belirsiz, aktivite odaklı veya ekip öncelikleriyle bağlantısız olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: people
  title: "Bireysel hedef belirleme"
  related: "okr-definition, performance-review, career-development-plan, career-ladder, one-on-one-prep"
  prompt: "Orta seviye backend mühendisi Deniz için ikinci yarı hedeflerini belirlememe yardım et. Ekip OKR'ı ödeme adımındaki gecikmeyi azaltmak, o da kıdemli seviyeye ilerlemek istiyor."
---

# Bireysel Hedef Belirleme

## Amaç
Kişiye, şekillendirilmesine kendisinin de katkı verdiği, ölçülebilir, etki alanı içinde olan ve ekip sonuçlarıyla ve kendi gelişimiyle açıkça bağlantılı az sayıda hedef vermek.

## Ne zaman kullanılır
- Yeni bir değerlendirme dönemi veya hedef belirleme döngüsü başladığında.
- Birinin rolü, seviyesi veya ekibi değiştiğinde.
- Mevcut hedefler iş listesi gibiyse ("X kaydını bitir") veya dönem sonunda değerlendirilemiyorsa.

## Ne zaman kullanılmaz
- Ekip veya şirket seviyesindeki hedefler için `okr-definition` kullanılır.
- Seviyeler boyunca uzun vadeli gelişim yol haritası için `career-development-plan` kullanılır.
- Resmi iyileştirme süreci içindeki hedefler için `underperformance-plan` kullanılır.

## Girdiler
Zorunlu:
- Kişinin rolü ve seviyesi, hedef dönemi ve ekibin o dönemdeki öncelikleri veya hedefleri.

İsteğe bağlı, kaliteyi artırır:
- Kişinin kendi hedefleri ve kendisinin belirlediği gelişim alanları.
- Mevcut ve bir sonraki seviyenin kariyer basamağı beklentileri.
- Son değerlendirmedeki odak alanları; bilinen kapasite sınırları (nöbet, izin, yarı zamanlı çalışma).

Ekip öncelikleri yoksa sor; onlarsız hedefler aktivite listesine dönüşür.

## Süreç
1. Dönemin ekip sonuçlarını listele ve bu kişinin hangilerini anlamlı ölçüde etkileyebileceğini belirle.
2. Bu sonuçlara bağlı 2-3 etki hedefi yaz. Görevi değil, sonucu ifade et.
3. Kişinin hedeflerinden ve bir sonraki seviye beklentileriyle arasındaki farktan 1-2 gelişim hedefi yaz.
4. Her hedefi SMART yap: belirli, ölçülebilir (metrik veya gözlemlenebilir kanıt), kapasiteye göre ulaşılabilir, ilgili ve tarihli.
5. Sayıyla ölçülemeyen hedefler için gözlemlenebilir kanıt tanımla (ör. "kabul edilen iki tasarım incelemesine liderlik etti").
6. Etki alanını kontrol et: Başarısı çoğunlukla başka ekiplere veya şansa bağlı hedefleri çıkar ya da yeniden yaz.
7. Ara hedefler (ör. dönem ortası kontrol noktası) ve yöneticinin taahhüt ettiği desteği (erişim, zaman, mentorluk, bütçe) ekle.
8. Seti dengele: en fazla beş hedef, açıkça belirtilmiş en fazla bir iddialı (stretch) hedef.
9. Adaleti kontrol et: Aynı seviyedeki ekip arkadaşlarıyla karşılaştırılabilir kapsam ve zorluk; yarı zamanlı çalışma veya planlı izin için kapasite ayarlanır ama seviye çıtası düşürülmez.
10. Kişinin henüz onaylamadığı önerilen değerleri `[VARSAYIM]` olarak işaretle ve birlikte netleştirmeyi planla.
11. Kullanıcının hedefi devam ediyorsa gelişim hedefleri için `career-development-plan` veya dönem sonunda değerlendirme için `performance-review` öner.

## Çıktı formatı
```markdown
# Hedefler: <ad> – <dönem>
Rol / seviye: <rol, seviye> · Bağlı ekip hedefleri: <liste>

| # | Hedef (sonuç) | Tür | Ölçüt / kanıt | Hedef değer ve tarih | Ara hedef | Yöneticiden destek |
|---|---|---|---|---|---|---|
| 1 | ... | Etki / Gelişim / İddialı | ... | ... | ... | ... |

## Ekip Sonuçlarıyla Bağlantı
- Hedef 1 → <ekip hedefi>

## Gelişimle Bağlantı
- Hedef <n> → <basamak beklentisi veya kişisel hedef>

## Varsayımlar ve Açık Noktalar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] 3-5 hedef var ve her biri görev değil, sonuç olarak yazıldı.
- [ ] Her hedefin ölçütü veya gözlemlenebilir kanıtı ve tarihi var.
- [ ] Başarı büyük ölçüde kişinin etki alanında.
- [ ] En az bir hedef kişinin belirttiği gelişim hedefini destekliyor.
- [ ] Yöneticinin taahhütleri listelendi.
- [ ] Hedeflerin kapsamı aynı seviyedeki ekip arkadaşlarıyla karşılaştırılabilir.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kolayca manipüle edilebilen çıktı metrikleri (PR sayısı, story point). Sonuçları veya kanıtın niteliğini tercih et.
- Hedefleri kişiyle birlikte değil, kişi için belirlemek. Taslakları tartışılacak öneriler olarak sun.
- Değişen bir ortamda sabit hedefler. Dönem ortası gözden geçirme planla ve değişiklikleri kaydet.

## Örnek
Girdi: "Deniz, orta seviye backend. Ekip OKR'ı: ödeme adımı p95 300 ms'nin altında. Kıdemli seviyeye ilerlemek istiyor."

Çıktıdan bir bölüm:
| 1 | Ödeme servisinin checkout p95'ine katkısını azaltmak | Etki | Panodaki ödeme çağrısı p95 değeri | 30 Kasım'a kadar ≤ 120 ms `[VARSAYIM: başlangıç değeri bilinmiyor]` | 15 Eylül'e kadar profil raporu | Ayrılmış performans test ortamı |
| 2 | Yeniden deneme/idempotency değişikliğinin tasarımına liderlik etmek | Gelişim | Mimari incelemede kabul edilen tasarım dokümanı | 31 Ekim'e kadar | Teknik liderle gözden geçirilmiş taslak | Staff mühendisle eşli çalışma |
