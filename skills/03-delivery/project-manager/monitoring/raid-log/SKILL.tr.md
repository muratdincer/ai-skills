---
description: Riskleri, Varsayımları, Sorunları ve Bağımlılıkları tutarlı numaralar, sahipler, tarihler, durumlar ve çapraz bağlantılarla tek yerde izleyen RAID kaydını oluşturur veya günceller ve neyin değiştiğine ve neyin dikkat gerektirdiğine dair kısa bir özet üretir. Süregelen proje kontrolünde, ham notların, toplantı çıktılarının veya e-postaların doğru RAID kategorisine ayrılması gerektiğinde ya da durum raporlamasından önce kullanılır.
related: risk-register, issue-management, dependency-map, decision-log, project-status-report
prompt: Bugünkü yönlendirme toplantısı notlarındaki maddelerle RAID kaydımızı güncelle ve neyin eskale edilmesi gerektiğini söyle.
---

# RAID Kaydı Tutma

## Amaç
Riskler, varsayımlar, sorunlar ve bağımlılıklar için doğru sınıflandırılmış ve sahipli, tek ve güncel bir kontrol kaydı tutmak; böylece toplantılarda veya e-postalarda dile getirilen hiçbir şey kaybolmaz ve raporlama tek kaynaktan beslenir.

## Ne zaman kullanılır
- Haftalık proje kontrolünde ve durum raporlarından önce.
- Yeni kaygıların dile getirildiği toplantılar, çalıştaylar veya eskalasyonlardan sonra.
- Eski bir kayıt dağınıksa ve temizlenip yeniden sınıflandırılması gerekiyorsa.

## Ne zaman kullanılmaz
- Bir geçiş kapısı için ayrıntılı, puanlı risk analizi gerekiyorsa `risk-register` kullanılır.
- Önemli tek bir sorunu çözüme kadar yönetmek için `issue-management` kullanılır.
- Kararları gerekçeleriyle kaydetmek için `decision-log` kullanılır.

## Girdiler
Zorunlu:
- Yeni ham maddeler (notlar, e-postalar, toplantı çıktıları) ve/veya mevcut RAID kaydı.

İsteğe bağlı, kaliteyi artırır:
- Proje planı ve kilometre taşları, kurumsal ölçekler, eskalasyon eşikleri.

Ne yeni madde ne de mevcut kayıt verilmişse iste.

## Süreç
1. Her ham maddeyi testlerle sınıflandır: Risk = gelecekteki belirsiz olay; Varsayım = doğru kabul edilen ama henüz doğrulanmamış; Sorun = şu an yaşanan ve projeyi etkileyen; Bağımlılık = başka bir taraftan veya başka bir taraf için gereken şey.
2. Mevcut kayıtlarla tekrarları ayıkla; yenisini açmak yerine mevcut olanı güncelle.
3. Her kaydı kesin yaz (riskler neden-olay-etki, sorunlar mevcut etki, varsayımlar doğrulama yöntemi, bağımlılıklar gereken tarih ile).
4. Sahip, bitiş veya gözden geçirme tarihi, öncelik (Y/O/D veya puan) ve durum ata.
5. Çapraz bağla: geçersiz çıkan varsayımlar sorun veya riske, kayan bağımlılıklar soruna, gerçekleşen riskler soruna dönüşür.
6. Yaşlandır: iki gözden geçirme döngüsünden uzun süredir güncellenmeyen kayıtları ve gecikmiş aksiyonları işaretle.
7. Eskalasyon adaylarını belirle: PM düzeyinde uygulanabilir aksiyonu olmayan Yüksek öncelikliler veya kritik yolda gecikmiş olanlar.
8. Kayıtları kapanış notu ve tarihle kapat; silme.
9. Değişiklik özeti üret: yeni, değişen, kapanan, eskalasyonlar.

## Çıktı formatı
```markdown
# RAID Kaydı: <proje> – güncelleme <tarih>
## Değişiklik Özeti
- Yeni: ... | Kapanan: ... | Eskale: ...
## Riskler
| No | Açıklama | O | E | Sahip | Yanıt / aksiyon | Tarih | Durum |
## Varsayımlar
| No | Varsayım | Doğrulama yöntemi | Sahip | Doğrulama tarihi | Durum (Açık/Geçerli/Geçersiz) |
## Sorunlar
| No | Açıklama | Etki | Öncelik | Sahip | Aksiyon | Tarih | Durum |
## Bağımlılıklar
| No | Öğe | Sağlayan | Alan | Gereken tarih | Durum |
## Bayat veya Gecikmiş Kayıtlar
```

## Kalite kontrol listesi
- [ ] Her kayıt kendi kategori testini geçiyor.
- [ ] Tekrar yok; güncellemeler mevcut numaralara uygulandı.
- [ ] Her açık kaydın sahibi ve tarihi var.
- [ ] Geçişler (varsayım → sorun, risk → sorun) bağlantılarıyla kaydedildi.
- [ ] Eskalasyon adayları açıkça belirtildi.

## Sık yapılan hatalar
- Sponsorları telaşlandırmamak için sorunları risk olarak kaydetmek. Şu an oluyorsa sorundur.
- Doğrulama tarihi olmayan varsayımlar; bunlar sessizce soruna dönüşür.
- Kaydı kapatmadan büyütmek; bayat kayıtlar gerçek olanları gizler.

## Örnek
Girdi: "Yönlendirme notları: tedarikçi API dokümanlarını gelecek hafta verecek; 2 test ortamı varsayıyoruz; veri merkezi taşıması geçişle çakışabilir."

Çıktıdan bir bölüm:
- B-07 Tedarikçiden API dokümantasyonu – Gereken tarih `[tarih]` – Durum Talep edildi.
- V-04 4. sprintten itibaren iki test ortamı mevcut – Altyapı ile `[TBD]` tarihine kadar doğrulanacak – Açık.
- R-12 Veri merkezi taşıması geçişe yakın planlandığı için altyapı değişiklikleri çakışabilir ve canlıya geçişi geciktirebilir – O3/E4 – Sahip Altyapı sorumlusu.
