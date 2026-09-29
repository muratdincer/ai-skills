# Kullanım Rehberi

Skill'lerin herhangi bir YZ aracına nasıl kurulacağı ve kullanılacağı. Örnek isteklerle skill listesi için [GUIDE.tr.md](GUIDE.tr.md), ağacın tamamı için [CATALOG.tr.md](CATALOG.tr.md) dosyasına bak.

## 1. Skill nedir

Skill, kısa bir YAML başlığı olan düz bir Markdown dosyasıdır (`SKILL.md`). Başlıktaki `description`, YZ'ye skill'i **ne zaman** kullanacağını söyler. Gövde ise **nasıl** kullanacağını anlatır: adımlar, çıktı şablonu, kalite kontrol listesi. Hiçbir skill belirli bir üreticiye bağlı değildir. Bu yüzden aynı dosya şu şekillerde kullanılabilir:

- açık Agent Skills formatını destekleyen araçlarda otomatik keşfedilen bir skill olarak,
- kural (rule) dosyası kullanan editörlerde bir kural veya talimat dosyası olarak,
- sohbet asistanlarında bir bilgi dosyası veya sistem prompt'u olarak,
- herhangi bir sohbete yapıştırılan bir prompt olarak.

Her skill'in İngilizce (`SKILL.md`) ve Türkçe (`SKILL.tr.md`) sürümü vardır. İkisinin ID'si, yapısı ve çıktısı aynıdır.

## 2. Dışa aktarma formatını seç

Tüm formatlar `scripts/export.py` ile üretilir (Python 3.8+, bağımlılık yok). Türkçe içerik için `--lang tr` kullan. Yalnızca ihtiyacın olanı kurmak için `--category`, `--role` veya `--skill` ile filtrele.

| Aracın şunu destekliyorsa… | Format | Komut |
|---|---|---|
| Agent Skills klasörleri (`<skills-dizini>/<id>/SKILL.md`) | `skills` | `python3 scripts/export.py skills --lang tr --dest <skills-dizini>` |
| Web/masaüstü uygulamada zip olarak skill yükleme | `zip` | `python3 scripts/export.py zip --lang tr --dest dist/zips` |
| Açıklamalı kural dosyaları (ör. `.mdc`) | `cursor-rules` | `python3 scripts/export.py cursor-rules --lang tr --dest .cursor/rules` |
| `AGENTS.md` (veya benzeri) bağlam dosyası | `agents-md` + `skills` | bkz. 3.3 |
| Özel asistanlar, projeler, bilgi dosyaları, sistem prompt'ları | `bundle` | `python3 scripts/export.py bundle --lang tr --role business-analyst --dest dist/is-analisti.md` |
| Özel bir destek yok (herhangi bir sohbet) | kopyala/yapıştır | skill dosyasını, ardından isteğini yapıştır |

## 3. Araç kurulumu

Skill klasörlerinin konumları sürümden sürüme değişebiliyor. Aşağıdaki yollar 2026 itibarıyla tipik olanlardır; aracının güncel dokümantasyonundan teyit et.

### 3.1 Agent Skills desteği yerleşik araçlar
Agent Skills formatını destekleyen kodlama ajanları ve sohbet uygulamaları, isteğin bir skill'in `description` alanıyla eşleştiğinde o skill'i otomatik yükler.

| Araç ailesi | Tipik proje konumu | Tipik kişisel konum |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| GitHub Copilot (agent modu / kodlama ajanı) | `.github/skills/` | aracın dokümanına göre |
| OpenAI Codex | aracın dokümanına göre (skills dizini) | `~/.codex/skills/` |
| Diğer Agent Skills uyumlu ajanlar | kendi skills dizinleri | kendi skills dizinleri |

```bash
# Örnek: tüm iş analizi skill'lerini Türkçe olarak bir projeye kur
python3 scripts/export.py skills --lang tr --category 01-business-analysis --dest .claude/skills
```

Skill yüklemeyi kabul eden web/masaüstü uygulamalar için (ör. Claude.ai) zip olarak dışa aktar ve ihtiyacın olanları yükle:

```bash
python3 scripts/export.py zip --lang tr --role product-owner --dest dist/zips
```

### 3.2 Kural dosyası kullanan editörler
Her skill için bir kural dosyası üret. Kurallar "ajan tarafından istenen" türdedir, her zaman uygulanmaz. Editör bir skill'i yalnızca açıklaması eşleştiğinde bağlama ekler.

```bash
python3 scripts/export.py cursor-rules --lang tr --role developer --dest .cursor/rules
```

### 3.3 AGENTS.md (veya benzeri bağlam dosyası) okuyan ajanlar
Skill'leri bir klasöre koy ve ajana hangi iş için hangi dosyayı açacağını söyleyen bir dizin ver.

