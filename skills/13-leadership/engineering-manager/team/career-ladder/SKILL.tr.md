---
name: career-ladder
description: "Bir meslek ailesi için seviyeleri, seviye başına kapsam ve etkiyi, gözlemlenebilir örneklerle yetkinlik beklentilerini ve paralel bireysel katkıcı ile yönetim yollarını içeren kariyer basamakları oluşturur veya revize eder. Terfi, işe alım ve değerlendirmelerde tutarlı seviyelendirme gerektiğinde, seviyeler belirsiz veya ekipler arasında tutarsız olduğunda ya da staff/principal veya yönetim yolu eklenirken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: team
  title: "Kariyer basamakları oluşturma"
  related: "role-definition, performance-review, career-development-plan, job-description, interview-plan"
  prompt: "Yazılım mühendislerimiz için junior'dan principal'a kariyer basamakları oluştur; takım liderinden direktöre ayrı bir yönetim yolu olsun."
---

# Kariyer Basamakları Oluşturma

## Amaç
Çalışanlara ve yöneticilere her seviyenin ne anlama geldiğine dair ortak ve adil bir tanım vermek. Böylece işe alım, değerlendirme ve terfiler ekipler arasında kalibre olur ve gelişim yolları herkese görünür hale gelir.

## Ne zaman kullanılır
- Kariyer basamakları yok ya da seviyeler yalnızca deneyim yılı veya unvanla tanımlı.
- Terfiler ekipler arasında tutarsız veya çalışanlar bir sonraki seviyenin ne gerektirdiğini bilemiyor.
- Yeni bir yol (staff/principal bireysel katkıcı, yönetim, uzman) veya meslek ailesi ekleniyor.

## Ne zaman kullanılmaz
- Mevcut basamaklara göre tek bir kişinin gelişim planı için `career-development-plan` kullanılır.
- Tek bir rolün sorumluluklarını ve karar yetkilerini tanımlamak için `role-definition` kullanılır.
- Ücret bantları ve ücret politikası basamakların dışında tutulur; İK politikasına yönlendirilir.

## Girdiler
Zorunlu:
- Meslek ailesi (ör. yazılım mühendisliği) ve istenen seviye sayısı veya adları ya da mevcut seviyeler.

İsteğe bağlı, kaliteyi artırır:
- Şirket değerleri, mevcut yetkinlikler, mevcut basamaklar veya değerlendirme şablonu.
- Organizasyon büyüklüğü ve yapısı, bireysel katkıcı ve yönetim yollarının paralel olup olmayacağı.

Seviye yapısı yoksa bir yapı öner (ör. 6 bireysel katkıcı, 3 yönetim seviyesi) ve `[VARSAYIM]` olarak işaretle.

## Süreç
1. Meslek ailesi için önemli 4-6 yetkinlik tanımla (ör. teknik ustalık, teslimat ve sahiplenme, sistem tasarımı, iş birliği ve iletişim, liderlik ve etki, iş etkisi).
2. Her seviye için kapsam eksenini tanımla: görev, özellik, ekip, birden fazla ekip, organizasyon, şirket; seviyeleri becerilerden çok bu eksen ayırır.
3. Her seviyenin özetini 2-3 cümleyle yaz: kapsam, özerklik, karşılanan belirsizlik ve etki.
4. Her yetkinlik ve seviye için beklentileri 1-2 örnekle gözlemlenebilir davranışlar olarak yaz; her seviye bir öncekini "daha fazla" diyerek tekrarlamamalı, yeni bir şey eklemeli.
5. Bireysel katkıcı ve yönetim yollarını eşdeğer seviyelerle paralel tasarla; yönetim, kıdemli bireysel katkıcılıktan terfi değil, farklı bir iştir.
6. Basamakların nasıl kullanılacağını belirt: Seviye tek bir projeye değil, bir dönem boyunca süreklilik gösteren kanıta göre değerlendirilir; tüm davranışlar gerekmez, genel örüntü belirleyicidir.
7. Kapsayıcılığı kontrol et: Etki yerine görünürlüğü, sonuç yerine sürekli ulaşılabilirliği veya tek bir çalışma tarzını ödüllendiren gereksinimleri çıkar; mentorluk, kod incelemesi ve olay sonrası takip gibi "yapıştırıcı işleri" değerli say.
8. Boşlukları ve sıçramaları kontrol et: Komşu seviyeler arasındaki adımlar benzer büyüklükte olmalı; belirli bir fırsat olmadan ulaşılması zor seviyeleri işaretle.
9. Kalibrasyon rehberi ekle: Yöneticiler kanıtları ekipler arasında nasıl karşılaştırır ve anlaşmazlıkları nasıl çözer.
10. İK veya yönetim kararı gerektiren konuları (unvanlar, seviye sayıları, mevcut çalışanların eşleştirilmesi) açık soru olarak listele; isimle kişi eşleştirme.
11. Kullanıcının hedefi devam ediyorsa bireyler için `career-development-plan`, basamaklara göre değerlendirme için `performance-review` veya işe alım için `job-description` öner.

## Çıktı formatı
```markdown
# Kariyer Basamakları: <meslek ailesi>

## Kullanım İlkeleri
- ...

## Seviyelere Genel Bakış
| Seviye | Unvan | Kapsam | Özet |
|---|---|---|---|

## Yetkinlik Matrisi
| Yetkinlik | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|

## Yönetim Yolu
| Seviye | Eşdeğer bireysel katkıcı seviyesi | Kapsam | Özet |
|---|---|---|---|

## Kalibrasyon Rehberi
- ...

## Açık Sorular / Gereken Kararlar
- ...
```

## Kalite kontrol listesi
- [ ] Her seviye komşusundan "daha fazla" veya "daha iyi" gibi sıfatlarla değil, kapsam ve davranışla ayrılıyor.
- [ ] Beklentiler gözlemlenebilir ve örnekli.
- [ ] Deneyim yılı eşiği veya ulaşılabilirlik, görünürlük ya da kişisel durumlara bağlı gereksinim yok.
- [ ] Yapıştırıcı işler (mentorluk, incelemeler, olaylar, dokümantasyon) tanınıyor.
- [ ] Bireysel katkıcı ve yönetim yolları paralel ve eşit değerde.
- [ ] Kullanım ve kalibrasyon rehberi eklendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Kıdemli = daha hızlı orta seviye." Seviyeler hızla değil, kapsam ve belirsizlikle ayrılmalı.
- Basamakları her hücresi işaretlenmesi gereken bir kontrol listesi gibi kullanmak. Kanıtın genel örüntüsünün belirleyici olduğunu yaz.
- Staff ve üstü terfiyi büyük bir projeye atanmaya bağlamak. Kapsama ulaşmanın birden fazla geçerli yolunu tarif et.

## Örnek
Girdi: Yazılım mühendisliği, L1-L6 bireysel katkıcı, M1-M3 yönetim.

Çıktıdan bir bölüm:
- L4 Kıdemli, Sistem tasarımı: Ekibin alanında birden fazla servise yayılan özellikleri tasarlar, ödünleşimleri belgeler ve etkilenen ekiplerden inceleme alır; örnek: iki ekibin benimsediği idempotent ödeme yeniden denemesi tasarım dokümanı.
- Zayıf hücre (kaçın): "L5: Çok güçlü tasarım becerisi." Güçlü hücre: "L5: 2-4 ekip genelinde teknik yönü belirler; çelişen tasarımları ödünleşimleri açık hale getirerek çözer."
- `[VARSAYIM]` M1 kapsam olarak L5'e eşdeğer; İK ile teyit edilmeli.
