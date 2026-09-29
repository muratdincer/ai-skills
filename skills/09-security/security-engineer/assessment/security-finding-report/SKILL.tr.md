---
description: "Başlık, etkilenen varlık, önem derecesi ve puanlama, açıklama, etki, tekrar üretme adımları, kanıt, çözüm ve referanslar içeren, sızma testi raporu, bug bounty yanıtı veya iç takip sistemi için uygun, net ve tekrar üretilebilir bir güvenlik bulgusu yazar. Doğrulanmış veya şüpheli bir güvenlik sorununun geliştiriciler, yönetim veya denetçiler için belgelenmesi gerektiğinde kullanılır."
related: "vulnerability-triage, secure-code-review, pentest-scope, bug-report, security-incident-response"
prompt: "Şunun için güvenlik bulgusu yaz: giriş yapmış herhangi bir kullanıcı URL'deki fatura numarasını değiştirerek başka bir kullanıcının fatura PDF'ini indirebiliyor."
---

# Güvenlik Bulgusu Yazma

## Amaç
Bir güvenlik sorununu, geliştiricinin tekrar üretip düzeltebileceği, yöneticinin riskini değerlendirebileceği ve denetçinin kapanışını doğrulayabileceği şekilde, hassas veri sızdırmadan belgelemek.

## Ne zaman kullanılır
- Sızma testi, kod incelemesi, bug bounty veya iç test bir güvenlik sorunu ortaya çıkardığında.
- Doğrulanmış bir tarayıcı bulgusu için takip kaydı gerektiğinde.
- Bir bulgunun tedarikçiye veya müşteriye iletilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Ham bir raporun önceliği henüz belirlenmediyse `vulnerability-triage` kullanılır.
- Sorun aktif olarak istismar ediliyorsa `security-incident-response` kullanılır.
- Güvenlik etkisi olmayan fonksiyonel bir hataysa `bug-report` kullanılır.

## Girdiler
Zorunlu:
- Gözlemlenen durum: davranış, yeri (varlık, endpoint, bileşen) ve nasıl tetiklendiği.

İsteğe bağlı, kaliteyi artırır:
- İstek/yanıt örnekleri, ekran görüntüleri, araç çıktıları.
- Ortam ve sürüm, test eden kişinin rolü ve hesap tipi.
- Kurumun kullandığı önem şeması (CVSS v3.1/v4.0, iç matris).

Gözlem veya konum eksikse sor. Tekrar üretme teyit edilmediyse bulguyu "Doğrulanmadı" olarak etiketle.

## Süreç
1. Somut bir başlık yaz: zayıflık + konum + sonuç (ör. "Fatura indirmede IDOR başka müşterilerin faturalarını ifşa ediyor").
2. Etkilenen varlığı, ortamı, sürümü ve keşif tarihini kaydet.
3. Sınıflandır: OWASP Top 10 / API Top 10 kategorisi ve CWE numarası.
4. Önem derecesini kurumun şemasıyla puanla; CVSS ise tam vektörü ver ve açık olmayan her metriği gerekçelendir. Teyit edilmemiş olgular için vektör tahmin etme.
5. Zayıflığı 2-4 cümleyle anlat: ne yanlış ve neden oluyor.
6. Etkiyi iş diliyle anlat: hangi veriler veya işlemler, hangi kullanıcılar, ölçek, mevzuat açısından önemi (KVKK/GDPR kapsamında kişisel veri, olası ihlal bildirimi yükümlülükleri).
7. Ön koşullar, hesaplar (gerçek kimlik bilgisi değil, rol olarak), istekler ve beklenen ile gerçekleşen sonuçla numaralı tekrar üretme adımları yaz.
8. Hassas değerleri maskeleyerek kanıt ekle: token'lar, parolalar, kişisel veriler, dışarıyla paylaşılıyorsa iç host adları.
9. Çözümü ver: kök neden düzeltmesi, kısa vadeli önlem ve düzeltmenin nasıl doğrulanacağı (tekrar test adımları).
10. Referansları (CWE, OWASP cheat sheet'leri, üretici duyurusu) ve durum alanlarını (sorumlu, SLA'ya göre son tarih, tekrar test sonucu) ekle.
11. Gözlenen kanıtın ötesinde çıkarım yapılan her şeyi `[VARSAYIM]` olarak işaretle, sonra önceliklendirme için `vulnerability-triage`, aktif istismar belirtisi varsa `security-incident-response` öner.

## Çıktı formatı
```markdown
# <ID>: <somut başlık>
| Alan | Değer |
|---|---|
| Varlık / bileşen | ... |
| Ortam / sürüm | ... |
| Keşif | <tarih>, <rol> tarafından |
| Kategori | OWASP <kat> · CWE-<id> |
| Önem | <derece> (<CVSS vektörü veya şema>) |
| Durum | Açık / Doğrulanmadı / Düzeltildi / Kabul edildi |
| Sorumlu / son tarih | ... |
## Açıklama
## Etki
## Tekrar Üretme Adımları
1. ...
Beklenen: ... Gerçekleşen: ...
## Kanıt (maskelenmiş)
## Çözüm
- Düzeltme: ... · Geçici önlem: ... · Doğrulama: ...
## Referanslar
```

## Kalite kontrol listesi
- [ ] Başka bir mühendis sorunu yalnızca adımları izleyerek tekrar üretebiliyor.
- [ ] Önem derecesi gerekçeli ve anlatılan etkiyle tutarlı.
- [ ] Kanıttaki secret'lar ve kişisel veriler maskelendi.
- [ ] Çözüm yalnızca test edilen payload'u değil, kök nedeni ele alıyor.
- [ ] Tekrar test için doğrulama adımları eklendi.
- [ ] Gözlemin ötesinde bir iddiada bulunulmadı; bilinmeyenler `[BİLİNMİYOR]` ile işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "API'de güvenlik sorunu" gibi belirsiz başlıklar. Başlık okuyana zayıflığı ve neyin tehlikede olduğunu söylemeli.
- Kanıt olmadan etkiyi abartmak ("tüm veritabanı ele geçirilir"). Gösterilenle makul olanı ayrı ayrı yaz.
- Belirtiyi düzeltmek: yetki kontrolü eklemek yerine tek bir parametre değerini engellemek.

## Örnek
Girdi: "/invoices/{no}/pdf adresindeki fatura numarasını değiştirmek, giriş yapmış herhangi bir kullanıcının başkalarının faturalarını indirmesine izin veriyor."

Çıktıdan bir bölüm:
# SEC-2026-014: Fatura PDF indirmede IDOR başka müşterilerin faturalarını ifşa ediyor
| Kategori | OWASP A01:2021 Broken Access Control · CWE-639 |
Etki: Faturalar ad, adres ve satın alma geçmişi içeriyor; ardışık numaralar toplu veri toplamaya imkan veriyor. Bu, KVKK/GDPR kapsamında kişisel veri ifşasıdır; bildirim yükümlülüklerini değerlendirmek için kişisel veri sorumlusunu/DPO'yu dahil et.
Düzeltme: fatura sahipliğini sunucuda kimliği doğrulanmış müşteri kimliğiyle karşılaştır; derinlemesine savunma için ardışık olmayan kimlikler kullan.
