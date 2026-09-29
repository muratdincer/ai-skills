---
name: docs-information-architecture
description: "Bir doküman setinin bilgi mimarisini Diátaxis dört türüne (eğitim, nasıl yapılır, referans, açıklama) göre tasarlar veya yeniden yapılandırır; mevcut sayfaları denetler, karışık içeriği sınıflandırıp böler, gezinme, adlandırma ve sayfa türlerini tanımlar, hedef site haritası ve geçiş planı üretir. Dokümanlarda gezinmek zor olduğunda, sayfalar öğrenme, görev, referans ve kavramı karıştırdığında, yeni bir ürün veya portal doküman yapısına ihtiyaç duyduğunda ya da bir doküman taşıma veya birleştirme öncesinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 12-technical-writing
  role: technical-writer
  area: docs
  title: "Doküman bilgi mimarisi"
  related: "tutorial, how-to-guide, user-guide, api-reference-docs, glossary-builder"
  prompt: "Mevcut 60 sayfalık doküman menümüz burada; geliştiricilerin kurulumu, görevleri ve API referansını daha hızlı bulması için yeniden yapılandırma öner."
---

# Doküman Bilgi Mimarisi

## Amaç
Doküman setine, okurların yapmaya çalıştığı işe (öğrenmek, bir görevi tamamlamak, bir şeye bakmak, anlamak) uyan bir yapı kazandırmak. Böylece her sayfanın tek bir işi olur, okurlar sayfaları öngörülebilir biçimde bulur, yazarlar da yeni içeriğin nereye gideceğini bilir.

## Ne zaman kullanılır
- Okurlar veya destek ekipleri dokümanlarda gezinmenin ya da aramanın zor olduğunu bildirdiğinde.
- Sayfalar eğitim adımlarını, görev tariflerini, parametre tablolarını ve kavram açıklamalarını karıştırdığında.
- Yeni bir ürün, API veya geliştirici portalı için doküman yapısı tanımlanacağında.
- Birden fazla doküman sitesi veya wiki taşınmadan, birleştirilmeden önce.

## Ne zaman kullanılmaz
- Tek bir öğrenme yolu yazılacaksa `tutorial` kullanılır.
- Tek bir görev sayfası yazılacaksa `how-to-guide` kullanılır.
- Bir API için referans içeriği üretilecekse `api-reference-docs` kullanılır.

## Girdiler
Zorunlu:
- Mevcut envanter (menü, site haritası, başlıklarıyla sayfa listesi veya bağlantılar) ya da yeni bir ürün için ürün kapsamı ve ana kullanıcı görevleri.
- Birincil hedef kitleler (ör. son kullanıcılar, yöneticiler, entegrasyon geliştiricileri, operasyon ekibi).

İsteğe bağlı, kaliteyi artırır:
- Analitik veya arama kayıtları (en çok okunan sayfalar, sonuçsuz aramalar), destek kaydı temaları.
- Ürün alanları ve adlandırma, mevcut stil rehberi veya sözlük, platform kısıtları (menü derinliği, sürümleme).

Ne envanter ne de ürün kapsamı verildiyse iste. Sayfa trafiği, kayıt sayısı veya okur araştırması uydurma; bu tür iddiaları `[BİLİNMİYOR]` olarak işaretle ve nasıl toplanacağını öner.

## Süreç
1. Envanter tablosu oluştur: her sayfa için başlık, mevcut konum, hedef kitle ve görünen amaç; başlıklar tek başına belirsizse örnek sayfa içeriği iste.
2. Her sayfayı başlığına değil okur ihtiyacına göre tek bir Diátaxis türüne (eğitim, nasıl yapılır, referans, açıklama) yerleştir; türleri karıştıran sayfaları "bölünecek" olarak işaretle ve hangi bölümün nereye gideceğini yaz.
3. Sorunları kanıtıyla işaretle: tekrarlar, yetim sayfalar, güncelliğini yitirmiş veya ürün içi (iç kullanım) içerik, çıkmaz sayfalar, ne işe yaradığını söylemeyen başlıklar; çıkarıma dayalı değerlendirmeleri `[VARSAYIM]` olarak etiketle.
4. Üst düzey ekseni belirle: her ürün alanı içinde Diátaxis türüne göre mi, her tür içinde ürün alanına göre mi; ürün genişliğine ve hedef kitlelerin örtüşmesine göre seç ve gerekçesini yaz.
5. En fazla üç gezinme seviyesi olan hedef site haritasını taslakla; her bölüm için okuru hedefine göre yönlendiren bir giriş sayfası ve sürüm notları, sorun giderme ve sözlük için net bir yer tanımla.
6. Sayfa türü başına adlandırma kuralları belirle (eğitim: "... oluşturma/kurma", nasıl yapılır: fiille başlayan görev, referans: isim, açıklama: "... hakkında / ... anlamak") ve yeniden adlandırmalara dayanıklı URL/slug kuralları koy.
7. Mevcut her sayfayı hedefine eşle: koru, taşı, böl, birleştir, yeniden yaz, kaldır; kaldırılan ve taşınan sayfalara yönlendirme (redirect) tanımla.
8. Boşlukları belirle: sayfası olmayan okur hedeflerini (kayıtlardan, arama terimlerinden veya ürün kapsamından) tür ve öncelikle yeni sayfalar olarak listele.
9. Sahiplik ve bakımı tanımla: bölüm başına bir sahip, gözden geçirme sıklığı ve yeni içeriğin nereye gideceği kuralı.
10. Geçişi dalgalara böl (en çok okunan veya en çok sorun yaratan alanlar önce), yönlendirme ve bağlantı kontrolü adımlarını ekle; açık soruları ve varsayımları listele.
11. Kullanıcının hedefi devam ediyorsa boşlukları doldurmak için `tutorial`, `how-to-guide` veya `api-reference-docs`, tutarsız terminolojiyi düzeltmek için `glossary-builder` öner.

