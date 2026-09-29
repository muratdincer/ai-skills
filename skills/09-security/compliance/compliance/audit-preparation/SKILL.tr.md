---
description: "Bir ekibi iç, sertifikasyon, müşteri veya düzenleyici denetimine hazırlar: kapsamı ve kriterleri teyit eder, sorumlu ve teslim tarihli kanıt talep listesi oluşturur, hazırlık eksiklerini kontrol eder, denetim haftasını ve denetlenenlerin bilgilendirilmesini planlar. Bir denetim tarihi açıklandığında (ISO 27001, SOC 2, KVKK, PCI DSS, BDDK, müşteri denetimi), denetçi talep listesi gönderdiğinde veya önceki bulgular bir sonraki denetimden önce kapatılmalıysa kullanılır."
related: "control-mapping, access-review, policy-writing, it-risk-assessment, schedule-plan"
prompt: "ISO 27001 gözetim denetimimiz altı hafta sonra. Kanıt listesini, eksikleri ve planı hazırla."
---

# Denetime Hazırlık

## Amaç
Açıklanan bir denetimi kontrollü bir projeye dönüştürmek: herkes hangi kanıtın beklendiğini, kimin ne zamana kadar teslim edeceğini, hangi eksiklerin önce kapatılacağını ve görüşmelerin nasıl yürütüleceğini bilir. Böylece denetim sürpriz ve önlenebilir bulgu üretmez.

## Ne zaman kullanılır
- Bir denetim veya değerlendirme tarihi belirlendiğinde: sertifikasyon, gözetim, SOC 2 incelemesi, KVKK denetimine hazırlık, PCI DSS değerlendirmesi, müşteri denetimi.
- Denetçi bir talep listesi ("prepared by client" listesi) gönderdiğinde ve listenin dağıtılıp takip edilmesi gerektiğinde.
- Önceki denetim bulguları veya uygunsuzluklar bir sonraki ziyaretten önce kapatılıp kanıtlanmalıysa.

## Ne zaman kullanılmaz
- Önce hangi kontrollerin standardı karşıladığını bilmeniz gerekiyorsa `control-mapping` kullanılır.
- Bulgu, var olmayan bir politikaysa `policy-writing` kullanılır.
- Kanıtın kendisi periyodik bir yetki gözden geçirmesiyse `access-review` kullanılır.

## Girdiler
Zorunlu:
- Denetim türü, standart veya kriterler ve denetim tarihi ya da dönemi.

İsteğe bağlı, kaliteyi artırır:
- Kapsam (tüzel kişilikler, lokasyonlar, sistemler, süreçler), işletim etkinliği denetimleri için denetim dönemi.
- Denetçinin talep listesi, önceki denetim raporu ve açık bulgular, Uygulanabilirlik Bildirgesi, kontrol eşlemesi.
- Ekip müsaitliği ve bilinen uygun olmayan tarihler.

Denetim türü veya tarihi yoksa iste. Geri kalan her şey `[TBD]` veya açık soru olur.

## Süreç
1. Kapsamı, kriterleri, standart sürümünü, denetim dönemini (SOC 2 Type II için gözlem dönemi), denetim tarihlerini, denetçiyi ve denetim tarzını (uzaktan/yerinde, örnekleme yaklaşımı) teyit et.
2. Kanıt listesini oluştur: her gereksinim veya talep kalemi için kanıt dokümanı, kayıt sistemi, kapsanan dönem, sorumlu, teslim tarihi ve durum. Denetçinin listesi varsa ondan, yoksa kontrol eşlemesinden başla.
3. Yoğun incelenen alanlara öncelik ver: yönetim sistemi maddeleri (risk değerlendirmesi, iç denetim, yönetimin gözden geçirmesi), erişim yönetimi, değişiklik yönetimi, olay yönetimi, tedarikçi yönetimi, yedekleme/geri yükleme, loglama, farkındalık eğitimi.
4. Her kanıt kaleminde hazırlık kontrolü yap: mevcut mu, dönem için eksiksiz mi, tarihli mi, onaylı mı, politika ifadesiyle tutarlı mı. Eksikleri Yok, Eksik veya Tutarsız olarak sınıflandır.
5. Eksikler için sorumlu ve tarihli düzeltme planla. Şimdi meşru biçimde yapılabilecek olanı (ör. geciken bir gözden geçirmeyi yapmak) geriye tarihlenemeyecek olandan ayır; kanıtı asla geriye dönük üretme veya değiştirme.
6. Önceki bulguları kontrol et: her birinin kök nedeni, düzeltici faaliyeti, uygulama kanıtı ve etkinlik kanıtı var mı.
7. Kanıtlardaki kişisel veriyi en aza indir: T.C. kimlik numaralarını, maaşları ve sağlık verilerini maskele; tam döküm yerine örnek paylaş; denetçinin güvenli kanalını kullan.
8. Denetim lojistiğini hazırla: alan bazında oturum takvimi, her oturum için görüşülecek kişi ve yedeği, kanıt odası veya paylaşımlı klasör yapısı, tek irtibat kişisi, talep takip kaydı.
9. Görüşülecek kişileri bilgilendir: sorulana yanıt ver, anlatmak yerine kanıt göster, emin değilsen "kontrol edip döneceğim" de, takip taleplerini kaydet.
10. Bugünden denetim gününe haftalık kontrol noktaları olan bir takvim oluştur; denetimden bir-iki hafta önce bir prova veya iç ön denetim ekle.
11. Kullanıcının teyit etmediği her durumu `[VARSAYIM]` olarak işaretle; eşleme yoksa `control-mapping`, belirli eksikler için `access-review` veya `policy-writing` öner.

