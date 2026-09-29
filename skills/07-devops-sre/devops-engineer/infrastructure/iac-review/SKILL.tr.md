---
description: "Kod olarak altyapıyı (Terraform/OpenTofu, Bicep, CloudFormation, Pulumi, Ansible vb.) ve plan çıktısını güvenlik yanlış yapılandırmaları, state ve sapma riskleri, yıkıcı değişiklikler, modülerlik, adlandırma/etiketleme ve maliyet açısından inceler. Bir IaC pull request'i veya planı incelenecekken, paylaşımlı ya da üretim altyapısına değişiklik uygulanmadan önce veya mevcut bir IaC kod tabanı denetlenirken kullanılır."
related: "secrets-management-plan, finops-review, environment-strategy, threat-model, pipeline-design"
prompt: "Bu Terraform modülünü ve plan çıktısını incele. Yeni servisimiz için bir storage bucket, bir veritabanı ve bir VPC oluşturuyor."
---

# Kod Olarak Altyapı İncelemesi

## Amaç
Güvensiz, yıkıcı veya sürdürülemez altyapı değişikliklerini uygulanmadan önce yakalamak ve kod tabanını daha modüler ve tutarlı bırakmak.

## Ne zaman kullanılır
- Bir IaC pull request'i veya plan/what-if çıktısı incelemeye geldiğinde.
- Değişiklikler üretime veya paylaşımlı altyapıya uygulanmak üzereyken.
- Mevcut bir IaC repository'si güvenlik ve yapı açısından denetlenirken.

## Ne zaman kullanılmaz
- Konu Kubernetes iş yükü YAML'ıysa `kubernetes-manifest-review` kullanılır.
- Soru genel secret yönetimi tasarımıysa `secrets-management-plan` kullanılır.
- Asıl endişe kod değil harcamaysa `finops-review` kullanılır.

## Girdiler
Zorunlu:
- İncelenecek IaC kodu veya diff.

İsteğe bağlı, kaliteyi artırır:
- Plan/what-if çıktısı (değişiklik incelemelerinde şiddetle önerilir).
- Hedef ortam, state backend kurulumu, modül registry'si, kurumsal politikalar (etiketleme, bölgeler, şifreleme, ağ).
- Kullanılan uyum temel çizgisi (ör. CIS benchmark'ları).

Kod veya diff yoksa iste. Plan çıktısı yoksa statik incele ve yıkıcı değişikliklerin doğrulanamadığını belirt.

## Süreç
1. Amacı anla: değişiklik hangi ortamda neyi oluşturacak, değiştirecek veya silecek.
2. Plan analizi: her destroy ve replace aksiyonunu listele; durum tutan kaynakların (veritabanları, diskler, bucket'lar, DNS zone'ları, key vault'lar) yeniden oluşturulmasını, bilinçli değilse engelleyici olarak işaretle; `prevent_destroy`/silme korumasını kontrol et.
3. Güvenlik: genel erişime açıklık (0.0.0.0/0 ingress, public bucket'lar, public IP'ler), durağan ve aktarımdaki veride şifreleme, politika gerektiriyorsa müşteri yönetimli anahtarlar, en az yetkili IAM (joker aksiyon/kaynak yok), loglama açık, private endpoint'ler, kodda, değişkenlerde veya state çıktılarında secret yok (çıktıları sensitive işaretle).
4. State ve sapma: kilitli ve şifreli uzak state, ortam/etki alanı bazında ayrılmış state, manuel değişiklik yok, mevcut kaynaklar için yeniden oluşturma yerine import.
5. Sürümleme: provider ve modül sürümleri kısıtlarla sabitlenmiş; lock dosyası commit edilmiş.
6. Yapı: net girdi/çıktıları olan yeniden kullanılabilir modüller, ortam başına kopyala-yapıştır yok, ortam farkları değişkenlerde, makul varsayılanlar, girdilerde doğrulama kuralları.
7. Adlandırma ve etiketleme: kurum standardı, zorunlu etiketler (sahip, masraf merkezi, ortam, veri sınıflandırması).
8. Güvenilirlik ve maliyet: gerekiyorsa zone yedekliliği, yedekler ve saklama, doğru boyutlu SKU'lar, yaşam döngüsü kuralları; maliyetli seçimleri nitel olarak işaretle.
9. Hat: pull request'te plan, apply yalnızca hattan ve onayla, policy-as-code kontrolleri.
10. Bulguları derecelendir, kod düzeltmeleri öner.

## Çıktı formatı
```markdown
# IaC İncelemesi: <modül / değişiklik>
Karar: Onay / Değişikliklerle onay / Engelle
## Yıkıcı veya Riskli Plan Aksiyonları
| Kaynak | Aksiyon | Durum tutuyor mu? | Bilinçli mi? | Gerekli önlem |
## Bulgular
| # | Önem | Kategori | Dosya:satır / kaynak | Bulgu | Düzeltme |
## Önerilen Kod Değişiklikleri
## Açık Sorular / Varsayımlar
```

## Kalite kontrol listesi
- [ ] Durum tutan kaynaklardaki tüm destroy/replace aksiyonları listelendi ve çözüldü.
- [ ] Açıklanmamış genel erişim veya joker IAM kalmadı.
- [ ] Secret'lar kodda, değişken varsayılanlarında veya maskelenmemiş çıktılarda yok.
- [ ] Provider/modül sürümleri sabitlenmiş.
- [ ] Plan çıktısı yoksa inceleme bunu belirtiyor.

## Sık yapılan hatalar
- Bir kaynağın veya modül adresinin adını değiştirip veritabanının silinip yeniden oluşturulmasına yol açmak. moved/import blokları kullan.
- Yalnızca diff'i inceleyip değişen modül varsayılanlarının etkisini kaçırmak. Planı kontrol et.
- Tüm ortamlar için tek state; dev'deki bir değişiklik üretimi kilitleyebilir veya bozabilir. State'i ortam ve alan bazında böl.

## Örnek
Girdi: Terraform diff'i `<provider>_db_instance.main` adını `<provider>_db_instance.orders` yapıyor; plan `-/+ destroy and then create replacement` gösteriyor.

Çıktıdan bir bölüm:
| Kaynak | Aksiyon | Durum tutuyor mu? | Bilinçli mi? | Gerekli önlem |
|---|---|---|---|---|
| db instance orders | replace | Evet | Hayır (yalnızca ad değişikliği) | `moved` bloğu ekle; silme korumasını aç; planı yeniden çalıştır |
Karar: Plan yeniden oluşturma göstermeyene kadar engelle.
