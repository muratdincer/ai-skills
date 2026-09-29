---
description: "Kaynak materyaldeki alan terimlerini, kısaltmaları ve çok anlamlı kelimeleri çıkarır; eş anlamlılar, yasaklı kullanımlar ve sorumlularla birlikte belirsizlik içermeyen, test edilebilir tanımlar yazar. Bir projede, dokümanda veya ekipte terminoloji tutarsızsa, kişiler bir alana alıştırılırken, gereksinim veya veri modeli yazılırken ya da sözlük veya ortak dil istendiğinde kullanılır."
related: "business-rules-catalog, bounded-context-map, technical-translation, data-catalog-entry, ambiguity-detection"
prompt: "Bu gereksinim notlarından bir sözlük oluştur; müşteri, cari, hesap ve abone kelimeleri birbirinin yerine kullanılıyor."
---

# Sözlük Oluşturma

## Amaç
Her terimin bağlam başına tek bir anlama sahip olduğu ortak bir kelime dağarcığı oluşturmak. Böylece gereksinimler, kod, veri ve konuşmalar birbirinden kopmaz ve belirsizlikten doğan hatalar önlenir.

## Ne zaman kullanılır
- Kaynak dokümanlarda tek kavram için birden fazla kelime ya da birden fazla kavram için tek kelime kullanılıyorsa.
- Yeni bir alan, ürün veya müşteri projesi başlıyor ve ortak bir dile ihtiyaç varsa.
- Gereksinimler, veri modelleri veya API'ler yazılıyor ve önce isimlerin sabitlenmesi gerekiyorsa.
- Bir çeviri veya yerelleştirme çalışması üzerinde anlaşılmış terim çiftlerine ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- Alanı farklı dillere sahip modellere bölmek gerekiyorsa önce `bounded-context-map` kullanılır, ardından her bağlam için ayrı sözlük oluşturulur.
- Tek bir veri seti veya tablo dokümante edilecekse `data-catalog-entry` kullanılır.
- Bir gereksinim dokümanındaki belirsiz cümleleri bulmak gerekiyorsa `ambiguity-detection` kullanılır.

## Girdiler
Zorunlu:
- Kaynak materyal (doküman, not, döküm, şema, ekran) veya bir terim listesi.

İsteğe bağlı, kaliteyi artırır:
- Sözlüğün ait olduğu alan veya bounded context.
- Uyum sağlanacak mevcut sözlükler, standartlar veya mevzuattaki tanımlar.
- Tanımları teyit edebilecek alan uzmanları.

Kaynak materyal veya terim listesi yoksa iste. Bir alan terimini yalnızca genel bilgiyle tanımlarsan `[VARSAYIM]` olarak işaretle.

## Süreç
1. Kaynakta aday terimleri tara: büyük harfle yazılan isimler, kısaltmalar, alana özgü fiiller (ör. "mahsuplaştırmak", "aktive etmek"), durumlar, roller, birimler ve tanımlayıcılar.
2. Genel kelimeleri ele; bir yeni gelenin yanlış okuyabileceği veya iki kişinin makul biçimde farklı tanımlayabileceği terimleri tut.
3. Eş anlamlıları ve sesteşleri grupla: farklı kelimelerin tek kavramı, tek kelimenin birkaç kavramı karşıladığı yerleri not et.
4. Her kavram için tercih edilen bir terim seç; alternatifleri eş anlamlı veya kullanımdan kaldırılmış terim olarak listele.
5. Tanımı cins-ayırt edici özellik biçiminde yaz: "<Terim>, <ayırt edici özellikleri> olan bir <üst sınıf>tır." Döngüsel tanımdan kaçın, terimi kendi tanımında kullanma.
6. Terimin ne olmadığını (en yakın karıştırılan kavram), ilgiliyse yaşam döngüsünü veya durumlarını ve bir örneği ekle.
7. Her tanım için bağlamı (alan, sistem, mevzuat) ve kaynağı kaydet; yasal veya standart bir tanım varsa adıyla referans ver.
8. Sınırlı kanıttan çıkarılmış tanımları `[VARSAYIM]` olarak işaretle ve teyit için muhtemel bir sorumlu ata.
9. Alfabetik sırala, kısaltmaları aç, ilişkili terimleri birbirine bağla.
10. Karar gerektiren çelişkileri listele (ör. "Satış ve Faturalama aktif müşteriyi farklı tanımlıyor").
11. Kullanıcının hedefi devam ediyorsa tanımlara gizlenmiş kurallar için `business-rules-catalog`, sözlüğün iki dilli olması gerekiyorsa `technical-translation` öner.

## Çıktı formatı
```markdown
# Sözlük: <alan / bağlam>
Kapsam: <sözlüğün kapsadığı alan> | Kaynaklar: <kullanılan dokümanlar> | Durum: taslak

| Terim | Tanım | Karıştırılmaması gereken | Eş anlamlı / kullanımdan kalkmış | Örnek | Kaynak | Sorumlu |
|---|---|---|---|---|---|---|
| <Tercih edilen terim> | <cins + ayırt edici özellik> | <en yakın kavram> | <alternatifler> | <...> | <doküman/bölüm> | <rol veya [TBD]> |

## Kısaltmalar
- <KIS>: <açılım> — bkz. <terim>

## Çözülmesi Gereken Terim Çelişkileri
1. <terim> — <A anlamı (kim)> ile <B anlamı (kim)> — <önerilen çözüm> — <karar verici>
```

## Kalite kontrol listesi
- [ ] Her kavramın tek bir tercih edilen terimi var; eş anlamlılar ayrı tanımlanmamış, listelenmiş.
- [ ] Hiçbir tanım döngüsel değil veya tanımlanan terimi içermiyor.
- [ ] Her tanım terimi en yakın karıştırılan kavramdan ayırıyor.
- [ ] Her tanımın kaynağı var ya da `[VARSAYIM]` olarak işaretli.
- [ ] Çelişkiler sessizce çözülmemiş, görünür kılınmış.
- [ ] Kısaltmalar açılmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca örnekle tanımlamak ("Müşteri, ör. ACME"). Önce sınıfı ve ayırt edici ölçütü ver, sonra örneği.
- Bağlamlar gerçekten farklıyken kurum genelinde tek tanım dayatmak. Tanımları bağlam bazında kapsamla ve eşlemeyi belirt.
- Her ismi sözlüğe almak. Kimsenin okumadığı uzun bir sözlük, yirmi keskin maddeden daha kötüdür.

## Örnek
Girdi: "Müşteri", "cari", "hesap" ve "abone" kelimelerini birbirinin yerine kullanan gereksinim notları.

Çıktıdan bir bölüm:
- | Müşteri | Şirketle en az bir sözleşme imzalamış tüzel veya gerçek kişi | Hesap (faturalama yapısı) | cari (kullanımdan kalkmış) | ACME A.Ş. | Notlar §2 | Satış operasyon `[TBD]` |
- | Hesap | Bir veya daha fazla aboneliği tek fatura adresi altında toplayan faturalama yapısı | Müşteri | — | ACC-1042 | Notlar §4 | Faturalama |
- Çelişki: "aktif müşteri" — Satış: son 12 ayda sözleşme imzalamış; Faturalama: ödenmemiş veya açık faturası olan — ürün sahibinin kararı gerekiyor.
