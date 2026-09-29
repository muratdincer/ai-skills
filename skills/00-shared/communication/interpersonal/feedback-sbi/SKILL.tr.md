---
description: Olumlu veya düzeltici geri bildirimi Durum-Davranış-Etki (SBI) modeliyle kurgular; gözlenen davranışı yorumdan ayırır, somut etkiyi belirtir ve bir talep ile açık bir soruyla bitirir. Birinin bir çalışma arkadaşına, ekip üyesine, eşdüzey birine veya yöneticisine geri bildirim vermesi, zor bir konuşmaya hazırlanması ya da kişiyi yargılar gibi duran bir geri bildirimi yeniden yazması gerektiğinde kullanılır.
related: one-on-one-prep, performance-review, conflict-resolution, tone-rewrite, underperformance-plan
prompt: Review beklemeden pull request'leri merge eden kıdemli bir geliştiriciye, onu savunmaya geçirmeden geri bildirim vermeme yardım et.
---

# Geri Bildirim Verme (SBI)

## Amaç
Birinin işiyle ilgili bir gözlemi, alıcının tanıyabileceği, sonucunu anlayabileceği ve üzerine harekete geçebileceği somut, adil ve uygulanabilir bir geri bildirime dönüştürmek; bunu yaparken ilişkiyi korumak.

## Ne zaman kullanılır
- Birebir görüşme için ya da bir olayın ardından düzeltici veya pekiştirici geri bildirim hazırlanırken.
- Şimdiye kadar yazılan geri bildirim belirsiz ("daha proaktif ol") veya kişisel ("dikkatsizsin") ise.
- Ton ve adaletin önemli olduğu yukarıya veya eşdüzeye geri bildirim verilirken.

## Ne zaman kullanılmaz
- Dönemsel, yapılandırılmış bir değerlendirme zamanı gelmişse. `performance-review` kullanın.
- Konu, resmi bir plan gerektiren tekrarlı ve belgelenmiş düşük performanssa. `underperformance-plan` kullanın.
- İki taraf süregelen bir anlaşmazlık içindeyse ve arabuluculuk gerekiyorsa. `conflict-resolution` kullanın.

## Girdiler
Zorunlu:
- Ne oldu: belirli durum ve gözlenen davranış (kim, ne zaman, nerede).
- İlişki (yönetici, eşdüzey, ekip üyesi, yukarıya) ve geri bildirimin amacı.

İsteğe bağlı:
- Bilinen etki, konuyla ilgili önceki geri bildirimler, alıcının bağlamı (iş yükü, yeni rol), tercih edilen dil ve ortam.

Davranış yalnızca bir kişilik özelliği olarak anlatılıyorsa ("kibirli"), arkasındaki somut örnekleri her seferinde tek soru sorarak isteyin. Asla olay, tarih veya alıntı uydurmayın; başkasından duyulanları öyle işaretleyin. Geri bildirim için gerekmeyen kişisel ayrıntıları en aza indirin.

