---
description: "Gereksinimleri, user story'leri veya kabul kriterlerini test edilebilirlik açısından inceler; belirsiz, ölçülemez, eksik, test edilemez veya hata davranışı tanımlanmamış maddeleri her biri için somut bir yeniden yazım önerisiyle işaretler. Test tasarımı veya tahminden önce, refinement oturumlarında ya da gereksinimlerin test için yeterince net olup olmadığı sorulduğunda kullanılır."
related: ambiguity-detection, acceptance-criteria, requirements-review-checklist, test-scenarios-from-requirements, nfr-specification
prompt: "Test case yazmaya başlamadan önce bu 8 user story'yi test edilebilirlik açısından kontrol et."
---

# Gereksinimlerin Test Edilebilirlik İncelemesi

## Amaç
Kimse test tasarlamadan veya kod yazmadan önce doğrulanamayan gereksinimleri yakalamak ve her bulguyu somut bir soruya ya da yeniden yazıma dönüştürerek beklenen davranışı kontrol edilebilir kılmak.

## Ne zaman kullanılır
- Gereksinimler, story'ler veya kabul kriterleri refinement, tahmin veya test aşamasına girmek üzere.
- Test uzmanları koşum sırasında sürekli "burada ne olmalı?" sorusuyla karşılaşıyor.
- Fonksiyonel olmayan gereksinimlerde "hızlı", "güvenli", "kullanıcı dostu" gibi ifadeler var.

## Ne zaman kullanılmaz
- Tüm bir doküman için genel dilsel belirsizlik taraması gerekiyorsa `ambiguity-detection` kullanılır.
- Kabul kriterleri sıfırdan yazılacaksa `acceptance-criteria` kullanılır.
- Standart bir kontrol listesine göre tam doküman incelemesi gerekiyorsa `requirements-review-checklist` kullanılır.

## Girdiler
Zorunlu:
- Gereksinim, story veya kabul kriteri metni.

İsteğe bağlı, kaliteyi artırır:
- Alan sözlüğü, iş kuralları, arayüz taslakları, ilgili fonksiyonel olmayan gereksinimler.
- Bilinen kısıtlar (roller, veri hacimleri, entegrasyonlar).

Gereksinim metni yoksa iste.

## Süreç
1. Bulguların atıf yapabilmesi için her gereksinimi veya kriteri numaralandır.
2. Her maddeyi test edilebilirlik ölçütlerine göre kontrol et: gözlemlenebilir sonuç, ölçülebilir eşik, tanımlı girdiler ve ön koşullar, tanımlı aktör/rol, tek davranış (atomik), iç çelişki olmaması.
3. Belirsiz ifadeleri işaretle: hızlı, kolay, uygun, vb., bazı, tüm (sınırsız), -meli (isteğe bağlı mı?), gerektiğinde, kullanıcı dostu, güvenli.
4. Eksik davranışı kontrol et: hata ve doğrulama durumları, boş/null veri, sınırlar (maksimum uzunluk, boyut, adet), eşzamanlılık, yetkiler, saat dilimleri ve tarihler, yerelleştirme.
5. Fonksiyonel olmayan gereksinimlerde metrik, hedef, ölçüm koşulu (ör. belirtilen yük altında p95 gecikme) ve doğrulama yöntemi olup olmadığını kontrol et.
6. Belirtilmemiş kurallara veya davranışı tanımlanmamış dış sistemlere bağımlılıkları kontrol et.
7. Her bulguyu sınıflandır: Belirsiz, Ölçülemez, Eksik, Test edilemez (gözlemlenebilir sonuç yok), Çelişkili, Negatif yol eksik.
8. Önem derecesini test tasarımını ne kadar engellediğine göre belirle: Engelleyici, Büyük, Küçük.
9. Her bulgu için yeniden yazım veya net bir soru öner. Önerilen eşikleri `[VARSAYIM]` ile işaretle; asla kararlaştırılmış gibi sunma.
10. Özetle: madde bazında test edilebilirlik durumu (Test edilebilir / Sorularla test edilebilir / Test edilemez) ve ürün sahibine sorulacak öncelikli sorular.
11. Çıkarımla yapılan her yorumu `[VARSAYIM]` ile işaretle; kullanıcı devam ederse zayıf maddeleri düzeltmek için `acceptance-criteria`, maddeler test edilebilir olunca `test-scenarios-from-requirements` öner.

## Çıktı formatı
```markdown
# Test Edilebilirlik İncelemesi: <kapsam>
Özet: <n> madde incelendi · <n> test edilebilir · <n> netleştirme gerekli · <n> test edilemez

| # | Gereksinim (kısa) | Bulgu türü | Önem | Sorun | Önerilen yeniden yazım / soru |
|---|---|---|---|---|---|

## Tanımlanması Gereken Eksik Senaryolar
- <madde #>: <eksik hata, sınır veya yetki davranışı>

## Ürün Sahibine Sorular (önceliğe göre)
1. ...
```

## Kalite kontrol listesi
- [ ] Her bulgu belirli bir maddeye atıf yapıyor ve sorunlu ifadeyi alıntılıyor.
- [ ] Her bulgunun bir yeniden yazımı veya somut bir sorusu var.
- [ ] Önerilen sayılar `[VARSAYIM]` ile işaretli.
- [ ] Her madde için negatif yollar, sınırlar ve yetkiler kontrol edildi.
- [ ] Bulgular çözüm tercihi değil doğrulanabilirlikle ilgili.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Test edilebilirlik yerine üslubu işaretlemek. Yalnızca bir testin geçti/kaldı kararı verebilmesini etkileyen konuları yükselt.
- Yeniden yazımda çözüm (arayüz tasarımı) önermek. Yalnızca gözlemlenebilir davranışı tanımla.
- Örtük fonksiyonel olmayan gereksinimleri kaçırmak; ör. veri hacmi veya sayfalama davranışı belirtilmemiş bir liste ekranı.

## Örnek
Girdi: "US-3: Kullanıcı olarak müşterileri hızlıca arayabilmeli ve ilgili sonuçları görebilmeliyim."

Çıktıdan bir bölüm:
| 3 | Müşteri arama | Ölçülemez + Belirsiz | Engelleyici | "hızlıca" ve "ilgili" için ölçüt yok | "1 milyon müşteri varken ad önekiyle (en az 3 karakter) arama, ilk sayfayı (20 satır) p95'te 1 sn içinde döndürür `[VARSAYIM]`; sonuçlar önce tam eşleşme, sonra alfabetik sıralanır." |
- Eksik: sonuç dönmeyen arama, özel karakterler, müşteri görüntüleme yetkisi olmayan kullanıcılar.
