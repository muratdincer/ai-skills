---
description: Ham araştırma verisini (görüşme notları, kullanılabilirlik gözlemleri, açık uçlu anket yanıtları) benzerlik gruplamasıyla kanıta dayalı bulgulara, içgörülere ve önceliklendirilmiş önerilere dönüştürür; her biri için sıklık, önem ve güven düzeyi verir. Görüşmeler veya kullanılabilirlik oturumlarından sonra, "ne öğrendik" sorulduğunda ya da notların bir karar için sunuma dönüşmesi gerektiğinde kullanılır.
related: research-plan, usability-test-script, interview-notes-analysis, feedback-synthesis, customer-journey-map
prompt: 8 onboarding görüşmesinin notlarını ürün ekibi için temel içgörülere ve önerilere dönüştür.
---

# Araştırma Bulgularını Sentezleme

## Amaç
Dağınık gözlemleri kanıta izlenebilen, güven düzeyi konusunda dürüst ve kararlara bağlı az sayıda içgörüye dönüştürmek. Böylece ekip en çarpıcı alıntıya değil, örüntülere göre hareket eder.

## Ne zaman kullanılır
- Saha çalışması (görüşmeler, kullanılabilirlik testleri, günlük çalışmaları, açık uçlu anket yanıtları) tamamlandığında.
- Birden fazla araştırmacının notlarının tek bir görünümde birleştirilmesi gerektiğinde.
- Paydaşlara veya bir karar toplantısına sunum gerektiğinde.

## Ne zaman kullanılmaz
- Yalnızca tek bir görüşme dökümünün yapılandırılması gerekiyorsa `interview-notes-analysis` kullanılır.
- Girdi bir çalışma değil, müşteri geri bildirimi, yorum veya destek kaydı akışıysa `feedback-synthesis` kullanılır.
- Çalışma henüz planlanmadıysa `research-plan` kullanılır.

## Girdiler
Zorunlu:
- Ham araştırma verisi: notlar, dökümler, gözlem tabloları veya anket yanıtları.

İsteğe bağlı, kaliteyi artırır:
- Araştırma planı ve soruları, takma adlı katılımcı profilleri, görev sonuçları, çalışmanın hizmet ettiği karar.

Ham veri verilmediyse iste; özetlerin özetinden sentez yapıyorsan bunu açıkça belirt. Alıntı yapmadan önce isimleri, iletişim bilgilerini ve diğer kişisel verileri çıkar veya maskele.

## Süreç
1. Araştırma sorularını ve kararı yeniden yaz; yoksa materyalden çıkar ve `[VARSAYIM]` olarak işaretle.
2. Veriyi atomik gözlemlere böl (her biri tek bir davranış, alıntı veya sonuç); katılımcı kodu, segment ve görev/konu ile etiketle. Gözlenen davranışı, katılımcının söylediğinden ve senin yorumundan ayrı tut.
3. Gözlemleri aşağıdan yukarıya, benzerliğe göre grupla (hazır kategorilerle başlama). Her grubu bir konu etiketiyle değil, örüntüyü anlatan bir cümleyle adlandır.
4. Her grup için kapsamı say (ör. 8 katılımcının 6'sı); çelişen kanıtları ve segment farklarını not et.
5. Grupları içgörüye dönüştür: gözlem + neden oluyor (altta yatan ihtiyaç veya zihinsel model) + ürün için sonucu. Katılımcılar bunu davranışla göstermediyse "neden" kısmını çıkarım olarak etiketle.
6. Her içgörüyü derecelendir: önem veya etki (Yüksek/Orta/Düşük), güven (kapsam, tutarlılık ve yönteme göre Yüksek/Orta/Düşük); ilgili araştırma sorularına bağla.
7. Kullanılabilirlik verisinde sorunları görev bazında bir önem ölçeğiyle (ör. 0-4: kozmetikten engelleyiciye) ve tamamlama sonuçlarıyla listele.
8. Önerileri çözülecek problemler veya yönler olarak yaz, her birini içgörülere bağla; hızlı düzeltmeleri ek araştırma gerektirenlerden ayır.
9. Çalışmanın cevaplayamayacağı şeyleri (örneklem sınırları, "kaç kişi" soruları) ve açık soruları kaydet.
10. Sunumu hazırla: önce en önemli 3-5 içgörü, sonra ayrıntı ve kanıt eki. Hedef tasarıma veya önceliklendirmeye devam ediyorsa `customer-journey-map` veya `opportunity-solution-tree` öner.

## Çıktı formatı
```markdown
# Araştırma Sentezi: <çalışma>
Katılımcılar: <n, segmentler> · Yöntem: <yöntem> · Tarihler: <tarihler>

## Temel İçgörüler
1. **<içgörü cümlesi>** — Kapsam: <n'de x> · Etki: <Y/O/D> · Güven: <Y/O/D>
   - Kanıt: K3 "<alıntı>", K5 <davranış>
   - Neden (çıkarım): ...
   - Sonuç: ...

## Kullanılabilirlik Sorunları (varsa)
| Görev | Sorun | Katılımcılar | Önem (0-4) | Kanıt |
|---|---|---|---|---|

## Öneriler
| # | Öneri | Dayanağı | Tür (hızlı düzeltme / tasarım / araştırma) |
|---|---|---|---|

## Sınırlar ve Açık Sorular
- ...

## Ek: Gruplar ve Gözlemler
- <grup> → K1, K4, K6
```

## Kalite kontrol listesi
- [ ] Her içgörü en az iki katılımcıdan kanıt gösteriyor ya da tek vakalık sinyal olarak işaretli.
- [ ] Gözlenen davranış, beyan edilen ifade ve yorum birbirinden ayırt edilebiliyor.
- [ ] Kapsam sayıları gerçek; küçük örneklemden şişirilmiş yüzdeler yok.
- [ ] Çelişen kanıtlar ve segment farkları raporlandı.
- [ ] Alıntılar takma adlı ve kişisel veri içermiyor.
- [ ] Öneriler içgörülere dayanıyor ve test edilmemiş çözümleri olgu gibi sunmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İçgörü yerine konu kutuları ("Navigasyon", "Fiyatlandırma") oluşturmak. Ne olduğunu ve nedenini yaz.
- 5 katılımcıdan "kullanıcıların %60'ı" diye raporlamak. Sayı kullan ve nitel sınırları belirt.
- Ekibin planını doğrulayan alıntıları seçmek. Örüntünün yanında çelişen vakaları da göster.

## Örnek
Girdi: 8 onboarding görüşmesinin notları.

Zayıf: "Onboarding: kullanıcılar kurulumda sorun yaşadı."
Güçlü: "**Yeni yöneticiler, çalışma alanını önce 'toparlamak' istedikleri için ekip arkadaşlarını davet etmeyi erteliyor** — Kapsam: 8'de 5 · Etki: Yüksek · Güven: Orta. Kanıt: K2 'Bu dağınıklığı görmelerini istemem'; K6 davet penceresini iki kez kapattı. Sonuç: kayıt anındaki davet çağrıları görmezden geliniyor; ekip aktivasyonu gecikiyor."
