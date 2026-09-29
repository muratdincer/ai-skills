---
name: retention-policy
description: "Veri setleri veya sistemler için veri saklama politikası tanımlar: yasal veya iş gerekçesiyle saklama süreleri, süreyi başlatan olaylar, arşiv katmanları, silme veya anonimleştirme yöntemleri, hukuki muhafaza (legal hold), yedeklerin ele alınışı ve imha kanıtı. Veri varsayılan olarak süresiz tutuluyorsa, KVKK veya GDPR gibi bir gizlilik mevzuatı saklama sınırlaması istiyorsa, depolama maliyetleri artıyorsa ya da verinin ne kadar süre tutulabileceği veya tutulması gerektiği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-architect
  area: governance
  title: "Veri saklama politikası"
  related: "data-classification, privacy-impact-assessment, backup-restore-plan, policy-writing, data-catalog-entry"
  prompt: "KVKK ve GDPR kapsamında müşteri, sipariş ve uygulama log verilerimiz için saklama politikası tanımla."
---

# Veri Saklama Politikası

## Amaç
Her veri kategorisi için ne kadar süre, neden saklanacağına, zaman içinde nerede duracağına ve nasıl imha edileceğine karar vermek. Böylece kurum yasal alt ve üst sınırlara uyar, ihlal durumundaki maruziyetini sınırlar ve depolama maliyetini kontrol eder.

## Ne zaman kullanılır
- Kimse aksi yönde karar vermediği için veri "sonsuza kadar" tutuluyorsa.
- Bir gizlilik incelemesi, denetim veya düzenleyici kurum saklama sınırlaması ve silme kanıtı istiyorsa.
- Yeni bir sistem veya veri ürünü tasarlanıyor ve yaşam döngüsü tanımlanmalıysa.
- Arşiv veya temizleme kuralı olmadan depolama ya da yedek maliyetleri artıyorsa.

## Ne zaman kullanılmaz
- Verinin hassasiyeti henüz bilinmiyorsa önce `data-classification` kullanılır.
- Bir işleme faaliyetinin tam gizlilik risk değerlendirmesi gerekiyorsa `privacy-impact-assessment` kullanılır.
- Konu yedekleme sıklığı ve geri yükleme prosedürleriyse `backup-restore-plan` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki veri kategorileri veya veri setleri ve iş amaçları.

İsteğe bağlı:
- Sınıflandırma, geçerli yargı alanları ve sektör mevzuatı, mevcut politikalar, sözleşmesel yükümlülükler, yedekler ve replikalar dahil depolama yerleri, hukuki muhafaza süreci.

Amaçlar bilinmiyorsa sor: saklama amaçla gerekçelendirilir. Kullanıcı veya hukuk danışmanı vermedikçe belirli bir yasal saklama süresini kesin bilgi gibi yazma; aksi halde `[HUKUKLA TEYİT EDİLECEK]` olarak işaretle.

