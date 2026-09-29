---
description: Bir ürün, pazara giriş veya stratejik karar için PESTLE analizi (politik, ekonomik, sosyal, teknolojik, yasal, çevresel) yapar; her faktörü etki, olasılık ve zaman ufkuna göre puanlar ve en önemli faktörleri somut ürün ve iş etkilerine çevirir. Yeni bir pazara veya ülkeye girerken, strateji veya yol haritası gözden geçirilirken, mevzuat veya makro risk değerlendirilirken ya da PESTEL/PEST veya "dış çevre" taraması istendiğinde kullanılır.
related: market-analysis, swot-analysis, porters-five-forces, product-strategy-one-pager, assumption-mapping
prompt: KOBİ bordro SaaS ürünümüzü gelecek yıl Almanya'da piyasaya sürmek için PESTLE analizi yap.
---

# PESTLE Analizi

## Amaç
Bir ürün veya kararın etrafındaki makro çevreyi taramak ve gerçekten önemli olan birkaç faktörü genel bir trend listesi yerine etkilere, aksiyonlara ve izlenecek sinyallere dönüştürmek.

## Ne zaman kullanılır
- Yeni bir ülkeye, bölgeye veya düzenlenmiş bir segmente giriş değerlendirilirken.
- Ürün stratejisi veya çok yıllı yol haritası yenilenirken.
- Büyük bir yatırımdan önce mevzuat, ekonomi veya teknoloji değişimlerine maruziyet değerlendirilirken.

## Ne zaman kullanılmaz
- Soru rakipler ve sektör kârlılığıyla ilgiliyse `porters-five-forces` veya `competitor-analysis` kullanılır.
- İç güçlü ve zayıf yönler dış faktörlerle birleştirilecekse `swot-analysis` kullanılır (PESTLE, fırsat ve tehditlerini besleyebilir).
- Pazar büyüklüğü ve segmentler gerekiyorsa `market-analysis` kullanılır.

## Girdiler
Zorunlu:
- Konu: ürün veya iş, analizin desteklediği pazar/coğrafya ve karar.

İsteğe bağlı, kaliteyi artırır:
- Zaman ufku, hedef segmentler, iş modeli, bilinen mevzuat, kullanıcının güvendiği iç araştırmalar veya kaynaklar.

Konu veya coğrafya yoksa iste. Güncel rakamları, yasaları veya oranları, kullanıcı vermedikçe ya da yerleşik bilgi olmadıkça olgu olarak sunma; bunları kontrol edilecek kaynak türüyle birlikte `[DOĞRULA]` olarak işaretle.

## Süreç
1. Kapsamı çerçevele: konu, coğrafya, segment, desteklenecek karar ve zaman ufku (örneğin 0-12 ay, 1-3 yıl, 3+ yıl).
2. Altı boyutun her biri için bu ürüne ve pazara özgü 3-6 aday faktör listele. Örnekler: Politik (ticaret politikası, kamu alımları, istikrar, kamu dijitalleşme programları); Ekonomik (faiz ve enflasyon dinamikleri, kur, işgücü maliyeti, KOBİ yatırım iştahı); Sosyal (demografi, çalışma biçimleri, güven, dil, dijital okuryazarlık); Teknolojik (platform değişimleri, altyapı, yapay zekâ, birlikte çalışabilirlik standartları); Yasal (GDPR/KVKK gibi veri koruma, sektör kuralları, iş hukuku, vergi, e-fatura, erişilebilirlik); Çevresel (sürdürülebilirlik raporlaması, enerji maliyetleri, müşterilerin ESG şartları).
3. Kaynaklı olguyu, genel bilgiyi ve çıkarımı ayır; her faktörü `[OLGU: kaynak]`, `[DOĞRULA]` veya `[VARSAYIM]` olarak etiketle.
4. Her faktörü puanla: konu üzerindeki Etki (Y/O/D), Olasılık veya kesinlik (Y/O/D), Yön (fırsat / tehdit / ikisi de) ve Zaman ufku.
5. Genel olan veya kararla makul bir bağı olmayan faktörleri çıkar. Kısa bir "değerlendirildi ve elendi" listesi tut.
6. En önemli 5-8 faktör için (Yüksek etki ve en az Orta olasılık) ürün, fiyatlama, pazara çıkış, operasyon veya uyum üzerindeki somut etkiyi yaz.
7. Etkileri aksiyona çevir: zorunlu (uyum, giriş engelleri), yapılmalı (farklılaştırıcılar) ve öncü göstergesi ile gözden geçirme tetikleyicisi olan izleme maddeleri.
8. Faktörler arası etkileşimleri (örneğin teknoloji gereksinimi doğuran bir yasal değişiklik) ve sonucun dayandığı temel varsayımları not et.
9. 3-5 maddede özetle: genel çekicilik veya maruziyet, engelleyici faktörler ve toplanacak sonraki kanıt.
10. Sonraki beceriyi öner: iç yetkinliklerle birleştirmek için `swot-analysis`, sektör yapısı için `porters-five-forces` veya en riskli varsayımları sınamak için `assumption-mapping`.

