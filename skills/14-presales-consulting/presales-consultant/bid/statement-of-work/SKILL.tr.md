---
name: statement-of-work
description: "Hedefleri, kapsam içi ve kapsam dışı işleri, kabul kriterleri ve prosedürüyle teslimatları, kilometre taşlarını, iki tarafın rol ve sorumluluklarını, varsayımları, bağımlılıkları, değişiklik kontrolünü ve ticari referansları sınanabilir ve yoruma kapalı bir dille tanımlayan bir iş tanımı (SOW) yazar. Bir teklif kabul edilip kapsamın sözleşmeyle sabitlenmesi gerektiğinde, bir çerçeve sözleşme altında proje veya faz için SOW gerektiğinde ya da mevcut bir SOW belirsizlik ve kapsam kayması riski açısından gözden geçirilecekse kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 14-presales-consulting
  role: presales-consultant
  area: bid
  title: "İş tanımı (SOW) yazma"
  related: "proposal-writing, effort-estimate-for-bid, scope-statement, acceptance-certificate, change-control"
  prompt: "Müşteri portalı projesinin 1. fazı için SOW taslağı hazırla: SSO, sipariş takibi ve ERP sipariş senkronizasyonu, sabit fiyat, 4 ay."
---

# İş Tanımı (SOW) Yazma

## Amaç
Neyin teslim edileceğini, nasıl kabul edileceğini ve kimin neden sorumlu olduğunu sabitlemek. Böylece iki taraf da kapsam hakkında tek ve bağlayıcı bir anlayışı paylaşır, anlaşmazlıklar hafızayla değil dokümanla çözülür.

## Ne zaman kullanılır
- Bir teklif kabul edildiğinde ve kapsam, teslimatlar ve kabulün sözleşmeyle kararlaştırılması gerektiğinde.
- Mevcut bir çerçeve sözleşme altında yeni bir proje, faz veya iş paketi sipariş edildiğinde.
- Mevcut bir SOW belirsiz ifadeler, eksik kabul koşulları veya gizli yükümlülükler açısından gözden geçirilecekse.

## Ne zaman kullanılmaz
- Müşteri hâlâ ikna ediliyorsa `proposal-writing` kullanılır.
- Sözleşme tarafı olmadan kendi ekibiniz için iç proje kapsamı gerekiyorsa `scope-statement` kullanılır.
- Teslim edilen işin resmi kabulü kayda alınıyorsa `acceptance-certificate` kullanılır.

## Girdiler
Zorunlu:
- Üzerinde uzlaşılmış kapsam dayanağı: teklif, tahmin, gereksinim listesi veya keşif çıktısı.
- Ticari model (sabit fiyat, zaman-malzeme, tavanlı) ve taraflar.

İsteğe bağlı, kaliteyi artırır:
- SOW'un atıf yapması gereken çerçeve sözleşme hükümleri (hukuki hükümler orada kalır).
- Tahmin varsayımları ve kapsam dışı maddeler; plan ve kilometre taşları.
- Müşterinin zorunlu SOW şablonu, kabul politikası, garanti beklentileri.

Kapsam dayanağı veya ticari model yoksa sor. Hukuki madde (sorumluluk, fikri mülkiyet, fesih) yazma; çerçeve sözleşmeye atıf yap ve `[HUKUKİ İNCELEME]` olarak işaretle.

## Süreç
1. Arka planı ve hedefleri teklife dayandırarak iki ila dört cümleyle yaz. Hedefler niyeti açıklar; teslimat değildir ve ek yükümlülük doğurmamalıdır.
2. Kapsam içi işi iş akışı bazında ölçülebilir sınırlarla tanımla (entegrasyon, ortam, kullanıcı rolü, dil sayısı, veri hacmi, lokasyon). Her "dahil fakat bunlarla sınırlı olmamak üzere", "vb." ve "gerektiği şekilde" ifadesini kapalı bir listeyle değiştir.
3. Açık kapsam dışı maddeleri yaz; özellikle müşterinin makul olarak dahil sanabileceklerini (veri temizliği, üçüncü taraf lisansları, donanım, hypercare sonrası canlı destek, içerik taşıma).
4. Teslimatları no, açıklama, format ve bağımsız bir gözden geçirenin doğrulayabileceği kabul kriterleriyle listele. Her teslimat bir kapsam kalemine bağlanır.
5. Kabul prosedürünü tanımla: kim inceler, inceleme süresi, hataların nasıl sınıflandığı, neyin kabulü engellediği, yeniden teslim ve müşteri yanıt vermezse zımni kabul.
6. Kilometre taşlarını belirle; sabit fiyatsa ödeme kilometre taşlarını kabul edilmiş teslimatlara bağla. Tarih verilmediyse tarihler görelidir (ör. "başlangıç + 6 hafta").
7. İki tarafın sorumluluklarını RACI benzeri bir tabloda yaz; müşteri sorumlulukları erişim, ortamlar, konu uzmanları, kararlar ve yanıt sürelerini içerir. Her birini gecikmenin sonucuna bağla.
8. Varsayım ve bağımlılıkları tahminden aynen aktar; her varsayım, yanlış çıkarsa ne olacağını (değişiklik talebi) belirtir.
9. Değişiklik kontrolünü tanımla: değişikliklerin nasıl talep edildiği, etki analizinin, onayın ve fiyatlamanın nasıl yapıldığı ve kimin onaylayabileceği.
10. Yönetişim ve raporlamayı (toplantı sıklığı, durum raporları, eskalasyon yolu), varsa kilit personeli ve garanti, gizlilik ve veri koruma hükümlerine atıfları ekle (kişisel veri varsa KVKK/GDPR veri işleme).
11. Belirsizlik taraması yap: zayıf kelimeleri ("destek", "yardım", "azami gayret", "kullanıcı dostu", "optimize"), tanımsız terimleri ve sahibi veya ölçüsü olmayan yükümlülükleri işaretle; kilit terimler için sözlük ekle. Çıkarım olan içeriği `[VARSAYIM]` olarak etiketle.
12. Hedef devam ediyorsa değişiklik süreci için `change-control`, onay için `acceptance-certificate` veya teslimatı başlatmak için `project-charter` öner.

