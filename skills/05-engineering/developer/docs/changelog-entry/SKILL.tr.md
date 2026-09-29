---
name: changelog-entry
description: "Commit'lerden, merge edilmiş pull request'lerden veya bir değişiklik listesinden Keep a Changelog formatında (Added, Changed, Deprecated, Removed, Fixed, Security) değişiklik günlüğü girdileri yazar; yazılımı kullananlar için yazılır, kırıcı değişiklikleri ve geçiş adımlarını öne çıkarır. Bir sürüm bölümü hazırlanırken, bir merge sonrasında Unreleased bölümü güncellenirken veya gürültülü commit geçmişi okunabilir bir değişiklik geçmişine dönüştürülürken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: docs
  title: "Değişiklik günlüğü girdisi"
  related: "commit-message, release-notes, semantic-versioning, pull-request-description, app-store-release-notes"
  prompt: "Merge edilmiş bu PR başlıklarını istemci kütüphanemizin 2.4.0 sürümü için bir değişiklik günlüğü girdisine dönüştür."
---

# Değişiklik Günlüğü Girdisi

## Amaç
Bir kütüphane, servis veya uygulamayı kullananlara sürüm başına kayda değer değişikliklerin seçilmiş, insanlar tarafından okunabilir bir kaydını sunmak; böylece yükseltip yükseltmeyeceklerine ve nasıl yükselteceklerine karar verebilirler. Değişiklik günlüğü okuyucu içindir, commit geçmişinin dökümü değildir.

## Ne zaman kullanılır
- Bir sürüm yayımlanmak üzereyken ve değişiklik günlüğü bölümünün yazılması gerektiğinde.
- Bir pull request merge edildiğinde ve Unreleased bölümüne girdi eklenmesi gerektiğinde.
- Bir projenin yalnızca commit geçmişi olduğunda ve okunabilir bir değişiklik geçmişine ihtiyaç duyulduğunda.

## Ne zaman kullanılmaz
- Bir sürümü son kullanıcılara bağlam ve öne çıkanlarla duyurmak için `release-notes` kullanılır.
- Mobil uygulama güncellemesi için mağaza sınırlı kısa metin için `app-store-release-notes` kullanılır.
- Sürüm numarasının kendisine karar vermek için `semantic-versioning` kullanılır.

## Girdiler
Zorunlu:
- Değişiklikler: commit'ler, merge edilmiş pull request başlıkları ve açıklamaları veya bir değişiklik listesi.

İsteğe bağlı, kaliteyi artırır:
- Hedef sürüm ve yayın tarihi; bir önceki sürüm.
- Mevcut değişiklik günlüğü (üslup, bağlantılar ve ifadelerle uyum için).
- Hedef kitle (kütüphane kullanıcıları, API istemcileri, işletenler) ve iş takip sistemi bağlantıları.

Değişiklikler verilmediyse iste. Sürüm veya tarih bilinmiyorsa girdiyi `[Unreleased]` altında veya `[TBD]` ile yaz.

