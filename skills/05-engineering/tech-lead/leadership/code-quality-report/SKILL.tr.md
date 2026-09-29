---
description: Statik analiz ve kod metriklerini (kapsam, karmaşıklık, tekrar, code smell'ler, güvenlik açıkları, bağımlılık yaşı) ve trendlerini sinyali gürültüden ayıran, sıcak noktaları değişim sıklığı ve hatalarla ilişkilendiren ve az sayıda önceliklendirilmiş aksiyon öneren bir kod kalitesi raporuna dönüştürür. Teknik lider kod sağlığını ekibe veya yönetime raporlayacağında, kalite kapısı sonuçları veya bir metrik panosu yorumlanacağında ya da refactoring eforunun nereye yatırılacağına karar verilirken kullanılır.
related: tech-debt-assessment, coding-standards, test-gap-finder, refactoring, defect-trend-analysis
prompt: Son üç sürümün statik analiz dökümü ekte. Mühendislik yöneticisi için bir kod kalitesi raporu yaz ve gelecek çeyrekte nereye odaklanmamız gerektiğini söyle.
---

# Kod Kalitesi Raporu

## Amaç
Ham kalite metriklerini kısa ve dürüst bir rapora dönüştürmek: ne iyileşiyor, ne kötüleşiyor, risk gerçekte nerede ve hangi birkaç aksiyon karşılığını verir. Metrikler başlı başına hedef değil, kararlar için kanıttır.

## Ne zaman kullanılır
- Ekip veya yönetim için dönemsel (sürüm, çeyrek) bir kod sağlığı raporu hazırlanacaksa.
- Bir kalite kapısı başarısız olduysa veya bir pano yorum gerektiren endişe verici rakamlar gösteriyorsa.
- Ekip, hangi modüllerin refactoring veya test yatırımını hak ettiğine karar verecekse.

## Ne zaman kullanılmaz
- Tek bir pull request incelenecekse `code-review` veya `clean-code-review` kullanılır.
- Amaç teknik borcun tam envanteri ve geri ödeme planıysa `tech-debt-assessment` kullanılır.
- Kodda test edilmemiş belirli yollar bulunacaksa `test-gap-finder` kullanılır.

## Girdiler
Zorunlu:
- Metrik verisi: statik analiz sonuçları, kapsam veya modül bazında ya da zaman içinde rakamlar içeren bir döküm/ekran görüntüsü açıklaması.

İsteğe bağlı, kaliteyi artırır:
- Trend için birden çok anlık görüntü; değişim sıklığı (dosya/modül başına commit); modül başına hata veya olay sayıları.
- Kalite kapısı eşikleri, kodlama standartları, raporun hedef kitlesi.
- Yakın bağlam: büyük refactoring'ler, yeni modüller, kural seti değişiklikleri.

Metrik verisi yoksa iste. Asla metrik değeri üretme; eksik olanlar `[BİLİNMİYOR]` olur.

## Süreç
1. Hedef kitleyi (ekip veya yönetim) ve dönemi belirle; ayrıntı düzeyini buna göre ayarla.
2. Yorumlamadan önce verinin geçerliliğini kontrol et: anlık görüntülerde aynı kural seti ve kapsam, üretilmiş veya dışarıdan alınmış kod hariç, kapsam aynı yöntemle ölçülmüş. Karşılaştırılabilirliği bozan her durumu işaretle.
3. Her anlık görüntü için ana metrikleri özetle: kapsam (varsa satır ve dal), cyclomatic/bilişsel karmaşıklık, tekrar, code smell'ler, hatalar, önem derecesine göre güvenlik açıkları ve güvenlik sıcak noktaları, eski veya açığı olan bağımlılıklar.
4. Trendleri (yön ve büyüklük) hesapla ve yeni kodun kalitesini genel eski kod seviyelerinden ayır; sabit bir toplam, kötüleşen yeni kodu gizleyebilir.
5. Sıcak noktaları bul: karmaşıklığı yüksek veya kapsamı düşük olup aynı zamanda sık değişen ya da hata üreten modüller. Değişim veya hata verisi yoksa sıcak nokta sıralamasını `[VARSAYIM]` olarak işaretle.
6. Yalnızca tekrarlama, yorumla: olası nedenleri açıkla (ör. testsiz büyük bir modül eklendiği için kapsam düştü) ve her yorumu çıkarım olarak etiketle.
7. Sorunları önceliklendir: önce güvenlik açıkları ve kritik hatalar, sonra sıcak noktalar, sonra tutarlılık ve smell'ler. Düzeltilmek yerine ayarlanması gereken gürültülü kuralları belirt.
8. Üç ile beş aksiyon öner; her birinin sorumlu tipi, kapsamı, adı verilen bir metriğe beklenen etkisi ve doğrulama adımı olsun (ör. "bir sonraki ölçümde billing dal kapsamı ≥ %70").
9. Verinin sınırlarını ve açık soruları belirt.
10. Hedef devam ediyorsa geri ödeme planı için `tech-debt-assessment`, kapsamı düşük sıcak noktalar için `test-gap-finder`, belirli bir modül için `refactoring` öner.

## Çıktı formatı
```markdown
# Kod Kalitesi Raporu: <sistem> · <dönem>
Hedef kitle: <ekip/yönetim> · Veri: <araç/döküm, anlık görüntüler> · Karşılaştırılabilirlik: <uygun / uyarılar>

## Özet
<3-5 cümle: genel yön, en büyük risk, ana öneri>

## Metrikler ve Trend
| Metrik | Önceki | Güncel | Trend | Yorum |
|---|---|---|---|---|

## Sıcak Noktalar
| Modül | Karmaşıklık | Kapsam | Değişim sıklığı | Hatalar | Neden önemli |
|---|---|---|---|---|---|

## Önerilen Aksiyonlar
| # | Aksiyon | Kapsam | Hedef metrik ve değer | Doğrulama |
|---|---|---|---|---|

## Veri Sınırları ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Rapordaki her sayı verilen veriden geliyor; eksik değerler `[BİLİNMİYOR]`.
- [ ] Anlık görüntülerin karşılaştırılabilirliği kontrol edildi ve uyarılar belirtildi.
- [ ] Yeni kodun kalitesi eski kod toplamlarından ayrıldı.
- [ ] Sıcak noktalar en az iki sinyali (ör. karmaşıklık ve değişim sıklığı) birleştiriyor ya da sıralama varsayım olarak etiketlendi.
- [ ] Her önerinin ölçülebilir bir hedefi ve doğrulama adımı var.
- [ ] Güvenlik bulguları ayrı raporlandı ve önem derecesine göre sıralandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Genel bir kapsam yüzdesinin peşine düşmek. Kararlı ve basit koddaki kapsam az şey katar; değişen ve karmaşık koda odaklan.
- Kural seti veya kapsam değişikliğini kalite artışı ya da çöküşü olarak raporlamak. Önce karşılaştırılabilirliği kontrol et.
- Yüzlerce smell listelemek. Yönetimin yöne ve üç aksiyona, ekibin sıcak nokta listesine ihtiyacı var.

## Örnek
Girdi: Kapsam %61 → %58 → %55; tekrar %4'te sabit; 2 yeni kritik güvenlik açığı; en yüksek karmaşıklık billing modülünde ve commit'lerin %40'ı orada.

Zayıf: "Kapsam 6 puan düştü, lütfen daha fazla test yazın."

Güçlü örnekten bir bölüm:
- Özet: Genel kapsam üç sürümde 6 puan düştü; bunun ana nedeni testsiz eklenen yeni dışa aktarma modülü `[VARSAYIM: modül bazlı veriden teyit et]`. Bağımlılıklardaki iki kritik açık bu iterasyonda düzeltilmeli.
- Aksiyon 1: Açığı olan iki kütüphaneyi güncelle; doğrulama: bir sonraki taramada sıfır kritik açık.
- Aksiyon 2: Yeni değişikliklerden önce billing'e karakterizasyon testleri ekle; hedef: bir sonraki ölçümde dal kapsamı ≥ %60.
