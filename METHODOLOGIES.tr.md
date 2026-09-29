# Metodoloji Rehberi

Skill'ler metodolojiden bağımsızdır. Bir kullanıcı hikayesi, risk kaydı veya retrospektif; ekip Scrum, Kanban ya da aşamalı bir plan ile çalışsa da aynı iştir. Bu rehber, yaygın çalışma biçimlerinin her adımında hangi skill'lerin kullanılacağını gösterir.

## 1. Yaşam döngüsü görünümü (her metodolojide geçerli)

| Yaşam döngüsü aşaması | Temel sorular | Skill'ler |
|---|---|---|
| Başlatma | Neden, kimin için, değer mi? | `request-intake-document`, `request-triage`, `problem-statement`, `feasibility-study`, `cost-benefit-analysis`, `project-charter`, `stakeholder-identification`, `stakeholder-map` |
| Keşif | Problem tam olarak ne, kullanıcılar kim? | `persona`, `jobs-to-be-done`, `problem-interview-script`, `customer-journey-map`, `opportunity-solution-tree`, `assumption-mapping`, `experiment-design` |
| Gereksinimler | Çözüm ne yapmalı? | `interview-question-set`, `workshop-plan`, `brd-writing`, `frd-writing`, `srs-writing`, `user-story`, `acceptance-criteria`, `nfr-specification`, `requirements-gap-analysis`, `ambiguity-detection`, `traceability-matrix` |
| Planlama | Ne kadar, ne zaman, kim? | `wbs`, `estimation-three-point`, `schedule-plan`, `resource-plan`, `risk-register`, `roadmap`, `release-planning`, `dependency-map` |
| Tasarım | Nasıl çalışacak? | `solution-architecture-document`, `c4-model`, `adr`, `event-storming`, `api-contract`, `database-schema-design`, `threat-model`, `user-flow`, `wireframe-spec` |
| Geliştirme | Yap | `task-breakdown`, `implement-from-story`, `unit-test-writing`, `code-review`, `pull-request-description`, `commit-message`, `pipeline-design` |
| Doğrulama | Çalışıyor mu, yeterince iyi mi? | `test-strategy`, `test-plan`, `test-case-writing`, `bug-report`, `uat-plan`, `secure-code-review`, `performance-test-plan`, `release-quality-gate` |
| Sürüm | Güvenle yayına al | `release-plan`, `deployment-checklist`, `rollback-plan`, `go-no-go`, `release-notes`, `go-to-market-plan` |
| İşletim | Sağlıklı tut | `slo-definition`, `alert-design`, `runbook`, `incident-response`, `ticket-triage`, `problem-management` |
| İyileştirme | Öğren ve uyarla | `postmortem`, `lessons-learned`, `feature-adoption-review`, `tech-debt-assessment`, `retrospective-facilitation` |

## 2. Plan güdümlü (Şelale, V-Modeli)

İş, aralarında resmi dokümanlar ve onaylar (geçiş kapıları) bulunan ardışık aşamalardan geçer.

| Aşama / kapı | Skill'ler |
|---|---|
| Proje başlangıcı, başlatma belgesi onayı | `project-charter`, `scope-statement`, `raci-matrix`, `communication-plan`, `kickoff-deck` |
| Gereksinim temel sürümü | `brd-writing`, `frd-writing`, `srs-writing`, `use-case-spec`, `requirements-review-checklist`, `requirements-sign-off` |
| Tasarım temel sürümü | `solution-architecture-document`, `technical-design-doc`, `architecture-review` |
| Planlama ve kontrol | `wbs`, `schedule-plan`, `budget-plan`, `earned-value-analysis`, `change-control`, `raid-log`, `project-status-report` |
| Test seviyeleri (V-Modeli: her tanım bir test seviyesiyle eşleşir) | gereksinimler ↔ `uat-plan`, tasarım ↔ `integration-test-writing`, ayrıntılı tasarım ↔ `unit-test-writing`; ek olarak `test-plan`, `traceability-matrix`, `test-summary-report` |
| Kabul ve kapanış | `acceptance-certificate`, `project-closure-report`, `lessons-learned` |

İpucu: Plan güdümlü çalışmada değişiklik pahalıdır. Gereksinim onayından önce `requirements-gap-analysis`, `ambiguity-detection` ve `requirements-consistency-check` skill'lerini çalıştır.

## 3. İteratif çerçeveler (Scrum ve benzerleri)

İş, sabit uzunluktaki iterasyonlarda (sprint) ve az sayıda etkinlikle teslim edilir.

