---
description: Bir çalışma için doğru kullanıcıları seçen katılımcı eleme anketi yazar; davranışa dayalı dahil etme ve hariç tutma kriterleri, doğru cevabı belli etmeyen yönlendirmesiz sorular, segment kotaları, eleme mantığı ve onay içerir. Görüşme, kullanılabilirlik testi veya günlük çalışması için katılımcı bulmadan önce ya da "kiminle konuşmalıyız" veya "katılımcı seçme anketi yaz" dendiğinde kullanılır.
related: research-plan, usability-test-script, questionnaire-design, persona, interview-question-set
prompt: En az ayda bir fatura kesen ve son bir yılda rakip bir uygulamayı denemiş 8 küçük işletme sahibini bulmak için eleme anketi yaz.
---

# Katılımcı Eleme Anketi

## Amaç
Davranışı araştırma sorularına uyan katılımcıları seçmek; profesyonel test katılımcılarını, şirket içinden kişileri ve "doğru" cevabı tahmin edenleri elemek. Böylece oturum süresi gerçekten önemli olan kullanıcılarla geçer.

## Ne zaman kullanılır
- Araştırma planı hedef segmentleri tanımladığında ve katılımcı bulma başlamak üzereyken.
- Bir katılımcı bulma ajansı veya paneli eleme kriterleri ve sorular istediğinde.
- Önceki oturumlara uygun olmayan katılımcılar geldiyse ve elemenin sıkılaştırılması gerektiğinde.

## Ne zaman kullanılmaz
- Amaç katılımcı bulmak değil, tutum veya davranışları geniş ölçekte ölçmekse `questionnaire-design` kullanılır.
- Segmentler ve çalışma hedefleri tanımlı değilse `research-plan` kullanılır.

## Girdiler
Zorunlu:
- Çalışmanın hedefi ve hedef katılımcı profili (kim, hangi davranış, hangi bağlam).

İsteğe bağlı, kaliteyi artırır:
- Araştırma planı, örneklem büyüklüğü ve segment kotaları, katılımcı bulma kanalı (müşteri listesi, panel, ajans, ürün içi davet), teşvik, oturum formatı ve tarihleri, pazarlar ve diller.

Hedef profil yoksa bunu kısa, numaralı tek bir soru grubuyla iste (kim, temel davranış, mutlaka hariç tutulacak gruplar). Diğer eksikler açık soru olur.

## Süreç
1. Hedef profili demografi veya öz tanımlar yerine davranışsal kriterlere çevir (sıklık, yakınlık, kullanılan araçlar, karardaki rolü); demografiyi yalnızca çeşitlilik kotaları için ekle.
2. Hariç tutmaları tanımla: şirketin ve rakiplerin çalışanları ve yakınları, pazar araştırması veya UX profesyonelleri, yakın zamanda çalışmaya katılanlar (ör. son 6 ay), yasal veya pazar kapsamı dışındakiler.
3. Segment kotalarını ve gereken karışımı belirle (ör. yeni ve deneyimli, cihaz, erişilebilirlik ihtiyacı). Verilmediyse gelmeme payı için %20-25 fazla katılımcı dahil toplam sayıyı `[VARSAYIM]` olarak yaz.
4. Soruları genelden özele sırala: önce hariç tutma soruları, sonra niteleyici davranışlar, sonra kotalar, en son lojistik; en ucuz eleyicileri başa koy.
5. Hedefi belli etmeyen sorular yaz: çeldirici seçenekli çoktan seçmeli sorular, eşiği ima etmeyen sıklık aralıkları, her listede "hiçbiri" seçeneği.
6. Her cevabı tetiklediği kuralla işaretle (Uygun, Sonlandır, Kota: segment X, İncelemeye al) ve puanlama mantığını tanımla.
7. Katılımcının düşüncelerini ifade edip edemediğini görmek için açık kriterlerle değerlendirilecek bir açık uçlu soru ekle.
8. Lojistik ve onayı ekle: uygunluk, uzaktan oturum için cihaz ve bağlantı, kayıt onayı, veri kullanımı ve saklama süresi. Yalnızca planlama için gereken kişisel veriyi topla ve eleme verisini oturum notlarından ayrı tut.
9. Süreyi tahmin et (5 dakikanın altı, 8-12 soru hedefle) ve yönlendirici ifadeleri ve bozuk mantığı yakalamak için 2-3 kişiyle pilot uygula.
10. Varsayımları ve açık soruları listele; oturumlar için `usability-test-script` veya `interview-question-set` öner.

## Çıktı formatı
```markdown
# Eleme Anketi: <çalışma>
Hedef: <n katılımcı> · Segmentler/kotalar: <...> · Kanal: <...> · Teşvik: <[TBD]>

## Kriterler
- Dahil: ...
- Hariç: ...
- Kotalar: | Segment | Hedef | Min | Maks |

## Sorular
**S1. <soru>** (tek seçim)
- a) ... → Sonlandır
- b) ... → Devam
- c) Hiçbiri → Sonlandır

**S2. <soru>** (çoklu seçim)
- ... → <kural> ise Uygun

**S9. <ifade becerisi sorusu>** (açık uçlu) → İnceleme: <kriterler>

## Lojistik ve Onay
<uygunluk, cihaz, kayıt onayı, veri saklama>

## Puanlama Mantığı
<hangi kombinasyonlar uygun; kota ataması>

## Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Kriterler davranışsal ve her biri araştırma sorularına bağlı.
- [ ] Hiçbir soru uygun cevabı belli etmiyor; her listede tarafsız bir çıkış seçeneği var.
- [ ] Her cevap seçeneğinin açık bir kuralı var (Uygun, Sonlandır, Kota, İnceleme).
- [ ] Standart hariç tutmalar (şirket içi, UX/pazar araştırması profesyonelleri, yakın zamanda katılanlar) mevcut.
- [ ] Toplanan kişisel veri, planlama ve onayın gerektirdiğiyle sınırlı.
- [ ] Süre yaklaşık 5 dakikanın altında ve pilot adımı planlandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Evet/hayır niteleyiciler ("Fatura yazılımı kullanıyor musunuz?"). Katılımcılar evet der; seçenekler ve sıklık aralıkları kullan.
- Öz tanıma göre elemek ("İleri düzey kullanıcı mısınız?"). Bunun yerine somut ve yakın tarihli davranışı sor.
- Kotaları unutup tüm katılımcıların en kolay bulunan segmentten gelmesi. Katılımcı bulma sırasında kotaları takip et.

## Örnek
Girdi: "En az ayda bir fatura kesen ve son bir yılda rakip bir uygulamayı denemiş 8 küçük işletme sahibi."

Zayıf: "Her ay fatura kesiyor musunuz? Evet / Hayır"
Güçlü: "Son 3 ayda işletmeniz yaklaşık kaç fatura kesti? a) Hiç → Sonlandır b) 1-2 → Sonlandır c) 3-10 → Devam d) 10'dan fazla → Devam"
- S4: "Son 12 ayda fatura için aşağıdaki araçlardan hangilerini kullandınız?" (bizim ürün, 3 rakip, tablo programı, diğer, hiçbiri) → Herhangi bir rakip seçildiyse Uygun.
