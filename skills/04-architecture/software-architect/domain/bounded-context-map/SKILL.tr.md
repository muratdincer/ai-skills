---
name: bounded-context-map
description: "Her sınırlı bağlamı, ortak dilini (ubiquitous language) ve sahipliğini adlandıran; bağlamlar arası ilişkileri (partnership, paylaşılan çekirdek, müşteri-tedarikçi, conformist, ACL, OHS, published language, ayrı yollar) upstream/downstream yönü ve entegrasyon biçimiyle sınıflandıran bir bağlam haritası üretir. Modül veya servis sınırları tanımlanırken, bir ekip sistem haritasına alıştırılırken ya da ekipler arası bağımlılık ve çeviri sorunları teşhis edilirken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: software-architect
  area: domain
  title: "Sınırlı bağlam haritası"
  related: "event-storming, service-decomposition, aggregate-design, integration-pattern-selection, team-topology"
  prompt: "Perakende platformumuz için bağlam haritası çiz: katalog, fiyatlama, sipariş, ödeme (harici PSP), depo ve CRM; dört ekip sahip."
---

# Sınırlı Bağlam Haritası

## Amaç
Model sınırlarını ve aralarındaki güç ilişkilerini açık hale getirmek. Böylece entegrasyon sözleşmeleri, çeviri katmanları ve ekip sorumlulukları tesadüfi bağımlılıklardan değil bilinçli seçimlerden doğar.

## Ne zaman kullanılır
- `event-storming` kilit olayları ve aday sınırları ortaya çıkardıktan sonra.
- Bir monoliti bölmeden veya servisleri ekiplere atamadan önce.
- Aynı terim sistemin farklı yerlerinde farklı anlamlara gelip hataya yol açıyorsa.
- Bir downstream ekip, upstream model değişiklikleri yüzünden sürekli bozuluyorsa.

## Ne zaman kullanılmaz
- Sınırlar henüz hiç keşfedilmemişse önce `event-storming` kullanılır.
- Asıl soru dağıtılabilir servislerin nasıl kesileceği ve verinin kime ait olacağıysa `service-decomposition` kullanılır.
- Yalnızca iki sistem arasındaki taşıma mekanizması seçilecekse `integration-pattern-selection` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki alt alanların, modüllerin veya sistemlerin listesi ve her birinin ne yaptığına dair bir cümle.

İsteğe bağlı:
- Sahip ekipler, mevcut entegrasyonlar, bilinen sıkıntılar, sözlük çatışmaları.
- Event storming çıktısı, organizasyon şeması, harici tedarikçiler ve sözleşmeleri.

Parça listesi verilmemişse iste. Bilinmeyen sahiplik veya yönleri `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Alt alanları çekirdek (farklılaştırıcı), destekleyici veya genel (generic) olarak sınıflandır; modellemeye nereye yatırım yapılacağını, nerede satın alınıp uyum sağlanacağını bu belirler.
2. Her sınırlı bağlamı tanımla: ad, sorumluluk, ortak dilinin temel terimleri, sahip ekip ve iç/dış olduğu.
3. Bağlamlar arasında farklı anlam taşıyan terimleri bul (ör. CRM'deki "Müşteri" ile Faturalama'daki) ve her anlamı bağlam bazında kaydet; tek bir kurumsal model dayatma.
4. Veri veya davranış alışverişi yapan her çift için upstream'i (model değişikliği kimden yayılır) ve downstream'i (kim etkilenir) belirle.
5. Her ilişkiyi desenle sınıflandır: Partnership, Shared Kernel (paylaşılan çekirdek), Customer-Supplier, Conformist, Anticorruption Layer (ACL), Open Host Service (OHS), Published Language (PL), Separate Ways ya da eski alanlar için Big Ball of Mud.
6. Desen uygunluğunu ekip gerçekliğiyle kontrol et: Shared Kernel ve Partnership sıkı iş birliği ister; harici veya eski bir upstream'e bakan downstream çekirdek bağlamda uyum sağlamak yerine normalde ACL olmalıdır.
7. Her ilişki için entegrasyon biçimini (senkron API, olay, dosya, paylaşılan veritabanı) not et ve paylaşılan veritabanlarını bağımlılık riski olarak işaretle.
8. Sana söylenmeyip çıkarım yaptığın her ilişkiyi `[VARSAYIM]` olarak işaretle ve sorunları listele: eksik ACL'ler, döngüsel bağımlılıklar, birbiriyle ilgisiz çok sayıda bağlama sahip tek ekip, ekipler arasında bölünmüş bağlamlar.
9. Haritayı kod olarak diyagram (ör. Mermaid veya Context Mapper DSL) ve bir ilişki tablosu şeklinde üret.
10. Değişiklikleri öncelik sırasıyla, her birinin giderdiği sıkıntı ve getirdiği maliyetle öner.
11. Hedef devam ediyorsa dağıtım sınırları için `service-decomposition`, çekirdek bağlam içinde `aggregate-design` veya ekip sahipliğini hizalamak için `team-topology` öner.

## Çıktı formatı
```markdown
# Bağlam Haritası: <sistem haritası>

## Sınırlı Bağlamlar
| Bağlam | Alt alan türü | Sorumluluk | Temel terimler | Sahip ekip | İç/Dış |
|---|---|---|---|---|---|

## İlişkiler
| Upstream | Downstream | Desen | Entegrasyon biçimi | Notlar / riskler |
|---|---|---|---|---|

## Diyagram
<Mermaid veya Context Mapper DSL kaynağı, ör. flowchart LR; Katalog -- "OHS/PL" --> Siparis>

## Terim Çatışmaları
- <terim>: <bağlam A anlamı> ile <bağlam B anlamı>

## Sorunlar ve Öneriler
1. <sorun> → <önerilen değişiklik> — fayda / maliyet

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her bağlamın tek bir sahip ekibi var veya `[BİLİNMİYOR]` olarak işaretli.
- [ ] Her ilişkinin bir yönü ve adı konmuş tek bir deseni var.
- [ ] Çatışan terimler zorla birleştirilmemiş, bağlam bazında listelenmiş.
- [ ] Çekirdek bağlamı besleyen harici ve eski upstream'ler ACL ile korunuyor ya da risk belirtilmiş.
- [ ] Bağlamlar arası paylaşılan veritabanları işaretlenmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İstenen geleceği bugünmüş gibi çizmek. Mevcut durum ve hedef haritalarını ayrı tut.
- Bir bağlamı bir mikroservisle eşitlemek. Bir bağlam birden fazla dağıtılabilir birim içerebilir; bir birim ise birden fazla bağlama yayılmamalıdır.
- Her şeyi Customer-Supplier diye etiketlemek. Upstream downstream ihtiyaçlarını gözetmiyorsa dürüst desen Conformist'tir.

## Örnek
Girdi: "Sipariş harici PSP'yi çağırıyor; Depo, Sipariş veritabanını doğrudan okuyor; Fiyatlama ve Katalog ekipleri ortak bir Ürün kütüphanesi kullanıyor."

Çıktıdan bir bölüm:
- Sipariş (downstream) ← PSP (upstream, harici): Bugün Conformist; PSP durum kodlarını sipariş modelinin dışında tutmak için ACL önerilir.
- Depo ← Sipariş: paylaşılan veritabanı, yüksek bağımlılık riski; Sipariş'in "Sipariş Verildi" olaylarını yayınlaması önerilir (OHS/PL).
- Fiyatlama ↔ Katalog: Shared Kernel (Ürün kütüphanesi) `[VARSAYIM: ortak değişiklik süreci var]`.
