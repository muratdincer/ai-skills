---
description: "Kurumun mevcut kontrollerini, süreçlerini ve kanıtlarını ISO/IEC 27001 Ek A veya SOC 2 Trust Services Criteria gibi bir hedef standarda eşler; kapsama oranını, kanıt eksiklerini ve diğer çerçevelerle örtüşmeleri gösterir. Sertifikasyona hazırlanırken, müşteri güvenlik anketini yanıtlarken, çerçeveleri birleştirirken (ISO 27001, SOC 2, KVKK, PCI DSS) veya bir kontrolün gerçekten denetim kanıtı üretip üretmediğini kontrol ederken kullanılır."
related: "audit-preparation, policy-writing, it-risk-assessment, access-review, traceability-matrix"
prompt: "Mevcut kontrollerimizi ISO 27001:2022 Ek A'ya eşle ve hangilerinin kanıtı olmadığını göster."
---

# Kontrolleri Standarda Eşleme

## Amaç
Hedef standardın her gereksinimi için hangi iç kontrolün onu karşıladığını, kontrolün işlediğini hangi kanıtın gösterdiğini, sorumlusunu ve eksikleri gösteren izlenebilir bir kontrol-gereksinim matrisi üretmek. Böylece sertifikasyon veya denetim çalışması varsayımlara değil olgulara dayanarak planlanır.

## Ne zaman kullanılır
- ISO/IEC 27001 sertifikasyonuna veya SOC 2 Type I/II incelemesine hazırlanırken.
- Bir müşteri veya düzenleyici güvenlik anketi gönderdiğinde ve yanıtların gerçek kontrollere dayanması gerektiğinde.
- Birden fazla çerçeve geçerli olduğunda (ISO 27001, SOC 2, KVKK teknik ve idari tedbirleri, PCI DSS, BDDK) ve ekip tek bir kontrol setini hepsine eşlemek istediğinde.
- Bir yeniden yapılanma veya araç değişikliğinden sonra hangi kontrollerin sorumlusunu ya da kanıtını kaybettiğini görmek için.

## Ne zaman kullanılmaz
- Denetim tarihi belli ve kanıt planı ile takvim gerekiyorsa `audit-preparation` kullanılır.
- Kontrol henüz yok ve yazılması gerekiyorsa `policy-writing` kullanılır.
- Hangi risklerin hangi kontrolleri gerektirdiğine karar vermeniz gerekiyorsa `it-risk-assessment` kullanılır.

## Girdiler
Zorunlu:
- Hedef standart ve sürümü (ör. ISO/IEC 27001:2022 Ek A, revize odak noktalarıyla SOC 2 TSC 2017).
- Mevcut kontrollerin, politikaların veya prosedürlerin tanımı (liste, politika seti, önceki denetim raporu veya serbest metin).

İsteğe bağlı, kaliteyi artırır:
- BGYS kapsamı veya SOC 2 için sistem sınırı.
- Uygulanabilirlik Bildirgesi (SoA), risk kaydı, önceki denetim bulguları.
- Çapraz eşlenecek diğer çerçeveler.

Standart veya kontrol tanımı yoksa iste. Ücretli standart metnini birebir kopyalama; gereksinim numaralarına ve kısa özetlere atıf yap.

