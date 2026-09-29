---
name: project-charter
description: "Projeyi resmi olarak yetkilendiren proje başlatma belgesini (project charter) hazırlar; amaç, ölçülebilir hedefler, üst düzey kapsam, kilit paydaşlar, bütçe zarfı, kilometre taşları, riskler ve proje yöneticisinin yetkilerini içerir. Bir proje onaylandığında ya da onay beklerken sponsor tarafından imzalanacak tek belgelik bir yetki metni gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: initiation
  title: "Proje başlatma belgesi"
  related: "scope-statement, stakeholder-register, kickoff-deck, business-model-canvas, governance-framework"
  prompt: "Şirket içi CRM'imizi SaaS platforma taşıma projesi için proje başlatma belgesi yaz; sponsor Satış Direktörü, hedef canlıya geçiş 2. çeyrek."
---

# Proje Başlatma Belgesi

## Amaç
Projeyi yetkilendiren, iş gerekçesine bağlanan ve proje yöneticisinin eskalasyona gerek kalmadan hareket edebileceği sınırları tanımlayan, sponsor onaylı kısa bir yetki belgesi üretmek.

## Ne zaman kullanılır
- Bir iş durumu (business case) veya talep onaylandığında ve projenin resmi olarak başlatılması gerektiğinde.
- Gayriresmi yürüyen bir projeye açık bir yetki, sponsor ve yetki sınırı tanımlanması gerektiğinde.
- Hedeflerde veya sponsorda büyük bir değişiklik sonrası yeniden baz çizgisi (re-baseline) oluşturulurken.

## Ne zaman kullanılmaz
- Teslimatlar ve kabul kriterleriyle ayrıntılı kapsam gerekiyorsa `scope-statement` kullanılır.
- Yatırım kararı henüz verilmemişse `feasibility-study` veya `cost-benefit-analysis` kullanılır.
- Mevcut bir ürün backlog'u içindeki küçük bir değişiklikse `feature-brief` kullanılır.

## Girdiler
Zorunlu:
- Proje adı ve iş ihtiyacı ya da onaylanmış iş durumu (herhangi bir formatta).
- Sponsorun adı veya rolü.

İsteğe bağlı, kaliteyi artırır:
- Bütçe zarfı, hedef tarihler ve bunları belirleyen etkenler, bilinen kısıtlar.
- Kurumsal belge şablonu, yönetişim kurulları, onay eşikleri.
- İlgili programlar, sözleşmeler veya mevzuat kaynaklı gereklilikler.

İş ihtiyacı veya sponsor yoksa iste. Diğer her şey açık sorulara gider.

## Süreç
1. İş ihtiyacını problem/fırsat olarak yeniden yaz ve bir stratejik hedefe ya da etkene (mevzuat, maliyet, gelir, risk) bağla.
2. 3-5 SMART hedef tanımla. Proje hedeflerini (kapanışta teslim edilir) iş faydalarından (sonradan gerçekleşir, sahibi iş birimidir) ayır.
3. Üst düzey kapsam içi/dışı ve ana teslimatları yaz. Ayrıntıyı kapsam tanımına bırak.
4. Kilometre taşlarını yalnızca verilen tarihlerle yaz; yoksa `[TBD]` işaretle ve tarihi neyin belirlediğini belirt.
5. Bütçe zarfını ve finansman kaynağını kaydet. Asla rakam uydurma; `[BİLİNMİYOR]` işaretle, biliniyorsa onay eşiğini yaz.
6. Sponsoru, proje yöneticisini, kilit paydaşları ve yönlendirme kurulunu belirle.
7. PM yetkisini tanımla: eskalasyonsuz karar verilebilecek bütçe sapması, takvim sapması ve kadro kararları ile eskalasyon yolu.
8. İlk 5 riski, varsayımları ve kısıtları özet düzeyde kaydet.
9. Proje kapanışı için başarı kriterlerini ve bunları kimin kabul edeceğini tanımla.
10. Onay bloğu ekle ve açık soruları açılış toplantısını ne kadar engellediklerine göre sırala.
11. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: kapsamı detaylandırmak için `scope-statement`, paydaşları eşlemek için `stakeholder-register`, ardından `kickoff-deck`.

## Çıktı formatı
```markdown
# Proje Başlatma Belgesi: <ad>
| Alan | Değer |
|---|---|
| Sponsor | <ad/rol> |
| Proje yöneticisi | <ad veya [TBD]> |
| Sürüm / tarih | <v0.1, tarih> |
| Bütçe zarfı | <tutar + kaynak veya [BİLİNMİYOR]> |
| Hedef bitiş | <tarih + etken veya [TBD]> |

## İş İhtiyacı ve Stratejik Uyum
## Hedefler (SMART)
| # | Hedef | Ölçüt | Hedef değer | Tarih |
## Beklenen Faydalar (sahibi iş birimi)
## Üst Düzey Kapsam
- İçinde: ... / Dışında: ...
## Ana Teslimatlar
## Kilometre Taşları
| Kilometre taşı | Hedef tarih | Belirleyen etken |
## Paydaşlar ve Yönetişim
## PM Yetkisi ve Eskalasyon
| Karar | PM'in karar sınırı | Eskalasyon |
## Özet Riskler, Varsayımlar, Kısıtlar
## Kapanış İçin Başarı Kriterleri
## Açık Sorular
## Onaylar
| Rol | Ad | Karar | Tarih |
```

## Kalite kontrol listesi
- [ ] Her hedef ölçülebilir ve zamana bağlı.
- [ ] Hedefler ile iş faydaları karıştırılmadı.
- [ ] PM yetki sınırları açık sayı veya kural olarak yazıldı ya da `[TBD]` işaretli.
- [ ] Hiçbir bütçe, tarih veya isim uydurulmadı.
- [ ] Kapsam dışı maddeler listelendi.
- [ ] Belge yaklaşık iki sayfaya sığıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Belgeye çözüm tasarımı yazmak. Yetki düzeyinde kal; tasarım sonra gelir.
- Yetkiyi tanımsız bırakıp her kararı sponsora taşımak. Tolerans belirle.
- Başlatma belgesini durum raporu gibi kullanmak. Onaydan sonra dondur, yalnızca `change-control` ile değiştir.

## Örnek
Girdi: "SaaS CRM geçişi için başlatma belgesi, sponsor Satış Direktörü, canlıya geçiş 2. çeyrek, mevcut lisans Haziran'da bitiyor."

Çıktıdan bir bölüm:
- Hedef 1: Aktif hesapların ve açık fırsatların %100'ünü lisans bitiminden önce SaaS CRM'e taşımak `[tarihi teyit et]`.
- PM yetkisi: 2 haftaya kadar takvim sapması eskalasyonsuz `[VARSAYIM]`; üstü yönlendirme kurulu.
- Açık soru: 5 yıldan eski kapalı hesapların arşivlenmesi kapsamda mı?
