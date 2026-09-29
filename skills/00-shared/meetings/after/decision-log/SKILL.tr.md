---
description: Toplantı, yazışma veya dokümanlardaki kararları bağlam, değerlendirilen seçenekler, gerekçe, karar verici, tarih, sonuçlar, geri alınabilirlik ve gözden geçirme tetikleyicisi içeren numaralı karar kaydı girdileri olarak kaydeder; önceki kararlarla çelişkileri işaretler. Bir ekip bir şeye neden karar verildiğinin kalıcı ve aranabilir kaydına ihtiyaç duyduğunda veya kararlar sürekli yeniden açıldığında kullanılır.
related: adr, meeting-minutes, meeting-notes, trade-off-analysis, raid-log
prompt: Bugünkü veri platformu toplantısındaki kararları karar kaydımıza ekle; Iceberg yerine Delta Lake'i seçtik, katalog seçimini erteledik.
---

# Karar Kaydı Tutma

## Amaç
Neye, kim tarafından, neden ve hangi alternatiflerle karar verildiğinin kalıcı bir kaydını tutmak. Böylece ekip kapanmış konuları yeniden tartışmaz, yeni katılanlar da gerekçeyi anlayabilir.

## Ne zaman kullanılır
- Bir toplantıda, sohbette veya e-postada karar alınmışsa ve kaybolmaması gerekiyorsa.
- Kararlar sürekli yeniden açılıyorsa veya neyin kararlaştırıldığı konusunda anlaşmazlık varsa.
- Bir proje veya ürün yönetişim ya da denetim için sürekli bir karar kaydına ihtiyaç duyuyorsa.

## Ne zaman kullanılmaz
- Karar kendi kaydını gerektiren önemli bir mimari kararsa `adr` kullanılır.
- Karar henüz alınmadıysa ve seçenekler karşılaştırılacaksa `trade-off-analysis` veya `decision-matrix` kullanılır.

## Girdiler
Zorunlu:
- Karar(lar)ı içeren kaynak: notlar, döküm, yazışma veya anlatım.

İsteğe bağlı:
- Mevcut karar kaydı (numaralandırma ve çelişki kontrolü için), karar yetkileri/RACI, proje adı.

Bir şeye gerçekten karar verilip verilmediği belirsizse `Önerildi` olarak kaydet ve gereken teyidi listele.

## Süreç
1. Bir seçeneği kapatan ifadeleri bul: onaylandı, seçildi, anlaşıldı, reddedildi, yapılmayacak, şu zamana kadar ertelendi. Tetikleyicisi olan erteleme de bir karardır.
2. Her karar için "<kapsam> için <seçim>" biçiminde tek satırlık başlık yaz ("Lakehouse tablo formatı olarak Delta Lake kullanımı").
3. Bağlamı yaz: problem veya tetikleyici ve kısıtlar, 1-3 cümle.
4. "Hiçbir şey yapmamak" dahil değerlendirilen seçenekleri ve her birinin reddedilme nedenini listele. Yalnızca kaynakta geçen seçenekleri yaz; eksikleri `[BİLİNMİYOR]` olarak işaretle.
5. Gerekçeyi yaz: dengeyi değiştiren kriterler.
6. Karar vericiyi (kişi veya kurul), tarihi, danışılan katılımcıları ve varsa muhalefeti kaydet.
7. Sonuçları belirt: neyi mümkün kılıyor, neyi dışarıda bırakıyor, takip aksiyonları.
8. Geri alınabilirliği sınıflandır: tek yönlü kapı (geri almak maliyetli) veya çift yönlü kapı; bir gözden geçirme tetikleyicisi belirle (tarih, metrik veya olay).
9. Durumu belirle: Önerildi, Kabul edildi, D-xxx ile geçersiz kılındı, Reddedildi.
10. Mevcut kayıtla karşılaştır; yeni karar öncekiyle çelişiyorsa öncekini Geçersiz kılındı olarak işaretle ve bunu açıkça yaz.

## Çıktı formatı
```markdown
## K-<nnn>: <kapsam> için <seçim>
| Alan | Değer |
|---|---|
| Durum | Önerildi / Kabul edildi / K-xxx ile geçersiz kılındı / Reddedildi |
| Tarih | <tarih> |
| Karar verici | <isim/kurul> |
| Danışılanlar | <isimler/roller> |
| Geri alınabilirlik | Tek yönlü / Çift yönlü |
| Gözden geçirme tetikleyicisi | <tarih, metrik veya olay> |

Bağlam: <...>
Değerlendirilen seçenekler:
1. <seçenek> – <neden seçilmedi>
2. <seçilen seçenek> – seçildi
Gerekçe: <kriterler>
Sonuçlar: <mümkün kıldıkları / dışarıda bıraktıkları>
Takip aksiyonları: <aksiyon – sorumlu – tarih>
Muhalefet: <yok / özet>
Kaynak: <toplantı, tarih, bağlantı>
```

## Kalite kontrol listesi
- [ ] Her girdi gerçek bir kararı kaydediyor; teyit edilmemiş olanlar `Önerildi` durumunda.
- [ ] Karar verici ve tarih mevcut ya da `[BİLİNMİYOR]` olarak işaretli.
- [ ] En az bir alternatif ve gerekçe kaydedildi.
- [ ] Sonuçlar ve bir gözden geçirme tetikleyicisi belirtildi.
- [ ] Önceki kararlarla çelişkiler Geçersiz kılındı durumuyla çözüldü.

## Sık yapılan hatalar
- Yalnızca sonucu kaydetmek. Bağlam ve reddedilen seçenekler olmadan karar yeniden açılır.
- En yüksek sesle söylenen görüşü karar olarak kaydetmek. Karar yetkisinin kimde olduğunu kontrol et.
- Önceki bir kararla sessizce çelişmek. Her zaman bağlantı kur ve geçersiz kıl.

## Örnek
Girdi: "Spark altyapımız doğrudan desteklediği için Iceberg yerine Delta ile gidiyoruz; katalog seçimi haziran güvenlik incelemesine kadar ertelendi."

Çıktıdan bir bölüm:
## K-014: Lakehouse tablo formatı olarak Delta Lake kullanımı
Durum: Kabul edildi | Karar verici: [BİLİNMİYOR] | Geri alınabilirlik: Tek yönlü
Seçenekler: Apache Iceberg – mevcut Spark altyapısında doğal desteği daha zayıf olduğu için reddedildi.
## K-015: Veri kataloğu seçiminin güvenlik incelemesine kadar ertelenmesi
Durum: Kabul edildi | Gözden geçirme tetikleyicisi: haziran güvenlik incelemesi `[tarihi teyit et]`
