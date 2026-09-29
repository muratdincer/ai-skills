---
name: release-plan
description: "Sürüm içeriğini, dondurma ve geçiş noktalarını içeren takvimi, isimli sorumluları, bağımlılıkları, iletişimi ve geri dönüş karar noktasını netleştiren bir sürüm planı yazar. Bir sürüm birden fazla ekip, bileşen veya ortamı kapsadığında, değişiklik penceresi gerektirdiğinde ya da sürüm takvimi, geçiş planı veya sürüm akışı istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: release-manager
  area: release
  title: "Sürüm planı yazma"
  related: "deployment-checklist, rollback-plan, go-no-go, release-notes, change-request-rfc"
  prompt: "4.2 sürümü için sürüm planı yaz: üç servis, bir veritabanı migration'ı ve bir mobil uygulama güncellemesi var, hedef üretim tarihi önümüzdeki perşembe gecesi."
---

# Sürüm Planı Yazma

## Amaç
Neyin yayına çıkacağı, her adımın ne zaman yapılacağı, kimin sorumlu olduğu ve sürümün nasıl durdurulacağı veya geri alınacağı konusunda herkese tek ve üzerinde anlaşılmış bir görünüm sağlamak. Böylece sürüm gecesi doğaçlama değil koordineli ilerler.

## Ne zaman kullanılır
- Sürüm birden fazla ekip, servis, veritabanı veya istemci uygulamadan değişiklik içerdiğinde.
- Sürüm bir değişiklik penceresi, müşteri bildirimi veya dış onay gerektirdiğinde.
- Önceki sürümler kaçan bağımlılıklar veya belirsiz sorumluluklar yüzünden kaydığında ya da başarısız olduğunda.

## Ne zaman kullanılmaz
- Yalnızca dağıtımın adım adım kontrolleri gerekiyorsa `deployment-checklist` kullanılır.
- Soru tek bir servisin kullanıcıya nasıl ulaşacağıysa (canary, blue-green) `deployment-strategy` kullanılır.
- Soru önümüzdeki aylarda hangi özelliklerin hangi sürüme gireceğiyse `release-planning` kullanılır.

## Girdiler
Zorunlu:
- Sürüm tanımlayıcısı ve dahil edilen değişikliklerin veya iş kalemlerinin listesi.
- Üretim için hedef tarih veya pencere.

İsteğe bağlı, kaliteyi artırır:
- Etkilenen bileşenler ve ortamlar, dağıtım sırası kısıtları, veritabanı veya veri migration'ları.
- Ekip ve sorumlu isimleri, onaylayıcılar, değişiklik yönetimi süreci.
- Kaçınılması gereken iş olayları (kampanyalar, ay sonu kapanışı, yoğun saatler), müşteri taahhütleri.
- Önceki sürümlerin retrospektifleri veya olayları.

Değişiklik listesi veya hedef pencere yoksa sor. Bilinmeyen sorumlular veya tarihler asla uydurulmaz; açık soruyla birlikte `[TBD]` olarak yazılır.

