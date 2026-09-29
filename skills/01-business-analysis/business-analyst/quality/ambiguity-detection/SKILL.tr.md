---
description: "Gereksinim metnini muğlak sözcükler, tanımsız terimler, zayıf veya öznel ifadeler, sınırsız listeler, aktörü belirsiz edilgen cümleler ve test edilemez ifadeler açısından tarar; net yeniden yazımlar önerir. Gereksinimler, kullanıcı hikayeleri veya kabul kriterleri netlik açısından incelenirken ya da testçiler veya geliştiriciler bir gereksinimin birden fazla şekilde okunabildiğini söylediğinde kullanılır."
related: "requirements-gap-analysis, requirements-consistency-check, glossary-builder, acceptance-criteria, testability-review"
prompt: "Bu 20 gereksinimi belirsiz ifadeler açısından kontrol et ve test edilebilir yeniden yazımlar öner."
---

# Belirsiz Gereksinim Tespiti

## Amaç
Her gereksinimin yalnızca tek bir şekilde okunmasını sağlamak; böylece tasarım, geliştirme ve test aynı yorumda buluşur. Çıktı her belirsizliği işaretler, riskini açıklar ve kesin, doğrulanabilir bir yeniden yazım önerir.

## Ne zaman kullanılır
- Bir gereksinim dokümanı veya hikaye seti onaya ya da tahmine gitmeden önce.
- Geliştiriciler, testçiler veya tedarikçiler aynı gereksinimi farklı yorumladığında.
- Gereksinimler sözleşme, RFP veya mevzuattan geliyor ve kabulde kullanılacaksa.

## Ne zaman kullanılmaz
- İçerik muğlak değil eksikse `requirements-gap-analysis` kullanılır.
- Gereksinimler birbiriyle çelişiyorsa `requirements-consistency-check` kullanılır.
- Onay öncesi tam kontrol listesi incelemesi gerekiyorsa `requirements-review-checklist` kullanılır.

## Girdiler
Zorunlu:
- Gereksinim ifadeleri, tercihen ID'leriyle.

İsteğe bağlı, kaliteyi artırır:
- Proje sözlüğü veya alan terimleri.
- "Hızlı", "güvenli" gibi ifadeleri tanımlayan mevcut NFR hedefleri veya SLA'lar.

ID yoksa ifadeleri kendin numaralandır (R1, R2...) ve bunu belirt.

## Süreç
1. Bileşik ifadeleri böl; her bulgu tek bir davranışa ("-meli/-malı") işaret etsin.
2. Muğlak nitelemeleri işaretle: hızlı, kolay, kullanıcı dostu, esnek, sağlam, verimli, yeterli, uygun şekilde, asgari, modern, sorunsuz.
3. Zayıf veya isteğe bağlı kipleri işaretle: -abilir, mümkünse, ideal olarak, çalışılacak, desteklemeli (davranış tanımsızsa).
4. Sınırsız veya açık listeleri işaretle: vb., gibi, bunlarla sınırlı olmamak üzere, ve/veya.
5. Eksik aktör ve tetikleyicileri işaretle: kim/ne/ne zaman belli olmayan edilgen yapılar ("doğrulanır", "gönderilecektir").
6. Tanımsız veya çok anlamlı terimleri işaretle: farklı anlamlarda kullanılan alan terimleri, açılımı verilmemiş kısaltmalar, neyi kastettiği belirsiz zamirler (bu, o, bunlar).
7. Sayısallaştırılmamış miktar ve süreleri işaretle: çok, büyük, hızlıca, gerçek zamanlı, düzenli olarak, anında, 7/24, tüm kullanıcılar.
8. Test edilemez ifadeleri işaretle: mutlak ifadeler (asla, her zaman, %100), kapsamı belirsiz olumsuzlar, öznel memnuniyet.
9. Her bulgu için aktör, eylem, nesne, koşul ve ölçülebilir kriter içeren bir yeniden yazım yap; bilinmeyen değerler uydurulmaz, `[TBD]` yer tutucusu olur.
10. Tanım gerektiren terimleri sözlük aday listesinde topla.
11. Kullanıcı devam etmek isterse eksik içerik için `requirements-gap-analysis`, toplanan terimler için `glossary-builder` veya yeniden yazılan ifadeleri test edilebilir kılmak için `acceptance-criteria` öner.

## Çıktı formatı
```markdown
# Belirsizlik İncelemesi: <doküman / kapsam>

## Özet
<incelenen ifade sayısı, bulgu içeren ifade sayısı, öne çıkan örüntüler>

## Bulgular
| Ger. ID | Orijinal metin | Belirsizlik türü | Neden riskli | Önerilen yeniden yazım | Sahibine soru |
|---|---|---|---|---|---|

## Sözlük Adayları
| Terim | Görülen kullanımlar | Önerilen tanım | Sorumlu |
|---|---|---|---|

## Temiz İfadeler
<bulgu olmayan ID'ler>
```

## Kalite kontrol listesi
- [ ] Her bulgu sorunlu sözcükleri birebir alıntılıyor.
- [ ] Yeniden yazımlar orijinal niyeti koruyor; sessizce kapsam eklenmedi veya çıkarılmadı.
- [ ] Hiçbir sayısal hedef uydurulmadı; bilinmeyen eşikler soruyla birlikte `[TBD]`.
- [ ] Her yeniden yazım test, inceleme, analiz veya gösterimle doğrulanabilir.
- [ ] Tanımsız terimler sözlük adaylarında toplandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Muğlak bir sözcüğü başka bir muğlak sözcükle değiştirmek ("hızlı" yerine "performanslı"). Her zaman ölçülebilir bir kriter veya `[TBD]` yer tutucusu ekle.
- Kurum "-meli" ile "-malı/-abilir" ayrımını bilinçli olarak öncelik için kullanıyorsa her birini hata saymak. Konvansiyonu bir kez sor ve tutarlı uygula.
- Gözlemlenebilir davranış yerine çözüm tasarımı yazmak (ör. "Redis önbellek kullanılacak").

## Örnek
Girdi: "R4: Arama hızlı olmalı ve tüm kullanıcılar için ilgili sonuçları getirmeli."

Çıktıdan bir bölüm:
| Ger. ID | Orijinal metin | Belirsizlik türü | Neden riskli | Önerilen yeniden yazım | Sahibine soru |
|---|---|---|---|---|---|
| R4 | "hızlı olmalı" | Muğlak niteleme | Geçti/kaldı eşiği yok | Sistem, `[TBD]` eşzamanlı kullanıcı altında ilk sonuç sayfasını 95. yüzdelikte `[TBD]` saniye içinde döndürmelidir. | Kabul edilebilir yanıt süresi ve yük nedir? |
| R4 | "ilgili sonuçlar" | Tanımsız terim | İlgililik test edilemez | Sonuçlar `[TBD: sıralama kuralı, ör. önce tam eşleşme, sonra tarihe göre azalan]` şeklinde sıralanmalıdır. | Kullanıcılar nasıl bir sıralama bekliyor? |
