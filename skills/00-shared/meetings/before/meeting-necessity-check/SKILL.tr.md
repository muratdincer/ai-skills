---
description: Planlanan bir toplantının gerçekten gerekli olup olmadığını, hedefini asenkron alternatiflerle karşılaştırarak değerlendirir; toplan, kısalt, asenkron yürüt veya iptal et önerisini kullanıma hazır bir alternatifle sunar. Yeni veya periyodik bir toplantı planlanırken, "bunun için toplantı şart mı?" sorulduğunda ya da toplantı yükü azaltılmak istendiğinde kullanılır.
related: meeting-agenda, meeting-invite, stakeholder-email, status-update, working-agreement
prompt: Veri taşıma ilerlemesini paylaşmak için 9 kişiyle haftalık 1 saatlik bir senkron toplantı kurmak istiyorum. Gerçekten gerekli mi?
---

# Toplantı Gerekli mi Kararı

## Amaç
Toplantıyı yalnızca hedefe ulaşmanın en ucuz yolu eş zamanlı etkileşim olduğunda yaparak ekibin odak süresini korumak; gerekli değilse somut bir asenkron alternatif sunmak.

## Ne zaman kullanılır
- Yeni bir toplantı veya çalıştay planlanırken.
- Periyodik bir toplantı gözden geçirilirken ya da toplantı yükünden şikâyet edildiğinde.
- Bir e-posta, doküman veya mesajın yeterli olup olmayacağı sorulduğunda.

## Ne zaman kullanılmaz
- Toplantı zaten gerekçelendirilmiş ve yapıya ihtiyaç duyuyorsa `meeting-agenda` kullanılır.
- Ekip genel toplantı kuralları belirlemek istiyorsa `working-agreement` kullanılır.

## Girdiler
Zorunlu:
- Toplantının hedefi (sonrasında ne farklı olmalı).
- Önerilen katılımcılar (sayı veya roller) ve süre/sıklık.

İsteğe bağlı:
- Aciliyet, görüş ayrılığının düzeyi, konunun hassasiyeti, saat dilimleri, daha önce denenen asenkron yöntemler.

Hedef verilmediyse iste: hedef yoksa cevap her zaman "henüz toplanma"dır.

## Süreç
1. Hedefi bir çıktı olarak yeniden yaz: karar, uyum, bilgi paylaşımı, problem çözme, ilişki/güven ya da yaratıcı üretim.
2. Maliyeti hesapla: katılımcı x süre x sıklık = aylık kişi-saat. Sayıyı göster.
3. Eş zamanlı etkileşim ihtiyacını şu sinyallerle puanla (her biri Evet/Hayır):
   - Canlı müzakere gerektiren gerçek bir görüş ayrılığı veya ödünleşim var.
   - Belirsizlik yüksek; problem henüz yazıya dökülemiyor.
   - İçerik hassas veya duygusal (kötü haber, çatışma, kişisel konular).
   - Birkaç kişi arasında hızlı iterasyon gerekiyor (tasarım, olay yönetimi).
   - Açık hedef ilişki kurmak veya oryantasyon.
   - Asenkron deneme daha önce başarısız oldu.
4. Eleyici durumları kontrol et: net hedef yok, karar verici davetli değil, tek yönlü durum paylaşımı, katılımcıların yarısından azı katkı veriyor.
5. Karar ver: Toplan / Daha kısa veya küçük toplan / Asenkron yürüt / İptal et. Genellikle iki veya daha fazla sinyal olup eleyici durum yoksa toplantı gerekçelidir.
6. Toplantı gerekiyorsa asgari katılımcı listesini (karar vericiler ve katkı verenler; diğerleri özeti alır) ve gerçekçi en kısa süreyi öner.
7. Asenkron ise formatı seç (yazılı güncelleme, yorum son tarihi olan karar dokümanı, kayıtlı anlatım, sohbet kanalı, anket) ve taslağını yaz.
8. Periyodik toplantılar için bir gözden geçirme tarihi ve toplantının sürmesi için başarı sinyali öner.
9. Önerini gerekçesiyle yaz ki toplantı sahibi bunu savunabilsin.

## Çıktı formatı
```markdown
# Toplantı Gerekliliği: <konu>
Hedef türü: <karar/uyum/bilgi/problem çözme/ilişki/yaratıcı>
Maliyet: <n> kişi x <süre> x <sıklık> = <kişi-saat/ay>

| Sinyal | Evet/Hayır | Not |
|---|---|---|
| Canlı görüş ayrılığı / ödünleşim | | |
| Yüksek belirsizlik | | |
| Hassas içerik | | |
| Hızlı çok kişili iterasyon | | |
| İlişki hedefi | | |
| Asenkron deneme başarısız | | |

Eleyici durumlar: <yok / liste>
Öneri: <Toplan / Kısalt-küçült / Asenkron / İptal>
Gerekçe: <2-3 cümle>

## Alternatif (asenkron ise)
Format: <...>  Sorumlu: <...>  Yanıt son tarihi: <tarih veya [TBD]>
<mesaj taslağı veya doküman iskeleti>

## Toplanılacaksa
Katılımcılar (zorunlu): ...  Yalnızca bilgilendirilecek: ...  Süre: ...  Gözden geçirme: ...
```

## Kalite kontrol listesi
- [ ] Hedef bir konu değil, bir çıktı.
- [ ] Kişi-saat cinsinden maliyet gösterildi.
- [ ] Öneri alışkanlıktan değil sinyallerden çıkıyor.
- [ ] Asenkron öneri hazır bir taslak ve yanıt son tarihi içeriyor.
- [ ] Toplantı önerisi katılımcı sayısını ve süreyi kısıyor.

## Sık yapılan hatalar
- Toplantıyı son tarihi ve sorumlusu olmayan bir asenkron mesajla değiştirmek; sonuçta hiçbir şey olmaz. İkisini de mutlaka belirle.
- Zaman kazanmak için hassas konuları (yeniden yapılanma, performans, çatışma) yazıya taşımak. Bunlar yüz yüze konuşma gerektirir.
- Periyodik toplantıları sonsuza kadar sürdürmek. Bir gözden geçirme tarihi ve açık bir sonlandırma kriteri ekle.

## Örnek
Girdi: Veri taşıma ilerlemesini paylaşmak için 9 kişiyle haftalık 1 saatlik toplantı.

Çıktıdan bir bölüm:
- Maliyet: 9 x 1 sa x 4,3 = ~39 kişi-saat/ay.
- Sinyaller: yalnızca "hızlı iterasyon" kısmen geçerli; hedef tek yönlü durum paylaşımı.
- Öneri: Asenkron. Her perşembe `status-update` ile yazılı haftalık güncelleme; durum Sarı veya Kırmızı olduğunda yalnızca 3 lider ile 20 dakikalık görüşme.
