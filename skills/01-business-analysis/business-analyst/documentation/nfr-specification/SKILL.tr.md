---
name: nfr-specification
description: "Fonksiyonel olmayan gereksinimleri kalite karakteristikleri (performans, erişilebilirlik/kesintisizlik, güvenilirlik, güvenlik, mahremiyet, kullanılabilirlik, erişilebilirlik, bakım yapılabilirlik, uyumluluk, taşınabilirlik, işletilebilirlik, mevzuat uyumu) boyunca; her biri metrik, hedef, ölçüm koşulu, doğrulama yöntemi ve kaynakla ölçülebilir ifadeler olarak tanımlar. Kalite beklentileri muğlak olduğunda ('hızlı', 'güvenli', '7/24'), BRD veya FRD'de NFR eksik olduğunda ya da 'NFR tanımla' dendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: documentation
  title: "Fonksiyonel olmayan gereksinimleri tanımlama"
  related: "frd-writing, nfr-to-architecture, slo-definition, security-requirements, performance-test-plan"
  prompt: "Yeni müşteri self-servis portalımız için NFR'leri tanımla; iş birimi sadece hızlı, güvenli ve her zaman açık olmalı dedi."
---

# Fonksiyonel Olmayan Gereksinimleri Tanımlama

## Amaç
Kalite beklentilerini sahibi ve kaynağı belli, ölçülebilir ve doğrulanabilir gereksinimlere çevirmek; böylece mimari, test ve operasyon sıfatlar üzerine tartışmak yerine bunlara göre tasarlayıp kanıtlayabilir.

## Ne zaman kullanılır
- Paydaşlar kaliteyi sıfatlarla ifade ettiğinde: hızlı, ölçeklenebilir, güvenli, hep açık, kolay kullanılır.
- Bir BRD veya FRD tamamlanırken kalite nitelikleri eksik veya test edilemez olduğunda.
- Bir tedarikçi sözleşmesi, SLA veya mimari karar kalite hedeflerine ihtiyaç duyduğunda.

## Ne zaman kullanılmaz
- Hedeflerin mimari taktiklere çevrilmesi gerekiyorsa `nfr-to-architecture` kullanılır.
- Çalışan bir servis için hizmet seviyesi hedefleri ve hata bütçeleri gerekiyorsa `slo-definition` kullanılır.
- Ayrıntılı bir güvenlik kontrol seti gerekiyorsa `security-requirements` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki sistem veya özellik ve şimdiye kadar dile getirilen kalite beklentileri (muğlak olsalar bile).

İsteğe bağlı, kaliteyi artırır:
- Beklenen kullanıcı ve yük, çalışma saatleri ve kritik dönemler, mevzuat (KVKK/GDPR, sektör kuralları), mevcut SLA'lar, mevcut sistem ölçümleri, kurumun NFR tabanı.

Kapsam yoksa iste. Eksik hedefler için sayı uydurma: `[VARSAYIM]` olarak bir aday aralık öner ve onu netleştirecek soruyu yaz.

## Süreç
1. Girdideki her kalite ifadesini topla ve alıntıla; kimin söylediğini ve onun için neden önemli olduğunu not et.
2. Her birini, kontrol listesi olarak ISO/IEC 25010'u kullanarak bir kalite karakteristiğine eşle: performans verimliliği, güvenilirlik/kesintisizlik, güvenlik, kullanılabilirlik/erişilebilirlik, bakım yapılabilirlik, uyumluluk, taşınabilirlik; bunlara mahremiyet, işletilebilirlik/gözlemlenebilirlik ve mevzuat uyumunu ekle.
3. Kimsenin bahsetmediği karakteristikler için listeyi dolaş ve bunları `[TBD]` gereksinim ya da gerekçeli "uygulanamaz" olarak ekle.
4. Her ifadeyi ölçülebilir bir gereksinim olarak yeniden yaz: metrik, hedef, ölçüm koşulu (yük, yüzdelik, dönem, lokasyon, veri hacmi) ve kapsam (hangi fonksiyon veya arayüz).
5. Ortalama yerine yüzdelik ve aralıkları tercih et ("500 eşzamanlı kullanıcıda p95 ≤ 2 sn") ve tepe yük senaryosunu açıkça yaz.
6. Kesintisizlik ve kurtarma için hizmet saatlerini, izin verilen kesintiyi, RTO ve RPO'yu ayrı ayrı belirt; "7/24"ü %100 ile eşitleme.
7. Güvenlik ve mahremiyet için geçerli standarda (OWASP ASVS seviyesi, KVKK/GDPR veri minimizasyonu, saklama süresi) ve ilgili kişisel veri kategorilerine referans ver.
8. Kullanılabilirlik ve erişilebilirlik için doğrulanabilir bir hedef koy (WCAG 2.2 AA, görev başarı oranı, desteklenen cihaz ve diller).
9. Her NFR'ye bir doğrulama yöntemi (yük testi, sızma testi, denetim, erişilebilirlik denetimi, izleme), bir sahip ve öncelik ata; çatışmaları (ör. katı saklama süresi ile analitik ihtiyacı) ödünleşim olarak işaretle.
10. Kaynağı olmayan her aday hedefi `[VARSAYIM]` olarak etiketle ve onu teyit edecek soruyu ve muhatabı listele.
11. Hedef devam ediyorsa tasarım taktikleri için `nfr-to-architecture`, operasyonel hedefler için `slo-definition`, doğrulama için `performance-test-plan` öner.

