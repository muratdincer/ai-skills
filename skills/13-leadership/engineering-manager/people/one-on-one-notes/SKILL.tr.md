---
name: one-on-one-notes
description: "Birebir görüşmenin ham notlarını veya dökümünü; konuşulan konular, sorumlu ve tarihli taahhütler, verilen/alınan geri bildirim ve takip edilecek kariyer veya iyi oluş sinyallerinden oluşan kısa ve olgusal notlara dönüştürür. Bir ekip üyesi veya mentiyle yapılan birebirden sonra ya da ileride değerlendirme ve gelişim planlarını besleyecek sürekli bir birebir kaydı tutarken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: people
  title: "Birebir görüşme notları"
  related: "one-on-one-prep, action-item-extraction, performance-review, career-development-plan, meeting-notes"
  prompt: "Bugün Emre ile yaptığım birebirin notlarını düzenle ve ikimizin de neyi taahhüt ettiğini çıkar."
---

# Birebir Görüşme Notları

## Amaç
Taahhütleri görünür tutan, sonraki değerlendirmeler için kanıt saklayan ve çalışanın mahremiyetine saygı gösteren kısa ve olgusal bir birebir kaydı üretmek.

## Ne zaman kullanılır
- Birebirden hemen sonra; kaba notlardan, maddelerden veya dökümden.
- Her ekip üyesi için değerlendirme ve gelişim planlarını besleyen sürekli bir kayıt tutarken.
- Birebirde çıkan bir taahhüdün veya endişenin kapanışa kadar izlenmesi gerektiğinde.

## Ne zaman kullanılmaz
- Sonraki görüşmeye hazırlanmak için `one-on-one-prep` kullanılır.
- Grup veya ekip toplantısı notları için `meeting-notes` kullanılır.
- Performans sorununun resmi olarak belgelenmesi için `underperformance-plan` kullanılır.

## Girdiler
Zorunlu:
- Birebirin ham notları veya dökümü ile çalışanın adı ya da takma adı.

İsteğe bağlı, kaliteyi artırır:
- Tarih, önceki notlar, birebir planı.
- Notların çalışanla paylaşılıp paylaşılmayacağı (önerilen) veya özel tutulacağı.

Ham notlar yoksa iste. Konuşmayı hafızaya dayalı ipuçlarından yeniden kurgulama.

## Süreç
1. Ham içeriği konulara göre grupla; karar, taahhüt veya sinyal taşımayan sohbeti çıkar.
2. Her konu için konuşulanı tarafsız bir dille yaz. Görüşleri olgu gibi değil, kişiye atfederek yaz ("Emre ... düşünüyor").
3. Tüm taahhütleri çıkar. Sorumluyu (çalışan veya yönetici), somut aksiyonu ve tarihi yaz; tarih yoksa `[TBD]` ile işaretle.
4. Verilen ve alınan geri bildirimi, yöneticiye verilen geri bildirim dahil, durum-davranış-etki biçiminde kaydet.
5. Kariyer ve gelişim sinyallerini yakala: hedefler, ilgi alanları, geliştirmek istediği beceriler, gelişimle ilgili hayal kırıklıkları.
6. İyi oluş veya elde tutma sinyallerini yalnızca çalışanın söylediği biçimde kaydet; teşhis koyma, spekülasyon yapma.
7. Birebir dışında aksiyon gerektiren maddeleri (eskalasyon, İK, başka ekip) ve bunları kimin üstlendiğini işaretle.
8. Hassas kişisel verileri (sağlık, aile, hukuki) çalışan açıkça istemedikçe çıkar veya genelleştir ve en aza indirildiğini not et.
9. Önceki notlardaki açık maddelere bağlantı kur; çözülenleri kapat.
10. Paylaşılabilir bir sürüm üret ve yöneticinin özel notlarında kalması gerekenleri işaretle.
11. Kullanıcının hedefi devam ediyorsa bir sonraki görüşme için `one-on-one-prep` veya kariyer sinyalleri tekrarlanıyorsa `career-development-plan` öner.

## Çıktı formatı
```markdown
# Birebir Notları: <ad> – <tarih>

## Konular
- **<konu>**: <tarafsız özet; görüşler kişiye atfedilmiş>

## Taahhütler
| # | Aksiyon | Sorumlu | Tarih | Durum |
|---|---|---|---|---|

## Geri Bildirim
- <ad> için: <durum – davranış – etki>
- <ad>'dan yöneticiye: ...

## Kariyer ve Gelişim Sinyalleri
- ...

## İyi Oluş / Elde Tutma Sinyalleri (söylendiği gibi)
- ...

## Önceki Görüşmeden Aktarılan / Kapanan
- ...

## Özel Not (paylaşılmaz) – isteğe bağlı
- ...
```

## Kalite kontrol listesi
- [ ] Her taahhüdün sorumlusu ve tarihi ya da `[TBD]` işareti var.
- [ ] Görüşler ve yorumlar olgu olarak değil, kişiye atfedilerek yazıldı.
- [ ] Kişilik veya sağlık hakkında teşhis, spekülasyon ya da etiket yok.
- [ ] Hassas kişisel veriler en aza indirildi veya çıkarıldı.
- [ ] Paylaşılabilir sürüm çalışanı şaşırtmaz veya mahcup etmez.
- [ ] Önceki açık maddeler açıkça kapatıldı veya aktarıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Notlara yargı yazmak ("tembel", "takım oyuncusu değil"). Yalnızca davranışı ve etkiyi kaydet; notlar ileride bir anlaşmazlıkta okunabilir.
- Yalnızca çalışanın taahhütlerini kaydetmek. En sık unutulanlar yöneticinin taahhütleridir.
- Kişiye söylenenden farklı notlar tutmak. Ortak anlayışı teyit etmek için notları paylaş.

## Örnek
Girdi: "emre - nöbet onu bitiriyor, geçen hafta gece 3 çağrı. k8s öğrenmek istiyor. alarm gürültüsünü platform ekibiyle konuşacağım. cumaya kadar ödeme job'ı için runbook yazacak."

Çıktıdan bir bölüm:
- **Nöbet yükü**: Emre geçen hafta gece üç çağrı aldığını ve bu yükün sürdürülemez olduğunu belirtiyor.
- Taahhütler: 1) Alarm gürültüsünü platform ekibine iletmek – Sorumlu: yönetici – Tarih: `[TBD]`. 2) Ödeme job'ı için runbook – Sorumlu: Emre – Tarih: Cuma.
- Gelişim sinyali: Kubernetes becerilerini geliştirmek istiyor.
