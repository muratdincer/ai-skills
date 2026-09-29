---
description: Bir ürünün veya sitenin bilgi mimarisini oluşturur; içerik envanteri, düzenleme şeması, site haritası hiyerarşisi, navigasyon modeli, etiketleme sistemi ve bunu doğrulamak için kart sıralama veya ağaç testi planı üretir. Bir ürün, portal veya dokümantasyon sitesi kurulurken ya da yeniden yapılandırılırken, kullanıcılar "aradığını bulamıyorsa" veya navigasyon ve menü etiketlerine karar verilecekse kullanılır.
related: user-flow, wireframe-spec, docs-information-architecture, research-plan, persona
prompt: İK self servis portalımızın navigasyonunu yeniden yapılandır; çalışanlar izin, bordro ve masraf sayfalarını bulamıyor.
---

# Bilgi Mimarisi Oluşturma

## Amaç
İçeriği ve işlevleri, kullanıcıların nerede ne olduğunu ve etiketlerin ne anlama geldiğini tahmin edebileceği şekilde düzenlemek ve bu yapıyı geliştirmeden önce kullanıcılarla doğrulamak. Böylece bulunabilirlik hataları ve destek yükü azalır.

## Ne zaman kullanılır
- Yeni bir ürün, portal veya site tasarlanıyor ve site haritasıyla navigasyona ihtiyaç var.
- Kullanıcılar özellikleri veya içeriği bulamadığını söylüyor ya da arama geçici çözüm olarak kullanılıyor.
- İki ürün veya bölüm birleştiriliyor ve yapıların uzlaştırılması gerekiyor.

## Ne zaman kullanılmaz
- İhtiyaç tek bir görevin adım sırasıysa `user-flow` kullanılır.
- Yapı teknik dokümantasyon (eğitim, nasıl yapılır, başvuru) içinse `docs-information-architecture` kullanılır.
- Bilgi mimarisi netleşti ve tek bir ekranın tanımlanması gerekiyorsa `wireframe-spec` kullanılır.

## Girdiler
Zorunlu:
- Ürünün veya sitenin kapsamı ve ana kullanıcı grupları.

İsteğe bağlı, kaliteyi artırır:
- Mevcut site haritası veya menü, içerik envanteri, analitik (en çok ziyaret edilen sayfalar, arama terimleri, çıkışlar), destek kayıtları, personalar, iş öncelikleri, platform kısıtları (mobil sekme çubuğu sınırı).

Kapsam veya kullanıcı grupları yoksa iste. Eksik envanter veya analitik uydurulmaz, eksik olarak listelenir.

## Süreç
1. Kullanıcı gruplarını ve en önemli görevlerini tanımla (ziyaretlerin çoğunu oluşturan 5-10 görevi hedefle); kanıta dayanan görevleri `[VARSAYIM]` olanlardan ayır.
2. İçerik envanterini oluştur veya gözden geçir: her öğe için tür, sahip, hedef kitle, kullanım sıklığı ve durum (tut, birleştir, kaldır, oluştur).
3. Her seviye için düzenleme şemasını seç: görev bazlı, kitle bazlı, konu bazlı veya kesin (alfabetik, kronolojik). Kullanıcılar departmanlara göre düşünmüyorsa organizasyon şeması yapısından kaçın.
4. Hiyerarşiyi (site haritası) mümkünse en fazla 3 seviye derinlikte taslakla; ana navigasyonda seviye başına 5-9 öğe olsun ve en önemli görevlere 2 tıklama/dokunuşta ulaşılsın.
5. Navigasyon modelini tanımla: genel, yerel, bağlamsal, yardımcı, alt bilgi, arama ve mobil uyarlama; hangi öğenin nerede görüneceğini belirt.
6. Etiketleri kullanıcıların dilinde yaz (arama kayıtlarını ve görüşme dilini kullan); dil bilgisi açısından tutarlı, birbirini dışlayan ve kurum içi jargondan arınmış olsun. Arama için eş anlamlıları listele.
7. Doğrulamayı planla: zihinsel modelleri keşfetmek için açık veya karma kart sıralama (nicel örüntüler için 15-30 katılımcı), ardından taslak hiyerarşi üzerinde görev senaryoları ve başarı hedefleriyle ağaç testi.
8. Ağaç testi görevlerini ve başarı metriklerini tanımla: doğrudan başarı, dolaylı başarı, ilk tıklama doğruluğu, süre; bir hedef belirle (ör. görev başına %70 başarı `[VARSAYIM]`).
9. Yönetişimi kaydet: her bölümün sahibi, yeni içeriğin nereye yerleşeceği ve etiketlerin ne zaman değişebileceği.
10. Varsayımları, riskleri ve açık soruları listele; sonraki adım için `user-flow` ve `wireframe-spec`, doğrulama çalışmasını planlamak için `research-plan` öner.

## Çıktı formatı
```markdown
# Bilgi Mimarisi: <ürün / site>
Kullanıcı grupları: <...> · Kapsam: <...>

## En Önemli Görevler
| # | Görev | Kullanıcı grubu | Kanıt |
|---|---|---|---|

## İçerik Envanteri (özet)
| Öğe | Tür | Hedef kitle | Kullanım | Aksiyon |
|---|---|---|---|---|

## Düzenleme Şeması
<seviye bazında şema ve gerekçe>

## Site Haritası
- 1 <Etiket>
  - 1.1 <Etiket>

## Navigasyon Modeli
<genel, yerel, bağlamsal, yardımcı, arama, mobil>

## Etiketleme
| Etiket | Anlamı / içeriği | Reddedilen alternatifler | Arama eş anlamlıları |
|---|---|---|---|

## Doğrulama Planı
- Kart sıralama: <tür, katılımcı, analiz>
- Ağaç testi: <görevler, doğru yollar, başarı hedefi>

## Yönetişim, Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] En önemli görevler belirlendi ve her birine iki seviye içinde ulaşılıyor.
- [ ] Düzenleme şeması organizasyon şemasını değil, kullanıcıların zihinsel modelini yansıtıyor.
- [ ] Etiketler kullanıcı dilinde, tutarlı ve birbiriyle örtüşmüyor.
- [ ] Derinlik ve genişlik dengeli; hiçbir seviye "diğer" veya "çeşitli" kutusu değil.
- [ ] Geliştirmeden önce başarı hedefli bir kart sıralama ve/veya ağaç testi planlandı.
- [ ] Kanıta dayalı görev ve etiketler varsayımlardan ayrıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Departmanları yansıtmak ("İK Operasyonları", "Finans Hizmetleri"). Kullanıcı "İzin talep et", "Bordrom" diye düşünür.
- Yaratıcı veya markalı etiketler. Bulunabilirlikte sade kelimeler yaratıcı olanları yener.
- Bilgi mimarisini görsel bir prototiple doğrulamak. Görseller yapı sorunlarını gizlemesin diye hiyerarşiyi tek başına ağaç testine sok.

## Örnek
Girdi: "Çalışanlar İK portalında izin, bordro ve masraf sayfalarını bulamıyor."

Çıktıdan bir bölüm:
- En önemli görevler (arama kayıtlarından `[VARSAYIM: kayıtlar henüz verilmedi]`): izin talep etme, bordro görüntüleme, masraf girme, banka bilgisi güncelleme.
- Önce: İK Operasyonları > Zaman Yönetimi > Devamsızlık Talepleri. Sonra: İzinler > İzin talep et.
- Ağaç testi görevi: "Önümüzdeki cuma izin almak istiyorsun. Nereye giderdin?" Doğru yol: İzinler > İzin talep et. Hedef: %80 doğrudan başarı.
