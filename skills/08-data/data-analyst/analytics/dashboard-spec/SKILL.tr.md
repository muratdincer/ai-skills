---
description: Bir gösterge panelini (dashboard) inşa edilmeden önce tanımlar; hedef kitle, desteklenen kararlar, sorular, tanımlarıyla KPI'lar, görseller, filtreler, detaya inme yolları, yenileme ve erişim kuralları. Yeni bir dashboard veya rapor sayfası istendiğinde, karmaşık bir panel yeniden tasarlanacağında ya da BI geliştiricisinin tahmin yürütmeden uygulayabileceği bir tanım gerektiğinde kullanılır.
related: metric-definition, kpi-definition, report-requirements, data-requirements, insight-summary
prompt: Müşteri destek yönetimi için iş kaydı birikimini, SLA uyumunu ve temsilci iş yükünü haftalık izleyecek bir dashboard tanımla.
---

# Gösterge Paneli Tanımlama

## Amaç
Hedef kitlenin kararlarından ve sorularından yola çıkan, uygulanabilir bir dashboard tanımı üretmek. Böylece sonuç, kullanılmayan bir grafik duvarına dönüşmek yerine düzenli olarak kullanılır.

## Ne zaman kullanılır
- Bir ekip yeni bir dashboard veya mevcut panele yeni bir sayfa istediğinde.
- Mevcut dashboard karmaşık, güvenilmeyen veya kullanılmayan bir hale geldiğinde ve yeniden tasarım gerektiğinde.
- BI geliştiricisinin belirsizlik içermeyen bir tanıma (metrikler, görseller, filtreler, güvenlik) ihtiyacı olduğunda.

## Ne zaman kullanılmaz
- İhtiyaç tek seferlik bir soruysa `analysis-plan` kullanılır.
- Tek bir metrik tartışmalı veya tanımsızsa önce `metric-definition` kullanılır.
- Talep, sabit yerleşimli resmi bir yasal veya operasyonel raporsa `report-requirements` kullanılır.

## Girdiler
Zorunlu:
- Hedef kitle ve neyi izlemek veya neye karar vermek istedikleri.

İsteğe bağlı, kaliteyi artırır:
- Mevcut raporlar, ekran görüntüleri, metrik tanımları.
- Veri kaynakları ve yenilenme sıklıkları.
- BI platformu kısıtları, kurumsal görsel standartlar, erişim kuralları.

Hedef kitle veya amaç yoksa sor. Diğer her şey açık soru olur.

## Süreç
1. Birincil hedef kitleyi ve kullanım biçimini (günlük operasyon kontrolü, haftalık gözden geçirme, aylık yönetim) belirt. Bir dashboard tek bir birincil kitleye hizmet eder.
2. Dashboard'un cevaplaması gereken 3-7 karar veya soruyu öncelik sırasıyla listele. Hiçbir soruya karşılık gelmeyen istekleri çıkar.
3. Her soru için KPI'ları tanımla: ad, formül referansı, tanecik, hedef/eşik, karşılaştırma (hedefe göre, önceki döneme göre). Tanımsız metrikleri `metric-definition` için işaretle.
4. Her soru için görsel seç: durum için trendli büyük sayı, zaman trendi için çizgi, sıralama/karşılaştırma için çubuk, arama için tablo, iki boyutlu yoğunluk için ısı haritası. 3 dilimden fazla pasta ve çift eksenden kaçın.
5. Yerleşimi okuma sırasına göre kur: başlık KPI'ları sol üstte, ardından trendler, altında tanısal kırılımlar, en sonda detay tabloları.
6. Genel ve yerel filtreleri, varsayılan değerleri ve detaya inme (drill-down/drill-through) yollarını tanımla.
7. Veriyi tanımla: kaynaklar, yenileme sıklığı, kabul edilebilir gecikme, "veri tarihi" etiketi, tamamlanmamış dönemlerin nasıl gösterileceği.
8. Erişimi tanımla: satır bazlı güvenlik, kişisel veriyi kimin göreceği, maskeleme. Varsayılan olarak toplulaştırılmış görünüm kullan.
9. Uyarı veya koşullu biçimlendirme eşiklerini ve renklerini, erişilebilirlik için renk dışı işaretlerle birlikte tanımla (WCAG 2.2 kontrast).
10. Kabulü tanımla: kaynak toplamlarla mutabakat, performans hedefi (yüklenme süresi) ve bir kullanım gözden geçirme tarihi.

## Çıktı formatı
```markdown
# Dashboard Tanımı: <ad>
| Alan | Değer |
|---|---|
| Birincil kitle | <rol> – <kullanım sıklığı> |
| Sahibi | <ad veya [BİLİNMİYOR]> |
| Veri yenileme | <sıklık, gecikme> |

## Cevapladığı Sorular
1. <soru> → <desteklediği karar>

## KPI'lar
| KPI | Tanım referansı | Tanecik | Hedef / eşik | Karşılaştırma |
|---|---|---|---|---|

## Yerleşim
| Bölge | Görsel | KPI / alanlar | Etkileşim |
|---|---|---|---|
| Üst satır | Büyük sayı + mini trend | ... | tıkla → sayfa 2 |

## Filtreler ve Detaya İnme
- Genel: <filtre> (varsayılan: ...)
- Detay: <nereden> → <nereye>

## Veri ve Güvenlik
- Kaynaklar: ...
- Satır bazlı güvenlik: ...
- Kişisel veri: <toplulaştırılmış / maskeli / hariç>

## Kabul Kriterleri
- Toplamlar <kaynak> ile <tolerans> içinde tutuyor.
- Varsayılan filtrelerle < <n> sn'de yükleniyor.

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Her görsel listelenmiş bir soruya karşılık geliyor.
- [ ] Her KPI'ın tanım referansı, taneciği ve karşılaştırması var.
- [ ] Eşikler ve renkler tanımlı ve yalnızca renge dayanmıyor.
- [ ] Tamamlanmamış güncel dönem ele alınmış (işaretli veya hariç).
- [ ] Erişim ve kişisel veri kuralları açık.
- [ ] Hiçbir şey uydurulmadı: bilinmeyen hedefler `[TBD]`.

## Sık yapılan hatalar
- "Herkes için" tasarlamak. Tek bir birincil kitle seç; diğerleri için ayrı görünüm oluştur.
- Sayıları bağlamsız göstermek. Her KPI'ı hedef veya önceki dönemle eşleştir.
- Aynı sayfada farklı tanecikleri (günlük ve aylık) etiketlemeden karıştırmak; toplamlar tutmaz.

## Örnek
Girdi: "Destek yönetimi iş kaydı birikimini, SLA uyumunu ve temsilci iş yükünü haftalık izlemek istiyor."

Çıktıdan bir bölüm:
- Soru 1: Bu hafta SLA'yı tutturuyor muyuz? → temsilcilerin yeniden dağıtılmasına karar vermek için.
- KPI: SLA uyum % = SLA içinde çözülen kayıt / çözülen kayıt, haftalık, önceliğe göre; hedef `[TBD]`.
- Yerleşim: üst satırda büyük sayılar (açık birikim, SLA %, medyan ilk yanıt süresi) ve 12 haftalık mini trend; ortada kuyruğa göre birikim çubuk grafiği; altta açık kaydı olan temsilciler tablosu (isimleri yalnızca takım liderleri görür).
