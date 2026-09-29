---
description: Sürüm sıklığı, paralel desteklenen sürüm sayısı, ekip büyüklüğü, CI olgunluğu ve uyum gereksinimlerine göre bir branch stratejisi (trunk-based development, GitHub Flow, GitFlow veya belgelenmiş bir varyant) önerir ve ortaya çıkan branch, merge ve sürüm kurallarını tanımlar. Ekip yeni bir repository kurduğunda, merge çakışmaları veya uzun ömürlü branch'lerle boğuştuğunda, sürüm modelini değiştirdiğinde ya da birden fazla canlı sürümü desteklemesi gerektiğinde kullanılır.
related: pipeline-design, release-plan, semantic-versioning, deployment-strategy, working-agreement
prompt: Tek serviste 12 geliştiriciyiz, haftalık yayına çıkıyoruz ama günlük istiyoruz; develop branch'i yüzünden hotfix'ler çok uzun sürüyor. Hangi branch stratejisini kullanalım?
---

# Branch Stratejisi Seçme

## Amaç
Ekibin gerçekte nasıl sürüm çıkardığına uyan bir branch modeli seçmek ve bunu uygulanabilir kurallar olarak yazmak. Doğru model entegrasyon sancısını ve teslim süresini azaltır; yanlış model merge borcu ve yavaş hotfix'ler üretir.

## Ne zaman kullanılır
- Yeni bir repository veya ekip için üzerinde anlaşılmış branch kuralları gerektiğinde.
- Uzun ömürlü branch'ler sancılı merge'lere yol açıyor ya da hotfix'ler yavaşsa.
- Sürüm modeli değişiyorsa (ör. planlı sürümlerden sürekli teslimata ya da birden fazla sürümü desteklemeye geçiş).

## Ne zaman kullanılmaz
- CI/CD pipeline'ının kendisini tasarlamak için `pipeline-design` kullanılır.
- Kodun canlıda kullanıcıya nasıl ulaşacağını seçmek (canary, blue-green) için `deployment-strategy` kullanılır.

## Girdiler
Zorunlu:
- Sürüm modeli: ne sıklıkta ve dağıtımın sürekli mi, planlı mı yoksa müşteriye teslim edilen (kurulumlu/mobil/kütüphane) bir ürün mü olduğu.
- Paralel olarak desteklenmesi gereken sürüm sayısı.

İsteğe bağlı, kaliteyi artırır:
- Ekip büyüklüğü ve repository'deki ekip sayısı, monorepo veya polyrepo.
- CI süresi, test otomasyonu seviyesi, feature flag imkânı.
- Mevzuat veya denetim gereksinimleri (değişiklik onayı, izlenebilirlik).
- Mevcut sorunlar.

Sürüm modeli veya desteklenen sürüm sayısı eksikse sor; öneri bunlara bağlıdır.

