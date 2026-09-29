---
name: integration-pattern-selection
description: "Sistemler arasındaki her etkileşim için entegrasyon desenini (senkron API, asenkron mesajlaşma, olay akışı, dosya/batch aktarımı, CDC, paylaşılan veritabanı) bağımlılık, gecikme, tutarlılık, hacim, sıralama ve hata davranışını analiz ederek seçer ve ödünleşimleri kaydeder. İki veya daha fazla sistemin veri ya da komut alışverişi tasarlanırken, noktadan noktaya veya dosya arayüzleri değiştirilirken ya da bir entegrasyon yük veya değişiklik altında sürekli bozulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 04-architecture
  role: solution-architect
  area: design
  title: "Entegrasyon deseni seçimi"
  related: "integration-requirements, event-driven-design, api-contract, adr, resilience-review"
  prompt: "Sipariş sistemi, ERP ve depo sistemi arasındaki entegrasyon desenlerini seç; ERP yalnızca SOAP ve gece dosyalarını destekliyor, depo stok güncellemesini bir dakika içinde istiyor."
---

# Entegrasyon Deseni Seçimi

## Amaç
Her etkileşim için gerçek gecikme, tutarlılık ve bağımlılık ihtiyacını karşılayan entegrasyon stilini seçmek ve ödünleşimleri açık hale getirmek. Böylece seçim hem mimari incelemeden hem de operasyondan sağ çıkar.

## Ne zaman kullanılır
- Yeni bir çözümün mevcut sistemlerle veri veya komut alışverişi yapması gerektiğinde.
- Noktadan noktaya ya da dosya arayüzleri sadeleştirilirken veya mesajlaşma/API'ye taşınırken.
- Bir entegrasyon yük, şema değişikliği veya karşı taraf kesintisi altında bozulduğunda.

## Ne zaman kullanılmaz
- Arayüzler seçilmiş, yalnızca sözleşme yazılacaksa `api-contract` kullanılır.
- Akışın tamamı olay güdümlüyse ve topic, şema, saga tasarımı gerekiyorsa `event-driven-design` kullanılır.
- İş düzeyindeki veri ihtiyaçları henüz net değilse önce `integration-requirements` kullanılır.

## Girdiler
Zorunlu:
- İlgili sistemler ve her etkileşimin amacı (veri mi komut mu, yönü).
- Her etkileşim için gecikme/güncellik beklentisi veya bunun `[BİLİNMİYOR]` olarak işaretlenmesine izin.

İsteğe bağlı:
- Hacimler ve tepe yükler, mesaj boyutları, sıralama ve tam-bir-kez ihtiyaçları.
- Her uç noktanın teknik yetenekleri (protokoller, CDC desteği, üretici limitleri).
- Mevcut ara katman (API gateway, broker, iPaaS, ESB), güvenlik ve uyum kısıtları.

Etkileşim listesi yoksa iste. Diğer her şey açık soru olur.

