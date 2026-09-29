---
name: pull-request-description
description: "Neyin değiştiğini, nedenini, nasıl test edildiğini, riskleri ve yayına alma notlarını ve inceleyenlerin nereye odaklanması gerektiğini anlatan bir pull request açıklaması yazar. Geliştirici bir pull/merge request açtığında veya güncellediğinde ve elindeki diff, commit listesi, iş kaydı veya kaba notları inceleyenler için özetlemesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: collaboration
  title: "Pull request açıklaması"
  related: "commit-message, code-review, implement-from-story, release-notes, rollback-plan"
  prompt: "Bu commit'ler için PR açıklaması yaz. Değişiklik fatura PDF üretimini arka plan işine taşıyor."
---

# Pull Request Açıklaması

## Amaç
İnceleyenlere hızlı ve güvenli inceleme için gereken her şeyi vermek: niyet, kapsam, tasarım tercihleri, test kanıtı ve risk. İyi bir açıklama inceleme turlarını kısaltır ve kodun neden bu hâlde olduğunun aranabilir kaydı olur.

## Ne zaman kullanılır
- Bir veya daha fazla commit içeren bir branch'ten pull/merge request açılırken.
- PR inceleme sonrası ciddi biçimde değişti ve açıklama güncelliğini yitirdiyse.
- Büyük veya riskli bir değişiklik için yönlendirilmiş bir inceleme sırası gerekiyorsa.

## Ne zaman kullanılmaz
- Tek bir commit mesajı için `commit-message` kullanılır.
- Tasarım hâlâ açıksa ve kodlamadan önce tartışılması gerekiyorsa `technical-design-doc` kullanılır.
- Başkasının PR'ını incelemek için `code-review` kullanılır.

## Girdiler
Zorunlu:
- Diff, commit listesi veya değişikliğin net bir açıklaması.

İsteğe bağlı, kaliteyi artırır:
- Bağlı iş kaydı ve kabul kriterleri.
- Test sonuçları, UI değişiklikleri için ekran görüntüsü veya kayıt.
- Dağıtım notları: migration'lar, feature flag'ler, yapılandırma, bağımlı servisler.
- Ekibin PR şablonu.

Değişiklik bilgisi verilmediyse iste. Test kanıtı yoksa testlerin çalıştırıldığını iddia etme; `[TBD: test kanıtı]` ekle.

## Süreç
1. Değişikliği inceleyenin bakış açısından bir iki cümleyle özetle: merge sonrası hangi davranış farklı.
2. Nedeni yaz: iş kaydını bağla veya problemi anlat. Neden verilmemişse `[TBD]` olarak işaretle.
3. Değişiklikleri dosyaya göre değil, konuya göre grupla (alan mantığı, API, veri, UI, yapılandırma, testler).
4. Tasarım kararlarını ve reddedilen alternatifleri belirt; böylece inceleyenler farkında olmadan aynı tartışmayı yeniden açmaz.
5. Nasıl test edildiğini anlat: eklenen veya değiştirilen otomatik testler, ortamıyla birlikte manuel adımlar, neyin test edilmediği ve nedeni.
6. Riskleri belirle: veri migration'ı, geriye dönük uyumluluk, performans, güvenlik yüzeyi, eşzamanlılık. Her biri için önlemi yaz.
7. Dağıtım ve rollback notlarını yaz: adımların sırası, flag'ler, migration'lar (geri alınabilir mi), gerekli yapılandırma.
8. Bir inceleme sırası öner ve en dikkatli bakılması gereken dosyaları göster; üretilmiş veya mekanik değişiklikleri "göz gezdirmek yeterli" olarak işaretle.
9. PR elle yazılmış yaklaşık 400 satırı aşıyorsa veya refactoring ile davranış değişikliğini karıştırıyorsa bölmeyi öner ve nasıl bölüneceğini göster.
10. Şablonu doldur; gerçekten uygulanmayan bölümleri her yere "Yok" yazmak yerine kaldır.
11. Hedef devam ediyorsa `related` içinden sonraki adımı öner: inceleyen çağırmadan önce öz inceleme için `code-review`, Riskler bölümü geri alınamaz bir değişiklik gösteriyorsa `rollback-plan`, değişiklik kullanıcıya dönükse `release-notes`.

## Çıktı formatı
```markdown
## Özet
<1-2 cümle: merge sonrası davranış>

## Neden
<problem / iş kaydı bağlantısı veya [TBD]>

## Değişiklikler
- <konu>: <değişiklik>

## Tasarım Notları
- Karar: <...> — Değerlendirilen alternatif: <...> — Gerekçe: <...>

## Nasıl Test Edildi
- Otomatik: <eklenen/değişen testler>
- Manuel: <adımlar, ortam>
- Test edilmeyen: <boşluk ve nedeni>

## Riskler ve Önlemler
| Risk | Etki | Önlem |
|---|---|---|

## Dağıtım / Rollback
- <migration'lar, flag'ler, yapılandırma, adım sırası>

## İnceleme Rehberi
1. <dosya/alan> ile başla — <neden>
- Göz gezdirmek yeterli: <üretilmiş / mekanik değişiklikler>

## Ekran Görüntüleri (yalnızca UI değişikliklerinde)
```

## Kalite kontrol listesi
- [ ] Özet dosya listesini değil davranışı anlatıyor.
- [ ] "Neden" yazılmış veya açıkça `[TBD]` olarak işaretli.
- [ ] Test kanıtı olgusal; kanıt olmadan testlerin çalıştığı iddia edilmiyor.
- [ ] Geri alınamayan adımlar (migration, veri değişikliği) rollback etkileriyle birlikte belirtilmiş.
- [ ] İnceleyenler nereden başlayacağını ve neye göz gezdireceğini biliyor.
- [ ] Çok büyük veya karışık PR'lar için somut bir bölme önerisi var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Commit başlıklarını açıklama olarak tekrar yazmak. İnceleyenin ihtiyacı branch'in değişiklik listesi değil, niyet ve risktir.
- Neyin test edilmediğini yazmamak. Sessizlik "tamamen test edildi" diye okunur ve risk farkında olmadan inceleyene geçer.
- Dağıtım bağımlılığını unutmak (ör. tüketicinin üreticiden önce yayına alınması gerekmesi). Sırayı açıkça yaz.

## Örnek
Girdi: "add InvoicePdfJob", "enqueue job on invoice finalize", "remove sync PDF call", "add job retry tests" commit'leri.

Çıktıdan bir bölüm:
- Özet: Fatura PDF'leri artık kesinleştirme sonrasında bir arka plan işiyle üretiliyor; kesinleştirme endpoint'i PDF oluşturmayı beklemiyor.
- Risk: Kullanıcı faturayı PDF'i oluşmadan açabilir — Önlem: UI "oluşturuluyor" durumu gösteriyor; `[TBD: UI değişikliğinin kapsamda olduğunu teyit et]`.
- Dağıtım: Worker, API değişikliğinden önce yayına alınmalı ve kuyruğu tüketiyor olmalı; aksi hâlde PDF hiç üretilmez.
