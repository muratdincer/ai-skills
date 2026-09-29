---
name: error-scenario-catalog
description: "Bir özellik, akış veya arayüz için hata senaryoları kataloğu oluşturur: her hata durumu için tetikleyici, tespit noktası, beklenen sistem davranışı, sonrasındaki veri durumu, kullanıcıya veya çağırana dönen mesaj, hata kodu, loglama ve alarm ile kurtarma yolu. Gereksinimler yalnızca mutlu yolu anlattığında, bir entegrasyon veya işlem akışı tasarlanıp test edilmeden önce ya da destek ekibi ile geliştiriciler bir şey başarısız olduğunda sistemin ne yapması gerektiği konusunda anlaşamadığında kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: system-analyst
  area: specification
  title: "Hata senaryoları kataloğu"
  related: "error-message-writing, edge-case-elicitation, sequence-flow, resilience-review, test-case-writing"
  prompt: "Para transferi akışımız için hata senaryoları kataloğu oluştur: doğrulama, limitler, core banking zaman aşımı ve tekrarlanan gönderimler."
---

# Hata Senaryoları Kataloğu

## Amaç
Bir şeyler ters gittiğinde sistemin ekranlarda, API'lerde ve toplu işlerde tutarlı biçimde nasıl davranacağını tanımlamak. Böylece geliştiriciler üzerinde anlaşılmış tek bir davranışı uygular, test uzmanları doğrular, destek ekibi kullanıcıların ne gördüğünü bilir. Katalog, dağınık "hataları yönet" ifadelerini karar verilebilir gereksinimlere dönüştürür.

## Ne zaman kullanılır
- Bir özellik veya entegrasyon akışı tanımlanmış ama hata davranışı eksik ya da tutarsızsa.
- İşlemsel bir akışın (ödeme, sipariş, rezervasyon) kısmi hata altında tutarlı kalması gerekiyorsa.
- Destek kayıtları veya olaylar kullanıcıların belirsiz hatalar aldığını ya da verinin yarım işlendiğini gösteriyorsa.

## Ne zaman kullanılmaz
- Genel olarak alışılmadık girdileri ve sınır durumlarını keşfetmek gerekiyorsa `edge-case-elicitation` kullanılır.
- Yalnızca bilinen hatalar için kullanıcıya dönük metin gerekiyorsa `error-message-writing` kullanılır.
- Yazılmış koddaki hata yönetimi inceleniyorsa `error-handling-review` kullanılır.

## Girdiler
Zorunlu:
- Özellik, akış veya arayüz tarifi (gereksinimler, akış, kullanım senaryosu veya API).

İsteğe bağlı, kaliteyi artırır:
- Akış veya entegrasyon ayrıntıları, durum modeli, iş kuralları ve limitler.
- Mevcut hata kodu şeması, mesaj yazım kılavuzu, destek ve izleme düzeni.
- Olay geçmişi veya bilinen sorunlu alanlar.

Akış tarifi yoksa iste. Fazlasını sorma; bilinmeyen davranış sorumlusuyla birlikte `[TBD]` olur.

## Süreç
1. Akışı adımlara böl ve her adım için neye bağımlı olduğunu not et: kullanıcı girdisi, iş kuralları, iç servisler, dış sistemler, veri depoları, zaman.
2. Her adım için kategorilere göre hata durumları üret: girdi doğrulama, iş kuralı reddi, yetki, bulunamayan veya bayat veri, çakışma ve eşzamanlılık, tekrarlanan istek, bağımlılığın erişilemez veya yavaş olması, veri kalıcılaştıktan sonra kısmi hata, kapasite veya istek sınırı, eksik yapılandırma ya da referans veri.
3. Her durum için tespit noktasını (istemci, API geçidi, servis, toplu iş) ve beklenen (iş) mi yoksa beklenmeyen (teknik) mi olduğunu belirle.
4. Beklenen davranışı tanımla: reddet, otomatik yeniden dene, sonraya kuyrukla, telafi et, kontrollü şekilde işlevi azalt veya manuel işleme devret. Hiçbir şey yarım kalmasın diye sonrasındaki veri durumunu yaz.
5. Kullanıcıya veya çağırana dönecek yanıtı tanımla: üzerinde anlaşılmış şemadan hata kodu (veya `[TBD]`), HTTP durumu veya eşdeğeri, mesajın amacı (ne oldu, şimdi ne yapmalı); iç ayrıntı veya kişisel veri sızdırmadan.
6. İşletilebilirliği tanımla: log seviyesi ve korelasyon ID'si, alarm tetiklenip tetiklenmeyeceği ve kime gideceği, metrik veya pano etkisi. Loglarda kişisel veri maskelenmelidir.
7. Kurtarmayı tanımla: kullanıcı, destek ekibi veya otomatik bir iş işlemi nasıl tamamlar ya da geri alır ve hangi runbook veya destek prosedürü geçerlidir.
8. Her senaryoyu olasılık ve etkiye göre (Yüksek/Orta/Düşük) tek satırlık gerekçeyle puanla; davranışın iş kararı olduğu senaryoları işaretle ve önerilerini `[VARSAYIM]` olarak etiketle.
9. Birleştir: tekrarları birleştir, benzer durumlarda kodları ve mesajları tutarlı yap, akışın her adımının en az bir senaryosu olduğunu kontrol et.
10. Kullanıcı devam etmek isterse son metinler için `error-message-writing`, her senaryoyu doğrulamak için `test-case-writing` veya bağımlılık hataları için `resilience-review` öner.