## Süreç
1. Etkileşimleri satır olarak listele: kaynak, hedef, amaç (sorgu, komut, olay bildirimi, durum aktarımı, toplu senkronizasyon), tetikleyici ve yön.
2. Her etkileşim için kuvvetleri kaydet: güncellik (ms/sn/dk/günlük), hacim ve tepe, tutarlılık ihtiyacı (güçlü, kendi yazdığını okuma, nihai), sıralama, mesaj boyutu ve kaynağın sonucu bilmesi gerekip gerekmediği.
3. Uç nokta yeteneklerini ve limitlerini belirtildiği gibi kaydet; çıkarım yapılanları `[VARSAYIM]` olarak işaretle.
4. Her satır için adayları üret: senkron istek/yanıt (REST/gRPC/SOAP), kuyruk üzerinden asenkron komut, broker/stream üzerinde olay bildirimi veya olayla durum aktarımı, kaynak veritabanından CDC, dosya/batch aktarımı, paylaşılan veritabanı (son çare olarak işaretle).
5. Adayları zamansal bağımlılık, şema bağımlılığı, erişilebilirlik bağımlılığı (senkron zincirlerin bileşik SLA'sı), geri basınç, yeniden oynatma/yeniden işleme, işletilebilirlik ve ekip yetkinliğine göre değerlendir.
6. Her asenkron seçim için teslim garantisini ve idempotency stratejisini belirle (en-az-bir-kez + idempotent tüketici, tekilleştirme anahtarı, üretici tarafında outbox).
7. Hata davranışını tanımla: zaman aşımları, geri çekilmeli yeniden denemeler, dead-letter yönetimi, batch/CDC için mutabakat ve hedef kapalıyken kullanıcının ne gördüğü.
8. Kesişen konuları kontrol et: güvenlik (sistemler arası kimlik doğrulama, aktarımda ve durağan veride veri sınıflandırması), sürümleme ve şema evrimi, gözlemlenebilirlik (uçtan uca korelasyon ID).
9. Sadeleştir: stil çeşitliliğini önle; kurumun varsayılan deseninden her sapmayı gerekçelendir.
10. Öneri tablosunu ve her önemli seçim için bir ADR adayını yaz; açık soruları sahibine göre listele.
11. Hedef devam ediyorsa seçilen API'ler için `api-contract`, olay akışları için `event-driven-design` veya kararı kaydetmek için `adr` öner.

## Çıktı formatı
```markdown
# Entegrasyon Deseni Seçimi: <çözüm>
## Etkileşim Envanteri
| # | Kaynak → Hedef | Amaç | Güncellik | Hacim/tepe | Tutarlılık | Sıralama |
|---|---|---|---|---|---|---|
## Öneri
| # | Desen | Neden | Reddedilen alternatif ve gerekçe | Garanti / idempotency | Hata yönetimi |
|---|---|---|---|---|---|
## Kesişen Kararlar
- Güvenlik: ...
- Şema evrimi / sürümleme: ...
- Gözlemlenebilirlik: ...
## Varsayımlar ve Riskler
- [VARSAYIM] ...
## ADR Adayları
## Açık Sorular
1. <soru> — <sahibi>
```

## Kalite kontrol listesi
- [ ] Her etkileşimin belirtilmiş veya `[BİLİNMİYOR]` güncelliği ve hacmi var; hiçbiri uydurulmadı.
- [ ] Her seçim reddedilen alternatifi ve gerekçesini belirtiyor.
- [ ] Senkron zincirlerin bileşik erişilebilirlik bağımlılığı gösterildi.
- [ ] Her asenkron akışın teslim garantisi, idempotency ve dead-letter stratejisi var.
- [ ] Paylaşılan veritabanı entegrasyonu açıkça gerekçelendirildi veya reddedildi.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Çağıranın anında yanıta ihtiyacı varken "modern olduğu için" mesajlaşma seçmek. Deseni amaca ve güncelliğe göre eşle.
- CDC'yi entegrasyon sözleşmesi saymak. Ham tablo değişiklikleri kaynak şemayı sızdırır; düzenlenmiş olaylar yayınla veya outbox kullan.
- Batch ve nihai tutarlı akışlarda mutabakatı unutmak. Periyodik karşılaştır-ve-onar işi planla.

## Örnek
Girdi: "Sipariş sistemi, ERP (yalnızca SOAP ve gece dosyası), depo stoğu bir dakika içinde istiyor."

Çıktıdan bir bölüm:
| # | Desen | Neden | Reddedilen alternatif |
|---|---|---|---|
| 1 Sipariş → Depo | Broker üzerinde olay bildirimi, en-az-bir-kez, sipariş ID'sine göre idempotent tüketici | < 1 dk güncellik, depo kesintisi ödeme adımını durdurmamalı | Senkron REST: ödeme erişilebilirliğini depoya bağlar |
| 2 Sipariş → ERP | Yönetilen dosya aktarımıyla gece dosyası + mutabakat raporu | ERP yalnızca dosya kabul ediyor; günlük güncellik `[VARSAYIM: finans teyit edecek]` | Sipariş başına SOAP: üretici hız limiti `[BİLİNMİYOR]` |
