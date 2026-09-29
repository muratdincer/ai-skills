---
name: raci-matrix
description: "Her aktivite veya çıktı için Sorumlu (R), Hesap Veren (A), Danışılan (C) ve Bilgilendirilen (I) rollerini atayan bir RACI matrisi oluşturur ve doğrular (tam bir A, en az bir R, aşırı yüklü rol yok, boş satır yok). Sorumluluklar belirsiz olduğunda, işler ekipler arasında kaldığında veya bir proje, süreç ya da analiz aktivitesi için 'kim neyin sahibi?' sorusu geldiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: stakeholders
  title: "RACI matrisi"
  related: "stakeholder-identification, stakeholder-map, communication-plan, project-charter, role-definition"
  prompt: "Ödeme altyapısı entegrasyonumuzun gereksinim fazı için RACI oluştur: iş analisti, PO, mimar, geliştirme lideri, QA, güvenlik, tedarikçi."
---

# RACI Matrisi

## Amaç
Her aktivitede işi kimin yaptığını, kimin sahiplendiğini, kime danışıldığını ve kimin bilgilendirildiğini açık hale getirerek sahiplik belirsizliğini ortadan kaldırmak. Böylece kararlar ve devir teslimler takılmaz.

## Ne zaman kullanılır
- Bir proje, faz veya süreçte birden çok rol var ve devir teslimler belirsizse.
- İşler sürekli ekipler arasında kalıyor ya da iki kişi aynı kararın sahibi olduğunu düşünüyorsa.
- Analiz, onay veya sürüm aktiviteleri için yönetişim kurulurken.

## Ne zaman kullanılmaz
- Paydaşların kim olduğu henüz bilinmiyorsa `stakeholder-identification` kullanılır.
- Etkiye göre bir katılım planı gerekiyorsa `stakeholder-map` kullanılır.
- Aktivite değil, pozisyon düzeyinde sorumluluklar gerekiyorsa `role-definition` kullanılır.

## Girdiler
Zorunlu:
- Kapsanacak aktiviteler, çıktılar veya kararlar (ya da bunların türetilebileceği kapsam).
- Dahil olan roller veya ekipler.

İsteğe bağlı, kaliteyi artırır:
- Mevcut yönetişim kuralları, onay politikaları, organizasyonel kısıtlar.
- Bilinen sorunlar ("test verisini kimse onaylamıyor", "mimari kararlar gecikiyor").

Aktiviteler yoksa kapsamdan taslak bir liste türet ve teyit için `[VARSAYIM]` olarak işaretle. Roller yoksa sor.

## Süreç
1. Aktiviteleri tutarlı bir ayrıntı düzeyinde listele: fiil + nesne ("BRD'yi onayla", "API sözleşmesini tanımla"), 8-25 satır. Sahibi farklı olan aktiviteleri böl.
2. Rolleri sütun olarak yaz (kişi değil rol; isimler açıklama bölümüne eklenebilir).
3. Her satıra tam olarak bir A ata: sonuçtan hesap veren ve evet/hayır diyebilen kişi.
4. En az bir R ata: işi yapan. Küçük işlerde A ve R aynı rol olabilir.
5. C'yi yalnızca iş tamamlanmadan önce girdi gerekiyorsa (çift yönlü), I'yı tamamlandıktan sonra haber vermek yetiyorsa (tek yönlü) ekle.
6. Doğrula: A'sı veya R'si olmayan satırlar; birden çok A'lı satırlar; çok sayıda A'sı olan sütunlar (darboğaz); hiç R veya A'sı olmayan sütunlar (bu rol neden burada?); aşırı C içeren satırlar (yavaş kararlar).
7. Eskalasyon yolu gerektiren kararları vurgula ve eskalasyon rolünü belirt.
8. Sahipliği tartışmalı veya bilinmeyen noktaları açık konu olarak listele; tahminle çözme. Kullanıcının söylemediği, senin çıkardığın her atamayı `[VARSAYIM]` olarak işaretle.
9. Hedef devam ediyorsa C ve I atamalarını iletişim ritmine çevirmek için `communication-plan`, iletişim stratejisi hâlâ eksikse `stakeholder-map` öner.

## Çıktı formatı
```markdown
# RACI: <kapsam>
Açıklama: R = Sorumlu, A = Hesap Veren, C = Danışılan, I = Bilgilendirilen

| Aktivite / çıktı | <Rol 1> | <Rol 2> | <Rol 3> | ... |
|---|---|---|---|---|
| ... | A/R | C | I | |

## Doğrulama bulguları
- ...

## Eskalasyon
- <karar türü> → <rol>

## Açık sahiplik soruları
- ...
```

## Kalite kontrol listesi
- [ ] Her satırda tam olarak bir A ve en az bir R var.
- [ ] Aktiviteler fiil + nesne biçiminde ve tutarlı düzeyde.
- [ ] Hiçbir rol darboğaz olacak kadar çok satırda A değil ya da bu durum işaretlendi.
- [ ] C idareli ve yalnızca gerçekten girdi gerektiğinde kullanıldı.
- [ ] Tartışmalı sahiplik sessizce atanmadı, açık soru olarak listelendi.
- [ ] Uydurma isimler değil roller kullanıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Bir kurulu Hesap Veren yapmak. Tek bir rol belirle; kurul Danışılan olabilir.
- Nezaketen herkesi Danışılan yapmak. Her C bir bekleme durumu ekler.
- RACI'yi tek başına hazırlamak. Listelenen rollerle birlikte gözden geçir; yoksa matris anlaşmaları değil varsayımları belgeler.

## Örnek
Girdi: "Ödeme altyapısı entegrasyonunun gereksinim fazı; roller: iş analisti, PO, mimar, geliştirme lideri, QA, güvenlik, tedarikçi."

Çıktıdan bir bölüm:
| Aktivite | İA | PO | Mimar | Geliştirme lideri | QA | Güvenlik | Tedarikçi |
|---|---|---|---|---|---|---|---|
| İş gereksinimlerini topla | R | A | C | I | I | | |
| API sözleşmesini tanımla | C | I | A | R | C | C | C |
| Güvenlik gereksinimlerini onayla | C | I | C | | | A/R | I |

Doğrulama: Mimar 10 satırın 4'ünde A – kapasiteyi teyit et veya devret.
