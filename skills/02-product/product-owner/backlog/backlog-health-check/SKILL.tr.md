---
description: "Bir backlog dökümünü veya listesini sağlık sorunları (bayat, tekrar eden, fazla büyük, sahipsiz, önceliksiz veya hedefsiz maddeler, çok fazla veya çok az hazır iş) açısından denetler; metriklerle bulgular, temizlik önerisi ve düzen kuralları üretir. Backlog yönetilemez hale geldiğinde, kimse ona güvenmediğinde, planlama döngüsünden önce ya da backlog'un temizlenmesi, denetlenmesi istendiğinde kullanılır."
related: "backlog-refinement, backlog-prioritization, definition-of-ready, roadmap, cycle-time-analysis"
prompt: "Ekte 340 maddelik backlog dökümümüz var (başlık, tür, oluşturma tarihi, son güncelleme, epic, durum). Sağlığını kontrol et ve neleri silmem gerektiğini söyle."
---

# Backlog Sağlık Kontrolü

## Amaç
Ürün sahibine backlog düzeni hakkında kanıta dayalı bir tablo ve somut bir temizlik planı vermek; böylece backlog bir dilek arşivi olmaktan çıkıp güncel stratejiyi yansıtan, güvenilir ve yönetilebilir bir araca dönüşür.

## Ne zaman kullanılır
- Backlog yüzlerce madde içeriyor ve kimse neyin önemli olduğunu söyleyemiyorsa.
- Çeyrek veya sürüm planlamasından önce ya da bir strateji değişikliğinden sonra.
- Yeni bir ürün sahibi bir ürünü devraldığında.
- Ekip belirsiz veya güncelliğini yitirmiş maddelerden yakınıyorsa.

## Ne zaman kullanılmaz
- Birkaç yaklaşan madde iyileştirilecekse `backlog-refinement` kullanılır.
- Maddeler sıralanacaksa `backlog-prioritization` kullanılır.
- Devam eden işlerin akış gecikmeleri analiz edilecekse `cycle-time-analysis` kullanılır.

## Girdiler
Zorunlu:
- Backlog listesi veya dökümü. Faydalı alanlar: ID, başlık, tür, durum, oluşturma tarihi, son güncelleme tarihi, üst epic/hedef, tahmin, sahip/talep eden. Veri verilmediyse iste; mevcut alanlarla çalış ve eksik olanları not et.

İsteğe bağlı, kaliteyi artırır:
- Güncel hedefler, yol haritası temaları veya OKR'lar.
- Ekip verimi (iterasyon/sprint başına veya haftalık tamamlanan madde).
- Kurum kuralları (ör. N aydan eski maddeler arşivlenir).

## Süreç
1. Veriyi profille: türe ve duruma göre madde sayısı, yaş dağılımı (medyan, 85. yüzdelik), üst hedefi, tahmini veya açıklaması olmayanların oranı.
2. Backlog derinliğini tahmin et: hazır veya hazıra yakın maddeler bölü verim, kaç hafta ya da iterasyonluk hazır iş olduğunu verir. Sağlıklı aralık kabaca 1-3 iterasyonluk hazır iştir; çok azsa (planlama açlığı) veya çok fazlaysa (israf) işaretle.
3. Bayat maddeleri bul: bir eşikten uzun süredir güncellenmemiş olanlar (varsayılan 6 ay `[VARSAYIM]` veya kurumun kuralı).
4. Benzer başlık veya aynı niyet üzerinden olası tekrarları bul; çiftleri güven notuyla listele.
5. Fazla büyük maddeleri bul: ekip normunun çok üstünde tahminler veya birden fazla yeteneği kapsayan belirsiz başlıklar.
6. Sahipsiz (orphan) maddeleri bul: bir epic'e, hedefe veya yol haritası temasına bağlı olmayanlar; ayrıca üst hedefi iptal edilmiş maddeler.
7. Sıralama kalitesini kontrol et: üstteki maddeler güncel hedeflerle uyumlu mu; hatalar ve teknik borç görünür mü, yoksa gömülü mü?
8. Her bulguyu gerekçesiyle sil/arşivle, birleştir, böl, yeniden bağla, iyileştir veya koru olarak sınıflandır.
9. Tekrarı önleyecek düzen kuralları (giriş filtresi, azami yaş, azami backlog boyutu, gözden geçirme sıklığı) ve ilk temizlik oturumu planı öner.

## Çıktı formatı
```markdown
# Backlog Sağlık Kontrolü: <ürün> – <tarih>
Veri: <n madde, mevcut alanlar, eksik alanlar>

## Sağlık Özeti
| Metrik | Değer | Sinyal |
|---|---|---|
| Toplam madde | <n> | |
| Medyan yaş / 85. yüzdelik | <gün> | |
| Bayat (> <eşik>) | <n, %> | Kırmızı/Sarı/Yeşil |
| Üst hedefi yok | <n, %> | |
| Hazır iş derinliği | <iterasyon/hafta veya [BİLİNMİYOR]> | |
| Olası tekrarlar | <çiftler> | |

## Bulgular ve Önerilen Aksiyon
| Madde(ler) | Sorun | Aksiyon | Gerekçe |
|---|---|---|---|

## Önerilen Düzen Kuralları
- <kural>

## İlk Temizlik Oturumu
- Kapsam, katılımcılar, süre, gereken kararlar
```

## Kalite kontrol listesi
- [ ] Metrikler yalnızca verilen veriden hesaplandı; eksik alanlar belirtildi.
- [ ] Kullanılan eşikler (bayatlık, boyut) açık ve varsayımsa işaretli.
- [ ] Tekrarlar otomatik silinmedi, güven notuyla aday olarak sunuldu.
- [ ] Önerilen her silmenin gerekçesi var ve ürün sahibi tarafından gözden geçirilebilir.
- [ ] Öneriler, verildiyse güncel hedeflere bağlanıyor.

## Sık yapılan hatalar
- Her şeyi "ne olur ne olmaz" diye tutmak. Gerçek değeri olan maddeler geri gelir; biriktirmek yerine notla arşivle.
- Yalnızca boyutu ölçmek. Birbiriyle ilgisiz maddelerden oluşan küçük bir backlog da sağlıksızdır; hedef uyumunu kontrol et.
- Kural koymadan bir kez temizlemek. Giriş filtresi ve gözden geçirme sıklığı olmadan backlog birkaç ayda yeniden şişer.

## Örnek
Girdi: "340 madde; alanlar: başlık, tür, oluşturma, güncelleme, epic."

Çıktıdan bir bölüm:
| Bayat (> 180 gün) | 142 (%42) | Kırmızı |
| Üst epic'i yok | 97 (%29) | Sarı |
- "Excel'e aktar" (#88) ve "Listeyi XLSX olarak indir" (#231) – olası tekrar, yüksek güven – #231 altında birleştir.
- Düzen kuralı: 180 gün güncellenmeyen maddeler, ürün sahibi yeniden onaylamadıkça aylık gözden geçirmede arşivlenir.
