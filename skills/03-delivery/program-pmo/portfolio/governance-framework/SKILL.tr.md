---
description: Riskine göre boyutlandırılmış proje veya program yönetişimini tanımlar: karar türüne göre karar yetkileri, üyeliği ve yetki alanı belli kurullar, giriş kriterli aşama veya karar kapıları, toleranslar ve eskalasyon yolları ile her kurulu besleyen raporlama sıklığı. Yeni bir proje veya program kurulurken, kararlar tıkandığında ya da yanlış yerde alındığında, bir denetim veya sponsor "kim neye karar veriyor" diye sorduğunda ya da mevcut yönetişim fazla ağır veya fazla hafif olduğunda kullanılır.
related: raci-matrix, steering-committee-pack, project-charter, change-control, communication-plan
prompt: Dış bir entegratörün, üç iş biriminin ve halihazırda var olan bir BT yönlendirme kurulunun yer aldığı 14 aylık ERP değişim programı için yönetişim tanımla.
---

# Proje Yönetişimi Tanımlama

## Amaç
Kimin neye, nerede, ne zaman ve hangi bilgiyle karar verdiğini; teslimat ekibinin sormadan hareket edebileceği toleransları ve edemediğinde izlenecek eskalasyon yollarını belirlemek. Böylece kararlar bürokrasiye boğulmadan hızlı, sahipli ve izlenebilir olur.

## Ne zaman kullanılır
- Bir proje veya program başlatılırken kontrol yapısının üzerinde anlaşılması gerektiğinde.
- Kararlar tıkandığında, tekrar tekrar açıldığında veya yetkisi olmayan kişilerce alındığında.
- Bir denetim, sponsor veya yeni bir yönetici net bir karar ve raporlama yapısı istediğinde.
- Mevcut yönetişim orantısız olduğunda (çok fazla kurul ya da yüksek riskli bir iş için hiç kurul olmaması).

## Ne zaman kullanılmaz
- Yalnızca teslimatlar için görev düzeyinde sorumluluk gerekiyorsa `raci-matrix` kullanılır.
- İhtiyaç tek bir yönlendirme toplantısının içeriğiyse `steering-committee-pack` kullanılır.
- Soru yalnızca kapsam değişikliği süreciyse `change-control` kullanılır.

## Girdiler
Zorunlu:
- Proje veya program: hedefi, büyüklüğü (bütçe/süre mertebesi) ve ana tarafları (sponsor, iş birimleri, tedarikçiler).

İsteğe bağlı, kaliteyi artırır:
- Mevcut kurumsal yönetişim (portföy kurulu, mimari kurul, değişiklik danışma kurulu, risk komitesi) ve zorunlu kapılar.
- Tedarikçilerle sözleşme yapısı; mevzuat veya denetim gereksinimleri.
- Bilinen karar sorunları veya geçmiş başarısızlıklar.
- Ekibin teslimat yaklaşımı (sabit iterasyonlar, akış, aşamalı).

Proje tanımı eksikse sor. Bilinmeyen roller ve isimler `[TBD]` olarak kalır; kişi uydurma.

## Süreç
1. Yönetişimi riske göre boyutlandır: karmaşıklığı, bütçeyi, mevzuat maruziyetini, taraf sayısını ve yeniliği değerlendir; ortaya çıkan yönetişim ağırlığını (hafif, standart, ağır) ve nedenini yaz. Paralel kurullar yaratmak yerine mevcut kurumsal kurulları yeniden kullan.
2. İşin karşılaşacağı karar türlerini tanımla: strateji/iş gerekçesi, kapsam, bütçe ve yedek bütçe kullanımı, takvim/kilometre taşları, mimari ve teknoloji, tedarikçi/sözleşme, risk kabulü, kalite/sürüm (go/no-go), fayda.
3. Her karar türü için karar yetkisini ata: kim karar verir, kime danışılır, kim bilgilendirilir ve kararı bir üst seviyeye taşıyan eşik nedir. Her karar türü ve seviye için tam olarak bir karar verici olmalı.
4. Her seviye için toleransları belirle (zaman, maliyet, kapsam, kalite, risk, fayda): tolerans içinde alt seviye karar verir; öngörülen aşım eskalasyonu tetikler. Toleransları muğlak kelimelerle değil, sayı veya `[TBD]` olarak ifade et.
5. Kurulları tasarla: her biri için amaç, başkan, üyeler, yetki alanı (hangi kararlar), yeter sayı, sıklık, gereken girdiler ve çıktılar (karar kaydı girdileri). Karar yetkisi olmayan kurulları kaldır.
6. Teslimat yaklaşımına uygun kapıları veya karar noktalarını tanımla: aşamalı projeler aşama kapıları, iteratif teslimat sonuç veya fonlama kontrol noktaları kullanır. Her kapı için giriş kriterleri, gereken kanıt, karar seçenekleri (devam, koşullu devam, yön değiştir, durdur) ve karar sahibi.
7. Süre sınırlı eskalasyon yollarını tanımla: sorun açılır → sahip seviyesi → <n> iş günü içinde bir üst seviye; bir eskalasyonun içermesi gereken bilgilerle birlikte.
8. Raporlama sıklığını tanımla: hangi rapor hangi kurula, ne sıklıkla, kimin sahipliğinde gider ve asgari içeriği nedir (toleransa göre durum, gereken kararlar, riskler, finansal durum).
9. Güvenceyi tanımla: bağımsız gözden geçirmeler, denetim temas noktaları, kararların ve değişikliklerin nasıl kaydedilip izlenebilir kılındığı.
10. Boşlukları ve çakışmaları kontrol et: her karar türünün her seviyede bir sahibi var; iki kurul aynı kararı sahiplenmiyor; teslimat ekibinin tolerans içinde hareket alanı var.
11. Varsayımları ve açık soruları listele; ardından teslimat düzeyinde roller için `raci-matrix`, ilk kurul toplantısı için `steering-committee-pack` veya değişiklik süreci için `change-control` öner.