## Çıktı formatı
```markdown
# PESTLE Analizi: <konu> – <coğrafya> – <ufuk>
**Desteklenen karar:** <...>
**Özet:** <3-5 madde>

| Boyut | Faktör | Kanıt etiketi | Yön | Etki | Olasılık | Ufuk | Etkisi (ne anlama geliyor) |
|---|---|---|---|---|---|---|---|
| Y | <faktör> | [DOĞRULA: resmi kaynak türü] | Tehdit | Y | Y | 0-12 ay | <...> |

## Öncelikli Faktörler ve Aksiyonlar
| Faktör | Aksiyon türü (zorunlu / yapılmalı / izle) | Aksiyon | Öncü gösterge | Sorumlu |
|---|---|---|---|---|

## Etkileşimler
- ...

## Değerlendirilip Elenenler
- <faktör> – <neden>

## Varsayımlar ve Doğrulanacaklar
- [VARSAYIM] ...
- [DOĞRULA] <iddia> – <nereden kontrol edilir>
```

## Kalite kontrol listesi
- [ ] Her faktör genel bir trend değil, bu ürüne ve coğrafyaya özgü.
- [ ] Yasalar, oranlar ve rakamlar ya kullanıcı kaynaklı ya da `[DOĞRULA]` etiketli; hiçbiri uydurulmadı.
- [ ] Her öncelikli faktörün bir etkisi ve somut bir aksiyonu veya göstergesi var.
- [ ] Tehditlerin yanında fırsatlar da yakalandı.
- [ ] Özet, analizin desteklediği karara cevap veriyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Ne olmuş yani?" sorusuna cevap vermeyen ansiklopedik listeler. Tutulan her faktörün bir etkisi olmalı, yoksa elenir.
- Mevzuatı veya ekonomik rakamları hafızadan güncel olgu gibi yazmak. Etiketle ve doğrulamaya yönlendir.
- Yasal ile Politik'i karıştırmak: Politik, politika yönü ve istikrardır; Yasal, bağlayıcı hukuk ve uygulamasıdır.

## Örnek
Girdi: "KOBİ bordro SaaS ürünümüzü gelecek yıl Almanya'da piyasaya sürmek için PESTLE."

Çıktıdan bir bölüm:
| Boyut | Faktör | Kanıt etiketi | Yön | Etki | Olasılık | Ufuk | Etkisi |
|---|---|---|---|---|---|---|---|
| Y | Bordro verisi kişisel ve hassas; GDPR ve çalışan temsilciliği (works council) beklentileri | [DOĞRULA: veri koruma otoritesi ve hukuk danışmanı] | Tehdit | Y | Y | 0-12 ay | Lansmandan önce AB'de veri yerleşimi, veri işleme sözleşmesi şablonları, denetim kayıtları |
| S | Almanca destek ve yerel muhasebe iş ortakları tercihi | [VARSAYIM] | İkisi de | O | Y | 0-12 ay | Mali müşavirlerle iş ortaklığı kanalı; yerelleştirilmiş onboarding |
| T | Zorunlu e-fatura ve dijital raporlama arayüzleri | [DOĞRULA: güncel zorunluluk ve tarihler] | Fırsat | O | O | 1-3 yıl | Sertifikalı arayüzleri farklılaştırıcı olarak sun |
