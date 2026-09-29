---
description: Bir sistemin, projenin, servisin, iş akışının veya rolün sahipliğini yeni sahibine devreden bir devir-teslim dokümanı yazar; bağlamı, mevcut durumu, sorumlulukları, iletişim kişilerini, erişimleri, periyodik görevleri, riskleri, açık işleri ve kabul noktası olan bir geçiş planını kapsar. Biri ayrıldığında, rol değiştirdiğinde, uzun izne çıktığında, bir proje teslimattan operasyona geçtiğinde, tedarikçi veya ekip değiştiğinde ya da "devir-teslim hazırla" dendiğinde kullanılır.
related: on-call-handover, runbook, onboarding-guide, raid-log, kb-article
prompt: İki hafta sonra başka bir ekibe geçiyorum. Sahibi olduğum ödeme mutabakat servisi için devir-teslim dokümanı yazmama yardım et.
---

# Devir-Teslim Dokümanı Yazma

## Amaç
Sahipliği bilgi, taahhüt ve ivme kaybetmeden devretmek. İyi bir devir-teslim, yeni sahibin ilk günden tek başına hareket etmesini sağlar, neyin kırılgan olduğunu gösterir ve sorumluluğun devredildiği anı açıkça belirler.

## Ne zaman kullanılır
- Bir kişi ayrıldığında, rol değiştirdiğinde veya uzun izne çıktığında.
- Bir proje veya ürün, teslimat ekibinden operasyon ya da destek ekibine geçtiğinde.
- Bir tedarikçi, yüklenici veya ekip değiştiğinde ya da bir iş akışı yeniden atandığında.

## Ne zaman kullanılmaz
- On-call sırasında vardiyadan vardiyaya operasyonel devir için `on-call-handover` kullanılır.
- Belirli bir görevin adım adım işletim prosedürü için `runbook` kullanılır.
- Belirli bir sahiplik değil, yeni gelenin ekibe genel oryantasyonu için `onboarding-guide` kullanılır.

## Girdiler
Zorunlu:
- Devredilen şey (sistem, proje, servis, rol) ve kime devredildiği (isim veya rol).
- Devreden kişinin bilgisi: notlar, serbest döküm veya sorulara cevaplar.

İsteğe bağlı, kaliteyi artırır:
- Devir tarihi, birlikte çalışma süresi, mevcut dokümantasyon, backlog, risk veya RAID kaydı.
- Mimari diyagramlar, runbook'lar, sözleşmeler, SLA'lar, paydaş listeleri.

Kapsam veya devralan kişi belirtilmemişse sor. Ardından bilgiyi en fazla 5 soruluk odaklı gruplarla (sorumluluklar, periyodik görevler, kırılgan noktalar, kişiler, açık taahhütler) topla; daha önce verilenleri tekrar sorma.

## Süreç
1. Devir kapsamını kesin olarak tanımla: neyin dahil olduğu, neyin başka birinde kaldığı ve neyin kullanımdan kaldırıldığı. Belirsiz olan her şeyi açıkça listele.
2. Bağlamı yaz: neden var olduğu, kime hizmet ettiği, temel kararlar ve gerekçeleri (varsa karar kayıtlarına bağlantı) ve bugünkü tuhaflıkları açıklayan geçmiş.
3. Mevcut durumu anlat: durum, sağlık, son değişiklikler, süren işler ve plandan ya da standarttan bilinen sapmalar. Teyit edilmemiş ifadeleri `[VARSAYIM]` olarak işaretle.
4. Sorumlulukları ve periyodik görevleri sıklık ve tetikleyicisiyle listele (günlük kontroller, aylık raporlar, sertifika yenilemeleri, lisans ve sözleşme tarihleri, denetimler). Takvime bağlı gizli görevler en sık kaybolan bilgidir.
5. Kişi haritasını çıkar: paydaşlar, karar vericiler, kullanıcılar, bağımlı ekipler, tedarikçiler ve eskalasyon kişileri; her birinin sahipten ne beklediğiyle birlikte. İsim verilmemişse rol kullan.
6. Erişim ve varlıkların envanterini çıkar: sistemler, ortamlar, repository'ler, dashboard'lar, ortak e-posta kutuları, lisanslar, parola kasaları. Erişimin nereden istendiğini yaz, sırların kendisini asla yazma.
7. Riskleri, kırılgan alanları ve kayıt dışı bilgiyi ("Y sırasında X'i yeniden başlatma", geçici çözümler, bilinen hatalar) tetikleyicisi ve önlemiyle listele.
8. Açık işleri ve taahhütleri listele: paydaşlara verilen sözler, bekleyen kararlar, açık kayıtlar, son tarihler ve devirden sonraki sahipleri.
9. Geçişi planla: birlikte çalışma aktiviteleri (gölgeleme, ters gölgeleme), bilgi aktarım oturumları, devir kabul noktası (tarih ve kriterler) ve devreden kişiye sonrasında nasıl ve ne süreyle ulaşılabileceği.
10. Gizlilik ve güvenliği kontrol et: parola, token veya iş iletişim bilgisi dışında kişisel veri olmasın; erişim iptali gerektiren her şeyi işaretle.
11. Çıktı şablonunu doldur, devreden kişi için açık soruları listele ve hedef devam ediyorsa sonraki beceriyi öner: burada ortaya çıkan prosedürler için `runbook`, yeniden kullanılabilir bilgi için `kb-article`, yeni sahip ekipte de yeniyse `onboarding-guide`.

