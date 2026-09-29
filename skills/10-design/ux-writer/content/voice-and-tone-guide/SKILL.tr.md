---
description: Bir ürün veya marka için ses ve ton rehberi yazar; her biri ne olduğu ve ne olmadığıyla tanımlanan 3-5 ses ilkesi, yap/yapma örnek çiftleri, kullanıcı bağlamına göre değişen bir ton haritası (başarı, hata, ilk kullanım, hassas anlar), dil bilgisi ve terminoloji kuralları ile yazarlar için bir gözden geçirme listesi içerir. Bir üründe tutarlı arayüz yazımı olmadığında, birden fazla ekip farklı yazdığında, yeni bir dile veya pazara girilirken ya da mevcut rehber uygulanamayacak kadar belirsiz olduğunda kullanılır.
related: microcopy, error-message-writing, style-guide-check, positioning-statement, glossary-builder
prompt: B2B faturalama uygulamamız için Türkçe ve İngilizce bir ses ve ton rehberi oluştur; metinlerimiz şu an her ekranda farklı konuşuyor.
---

# Ses ve Ton Rehberi

## Amaç
Ürün metni yazan herkese ürünün nasıl konuştuğuna dair ortak ve sınanabilir bir tanım vermek. Böylece metinler ekranlar, ekipler ve diller arasında tutarlı kalırken ton kullanıcının durumuna uyum sağlar.

## Ne zaman kullanılır
- Arayüz ve mesaj metinleri ekipler veya özellikler arasında tutarsız olduğunda.
- Ürün lansman, yeniden markalaşma ya da yeni bir dil veya pazara açılma aşamasındayken.
- Mevcut ses rehberi sıfatları ("samimi, akıllı") sıralıyor ama yazarlar onu uygulayamıyorsa.

## Ne zaman kullanılmaz
- Belirli ekranlar için hemen metin gerekiyorsa `microcopy` veya `error-message-writing` kullanılır.
- Bir doküman mevcut bir rehbere göre kontrol edilecekse `style-guide-check` kullanılır.
- Yazım üslubu değil pazar konumlandırması gerekiyorsa `positioning-statement` kullanılır.

## Girdiler
Zorunlu:
- Ürün tanımı ve birincil hedef kitle (metni kim, hangi bağlamda okuyor).
- En az birkaç gerçek metin örneği ya da henüz örnek olmadığı bilgisi.

İsteğe bağlı, kaliteyi artırır:
- Marka değerleri, konumlandırma, mevcut marka kılavuzu.
- Hedef diller ve hitap kuralları (ör. Türkçede "siz" veya "sen").
- Tonla ilgili bilinen kullanıcı şikâyetleri; düzenlemeye tabi veya hassas alanlar.

Hedef kitle veya ürün tanımı yoksa sor. Bir seferde en fazla 5 odaklı soru sor ve verilmiş bilgiyi yeniden sorma.

