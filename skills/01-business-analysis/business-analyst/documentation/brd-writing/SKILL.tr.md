---
description: "İş problemini, ölçülebilir başarı kriterli hedefleri, kapsamı, paydaşları, üst düzey iş gereksinimlerini, iş kurallarını, kısıtları, varsayımları ve riskleri herhangi bir çözüm tasarımından bağımsız olarak ortaya koyan bir İş Gereksinimleri Dokümanı (BRD) yazar. Bir girişimin çözüm veya fonksiyonel tasarımdan önce uzlaşılmış bir iş temeline ihtiyacı olduğunda ya da bir proje veya değişiklik için 'BRD yaz' dendiğinde kullanılır."
related: "request-intake-document, frd-writing, stakeholder-identification, requirements-review-checklist, requirements-sign-off"
prompt: "Manuel tedarikçi kaydını (e-posta ve Excel) self-servis bir süreçle değiştirmek için BRD yaz; çalıştay notları ekte."
---

# İş Gereksinimleri Dokümanı (BRD) Yazma

## Amaç
Girişimin neden var olduğunu, işin neye ihtiyaç duyduğunu ve başarının nasıl değerlendirileceğini tek bir uzlaşılmış metinde toplamak. Böylece çözüm tasarımı, tahmin ve onay kişisel beklentilere değil, ortak bir temele dayanır.

## Ne zaman kullanılır
- Bir girişim veya büyük bir değişiklik talep aşamasını geçmiş ve tasarımdan önce iş temeline ihtiyaç duyuyorsa.
- Birden çok departmanın farklı beklentileri tek bir dokümanda uzlaştırılacaksa.
- Bir sponsor, portföy kurulu veya tedarikçi çözümden bağımsız bir ihtiyaç tanımı istiyorsa.

## Ne zaman kullanılmaz
- Sistem davranışı, ekranlar ve arayüzler tanımlanacaksa `frd-writing` veya `srs-writing` kullanılır.
- Talep hâlâ ham ve nitelendirilmemişse `request-intake-document` kullanılır.
- Ekip bir özellik için ürün düzeyinde bir dokümanla çalışıyorsa `prd-writing` kullanılır.

## Girdiler
Zorunlu:
- Kaynak materyal: talep alma dokümanı, notlar, çalıştay veya görüşme çıktıları ya da girişimin tarifi.
- Sponsor veya karar verici (en azından rolü).

İsteğe bağlı, kaliteyi artırır:
- Desteklediği stratejik hedefler veya OKR'ler; as-is süreç tarifi; bilinen kısıtlar (bütçe aralığı, tarihler, mevzuat).
- Kurumun BRD şablonu veya zorunlu bölümleri.

Kaynak materyal yoksa iste. Sponsor bilinmiyorsa `[BİLİNMİYOR]` ile devam et ve bunu ilk açık soru yap. Bir seferde en fazla 5 engelleyici soru sor.

## Süreç
1. Kaynaklardan çıkar: problem, itici güçler, hedefler, paydaşlar, ihtiyaçlar, kurallar, kısıtlar. Çıkarım olan her şeyi `[VARSAYIM]` olarak etiketle.
2. İş problemini veya fırsatını ve kanıtını (hacimler, maliyet, olaylar) yalnızca verildiği kadarıyla yaz; eksik kanıtı `[TBD]` olarak işaretle.
3. 2-5 iş hedefi tanımla; her birine ölçülebilir başarı kriteri ver: metrik, başlangıç değeri, hedef, tarih. Başlangıç değeri asla uydurma.
4. Kapsamı belirle: kapsam içi, kapsam dışı ve gelecek değerlendirmeler. Organizasyon birimlerini, süreçleri, ürünleri ve kanalları adıyla yaz.
5. Paydaşları rolü, ilgisi ve onlardan beklenenle (onay, girdi, kabul) listele.
6. Mevcut durumu kısaca ve hedeflenen iş yeteneğini ekran veya teknoloji dayatmadan anlat.
7. Üst düzey iş gereksinimlerini "İşin ... yapabilmesi gerekir" cümleleriyle yaz; her birine ID, kaynak, öncelik ve bir hedefe bağlantı ver. Çözümden bağımsız tut.
8. İş kurallarını, yasal yükümlülükleri (ör. KVKK/GDPR, sektör kuralları), veri ve raporlama ihtiyaçlarını ve iş düzeyindeki kalite beklentilerini kaydet.
9. Kısıtları, bağımlılıkları, varsayımları ve riskleri, biliniyorsa sahibiyle birlikte kaydet.
10. Geçiş ihtiyaçlarını belirt: organizasyonel değişim, eğitim, veri taşıma, paralel çalışma.
11. Açık soruları ve onay bloğunu (rol, karar, tarih boş bırakılır) ekle.
12. Hedef devam ediyorsa sistem davranışı için `frd-writing`, onaydan önce `requirements-review-checklist`, onay almak için `requirements-sign-off` öner.

