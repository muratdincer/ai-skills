---
name: report-requirements
description: "Rapor gereksinimlerini raporun desteklediği karardan başlayarak tanımlar: hedef kitle, cevaplanan sorular, kesin hesaplaması ve granülerliğiyle alanlar ve ölçüler, boyutlar, filtreler ve parametreler, sıralama ve gruplama, veri kaynakları ve güncellik, erişim ve maskeleme, teslim ve format, mutabakat rakamına karşı kabul kontrolleri. Biri yeni bir rapor, dışa aktarım veya liste istediğinde, mevcut bir raporun rakamları tartışmalı olduğunda ya da 'rapor gereksinimi yaz' dendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Rapor gereksinimi tanımlama"
  related: "dashboard-spec, metric-definition, data-requirements, kpi-definition, request-intake-document"
  prompt: "Finans'ın istediği, müşteri segmenti ve yaşlandırma dilimine göre aylık vadesi geçmiş alacaklar raporunun gereksinimlerini yaz."
---

# Rapor Gereksinimi Tanımlama

## Amaç
Bir raporu, hedef kitlenin gerçek sorusunu cevaplayacak, her rakamı yeniden üretilip mutabakat yapılabilecek ve geliştiricilerin hesaplama, filtre veya erişim konusunda tahmin yürütmesine gerek kalmayacak kesinlikte tanımlamak.

## Ne zaman kullanılır
- Bir paydaş yeni bir rapor, dışa aktarım, liste veya zamanlanmış veri çekimi istediğinde.
- Mevcut bir raporun rakamları tartışıldığında veya başka bir kaynaktan farklı çıktığında.
- Bir rapor yeni bir platforma taşınırken mantığının açık hâle getirilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Yerleşimiyle birlikte etkileşimli, çok grafikli bir dashboard gerekiyorsa `dashboard-spec` kullanılır.
- Yalnızca tek bir metriğin uzlaşılmış tanımı gerekiyorsa `metric-definition` kullanılır.
- Talebin kendisi hâlâ ham ve nitelendirilmemişse önce `request-intake-document` kullanılır.

## Girdiler
Zorunlu:
- Rapor talebi ve hedef kitlesi (raporu kimin kullanacağı).

İsteğe bağlı, kaliteyi artırır:
- Mevcut raporun bir örneği veya taslağı, metrik tanımları, veri kaynakları, iş kuralları, erişim politikası, yasal gereklilikler.

Hedef kitle veya amaç yoksa sor: "Bu rapor hangi kararı veya aksiyonu tetikleyecek ve bunu kim yapacak?" Bir seferde en fazla 5 engelleyici soru sor.

## Süreç
1. Birebir isteneni ("X'in Excel listesi") desteklediği karar veya kontrolden ayır; raporun amacını tek cümlede yaz ve çıkarımı `[VARSAYIM]` olarak işaretle.
2. Raporun cevaplaması gereken iş sorularını listele; hiçbirine cevap vermeyen alanları çıkar.
3. Granülerliği tanımla: bir satır neyi temsil ediyor (bir fatura, ay bazında bir müşteri). Tartışmaların çoğu belirsiz granülerlikten doğar.
4. Her alanı tanımla: iş adı, tanım, kaynak, format; ölçüler için kesin hesaplama, toplama yöntemi, birim/para birimi ve yuvarlama. Varsa `metric-definition` ID'lerine referans ver.
5. Boyutları, gruplamayı, ara toplamları, sıralamayı ve zaman mantığını (dönem, itibariyle tarihi, saat dilimi, mali veya takvim yılı) tanımla.
6. Filtreleri ve parametreleri tanımla: varsayılanlar, zorunlu olanlar, izin verilen değerler, "tümü" ve boş değerlerin nasıl davrandığı.
7. Veri güncelliğini ve kesim noktasını (gerçek zamanlı, günlük belirli saatte, ay sonu kapanışı) ve geç gelen veya düzeltilen veriye ne olduğunu belirt.
8. Erişimi tanımla: kim hangi satır ve kolonları görebilir; amaç için gerekmeyen kişisel verileri maskele veya çıkar (KVKK/GDPR minimizasyonu).
9. Teslimi tanımla: talep üzerine veya zamanlanmış, kanal, dosya formatı, boyut sınırları, üretilen dosyaların saklanması.
10. Kabulü tanımla: bir mutabakat rakamı (ör. toplam, dönemin genel muhasebe bakiyesine eşit) ve doğrulanacak örnek durumlar; varsayımları ve açık soruları muhataplarıyla listele.
11. Hedef devam ediyorsa tartışmalı ölçüler için `metric-definition`, görsel keşif gerekiyorsa `dashboard-spec`, yeni veri için `data-requirements` öner.

