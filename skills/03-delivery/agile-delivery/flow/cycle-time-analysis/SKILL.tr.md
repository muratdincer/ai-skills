---
description: "İş maddelerinin başlangıç/bitiş tarihlerinden döngü süresini (cycle time) ve teslim süresini (lead time) analiz eder: yüzdelikleri hesaplar, dağılımı okur, durumda geçen süreden darboğaz durumları bulur, devam eden işleri geçmiş yüzdeliklere göre yaşlanma açısından işaretler ve bir hizmet seviyesi beklentisi önerir. Madde başlangıç/bitiş tarihleri veya pano durum geçmişi paylaşılıp işin ne kadar sürdüğü, nerede beklediği ya da hangi maddelerin takılma riski taşıdığı sorulduğunda kullanılır."
related: "wip-policy, monte-carlo-forecast, velocity-analysis, value-stream-map, engineering-metrics-review"
prompt: "Başlangıç ve bitiş tarihleriyle 40 biten madde ve başlangıç tarihleriyle devam eden 9 madde var. İşimiz ne kadar sürüyor ve ne takılmış?"
---

# Döngü/Teslim Süresi Analizi

## Amaç
Ham madde zaman damgalarını işin ne kadar sürdüğü, nerede beklediği ve hangi devam eden maddelerin kaydığı hakkında dürüst bir tabloya dönüştürmek. Böylece ekip yüzdeliğe dayalı taahhüt verebilir ve yaşlanan işe geç kalmadan müdahale edebilir.

## Ne zaman kullanılır
- Ekip veya bir paydaş "tipik bir madde ne kadar sürüyor?" diye soruyor ya da bir hizmet seviyesi beklentisi (SLE) istiyor.
- Teslimat yavaş hissediliyor ve ekip gecikmeye hangi durumun veya devrin yol açtığını bilmek istiyor.
- Düzenli akış değerlendirmesinde yaşlanan WIP kontrolü gerekiyor.

## Ne zaman kullanılmaz
- Bir iş grubu için kaç madde veya hangi tarih öngörüsü için `monte-carlo-forecast` kullanılır.
- İterasyon başına teslim edilen puanı analiz etmek için `velocity-analysis` kullanılır.
- Ekip dışı adımlar dahil uçtan uca süreci haritalamak için `value-stream-map` kullanılır.

## Girdiler
Zorunlu:
- Biten maddeler için başlangıç ve bitiş tarihi (veya durum geçiş geçmişi). En az ~15 madde; kullanılan "başlangıç" ve "bitiş" tanımları belirtilmeli.

İsteğe bağlı, kaliteyi artırır:
- Madde bazında durumda geçen süre geçmişi (ör. analiz, geliştirme, inceleme, test, deployment bekleme).
- Başlangıç tarihi ve güncel durumuyla devam eden maddeler.
- Madde türü, hizmet sınıfı, büyüklük, bloke kalınan süreler.
- Döngü süresine ek olarak teslim süresini (oluşturma → bitiş) hesaplamak için oluşturma tarihi.

Başlangıç/bitiş tanımları belirsizse bunları netleştirmek için tek bir soru sor; tanımlar olmadan rakamlar karşılaştırılamaz. ~15'ten az madde varsa her yüzdeliği `[DÜŞÜK GÜVEN]` olarak işaretle.