## Çıktı formatı
```markdown
# İş Gereksinimleri Dokümanı: <girişim>
Sürüm: <x.y> · Durum: Taslak · Sponsor: <rol/ad veya [BİLİNMİYOR]> · Yazan: <rol>

## 1. Yönetici Özeti
## 2. İş Problemi / Fırsat ve Kanıt
## 3. Hedefler ve Başarı Kriterleri
| ID | Hedef | Metrik | Başlangıç | Hedef değer | Tarih |
## 4. Kapsam (İçi / Dışı / Gelecek)
## 5. Paydaşlar
| Paydaş | Rol | İlgi | Ondan beklenen |
## 6. Mevcut Durum Özeti ve Hedeflenen İş Yeteneği
## 7. İş Gereksinimleri
| ID | Gereksinim ("İşin … yapabilmesi gerekir") | Hedef | Öncelik | Kaynak |
## 8. İş Kuralları ve Yasal Yükümlülükler
## 9. Veri, Raporlama ve Kalite Beklentileri
## 10. Kısıtlar, Bağımlılıklar, Varsayımlar, Riskler
## 11. Geçiş İhtiyaçları
## 12. Açık Sorular
## 13. Onay
| Rol | Ad | Karar | Tarih |
```

## Kalite kontrol listesi
- [ ] Her iş gereksinimi en az bir hedefe bağlı, her hedefin ölçülebilir bir kriteri var.
- [ ] Hiçbir gereksinim ekran, teknoloji veya tedarikçi dayatmıyor.
- [ ] Kapsam dışı maddeler açıkça yazılı.
- [ ] Başlangıç değerleri, rakamlar ve tarihler kaynaklardan geliyor ya da `[TBD]` / `[VARSAYIM]` olarak işaretli.
- [ ] Yasal ve kişisel veri koruma yükümlülükleri değerlendirildi; yazıldı veya gerekçesiyle hariç tutuldu.
- [ ] Her riskin ve açık sorunun bir sahibi var ya da `[BİLİNMİYOR]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kılık değiştirmiş bir FRD yazmak. Alan, düğme veya API adı geçiyorsa fonksiyonel şartnameye aittir.
- Başlangıç değeri olmayan hedefler. "Kayıt süresini azaltmak" test edilemez; başlangıcı `[TBD]` olarak kaydet ve kimin ölçeceğini yaz.
- "Hiçbir şey yapmama" seçeneğini atlamak. Harekete geçilmezse ne olacağını yaz; önceliği bu sabitler.

## Örnek
Girdi: "Tedarikçi kaydı e-posta ve Excel ile haftalar sürüyor; satın alma self-servis istiyor; denetim eksik vergi levhaları buldu."

Çıktıdan bir bölüm:
| ID | Hedef | Metrik | Başlangıç | Hedef değer | Tarih |
|---|---|---|---|---|---|
| HDF-1 | Tedarikçi kaydını kısaltmak | Talepten aktif tedarikçiye medyan gün | [TBD – satın alma ölçecek] | [TBD] | [TBD] |
| HDF-2 | Tedarikçi dokümanlarıyla ilgili denetim bulgusunu kapatmak | Geçerli vergi levhası olmayan aktif tedarikçi sayısı | Denetim bulgusu (adet [TBD]) | 0 | Sonraki denetim |

İG-04: İşin, zorunlu dokümanlar doğrulanmadan bir tedarikçinin aktifleştirilmesini engelleyebilmesi gerekir. (HDF-2, Must, denetim raporu)
