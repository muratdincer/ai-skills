---
name: project-status-report
description: "Genel ve boyut bazında RAG durumunu (takvim, maliyet, kapsam, kalite, kaynak), kilometre taşlarına göre ilerlemeyi, sapma açıklamalarını, öncelikli riskleri ve sorunları ve sponsorlardan gereken kararları içeren dönemsel proje durum raporunu yazar. Sponsorlara veya yönlendirme kurullarına haftalık ya da aylık raporlamada veya proje sağlığının plan ve gerçekleşme verisinden nesnel olarak özetlenmesi gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: monitoring
  title: "Proje durum raporu"
  related: "status-update, steering-committee-pack, earned-value-analysis, raid-log, executive-summary"
  prompt: "İK sistemi projesinin bu ayki durum raporunu bu kilometre taşı güncellemeleri, bütçe gerçekleşmeleri ve RAID kaydından yaz."
---

# Proje Durum Raporu

## Amaç
Sponsorlara, baz çizgisine göre proje sağlığının dürüst ve kanıta dayalı bir görünümünü ve vermeleri gereken kararların net listesini iki dakikada okunabilecek bir formatta sunmak.

## Ne zaman kullanılır
- Sponsora, yönlendirme kuruluna veya PMO'ya düzenli raporlama döngüsünde.
- Karar gerektiren bir yönetişim toplantısından önce.
- Durumun dağınık güncellemelerden ve verilerden yeniden kurulması gerektiğinde.

## Ne zaman kullanılmaz
- Baz çizgisine bağlı olmayan kısa bir ekip veya birimler arası güncelleme için `status-update` kullanılır.
- Finansallar ve seçenekler içeren tam yönlendirme kurulu paketi için `steering-committee-pack` kullanılır.
- Değer anlatısıyla dış müşteriye raporlama için `client-steering-report` kullanılır.

## Girdiler
Zorunlu:
- Raporlama dönemi ve baz çizgisi (kilometre taşları, bütçe) veya son rapor.
- İlerleme verisi: kilometre taşı durumu, tamamlanan işler, gerçekleşen maliyet veya efor.

İsteğe bağlı, kaliteyi artırır:
- RAID kaydı, değişiklik talepleri, kazanılmış değer metrikleri, ekip güncellemeleri, kurumsal RAG tanımları.

İlerleme verisi yoksa iste. Sessizlikten durum çıkarma.

## Süreç
1. Verilmişse kurumsal kuralları kullanarak RAG eşiklerini tanımla; yoksa: Yeşil tolerans içinde, Sarı tolerans riskte ama PM tarafından düzeltilebilir, Kırmızı tolerans aşıldı veya sponsor aksiyonu gerekli. Eşikleri belirt.
2. Her boyutu (takvim, maliyet, kapsam, kalite, kaynak) baz çizgisine göre kanıtla (tarihler, tutarlar, sayılar) değerlendir.
3. Genel durumu belirle: hedefleri etkileyen en kötü boyuttan daha iyi olamaz; farklıysa açıkla.
4. Önceki döneme göre eğilimi göster (iyileşiyor, sabit, kötüleşiyor).
5. Kilometre taşlarını listele: baz tarih, öngörülen tarih, sapma, durum.
6. Dönemin kazanımlarını ve gelecek dönemin planını özetle (faaliyet değil sonuç).
7. Sahip, aksiyon ve tarihle ilk 3-5 risk ve sorunu çek.
8. Gereken kararları seçenekler, öneri ve son tarihle açık talepler olarak formüle et.
9. 3 cümlelik yönetici özetini en son yaz.
10. Eksik veriyi `[BİLİNMİYOR]` olarak işaretle ve Kırmızı durumu gizleyen yumuşatıcı dilden kaçın.
11. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: altta yatan kayıtları güncellemek için `raid-log`, maliyet ve takvim endeksleri gerekiyorsa `earned-value-analysis` ya da karar toplantısı için `steering-committee-pack`.

## Çıktı formatı
```markdown
# Proje Durum Raporu: <proje> – <dönem>
Genel: <RAG> (eğilim <↑/→/↓>) | PM <ad> | Tarih <tarih>
## Yönetici Özeti
## Boyut Bazında Durum
| Boyut | RAG | Eğilim | Kanıt / sapma | Düzeltme aksiyonu |
## Kilometre Taşları
| Kilometre taşı | Baz | Öngörü | Sapma | Durum |
## Bu Dönemin Kazanımları
## Gelecek Dönem Planı
## Öncelikli Riskler ve Sorunlar
| No | Açıklama | Sahip | Aksiyon | Tarih |
## Gereken Kararlar
| Karar | Seçenekler | Öneri | Son tarih |
## RAG Tanımları
```

## Kalite kontrol listesi
- [ ] Her RAG değeri baz çizgisine göre kanıtla destekleniyor.
- [ ] Genel durum boyut durumlarıyla tutarlı.
- [ ] Kararlar son tarihli açık talepler olarak yazıldı.
- [ ] Karpuz raporlama yok: sorunlar metne gömülmemiş, görünür.
- [ ] Eksik veri Yeşil varsayılmadı, işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Birden Kırmızıya dönene kadar Yeşil göstermek. Sarıyı erken ve düzeltme planıyla raporla.
- Sonuç yerine faaliyet listesi ("tedarikçiyle toplantılar yapıldı"). Neyin değiştiğini raporla.
- Kararları risk metninin içine gizlemek. Talepleri ayrı bölüme koy.

## Örnek
Girdi: "UAT başlangıcı 1 Mart'tan 15 Mart'a kaydı; %55 tamamlanmada bütçenin %62'si harcandı; tedarikçi kaynağı değişti."

Çıktıdan bir bölüm:
| Takvim | Sarı | ↓ | UAT başlangıcı +2 hafta; tampon kullanılarak canlıya geçiş hâlâ mümkün | Paralel test verisi hazırlığı |
| Maliyet | Sarı | → | %55 tamamlanmaya karşı %62 harcama `[EV yöntemini teyit et]` | Tedarikçi harcama hızının gözden geçirilmesi |
- Gereken karar: UAT için 1 haftalık proje tamponunun kullanımının onayı — son tarih 5 Mart.