## Çıktı formatı
```markdown
# Fonksiyonel Olmayan Gereksinimler: <sistem / özellik>
Kapsam: <fonksiyonlar, arayüzler> · Kaynaklar: <dokümanlar, paydaşlar>

| ID | Karakteristik | Gereksinim | Metrik ve hedef | Koşul | Doğrulama | Öncelik | Kaynak |
|---|---|---|---|---|---|---|---|
| NFR-PERF-01 | Performans | ... | p95 ≤ ... | ... | Yük testi | Olmalı | ... |

## Uygulanamaz (gerekçesiyle)
## Ödünleşimler ve Çatışmalar
## Varsayımlar ve Açık Sorular
- [VARSAYIM] <aday hedef> — <muhatap> ile teyit et
```

## Kalite kontrol listesi
- [ ] Her NFR'nin metriği, hedefi ve ölçüm koşulu var; sıfat kalmadı.
- [ ] ISO/IEC 25010 karakteristiklerinin tamamı ile mahremiyet, işletilebilirlik ve mevzuat uyumu kapsandı ya da gerekçeyle uygulanamaz işaretlendi.
- [ ] Kesintisizlik; hizmet saatlerini, kesintiyi, RTO ve RPO'yu ayrı ayrı belirtiyor.
- [ ] Her NFR'nin bir doğrulama yöntemi ve sahibi var.
- [ ] Hiçbir hedef kaynaksız olarak uzlaşılmış gibi sunulmadı; adaylar `[VARSAYIM]`.
- [ ] İlgili yerlerde kişisel veri kategorileri ve minimizasyon/saklama ihtiyaçları belirlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Arkasındaki yük, yüzdelik veya maliyet olmadan genel hedefleri kopyalamak ("%99,99", "1 saniye"). Her sayıyı bir senaryoya ve kaynağa bağla.
- Yüzdelik yerine ortalama kullanmak. 1 sn'lik ortalama, kullanıcının hissettiği 10 sn'lik kuyruğu gizleyebilir.
- Canlıya geçişten önce kimsenin test edemeyeceği NFR'ler yazmak. Doğrulama yöntemini şimdi ekle, yoksa gereksinim sessizce düşer.

## Örnek
Girdi: "Portal hızlı, güvenli ve her zaman erişilebilir olmalı."

Zayıf: "Sistem hızlı ve yüksek erişilebilir olmalıdır."

Güçlü:
| ID | Gereksinim | Metrik ve hedef | Koşul | Doğrulama |
|---|---|---|---|---|
| NFR-PERF-01 | Fatura listesi sayfası hızlı yanıt verir | p95 ≤ 2 sn `[VARSAYIM]` | 500 eşzamanlı kullanıcı, ay sonu tepe yükü `[TBD: tepe yükü teyit et]` | Yük testi |
| NFR-AVL-01 | Portal hizmet saatlerinde erişilebilir | Aylık ≥ %99,5 `[VARSAYIM]`, RTO 4 saat, RPO 15 dk `[TBD]` | Duyurulan bakımlar hariç 7/24 | İzleme |
| NFR-SEC-01 | Kimlik doğrulama ve oturum kontrolleri | OWASP ASVS Seviye 2 | Tüm dışa açık uç noktalar | Sızma testi |

Açık soru: Ay sonunda portalın bir saat kapalı kalmasının iş maliyeti nedir? — Müşteri hizmetleri direktörü
