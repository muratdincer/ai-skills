---
description: Kapsam içi ve dışı işleri, kabul kriterleriyle teslimatları, kısıtları, varsayımları ve hariç tutulanları tanımlayan, değişiklik kontrolü için baz çizgisi oluşturan proje kapsam tanımını yazar. Başlatma belgesi hazır olduğunda kapsamın planlama, tahmin ve sözleşme yapılabilecek netliğe getirilmesi gerektiğinde ya da kapsam kaymasına karşı açık bir referans gerektiğinde kullanılır.
related: project-charter, wbs, change-control, acceptance-certificate, statement-of-work
prompt: Bu başlatma belgesine ve çalıştay notlarına göre müşteri self-servis portalı projesi için kapsam tanımı yaz.
---

# Kapsam Tanımı Yazma

## Amaç
Planlama, tahmin, sözleşme ve sonraki değişiklik kararlarının aynı tanıma dayanması için neyin teslim edilip neyin edilmeyeceğini belirsizliğe yer bırakmadan ortaya koyan bir kapsam baz çizgisi oluşturmak.

## Ne zaman kullanılır
- Başlatma belgesi onaylandıktan sonra, WBS ve takvimden önce.
- Paydaşlar neyin dahil olduğu konusunda anlaşamadığında.
- Bir tedarikçi sözleşmesi veya iç taahhüt imzalanmadan önce.

## Ne zaman kullanılmaz
- Proje henüz yetkilendirilmemişse önce `project-charter` kullanılır.
- Ticari koşulları olan sözleşmesel kapsam gerekiyorsa `statement-of-work` kullanılır.
- Yinelemeli bir MVP için ürün düzeyinde kapsam gerekiyorsa `mvp-scoping` kullanılır.

## Girdiler
Zorunlu:
- Başlatma belgesi, iş durumu ya da hedeflerin ve ana teslimatların tanımı.

İsteğe bağlı, kaliteyi artırır:
- Gereksinim dokümanları, çalıştay notları, mevcut sözleşmeler.
- Kurumsal kısıtlar (standartlar, platformlar, mevzuat).
- Sponsorla üzerinde anlaşılmış hariç tutmalar.

Hedef veya teslimat tanımı yoksa iste.

## Süreç
1. Proje hedeflerini çıkar ve ürün/hizmet tanımını 3-5 cümlede yeniden yaz.
2. Teslimatları isim olarak listele ("müşteri veritabanını taşımak" değil "taşınmış müşteri veritabanı"). Proje yönetimi teslimatlarını da ekle (eğitim, dokümantasyon, devir).
3. Her teslimat için doğrulanabilir kabul kriterleri yaz ve kabul edeni belirt.
4. Hariç tutulanları açıkça yaz. Tipik gri alanları sorgula: veri taşıma, eski sistemin kapatılması, eğitim, hypercare, entegrasyonlar, raporlama, yerelleştirme, üretim dışı ortamlar.
5. Kısıtları (tarih, bütçe, teknoloji, mevzuat, kaynak) kaynağıyla kaydet.
6. Varsayımları, teyit edebilecek sahibi ve yanlış çıkarsa etkisiyle kaydet.
7. Kapsam sınırlarını arayüzleriyle tanımla: hangi sistemler, birimler ve coğrafyalar etkileniyor.
8. Kapsam değişikliklerinin nasıl ele alınacağını yaz ve değişiklik kontrol yoluna referans ver.
9. Desteklenmeyen her öğeyi `[BİLİNMİYOR]` veya `[VARSAYIM]` olarak işaretle, açık soruları listele.
10. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: teslimatları ayrıştırmak için `wbs`, temel onaylandıktan sonra `change-control`.

## Çıktı formatı
```markdown
# Kapsam Tanımı: <proje>
Sürüm <x> | Tarih <tarih> | Baz referansı <başlatma belgesi no>

## Ürün / Hizmet Tanımı
## Teslimatlar ve Kabul Kriterleri
| No | Teslimat | Kabul kriteri | Kabul eden |
## Kapsam İçi
## Kapsam Dışı (Hariç Tutulanlar)
## Sınırlar ve Arayüzler
## Kısıtlar
| Kısıt | Kaynak |
## Varsayımlar
| Varsayım | Teyit edecek kişi | Yanlışsa etkisi |
## Kapsam Değişikliği Yönetimi
## Açık Sorular
## Onay
```

## Kalite kontrol listesi
- [ ] Her teslimat bir isim ve doğrulanabilir kabul kriterine sahip.
- [ ] Kapsam dışı listesi tipik gri alanları kapsıyor.
- [ ] Her varsayımın sahibi ve etkisi var.
- [ ] Tanımsız belirsiz ifade yok ("vb.", "gerektiği kadar", "kullanıcı dostu").
- [ ] Hiçbir şey uydurulmadı; boşluklar işaretli.
- [ ] Değişiklik yönetimi somut bir yola referans veriyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Teslimat yerine faaliyet listelemek; bu durumda WBS ve kabul izlenemez.
- Sessiz hariç tutmalar. Kapsam dışı diye yazılmamışsa paydaşlar dahil sanar.
- "Doğru çalışır" gibi kabul kriterleri. Test sonuçlarına, metriklere veya dokümanlara bağla.

## Örnek
Girdi: "Self-servis portal: müşteriler faturalarını görecek ve iletişim bilgilerini güncelleyecek. Başlatma belgesine göre canlıya geçiş 6 ay sonra."

Çıktıdan bir bölüm:
| T-03 | Fatura geçmişi sayfası (son 24 ay) | Örneklenen 50 hesapta faturalama sistemiyle birebir aynı faturaları gösterir | Finans sorumlusu |
- Kapsam dışı: Online ödeme, fatura itirazları, yerel mobil uygulamalar, 24 aydan eski faturaların taşınması `[teyit et]`.
- Varsayım: Faturalama sistemi fatura API'si sunuyor — Sahip: Faturalama BT — Yanlışsa: ek entegrasyon işi, tarih riskte.
