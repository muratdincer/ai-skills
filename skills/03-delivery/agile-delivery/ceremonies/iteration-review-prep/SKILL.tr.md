---
description: "Bir iterasyon/sprint değerlendirmesini hazırlar: artımı iterasyon hedefine göre özetler, demoyu kullanıcı senaryoları etrafında sıralar, yapılmayanları ve nedenlerini belirtir, hedefli geri bildirim soruları ve backlog etkisi soruları taslaklar. Ekibin iterasyon değerlendirmesi, sprint review veya iterasyon sonu demosu yaklaştığında ve gündem, demo sırası veya artım özeti istendiğinde kullanılır."
related: "stakeholder-review-prep, demo-script, iteration-goal, burndown-analysis, retrospective-facilitation"
prompt: "Perşembe günkü sprint review'ı hazırla. Hedef 'üye işyerleri kısmi iade yapabilir' idi. Biten: iade API, iade arayüzü, e-posta bildirimi. Bitmeyen: iade raporu. Finans ve destekten 8 paydaş gelecek."
---

# İterasyon Değerlendirmesi Hazırlığı

## Amaç
İterasyon değerlendirmesini bir slayt gösterisi yerine artımın incelendiği ve backlog'u değiştiren bir konuşmaya dönüştürmek: çalışan sonuçları anlamlı bir sırayla göstermek, bitmeyenler konusunda şeffaf olmak ve ekibin cevabına ihtiyaç duyduğu soruları sormak.

## Ne zaman kullanılır
- Bir iterasyon/sprint değerlendirmesi veya iterasyon sonu demosu planlandı.
- Ekip madde madde demo yapma eğiliminde ve az işe yarar geri bildirim alıyor.
- Geri bildirim verebilmek için bağlama ihtiyaç duyan yeni paydaşlar katılıyor.

## Ne zaman kullanılmaz
- Yöneticilerle ve birden çok iterasyonu kapsayan kararlarla ürün seviyesinde bir değerlendirme için `stakeholder-review-prep` kullanılır.
- Adım adım demo senaryosunun kendisini yazmak için `demo-script` kullanılır.
- Ekibin iç iyileştirme tartışması için `retrospective-facilitation` kullanılır.

## Girdiler
Zorunlu:
- İterasyon hedefi ve tamamlanan ile tamamlanmayan maddelerin listesi.

İsteğe bağlı, kaliteyi artırır:
- Rolleriyle katılımcı listesi ve ayrılan süre.
- Hedefle ilgili metrikler veya sinyaller (kullanım, test sonuçları, performans).
- Sıradaki backlog maddeleri ve açık ürün soruları.
- Neyin bitmiş sayılacağını teyit etmek için Bitti Tanımı (DoD).

Hedef veya madde durumu eksikse sor. Aksi halde devam et ve eksikleri açık soru olarak listele.

## Süreç
1. İterasyon hedefini yeniden ifade et ve kanıtıyla birlikte karşılandı, kısmen karşılandı veya karşılanmadı olarak değerlendir. Gösterilebilir bir sinyal olmadan "karşılandı" deme.
2. Demoya yalnızca Bitti Tanımı'nı karşılayan maddeleri al; kısmen biten işi bitmiş gibi sunmadan ayrı listele.
3. Biten maddeleri hedefin hikayesini anlatan 1-3 kullanıcı senaryosunda grupla; en değerli veya en riskli sonuç önce gelecek şekilde sırala.
4. Her senaryo için sunucu adayını, gereken ortamı ve veriyi, ortam çökerse yedek planı (kayıt veya ekran görüntüleri) belirt. Teyit edilmemiş sunucuları `[TBD]` olarak işaretle.
5. Bitmeyen maddeleri nedeniyle (kapsam değişikliği, bağımlılık, eksik tahmin) ve nereye gideceğiyle özetle; suçlayıcı dil kullanma.
6. Katılımcıların rollerine yönelik 3-6 geri bildirim sorusu yaz; her biri bir karara veya backlog maddesine bağlı olsun (ör. "İade limiti sipariş başına mı, gün başına mı?").
7. Kısa bir "sırada ne var" görünümü hazırla: sıradaki üst backlog maddeleri ve katılımcıların tepki vermesi gereken pazar, kullanım veya zaman çizelgesi değişiklikleri.
8. Sürenin en az üçte birini geri bildirim ve tartışmaya ayıran zaman kutulu bir gündem oluştur.
9. Geri bildirimleri, yeni backlog maddelerini ve kararları kaydetmek için bir şablon ekle.
10. Kullanıcının hedefi devam ediyorsa her senaryoyu yazmak için `demo-script`, ekibin retrospektifi için `retrospective-facilitation` öner.

## Çıktı formatı
```markdown
# İterasyon Değerlendirmesi: <iterasyon> – <tarih>, <süre>
**Hedef:** <hedef> – **Sonuç:** Karşılandı / Kısmen / Karşılanmadı – <kanıt>

## Gündem
| Saat | Konu | Yürüten |
|---|---|---|

## Demo Sırası
1. Senaryo: <sonucun kullanıcı hikayesi> – Maddeler: ... – Sunan: <isim/[TBD]> – Ortam/veri: ... – Yedek: ...

## Bitmeyenler
| Madde | Durum | Neden | Sonraki |
|---|---|---|---|

## Geri Bildirim Soruları
1. <soru> – <hedef kitle> – <beslediği karar/backlog maddesi>

## Sırada Ne Var
- ...

## Kayıt (toplantıda doldurulur)
| Geri bildirim / fikir | Kimden | Backlog etkisi | Karar |
|---|---|---|---|
```

## Kalite kontrol listesi
- [ ] Hedef sonucu iddia edilmeden, kanıtıyla belirtildi.
- [ ] Yalnızca Bitti Tanımı'nı karşılayan maddeler bitmiş olarak gösteriliyor.
- [ ] Demo madde numarasına göre değil, senaryo ve değere göre sıralı.
- [ ] Her geri bildirim sorusu bir karara veya backlog maddesine bağlı.
- [ ] Sürenin en az üçte biri tartışmaya ayrıldı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Neredeyse bitti" diye yarım işi demolamak. Algılanan ilerlemeyi şişirir; yalnızca açıkça etiketlenmiş devam eden iş olarak göster.
- Sonda "Geri bildirim var mı?" diye sormak. Açık uçlu sorular sessizlik getirir; role özel, somut sorular sor.
- Değerlendirmeyi onay toplantısı gibi görmek. Çıktısı onay değil, güncellenmiş bir backlog'dur.

## Örnek
Girdi: hedef "üye işyerleri kısmi iade yapabilir"; biten: iade API, iade arayüzü, e-posta bildirimi; bitmeyen: iade raporu; finans ve destek katılıyor.

Çıktıdan bir bölüm:
- Sonuç: Karşılandı – staging'de uçtan uca kısmi iade yapılıyor ve üye işyeri e-postayı alıyor `[toplantı öncesi staging verisini teyit et]`.
- Bitmeyen: İade raporu | Başlanmadı | API işi eksik tahmin edildi | Sonraki iterasyonun ilk adayı.
- Geri bildirim sorusu: "Destek temsilcileri de kısmi iade yapabilmeli mi, yoksa yalnızca üye işyerleri mi?" – destek lideri – yetki maddesini besler.
