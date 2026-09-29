---
description: "Bir iş varlığının (sipariş, başvuru, hasar dosyası, sözleşme, kayıt) yaşam döngüsünü modeller: durumlar, geçişler, tetikleyici olaylar, koşullar (guard), eylemler, her geçişi kimin tetikleyebileceği ve geçersiz geçişler; çıktı bir geçiş tablosu ve diyagram kodudur. Bir varlığın davranışı belirleyen durumları olduğunda, durum kuralları dağınık veya tartışmalı olduğunda ya da iş akışı, API veya durum geçiş testleri tasarlanmadan önce kullanılır."
related: "business-rules-catalog, state-transition-testing, sequence-flow, error-scenario-catalog, diagram-as-code"
prompt: "Bir sigorta hasar dosyasının başvurudan ödemeye veya redde kadar durumlarını, yeniden açma ve iptal dahil modelle."
---

# Durum Modeli Çıkarma

## Amaç
Bir varlığın yaşam döngüsünü açık ve eksiksiz hâle getirmek. Böylece her durum, izin verilen her geçiş, kural ve yan etki bir kez üzerinde anlaşılır; ekranlarda, API'lerde, toplu işlerde ve raporlarda tutarlı biçimde geliştirilip test edilebilir.

## Ne zaman kullanılır
- Bir varlığın, kullanıcıların veya sistemlerin ne yapabileceğini belirleyen bir durum alanı varsa.
- Ekipler "Onaylandı" veya "Kapandı"nın ne anlama geldiğinde anlaşamıyorsa ya da durum kuralları birden çok dokümana dağılmışsa.
- Bir iş akışı, API veya olay tasarımı ya da durum geçiş testleri başlamak üzereyse.

## Ne zaman kullanılmaz
- Roller arası adım adım iş süreci gerekiyorsa `bpmn-model` veya `as-is-process` kullanılır.
- Tek bir senaryo için sistemler arası mesaj sırası gerekiyorsa `sequence-flow` kullanılır.
- Üzerinde anlaşılmış bir modelden yalnızca diyagram üretilecekse `diagram-as-code` kullanılır.

## Girdiler
Zorunlu:
- Varlık ve yaşam döngüsüne dair herhangi bir tarif (gereksinimler, süreç notları, mevcut durum listesi).

İsteğe bağlı, kaliteyi artırır:
- Veritabanından veya ekranlardan mevcut durum değerleri, iş kuralları, roller ve yetkiler.
- Durumu okuyan entegrasyonlar veya raporlar, SLA sayaçları, yasal saklama kuralları.

Varlık veya yaşam döngüsü tarifi yoksa iste. Fazlasını sorma; bilinmeyen kuralları açık soru olarak kaydet.

## Süreç
1. Girdiden aday durumları listele. Eş anlamlıları birleştir, iki anlam saklayan durumları böl (örn. hem müşteri hem onaycı beklemesi için "Beklemede") ve her durumu bir eylem değil bir hâl olarak adlandır ("İncelemede").
2. Başlangıç durumunu, son (terminal) durumları ve yalnızca yöneticilerin veya toplu işlerin ulaşabildiği durumları işaretle.
3. Her durum için varlığı dışarı taşıyan olayları sor: kullanıcı eylemi, sistem olayı, zamanlayıcı veya dış mesaj. Her birini geçiş olarak kaydet: kaynak, olay, koşul, hedef, eylem veya yan etki, izinli aktör.
4. Durum-olay matrisinin tamamını oluştur ve her boş hücreyi İzin yok (hatayla reddet), Yok say (işlem yok) veya `[TBD]` olarak sınıflandır; hiçbir hücreyi değerlendirmeden bırakma.
5. Yaşam döngüsünün eksiksizliğini kontrol et: iptal veya geri çekme, yeniden açma, süre dolması ve zaman aşımları, alt sistem hatasında geri alma, son durumdan sonra düzeltme, saklama kurallarına göre arşivleme veya silme.
6. Eşzamanlılığı kontrol et: iki aktörün aynı anda çelişen geçişleri tetiklemesi, tekrarlanan olaylar, sırası bozuk dış mesajlar. Beklenen kuralı yaz (ilk gelen kazanır, iyimser kilit, idempotent olay).
7. Her geçişin yan etkilerini listele: bildirimler, entegrasyon mesajları, denetim kayıtları, SLA sayacı başlatma/durdurma. Bildirimlerdeki kişisel veriyi minimizasyon için işaretle.
8. Girdide belirtilmeyen her kuralı `[VARSAYIM]` olarak etiketle ve muhtemel sorumlusuyla açık sorulara taşı.
9. Tabloyla tutarlı diyagram kodu üret (Mermaid stateDiagram-v2 veya PlantUML); her geçiş her ikisinde de yer alsın.
10. Kullanıcı devam etmek isterse test türetmek için `state-transition-testing`, koşul kuralları için `business-rules-catalog` veya reddedilen geçişler için `error-scenario-catalog` öner.

