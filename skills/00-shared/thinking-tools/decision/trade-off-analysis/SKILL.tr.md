---
name: trade-off-analysis
description: "Her seçeneğin rekabet eden nitelikler (ör. hız ve güvenlik, maliyet ve dayanıklılık, esneklik ve sadelik, kapsam ve zaman) arasında neyi kazanıp neyi feda ettiğini açıkça ortaya koyar; belirleyici gerilimi, her tercihin geri alınabilirliğini ve tercih edilen seçeneğin hangi koşullarda doğru olmaktan çıkacağını belirler. Hiçbir seçeneğin her konuda üstün olmadığı mimari, ürün, kapsam veya süreç kararlarında, paydaşlar birbirini anlamadan tartıştığında veya bir kararı kayda geçirmeden önce kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: thinking-tools
  area: decision
  title: "Ödünleşim analizi"
  related: "decision-matrix, adr, architecture-review, pros-cons, technology-selection"
  prompt: "Yeni hasar yönetim sistemimiz için modüler monolit ile mikroservisler arasındaki ödünleşimleri analiz et."
---

# Ödünleşim Analizi

## Amaç
"Hangi seçenek en iyisi" sorusunu "neyi feda etmeye razıyız ve neden" sorusuyla değiştirmek; böylece karar kurumun önceliklerini açıkça yansıtır ve bu öncelikler ya da koşullar değiştiğinde yeniden ele alınabilir.

## Ne zaman kullanılır
- Seçeneklerin her biri farklı niteliklerde güçlüyse ve hiçbiri diğerlerine baskın değilse.
- Bir karar rekabet eden kalite niteliklerini (performans, erişilebilirlik, güvenlik, maliyet, pazara çıkış süresi, bakım kolaylığı) dengelemek zorundaysa.
- Paydaşlar farklı hedefleri optimize ettikleri için birbirini anlamadan tartışıyorsa.

## Ne zaman kullanılmaz
- Çok sayıda seçeneğin puanlanıp sıralanması gerekiyorsa `decision-matrix` kullanılır.
- Tek bir öneri için hızlı bir avantaj/dezavantaj listesi yeterliyse `pros-cons` kullanılır.
- Gereksinimlere karşı tam bir mimari değerlendirme gerekiyorsa `architecture-review` kullanılır.

## Girdiler
Zorunlu:
- Karar ve en az iki seçenek.
- Kararın hedefi veya belirleyicileri.

İsteğe bağlı, kaliteyi artırır:
- Kalite niteliği öncelikleri, kısıtlar (bütçe, son tarih, yetkinlikler, mevzuat).
- Bağlam: mevcut sistem, ekip büyüklüğü, beklenen yük ve büyüme.

Belirleyiciler yoksa en önemli iki-üç sonucun hangileri olduğunu sor; bunlar olmadan ödünleşimler değerlendirilemez.

## Süreç
1. Kararı, öncelik sırasına göre belirleyicilerini ve sabit kısıtları ifade et.
2. Bu karar için önemli olan nitelikleri (5-8) iki yönü de görünür olacak şekilde listele ("ilk sürüme kadar geçen süre", "bağımsız ölçekleme").
3. Her seçenek için, diğer seçeneklere kıyasla her nitelikte neyi kazandığını ve neyi feda ettiğini somut olarak tarif et.
4. Belirleyici gerilimleri bul: seçeneklerin en çok ayrıştığı ve belirleyicilerin çeliştiği bir-iki nitelik.
5. Gözden kaçması kolay maliyetleri görünür kıl: operasyon yükü, bilişsel yük, yetkinlik, taşıma eforu, bağımlılık (lock-in) ve gecikme maliyeti.
6. Geri alınabilirliği değerlendir: sonradan yön değiştirmek ne kadar pahalı (tek yönlü kapı mı, çift yönlü kapı mı)? Geri alınamaz tercihler daha fazla kanıt ister.
7. Her seçeneğin hangi koşullarda doğru seçenek haline geldiğini belirle (ölçek, ekip büyüklüğü, değişiklik sıklığı, mevzuat değişikliği).
8. Geri alınamaz kısım için zaman kazandıran hibrit veya aşamalı seçenekleri kontrol et (ör. modüler başla, sonra ayır).
9. Bir seçenek öner; bedel olarak neyin kabul edildiğini açıkça yaz ve kararın yeniden ele alınmasını tetikleyecek sinyalleri tanımla.
10. Çıkarımları ve eksik olguları `[VARSAYIM]` veya `[BİLİNMİYOR]` olarak işaretle ve açık soruları listele.
11. Kullanıcının hedefi devam ediyorsa kararı ve kabul edilen ödünleşimleri kaydetmek için `adr`, daha fazla seçenek çıkarsa `decision-matrix` öner.

