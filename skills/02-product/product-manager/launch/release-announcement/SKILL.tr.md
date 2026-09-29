---
name: release-announcement
description: "Okuyucuya sağlanan faydayla başlayan, neyin değiştiğini ve kimi etkilediğini anlatan, erişilebilirliği ve gereken aksiyonu belirten, net bir sonraki adımla biten ve kanala (e-posta, blog, uygulama içi, sosyal medya) uyarlanmış müşteriye yönelik bir sürüm duyurusu yazar. Bir özellik veya ürün sürümü müşterilere açıldığında, sürüm notlarının pazarlamaya hazır metne dönüştürülmesi gerektiğinde ya da bir sürümü \"duyurmak\" veya \"müşterilere anlatmak\" istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 02-product
  role: product-manager
  area: launch
  title: "Sürüm duyurusu yazma"
  related: "positioning-statement, go-to-market-plan, release-notes, announcement, microcopy"
  prompt: "Önümüzdeki salı e-posta ve uygulama içi bildirimle çıkacak yeni toplu fatura yükleme özelliğimiz için müşteri duyurusu yaz."
---

# Sürüm Duyurusu Yazma

## Amaç
Yayına alınan bir değişikliği, müşterinin okuyup anlayacağı ve harekete geçeceği kısa, fayda odaklı bir mesaja dönüştürmek; aşırı vaatte bulunmadan ve gereken aksiyonları gömmeden. Böylece sürüm destek talebi değil, benimsenme üretir.

## Ne zaman kullanılır
- Yeni bir özellik, ürün sürümü veya önemli bir iyileştirme müşterilerin kullanımına açıldığında.
- İç sürüm notlarının veya bir PRD'nin müşteriye yönelik metne dönüştürülmesi gerektiğinde.
- Aynı sürüm için e-posta, blog, uygulama içi ve sosyal medya kanallarında tutarlı versiyonlar gerektiğinde.

## Ne zaman kullanılmaz
- Kitle teknikse ve eksiksiz değişiklik listesi istiyorsa `release-notes` veya `changelog-entry` kullanılır.
- Mesaj çalışanlara yönelik bir iç duyuruysa `announcement` kullanılır.
- Lansman stratejisi, zamanlama ve kanal karması belli değilse `go-to-market-plan` kullanılır.

## Girdiler
Zorunlu:
- Yayına alınan şey (özellik tanımı, sürüm notları veya PRD bölümü).
- Hedef kitle (tüm müşteriler, bir paket, bir segment, bir bölge).

İsteğe bağlı, kaliteyi artırır:
- Konumlandırma cümlesi veya mesaj ayakları.
- Erişilebilirlik: tarih, kademeli açılış aşamaları, paketler/bölgeler, fiyat etkisi.
- Müşterinin yapması gereken aksiyon, geriye uyumsuz değişiklikler, kullanımdan kaldırmalar.
- Kanallar ve uzunluk sınırları; marka ses kılavuzu; doküman veya demo bağlantıları.
- Müşteri alıntısı veya sonucu (yalnızca gerçekse ve onaylıysa).

Sürüm içeriği veya kitle eksikse sor. Verilmeyen diğer her şeyi `[TBD]` olarak işaretle.

