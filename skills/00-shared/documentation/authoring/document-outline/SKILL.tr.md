---
name: document-outline
description: "Herhangi bir doküman (tasarım dokümanı, politika, rehber, rapor, teklif, şartname) için amacından, hedef kitlesinden ve desteklemesi gereken kararlardan yola çıkarak bölüm hedefleri ve içerik notlarıyla uygun bir yapı önerir. Yeni bir doküman başlatılacağında, boş sayfa karşısında kalındığında, dağınık bir doküman yeniden yapılandırılacağında veya bir dokümanda hangi bölümlerin olması gerektiği sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 00-shared
  role: documentation
  area: authoring
  title: "Doküman iskeleti çıkarma"
  related: "docs-information-architecture, document-review, executive-summary, technical-design-doc, brd-writing"
  prompt: "Batch raporlama işlerimizi event-driven bir pipeline'a taşımayı öneren bir dokümanın iskeletini çıkar; okuyucular mimari kurul."
---

# Doküman İskeleti Çıkarma

## Amaç
Dokümanın ulaşması gereken sonuçtan türetilmiş, bölüm bölüm bir iskelet üretmek. Böylece yazar yapıyı yazarken keşfetmek yerine kanıtlanmış bir yapıyı doldurur, okuyucu da ihtiyaç duyduğu bilgiyi ihtiyaç duyduğu sırada bulur.

## Ne zaman kullanılır
- Yeni bir doküman gerektiğinde ve yazar konuyu bilip yapıyı bilmediğinde.
- Mevcut bir doküman plansız büyüdüğünde ve yeniden yazımdan önce yeni bir yapıya ihtiyaç duyduğunda.
- Birden fazla yazar katkı verecekse ve bölüm sorumlularıyla üzerinde anlaşılmış bir iskelet gerektiğinde.
- Kurum şablonu var ama bu özel duruma uymuyor ve uyarlanması gerekiyorsa.

## Ne zaman kullanılmaz
- Çok sayfalı bir doküman setinin bütünü düzenlenecekse `docs-information-architecture` kullanılır.
- Doküman mevcutsa ve yeni yapı değil kalite geri bildirimi isteniyorsa `document-review` kullanılır.
- Doküman türünün kendi şablonuyla ayrı bir skill'i varsa (ör. `technical-design-doc`, `brd-writing`, `adr`) o kullanılır.

## Girdiler
Zorunlu:
- Dokümanın amacı: okuyucu okuduktan sonra neyi bilecek, neye karar verecek veya ne yapacak.
- Birincil hedef kitle.

İsteğe bağlı, kaliteyi artırır:
- Doküman türü ve zorunlu kurum şablonu veya standart.
- Kaynak materyal, notlar veya mevcut taslak.
- Uzunluk sınırı, son tarih, gözden geçirenler ve onaylayanlar.

Amaç veya hedef kitle eksikse tek bir soruyla iste. Geri kalanı varsayım veya açık soru olur.

