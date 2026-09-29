---
description: Toplantı notları, dökümler, e-postalar veya sohbet akışlarındaki tüm açık ve örtük taahhütleri bulur ve her birini tek bir sorumlusu, tarihi, durumu ve kaynak atfı olan doğrulanabilir bir aksiyona dönüştürür; sorumlusu veya tarihi eksik olanları işaretler. "Aksiyonlar neler?", "kim ne yapacak?" sorulduğunda ya da bir toplantı veya tartışma sonrasında takip aracına hazır işler gerektiğinde kullanılır.
related: meeting-notes, meeting-follow-up, open-questions-tracker, decision-log, task-breakdown
prompt: Sürüm hazırlık görüşmemizin dökümündeki tüm aksiyonları çıkar ve bir tabloya koy.
---

# Aksiyon Maddelerini Çıkarma

## Amaç
Bir görüşmede verilen hiçbir taahhüdün kaybolmamasını sağlamak; her birini net, sahibi belli, tarihli ve takip edilebilir bir işe dönüştürmek.

## Ne zaman kullanılır
- Bir toplantı, çalıştay, olay görüşmesi veya uzun sohbet/e-posta akışından sonra.
- Notlar var ama aksiyonlar tartışmanın içinde kaybolmuşsa.
- Aksiyonlar bir iş takip aracına veya takip mesajına aktarılacaksa.

## Ne zaman kullanılmaz
- Toplantının tam yapılandırılmış kaydı gerekiyorsa `meeting-notes` kullanılır.
- Takip edilmesi gereken işler değil çözülmemiş sorularsa `open-questions-tracker` kullanılır.
- Bir özellik mühendislik görevlerine bölünecekse `task-breakdown` kullanılır.

## Girdiler
Zorunlu:
- Kaynak metin (notlar, döküm, yazışma).

İsteğe bağlı:
- Toplantı tarihi ("gelecek cuma" gibi göreli tarihleri çözmek için), katılımcı listesi ve roller, güncellenecek mevcut aksiyon listesi.

Toplantı tarihi yoksa göreli tarihleri yazıldığı gibi bırak ve `[tarihi teyit et]` olarak işaretle.

## Süreç
1. Taahhüt sinyallerini tara: "yapacağım", "yaparız", "bakabilir misin", "hadi şunu", "X, Y'yi yapsın", "cumaya kadar", "dönüş yaparım", "gönder", "kontrol et", "sor", "hazırla" ve kararlardaki mutabık kalınan sonraki adımlar.
2. Bir karardan doğrudan çıkan örtük aksiyonları da ekle ("B tedarikçisiyle devam" kararı, "A tedarikçisini bilgilendir" aksiyonunu doğurur) ve `[ÖRTÜK]` olarak işaretle.
3. Her birini fiille başlayan, tamamlanma durumu net, doğrulanabilir bir iş olarak yeniden yaz ("Revize tahmini Finans'a gönder", "tahmin" değil).
4. Tam olarak bir sorumlu ata. Kaynak bir grup adı veriyorsa belirtilmiş lideri seç, yoksa `[SORUMLU BİLİNMİYOR]` yaz. Asla tahminle atama.
5. Toplantı tarihi biliniyorsa tarihleri takvim tarihine çevir; bilinmiyorsa ifadeyi koru ve işaretle.
6. Durumu belirle: Açık, Devam ediyor, Tamamlandı (toplantıda bittiyse), Engelli (engeliyle birlikte).
7. Aksiyonlar arası bağımlılıkları kaydet ve her birini kaynağına bağla (konu, zaman damgası veya alıntı).
8. Tekrarları birleştir, bileşik aksiyonları ("Ali ve Zeynep inceleyip deploy edecek") ayrı maddelere böl.
9. Aslında soru veya risk olan maddeleri ayır ve tablonun altında listele.
10. Eksikleri özetle: takip mesajında çözülmesi gereken sorumlusuz veya tarihsiz aksiyon sayısı.
11. Kullanıcının hedefi devam ediyorsa aksiyonları paylaşmak için `meeting-follow-up`, taahhüt olmayan sorular için `open-questions-tracker`, tek maddede bitmeyecek kadar büyük aksiyonlar için `task-breakdown` öner.

## Çıktı formatı
```markdown
# Aksiyonlar – <toplantı/yazışma>, <tarih>
| # | Aksiyon (fiille başlar) | Sorumlu | Tarih | Durum | Bağımlılık | Kaynak |
|---|---|---|---|---|---|---|
| A1 | ... | ... | YYYY-AA-GG | Açık | – | <konu/zaman damgası> |

Örtük aksiyonlar: <[ÖRTÜK] işaretli numaralar>
Eksikler: <n> sorumlusuz, <n> tarihsiz
Aksiyon olmayanlar (sorulara/risklere taşı):
- ...
```

## Kalite kontrol listesi
- [ ] Kaynaktaki her taahhüt yakalandı, örtük olanlar dahil (işaretli).
- [ ] Her aksiyon fiille başlıyor ve tamamlanma durumu net.
- [ ] Her aksiyonun tam olarak bir sorumlusu veya `[SORUMLU BİLİNMİYOR]` işareti var.
- [ ] Göreli tarihler çözüldü veya işaretlendi.
- [ ] Sorular ve riskler aksiyon kılığına sokulmadı.
- [ ] Her aksiyon kaynağına bağlı.
- [ ] Girdide söylenmeyen her şey `[VARSAYIM]` olarak işaretlendi veya açık soru olarak listelendi; olgu gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Ekip"i veya iki kişiyi sorumlu yazmak. Hesap verebilirlik tek bir isim gerektirir.
- Yumuşak taahhütleri kaçırmak ("bir bakarım"). Bunlar da aksiyondur; yakala ve takip mesajında teyit et.
- Tartışmada ortaya atılan fikirleri mutabık kalınmış aksiyon saymak. Yalnızca birinin üstlendiği veya kendisinden istenip kabul ettiği işleri ekle.

## Örnek
Girdi: "Burak: Perşembeden önce rollback betiğine bakarım. Çarşambadan itibaren merge dondurma kararı aldık. Birinin desteğe sürüm penceresini söylemesi lazım."

Çıktıdan bir bölüm:
| A1 | Rollback betiğini staging'de doğrula | Burak | Perş `[tarihi teyit et]` | Açık | – | Rollback konusu |
| A2 | Çarşambadan itibaren merge dondurmayı tüm geliştiricilere duyur `[ÖRTÜK]` | [SORUMLU BİLİNMİYOR] | Çarş. öncesi | Açık | – | Dondurma kararı |
| A3 | Destek ekibini sürüm penceresi hakkında bilgilendir | [SORUMLU BİLİNMİYOR] | [BİLİNMİYOR] | Açık | – | "Birinin desteğe söylemesi lazım" |
