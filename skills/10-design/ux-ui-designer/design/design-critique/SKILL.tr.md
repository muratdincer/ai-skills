---
name: design-critique
description: "Tasarımın hedeflerine, kullanıcılarına ve kısıtlarına dayanan, konum ve etki açısından somut, gözlemi görüşten ayıran ve geri bildirimi önerilen yönlerle birlikte mutlaka düzeltilmeli, değerlendirilmeli ve ufak dokunuşlar olarak önceliklendiren yapılandırılmış tasarım eleştirisi verir. Bir tasarımcı devam eden işini paylaşıp geri bildirim istediğinde, tasarım incelemesine veya eleştiri oturumuna hazırlanırken ya da \"bu tasarım hakkında ne düşünüyorsun\" sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 10-design
  role: ux-ui-designer
  area: design
  title: "Tasarım eleştirisi"
  related: "heuristic-evaluation, accessibility-audit, wireframe-spec, feedback-sbi, review-comment-writing"
  prompt: "Bu gösterge paneli yeniden tasarımını eleştir; hedef, operasyon yöneticilerinin sorunlu mağazaları 10 saniye içinde görebilmesi."
---

# Tasarım Eleştirisi

## Amaç
Devam eden bir işi zevke göre değil hedeflerine göre değerlendirerek tasarımcının onu geliştirmesine yardım etmek. Somut, önceliklendirilmiş ve uygulanabilir geri bildirim, işe yarayanı korur ve tartışmayı en önemli konulara odaklar.

## Ne zaman kullanılır
- Bir tasarımcı maket, prototip veya akış paylaşıp geri bildirim istediğinde.
- Ekip eleştiri oturumu veya tasarım incelemesi planlandıysa ve geri bildirim hazırlanması gerekiyorsa.
- Paydaş geri bildirimi belirsizse ("daha dikkat çekici olsun") ve hedef bazlı eleştiriye dönüştürülmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Önem dereceli sistematik bir kullanılabilirlik incelemesi gerekiyorsa `heuristic-evaluation` kullanılır.
- Kontrol WCAG uygunluğuysa `accessibility-audit` kullanılır.
- Geri bildirim bir tasarım hakkında değil, bir kişinin davranışı veya performansı hakkındaysa `feedback-sbi` kullanılır.

## Girdiler
Zorunlu:
- Tasarım (görsel, prototip tarifi veya ayrıntılı açıklama) ve hedefi: kimin için ve neyi başarması gerektiği.

İsteğe bağlı, kaliteyi artırır:
- Aşama (keşif, iyileştirme, son hâl), kısıtlar (tasarım sistemi, teknik, marka, süre), tasarımcının istediği geri bildirim türü, önceki geri bildirimler.

Hedef veya hedef kullanıcı yoksa önce onu iste; hedefsiz eleştiri zevke dönüşür. Aşama belirsizse sor, çünkü hangi geri bildirimin yararlı olduğunu değiştirir.

## Süreç
1. Tasarımcının çerçeveyi teyit edebilmesi için hedefi, kullanıcıyı, temel görevi ve aşamayı birer satırda yeniden yaz.
2. Hangi geri bildirimin istendiğini (konsept, akış, yerleşim, görsel, metin) sor veya çıkar; diğer geri bildirimleri kısa tut ya da sonraya bırak.
3. Tasarıma temel görevi yapan kullanıcı gözüyle bak: ilk ne görülüyor, ne anlaşılıyor, hangi aksiyon belirgin, ne eksik.
4. Önce güçlü yönleri somut olarak yaz (ne işe yarıyor ve neden) ki yinelemelerde kaybolmasın.
5. Gözlemleri yargıdan önce "Y konumunda X'i fark ediyorum" biçiminde yaz; ardından hedefe etkisini belirt ("bu da kullanıcının … olabileceği anlamına geliyor"); kişisel tercihi öyle etiketle.
6. Hiyerarşi ve odağı, akış ve görev uyumunu, tasarım sistemi ve platformla tutarlılığı, içerik ve metni, durumlar ve uç durumları, temel erişilebilirliği (kontrast, dokunma alanı, metin alternatifleri) kontrol et.
7. Sorunları, çözümü tasarımcıya bırakan sorular veya yönler olarak çerçevele ("Sorunlu mağazalar en üste sıralansa nasıl olur?"); ayrıntılı yeniden tasarım dayatma.
8. Önceliklendir: Mutlaka düzeltilmeli (hedefi engelliyor), Değerlendirilmeli (hedefi zayıflatıyor), Ufak dokunuş (cila); mutlaka düzeltilmesi gerekenleri en önemli birkaç maddeyle sınırla.
9. Kanıta dayalı noktaları görüşlerden ve kullanıcılarla ilgili varsayımlardan ayır; tartışmalı noktaların nasıl doğrulanacağını öner (hızlı test, veri kontrolü).
10. En önemli 3 aksiyonla kapat; sistematik bir tarama için `heuristic-evaluation` veya `accessibility-audit`, kullanıcı kanıtı gerekiyorsa `usability-test-script` öner.

## Çıktı formatı
```markdown
# Tasarım Eleştirisi: <tasarım adı>
Hedef: <...> · Kullanıcı / temel görev: <...> · Aşama: <...> · Geri bildirim odağı: <...>

## İşe Yarayanlar
- <somut güçlü yön> — hedefe nasıl yardım ediyor

## Mutlaka Düzeltilmeli
1. <konum>: ... fark ediyorum → hedefe etkisi ... → yön/soru ...

## Değerlendirilmeli
- ...

## Ufak Dokunuşlar
- ...

## Görüşler ve Varsayımlar (doğrulanacak)
- [GÖRÜŞ] ... / [VARSAYIM] ...

## Sonraki En Önemli 3 Aksiyon
1. ...
```

## Kalite kontrol listesi
- [ ] Her nokta zevke değil, belirtilen hedefe, kullanıcıya veya kısıta bağlı.
- [ ] Her nokta bir konum ve bir etki belirtiyor.
- [ ] Güçlü yönler somut ve eleştiride yer alıyor.
- [ ] Geri bildirim önceliklendirildi ve mutlaka düzeltilmesi gerekenler az sayıda.
- [ ] Görüşler ve varsayımlar etiketlendi ve kanıttan ayrıldı.
- [ ] Geri bildirim aşamaya uygun (erken bir konsepte piksel düzeyinde yorum yok).
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Maviyi sevmedim." Hedefe bağlanmayan zevk, tasarımcıya yapacak bir şey bırakmaz.
- Geri bildirimde ekranı yeniden tasarlamak. Yön ve soru sun; çözümü tasarımcı bulsun.
- Tek engelleyici sorunu yirmi ufak yorumun arasına gömmek. Hedefi engelleyenle başla.

## Örnek
Girdi: "Gösterge paneli yeniden tasarımı; operasyon yöneticileri sorunlu mağazaları 10 saniye içinde görmeli."

Zayıf: "Çok kalabalık, renkler de olmamış. Daha sade bir görünüm dene."
Güçlü: "Mutlaka düzeltilmeli — Mağaza ızgarası: Sorunlu mağazaların yalnızca küçük kırmızı bir noktayla işaretlendiğini ve ızgaranın alfabetik sıralandığını fark ediyorum. 120 mağazada yönetici her kutuyu taramak zorunda kalıyor; bu 10 saniye hedefiyle çelişiyor. Sorunlu mağazalar üst bilgide sayılarıyla birlikte en üste sabitlense nasıl olur? Ayrıca yalnızca kırmızıyla durum göstermek renk körü kullanıcılar için yetersiz; bir ikon veya etiketle destekle."
