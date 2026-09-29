---
description: "Bir hizmet kesintisinin her aşaması (inceleniyor, neden bulundu, izleniyor, çözüldü) ve planlı bakım için müşteriye yönelik kesinti bildirimleri yazar: sade dille etki, etkilenen hizmetler ve bölgeler, durum, geçici çözüm ve sonraki güncelleme zamanı; spekülasyon ve suçlama içermez. Müşteriler bir kesinti veya performans düşüşünden etkilendiğinde, durum sayfası veya e-posta güncellemesi gerektiğinde ya da planlı bakım duyurulacağında kullanılır."
related: "incident-communication, incident-response, ticket-response, postmortem, known-error-article"
prompt: "İlk durum sayfası bildirimini yaz: 14:05'ten beri Türkiye'deki müşterilerin yaklaşık %30'unda kartla ödeme başarısız oluyor, neden bilinmiyor, ekip inceliyor."
---

# Müşteriye Kesinti Bildirimi

## Amaç
Etkilenen müşterilere neyin çalışmadığını, bu sırada ne yapabileceklerini ve bir sonraki bilgiyi ne zaman alacaklarını hızlı ve dürüst biçimde söylemek. Böylece güven korunur, destek kuyrukları aynı soruyla dolmaz.

## Ne zaman kullanılır
- Bir olay veya performans düşüşü müşterileri etkilediğinde ve durum sayfası, e-posta, uygulama içi veya sosyal medya güncellemesi gerektiğinde.
- Olay yeni bir aşamaya (neden bulundu, izleniyor, çözüldü) geçtiğinde ve bildirim güncellenmesi gerektiğinde.
- Kesinti beklenen planlı bir bakımın önceden duyurulması gerektiğinde.

## Ne zaman kullanılmaz
- Hedef kitle iç paydaşlar veya üst yönetimse `incident-communication` kullanılır.
- Çözümden sonra yazılı bir analiz gerekiyorsa `postmortem` kullanılır.
- Tek bir müşterinin bireysel sorunu için `ticket-response` kullanılır.

## Girdiler
Zorunlu:
- Müşterilerin yaşadığı belirti, etkilenen hizmet ve başlangıç zamanı.
- Olayın mevcut aşaması.

İsteğe bağlı, kaliteyi artırır:
- Etkilenen bölgeler, müşteri segmentleri, etkilenen oran veya sayı; geçici çözüm.
- Güncelleme aralığı, iletişim politikası, kanallar ve onaylayanlar.
- Sözleşmesel veya yasal bildirim yükümlülükleri (SLA iadeleri, düzenleyici kurum, kişisel veri söz konusuysa KVKK/GDPR).

Belirti, hizmet veya başlangıç zamanı eksikse tek bir mesajla iste. Kişisel veri açığa çıkmış olabilirse dur ve güvenlik ve kişisel veri ekibine yönlendir: ihlal bildirimleri ayrı, hukuken incelenmiş bir süreçle yapılır ve bir kesinti bildiriminde doğaçlama yazılmamalıdır.

## Süreç
1. Olguları ve ne kadar kesin olduklarını olay yöneticisiyle teyit et; doğrulanmayan hiçbir şey yayımlanmaz. Doğrulanacak `[VARSAYIM]` maddelerini iç bir listede tut.
2. Aşama etiketini seç: İnceleniyor, Neden Bulundu, İzleniyor, Çözüldü veya Planlı Bakım. Tüm kanallarda aynı etiketleri kullan.
3. Etkiyi müşterinin bakış açısından anlat: hangi işlem başarısız veya yavaş, kimin için, ne zamandan beri (saat dilimiyle). İç bileşen adlarından ve teknik jargondan kaçın.
4. Yalnızca doğrulanmış sayılarla sayısallaştır (oran bilinmiyorsa "bazı müşteriler" kabul edilebilir); asla küçümseme ("ufak bir aksaklık") veya abartma.
5. Güvenli ve doğrulanmış bir geçici çözüm varsa ver; yoksa henüz geçici çözüm olmadığını söyle.
6. Ekibin ne yaptığını, neden hakkında spekülasyon yapmadan ve bir tedarikçiyi veya kişiyi suçlamadan tek cümleyle yaz.
7. Olay yöneticisi bir tahmini süre teyit etmedikçe çözüm zamanına değil, bir sonraki güncelleme zamanına söz ver (örneğin 30 dakika içinde).
8. Çözüldü aşamasında: bitiş zamanı, toplam süre, müşterinin bir şey yapması gerekip gerekmediği (başarısız işlemleri yeniden deneme, yeniden giriş), biliniyorsa veri etkisi ve bir postmortem özetinin paylaşılıp paylaşılmayacağı.
9. Planlı bakımda: saat dilimiyle bakım penceresi ve süresi, etkilenen işlevler, beklenen müşteri etkisi, hazırlık adımları ve iletişim kanalı.
10. Aynı olgulardan kanala göre uzunluğu uyarla (durum sayfası, e-posta, uygulama içi banner, SMS) ve politika gerektiriyorsa onaya gönder.
11. Devret: iç paydaşlar için `incident-communication`, çözümden sonra `postmortem`, kalıcı bir geçici çözüm kalıyorsa `known-error-article` öner.

