---
name: budget-proposal
description: "Yatırım (değişim) ile işletim maliyetlerini ayıran, her kalemi bir iş sonucuna bağlayan, finanse edilmemenin maliyetini gösteren ve sonuçlarıyla birlikte finansman senaryoları sunan bir teknoloji bütçe teklifi yazar. Bir teknoloji yöneticisi yıllık veya proje bütçesi istemek ya da savunmak, kişi sayısı, lisans veya bulut harcamasını gerekçelendirmek ya da finans veya üst yönetime seçenek sunmak zorunda olduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: executive
  area: strategy
  title: "Bütçe teklifi yazma"
  related: "technology-strategy, cost-benefit-analysis, cloud-cost-estimate, budget-plan, board-update"
  prompt: "Gelecek yılın BT bütçe teklifini hazırla; bulut ve lisanslar yüzünden işletim maliyetleri %12 artıyor, ayrıca bir veri platformu ve 4 mühendis daha için finansman istiyoruz."
---

# Bütçe Teklifi Yazma

## Amaç
Karar vericilere bilinçli olarak onaylayabilecekleri, azaltabilecekleri veya reddedebilecekleri bir bütçe talebi sunmak: Her kalem gerekçeli, işletim ve değişim maliyetleri ayrı ve her finansman senaryosu kurumun ne kazandığını ve neden vazgeçtiğini gösteriyor.

## Ne zaman kullanılır
- Bir teknoloji departmanı veya büyük bir alan için yıllık bütçe hazırlanırken.
- Yeni bir girişim, kişi sayısı, lisans veya altyapı için finansman istenirken.
- Finans kesinti veya senaryo istiyor ve sonuçların açıkça görülmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Onaylanmış bir projenin ayrıntılı maliyet planı için `budget-plan` kullanılır.
- Tek bir girişimin kendini amorti edip etmediğine karar vermek için `cost-benefit-analysis` kullanılır.
- Belirli bir tasarımın bulut maliyetini tahmin etmek için `cloud-cost-estimate` kullanılır.

## Girdiler
Zorunlu:
- Mevcut maliyet tabanı veya geçen yılın gerçekleşenleri (en azından ana kategoriler bazında) ve önerilen yeni harcama kalemleri.

İsteğe bağlı, kaliteyi artırır:
- Bütçenin desteklediği strateji ve hedefler; sözleşme yenilemeleri ve fiyat değişiklikleri; kişi sayısı planı.
- Finans kuralları: capex/opex ayrımı, para birimi, enflasyon varsayımları, onay eşikleri.
- İşletim maliyetini süren kullanım eğilimleri (kullanıcı, işlem, veri hacmi).

Maliyet tabanı yoksa iste. Asla tutar, oran veya fiyat uydurma; boşlukları `[BİLİNMİYOR]`, tahminleri dayanağıyla birlikte `[VARSAYIM]` olarak işaretle.

## Süreç
1. Tabanı oluştur: geçen dönemin kategori bazında gerçekleşenleri (personel, lisans/abonelik, bulut/barındırma, donanım, hizmet/yüklenici, eğitim) ve bilinen bağlayıcı sözleşmeler.
2. İşletimi (kullanım, fiyat ve sözleşme değişikliklerinden gelen zorunlu artış dahil sistemi ayakta tutma) değişimden (yeni yatırımlar) ayır; her işletim artışını sürücüsüyle açıkla.
3. Her yatırım için iş sonucunu, hizmet ettiği hedefi, zaman içindeki maliyet profilini (tek seferlik ve tekrarlayan, ardından gelen işletim maliyeti dahil) ve ilk görünür faydayı yaz.
4. Her kalemin finanse edilmemesinin maliyetini ve riskini (uyum açığı, kesinti riski, kaçan gelir, artan bakım) mümkünse kanıtla belirt.
5. Tasarruf ve dengeleme kalemlerini bul: sistem kapatma, lisans konsolidasyonu, doğru boyutlandırma, sözleşme yeniden müzakeresi; teyit edilmemiş tasarrufları `[VARSAYIM]` olarak işaretle.
6. 2-3 senaryo kur (ör. temel, önerilen, azaltılmış) ve hangi kalemlerin senaryolar arasında yer değiştirdiğini ve her birinde hangi sonucun kaybedildiğini tam olarak yaz.
7. Kullanıcının verdiği finans kurallarını (capex/opex, para birimi, enflasyon) uygula; bilinmiyorsa tahmin etmek yerine açık soru olarak listele.
8. Riskleri ve duyarlılıkları ekle: döviz kuru, kullanım artışı, işe alım zamanlaması, tedarikçi fiyat değişiklikleri.
9. Dönem boyunca harcamanın ve sonuçların nasıl izlenip raporlanacağını tanımla.
10. Tek sayfalık özet yaz: toplam talep, geçen döneme göre değişim, önerilen senaryo, ilk üç gerekçe.
11. Kullanıcının hedefi devam ediyorsa sunum için `board-update`, tartışmalı bir kalem için `cost-benefit-analysis` veya işi aşamalandırmak için `quarterly-planning` öner.

