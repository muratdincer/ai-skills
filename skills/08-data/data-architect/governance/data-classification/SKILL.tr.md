---
name: data-classification
description: "Veri setlerini ve alanları hassasiyet ve gizlilik kategorisine göre sınıflandırır: gizlilik düzeyi, kişisel veri, KVKK Madde 6 ve GDPR Madde 9-10 kapsamında özel nitelikli veri, doğrudan ve dolaylı tanımlayıcılar; buradan maskeleme, şifreleme, erişim ve saklama gibi işleme kontrollerini türetir. Veri bir platforma alınırken, DPIA veya erişim modeli hazırlanırken ya da kişisel veya hassas sütunlar etiketlenmek istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-architect
  area: governance
  title: "Veri hassasiyet sınıflandırması"
  related: "privacy-impact-assessment, retention-policy, data-catalog-entry, access-review, secrets-management-plan"
  prompt: "Müşteri ve kredi başvuru tablolarımızın sütunlarını KVKK'ya göre sınıflandır ve maskeleme kuralları öner."
---

# Veri Hassasiyet Sınıflandırması

## Amaç
Her alana ve veri setine savunulabilir bir hassasiyet ve gizlilik sınıfı atamak ve bunu somut işleme kontrollerine çevirmek. Böylece erişim, maskeleme, saklama ve ihlal müdahalesi tahmine değil veriye dayanır.

## Ne zaman kullanılır
- Yeni kaynaklar veya veri setleri ortak bir platforma ya da analitik ortama alınırken.
- Erişim modeli, maskeleme politikası, DPIA veya veri paylaşım sözleşmesi hazırlanırken.
- Denetim veya düzenleyici, kişisel ya da özel nitelikli verinin nerede bulunduğunu sorduğunda.

## Ne zaman kullanılmaz
- Bir işleme faaliyetinin tam gizlilik risk değerlendirmesi gerekiyorsa `privacy-impact-assessment` kullanılır.
- Yalnızca saklama süreleri tanımlanıyorsa `retention-policy` kullanılır.
- Gizli bilgi (secret) ve kimlik bilgisi yönetimi için `secrets-management-plan` kullanılır.

## Girdiler
Zorunlu:
- Adları ve tercihen açıklamaları veya örnek değer kalıplarıyla alan listesi (asla gerçek kişisel değerler değil).

İsteğe bağlı:
- Kurumun sınıflandırma şeması (düzeyler ve tanımları), ilgili kişi grupları, işleme amaçları, yargı alanları, mevcut kontroller.

Şema verilmemişse dört düzeyli varsayılanı (Genel, Kurum İçi, Gizli, Çok Gizli) kullan ve `[VARSAYIM]` olarak işaretle. Yalnızca gerçek veri örnekleri varsa bunun yerine maskelenmiş örnek iste.