## Süreç
1. Kitleyi ve neyi önemsediğini belirle; segmentler belirgin biçimde farklıysa (yöneticiler ve son kullanıcılar gibi) ayrı versiyonlar planla.
2. Her özelliği müşteri faydasına çevir: artık ne yapabiliyor, ne kadar daha hızlı veya güvenli, hangi acı ortadan kalkıyor. Bu kitle için en önemli bir ila üç faydayı tut. Çıkarım olan faydaları `[VARSAYIM]` olarak işaretle.
3. Başlığı özellik adı veya iç kod adı değil, fayda olarak yaz.
4. Giriş paragrafını (2-3 cümle) şu sorulara cevap verecek şekilde yaz: ne yeni, kimin için, neden önemli.
5. Nasıl çalıştığını tek bir somut senaryoyla sade dille anlat; iç jargonu ve mimari ayrıntıları çıkar.
6. Erişilebilirliği net yaz: tarih, paketler, bölgeler, açılış hızı. Kademeli açılıyorsa herkese açık olduğunu ima etme.
7. Okuyucunun yapması gereken her şeyi (etkinleştirme, güncelleme, yeniden yapılandırma) ve geriye uyumsuz değişiklik veya kullanımdan kaldırmaları tarihiyle birlikte görünür biçimde ve erken yer ver.
8. Tek bir net çağrı (call to action) ve destekleyici bağlantılar ekle (doküman, video, iletişim).
9. İstenen her kanala uyarla: e-posta (konu + önizleme metni), blog (tam metin), uygulama içi (bir-iki satır + bağlantı), sosyal medya (kısa kanca). Uzunluk sınırlarına uy.
10. İddiaları kontrol et: her sayı, alıntı ve karşılaştırma girdilerden gelmeli; aksi halde çıkar veya `[KANIT GEREKLİ]` olarak işaretle. Tonu marka kılavuzuna göre kontrol et.
11. Hedef devam ediyorsa daha geniş lansman çalışmaları için `go-to-market-plan`, teknik değişiklik listesi için `release-notes` veya ürün içi metinler için `microcopy` öner.

## Çıktı formatı
```markdown
# Sürüm Duyurusu: <özellik / sürüm>
Kitle: <segment> · Kanallar: <liste> · Erişilebilirlik: <tarih / paketler / bölgeler>

## Başlık
<fayda odaklı başlık>

## Giriş
<ne yeni, kimin için, neden önemli — 2-3 cümle>

## Artık Neler Yapabilirsiniz
- <fayda 1, somut senaryoyla>
- <fayda 2>

## Erişilebilirlik
<tarih, paketler, bölgeler, açılış planı>

## Gereken Aksiyon (varsa)
<ne, ne zamana kadar, nasıl>

## Çağrı
<tek aksiyon + bağlantı>

## Kanal Versiyonları
- E-posta konu / önizleme: ...
- Uygulama içi: ...
- Sosyal medya: ...

## Varsayımlar ve Teyit Edilecekler
- [VARSAYIM] / [TBD] / [KANIT GEREKLİ] ...
```

## Kalite kontrol listesi
- [ ] Başlık ve giriş bir özellik adı değil, müşteri faydası anlatıyor.
- [ ] Erişilebilirlik (tarih, paketler, bölgeler, açılış) net ve abartısız.
- [ ] Gereken aksiyonlar ve geriye uyumsuz değişiklikler tarihleriyle birlikte metnin başında görünüyor.
- [ ] Tam olarak bir ana çağrı var.
- [ ] Uydurulmuş sayı, alıntı veya karşılaştırma yok; desteklenmeyen iddialar çıkarıldı veya işaretlendi.
- [ ] İç jargon ve kod adları temizlendi; çıkarımlar etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yayına alınan her şeyi listelemek. Müşteri göz gezdirir; bu kitle için önemli birkaç faydayı seç, tam notlara bağlantı ver.
- Gereken aksiyonu veya fiyat değişikliğini en alta saklamak. Güveni zedeler ve destek talebi yaratır; başa yakın koy.
- Paket veya bölgeye göre kademeli açılan bir özelliği tüm müşterilere duyurmak. Kimde olduğunu ve diğerlerine ne zaman geleceğini yaz.

## Örnek
Girdi: "Toplu fatura yükleme: tek seferde 500'e kadar PDF, alanları otomatik çıkarır. Tüm ücretli paketler, salıdan itibaren kademeli açılıyor."

Zayıf başlık: "Yeni OCR hattıyla BulkUpload v2.3 karşınızda"

Güçlü (bölüm):
- Başlık: "Bir aylık faturayı tek seferde yükleyin"
- Giriş: "Artık 500'e kadar fatura PDF'ini tek seferde bırakabilirsiniz; tedarikçi, tarih ve tutarı sizin yerinize dolduruyoruz. Saatler süren ay sonu girişi bir kontrol adımına dönüşüyor `[VARSAYIM: zaman tasarrufu iddiasını teyit et]`."
- Erişilebilirlik: "Salıdan itibaren tüm ücretli paketlerde kademeli olarak açılıyor `[TBD: tarih]`; tüm hesaplarda `[TBD]` gün içinde kullanılabilir olacak."
