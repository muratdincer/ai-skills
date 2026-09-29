---
name: rollback-plan
description: "Bir sürüm veya değişiklik için ölçülebilir tetikleyiciler, karar sahibi ve son saati, bileşen bazlı adımlar, veri ve şema konuları, ileri düzeltme alternatifleri ve geri dönüş sonrası doğrulama içeren bir geri dönüş planı yazar. Bir üretim değişikliği onaylanmadan önce, değişiklik migration'lar veya geri alınamaz adımlar içerdiğinde ya da bir sürümün nasıl geri alınacağı sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Geri dönüş planı"
  related: "deployment-checklist, release-plan, deployment-strategy, schema-migration-plan, backup-restore-plan"
  prompt: "Sipariş servisini yükselten ve sipariş durum kolonunu metinden enum tablosuna taşıyan sürümümüz için bir geri dönüş planı yaz."
---

# Geri Dönüş Planı Yazma

## Amaç
Bir değişikliğin ne zaman ve nasıl geri alınacağına, bu arada yazılan verinin ne olacağı dahil, önceden karar vermek. Böylece başarısız bir sürüm, yorgun ve baskı altındaki kişiler tarafından hızla geri alınabilir.

## Ne zaman kullanılır
- Bir üretim değişikliği onay gerektirdiğinde ve test edilmiş bir geri dönüş yolu göstermesi gerektiğinde.
- Değişiklik şema veya veri migration'ı, yapılandırma veya altyapı değişikliği ya da dış sözleşme değişikliği içerdiğinde.
- Önceki bir geri dönüş başarısız olduğunda, çok uzun sürdüğünde veya veriyi bozduğunda.

## Ne zaman kullanılmaz
- Yayına alma mekanizmasının kendisini seçmek (canary, blue-green) için `deployment-strategy` kullanılır.
- Migration adımlarını ayrıntılı tasarlamak için `schema-migration-plan` kullanılır.
- Bir sürümü geri almak yerine felaket sonrası geri yükleme için `dr-plan` veya `backup-restore-plan` kullanılır.

## Girdiler
Zorunlu:
- Değişiklik: bileşenler, sürümler, yapılandırma ve varsa veri veya şema değişiklikleri.
- Nasıl dağıtıldığı (pipeline, manuel, kod olarak altyapı).

İsteğe bağlı, kaliteyi artırır:
- SLO'lar ve kilit metrikler, dağıtım stratejisi, feature flag imkânı.
- Yedekleme ve geri yükleme imkânı ve son test edilen geri yükleme.
- Diğer ekiplere, dış sistemlere veya istemci uygulamalara bağımlılıklar.

Veri veya şema değişiklikleri bilinmiyorsa sor; geri dönüşün mümkün olup olmadığını bunlar belirler. Diğer eksikler açık soru olur.

