---
name: access-review
description: "Bir uygulama, veritabanı, bulut hesabı veya dizin grubu için kullanıcı erişim gözden geçirmesi (erişim yeniden onayı) yapar: yetkileri İK ve rol verileriyle karşılaştırarak fazla, sahipsiz, kullanılmayan, paylaşılan ve görevler ayrılığıyla çakışan yetkileri tespit eder, denetçiler için kanıtlı kaldır/koru kararları üretir. ISO 27001, SOC 2, SOX veya BDDK kapsamındaki periyodik erişim gözden geçirmelerinde, yeniden yapılanmalardan sonra ya da yetki birikmesinden şüphelenildiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: security-engineer
  area: operations
  title: "Erişim yetkisi gözden geçirme"
  related: "authn-authz-design, audit-preparation, control-mapping, it-risk-assessment, raci-matrix"
  prompt: "ERP'mizden alınan kullanıcı-rol listesi ve İK'nın aktif çalışan listesi burada. Çeyreklik erişim gözden geçirmesini yap ve kaldırılması gerekenleri işaretle."
---

# Erişim Yetkisi Gözden Geçirme

## Amaç
Her hesabın ve yetkinin hâlâ gerekli, sahipli ve en az yetki ile görevler ayrılığı ilkelerine uygun olduğunu teyit etmek ve kararların denetlenebilir bir izini bırakmak.

## Ne zaman kullanılır
- Periyodik erişim yeniden onayının zamanı geldiğinde (politikaya göre çeyreklik veya yıllık).
- Yeniden yapılanma, birleşme, toplu ayrılış veya rol modeli değişikliğinden sonra.
- Bir denetçi, olay ya da yetki birikmesi şüphesi hedefli bir gözden geçirme gerektirdiğinde.

## Ne zaman kullanılmaz
- Yeni bir rol veya yetki modeli tasarlanıyorsa `authn-authz-design` kullanılır.
- Birçok kontrol için aynı anda kanıt toplanıyorsa `audit-preparation` kullanılır.
- Ele geçirildiğinden şüphelenilen bir hesap inceleniyorsa `security-incident-response` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki sistemin yetki dökümü (hesap, rol/grup/yetki, varsa son giriş tarihi).

İsteğe bağlı, kaliteyi artırır:
- İK listesi (aktifler, ayrılanlar, departman ve yöneticisiyle görev değiştirenler).
- Amaçlanan yetkileriyle rol kataloğu, görevler ayrılığı (SoD) kural seti.
- Önceki gözden geçirme sonuçları ve onaylı istisnalar.

Yetki dökümü yoksa iste. İK verisi yoksa sahipsiz hesap tespitinin mümkün olmadığını belirt ve eksik olarak listele. Mümkünse takma adlandırılmış (pseudonymized) kimliklerle çalış; gözden geçirmenin gerektirdiğinden fazla kişisel veriyi tekrarlama.

## Süreç
1. Kapsamı ve dönemi tanımla: sistem, ortamlar, hesap tipleri (insan, servis, paylaşılan, acil durum), gözden geçirenler (yöneticiler ve sistem sahipleri).
2. Veriyi normalleştir: hesap-yetki başına bir satır; hesapları kalıcı bir anahtarla İK kimliklerine eşle; eşleşmeyen hesapları işaretle.
3. Sahipsiz hesapları tespit et: eşleşen aktif çalışan veya yüklenici yok ya da sahibi ayrılmış.
4. Kullanılmayan hesapları tespit et: politika eşiğini (ör. 90 gün) aşan süredir giriş yok [politika bilinmiyorsa VARSAYIM].
5. Fazla erişimi tespit et: rol kataloğunun ötesindeki yetkiler, yönetici olmayan fonksiyonlarda ayrıcalıklı roller, eski departman erişimini koruyan görev değiştirenler.
6. SoD kurallarıyla çakışan kombinasyonları tespit et (ör. tedarikçi oluşturma + ödeme onaylama; geliştirme + inceleme olmadan üretime deployment).
7. İnsan dışı ve paylaşılan hesapları incele: sahip, amaç, kimlik bilgisi rotasyonu, etkileşimli girişin kapalı olması.
8. Gözden geçiren başına karar listesi hazırla: Koru / Kaldır / Değiştir / İstisna, gerekçesiyle; istisnalar telafi edici kontrol ve bitiş tarihi gerektirir.
9. Düzeltmeleri takip et: kaldırmalar için kayıtlar, hedef tarihler, erişimin gerçekten kaldırıldığının doğrulanması.
10. Denetçiler için özetle: popülasyon, bütünlük kontrolü (döküm toplamı ile sistem toplamı), türüne göre bulgular, kararlar, düzeltme süresi.
11. Çıkarıma dayanan her bulguyu (ör. belgelenmiş bir görev ayrılığı kuralı olmadan çakışan sayılan rol) `[VARSAYIM]` olarak işaretle; gözden geçirme bir denetimin kanıtı olacaksa `audit-preparation` veya `control-mapping` öner.

## Çıktı formatı
```markdown
# Erişim Gözden Geçirmesi: <sistem> – <dönem>
## Kapsam ve Popülasyon
- İncelenen hesap: <n> (insan <n>, servis <n>, paylaşılan <n>) · Döküm tarihi: ...
- Bütünlük kontrolü: <döküm sayısı ile sistem sayısı>
## Bulgular
| # | Hesap (takma ad) | Yetki | Bulgu türü | Kanıt | Önerilen karar | Gözden geçiren |
## SoD Çakışmaları
| Hesap | Çakışan yetkiler | Kural | Karar / telafi edici kontrol |
## İstisnalar
| Hesap | Gerekçe | Telafi edici kontrol | Onaylayan | Bitiş |
## Düzeltme Takibi
| Kayıt | Aksiyon | Son tarih | Doğrulandı |
## Denetim İçin Özet
## Eksikler ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Popülasyonun eksiksizliği varsayılmadı, doğrulandı.
- [ ] Her bulgu türü (sahipsiz, kullanılmayan, fazla, SoD, paylaşılan/servis) kontrol edildi veya mümkün olmadığı belirtildi.
- [ ] Gözden geçirenler kendi erişimlerini onaylamıyor.
- [ ] İstisnaların onaylayanı ve bitiş tarihi var.
- [ ] Kişisel veri en aza indirildi, paylaşılan çıktılarda hesaplar takma adlandırıldı.
- [ ] Kaldırmalar bir doğrulama adımı içeriyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Göstermelik onay: yöneticilerin her şeyi toplu onaylaması. Karar için yalnızca riskli satırları sun, ayrıcalıklı erişimde Koru kararı için gerekçe iste.
- Yöneticisi olmadığı için servis ve paylaşılan hesapları atlamak. Her birine bir sahip ata.
- Gözden geçirmeyi erişim gerçekten kaldırıldığında değil, kararlar verildiğinde kapatmak.

## Örnek
Girdi: "412 hesap ve rol içeren ERP dökümü, 380 kişilik İK aktif listesi."

Çıktıdan bir bölüm:
| 7 | U-0193 | AP_Clerk + Vendor_Master_Maintain | SoD çakışması | Tedarikçi oluşturup o tedarikçiye fatura kaydedebiliyor | Vendor_Master_Maintain kaldırılsın | Finans yöneticisi |
| 12 | U-0241 | Tümü | Sahipsiz | İK listesinde eşleşme yok; son giriş 140 gün önce | Kaldır | Sistem sahibi |