## Süreç
1. İçerik envanterini çıkar: her değişiklik için bileşen, sorumlu, risk (gerekçeli Yüksek/Orta/Düşük), feature flag durumu ve veriye veya dış sözleşmelere dokunup dokunmadığı.
2. Bağımlılıkları ve sırayı belirle: koddan önce şema, istemciden önce backend, tüketiciden önce sağlayıcı; dış bağımlılıkları (tedarikçiler, uygulama mağazası incelemesi, iş ortağı ekipler) işaretle.
3. Dağıtımı yayından ayır: hangi değişikliklerin flag arkasında karanlık yayınlandığını ve ne zaman açılacağını listele.
4. Takvimi üretim penceresinden geriye doğru kur: kod dondurma, sürüm adayı kesimi, test/staging onayı, go/no-go, dağıtım adımları, doğrulama, hypercare bitişi.
5. Pencereyi iş takvimi ve kadroyla karşılaştır: yoğun yük veya kritik iş olaylarıyla çakışma yok; kilit sorumlular müsait; nöbetçi haberdar.
6. Tek bir sürüm sorumlusu (karar yetkisi) ve her adım için bir isimli sorumlu ata; kritik adımlara yedek sorumlu ekle.
7. Go/no-go giriş kriterlerini ve geri dönüşsüz noktayı (ör. geri alınamaz bir migration sonrası) ve ondan önceki geri dönüş karar son saatini tanımla.
8. İletişimi planla: kime, neyin, ne zaman söyleneceği (iç ekipler, destek, müşteriler, durum sayfası); "tamamlandı" ve "geri alındı" mesajları dahil.
9. Riskleri azaltma önlemleriyle ve bileşen bazlı geri dönüş yaklaşımıyla listele; geri dönüş planına referans ver.
10. Hypercare'i tanımla: süre, izleme odağı, sorumlular, çıkış kriterleri.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa uygulama kontrolleri için `deployment-checklist`, geri alma yolu için `rollback-plan`, karar toplantısı için `go-no-go` veya hedef kitleye yönelik özet için `release-notes` öner.

## Çıktı formatı
```markdown
# Sürüm Planı: <sürüm no>
| Alan | Değer |
|---|---|
| Sürüm sorumlusu | <ad veya [TBD]> |
| Üretim penceresi | <tarih, saat, saat dilimi> |
| Değişiklik kaydı | <no veya [TBD]> |
| Geri dönüşsüz nokta | <adım> – geri dönüş kararı en geç <saat> |

## İçerik
| Değişiklik | Bileşen | Sorumlu | Risk | Flag | Veri/sözleşme etkisi |

## Bağımlılıklar ve Sıra
1. ...

## Takvim
| Ne zaman | Kilometre taşı / adım | Sorumlu | Çıkış kriteri |

## Go/No-Go Kriterleri
- ...

## İletişim
| Ne zaman | Hedef kitle | Kanal | Mesaj | Sorumlu |

## Riskler ve Geri Dönüş
| Risk | Azaltma | Geri dönüş yaklaşımı |

## Hypercare
<süre, izleme odağı, çıkış kriterleri>

## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her değişikliğin bir sorumlusu ve gerekçeli risk derecesi var; bilinmeyen sorumlular `[TBD]`.
- [ ] Dağıtım sırası şema, API ve istemci uyumluluğunu gözetiyor.
- [ ] Geri dönüşsüz nokta açık ve geri dönüş karar son saati ondan önce.
- [ ] Pencere iş olayları ve kadroyla karşılaştırıldı ya da bu kontrol açık soru olarak yazıldı.
- [ ] İletişim yalnızca başlangıcı değil, başarı ve geri dönüş sonuçlarını da kapsıyor.
- [ ] Hiçbir tarih, isim veya süre uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Staging onayı ile üretim arasında hiç pay bırakmayan takvim. Takvimi geriye doğru kur ve başarısız bir aday için tampon bırak.
- Mobil uygulama değişikliklerini sunucu sürümü gibi planlamak. Mağaza inceleme süresi ve sahadaki eski istemci sürümleri geriye uyumlu API gerektirir.
- Sürümün birden fazla "sahibi" olması. Tek bir karar sahibi belirle; diğerleri adımların sahibidir.

## Örnek
Girdi: "4.2 sürümü: sipariş, ödeme ve bildirim servisleri, orders tablosunda bir kolon bölme, iOS/Android güncellemesi. Üretim perşembe 22:00."

Çıktıdan bir bölüm:
- Sıra: expand migration (yeni kolonları ekle, çift yazma) → servisler → mobil mağaza gönderimi; contract adımı 4.3'e ertelendi `[VARSAYIM]`.
- Geri dönüşsüz nokta: migration yalnızca ekleme yaptığı için bu sürümde yok; hypercare boyunca geri dönüş mümkün.
- Açık soru: Mobil build perşembeden önce mağaza incelemesine yetecek kadar erken gönderildi mi? Sorumlu: mobil lider `[TBD]`.
