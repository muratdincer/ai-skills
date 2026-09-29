---
description: Genel RAG durumu, plana göre ilerleme, riskler ve sorunlar, gereken kararlar veya destek ve sonraki adımları içeren kısa bir durum güncellemesi yazar. Bir proje, iş akışı, girişim veya olay hakkındaki ilerlemenin yöneticiye, sponsora, yönlendirme komitesine veya ekip kanalına raporlanması gerektiğinde ya da "haftalık güncelleme", "durum raporu", "ne durumdayız" istendiğinde kullanılır.
related: project-status-report, executive-summary, escalation-message, raid-log, steering-committee-pack
prompt: Veri platformu taşıması için bu haftanın durum güncellemesini yaz: 5 alandan 3'ü taşındı, finans alanı bir firewall değişikliği yüzünden bekliyor, canlıya geçiş hâlâ ayın 30'u olarak planlı.
---

# Durum Güncellemesi Yazma

## Amaç
Okuyucuya bir dakikadan kısa sürede işin yolunda olup olmadığını, son güncellemeden bu yana neyin değiştiğini ve kendisinin ne yapması gerektiğini anlatmak. Böylece sorunlar erken görünür ve kararlar belirsiz raporlama yüzünden gecikmez.

## Ne zaman kullanılır
- Sponsora, yöneticiye veya yönlendirme komitesine düzenli (haftalık, iterasyon bazlı) güncellemelerde.
- Bir proje, iş akışı veya taşıma için anlık "ne durumdayız?" sorusunda.
- Geniş bir kitleye ilerlemeyi özetleyen ekip kanalı paylaşımlarında.

## Ne zaman kullanılmaz
- Bütçe, takvim baz çizgisi ve RAID ayrıntısı içeren resmi proje raporu gerekiyorsa `project-status-report` kullanılır.
- Durum, üst seviyeden hemen bir karar gerektiriyorsa `escalation-message` kullanılır.
- Devam eden bir olay için `incident-communication` kullanılır.

## Girdiler
Zorunlu:
- İşin ne olduğu ve hedefi veya kilometre taşı.
- Son güncellemeden bu yana ilerleme bilgileri (biten, devam eden, bloke olan).

İsteğe bağlı:
- Plan/baz çizgisi (tarihler, kapsam, bütçe), önceki güncelleme, kurumun kullandığı RAG kriterleri, riskler ve sorunlar, hedef kitle.

İlerleme bilgileri eksikse tek bir kısa soru grubuyla iste. RAG durumunu yalnızca anlatımın tonundan çıkarma; plan bilinmiyorsa durumu `[VARSAYIM]` olarak işaretle ve neye dayandığını yaz.

## Süreç
1. Hedef kitleyi ve neye karar verdiğini veya neyi kontrol ettiğini belirle; ayrıntı düzeyi ve talep buna göre şekillenir.
2. Baz çizgisini ortaya koy: kilometre taşı, hedef tarih, kapsam. Verilmediyse var gibi göstermek yerine "baz çizgisi verilmedi" yaz.
3. Genel durumu açık kriterlerle derecelendir: Yeşil = yolunda, destek gerekmiyor; Sarı (Amber) = risk altında, belirtilen aksiyonla toparlanabilir; Kırmızı = karar veya destek olmadan hedef kaçacak. Kurumun kriterleri verildiyse onları kullan.
4. Başlığı tek cümleyle yaz: RAG, en önemli tek bilgi ve varsa talep.
5. İlerlemeyi faaliyet değil sonuç olarak listele ("taşıma üzerinde çalışıldı" değil "5 alandan 3'ü canlıda"), verildiyse rakamlarla.
6. Son güncellemeden bu yana değişenleri, RAG değişikliklerini gerekçesiyle yaz ("Sarı → Kırmızı, çünkü...").
7. En önemli riskleri ve sorunları (en fazla 3-5) etki, sorumlu ve azaltma aksiyonuyla listele; geri kalanını `raid-log`'a taşı.
8. Gereken kararları veya desteği kişi, net talep ve gereken tarihle yaz.
9. Gelecek dönemin sonraki adımlarını sorumlularıyla listele.
10. Kullanıcının verdiği olgularla kendi çıkarımlarını ayır; çıkarımları `[VARSAYIM]` olarak işaretle, eksikleri açık soru olarak listele.
11. Tek ekrana sığacak kadar kısalt; ayrıntıyı bağlantıya veya eke taşı.
12. Kullanıcının hedefi devam ediyorsa karar gerektiren Kırmızı maddeler için `escalation-message`, üst yönetime yoğunlaştırılmış sürüm için `executive-summary` öner.

## Çıktı formatı
```markdown
**<İşin adı> – Durum <tarih veya dönem>**  Genel: <Yeşil/Sarı/Kırmızı> (<önceki RAG>)
**Başlık:** <tek cümle: durum + kilit bilgi + talep>

**Son güncellemeden bu yana ilerleme**
- <rakamlı sonuç>

**Değişiklikler / RAG hareketi**
- <ne değişti, neden>

**Riskler ve sorunlar**
| Madde | Etki | Sorumlu | Azaltma / sonraki aksiyon |
|---|---|---|---|

**Gereken kararlar / destek**
- <kim>: <net talep>, <tarih>'e kadar

**Sonraki adımlar**
- <aksiyon> – <sorumlu> – <tarih>

**Varsayımlar / açık sorular**
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] RAG durumu belirtilen kriterlere uyuyor ve içerikle tutarlı ("bloke madde varken Yeşil" yok).
- [ ] Başlık tek başına meşgul bir okuyucuya durumu ve talebi anlatıyor.
- [ ] İlerleme, mümkün olduğunca rakamlarla, sonuç olarak ifade edildi.
- [ ] Her risk, sorun ve talebin sorumlusu var; her talebin gereken tarihi veya `[TBD]` işareti var.
- [ ] Uydurulmuş tarih, yüzde veya isim yok; çıkarımlar işaretli.
- [ ] Tek ekrana sığıyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Karpuz raporu: dışı yeşil, içi kırmızı. Kilometre taşı risk altındaysa şimdi Sarı de; geç gelen Kırmızı güveni erken gelen Sarı'dan çok daha fazla zedeler.
- Sinyal taşımayan faaliyet listeleri ("toplantılar yapıldı, analiz sürüyor"). Sonuçları ve farkları raporla.
- Talebi sona gömmek. Okuyucunun harekete geçmesi gerekiyorsa talebi başlığa koy.

## Örnek
Girdi: "5 alandan 3'ü taşındı, finans firewall değişikliğinde takıldı, canlıya geçiş 30'unda."

Zayıf: "Bu hafta iyi ilerleme kaydettik. Bazı alanları taşıdık, kalanlar üzerinde çalışıyoruz. Bazı ağ sorunları var. Canlıya geçiş planlandığı gibi."

Güçlü (bölüm):
**Veri Platformu Taşıması – 38. hafta durumu**  Genel: Sarı (önceki: Yeşil)
**Başlık:** 5 alandan 3'ü canlıda; finans firewall değişikliği `[TBD – ağ ekibinden tarih bekleniyor]` tarihine kadar onaylanmazsa 30'undaki canlıya geçiş risk altında.
**Gereken destek:** Ağ lideri: finans veritabanı portları için değişikliği `[TBD]` tarihine kadar onaylayın.
