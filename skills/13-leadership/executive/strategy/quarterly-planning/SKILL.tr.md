---
description: Bir teknoloji organizasyonu için çeyreklik planlama döngüsünü yürütür; stratejiyi ve talepleri kapasiteye dayalı taahhütlere, iddialı hedeflere (stretch) ve açık ödünleşimlere dönüştürür, bağımlılıkları ve riskleri görünür kılar. Bir CTO, başkan yardımcısı veya direktör ekiplerin gelecek çeyrekte neyi taahhüt edeceğine karar vermek zorunda olduğunda, talep kapasiteyi aştığında ya da önceki çeyrekler fazla taahhüt edilip eksik teslim edildiğinde kullanılır.
related: technology-strategy, capacity-planning, okr-definition, portfolio-prioritization, cross-team-dependency-board
prompt: 6 mühendislik ekibimiz için 3. çeyreği planlamama yardım et; işten 40 talep var, bir platform geçişi var ve kapasitenin %20'si zaten desteğe gidiyor.
---

# Çeyreklik Planlama

## Amaç
Yönetimin arkasında durabileceği bir çeyrek planı üretmek: gerçek kapasiteye göre boyutlanmış taahhütler, kısa bir iddialı hedef listesi ve nelerden neden vazgeçildiğinin görünür kaydı. Böylece iş birimi ne bekleyeceğini bilir, ekipler de aşırı yüklenmez.

## Ne zaman kullanılır
- Birden fazla ekip veya bir departman için gelecek çeyreğin planı hazırlanırken.
- İş talebi mühendislik kapasitesini açıkça aşıyor ve seçimlerin açıkça yapılması gerekiyorsa.
- Geçmiş çeyreklerde sürekli fazla taahhüt, devreden iş veya sık yeniden planlama görülüyorsa.

## Ne zaman kullanılmaz
- Çok yıllık yön ve seçimler için `technology-strategy` kullanılır.
- Kapasite eşlemesi olmadan bir proje portföyünü sıralamak için `portfolio-prioritization` kullanılır.
- Tek bir ekibin sonraki iterasyonunu planlamak için `iteration-planning` kullanılır.

## Girdiler
Zorunlu:
- Aday işler (girişimler, talepler, yükümlülükler) ve ilgili ekipler ile yaklaşık büyüklükleri.

İsteğe bağlı, kaliteyi artırır:
- Döneme ait strateji, OKR'ler veya iş hedefleri; geçen çeyreğin planı ile gerçekleşen teslimat.
- Kişi sayısı, planlı izinler, işe alım ve ayrılmalar; desteğe, olaylara ve bakıma giden kapasite payı.
- Bilinen son tarihler (mevzuat, sözleşme, etkinlik) ve ekipler arası bağımlılıklar.

Aday işler veya ekip yapısı yoksa iste. Kapasite rakamı uydurma; `[BİLİNMİYOR]` olarak işaretle ve kullanıcı teyit edene kadar göreli olarak planla.

## Süreç
1. Geçen çeyreği incele: planlanan ve teslim edilen, devreden işler ve kaymanın ana nedenleri. %100 varsaymak yerine gerçekçi bir teslimat oranı çıkar.
2. Ekip başına kullanılabilir kapasiteyi hesapla: kişi × iş günü, eksi izin, oryantasyon, nöbet, destek ve sistemi ayakta tutma payı. Yaptığın her tahmini `[VARSAYIM]` olarak etiketle.
3. Talepleri sınıflandır: zorunlu (mevzuat, sözleşme, güvenlik, destek sonu), stratejik (belirtilmiş bir hedefe bağlı), iyileştirme (teknik borç, güvenilirlik, geliştirici deneyimi) ve hedefi belirtilmemiş talepler.
4. Önce zorunlu işler için kapasite ayır, ardından yüzde olarak açık bir sağlık bütçesi (teknik borç, güvenilirlik) belirle; yüzdeyi ve kimin onayladığını yaz.
5. Kalan stratejik ve iyileştirme işlerini değer, aciliyet, risk azaltımı ve efora göre tek ve görünür bir yöntemle sırala; en yüksek sesle isteyene göre sıralama.
6. Gerçekçi kapasitenin yaklaşık %70-80'ini taahhütlerle doldur; sonraki işleri söz verilmediği açıkça belirtilen iddialı hedefler olarak listele.
7. Ekipler arası ve dış taraflara bağımlılıkları eşle; teyit edilmemiş bir bağımlılığa dayanan taahhüdü iddialı hedeflere taşı veya tarihli bir karar noktası ekle.
8. Ödünleşim listesini yaz: ertelenen veya reddedilen işler, gerekçesi ve bilgilendirilen talep sahibi. Paydaşlar için en önemli çıktı budur.
9. 3-5 çeyrek sonucu (görev listesi değil) ve çeyrek ortasında ilerlemenin nasıl görüleceğini tanımla.
10. Riskleri, varsayımları ve yeniden planlama kuralını (hangi olay değişikliği tetikler, kim karar verir) kaydet.
11. Yönetim için tek sayfalık özet çıkar; ekip düzeyindeki ayrıntıyı eke koy.
12. Kullanıcının hedefi devam ediyorsa sonuçları ifade etmek için `okr-definition`, bağımlılık takibi için `cross-team-dependency-board` veya kapasitenin artması gerekiyorsa `budget-proposal` öner.

