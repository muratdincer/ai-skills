---
name: mobile-release-checklist
description: "Bir mobil uygulama sürümü için sürümleme, build ve imzalama, izinler ve gizlilik beyanları, mağaza sayfası ve görselleri, kalite kapıları, backend ve zorunlu güncelleme uyumluluğu, kademeli yayın, izleme ve geri alma konularını kapsayan bir go/no-go kontrol listesi oluşturup yürütür; her maddeyi kanıtıyla tamam, açık veya engelli olarak raporlar. Bir iOS veya Android build'i mağaza gönderimine ya da kademeli yayına hazırlanırken veya ekip tekrarlanabilir bir mobil sürüm kontrol listesi istediğinde kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 05-engineering
  role: developer
  area: mobile
  title: "Mobil sürüm kontrol listesi"
  related: "app-store-release-notes, release-quality-gate, deployment-checklist, rollback-plan, go-no-go"
  prompt: "Android ve iOS uygulamalarımızın 4.2.0 sürümünü gelecek salı gönderiyoruz. Konuma dayalı kampanyalar ekliyor. Mobil sürüm kontrol listesini benimle birlikte yürüt."
---

# Mobil Sürüm Kontrol Listesi

## Amaç
Bir mobil build'in sürprizsiz biçimde gönderilebilmesini, onaylanabilmesini, yayına alınabilmesini ve gerekirse etkisinin sınırlanabilmesini sağlamak. Mobil sürümler sunucu deployment'ı gibi geri alınamaz; bu yüzden kontrol listesi mağazaların, kullanıcıların ve eski uygulama sürümlerinin karşılaşacaklarını en başa alır.

## Ne zaman kullanılır
- Bir iOS veya Android build'i mağaza gönderimine hazırlanırken.
- Kademeli yayın planlandığında ve ilerleme ya da durdurma kriterleri gerektiğinde.
- Ekip kendi uygulamasına uyarlanmış yeniden kullanılabilir bir kontrol listesi istediğinde.

## Ne zaman kullanılmaz
- "Yenilikler" metnini yazmak için `app-store-release-notes` kullanılır.
- Sunucu tarafı deployment adımları için `deployment-checklist` kullanılır.
- Ekipler arası resmî sürüm karar toplantısı için `go-no-go` kullanılır.

## Girdiler
Zorunlu:
- Uygulama adı, hedef platformlar, yayınlanan sürüm ve değişiklik listesi (veya sürüm kapsamı).

İsteğe bağlı, kaliteyi artırır:
- Planlanan gönderim ve yayın tarihleri, yayın stratejisi, ilgili feature flag'ler.
- Bu sürümde eklenen yeni izinler, SDK'lar veya veri toplama.
- Desteklenen en düşük işletim sistemi ve uygulama sürümleri, birlikte çıkan backend değişiklikleri.
- Ekibin mevcut kontrol listesi veya önceki sürümlerde yaşanan sorunlar.

Değişiklik listesi yoksa iste; izinler, gizlilik beyanları ve uyumluluk buna bağlıdır. Kullanıcının teyit edemediği maddeler "Tamam" değil, "Açık" kalır.

## Süreç
1. Kapsamı ve platformları teyit et; mağaza incelemesinde risk taşıyan değişiklikleri işaretle (yeni izinler, arka planda konum, ödemeler, silme imkânı olmadan hesap oluşturma, kullanıcı içeriği, sağlık veya finans verisi).
2. Sürümleme: kullanıcıya görünen sürüm ekibin şemasına (örneğin SemVer) uyuyor ve build numaraları her platformda artarak ilerliyor; release branch'i veya etiketi oluşturuldu; ekip gerektiriyorsa sürüm platformlar arasında tutarlı.
3. Build ve imzalama: release yapılandırması (debug bayrakları yok, log seviyesi uygun, test uç noktaları kaldırılmış), doğru imzalama kimliği ve süresi dolmak üzere olmayan sertifikalar, CI'dan tekrarlanabilir build, çökme sembolikleştirmesi için sembol ve mapping dosyalarının yüklenmesi.
4. İzinler ve gizlilik: her yeni iznin gerçek kullanımla örtüşen bir amaç metni var ve bağlam içinde isteniyor; mağaza gizlilik beyanları (toplanan veri, amaç, kullanıcıyla ilişkilendirme, takip) yeni SDK'lar için güncellendi; kişisel veri en aza indirildi ve mağaza politikası veya mevzuat (KVKK/GDPR) gerektiriyorsa hesap silme mevcut.
5. Mağaza sayfası: sürüm notları, değişen ekranların görüntüleri, yaş derecelendirmesi yanıtları, uygulama içi satın alma ve abonelik bilgileri, yerelleştirilmiş metinler, inceleme ekibi için notlar ve demo hesap (kimlik bilgileri mağazanın inceleyici kanalıyla paylaşılır, asla kontrol listesine yazılmaz).
6. Kalite kapıları: desteklenen en düşük ve en güncel işletim sistemi sürümlerinde ve temsili cihazlarda regresyon ve smoke testleri, erişilebilirlik kontrolü, beta/iç kanalın çökme olmayan oranı, bütçeye göre performans (açılış süresi, uygulama boyutu artışı).
7. Uyumluluk: backend değişiklikleri hâlâ kullanımda olan sürümlerle geriye dönük uyumlu; eski sürümler bozulacaksa zorunlu veya yumuşak güncelleme kuralları ayarlandı; cihazdaki veri veya şema geçişleri desteklenen en eski yükseltme yolundan test edildi.
8. Feature flag ve uzaktan yapılandırma: yeni özellikler güvenli varsayılanla geliyor, flag'ler yeni build olmadan kapatılabiliyor, riskli özellikler için bir kapatma anahtarı (kill switch) var.
9. Yayın planı: kademeli yüzdeler ve bekleme süreleri, her adımı geçiren metrikler (çökmesiz kullanıcı oranı, ANR veya donma oranı, ana huni dönüşümü, destek talepleri), yayını kimin durdurabileceği ve mağaza incelemesi ile hafta sonu boşluklarından kaçınan zamanlama.
10. Sınırlama ve geri dönüş: kurulu build'ler geri çekilemediği için durdurma prosedürünü, flag kapatma seçeneklerini, gerekirse hızlandırılmış incelemeyle hotfix yolunu ve kullanıcı iletişimini tanımla.
11. Her maddeyi Tamam (kanıtıyla), Açık (sorumlu, tarih) veya Engelli olarak raporla ve bir go/no-go önerisi ver. Mağaza metni için `app-store-release-notes`, ayrıntılı sınırlama planı için `rollback-plan`, resmî karar için `go-no-go` öner.