## Süreç
1. Amacı tek cümleyle yeniden yaz: "Okuduktan sonra <hedef kitle> <X>'i bilecek/karar verecek/yapacak." Okuyucu karar verecekse yapı karar öncelikli olur.
2. Dokümanı sınıflandır: karar (teklif, ADR benzeri), referans (şartname, politika, API), yönlendirici (rehber, runbook) veya anlatı/rapor (durum, değerlendirme). Her birinin omurgası farklıdır.
3. İkincil hedef kitleleri ve her birinin neye göz gezdireceğini belirle; hepsini okumadan onlara hizmet eden bir özet veya tablo planla.
4. Omurgayı seç: karar = bağlam, problem, seçenekler, öneri, sonuçlar; referans = kapsam, tanımlar, kurallar/maddeler, istisnalar; yönlendirici = ön koşullar, adımlar, doğrulama, sorun giderme; rapor = özet, bulgular, analiz, sonraki adımlar.
5. Zorunlu içeriği kontrol et: yasal bölümler, standart yapılar (ör. gereksinimler için ISO/IEC/IEEE 29148, mimari için arc42), kurum şablonları. Bunları tekrarlamak yerine omurgaya eşle.
6. Her bölüm için amacını ve cevapladığı temel soruyu tek satırda yaz; içerik notlarını ve kullanılacak kaynakları ekle.
7. Bölümleri yazım sırasına veya kronolojiye göre değil okuyucu ihtiyacına göre sırala; birincil okuyucunun ihtiyacını öne koy.
8. Amaca hizmet etmeyen bölümleri çıkar; olsa iyi olur içeriği eklere taşı.
9. Toplam uzunluk sınıra sığsın diye bölüm başına uzunluk rehberi ver; başkalarından girdi gerektiren bölümleri sorumluyla veya `[TBD]` ile işaretle.
10. Belirli bölümleri engelleyen açık soruları listele.
11. Girdide okunmayıp çıkarımla belirlenen her bölümü, hedef kitleyi veya amacı `[VARSAYIM]` olarak işaretle; böylece talep sahibi yazıma başlamadan önce teyit edebilir.
12. Kullanıcının hedefi devam ediyorsa iskeleti doldurmak için `technical-design-doc` veya `brd-writing`, ardından taslak için `document-review` öner.

## Çıktı formatı
```markdown
# İskelet: <doküman başlığı>
Amaç: Okuduktan sonra <hedef kitle> <X>'i bilecek/karar verecek/yapacak.
Doküman türü: <karar / referans / yönlendirici / rapor>
Birincil hedef kitle: <...> | İkincil: <...>
Hedef uzunluk: <sayfa veya kelime> | Zorunlu şablon/standart: <ad veya yok>

| # | Bölüm | Amaç / cevapladığı soru | İçerik notları ve kaynaklar | Uzunluk | Sorumlu |
|---|---|---|---|---|---|
| 1 | Özet | <...> | <...> | <...> | <...> |

## Ekler
- <ana akıştan çıkarılan içerik>

## Açık Sorular
1. <soru> — <engellenen bölüm> — <kim cevaplayabilir>
```

## Kalite kontrol listesi
- [ ] Amaç cümlesi bir hedef kitle ve bir sonuç içeriyor.
- [ ] Omurga doküman türüne uygun (karar dokümanları öneri veya istenen kararla başlıyor).
- [ ] Her bölümün belirtilmiş bir amacı var; hiçbiri "şablonda var" diye durmuyor.
- [ ] Zorunlu bölümler mevcut ve eşlenmiş, tekrarlanmamış.
- [ ] Bölüm uzunlukları hedef uzunluğa denk geliyor.
- [ ] Bilinmeyenler `[TBD]` olarak işaretli veya açık soru olarak listeli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- İskeleti yazarın konuyu öğrendiği sırayla kurmak (önce tarihçe). Okuyucu önce sonucu ve talebi görmek ister.
- Genel bir şablonu olduğu gibi kopyalamak; bölümlerin yarısı "Uygulanamaz" kalır. Uyarla ve sil.
- Referans ve yönlendirici içeriği tek akışta karıştırmak. Adımları olgulardan ayır veya ayrı bölümler kullan.

## Örnek
Girdi: "Batch raporlama işlerini event-driven pipeline'a taşıma teklifi, mimari kurul için."

Çıktıdan bir bölüm:
- Amaç: Okuduktan sonra mimari kurul, event-driven raporlama için bir pilotun finanse edilip edilmeyeceğine karar verecek.
- Tür: karar.
- | 1 | İstenen karar | Kuruldan tam olarak neyin onayı isteniyor? | Kapsam, bütçe `[TBD]`, pilot süresi | 0,5 sayfa | Yazar |
- | 4 | Değerlendirilen seçenekler | Neden batch'i korumuyor veya iyileştirmiyoruz? | Mevcut durum, iyileştirilmiş batch, CDC + streaming | 1 sayfa | Yazar |
- Açık soru: Pilot bütçesi kurulun onay limiti içinde mi? — bölüm 1 — PMO.
