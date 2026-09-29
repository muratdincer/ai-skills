---
description: Bir proje, sürüm, faz, olay veya girişimden çıkarılan dersleri; neyin işe yarayıp neyin yaramadığına dair kanıta dayalı gözlemler, nedenleri ve korunacak ya da değiştirilecek, sahibi ve uygulanacağı yer belli somut aksiyonlar olarak kayda geçirir. Bir proje veya fazın sonunda, bir sürüm ya da önemli bir olaydan sonra, kapanış raporu hazırlanırken veya notlar, retrospektifler ya da zaman çizelgelerinden "çıkarılan dersleri yaz" dendiğinde kullanılır.
related: retrospective-facilitation, postmortem, project-closure-report, kb-article, action-item-extraction
prompt: Bu retro notlarını ve zaman çizelgesini kullanarak CRM geçiş projemizden çıkarılan dersleri yaz.
---

# Çıkarılan Dersleri Kaydetme

## Amaç
Deneyimi yeniden kullanılabilir ve uygulanabilir bilgiye dönüştürmek; böylece sonraki ekip aynı hataları tekrarlamaz ve işe yarayanı korur. Bir ders, ancak bir yerde bir uygulamayı, şablonu, kontrol listesini veya karar kuralını değiştiriyorsa ders sayılır.

## Ne zaman kullanılır
- Bir proje, faz, sürüm veya büyük girişim bittiğinde ya da bir kilometre taşına ulaştığında.
- Retrospektif notları, zaman çizelgesi veya durum raporları var ve başkaları için damıtılması gerekiyorsa.
- Kapanış raporu ya da portföy değerlendirmesi bir dersler bölümü istiyorsa.

## Ne zaman kullanılmaz
- Tek bir üretim olayı için suçlamasız nedensel analiz gerekiyorsa `postmortem` kullanılır.
- Ekibin değerlendirme oturumunun kendisi yürütülecekse `retrospective-facilitation` kullanılır.
- Kapsam, bütçe ve devri içeren resmi bir proje sonu dokümanı isteniyorsa `project-closure-report` kullanılır.

## Girdiler
Zorunlu:
- Kaynak materyal: retro notları, zaman çizelgesi, durum raporları, olay notları veya kullanıcının kendi anlatımı.

İsteğe bağlı, kaliteyi artırır:
- Başlangıç hedefleri, başarı kriterleri, plan ve gerçekleşen (tarih, kapsam, bütçe).
- Derslerin hedef kitlesi (aynı ekip, diğer ekipler, yönetim, portföy ofisi).
- Derslerin nerede saklandığı ve nasıl yeniden kullanıldığı (şablonlar, kontrol listeleri, bilgi bankası).

Kaynak materyal verilmemişse kullanıcıdan olanları kısaca anlatmasını, her seferinde tek bir odaklı soru sorarak (en fazla 5) iste.

