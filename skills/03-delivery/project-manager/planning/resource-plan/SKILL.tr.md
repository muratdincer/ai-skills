---
name: resource-plan
description: "Zaman içinde gereken rolleri ve yetkinlikleri, dönem bazında kişi veya rol atamalarını, aşırı yüklemeleri, kapasite açıklarını ve bunları kapatma seçeneklerini (işe alım, dış kaynak, yeniden önceliklendirme, yeniden planlama) gösteren proje kaynak planını oluşturur. Takvim hazır olduğunda ekip kurulacaksa, kişiler projeler arasında paylaşılıyorsa ya da bir yetkinlik açığı planı tehdit ediyorsa kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: project-manager
  area: planning
  title: "Kaynak planı"
  related: "schedule-plan, wbs, budget-plan, raci-matrix, onboarding-plan-30-60-90"
  prompt: "Ödeme geçidi projemizin önümüzdeki 6 ayı için kaynak planı oluştur; takvim ve müsaitlikleriyle ekip listesi ekte."
---

# Kaynak Planı

## Amaç
Projenin doğru yetkinliklere doğru zamanda ve doğru miktarda sahip olup olmadığını göstermek; açıkları ve aşırı yüklemeleri harekete geçmeye yetecek kadar erken görünür kılmak.

## Ne zaman kullanılır
- Takvim taslağından sonra projeye kadro atamak ve fizibiliteyi doğrulamak için.
- Ekip üyeleri projeler arasında paylaşılıyor veya sınırlı müsaitse.
- Yeni bir faz farklı yetkinlikler gerektiriyorsa (ör. veri taşıma, test, hypercare).

## Ne zaman kullanılmaz
- Teslimatlardan kimin sorumlu veya hesap verebilir olduğuna karar vermek için `raci-matrix` kullanılır.
- Uzun vadeli organizasyon kapasitesi veya ekip tasarımı için `team-topology` kullanılır.
- Ekip içi iterasyon kapasite planlaması için `iteration-planning` kullanılır.

## Girdiler
Zorunlu:
- İş paketleri ve zaman dönemleriyle takvim veya faz planı.
- İş paketi başına gereken roller/yetkinlikler ya da bunları çıkarmaya yetecek kapsam.

İsteğe bağlı, kaliteyi artırır:
- Müsaitlikleriyle (% veya saat) isimli ekip üyeleri, izinler, diğer taahhütler.
- Ücret kartları (bütçe bağlantısı için), işe alım veya sözleşme temin süreleri.

Ne takvim ne de gereken roller verilmişse iste. Bir kişinin müsaitliğini asla varsayma; `[BİLİNMİYOR]` işaretle.

## Süreç
1. Talebi çıkar: her dönem (hafta veya ay) için takvim ve tahminlerden rol/yetkinlik başına gereken FTE.
2. Arzı kaydet: rol başına isimli kişiler veya açık pozisyonlar ve gerçekçi müsaitlikleri (toplantılar, destek görevleri, izinler düşülür; tipik verimli pay %70-85, kullandığın değeri belirt).
3. Dönem bazında atama matrisini kur ve talep eksi arzı hesapla.
4. Aşırı yüklemeleri (>%100), açıkları (arzı olmayan talep) ve tek hata noktalarını (tek kişide olan kritik yetkinlikler) işaretle.
5. Her açık için temin süresi ve maliyet/etkiyle seçenek öner: iç transfer, işe alım, sözleşmeli çalışan, tedarikçi, kapsam azaltma, yeniden planlama, eğitim.
6. Kritik yolla uyumu kontrol et: kritik faaliyetlerdeki açıklar önceliklidir.
7. Yeni üyeler için oryantasyon süresini, ayrılanlar için bilgi aktarımını planla.
8. Varsayımları ve gözden geçirme sıklığını kaydet.
9. Çıkarım yaptığın her öğeyi `[VARSAYIM]` olarak etiketle ve varsayımlara ya da açık sorulara taşı. Kullanıcının hedefi devam ediyorsa sonraki beceriyi öner: atamayı maliyetlendirmek için `budget-plan` ya da sorumlulukları netleştirmek için `raci-matrix`.

## Çıktı formatı
```markdown
# Kaynak Planı: <proje>
Dönem birimi <hafta/ay> | Verimli pay varsayımı <%x>
## Talep ve Arz (FTE)
| Rol / yetkinlik | D1 talep | D1 arz | D2 talep | D2 arz | ... |
## Kişi Bazında Atama
| Kişi / pozisyon | Rol | D1 % | D2 % | ... | Diğer taahhütler |
## Açıklar ve Aşırı Yüklemeler
| Dönem | Rol | Açık (FTE) | Kritik yolda mı? | Seçenek | Temin süresi | Karar sahibi |
## Tek Hata Noktaları
## Oryantasyon ve Bilgi Aktarımı
## Varsayımlar ve Açık Sorular
```

## Kalite kontrol listesi
- [ ] Talep mevcut ekip büyüklüğünden değil takvimden türetildi.
- [ ] Müsaitlik gerçekçi ve verimli pay varsayımı belirtildi.
- [ ] %100'ü aşan hiçbir kişi işaretsiz bırakılmadı.
- [ ] Her açığın en az bir seçeneği ve karar sahibi var.
- [ ] Kişisel veri planlamanın gerektirdiğiyle sınırlı (izin nedenleri veya sağlık verisi yok).
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Paylaşılan uzmanları tam zamanlı saymak. Gerçek atamalarını bağlı oldukları yöneticiyle teyit et.
- Yeni katılanlar ve sözleşmeliler için ısınma süresini yok saymak.
- Yalnızca kişi sayısını planlayıp belirli yetkinlikleri kaçırmak (ör. üç veri taşıma için tek DBA).

## Örnek
Girdi: "3-4. aylarda 2 test mühendisi gerekiyor; bir test mühendisi %50 başka projede."

Çıktıdan bir bölüm:
| A3 | Test mühendisi | 1,5 FTE | Evet (sistem testi) | Sözleşmeli test uzmanı, 4 hafta temin süresi | Teslimat yöneticisi |
- Tek hata noktası: ödeme şeması sertifikasyon bilgisi tek bir geliştiricide.