## Çıktı formatı
```markdown
# Hata Senaryoları Kataloğu: <özellik / akış>
Kapsam: <kapsanan adımlar> · Kod şeması: <verilen / [TBD]>

## Senaryolar
| ID | Adım | Kategori | Tetikleyici | Tespit noktası | Beklenen davranış | Sonraki veri durumu | Kod / durum | Mesaj amacı | Log / alarm | Kurtarma | O / E |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Adım Bazında Kapsama
| Adım | Senaryolar |
|---|---|

## Gereken İş Kararları
- [VARSAYIM] <önerilen davranış> — sorumlu

## Açık Sorular
1. ...
```

## Kalite kontrol listesi
- [ ] Akışın her adımının bağımlılık hatası dahil en az bir senaryosu var.
- [ ] Her senaryo sonrasındaki veri durumunu belirtiyor; yarım işlenmiş hiçbir sonuç tanımsız bırakılmadı.
- [ ] Mesajlar kullanıcıya ne yapacağını söylüyor ve stack trace, iç isim veya kişisel veri göstermiyor.
- [ ] Yeniden deneme yalnızca idempotent işlemler için veya idempotency anahtarıyla tanımlandı.
- [ ] Her senaryonun tespit noktası, loglama kararı ve kurtarma yolu var.
- [ ] Önerilen iş davranışları `[VARSAYIM]` olarak etiketli ve karar için listelendi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Her şey için tek bir genel "teknik hata, daha sonra tekrar deneyin" mesajı. Kullanıcılar idempotent olmayan işlemleri tekrarlar ve mükerrer kayıt oluşur; kurtarılabilirliğe göre ayrıştır.
- Yalnızca doğrulama hatalarını kapsamak. Pahalı hatalar, zaman aşımları ve veri kalıcılaştıktan sonraki kısmi hatalardır.
- İş sonuçlarını geliştiricilere bırakmak (örn. başarısız bir transferin geri alınıp alınmayacağı). Bunları açık kararlar olarak iş sahibine yönlendir.

## Örnek
Girdi: "Müşteri para transferi yapar: IBAN ve tutar girer, günlük limit kontrol edilir, core banking çağrılır, dekont gösterilir."

Çıktıdan bir bölüm:
| ID | Adım | Kategori | Tetikleyici | Beklenen davranış | Sonraki veri durumu | Kod | Mesaj amacı | Kurtarma |
|---|---|---|---|---|---|---|---|---|
| E03 | Limit kontrolü | İş kuralı | Tutar kalan günlük limiti aşıyor | Core çağrısından önce reddet | Transfer oluşmadı | TRF-LIMIT `[TBD]` | Kalan limiti göster, daha düşük tutar öner | Gerekmez |
| E07 | Core çağrısı | Bağımlılık yavaş | `[TBD]` sn içinde yanıt yok | Yeniden deneme yok; Beklemede işaretle, durumu sorgula | Transfer Beklemede | TRF-PENDING | "Transferiniz işleniyor; tekrar göndermeyin" | Durum işi sonuçlandırır; destek prosedürü `[TBD]` |

Zayıf: "E07: hata göster." Güçlü: Beklemede veri durumunu, yeniden deneme yapılmayacağını ve kullanıcıya tekrar göndermemesi talimatını belirtir.
