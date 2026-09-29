---
description: Teslimat sonrası fayda gerçekleşmesini izler; planlanan faydaları baz değer, hedef, sahip ve ölçüm tarihleri olan ölçülebilir göstergelere dönüştürür, planlanan ve gerçekleşen değerleri karşılaştırır, değişimin ne kadarının girişime ait olduğunu değerlendirir ve düzeltici aksiyon ya da yeniden tahmin önerir. Bir proje veya program canlıya geçtikten sonra, uygulama sonrası veya fayda gözden geçirmesinde, iş gerekçesinin sonuçlarla karşılaştırılması gerektiğinde ya da "vaat ettiğimiz değeri aldık mı" diye sorulduğunda kullanılır.
related: kpi-definition, cost-benefit-analysis, feature-adoption-review, project-closure-report, portfolio-prioritization
prompt: Self-servis portalımızın canlıya geçişinden altı ay sonra fayda gerçekleşmesini kontrol et; iş gerekçesi çağrı merkezi temaslarında %30 azalma ve daha hızlı müşteri kaydı vaat ediyordu.
---

# Fayda Gerçekleşme Takibi

## Amaç
İş gerekçesinde vaat edilen değerin gelip gelmediğini, bunun ne kadarının teslim edilen değişikliğe bağlanabileceğini ve fayda sahiplerinin açığı kapatmak için ne yapması gerektiğini dürüstçe göstermek. Böylece portföy sonuçlardan öğrenir ve fonlama kararları kanıta dayanır.

## Ne zaman kullanılır
- Bir proje veya program canlıya geçmiş ve faydalarının ölçülme zamanı gelmişse.
- Planlanmış bir uygulama sonrası veya fayda gözden geçirmesi yaklaşıyorsa.
- Portföy kurulu bir sonraki aşamayı fonlamadan önce planlanan ve gerçekleşen değeri görmek istiyorsa.
- İş gerekçesindeki faydalar muğlak olduğu için bir fayda kaydının oluşturulması veya düzeltilmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Faydalar henüz tahmin edilmediyse (yatırım öncesi) `cost-benefit-analysis` kullanılır.
- Soru tek bir ürün özelliğinin kullanımıysa `feature-adoption-review` kullanılır.
- Amaç projeyi resmi olarak kapatmaksa bu gözden geçirmeyi girdi yaparak `project-closure-report` kullanılır.

## Girdiler
Zorunlu:
- Planlanan faydalar (iş gerekçesi, proje başlatma belgesi veya dile getirilen vaatler).
- Teslimattan sonra mevcut gerçekleşen veriler ya da henüz veri olmadığının teyidi.

İsteğe bağlı, kaliteyi artırır:
- Teslimattan önce ölçülmüş baz değerler, ölçüm tanımları, veri kaynakları.
- İş tarafındaki fayda sahipleri, canlıya geçiş tarihi ve benimsenme verisi.
- Aynı göstergeleri etkileyen diğer girişimler veya dış etkenler.
- Gerçekleşen maliyetler (net fayda ve getiri karşılaştırması için).

Planlanan faydalar eksikse sor. Verilmeyen gerçekleşen değerleri asla doldurma; `[BİLİNMİYOR]` olarak işaretle ve nasıl ölçüleceğini planla.

## Süreç
1. Planlanan her faydayı listele ve sınıflandır: nakit serbest bırakan finansal, nakit dışı finansal (serbest kalan kapasite), ölçülebilir finansal olmayan (kalite, hız, memnuniyet), uyum veya risk azaltma. Varsa olumsuz etkileri (disbenefit) not et.
2. Her faydayı ölçülebilir kıl: gösterge, formül, veri kaynağı, baz değer (değer ve tarih), hedef, hedef tarih ve fayda sahibi (proje yöneticisi değil, bir iş rolü). Sonradan yeniden oluşturulan baz değerleri `[VARSAYIM]` olarak işaretle.
3. Her faydayı onu mümkün kılan değişikliğe ve bağlı olduğu benimsenmeye (ör. portal kullanım oranı) eşle; çünkü fayda benimsenmenin arkasından gelir.
4. Her gösterge ve dönem için gerçekleşen değerleri topla; her değerin kaynağını ve tarihini yaz.
5. Planlanan ile gerçekleşeni karşılaştır: sapma, eğilim ve hedef tarihin geçip geçmediği. Her faydayı değerlendir: Yolunda, Geride, Riskte, Gerçekleşti, Ölçülemiyor.
6. Atıf yap: değişimin ne kadarının bu girişimden, ne kadarının mevsimsellikten, diğer girişimlerden veya dış etkenlerden geldiğini tahmin et. Kontrol grubu, eğilimli önce-sonra karşılaştırması veya sahip görüşü kullan; yöntemi ve güveni etiketle.
7. Geride veya riskte olan her fayda için nedeni bul (benimsenme açığı, süreç değişmedi, baz değer yanlış, hedef gerçekçi değil, dış etken) ve sahibi ile tarihi belli bir düzeltici aksiyon ya da resmi bir yeniden tahmin öner.
8. Finansal olanlarda toplam gerçekleşen ve planlanan değeri özetle; nakit ve nakit dışı faydaları belirtmeden tek bir rakamda toplama. Planlanmamış faydaları ve olumsuz etkileri belirle.
9. Sonraki ölçüm noktalarını ve takibin ne zaman biteceğini (fayda kalıcılaştı veya kapatıldı) tanımla.
10. Gelecekteki iş gerekçeleri için dersleri kaydet (hangi tahminler iyimserdi, hangi göstergeleri ölçmek zordu).
11. Hedef devam ediyorsa zayıf göstergeleri düzeltmek için `kpi-definition`, sonucu kaydetmek için `project-closure-report` veya sonuçları bir sonraki fonlama turuna taşımak için `portfolio-prioritization` öner.

