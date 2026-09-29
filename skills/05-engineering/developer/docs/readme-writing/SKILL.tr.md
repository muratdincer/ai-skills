---
description: Projenin ne olduğunu, kimin için olduğunu, nasıl çalıştırılacağını, nasıl kullanılıp yapılandırılacağını ve nasıl katkı verileceğini kopyalanıp doğrulanabilir komutlarla anlatan bir repository README'si yazar veya yeniden düzenler. Repository'de README yoksa, mevcut olan eskimiş veya dağınıksa, yeni katılanlar projeyi çalıştırmakta zorlanıyorsa ya da bir kütüphane veya servis diğer ekiplerle paylaşılmak üzereyse kullanılır.
related: code-documentation, api-reference-docs, technical-onboarding, how-to-guide, changelog-entry
prompt: Dahili invoice-service repository'miz için README yaz. PostgreSQL veritabanı ve bir arka plan worker'ı olan bir REST API; klasör yapısı ve Makefile ekte.
---

# README Yazma

## Amaç
Repository'ye gelen herkesin bir dakika içinde "bu nedir, beni ilgilendirir mi, nasıl çalıştırırım" sorularına yanıt bulmasını ve katkı verecek kişinin clone'dan geçen bir test koşumuna kadar doğrulanmış bir yol izlemesini sağlamak. İyi bir README oryantasyon süresini ve ekip kanallarındaki tekrar eden soruları azaltır.

## Ne zaman kullanılır
- Repository'de README yoksa veya README kodun artık sahip olmadığı bir durumu anlatıyorsa.
- Yeni ekip üyeleri veya başka ekipler projeyi nasıl kurup çalıştıracaklarını tekrar tekrar soruyorsa.
- Bir kütüphane, SDK, CLI veya servis kurum içinde ya da açık kaynak olarak yayımlanmak üzereyse.

## Ne zaman kullanılmaz
- Tek tek fonksiyonları, sınıfları veya tasarım gerekçelerini kod içinde belgelemek için `code-documentation` kullanılır.
- Bir API'nin tüm uç noktalarını, parametrelerini ve hatalarını belgelemek için `api-reference-docs` kullanılır.
- Kişiler, erişimler ve ilk görevlerle tam bir oryantasyon programı için `technical-onboarding` kullanılır.

## Girdiler
Zorunlu:
- Projenin ne olduğu ve ne yaptığı (kullanıcıdan bir cümle, mevcut README veya kod yapısı).
- Nasıl derlendiği ve çalıştırıldığı: build dosyaları, script'ler, Makefile, container dosyaları veya ekibin kullandığı komutlar.

İsteğe bağlı, kaliteyi artırır:
- Hedef kitle (kütüphanenin son kullanıcıları, servisi işletenler, dahili katkı verenler).
- Yapılandırma dosyaları ve ortam değişkenleri, gerekli dış servisler.
- Katkı kuralları, lisans, sahipler ve destek kanalları, CI rozetleri.

Build ve çalıştırma bilgisi eksikse tek bir kısa soru grubuyla iste; komut uydurma. Girdiden doğrulayamadığın her komutu `[DOĞRULANMADI]` olarak işaretle.

## Süreç
1. Hedef kitleyi ve proje türünü belirle (kütüphane, servis, CLI, uygulama, monorepo); bölüm sırasını bu belirler. Kütüphanelerde kurulum ve kullanım öne çıkar; servislerde yerel çalıştırma ve yapılandırma.
2. Girişi yaz: proje adı, ne yaptığını ve kimin için olduğunu anlatan tek cümle ve biliniyorsa durum (aktif, bakım, kullanımdan kalkıyor).
3. Ön koşulları build dosyalarında yazan runtime ve araç gereksinimleriyle tam olarak listele; sürüm tahmin etme, `[TBD: sürüm]` yaz.
4. Hızlı başlangıcı yaz: clone'dan çalışan bir sonuca (ayağa kalkan servis, geçen testler veya ilk başarılı çağrı) giden en kısa komut dizisi; her adımın beklenen sonucuyla.
5. Yapılandırmayı tablo olarak belgele: değişken veya anahtar, amaç, varsayılan, zorunlu/isteğe bağlı, örnek değer. Asla gerçek gizli bilgi yazma; yer tutucu göster ve gizli bilginin nereden geldiğini belirt.
6. Kullanımı ekle: her seçeneği değil ana kullanım durumunu kapsayan iki üç gerçekçi örnek (kod parçası, CLI çağrısı veya HTTP isteği).
7. Proje yapısını kısaca anlat (üst düzey klasörler ve sorumlulukları) ve katkı verenin bilmesi gereken temel mimari olguları yaz; derin dokümanları tekrarlamak yerine bağlantı ver.
8. Geliştirme akışını ekle: testlerin, linter ve formatter'ların nasıl çalıştırılacağı, tek bir testin nasıl koşulacağı ve biliniyorsa branch ve pull request kuralları.
9. İşletim ve destek bilgisini ekle: dağıtım veya sürüm çıkarma (ya da bağlantısı), log ve panoların yeri, sahipler ve destek kanalı, lisans.
10. Ayıkla: pazarlama dilini, tekrar eden içeriği ve çabuk eskiyecek her şeyi (sabit sayılar, tarihli ifadeler) çıkar; bunun yerine asıl kaynağa bağlantı ver.
11. Doğrulanmamış her komutu veya çıkarımı `[DOĞRULANMADI]` ya da `[VARSAYIM]` olarak işaretle ve sahipler için açık soruları listele.
12. Kullanıcının ihtiyacı devam ediyorsa uç nokta ayrıntıları için `api-reference-docs`, tam oryantasyon planı için `technical-onboarding` veya değişiklik günlüğü başlatmak için `changelog-entry` öner.

