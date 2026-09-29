---
name: defect-trend-analysis
description: "Hata verisini zaman içinde analiz ederek yoğunluk, kaçak hata (leakage) oranı, yeniden açılma oranı, yaşlanma ve kök neden kategorilerini ortaya koyar; gerçek kalite sinyalini raporlama gürültüsünden ayırır ve kanıta dayalı iyileştirme aksiyonlarıyla bitirir. Ekip kalitenin neden düştüğünü sorduğunda, retrospektif veya kalite değerlendirmesi hazırlanırken, canlıya kaçan hatalar açıklanmak istendiğinde ya da elde bir hata dökümü olup trendlerin yorumlanması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: execution
  title: "Hata trendi analizi"
  related: "bug-triage, test-summary-report, five-whys, engineering-metrics-review, code-quality-report"
  prompt: "Son 6 sürümün hata dökümü ekte. Trendleri analiz et: hatalar nereden geliyor, ne kadarı canlıya kaçıyor, neyi değiştirmeliyiz?"
---

# Hata Trendi Analizi

## Amaç
Hata kayıtlarını az sayıda güvenilir trend bulgusuna (hataların nerede üretildiği, nerede yakalandığı, nerede kaçtığı) ve hedefli iyileştirme aksiyonlarına dönüştürmek. Böylece ekip yalnızca hataları değil, hatayı üreten süreci düzeltir.

## Ne zaman kullanılır
- Kalite değerlendirmesi, retrospektif veya yönlendirme toplantısı için sürümler ya da iterasyonlar boyunca veriye dayalı bir hata görünümü gerektiğinde.
- Canlıya kaçan veya müşterinin bildirdiği hatalar arttığında ve nedeni anlaşılmak istendiğinde.
- Yönetim kalitenin iyileşip iyileşmediğini sorduğunda ve cevabın rakamlarla savunulması gerektiğinde.

## Ne zaman kullanılmaz
- Tek tek hatalar için düzelt/düzeltme kararı gerekiyorsa `bug-triage` kullanılır.
- Tek bir sürümün sonuçları paydaşlara raporlanacaksa `test-summary-report` kullanılır.
- Belirli bir olayın nedensel analizi gerekiyorsa `five-whys` veya `postmortem` kullanılır.

## Girdiler
Zorunlu:
- En az şu alanları içeren hata kayıtları (döküm veya özet): oluşturma tarihi, önem, durum, bileşen/modül ve hatanın bulunduğu aşama veya ortam.

İsteğe bağlı, kaliteyi artırır:
- Kök neden kategorisi, hatanın üretildiği aşama, sürüm/iterasyon etiketi, yeniden açılma sayısı, kapanış tarihi.
- Boyut normalleştiricileri: değişen satır, story point, değişiklik sayısı, koşulan test case sayısı, aktif kullanıcı.
- Ekibin önem tanımları ve dönem içinde yapılan süreç değişiklikleri.

Hata verisi yoksa iste. Boyut normalleştiricisi yoksa yalnızca mutlak sayıları raporla ve yoğunluğun hesaplanamadığını belirt; payda uydurma.