## Çıktı formatı
```markdown
# İş Tanımı (SOW): <proje / faz>
| Alan | Değer |
|---|---|
| Taraflar | ... |
| Çerçeve sözleşme ref. | <ref veya [BİLİNMİYOR]> |
| Ticari model | ... |
| Süre | <başlangıç / bitiş veya göreli> |

## 1. Arka Plan ve Hedefler
## 2. Kapsam
### 2.1 Kapsam içi (sınırlarıyla)
### 2.2 Kapsam dışı
## 3. Teslimatlar
| No | Teslimat | Format | Kabul kriterleri | Kapsam ref. |
## 4. Kabul Prosedürü
## 5. Kilometre Taşları ve Ödeme
| Kilometre taşı | Teslimatlar | Hedef | Ödeme tetikleyicisi |
## 6. Sorumluluklar
| Faaliyet | Tedarikçi | Müşteri | Gecikmenin sonucu |
## 7. Varsayımlar ve Bağımlılıklar
| No | Varsayım | Yanlış çıkarsa |
## 8. Değişiklik Kontrolü
## 9. Yönetişim ve Raporlama
## 10. Diğer Hükümler (çerçeve sözleşmeye atıf) [HUKUKİ İNCELEME]
## 11. Sözlük
## Açık Noktalar
```

## Kalite kontrol listesi
- [ ] Her teslimatın doğrulanabilir kabul kriterleri var ve bir kapsam kalemine bağlı.
- [ ] Kapsamın ölçülebilir sınırları var; "vb.", "bunlarla sınırlı olmamak üzere" veya "gerektiği şekilde" yok.
- [ ] Kapsam dışı, müşterinin dahil sanma olasılığı en yüksek maddeleri listeliyor.
- [ ] Müşteri sorumluluklarının yanıt süreleri ve gecikme sonuçları var.
- [ ] Varsayımlar tahminle uyumlu ve yanlış çıkarsa ne olacağını belirtiyor.
- [ ] Hukuki madde yazılmadı; çerçeve sözleşmeye atıf yapılıp incelemeye işaretlendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Teslimatları faaliyet olarak tanımlamak ("UAT'ye destek vermek"). Bir çıktı ve nasıl kabul edileceğini tanımla ya da eforu sınırla.
- Zımni kabul maddesi koymamak. Bu olmadan kilometre taşları ve ödemeler süresiz takılabilir.
- Varsayımları yalnızca teklifte bırakmak. SOW'a yazılmadıkça kimseyi korumazlar.

## Örnek
Girdi: "1. faz: SSO, sipariş takibi, ERP sipariş senkronizasyonu. Sabit fiyat, 4 ay."

Zayıf: "Tedarikçi portalı ERP ile entegre edecek ve gerektiği şekilde teste destek verecektir."

Güçlü:
| No | Teslimat | Kabul kriterleri |
|---|---|---|
| T3 | ERP sipariş senkronizasyonu (sipariş, sipariş kalemi, sevkiyat durumu) | Üzerinde uzlaşılan UAT setindeki tüm test senaryoları müşteri test ortamında geçer; açık Önem 1-2 hata yoktur |
- Varsayım V4: Müşteri, dokümante API'leri olan bir test ERP ortamını başlangıç + 4 haftaya kadar sağlar. Yanlış çıkarsa: takvim ve efor için değişiklik talebi.