## Çıktı formatı
```markdown
# Ödünleşim Analizi: <karar>
**Belirleyiciler (öncelik sırasıyla):** 1. ... 2. ... **Kısıtlar:** ...

| Nitelik | Seçenek A kazanır / feda eder | Seçenek B kazanır / feda eder |
|---|---|---|
| <nitelik> | + ... / - ... | + ... / - ... |

## Belirleyici Gerilimler
- <nitelik X ve nitelik Y>: ...

## Gizli Maliyetler ve Geri Alınabilirlik
| Seçenek | Gizli maliyetler | Geri alınabilirlik (tek yönlü / çift yönlü) | Sonradan değiştirme maliyeti |
|---|---|---|---|

## Hangi Seçenek Ne Zaman Doğru
- Seçenek A şu durumda ...; Seçenek B şu durumda ...

## Öneri
<seçenek>. <kazanım> karşılığında <bedel>i kabul ediyoruz. <sinyal> olduğunda yeniden ele al.

## Varsayımlar ve Açık Sorular
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her seçenek hem kazanımları hem bedelleri gösteriyor; hiçbir seçenek bedelsiz sunulmamış.
- [ ] Belirleyici gerilimler belirtilen belirleyicilere bağlanmış.
- [ ] Geri alınabilirlik ve gizli maliyetler (operasyon, yetkinlik, bağımlılık) ele alınmış.
- [ ] Öneri kabul edilen bedeli ve yeniden ele alma sinyallerini adlandırıyor.
- [ ] Çıkarımlar ve eksik olgular işaretli; hiçbir sayı uydurulmamış.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Seçenekleri birbirleriyle değil bir idealle karşılaştırmak. Her kazanım gerçek bir alternatife görelidir.
- Tercih edilen seçeneğin bedelini gizlemek. Bedeli açıkça yaz; kararı güvenilir kılan budur.
- Geri alınabilir kararlara geri alınamazlar kadar tören uygulamak. Çift yönlü kapılarda hızlı karar ver.
- Belirleyicilerin haklı çıkarmadığı bir gelecek ölçeği için seçim yapmak.

## Örnek
Girdi: "Yeni hasar yönetim sistemimiz için modüler monolit mi, mikroservisler mi? Ekip 8 kişi, 9 ay içinde canlıya çıkış."

Çıktıdan bir bölüm:
| Nitelik | Modüler monolit | Mikroservisler |
|---|---|---|
| İlk sürüme kadar geçen süre | + tek deploy birimi, tek pipeline / - | - özelliklerden önce platform işi / + |
| Bağımsız ölçekleme | - tek birim olarak ölçeklenir / | + servis bazında ölçekleme / - daha fazla altyapı |
| Operasyon yükü | + düşük / | - 8 kişiyle dağıtık izleme ve çok sayıda pipeline `[VARSAYIM: platform ekibi yok]` |

Öneri: modül sınırları zorunlu tutulan modüler monolit. Canlıya çıkış hızı karşılığında kaba taneli ölçeklemeyi kabul ediyoruz. Bir modül ayrı sürüm ritmine veya ölçekleme profiline ihtiyaç duyduğunda yeniden ele al.
