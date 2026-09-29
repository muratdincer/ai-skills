---
description: "Bir varlığı veya iş akışını durumlar, olaylar, koşullar ve aksiyonlar olarak modeller; ardından tüm geçerli geçişler, geçersiz geçişler (reddedilmesi gereken durum-olay çiftleri) ve önemli geçiş dizileri (0-switch ve 1-switch kapsamı) için testler türetir. Davranış duruma veya geçmişe bağlı olduğunda (sipariş, başvuru, onay, hesap, oturum, cihaz) ya da bir iş akışının veya yaşam döngüsünün test edilmesi istendiğinde kullanılır."
related: state-model, decision-table-testing, test-case-writing, test-scenarios-from-requirements, api-test-design
prompt: "Satın alma talebi için durum geçiş testleri oluştur: Taslak, Gönderildi, Onaylandı, Reddedildi, İptal, Sipariş verildi. Yalnızca talep sahibi, sipariş verilmeden önce iptal edebilir."
---

# Durum Geçiş Testi

## Amaç
Bir yaşam döngüsünün yalnızca izin verilen geçişlere, doğru koşul ve rollerle izin verdiğini ve diğer tüm geçişleri reddettiğini doğrulamak. Yasak geçişler, veri bozulması ve güvenlik hatalarının sık rastlanan kaynağıdır.

## Ne zaman kullanılır
- Bir varlığın durumları var ve bazı işlemlere yalnızca belirli durumlarda izin veriliyor.
- İş akışlarında onaylar, zaman aşımları, yeniden denemeler, iptaller veya yeniden açmalar var.
- Bir API, yanlış sırada çağrılabilecek durum değiştiren uç noktalar sunuyor.

## Ne zaman kullanılmaz
- Durum modelinin kendisi iş birimi için tasarlanacak veya dokümante edilecekse `state-model` kullanılır.
- Sonuç durumdan değil yalnızca anlık girdi kombinasyonlarından etkileniyorsa `decision-table-testing` kullanılır.
- Bir özelliğin tüm senaryoları üst düzeyde gerekiyorsa `test-scenarios-from-requirements` kullanılır.

## Girdiler
Zorunlu:
- Durumlar ve izin verilen geçişler ya da iş akışının tanımı.

İsteğe bağlı, kaliteyi artırır:
- Koşullar (guard, roller), geçişteki aksiyonlar (bildirim, stok, denetim kaydı), zaman aşımları.
- Mevcut diyagram veya durum alanı değerleri.

İş akışı tanımı yoksa iste. İzinli veya yasak olduğu belirtilmemiş geçişler açık soru olur.

## Süreç
1. Başlangıç, bitiş ve örtük durumlar dahil tüm durumları listele (ör. zaman aşımı sonrası "Süresi doldu", "Silindi").
2. Olayları/tetikleyicileri listele: kullanıcı işlemleri, sistem olayları, zamanlayıcılar, dış geri çağrılar.
3. Durum geçiş tablosunu kur: her geçerli geçiş için kaynak durum, olay, koşul, hedef durum ve aksiyonları yaz.
4. Gözden geçirilebilmesi için diyagramı metinle (ör. Mermaid state diagram) çiz veya tarif et.
5. Tam durum x olay matrisini kur; her boş hücre bir geçersiz geçiş adayıdır. Beklenen davranışa karar ver: mesajla reddedilir, yok sayılır veya `[BİLİNMİYOR]`.
6. 0-switch testlerini türet: her geçerli geçiş için koşul doğru/yanlış ve rol varyantları dahil bir test.
7. Yüksek riskli hücreler (bitiş durumları, finansal etkiler, güvenlikle ilgili roller) için arayüzü atlayan doğrudan API çağrıları dahil geçersiz geçiş testleri türet.
8. Riskli yollar için 1-switch veya daha uzun diziler türet: ret sonrası yeniden açma, onay sonrası iptal, hata sonrası yeniden deneme, döngüler.
9. Zamanlama ve eşzamanlılık case'leri ekle: sınırda zaman aşımı, iki aktörün aynı anda çelişen olayları tetiklemesi.
10. Her geçişin yan etkilerini doğrula: denetim izi, bildirimler, bağımlı varlıklar.
11. Tanımsız hücreler için açık soruları listele.

## Çıktı formatı
```markdown
# Durum Geçiş Testleri: <varlık / iş akışı>
## Durumlar ve Olaylar
## Geçiş Tablosu
| # | Kaynak | Olay | Koşul | Hedef | Aksiyonlar |
## Diyagram
<metin veya Mermaid stateDiagram>
## Durum x Olay Matrisi
| Durum \ Olay | O1 | O2 | ... |   (hedef durum, "Ret" veya [BİLİNMİYOR])
## Testler
| Test | Tür (geçerli / geçersiz / dizi) | Yol | Veri / rol | Beklenen |
## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Her geçerli geçiş en az bir testle kapsanıyor (0-switch kapsamı).
- [ ] Durum x olay matrisinin her hücresinin beklenen davranışı var veya açık soru.
- [ ] Bitiş durumlarının tüm olayları reddettiği test ediliyor.
- [ ] Koşullar, rol kontrolleri dahil doğru ve yanlış varyantlarıyla test ediliyor.
- [ ] Yalnızca sonuç durumu değil, yan etkiler de doğrulanıyor.

## Sık yapılan hatalar
- Geçersiz butonların gizlendiği arayüz üzerinden test etmekle yetinmek. Alttaki API'yi veya servisi doğrudan çağır.
- Zamanlayıcı ve sistem kaynaklı geçişleri unutmak.
- Eşzamanlı geçişleri (aynı anda onay ve iptal) yok saymak.

## Örnek
Girdi: "Taslak, Gönderildi, Onaylandı, Reddedildi, İptal, Sipariş verildi; yalnızca talep sahibi, sipariş verilmeden önce iptal edebilir."

Çıktıdan bir bölüm:
| 5 | Onaylandı | İptal et | aktör = talep sahibi | İptal | Onaylayana bildirim |
| ST-12 | Geçersiz | Sipariş verildi → İptal | talep sahibi | Reddedilir, durum değişmez |
| ST-15 | Geçersiz | Onaylandı → İptal | onaylayan (talep sahibi değil) | Yetki hatasıyla reddedilir |
- Açık soru: Reddedilen talep düzenlenip yeniden gönderilebilir mi, yoksa yeni talep mi gerekir?
