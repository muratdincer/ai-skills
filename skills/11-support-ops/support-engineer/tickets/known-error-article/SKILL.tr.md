---
name: known-error-article
description: "Destek bilgi bankası için bilinen hata makalesi yazar: aranabilir belirti, kapsam ve etkilenen sürümler, doğrulanmış veya şüphelenilen neden, riskleriyle adım adım geçici çözüm, kalıcı çözüm durumu ve ilişkili kayıtlar. Bir problemin kök nedeni veya geçici çözümü belgelendiğinde, aynı kayıt tekrar tekrar geldiğinde ya da kalıcı çözüm beklenirken destek ekibinin tutarlı bir yanıt vermesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 11-support-ops
  role: support-engineer
  area: tickets
  title: "Bilinen hata makalesi"
  related: "problem-management, ticket-response, ticket-triage, how-to-guide, faq-builder"
  prompt: "Bilinen hata makalesi yaz: 7.3 sürümünden beri 10.000 satırı aşan raporlarda PDF dışa aktarma 'Error 500' ile başarısız oluyor; geçici çözüm CSV'ye aktarmak; düzeltme 7.4'te planlandı."
---

# Bilinen Hata Makalesi

## Amaç
Herhangi bir destek uzmanının veya kullanıcının bilinen bir sorunu belirtisinden saniyeler içinde tanıyıp güvenli bir geçici çözüm uygulamasını sağlamak. Böylece tekrarlayan kayıtlar ilk temasta çözülür, kalıcı çözüm durumu herkese aynı şekilde iletilir.

## Ne zaman kullanılır
- Problem yönetimi bir kök nedeni veya geçici çözümü doğruladığında.
- Aynı belirti birden çok kayıtta görüldüğünde ve destek uzmanları farklı yanıtlar verdiğinde.
- Bir hata kabul edildiğinde ama kalıcı çözüm bir veya daha fazla sürüm alacağında.

## Ne zaman kullanılmaz
- Neden, olaylar genelinde hâlâ araştırılıyorsa önce `problem-management` kullanılır.
- İçerik bir hata değil, genel bir görev rehberiyse `how-to-guide` kullanılır.
- Müşterileri şu anda etkileyen canlı bir kesinti için bildirim gerekiyorsa `customer-outage-notice` kullanılır.

## Girdiler
Zorunlu:
- Belirti (hata metni veya gözlenen davranış) ve şimdiye kadar bilinen geçici çözüm veya neden.

İsteğe bağlı, kaliteyi artırır:
- Etkilenen ürünler, sürümler, platformlar, yapılandırmalar; ilişkili problem, hata ve değişiklik kayıt numaraları.
- Taahhüt edildiyse kalıcı çözüm durumu ve hedef sürüm.
- Hedef kitle (yalnızca iç destek ekibi veya müşteriye açık) ve bilgi bankası şablonu.