## Çıktı formatı
```markdown
# Rapor Gereksinimleri: <rapor adı>
| Alan | Değer |
|---|---|
| Amaç (karar / kontrol) | ... |
| Hedef kitle | ... |
| Granülerlik (bir satır =) | ... |
| Güncellik / kesim | ... |
| Teslim | <talep üzerine / zamanlanmış, kanal, format> |

## İş Soruları
## Alanlar ve Ölçüler
| # | Alan | Tanım | Kaynak | Hesaplama / toplama | Format |
## Boyutlar, Gruplama, Sıralama, Zaman Mantığı
## Filtreler ve Parametreler
| Filtre | Varsayılan | Zorunlu | İzin verilen değerler | Boş/tümü davranışı |
## Erişim ve Maskeleme
## Kabul ve Mutabakat
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Amaç yalnızca rapor içeriğini değil, bir kararı veya kontrolü adlandırıyor.
- [ ] Granülerlik belirtildi ve her ölçünün kesin hesaplaması, toplama yöntemi ve birimi var.
- [ ] Zaman mantığı (dönem, itibariyle tarihi, saat dilimi) ve güncellik açık.
- [ ] Her filtrenin varsayılanı ve boş/tümü davranışı var.
- [ ] Kişisel verinin erişimi ve maskelemesi tanımlandı.
- [ ] Kabul, kaynağıyla bir mutabakat rakamı içeriyor; rakam uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Arkasındaki soruyu yazmadan kolon tanımlamak. Raporlar kimsenin okumadığı 60 kolona büyür; her alanı bir soruya bağla.
- Net mi brüt mü, kayıtlı mı faturalı mı, hangi para birimi ve hangi tarih olduğunu söylemeden "toplam satış" yazmak. Her ölçüyü kesin tanımla.
- Kesim sonrası düzeltmeleri yok saymak. Kapanmış dönemlerin yeniden hesaplanıp hesaplanmadığını belirt.

## Örnek
Girdi: "Finans, segment ve yaşlandırmaya göre aylık vadesi geçmiş alacaklar raporu istiyor."

Çıktıdan bir bölüm:
- Amaç `[VARSAYIM]`: ay sonu kapanışında hangi segmentlerin tahsilat aksiyonu ve karşılık gerektirdiğine karar vermek.
- Granülerlik: ayın son takvim günü itibarıyla açık bir fatura `[TBD: takvim ayı mı mali ay mı]`.
- Ölçü: Vadesi geçmiş tutar = vade tarihi < itibariyle tarihi olan açık fatura tutarı, ay sonu kuruyla raporlama para biriminde `[TBD: kur kaynağı]`.
- Yaşlandırma dilimleri: vadeden 1-30, 31-60, 61-90, 90+ gün geçmiş.
- Erişim: segment yöneticileri yalnızca kendi segmentini görür; müşteri iletişim bilgileri hariç tutulur.
- Kabul: vadesi geçmiş toplam, aynı itibariyle tarihi için alacak yardımcı defteri yaşlandırma toplamına eşittir.