## Çıktı formatı
```markdown
# Çeyrek Planı <çeyrek>: <organizasyon>

## Özet
- Bu çeyreğin sonuçları: ...
- Taahhütlere ayrılan kapasite: <gerçekçi kapasitenin %x'i>
- Temel ödünleşimler: ...

## Geçen Çeyrek Değerlendirmesi
| Planlanan | Teslim edilen | Devreden | Ana nedenler |
|---|---|---|---|

## Kapasite
| Ekip | Brüt | İzin/nöbet/destek | Sağlık bütçesi | Kullanılabilir | Dayanak |
|---|---|---|---|---|---|

## Taahhütler
| # | İş | Sınıf | Sonuç/hedef | Ekip(ler) | Büyüklük | Bağımlılıklar |
|---|---|---|---|---|---|---|

## İddialı Hedefler (söz verilmez)
- ...

## Ertelenen veya Reddedilen
| İş | Talep sahibi | Gerekçe | Tekrar bakılacak zaman |
|---|---|---|---|

## Riskler, Varsayımlar, Yeniden Planlama Kuralı
- [VARSAYIM] ...
- [RİSK] ...
- Yeniden planlama tetikleyicisi: <olay> – karar veren: <rol>
```

## Kalite kontrol listesi
- [ ] Kapasite izin, destek ve sağlık bütçesi düşülmüş net değer ve dayanağı gösterilmiş.
- [ ] Taahhütler gerçekçi kapasitenin en fazla yaklaşık %80'ini dolduruyor.
- [ ] Her taahhüt bir hedefe veya zorunlu bir yükümlülüğe bağlı.
- [ ] Ertelenen ve reddedilen işler gerekçe ve talep sahibiyle listelenmiş.
- [ ] Teyit edilmemiş taraflara olan bağımlılıklar taahhütlerin içinde gizlenmemiş.
- [ ] Uydurulmuş kişi sayısı, büyüklük veya tarih yok; tahminler `[VARSAYIM]` veya `[BİLİNMİYOR]` olarak etiketli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- %100 kapasiteyle planlamak. Plansız iş her zaman gelir; geçen çeyreğin gerçek oranını kullan.
- İçinde hiç "hayır" olmayan bir plan. Hiçbir şey ertelenmediyse önceliklendirme yapılmamıştır.
- Sonuç yerine iş listesi. Yönetim hangi kayıtların kapandığını değil, iş için neyin değiştiğini bilmek ister.

## Örnek
Girdi: 6 ekip, 40 iş talebi, bir platform geçişi, kapasitenin %20'si zaten destekte.

Çıktıdan bir bölüm:
- Kapasite: 6 ekip × ~`[VARSAYIM: 6 mühendis]` × 60 gün, eksi %20 destek ve %15 sağlık bütçesi, geçen çeyrekten teslimat oranı 0,8 `[teyit et]`.
- Zayıf sonuç (kaçın): "25 kayıt teslim et." Güçlü sonuç: "Ödeme servisi tüm trafikle birlikte yeni platformda canlıda çalışıyor."
- Reddedilen: Hedefi belirtilmemiş 14 talep – "bu hangi hedefi ilerletiyor?" sorusuyla talep sahiplerine iade edildi.