## Süreç
1. Önce veriyi profille: kapsanan dönem, kayıt sayısı, sütun bazında eksik alanlar, mükerrer/reddedilen oranı. Herhangi bir bulgudan önce veri kalitesi sınırlarını yaz.
2. Kategorileri normalleştir (bileşen ve kök nedenlerdeki eş anlamlıları birleştir, önemleri ekip ölçeğine eşle). Çıkarımla yaptığın her eşlemeyi `[VARSAYIM]` olarak kaydet.
3. Sürüm veya dönem bazında temel metrikleri hesapla: gelen ve kapanan hata, açık backlog, yoğunluk (varsa hata / boyut birimi), kaçak oranı (canlıda bulunan ÷ toplam bulunan), yeniden açılma oranı, önem bazında açık hataların medyan yaşı.
4. Aşama tutma (phase containment) görünümü oluştur: üretildiği aşama × bulunduğu aşama (gereksinim, tasarım, kod, entegrasyon, sistem testi, UAT, canlı). Üretildikten iki veya daha fazla aşama sonra bulunan hataları vurgula.
5. Bileşenleri ve kök neden kategorilerini Pareto kesimiyle sırala (hataların çoğunu üreten ~%20'lik kategoriler). Sayıca yüksek kümeleri önemce yüksek kümelerden ayır.
6. Her görünür trendi gürültüye karşı sına: küçük örneklem, değişen raporlama kuralları, büyük bir sürüm, yeni bir testçi veya araç. Trend için aynı yönde en az üç veri noktası gerekir; yoksa izlenecek sinyal olarak adlandır.
7. Bilinen olaylarla (süreç, ekip veya mimari değişikliği) yalnızca kullanıcı bunları verdiyse ilişki kur; her nedensel bağı sonuç değil hipotez olarak etiketle.
8. Her biri tek bir bulguya bağlı 3-5 iyileştirme aksiyonu çıkar: sorumlu rol, beklenen metrik hareketi ve verilmediyse `[TBD]` gözden geçirme tarihi.
9. Etkinin nasıl ölçüleceğini tanımla: hangi metrik, başlangıç değeri, hedef yön, sonraki gözden geçirme noktası.
10. Kullanıcı devam ederse en büyük küme için `five-whys`, test eforunu sıcak bileşenlere odaklamak için `risk-based-testing`, daha geniş teslimat görünümü için `engineering-metrics-review` öner.

## Çıktı formatı
```markdown
# Hata Trendi Analizi: <ürün/ekip>, <dönem>
## Veri Temeli
- Kayıt: <n> | Dönem: <başlangıç–bitiş> | Eksik alanlar: <liste> | Hariç tutulan: <n reddedilen/mükerrer>
- Sınırlar: <neyin sonucuna varılamayacağı>

## Temel Metrikler
| Sürüm/Dönem | Gelen | Kapanan | Açık | Yoğunluk | Kaçak oranı | Yeniden açılma | Medyan yaş (Kritik/Majör) |
|---|---|---|---|---|---|---|---|

## Aşama Tutma
| Üretildiği \ Bulunduğu | Gereksinim | Tasarım | Kod | Entegr. | Sistem | UAT | Canlı |
|---|---|---|---|---|---|---|---|

## Bulgular
1. <bulgu> — kanıt: <rakamlar> — güven: Yüksek/Orta/Düşük — [HİPOTEZ] neden: <...>

## İyileştirme Aksiyonları
| # | Aksiyon | İlgili bulgu | Sorumlu rol | Hareket etmesi beklenen metrik | Gözden geçirme tarihi |
|---|---|---|---|---|---|

## İzleme Listesi (zayıf sinyaller)
- ...

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Veri kalitesi sınırları bulgulardan önce yazıldı.
- [ ] Her bulgu dayandığı rakamları gösteriyor ve bir güven düzeyi taşıyor.
- [ ] Yoğunluk yalnızca gerçek bir boyut normalleştiricisiyle raporlandı; uydurma payda yok.
- [ ] Veri kanıtlamadıkça nedenler hipotez olarak etiketlendi.
- [ ] Her aksiyon bir bulguya ve hareket etmesi gereken bir metriğe bağlı.
- [ ] Hiçbir geliştirici veya testçi isimle anılmadı ya da sıralanmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Artan hata sayısını düşen kalite olarak okumak. Daha fazla test, yeni bir testçi veya daha iyi raporlama da sayıyı artırır; önce eforu ve kapsamı kontrol et.
- Hata metriklerini kişileri sıralamak için kullanmak. Raporlama dürüstlüğünü yok eder; bunun yerine bileşenleri ve süreç adımlarını analiz et.
- İki veri noktasından trend ilan etmek. Örüntü tutana kadar izleme maddesi olarak işaretle.

## Örnek
Girdi: 6 sürümde 412 hata; alanlar: oluşturma tarihi, önem, bileşen, bulunduğu ortam; boyut verisi yok.

Çıktıdan bir bölüm:
- Sınırlar: boyut normalleştiricisi olmadığı için yoğunluk raporlanmadı; kayıtların %9'unda bileşen eksik.
- Bulgu: kaçak oranı 4-6. sürümlerde %6'dan %14'e çıktı; kaçakların %58'i `payments` bileşeninde — güven: Orta. `[HİPOTEZ]` neden: payments entegrasyon testleri 4. sürümde sürüm pipeline'ından çıkarılmış (ekiple teyit et).
- Aksiyon: payments sözleşme testlerini pipeline'a geri al — metrik: `payments` kaçak oranı — 2 sürüm sonra gözden geçir.