## Süreç
1. Bağlamın profilini çıkar: sürüm sıklığı, paralel desteklenen sürümler, CI hızı ve güvenilirliği, kritik akışlardaki test otomasyonu kapsamı, feature flag varlığı, ekip sayısı.
2. Karar sezgilerini uygula:
   - Sürekli veya günlük dağıtım, tek canlı sürüm, ~15 dakikanın altında güvenilir CI: kısa ömürlü branch'ler (< 2 gün) ve feature flag'lerle trunk-based development.
   - Sık dağıtım ama pull request ile inceleme ve orta düzey CI: GitHub Flow (main her zaman dağıtılabilir, kısa feature branch'ler, main'den dağıtım).
   - Stabilizasyon dönemli planlı sürümler veya birden fazla desteklenen sürüm (kurulumlu yazılım, SDK'lar, zorunlu güncellemenin geciktiği mobil): main'den release branch'leri; GitFlow yalnızca paralel sürümler ve ağır bir sürüm süreci gerçek kısıtlarsa.
3. Seçilen modelin bu bağlamdaki risklerini adlandır (ör. flag'siz trunk-based yarım işi açığa çıkarır; GitFlow teslim süresini ve hotfix yolunu uzatır).
4. Branch türlerini, adlandırmayı (`feature/<id>-<slug>`, `release/<x.y>`, `hotfix/<id>`), azami ömrü ve kimin oluşturabileceğini tanımla.
5. Merge kurallarını tanımla: merge yöntemi (squash, rebase, merge commit) ve gerekçesi, zorunlu incelemeler, zorunlu kontroller, branch koruması, doğrusal geçmiş istenip istenmediği.
6. Sürüm ve hotfix akışını tanımla: tag'lerin nerede atıldığı, düzeltmelerin ileri veya geri nasıl taşındığı (cherry-pick yönü), sürümleme şeması.
7. Ön koşulları ve mevcut modelden geçiş planını ölçülebilir sinyallerle yaz (branch yaşı, PR teslim süresi, merge çakışma sıklığı, hotfix teslim süresi).
8. Ekibin çalışma anlaşmasına ekleyebileceği tek sayfalık bir politika olarak özetle.
9. Politikanın gerektirdiği devam adımlarını öner: CI'da uygulatmak için `pipeline-design`, sürüm branch'leri ve etiketler için `semantic-versioning` ve `release-plan`, ekiple kayıt altına almak için `working-agreement`.

## Çıktı formatı
```markdown
# Branch Stratejisi: <repository/ekip>
## Bağlam
| Faktör | Değer |
|---|---|
| Sürüm sıklığı | ... |
| Paralel desteklenen sürüm | ... |
| CI süresi / güvenilirliği | ... |
| Feature flag | var/yok |

## Öneri
<model> — <yukarıdaki faktörlere bağlı gerekçe>
Reddedilen: <model> — <gerekçe>

## Branch Kuralları
| Branch | Adlandırma | Nereden açılır | Nereye merge edilir | Azami ömür | Koruma |
|---|---|---|---|---|---|

## Merge ve İnceleme Politikası
- ...

## Sürüm ve Hotfix Akışı
1. ...

## Ön Koşullar ve Geçiş Adımları
- ...

## Başarı Sinyalleri
- <metrik> — mevcut [BİLİNMİYOR] — hedef ...
```

## Kalite kontrol listesi
- [ ] Öneri popülerliğe değil, belirtilen sürüm modeline ve desteklenen sürümlere dayanıyor.
- [ ] En az bir alternatif gerekçesiyle reddedilmiş.
- [ ] Hotfix ve geri taşıma (back-port) akışları açık.
- [ ] Branch ömrü sınırları ve koruma kuralları somut.
- [ ] Ön koşullar (CI hızı, flag'ler, testler) boşluklarıyla listelenmiş.
- [ ] Verilmeyen mevcut metrikler uydurulmamış, `[BİLİNMİYOR]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sürekli dağıtılan bir web servisi için GitFlow benimsemek. Develop branch'i ikinci bir entegrasyon noktası ekler ve her düzeltmeyi yavaşlatır.
- Feature flag veya hızlı CI olmadan trunk-based development ilan etmek. Yarım işler sızar ve ekipler uzun ömürlü branch'lere geri döner.
- Düzeltmeleri yalnızca release branch'ine cherry-pick etmek. Önce main'de düzelt, sonra geriye taşı; aksi hâlde hata bir sonraki sürümde geri gelir.

## Örnek
Girdi: 12 geliştirici, tek servis, haftalık dağıtım ve günlük hedefi, `develop` yüzünden yavaş hotfix'ler, CI 25 dakika, feature flag yok.

Çıktıdan bir bölüm:
- Öneri: Şimdilik GitHub Flow; CI 15 dakikanın altına indiğinde ve feature flag altyapısı kurulduğunda trunk-based'e geçiş. Reddedilen: GitFlow'da kalmak — yalnızca tek canlı sürüm destekleniyor; `develop` ve release branch'leri fayda sağlamadan gecikme ekliyor.
- Hotfix akışı: `main`'den branch aç, hızlandırılmış incelemeli PR, `main`'den dağıt; `develop`'a ayrıca geri merge yok.
- Ön koşul: CI'ı 15 dakikanın altına indir; mevcut branch yaşı [BİLİNMİYOR] — geçişten önce iki hafta ölç.
