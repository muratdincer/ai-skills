---
name: requirements-gap-analysis
description: "Bir gereksinim setini (BRD, FRD, kullanıcı hikayeleri, use case'ler) inceler ve eksikleri tespit eder: akışlar, aktörler ve roller, uç durumlar, hata yönetimi, veri kuralları, fonksiyonel olmayan gereksinimler ve geçiş ihtiyaçları. Gereksinimler tamam görünse de sınanmamışsa, tahmin veya onaydan önce ya da 'neyi atlıyoruz?' sorusu sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: quality
  title: "Gereksinimlerde eksik bulma"
  related: "ambiguity-detection, requirements-consistency-check, requirements-review-checklist, nfr-specification, error-scenario-catalog"
  prompt: "Kredi başvuru modülünün FRD'si ekte. Tahmine göndermeden önce eksikleri bul."
---

# Gereksinimlerde Eksik Bulma

## Amaç
Eksik gereksinimleri değişiklik talebi, hata veya yeniden iş olarak ortaya çıkmadan önce görünür kılmak. Çıktı, her eksik için somut bir soru veya önerilen gereksinim içeren önceliklendirilmiş bir eksik listesidir.

## Ne zaman kullanılır
- Bir gereksinim dokümanı veya hikaye seti tahmine, onaya ya da tasarıma gitmek üzereyken.
- Paydaşlar "her şey yazılı" dese de yalnızca mutlu yol (happy path) tarif edilmişse.
- Mevcut bir özelliğe yeni bir kanal, rol veya bölge eklenirken.

## Ne zaman kullanılmaz
- Sorun eksik içerik değil muğlak ifadeyse `ambiguity-detection` kullanılır.
- Gereksinimler birbiriyle çelişiyorsa `requirements-consistency-check` kullanılır.
- Mevcut ve hedef süreç karşılaştırılıyorsa `process-gap-analysis` kullanılır.

