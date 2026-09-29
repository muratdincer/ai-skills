---
description: "Belirgin bir belirtiden başlayıp doğrulanabilir bir veya daha fazla kök nedene inen disiplinli bir 5 Neden analizi yapar; her halkanın kanıtını, katkıda bulunan her neden için ayrı bir dalı ve belirtiyi değil nedeni hedefleyen önlemleri ortaya koyar. Bir olay, hata, kaçırılan hedef veya tekrarlayan problem için kök neden gerektiğinde, 'bu neden sürekli oluyor' sorulduğunda ya da bir postmortem veya çıkarılan dersler çalışması nedensel derinlik istediğinde kullanılır."
related: "problem-statement, fishbone-analysis, postmortem, debugging-hypotheses, lessons-learned"
prompt: "Şunun için 5 Neden analizi yap: gece çalışan müşteri aktarımı bu ay üç kez hata verdi ve finans raporu her seferinde geç aldı."
---

# 5 Neden Analizi

## Amaç
Somut bir belirtiyi, kanıtlanmış neden-sonuç halkalarından oluşan bir zincirle kurumun müdahale edebileceği bir kök nedene kadar izlemek. Böylece alınan önlem son vakayı yamamak yerine tekrarı önler.

## Ne zaman kullanılır
- Bir olay, hata veya süreç aksaklığı kontrol altına alınmış ve artık kök nedeni aranıyorsa.
- Aynı problem tekrar ediyor ve önceki düzeltmeler kalıcı olmadıysa.
- Bir postmortem, çıkarılan dersler veya düzeltici faaliyet raporu nedensel akıl yürütme gerektiriyorsa.

## Ne zaman kullanılmaz
- Problemin kendisi belirsiz veya tartışmalıysa önce `problem-statement` kullanılır.
- İnsan, süreç, araç ve ortam arasında etkileşen çok sayıda neden şüphesi varsa `fishbone-analysis` kullanılır, ardından en güçlü dallarda 5 Neden çalıştırılır.
- Canlı bir teknik arıza ayıklanıyorsa `debugging-hypotheses` kullanılır.

## Girdiler
Zorunlu:
- Belirti: ne oldu, nerede, ne zaman ve etkisi ne.

İsteğe bağlı, kaliteyi artırır:
- Zaman çizelgesi, loglar, metrikler, kayıtlar, değişiklik geçmişi (kişisel veriler maskelenmiş).
- Tespit ve müdahalede kimlerin yer aldığı (suçlama değil, roller).
- Önceki düzeltmeler ve neden tutmadıkları.

Belirti yoksa veya yalnızca bir çözüm olarak ifade edilmişse ("izleme lazım") gerçekte ne olduğunu sor. Destekleyemediğin her halka için tek seferde tek soru sor.

## Süreç
1. Belirtiyi olgusal ve sınırları çizili bir ifade olarak yaz: ne, nerede, ne zaman, ne sıklıkla, etkisi. İçinde neden olmasın.
2. "Bu neden oldu?" diye sor ve doğrudan nedeni bir kişi hakkında değil, sistem veya süreç hakkında doğrulanabilir bir olgu olarak yaz ("yeniden deneme limiti 0'dı", "Ali unuttu" değil).
3. Her cevap için kanıtı (log satırı, metrik, yapılandırma, doküman, görüşme) kaydet ya da `[VARSAYIM — <kontrol> ile doğrula]` olarak işaretle.
4. Zinciri geriye doğru "bu yüzden" testiyle oku: aşağıdan yukarıya "bu yüzden" diyerek okunduğunda her adım mantıksal olarak izlemeli.
5. Bir cevabın birden fazla katkı veren nedeni varsa dallandır; tek bir çizgiye zorlamak yerine her dalı ayrı analiz et.
6. Kurumun kontrolünde olan ve ortadan kaldırıldığında tekrarı önleyecek bir nedene ulaşana kadar devam et. Beş bir sezgisel kuraldır: kanıt neye izin veriyorsa o kadar erken dur veya ilerle.
7. Bir dalı "insan hatası", "zaman yetersizliği" veya "bütçe" noktasında ancak sistemin bu hataya ya da kısıta neden izin verdiğini sorduktan sonra durdur; bunlar nadiren kök nedendir.
8. Kök nedeni, katkıda bulunan faktörlerden ve problemin neden daha erken fark edilmediğinden (tespit boşluğu) ayır.
9. Her kök neden için önlem tanımla: acil kontrol altına alma, kalıcı düzeltici faaliyet ve tespit iyileştirmesi; her birine sorumlu rol ve doğrulama yöntemi ekle.
10. Sonucu değiştirebilecek varsayımları ve kanıt boşluklarını listele.
11. Kullanıcının hedefi devam ediyorsa olayı belgelemek için `postmortem`, nedenler hâlâ genişse `fishbone-analysis`, öğrenileni paylaşmak için `lessons-learned` öner.