## Süreç
1. Tanımları sabitle: döngü süresi = aktif işin başlaması → bitiş; teslim süresi = talebin oluşturulması/taahhüt edilmesi → bitiş. Gün sayma kuralını seç (takvim günü, dahil: aynı gün biten = 1) ve belirt.
2. Veriyi temizle: tarihi eksik maddeleri çıkar, negatif veya sıfır süreli anormallikleri işaretle, iptal edilenleri ayır, yeniden açılan maddeleri not et. Kaç maddenin neden çıkarıldığını raporla.
3. Dağılımı hesapla: sayı, medyan (P50), P70, P85, P95, en düşük, en yüksek. Hesap yöntemini göster (sıralı değerlerde en yakın sıra). Ortalamayı ana değer olarak kullanma; döngü süresi sağa çarpıktır.
4. Şekli oku: uzun kuyruk (birkaç madde çok daha uzun sürüyor), iki tepeli (iki tür iş karışmış; türe göre ayır) veya dar. Türler farklıysa yüzdelikleri tür veya hizmet sınıfı bazında hesapla.
5. Durumda geçen süreden darboğazları bul: durum başına toplam ve medyan süre; aktif durumlar ve bekleme durumları (kuyruklar, "incelemeye hazır", "deployment bekliyor") olarak ayır. İkisi de varsa akış verimliliği = aktif süre / toplam süre hesapla; bekleme durumları panoda modellenmemişse `[TAHMİN]` olarak etiketle.
6. Yaşlanan WIP'i kontrol et: devam eden her madde için şimdiye kadarki yaşı hesapla ve biten maddelerin P50/P85 değerleriyle karşılaştır. P85 üstünü "riskli", P95 üstünü "takılmış" olarak işaretle.
7. Trendlere bak: son 4-6 haftayı önceki dönemle karşılaştır; yükselen P85 çoğu zaman artan WIP'e veya büyüyen parti boyutuna işaret eder.
8. Bir SLE öner: örnek dönemiyle birlikte P85'e dayanan "<tür> maddelerin %85'i N gün içinde biter".
9. Kanıta bağlı 2-4 aksiyon öner: en eski maddelere ekipçe odaklanmak, darboğaz durumunda WIP'i sınırlamak (`wip-policy`), büyük maddeleri bölmek, bir devri veya kuyruğu kaldırmak.
10. Devret: darboğazlara göre aksiyon almak için `wip-policy`, teslim öngörüsü için `monte-carlo-forecast` öner; açık veri sorularını listele.

## Çıktı formatı
```markdown
# Döngü/Teslim Süresi Analizi – <ekip>, <dönem>
Tanımlar: başlangıç = <...>, bitiş = <...>, takvim günü, dahil
Örneklem: <n> biten madde (<çıkarılan n>: <nedenler>)

## Dağılım
| Metrik | Döngü süresi | Teslim süresi |
|---|---|---|
| P50 / P70 / P85 / P95 | | |
| En düşük / En yüksek | | |
Şekil: <dar / uzun kuyruk / iki tepeli> – <kanıt>

## Durumda Geçen Süre
| Durum | Tür (aktif/bekleme) | Medyan gün | Toplamdaki payı |
|---|---|---|---|
Akış verimliliği: <%x> [gerekirse TAHMİN]
Darboğaz: <durum> – <kanıt>

## Yaşlanan WIP
| Madde | Durum | Yaş (gün) | P85'e göre | İşaret |
|---|---|---|---|---|

## Hizmet Seviyesi Beklentisi
<<tür> maddelerin %85'i N gün içinde biter (örnek dönem)>

## Aksiyonlar
1. <aksiyon> – <kanıt> – <sorumlu rol>

## Veri Uyarıları ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Başlangıç/bitiş tanımları ve gün sayma kuralı belirtildi.
- [ ] Ana metrikler yüzdelikler; ortalama tipik değer olarak kullanılmadı.
- [ ] Çıkarılan veya anormal maddeler sayıldı ve açıklandı.
- [ ] Devam eden her madde geçmiş yüzdeliklerle karşılaştırıldı.
- [ ] Darboğaz iddiaları durumda geçen süre verisine dayanıyor veya `[ÇIKARIM]` olarak etiketli.
- [ ] Bireysel performans sıralanmadı; analiz iş sistemine dair.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İş türlerini (hata, özellik, destek) tek dağılımda karıştırmak. Şekil iki tepeliyse ayır.
- Yalnızca biten maddelere bakmak. Yaşlanan WIP öncü göstergedir; biten madde yüzdelikleri geriden gelir.
- Pano durumlarını gerçek süreç sanmak. Bekleme "Devam ediyor" içinde gizliyse akış verimliliği olduğundan yüksek çıkar; bunu belirt.

## Örnek
Girdi: 40 biten madde, sıralı döngü süreleri: 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, ... 14, 18, 27; devam eden 9 madde.

Çıktıdan bir bölüm:
- P50 = 4 gün, P85 = 11 gün, P95 = 18 gün; uzun kuyruğu dış bir API'de bloke kalan 3 madde oluşturuyor `[belirtildi]`.
- Darboğaz: "İncelemeye hazır" medyan 2,5 gün, toplam sürenin %38'i – bekleme durumu.
- Yaşlanan WIP: ITEM-212 14 gündür Test'te (> P85) → riskli; bugün ekipçe odaklanın.
- SLE: hikâyelerin %85'i 11 gün içinde biter (örnek: son 12 hafta).
