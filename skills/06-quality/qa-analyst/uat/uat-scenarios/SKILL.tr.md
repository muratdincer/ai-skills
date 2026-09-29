---
name: uat-scenarios
description: "Ekranlar ve tıklamalar yerine gerçek roller, iş olayları ve sonuçlar üzerine kurulu, iş dilinde uçtan uca kullanıcı kabul senaryoları yazar; her senaryoda gerçekçi veri, iş tarafının doğrulayabileceği kontrol noktaları ve geçme kriteri bulunur. İş kullanıcılarının UAT'de koşacağı senaryolar gerektiğinde, gereksinimler veya süreçler kabul akışlarına dönüştürülecekken ya da mevcut UAT metinleri teknik test case gibi okunduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 06-quality
  role: qa-analyst
  area: uat
  title: "Kabul testi senaryoları"
  related: "uat-plan, test-scenarios-from-requirements, to-be-process, acceptance-criteria, test-data-design"
  prompt: "İade süreci için UAT senaryoları yaz: mağaza personeli, depo ve finans yeni iade akışını uçtan uca test edecek."
---

# Kabul Testi Senaryoları

## Amaç
İş kullanıcılarına gerçekte nasıl çalıştıklarını yansıtan senaryolar vermek. Böylece kabul testleri çözümün roller ve sistemler boyunca gerçek iş sonuçlarını desteklediğini kanıtlar ve sonuçlar teknik bilgi gerekmeden değerlendirilebilir.

## Ne zaman kullanılır
- Bir UAT penceresi planlandığında ve iş tarafı testçilerinin koşacakları somut bir şeye ihtiyacı olduğunda.
- Gereksinimler, user story'ler veya bir hedef süreç (to-be) mevcutsa ve kabul akışlarına dönüştürülmesi gerektiğinde.
- Mevcut UAT metinleri, iş kullanıcılarının izlemekte ve değerlendirmekte zorlandığı tıklama düzeyinde test case'ler olduğunda.

## Ne zaman kullanılmaz
- UAT'nin kendisini organize etmek (kişiler, takvim, onay) gerekiyorsa `uat-plan` kullanılır.
- QA için adım düzeyinde ayrıntılı sistem test case'leri gerekiyorsa `test-case-writing` kullanılır.
- Sistem testi için geniş fonksiyonel senaryo kapsamı gerekiyorsa `test-scenarios-from-requirements` kullanılır.

## Girdiler
Zorunlu:
- Kapsamdaki iş süreci, gereksinimler veya story'ler.
- Sürece katılan roller.

İsteğe bağlı, kaliteyi artırır:
- Hedef süreç modeli, iş kuralları, bilinen istisnalar, gerçek hacimler ve takvim olayları (ay sonu, kampanyalar).
- Rol bazında mevcut test verisi ve hesaplar.

Süreç veya roller yoksa her seferinde tek bir odaklı soruyla iste. Çıkarımla belirlediğin her iş kuralını `[VARSAYIM]` olarak işaretle ve süreç sahibiyle teyit et.

