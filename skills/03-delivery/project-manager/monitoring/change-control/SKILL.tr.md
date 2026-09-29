---
name: change-control
description: "Bir değişiklik talebini değişiklik kontrolünden geçirir; talebi kaydeder, kapsam, takvim, maliyet, kalite, risk ve sözleşme üzerindeki etkisini değerlendirir, seçenekleri ortaya koyar, doğru karar merciine yönlendirir ve değişiklik kaydını ve temel planları günceller. Onaylı kapsam, tarih veya bütçeye ekleme, çıkarma ya da değişiklik istendiğinde, bir tedarikçi değişiklik talebi sunduğunda veya kapsam kaymasının görünür kılınıp karara bağlanması gerektiğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: monitoring
  title: "Değişiklik kontrolü"
  related: "scope-statement, impact-analysis, raid-log, decision-log, earned-value-analysis"
  prompt: "Müşteri artık kararlaştırılan girişe ek olarak kendi Azure AD'leriyle SSO istiyor. Değişiklik kurulu için etki değerlendirmeli bir değişiklik talebi hazırla."
---

# Değişiklik Kontrolü

## Amaç
Onaylı bir temel plana yapılan her değişikliği açık, değerlendirilmiş ve doğru merci tarafından karara bağlanmış hale getirmek. Böylece kapsam, takvim ve bütçe tutarlı kalır, kimse onaylanmamış işi sessizce üstlenmez.

## Ne zaman kullanılır
- Temel plan onaylandıktan sonra bir paydaş yeni veya değişmiş kapsam istediğinde.
- Bir tarih, bütçe veya kalite hedefinin değişmesi gerektiğinde.
- Bir tedarikçi değişiklik talebi sunduğunda ya da ek efor talep ettiğinde.
- Gayriresmî "küçük eklemeler" biriktiğinde ve görünür kılınması gerektiğinde.

## Ne zaman kullanılmaz
- Temel plan henüz onaylanmadıysa `scope-statement` ile netleştirilir.
- Değişikliğin derin teknik veya gereksinim etkisi için `impact-analysis` kullanılır, karar için buraya dönülür.
- Üretim sistemlerinde operasyonel bir değişiklikse proje değişiklik kontrolü değil, servis değişiklik süreci kullanılır.

## Girdiler
Zorunlu:
- Değişikliğin tanımı (ne, kim istedi, neden).
- Mevcut temel plan referansı (kapsam tanımı, takvim, bütçe) ya da ilgili bölümleri.

İsteğe bağlı, kaliteyi artırır:
- Yönetişim eşikleri (hangi büyüklükteki değişikliği kim onaylar), sözleşmenin değişiklik maddeleri.
- Ekipten gelen tahminler, bağımlılık haritası, güncel RAID kaydı.

Değişiklik tanımı veya temel plan referansı yoksa iste. Diğer her şey açık soru olur.

## Süreç
1. Talebi numara, talep sahibi, tarih ve talep sahibinin belirttiği gerekçeyle kaydet; sözel isteği altta yatan ihtiyaçtan ayır ve çıkarılan ihtiyacı `[VARSAYIM]` olarak işaretle.
2. Sınıflandır: kapsam ekleme, kapsam azaltma, kapsam değiştirme, takvim değişikliği, bütçe değişikliği, kalite/standart değişikliği ya da temel plan hatasının düzeltilmesi (değişiklik değildir).
3. Talebin zaten temel planda olup olmadığını kontrol et; kapsanıyorsa referans vererek netleştirme olarak kapat.
4. Kapsam, takvim (kritik yolda mı), maliyet (efor, lisans, tedarikçi), kalite, risk, kaynaklar, bağımlılıklar ve sözleşme üzerindeki etkiyi değerlendir; aralık kullan, henüz gelmemiş ekip tahminlerini `[TBD]` olarak işaretle.
5. Yan etkileri belirle: çöpe gidecek tamamlanmış iş, mevzuat veya güvenlik etkileri, diğer projelere etkiler.
6. Seçenekleri oluştur: istendiği gibi onay, ödünleşimle onay (eşit kapsamı çıkarma), sonraki faza erteleme, ret. Her birinin sonuçlarını ver.
7. Karar merciini yönetişim eşiklerinden belirle; eşikler verilmediyse bir öneri yap ve `[VARSAYIM]` olarak işaretle.
8. Tek paragraflık gerekçeyle bir seçenek öner; olgularla PM değerlendirmesini ayrı tut.
9. Karardan sonra kararı kaydet, temel planları (kapsam, takvim, bütçe), RAID kayıtlarını ve değişiklik kaydını güncelle, etkilenen taraflara bildir.
10. Kullanıcının hedefi devam ediyorsa derin teknik etki için `impact-analysis`, kararı kaydetmek için `decision-log` ya da izlemeyi yeni temele almak için `earned-value-analysis` öner.

## Çıktı formatı
```markdown
# Değişiklik Talebi CR-<no>: <kısa başlık>
| Alan | Değer |
|---|---|
| Talep eden / tarih | <...> |
| Tür | <sınıflandırma> |
| Gerekçe (belirtilen) | <...> |
| Altta yatan ihtiyaç | <... veya [VARSAYIM]> |
| Karar mercii | <rol / kurul> |
| Durum | Sunuldu / Değerlendirildi / Onaylandı / Reddedildi / Ertelendi |

## Etki Değerlendirmesi
| Boyut | Etki | Güven | Notlar |
|---|---|---|---|
| Kapsam | | | |
| Takvim | | | |
| Maliyet | | | |
| Kalite / risk | | | |
| Kaynak / bağımlılık | | | |
| Sözleşme | | | |

## Seçenekler
| Seçenek | Sonuçlar | Maliyet / süre |

## Öneri
## Karar Kaydı
Karar: <...> | Veren: <...> | Tarih: <...> | Güncellenen temel planlar: <liste>

## Açık Sorular
```

## Kalite kontrol listesi
- [ ] Değişiklik hafızaya göre değil, gerçek temel plana göre karşılaştırıldı.
- [ ] Her etki boyutu değerlendirildi ya da sahibiyle birlikte `[TBD]` olarak işaretlendi.
- [ ] "İstendiği gibi onay" dışında en az bir alternatif sunuldu.
- [ ] Karar mercii değişikliğin büyüklüğüyle uyumlu.
- [ ] Karar sonrası temel plan ve kayıt güncellemeleri listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- "Küçük" değişiklikleri gayriresmî onaylamak; toplamları bütçe aşımına dönüşür. Eşik altında otomatik onaylansa bile her değişikliği kaydet.
- Yalnızca maliyeti değerlendirip kritik yolu, test eforunu veya operasyonu atlamak.
- Teslim edilen işteki hataları değişiklik talebi saymak (ya da tersi). Kabul kriterleriyle karşılaştır.

## Örnek
Girdi: "Müşteri kararlaştırılan kullanıcı adı/parola girişinin yanında kendi Azure AD'leriyle SSO istiyor."

Çıktıdan bir bölüm:
- Tür: Kapsam ekleme. Temel plan yalnızca yerel girişi kapsıyor (Kapsam tanımı §3.2).
- Altta yatan ihtiyaç: `[VARSAYIM]` güvenlik politikalarından kaynaklanan, işe giriş/çıkışlar için merkezi hesap yaşam döngüsü.
- Seçenekler: (a) mevcut sürüme ekle – takvim etkisi `[TBD – ekip tahmini]`; (b) raporlama modülüyle takas; (c) 2. faz.
- Karar mercii: değişiklik kurulu (PM eşiğinin üstünde) `[eşiği teyit et]`.