## Süreç
1. Her değişikliği geri alınabilirliğe göre sınıflandır: durumsuz ve geri alınabilir (binary, yapılandırma), dikkatle geri alınabilir (ekleme yapan şema, flag'ler), geri alınamaz veya kayıplı (yıkıcı migration, gönderilmiş e-posta veya ödeme gibi dış yan etkiler, veri formatı dönüşümleri).
2. Tetikleyicileri SLO'lara veya iş metriklerine bağlı ölçülebilir koşullar olarak gözlem pencereleriyle tanımla (hata oranı, gecikme, başarısız işlemler, veri bütünlüğü kontrolü); bir de genel "sürüm sorumlusunun kararı" maddesi ekle.
3. Karar sahibini, danışılması gereken kişileri ve özellikle geri dönüşsüz noktadan önce bir karar son saatini belirt.
4. Her bileşen için mekanizmayı seç: trafik geçişi, önceki artefaktı yeniden dağıtma, flag kapatma, yapılandırmayı geri alma, altyapıyı geri alma veya bir düzeltmeyle ileri gitme (roll forward).
5. Veriyi açıkça ele al: yeni sürümün yazdığı satırlara ne olacak; eski sürüm onları okuyabiliyor mu; ters migration veya telafi script'i gerekiyor mu; geri yükleme gerekiyor mu ve hangi veri kaybını (RPO) doğurur.
6. Geri dönüş adımlarını ters bağımlılık sırasıyla diz; her birine sorumlu, bilinmiyorsa `[TBD]` olarak tahmini süre ve doğrulama ver.
7. Yan kanalları kapsa: cache'ler, yeni formatta mesaj içeren kuyruklar, zamanlanmış işler, arama indeksleri, zaten güncellenmiş istemci uygulamalar, iş ortağı entegrasyonları.
8. Geri dönüş sonrası doğrulamayı ve iletişimi (iç, destek, müşteriler, durum sayfası) tanımla.
9. İleri düzeltmenin ne zaman tercih edileceğini (ör. geri alınamaz bir migration sonrası) ve neyi gerektirdiğini belirt.
10. Geri dönüşün prova edildiğine dair kanıt iste ya da edilmediğini risk olarak yaz.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa durdurma koşullarını yerleştirmek için `deployment-checklist`, migration'ı geri alınabilir kılmak için `schema-migration-plan` veya onay kararı için `go-no-go` öner.

## Çıktı formatı
```markdown
# Geri Dönüş Planı: <değişiklik/sürüm>
Karar sahibi: <ad veya [TBD]> · Karar son saati: <saat veya adım> · Prova edildi: evet/hayır

## Geri Alınabilirlik
| Bileşen | Değişiklik | Sınıf (geri alınabilir / dikkatle / geri alınamaz) | Notlar |

## Tetikleyiciler
| Sinyal | Eşik | Pencere | Kaynak |
- Ek olarak: sürüm sorumlusunun kararı.

## Geri Dönüş Adımları
| # | Adım | Sorumlu | Tahmini süre | Doğrulama |

## Veri Konuları
- Yeni sürümün yazdığı veri: ...
- Ters migration / telafi: ...
- Geri yükleme gerekli mi: evet/hayır – beklenen veri kaybı: ...

## Yan Kanallar
- Kuyruklar, cache'ler, işler, istemciler, iş ortakları: ...

## İleri Düzeltme Seçeneği
## Doğrulama ve İletişim
## Riskler, Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her tetikleyici eşik ve pencereyle ölçülebilir ya da `[TBD]` olarak işaretli.
- [ ] Dağıtımdan sonra yazılan veri açıkça ele alındı.
- [ ] Geri alınamaz adımlar belirlendi ve karar son saati bunlardan önce.
- [ ] Adımlar ters bağımlılık sırasında, her birinin sorumlusu ve doğrulaması var.
- [ ] Prova durumu belirtildi; prova edilmemiş geri dönüş risk olarak listelendi.
- [ ] Hiçbir süre, eşik veya isim uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Planın tamamının "önceki sürümü yeniden dağıt" olması. Önceki binary yeni veriyi veya şemayı okuyamayabilir.
- "Bir şeyler ters giderse" gibi tetikleyiciler. Kararın hızlı olması için her tetikleyiciyi bir metriğe ve pencereye bağla.
- Kuyruklarda yeni formatta bekleyen mesajları unutmak. Boşalt, dönüştür veya eski tüketicileri toleranslı yap.

## Örnek
Girdi: "Sipariş servisi v5 ve order_status'u metinden durum tablosuna çeviren migration."

Çıktıdan bir bölüm:
- Geri alınabilirlik: metin kolonu aynı sürümde silinirse migration geri alınamaz → böl: v5'te metin kolonunu koru ve çift yaz, silmeyi sonraki bir sürümde yap `[VARSAYIM: ekip iki aşamayı kabul ediyor]`.
- Tetikleyici: 10 dk boyunca başarısız sipariş oluşturma oranı `[TBD]` % üzerinde veya metin ile durum tablosu arasında herhangi bir bütünlük uyuşmazlığı.
- Veri: v5'te oluşturulan siparişler her iki kolona da yazılır, böylece geri dönüşten sonra v4 onları okuyabilir.
