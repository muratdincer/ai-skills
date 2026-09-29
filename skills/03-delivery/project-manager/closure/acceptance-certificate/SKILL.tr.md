---
name: acceptance-certificate
description: "Neyin teslim edildiğini, kararlaştırılan kabul kriterlerini ve her birinin kanıtını, açık hataları ve kabul edilen sapmaları, koşullu kabul şartlarını ve yetkili tarafların onaylarını kayıt altına alan bir teslimat kabul belgesi hazırlar. Bir teslimatın, kilometre taşının veya fazın müşteri, sponsor ya da iş sahibi tarafından resmî olarak kabul edilmesi gerektiğinde, bir kilometre taşı ödemesinden önce veya bir tedarikçi teslimatının kayıtlı olarak kabul ya da reddedilmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: closure
  title: "Teslimat kabul belgesi"
  related: "acceptance-criteria, uat-plan, statement-of-work, project-closure-report, change-control"
  prompt: "2. kilometre taşı (raporlama modülü) için kabul belgesini hazırla. UAT tamamlandı, 3 küçük hata açık; müşteri koşullu imzalamak istiyor."
---

# Teslimat Kabul Belgesi

## Amaç
Belirli bir teslimatın kararlaştırılan kabul kriterlerini karşıladığına ya da hangi koşullarla kabul edildiğine dair açık ve imzalı bir kayıt oluşturmak. Böylece ödeme, garanti ve devir, net ve denetlenebilir bir karara dayanır.

## Ne zaman kullanılır
- Bir teslimat, kilometre taşı veya faz tamamlandığında ve resmî kabul gerektiğinde.
- Sözleşme ödemeyi veya garanti başlangıcını kabule bağladığında.
- Müşteri koşullu kabul veya ret vermek istediğinde ve bunun kaydedilmesi gerektiğinde.

## Ne zaman kullanılmaz
- Kabul kriterlerinin kendisi tanımlanacaksa `acceptance-criteria` ya da `statement-of-work` üzerinden SOW kullanılır.
- Kullanıcı kabul testi planlanacak veya yürütülecekse `uat-plan` kullanılır.
- Projenin tamamı kapatılacaksa `project-closure-report` kullanılır.

## Girdiler
Zorunlu:
- Teslimat (ad, sürüm, kapsam) ve kararlaştırılan kabul kriterleri ya da kaynakları (SOW, sözleşme, gereksinimler).
- Karşılandığının kanıtı (test sonuçları, UAT onayı, gözden geçirme kayıtları, demolar).

İsteğe bağlı, kaliteyi artırır:
- Açık hata listesi, sapmalar veya muafiyetler, sözleşmedeki kabul süresi ve zımni kabul maddeleri.
- Yetkili imzacıların adları ve rolleri.

Kabul kriterleri veya kanıt yoksa iste. Kanıtı olmayan bir kriteri asla karşılandı olarak işaretleme.

## Süreç
1. Teslimatı kesin olarak tanımla: ad, sürüm veya derleme, teslim tarihi, kapsam referansı ve açıkça hariç tutulanlar.
2. Kaynaktaki her kararlaştırılmış kabul kriterini anlamını değiştirmeden listele.
3. Her kritere kanıt eşle ve sonucu kaydet: karşılandı, sapmayla karşılandı, karşılanmadı, test edilmedi. Kanıt referansını göster.
4. Açık hataları önem derecesi ve kararlaştırılan düzeltme tarihleriyle listele; sözleşmedeki kabul eşikleriyle karşılaştır (ör. açık kritik veya yüksek hata olmaması).
5. Kabul eden tarafın bilerek kabul ettiği sapmaları ve muafiyetleri, gerekçesi ve onaylayanıyla kaydet.
6. Önerilen kararı belirle: kabul, koşullu kabul (koşullar, sahipler ve son tarihlerle) ya da ret (kriterlere bağlı gerekçelerle).
7. Sözleşme mekaniklerini kontrol et: kabul süresi, zımni kabul maddeleri, ödeme ve garanti başlangıcına etkisi; bilinmeyenleri `[TBD – sözleşmeyi kontrol et]` olarak işaretle.
8. İmzacıların kabul yetkisi olduğunu doğrula; bilinmiyorsa `[VARSAYIM]` olarak işaretle ve açık soru olarak listele.
9. Her iki taraf için imza satırları ve dağıtım listesiyle belgeyi üret.
10. Kullanıcının hedefi devam ediyorsa koşullar kapsamı değiştiriyorsa `change-control`, tüm teslimatlar kabul edildiğinde `project-closure-report` öner.

## Çıktı formatı
```markdown
# Kabul Belgesi: <teslimat> – <sürüm>
| Alan | Değer |
|---|---|
| Proje / sözleşme ref | <...> |
| Teslimat ve kapsam ref | <...> |
| Teslim tarihi | <tarih> |
| Bu kabulün dışında kalanlar | <...> |
| Karar | Kabul / Koşullu kabul / Ret |

## Kabul Kriterleri ve Kanıtlar
| # | Kriter (kaynak ref) | Sonuç | Kanıt |
## Açık Hatalar
| No | Önem | Açıklama | Düzeltme tarihi | Kabulü engelliyor mu? |
## Kabul Edilen Sapmalar / Muafiyetler
| Sapma | Gerekçe | Onaylayan |
## Koşullar (koşullu ise)
| Koşul | Sahip | Son tarih | Karşılanmazsa sonucu |
## Sözleşmesel Etkiler
- Ödeme kilometre taşı: ... | Garanti başlangıcı: ... | Kabul süresi: ...
## Onay
| Taraf | Ad | Rol | İmza | Tarih |
```

## Kalite kontrol listesi
- [ ] Kararlaştırılan her kriter sonuç ve kanıt referansıyla yer alıyor.
- [ ] Teslimatın sürümü ve hariç tutulanlar açık.
- [ ] Koşulların sahibi, son tarihi ve sonucu var.
- [ ] Açık hatalar sözleşmedeki eşiklerle karşılaştırıldı.
- [ ] İmzacıların yetkisi teyit edildi ya da işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Belirsiz açık noktalarla "kabul" imzalamak; bunlar anlaşmazlığa dönüşür. Açık koşullarla koşullu kabul kullan.
- Kabul anında yeni kriterler eklemek. Yeni beklentiler `change-control` üzerinden geçer.
- Sözleşmedeki zımni kabul sürelerini kaçırmak; teslimat kendiliğinden kabul edilmiş sayılır.

## Örnek
Girdi: "2. kilometre taşı raporlama modülü v1.4; UAT 3 küçük hata dışında geçti; müşteri koşullu imza istiyor."

Çıktıdan bir bölüm:
- Karar: Koşullu kabul.
- Kriter 4 "Aylık satış raporu muhasebe toplamlarıyla tutuyor" – Karşılandı – UAT senaryosu R-12 kanıtı `[ref]`.
- Koşul: D-31, D-33, D-34 hatalarının `[tarih]`e kadar düzeltilmesi – Sahip tedarikçi lideri – karşılanmazsa 2b ödemesi bekletilir `[sözleşmeyle teyit et]`.