| Etkinlik / artefakt | Skill'ler |
|---|---|
| Ürün hedefi, ürün backlog'u | `product-vision`, `roadmap`, `backlog-refinement`, `backlog-prioritization`, `story-splitting`, `definition-of-ready` |
| İterasyon planlaması | `iteration-goal`, `iteration-planning`, `task-breakdown`, `estimation-session` |
| Günlük toplantı | `daily-sync-summary`, `impediment-tracking` |
| Artım ve Bitti Tanımı | `definition-of-done`, `code-review`, `release-quality-gate` |
| İterasyon değerlendirmesi | `iteration-review-prep`, `stakeholder-review-prep`, `demo-script` |
| Retrospektif | `retrospective-format`, `retrospective-facilitation`, `action-item-extraction` |
| Öngörü | `velocity-analysis`, `burndown-analysis`, `monte-carlo-forecast` |

## 4. Akış tabanlı (Kanban)

İş sürekli akar. Odak, devam eden işi sınırlamak ve akışı iyileştirmektir.

| Uygulama | Skill'ler |
|---|---|
| İş akışını görselleştir ve tanımla | `wip-policy`, `value-stream-map`, `definition-of-done` |
| WIP'i sınırla, akışı yönet | `wip-policy`, `cycle-time-analysis`, `impediment-tracking` |
| Yeniden doldurma (replenishment) | `request-triage`, `backlog-prioritization` |
| Teslimat planlama | `monte-carlo-forecast`, `release-planning` |
| Hizmet teslimi / operasyon değerlendirmesi | `cycle-time-analysis`, `sla-breach-analysis`, `status-update` |
| Birlikte iyileştir | `retrospective-facilitation`, `five-whys` |

## 5. Mühendislik pratikleri (XP)

| Pratik | Skill'ler |
|---|---|
| Test güdümlü geliştirme | `tdd-cycle`, `unit-test-writing` |
| Refactoring, basit tasarım | `refactoring`, `clean-code-review` |
| Eşli / grup programlama, ortak sahiplik | `code-review`, `review-comment-writing`, `coding-standards` |
| Sürekli entegrasyon, küçük sürümler | `pipeline-design`, `branching-strategy`, `commit-message` |
| Müşteri testleri | `bdd-feature-file`, `acceptance-criteria` |

## 6. Yalın (Lean) ve Yalın Girişim

| Fikir | Skill'ler |
|---|---|
| Değeri belirle, israfı kaldır | `value-stream-map`, `process-gap-analysis` |
| Oluştur-ölç-öğren | `hypothesis-statement`, `experiment-design`, `mvp-scoping`, `ab-test-analysis` |
| Doğrulanmış öğrenme | `feedback-synthesis`, `feature-adoption-review`, `assumption-mapping` |

## 7. Ölçeklenmiş çeviklik (SAFe, LeSS, Nexus ve benzerleri)

| İhtiyaç | Skill'ler |
|---|---|
| Portföy kararları | `portfolio-prioritization`, `backlog-prioritization` (WSJF), `benefits-realization` |
| Çok ekipli planlama etkinliği | `program-roadmap`, `cross-team-dependency-board`, `dependency-map`, `iteration-planning` |
| Yönetişim | `governance-framework`, `steering-committee-pack` |
| Mimari pist (architecture runway) | `target-state-architecture`, `architecture-principles`, `tech-radar` |
| Ekip topolojileri | `team-topology`, `role-definition` |

## 8. DevOps ve sürekli teslimat

| Pratik | Skill'ler |
|---|---|
| Hatlar (pipeline) ve dağıtım | `pipeline-design`, `deployment-strategy`, `environment-strategy`, `iac-review` |
| Sürüm güvenliği | `rollback-plan`, `deployment-checklist`, `semantic-versioning` |
| Güvenilirlik (SRE) | `slo-definition`, `error-budget-policy`, `alert-design`, `observability-plan` |
| Olaylardan öğrenme | `incident-response`, `postmortem`, `runbook` |
| Teslimatı ölçme | `engineering-metrics-review` (DORA) |

## 9. Tasarım odaklı düşünme ve UX

| Aşama | Skill'ler |
|---|---|
| Empati kur | `research-plan`, `problem-interview-script`, `observation-notes`, `persona` |
| Tanımla | `research-synthesis`, `problem-statement`, `jobs-to-be-done` |
| Fikir üret | `opportunity-solution-tree`, `user-flow` |
| Prototiple | `wireframe-spec`, `information-architecture` |
| Test et | `usability-test-script`, `heuristic-evaluation` |

## 10. Hibrit yapılar

Çoğu kurum yöntemleri karıştırır: aşamalı bütçe ve sözleşme içinde iteratif teslimat ya da plan güdümlü bir sürüm sürecini besleyen Scrum ekipleri gibi. Skill'leri metodolojiye göre değil aktiviteye göre seç:

- Sözleşme ve bütçe seviyesi: `statement-of-work`, `project-charter`, `budget-plan`, `steering-committee-pack`.
- Ekip seviyesi: 3. ve 4. bölümlerdeki iteratif veya akış skill'leri.
- Sürüm seviyesi: `release-plan`, `go-no-go`, `change-request-rfc`.

Bir skill adımında "ekip sabit iterasyonlarla çalışıyorsa…" yazıyorsa, bu yalnızca senin durumun buysa uygulanır. Değilse atla.