## Süreç
1. Veri kategorilerini işe yarar bir ayrıntıda listele (ör. müşteri ana verisi, sipariş ve faturalar, destek kayıtları, uygulama logları, pazarlama izinleri, kamera kayıtları); amaç ve sınıfıyla birlikte.
2. Her kategori için saklama belirleyicilerini çıkar: yasal alt sınır (vergi, ticaret, sektör mevzuatı), yasal üst sınır veya saklama sınırlaması ilkesi (KVKK/GDPR), sözleşmesel, operasyonel ve analitik ihtiyaç. Her belirleyicinin kaynağını kaydet.
3. Süreyi başlatan olayı tanımla (sözleşme bitişi, son aktivite, işlem tarihi, hesap kapanışı); yalnızca "oluşturma tarihi" yetmez.
4. Saklama süresini, gerekçelendirilmiş en uzun alt sınır olarak ve amacın izin verdiğinden uzun olmayacak şekilde belirle; belirleyiciler çelişirse veriyi böl (ör. fatura alanlarını tut, davranışsal alanları anonimleştir).
5. Yaşam döngüsü katmanlarını tanımla: aktif (çevrimiçi), kısıtlı/arşiv (erişim belirli rol ve amaçlarla sınırlı), imha edilmiş. Her katmanın erişim kurallarını belirt.
6. Kategori bazında imha yöntemini tanımla: kalıcı silme, kriptografik imha (crypto-shredding), geri döndürülemez anonimleştirme (takma adlandırma değil) veya toplulaştırma. Türetilmiş kopyaların (veri ambarı, dışa aktarımlar, önbellekler, test ortamları) nasıl kapsandığını açıkla.
7. Yedekleri ve replikaları ele al: yedekler düzenlenmez, kendi döngüleriyle süresi dolar; geri yüklenen veride, yedekten sonra yapılmış silmeler yeniden uygulanmalıdır.
8. Hukuki muhafazayı tanımla: kimin koyup kaldırabileceği, imhayı nasıl askıya aldığı ve nasıl kayıt altına alındığı.
9. Uygulama ve kanıtı tanımla: otomatik temizleme işleri veya manuel prosedür, sıklık, sayılarla silme logları, istisna yönetimi ve politikanın periyodik gözden geçirilmesi.
10. Kategori bazında sahiplik ata (veri sahibi onaylar, teknik sahip uygular); varsayımları ve açık soruları listele. Hedef devam ediyorsa resmileştirmek için `policy-writing`, yedek süresini hizalamak için `backup-restore-plan` veya her veri setinde saklama bilgisini yayımlamak için `data-catalog-entry` öner.

## Çıktı formatı
```markdown
# Veri Saklama Politikası: <kapsam>
Yargı alanları: <...> | Sahip: <...> | Gözden geçirme döngüsü: <...>

## Saklama Çizelgesi
| Kategori | Amaç | Sınıf | Belirleyici(ler) ve kaynak | Başlatan olay | Aktif | Arşiv | Toplam | İmha yöntemi | Sahip |
|---|---|---|---|---|---|---|---|---|---|

## Türetilmiş Kopyalar ve Yedekler
- <veri ambarı, dışa aktarımlar, test verisi, yedekler: saklamanın nasıl uygulandığı>

## Hukuki Muhafaza
- <yetki, süreç, kayıt>

## Uygulama ve Kanıt
- <işler/prosedürler, sıklık, silme logu, istisnalar>

## Varsayımlar ve Açık Sorular
- [HUKUKLA TEYİT EDİLECEK] ...
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her süre bir belirleyiciye ve kaynağına dayanıyor; hiçbir yasal süre uydurulmadı.
- [ ] Her kategorinin yalnızca süresi değil, başlatan olayı da var.
- [ ] İmha yöntemi tanımlı ve anonimleştirme gerçekten geri döndürülemez.
- [ ] Türetilmiş kopyalar, test ortamları ve yedekler kapsandı.
- [ ] Hukuki muhafaza imhayı askıya alabiliyor ve denetlenebilir.
- [ ] Kişisel veri, amacının gerektirdiğinden uzun tutulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bütün bir sistem için tek saklama süresi. Farklı alanların çoğu zaman farklı belirleyicileri vardır; kategori veya alan grubuna göre böl.
- Canlı ortamdan silip veri ambarından, loglardan, dışa aktarımlardan ve test kopyalarından silmemek.
- Takma adlandırılmış veriyi anonim saymak. Eldeki başka verilerle yeniden tanımlanabiliyorsa hâlâ kişisel veridir.

## Örnek
Girdi: "Müşteri, sipariş ve uygulama log verisi; KVKK ve GDPR kapsamında faaliyet gösteriyoruz."

Çıktıdan bir bölüm:
- Sipariş ve faturalar: belirleyici vergi/ticari kayıt tutma yükümlülüğü `[HUKUKLA TEYİT EDİLECEK: süre]`; başlatan olay işlemin mali yılının sonu; 2 yıl sonra arşiv `[VARSAYIM]`; ardından kalıcı silme.
- Uygulama logları: yalnızca operasyonel ihtiyaç; 90 gün aktif `[VARSAYIM]`; IP ve kullanıcı kimliği alımda maskelenir; günlük temizleme işi silinen kayıt sayısını loglar.
- Pazarlama izni kayıtları: izin kullanıldığı sürece ve ispat süresi boyunca saklanır `[HUKUKLA TEYİT EDİLECEK]`.
