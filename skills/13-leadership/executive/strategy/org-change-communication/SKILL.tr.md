---
description: Bir organizasyon değişikliğinin (yeniden yapılanma, yeni ekipler, raporlama hattı değişiklikleri, rol değişiklikleri, ofis veya süreç değişiklikleri) iletişimini planlar ve yazar: neden, ne değişiyor, ne değişmiyor, kim etkileniyor, zaman çizelgesi, destek ve nereye sorulacağı; etkilenenlerin önce ve özel olarak duyacağı şekilde sıralanır. Bir yönetici yeniden yapılanma veya ekip değişikliği duyururken, söylentilere yanıt vermek gerektiğinde ya da farklı kitleler için bir mesaj seti gerektiğinde kullanılır.
related: team-topology, announcement, bad-news-delivery, faq-builder, communication-plan
prompt: Gelecek ay mobil ve web ekiplerini ürün odaklı ekiplerde birleştiriyoruz; duyuruyu ve kimin neyi ne zaman duyacağını gösteren planı yaz.
---

# Organizasyon Değişikliği İletişimi

## Amaç
İnsanların bir organizasyon değişikliğini, kendilerini nasıl etkilediğini ve nereden destek alabileceklerini anlamasını sağlamak. Böylece güven korunur, söylentilerin önüne geçilir ve değişiklik direnç yerine işlemeye başlar.

## Ne zaman kullanılır
- Bir yeniden yapılanma, ekip birleşmesi veya bölünmesi, yeni raporlama hatları ya da rol değişiklikleri duyurulmak üzereyken.
- Değişiklik sızdı veya söylentiler yayıldı ve hızla net bir mesaj gerekiyorsa.
- Farklı kitleler (doğrudan etkilenenler, yöneticileri, geniş departman, iş ortakları) için uyarlanmış mesajlar gerektiğinde.

## Ne zaman kullanılmaz
- Yeni ekip yapısının kendisini tasarlamak için `team-topology` veya `role-definition` kullanılır.
- Bir kişiye olumsuz bir kararı (rolün kaldırılması, performans sonucu) iletmek için `bad-news-delivery` kullanılır.
- Ürün veya sürüm duyurusu için `announcement` kullanılır.

## Girdiler
Zorunlu:
- Neyin değiştiği, neden değiştiği ve yürürlük tarihi (ya da henüz kararlaştırılmadığı).

İsteğe bağlı, kaliteyi artırır:
- Kimin nasıl etkilendiği (özel görüşmeler için gerekmedikçe isim değil grup bazında).
- Neyin değişmediği (ücret, lokasyon, projeler, araçlar), hâlâ açık kararlar ve sunulan destek.
- Hukuk, İK veya çalışan temsilciliği kısıtları ve gereken danışma adımları.

Değişikliğin gerekçesi yoksa sor; nedeni belirtilmeyen değişiklik keyfi görünür. Gerekçe, tarih veya garanti (ör. "kimse işini kaybetmeyecek") uydurma; yalnızca kullanıcının teyit ettiğini yaz, gerisini `[TBD]` olarak işaretle.

