---
name: retrospective-facilitation
description: "Bir ekip retrospektifini baştan sona planlar ve yürütür: ortamı hazırlar, veri toplar, içgörü üretir, not al ve oyla yöntemiyle yakınsar, az sayıda sahipli ve doğrulanabilir iyileştirme aksiyonu çıkarır ve önceki aksiyonları takip eder. Retrospektif zamanı geldiğinde, retro panosu notları paylaşılıp aksiyon istendiğinde veya geçmiş retroların aksiyonları hiç hayata geçmediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: agile-delivery
  area: ceremonies
  title: "Retrospektif kolaylaştırma"
  related: "retrospective-format, team-health-check, working-agreement, five-whys, impediment-tracking"
  prompt: "Sprint retromuzu yürüt: 7 kişilik uzaktan ekip, 60 dakika. Geçen sprint iki üretim olayı ve çok fazla bağlam değiştirme yaşandı. Önceki retro aksiyonları: incelemelerde eşli çalışma (yapılmadı), kararsız testleri düzeltme (yapıldı)."
---

# Retrospektif Kolaylaştırma

## Amaç
Ekibin nasıl çalıştığını incelemesine ve güvenli, odaklı ve zaman kutulu bir oturum sonunda gerçekten uygulayacağı bir ila üç iyileştirme aksiyonuyla ayrılmasına yardımcı olmak.

## Ne zaman kullanılır
- Düzenli bir iterasyon veya kilometre taşı retrospektifinin zamanı geldi.
- Ham retro panosu notları var ve kümelenmesi, önceliklendirilmesi ve aksiyona dönüştürülmesi gerekiyor.
- Retro aksiyonları sürekli unutuluyor ve döngünün kapatılması gerekiyor.

## Ne zaman kullanılmaz
- Yalnızca yeni veya temalı bir format tasarlamak için `retrospective-format` kullanılır.
- Kurum geneline yönelik proje sonu değerlendirmesi için `lessons-learned` kullanılır.
- Belirli bir olayın suçlamasız analizi için `postmortem` kullanılır.

## Girdiler
Zorunlu:
- Bağlam: ekip büyüklüğü, uzaktan/yerinde, ayrılan süre ve değerlendirilen dönem.

İsteğe bağlı, kaliteyi artırır:
- Dönemin dikkat çeken olayları (olaylar, sürümler, ekip değişiklikleri, metrikler).
- Önceki retro aksiyonları ve durumları.
- Retro zaten yapıldıysa ham notlar.
- Ekip sağlığı veya ruh hali sinyalleri.

Bağlam eksikse en fazla 3 soru sor. Ham notlar verildiyse zaten gerçekleşmiş planlama adımlarını atla.

## Süreç
1. Önce önceki aksiyonları gözden geçir: yapıldı, kısmen yapıldı, bırakıldı. Bırakılanlar için nedenini sor; sessizce yeniden ekleme.
2. Beş aşamalı bir yapı seç: ortamı hazırla, veri topla, içgörü üret, ne yapılacağına karar ver, kapanış. Süreyi dağıt (ör. 60 dakika için 5/15/15/15/10). Özel bir format gerekiyorsa `retrospective-format` üzerinden seç.
3. Ortamı hazırla: odağı belirt ve ekibe temel yönergeyi (prime directive) veya eşdeğer bir güven cümlesini hatırlat; hızlı bir giriş turu planla (tek kelime, 1-5 ölçeği). Uzaktan ekipler için anonim girdi planla.
4. Veri topla: önce sessiz yazma (5-7 dakika), sonra okuma; tartışmanın hafızaya değil olgulara dayanması için dönemin olaylarından bir zaman çizelgesi ekle.
5. İçgörü üret: notları kümele, her kümeye ad ver, ardından nokta oylamasıyla (kişi başı 3 oy) en üstteki 1-2 kümeyi seç. En üst küme için nedenleri 5 neden veya hızlı bir balık kılçığıyla araştır; büyük ekiplerde 2-3 kişilik küçük gruplara ayır.
6. Aksiyonlara karar ver: en fazla üç tane; her biri somut, adı belli bir sahibi olan, bir bitiş tarihi veya sonraki iterasyonu ve gerçekleştiğini doğrulama yolu olan. Kalıcı kurallar yerine deneyleri ("sonraki iki iterasyon boyunca şunu yapacağız...") tercih et.
7. Ekibin kontrolündeki aksiyonları kontrolü dışındaki konulardan ayır; ikinciler sahibi olan eskalasyonlara dönüşür.
8. Kapanış: harcanan zamanın getirisi oylaması veya tek cümlelik teşekkür; aksiyonların nerede izleneceğini (backlog veya pano) teyit et.
9. Kaydı yaz; bireysel alıntıları anonimleştir, problem tanımlarında isim kullanma.
10. Kullanıcının hedefi devam ediyorsa aksiyonlar ekip normlarını değiştiriyorsa `working-agreement`, daha geniş trendler için `team-health-check`, eskalasyonlar için `impediment-tracking` öner.

