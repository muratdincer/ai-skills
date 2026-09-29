---
description: "Herhangi bir dokümanı açıklık, bütünlük, iç tutarlılık, iddiaların doğruluğu ve hedef kitle ile amaca uygunluk açısından inceler; öncelikli, konumu belirtilmiş bulguları önerilen düzeltmeler ve bir genel kararla verir. Bir taslak için geri bildirim istendiğinde, bir doküman onay veya yayın öncesi kontrol edilecekse ya da bir şartname, teklif, politika, rehber veya rapor için ikinci görüş gerektiğinde kullanılır."
related: "requirements-review-checklist, architecture-review, document-simplify, style-guide-check, doc-diff-summary"
prompt: "Bu olay yönetimi süreç dokümanını operasyon direktörlerine onaya göndermeden önce gözden geçir."
---

# Doküman Gözden Geçirme

## Amaç
Yazara, dokümanı okuyucularına ve desteklemesi gereken karara uygun hâle getirecek, önceliklendirilmiş ve uygulanabilir bulgular vermek; üslup tercihlerinden oluşan bir liste değil.

## Ne zaman kullanılır
- Bir taslak onaya, imzaya veya yayına gitmek üzereyken.
- Yazar geri bildirim veya ikinci bir göz istediğinde.
- Bir tedarikçiden, müşteriden veya başka bir ekipten gelen doküman güvenilmeden önce değerlendirilecekse.

## Ne zaman kullanılmaz
- Doküman, biçimsel kalite kriterleri gerektiren bir gereksinim şartnamesiyse `requirements-review-checklist` kullanılır.
- İçerik, esası açısından değerlendirilecek bir mimariyse `architecture-review` veya `atam-evaluation` kullanılır.
- Yalnızca stil kılavuzuna uygunluk gerekiyorsa `style-guide-check`, yalnızca kısaltma gerekiyorsa `document-simplify` kullanılır.

## Girdiler
Zorunlu:
- Doküman metni.

İsteğe bağlı, kaliteyi artırır:
- Amaç, hedef kitle ve dokümanın sağlaması gereken karar veya aksiyon.
- İnceleme odağı (ör. yalnızca bütünlük), kurum şablonu, ilişkili dokümanlar.
- İnceleme derinliği: hızlı tarama veya tam inceleme.

Doküman yoksa iste. Amaç ve hedef kitle verilmemişse metinden çıkar, çıkarımı `[VARSAYIM]` olarak belirt ve incelemeyi buna göre yap.

## Süreç
1. Amacı, hedef kitleyi ve doküman türünü belirle; bulguların bunlara göre değerlendirilebilmesi için incelemenin başına yaz.
2. Argümanı anlamak için dokümanı yorum yapmadan baştan sona bir kez oku, ardından iki cümlelik bir özet yaz. Yazamıyorsan ilk bulgu açıklıktır.
3. Yapı: sıralama okuyucuya hizmet ediyor mu (sonuç veya talep önde, ayrıntılar arkada)? Başlıklar bilgi veriyor mu?
4. Bütünlük: doküman türünün gerektirdiği bölümleri (ör. kapsam, sorumlular, istisnalar, tarihler, başarı kriterleri, geri alma) ve hedef kitlenin soracağı ama cevaplanmamış soruları kontrol et.
5. Tutarlılık: sayıları, isimleri, tarihleri, terimleri ve ifadeleri bölümler, tablolar ve diyagramlar arasında karşılaştır; çelişkileri iki konumuyla birlikte listele.
6. Doğruluk ve dayanak: kanıtsız iddiaları, kaynaksız rakamları ve bilinen standartlarla veya verilen bağlamla çelişen ifadeleri işaretle. Doğrulayamadığın olguları iddia etme; bunun yerine soru sor.
7. Açıklık: belirsiz kelimeleri (uygun, hızlıca vb.), tanımlanmamış kısaltmaları, eylemi yapanı gizleyen edilgen cümleleri ve iki işi birden yapan paragrafları bul.
8. Hedef kitleye uygunluk: jargon düzeyi, uzunluk, ton ve her okuyucu grubu için gereken aksiyonların açık olup olmadığı.
9. Her bulguyu sınıflandır: Kritik (amacı engelliyor veya yanlış), Önemli (okuyucu yanlış anlayacak veya soru soracak), Küçük (cilalama). Konumu, sorunu ve somut bir düzeltme veya yeniden yazım önerisini ver.
10. Genel bir karar ver: hazır, küçük değişikliklerle hazır veya yeniden çalışılmalı; ayrıca ilk üç aksiyonu yaz.
11. Kullanıcının hedefi devam ediyorsa ana bulgu uzunluk veya jargon ise `document-simplify`, gereksinim dokümanları için `requirements-review-checklist` öner.

## Çıktı formatı
```markdown
# İnceleme: <doküman başlığı / sürüm>
Amaç (varsayım mı?): <...> | Hedef kitle: <...> | Karar: <Hazır / Küçük değişiklik / Yeniden çalışma>
Doküman özeti: <2 cümle>

## İlk 3 Aksiyon
1. ...

## Bulgular
| # | Önem | Konum | Sorun | Önerilen düzeltme |
|---|---|---|---|---|
| 1 | Kritik | §3.2 | <...> | <yeniden yazım veya aksiyon> |

## Yazara Sorular
- ...

## Korunması Gereken Güçlü Yönler
- ...
```

## Kalite kontrol listesi
- [ ] Her bulgunun bir konumu ve yalnızca şikâyet değil somut bir düzeltmesi var.
- [ ] Önem dereceleri amaca ve hedef kitleye etkiyle gerekçelendirilmiş.
- [ ] Çelişkiler iki konumu da belirtiyor.
- [ ] Yeni olgu eklenmemiş; doğrulanamayan iddialar soruya dönüştürülmüş.
- [ ] Genel karar Kritik ve Önemli bulgularla tutarlı.
- [ ] Yorumlar yazara değil dokümana odaklı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kritik sorunları elli yazım hatası yorumunun arasında boğmak. Küçük sorunları grupla, amacı engelleyenle başla.
- Dokümanı amacına ve hedef kitlesine göre değil kendi tercih ettiğin yapıya göre incelemek.
- İncelemek yerine bütün dokümanı yeniden yazmak. Hedefli yeniden yazımlar öner; tam yeniden yazımı yalnızca istenirse sun.

## Örnek
Girdi: Operasyon direktörleri için olay yönetimi süreci taslağı.

Çıktıdan bir bölüm:
- Karar: Küçük değişiklik. Özet: üretim olayları için önem seviyelerini ve eskalasyon yollarını tanımlıyor.
- | 1 | Kritik | §4 tablosu ile §2 metni | Sev-1 müdahale süresi §2'de 15 dk, §4'te 30 dk | Tek değere hizala; servis sahibiyle teyit et |
- | 2 | Önemli | §5 | Olayı kapatma ve postmortem'i başlatma sorumlusu yok | "Olay komutanı olayı kapatır ve `[TBD]` gün içinde postmortem planlar" ifadesini ekle |
