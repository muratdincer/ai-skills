---
name: escalation-message
description: "Sorunu, doğrulanmış olguları, iş etkisini ve son tarihi, şimdiye kadar denenenleri, ödünleşimleriyle seçenekleri, bir öneriyi ve eskalasyon sahibinden tek ve net bir talebi içeren bir eskalasyon mesajı yazar. Bir engel, bağımlılık, anlaşmazlık veya risk mevcut seviyede çözülemediğinde ve bir yöneticiden, sponsordan, tedarikçi hesap sorumlusundan ya da başka bir ekibin yönetiminden karar, kaynak veya müdahale gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: communication
  area: written
  title: "Eskalasyon mesajı yazma"
  related: "stakeholder-email, status-update, raid-log, trade-off-analysis, conflict-resolution"
  prompt: "Direktörüme, kimlik ekibinin SSO entegrasyonunu üç haftadır teslim etmediğini ve ayın 8'ine kadar gelmezse 15'indeki pilotun kayacağını eskale et."
---

# Eskalasyon Mesajı Yazma

## Amaç
Takılmış bir konuyu onu çözebilecek seviyeye, kararın tek bir yanıtla veya kısa bir toplantıda verilebileceği kadar olgu ve seçenekle taşımak; bunu kişileri suçlamadan ve çalışma ilişkilerini zedelemeden yapmak.

## Ne zaman kullanılır
- Bir engel veya bağımlılık olağan kanallarla çözülemediyse ve bir son tarih risk altındaysa.
- İki taraf anlaşamıyorsa ve ikisinin de karar yetkisi yoksa.
- Bir risk mevcut sorumlunun tolerans veya bütçe yetkisini aşıyorsa.

## Ne zaman kullanılmaz
- Konu henüz doğrudan sorumlu kişiye iletilmediyse önce `stakeholder-email` kullanılır.
- Sarı bir madde içeren olağan ilerleme raporuysa `status-update` kullanılır.
- Devam eden bir canlı ortam olayıysa `incident-communication` kullanılır.

## Girdiler
Zorunlu:
- Sorun ve etkisi (neyin, ne zaman kayacağı, maliyet yaratacağı veya bozulacağı).
- Şimdiye kadar kime sorulduğu ve ne olduğu.

İsteğe bağlı:
- Kanıtlar (kayıt numaraları, taleplerin tarihleri), değerlendirilen seçenekler, eskalasyon sahibinin rolü, kurumsal eskalasyon yolu.

Etki veya son tarih eksikse sor: bunlar olmadan eskalasyon önceliklendirilemez. Kullanıcının vermediği maliyet veya gecikme rakamlarını tahmin etme; `[TBD]` olarak işaretle.

## Süreç
1. Eskalasyonun gerekli olduğunu doğrula: olağan kanal denendi, son tarih veya tolerans risk altında, mevcut seviyenin yetkisi yok. Değilse önce doğrudan bir mesaj öner.
2. Eskalasyon sahibini belirle: karar verebilecek en alt seviye. Karşı tarafın yöneticisini yalnızca anlaşılmışsa veya zaten bilgisi varsa ekle; eskale etmeden önce karşı tarafa haber ver ("sürpriz yok").
3. Konuyu `Eskalasyon: <sorun> – <tarih>'e kadar karar gerekli` biçiminde yaz.
4. Talebi ilk cümlede belirt: gereken karar, kaynak veya müdahale ve ne zamana kadar.
5. Doğrulanmış olguları tarih ve referanslarıyla listele; yorumlardan açıkça ayır ve yorumları öyle işaretle.
6. Etkiyi okuyucunun diliyle ölç: tarihler, müşteriler, para, uyum, diğer ekipler. Yalnızca verilen rakamları kullan.
7. Şimdiye kadar deneneni ve sonucunu, kişiler hakkında değil sistemler ve taahhütler hakkında tarafsız bir dille özetle.
8. "Hiçbir şey yapmamak" dahil 2-3 seçeneği ödünleşimleriyle ve gerekçeli önerinle ver.
9. Son tarihe kadar karar çıkmazsa ne olacağını ve bir sonraki kontrol tarihini yaz.
10. Duygusal ifadeleri, suçlamayı ve ironiyi çıkar; metni karşı tarafın da göreceğini varsayarak yeniden oku, çünkü büyük olasılıkla görecek.
11. Kullanıcının hedefi devam ediyorsa seçeneklerin daha derin karşılaştırılması için `trade-off-analysis`, konuyu kapanana kadar izlemek için `raid-log` öner.

## Çıktı formatı
```markdown
Konu: Eskalasyon: <sorun> – <tarih>'e kadar karar gerekli

<İsim>, <sonucu korumak> için <tarih>'e kadar <karar/kaynak/müdahale> gerekiyor.

**Olgular**
- <tarih>: <referanslı olgu>

**Çözülmezse etkisi**
- <ne, ne zaman, kimin için kayar/maliyet yaratır/bozulur>

**Denenenler**
- <aksiyon> → <sonuç>

**Seçenekler**
| Seçenek | Artılar | Eksiler / maliyet |
|---|---|---|
| A (önerilen) | ... | ... |
| B | ... | ... |
| Hiçbir şey yapmamak | ... | ... |

**Talep:** <tarih>'e kadar <net karar>. O tarihe kadar karar çıkmazsa <sonuç>.
<Karşı taraf bilgilendirildi: evet/hayır>   Sonraki kontrol: <tarih>
```

## Kalite kontrol listesi
- [ ] Talep ve son tarih ilk cümlede.
- [ ] Olgular tarihli ve referanslı; yorumlar işaretli.
- [ ] Etki eskalasyon sahibinin diliyle ifade edildi; uydurulmuş rakam yok.
- [ ] Seçenekler ödünleşimleri ve "hiçbir şey yapmamak" seçeneğini içeriyor; öneri verildi.
- [ ] Dil tarafsız; kişisel kusura değil taahhütlere odaklanıyor.
- [ ] Karşı taraf, eskalasyon ulaşmadan önce bilgilendirildi veya bilgilendirilecek.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Olgular yerine bir duyguyu eskale etmek ("hiç dönüş yapmıyorlar"). Bunu tarihli taleplerle ve kaçırılan taahhütlerle değiştir.
- Seçeneksiz eskalasyon; analizi yukarıya iter. Her zaman bir öneriyle git.
- Geç eskale etmek. Tolerans aşıldığında aynı gün eskale et; geç kalan eskalasyon seçenek bırakmaz.

## Örnek
Girdi: kimlik ekibi SSO'yu üç haftadır teslim etmedi; 8'ine kadar gelmezse 15'indeki pilot kayıyor.

Zayıf: "Merhaba, kimlik ekibinden gerçekten çok bıktık. Sürekli söz veriyorlar ama hiçbir şey olmuyor. Bir şey yapabilir misiniz?"

Güçlü (bölüm):
Konu: Eskalasyon: Pilot için SSO entegrasyonu – 5'ine kadar karar gerekli
"Selin Hanım, SSO entegrasyonu için 5'ine kadar bir önceliklendirme kararına ihtiyacım var; 8'inde hazır olmazsa 15'indeki müşteri pilotu kayıyor.
Olgular: `[tarih]` tarihinde talep edildi (kayıt `[ID]`); taahhüt edilen `[tarih]` ve `[tarih]` kaçırıldı."
Seçenekler: A) Kimlik ekibi bir hafta SSO'ya öncelik verir (önerilen); B) Pilot yerel hesaplarla yapılır `[güvenlik onayı gerekli]`; C) Pilot ertelenir.