## Süreç
1. Niyet ve zamanlamayı kontrol edin: geri bildirim olaydan kısa süre sonra, düzeltici ise baş başa ve veren kişi sakin kalabilecekken verilir. Zamanlama uygun değilse not edin.
2. Durumu yazın: hatırlanacak kadar belirli ne zaman ve nerede ("salı günkü faturalama servisi sürümünde"); "her zaman" veya "son zamanlarda" değil.
3. Davranışı yazın: yalnızca gözlenebilir eylem ve sözler, bir kameranın kaydedeceği şeyler. Sıfatları, niyetleri ve etiketleri çıkarın; her yorumu `[YORUM]` olarak işaretli ayrı bir satıra taşıyın.
4. Etkiyi yazın: ekip, müşteri, kalite, takvim veya veren kişi üzerindeki somut sonuç ("iki hata canlıya çıktı; nöbetçi iki kez arandı"). Kişisel etki için "ben" dili kullanın. Doğrulanmamış etkiyi `[TBD]` olarak işaretleyin.
5. Davet ekleyin: karşı tarafın görüşünü duymak için açık ve yönlendirmeyen bir soru ("Sen nasıl gördün?"); çünkü alıcı, verenin bilmediği bir bağlama sahip olabilir.
6. Talep veya pekiştirme ekleyin: düzeltici geri bildirimde bundan sonra beklenen belirli davranış; olumlu geri bildirimde tam olarak neyin sürdürülmesi gerektiği.
7. Denge ve adaleti kontrol edin: bir konuşmada tek konu, üst üste yığılmış şikâyet yok, mesajı gizleyen "sandviç" yok.
8. İlişkiye ve kültüre uyarlayın: yukarıya geri bildirimde izin isteyin ve kendi işinize etkisine odaklanın; resmi ilişkilerde "siz" dilini koruyun ve talebi gizleyen dolaylılıktan kaçının.
9. Tepkilere hazırlanın: olası savunmacı yanıtlar ve her birine sakin bir cevap; değişimin nasıl teyit edileceğini belirleyin.
10. Kullanıcının hedefi devam ediyorsa konuşmayı planlamak için `one-on-one-prep`, karşı taraf durumu kabul etmezse `conflict-resolution`, dönemsel değerlendirme için `performance-review` öner.

## Çıktı formatı
```markdown
# Geri Bildirim: <alıcının rolü> – <konu>
Tür: Düzeltici / Pekiştirici | Ortam: <birebir, baş başa, ne zaman>

- Durum: <ne zaman, nerede>
- Davranış: <gözlenebilir eylem/sözler>
- Etki: <ekip/müşteri/iş/ben üzerindeki somut sonuç>
- Davet: "<açık soru>"
- Talep / sürdür: <bundan sonraki belirli davranış>

Sözlü sürüm (3-5 cümle):
"<...>"

Olası tepkiler ve cevaplar:
- "<tepki>" -> <sakin cevap>
Takip: <değişimin nasıl ve ne zaman fark edileceği>
Mesajın dışında tutulan [YORUM] / [TBD] maddeleri: ...
```

## Kalite kontrol listesi
- [ ] Davranış yalnızca gözlenebilir olgular içeriyor; kişilik özelliği, niyet veya sıfat yok.
- [ ] Durum belirli; "her zaman", "asla" veya "son zamanlarda" yok.
- [ ] Etki somut ve doğrulanmış ya da `[TBD]` olarak işaretli.
- [ ] Tek konu, açık bir davet ve belirli bir talep var.
- [ ] İfadeler ilişkiye (yukarı, eşdüzey, aşağı) ve dilin resmiyetine uygun.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Davranış yerine kişiyi tarif etmek ("dikkatsizsin"). Bir kameranın göreceği eylemi anlatın.
- Geri bildirimi haftalar sonra bir değerlendirmede vermek. Olaya yakın zamanda verin.
- Yalnızca düzeltici geri bildirim vermek. SBI'yı iyi davranışı pekiştirmek için de kullanın ki yalnızca eleştiriyle özdeşleşmesin.

## Örnek
Girdi: Kıdemli geliştirici pull request'leri review beklemeden merge ediyor.

Zayıf: "Ekibin sürecine saygı duymuyorsun ve kurallar sana uymuyormuş gibi davranıyorsun."

Güçlü (alıntı):
- Durum: Faturalama servisinin son iki sürümünde (`[tarihler]`).
- Davranış: Üç pull request, hiçbir reviewer yorum yapmadan, açıldıktan birkaç dakika sonra merge edildi.
- Etki: Bunlardan biri müşterilerin bildirdiği yuvarlama hatasını getirdi; ekip de değişikliklerinin zaten canlıda olduğunu düşünerek onları incelemeyi bıraktı.
- Davet: "O merge'lerde senin tarafında neler oluyordu?"
- Talep: "Bundan sonra en az bir onay bekle; acil bir durum varsa bana ya da nöbetçi reviewer'a haber ver."
