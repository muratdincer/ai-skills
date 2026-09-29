---
name: kb-article
description: "Notlardan, kayıtlardan, sohbet yazışmalarından veya uzman girdisinden aranabilir bir bilgi bankası makalesi (nasıl yapılır, sorun giderme veya açıklama) yazar; bulunabilir bir başlık, okuyucuların gerçekten kullandığı belirtiler ve arama terimleri, geçerlilik kapsamı, doğrulanmış adımlar, beklenen sonuçlar ve sahiplik içerir. Aynı soru sürekli sorulduğunda, bir destek kaydı veya olay yeniden kullanılabilir bir çözüm ürettiğinde, kayıt dışı bilgi yazıya dökülmesi gerektiğinde ya da \"bilgi bankası makalesi yaz\" veya \"bunu wiki için dokümante et\" dendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: knowledge
  area: capture
  title: "Bilgi bankası makalesi yazma"
  related: "how-to-guide, faq-builder, runbook, document-review, glossary-builder"
  prompt: "Yeni dizüstü bilgisayarlardaki VPN sertifika hatalarıyla ilgili bu destek yazışmasını bir bilgi bankası makalesine dönüştür."
---

# Bilgi Bankası Makalesi Yazma

## Amaç
Tekrar eden bir soruyu bir kez, insanların kendi kelimeleriyle arayarak bulabileceği ve yardım almadan uygulayabileceği biçimde cevaplamak. İyi bir makale tekrarlayan soruları ve kayıtları azaltır; bir sahibi ve gözden geçirme tarihi olduğu için güvenilir kalır.

## Ne zaman kullanılır
- Aynı soru veya kayıt tekrar tekrar geldiğinde.
- Bir destek vakası, olay veya uzman görüşmesi yeniden kullanılmaya değer bir çözüm ya da açıklama ürettiğinde.
- Bilgi tek bir kişinin kafasında veya bir sohbet yazışmasında duruyor ve yazıya dökülmesi gerekiyorsa.

## Ne zaman kullanılmaz
- Bir ürünün son kullanıcıları için birden çok görevi kapsayan eksiksiz bir rehber için `user-guide` veya `how-to-guide` kullanılır.
- On-call veya rollback içeren üretim değişiklikleri için operasyonel prosedürde `runbook` kullanılır.
- Tek bir kaynak dokümandan çok sayıda kısa soru çıkarılacaksa `faq-builder` kullanılır.

## Girdiler
Zorunlu:
- Kaynak materyal: kayıt, sohbet yazışması, notlar veya bir uzmanın problem ve çözüm anlatımı.

İsteğe bağlı, kaliteyi artırır:
- Hedef kitle (son kullanıcılar, destek ekibi, mühendisler) ve teknik seviyeleri.
- Ortam/sürüm kapsamı, ekran görüntüleri, hata mesajları, ilgili makaleler.
- Bilgi bankasının makale şablonu, kategorileri ve etiket kuralları.

Kaynak materyal yoksa iste. Çözümün doğrulanıp doğrulanmadığı belirsizse sor; aksi hâlde adımları `[DOĞRULANMADI]` olarak işaretle.

## Süreç
1. Tek bir makale türü seç: nasıl yapılır (görev), sorun giderme (belirti → neden → çözüm) veya açıklama (kavram/neden). Kaynak birden fazla soruyu cevaplıyorsa birkaç makaleye böl.
2. Hedef kitleyi ve arama kutusuna ne yazacaklarını belirle: birebir hata mesajları, kullanıcı dilindeki belirtiler, ürün ve özellik adları, sık yazım hataları veya eş anlamlılar.
3. Arama niyetiyle örtüşen bir başlık yaz: görev ("... nasıl sıfırlanır") veya belirti ("... sırasında 'X' hatası"). Başlıkta iç jargon ve kayıt numarası kullanma.
4. Soruyu doğrudan cevaplayan iki satırlık bir özet yaz; orada okumayı bırakan okuyucu da yardım almış olsun.
5. Geçerlilik kapsamını belirt: geçerli olduğu ve olmadığı ortamlar, sürümler, roller, platformlar.
6. Sorun gidermede önce belirtileri, sonra olasılık sırasına göre nedenleri, ardından her neden için hangi nedenin geçerli olduğunu doğrulama yoluyla birlikte çözümü listele.
7. Adımları numaralı, tek eylemli emir cümleleri olarak yaz; önemli adımlardan sonra beklenen sonucu ekle, arayüz etiketlerini, komutları veya yolları kaynaktaki hâliyle birebir kullan. Menü adı, komut veya değer uydurma; boşlukları `[BİLİNMİYOR]` olarak işaretle.
8. Adımlardan önce ön koşulları (erişim, yetki, araç), sonuna da eskalasyon yolunu içeren "Bu işe yaramadıysa" bölümünü ekle.
9. Hedef kitlenin görmemesi gereken kişisel verileri, iç sunucu adlarını veya sırları çıkar; yerlerine yer tutucu koy.
10. Üst verileri ekle: etiketler/anahtar kelimeler, ilgili makaleler, sahip, son doğrulama tarihi ve gözden geçirme aralığı, adımların doğrulanma durumu.
11. Hedef devam ediyorsa sonraki beceriyi öner: kalite geçişi için `document-review`, terimlerin tanımlanması gerekiyorsa `glossary-builder`, kısa soru-cevaplar türetmek için `faq-builder`.

