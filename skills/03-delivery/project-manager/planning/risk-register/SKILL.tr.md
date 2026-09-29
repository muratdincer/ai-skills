---
name: risk-register
description: "Neden-olay-etki biçiminde risk ifadeleri, olasılık ve etki puanları, yakınlık, sahipler, aksiyon ve tetikleyicileriyle yanıt stratejileri (kaçın, azalt, devret, kabul et, fırsatı kullan) ve kalıntı risk içeren proje risk kaydını oluşturur. Proje planlanırken, bir geçiş kapısı veya yönlendirme toplantısı öncesinde ya da yeni tehdit veya fırsatlar ortaya çıktığında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: planning
  title: "Risk kaydı"
  related: "raid-log, pre-mortem, technical-risk-review, it-risk-assessment, budget-plan"
  prompt: "Depo yönetim sistemi geçişimiz için risk kaydı oluştur; plan ve açılış toplantısında dile getirilen kaygılar ekte."
---

# Risk Kaydı

## Amaç
Hedefleri etkileyebilecek belirsiz olayları açık, önceliklendirilmiş ve sahipli hale getirmek ve somut yanıtlar tanımlamak; böylece riskler sorun olmadan önce yönetilir.

## Ne zaman kullanılır
- Planlama sırasında risk kaydının baz çizgisini oluşturmak için.
- Geçiş kapıları, yönlendirme toplantıları veya büyük sürümler öncesinde.
- Yeni bilgiler (tedarikçi sorunları, mevzuat değişikliği, kilit kişinin ayrılması) risk profilini değiştirdiğinde.

## Ne zaman kullanılmaz
- Riskleri varsayım, sorun ve bağımlılıklarla birlikte tek bir hafif kayıtta izlemek için `raid-log` kullanılır.
- Ekiple yapılandırılmış bir başarısızlık beyin fırtınası için önce `pre-mortem` kullanılır, sonra bu kayıt beslenir.
- Kurumsal BT veya bilgi güvenliği risk değerlendirmesi için `it-risk-assessment` kullanılır.

## Girdiler
Zorunlu:
- Proje bağlamı (başlatma belgesi, kapsam veya plan özeti).

İsteğe bağlı, kaliteyi artırır:
- Mevcut kaygılar, benzer projelerden alınan dersler, kurumsal risk ölçekleri ve risk iştahı.
- Etkiyi sayısallaştırmak için takvim ve bütçe.

Bağlam yoksa proje özetini iste. Verilmişse kurumsal ölçekleri kullan; yoksa çıktıda tanımlanan 1-5 ölçeğini kullan.

## Süreç
1. Riskleri kategoriye göre topla: kapsam/gereksinim, takvim, maliyet, kaynak, teknoloji, veri, tedarikçi, organizasyonel değişim, mevzuat, güvenlik, operasyon.
2. Her riski "<neden> nedeniyle <belirsiz olay> gerçekleşebilir ve <hedefe etki> doğurur" biçiminde yaz. "Kaynaklar" gibi belirsiz girdileri kabul etme.
3. Riskleri sorunlardan (zaten gerçekleşmiş) ve varsayımlardan ayır; bunları ilgili kayda taşı.
4. Olasılık ve etkiyi (1-5) tanımlı çıpalarla puanla; etkiyi baskın hedefe (zaman, maliyet, kapsam, kalite) göre puanla ve hangisi olduğunu belirt.
5. Yakınlığı (riskin ne zaman gerçekleşebileceği) ve erken uyarı tetikleyicilerini ekle.
6. Puana ve yakınlığa göre sırala; ilk 10'u belirle.
7. Her risk için yanıt stratejisi seç: tehditler (kaçın, azalt, devret, kabul et), fırsatlar (kullan, güçlendir, paylaş, kabul et). Sahip ve tarihle somut aksiyonlar tanımla.
8. Yanıt sonrası kalıntı puanı tahmin et; kalıntısı yüksek riskler için geri dönüş (fallback) planları tanımla.
9. Bütçe elveriyorsa yedek payı boyutlandırmak için beklenen parasal değeri (olasılık × maliyet etkisi) hesapla; maliyet etkisini asla uydurma.
10. Gözden geçirme sıklığını ve kapanış kriterlerini belirle.
11. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: sürekli takip için `raid-log` ya da ekibin henüz adlandırmadığı riskleri ortaya çıkarmak için `pre-mortem`.

## Çıktı formatı
```markdown
# Risk Kaydı: <proje>
Ölçek: O ve E 1-5 (çıpalar aşağıda) | Gözden geçirme sıklığı <x>
| No | Risk ifadesi (neden → olay → etki) | Kategori | O | E | Puan | Yakınlık | Tetikleyici | Strateji | Aksiyonlar (sahip, tarih) | Kalıntı | Durum |
|---|---|---|---|---|---|---|---|---|---|---|---|
## Öncelikli Riskler Özeti
## Ölçek Çıpaları
| Puan | Olasılık | Takvime etki | Maliyete etki |
## Yedek Pay Bağlantısı (kullanılıyorsa BPD)
## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her risk neden-olay-etki yapısında ve gelecekteki belirsiz bir olay.
- [ ] Her riskin tek bir sahibi ve en az bir tarihli aksiyonu ya da açık bir kabul kararı var.
- [ ] Ölçekler tanımlı; puanlar tutarlı.
- [ ] Yalnızca tehditler değil fırsatlar da değerlendirildi.
- [ ] Hiçbir etki değeri uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her projeye uyan genel riskler listelemek. Bu bağlama özgü yaz.
- Riski etkileyemeyen sahipler atamak. Harekete geçme yetkisi olan birini ata.
- Kaydı bir kez gözden geçirilen bir uyum belgesi gibi görmek. Gözden geçirmeleri raporlama döngüsüne bağla.

## Örnek
Girdi: "Depo yönetim sistemi geçişi; tedarikçi ERP'mizle hiç entegrasyon yapmadı; yoğun sezon Kasım'da başlıyor."

Çıktıdan bir bölüm:
| R-02 | Tedarikçinin ERP'mizle önceki entegrasyon deneyimi olmadığı için arayüz hataları testte geç ortaya çıkabilir ve canlıya geçişi yoğun sezon öncesi dondurma döneminin ötesine kaydırabilir | Teknoloji | 4 | 5 | 20 | Entegrasyon testi fazı | SIT ortasında >10 açık arayüz hatası | Azalt | A2'ye kadar erken arayüz prototipi (Entegrasyon sorumlusu) | 12 | Açık |
