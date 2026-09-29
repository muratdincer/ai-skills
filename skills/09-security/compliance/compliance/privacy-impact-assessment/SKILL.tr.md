---
name: privacy-impact-assessment
description: "Bir özellik veya sistem için KVKK/GDPR kişisel veri etki değerlendirmesi (DPIA) yapar: işleme faaliyetlerini, hukuki sebepleri, veri akışlarını ve aktarımları çıkarır, ilgili kişiler açısından riskleri puanlar ve tasarımda gizlilik önlemleri önerir. Yeni bir özellik veya sistem kişisel ya da özel nitelikli veri işlediğinde, profilleme, izleme, yeni alıcılar veya yurt dışı aktarım getirdiğinde ya da hukuk birimi veya veri koruma sorumlusu DPIA istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 09-security
  role: compliance
  area: compliance
  title: "Kişisel veri etki değerlendirmesi"
  related: "data-classification, threat-model, retention-policy, security-requirements, it-risk-assessment"
  prompt: "Mağaza ziyaretlerini konumla izleyip kişiye özel kampanya gönderen yeni müşteri sadakat uygulamamız için kişisel veri etki değerlendirmesi yap."
---

# Kişisel Veri Etki Değerlendirmesi

## Amaç
Canlıya geçmeden önce bir özelliğin veya sistemin hangi kişisel verileri, hangi hukuki sebeple işlediğini, ilgili kişiler için hangi riskleri doğurduğunu ve bu riskleri kabul edilebilir seviyeye indiren önlemleri ortaya koymak. Böylece kurum karar verebilir ve KVKK (6698 sayılı Kanun) ile GDPR kapsamındaki hesap verebilirliğini gösterebilir.

## Ne zaman kullanılır
- Yeni bir özellik veya sistem kişisel veri, özellikle özel nitelikli veri (sağlık, biyometrik, din, ceza mahkûmiyeti) ya da çocuklara veya çalışanlara ait veri işlediğinde.
- İşleme profilleme, sistematik izleme, konum takibi, veri setlerinin büyük ölçekte birleştirilmesi veya önemli sonuç doğuran otomatik kararlar içerdiğinde.
- Veri yeni bir veri işleyene veya üçüncü tarafa paylaşıldığında ya da yurt dışına aktarıldığında.
- Mevcut bir işleme faaliyetinin amacı, kapsamı veya teknolojisi değiştiğinde.

## Ne zaman kullanılmaz
- Bir işleme faaliyetini değerlendirmeden yalnızca veri varlıklarını sınıflandırmanız gerekiyorsa `data-classification` kullanılır.
- İlgili kişilere yönelik riskler yerine sisteme yönelik güvenlik tehditleri gerekiyorsa `threat-model` kullanılır.
- Yalnızca saklama süreleri ve silme kuralları gerekiyorsa `retention-policy` kullanılır.

## Girdiler
Zorunlu:
- Özelliğin veya sistemin tanımı: amaç, toplanan veriler, kullanıcılar, ilgili kişiler, verinin gittiği yerler.

İsteğe bağlı, kaliteyi artırır:
- Veri işleme envanteri (KVKK için VERBİS kaydı, GDPR için Madde 30 kaydı).
- Mimari veya veri akış diyagramı, veri işleyen ve alt veri işleyen listesi, barındırma lokasyonları.
- Mevcut aydınlatma metinleri, açık rıza metinleri, saklama politikası, güvenlik kontrolleri.
- Kurumun veri sorumlusu, müşterek veri sorumlusu veya veri işleyen rolünde olup olmadığı.

Özellik tanımı yoksa iste. Hukuki sebep analizini engelleyen her konu için bir seferde tek ve odaklı soru sor; geri kalanlar açık soru olur. Örneklerde gerçek kişisel veri yerine yer tutucu kullan ve kullanıcının paylaştığı örnek verileri en aza indir.