## Süreç
1. Şemayı teyit et: tanımlarıyla gizlilik düzeyleri ve etiketlenecek gizlilik kategorileri (kişisel, özel nitelikli, ceza mahkûmiyeti verisi, çocuk verisi, finansal/ödeme, kimlik doğrulama).
2. Her alan için, doğrudan veya birleşik olarak kimliği belirli ya da belirlenebilir bir gerçek kişiyle ilişkili olup olmadığına karar ver.
3. Tanımlayıcı rolünü etiketle: doğrudan tanımlayıcı (ad, TC kimlik no, e-posta, telefon), yarı tanımlayıcı (doğum tarihi, posta kodu, cinsiyet, unvan), hassas nitelik veya kişisel olmayan.
4. Özel nitelikli verileri KVKK Madde 6'ya (ör. sağlık, biyometrik, genetik, din, siyasi düşünce, sendika üyeliği, ceza mahkûmiyeti, kılık kıyafet) ve GDPR Madde 9-10'a göre etiketle. Serbest metin alanlarının çoğu zaman bunları içerdiğini not et.
5. Birleşim ve çıkarım riskini değerlendir: birlikte yeniden tanımlamaya yol açan yarı tanımlayıcılar; hassas bir niteliği açığa çıkaran türetilmiş alanlar (ör. eczane alışverişlerinin sağlık durumunu ima etmesi).
6. Her alana gizlilik düzeyi ata; alanlar ayrılmadıkça veri seti en yüksek alan düzeyini devralır.
7. Düzey/kategori bazında kontrolleri türet: durağan ve aktarımdaki şifreleme, sütun maskeleme veya tokenizasyon, analitik için takma adlandırma (pseudonymization), satır düzeyi kısıtlar, erişim kaydı, dışa aktarım kısıtları, saklama ve silme.
8. Veri minimizasyonu fırsatlarını belirle: belirtilen amaç için gerekmeyen alanlar, hassasiyet düşürme (doğum tarihi yerine doğum yılı), toplulaştırma.
9. Biliniyorsa yurt dışına aktarım ve üçüncü taraf erişimini işaretle.
10. Belirsiz sınıflandırmaları veri sahibi/KVKK sorumlusu teyidi için kaydet.
11. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa sonraki beceriyi öner: saklama ve silme kuralları için `retention-policy`, yüksek riskli işleme için `privacy-impact-assessment` veya yetkileri hizalamak için `access-review`.

## Çıktı formatı
```markdown
# Veri Sınıflandırması: <veri seti/sistem>
Şema: <düzeyler> | Yargı alanları: <KVKK/GDPR/...> | Gözden geçiren: <[TBD]>

## Alan Sınıflandırması
| Alan | Kişisel mi? | Tanımlayıcı rolü | Özel nitelik | Düzey | Kontroller | Minimizasyon notu |
|---|---|---|---|---|---|---|

## Birleşim / Çıkarım Riskleri
- <alanlar> birlikte <risk> doğurur → <kontrol>

## Veri Seti Düzeyinde Sonuç
Düzey: <...> | Özel nitelikli veri içeriyor: <evet/hayır> | Önerilen ayrıştırma: <...>

## Düzeye Göre İşleme Kontrolleri
| Düzey | Depolama | Erişim | Maskeleme | Paylaşım | Saklama |
|---|---|---|---|---|---|

## Teyit Edilecekler (sahip/KVKK sorumlusu)
1. ...
```

## Kalite kontrol listesi
- [ ] Her alanın bir düzeyi ve kişisel/kişisel değil kararı var.
- [ ] Serbest metin alanları dahil özel nitelikli veri açıkça kontrol edildi.
- [ ] Yarı tanımlayıcı birleşimleri değerlendirildi.
- [ ] Her düzey yalnızca etikete değil somut kontrollere eşlendi.
- [ ] Çıktıda gerçek kişisel değer yok.
- [ ] Belirsiz maddeler sahip/KVKK sorumlusuna yönlendirildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca doğrudan tanımlayıcıları kişisel veri saymak. Yarı tanımlayıcılar ve takma adlandırılmış veri de kişisel veridir.
- Özel nitelikli verinin sıklıkla saklandığı serbest metin, not ve ek alanlarını gözden kaçırmak.
- Kontrolsüz etiketleme. Erişimi veya maskelemeyi değiştirmeyen sınıflandırmanın etkisi yoktur.

## Örnek
Girdi: "loan_application: applicant_name, tckn, birth_date, city, monthly_income, health_declaration_text, score."

Çıktıdan bir bölüm:
- tckn: doğrudan tanımlayıcı, Çok Gizli; analitikte tokenize et, yalnızca kredi değerlendirme rolünde aç.
- health_declaration_text: özel nitelikli (sağlık, KVKK md. 6), Çok Gizli; analitik katmandan hariç tut.
- birth_date + city: yarı tanımlayıcılar; analitik mart'larda yalnızca doğum yılını yayımla.