## Çıktı formatı
```markdown
# Yönetişim Çerçevesi: <proje / program>
Yönetişim ağırlığı: <hafif / standart / ağır> — <gerekçe>

## Yapı
<sponsor → yönlendirme kurulu → program/proje lideri → iş akışları; bağlı mevcut kurumsal kurullar>

## Karar Yetkileri
| Karar türü | Ekip seviyesi | Proje/program lideri | Yönlendirme kurulu | Kurumsal kurul | Eskalasyon eşiği |
|---|---|---|---|---|---|

## Toleranslar
| Boyut | Lider toleransı | Kurul toleransı | Aşılırsa → |
|---|---|---|---|

## Kurullar
| Kurul | Amaç / yetki alanı | Başkan | Üyeler | Sıklık | Girdiler | Çıktılar |
|---|---|---|---|---|---|---|

## Kapılar / Karar Noktaları
| Kapı | Ne zaman | Giriş kriterleri | Kanıt | Karar sahibi | Seçenekler |
|---|---|---|---|---|---|

## Eskalasyon Yolu
## Raporlama Sıklığı
| Rapor | Kitle / kurul | Sıklık | Sahip | Asgari içerik |
|---|---|---|---|---|

## Güvence ve İzlenebilirlik
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Yönetişim ağırlığı riskle gerekçelendirildi ve mevcut kurumsal kurullar yeniden kullanıldı.
- [ ] Her karar türünün her seviyede tam olarak bir karar vericisi ve sayısal ya da `[TBD]` bir eskalasyon eşiği var.
- [ ] Her kurulun gerçek karar yetkisi içeren bir yetki alanı var; hiçbiri diğerini tekrarlamıyor.
- [ ] Kapıların giriş kriterleri, gereken kanıtı ve açık durdur/yön değiştir seçenekleri var.
- [ ] Eskalasyon yollarının süre sınırı ve gerekli içeriği var.
- [ ] Uydurulmuş isim veya eşik yok; çıkarımlar etiketli ve listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca bilgi alan kurullar yaratmak. Alacak kararı olmayan bir kurul bir raporlama toplantısıdır; birleştir veya kaldır.
- Tolerans belirlememek ve böylece her sapmayı eskale etmek. Kararları işe yakın tutmak için sayısal toleranslar içinde yetki devret.
- İteratif teslimata aşama kapısı yönetişimi dayatmak. Doküman tamamlanmasına değil, sonuçlara ve fonlama kontrol noktalarına göre kapı koy.

## Örnek
Girdi: "14 aylık ERP değişimi, dış entegratör, 3 iş birimi, mevcut BT yönlendirme kurulu."

Çıktıdan bir bölüm:
| Karar türü | Program lideri | Yönlendirme kurulu | Eskalasyon eşiği |
|---|---|---|---|
| Yedek bütçe kullanımı | yedek bütçenin `[TBD]`%'sine kadar | bunun üzeri | Yedek bütçeyi `[TBD]` altına düşürecek her kullanım |
| Kapsam değişikliği | anlaşılan backlog içinde, kilometre taşı etkisi yok | kilometre taşı veya iş birimleri arası etki | Değişiklik bir kilometre taşını 2 haftadan fazla kaydırıyorsa `[VARSAYIM]` |
| Tedarikçi değişiklik talebi | önerir | onaylar | Sözleşme bedelinde her değişiklik |

- Kurul kararı: yeni bir kurul yaratmak yerine mevcut BT yönlendirme kurulu, 3 iş birimi başkanı eklenerek program kurulu olarak kullanılır.