## Çıktı formatı
```markdown
# Mobil Sürüm Kontrol Listesi: <uygulama> v<sürüm> (<platformlar>)
Gönderim: <tarih> · Yayın başlangıcı: <tarih> · Sürüm sahibi: <ad veya [BİLİNMİYOR]>

## Mağaza İncelemesi Riskleri
- ...

| Alan | Madde | Platform | Durum (Tamam/Açık/Engelli) | Kanıt / Sorumlu / Tarih |
|---|---|---|---|---|
| Sürümleme | ... | | | |
| Build ve imzalama | ... | | | |
| İzinler ve gizlilik | ... | | | |
| Mağaza sayfası | ... | | | |
| Kalite kapıları | ... | | | |
| Uyumluluk | ... | | | |
| Flag ve yapılandırma | ... | | | |

## Yayın Planı
| Adım | Kitle % | Bekleme | İlerleme koşulu | Durdurma koşulu |
|---|---|---|---|---|

## Sınırlama
- Durdurma: ... · Flag kapatma: ... · Hotfix yolu: ... · Kullanıcı iletişimi: ...

## Öneri
<Go / Koşullu go / No-go> — <gerekçeler, açık engeller>
```

## Kalite kontrol listesi
- [ ] Her yeni izin, SDK veya veri türü bir amaç metnine ve güncellenmiş bir gizlilik beyanına bağlandı.
- [ ] Eski kurulu sürümlerle geriye dönük uyumluluk ve yükseltme yolu açıkça ele alındı.
- [ ] Yayın adımlarının ölçülebilir ilerleme ve durdurma kriterleri ve adı belli bir karar sahibi var.
- [ ] Hiçbir madde kanıtsız Tamam işaretlenmedi; teyit edilmeyenler Açık kaldı.
- [ ] Çıktıda kimlik bilgisi, imzalama anahtarı veya inceleyici şifresi yok.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sürümü anında geri alınabilen bir sunucu deployment'ı gibi ele almak. Eski build'ler cihazlarda kalır; flag'leri, zorunlu güncelleme kurallarını ve hotfix yolunu yayından önce planla.
- Veri toplayan bir SDK ekleyip gizlilik beyanlarını güncellememek; bu ret veya politika ihlaline yol açar.
- Cuma günü bir anda %100'e açmak; çökme artışı hafta sonu boyunca kimse durduramadan sürer.

## Örnek
Girdi: "v4.2.0, Android ve iOS, konuma dayalı kampanyalar ekliyor, salı gönderilecek."

Çıktıdan bir bölüm:
- Mağaza incelemesi riski: yeni konum izni. Yalnızca kullanım sırasında konum `[VARSAYIM]`; arka planda konum ayrı gerekçe gerektirir.

| Alan | Madde | Platform | Durum | Kanıt / Sorumlu / Tarih |
|---|---|---|---|---|
| İzinler ve gizlilik | Konum amaç metni kullanıcının yakınındaki kampanyaları açıklıyor | iOS, Android | Açık | Mobil lider, Pzt |
| İzinler ve gizlilik | Gizlilik beyanına "hassas konum, uygulama işlevi için" eklendi | İki mağaza | Açık | Ürün + hukuk, Pzt |
| Uyumluluk | Kampanya API'si v4.1 istemcilerine hata değil boş liste dönüyor | Backend | Tamam | Sözleşme testi çalıştırma linki |
| Flag ve yapılandırma | `location_offers` uzak flag'i varsayılan kapalı, her yayın adımında açılıyor | İkisi | Tamam | Yapılandırma ekran görüntüsü |
