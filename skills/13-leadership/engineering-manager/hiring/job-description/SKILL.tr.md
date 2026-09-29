---
name: job-description
description: "Bir yazılım rolü için rolün amacını, ilk yıl sonuçlarını, sorumlulukları, olmazsa olmaz ve tercih sebebi gereksinimleri, ekip bağlamını ve pratik bilgileri içeren kapsayıcı ve doğru bir iş ilanı yazar ve metni önyargılı veya dışlayıcı dil açısından kontrol eder. Yeni bir pozisyon açılırken, güncelliğini yitirmiş bir ilan yeniden yazılırken veya ilan yanlış adayları ya da çok az çeşitlilikte başvuru çektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: engineering-manager
  area: hiring
  title: "İş ilanı yazma"
  related: "role-definition, interview-plan, career-ladder, onboarding-plan-30-60-90, tone-rewrite"
  prompt: "İstanbul'daki platform ekibimiz için hibrit çalışan, Kafka ve Spark ile streaming pipeline'lar üzerinde çalışacak Kıdemli Veri Mühendisi ilanı yaz."
---

# İş İlanı Yazma

## Amaç
Rolün neyi başaracağını, gerçekte neyi gerektirdiğini ve burada çalışmanın nasıl olduğunu, nitelikli kişileri dışlamayan bir dille anlatarak doğru adayları çekmek ve adayların kendilerini doğru değerlendirmesini sağlamak.

## Ne zaman kullanılır
- Yeni bir pozisyon onaylandığında ve açık ilana ihtiyaç olduğunda.
- Mevcut ilan güncel değilse veya uyumsuz başvurular getiriyorsa.
- İşe alımda aday havuzu genişletilmek isteniyor ve metnin kapsayıcılık incelemesi gerekiyorsa.

## Ne zaman kullanılmaz
- Bir rolün kurum içi sorumlulukları ve karar yetkileri için `role-definition` kullanılır.
- Mülakat aşamalarını tasarlamak için `interview-plan` kullanılır.
- Mevcut çalışanların seviye beklentileri için `career-ladder` kullanılır.

## Girdiler
Zorunlu:
- Rol adı ve seviyesi, ekip ve rolün başarması gerekenler, temel teknolojiler veya alan.

İsteğe bağlı, kaliteyi artırır:
- Lokasyon, çalışma modeli (ofis/hibrit/uzaktan), istihdam türü, ücret aralığı (paylaşılıyorsa), yan haklar.
- Ekip büyüklüğü ve yapısı, raporlama hattı, ürün bağlamı.
- Şirket tanıtım metni ve fırsat eşitliği beyanı.
- İlanlara ilişkin yerel yasal gereklilikler.

Rolün amacı veya seviyesi belirsizse sor; ücret, yan hak veya şirket bilgisi uydurma, `[TBD]` olarak işaretle.

## Süreç
1. 2-3 cümlelik bir misyon yaz: rol neden var ve yaklaşık bir yıl sonra başarı neye benzer.
2. 4-6 sonucu veya sorumluluğu bağlamıyla birlikte fiillerle yaz ("sipariş event'leri için streaming pipeline'ları tasarla ve işlet"); görev listesi dökme.
3. Olmazsa olmazları tercih sebeplerinden ayır. Olmazsa olmazları ilk günden gerçekten gereken 4-6 maddeyle sınırla.
4. Deneyimi mümkün olduğunca yıl yerine yetkinlik olarak ifade et ("8+ yıl" yerine "ölçekli üretim veri pipeline'ları işletmiş").
5. Vekil işlevi gören gereksinimleri çıkar (belirli üniversiteler, gerekmediği halde diploma, profesyonel yetkinlik yeterliyken "anadil", "genç, dinamik" gibi yaşa gönderme yapan ifadeler).
6. Dil kontrolü: Cinsiyet kodlu veya dışlayıcı terimleri (rockstar, ninja, agresif, baskın) değiştir; "sen/siz" ve cinsiyetsiz dil kullan; Türkçede "bay/bayan" veya cinsiyetli unvanlardan kaçın.
7. Ekibi, teknik ortamı ve çalışma şeklini, varsa nöbet veya seyahat dahil, dürüstçe anlat.
8. Pratik bilgileri ekle: lokasyon, çalışma modeli, istihdam türü, izin verilirse ücret aralığı, makul düzenleme beyanı, başvuru şekli, süreç adımları.
9. Yerel mevzuat ve kurum politikasıyla uyumlu bir fırsat eşitliği ve düzenleme cümlesi ekle.
10. Uzunluğu (400-700 kelime) ve okunabilirliği kontrol et; bilinmeyen bilgileri `[TBD]` olarak işaretle.
11. Kullanıcının hedefi devam ediyorsa aynı gereksinimlere göre mülakat sürecini tasarlamak için `interview-plan` veya yeni çalışan için `onboarding-plan-30-60-90` öner.

## Çıktı formatı
```markdown
# <Unvan> (<seviye>) – <ekip>
Lokasyon / model: <...> · Tür: <...> · Ücret: <aralık veya [TBD]>

## Bu Rol Neden Var
<misyon, 2-3 cümle>

## Neler Yapacaksın
- ...

## Aradığımız Nitelikler (olmazsa olmaz)
- ...

## Tercih Sebebi
- ...

## Ekip ve Çalışma Şeklimiz
- ...

## Sunduklarımız
- ...

## İşe Alım Süreci
<adımlar, yaklaşık süre>

<Fırsat eşitliği ve makul düzenleme beyanı>
```

## Kalite kontrol listesi
- [ ] Misyon yalnızca görevleri değil sonuçları anlatıyor.
- [ ] Olmazsa olmazlar en fazla altı madde ve ilk günden gerçekten gerekli.
- [ ] Cinsiyet veya yaş kodlu ya da dışlayıcı dil yok; gereksiz diploma veya yıl şartı yok.
- [ ] Nöbet, seyahat ve çalışma modeli dürüstçe belirtildi.
- [ ] Uydurulmuş ücret, yan hak veya şirket iddiası yok; bilinmeyenler `[TBD]`.
- [ ] İşe alım süreci adımları listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- 15 teknolojilik istek listeleri. Tüm kriterleri karşılamadıkça başvurmayan nitelikli adayları caydırır. Fazlalıkları tercih sebebine taşı.
- Kurum içi kariyer basamağı metnini kopyalamak. Adayların kalibrasyon dili değil, sonuç ve bağlam görmesi gerekir.
- Ekibin gösteremeyeceği kültür özellikleri vaat etmek. Bunun yerine somut uygulamaları anlat.

## Örnek
Girdi: "Kıdemli Veri Mühendisi, İstanbul platform ekibi, hibrit, Kafka ve Spark ile streaming."

Çıktıdan bir bölüm:
- Bu rol neden var: Platform ekibimiz sipariş ve ödeme event'lerini ürün ve finans için güvenilir, neredeyse gerçek zamanlı veriye dönüştürüyor. Kritik streaming pipeline'ların sahibi olacak ve platform genelinde veri kalitesi çıtasını yükselteceksin.
- Olmazsa olmaz: Üretimde streaming pipeline tasarlamış ve işletmiş olmak (ör. Kafka ile Spark veya Flink).
- Ücret: `[TBD – aralığın yayımlanıp yayımlanamayacağını teyit et]`
