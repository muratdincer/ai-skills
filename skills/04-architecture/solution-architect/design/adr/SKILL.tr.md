---
description: Bağlamı, karar etkenlerini, artı ve eksileriyle değerlendirilen seçenekleri, kararı ve sonuçlarını Nygard veya MADR tarzında, durum ve yerine geçme bağlantılarıyla birlikte kaydeden bir Mimari Karar Kaydı (ADR) yazar. Mimari açıdan önemli bir karar verildiğinde veya verilmesi gerektiğinde, geçmiş bir kararın geriye dönük belgelenmesi gerektiğinde ya da bir karar geri alınırken kullanılır.
related: decision-log, trade-off-analysis, technology-selection, solution-architecture-document, architecture-principles
prompt: Sipariş servisi için MongoDB yerine PostgreSQL seçimimizle ilgili bir ADR yaz; etkenler işlemsel tutarlılık, ekip yetkinliği ve raporlama ihtiyaçları.
---

# Mimari Karar Kaydı (ADR) Yazma

## Amaç
Mimari açıdan önemli tek bir kararı kaydederek gelecekteki okuyucuların tartışmayı yeniden kurmadan neye, neden karar verildiğini, başka nelerin değerlendirildiğini ve bedelinin ne olduğunu anlamasını sağlamak.

## Ne zaman kullanılır
- Karar yapıyı, kalite niteliklerini, arayüzleri, bağımlılıkları veya derleme/dağıtım yaklaşımını etkiliyor ve geri alınması zorsa.
- Bir karar toplantıda veya sohbette alınmış ve hiçbir yerde yazılı değilse.
- Önceki bir ADR'nin yerine yenisi geçiyor veya geçersiz kılınıyorsa.
- Bir ilkeye istisna tanınıyorsa.

## Ne zaman kullanılmaz
- Günlük iş veya proje kararları için `decision-log` kullanılır.
- Seçenekler hâlâ çok açıksa ve önce yapılandırılmış bir karşılaştırma gerekiyorsa `trade-off-analysis` veya `technology-selection` kullanılır, sonuç burada kaydedilir.
- Çözümün tamamı belgelenecekse `solution-architecture-document` kullanılır.

## Girdiler
Zorunlu:
- Karar sorusu (veya alınmış karar) ve bağlamı.
- Değerlendirilen seçenekler ya da gerçekçi seçenekleri belirlemeye yetecek bağlam.

İsteğe bağlı:
- Karar etkenleri: kalite nitelikleri, kısıtlar, ilkeler, maliyetler, son tarihler.
- Katılımcılar, tarih, ilgili ADR'ler, kanıtlar (spike, benchmark, PoC).
- Tercih edilen şablon (Nygard kısa biçim veya MADR).

Karar sorusu belirsizse sor. Karar henüz verilmediyse ADR'yi Önerildi durumuyla ve bir öneriyle yaz.

## Süreç
1. Önemi kontrol et: kolay geri alınabilen ve tek bir bileşene özgü bir kararsa kod yorumu veya tasarım notu öner.
2. Başlığı kararın kısa bir isim öbeği olarak yaz ("Sipariş kalıcılığı için PostgreSQL kullanımı"); ekip kullanıyorsa sıra numarası ver.
3. Bağlamı tarafsız anlat: etkenler, kısıtlar, mevcut durum, kararı neyin tetiklediği. Burada hiçbir seçeneği savunma.
4. Karar etkenlerini adlandırılmış ve sıralanmış ölçütler olarak listele (ör. "sipariş satırları arasında işlemsel tutarlılık", "ekip deneyimi", "raporlama sorguları").
5. İlgiliyse "hiçbir şey yapma / mevcut hâli koru" dahil 2-4 gerçekçi seçenek listele.
6. Her seçenek için etkenlere göre artı ve eksileri yaz; kanıta atıf yap veya `[VARSAYIM]` olarak işaretle.
7. Kararı etken çatı kipinde tek cümleyle yaz ("... kullanacağız") ve en önemli etkenlerde neden öne çıktığını belirt.
8. Sonuçları yaz: olumlu, olumsuz (maliyetler, riskler, yeni borç) ve sorumlusu belli takip aksiyonları.
9. Durumu (Önerildi, Kabul edildi, Geçersiz, ADR-n ile değiştirildi) ve tarihi belirle; ilgili veya yerine geçilen ADR'leri bağla.
10. Bir gözden geçirme tetikleyicisi ekle: bu kararın hangi koşulda yeniden ele alınacağı.
11. Hedef devam ediyorsa ADR'ye atıf için `solution-architecture-document`, ilişkili mimari olmayan kararlar için `decision-log` öner.

## Çıktı formatı
```markdown
# ADR-<n>: <karar başlığı>
Durum: <Önerildi | Kabul edildi | Geçersiz | ADR-x ile değiştirildi> · Tarih: <tarih> · Karar vericiler: <roller veya [BİLİNMİYOR]>

## Bağlam
## Karar Etkenleri
1. ...
## Değerlendirilen Seçenekler
- Seçenek A – <ad>
- Seçenek B – <ad>
## Seçeneklerin Artı ve Eksileri
### Seçenek A
- İyi, çünkü ...
- Kötü, çünkü ...
## Karar
<karar> kullanacağız, çünkü <en önemli etkenler>.
## Sonuçlar
- Olumlu: ...
- Olumsuz: ...
- Takip: <aksiyon – sorumlu>
## Gözden Geçirme Tetikleyicisi
## Bağlantılar
```

## Kalite kontrol listesi
- [ ] ADR başına tek karar var; başlık problemi değil kararı belirtiyor.
- [ ] Bağlam tarafsız ve bir yıl sonra ekibe katılan birinin anlayacağı düzeyde.
- [ ] En az iki gerçek seçenek, adlandırılmış etkenlere göre artı ve eksileriyle değerlendirildi.
- [ ] Olumsuz sonuçlar dürüstçe listelendi.
- [ ] Durum, tarih ve bağlantılar belirlendi; karar verici veya tarih uydurulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Yalnızca seçimi haklı çıkarmak için eklenmiş göstermelik alternatifler. Yetkin bir ekibin seçebileceği seçenekleri ekle.
- Kabul edilmiş bir ADR'yi kararı değiştirmek için düzenlemek. Yeni bir ADR yaz ve eskisini değiştirildi olarak işaretle.
- Bağlamda "neden şimdi" sorusunu atlamak; karar sonradan keyfi görünür.

## Örnek
Girdi: "Sipariş servisi için MongoDB yerine PostgreSQL seçtik; tutarlılık, yetkinlik ve raporlama önemli."

Çıktıdan bir bölüm:
- Başlık: ADR-012: Sipariş Servisi Kalıcılığı için PostgreSQL Kullanımı
- Karar: Siparişleri PostgreSQL'de saklayacağız, çünkü çok satırlı işlemsel tutarlılık ve SQL ile raporlama en üst sıradaki etkenler ve ekip bugün PostgreSQL işletiyor.
- Olumsuz sonuç: Şema değişiklikleri pipeline'da migration script'leri gerektirir; esnek nitelikler doğrulamalı JSONB ile tutulacak.
- Gözden geçirme tetikleyicisi: Sipariş yazma hacmi tek bir birincil sunucunun kaldırabileceğini aşarsa `[eşik yük testinden sonra TBD]`.