## Çıktı formatı
```markdown
# <Arama niyetine uygun başlık>
**Özet:** <1-2 cümlelik doğrudan cevap>
**Geçerli olduğu yer:** <ürün/sürüm/ortam/rol> · **Geçerli olmadığı yer:** <...>

## Belirtiler (yalnızca sorun giderme)
- <birebir hata mesajı veya kullanıcının gördüğü davranış>

## Neden (yalnızca sorun giderme)
- <neden> — nasıl doğrulanır: <kontrol>

## Başlamadan Önce
- <erişim, yetki, araç>

## Adımlar
1. <tek eylem> — Beklenen: <sonuç>

## Bu İşe Yaramadıysa
- <sonraki kontrol> · Eskalasyon: <ekip/kanal>

## İlgili Makaleler
- <makale>

---
Anahtar kelimeler: <arama terimleri, eş anlamlılar, hata kodları> · Sahibi: <rol/ekip veya TBD> · Son doğrulama: <tarih veya TBD> · Gözden geçirme sıklığı: <aralık> · Durum: <Doğrulandı/[DOĞRULANMADI]>
```

## Kalite kontrol listesi
- [ ] Başlık ve anahtar kelimeler, birebir hata metni dahil okuyucunun arayacağı kelimeleri içeriyor.
- [ ] Özet, devamını okumaya gerek bırakmadan soruyu cevaplıyor.
- [ ] Her adım tek bir eylem; önemli adımların beklenen sonucu var.
- [ ] Hiçbir şey uydurulmamış: bilinmeyen komut, etiket veya değerler işaretli; doğrulanmamış adımlar belirtilmiş.
- [ ] Geçerlilik kapsamı, sahip ve gözden geçirme tarihi belirtilmiş; sır veya kişisel veri yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kullanıcılar belirtiyle ararken ("VPN sertifika güvenilmiyor diyor") başlığı iç nedene göre koymak ("Sertifika zinciri yapılandırma hatası"). Okuyucunun kelimelerini kullan.
- Sohbet yazışmasını çıkmaz denemeleriyle birlikte kopyalamak. Yalnızca teyit edilmiş yolu bırak; alternatifleri "Bu işe yaramadıysa" bölümüne taşı.
- Sahip veya gözden geçirme tarihi olmadan yayımlamak. Sahipsiz makaleler eskir ve tüm bilgi bankasına olan güveni zedeler.

## Örnek
Girdi: yeni dizüstü bilgisayarlarda VPN girişinin "sertifika güvenilir değil" hatasıyla başarısız olduğu bir destek yazışması; çözüm, şirket kök sertifikasını self-servis portaldan yüklemek.

Zayıf başlık: "VPN sorunu çözümü (kayıt 4812)".
Güçlü başlık: "Yeni dizüstü bilgisayarda VPN 'sertifika güvenilir değil' hatası".
- Özet: Yeni bilgisayarlarda şirket kök sertifikası eksik olabilir; self-servis portaldan yükleyip yeniden bağlanın.
- Adım 2: Self-servis portalı açın ve `[BİLİNMİYOR: menü etiketinin tam adı]` seçeneğini seçin — Beklenen: sertifikanın yüklendiğine dair onay.
- Anahtar kelimeler: VPN, sertifika güvenilir değil, yeni dizüstü, kök sertifika · Durum: temiz bir cihazda test edilene kadar `[DOĞRULANMADI]`.