```bash
python3 scripts/export.py skills    --lang tr --dest .agent-skills
python3 scripts/export.py agents-md --lang tr --dest AGENTS.md --skills-root .agent-skills
```

Aracın farklı bir bağlam dosyası adı kullanıyorsa (ör. `GEMINI.md`), `--dest` olarak o adı ver ya da aracı `AGENTS.md` okuyacak şekilde yapılandır.

### 3.4 Sohbet asistanları (özel asistanlar, projeler, GPT'ler, Gem'ler)
Her rol için bir asistan oluştur ve bilgi dosyası veya talimat olarak bir paket (bundle) ver:

```bash
python3 scripts/export.py bundle --lang tr --role business-analyst --dest dist/is-analisti.md
```

Asistan için önerilen talimat: "Ekteki dosyada bir skill seti var. Her istekte açıklamasına göre uygun skill'i seç, Süreç adımlarını uygula ve Çıktı formatında yanıt ver. Zorunlu girdiler eksikse önce onları sor."

Bir kategorinin tamamını içeren paketler büyük olabilir. Rol başına bir paket tercih et.

### 3.5 Doğrudan API kullanımı
Skill gövdesini sistem prompt'u (veya bir parçası) olarak, kullanıcının isteğini kullanıcı mesajı olarak gönder. Modelin birçok skill arasından seçim yapması için bir paketteki dizini (ID'ler + açıklamalar) sistem prompt'una koy, modelin ihtiyaç duyduğu skill'i söylemesini sağla ve bir sonraki çağrıda o dosyayı yükle.

## 4. Skill'leri kullanma

**Seçimi araca bırak.** İşi doğal bir dille anlat: "Bugünkü çalıştaydan notlarım bunlar, aksiyon maddelerine çevir." Skill destekleyen bir araç `action-item-extraction` skill'ini seçer.

**Kesinlik istiyorsan skill'in adını ver:** "Aşağıdaki talep için request-completeness-check kullan."

**Zorunlu girdileri ver.** Her skill'in *Girdiler* bölümü bunları listeler. Bir şey eksikse skill uydurmak yerine onu sorar ya da `[BİLİNMİYOR]` / `[VARSAYIM]` olarak işaretler.

**Skill'leri zincirle.** Skill'ler bilerek küçük tutuldu. Tipik zincirler:

| Hedef | Zincir |
|---|---|
| Yeni talepten hazır backlog'a | `request-intake-document` → `request-clarification-questions` → `request-completeness-check` → `brd-writing` → `epic-breakdown` → `user-story` → `acceptance-criteria` → `invest-check` |
| Toplantıdan takibe | `meeting-agenda` → `meeting-notes` → `decision-log` → `action-item-extraction` → `meeting-follow-up` |
| Fikirden mimari karara | `problem-statement` → `technology-selection` → `trade-off-analysis` → `adr` → `architecture-review` |
| Hikayeden birleştirilmiş koda | `task-breakdown` → `implement-from-story` → `unit-test-writing` → `commit-message` → `pull-request-description` → `code-review` |
| Gereksinimden sürüme | `testability-review` → `test-scenarios-from-requirements` → `test-case-writing` → `bug-report` → `test-summary-report` → `release-quality-gate` → `release-notes` |
| Olaydan öğrenmeye | `incident-response` → `incident-communication` → `postmortem` → `lessons-learned` |

Her skill, başlığındaki `related` alanında komşu skill'leri listeler.

**Dil.** Türkçe çıktı ve Türkçe şablonlar için Türkçe dosyaları kur. İngilizce skill'leri kurup yanıtı Türkçe de isteyebilirsin; yapı aynı kalır.

## 5. Özelleştirme

- Bir skill'i kopyala ve *Çıktı formatı* bölümünü kurumunun şablonuna uyarla. ID'yi koru ya da katalogda yeni bir ID oluştur.
- Şirket kurallarını (isimlendirme, zorunlu alanlar, onay adımları) *Süreç* veya *Kalite kontrol listesi* bölümüne ekle.
- Yeni bir skill eklemek için [AUTHORING.md](AUTHORING.md) dosyasını izle ya da doğrudan `ai-skill-authoring` skill'ini kullan.

## 6. İyi uygulamalar

- İçeriği herhangi bir YZ aracına göndermeden önce kişisel verileri, kimlik bilgilerini ve gizli rakamları çıkar veya maskele.
- Çıktıları taslak olarak değerlendir. Kalite kontrol listesi hataları azaltır ama kararın sahibi bir insandır.
- Yalnızca ihtiyacın olan rolleri kur. Daha az sayıda ve ilgili skill daha güvenilir şekilde seçilir.