## Çıktı formatı
```markdown
# Bütçe Teklifi <dönem>: <organizasyon/alan>

## Özet
- Toplam talep: <tutar> (geçen döneme göre <+/-%x>) – önerilen senaryo: <ad>
- Ana gerekçeler: 1) ... 2) ... 3) ...

## Taban (geçen dönem gerçekleşen)
| Kategori | Gerçekleşen | Gelecek dönem bağlayıcı | Kaynak |
|---|---|---|---|

## İşletim Maliyetleri
| Kategori | Gelecek dönem | Değişim | Sürücü |
|---|---|---|---|

## Yatırımlar
| Kalem | Sonuç / hedef | Tek seferlik | Tekrarlayan | İlk fayda | Finanse edilmemenin maliyeti |
|---|---|---|---|---|---|

## Tasarruf ve Dengelemeler
- ...

## Senaryolar
| Senaryo | Toplam | Dahil | Hariç | Sonuç |
|---|---|---|---|---|

## Riskler, Duyarlılıklar, Varsayımlar
- [VARSAYIM] ...

## İzleme ve Raporlama
- ...
```

## Kalite kontrol listesi
- [ ] İşletim ve değişim maliyetleri ayrı; her işletim artışının bir sürücüsü var.
- [ ] Her yatırım bir sonucu, ardından gelen işletim maliyetini ve finanse edilmemenin maliyetini belirtiyor.
- [ ] Senaryolar yalnızca daha düşük bir rakamı değil, neyin kaybedildiğini gösteriyor.
- [ ] Uydurulmuş tutar, fiyat veya tasarruf yok; her rakamın kaynağı ya da `[VARSAYIM]` etiketi var.
- [ ] Özet tek sayfaya sığıyor ve önerilen senaryoyu belirtiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yatırımların tekrarlayan maliyetini gizlemek. Yeni bir platform gelecek yılın işletim bütçesine lisans, bulut ve personel ekler; bunu şimdiden göster.
- Sürücüsü olmayan yüzde artış talepleri ("büyüme için +%10"). Finans açıklanmayanı keser.
- Tek bir rakam sunmak. Senaryo yoksa karar keyfi bir kesintiye dönüşür.

## Örnek
Girdi: Bulut ve lisanslardan işletim +%12; bir veri platformu ve 4 mühendis talebi.

Çıktıdan bir bölüm:
- İşletim sürücüsü: işlem artışından bulut +`[BİLİNMİYOR]` ve fiyat artışlı bir lisans yenilemesi `[sözleşme koşullarını teyit et]`.
- Zayıf gerekçe (kaçın): "Veri platformu stratejiktir." Güçlü: "Veri platformu aylık 3 manuel raporu ortadan kaldırır ve fiyatlama hedefini mümkün kılar; finanse edilmezse yasal rapor tablolarda kalır (denetim bulgusu riski)."
- Azaltılmış senaryo: yalnızca veri platformu 1. faz, 2 mühendis; sonuç: fiyatlama analitiği 2 çeyrek kayar `[VARSAYIM]`.
