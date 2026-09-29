---
name: security-requirements
description: "Bir sistem veya özellik için OWASP ASVS seviye ve bölümleriyle uyumlu, gerekçesi, doğrulama yöntemi ve önceliği belli, test edilebilir güvenlik gereksinimleri tanımlar. Yeni bir uygulama veya özellik için güvenlik kabul kriterleri gerektiğinde, tehdit modeli backlog kalemlerine dönüştürülecekken ya da müşteri veya denetçi güvenlik gereksinimi temel çizgisi istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: security-engineer
  area: design
  title: "Güvenlik gereksinimleri"
  related: "threat-model, nfr-specification, authn-authz-design, secure-code-review, acceptance-criteria"
  prompt: "Yeni müşteri self-servis portalımız için güvenlik gereksinimlerini tanımla; portal kişisel veri işliyor, ödemeler barındırılan ödeme sayfası üzerinden alınıyor."
---

# Güvenlik Gereksinimleri

## Amaç
Geliştiricilerin üzerine inşa edebileceği, test ekibinin doğrulayabileceği, kısa ve test edilebilir bir güvenlik gereksinimleri seti üretmek. Seti OWASP ASVS'ye bağlayarak kapsamı ve seviyeyi açık hale getirmek.

## Ne zaman kullanılır
- Yeni bir uygulama, API veya önemli bir özellik tasarım ya da backlog iyileştirme aşamasına girdiğinde.
- Tehdit modelinden çıkan önlemlerin gereksinime dönüştürülmesi gerektiğinde.
- İhale, müşteri sözleşmesi veya denetçi belgelenmiş bir güvenlik temel çizgisi istediğinde.

## Ne zaman kullanılmaz
- Hangi tehditlerin olduğu henüz bilinmiyorsa önce `threat-model` kullanılır.
- Genel kalite nitelikleri (performans, erişilebilirlik) gerekiyorsa `nfr-specification` kullanılır.
- Mevcut kod gereksinimlere göre inceleniyorsa `secure-code-review` kullanılır.

## Girdiler
Zorunlu:
- Sistem veya özelliğin tanımı: kullanıcılar, arayüzler, işlenen veriler ve dağıtım şekli.

İsteğe bağlı, kaliteyi artırır:
- Hedef ASVS seviyesi (L1, L2, L3) ya da seviyeyi belirlemek için risk profili.
- Tehdit modeli çıktısı, mevcut güvenlik standartları veya politikalar.
- Mevzuat kapsamı (KVKK/GDPR, PCI DSS, sektörel düzenlemeler), kimlik sağlayıcı, teknoloji yığını.

Sistem tanımı yoksa iste. ASVS seviyesi verilmemişse gerekçesiyle bir seviye öner ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Sistem bağlamını özetle: maruziyet (internet/iç ağ), kullanıcı tipleri, veri sınıfları, entegrasyonlar.
2. ASVS seviyesini seç: düşük risk için L1; kişisel veya iş açısından kritik veri işleyen uygulamalar için varsayılan L2; yüksek değerli işlemler veya emniyet açısından kritik sistemler için L3. Gerekçeyi yaz.
3. İlgili ASVS bölümlerini seç (ör. kimlik doğrulama, oturum yönetimi, erişim kontrolü, doğrulama ve kodlama, kriptografi, hata yönetimi ve loglama, veri koruma, API, yapılandırma). Uygulanmayan bölümleri nedeniyle birlikte çıkar.
4. Her gereksinimi bağlama uyarlanmış, test edilebilir tek bir "-malıdır" cümlesiyle yaz; ASVS metnini kopyalamak yerine bölüm/gereksinim referansı ver.
5. Tehdit modeli ve mevzuattan gelen bağlama özel gereksinimleri ekle: veri minimizasyonu, saklama süresi, loglarda maskeleme, açık rıza, KVKK/GDPR ilgili kişi başvurularının karşılanması.
6. Her gereksinim için doğrulama yöntemi belirle: otomatik test, SAST/DAST/SCA kuralı, kod incelemesi, yapılandırma kontrolü, sızma testi.
7. MoSCoW veya Must/Should/Could ile önceliklendir; Must kalemlerini sürüm geçiş kapılarına (release gate) bağla.
8. Çatışmaları ve ödünleşimleri (ör. oturum zaman aşımı ile kullanılabilirlik) ve kimin karar vereceğini işaretle.
9. Açık soruları ve varsayımları listele.
10. Sonraki beceriyi öner: her gereksinimi iş kalemlerinde test edilebilir kılmak için `acceptance-criteria`, tehditler henüz modellenmediyse `threat-model`, doğrulama için `secure-code-review`.

## Çıktı formatı
```markdown
# Güvenlik Gereksinimleri: <sistem/özellik>
Hedef seviye: OWASP ASVS <sürüm> L<n> – <gerekçe>
## Bağlam
- Maruziyet, kullanıcılar, veri sınıfları, entegrasyonlar
## Gereksinimler
| ID | Gereksinim (-malıdır) | ASVS ref | Kaynak (ASVS / tehdit / mevzuat) | Öncelik | Doğrulama | Sorumlu |
|---|---|---|---|---|---|---|
| SEC-01 | ... | V<bölüm>.<alt bölüm> | ... | Must | Otomatik test | ... |
## Hariç Tutulan Bölümler
- <bölüm> – gerekçe
## Ödünleşimler ve Gereken Kararlar
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her gereksinim doğrulama yöntemi olan, tek ve test edilebilir bir ifade.
- [ ] ASVS seviyesi ve sürümü belirtildi ve gerekçelendirildi.
- [ ] Kişisel veri gereksinimleri minimizasyon, loglarda maskeleme ve saklama süresini kapsıyor.
- [ ] ASVS metni birebir alıntılanmadı; referanslar bölüme işaret ediyor.
- [ ] Must gereksinimleri bir sürüm geçiş kapısına bağlı.
- [ ] Mevcut kontroller hakkında hiçbir şey uydurulmadı; bilinmeyenler işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Sistem güvenli olmalıdır" tarzı gereksinimler yazmak. Her madde gözlemlenebilir bir davranışı tarif etmeli.
- ASVS'nin tamamını backlog'a kopyalamak. Bağlama uyarla, uygulanmayanı gerekçesiyle çıkar.
- Loglama, izleme ve gizli anahtar rotasyonu gibi fonksiyonel olmayan güvenlik ihtiyaçlarını unutmak.

## Örnek
Girdi: "Müşteri self-servis portalı, internete açık, ad, telefon ve adres saklıyor; ödemeler barındırılan ödeme sayfasıyla alınıyor."

Çıktıdan bir bölüm:
- Hedef seviye: ASVS L2 – internete açık, kişisel veri var, kart verisi saklanmıyor.
| SEC-04 | Portal, çıkışta ve 15 dakika hareketsizlikten sonra sunucu tarafındaki oturumu sonlandırmalıdır [VARSAYIM: süre teyit edilecek] | V3 | ASVS | Must | Otomatik test |
| SEC-11 | Uygulama logları telefon numarası ve adresi açık metin olarak içermemelidir | V7 | KVKK | Must | Log incelemesi + test |