## Süreç
1. Süreci başlatan iş olaylarını (müşteri bir ürünü iade eder, ay sonu kapanışı) ve her birinin üretmesi gereken iş sonucunu listele.
2. Her olay için tetikleyiciden iş sonucuna kadar roller ve sistemler boyunca ilerleyen bir ana senaryoyu kullanıcıların kendi sözcükleriyle hikâye olarak yaz.
3. Gerçek operasyonda önemli olan iş varyantlarını ekle: istisnalar (hasarlı ürün, fişsiz iade), onay ve retler, iptaller, düzeltmeler, dönem sınırları, yüksek hacimli günler.
4. Kabulün bunlara bağlı olduğu yerlerde rol ve yetki kontrollerini ekle (mağaza görevlisi limit üstü iadeyi onaylayamaz).
5. Her senaryo için maskelenmiş veya sentetik kayıtlarla gerçekçi veri tanımla (müşteri tipi, ürün, tutar, tarihler); gerçek kişiler yerine adlandırılmış veri setlerine atıf yap.
6. İş kullanıcısının kendisinin doğrulayabileceği kontrol noktaları yaz: üretilen belge, değişen bakiye, görünen durum, alınan bildirim, rapordaki rakam. Veritabanı veya log erişimi gerektiren kontrollerden kaçın.
7. Her senaryonun geçme kriterini ve neyin işi durduran hata, neyin kozmetik sorun sayılacağını belirt.
8. Her senaryoyu kapsadığı gereksinimlere veya süreç adımlarına eşle; kapsanmayan adımları boşluk olarak işaretle.
9. Senaryoları iş kritikliğine ve bağımlılığa göre sırala (iade için önce bir satış olmalı) ve koşum için rol ve gün bazında grupla.
10. Kullanıcı devam ederse koşumu takvimlemek için `uat-plan`, veri setleri için `test-data-design`, bir boşluk eksik kuralları ortaya çıkarıyorsa `acceptance-criteria` öner.

## Çıktı formatı
```markdown
# UAT Senaryoları: <süreç/sürüm>
| No | Senaryo | Roller | Öncelik | Kapsadığı |
|---|---|---|---|---|

## UAT-<nn>: <iş dilinde başlık>
- İş olayı: ...
- Roller: ...
- Ön koşullar ve veri: <veri seti adı, anahtar değerler>
- Akış:
  1. <rol> <iş aksiyonu yapar> → kontrol noktası: <görmesi/alması gereken>
  2. ...
- Beklenen iş sonucu: ...
- Geçme kriteri: ...
- Sonuç: Geçti / Kaldı / Bloke — notlar: ...

## Kapsam Boşlukları
- ...
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her senaryo bir iş olayıyla başlıyor ve doğrulanabilir bir iş sonucuyla bitiyor.
- [ ] Dil iş dili; alan kodu, endpoint veya teknik jargon yok.
- [ ] Kontrol noktaları iş kullanıcısı tarafından teknik erişim olmadan doğrulanabiliyor.
- [ ] Yalnızca mutlu yol değil; istisnalar, onay/retler ve dönem sınırları da kapsanıyor.
- [ ] Veri gerçekçi ve maskelenmiş veya sentetik; gerçek kişisel veri yok.
- [ ] Kapsamdaki her gereksinim veya süreç adımı bir senaryoya eşleniyor ya da boşluk olarak listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Ekran ekran metin yazmak. İş kullanıcıları bu durumda işlerinin yapılıp yapılmadığını değil arayüzü test eder; iş aksiyonlarını ve sonuçlarını tarif et.
- Yalnızca mutlu yollar. Gerçek kabul sorunları istisnalarda ve düzeltmelerde yaşanır.
- Tek sistemde biten senaryolar. Sonucu sonraki role (depo, finans, raporlama) kadar takip et.

## Örnek
Girdi: iade akışı; roller: mağaza personeli, depo, finans.

Zayıf: "İadeler ekranını aç, sipariş no gir, Kaydet'e tıkla, başarı mesajını doğrula."

Güçlü, bir bölüm:
- UAT-03: Müşteri hediye kartıyla aldığı hasarlı ürünü fişsiz iade ediyor.
- Akış: mağaza personeli satışı kartla bulur → kontrol noktası: satış ve ürün listelenir; depo ürünü "hasarlı" olarak teslim alır → kontrol noktası: satılabilir stoğa eklenmez; finans → kontrol noktası: iade yeni bir hediye kartına yapılır, tutar satışla aynı.
- Geçme kriteri: müşteri doğru tutarı alır ve stok doğru kalır. `[VARSAYIM]` fişsiz iadeye kartla sorgulama ile izin veriliyor — süreç sahibiyle teyit et.
