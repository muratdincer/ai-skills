---
name: meeting-agenda
description: "Net bir amaç, beklenen çıktılar, sorumlusu ve süresi belirli gündem maddeleri ve gerekli ön okumalarla zaman planlı bir toplantı gündemi hazırlar. Herhangi bir toplantı, çalıştay veya periyodik oturum planlanırken, tartışma yerine karar üreten yapılandırılmış bir gündem gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: meetings
  area: before
  title: "Toplantı gündemi hazırlama"
  related: "meeting-invite, meeting-necessity-check, facilitation-guide"
  prompt: "Ürün, geliştirme ve test liderleriyle 3. çeyrek sürüm kapsamına karar vereceğimiz 60 dakikalık toplantı için gündem hazırla."
---

# Toplantı Gündemi Hazırlama

## Amaç
Her toplantıya tek bir amaç, somut çıktılar ve gerçekçi bir zaman planı vermek. Böylece katılımcılar hazırlıklı gelir, toplantı sadece konuşmayla değil kararlarla biter.

## Ne zaman kullanılır
- Yeni bir toplantı, çalıştay, değerlendirme veya yönlendirme oturumu planlanırken.
- Periyodik bir toplantı dağılmışsa ve yeniden odaklanması gerekiyorsa.

## Ne zaman kullanılmaz
- Toplantının gerekli olduğundan emin değilsen önce `meeting-necessity-check` kullan.
- Ayrıntılı bir kolaylaştırıcı metnine ihtiyaç varsa `facilitation-guide` kullan.

## Girdiler
Zorunlu:
- Toplantı konusu veya amacı.
- Süre.

İsteğe bağlı:
- Katılımcılar ve rolleri.
- Arka plan materyali, önceki toplantı notları, açık konular.
- Alınması gereken kararlar.

## Süreç
1. Amacı fiille başlayan tek bir cümleyle yaz: karar vermek, uzlaşmak, gözden geçirmek, planlamak, bilgilendirmek, çözmek.
2. 1-3 beklenen çıktı tanımla (örneğin "onaylı kapsam listesi", "her risk için bir sorumlu").
3. Amaca hizmet eden konuları listele. Hizmet etmeyenleri çıkar.
4. Her gündem maddesini isim olarak değil soru veya çıktı olarak yaz ("Q3 özellikleri" yerine "Q3'e hangi 5 özellik girecek?").
5. Her maddeye bir sorumlu ve tür ata: Bilgilendirme, Tartışma, Karar.
6. Süreleri dağıt. Karar maddelerini enerji yüksekken başa koy. %10 tampon ve son 5 dakikayı kapanışa (kararlar, aksiyonlar, sonraki adımlar) ayır.
7. Toplamı süreyle karşılaştır. Taşıyorsa maddeleri kes veya asenkron yürütülecek şekilde dışarı al.
8. Ön okumaları ve katılımcıların hazırlaması gerekenleri listele.
9. Rolleri belirle: kolaylaştırıcı, not tutan, zaman tutan.
10. Kullanıcının hedefi devam ediyorsa gündemi göndermek için `meeting-invite`, oturum bir yönetim metni gerektiriyorsa `facilitation-guide` öner.

## Çıktı formatı
```markdown
# <Toplantı başlığı>
**Amaç:** <tek cümle>
**Beklenen çıktılar:** <1-3 madde>
**Tarih / Süre:** <...>  **Kolaylaştırıcı:** <...>  **Not tutan:** <...>
**Katılımcılar:** <ad – rol>

| # | Zaman | Madde (soru/çıktı) | Tür | Sorumlu |
|---|---|---|---|---|
| 1 | 00:00-00:05 | Amaç ve bağlam | Bilgilendirme | ... |
| ... | | | | |
| n | son 5 dk | Kapanış: kararlar, aksiyonlar, sonraki adımlar | Karar | Kolaylaştırıcı |

**Ön okuma / hazırlık:** <bağlantılar, getirilecekler>
**Park alanı:** kapsam dışı kalan konular buraya yazılır
```

## Kalite kontrol listesi
- [ ] Amaç, eylem fiili içeren tek bir cümle.
- [ ] Her maddenin türü, sorumlusu ve süresi var.
- [ ] Toplam süre, tampon dahil toplantı süresine sığıyor.
- [ ] Karar maddeleri açık ve başta.
- [ ] Sonda kapanışa zaman ayrılmış.
- [ ] Girdide söylenmeyen her şey `[VARSAYIM]` olarak işaretlendi veya açık soru olarak listelendi; olgu gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Gündemin yalnızca isimlerden oluşması; bir maddenin ne zaman "bitmiş" sayılacağı belli olmaz.
- Süreye sığmayacak kadar çok madde koymak.
- Yalnızca bir madde için gereken kişiyi tüm toplantıya çağırmak. Bunun yerine zamanlı bir slot öner.

## Örnek
Amaç: 3. çeyrek sürüm kapsamına karar vermek.
Madde 2 (00:05-00:25, Karar, Ürün Lideri): "8 aday özellikten hangileri 3. çeyrek kapasitesine sığıyor?"