## Süreç
1. İhtiyacı ön elemeden geçir: hangi yüksek risk göstergelerinin geçerli olduğunu listele (özel nitelikli veri, büyük ölçek, profilleme, izleme, hassas gruplar, yeni teknoloji, yurt dışı aktarım, otomatik karar). Hiçbiri yoksa tam DPIA gerekmeyebileceğini belirt ve ön eleme sonucunu kaydet.
2. İşlemeyi tanımla: amaç(lar), ilgili kişi grupları, veri kategorileri, kaynaklar, alıcılar, sistemler, saklama süresi, veri sorumlusu/veri işleyen rolleri.
3. Toplamadan silmeye kadar veri akışını çıkar; yedekler, loglar, analitik ve destek araçları dahil. Türkiye veya AEA dışına her aktarımı işaretle.
4. Her amaç için hukuki sebebi belirle: KVKK md. 5 (genel) veya md. 6 (özel nitelikli); GDPR md. 6 ve md. 9. Açık rıza varsayılan değil, son çaredir; bir hizmete bağlanmış rızaya dayanan amaçları işaretle.
5. Gereklilik ve ölçülülüğü kontrol et: veri minimizasyonu, amaçla sınırlılık, doğruluk, saklama sınırlaması. Her alanı sorgula: toplanmazsa ne bozulur?
6. İlgili kişi haklarını ve şeffaflığı kontrol et: aydınlatma metni içeriği, rızanın alınması ve geri çekilmesi, erişim, düzeltme, silme, itiraz ve yasal süreler içinde yanıt verme yolu.
7. Aktarımları kontrol et: KVKK için md. 9 kapsamında kullanılan mekanizma (yeterlilik, standart sözleşme, bağlayıcı şirket kuralları veya arızi aktarım istisnaları); GDPR için yeterlilik kararı veya SCC ile aktarım etki değerlendirmesi.
8. Yalnızca şirkete değil ilgili kişilere yönelik riskleri belirle: yetkisiz erişim, yeniden kimliklendirme, amaç kayması, ayrımcılık, kontrol kaybı, caydırıcı etki. Olasılık ve ciddiyeti (Yüksek/Orta/Düşük) gerekçesiyle puanla.
9. Her risk için önlem öner: teknik (takma adlandırma, şifreleme, erişim kontrolü, toplulaştırma, silme işleri) ve idari (veri işleyenle sözleşme, eğitim, onay akışı). Kalan riski puanla.
10. Karar ver: devam, koşullu devam veya denetim otoritesine danışma (yüksek kalan risk varsa GDPR md. 36). Veri koruma sorumlusu/hukuk görüşü verilmediyse `[TBD]` olarak kaydet.
11. Veri akışları, roller veya hukuki sebep hakkındaki her çıkarımı `[VARSAYIM]` olarak işaretle; sonra silme kuralları için `retention-policy`, teknik önlemler için `security-requirements` veya sistem bakışı için `threat-model` öner.

## Çıktı formatı
```markdown
# Kişisel Veri Etki Değerlendirmesi: <özellik/sistem> (<tarih>, v<n>)
## Ön Eleme
| Gösterge | Geçerli mi? | Not |
## İşleme Tanımı
| Amaç | İlgili kişiler | Veri kategorileri | Kaynak | Alıcılar | Saklama | Hukuki sebep (KVKK / GDPR) |
## Veri Akışı ve Aktarımlar
- Toplama -> ... -> silme; yurt dışı aktarımlar: <ülke, mekanizma>
## Gereklilik ve Ölçülülük
- <alan> – <amaç> için gerekli / kaldır / toplulaştır
## İlgili Kişi Hakları ve Şeffaflık
- Aydınlatma metni: ... / Açık rıza: ... / Hak başvuruları: ...
## İlgili Kişilere Yönelik Riskler
| No | Risk | Olasılık | Ciddiyet | Önlemler | Kalan risk | Sorumlu |
## Karar
- Sonuç: devam / koşullu devam / otoriteye danış
- Veri koruma sorumlusu / hukuk görüşü: [TBD]
## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her amacın, ikisi de uygulanıyorsa hem KVKK hem GDPR kapsamında kendi hukuki sebebi var.
- [ ] Özel nitelikli veriler belirlendi ve KVKK md. 6 / GDPR md. 9 kapsamında ele alındı.
- [ ] Her veri alanının gerekliliği yazıldı; gereksiz alanlar kaldırılmak üzere işaretlendi.
- [ ] Yurt dışı aktarımlarda mekanizma belirtildi ya da `[BİLİNMİYOR]` ile işaretlendi.
- [ ] Riskler ilgili kişinin bakış açısından yazıldı ve her Yüksek riskin bir önlemi var.
- [ ] Hiçbir hukuki sonuç, veri koruma sorumlusu/hukuk incelemesi notu olmadan kesin gibi sunulmadı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her şey için açık rızayı hukuki sebep yapmak. Hizmet veri olmadan çalışamıyorsa rıza özgür iradeyle verilmiş sayılmaz; önce sözleşme veya meşru menfaate bak.
- İkincil kopyaları unutmak: loglar, analitik olayları, destek kaydı ekleri, yedekler ve test ortamları.
- Başka ülkede bulut barındırmayı "aktarım değil" saymak. Yurt dışından uzaktan erişim veya depolama her iki düzenlemede de aktarımdır.
- Yalnızca şirkete yönelik güvenlik risklerini değerlendirmek. DPIA kişilerin hak ve özgürlükleriyle ilgilidir.

## Örnek
Girdi: "Sadakat uygulaması mağaza ziyaretlerini konumla izliyor ve kişiye özel kampanya gönderiyor."

Çıktıdan bir bölüm:
| R2 | Sürekli konum takibi günlük rutini ve ev adresini ortaya çıkarır (amacı aşan profilleme) | O | Y | Yalnızca mağaza alanlarında geofence, geofence dışında arka plan takibi yok, ham koordinat yerine mağaza ziyareti olayı, 12 ay saklama [VARSAYIM] | Düşük | Mobil ekip lideri |
- Kişiye özel kampanya için hukuki sebep: sadakat üyelik koşullarından ayrı alınan açık rıza (KVKK md. 5/1, GDPR md. 6(1)(a)); rıza uygulama içinden geri çekilebilmeli.