## Süreç
1. Hedef standardı, sürümü ve kapsam sınırını (tüzel kişilikler, lokasyonlar, sistemler, hizmetler) teyit et. Kapsam dışı alanları açıkça yaz.
2. Mevcut kontrolleri bir kontrol listesine dönüştür: numara, kısa ifade, tür (önleyici/tespit edici/düzeltici), niteliği (manuel/otomatik), sıklık, sorumlu.
3. Hedef standardın gereksinimlerini numarası ve kısa özetiyle listele. ISO 27001 için Ek A'nın yanında 4-10. maddeleri de ekle; SOC 2 için ortak kriterleri ve seçilen ek kategorileri ekle.
4. Her gereksinimi bir veya daha fazla kontrole eşle. Kapsamayı puanla: Tam, Kısmi, Yok veya Uygulanamaz (gerekçesiyle; ISO 27001'de bu SoA'yı besler).
5. Her eşleme için tasarım ve işletim etkinliğini kanıtlayan delili adlandır: doküman/kayıt, kayıt sistemi, örnekleme dönemi, üreten kişi. Belge olmadan "bunu yapıyoruz" bir eksiktir.
6. Kanıt kalitesi sorunlarını işaretle: tarihsiz ekran görüntüleri, manuel kayıtlar, yalnızca talep üzerine üretilen kanıtlar, sorumlusu olmayan kontroller.
7. Başka çerçeveler de kapsamdaysa aynı kontrol ve kanıtı yeniden kullanmak için sütun ekle (bir kez test et, çok yerde karşıla). Gereksinimlerin gücü farklıysa eşdeğerlik varsayma; kısmi örtüşmeleri işaretle.
8. Eksikleri gereksinim bazında özetle; önerilen düzeltme (yeni kontrol, güçlendirilmiş kontrol, yeni kanıt kaynağı), sorumlu ve denetim riskine göre öncelik ekle.
9. Görülen kanıta değil anlatıma dayanan her kapsama puanını `[VARSAYIM]` olarak işaretle ve kontrol sorumlusu bazında açık soruları listele.
10. Devret: kanıt toplamayı planlamak için `audit-preparation`, eksik politikalar için `policy-writing`, hariç tutmaları gerekçelendirmek için `it-risk-assessment`.

## Çıktı formatı
```markdown
# Kontrol Eşleme: <standart, sürüm> – <kapsam> (<tarih>)
## Kapsam
- Kapsam içi: ... / Kapsam dışı: ...
## Kontrol Envanteri
| Kontrol No | İfade | Tür | Manuel/Otomatik | Sıklık | Sorumlu |
## Eşleme Matrisi
| Gereksinim No | Özet | Kontrol No(ları) | Kapsama | Kanıt (doküman, sistem, dönem) | Diğer çerçeveler | Notlar |
## Eksikler ve Düzeltme
| Gereksinim No | Eksik | Önerilen aksiyon | Sorumlu | Öncelik |
## Uygulanamazlık Gerekçeleri
- <gereksinim no> – gerekçe
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Seçilen standart sürümünün her gereksinimi bir kez ve bir kapsama puanıyla yer alıyor.
- [ ] Her Tam veya Kısmi puan bir niyeti değil somut bir kanıtı adlandırıyor.
- [ ] Uygulanamaz maddelerin kapsam veya riske bağlı gerekçesi var.
- [ ] Her kontrolün bir sorumlusu var ya da `[BİLİNMİYOR]` ile işaretli.
- [ ] Ücretli standart metni birebir kopyalanmadı.
- [ ] Gücü farklı olan çerçeveler arası örtüşmeler kısmi olarak işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kontrol yerine politikayı eşlemek. Politika ifadesi kontrolün işlediğinin kanıtı değildir; prosedürü ve kayıtlarını eşle.
- ISO 27001:2013 ile 2022 kontrol numaralarını karıştırmak. Sürümü teyit et ve numaralandırmayı tutarlı kullan.
- Araç var diye Tam puan vermek. Aracın sayılması için yapılandırma kanıtı ve gözden geçirme kayıtları gerekir.
- Yönetim sistemi maddelerini (risk işleme, iç denetim, yönetimin gözden geçirmesi) unutup yalnızca Ek A'yı eşlemek.

## Örnek
Girdi: "VPN'de MFA kullanıyoruz, çeyreklik erişim gözden geçirmesini tabloda yapıyoruz, haftalık yedek alıyoruz. ISO 27001:2022'ye eşle."

Çıktıdan bir bölüm:
| A.5.18 | Erişim haklarının verilmesi, gözden geçirilmesi, kaldırılması | AC-03 çeyreklik erişim gözden geçirmesi | Kısmi | Çeyrek başına gözden geçirme tablosu [VARSAYIM: onay kanıtı yok] | SOC 2 CC6.2 (kısmi) | Kaldırmaların uygulandığına dair kanıt yok |
| A.8.13 | Bilgi yedekleme | OPS-02 haftalık yedek | Kısmi | Yedekleme işi logları | – | Geri yükleme testi kanıtı yok |
