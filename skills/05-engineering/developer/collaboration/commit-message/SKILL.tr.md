---
description: Conventional Commits formatında; net bir başlık, değişikliğin nedenini açıklayan bir gövde ve kırıcı değişiklik ile iş kaydı referansları için alt bilgiler içeren commit mesajı yazar. Geliştiricinin elinde bir diff, değişiklik listesi veya kısa bir açıklama olduğunda ve commit mesajına ihtiyaç duyduğunda ya da karışık bir değişikliği iyi kapsamlanmış commit'lere bölmek istediğinde kullanılır.
related: pull-request-description, changelog-entry, semantic-versioning, branching-strategy
prompt: Bu diff için commit mesajı yaz. Ödeme istemcisine backoff ile yeniden deneme ekliyor ve timeout yapılandırma anahtarının adını düzeltiyor.
---

# Commit Mesajı Yazma

## Amaç
İnceleyenin, geçmişte arama yapan gelecekteki geliştiricinin ve sürüm araçlarının birlikte kullanabileceği bir commit mesajı üretmek: taranabilir bir başlık, değişikliğin gerekçesi ve sürümleme ile değişiklik günlüğü için makine tarafından okunabilir işaretler.

## Ne zaman kullanılır
- Bir diff veya değişiklik açıklaması hazır olduğunda ve commit mesajı gerektiğinde.
- Stage edilmiş değişiklik birden fazla konuyu karıştırıyorsa ve birkaç commit'e bölünmesi gerekiyorsa.
- Ekip Conventional Commits'e geçiyor ve otomatik sürümleme veya changelog üreten mesajlar istiyorsa.

## Ne zaman kullanılmaz
- Bütün bir branch'i inceleyenlere anlatmak için `pull-request-description` kullanılır.
- Kullanıcıya dönük sürüm geçmişi yazmak için `changelog-entry` veya `release-notes` kullanılır.

## Girdiler
Zorunlu:
- Diff veya neyin değiştiğine dair net bir açıklama.

İsteğe bağlı, kaliteyi artırır:
- Değişikliğin nedeni (hata, gereksinim, olay, refactoring hedefi).
- İş kaydı numarası, ekibin scope adları, değişikliğin kırıcı olup olmadığı.
- Ekip kuralları (izinli type ve scope'lar, başlık uzunluğu, sign-off kuralları).

Ne diff ne de açıklama verildiyse iste. Neden belirtilmemişse tahmin etme; gövdeye `[TBD: neden]` yer tutucusu koy.

## Süreç
1. Değişikliği oku ve her mantıksal değişikliği listele. Birbiriyle ilgisiz amaçlara hizmet ediyorlarsa (ör. bir özellik ve alakasız bir yeniden adlandırma) ayrı commit'ler öner ve her biri için ayrı mesaj yaz.
2. Type'ı seç: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`, `revert`, `style`. Seçimi dokunulan dosya türüne göre değil, gözlemlenebilir etkiye göre yap.
3. Etkilenen modül veya bounded context'ten isteğe bağlı bir scope seç; biliniyorsa ekibin mevcut scope adlarını kullan.
4. Başlığı yaz: emir kipi (İngilizce mesajlarda imperative), iki noktadan sonra küçük harf, sonda nokta yok, en fazla ~50 karakter (kesin sınır 72). Başlık geliştiricinin ne yaptığını değil, commit'in ne yaptığını söyler.
5. Değişikliğin kırıcı olup olmadığına karar ver (public API, şema, yapılandırma anahtarı, mesaj sözleşmesi, CLI parametresi). Kırıcıysa type/scope'tan sonra `!` ekle ve geçiş talimatı içeren `BREAKING CHANGE:` alt bilgisini yaz.
6. Gövdeyi 72 sütunda satır kaydırarak yaz: problem veya motivasyon, neden bu yaklaşım, dikkat edilmesi gereken yan etkiler veya ödünleşimler. Diff'i satır satır tekrar etme.
7. Alt bilgileri ekle: iş kaydı için `Refs:` veya `Closes:`, eşli çalışıldıysa `Co-authored-by:`, gerekiyorsa sign-off.
8. Mesajda diff'ten kopyalanmış parola, müşteri verisi, iç sunucu adı veya kimlik bilgisi olmadığını kontrol et.
9. Kullanıcı incelemeye veya sürüme doğru ilerliyorsa branch için `pull-request-description`, kullanıcıya dönük geçmiş için `changelog-entry`, kırıcı değişiklik sonraki sürüm numarasını etkiliyorsa `semantic-versioning` öner.

## Çıktı formatı
```markdown
<type>(<scope>)<!>: <emir kipinde başlık, <=50 karakter>

<neden: problem veya motivasyon, 1-3 cümle>
<nasıl / bilinmesi gereken ödünleşimler, isteğe bağlı>

BREAKING CHANGE: <ne bozuluyor ve nasıl geçilir>   (yalnızca kırıcıysa)
Refs: <iş kaydı numarası veya [TBD]>
```
Bölme önerildiyse her commit'i içerdiği dosya veya parçalarla birlikte listele, ardından mesajını yaz.

## Kalite kontrol listesi
- [ ] Her commit tek bir mantıksal değişiklik içeriyor; karışık değişiklikler bölme önerisiyle işaretlendi.
- [ ] Type etkiyi yansıtıyor (`fix`, `refactor`, `perf` ayrımı) ve ekip kurallarına uyuyor.
- [ ] Başlık emir kipinde, somut ve uzunluk sınırı içinde.
- [ ] Gövde nedeni açıklıyor; yalnızca diff'e bakarak okunabilecek bilgiyi tekrarlamıyor.
- [ ] Kırıcı değişiklikler hem `!` hem de `BREAKING CHANGE:` alt bilgisiyle işaretli.
- [ ] Uydurma iş kaydı numarası yok; bilinmeyen referanslar `[TBD]`.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "fix bug" veya "update code" gibi belirsiz başlıklar. Davranışı adlandır: "fix: reject expired tokens in refresh flow".
- Davranış değiştiren bir değişikliği `refactor` olarak etiketlemek. Refactoring gözlemlenebilir davranışı değiştirmez; değiştiriyorsa `feat` veya `fix` kullanılır.
- Kırıcı bir yapılandırma veya sözleşme değişikliğini `chore` içine gizlemek. Sürüm araçları bunu patch olarak yayınlar.

## Örnek
Girdi: "PaymentClient'a üstel backoff ile yeniden deneme eklendi (3 deneme); `payment.timeOut` yapılandırma anahtarı `payment.timeout` olarak değiştirildi."

Zayıf: `fix: update payment stuff` — iki değişikliği karıştırıyor, kırıcı yeniden adlandırmayı gizliyor, nedeni yok.

Güçlü, çıktıdan bir bölüm (iki commit'e bölündü):
```
fix(payment)!: rename timeout config key to payment.timeout

The old key was misspelled and silently ignored, so the client
always used the 100 s library default.

BREAKING CHANGE: rename `payment.timeOut` to `payment.timeout`
in every environment config before deploying.
Refs: [TBD]
```
```
feat(payment): retry transient failures with exponential backoff
```
Not: Ekip commit mesajlarını Türkçe yazıyorsa aynı yapı korunur, yalnızca başlık ve gövde Türkçe olur.