## Süreç
1. Hedef kitleyi özetle: uzmanlık düzeyi, kritik anlardaki duygusal durum, okuma bağlamı (masa başı, mobil, zaman baskısı altında) ve erişilebilirlik ya da sade dil ihtiyaçları.
2. Verilen metin örneklerini denetle: hitap, kişi, terminoloji, büyük harf kullanımı ve duygu tutarsızlıklarını not et. Her ilkenin gerekçesi bu bulgulardır; örnek yoksa ilkelerin gerçek metin gelene kadar `[VARSAYIM]` olduğunu belirt.
3. 3-5 ses ilkesi çıkar. Her birini "X, Y değil" kalıbıyla tanımla (ör. "Doğrudan, sert değil") ve bu kitleye neden uyduğunu tek satırla açıkla. Hiçbir rakibin itiraz etmeyeceği genel sıfatları reddet.
4. Her ilke için gerçekçi ürün metinleriyle en az bir yap/yapma çifti yaz.
5. Ton haritası oluştur: kritik bağlamlar (ilk kullanım, rutin görev, başarı, uyarı, hata, veri kaybı veya güvenlik, faturalama, hassas kişisel anlar) için resmiyet, sıcaklık, mizah ve aciliyet gibi ayarları belirle ve örnek bir satır ekle.
6. Dil bazında dil mekaniğini belirle: hitap biçimi, kişi (biz/siz), cümle veya başlık düzeni büyük harf, kısaltmalar, sayılar, tarihler, para birimi, noktalama, emoji politikası, kapsayıcı ve cinsiyetsiz dil.
7. Bir başlangıç terim listesi oluştur: tercih edilen terimler, yasaklı terimler ve yerlerine geçenler; tam sözlük için `glossary-builder` becerisine yönlendir.
8. Erişilebilirlik ve sade dil kurallarını ekle: hedef okunabilirlik düzeyi, cümle uzunluğu, çevrilemeyen deyimlerden kaçınma, bağlantı metni kuralları.
9. Yazarların her metne uygulayacağı kısa bir kontrol listesi ve yönetişim notu yaz: sahibi, değişiklik önerme yolu, örneklerin toplandığı yer.
10. Kanıta dayalı kuralları (denetimden gelenler) senin önerdiğin tercihlerden ayır; tercihleri paydaş onayı için `[VARSAYIM]` olarak etiketle.
11. Hedef devam ediyorsa rehberi uygulamak için `microcopy` veya `error-message-writing`, mevcut içeriği rehbere göre denetlemek için `style-guide-check` öner.

## Çıktı formatı
```markdown
# Ses ve Ton Rehberi: <ürün>
## Hedef Kitle
- ...

## Ses İlkeleri
### 1. <X, Y değil>
Neden: ...
| Yap | Yapma |
|---|---|

## Ton Haritası
| Bağlam | Resmiyet | Sıcaklık | Mizah | Aciliyet | Örnek |
|---|---|---|---|---|---|

## Dil Mekaniği
| Kural | EN | TR |

## Terminoloji
| Kullan | Kaçın | Not |

## Erişilebilirlik ve Sade Dil
- ...

## Yazar Kontrol Listesi
- [ ] ...

## Yönetişim
- Sahibi: ...  - Değişiklik süreci: ...

## Doğrulanacak Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Her ilke "X, Y değil" kalıbında ve en az bir gerçekçi yap/yapma çifti var.
- [ ] Ton haritası hata, başarı ve en az bir yüksek riskli bağlamı kapsıyor.
- [ ] Mekanik kurallar hitap biçimi dahil her hedef dil için ayrı belirtilmiş.
- [ ] Kurallar hedef kitleye veya metin denetimine dayanıyor; öneriler `[VARSAYIM]` olarak etiketli.
- [ ] Bir yazar iki taslak arasında yalnızca bu rehberle karar verebiliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sıfat listeleri ("samimi, yenilikçi, insani"). Sınanamazlar; sınırları "değil" ve örneklerle çiz.
- Her yerde tek ton. Ses sabit kalır; ton hatalarda, faturalamada ve güvenlikte sakinleşmelidir.
- İngilizce rehberi çevirmek. Resmiyet, hitap ve mizah her dilde farklı işler; kuralları o dilde kur.

## Örnek
Girdi: "Muhasebeciler için B2B faturalama uygulaması, EN ve TR; metinler 'sen' ile 'siz'i karıştırıyor, hata mesajlarında espri var."

Zayıf ilke: "Samimi — ulaşılabilir ve eğlenceliyiz."

Güçlü ilke: "Kesin, bilgiçlik taslamayan." Neden: muhasebeciler tam rakam ve tarihlere göre iş yapar.
| Yap | Yapma |
|---|---|
| "1042 numaralı faturanızın son ödeme tarihi 15 Mart." (her zaman "siz") | "Faturan yakında patlıyor!" |
| EN: "Invoice #1042 is due on 15 March." | EN: "Heads up! Something's due soon 🙂" |
