---
name: onboarding-guide
description: "Bir ekibe, departmana veya projeye yeni katılan kişiyi bağlam, çalışma biçimi, araçlar ve erişimler, kilit kişiler, terimler ve açık \"hazırsın\" kilometre taşlarıyla sıralanmış ilk görevler boyunca yönlendiren bir oryantasyon rehberi yazar. Ekibe yeni üyeler, yükleniciler veya transferler katılacaksa, mevcut oryantasyon bilgisi wiki ve sohbetlere dağılmışsa ya da bir rol veya ekip için \"oryantasyon rehberi yaz\" dendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: knowledge
  area: capture
  title: "Oryantasyon rehberi yazma"
  related: "onboarding-plan-30-60-90, technical-onboarding, handover-document, glossary-builder, kb-article"
  prompt: "Ödeme ekibimize katılan yeni iş analistleri için bir oryantasyon rehberi yaz."
---

# Oryantasyon Rehberi Yazma

## Amaç
Yeni gelenin bağımsız katkı vermeye başlamasına kadar geçen süreyi kısaltmak ve bunu, o an açıklama yapmaya kimin müsait olduğundan bağımsız hâle getirmek. Rehber yeniden kullanılabilir bir yol sunar: neyin anlaşılacağı, kiminle tanışılacağı, neyin kurulacağı ve önce ne yapılacağı, sırasıyla.

## Ne zaman kullanılır
- Ekibe yeni üyeler, yükleniciler veya şirket içi transferler katılacaksa.
- Oryantasyon bilgisi wiki'lere, sohbetlere ve kişilere dağılmışsa.
- Yeni gelenler aynı soruları tekrar tekrar soruyor veya üretken olmaları uzun sürüyorsa.

## Ne zaman kullanılmaz
- Belirli bir çalışanın ilk üç ayı için hedefli kişisel plan gerekiyorsa `onboarding-plan-30-60-90` kullanılır.
- Geliştirici ortamı kurulumu ve kod tabanında ayrıntılı gezinti için `technical-onboarding` kullanılır.
- Belirli bir sistem veya projenin sahipliği devrediliyorsa `handover-document` kullanılır.

## Girdiler
Zorunlu:
- Ekip veya proje ve rehberin hitap ettiği rol(ler).

İsteğe bağlı, kaliteyi artırır:
- Ekibin misyonu, ürünler/sistemler, paydaşlar, çalışma anlaşmaları, toplantı ritmi.
- Araç listesi ve erişim talep süreci, mevcut dokümanlar, sözlük, organizasyon şeması.
- Tipik ilk görevler ve bu rol için "üretken olmanın" ne anlama geldiği.

Ekip veya rol belirtilmemişse sor. Geri kalanını en fazla 5 soruluk odaklı gruplarla topla, daha önce verilenleri tekrar sorma; cevaplanmayanları rehber sahibi için `[TBD]` olarak bırak.

## Süreç
1. Hedef kitleyi (rol, kıdem, iç veya dış) ve hedefi tanımla: yeni gelen neyi, ne zamana kadar bağımsız yapabilmeli. Hedef verilmemişse önerdiğin hedefi `[VARSAYIM]` olarak işaretle.
2. Bağlam katmanını yaz: ekibin neden var olduğu, kime hizmet ettiği, neyin sahibi olduğu, organizasyona nasıl oturduğu ve güncel öncelikler. Yalnızca yeni gelenin ilk haftada ihtiyaç duyacağı kadarını yaz.
3. Çalışma biçimini anlat: planlama ritmi, düzenli toplantılar ve amaçları, iş öğelerinin nasıl aktığı, kullanılıyorsa hazır/bitti tanımları, karar ve eskalasyon yolları, iletişim normları (hangi konu için hangi kanal, cevap beklentisi).
4. Araçları ve erişimleri kontrol listesi olarak sırala: araç, amaç, nasıl talep edilir, tipik bekleme süresi, onaylayan. İlk görevleri engelleyenden başlayarak sırala. Asla kimlik bilgisi yazma.
5. Kişi haritasını çıkar: role göre kilit kişiler (yönetici, buddy, ürün/iş muhatabı, teknik lider, operasyon, kilit paydaşlar) ve her birine hangi konuda gidileceği. İsim bilinmiyorsa rol kullan.
6. Terimleri topla: ekibe özgü terimler, kısaltmalar ve sistem adları, tek satırlık tanımlarıyla ya da sözlüğe yönlendirerek.
7. İlk görevleri düşük riskten gerçek katkıya doğru sırala (oku, gözlemle, eşli çalış, gözden geçirmeyle yap, tek başına yap); her birine öğrenme hedefi ve "bitti" sinyali ekle.
8. Kilometre taşlarını her dönem için (örneğin ilk hafta, ilk ay) yalnızca aktivite listesi olarak değil, gözlemlenebilir hazırlık kontrolleri olarak tanımla.
9. Geri bildirim döngüsü ekle: yeni gelen ve buddy'nin ne zaman görüşeceği ve yeni gelenin rehberdeki eksikleri nasıl bildireceği ki rehber güncellensin.
10. Rehbere sahip ve gözden geçirme aralığı ata; sık değişen bilgileri kopyalamak yerine kaynağa bağlantı verecek şekilde işaretle.
11. Hedef devam ediyorsa sonraki beceriyi öner: kişisel plan için `onboarding-plan-30-60-90`, mühendislik kurulumu için `technical-onboarding`, terimler bölümü büyükse `glossary-builder`.

