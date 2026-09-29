---
description: Her hedef kitle için hangi bilgiyi, ne zaman ve hangi sıklıkta, hangi kanaldan, kimden alacağını ve geri bildirim ile eskalasyonların nasıl geri akacağını belirleyen proje iletişim planını oluşturur. Proje başında, paydaşlar bilgisiz kaldıklarından veya aşırı yüklendiklerinden şikayet ettiğinde ya da yönetişim ve raporlama ritimleri üzerinde anlaşılması gerektiğinde kullanılır.
related: stakeholder-register, project-status-report, governance-framework, status-update, announcement
prompt: Ana bankacılık yükseltmemiz için yöneticileri, şube personelini, BT operasyonu ve tedarikçiyi kapsayan bir iletişim planı oluştur.
---

# İletişim Planı

## Amaç
Her paydaş grubunun doğru bilgiyi doğru ayrıntı ve sıklıkta, net göndericiler ve geri bildirim yollarıyla almasını sağlamak; böylece hem sürprizler hem de gürültü en aza iner.

## Ne zaman kullanılır
- Başlatma aşamasında, paydaş kaydı taslağı hazırlandıktan sonra.
- Eksik bilgi ya da çok fazla mesaj konusunda şikayetler çıktığında.
- Daha sıkı iletişim gerektiren kritik fazlardan (geçiş, canlıya alma, sistem kapatma) önce.

## Ne zaman kullanılmaz
- Tek bir mesaj veya güncelleme yazılacaksa `status-update` veya `stakeholder-email` kullanılır.
- Karar yetkileri ve kurullar tanımlanacaksa `governance-framework` kullanılır.
- Organizasyonel yeniden yapılanma için değişim iletişimi gerekiyorsa `org-change-communication` kullanılır.

## Girdiler
Zorunlu:
- İlgi alanlarıyla birlikte paydaş listesi veya kaydı.
- Temel proje yönetişimi (sponsor, yönlendirme kurulu, PM).

İsteğe bağlı, kaliteyi artırır:
- Mevcut kurumsal kanallar ve araçlar, dil ihtiyaçları, saat dilimleri.
- Kilometre taşları ve hassas olaylar (geçiş, işten çıkarmalar, tedarikçi değişiklikleri).

Paydaş listesi yoksa iste ya da önce hızlı bir belirleme yap.

## Süreç
1. Benzer ihtiyaçları olan kitleleri grupla; karar vericileri tek tek tut.
2. Her kitle için bilgi ihtiyacını tanımla: kararlar, ilerleme, onlara etkisi, gereken aksiyonlar.
3. Format ve ayrıntı düzeyini seç (gösterge paneli, tek sayfalık rapor, brifing, demo, bülten).
4. Sıklığı ve zamanlamayı karar döngülerine bağla (ör. yönlendirme toplantısından önce durum raporu).
5. Erişim ve gizliliği gözeterek kanal seç (toplantı, e-posta, intranet, sohbet kanalı, portal).
6. Her iletişime bir gönderici/sahip ve bir yedek ata.
7. Geri bildirim ve eskalasyon yollarını tanımla: kitleler nasıl soru sorar veya kaygı iletir, yanıt süresi nedir.
8. Olay tetiklemeli iletişimleri ekle: canlıya geçiş, olaylar, gecikmeler, kapsam değişiklikleri; hassas mesajlar için onay kuralları.
9. Etkinliğin nasıl kontrol edileceğini (katılım, okunma oranı, nabız soruları, paydaş geri bildirimi) ve planın gözden geçirme sıklığını tanımla.
10. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: ilk planlı mesajı üretmek için `project-status-report` veya `status-update`.

## Çıktı formatı
```markdown
# İletişim Planı: <proje>
## İletişim Matrisi
| Kitle | Bilgi ihtiyacı | Format | Sıklık / zamanlama | Kanal | Sahip (yedek) | Geri bildirim yolu |
## Olay Tetiklemeli İletişimler
| Tetikleyici | Kitle | Mesaj sahibi | Onaylayan | Ön süre |
## Eskalasyon Yolu
## Etkinlik Ölçütleri
## Takvim (ilk 3 ay)
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Etkisi yüksek her paydaş matriste yer alıyor.
- [ ] Her iletişimin bir sahibi ve net bir amacı var.
- [ ] Zamanlama keyfi değil, karar noktalarına bağlı.
- [ ] Hassas iletişimlerin bir onaylayanı var.
- [ ] Yalnızca giden mesajlar değil, geri bildirim yolları da var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Herkese tek bir durum raporu. Derinliği uyarla: yöneticiler karar ve risk, ekipler ayrıntı ister.
- Çok fazla tekrarlayan toplantı planlamak. Tartışma gerekmiyorsa asenkron güncellemeyi tercih et.
- Canlıya geçişten önce servis masası ve operasyon gibi dolaylı kitleleri unutmak.

## Örnek
Girdi: "Ana bankacılık yükseltmesi; yöneticiler, şube personeli, BT operasyonu, tedarikçi."

Çıktıdan bir bölüm:
| Şube personeli | Onlar için ne değişiyor, ne zaman, eğitim | 1 sayfalık bülten + kısa video | İki haftada bir; T-4 haftadan itibaren haftalık | İntranet + şube müdürü brifingi | Değişim sorumlusu (PM) | Sorular şube müdürleri üzerinden, 2 günde yanıt |