## Çıktı formatı
```markdown
# Durum Modeli: <varlık>
Başlangıç: <durum> · Son: <durumlar> · Kaynak: <dokümanlar>

## Durumlar
| Durum | Anlamı (hâl) | Giriş yolu | Son mu? | Kimler görür |
|---|---|---|---|---|

## Geçişler
| # | Kaynak | Olay / tetikleyici | Koşul | Hedef | Eylem / yan etki | Aktör |
|---|---|---|---|---|---|---|

## İzin Verilmeyen / Yok Sayılan Olaylar
| Durum | Olay | İşlem (Mesajla reddet / Yok say / TBD) |
|---|---|---|

## Eşzamanlılık ve Zamanlama Kuralları
- ...

## Diyagram
<Mermaid stateDiagram-v2 veya PlantUML kodu>

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ... — sorumlu
```

## Kalite kontrol listesi
- [ ] Her duruma başlangıç durumundan ulaşılabiliyor ve son olmayan her durumun en az bir çıkışı var.
- [ ] Her geçişin bir olayı var ve koşullar test edilebilir biçimde yazılmış.
- [ ] Her durum-olay kombinasyonu ele alınmış: izinli, izin yok veya `[TBD]`.
- [ ] İptal, yeniden açma, süre dolması ve hata yolları açıkça değerlendirildi.
- [ ] Tablo ve diyagram birebir örtüşüyor.
- [ ] Çıkarım olan kurallar `[VARSAYIM]` olarak etiketli ve açık sorularda listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Eylemleri durum olarak kullanmak ("Onayla", "Gönder"). Durum, bir olay gerçekleşene kadar süren bir hâli anlatır.
- Tek bir durum alanına birden çok boyut koymak (ödeme durumu ve inceleme durumu). Bunları ayrı durum makineleri veya dik bölgeler olarak modelle.
- Zamanlayıcı, toplu iş ve gelen mesaj gibi insan dışı tetikleyicileri unutmak; üretimdeki sürprizlerin çoğu bunlardan çıkar.

## Örnek
Girdi: "Hasar dosyası açılır, eksper inceler, onaylanır veya reddedilir, sonra ödenir. Müşteri karardan önce iptal edebilir."

Çıktıdan bir bölüm:
| # | Kaynak | Olay | Koşul | Hedef | Eylem | Aktör |
|---|---|---|---|---|---|---|
| T1 | Açıldı | Eksper ata | Evrak tam | İncelemede | SLA sayacını başlat | Takım lideri |
| T2 | İncelemede | Onayla | Tutar ≤ eksper limiti `[VARSAYIM]` | Onaylandı | Ödeme emri oluştur | Eksper |
| T3 | Açıldı, İncelemede | İptal et | Henüz karar yok | İptal (son) | Müşteriyi bilgilendir | Müşteri |

İzin yok: Onaylandı durumunda İptal → "Dosya karara bağlanmış" mesajıyla reddet. Açık soru: Reddedilen bir dosya itiraz sonrası yeniden açılabilir mi, kim açabilir?