## Süreç
1. Bir önceki sürümden bu yana tüm değişiklikleri topla; hedef kitle katkı verenler değilse saf dahili gürültüyü (biçimlendirme, yalnızca test, CI ayarları, gözlemlenebilir etkisi olmayan refactoring'ler) çıkar.
2. İlişkili maddeleri birleştir: tek bir özellik için yapılmış birkaç commit tek girdi olur.
3. Her girdiyi Keep a Changelog bölümlerinden tam olarak birine yerleştir: Added (yeni yetenekler), Changed (mevcut davranışta değişiklik), Deprecated (hâlâ çalışıyor, kaldırılacak), Removed, Fixed (hatalar), Security (güvenlik açıkları). Commit'lerde yanlış etiketlenmiş bir değişikliği (ör. `refactor` olarak etiketlenmiş bir davranış değişikliği) etkisine göre sınıflandır ve bunu not et.
4. Her girdiyi tüketicinin bakış açısıyla yaz: artık ne yapabildiği veya neyin farklı davrandığı; tek satırda, bir fiille veya etkilenen özellikle başlayarak. Public API değilse dahili sınıf adlarından kaçın.
5. Kırıcı değişiklikleri belirle (kaldırılan veya yeniden adlandırılan public API, değişen varsayılanlar, şema veya yapılandırma değişiklikleri, sıkılaşan doğrulama, değişen hata kodları) ve bir iki satırlık geçiş adımıyla `**BREAKING:**` olarak işaretle.
6. Security girdilerinde etkilenen sürümleri ve önem referansını (varsa CVE numarası) istismar ayrıntısı vermeden yaz.
7. Varsa referansları ekle: issue veya pull request numaralarını bağlantı olarak ver; numara uydurma.
8. Bölümleri Keep a Changelog'un öngördüğü sırayla, bölüm içindeki girdileri ise tüketici açısından önemine göre sırala.
9. Sürüm başlığını `## [x.y.z] - YYYY-AA-GG` (ISO 8601 tarih) formatında yaz; mevcut günlük karşılaştırma bağlantıları kullanıyorsa en alttaki bağlantıyı ekle veya güncelle.
10. Sürümü değişikliklerle karşılaştır: SemVer kullanan projelerde kırıcı değişiklik major, yeni özellik minor, düzeltme patch artışı gerektirir. Uyuşmuyorsa işaretle ve `semantic-versioning` öner; kullanıcıya dönük bir duyuru için `release-notes` öner.

## Çıktı formatı
```markdown
## [<x.y.z> | Unreleased] - <YYYY-AA-GG | TBD>
### Added
- <tüketiciye dönük değişiklik> ([#<ref>](<bağlantı>))
### Changed
- **BREAKING:** <ne değişti>. Geçiş: <adım>.
### Deprecated
- <öğe> — yerine <alternatif> kullanın; kaldırılması <sürüm veya [TBD]> sürümünde planlanıyor.
### Removed
### Fixed
### Security
- <düzeltilen açık, etkilenen sürümler, referans>
```
Boş bölümler çıkarılır.

## Kalite kontrol listesi
- [ ] Her girdi bir uygulama adımını değil, tüketicinin gözlemleyebileceği bir etkiyi anlatıyor.
- [ ] Her girdi tam olarak bir doğru bölümde; boş bölümler çıkarılmış.
- [ ] Her kırıcı değişiklik işaretli ve bir geçiş adımı içeriyor.
- [ ] Hiçbir referans, sürüm veya tarih uydurulmadı; bilinmeyenler `[TBD]`.
- [ ] Sürüm numarası değişikliklerin türüyle tutarlı ya da uyumsuzluk işaretlenmiş.
- [ ] Harici kitleler için dahili gürültü (CI, biçimlendirme, yalnızca test değişiklikleri) çıkarılmış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Commit başlıklarını olduğu gibi yapıştırmak ("fix typo", "wip", "address review"). Okuyucu için seç ve yeniden yaz.
- Kırıcı bir varsayılan değişikliğini Fixed altına saklamak. Yükseltmeyi bozabilecek her şey BREAKING işaretiyle Changed veya Removed altına girer.
- "Çeşitli hata düzeltmeleri ve iyileştirmeler" yazmak. Kayda değer olanları listele ya da hiçbir şey yazma.

## Örnek
Girdi: PR'lar "#212 add retry option to HttpClient", "#215 refactor: timeout default 30s -> 10s", "#218 fix NPE when header missing", "#219 bump test deps".

Zayıf: "- Timeout varsayılanı refactor edildi. - Test bağımlılıkları güncellendi. - NPE düzeltildi."

Güçlü bölüm:
```markdown
## [3.0.0] - [TBD]
### Added
- `retry` seçeneğiyle geçici HTTP hataları için yapılandırılabilir yeniden deneme ([#212]).
### Changed
- **BREAKING:** Varsayılan istek timeout'u 30 sn'den 10 sn'ye düşürüldü. Geçiş: önceki davranışı korumak için `timeout: 30s` ayarlayın ([#215]).
### Fixed
- İsteğe bağlı bir header eksik olduğunda istekler artık null referans hatasıyla başarısız olmuyor ([#218]).
```
Not: #215 `refactor` olarak etiketlenmiş ama davranışı değiştiriyor; sürüm 2.4.0 değil, major artış olmalı.