## Çıktı formatı
```markdown
# 5 Neden: <belirtinin kısa başlığı>

**Belirti:** <ne, nerede, ne zaman, ne sıklıkla, etki>

| # | Neden? | Cevap (neden) | Kanıt |
|---|---|---|---|
| 1 | <belirti> neden oldu? | ... | <kaynak> / [VARSAYIM] |
| 2 | <cevap 1> neden oldu? | ... | ... |
| ... | | | |

**Dal B (varsa):** <aynı tablo>

## Kök Neden(ler)
- <kök neden> – kontrolümüzde mi: evet/hayır

## Katkıda Bulunan Faktörler ve Tespit Boşluğu
- ...

## Önlemler
| Tür | Aksiyon | Sorumlu (rol) | Doğrulama |
|---|---|---|---|
| Kontrol altına alma | ... | ... | ... |
| Düzeltici | ... | ... | ... |
| Tespit | ... | ... | ... |

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Belirti ifadesi neden veya çözüm içermiyor.
- [ ] Her halkanın kanıtı var ya da doğrulama adımıyla birlikte `[VARSAYIM]` olarak işaretli.
- [ ] Zincir aşağıdan yukarıya "bu yüzden" ile mantıklı okunuyor.
- [ ] Hiçbir kök neden bir kişinin adı veya arkasındaki sistem nedeni gösterilmemiş "insan hatası" değil.
- [ ] Her kök nedenin bir düzeltici faaliyeti ve işe yaradığını doğrulama yolu var.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İlk makul cevabın peşine düşmek. Her halkayı kanıtla kontrol et; doğrulanmamış bir zincir kendinden emin ama yanlış düzeltmeler üretir.
- Belirtinin sahibinde durmak ("operasyon ekibi alarmı kaçırdı"). Alarmın neden kaçırılabilir olduğunu sor.
- Kontrol alanının dışına sıçramak ("tedarikçi güvenilmez"). Bir adım geri gidip sürecin tedarikçi hakkında neyi varsaydığına bak.
- Yalnızca manuel kontrol ekleyen önlemler. Hata biçimini ortadan kaldıran değişiklikleri tercih et.

## Örnek
Girdi: "Gece çalışan müşteri aktarımı bu ay üç kez hata verdi; finans raporu her seferinde geç aldı."

Çıktıdan bir bölüm:
| # | Neden? | Cevap | Kanıt |
|---|---|---|---|
| 1 | Rapor neden geç kaldı? | Aktarım işi hata verdi ve 08:00'den önce kimse yeniden çalıştırmadı. | Zamanlayıcı geçmişi |
| 2 | İş neden hata verdi? | İş başladığında kaynak veritabanı bakım penceresindeydi. | Veritabanı bakım takvimi |
| 3 | Neden çakıştılar? | Bakım penceresi geçen ay kaydırıldı; iş zamanlaması güncellenmedi. | Değişiklik kaydı `[VARSAYIM — değişiklik numarasını teyit et]` |
| 4 | İş neden güncellenmedi? | İşlerin bakım pencerelerine bağımlılıkları hiçbir yerde kayıtlı değil. | [VARSAYIM] |

Kök neden: zamanlama bağımlılıkları belgelenmemiş, bu yüzden bir taraftaki değişiklik diğer tarafın gözden geçirilmesini tetiklemiyor. Tespit boşluğu: iş hata alarmları geceleri kimsenin izlemediği ortak bir posta kutusuna gidiyor.
