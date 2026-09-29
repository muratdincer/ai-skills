---
description: Bir analizi, öneriyi veya kararı doğrulama, çıpalama, hayatta kalan yanılgısı, batık maliyet, erişilebilirlik, aşırı özgüven ve grup düşüncesi gibi bilişsel yanlılıklar açısından inceler; her şüpheli yanlılığın kanıtını gösterir ve somut bir düzeltici aksiyon önerir. Bir karar verilmek veya analiz paylaşılmak üzereyken, "bir şeyi atlıyor muyum?", "bu yanlı mı?", "mantığımı sorgula" denildiğinde ya da bir sonuca karşı eleştirel bakış istendiğinde kullanılır.
related: pre-mortem, assumption-mapping, decision-matrix, trade-off-analysis, decision-log
prompt: Yönlendirme komitesine göndermeden önce bu öneriyi yanlılık açısından kontrol et: kurum içi zamanlayıcıya yatırıma devam etmeliyiz, çünkü üzerinde zaten 18 ay çalıştık ve iki pilot ekip çok memnun.
---

# Bilişsel Yanlılık Kontrolü

## Amaç
Bir analizin veya kararın kanıta değil çarpık bir akıl yürütmeye dayandığı noktaları bulmak ve her bulguyu somut bir düzeltici aksiyona çevirmek. Hedef, yazar hakkında hüküm vermek değil daha iyi bir karar almaktır.

## Ne zaman kullanılır
- Bir öneri, iş gerekçesi, tahmin veya mimari tercih onaylanmak ya da paylaşılmak üzereyken.
- Bir sonuç fazla oybirliğiyle, hızlı veya duygusal biçimde çıktıysa ve kimse karşı tarafı savunmadıysa.
- Geriye dönük bir incelemede kötü şansı kötü akıl yürütmeden ayırmak gerektiğinde.
- Kullanıcı düşüncesinin açıkça sorgulanmasını istediğinde.

## Ne zaman kullanılmaz
- Amaç bir planın gelecekte nasıl başarısız olacağını hayal etmekse `pre-mortem` kullanılır.
- Amaç planın dayandığı varsayımları listeleyip sınamaksa `assumption-mapping` kullanılır.
- Seçeneklerin henüz kriterlere göre puanlanması gerekiyorsa `decision-matrix` kullanılır.

## Girdiler
Zorunlu:
- Analiz, öneri veya karar metni; kullanılan gerekçe ve kanıtlarla birlikte.

İsteğe bağlı, kaliteyi artırır:
- Değerlendirilip elenen seçenekler ve elenme nedenleri.
- Kararı kimin verdiği, çıkarı ve grubun karara nasıl vardığı.
- Veri kaynakları, örneklem büyüklüğü, zaman aralığı, önceki taahhütler veya harcamalar.

Gerekçe metni yoksa iste. İsteğe bağlı girdileri en başta sorma; eksikliklerini açık soru olarak listele.

## Süreç
1. Sonucu tek cümleyle yeniden yaz ve dayandığı iddiaları listele; her birini belirtilmiş kanıt, belirtilmiş görüş veya senin çıkarımın olarak etiketle.
2. Kanıtın kaynağını çıkar: kim topladı, örneklem büyüklüğü, seçim yöntemi, zaman aralığı ve gerekli olduğu hâlde bulunmayan kanıt.
3. Yanlılık listesiyle tara: doğrulama, çıpalama, erişilebilirlik, hayatta kalan yanılgısı, batık maliyet, aşırı özgüven/planlama yanılgısı, çerçeveleme, otorite (HiPPO), grup düşüncesi/sürü etkisi, statüko, taban oranı ihmali, yakınlık etkisi, iyimserlik, IKEA/burada icat edilmedi, sonuç yanlılığı.
4. Şüphelenilen her yanlılık için onu tetikleyen cümleyi veya veri noktasını aynen alıntıla ya da göster. Alıntı yoksa bulgu da yoktur.
5. Her bulguyu puanla: karara Etkisi (Yüksek/Orta/Düşük) ve yanlılığın var olduğuna Güven (Yüksek/Orta/Düşük). "Olası" yanlılıkları "belirgin" olanlardan ayrı tut.
6. Karşı görüşün en güçlü hâlini (steelman) 3-5 cümleyle yaz; yalnızca girdideki olguları veya açıkça işaretlenmiş varsayımları kullan.
7. Etkisi Yüksek her bulgu için somut bir düzeltici aksiyon öner: çürütücü bir test, taban oranı veya referans sınıfı kontrolü, bağımsız tahmin, sıfır tabanlı ("bugün başlasaydık") soru, kör inceleme veya atanmış bir şeytanın avukatı.
8. Sonucu değiştirecek kanıtı (vazgeçme kriterleri) belirle ve karar tarihinden önce elde edilip edilemeyeceğini yaz.
9. Genel bir değerlendirme ver: akıl yürütme sağlam / çekincelerle sağlam / karardan önce yeniden çalışılmalı; tek satırlık gerekçesiyle.
10. Şablonu doldur. Kullanıcı devam etmek isterse başarısızlık senaryoları için `pre-mortem`, en riskli varsayımları sınamak için `assumption-mapping` veya nihai kararı çekinceleriyle kaydetmek için `decision-log` öner.

