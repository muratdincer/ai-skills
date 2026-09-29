---
name: microcopy
description: "Buton ve bağlantı etiketleri, form etiketleri, yardımcı metinler, yer tutucular, araç ipuçları, boş durumlar, onaylar ve başarı mesajları gibi arayüz mikro metinlerini kullanıcının görevine, ürünün sesine, uzunluk sınırlarına ve yerelleştirmeye uygun şekilde yazar. Bir ekranın veya akışın arayüz metinlerinin yazılması ya da iyileştirilmesi gerektiğinde, etiketler belirsiz veya tutarsız olduğunda ya da \"bu buton ne demeli\" sorusu sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 10-design
  role: ux-writer
  area: content
  title: "Mikro metin yazma"
  related: "error-message-writing, voice-and-tone-guide, design-handoff, style-guide-check, glossary-builder"
  prompt: "Yeni \"ekip arkadaşı davet et\" penceremizin mikro metinlerini yaz: başlık, alan etiketleri, yardımcı metin, butonlar ve boş durum."
---

# Mikro Metin Yazma

## Amaç
Arayüzdeki her öğeye, ne olduğunu ve ne olacağını anlatan, netliğin izin verdiği en az kelimeyle yazılmış, ürünün sesi ve terminolojisiyle tutarlı bir metin vermek.

## Ne zaman kullanılır
- Yeni bir ekran, pencere veya akışın arayüz metinlerine ihtiyaç olduğunda.
- Mevcut etiketler belirsiz ("Gönder", "Tamam"), tutarsız olduğunda veya destek sorularına yol açtığında.
- Boş durumlar, başlangıç ipuçları veya onaylar bir sonraki eyleme yönlendirmeliyse.

## Ne zaman kullanılmaz
- Metin bir hata veya doğrulama mesajıysa `error-message-writing` kullanılır.
- Ürünün genel ses ilkeleri gerekiyorsa `voice-and-tone-guide` kullanılır.
- Uzun dokümantasyon bir stil rehberine göre kontrol ediliyorsa `style-guide-check` kullanılır.

## Girdiler
Zorunlu:
- Ekran veya akış bağlamı: kullanıcının ne yapmaya çalıştığı ve metin gereken öğeler (liste, wireframe veya ekran görüntüsü tarifi).

İsteğe bağlı, kaliteyi artırır:
- Ses ve ton rehberi, terim sözlüğü, büyük harf kuralları.
- Karakter sınırları, platformlar, hedef diller.
- Mevcut metinler ve bilinen kullanıcı kafa karışıklıkları (destek kayıtları, test bulguları).

Bağlam veya öğe listesi yoksa iste. Diğer her şey açık soru olur.