## Süreç
1. Bağlamı üç satırda ortaya koy: çalışmanın ne olduğu, hedefleri ve girdinin desteklediği boyutlarda plan ile gerçekleşen. Eksik rakamları `[BİLİNMİYOR]` olarak işaretle; asla tahmin etme.
2. Kaynaktan ham gözlemleri çıkar ve her birini "iyi gitti", "kötü gitti" veya "sürpriz" olarak etiketle. Kanıt taşıyan yerlerde kullanıcının ifadesini koru.
3. Olguyu yorumdan ayır: her gözlem kanıtını (olay, tarih, metrik, doküman) göstersin; çıkarım olan her şey `[VARSAYIM]` olarak işaretlensin.
4. Gözlemleri temalara grupla (örneğin planlama, gereksinimler, bağımlılıklar, teknik, test, iletişim, paydaşlar, araçlar, insan). Tekrarları birleştir.
5. Her önemli tema için, bir kişiye değil kurumun üzerinde aksiyon alabileceği bir nedene (süreç, karar kuralı, şablon, yetkinlik veya yapı) ulaşana kadar "bu neden oldu?" diye sor. Tonu suçlamasız tut.
6. Her dersi şöyle yaz: bağlam → ne oldu → neden → ders (genellenebilir bir kural) → aksiyon. Yalnızca olayı tekrar eden bir ders ("test geç kaldı") bitmiş sayılmaz.
7. Aksiyonları koru, başla, bırak veya değiştir olarak tanımla; her birine sahip, hedef (uygulanacağı şablon, kontrol listesi, süreç veya ekip) ve bitiş tarihi ya da `[TBD]` ver.
8. Önceliklendir: gelecekteki çalışmalara beklenen etkisi en yüksek 3-5 dersi işaretle; küçük gözlemleri eke taşı.
9. Hedef kitle ve gizliliği kontrol et: kişisel suçlamayı, olumsuz bağlamdaki isimleri ve kişisel verileri çıkar; hassas olanı maskele.
10. Çıktı şablonunu doldur ve açık soruları listele.
11. Hedef devam ediyorsa sonraki beceriyi öner: bir dersi yeniden kullanım için yayımlamak üzere `kb-article`, aksiyonları bir takip aracına aktarmak için `action-item-extraction`, kapanışa dahil etmek için `project-closure-report`.

## Çıktı formatı
```markdown
# Çıkarılan Dersler: <çalışmanın adı>
Dönem: <başlangıç – bitiş> · Hedef kitle: <kim> · Kaynaklar: <retro notları, zaman çizelgesi, ...>

## Bağlam
- Hedef: ... · Plan ve gerçekleşen: <kapsam/zaman/bütçe veya [BİLİNMİYOR]>

## Öne Çıkan Dersler
### D1. <kural olarak ders, tek cümle>
- Bağlam / ne oldu: ... (kanıt: ...)
- Neden: ... [çıkarımsa VARSAYIM]
- Aksiyon: <Koru/Başla/Bırak/Değiştir> — <ne> — sahibi: <isim/rol veya TBD> — uygulanacağı yer: <şablon/süreç> — tarih: <tarih veya TBD>

## İşe Yarayanlar (korunacak)
- ...

## Diğer Gözlemler
- ...

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Her ders bir olayın tekrarı değil, genellenebilir bir kural.
- [ ] Her dersin sahibi ve uygulanacağı somut bir yeri olan en az bir aksiyonu var.
- [ ] Gözlemler kanıta dayanıyor; çıkarımlar `[VARSAYIM]` olarak etiketli; uydurma rakam yok.
- [ ] Hem işe yarayanlar hem yaramayanlar kaydedilmiş.
- [ ] Metin suçlamasız ve gereksiz kişisel veri içermiyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Dersler kaydedildi ama öğrenilmedi": dosyalanıp unutulan bir doküman. Her aksiyonu bir şablona, kontrol listesine veya süreç sahibine bağla.
- Kişileri suçlamak ("tedarikçi beceriksizdi"). Sonuca izin veren koşulu anlat; örneğin sözleşmede kabul kapılarının olmaması.
- Yalnızca olumsuzları listelemek. İşe yarayan da aynı derecede değerlidir ve tekrarlaması daha kolaydır.

## Örnek
Girdi: "Retro notları: veri taşıma 3 hafta kaydı, kaynak veri kalitesi beklenenden kötüydü, iş birimi anahtar kullanıcıları teste geç katıldı. Günlük geçiş toplantıları iyi işledi."

Zayıf ders: "Veri kalitesi kötüydü."
Güçlü ders: "D1. Taşıma tarihlerini kesinleştirmeden önce kaynak veriyi profille." Neden: tarihler hiçbir profilleme yapılmadan belirlendi `[VARSAYIM: PM ile teyit et]`. Aksiyon: Değiştir — taşıma planı şablonuna veri profilleme adımı ve çıkış kriteri ekle — sahibi: PMO `[TBD]`.
Koru: son iki haftadaki günlük geçiş toplantıları.