Ne neden ne de geçici çözüm biliniyorsa makalenin erken olduğunu söyle ve `problem-management` öner. Müşteriye açık bir makalede iç ayrıntıları (sunucu adları, iç URL'ler, güvenlik zafiyetleri) asla yayımlama.

## Süreç
1. Hedef kitleye karar ver: iç (teşhis ve yönetici adımları içerebilir) veya dış (yalnızca kullanıcının güvenle uygulayabileceği adımlar). İkisi de gerekiyorsa aynı olgulardan iki sürüm üret.
2. Başlığı iç neden olarak değil, kullanıcının gördüğü belirti olarak ve hata metninin tamamıyla yaz ("Büyük raporlarda PDF dışa aktarma Error 500 ile başarısız oluyor", "Renderer heap limiti" değil).
3. Arama anahtar sözcükleri ekle: hata kodları, mesaj parçaları, ürün alanı adları ve kullanıcıların sık kullandığı ifadeler.
4. Kapsamı kesin tanımla: etkilenen sürümler, platformlar, yapılandırmalar ve sorunu tetikleyen koşullar (eşikler, veri türleri). Yanlış eşleşmeleri önlemek için neyin etkilenMEdiğini de yaz.
5. Nedeni yalnızca doğrulanmış düzeyde anlat. Doğrulanmamış açıklamaları `[VARSAYIM]` olarak işaretle, dış kitle için güvenlik açısından hassas ayrıntıları çıkar.
6. Geçici çözümü beklenen sonuçlarıyla numaralı, test edilebilir adımlar olarak yaz; yan etkileri, veri risklerini ve kimin uygulayabileceğini (kullanıcı, yönetici, yalnızca destek) belirt.
7. Hızlı bir teşhis ekle: destek uzmanı, geçici çözümü uygulamadan önce bir kaydın bu bilinen hatayla eşleştiğini nasıl doğrular.
8. Kalıcı çözüm durumunu belirt (araştırılıyor, düzeltme planlandı, X sürümünde düzeltildi, gerekçesiyle düzeltilmeyecek); hedefi yalnızca taahhüt edildiyse yaz, aksi hâlde `[TBD]`.
9. Kayıtları ilişkilendir: problem, hata, değişiklik numaraları ve ilgili olaylar; düzeltme yayına çıktığında makalenin kaldırılması için bir sahip ve gözden geçirme tarihi belirle.
10. Devret: eşleşen kayıtlara makaleyle yanıt vermek için `ticket-response`, problem kaydını bilinen hata durumuyla güncellemek için `problem-management` öner.

## Çıktı formatı
```markdown
# Bilinen Hata: <kullanıcının gördüğü belirti>
| Alan | Değer |
|---|---|
| BH no / Problem no | <...> / <...> |
| Hedef kitle | iç / dış |
| Etkilenen | <ürün, sürümler, platformlar, koşullar> |
| Etkilenmeyen | <...> |
| Durum | araştırılıyor / düzeltme planlandı (<sürüm veya TBD>) / <sürüm>'de düzeltildi / düzeltilmeyecek |
| Sahip / Gözden geçirme | <...> / <tarih> |
| Anahtar sözcükler | <hata kodları, ifadeler> |

## Belirti
<mesajın tamamı ve davranış>
## Nasıl Doğrulanır
1. ...
## Neden
<doğrulanmış neden veya [VARSAYIM] ...>
## Geçici Çözüm
1. <adım> – beklenen sonuç: ...
- Yan etkiler / riskler: ...
- Kim uygulayabilir: ...
## Kalıcı Çözüm
<durum, hedef, müşterilerin nasıl bilgilendirileceği>
## İlişkili Kayıtlar
- ...
```

## Kalite kontrol listesi
- [ ] Başlık ve anahtar sözcükler, kullanıcıların gerçekten bildirdiği ifadeler ve hata metniyle eşleşiyor.
- [ ] Kapsam hem etkilenen hem etkilenmeyen koşulları belirtiyor.
- [ ] Her geçici çözüm adımı test edilebilir; riskleri ve gereken rol yazılı.
- [ ] Çözüm tarihleri yalnızca taahhüt edildiyse var; aksi hâlde `[TBD]`.
- [ ] Dış sürümde iç sunucu adları, kimlik bilgileri veya istismar edilebilir güvenlik ayrıntısı yok.
- [ ] Makalenin sahibi, ilişkili kayıtları ve gözden geçirme veya kaldırma tarihi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Başlığı iç nedene göre koymak; belirtiyle arayan uzmanlar makaleyi hiç bulamaz. Belirtiyle başla.
- Sessizce veri kaybettiren veya kontrolleri atlatan geçici çözümler. Yan etkileri yaz, riskli adımları yöneticilerle sınırla.
- Düzeltme yayına çıktıktan sonra makaleyi yayında bırakıp kullanıcıları eskimiş bir yola yönlendirmek. Gözden geçirme tarihi koy ve makaleyi kaldır.
- Taahhüt edilmemiş bir düzeltme sürümünü vaat etmek; bu müşteriye verilmiş bir söze dönüşür.

## Örnek
Girdi: "7.3'ten beri 10.000 satırı aşan raporlarda PDF dışa aktarma 'Error 500' veriyor; geçici çözüm CSV; düzeltme 7.4'te planlandı."

Zayıf başlık: "Renderer bellek sorunu."
Güçlü, çıktıdan bir bölüm:
- Başlık: "10.000 satırı aşan raporlarda PDF dışa aktarma 'Error 500' ile başarısız oluyor"
- Etkilenen: 7.3 sürümü, tüm tarayıcılar, yaklaşık 10.000 satırın üzerindeki raporlar [VARSAYIM: kesin eşik doğrulanacak]. Etkilenmeyen: CSV ve Excel dışa aktarma; eşiğin altındaki raporlar.
- Geçici çözüm: 1. Dışa Aktar > CSV'yi seçin. 2. Bir hesap tablosu aracında açın. Beklenen: tüm satırlar mevcut. Risk: CSV biçimlendirmeyi ve grafikleri kaybeder.
- Durum: düzeltme 7.4'te planlandı [dışarıya yayımlamadan önce sürüm sahibiyle teyit et].