## Süreç
1. Kullanıcının bu ekrandaki hedefini ve tek birincil eylemi belirle. Birincil eylemin etiketi mekanizmayı ("Gönder") değil sonucu ("Davetleri gönder") adlandırır.
2. Metin gereken her öğeyi listele: başlık, etiketler, yardımcı metin, yer tutucular, butonlar, bağlantılar, araç ipuçları, boş durumlar, onaylar, başarı mesajları.
3. Terim sözlüğündeki ürün terimlerini kullan; sözlük yoksa her kavram için tek terim seç ve her yerde onu kullan ("çalışma alanı" ile "proje" arasında gidip gelme). Yeni terimleri `[YENİ TERİM]` olarak işaretle.
4. Etiketleri kısa isim öbekleri, butonları nesne + fiil olarak yaz. Buton çiftlerini gövde metni okunmadan seçim netleşecek şekilde kur ("Evet" / "Hayır" değil, "Dosyayı sil" / "Dosyayı sakla").
5. Zorunlu yönlendirmeyi yer tutucuya koyma; yer tutucular yazmaya başlayınca kaybolur ve erişilebilirlikte başarısız olur. Format kurallarını yardımcı metne koy.
6. Boş durumlarda bu alanın ne için olduğunu, neden boş olduğunu ve sonraki eylemi yaz; ilk kullanım, sonuç yok ve temizlenmiş durumları birbirinden ayır.
7. Geri alınamaz eylemlerin onaylarında nesneyi, sonucu ve geri alınıp alınamayacağını belirt.
8. Anahtar kelimeyi başa al, stil rehberi aksini söylemiyorsa yalnızca cümle başını büyük yaz, jargon, çift olumsuzluk ve suçlama kullanma, uzunluk sınırlarını kontrol et. Yerelleştirme için yaklaşık %30-40 uzamaya yer bırak ve metinleri parça parça birleştirme (Türkçede ek uyumu bunu özellikle bozar).
9. Erişilebilirliği kontrol et: bağlantı ve buton metni bağlamdan bağımsız anlamlı; yalnızca ikondan oluşan butonların erişilebilir adı var; hiçbir şey renge veya konuma dayanmıyor ("yeşil butona tıklayın").
10. Her öğe için bir önerilen seçenek ver; yalnızca gerçek bir ödünleşim varsa alternatif ekle ve açık olmayan tercihler için tek satır gerekçe yaz. Kullanıcı niyetine dair her varsayımı `[VARSAYIM]` olarak etiketle.
11. Hedef devam ediyorsa hata yolları için `error-message-writing`, ses tanımlı değilse `voice-and-tone-guide` veya metinleri spesifikasyona bağlamak için `design-handoff` öner.

## Çıktı formatı
```markdown
# Mikro Metin: <ekran / akış>
Kullanıcı hedefi: <tek satır>  ·  Birincil eylem: <etiket>

| Anahtar | Öğe | Metin | Karakter | Gerekçe / not |
|---|---|---|---|---|
| invite.title | Pencere başlığı | ... | .. | ... |
| invite.email.label | Alan etiketi | ... | .. | ... |
| invite.email.help | Yardımcı metin | ... | .. | ... |
| invite.cta.primary | Birincil buton | ... | .. | ... |

## Boş / Onay / Başarı Durumları
| Durum | Başlık | Gövde | Eylem |

## Kullanılan Terimler
- <terim>: <anlam> [sözlükte yoksa YENİ TERİM]

## Varsayımlar ve Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Birincil buton sonucu adlandırıyor ve buton çiftleri bağlam olmadan ayırt edilebiliyor.
- [ ] Her kavram için tek terim var, sözlükle tutarlı; yeni terimler işaretli.
- [ ] Hiçbir temel yönlendirme yalnızca yer tutucuda durmuyor.
- [ ] Her boş durum bir neden ve bir sonraki eylem veriyor.
- [ ] Metinler sınırlara sığıyor, yerelleştirme uzamasına yer bırakıyor ve parça birleştirme yok.
- [ ] Bağlantı, buton ve ikon adları ekran okuyucu kullanıcısı için bağlamdan bağımsız anlamlı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Net yerine esprili yazmak. Ana akıştaki mizah kullanıcıyı yavaşlatır ve kötü çevrilir; kişiliği riskin düşük olduğu anlara sakla.
- Genel etiketler ("Gönder", "Devam", "Tamam"). Ne olacağını adlandır.
- Ortak terim listesi olmadan ekran ekran yazmak; aynı şey ürün genelinde üç farklı ad alır.

## Örnek
Girdi: "Ekip arkadaşı davet penceresi: e-posta alanı, rol seçici, gönder butonu ve henüz kimse davet edilmemişken boş durum."

Zayıf: Buton "Gönder" · Yer tutucu "E-postaları virgülle ayırarak girin" · Boş durum "Burada bir şey yok."

Güçlü:
| Öğe | Metin |
|---|---|
| Alan etiketi | E-posta adresleri |
| Yardımcı metin | Birden fazla adresi virgülle ayırın. |
| Birincil buton | Davetleri gönder |
| Boş durum | Henüz ekip arkadaşınız yok. Projeleri paylaşmak ve görev atamak için kişileri davet edin. [Ekip arkadaşı davet et] |
