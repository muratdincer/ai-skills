---
name: client-steering-report
description: "Bir danışmanlık veya teslimat işi için müşteriye yönelik yönlendirme komitesi raporu yazar; açık bir puanlama kuralıyla plana göre genel durumu, kilometre taşlarındaki ilerlemeyi, üzerinde uzlaşılan sonuçlara göre sağlanan değeri, bütçe ve efor tüketimini, öne çıkan risk ve sorunları, değişiklik taleplerini ve müşteri yönlendirme grubunun alması gereken kararları kapsar. Bir müşteri yönlendirme komitesi veya yönetici incelemesi öncesinde, dönemsel bir iş raporu zamanı geldiğinde ya da teslimat verileri karar odaklı bir müşteri güncellemesine çevrilecekken kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 14-presales-consulting
  role: presales-consultant
  area: consulting
  title: "Müşteri yönlendirme raporu"
  related: "steering-committee-pack, project-status-report, benefits-realization, raid-log, bad-news-delivery"
  prompt: "Müşterimizin CRM geçişi için aylık yönlendirme raporunu yaz: 2. faz iki hafta geride, bütçe yolunda, veri taşıma kapsamı için karar gerekiyor."
---

# Müşteri Yönlendirme Raporu

## Amaç
Müşterinin yönlendirme grubuna işin dürüst ve karara hazır bir görünümünü vermek: nerede durduğu, hangi değeri sağladığı, onu neyin tehdit ettiği ve tam olarak neye karar vermeleri gerektiği. Böylece yönetişim zamanı durum okumaya değil kararlara gider.

## Ne zaman kullanılır
- Bir müşteri yönlendirme komitesi, yönetici incelemesi veya çeyreklik iş değerlendirmesi planlandığında.
- Sözleşme gereği dönemsel bir iş raporu teslim edilmesi gerektiğinde.
- Teslimat verileri (plan, tüketim, RAID, değişiklik talepleri) müşteri yöneticileri için yorumlanacaksa.

## Ne zaman kullanılmaz
- Kendi kurumunuz için iç portföy veya program yönlendirme paketi hazırlanıyorsa `steering-committee-pack` kullanılır.
- Rutin ekip düzeyinde durum güncellemesi gerekiyorsa `project-status-report` veya `status-update` kullanılır.
- İş bittikten sonra gerçekleşen faydalar ölçülüyorsa `benefits-realization` kullanılır.

## Girdiler
Zorunlu:
- Raporlama dönemi ve işin kapsamı.
- Güncel teslimat verileri: plana göre kilometre taşı durumu, öne çıkan riskler ve sorunlar ve gereken karar.

İsteğe bağlı, kaliteyi artırır:
- Temel plan, bütçe ve efor tüketimi; değişiklik talebi kaydı.
- Teklif veya SOW'daki üzerinde uzlaşılan sonuçlar veya KPI'lar.
- Önceki yönlendirme raporu ve aksiyon maddeleri.
- Müşteri tarafı bağımlılıklar ve durumları.

Durum verisi veya dönem yoksa sor. Yüzde, harcama veya fayda asla uydurma; `[BİLİNMİYOR]` olarak işaretle.

## Süreç
1. Puanlamadan önce puanlama kuralını belirt (ör. Yeşil: planda; Sarı: yönlendirme aksiyonu olmadan faz içinde telafi edilebilir sapma; Kırmızı: yönlendirme kararı veya yeniden planlama gerekir) ve bunu takvim, bütçe, kapsam, kalite ve genel duruma uygula.
2. Üç satırlık bir özet yaz: genel durum ve nedeni, son rapordan bu yana en önemli değişiklik ve bugün istenen kararlar.
3. Kilometre taşı ilerlemesini temel plana göre raporla: planlanan ve öngörülen tarihler, sapma ve nedeni. Umut değil öngörü sun; dayanağı olmayan tarih `[BİLİNMİYOR]` olur.
4. Üzerinde uzlaşılan sonuçlara göre sağlanan değeri raporla: kullanıcıların artık ne yapabildiği, ölçülüyorsa benimseme veya KPI hareketi. Çıktıları (teslim edilen) sonuçlardan (ulaşılan) ayır ve veri olmadan sonuç iddia etme.
5. Bütçe ve eforu raporla: bugüne kadarki tüketim, tamamlanmadaki öngörü, sapma ve etkenler; bekleyen değişiklik taleplerinin etkisini dahil et.
6. Etkisi, sorumlusu (tedarikçi veya müşteri) ve azaltma eylemiyle en önemli 3-5 risk ve sorunu sun; geciken müşteri tarafı bağımlılıkları olgusal ve suçlamadan belirt.
7. Her kararı şöyle çerçevele: bağlam, zaman, maliyet, kapsam ve risk etkisiyle seçenekler (hiçbir şey yapmamak dahil), önerin ve kararın son tarihi.
8. Önceki yönlendirme toplantısının aksiyonlarını gözden geçir: tamamlanan, açık, geciken.
9. Kötü haberi erken ve açıkça ver: olgu, etki ve telafi planıyla başla; eke gömme.
10. Raporu bir yönlendirme grubunun on dakikada okuyacağı kadar tut; ayrıntıyı eklere taşı. Çıkarımları ve öngörüleri `[VARSAYIM]` veya `[ÖNGÖRÜ]` olarak etiketle.
11. Hedef devam ediyorsa toplantı slaytları için `presentation-outline`, zor bir mesaj için `bad-news-delivery` veya sonuç takibi için `benefits-realization` öner.

