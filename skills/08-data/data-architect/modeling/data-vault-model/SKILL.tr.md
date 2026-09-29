---
name: data-vault-model
description: "Data Vault 2.0 modeli tasarlar: iş anahtarlarından hub'lar, ilişki ve işlemler için link'ler, kaynağa ve değişim hızına göre bölünmüş satellite'lar; hash key, load date, record source ve business vault yapıları (PIT, bridge, effectivity). Çok sayıda değişken kaynak üzerinde denetlenebilir, kaynakları entegre eden ham katman kurulurken ya da hub, link ve satellite istendiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 08-data
  role: data-architect
  area: modeling
  title: "Data Vault modeli tasarlama"
  related: "dimensional-model, logical-data-model, master-data-strategy, incremental-load-design, data-lineage-doc"
  prompt: "CRM, çekirdek bankacılık ve web müşteri edinim uygulamasından gelen müşteri ve sözleşme verisi için Data Vault tasarla."
---

# Data Vault Modeli Tasarlama

## Amaç
Tüm kaynak tarihçesini yalnızca ekleme (insert-only) yapılan, denetlenebilir bir biçimde tutan, kaynakları ortak iş anahtarları üzerinde birleştiren ve kaynak değişikliklerini minimum yeniden işle karşılayan bir entegrasyon katmanı oluşturmak. Böylece alt katmandaki mart'lar her an yeniden üretilebilir.

## Ne zaman kullanılır
- Birçok kaynak aynı iş kavramlarını tanımlıyor ve sık değişiyorsa.
- Geçmişteki herhangi bir durumun tam denetlenebilirliği ve yeniden üretilebilirliği gerekiyorsa (düzenlemeye tabi sektörler).
- Her kaynak değişikliğinde yeniden modelleme yapmadan, ölçekli paralel ve artımlı yükleme gerekiyorsa.

## Ne zaman kullanılmaz
- Küçük bir raporlama ihtiyacını tek kaynak besliyorsa doğrudan `dimensional-model` kullanılır.
- İhtiyaç operasyon için altın kayıt çözümlemesiyse `master-data-strategy` kullanılır.
- Operasyonel (OLTP) şema tasarlanıyorsa `logical-data-model` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki kaynak sistemler, varlıkları/tabloları ve taşıdıkları iş anahtarları.
- Temel iş kavramları (kavramsal model veya liste).

İsteğe bağlı:
- Kaynak bazında değişim sıklığı ve hacim, CDC imkânı, kaynaklar arası bilinen anahtar çakışmaları, alt katman mart gereksinimleri, gizlilik kısıtları (silme yükümlülükleri).

Bir kaynak için iş anahtarı belirlenemiyorsa sor; tahmini anahtar entegrasyonu bozar.