## Çıktı formatı
```markdown
# Oryantasyon Rehberi: <ekip/proje> — <rol>
Kimin için: <hedef kitle> · Hedef: <zaman veya TBD> içinde <yetkinlik> konusunda bağımsız · Sahibi: <rol> · Gözden geçirme: <aralık>

## 1. Neden Varız ve Neyin Sahibiyiz
## 2. Nasıl Çalışırız
- Ritim ve toplantılar: ... · İş akışı: ... · Kararlar ve eskalasyon: ... · İletişim normları: ...
## 3. Araçlar ve Erişimler
| Araç | Amaç | Nasıl talep edilir | Bekleme süresi | Onaylayan | Tamam |
|---|---|---|---|---|---|
## 4. Tanışılacak Kişiler
| Rol / isim | Hangi konuda | Ne zaman |
|---|---|---|
## 5. Terimler
- <terim>: <tanım>
## 6. İlk Görevler
| # | Görev | Biçim (oku/gözlemle/eşli/gözden geçirmeli/tek başına) | Öğrenme hedefi | Bitti sayılır |
|---|---|---|---|---|
## 7. Kilometre Taşları
- 1. hafta sonu: <gözlemlenebilir hazırlık kontrolü>
- 1. ay sonu: ...
## 8. Geri Bildirim ve Yardım
- Buddy görüşmeleri: ... · Rehberdeki eksikler şuraya bildirilir: ...
## Rehber Sahibi İçin Açık Maddeler
- [TBD] ...
```

## Kalite kontrol listesi
- [ ] Rehber, rol için "bağımsız"ın ne demek olduğunu ve ne zamana kadar beklendiğini belirtiyor (ya da `[VARSAYIM]`/`[TBD]` olarak işaretliyor).
- [ ] Erişim maddeleri ilk görevleri engelleme sırasına göre dizilmiş, bekleme süreleri ya da `[TBD]` içeriyor.
- [ ] İlk görevler gözlemden tek başına yapmaya doğru ilerliyor ve her birinin bitti sinyali var.
- [ ] Kilometre taşları aktivite listesi değil, gözlemlenebilir kontroller.
- [ ] Kimlik bilgisi veya gereksiz kişisel veri yok; sık değişen bilgiler kaynağa bağlanmış.
- [ ] Ekip hakkında hiçbir şey uydurulmamış; boşluklar rehber sahibi için listelenmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İlk gün tüm bağlantıları yığmak. Bilgiyi ihtiyaç duyulduğu zamana göre sırala; ilk hafta bağlam, erişim ve kişilerdir.
- Erişim bekleme sürelerini unutmak; yeni gelen bir hafta boş bekler. Engelleyici erişimleri başlangıç tarihinden önce talep et.
- Rehberin sahipsiz kalması. İlk yeniden yapılanmadan sonra eskir; bir sahip ata ve her yeni gelenden bir eksiği düzeltmesini iste.

## Örnek
Girdi: "Ödeme ekibine yeni iş analistleri katılıyor. Kart akışlarını, backlog aracımızı ve fraud ekibini anlamaları gerekiyor."

Çıktıdan bir bölüm:
- Hedef: 1. ayın sonunda bir kart ödeme değişikliği için iş öğesini yalnızca gözden geçirme desteğiyle yazıp olgunlaştırır `[VARSAYIM]`.
- Erişim: backlog aracı — iş öğeleri için — talep yolu `[BİLİNMİYOR: erişim süreci]` — bekleme süresi `[TBD]`.
- İlk görev 2: fraud ekibiyle bir olgunlaştırma (refinement) oturumunu gözlemle — öğrenme hedefi: chargeback kurallarını anlamak — bitti sayılır: chargeback akışını buddy'ye kendi cümleleriyle anlatabildiğinde.