## Çıktı formatı
```markdown
# Yönlendirme Raporu: <müşteri> — <iş> — <dönem>
## Özet
| Genel | Takvim | Bütçe | Kapsam | Kalite |
|---|---|---|---|---|
| <RAG> | <RAG> | <RAG> | <RAG> | <RAG> |
- Neden: ...  - Son rapordan bu yana ana değişiklik: ...  - İstenen kararlar: ...
Puanlama kuralı: ...

## Kilometre Taşları
| Kilometre taşı | Temel plan | Öngörü | Sapma | Neden / telafi |

## Sağlanan Değer
| Uzlaşılan sonuç | Şimdiye kadar teslim edilen (çıktı) | Sonucun kanıtı |

## Bütçe ve Efor
| Bütçe | Harcanan | Tamamlanmada öngörü | Sapma | Etkenler |

## Riskler ve Sorunlar
| # | Risk / sorun | Etki | Sorumlu (tedarikçi/müşteri) | Azaltma | Tarih |

## Değişiklik Talepleri
| DT | Açıklama | Etki | Durum |

## Gereken Kararlar
### K1: <başlık>
- Bağlam: ...  - Seçenekler: A / B / hiçbir şey yapmamak (etki)  - Öneri: ...  - Gereken tarih: ...

## Önceki Aksiyonlar
| Aksiyon | Sorumlu | Durum |

## Ek
```

## Kalite kontrol listesi
- [ ] Puanlama kuralı belirtilmiş ve her RAG ona uyuyor; kırmızı ayrıntıların üstünde "karpuz" yeşili yok.
- [ ] Her kararın seçenekleri, etkileri, önerisi ve son tarihi var.
- [ ] Çıktılar ve sonuçlar ayrılmış; ölçülmemiş fayda iddiası yok.
- [ ] Öngörüler, harcamalar ve yüzdeler girdiden geliyor ya da `[BİLİNMİYOR]` olarak işaretli.
- [ ] Müşteri tarafı bağımlılıklar sorumlusu ve etkisiyle olgusal olarak belirtilmiş.
- [ ] Ana gövde yaklaşık on dakikada okunabiliyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Talep içermeyen durum raporu. Yönlendirme raporu karar almak için vardır; karar gerekmiyorsa bunu açıkça yaz.
- Gecikmeleri kriz olana kadar yumuşatmak. Sapmayı ilk öngörüldüğü anda telafi planıyla raporla.
- Faaliyetleri değer diye listelemek ("40 çalıştay yapıldı"). Müşterinin artık ne yapabildiğini veya ölçebildiğini göster.

## Örnek
Girdi: "CRM geçişi, 2. faz müşteri test verisinin gecikmesi nedeniyle iki hafta geride; bütçe yolunda; 10 yıllık mı 3 yıllık mı geçmiş taşınacağına karar gerekiyor."

Zayıf: "Durum: genel olarak Yeşil. 2. fazda bazı küçük gecikmeler var. Veri taşıma konuşuluyor."

Güçlü:
- Genel Sarı (kural: faz içinde telafi edilebilir). 2. faz canlıya geçiş öngörüsü +2 hafta; neden: test verisi uzlaşılan tarihten sonra teslim edildi `[gün sayısını teyit et]` (müşteri bağımlılığı).
- K1: Taşıma kapsamı. Seçenekler: A) 10 yıllık geçmiş: +`[BİLİNMİYOR]` AG, +3 hafta `[ÖNGÖRÜ]`; B) 3 yıl artı arşive erişim: takvim etkisi yok. Öneri: B. Gereken tarih: bir sonraki yönlendirme toplantısı.