## Girdiler
Zorunlu:
- Gereksinim metni (doküman, hikaye listesi, use case'ler).

İsteğe bağlı, kaliteyi artırır:
- Kapsamı hedeflere göre kontrol etmek için iş hedefleri veya talep dokümanı.
- Süreç modeli, veri modeli, ekran listesi veya entegrasyon listesi.
- Uygulanacak mevzuat (ör. KVKK/GDPR, sektör düzenlemeleri).

Gereksinim metni yoksa iste. Diğer her şeyi eksik olabilecek bağlam olarak ele al ve çıktıda belirt.

## Süreç
1. Envanter çıkar: metindeki aktörleri, iş nesnelerini, use case/hikayeleri, ekranları, raporları, entegrasyonları ve belirtilen NFR'leri listele.
2. Hedef kapsamını kontrol et: her iş hedefi en az bir gereksinimle karşılanmalı, her gereksinim bir hedefe bağlanmalı.
3. Her akışı CRUD+yaşam döngüsü merceğiyle yürü: oluşturma, okuma, güncelleme, silme/arşivleme, onay/ret, iptal, yeniden açma, süre dolumu. İş nesnesi bazında eksik yaşam döngüsü aksiyonlarını not et.
4. Her akışı istisna merceğiyle yürü: geçersiz girdi, zaman aşımı, kısmi hata, mükerrer gönderim, eşzamanlı düzenleme, dış sistemin kapalı olması, yetkisiz erişim.
5. Aktör, rol ve yetkileri kontrol et: kim neyi yapabilir, vekâlet, yedek kişi, yönetici/back-office, denetçi, batch/sistem aktörleri; ayrıca tetikleyiciler, ön/son koşullar, destek/operasyon (izleme, runbook ihtiyacı) ve raporlama/denetim izi.
6. Veriyi kontrol et: zorunlu alanlar, doğrulama kuralları, varsayılanlar, hesaplamalar, yuvarlama, referans veri sahipleri, saklama süresi, kişisel verinin maskelenmesi.
7. Sınırları kontrol et: hacimler, limitler, saat dilimleri, para birimleri, diller, tarih kesimleri, ay/yıl sonu.
8. NFR kategorilerini kontrol et: performans, erişilebilirlik (availability), güvenlik, gizlilik, denetlenebilirlik, erişilebilirlik (WCAG 2.2), kullanılabilirlik, işletilebilirlik, ölçeklenebilirlik.
9. Geçiş ihtiyaçlarını kontrol et: veri göçü, paralel çalışma, eğitim, iletişim, geri dönüş (rollback), eski sistemin kapatılması.
10. Her bulguyu ABSENT (hiç geçmiyor), WEAK (geçiyor ama karar verilebilir veya test edilebilir değil) ya da DEFERRED (açıkça ertelenmiş) olarak sınıflandır, kanıtı alıntıla ve belirsizliğin üstünü örtme. Etkiyi geç bulunmasının maliyetine göre (Yüksek/Orta/Düşük) puanla; bir soru ya da `[VARSAYIM]` işaretli aday gereksinim yaz.
11. Kullanıcı devam etmek isterse WEAK maddeler için `ambiguity-detection`, eksik kalite nitelikleri için `nfr-specification` veya eksik hata davranışları için `error-scenario-catalog` öner.

## Çıktı formatı
```markdown
# Gereksinim Eksik Analizi: <doküman / kapsam>
İncelenen: <doküman adı, sürüm> · Kapsam dayanağı: <hedefler / süreç / veri modeli / yok>

## Özet
<3-5 satır: genel bütünlük, en önemli 3 risk>

## Eksik Listesi
| # | Kategori | Konum (bölüm/hikaye) | Eksik | Sınıf (ABSENT/WEAK/DEFERRED) | Etki | Soru veya önerilen gereksinim | Sorumlu |
|---|---|---|---|---|---|---|---|
| E1 | İstisna akışı | UC-03 | Kredi bürosuna ulaşılamadığında davranış yok | ABSENT | Yüksek | Başvuru sahibi ne görmeli, başvuru kaydedilebilir mi? | Ürün sahibi |

## Kapsam Kontrolü
| Hedef / Alan | Karşılayan gereksinim | Durum (Karşılandı / Kısmi / Eksik) |
|---|---|---|

## İnceleme Kapsamı Dışında
- <neyin kontrol edilmediği ve nedeni>
```

## Kalite kontrol listesi
- [ ] Her eksik bir konuma işaret ediyor ya da "hiçbir yerde yok" diyor.
- [ ] Her eksik için "netleştir" yerine somut bir soru veya aday gereksinim var.
- [ ] Önerilen gereksinimler teyit edilene kadar `[VARSAYIM]` olarak işaretli.
- [ ] Yalnızca fonksiyonel akışlar değil, NFR ve geçiş kategorileri de kontrol edildi.
- [ ] Etki puanları sezgiyle değil sonuca göre gerekçelendirildi.
- [ ] Kişisel veri geçen yerlerde veri işleme eksikleri işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Hangi kararın eksik olduğunu söylemeden genel eksikler yazmak ("güvenlik tanımlı değil"). Eksik kararı tam adıyla belirt, ör. oturum zaman aşımı, onaylayan rol.
- Eksikleri kapatmak için iş kuralı uydurmak. Aday olarak öner ve bir sorumluya yönlendir.
- Ana aktörün mutlu yolunda durmak; back-office, batch ve denetçi rolleri genellikle kör noktadır.

## Örnek
Girdi: "Müşteri kredi başvurusunu online yapar; sistem kredi skorunu kontrol eder; yetkili onaylar; müşteri bilgilendirilir."

Çıktıdan bir bölüm:
| # | Kategori | Konum | Eksik | Sınıf (ABSENT/WEAK/DEFERRED) | Etki | Soru veya önerilen gereksinim | Sorumlu |
|---|---|---|---|---|---|---|---|
| E1 | İstisna akışı | Kredi kontrolü | Skorlama servisi hata verirse davranış yok | ABSENT | Yüksek | Kuyruğa alıp yeniden denensin mi, manuel skorlamaya mı düşsün? | Kredi risk |
| E2 | Yaşam döngüsü | Başvuru | Müşteri başvurusunu geri çekemiyor | ABSENT | Orta | [VARSAYIM] Müşteri yetkili kararına kadar başvuruyu geri çekebilir | Ürün sahibi |
| E3 | Rol | Onay | Limite bağlı onay veya yedek yetkili yok | WEAK | Yüksek | Hangi tutarlar ikinci onay gerektiriyor? | Operasyon |