## Süreç
1. Kaynak tablolardan değil iş kavramlarından başla. Her kavram için kurum genelinde kullanılan iş anahtarını belirle (mümkünse kaynak vekil ID'leri değil).
2. Anahtar çakışmalarını çöz: kaynaklar aynı kavram için farklı anahtar kullanıyorsa, anahtar eşlemeli ortak hub (same-as link) ile anahtarda çakışma kodu/tenant ön eki arasında karar ver.
3. Hub'ları tanımla: normalize edilmiş iş anahtarı üzerinden hash key (trim, büyük harf, sabit ayraç, çakışma kodu), iş anahtarı sütunları, load date, record source.
4. Hub'lar arasındaki her ilişki veya işlem için, katılan tüm hub anahtarları üzerinden hash key'li link tanımla. Link'leri çoka çok tut; kardinaliteyi kodlama. Değişmeyen olaylar için tarihçesiz (transactional) link kullan.
5. Satellite'ları tanımla: kaynak sisteme, değişim hızına ve hassasiyete göre böl (silme/crypto-shredding için kişisel veriyi ayrı satellite'a koy). Değişiklik tespiti için hash diff, load date, record source ekle; link geçerliliği için effectivity satellite ekle.
6. Çok değerli nitelikleri (müşteri başına birden çok telefon) multi-active satellite ve alt sıra anahtarıyla yönet.
7. Teknik kuralları standartlaştır: hash algoritması ve girdi normalizasyonu, load date anlamı (varış zamanı mı uygulanma tarihi mi), ghost record, eksik referanslar için sıfır anahtarlar.
8. Türetilmiş mantık için business vault tasarla: hesaplanmış satellite'lar, same-as ve hiyerarşi link'leri, alt katman sorgularını verimli kılan PIT tabloları ve bridge'ler.
9. Yükleme örüntülerini belirt: hub ve link'lerde yoksa ekle, satellite'larda hash diff değiştiyse ekle; tüm yüklemeler idempotent ve katman içinde paralel.
10. Raw vault'u alt katman bilgi mart'larına eşle (PIT + satellite'lardan sanal boyut/olgular).
11. Her kaynak niteliğinin tam olarak bir satellite'a düştüğünü kontrol et; eşlenmemiş nitelikleri listele.
12. Her çıkarımı `[VARSAYIM]` olarak etiketle, desteklenmeyen maddeleri açık sorulara taşı. Hedef devam ediyorsa sonraki beceriyi öner: hub, link ve satellite yüklemesi için `incremental-load-design`, bilgi martları için `dimensional-model` veya `data-lineage-doc`.

## Çıktı formatı
```markdown
# Data Vault Modeli: <kapsam>
## Hub'lar
| Hub | İş anahtarı (normalize) | Çakışma yönetimi | Kaynaklar |
|---|---|---|---|

## Link'ler
| Link | Hub'lar | Tip (standart / tarihçesiz / same-as / hiyerarşi) | Sürücü anahtar (effectivity varsa) |
|---|---|---|---|

## Satellite'lar
| Satellite | Ebeveyn | Kaynak | Değişim hızı | Nitelikler | Hassas mı? | Multi-active mi? |
|---|---|---|---|---|---|---|

## Teknik Standartlar
- Hash: <algoritma>, girdi normalizasyonu: <kurallar>
- Load date: <anlam> | Record source: <format> | Sıfır/ghost anahtarlar: <...>

## Business Vault
- PIT: <hub + satellite'lar, anlık görüntü sıklığı>
- Bridge / hesaplanmış satellite'lar: <...>

## Alt Katman Eşlemesi
| Mart nesnesi | Kaynağı |
|---|---|

## Açık Sorular / Varsayımlar
- ...
```

## Kalite kontrol listesi
- [ ] Her hub gerçek bir iş anahtarına dayanıyor ve anahtar çakışmaları açıkça çözüldü.
- [ ] Link'ler tanımlayıcı nitelik taşımıyor; ilişkiler hub'lara gömülmedi.
- [ ] Satellite'lar kaynak ve değişim hızına göre bölündü; kişisel veri ayrıştırıldı.
- [ ] Hash ve load date kuralları bir kez tanımlandı ve her yerde uygulanıyor.
- [ ] Yüklemeler yalnızca ekleme yapıyor ve idempotent.
- [ ] Her kaynak niteliği tam olarak bir satellite'a eşlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kaynak sistem vault'u: teknik ID'lerle kaynak tablo başına bir hub; hiçbir şeyi entegre etmez. İş kavramları etrafında modelle.
- İş kurallarını raw vault'a koymak. Raw vault kaynağa sadık kalsın; kuralları business vault'ta uygula.
- BI için doğrudan raw vault'u sorgulamak. PIT/bridge yapıları ve mart'lar sağla.
- Insert-only modelde silme yükümlülüklerini yok saymak. Kişisel veriyi silinebilir veya parçalanabilir olacak şekilde ayrıştır.

## Örnek
Girdi: "Müşteri CRM'den (CRM_ID), çekirdek bankacılıktan (müşteri numarası) ve web müşteri ediniminden (e-posta) geliyor."

Çıktıdan bir bölüm:
- Hub Müşteri: iş anahtarı = çekirdek bankacılık müşteri numarası; same-as link CRM_ID ve edinim e-postasını buna eşler.
- Satellite'lar: Sat Müşteri CRM (haftalık değişim), Sat Müşteri Core (günlük), Sat Müşteri PII (ad, TC kimlik no, iletişim; silme için ayrık).
- Link Müşteri-Sözleşme, effectivity satellite ile; sürücü anahtar Sözleşme.
