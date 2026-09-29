---
description: "Bir Dockerfile'ı (veya Containerfile) imaj boyutu, katman ve önbellek verimliliği, güvenlik sıkılaştırması ve derleme tekrarlanabilirliği açısından inceler; düzeltilmiş kod parçalarıyla önceliklendirilmiş bulgular verir. Bir Dockerfile inceleme için paylaşıldığında, imaj büyük veya yavaş derleniyorsa ya da tarayıcı bulgu veriyorsa ve bir servisin ilk üretim sürümünden önce kullanılır."
related: "kubernetes-manifest-review, pipeline-design, secrets-management-plan, dependency-vulnerability-review"
prompt: "Node.js servisimizin bu Dockerfile'ını incele. İmaj 1,2 GB ve güvenlik taraması 40 zafiyet raporluyor."
---

# Dockerfile İnceleme

## Amaç
Çalışan bir Dockerfile'ı küçük, güvenli, tekrarlanabilir ve önbellek dostu hale getirmek; her bulguyu gerekçelendirip somut bir düzeltmeyle vermek.

## Ne zaman kullanılır
- Bir Dockerfile pull request ile geldiğinde veya inceleme için paylaşıldığında.
- İmaj büyükse, yavaş derleniyorsa veya çok sayıda tarayıcı bulgusu varsa.
- Bir servis ilk kez üretime çıkmak üzereyken.

## Ne zaman kullanılmaz
- Sorun orkestratördeki çalışma zamanı yapılandırmasıysa `kubernetes-manifest-review` kullanılır.
- Konu uygulama bağımlılıklarındaki zafiyetlerse `dependency-vulnerability-review` kullanılır.
- Hata dosyada değil derleme hattındaysa `pipeline-failure-triage` kullanılır.

## Girdiler
Zorunlu:
- Dockerfile metni.

İsteğe bağlı, kaliteyi artırır:
- Ignore dosyası (ör. `.dockerignore`), dil/derleme aracı, hedef çalışma platformu ve mimari.
- Mevcut imaj boyutu, tarayıcı çıktısı, derleme süresi.
- Kurumsal base image politikası.

Dockerfile yoksa iste.

## Süreç
1. Teknoloji yığınını, derleme türünü ve multi-stage build kullanılıp kullanılmadığını belirle.
2. Base image: resmi veya onaylı kaynak, minimal varyant (slim, distroless, libc uyumluysa alpine), tag ve digest ile sabitlenmiş, `latest` değil.
3. Derleme aşamaları: derleme araçlarını çalışma zamanından ayır; son aşamaya yalnızca çıktıları kopyala.
4. Katman ve önbellek: bağımlılık manifestleri kaynaktan önce kopyalanıp kurulmalı; ilişkili `RUN` komutları birleştirilmeli; paket önbellekleri aynı katmanda temizlenmeli; ignore dosyası `.git`, testler ve yerel env dosyalarını dışlamalı.
5. Güvenlik: sabit UID ile root olmayan `USER`; `ARG`/`ENV`/katmanlarda secret yok (build secret mount kullan); checksum olmadan `curl | sh` yok; minimum paket; mümkünse çalışma zamanında SSH veya shell yok; salt okunur dosya sistemiyle uyumlu.
6. Tekrarlanabilirlik: sabitlenmiş paket sürümleri veya lockfile; deterministik kurulum komutları (`npm ci`, `pip install --require-hashes`, kilitli restore); çok mimarili ise açık platform.
7. Çalışma zamanı doğruluğu: sinyallerin sürece ulaşması için exec formunda `ENTRYPOINT`/`CMD`; doğru PID 1 yönetimi; `EXPOSE` ve `WORKDIR` tanımlı; `HEALTHCHECK` yalnızca orkestratör probe yapmıyorsa.
8. Metadata: kaynak, revizyon ve sürüm için OCI etiketleri.
9. Her bulguyu Kritik/Yüksek/Orta/Düşük olarak derecelendir ve düzeltilmiş kod parçası ver; değişiklikler kapsamlıysa gözden geçirilmiş Dockerfile'ın tamamını sun.
10. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa çalışma zamanı yapılandırması için `kubernetes-manifest-review` veya base image ve paket bulguları için `dependency-vulnerability-review` öner.

## Çıktı formatı
````markdown
# Dockerfile İncelemesi: <imaj/servis>
Özet: <2-3 satır: ana riskler, beklenen boyut/güvenlik etkisi (nitel)>
| # | Önem | Kategori | Satır | Bulgu | Düzeltme |
## Gözden Geçirilmiş Dockerfile
```dockerfile
...
```
## Açık Sorular / Varsayımlar
````

## Kalite kontrol listesi
- [ ] Her bulgu girdideki bir satıra veya talimata referans veriyor.
- [ ] Son aşama root olmayan kullanıcıyla çalışıyor ve derleme aracı ya da secret içermiyor.
- [ ] Base image sabitlenmiş; `latest` yok.
- [ ] Gözden geçirilmiş dosya sözdizimsel olarak geçerli ve orijinal davranışı koruyor.
- [ ] Boyut veya CVE sayısı uydurulmadı; veri verilmediyse beklenen etkiler nitel.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bağımlılıkları kurmadan önce tüm bağlamı kopyalamak; her değişiklikte önbellek bozulur. Önce manifestleri kopyala.
- Bir secret'ı sonraki katmanda silmek; geçmişte kalmaya devam eder. Build secret mount kullan.
- glibc'ye bağımlı runtime'larda körü körüne alpine'e geçmek. Uyumluluğu doğrula veya slim/distroless kullan.

## Örnek
Girdi: `FROM node:latest`, `COPY . .`, `RUN npm install`, `CMD npm start`.

Çıktıdan bir bölüm:
| # | Önem | Kategori | Satır | Bulgu | Düzeltme |
|---|---|---|---|---|---|
| 1 | Yüksek | Tekrarlanabilirlik | 1 | Sabitlenmemiş `latest` tam imaj | `node:<major>-slim@sha256:...` ile sabitle |
| 2 | Yüksek | Güvenlik | – | Root olarak çalışıyor | Son aşamaya `USER node` ekle |
| 3 | Orta | Önbellek | 2-3 | Kaynak kurulumdan önce kopyalanıyor | `package*.json` kopyala, `npm ci --omit=dev`, sonra kaynağı kopyala |
| 4 | Orta | Çalışma zamanı | 4 | npm üzerinden shell formunda CMD, sinyaller kayboluyor | `CMD ["node","server.js"]` |