## Çıktı formatı
```markdown
# Denetime Hazırlık: <denetim türü, standart> – <tarihler>
## Kapsam ve Kriterler
- Kapsam: ... / Dönem: ... / Denetçi: [TBD] / Biçim: uzaktan / yerinde
## Kanıt Takibi
| # | Gereksinim / talep | Kanıt | Sistem / konum | Dönem | Sorumlu | Teslim | Durum (Hazır/Eksik) |
## Eksikler ve Düzeltme
| # | Eksik türü | Açıklama | Aksiyon | Sorumlu | Tarih | Denetimden önce kapanabilir mi? |
## Önceki Bulgular
| Bulgu | Düzeltici faaliyet | Etkinlik kanıtı | Durum |
## Denetim Takvimi ve Görüşülecek Kişiler
| Gün / saat | Alan | Görüşülecek kişi | Yedek |
## Denetim Gününe Kadar Takvim
- Hafta -6: ... / Hafta -2: iç prova / Hafta 0: denetim
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her kanıt kaleminin sorumlusu, teslim tarihi ve kapsaması gereken dönemi var.
- [ ] Eksikler sınıflandırıldı ve hiçbiri geriye tarihleme veya kanıt uydurma ile "kapatılmadı".
- [ ] Önceki bulguların her biri yalnızca yapılan aksiyonu değil etkinlik kanıtını da gösteriyor.
- [ ] Kanıtlardaki kişisel veriler maskelendi veya örneklendi.
- [ ] Takvim denetim gününden önce bir prova içeriyor.
- [ ] Teyit edilmeyen durumlar ve tarihler `[VARSAYIM]` veya `[TBD]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kanıtları denetimden bir hafta önce toplayıp kontrolün aylardır işlemediğini keşfetmek. İşe dönem kapsaması kontrolüyle başla.
- Fazla paylaşım: örnek yerine tüm İK veya müşteri veri setini göndermek. Gereken en azını paylaş ve neyin paylaşıldığını kaydet.
- Görüşülen kişilerin tahmin yürütmesi. Onları kesin yanıt verecek ve kanıt gösterecek şekilde bilgilendir.
- Denetimi bir dokümantasyon işi sanmak. Kontrol işlemiyorsa bunu eksik olarak kaydet ve gerçekten düzelt.

## Örnek
Girdi: "ISO 27001 gözetim denetimi altı hafta sonra; geçen yıl tedarikçi gözden geçirmelerinde minör uygunsuzluk almıştık."

Çıktıdan bir bölüm:
| 7 | A.5.22 tedarikçi hizmetlerinin izlenmesi | Yıllık tedarikçi gözden geçirme kayıtları | GRC klasörü / Tedarikçiler | Son 12 ay | Satın alma lideri [VARSAYIM] | Hafta -4 | Eksik: 11 kritik tedarikçiden 3'ü gözden geçirilmemiş |
| Önceki NC-02 tedarikçi gözden geçirmeleri | Gözden geçirme şablonu devreye alındı | Tüm kritik tedarikçiler için tamamlanmış gözden geçirmeler | Açık – etkinlik henüz gösterilmedi |