## Çıktı formatı
```markdown
# <Proje adı>
<Tek cümle: ne yapar ve kimin için.> Durum: <aktif | bakım | kullanımdan kalkıyor | [BİLİNMİYOR]>

## Hızlı Başlangıç
1. <komut>  # beklenen: <sonuç>

## Ön Koşullar
- <runtime/araç ve sürüm veya [TBD: sürüm]>

## Yapılandırma
| Anahtar / değişken | Amaç | Varsayılan | Zorunlu | Örnek |
|---|---|---|---|---|

## Kullanım
<2-3 gerçekçi örnek>

## Proje Yapısı
- `<klasör>/` — <sorumluluk>

## Geliştirme
- Testler: `<komut>` · Tek test: `<komut>` · Lint/format: `<komut>`

## Dağıtım ve İşletim
<bağlantı veya kısa adımlar; loglar, panolar>

## Katkı, Sahipler ve Destek
<kurallar, sahip ekip, kanal, lisans>

<!-- Açık sorular: ... -->
```

## Kalite kontrol listesi
- [ ] İlk iki satır, projeyi hiç bilmeyen birine ne olduğunu ve kendisini ilgilendirip ilgilendirmediğini söylüyor.
- [ ] Hızlı başlangıç clone'dan doğrulanabilir bir sonuca gidiyor ve her adım beklenen sonucunu belirtiyor.
- [ ] Hiçbir komut, sürüm veya varsayılan uydurulmadı; doğrulanmayanlar `[DOĞRULANMADI]` veya `[TBD]` olarak işaretli.
- [ ] Gizli bilgi, dahili kimlik bilgisi veya kişisel veri yok; yer tutucular yalnızca formatı gösteriyor.
- [ ] Derin içerik tekrarlanmak yerine bağlantıyla veriliyor ve zamana bağlı hiçbir bilgi sabit yazılmamış.
- [ ] Bölüm sırası hedef kitleye uygun (kütüphane kullanıcısı, katkı veren veya işleten).
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Sessizce yerel bir kuruluma (önceden kurulu veritabanı, önbellekteki kimlik bilgileri) dayanan bir hızlı başlangıç. Temiz bir makinede zihinsel olarak dene ve her bağımlılığı listele.
- README'yi tasarım dokümanı gibi yazmak. Mimariyi katkı verenin ihtiyacı kadar tut, tasarım dokümanına veya ADR'lere bağlantı ver.
- Gerçek değerler içeren `.env` dosyalarını örneklere kopyalamak. `<api-anahtariniz>` gibi açık yer tutucular kullan.

## Örnek
Girdi: "invoice-service: REST API + worker, PostgreSQL, Makefile'da `make up`, `make test` var."

Zayıf bölüm: "## Kurulum — Her şeyi kur ve projeyi çalıştır."

Güçlü bölüm:
- Hızlı başlangıç: 1) `make up` — beklenen: `http://localhost:8080/health` adresindeki API `200` döner; worker `listening on queue invoices` loglar `[DOĞRULANMADI: kuyruk adı]`. 2) `make test` — beklenen: tüm testler geçer.
- Yapılandırma: `DATABASE_URL` | bağlantı cümlesi | yok | zorunlu | `postgres://user:<parola>@localhost:5432/invoices`.
- Açık soru: Build hangi runtime sürümünü gerektiriyor? `[TBD: sürüm]`