## Çıktı formatı
```markdown
# Retrospektif – <ekip>, <dönem>, <tarih>
Format: <ad> · Süre: <dk> · Katılımcı: <n>

## Önceki Aksiyonlar
| Aksiyon | Durum | Not |
|---|---|---|

## Gündem
| Aşama | Etkinlik | Dakika |
|---|---|---|

## Veri ve İçgörüler
- Zaman çizelgesinden öne çıkanlar: ...
- Üst kümeler (oy): <küme> (<n>), <küme> (<n>)
- Üst kümenin kök nedeni: ... [ekip belirtmediyse ÇIKARIM]

## Aksiyonlar
| # | Aksiyon (deney) | Sahip | Bitiş | Nasıl doğrulanır |
|---|---|---|---|---|

## Eskalasyonlar (ekip kontrolü dışında)
- <konu> – <kime eskale edildi> – <sahip>

## Kapanış
- ...
```

## Kalite kontrol listesi
- [ ] Yeni veri toplanmadan önce önceki aksiyonlar gözden geçirildi.
- [ ] En fazla üç yeni aksiyon var ve her birinin sahibi, bitişi ve doğrulaması belli.
- [ ] Aksiyonlar en yüksek sesli görüşü değil, en çok oy alan kümeleri ele alıyor.
- [ ] Ekip kontrolü dışındaki konular ekip aksiyonu değil, eskalasyon olarak yazıldı.
- [ ] Kayıt suçlama veya kişiye atfedilebilir alıntı içermiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- On tane belirsiz aksiyonla ("daha iyi iletişim kuralım") bitirmek. Az sayıda seç, somut ve doğrulanabilir yap.
- Veri toplama sırasında çözüme atlamak. Aşamaları ayrı tut; yakınsama kümeleme ve oylamadan sonra olur.
- Her seferinde aynı formatı kullanmak. Enerji düştüğünde formatı değiştir, bkz. `retrospective-format`.
- Yöneticinin tartışmaya hakim olmasına izin vermek. Herkesin sesi duyulsun diye sessiz yazma ve anonim girdi kullan.

## Örnek
Girdi: "7 kişilik uzaktan ekip, 60 dk. İki üretim olayı, çok fazla bağlam değiştirme. Önceki aksiyonlar: incelemelerde eşli çalışma (yapılmadı), kararsız testleri düzeltme (yapıldı)."

Çıktıdan bir bölüm:
- Önceki: "İncelemelerde eşli çalışma" – yapılmadı – ekip zaman ayrılmadığını söylüyor; tartış, otomatik yeniden ekleme.
- Zayıf aksiyon: "Bağlam değiştirmeyi azaltalım."
- Güçlü aksiyon: "Sonraki 2 iterasyon boyunca dönüşümlü bir kişi tüm destek taleplerine bakar; diğerleri 15:00'e kadar destek kanalını takip etmez. Sahip: Deniz. Doğrulama: bir sonraki retroda kişi başı kaydedilen kesinti sayısı."
