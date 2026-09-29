---
description: Eğitilmiş bir modelin kullanım amacını, kapsam dışı kullanımlarını, eğitim ve değerlendirme verisini, genel ve grup bazında performansını, sınırlamalarını, etik ve gizlilik değerlendirmelerini ve sahipliğini belgeleyen bir model kartı yazar. Bir model yayına alındığında, ekipler arasında paylaşıldığında, yönetişim veya denetim incelemesine sunulduğunda ya da kullanıcıların modele neyde güvenip neyde güvenemeyeceğini bilmesi gerektiğinde kullanılır.
related: model-evaluation-report, ml-monitoring-plan, ml-problem-framing, privacy-impact-assessment, ai-use-case-assessment
prompt: İK işe alım uzmanlarının kullandığı CV eleme sıralama modelimiz için model kartı yaz; değerlendirme sonuçları ve eğitim verisi özeti ekte.
---

# Model Kartı Yazma

## Amaç
Bir modeli kullanan, inceleyen veya devralan herkes için kısa ve dürüst bir başvuru kaynağı sunmak: model ne için, kimin için ne kadar iyi çalışıyor ve nerede kesinlikle kullanılmamalı. Yaygın model kartı pratiğini (Mitchell ve ark.) izler ve yüksek riskli sistemler için AB Yapay Zeka Yasası (EU AI Act) gibi düzenlemelerdeki dokümantasyon yükümlülüklerini destekler.

## Ne zaman kullanılır
- Bir model üretime veya başka ekiplere açıldığında.
- Bir YZ yönetişimi, risk veya denetim süreci dokümantasyon gerektirdiğinde.
- Bir model yeni bir sahibe devredildiğinde.

## Ne zaman kullanılmaz
- Yayın kararı için ayrıntılı teknik karşılaştırma gerekiyorsa `model-evaluation-report` kullanılır.
- Kullanım senaryosunun kendisi henüz onaylanmadıysa `ai-use-case-assessment` kullanılır.
- Tam bir veri koruma değerlendirmesi gerekiyorsa `privacy-impact-assessment` kullanılır.

## Girdiler
Zorunlu:
- Modelin amacı ve değerlendirme sonuçları (en azından genel metrikler).

İsteğe bağlı, kaliteyi artırır:
- Eğitim verisi tanımı (kaynaklar, dönem, büyüklük, etiketleme).
- Dilim ve adillik sonuçları, bilinen başarısızlık biçimleri.
- Sahip, sürüm, dağıtım bağlamı, mevzuat sınıflandırması.

Değerlendirme sonuçları yoksa, performans alanları `[BİLİNMİYOR]` olarak işaretlenmiş bir kart iskeleti üret ve kartın yayına hazır olmadığını belirt.

## Süreç
1. Model ayrıntılarını kaydet: ad, sürüm, tip/mimari ailesi, sahip, tarih, lisans veya iç statü, iletişim.
2. Kullanım amacını tanımla: birincil kullanıcılar, desteklenen kararlar, otomasyon düzeyi (tavsiye veya otomatik) ve gereken insan gözetimi.
3. Kapsam dışı ve yasaklı kullanımları, cazip kötüye kullanımlar dahil açıkça listele.
4. Eğitim verisini özetle: kaynaklar, dönem, büyüklük, etiketleme süreci, bilinen boşluklar ve temsil gücü; kişisel veri kategorilerini ve uygulanan veri minimizasyonunu belirt (KVKK/GDPR).
5. Değerlendirme verisini ve eğitim ile üretimden farkını özetle.
6. Performansı genel olarak ve ilgili gruplar ile koşullar için, metrik tanımları ve kullanılan eşikle birlikte raporla.
7. Sınırlamaları yaz: performansın düştüğü koşullar, dağılım kaymasına duyarlılık, kalibrasyon sorunları, bilinen başarısızlık biçimleri.
8. Etik değerlendirmeleri belgele: etkilenen kişiler, olası zararlar, adillik ölçütü ve sonuçları, önlemler, etkilenen bireyler için itiraz yolu.
9. İzlemeyi, yeniden eğitim sıklığını ve emekliye ayırma kriterlerini açıkla; izleme planına atıf yap.
10. Dili uzman olmayan bir inceleyicinin anlayacağı sadelikte tut; teknik ayrıntıyı referanslara taşı.

## Çıktı formatı
```markdown
# Model Kartı: <ad> v<sürüm>
| Alan | Değer |
|---|---|
| Sahip / iletişim | ... |
| Model tipi | ... |
| Yayın tarihi | ... |
| Otomasyon düzeyi | Tavsiye / Döngüde insan / Otomatik |
| Risk sınıfı | <iç veya mevzuat, ya da [BİLİNMİYOR]> |

## Kullanım Amacı
- Kullanıcılar: ...
- Desteklenen kararlar: ...
- İnsan gözetimi: ...

## Kapsam Dışı Kullanımlar
- ...

## Eğitim Verisi
...

## Değerlendirme Verisi
...

## Performans
| Metrik (tanım, eşik) | Genel | Grup A | Grup B |
|---|---|---|---|

## Sınırlamalar
- ...

## Etik ve Gizlilik Değerlendirmeleri
- Olası zararlar: ...
- Adillik: ...
- Kişisel veri: ...
- İtiraz yolu: ...

## İzleme ve Bakım
- ...
```

## Kalite kontrol listesi
- [ ] Kapsam dışı kullanımlar ima edilmiyor, açıkça yazılıyor.
- [ ] Performans yalnızca genel değil, ilgili gruplara göre de raporlandı.
- [ ] Sınırlamalar modelin başarısız olduğu somut koşulları içeriyor.
- [ ] İnsanlarla ilgili kararlar için insan gözetimi ve itiraz yolu tanımlı.
- [ ] Hiçbir metrik veya veri bilgisi uydurulmadı; boşluklar işaretli.
- [ ] Uzman olmayan biri kullanım amacını ve sınırları anlayabiliyor.

## Sık yapılan hatalar
- Sınırlamalar yerine pazarlama metni yazmak. Her kart, en az bir okuyucunun modeli bir iş için kullanmamaya karar vermesini sağlamalı.
- Yalnızca toplam doğruluğu raporlayıp gruplar arası farkları gizlemek.
- Kartın eskimesine izin vermek; güncellemeleri her sürüm yayınına bağla.

## Örnek
Girdi: İK işe alım uzmanları için CV sıralama modeli; adayları mülakat kısa listesi için sıralıyor.

Çıktıdan bir bölüm:
- Otomasyon düzeyi: Tavsiye – uzmanlar her kısa listeyi inceler; model hiçbir adayı otomatik elemez.
- Kapsam dışı: Nihai işe alım kararları, maaş belirleme, iç terfi sıralaması, eğitim verisinde bulunmayan iş ailelerindeki roller.
- Adillik: Her iş ailesi için cinsiyete göre seçilme oranı oranı raporlanır `[sonuçlar verilmedi]`; ad, fotoğraf ve yaş alanları skorlama öncesinde kaldırılır.