## Süreç
1. Değişikliği netleştir: önceki ve sonraki yapı, gerekçe (çözdüğü problem), yürürlük tarihi, karar durumu (kesin veya danışma aşamasında) ve açık kalanlar.
2. Kitleleri etkiye göre eşle: doğrudan etkilenenler (rolü, yöneticisi veya ekibi değişenler), dolaylı etkilenenler (arayüzler, paydaşlar) ve yalnızca bilgilendirilecekler. Bireysel ayrıntıları gizli tut ve kişisel veriyi en aza indir.
3. İletişimi sırala: önce doğrudan etkilenenler yöneticileriyle özel görüşmede, sonra konuşma notlarıyla bilgilendirilen yöneticiler, ardından geniş duyuru, en son iş ortakları. Sızıntıyı önlemek için adımlar arası süreyi kısa tut (haftalar değil saatler).
4. Adalet ve tutarlılığı kontrol et: Tüm etkilenenlere aynı kriterler uygulandı mı? Bir grubu orantısız etkileyen değişiklikleri (ör. lokasyon, yarı zamanlı çalışma, izin durumu) İK incelemesi için işaretle ve kişileri hedef gösteren ifadelerden kaçın.
5. Ana mesajı taslakla: neden, ne değişiyor, ne değişmiyor, kim etkileniyor, ne zaman, sonra ne olacak, nereye sorulacak. Organizasyon şemasıyla değil, gerekçe ve insanlar üzerindeki etkiyle başla.
6. Belirsizlik konusunda açık ol: Henüz neyin kararlaştırılmadığını ve ne zaman kararlaştırılacağını söyle; teyit edilmemiş hiçbir şeyi vaat etme.
7. Yönetici bilgilendirme notu yaz: ana mesajlar, olası sorular ve cevapları, spekülasyon yapılmaması gereken konular, eskalasyon yolu.
8. Olası sorulardan bir SSS oluştur: rolüm, yöneticim, projelerim, ücret ve unvan, lokasyon, kariyer yolları, zaman çizelgesi, kaygılar nasıl iletilir.
9. Geri bildirim ve destek kanallarını (ofis saatleri, bir üst yöneticiyle görüşmeler, anonim sorular) ve bir takip tarihini tanımla.
10. Tonu gözden geçir: saygılı, doğrudan, kurumsal örtmece yok, kişileri veya önceki yöneticileri suçlama yok.
11. Kullanıcının hedefi devam ediyorsa SSS'yi genişletmek için `faq-builder`, daha uzun bir değişim programı için `communication-plan` veya zor bireysel görüşmeler için `bad-news-delivery` öner.

## Çıktı formatı
```markdown
# Organizasyon Değişikliği İletişimi: <değişiklik>

## Sıralama
| Adım | Kitle | Kanal | Sorumlu (rol) | Zaman |
|---|---|---|---|---|

## Ana Duyuru
Konu: <net konu>
- Neden: ...
- Ne değişiyor: ...
- Ne değişmiyor: ...
- Kim etkileniyor: ...
- Zaman çizelgesi: ...
- Henüz kararlaştırılmayanlar: ... (beklenen karar <tarih veya [TBD]>)
- Destek ve sorular: ...

## Yönetici Bilgilendirme Notu
- Ana mesajlar: ...
- Olası sorular ve cevaplar: ...
- Spekülasyon yapılmayacak konular: ...

## SSS
1. <soru> – <cevap veya [TBD]>

## Adalet ve Risk Notları (iç kullanım)
- ...
```

## Kalite kontrol listesi
- [ ] Doğrudan etkilenenler geniş duyurudan önce ve özel olarak bilgilendiriliyor.
- [ ] Mesaj nedeni, neyin değiştiğini, neyin değişmediğini, zaman çizelgesini ve nereye sorulacağını belirtiyor.
- [ ] Kullanıcının teyit etmediği hiçbir şey vaat edilmiyor veya olgu olarak yazılmıyor; açık maddeler `[TBD]`.
- [ ] Kriterler tutarlı uygulanmış; herhangi bir grup üzerindeki orantısız etki İK incelemesi için işaretli.
- [ ] Geniş iletişimde isim veya kişisel ayrıntı yok.
- [ ] Ton doğrudan ve saygılı; örtmece veya suçlama yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Herkese aynı anda duyurmak. Rolü etkilenen biri bunu asla genel toplantı slaytından öğrenmemeli.
- Yalnızca yeni organizasyon şemasını anlatmak. İnsanlar önce kendilerine ne olacağını bilmek ister; yapıdan önce bunu cevapla.
- Aşırı güvence vermek. Sonradan yanlış çıkan bir "sizin için hiçbir şey değişmiyor", dürüst bir "henüz karar verilmedi"den çok daha fazla güven kaybettirir.

## Örnek
Girdi: Mobil ve web ekipleri gelecek ay ürün odaklı ekiplerde birleşiyor.

Çıktıdan bir bölüm:
- Neden: Web ve mobili kapsayan özellikler bugün iki ekip ve iki backlog gerektiriyor, bu da teslimatı yavaşlatıyor `[kanıtla teyit et, ör. teslim süresi]`.
- Zayıf cümle (kaçın): "Sinerjiyi açığa çıkaracak yeni yapımızı duyurmaktan heyecan duyuyoruz." Güçlü cümle: "<tarih> itibarıyla her ürün alanında web ve mobilden sorumlu tek bir ekip olacak. Yöneticiniz bu hafta ekibiniz hakkında sizinle görüşecek; ücret ve unvanlar değişmiyor."
- Henüz kararlaştırılmayan: iki ekibin teknik lider atamaları – karar tarihi `[TBD]`.
