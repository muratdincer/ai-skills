---
description: Bir rolü misyonu, sonuçları, sorumlulukları, karar yetkileri, diğer rollerle arayüzleri ve rolün hesap vermediği konularla birlikte tanımlar. Yeni bir rol (ör. staff mühendis, teknik lider, platform ürün sahibi) oluşturulurken, iki rol çakıştığında veya çatıştığında ya da karar yetkileri belirsiz olduğu için işler rollerin arasında kaldığında kullanılır.
related: raci-matrix, career-ladder, job-description, team-topology, governance-framework
prompt: Ekiplerimizdeki teknik lider rolünü tanımla; insanlar bu rolü mühendislik yöneticisi ve mimarla karıştırıyor.
---

# Rol Tanımlama

## Amaç
Bir rolün amacını, hesap verdiği sonuçları ve karar yetkilerini açık hale getirmek. Böylece rolü üstlenen kişi, ekip arkadaşları ve yöneticisi aynı beklentiyi paylaşır ve önemli hiçbir iş rollerin arasında kalmaz.

## Ne zaman kullanılır
- Yeni bir rol getiriliyor veya mevcut bir rol yeniden yapılanma sonrası değişiyor.
- İki rol çakışıyor (teknik lider ve mühendislik yöneticisi, mimar ve staff mühendis, PO ve PM) ve sürtünme yaratıyor.
- Kimin karar verdiği bilinmediği için kararlar tıkanıyor.

## Ne zaman kullanılmaz
- Dışarıya yönelik bir iş ilanı için `job-description` kullanılır (bu tanımı yeniden kullanabilir).
- Bir meslek ailesindeki seviye beklentileri için `career-ladder` kullanılır.
- Tek bir projede çok sayıda görevi çok sayıda role dağıtmak için `raci-matrix` kullanılır.

## Girdiler
Zorunlu:
- Rolün adı ve içinde bulunduğu ekip veya organizasyon bağlamı.

İsteğe bağlı, kaliteyi artırır:
- Komşu roller ve mevcut tanımları, bilinen çatışmalar veya arada kalan işler.
- Raporlama hattı, ekip topolojisi, yönetişim forumları, mevcut kariyer basamakları.

Komşu roller bilinmiyorsa yeni rolün en çok hangi rollerle çalıştığını sor; bunlar olmadan arayüzler tanımlanamaz.

## Süreç
1. Rolün misyonunu tek cümleyle yaz: neden var ve olmasaydı ne ters giderdi.
2. Rolün bir dönem boyunca hesap verdiği, ölçülebilir veya gözlemlenebilir 3-5 sonuç tanımla (aktivite değil).
3. Sorumlulukları alanlara göre grupla (teknik, teslimat, insan, paydaşlar) ve her birini fiil ile başlayan bir ifadeyle yaz.
4. Karar yetkilerini düzeyleriyle tanımla: tek başına karar verir, danışarak karar verir, önerir, bilgilendirilir. Kararları somut adlandır (ör. ekip içi kütüphane seçimi, canlıya çıkış, işe alım kararı).
5. Komşu rollerle arayüzleri haritala: bu rol onlardan ne alır, onlara ne verir; bilinen her çakışmayı tek ve açık bir sahiple çöz.
6. Kapsam kaymasını önlemek için açıkça rolün sorumluluğunda olmayanları yaz (ör. teknik lider performans değerlendirmesi yazmaz).
7. Rol farklı aktiviteleri birleştiriyorsa zaman dağılımını aralık olarak ver (ör. uygulamalı kodlama %30-50); teyit edilmediyse `[VARSAYIM]` olarak işaretle.
8. Raporlama hattını, yönetim alanını ve rolün bir seviye, pozisyon veya geçici görev olup olmadığını not et.
9. Dili kapsayıcı ve role odaklı tut; rolü şu anki kişinin kişiliği üzerinden tarif etme.
10. Karar yetkilerinin tartışmalı olduğu yerleri ve bunları kimin netleştirmesi gerektiğini açık soru olarak listele.
11. Kullanıcının hedefi devam ediyorsa proje düzeyinde dağılım için `raci-matrix`, rol için işe alım yapmak üzere `job-description` veya rolü seviyelere yerleştirmek için `career-ladder` öner.

## Çıktı formatı
```markdown
# Rol: <ad>
Bağlam: <ekip / organizasyon> · Raporladığı: <rol> · Tür: <seviye / pozisyon / görevlendirme>

## Misyon
<tek cümle>

## Sonuçlar
1. ...

## Sorumluluklar
| Alan | Sorumluluk |
|---|---|

## Karar Yetkileri
| Karar | Karar veren | Danışılan | Bilgilendirilen |
|---|---|---|---|

## Arayüzler
| Rol | Bu rolün sağladığı | Bu rolün ihtiyacı |
|---|---|---|

## Sorumluluğunda Olmayanlar
- ...

## Zaman Dağılımı (yaklaşık)
- ...

## Açık Sorular
- ...
```

## Kalite kontrol listesi
- [ ] Misyon rolün gündelik işini değil, neden var olduğunu açıklıyor.
- [ ] Sonuçlar gözlemlenebilir ve sorumlulukların tekrarı değil.
- [ ] Komşu rollerle bilinen her çakışmanın tek ve açık bir sahibi var.
- [ ] Karar yetkileri somut kararları adlandırıyor.
- [ ] Sorumlulukta olmayanlar listelendi.
- [ ] Tanım şu anki kişiyi değil rolü anlatıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Herkesin yapabileceği her görevi listelemek. Rolün hesap verdiği şeylerle sınırlı kal.
- Tartışmalı kararlar için "ortak" sahiplik bırakmak. Ortak demek kimse demektir; birini seç, diğerine danışılsın.
- Rolü güçlü bir kişinin etrafında yazmak. Tanım, kişi değiştiğinde de geçerli olmalı.

## Örnek
Girdi: Teknik lider rolü; sprint kapsamına ve düşük performansa kimin bakacağı konusunda mühendislik yöneticisiyle çatışma var.

Çıktıdan bir bölüm:
- Misyon: Ekibin teknik kararlarının sağlam ve tutarlı olmasını sağlayarak ekibin sürdürülebilir hızda güvenle teslim etmesini sağlar.
- Karar yetkileri: Ekip sınırları içinde teknik tasarım – teknik lider karar verir, ekipler arası etki için mimara danışılır. İterasyon kapsamı – ürün sahibi karar verir, teknik lidere danışılır.
- Sorumluluğunda olmayanlar: performans değerlendirmeleri, ücretlendirme, resmi performans iyileştirme planları (mühendislik yöneticisi).