## Çıktı formatı
```markdown
# Doküman Bilgi Mimarisi: <ürün / site>
Hedef kitleler: <...> | Kapsam: <kapsanan siteler/bölümler>

## Bulgular
- <sorun> – <kanıt / sayfalar> [çıkarımsa VARSAYIM]

## Yapı Kararı
Üst düzey eksen: <önce tür / önce ürün alanı> – <gerekçe>

## Hedef Site Haritası
- <Bölüm giriş sayfası>
  - Eğitimler: ...
  - Nasıl yapılır rehberleri: ...
  - Referans: ...
  - Açıklama: ...

## Adlandırma ve URL Kuralları
| Sayfa türü | Başlık kalıbı | Slug kalıbı |

## Sayfa Eşleme
| Mevcut sayfa | Tür | Aksiyon (koru/taşı/böl/birleştir/yeniden yaz/kaldır) | Hedef konum | Yönlendirme |

## Boşluklar (Yeni Sayfalar)
| Okur hedefi | Tür | Öncelik | Kanıt kaynağı |

## Sahiplik ve Yönetişim
## Geçiş Dalgaları
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her sayfanın tek bir Diátaxis türü ya da her bölümün nereye gideceğini gösteren bir bölme planı var.
- [ ] Gezinme derinliği en fazla üç seviye ve her bölümün hedef odaklı bir giriş sayfası var.
- [ ] Mevcut her sayfanın bir aksiyonu, taşınan veya kaldırılan her sayfanın bir yönlendirmesi var.
- [ ] Boşluklar kanıta (kayıtlar, aramalar, ürün kapsamı) bağlı ya da `[VARSAYIM]` olarak etiketli.
- [ ] Adlandırma kuralları sayfa türü başına tanımlı ve site haritasında uygulanmış.
- [ ] Sahiplik ve "yeni içerik nereye gider" kuralı yazılmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Okur hedefleri yerine organizasyon şemasını veya ürünün iç modül adlarını yansıtmak. Bölümleri okurların yapmak ya da bakmak istediği şeye göre adlandır.
- Başlığa göre sınıflandırmak ("Başlarken" otomatik olarak eğitim değildir). İçeriğin okur için gerçekte ne yaptığına göre sınıflandır.
- Yönlendirme olmadan yeniden yapılandırmak; bu, yer imlerini, arama sıralamasını ve ürün içi bağlantıları bozar.

## Örnek
Girdi: "Menü: Genel Bakış, Başlarken, Yapılandırma, Webhook'lar, API, SSS, İleri Düzey, Diğer (60 sayfa). Hedef kitle: entegrasyon geliştiricileri ve yöneticiler."

Çıktıdan bir bölüm:
- Bulgu: "Yapılandırma" (14 sayfa) yönetici görevlerini tam bir ayarlar tablosuyla karıştırıyor – nasıl yapılır rehberleri ve bir Ayarlar referansı olarak bölünmeli `[VARSAYIM: başlıklara dayanıyor, örnek sayfalarla teyit et]`.
- Bulgu: "İleri Düzey" ve "Diğer" içerik hakkında bir şey söylemiyor; 9 sayfa yeniden dağıtıldı, 3'ü Webhook sayfalarının tekrarı olarak kaldırıldı.
- Sayfa eşleme: "Webhook'lar" → bölünür: "İlk webhook'unuzu alın" (eğitim), "Webhook imzalarını doğrulama" (nasıl yapılır), "Webhook olay türleri" (referans), "Webhook teslimi ve yeniden denemeler hakkında" (açıklama).
