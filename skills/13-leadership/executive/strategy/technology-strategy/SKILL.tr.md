---
name: technology-strategy
description: "İş hedeflerine bağlı, açık ödünleşimler, yapılmayacaklar ve ilerleme ölçütleri içeren; teşhis, yol gösterici politika ve tutarlı aksiyonlar şeklinde yapılandırılmış bir teknoloji stratejisi yazar. Bir CTO veya teknoloji liderinin çok yıllı bir yöne ihtiyacı olduğunda, mevcut planlar seçim içermeyen dilek listeleri olduğunda ya da mimari, platform, yetenek ve yatırım kararlarını iş stratejisiyle hizalarken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 13-leadership
  role: executive
  area: strategy
  title: "Teknoloji stratejisi yazma"
  related: "target-state-architecture, architecture-principles, product-strategy-one-pager, tech-radar, budget-proposal"
  prompt: "Sigorta şirketimiz için 3 yıllık teknoloji stratejisi yaz; eski bir çekirdek sistemimiz, yavaş sürümlerimiz ve yeni bir dijital satış hedefimiz var."
---

# Teknoloji Stratejisi Yazma

## Amaç
Organizasyona en önemli sorununu çözen az sayıda net teknoloji seçimi vermek. Böylece ekipler tutarlı kararlar alabilir, yönetim de bu seçimleri finanse edip izleyebilir.

## Ne zaman kullanılır
- Yeni bir teknoloji lideri veya yeni bir iş stratejisi, bir teknoloji yönü gerektiriyor.
- Mevcut planlar çok sayıda girişim sıralıyor ama teşhis veya öncelik içermiyor.
- Mimari, platform, kaynak sağlama ve yetenek kararları çelişiyor ve ortak bir çerçeveye ihtiyaç var.

## Ne zaman kullanılmaz
- Ayrıntılı hedef mimari ve geçiş durumları için `target-state-architecture` kullanılır.
- Gelecek çeyreğin taahhütleri ve kapasitesi için `quarterly-planning` kullanılır.
- Seçilmiş girişimler için finansman talebi için `budget-proposal` kullanılır.

## Girdiler
Zorunlu:
- Teknolojinin desteklemesi gereken iş stratejisi veya hedefler ve mevcut ana teknoloji sorunları.

İsteğe bağlı, kaliteyi artırır:
- Mevcut mimari, uygulama portföyü, teslimat metrikleri, maliyet tabanı, olay geçmişi.
- Organizasyon ve yetenek durumu, mevzuat kısıtları, pazar ve rakip hamleleri.
- Zaman ufku ve planlama döngüsü.

İş hedefleri yoksa sor; iş hedefi olmayan bir strateji teknoloji dilek listesine dönüşür.

## Süreç
1. Her alan için olguları topla (iş hedefleri, mimari, teslimat, güvenilirlik, güvenlik, veri, maliyet, insan) ve kanıtı görüşten ayır.
2. Teşhisi yaz: İş hedeflerini en çok engelleyen 1-3 kritik sorunu kanıtıyla, sade bir dille.
3. Yol gösterici politikayı tanımla: Teşhise yanıt veren 3-5 ilke veya seçim; her biri neyi tercih ettiğini ve neden vazgeçtiğini belirtsin.
4. Kapasite açmak için nelerin yapılmayacağını veya durdurulacağını açıkça yaz.
5. Tutarlı aksiyonları türet: Birbirini güçlendiren, bağımlılık ve riske göre sıralanmış 5-8 girişim; ilk 6-12 ay sonraki yıllardan daha ayrıntılı olsun.
6. Her aksiyonu bir iş hedefine ve teşhise bağla; hiçbirine bağlanmayan aksiyonları çıkar.
7. Ölçütleri tanımla: sonuç göstergeleri (ör. teslim süresi, erişilebilirlik, işlem başına maliyet, bir iş ortağını devreye alma süresi); verilmemişse başlangıç değerlerini `[BİLİNMİYOR]` olarak işaretle.
8. Başlıca riskleri, varsayımları ve stratejinin yeniden ele alınacağı karar noktalarını belirle.
9. Organizasyon, yetkinlik ve kaynak sağlama (yap, satın al, iş ortağı) etkilerini kişi adı vermeyen bir düzeyde tarif et.
10. Yöneticiler için tek sayfalık bir özet yaz; ayrıntıları eklerde tut.
11. Kullanıcının hedefi devam ediyorsa mimari ayrıntı için `target-state-architecture`, finansman için `budget-proposal` veya ilk taahhütler için `quarterly-planning` öner.

## Çıktı formatı
```markdown
# Teknoloji Stratejisi <ufuk>: <organizasyon>

## Yönetici Özeti (tek sayfa)

## İş Bağlamı ve Hedefler
- ...

## Teşhis
1. <sorun> – kanıt – iş hedeflerine etkisi

## Yol Gösterici Politika
| Seçim | Tercih ettiğimiz | Vazgeçtiğimiz |
|---|---|---|

## Durduracaklarımız / Yapmayacaklarımız
- ...

## Tutarlı Aksiyonlar
| # | Aksiyon | Çözdüğü sorun | İş hedefi | Ufuk | Bağımlılık |
|---|---|---|---|---|---|

## Ölçütler
| Gösterge | Başlangıç değeri | Hedef yönü | Gözden geçirme sıklığı |
|---|---|---|---|

## Organizasyon ve Kaynak Sağlama Etkileri
- ...

## Riskler, Varsayımlar, Yeniden Ele Alma Tetikleyicileri
- ...
```

## Kalite kontrol listesi
- [ ] Teşhis her şeyi sıralamıyor; kritik sorunu kanıtıyla adlandırıyor.
- [ ] Her yol gösterici seçim neden vazgeçildiğini belirtiyor.
- [ ] Her aksiyon teşhise ve bir iş hedefine bağlanıyor.
- [ ] "Durdur / yapma" maddeleri var ve somut.
- [ ] Uydurulmuş başlangıç değeri, maliyet veya tarih yok; bilinmeyenler işaretli.
- [ ] Yeniden ele alma tetikleyicileri ve gözden geçirme sıklığı tanımlı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Strateji kılığında hedefler ("bulut yerlisi, önce yapay zekâ, dünya standartlarında olmak"). Teşhis ve seçim yapmaya zorla.
- Eşit öncelikli çok sayıda girişim. Sınırla ve sırala; neyin daha az finansman alacağını göster.
- İnsan tarafını yok saymak. Aksiyonların gerçekleşip gerçekleşmeyeceğini çoğu zaman yetkinlik ve kaynak sağlama boşlukları belirler.

## Örnek
Girdi: Sigorta şirketi, eski çekirdek sistem, çeyreklik sürümler, hedef: iş ortakları üzerinden dijital satış.

Çıktıdan bir bölüm:
- Teşhis: Fiyatlama ve poliçe mantığı yalnızca batch arayüzlü eski çekirdekte bulunduğu için bir iş ortağını devreye almak aylar sürüyor `[mevcut devreye alma süresini teyit et]`.
- Yol gösterici seçim: Şimdi tam çekirdek değişimi yerine (vazgeçilen: daha hızlı kapatma) çekirdeğin önünde kararlı API'lerle ürün ve fiyatlamayı dışarı açmak (tercih).
- Zayıf aksiyon (kaçın): "BT'yi modernize et." Güçlü aksiyon: "İlk 2 ürün için fiyatlama API katmanını kur, 12 ay içinde ilk iş ortağını canlıya al."