## Çıktı formatı
```markdown
# Devir-Teslim: <ne>, <devreden> → <devralan>
Devir tarihi: <tarih veya TBD> · Birlikte çalışma: <süre> · Kabul kriteri: <kriterler>

## Kapsam
- Dahil: ... · Dahil değil (kimde kalıyor): ... · Belirsiz: ...

## Bağlam ve Temel Kararlar
- ...

## Mevcut Durum
- Durum/sağlık: ... · Süren işler: ... · Bilinen sapmalar: ...

## Sorumluluklar ve Periyodik Görevler
| Görev | Sıklık / tetikleyici | Sonraki tarih | Nasıl / referans |
|---|---|---|---|

## Kişiler ve Eskalasyon
| Rol / isim | İlişki | Beklentisi | Kanal |
|---|---|---|---|

## Erişim ve Varlıklar
| Varlık | Nerede / erişim nasıl istenir | Yeni sahip için durum |
|---|---|---|

## Riskler, Kırılgan Alanlar ve Kayıt Dışı Bilgi
- <madde> — tetikleyici — önlem

## Açık İşler ve Taahhütler
| Madde | Kime söz verildi | Tarih | Devirden sonra sahibi |
|---|---|---|---|

## Geçiş Planı
- Oturumlar: ... · Gölgeleme: ... · Devredene ulaşım: <ne zamana kadar, nasıl>

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Kapsam, devredilmeyenler dahil açıkça belirtilmiş.
- [ ] Her periyodik veya takvime bağlı görevin sıklığı ve sonraki tarihi ya da `[TBD]` var.
- [ ] Her açık taahhüdün devirden sonraki sahibi belli.
- [ ] Kabul noktası (tarih ve kriterler) belirtilmiş.
- [ ] Sır veya gereksiz kişisel veri yok; erişim, nasıl isteneceğiyle anlatılmış.
- [ ] Teyit edilmemiş ifadeler `[VARSAYIM]` olarak işaretli; hiçbir şey uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sahiplik yerine doküman devretmek. Kabul noktası olmadan sorumluluk belirsiz kalır ve sorunlar iki sahip arasında düşer.
- Yıllık veya çeyreklik görevleri unutmak (sertifika bitişi, lisans yenileme, denetim kanıtı). Tam bir yıllık takvimi baştan sona gözden geçir.
- Yalnızca her şeyin yolunda gittiği akışı yazmak. Yeni sahibin en çok ihtiyaç duyduğu şey geçici çözümler ve "asla X yapma" kurallarıdır.

## Örnek
Girdi: "İki hafta sonra ekip değiştiriyorum. Ödeme mutabakat servisinin sahibiyim. Finans ekibi günlük rapor alıyor; banka dosya formatı her ocak ayında değişiyor."

Çıktıdan bir bölüm:
- Periyodik görev: banka dosya formatı güncellemesi — yıllık, ocak — sonraki tarih `[TBD: bankayla teyit et]` — referans: `[BİLİNMİYOR: runbook var mı?]`.
- Kişiler: Finans operasyon (rol) — günlük raporu 09:00'a kadar bekliyor `[VARSAYIM]` — eskalasyon: `[BİLİNMİYOR]`.
- Kabul kriteri: yeni sahip, günlük mutabakatı 5 iş günü boyunca yardımsız tek başına yürütür.
