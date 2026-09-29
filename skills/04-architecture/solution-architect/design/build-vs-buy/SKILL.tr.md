---
name: build-vs-buy
description: "Bir yetkinlik için kendin geliştirme, satın alma (COTS/SaaS), mevcut platformu genişletme veya açık kaynak kullanma seçeneklerini stratejik farklılaşma, fonksiyonel uygunluk, çok yıllık toplam sahip olma maliyeti, risk, değere ulaşma süresi ve çıkış maliyeti açısından karşılaştırır ve gerekçeli bir öneri üretir. Bir ekip bir yetkinliği içeride mi geliştireceğine yoksa satın mı alacağına karar vermek zorunda olduğunda veya mevcut özel bir sistem ya da ürün yenilenecekse kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: solution-architect
  area: design
  title: "Yap ya da satın al kararı"
  related: "technology-selection, vendor-evaluation, cost-benefit-analysis, fit-gap-analysis, adr"
  prompt: "Müşteri bildirim servisimizi kendimiz mi geliştirelim yoksa SaaS bir ürün mü alalım? Ayda yaklaşık 2 milyon e-posta ve SMS gönderiyoruz, Türkçe ve İngilizce şablon gerekiyor."
---

# Yap ya da Satın Al Kararı

## Amaç
Bir yetkinlik için kaynak seçimi kararını lisans fiyatına veya geliştirici hevesine göre değil; stratejik değer, uygunluk, toplam maliyet, risk ve geri dönülebilirlik karşılaştırmasıyla savunulabilir biçimde vermek.

## Ne zaman kullanılır
- Yeni bir yetkinlik gerektiğinde ve hem özel geliştirme hem de pazardaki ürünler makul olduğunda.
- Özel bir sistemin bakımı pahalıysa ve bir ürün onun yerini alabilecekse ya da tersi.
- Yönetim maliyet ve riskiyle birlikte bir kaynak seçimi önerisi istediğinde.

## Ne zaman kullanılmaz
- Karar yalnızca benzer ürünler veya çatılar arasındaysa `technology-selection` veya `vendor-evaluation` kullanılır.
- Gereksinimler henüz bilinmiyorsa önce `fit-gap-analysis` veya `brd-writing` kullanılır.
- Onaylanmış bir yatırımın salt finansal değerlendirmesi gerekiyorsa `cost-benefit-analysis` kullanılır.

## Girdiler
Zorunlu:
- Yetkinlik ve olmazsa olmazlar dahil temel gereksinimleri.
- Değerlendirilen seçenekler veya bunları önermeye izin.

İsteğe bağlı:
- Hacimler, kullanıcılar, büyüme; TCO ufku (genellikle 3-5 yıl).
- Ekip kapasitesi ve yetkinlikleri, iç maliyet oranları, üretici teklifleri.
- Kısıtlar: veri yerleşimi, KVKK/GDPR, güvenlik, entegrasyon ortamı, satın alma kuralları.

Yetkinlik veya olmazsa olmazlar yoksa sor. Fiyat asla uydurma; `[BİLİNMİYOR]` ya da kullanıcının verdiği aralıkları kullan.