## Çıktı formatı
```markdown
# Yanlılık Kontrolü: <karar veya analiz başlığı>
**İncelenen sonuç:** <tek cümle>
**Genel değerlendirme:** <Sağlam / Çekincelerle sağlam / Yeniden çalışılmalı> – <neden>

## İddialar ve Kanıtlar
| # | İddia | Tür (kanıt / görüş / çıkarım) | Kaynak | Eksik |
|---|---|---|---|---|

## Bulgular
| # | Yanlılık | Tetikleyici (alıntı veya veri) | Etki | Güven | Düzeltici aksiyon |
|---|---|---|---|---|---|

## Karşı Görüşün En Güçlü Hâli
<3-5 cümle>

## Sonucu Ne Değiştirir
- <kanıt> – <karardan önce elde edilebilir mi? evet/hayır>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
- <soru> – <kim cevaplayabilir>
```

## Kalite kontrol listesi
- [ ] Her bulgu girdideki belirli bir cümleye, sayıya veya süreç olgusuna dayanıyor.
- [ ] Belirgin yanlılıklar yalnızca olası olanlardan ayrılmış, güven düzeyi belirtilmiş.
- [ ] Etkisi Yüksek her bulgunun yalnızca bir etiketi değil, uygulanabilir bir düzeltici adımı var.
- [ ] Karşı görüş adil biçimde savunulmuş ve hiçbir olgu uydurulmamış.
- [ ] Ton kişileri değil akıl yürütmeyi eleştiriyor; kanıt olmadan niyet atfedilmiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yanlılık tombalası: kanıtsız on yanlılık adı sıralamak. Yalnızca metne bağlanabilen bulguları tut.
- Kötü bir sonucu kötü akıl yürütmenin kanıtı saymak (incelemecinin sonuç yanlılığı). Akıl yürütmeyi o anda eldeki bilgiyle değerlendir.
- Yanlılık var diye doğru bir sonucu reddetmek. Yanlı bir yol da doğru sonuca varabilir; düzeltmeden sonra sonucun ayakta kalıp kalmadığını söyle.

## Örnek
Girdi: "Kurum içi zamanlayıcıya yatırıma devam edelim: 18 ay harcadık ve iki pilot ekip çok memnun."

Çıktıdan bir bölüm:
| # | Yanlılık | Tetikleyici | Etki | Güven | Düzeltici aksiyon |
|---|---|---|---|---|---|
| 1 | Batık maliyet | "zaten 18 ay harcadık" | Yüksek | Yüksek | Sor: bugün başlasaydık geliştirir miydik, satın alır mıydık? Yalnızca kalan maliyeti karşılaştır. |
| 2 | Hayatta kalan yanılgısı / küçük örneklem | "iki pilot ekip çok memnun" | Yüksek | Orta | Pilota katılmayan veya bırakan ekiplere sor; benimseme ve memnuniyet metriklerini tanımla. |
| 3 | IKEA etkisi | Aynı ekip geliştirdi ve değerlendirdi | Orta | Orta `[çıkarım]` | Geliştirmeyen bir ekibe bağımsız inceleme yaptır. |

Zayıf bulgu: "Doğrulama yanlılığı olabilir." Güçlü bulgu: "Yalnızca olumlu pilot geri bildirimi aktarılmış; katılmayan 6 ekipten veri yok `[VARSAYIM: sayı teyit edilmeli]`."
