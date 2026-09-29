---
name: incident-response
description: "Canlı bir olayı ilandan çözüme kadar yönetir: önem derecesi değerlendirmesi, rol ataması (olay komutanı, operasyon, iletişim, kayıt tutucu), hipotezler ve paralel iş kollarıyla önce hafifletmeye odaklı plan, zaman damgalı zaman çizelgesi, güncelleme sıklığı ve çıkış kriterleri. Bir kesinti veya performans düşüşü yaşanırken ya da şüphelenilirken, canlı ortam etkisi için şu an ne yapılması gerektiği sorulduğunda veya devam eden bir olay kanalını düzene sokmak için kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 07-devops-sre
  role: sre
  area: incident
  title: "Olay müdahalesi yürütme"
  related: "runbook, incident-communication, postmortem, log-analysis, security-incident-response"
  prompt: "Bir olayımız var: 14:05 deploy'undan on dakika sonra checkout hata oranı %15'e çıktı. Yönetmeme yardım et."
---

# Olay Müdahalesi Yürütme

## Amaç
Canlı bir olayı, kullanıcı etkisi olabildiğince hızlı azalacak, herkes net rollerle ve iş tekrarı olmadan çalışacak, paydaşlar bilgilendirilecek ve postmortem için güvenilir bir zaman çizelgesi oluşacak şekilde koordine etmek.

## Ne zaman kullanılır
- Canlı ortamda etki yaşanıyor veya şüpheleniliyor (alarmlar, müşteri bildirimleri, SLO tüketimi).
- Olay kanalı açık ama dağınık: komutan yok, koordinasyonsuz paralel düzeltmeler, güncelleme yok.
- Baskı altındaki bir müdahale ekibi üyesi yapılandırılmış bir sonraki adım istiyor.

## Ne zaman kullanılmaz
- Olay şüpheli bir güvenlik ihlali veya veri sızıntısıysa `security-incident-response` kullanılır; kanıt yönetimi ve yasal yükümlülükler farklıdır.
- Olay bitti ve amaç öğrenmekse `postmortem` kullanılır.
- Yalnızca bir güncellemenin metni gerekiyorsa `incident-communication` kullanılır.

## Girdiler
Zorunlu:
- Şu an gözlenenler: belirtiler, etkilenen servis, biliniyorsa başlangıç zamanı.

