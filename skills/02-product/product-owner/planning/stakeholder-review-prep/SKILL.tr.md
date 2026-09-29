---
description: "Bir ürün veya paydaş değerlendirme toplantısını hazırlar: ne yapıldı ve neden, ürün hedefini nasıl ilerletiyor, kimden hangi geri bildirim gerekiyor, hangi kararlar alınmalı; demo akışı ve güncel görünümle birlikte bir gündem sunar. İterasyon/sprint değerlendirmesi, aylık ürün değerlendirmesi veya paydaşların ilerlemeyi inceleyip girdi vermesi gereken ürün kontrol noktalarından önce kullanılır."
related: "iteration-review-prep, demo-script, roadmap, feature-adoption-review, meeting-agenda"
prompt: "Satış ve operasyon direktörleriyle aylık ürün değerlendirme toplantımızı hazırla: toplu yükleme ve yeni fatura ekranını yayınladık; fiyatlandırma sayfası için karar ve mobil beta için geri bildirim almam gerekiyor."
---

# Ürün Değerlendirme Toplantısı Hazırlığı

## Amaç
Paydaş değerlendirmesini bir durum yayınından, geri bildirim ve karar üreten bir çalışma oturumuna dönüştürmek. Ürün sahibi toplantıdan doğrulanmış veya düzeltilmiş bir yön ve takip işleri için net sahiplerle çıkar.

## Ne zaman kullanılır
- İş paydaşlarıyla yapılacak iterasyon/sprint değerlendirmesi, aylık veya çeyreklik ürün değerlendirmesi öncesinde.
- Bekleyen paydaş kararları (kapsam, öncelik, bütçe, lansman) varsa.
- Yayınlanmış bir özellik için kullanıcılardan veya iş sahiplerinden yapılandırılmış geri bildirim gerekiyorsa.

## Ne zaman kullanılmaz
- Ekip seviyesinde demo sırası ve artım özeti için `iteration-review-prep` kullanılır.
- Projeler genelinde bütçe ve risk üzerine resmi bir yönetişim toplantısı için `steering-committee-pack` kullanılır.
- Yalnızca canlı demo akışı gerekiyorsa `demo-script` kullanılır.

## Girdiler
Zorunlu:
- Son değerlendirmeden bu yana teslim edilenler (maddeler, özellikler) ve güncel ürün hedefi.
- Toplantının hedef kitlesi. Yoksa sor; içerik kimin karar verdiğine bağlıdır.

İsteğe bağlı, kaliteyi artırır:
- Teslim edilen özelliklerin kullanım veya sonuç verisi.
- Bekleyen kararlar, açık riskler, yol haritası değişiklikleri.
- Şimdiye kadar alınan geri bildirimler, önceki toplantının aksiyon maddeleri.

## Süreç
1. Toplantının amacını tek satırda ve ürün sahibinin ihtiyaç duyduğu 1-3 çıktıyı tanımla (ör. X hakkında karar, Y hakkında geri bildirim, sonraki öncelikler üzerinde uzlaşma).
2. Hedef kitleyi eşle: kim neye karar verir, kim hangi geri bildirimi verir, kim yalnızca bilgilendirilir. Davetleri buna göre yap.
3. Yapılanları kullanıcı sonuçları cinsinden, hedeflere göre gruplayarak özetle; yapılmayanları ve nedenini belirt.
4. Kanıt topla: ilk kullanım, kalite veya destek sinyalleri. Yoksa başarı ima etmek yerine bunu açıkça söyle.
5. Her özellik için geri bildirim soruları yaz: somut, açık uçlu ve bir karara bağlı (ör. "Bu, ekibinizdeki mevcut Excel sürecinin yerini alır mı? Neyin engeli var?").
6. Her karar talebini şu yapıda yaz: bağlam, seçenekler, öneri, karar verilmezse sonucu, ne zamana kadar gerekli.
7. Görünümü güncelle: sırada ne var, yol haritasında veya sürüm planında değişiklikler, paydaş desteği gereken riskler.
8. Süreleri belli bir gündem oluştur: bağlam (kısa) → demo/gezinti → geri bildirim → kararlar → görünüm → aksiyonlar. Kararları zamanın yetmeme ihtimalinden önceye koy.
9. Tek sayfalık bir ön okuma ve geri bildirim ile kararları kaydetmek için bir takip şablonu hazırla.
10. Kullanıcının hedefi devam ediyorsa gösterimi senaryolaştırmak için `demo-script`, daveti göndermek için `meeting-agenda` öner.

## Çıktı formatı
```markdown
# Ürün Değerlendirmesi: <ürün> – <tarih>
Amaç: <tek satır> · Gereken çıktılar: <liste>
Katılımcılar: <ad/rol – karar verir / görüş verir / bilgilenir>

## Gündem (<toplam> dk)
| Süre | Konu | Sunan | Çıktı |
|---|---|---|---|

## Teslim Ettiklerimiz
| Hedef | Teslim edilen | Kullanıcı sonucu | Kanıt |
|---|---|---|---|
Yapılmayan: <madde – gerekçe>

## İhtiyaç Duyduğumuz Geri Bildirim
- <özellik>: <soru> – <kimden>

## Gereken Kararlar
### K1: <başlık>
Bağlam · Seçenekler · Öneri · Karar verilmezse · Gereken tarih

## Görünüm
- Sırada: ...
- Plandaki değişiklikler: ...
- Destek gereken riskler: ...

## Takip Şablonu
| Geri bildirim / karar | Sahip | Tarih |
|---|---|---|
```

## Kalite kontrol listesi
- [ ] Her karar talebinin seçenekleri, önerisi ve son tarihi var.
- [ ] Geri bildirim soruları somut ve bir karara veya sonraki adıma bağlı.
- [ ] Teslim edilen iş, kanıtla ya da açık bir "henüz veri yok" ifadesiyle sonuç olarak çerçevelenmiş.
- [ ] Teslim edilmeyen taahhütler gerekçeleriyle açıklanmış.
- [ ] Gündem yalnızca demoya değil, kararlara ve geri bildirime de zaman ayırıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Toplantıyı slayt tabanlı bir durum raporu gibi yürütmek. Çalışan yazılımı veya gerçek ekranları göster, zamanın çoğunu girdi almaya ayır.
- Sonda "geri bildirim var mı?" diye sormak. Her kitle için hedefli sorular hazırla.
- Kötü haberi gömmek. Kaymaları ve etkilerini güncellenmiş görünümle birlikte en başta açıkla.

## Örnek
Girdi: "Toplu yükleme ve yeni fatura ekranı yayınlandı; fiyatlandırma sayfası için karar, mobil beta için geri bildirim gerekiyor. Katılımcılar: satış ve operasyon direktörleri."

Çıktıdan bir bölüm:
- Geri bildirim: Toplu yükleme – "Bugün hangi müşteri dosyaları hâlâ yüklemede hata veriyor ve bunlarla kim ilgileniyor?" – Operasyon direktöründen.
### K1: Fiyatlandırma sayfasının yayınlanması
Seçenekler: 3 paketle şimdi yayınla / kurumsal paketi bekle. Öneri: şimdi yayınla. <tarih [TBD]> tarihine kadar karar verilmezse Q2 kampanyası kayar.
