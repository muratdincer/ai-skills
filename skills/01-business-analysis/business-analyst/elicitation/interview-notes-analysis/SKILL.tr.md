---
description: "Ham görüşme notlarını veya dökümlerini analiz eder; ihtiyaçları, sorunları, iş kurallarını, istisnaları, anılan veri ve sistemleri, çelişkileri ve açık soruları kaynağına bağlı olarak çıkarır. Bir veya daha fazla gereksinim görüşmesinden sonra, notlar dağınıksa veya 'bu görüşmelerden ne öğrendik?' sorusu geldiğinde kullanılır."
related: "interview-question-set, business-rules-catalog, requirements-consistency-check, feedback-synthesis, open-questions-tracker"
prompt: "Üç borç muhasebesi uzmanıyla yaptığım görüşmelerin notları burada. İhtiyaçları, sorunları, kuralları ve çelişkileri çıkar."
---

# Görüşme Notlarını Analiz Etme

## Amaç
Görüşme notlarını, olguları, görüşleri ve yorumları birbirinden ayrı tutarak gereksinimlere girdi olabilecek yapılandırılmış ve izlenebilir bulgulara dönüştürmek.

## Ne zaman kullanılır
- Gereksinim görüşmelerinden sonra, gereksinimler yazılmadan önce.
- Birden çok kişiyle yapılan görüşmelerin notları karşılaştırılacağında.
- Döküm uzun ve analistin özüne hızla ulaşması gerektiğinde.

## Ne zaman kullanılmaz
- Notlar, kararların ve aksiyonların önemli olduğu bir toplantıya aitse `meeting-notes` veya `action-item-extraction` kullanılır.
- Çok sayıda müşteri geri bildirimi sıklığa göre temalandırılacaksa `feedback-synthesis` kullanılır.

## Girdiler
Zorunlu:
- Her biri için görüşülen kişinin rolü belirtilmiş görüşme notları veya dökümleri.

İsteğe bağlı, kaliteyi artırır:
- Görüşme hedefleri, girişim kapsamı, önceki bulgular, terimler sözlüğü.

Notlar yoksa iste. Roller yoksa kaynakları Görüşmeci A, B, C olarak etiketle ve devam et.

## Süreç
1. Gerekmeyen kişisel verileri maskele (üçüncü kişilerin adları, müşteri bilgileri); görüşülenlere rol veya kodla atıf yap.
2. Notları ifadelere böl; her birini etiketle: Olgu (gözlenen/anlatılan uygulama), Görüş, İhtiyaç, Sorun, Kural, İstisna, Geçici çözüm, Veri/Sistem, Metrik veya Fikir/çözüm önerisi.
3. İhtiyaçları problem odaklı ifadelerle yeniden yaz ("Y'den önce X'i bilmem gerekiyor"); çözüm fikirlerini ayrı tut.
4. İş kurallarını standart biçimde (koşul → eylem) ve belirtilen kaynağıyla çıkar; yalnızca bir kişiden duyulan kuralları `[TEYİT EDİLECEK]` olarak işaretle.
5. Notların izin verdiği yerde sayısallaştır (sıklık, hacim, süre); asla rakam uydurma.
6. Görüşülenleri karşılaştır: uzlaşmaları, çelişkileri ve aynı adım için farklı uygulamaları bul.
7. Bulguları kişiler arası tekrar sıklığına ve belirtilen etkiye göre önceliklendir.
8. Açık soruları ve takip konularını, her birini kimin cevaplayabileceğiyle listele.

## Çıktı formatı
```markdown
# Görüşme Analizi: <girişim>
Kaynaklar: <kodlar ve roller> · Tarih(ler): <...>

## Ana bulgular (ilk 5)
1. ... (kaynaklar: A, C)

## İhtiyaçlar
| ID | İhtiyaç | Kaynaklar | Kanıt (kısa alıntı) |
|---|---|---|---|

## Sorunlar ve geçici çözümler
| ID | Sorun | Geçici çözüm | Sıklık / etki | Kaynaklar |

## İş kuralları ve istisnalar
| ID | Kural (koşul → eylem) | İstisna | Kaynak | Durum |

## Anılan veri ve sistemler
- ...

## Çelişkiler
- A ... diyor, B ... diyor → çözülecek soru

## Gündeme gelen çözüm fikirleri (gereksinim değil)
- ...

## Açık sorular
- ...
```

## Kalite kontrol listesi
- [ ] Her bulgu en az bir kaynağa izlenebiliyor.
- [ ] Olgular, görüşler ve çözüm fikirleri ayrı tutuldu.
- [ ] Tek kaynaktan gelen kurallar `[TEYİT EDİLECEK]` olarak işaretli.
- [ ] Çelişkiler ortalaması alınarak yok edilmedi, gösterildi.
- [ ] Gerekmeyen kişisel veriler maskelendi.
- [ ] Notlarda olmayan hiçbir rakam yok.

## Sık yapılan hatalar
- Güçlü bir görüşü gereksinime yükseltmek. Kaynakları say ve kanıt ara.
- İstisnaları kaybetmek. "... hariç" cümleleri çoğu zaman tasarım eforunun büyük kısmını belirler.
- Her görüşmeyi karşılaştırmadan ayrı ayrı özetlemek. Değer farklılıklardadır.

## Örnek
Girdi: "A: 'Her faturayı siparişle elle karşılaştırıyorum, çok uzun sürüyor; elektrik-su faturaları hariç, onları direkt ödüyoruz.' B: 'Sipariş eşleşmesi olmadan asla ödeme yapmayız.'"

Çıktıdan bir bölüm:
| ID | Kural (koşul → eylem) | İstisna | Kaynak | Durum |
|---|---|---|---|---|
| BR-1 | Fatura geldi → ödeme öncesi siparişle eşleştir | Elektrik-su faturaları siparişsiz ödeniyor (A) | A, B | Çelişkili |

Çelişkiler: A bir fatura istisnası anlatıyor; B istisna olmadığını söylüyor → politikayı borç muhasebesi yöneticisiyle teyit et.
