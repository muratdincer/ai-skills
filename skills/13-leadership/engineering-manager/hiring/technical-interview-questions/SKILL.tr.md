---
description: Tek bir mülakat aşaması için seviyeye göre ayarlanmış teknik sorular, takip soruları ve davranışa dayalı bir puanlama ölçeği hazırlar. Kodlama, sistem tasarımı, hata ayıklama veya alan bilgisi aşaması için soru seti gerektiğinde, soruları bir seviyeye kalibre ederken ya da ezber ve bulmaca sorularını işle ilgili sorularla değiştirirken kullanılır.
related: interview-plan, interview-scorecard, career-ladder, job-description, candidate-debrief
prompt: Kıdemli backend mühendisi için 60 dakikalık sistem tasarımı soru seti ve puanlama ölçeği hazırla. Olay güdümlü sipariş işleme üzerinde çalışıyoruz.
---

# Teknik Mülakat Soruları

## Amaç
Mülakatçılara az sayıda, işle ilgili soru, takip soruları ve bir puanlama ölçeği vermek. Böylece aynı seviyedeki her adaya karşılaştırılabilir sorular sorulur ve adaylar sezgiye göre değil, aynı gözlemlenebilir ölçütlere göre puanlanır.

## Ne zaman kullanılır
- Bir mülakat aşamasının yetkinlikleri belli ama soruları henüz yok.
- Mevcut sorular ezber, bulmaca ya da tek bir mülakatçının sevdiği konuya bağlı.
- Mülakatçılar puanlarda anlaşamıyor ve bir seviye için ortak ölçütlere ihtiyaç var.

## Ne zaman kullanılmaz
- Sürecin tamamı (aşamalar, sorumlular, aşama başına yetkinlikler) tasarlanmadıysa `interview-plan` kullanılır.
- Belirli bir adayın yanıtlarını kaydedip puanlamak için `interview-scorecard` kullanılır.
- Her seviyenin ne anlama geldiğini tanımlamak için `career-ladder` kullanılır.

## Girdiler
Zorunlu:
- Rol, hedef seviye, aşama türü (kodlama, sistem tasarımı, hata ayıklama, mimari, alan bilgisi) ve süre.
- Bu aşamanın ölçmesi gereken yetkinlikler.

İsteğe bağlı, kaliteyi artırır:
- Ekibin gerçek problem alanı ve teknoloji yığını, seviyenin kariyer basamağındaki tanımı.
- Mevcut soru havuzu, dışarı sızmış sorular, adayların erişilebilirlik veya dil ihtiyaçları.

Aşamanın yetkinlikleri yoksa önce onları sor; yetkinlikleri sormak istediğin sorudan türetme.

## Süreç
1. Yetkinlikleri ve seviye çıtasını gözlemlenebilir ifadelerle yeniden yaz (bu seviyede çıtayı karşılayan bir yanıt neyi gösterir).
2. Aşama süresine uygun 1-2 ana problem seç; 60 dakikalık bir aşama genellikle bir derin ve bir kısa problemden fazlasını kaldırmaz.
3. Problemleri, ekibin alanındaki gerçekçi işlerden, kuruma özel ayrıntıları çıkararak kur; ezber, zekâ bulmacası ve API ayrıntısı ezberini ödüllendiren sorulardan kaçın.
4. Her problem için okunacak metni aynen, bilerek açık bırakılan kısıtları ve adayın netleştirmek için sorması beklenenleri yaz.
5. Aynı problemin orta, kıdemli ve staff sinyallerini ayırt edebilmesi için kademeli takip soruları ekle (temel, genişletme, seviye yükseltme).
6. Her yetkinlik için 4 dereceli bir ölçek yaz (kesin hayır, hayır, evet, kesin evet); dereceleri sıfatlarla değil gözlemlenebilir davranışlarla tanımla.
7. İşle ilgili olumlu ve olumsuz sinyalleri listele; aksan, mezun olunan okul, özgüven tarzı veya konuşma hızıyla ilgili sinyalleri dışarıda bırak.
8. Zaman planı (tanışma, problem, takip soruları, adayın soruları) ve ipuçlarının nasıl verileceği ile puana etkisine dair mülakatçı notları ekle.
9. Adaleti kontrol et: Soru rolle ilgisiz bilgiye dayanmıyor, makul düzenlemeye izin veriyor ve mümkünse adayın seçtiği dil/araçla yanıtlanabiliyor.
10. Çıkarım yaptığın alan bilgilerini veya seviye beklentilerini `[VARSAYIM]` olarak işaretle ve işe alım yöneticisi için açık noktaları listele.
11. Kullanıcının hedefi devam ediyorsa bu ölçeğe göre kanıt toplamak için `interview-scorecard` veya aşamayı sürece yerleştirmek için `interview-plan` öner.

## Çıktı formatı
```markdown
# Soru Seti: <rol> – <seviye> – <aşama> (<süre>)
Ölçülen yetkinlikler: <liste>

## Zaman Planı
| Dakika | Bölüm |
|---|---|

## Problem 1: <başlık>
Metin (sesli okunacak): ...
Açık kısıtlar: ...
Beklenen netleştirme soruları: ...
Takip soruları: temel → genişletme → seviye yükseltme
İpucu politikası: <ipucu> – <puana etkisi>

## Puanlama Ölçeği
| Yetkinlik | Kesin hayır | Hayır | Evet | Kesin evet |
|---|---|---|---|---|

## Olumlu / Olumsuz Sinyaller (yalnızca işle ilgili)
- ...

## Varsayımlar ve Açık Noktalar
- [VARSAYIM] ...
```

## Kalite kontrol listesi
- [ ] Her soru atanmış en az bir yetkinliğe bağlı.
- [ ] Ölçek dereceleri hedef seviye için gözlemlenebilir davranışları tanımlıyor.
- [ ] Ezber, bulmaca, okul/geçmiş prestiji veya "kültüre uyum" vekili sinyal yok.
- [ ] Problem süreye sığıyor ve adayın sorularına zaman kalıyor.
- [ ] İpucu politikası ve puana etkisi açık.
- [ ] Çıkarım yapılan alan bilgileri ve seviye beklentileri `[VARSAYIM]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Akıl yürütme, ödünleşim ve iletişim yerine "doğru cevabı buldu mu"yu puanlamak. Ölçeği yalnızca sonuca değil, adayın nasıl çalıştığına dayandır.
- Her seviyeye aynı soruyu aynı derinlikte sormak. Karşılaştırılamaz farklı sorular yerine takip sorularıyla çıtayı yükselt.
- Mülakatçıların zorluğu değiştiren doğaçlama takip soruları sorması. Takip sorularını yazılı hale getir.

## Örnek
Girdi: Kıdemli backend, sistem tasarımı, 60 dk, yetkinlikler: dağıtık tasarım, ödünleşimler, işletilebilirlik.

Çıktıdan bir bölüm:
- Problem: "Ödeme, stok ve kargo servislerinin olay yayınladığı bir pazaryerinde sipariş durum güncellemelerini tasarla."
- Seviye yükseltme sorusu: "Broker failover sırasında bir olay iki kez ve sırasız geliyor. Müşteri ne görür, bunu nasıl önlersin?"
- Ölçek, ödünleşimler, Evet: En az iki seçeneği (outbox ve çift yazma) sayar, her birinin önlediği hatayı söyler ve gerekçeyle birini seçer.
- Zayıf derece (kaçın): "Kafka'yı iyi biliyor." Güçlü derece: "Idempotency anahtarı seçimini ve saklama maliyetini açıklıyor."