## Çıktı formatı
```markdown
# Fayda Gerçekleşme Değerlendirmesi: <girişim> — <değerlendirme tarihi>
Canlıya geçiş: <tarih> · Değerlendirme noktası: <ör. +6 ay> · Genel: <RAG>

## Fayda Kaydı
| ID | Fayda | Tür | Gösterge (formül) | Baz (tarih) | Hedef (tarih) | Gerçekleşen (tarih, kaynak) | Sapma | Durum | Sahip |
|---|---|---|---|---|---|---|---|---|---|

## Benimsenme Etkenleri
| Etken | Beklenen benimsenme | Gerçekleşen | Faydaya etkisi |
|---|---|---|---|

## Atıf
| Fayda | Yöntem | Girişime atfedilen pay | Güven |
|---|---|---|---|

## Açıklar ve Düzeltici Aksiyonlar
| Fayda | Neden | Aksiyon / yeniden tahmin | Sahip | Tarih |
|---|---|---|---|---|

## Planlanmamış Faydalar ve Olumsuz Etkiler
## Sonraki Ölçüm Noktaları
## Gelecekteki İş Gerekçeleri İçin Dersler
## Varsayımlar ve Veri Boşlukları
- [VARSAYIM] / [BİLİNMİYOR] ...
```

## Kalite kontrol listesi
- [ ] Her faydanın göstergesi, formülü, baz değeri, hedefi, tarihi ve iş tarafında bir sahibi var.
- [ ] Her gerçekleşen değerin kaynağı ve tarihi var; eksik gerçekleşenler tahmin edilmedi, `[BİLİNMİYOR]` olarak işaretli.
- [ ] Her fayda için atıf yöntemi ve güven düzeyi belirtildi.
- [ ] Hedefin gerisindeki faydaların nedeni ve düzeltici aksiyonu ya da yeniden tahmini var.
- [ ] Nakit ve nakit dışı faydalar sessizce toplanmadı; olumsuz etkiler listelendi.
- [ ] Çıkarımlar ve yeniden oluşturulan baz değerler etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Fayda sahipliğini proje yöneticisine vermek. Faydalar proje bittikten sonra iş tarafında gerçekleşir; sahip bir iş rolü olmalı.
- Bir KPI'daki hareketin tamamını sahiplenmek. Diğer girişimler ve mevsimsellik aynı sayıları oynatır; atfı ve güveni belirt.
- Yalnızca canlıya geçişte bir kez ölçmek. Fayda benimsenmenin arkasından gelir; birden fazla ölçüm noktası planla.

## Örnek
Girdi: "Self-servis portal, canlıya geçişten 6 ay sonra; iş gerekçesi: çağrı merkezi temaslarında %30 azalma, daha hızlı müşteri kaydı."

Çıktıdan bir bölüm:
| ID | Fayda | Baz | Hedef | Gerçekleşen | Durum |
|---|---|---|---|---|---|
| F1 | Temas hacminde azalma | Canlıya geçiş öncesi aylık temas `[BİLİNMİYOR]` | +12. ayda −%30 | +6. ayda −%12 (çağrı merkezi raporu) | Geride |
| F2 | Daha hızlı müşteri kaydı | `[BİLİNMİYOR]` | `[TBD]` gün | ölçülmedi | Ölçülemiyor |

- F1 nedeni: portal benimsenmesi beklenen %60'a karşı %35; aksiyon: IVR'a ve onay e-postalarına portal bağlantısı ekle — sahip: müşteri hizmetleri müdürü `[TBD: isim]`.
- F2: "başvurudan aktif hesaba kadar geçen gün" göstergesini tanımla ve baz değeri CRM'den yeniden oluştur `[VARSAYIM]`.