## Çıktı formatı
```markdown
**[<Aşama>] <Hizmet> – <müşterinin gördüğü belirti>**
Yayın: <tarih saat, saat dilimi>

**Etki:** <müşterilerin ne yapamadığı veya göremediği, kim, ne zamandan beri>
**Mevcut durum:** <ekibin ne yaptığına dair tek cümle>
**Geçici çözüm:** <adımlar veya "Henüz bir geçici çözüm bulunmuyor.">
**Sonraki güncelleme:** <saat, saat dilimi> veya durum değişirse daha önce.

<Yalnızca Çözüldü>
**Çözülme zamanı:** <saat> (süre <s:dd>)
**Sizden beklenen:** <yok / yeniden deneyin / yeniden giriş yapın / ...>
**Takip:** <neden özeti <tarih> itibarıyla paylaşılacak / [TBD]>

---
Yalnızca iç kullanım (yayımlama): doğrulanacak olgular – [VARSAYIM] ...; onaylayan: <ad/rol>
```

## Kalite kontrol listesi
- [ ] Yayımlanan her ifade olay yöneticisince teyit edildi; neden hakkında spekülasyon yok.
- [ ] Etki müşteri diliyle, başlangıç zamanı ve saat dilimiyle yazıldı.
- [ ] Bir sonraki güncelleme zamanı verildi; çözüm zamanı yalnızca teyit edildiyse var.
- [ ] Tedarikçileri veya kişileri suçlama, iç sunucu adları veya güvenlik ayrıntısı yok.
- [ ] Olası kişisel veri açığa çıkması bildirimde anlatılmadı, güvenlik/kişisel veri ekibine yönlendirildi.
- [ ] Aşama etiketi ve olgular tüm kanallarda tutarlı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Nedeni bulmadan bildirim yayımlamamak. "İnceleniyor" bildirimini erken yayımla; sessizlik kayıt sayısını artırır.
- Müşterileri sakinleştirmek için tahmini süre verip sonra kaçırmak. Çözüm zamanı değil, güncelleme zamanı söz ver.
- Tam bir kesinti için "bazı kullanıcılar sorun yaşayabilir" demek. Durumu küçümsemek güveni kesintinin kendisinden daha çok zedeler.
- "Çözüldü" bildirimini yayımlamayı veya müşterilere başarısız işlemleri yeniden denemelerini söylemeyi unutmak.

## Örnek
Girdi: "14:05'ten beri Türkiye'deki müşterilerin yaklaşık %30'unda kartla ödeme başarısız, neden bilinmiyor, ekip inceliyor."

Zayıf: "Ödeme sağlayıcımız kaynaklı ufak teknik sorunlar yaşıyoruz. Yakında düzelecek."

Güçlü:
**[İnceleniyor] Ödemeler – bazı kartlı ödemeler başarısız oluyor**
Yayın: 14:25 TSİ
**Etki:** 14:05 TSİ'den beri Türkiye'deki bazı müşterilerimiz kartla öderken hata alıyor. Diğer ödeme yöntemleri etkilenmiyor [VARSAYIM: olay yöneticisiyle teyit et].
**Mevcut durum:** Ekibimiz nedeni inceliyor.
**Geçici çözüm:** Hesabınızda tanımlıysa bu sürede havale/EFT kullanabilirsiniz.
**Sonraki güncelleme:** 14:55 TSİ veya daha önce.