## Süreç
1. Yetkinliği farklılaştırıcı, gerekli-ama-yaygın veya emtia olarak sınıflandır (ör. yetkinlik haritası veya Wardley evrimiyle). Varsayılan: farklılaştıranı geliştir, emtiayı satın al.
2. Seçenekleri tanımla: geliştir, SaaS satın al, COTS satın alıp kendin barındır, açık kaynak benimse, mevcut platformu genişlet, hibrit (çekirdeği satın al, kenarları geliştir).
3. Ağırlıklı kriterleri tanımla: stratejik değer, fonksiyonel uygunluk (olmazsa olmazlar puan değil eşiktir), fonksiyonel olmayan uygunluk, entegrasyon eforu, değere ulaşma süresi, TCO, üretici/ekosistem riski, bağımlılık ve çıkış maliyeti, ekip yetkinliği.
4. Her seçeneğin uygunluğunu değerlendir: önce olmazsa olmaz eşiği geçti/kaldı, sonra boşluklar ve kapatmak için gereken özelleştirme; doğrulanmamış üretici iddialarını `[VARSAYIM]` olarak işaretle.
5. Ufuk boyunca şu kalemlerle bir TCO modeli kur: lisans/abonelik, kurulum, entegrasyon, özelleştirme, altyapı/işletim, destek ve operasyon personeli, sürüm yükseltmeleri, eğitim, çıkış/göç. Yalnızca verilen rakamları veya yer tutucuları kullan.
6. Riskleri değerlendir: üreticinin sürdürülebilirliği, yol haritası kontrolü, özelleştirilmiş ürünlerde sürüm yükseltme yükü, güvenlik/uyum durumu, geliştirmede kilit kişi riski, teslim riski.
7. Geri dönülebilirliği değerlendir: veri dışa aktarımı, standart arayüzler, sözleşme şartları, sonradan geçişin maliyeti.
8. Puanla ve karşılaştır; en yüksek ağırlıklı veya en belirsiz iki-üç kriterde duyarlılık kontrolü yap.
9. Öneriyi koşullarıyla (ör. "veri yerleşimi sözleşmeyle garanti edilirse satın al") ve hâlâ gereken kanıtlarla (PoC, referans görüşmesi, teklif) yaz.
10. Hedef devam ediyorsa ürün kısa listesi için `vendor-evaluation`, geliştirme teknolojisi için `technology-selection` veya kararı kaydetmek için `adr` öner.

## Çıktı formatı
```markdown
# Yap ya da Satın Al: <yetkinlik>
## Yetkinlik Sınıflandırması
<farklılaştırıcı | yaygın | emtia> – <gerekçe>
## Seçenekler
## Olmazsa Olmaz Eşikleri
| Olmazsa olmaz | Geliştir | Satın Al A | Açık kaynak | Genişlet |
|---|---|---|---|---|
## Ağırlıklı Değerlendirme
| Kriter | Ağırlık | Geliştir | Satın Al A | Açık kaynak | Genişlet |
|---|---|---|---|---|---|
## TCO (<ufuk>)
| Maliyet kalemi | Geliştir | Satın Al A | ... |
|---|---|---|---|
## Riskler ve Çıkış Değerlendirmesi
## Duyarlılık
## Öneri ve Koşullar
## Hâlâ Gereken Kanıtlar / Açık Sorular
```

## Kalite kontrol listesi
- [ ] Olmazsa olmazlar eşik olarak işliyor; birini karşılamayan seçenek diğer puanlarla kurtarılmıyor.
- [ ] TCO tüm ufku kapsıyor; yalnızca lisans veya geliştirme eforunu değil işletim, yükseltme ve çıkış maliyetlerini de içeriyor.
- [ ] Hiçbir fiyat veya efor rakamı uydurulmadı; bilinmeyenler işaretli.
- [ ] Satın alınan ürünün özelleştirmesi, sürüm yükseltme etkisiyle birlikte maliyetlendirildi.
- [ ] Öneri koşullarını ve hâlâ gereken kanıtları belirtiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İlk yılın lisans maliyetini geliştirme eforuyla karşılaştırıp geliştirmenin yıllarca gerektireceği bakım ekibini yok saymak.
- Satın alıp yoğun özelleştirmek; bu, yükseltilemeyen bir çatallanma yaratır. Yapılandırmayı veya kenarlarda geliştirmeyi tercih et.
- Ekip ilginç bulduğu için emtia yetkinlikleri geliştirmek.

## Örnek
Girdi: "Bildirim servisi geliştirilsin mi satın mı alınsın; ayda ~2M e-posta/SMS, TR ve EN şablonlar."

Çıktıdan bir bölüm:
- Sınıflandırma: emtia – bildirim iletimi işi farklılaştırmıyor `[VARSAYIM: ürün ekibiyle teyit et]`.
- Eşik: Türkiye'deki yerel operatörler üzerinden SMS iletimi – Satın Al A `[BİLİNMİYOR, üreticiye sor]`, Geliştir geçti (mevcut SMS ağ geçidi üzerinden).
- TCO notu: Geliştir seçeneği nöbet rotası ve teslim edilebilirlik yönetimini içeriyor; Satın Al A mesaj başı fiyatı `[BİLİNMİYOR – aylık 2M için teklif iste]`.
- Öneri: Hibrit – e-posta iletimini satın al, şablon ve tercih servisini içeride tut; veri yerleşimi şartlarına bağlı.