İsteğe bağlı, kaliteyi artırır:
- Son değişiklikler (deploy'lar, konfigürasyon, altyapı, bağımlılıklar), çalan alarmlar, panolar.
- Kurumun önem derecesi tanımları ve nöbet/eskalasyon listesi.
- İlgili runbook'lar.

Girdi toplamak için hafifletmeyi geciktirme. Yalnızca bir sonraki aksiyonu değiştirecek en fazla bir iki soruyu sor; geri kalan her şey bir iş kolu veya açık soru olur.

## Süreç
1. İlan et ve sınıflandır: kullanıcı etkisinden (kapsam, kaybedilen işlev, risk altındaki veri) bir önem derecesi ata; kurumun ölçeğini ya da `[ÖNERİ]` olarak işaretli bir SEV1-4 ölçeği kullan; olgular değiştikçe önem derecesinin değişebileceğini belirt.
2. Rolleri ata: olay komutanı (koordine eder, karar verir, hata ayıklamaz), operasyon lider(ler)i, iletişim lideri, kayıt tutucu; uzun olaylar için bir devir kuralı belirle.
3. Olguları netleştir: başlangıç zamanı, yakın zamanda ne değişti, etki alanı (kullanıcılar, bölgeler, tenant'lar), bilinen ve varsayılan; her varsayımı etiketle.
4. Önce hafifletmeyi seç: yakın tarihli bir değişiklik zamanlama olarak örtüşüyorsa kök neden analizinden önce onu geri al veya flag'ini kapat; diğer seçenekler trafik kaydırma, ölçekleme, failover, yük atma, bağımlılığı devre dışı bırakmadır.
5. Her biri tek sahipli paralel iş kolları yürüt (örn. hafifletme, teşhis, müşteri etkisi); her birinin hipotezi, süre sınırı ve rapor zamanı olsun; her seferinde tek bir değişken değiştir.
6. Gözlemlerin, kararların ve aksiyonların sahipleriyle birlikte zaman damgalı bir zaman çizelgesini UTC veya belirtilmiş bir saat diliminde tut.
7. Güncelleme sıklığını önem derecesine göre belirle (örn. en yüksek derecede 30 dakikada bir veya önemli bir değişiklikte) ve içeriği `incident-communication`'a aktar.
8. Süre sınırı ilerleme olmadan dolduğunda, veri bütünlüğü risk altındayken veya daha fazla yetki gerektiğinde (örn. müşteriye dönük bir karar) eskale et.
9. Hafifletmeyi sinyallerle doğrula (SLI'lar kararlaştırılan bir süre boyunca normal aralıkta), ardından kapatmadan önce izleme süresine karar ver.
10. Kapat: çözümü, kalan riski, takip sahiplerini ve politikaya göre postmortem gerekip gerekmediğini kaydet (genellikle en yüksek önem dereceleri veya bütçeyi aşan olaylar için).
11. Her çıkarımı `[VARSAYIM]` olarak etiketle ve sonraki beceriyi öner: çözümden sonra `postmortem`, bir prosedür eksikse `runbook`, son güncelleme için `incident-communication`.

## Çıktı formatı
```markdown
# Olay: <kısa başlık> · Önem: <SEVn> · Durum: <araştırılıyor / hafifletiliyor / izleniyor / çözüldü>
Başlangıç: <zaman> · İlan: <zaman> · Komutan: <ad> · Operasyon: <ad> · İletişim: <ad> · Kayıt: <ad>

## Mevcut Etki
## Bilinen Olgular ve Varsayımlar
## Hafifletme Planı
| Seçenek | Risk | Karar | Sahip |

## İş Kolları
| İş kolu | Sahip | Hipotez | Süre sınırı | Rapor zamanı |

## Zaman Çizelgesi
| Zaman | Olay / karar / aksiyon | Kim |

## Sonraki Güncelleme Zamanı
## Çıkış Kriterleri ve Takipler
```

## Kalite kontrol listesi
- [ ] Önem derecesi kullanıcı etkisine dayanıyor ve roller atandı; komutan hata ayıklamıyor.
- [ ] Kök neden çalışmasından önce hafifletme seçenekleri değerlendirildi.
- [ ] Her iş kolunun tek sahibi, hipotezi ve süre sınırı var.
- [ ] Zaman çizelgesi zamanları, kararları ve sahipleri kaydediyor; olgular varsayımlardan ayrı.
- [ ] Sonraki güncelleme zamanı ve çıkış kriterleri belirtildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Kullanıcılar hâlâ etkilenirken kök nedeni ayıklamak. Geri alma güvenliyse önce onu yap.
- Herkesin çağrıya katılıp aynı anda düzeltme denemesi. Sahip ata ve etkiler izlenebilir kalsın diye her seferinde tek şey değiştir.
- İlk yeşil grafikte çözüldü demek. Kararlaştırılan izleme süresi boyunca SLI'larla doğrula.

## Örnek
Girdi: "Checkout hataları yaklaşık 14:15'ten beri %15; deploy 14:05'te."

Çıktıdan bir bölüm:
- Önem: SEV2 `[ÖNERİ: kritik bir işlevin kısmi kaybı; kurum ölçeğiyle teyit et]`.
- Olgu: deploy 14:05'te; hatalar ~14:15'ten beri. Varsayım: deploy ilişkili `[VARSAYIM: zaman örtüşmesi, henüz kanıtlanmadı]`.
- Hafifletme kararı: 14:05 deploy'unu geri al (düşük risk, hızlı) – Operasyon lideri; paralelde Teşhis iş kolu yeni kod yolu için hata loglarını inceler, 14:40'ta rapor verir.
- Sonraki güncelleme: 14:45 veya önemli bir değişiklikte.
