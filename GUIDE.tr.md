# Skill Kullanım Rehberi

Her skill için ne zaman kullanılacağı ve hazır bir örnek istek. Örneği (veya kendi versiyonunu) skill'in kurulu olduğu herhangi bir YZ aracına yaz ya da önce skill dosyasını, ardından isteği yapıştır. Araç kurulumu için [USAGE.tr.md](USAGE.tr.md), hangi skill'in hangi aşamaya uyduğu için [METHODOLOGIES.tr.md](METHODOLOGIES.tr.md) dosyasına bak.

## İçindekiler

- [Ortak (Roller Arası)](#ortak-roller-arası)
  - [Toplantılar](#toplantılar)
  - [İletişim](#iletişim)
  - [Dokümantasyon](#dokümantasyon)
  - [Problem Çözme ve Karar Araçları](#problem-çözme-ve-karar-araçları)
  - [Bilgi Yönetimi](#bilgi-yönetimi)
- [İş Analizi](#iş-analizi)
  - [İş Analisti](#iş-analisti)
  - [Sistem Analisti](#sistem-analisti)
- [Ürün Yönetimi](#ürün-yönetimi)
  - [Ürün Yöneticisi](#ürün-yöneticisi)
  - [Ürün Sahibi](#ürün-sahibi)
- [Proje ve Teslimat Yönetimi](#proje-ve-teslimat-yönetimi)
  - [Proje Yöneticisi](#proje-yöneticisi)
  - [Scrum Master / Çevik Koç](#scrum-master--çevik-koç)
  - [Program Yöneticisi / PMO](#program-yöneticisi--pmo)
- [Mimari](#mimari)
  - [Kurumsal Mimar](#kurumsal-mimar)
  - [Çözüm Mimarı](#çözüm-mimarı)
  - [Yazılım Mimarı](#yazılım-mimarı)
- [Yazılım Geliştirme](#yazılım-geliştirme)
  - [Geliştirici (Backend/Frontend/Mobil)](#geliştirici-backendfrontendmobil)
  - [Teknik Lider](#teknik-lider)
- [Kalite Güvence ve Test](#kalite-güvence-ve-test)
  - [Test Analisti / Test Mühendisi](#test-analisti--test-mühendisi)
  - [Test Otomasyon Mühendisi](#test-otomasyon-mühendisi)
  - [Performans Test Mühendisi](#performans-test-mühendisi)
- [DevOps, SRE ve Platform](#devops-sre-ve-platform)
  - [DevOps / Platform Mühendisi](#devops--platform-mühendisi)
  - [Sürüm Yöneticisi](#sürüm-yöneticisi)
  - [Site Güvenilirlik Mühendisi](#site-güvenilirlik-mühendisi)
- [Veri ve Yapay Zeka](#veri-ve-yapay-zeka)
  - [Veri Mimarı](#veri-mimarı)
  - [Veri Mühendisi](#veri-mühendisi)
  - [Veritabanı Yöneticisi](#veritabanı-yöneticisi)
  - [Veri / BI Analisti](#veri--bi-analisti)
  - [Veri Bilimci / ML ve YZ Mühendisi](#veri-bilimci--ml-ve-yz-mühendisi)
- [Güvenlik ve Uyum](#güvenlik-ve-uyum)
  - [Güvenlik Mimarı / Uygulama Güvenliği Mühendisi](#güvenlik-mimarı--uygulama-güvenliği-mühendisi)
  - [Yönetişim, Risk ve Uyum](#yönetişim-risk-ve-uyum)
- [UX / UI Tasarım](#ux--ui-tasarım)
  - [UX Araştırmacısı](#ux-araştırmacısı)
  - [UX / UI Tasarımcı](#ux--ui-tasarımcı)
  - [UX Yazarı / İçerik Tasarımcısı](#ux-yazarı--içerik-tasarımcısı)
- [Destek ve BT Operasyonları](#destek-ve-bt-operasyonları)
  - [Destek Mühendisi (L1-L3)](#destek-mühendisi-l1-l3)
  - [BT Hizmet Yönetimi](#bt-hizmet-yönetimi)
- [Teknik Yazarlık](#teknik-yazarlık)
  - [Teknik Yazar](#teknik-yazar)
- [Mühendislik Yönetimi ve Liderlik](#mühendislik-yönetimi-ve-liderlik)
  - [Mühendislik Yöneticisi](#mühendislik-yöneticisi)
  - [CTO / Başkan Yardımcısı / Direktör](#cto--başkan-yardımcısı--direktör)
- [Ön Satış ve Danışmanlık](#ön-satış-ve-danışmanlık)
  - [Ön Satış / Çözüm Danışmanı](#ön-satış--çözüm-danışmanı)

## Ortak (Roller Arası)

### Toplantılar

#### Toplantı Öncesi

**Toplantı gündemi hazırlama** · `meeting-agenda`

- Ne zaman: Net bir amaç, beklenen çıktılar, sorumlusu ve süresi belirli gündem maddeleri ve gerekli ön okumalarla zaman planlı bir toplantı gündemi hazırlar. Herhangi bir toplantı, çalıştay veya periyodik oturum planlanırken, tartışma yerine karar üreten yapılandırılmış bir gündem gerektiğinde kullanılır.
- Örnek istek: _"Ürün, geliştirme ve test liderleriyle 3. çeyrek sürüm kapsamına karar vereceğimiz 60 dakikalık toplantı için gündem hazırla."_
- İlgili: `meeting-invite`, `meeting-necessity-check`, `facilitation-guide`
- Dosya: [skills/00-shared/meetings/before/meeting-agenda/SKILL.tr.md](skills/00-shared/meetings/before/meeting-agenda/SKILL.tr.md)

**Toplantı daveti yazma** · `meeting-invite`

- Ne zaman: Amacı, beklenen çıktıyı, gündem özetini, her katılımcının neden davet edildiğini ve gereken hazırlığı net biçimde belirten bir toplantı daveti yazar. Takvim daveti veya toplantı talebi e-postası gönderilirken, alıcıların katılıp katılmayacağına karar verebilmesi ve hazırlıklı gelmesi gerektiğinde kullanılır.
- Örnek istek: _"Önümüzdeki salı ödeme servisinin yeniden tasarımı için 45 dakikalık bir mimari inceleme toplantısı daveti yaz."_
- İlgili: `meeting-agenda`, `meeting-necessity-check`
- Dosya: [skills/00-shared/meetings/before/meeting-invite/SKILL.tr.md](skills/00-shared/meetings/before/meeting-invite/SKILL.tr.md)

**Toplantı gerekli mi kararı** · `meeting-necessity-check`

- Ne zaman: Planlanan bir toplantının gerçekten gerekli olup olmadığını, hedefini asenkron alternatiflerle karşılaştırarak değerlendirir; toplan, kısalt, asenkron yürüt veya iptal et önerisini kullanıma hazır bir alternatifle sunar. Yeni veya periyodik bir toplantı planlanırken, \"bunun için toplantı şart mı?\" sorulduğunda ya da toplantı yükü azaltılmak istendiğinde kullanılır.
- Örnek istek: _"Veri taşıma ilerlemesini paylaşmak için 9 kişiyle haftalık 1 saatlik bir senkron toplantı kurmak istiyorum. Gerçekten gerekli mi?"_
- İlgili: `meeting-agenda`, `meeting-invite`, `stakeholder-email`, `status-update`, `working-agreement`
- Dosya: [skills/00-shared/meetings/before/meeting-necessity-check/SKILL.tr.md](skills/00-shared/meetings/before/meeting-necessity-check/SKILL.tr.md)

#### Toplantı Sırasında

**Yapılandırılmış toplantı notu tutma** · `meeting-notes`

- Ne zaman: Ham toplantı notlarını, sohbet kayıtlarını veya bir dökümü; tartışma noktalarını, kararları, aksiyonları ve açık soruları ayıran, gerektiğinde konuşmacıyı belirten konu bazlı yapılandırılmış notlara dönüştürür. Dağınık notlar veya bir döküm paylaşılıp konuşulanların \"toparlanması\", \"yapılandırılması\" ya da \"yazıya dökülmesi\" istendiğinde kullanılır.
- Örnek istek: _"Platform ekibiyle bugünkü sprint planlamasından ham notlarım bunlar. Bunları yapılandırılmış toplantı notlarına çevir."_
- İlgili: `transcript-cleanup`, `meeting-summary`, `action-item-extraction`, `decision-log`, `open-questions-tracker`
- Dosya: [skills/00-shared/meetings/during/meeting-notes/SKILL.tr.md](skills/00-shared/meetings/during/meeting-notes/SKILL.tr.md)

**Toplantı dökümünü temizleme** · `transcript-cleanup`

- Ne zaman: Ham veya otomatik oluşturulmuş bir toplantı dökümünü dolgu sözcüklerini, yarım cümleleri ve üst üste konuşmaları ayıklayarak, konuşmacı etiketlerini ve bariz tanıma hatalarını düzelterek, anlamı ve ifadeleri koruyarak temizler. Bir döküm özete dönüştürülmeden okunabilir, alıntılanabilir veya arşivlenebilir hâle getirilecekse kullanılır.
- Örnek istek: _"Tedarikçi görüşmemizin otomatik dökümünü temizle. Konuşmacı 1 benim (Selin), Konuşmacı 2 tedarikçinin proje yöneticisi."_
- İlgili: `meeting-notes`, `meeting-minutes`, `meeting-summary`, `glossary-builder`
- Dosya: [skills/00-shared/meetings/during/transcript-cleanup/SKILL.tr.md](skills/00-shared/meetings/during/transcript-cleanup/SKILL.tr.md)

**Toplantı kolaylaştırma** · `facilitation-guide`

- Ne zaman: Bir toplantı veya çalıştay için dakika dakika akış planı, açılış ve kapanış metni, gündem maddesi başına yönlendirici sorular, karar kuralı ve baskınlık, sessizlik, konudan sapma ve çatışma için taktikler içeren kolaylaştırıcı metni hazırlar. Birisi bir toplantıyı yönetecek ve özellikle karar, uyum veya ekipler arası oturumları güvenle yürütmek istiyorsa kullanılır.
- Örnek istek: _"Ürün, satış ve mühendislikle 3. çeyrek önceliklerinde anlaşmak için 90 dakikalık bir oturumu kolaylaştıracağım. Bana bir kolaylaştırma rehberi ver."_
- İlgili: `meeting-agenda`, `conflict-resolution`, `retrospective-facilitation`, `workshop-plan`, `decision-matrix`
- Dosya: [skills/00-shared/meetings/during/facilitation-guide/SKILL.tr.md](skills/00-shared/meetings/during/facilitation-guide/SKILL.tr.md)

#### Toplantı Sonrası

**Toplantı özeti çıkarma** · `meeting-summary`

- Ne zaman: Bir toplantının sonuçla başlayan, kararları, önemli aksiyonları ve açık noktaları listeleyen ve okuyucunun dikkat etmesi gerekenleri öne çıkaran, bir dakikadan kısa sürede okunabilen yönetici özetini çıkarır. Bir yönetici, sponsor veya katılamayan paydaş toplantıdan ne çıktığını tüm notları veya dökümü okumadan öğrenmek istediğinde kullanılır.
- Örnek istek: _"Bu 1 saatlik mimari inceleme dökümünü CTO'muz için birkaç satırda özetle."_
- İlgili: `meeting-notes`, `meeting-minutes`, `meeting-follow-up`, `executive-summary`, `action-item-extraction`
- Dosya: [skills/00-shared/meetings/after/meeting-summary/SKILL.tr.md](skills/00-shared/meetings/after/meeting-summary/SKILL.tr.md)

**Resmi toplantı tutanağı yazma** · `meeting-minutes`

- Ne zaman: Toplantı bilgileri, katılım ve yeter sayı, sırasıyla gündem maddeleri, özlü görüşme kayıtları, oylama veya onay sonucuyla numaralandırılmış kararlar, aksiyonlar ve onay imzalarını içeren resmi toplantı tutanağı oluşturur. Yönlendirme komiteleri, yönetim kurulları, değişiklik danışma kurulları, denetimler, sözleşmesel veya tedarikçi toplantıları ya da kaydın kanıt olarak kullanılabileceği her durumda kullanılır.
- Örnek istek: _"Dünkü proje yönlendirme komitesi için bu notlardan resmi tutanak yaz; iki değişiklik talebi onaylandı, biri ertelendi."_
- İlgili: `meeting-notes`, `meeting-summary`, `decision-log`, `steering-committee-pack`, `audit-preparation`
- Dosya: [skills/00-shared/meetings/after/meeting-minutes/SKILL.tr.md](skills/00-shared/meetings/after/meeting-minutes/SKILL.tr.md)

**Aksiyon maddelerini çıkarma** · `action-item-extraction`

- Ne zaman: Toplantı notları, dökümler, e-postalar veya sohbet akışlarındaki tüm açık ve örtük taahhütleri bulur ve her birini tek bir sorumlusu, tarihi, durumu ve kaynak atfı olan doğrulanabilir bir aksiyona dönüştürür; sorumlusu veya tarihi eksik olanları işaretler. \"Aksiyonlar neler?\", \"kim ne yapacak?\" sorulduğunda ya da bir toplantı veya tartışma sonrasında takip aracına hazır işler gerektiğinde kullanılır.
- Örnek istek: _"Sürüm hazırlık görüşmemizin dökümündeki tüm aksiyonları çıkar ve bir tabloya koy."_
- İlgili: `meeting-notes`, `meeting-follow-up`, `open-questions-tracker`, `decision-log`, `task-breakdown`
- Dosya: [skills/00-shared/meetings/after/action-item-extraction/SKILL.tr.md](skills/00-shared/meetings/after/action-item-extraction/SKILL.tr.md)

**Karar kaydı tutma** · `decision-log`

- Ne zaman: Toplantı, yazışma veya dokümanlardaki kararları bağlam, değerlendirilen seçenekler, gerekçe, karar verici, tarih, sonuçlar, geri alınabilirlik ve gözden geçirme tetikleyicisi içeren numaralı karar kaydı girdileri olarak kaydeder; önceki kararlarla çelişkileri işaretler. Bir ekip bir şeye neden karar verildiğinin kalıcı ve aranabilir kaydına ihtiyaç duyduğunda veya kararlar sürekli yeniden açıldığında kullanılır.
- Örnek istek: _"Bugünkü veri platformu toplantısındaki kararları karar kaydımıza ekle; Iceberg yerine Delta Lake'i seçtik, katalog seçimini erteledik."_
- İlgili: `adr`, `meeting-minutes`, `meeting-notes`, `trade-off-analysis`, `raid-log`
- Dosya: [skills/00-shared/meetings/after/decision-log/SKILL.tr.md](skills/00-shared/meetings/after/decision-log/SKILL.tr.md)

**Toplantı sonrası takip mesajı** · `meeting-follow-up`

- Ne zaman: Toplantı sonrasında katılımcılara ve paydaşlara teşekkür satırı, sonuç, kararlar, sorumlu ve tarihli aksiyonlar, açık sorular, sonraki toplantı ve düzeltme son tarihi içeren takip mesajını yazar. Bir toplantının hemen ardından herkesin aynı anlayış ve taahhütlerle ayrılması için özet e-posta veya sohbet mesajı gönderilmesi gerektiğinde kullanılır.
- Örnek istek: _"Bu notlara göre bugün tedarikçiyle yaptığımız başlangıç toplantısının katılımcılarına bir takip e-postası yaz."_
- İlgili: `meeting-summary`, `action-item-extraction`, `meeting-notes`, `stakeholder-email`, `open-questions-tracker`
- Dosya: [skills/00-shared/meetings/after/meeting-follow-up/SKILL.tr.md](skills/00-shared/meetings/after/meeting-follow-up/SKILL.tr.md)

**Açık soruları takip etme** · `open-questions-tracker`

- Ne zaman: Toplantılardan, dokümanlardan ve yazışmalardan çözülmemiş soruları; net soru, neden önemli olduğu, neyi engellediği, sorumlusu, gereken tarih, durum ve cevapla birlikte bir takip listesinde toplar ve engellediği işe göre önceliklendirir. Bir projede çok sayıda dağınık soru olduğunda, analiz veya tasarım cevap beklediğinde ya da \"hâlâ neyi bekliyoruz?\" sorulduğunda kullanılır.
- Örnek istek: _"Bu üç toplantı notunu ve gereksinim dokümanını incele, sorumlu ve tarihleriyle bir açık sorular listesi oluştur."_
- İlgili: `action-item-extraction`, `meeting-notes`, `raid-log`, `request-clarification-questions`, `decision-log`
- Dosya: [skills/00-shared/meetings/after/open-questions-tracker/SKILL.tr.md](skills/00-shared/meetings/after/open-questions-tracker/SKILL.tr.md)

### İletişim

#### Yazılı İletişim

**Durum güncellemesi yazma** · `status-update`

- Ne zaman: Genel RAG durumu, plana göre ilerleme, riskler ve sorunlar, gereken kararlar veya destek ve sonraki adımları içeren kısa bir durum güncellemesi yazar. Bir proje, iş akışı, girişim veya olay hakkındaki ilerlemenin yöneticiye, sponsora, yönlendirme komitesine veya ekip kanalına raporlanması gerektiğinde ya da \"haftalık güncelleme\", \"durum raporu\", \"ne durumdayız\" istendiğinde kullanılır.
- Örnek istek: _"Veri platformu taşıması için bu haftanın durum güncellemesini yaz: 5 alandan 3'ü taşındı, finans alanı bir firewall değişikliği yüzünden bekliyor, canlıya geçiş hâlâ ayın 30'u olarak planlı."_
- İlgili: `project-status-report`, `executive-summary`, `escalation-message`, `raid-log`, `steering-committee-pack`
- Dosya: [skills/00-shared/communication/written/status-update/SKILL.tr.md](skills/00-shared/communication/written/status-update/SKILL.tr.md)

**Yönetici özeti yazma** · `executive-summary`

- Ne zaman: Bir dokümanı, analizi, teklifi veya tartışmayı; önce sonucu ve talebi, ardından destekleyici noktaları, seçenekleri, riskleri ve sonraki adımları veren tek sayfalık, karar odaklı bir yönetici özetine indirger. Üst düzey bir okuyucunun uzun veya teknik bir içeriği hızla anlayıp harekete geçmesi gerektiğinde ya da \"kısaca\", \"yönetici özeti\", \"yönetim için tek sayfa\" istendiğinde kullanılır.
- Örnek istek: _"Bu 20 sayfalık tedarikçi değerlendirmesini, gelecek hafta kısa listedeki iki tedarikçi arasında seçim yapacak CIO için yönetici özetine dönüştür."_
- İlgili: `status-update`, `steering-committee-pack`, `document-simplify`, `decision-matrix`, `presentation-outline`
- Dosya: [skills/00-shared/communication/written/executive-summary/SKILL.tr.md](skills/00-shared/communication/written/executive-summary/SKILL.tr.md)

**Paydaş e-postası yazma** · `stakeholder-email`

- Ne zaman: Paydaşa; eylemi belirten bir konu satırı, ilk iki satırda talep veya ana mesaj, yalnızca gerekli bağlam ve okuyucunun rolüne ve ilişkiye uygun bir tonla amacı önde olan bir e-posta yazar. Bir yöneticiden, sponsordan, müşteriden, tedarikçiden veya başka bir ekipten e-posta ya da uzun sohbet mesajıyla bir şey istemek, bilgi vermek, uzlaşmak veya takip etmek gerektiğinde kullanılır.
- Örnek istek: _"Finans direktörüne, gelecek hafta UAT'ye başlayabilmemiz için ekibinin yeni maliyet dağıtım kurallarını cumaya kadar doğrulamasını isteyen bir e-posta yaz."_
- İlgili: `tone-rewrite`, `escalation-message`, `bad-news-delivery`, `stakeholder-map`, `meeting-follow-up`
- Dosya: [skills/00-shared/communication/written/stakeholder-email/SKILL.tr.md](skills/00-shared/communication/written/stakeholder-email/SKILL.tr.md)

**Eskalasyon mesajı yazma** · `escalation-message`

- Ne zaman: Sorunu, doğrulanmış olguları, iş etkisini ve son tarihi, şimdiye kadar denenenleri, ödünleşimleriyle seçenekleri, bir öneriyi ve eskalasyon sahibinden tek ve net bir talebi içeren bir eskalasyon mesajı yazar. Bir engel, bağımlılık, anlaşmazlık veya risk mevcut seviyede çözülemediğinde ve bir yöneticiden, sponsordan, tedarikçi hesap sorumlusundan ya da başka bir ekibin yönetiminden karar, kaynak veya müdahale gerektiğinde kullanılır.
- Örnek istek: _"Direktörüme, kimlik ekibinin SSO entegrasyonunu üç haftadır teslim etmediğini ve ayın 8'ine kadar gelmezse 15'indeki pilotun kayacağını eskale et."_
- İlgili: `stakeholder-email`, `status-update`, `raid-log`, `trade-off-analysis`, `conflict-resolution`
- Dosya: [skills/00-shared/communication/written/escalation-message/SKILL.tr.md](skills/00-shared/communication/written/escalation-message/SKILL.tr.md)

**Duyuru yazma** · `announcement`

- Ne zaman: Bir değişikliği, sürümü, politikayı, süreci veya kararı; ne değişiyor, neden, kim ve nasıl etkileniyor, ne zaman yürürlüğe giriyor, okuyucunun ne yapması gerekiyor ve nereden yardım alınır yapısıyla duyuran bir metin yazar. Bir ekibin, departmanın veya kullanıcı kitlesinin yeni ya da farklı bir şeyden e-posta, sohbet kanalı, intranet yazısı veya bülten aracılığıyla haberdar edilmesi gerektiğinde kullanılır.
- Örnek istek: _"Tüm yazılım ekiplerine 1 Mart'tan itibaren her canlı ortam dağıtımının yeni güvenlik tarama kapısından geçmesi gerektiğini ve o tarihe kadar ne yapmaları gerektiğini duyur."_
- İlgili: `release-announcement`, `org-change-communication`, `communication-plan`, `faq-builder`, `stakeholder-email`
- Dosya: [skills/00-shared/communication/written/announcement/SKILL.tr.md](skills/00-shared/communication/written/announcement/SKILL.tr.md)

**Ton düzenleme** · `tone-rewrite`

- Ne zaman: Mevcut bir mesajı; olgularını, taahhütlerini ve taleplerini koruyarak hedef bir tona (daha net, daha yumuşak, daha kararlı, daha resmi, daha kısa, daha tarafsız) göre yeniden yazar ve temel değişiklikleri açıklar. Elinde fazla sert, fazla belirsiz, fazla uzun, fazla gayriresmi veya fazla çekingen görünen bir e-posta, sohbet mesajı, inceleme yorumu veya yanıt taslağı olduğunda ya da \"daha iyi göster\", \"yumuşat\", \"daha kararlı yaz\", \"profesyonelleştir\" istendiğinde kullanılır.
- Örnek istek: _"Müşteriye yazdığım bu yanıtı nazik kalarak daha kararlı hale getir: \"Kusura bakmayın, özel raporu bu ay yapamayabiliriz, mümkünse belki gelecek ay?"_
- İlgili: `stakeholder-email`, `feedback-sbi`, `bad-news-delivery`, `document-simplify`, `technical-translation`
- Dosya: [skills/00-shared/communication/written/tone-rewrite/SKILL.tr.md](skills/00-shared/communication/written/tone-rewrite/SKILL.tr.md)

**Kötü haber iletme** · `bad-news-delivery`

- Ne zaman: Bir gecikmeyi, iptali, kapsam daralmasını, başarısız teslimatı, reddedilen talebi veya tutulamayan bir taahhüdü; haberi en başta, nedeni suçlamadan, okuyucuya etkisini, yapılanları, seçenekleri ve bir sonraki güncellemeyi belirterek şeffaf biçimde iletir. Bir müşteriye, sponsora, yöneticiye veya ekibe bir şeyin söz verildiği ya da beklendiği gibi olmayacağını yazılı olarak ya da bir görüşme için konuşma notlarıyla söylemek gerektiğinde kullanılır.
- Örnek istek: _"Sponsora, ayın 20'sinde planlanan raporlama sürümünün veri sağlayıcısının API'si değiştiği için üç hafta kayacağını ve bunun yerine ne önerdiğimizi söylememe yardım et."_
- İlgili: `tone-rewrite`, `escalation-message`, `stakeholder-email`, `status-update`, `customer-outage-notice`
- Dosya: [skills/00-shared/communication/written/bad-news-delivery/SKILL.tr.md](skills/00-shared/communication/written/bad-news-delivery/SKILL.tr.md)

#### Sunum ve Sözlü

**Sunum iskeleti çıkarma** · `presentation-outline`

- Ne zaman: Hedef kitleye özel bir akış ve her slaytta tek mesaj, destekleyici kanıt, net bir talep ve süre planı içeren slayt slayt bir sunum iskeleti çıkarır. Birinin yöneticilere, müşteriye, bir kurula veya ekibe öneri, durum, tasarım, sonuç ya da karar sunması gerektiğinde ve slaytları tasarlamadan önce yapıya ihtiyaç duyduğunda kullanılır.
- Örnek istek: _"Yönetim ekibine, raporlama iş yüklerimizi gelecek yıl yeni veri platformuna taşımayı önerdiğimiz 20 dakikalık bir sunumun iskeletini çıkar."_
- İlgili: `executive-summary`, `steering-committee-pack`, `demo-script`, `elevator-pitch`, `stakeholder-map`
- Dosya: [skills/00-shared/communication/verbal/presentation-outline/SKILL.tr.md](skills/00-shared/communication/verbal/presentation-outline/SKILL.tr.md)

**Demo senaryosu yazma** · `demo-script`

- Ne zaman: Kullanıcı hikâyesine dayalı akış, adım adım tıklama sırası, kitlenin değer gördüğü noktalara bağlı anlatım, hazır veri, süre planı ve her riskli adım için yedek plan içeren bir ürün veya özellik demo senaryosu yazar. Bir ekip yazılımı paydaşlara, müşteriye, bir inceleme oturumuna veya potansiyel müşteriye göstermesi gerektiğinde ve doğaçlama yerine prova edilebilir bir akış istediğinde kullanılır.
- Örnek istek: _"Yeni fatura onay akışını iterasyon incelemesinde finans müdürlerine göstermek için 10 dakikalık bir demo senaryosu yaz."_
- İlgili: `presentation-outline`, `iteration-review-prep`, `stakeholder-review-prep`, `uat-scenarios`, `elevator-pitch`
- Dosya: [skills/00-shared/communication/verbal/demo-script/SKILL.tr.md](skills/00-shared/communication/verbal/demo-script/SKILL.tr.md)

**Asansör konuşması hazırlama** · `elevator-pitch`

- Ne zaman: Bir fikir, proje, ürün veya talep için tek bir dinleyiciye göre uyarlanmış; dikkat çekici bir giriş, problem, öneri, kanıt ve tek bir somut talep içeren 30-60 saniyelik sözlü bir konuşma yazar. Birinin meşgul bir kişiyi bir sonraki adımı atacak kadar ilgilendirmek için kısa bir fırsatı (koridor, görüşme açılışı, toplantıda tanıtım, bütçe veya sponsorluk talebi) olduğunda kullanılır.
- Örnek istek: _"CTO'muzu mikroservislerimiz arasında otomatik kontrat testi pilotuna sponsor olmaya ikna edecek 45 saniyelik bir konuşma hazırla."_
- İlgili: `presentation-outline`, `executive-summary`, `value-proposition-canvas`, `problem-statement`, `stakeholder-map`
- Dosya: [skills/00-shared/communication/verbal/elevator-pitch/SKILL.tr.md](skills/00-shared/communication/verbal/elevator-pitch/SKILL.tr.md)

#### Kişilerarası

**Geri bildirim verme (SBI)** · `feedback-sbi`

- Ne zaman: Olumlu veya düzeltici geri bildirimi Durum-Davranış-Etki (SBI) modeliyle kurgular; gözlenen davranışı yorumdan ayırır, somut etkiyi belirtir ve bir talep ile açık bir soruyla bitirir. Birinin bir çalışma arkadaşına, ekip üyesine, eşdüzey birine veya yöneticisine geri bildirim vermesi, zor bir konuşmaya hazırlanması ya da kişiyi yargılar gibi duran bir geri bildirimi yeniden yazması gerektiğinde kullanılır.
- Örnek istek: _"Review beklemeden pull request'leri merge eden kıdemli bir geliştiriciye, onu savunmaya geçirmeden geri bildirim vermeme yardım et."_
- İlgili: `one-on-one-prep`, `performance-review`, `conflict-resolution`, `tone-rewrite`, `underperformance-plan`
- Dosya: [skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.tr.md](skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.tr.md)

**Çatışma çözme** · `conflict-resolution`

- Ne zaman: Bir iş yeri çatışmasını taraflar, dile getirilen pozisyonlar, altta yatan çıkarlar, olgular ile algılar ve çatışma türü olarak haritalar; ardından ortak çıkarlara hizmet eden seçenekler ve üzerinde anlaşılan sonraki adımlarla arabulucu bir çözüm yolu önerir. İki kişi, ekip veya birim öncelikler, sahiplik, yaklaşım ya da davranış konusunda anlaşamadığında ve bu anlaşmazlık işi durdurduğunda veya ilişkiye zarar verdiğinde kullanılır.
- Örnek istek: _"Backend ve mobil ekiplerimiz API versiyonlamanın kimde olduğu konusunda sürekli tartışıyor ve sürümler kayıyor. Arabuluculuk yapmama yardım et."_
- İlgili: `feedback-sbi`, `negotiation-prep`, `facilitation-guide`, `trade-off-analysis`, `decision-log`
- Dosya: [skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.tr.md](skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.tr.md)

**Müzakereye hazırlanma** · `negotiation-prep`

- Ne zaman: Bir müzakereye hazırlık için hedefinizi, çıkarlarınızı, BATNA'nızı, masadan kalkma noktanızı, karşı tarafın olası çıkarlarını ve BATNA'sını, olası anlaşma alanını, takas edilebilir tavizleri ve gerekçesiyle açılış pozisyonunu belirler. Birinin müşteri, tedarikçi, sponsor veya başka bir ekiple kapsam, teslim tarihi, bütçe, kaynak, tedarikçi sözleşmesi, ücret veya koşullar üzerine müzakere etmesi gerektiğinde kullanılır.
- Örnek istek: _"Mevcut ekiple ancak %60'ını teslim edebilecekken kapsamın tamamını mart ayına kadar isteyen iş sponsoruyla müzakereye hazırlanmama yardım et."_
- İlgili: `conflict-resolution`, `stakeholder-map`, `trade-off-analysis`, `vendor-evaluation`, `pricing-analysis`
- Dosya: [skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.tr.md](skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.tr.md)

### Dokümantasyon

#### Yazım

**Doküman iskeleti çıkarma** · `document-outline`

- Ne zaman: Herhangi bir doküman (tasarım dokümanı, politika, rehber, rapor, teklif, şartname) için amacından, hedef kitlesinden ve desteklemesi gereken kararlardan yola çıkarak bölüm hedefleri ve içerik notlarıyla uygun bir yapı önerir. Yeni bir doküman başlatılacağında, boş sayfa karşısında kalındığında, dağınık bir doküman yeniden yapılandırılacağında veya bir dokümanda hangi bölümlerin olması gerektiği sorulduğunda kullanılır.
- Örnek istek: _"Batch raporlama işlerimizi event-driven bir pipeline'a taşımayı öneren bir dokümanın iskeletini çıkar; okuyucular mimari kurul."_
- İlgili: `docs-information-architecture`, `document-review`, `executive-summary`, `technical-design-doc`, `brd-writing`
- Dosya: [skills/00-shared/documentation/authoring/document-outline/SKILL.tr.md](skills/00-shared/documentation/authoring/document-outline/SKILL.tr.md)

**Sözlük oluşturma** · `glossary-builder`

- Ne zaman: Kaynak materyaldeki alan terimlerini, kısaltmaları ve çok anlamlı kelimeleri çıkarır; eş anlamlılar, yasaklı kullanımlar ve sorumlularla birlikte belirsizlik içermeyen, test edilebilir tanımlar yazar. Bir projede, dokümanda veya ekipte terminoloji tutarsızsa, kişiler bir alana alıştırılırken, gereksinim veya veri modeli yazılırken ya da sözlük veya ortak dil istendiğinde kullanılır.
- Örnek istek: _"Bu gereksinim notlarından bir sözlük oluştur; müşteri, cari, hesap ve abone kelimeleri birbirinin yerine kullanılıyor."_
- İlgili: `business-rules-catalog`, `bounded-context-map`, `technical-translation`, `data-catalog-entry`, `ambiguity-detection`
- Dosya: [skills/00-shared/documentation/authoring/glossary-builder/SKILL.tr.md](skills/00-shared/documentation/authoring/glossary-builder/SKILL.tr.md)

**SSS oluşturma** · `faq-builder`

- Ne zaman: Belirli bir hedef kitlenin bir ürün, değişiklik, politika veya proje hakkında soracağı olası soruları üretir ve bunları yalnızca verilen kaynak materyale dayanarak cevaplar, boşlukları işaretler. Bir lansman, geçiş, politika değişikliği, iç araç veya müşteri yardım sayfası için SSS hazırlanırken ya da destek veya sohbet kanallarına aynı sorular tekrar tekrar geldiğinde kullanılır.
- Örnek istek: _"Bu yaygınlaştırma planına göre, eski VPN'den yeni zero-trust erişim istemcisine geçiş hakkında çalışanlar için bir SSS hazırla."_
- İlgili: `kb-article`, `announcement`, `org-change-communication`, `user-guide`, `ticket-response`
- Dosya: [skills/00-shared/documentation/authoring/faq-builder/SKILL.tr.md](skills/00-shared/documentation/authoring/faq-builder/SKILL.tr.md)

**Kod olarak diyagram üretme** · `diagram-as-code`

- Ne zaman: Bir sistemin, sürecin, etkileşim sırasının, veri modelinin veya durum makinesinin metinsel tarifini Mermaid veya PlantUML ile doğru ve okunabilir bir diyagrama çevirir; uygun diyagram türünü seçer ve varsayımları listeler. Bir şeyin çizilmesi, görselleştirilmesi veya diyagramının çıkarılması istendiğinde, dokümanlar veya pull request için sürüm kontrolüne uygun bir diyagram gerektiğinde ya da bir beyaz tahta fotoğrafı tarifi veya eski bir diyagram koda çevrilecekse kullanılır.
- Örnek istek: _"Mermaid sequence diyagramı çiz: mobil uygulama API gateway'i çağırıyor, gateway token'ı kimlik sağlayıcıyla doğruluyor, sonra sipariş servisini çağırıyor, sipariş servisi OrderCreated event'i yayınlıyor."_
- İlgili: `c4-model`, `bpmn-model`, `sequence-flow`, `state-model`, `document-outline`
- Dosya: [skills/00-shared/documentation/authoring/diagram-as-code/SKILL.tr.md](skills/00-shared/documentation/authoring/diagram-as-code/SKILL.tr.md)

**Teknik çeviri** · `technical-translation`

- Ne zaman: Teknik içeriği (şartname, dokümantasyon, arayüz metni, hata mesajı, sürüm notu, runbook) İngilizce ile Türkçe arasında terminolojiyi, kodu, tanımlayıcıları, biçimi ve anlamı koruyarak çevirir; kaynaktaki belirsiz metni işaretler. Teknik bir doküman, mesaj veya arayüz diğer dilde teslim edilecekse ya da mevcut bir çevirinin terminolojisi hizalanacaksa kullanılır.
- Örnek istek: _"Geliştirici rehberimizin API hata yönetimi bölümünü İngilizceden Türkçeye çevir; kodu ve HTTP terimlerini olduğu gibi bırak."_
- İlgili: `glossary-builder`, `microcopy`, `error-message-writing`, `document-review`, `style-guide-check`
- Dosya: [skills/00-shared/documentation/authoring/technical-translation/SKILL.tr.md](skills/00-shared/documentation/authoring/technical-translation/SKILL.tr.md)

#### Gözden Geçirme

**Doküman gözden geçirme** · `document-review`

- Ne zaman: Herhangi bir dokümanı açıklık, bütünlük, iç tutarlılık, iddiaların doğruluğu ve hedef kitle ile amaca uygunluk açısından inceler; öncelikli, konumu belirtilmiş bulguları önerilen düzeltmeler ve bir genel kararla verir. Bir taslak için geri bildirim istendiğinde, bir doküman onay veya yayın öncesi kontrol edilecekse ya da bir şartname, teklif, politika, rehber veya rapor için ikinci görüş gerektiğinde kullanılır.
- Örnek istek: _"Bu olay yönetimi süreç dokümanını operasyon direktörlerine onaya göndermeden önce gözden geçir."_
- İlgili: `requirements-review-checklist`, `architecture-review`, `document-simplify`, `style-guide-check`, `doc-diff-summary`
- Dosya: [skills/00-shared/documentation/review/document-review/SKILL.tr.md](skills/00-shared/documentation/review/document-review/SKILL.tr.md)

**Dokümanı sadeleştirme** · `document-simplify`

- Ne zaman: Bir dokümanı veya metin parçasını; tüm yükümlülükleri, sayıları, koşulları ve kararları koruyarak tekrarları, jargonu, çekinceli ifadeleri ve isimleştirmeleri ayıklayıp hedef kitlesi için daha kısa ve kolay okunur hâle getirir. Bir metin okuyucusu için fazla uzun, yoğun veya teknikse, bir şeyin kısaltılması, sadeleştirilmesi veya sade dille yazılması istendiğinde ya da doküman bir uzunluk sınırına sığmalıysa kullanılır.
- Örnek istek: _"Üç sayfalık bu veri saklama politikasını takım liderlerinin ne yapmaları gerektiğini anlayacağı şekilde sadeleştir; tüm yükümlülükleri koru."_
- İlgili: `document-review`, `executive-summary`, `tone-rewrite`, `microcopy`, `technical-translation`
- Dosya: [skills/00-shared/documentation/review/document-simplify/SKILL.tr.md](skills/00-shared/documentation/review/document-simplify/SKILL.tr.md)

**Doküman değişikliklerini özetleme** · `doc-diff-summary`

- Ne zaman: Bir dokümanın (sözleşme, şartname, politika, runbook, gereksinimler) iki sürümünü karşılaştırır; esaslı değişiklikleri, her paydaşa etkilerini ve doğurdukları soruları, anlam değişikliklerini biçimsel olanlardan ayırarak kategorize edilmiş bir özet hâlinde sunar. Bir dokümanın yeni sürümü geldiğinde, yeniden onay veya imza öncesinde, tedarikçi ya da müşteri revize taslak gönderdiğinde veya iki sürüm arasında neyin değiştiği sorulduğunda kullanılır.
- Örnek istek: _"Tedarikçiden gelen entegrasyon şartnamesinin v1.3 ve v1.4 sürümleri burada. Ne değişti ve bizim için ne anlama geliyor?"_
- İlgili: `change-request-analysis`, `impact-analysis`, `document-review`, `changelog-entry`, `requirements-sign-off`
- Dosya: [skills/00-shared/documentation/review/doc-diff-summary/SKILL.tr.md](skills/00-shared/documentation/review/doc-diff-summary/SKILL.tr.md)

### Problem Çözme ve Karar Araçları

#### Problem Tanımlama

**Problem tanımı yazma** · `problem-statement`

- Ne zaman: Bir problemi; kimin etkilendiğini, ne olduğunu, ne zaman ve nerede olduğunu nicel etki ve kanıtla, sınırları ve başarı sinyalleriyle birlikte çözüm içermeyen kesin bir ifadeyle tanımlar. Her girişim, inceleme, iyileştirme veya tasarım çalışmasının başında, ekip doğrudan çözüme atladığında, paydaşlar aynı sorunu farklı anlattığında veya bir problemin tanımlanması ya da yeniden çerçevelenmesi istendiğinde kullanılır.
- Örnek istek: _"Problem tanımı yaz: müşteriler aylık faturanın yanlış olduğundan sürekli şikâyet ediyor ve destek ekibi her ay başında aşırı yükleniyor."_
- İlgili: `five-whys`, `fishbone-analysis`, `assumption-mapping`, `hypothesis-statement`, `request-intake-document`
- Dosya: [skills/00-shared/thinking-tools/problem/problem-statement/SKILL.tr.md](skills/00-shared/thinking-tools/problem/problem-statement/SKILL.tr.md)

**5 Neden analizi** · `five-whys`

- Ne zaman: Belirgin bir belirtiden başlayıp doğrulanabilir bir veya daha fazla kök nedene inen disiplinli bir 5 Neden analizi yapar; her halkanın kanıtını, katkıda bulunan her neden için ayrı bir dalı ve belirtiyi değil nedeni hedefleyen önlemleri ortaya koyar. Bir olay, hata, kaçırılan hedef veya tekrarlayan problem için kök neden gerektiğinde, 'bu neden sürekli oluyor' sorulduğunda ya da bir postmortem veya çıkarılan dersler çalışması nedensel derinlik istediğinde kullanılır.
- Örnek istek: _"Şunun için 5 Neden analizi yap: gece çalışan müşteri aktarımı bu ay üç kez hata verdi ve finans raporu her seferinde geç aldı."_
- İlgili: `problem-statement`, `fishbone-analysis`, `postmortem`, `debugging-hypotheses`, `lessons-learned`
- Dosya: [skills/00-shared/thinking-tools/problem/five-whys/SKILL.tr.md](skills/00-shared/thinking-tools/problem/five-whys/SKILL.tr.md)

**Balık kılçığı analizi** · `fishbone-analysis`

- Ne zaman: Açıkça tanımlanmış bir sonucun tüm makul nedenlerini alana uygun kategorilerde düzenleyen bir Ishikawa (balık kılçığı) diyagramı oluşturur, kanıtlı nedenleri hipotezlerden ayırır ve önce doğrulanmaya değer birkaç nedeni seçer. Bir problemin birden fazla etkileşen nedeni olabileceğinde, ekip nedenler üzerine beyin fırtınası yapıp yapıya ihtiyaç duyduğunda veya en umut verici dallarda 5 Neden çalıştırmadan önce kullanılır.
- Örnek istek: _"Balık kılçığı analizi yap: sürüm teslim süremiz son iki çeyrekte 3 günden 2 haftaya çıktı."_
- İlgili: `problem-statement`, `five-whys`, `postmortem`, `diagram-as-code`, `assumption-mapping`
- Dosya: [skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.tr.md](skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.tr.md)

**Varsayım haritalama** · `assumption-mapping`

- Ne zaman: Bir planın, ürün fikrinin, tahminin veya kararın arkasındaki varsayımları ortaya çıkarır, türlerine göre sınıflar (arzu edilebilirlik, kullanılabilirlik, fizibilite, ekonomik yapılabilirlik, etik/mevzuat, teslimat), önem ve kanıta göre konumlandırır ve en riskli olanları en ucuz testle birlikte test edilebilir ifadelere çevirir. Bütçe veya kapsam taahhüdünden önce, bir plan fazla iyimser göründüğünde ya da bunun işe yaraması için neyin doğru olması gerektiği sorulduğunda kullanılır.
- Örnek istek: _"KOBİ müşterileri için gelecek çeyrekte self-servis oryantasyon başlatma planımızın varsayımlarını haritala."_
- İlgili: `hypothesis-statement`, `experiment-design`, `pre-mortem`, `risk-register`, `problem-statement`
- Dosya: [skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.tr.md](skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.tr.md)

#### Karar Verme

**Ağırlıklı karar matrisi** · `decision-matrix`

- Ne zaman: Seçenekleri açık ağırlıklara, puanlama ölçeklerine ve eleyici zorunlu kurallara sahip, üzerinde uzlaşılmış ve birbirinden bağımsız kriterlere göre karşılaştıran ağırlıklı bir karar matrisi oluşturur; ardından sonucun ağırlıklara ve belirsiz puanlara ne kadar duyarlı olduğunu test eder. Üç veya daha fazla seçenek (tedarikçi, teknoloji, tasarım, yatırım adayı) arasında seçim yapılırken, kararın başkalarına savunulabilir olması gerektiğinde veya bir grubun uzlaşması gerektiğinde kullanılır.
- Örnek istek: _"Sipariş platformumuz için üç mesaj kuyruğu (broker) arasında seçim yapmak üzere ağırlıklı bir karar matrisi oluştur."_
- İlgili: `trade-off-analysis`, `pros-cons`, `vendor-evaluation`, `technology-selection`, `decision-log`
- Dosya: [skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.tr.md](skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.tr.md)

**Artı-eksi analizi** · `pros-cons`

- Ne zaman: Tek bir öneri veya birkaç seçenek için dengeli bir artı ve eksi analizi yapar; her maddeyi etki ve olasılığa göre tartar, olguları görüşlerden ayırır, hiçbir şey yapmama durumunu da temel alır ve net, koşula bağlı bir öneriyle bitirir. Hızlı kararlar, evet/hayır önerileri veya bir yaklaşıma bağlanmadan önce avantajları ve dezavantajları sorulduğunda kullanılır.
- Örnek istek: _"Haftalık sürümden ihtiyaç anında sürüme geçmenin artılarını ve eksilerini çıkar, bir öneri ver."_
- İlgili: `decision-matrix`, `trade-off-analysis`, `bias-check`, `pre-mortem`, `decision-log`
- Dosya: [skills/00-shared/thinking-tools/decision/pros-cons/SKILL.tr.md](skills/00-shared/thinking-tools/decision/pros-cons/SKILL.tr.md)

**SWOT analizi** · `swot-analysis`

- Ne zaman: Sınırları belirli bir konu (ürün, ekip, platform, girişim, iş birimi) için belirtilen bir hedefe göre SWOT analizi yapar; iç güçlü ve zayıf yönleri dış fırsat ve tehditlerden ayrı tutar, her maddeyi kanıtla destekler ve sonucu TOWS stratejilerine ve önceliklendirilmiş aksiyonlara dönüştürür. Strateji veya planlama oturumlarında, büyük bir yatırımdan önce, yeni bir pazara girerken ya da SWOT istendiğinde kullanılır.
- Örnek istek: _"Gelecek yılın planlaması öncesinde kurum içi veri platformu ekibimiz için SWOT analizi yap."_
- İlgili: `competitor-analysis`, `product-strategy-one-pager`, `technology-strategy`, `assumption-mapping`, `risk-register`
- Dosya: [skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.tr.md](skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.tr.md)

**Ödünleşim analizi** · `trade-off-analysis`

- Ne zaman: Her seçeneğin rekabet eden nitelikler (ör. hız ve güvenlik, maliyet ve dayanıklılık, esneklik ve sadelik, kapsam ve zaman) arasında neyi kazanıp neyi feda ettiğini açıkça ortaya koyar; belirleyici gerilimi, her tercihin geri alınabilirliğini ve tercih edilen seçeneğin hangi koşullarda doğru olmaktan çıkacağını belirler. Hiçbir seçeneğin her konuda üstün olmadığı mimari, ürün, kapsam veya süreç kararlarında, paydaşlar birbirini anlamadan tartıştığında veya bir kararı kayda geçirmeden önce kullanılır.
- Örnek istek: _"Yeni hasar yönetim sistemimiz için modüler monolit ile mikroservisler arasındaki ödünleşimleri analiz et."_
- İlgili: `decision-matrix`, `adr`, `architecture-review`, `pros-cons`, `technology-selection`
- Dosya: [skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.tr.md](skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.tr.md)

**Pre-mortem** · `pre-mortem`

- Ne zaman: Bir plan, proje, lansman veya karar için başarısızlığın zaten gerçekleştiğini varsayarak geriye doğru çalışır; en olası nedenleri, erken uyarı sinyallerini ve önlemleri ortaya çıkarır. Bir plan, lansman, geçiş veya büyük karar kesinleşmeden önce, ekip aşırı iyimser göründüğünde ya da \"ne ters gidebilir?\" veya \"pre-mortem yapalım\" dendiğinde kullanılır.
- Örnek istek: _"Faturalama veritabanını mart ayında tek bir hafta sonunda yeni bir bulut bölgesine taşıma planımız için pre-mortem yap."_
- İlgili: `risk-register`, `assumption-mapping`, `bias-check`, `raid-log`, `technical-risk-review`
- Dosya: [skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.tr.md](skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.tr.md)

**Bilişsel yanlılık kontrolü** · `bias-check`

- Ne zaman: Bir analizi, öneriyi veya kararı doğrulama, çıpalama, hayatta kalan yanılgısı, batık maliyet, erişilebilirlik, aşırı özgüven ve grup düşüncesi gibi bilişsel yanlılıklar açısından inceler; her şüpheli yanlılığın kanıtını gösterir ve somut bir düzeltici aksiyon önerir. Bir karar verilmek veya analiz paylaşılmak üzereyken, \"bir şeyi atlıyor muyum?\", \"bu yanlı mı?\", \"mantığımı sorgula\" denildiğinde ya da bir sonuca karşı eleştirel bakış istendiğinde kullanılır.
- Örnek istek: _"Yönlendirme komitesine göndermeden önce bu öneriyi yanlılık açısından kontrol et: kurum içi zamanlayıcıya yatırıma devam etmeliyiz, çünkü üzerinde zaten 18 ay çalıştık ve iki pilot ekip çok memnun."_
- İlgili: `pre-mortem`, `assumption-mapping`, `decision-matrix`, `trade-off-analysis`, `decision-log`
- Dosya: [skills/00-shared/thinking-tools/decision/bias-check/SKILL.tr.md](skills/00-shared/thinking-tools/decision/bias-check/SKILL.tr.md)

### Bilgi Yönetimi

#### Kayıt ve Aktarım

**Çıkarılan dersleri kaydetme** · `lessons-learned`

- Ne zaman: Bir proje, sürüm, faz, olay veya girişimden çıkarılan dersleri; neyin işe yarayıp neyin yaramadığına dair kanıta dayalı gözlemler, nedenleri ve korunacak ya da değiştirilecek, sahibi ve uygulanacağı yer belli somut aksiyonlar olarak kayda geçirir. Bir proje veya fazın sonunda, bir sürüm ya da önemli bir olaydan sonra, kapanış raporu hazırlanırken veya notlar, retrospektifler ya da zaman çizelgelerinden \"çıkarılan dersleri yaz\" dendiğinde kullanılır.
- Örnek istek: _"Bu retro notlarını ve zaman çizelgesini kullanarak CRM geçiş projemizden çıkarılan dersleri yaz."_
- İlgili: `retrospective-facilitation`, `postmortem`, `project-closure-report`, `kb-article`, `action-item-extraction`
- Dosya: [skills/00-shared/knowledge/capture/lessons-learned/SKILL.tr.md](skills/00-shared/knowledge/capture/lessons-learned/SKILL.tr.md)

**Devir-teslim dokümanı yazma** · `handover-document`

- Ne zaman: Bir sistemin, projenin, servisin, iş akışının veya rolün sahipliğini yeni sahibine devreden bir devir-teslim dokümanı yazar; bağlamı, mevcut durumu, sorumlulukları, iletişim kişilerini, erişimleri, periyodik görevleri, riskleri, açık işleri ve kabul noktası olan bir geçiş planını kapsar. Biri ayrıldığında, rol değiştirdiğinde, uzun izne çıktığında, bir proje teslimattan operasyona geçtiğinde, tedarikçi veya ekip değiştiğinde ya da \"devir-teslim hazırla\" dendiğinde kullanılır.
- Örnek istek: _"İki hafta sonra başka bir ekibe geçiyorum. Sahibi olduğum ödeme mutabakat servisi için devir-teslim dokümanı yazmama yardım et."_
- İlgili: `on-call-handover`, `runbook`, `onboarding-guide`, `raid-log`, `kb-article`
- Dosya: [skills/00-shared/knowledge/capture/handover-document/SKILL.tr.md](skills/00-shared/knowledge/capture/handover-document/SKILL.tr.md)

**Bilgi bankası makalesi yazma** · `kb-article`

- Ne zaman: Notlardan, kayıtlardan, sohbet yazışmalarından veya uzman girdisinden aranabilir bir bilgi bankası makalesi (nasıl yapılır, sorun giderme veya açıklama) yazar; bulunabilir bir başlık, okuyucuların gerçekten kullandığı belirtiler ve arama terimleri, geçerlilik kapsamı, doğrulanmış adımlar, beklenen sonuçlar ve sahiplik içerir. Aynı soru sürekli sorulduğunda, bir destek kaydı veya olay yeniden kullanılabilir bir çözüm ürettiğinde, kayıt dışı bilgi yazıya dökülmesi gerektiğinde ya da \"bilgi bankası makalesi yaz\" veya \"bunu wiki için dokümante et\" dendiğinde kullanılır.
- Örnek istek: _"Yeni dizüstü bilgisayarlardaki VPN sertifika hatalarıyla ilgili bu destek yazışmasını bir bilgi bankası makalesine dönüştür."_
- İlgili: `how-to-guide`, `faq-builder`, `runbook`, `document-review`, `glossary-builder`
- Dosya: [skills/00-shared/knowledge/capture/kb-article/SKILL.tr.md](skills/00-shared/knowledge/capture/kb-article/SKILL.tr.md)

**Oryantasyon rehberi yazma** · `onboarding-guide`

- Ne zaman: Bir ekibe, departmana veya projeye yeni katılan kişiyi bağlam, çalışma biçimi, araçlar ve erişimler, kilit kişiler, terimler ve açık \"hazırsın\" kilometre taşlarıyla sıralanmış ilk görevler boyunca yönlendiren bir oryantasyon rehberi yazar. Ekibe yeni üyeler, yükleniciler veya transferler katılacaksa, mevcut oryantasyon bilgisi wiki ve sohbetlere dağılmışsa ya da bir rol veya ekip için \"oryantasyon rehberi yaz\" dendiğinde kullanılır.
- Örnek istek: _"Ödeme ekibimize katılan yeni iş analistleri için bir oryantasyon rehberi yaz."_
- İlgili: `onboarding-plan-30-60-90`, `technical-onboarding`, `handover-document`, `glossary-builder`, `kb-article`
- Dosya: [skills/00-shared/knowledge/capture/onboarding-guide/SKILL.tr.md](skills/00-shared/knowledge/capture/onboarding-guide/SKILL.tr.md)

## İş Analizi

### İş Analisti

#### Talep Alma

**Talep alma dokümanı oluşturma** · `request-intake-document`

- Ne zaman: Ham bir iş talebini (e-posta, sohbet mesajı, toplantı notu, kayıt) hedef, kapsam, değer, paydaşlar, kısıtlar ve açık sorular içeren yapılandırılmış bir talep alma dokümanına dönüştürür. Yeni bir talep, fikir veya değişiklik isteği geldiğinde, analiz, tahmin ya da önceliklendirmeden önce kayıt altına alınması gerektiğinde kullanılır.
- Örnek istek: _"Bu talep için talep alma dokümanı oluştur: Satış ekibi denetim için ay sonuna kadar müşteri listesi ekranına Excel aktarımı istiyor."_
- İlgili: `request-clarification-questions`, `request-completeness-check`, `request-triage`, `stakeholder-identification`
- Dosya: [skills/01-business-analysis/business-analyst/intake/request-intake-document/SKILL.tr.md](skills/01-business-analysis/business-analyst/intake/request-intake-document/SKILL.tr.md)

**Talep netleştirme soruları** · `request-clarification-questions`

- Ne zaman: Yeni bir talep için talep sahibine sorulacak netleştirme sorularını konu başlıklarına (iş, kullanıcılar, veri, entegrasyon, NFR, yasal, operasyon, raporlama, geçiş) göre gruplar ve cevabın analizi ne kadar engellediğine göre önceliklendirir. Talep belirsizse, netleştirme toplantısı veya e-postası öncesinde ya da 'iş birimine bununla ilgili ne sormalıyım?' sorusu geldiğinde kullanılır.
- Örnek istek: _"Bu talep için talep sahibine ne sormalıyım: 'Müşteriler adreslerini mobil uygulamadan kendileri güncelleyebilsin.'"_
- İlgili: `request-intake-document`, `request-completeness-check`, `interview-question-set`, `open-questions-tracker`
- Dosya: [skills/01-business-analysis/business-analyst/intake/request-clarification-questions/SKILL.tr.md](skills/01-business-analysis/business-analyst/intake/request-clarification-questions/SKILL.tr.md)

**Gelen talepleri sınıflandırma** · `request-triage`

- Ne zaman: Gelen bir veya birden çok iş talebini tür, aciliyet, değer, efor sınıfı ve riske göre sınıflandırır, mükerrerleri bulur ve her birini doğru yola (hızlı yol, analiz, fizibilite, proje, destek, ret) yönlendirir. Yeni taleplerden oluşan bir kuyruk sıralanacağında, talep değerlendirme toplantısında veya 'bu talepler nereye gitmeli, önce hangisi?' sorusu geldiğinde kullanılır.
- Örnek istek: _"Bu haftaki gelen kutusundaki 8 talebi sınıflandır; hangileri analize gider, hangileri destek kaydı, hangilerini reddetmeliyiz söyle."_
- İlgili: `request-intake-document`, `request-completeness-check`, `ticket-triage`, `backlog-prioritization`, `change-request-analysis`
- Dosya: [skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.tr.md](skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.tr.md)

**Talep eksiklik kontrolü** · `request-completeness-check`

- Ne zaman: Bir talebi veya talep alma dokümanını eksik kontrol listesine (iş, kullanıcılar, veri, entegrasyon, NFR, yasal, operasyon, raporlama, geçiş) göre inceler; eksik, belirsiz veya çelişkili noktaları önem derecesiyle raporlar ve hazır/hazır değil kararı verir. Talep analize, tahmine veya sprint/backlog'a girmeden önce ya da 'bu talep başlamak için yeterince eksiksiz mi?' sorusu geldiğinde kullanılır.
- Örnek istek: _"Bu talep analize başlamak için yeterince eksiksiz mi kontrol et: 'Belli bir limitin üstündeki siparişlere indirim onay adımı ekleyelim, yöneticiler e-postayla onaylasın.'"_
- İlgili: `request-intake-document`, `request-clarification-questions`, `ambiguity-detection`, `requirements-gap-analysis`, `definition-of-ready`
- Dosya: [skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.tr.md](skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.tr.md)

#### Paydaş Analizi

**Paydaşları belirleme** · `stakeholder-identification`

- Ne zaman: Bir girişimi etkileyen, ondan etkilenen veya hakkında karar veren herkesi, gizli ve dolaylı paydaşlar (uyum, operasyon, veri sahipleri, dış taraflar) dahil olmak üzere rolleri, ilgi alanları ve onlardan ne gerektiğiyle birlikte belirler. Bir talebin, projenin veya analizin başında ya da 'kimleri dahil etmemiz gerekiyor?' sorusu geldiğinde kullanılır.
- Örnek istek: _"Kağıt tabanlı masraf onayını dijital iş akışıyla değiştirme projesinin paydaşları kimler?"_
- İlgili: `stakeholder-map`, `raci-matrix`, `stakeholder-register`, `request-intake-document`, `communication-plan`
- Dosya: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.tr.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.tr.md)

**Güç/ilgi paydaş haritası** · `stakeholder-map`

- Ne zaman: Paydaşları her puan için kanıtıyla birlikte güç/ilgi matrisine yerleştirir, mevcut ve hedeflenen tutumu ekler; her çeyrek ve kilit kişi için iletişim stratejisi, kanal ve sıklık belirler. Paydaşlar belirlendikten sonra, iletişim planı öncesinde veya girişime desteğin belirsiz olduğu durumlarda kullanılır; 'güç ilgi matrisi', 'kimi yakından yönetmeliyiz?' gibi ifadeler tetikleyicidir.
- Örnek istek: _"CRM geçişi için bu 9 paydaşı güç/ilgi matrisine yerleştir ve her biriyle nasıl ilerlememiz gerektiğini söyle."_
- İlgili: `stakeholder-identification`, `raci-matrix`, `communication-plan`, `stakeholder-register`, `conflict-resolution`
- Dosya: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.tr.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.tr.md)

**RACI matrisi** · `raci-matrix`

- Ne zaman: Her aktivite veya çıktı için Sorumlu (R), Hesap Veren (A), Danışılan (C) ve Bilgilendirilen (I) rollerini atayan bir RACI matrisi oluşturur ve doğrular (tam bir A, en az bir R, aşırı yüklü rol yok, boş satır yok). Sorumluluklar belirsiz olduğunda, işler ekipler arasında kaldığında veya bir proje, süreç ya da analiz aktivitesi için 'kim neyin sahibi?' sorusu geldiğinde kullanılır.
- Örnek istek: _"Ödeme altyapısı entegrasyonumuzun gereksinim fazı için RACI oluştur: iş analisti, PO, mimar, geliştirme lideri, QA, güvenlik, tedarikçi."_
- İlgili: `stakeholder-identification`, `stakeholder-map`, `communication-plan`, `project-charter`, `role-definition`
- Dosya: [skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.tr.md](skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.tr.md)

#### Gereksinim Toplama

**Görüşme soruları hazırlama** · `interview-question-set`

- Ne zaman: Paydaş tipine (üst yönetici, süreç sahibi, son kullanıcı, BT/sistem sahibi, uyum) göre uyarlanmış; açılış, bağlam, açık uçlu, derinleştirici ve doğrulayıcı sorular, süre planı ve takip sorularını içeren bir gereksinim görüşmesi rehberi hazırlar. Gereksinim görüşmesi öncesinde veya 'görüşmede kullanıcılara/yöneticilere ne sormalıyım?' sorusu geldiğinde kullanılır.
- Örnek istek: _"Depo vardiya amirleriyle bugün stok farklarını nasıl yönettiklerine dair 45 dakikalık bir görüşme hazırla."_
- İlgili: `interview-notes-analysis`, `request-clarification-questions`, `workshop-plan`, `stakeholder-identification`, `problem-interview-script`
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.tr.md)

**Görüşme notlarını analiz etme** · `interview-notes-analysis`

- Ne zaman: Ham görüşme notlarını veya dökümlerini analiz eder; ihtiyaçları, sorunları, iş kurallarını, istisnaları, anılan veri ve sistemleri, çelişkileri ve açık soruları kaynağına bağlı olarak çıkarır. Bir veya daha fazla gereksinim görüşmesinden sonra, notlar dağınıksa veya 'bu görüşmelerden ne öğrendik?' sorusu geldiğinde kullanılır.
- Örnek istek: _"Üç borç muhasebesi uzmanıyla yaptığım görüşmelerin notları burada. İhtiyaçları, sorunları, kuralları ve çelişkileri çıkar."_
- İlgili: `interview-question-set`, `business-rules-catalog`, `requirements-consistency-check`, `feedback-synthesis`, `open-questions-tracker`
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.tr.md)

**Gereksinim çalıştayı planlama** · `workshop-plan`

- Ne zaman: Bir gereksinim çalıştayı tasarlar: hedefler, katılımcılar ve roller, ön hazırlık, süreleri belli gereksinim toplama aktiviteleri (ör. süreç yürüyüşü, story mapping, kural/istisna turu, önceliklendirme), materyaller, karar kuralları ve beklenen çıktılar; yerinde veya uzaktan formatlar için. Birden çok paydaşın gereksinimler üzerinde uzlaşması veya birlikte üretmesi gerektiğinde ya da 'şunun için bir çalıştay planla' denildiğinde kullanılır.
- Örnek istek: _"Otomatik kredi limiti kontrolü gereksinimlerini tanımlamak için finans, satış operasyon ve BT ile yarım günlük uzaktan bir çalıştay planla."_
- İlgili: `facilitation-guide`, `meeting-agenda`, `interview-question-set`, `story-mapping`, `discovery-workshop`
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.tr.md)

**Anket tasarlama** · `questionnaire-design`

- Ne zaman: Geniş veya dağınık bir kitle için yanlılıksız bir gereksinim anketi tasarlar: bilgi hedefleri, hedef kitle, yönlendirici veya çift konulu olmayan soru tipleri ve ifadeleri, dallanma mantığı, pilot planı, aydınlatma metni ve analiz planı. Çok sayıda kullanıcıya veya lokasyona aynı sorular sorulacaksa ya da 'gereksinim toplamak için bir anket hazırla' dendiğinde kullanılır.
- Örnek istek: _"Mevcut kredi başvuru ekranında en çok zaman alan adımları bulmak için 400 şube çalışanına yönelik bir anket tasarla."_
- İlgili: `interview-question-set`, `screener-survey`, `feedback-synthesis`, `research-plan`, `data-classification`
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.tr.md)

**Mevcut dokümanlardan gereksinim çıkarma** · `document-analysis`

- Ne zaman: Şartname, kullanım kılavuzu, prosedür, sözleşme, mevzuat, form ve rapor gibi mevcut dokümanlardan gereksinim çıkarır; kaynağa izlenebilen aday gereksinimler, iş kuralları, veri öğeleri ve çelişkiler listesi üretir. Eski sistem dokümanları, bir mevzuat veya sözleşme görüşmelerden önce taranacaksa ya da 'bu dokümanlardan hangi gereksinimleri çıkarabiliriz?' diye sorulduğunda kullanılır.
- Örnek istek: _"Mevcut hasar sistemimizin 20 sayfalık operasyon kılavuzundan ve yeni yönetmelik metninden gereksinimleri çıkar, nerede çeliştiklerini göster."_
- İlgili: `business-rules-catalog`, `interview-question-set`, `requirements-consistency-check`, `traceability-matrix`, `glossary-builder`
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.tr.md)

**Gözlem notlarını yapılandırma** · `observation-notes`

- Ne zaman: Ham iş gölgeleme (job shadowing) veya bağlamsal gözlem notlarını süreleri, kullanılan araçları, sorunları, geçici çözümleri, kesintileri ve yazılı süreç ile gerçek süreç arasındaki farkı gösteren bir görev dizisine dönüştürür. Kullanıcılar işbaşında gözlemlendikten sonra, saha notları dağınık olduğunda veya 'ekibi izlerken ne öğrendik?' diye sorulduğunda kullanılır.
- Örnek istek: _"İki çağrı merkezi temsilcisini üç saat gölgelediğim notlar bunlar. Görev, sorun ve geçici çözümler olarak yapılandır."_
- İlgili: `as-is-process`, `interview-notes-analysis`, `value-stream-map`, `customer-journey-map`, `research-synthesis`
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.tr.md)

**Etkileşimli gereksinim görüşmesi** · `requirements-interview`

- Ne zaman: Kullanıcıyla her seferinde tek soru sorarak ve her soruyu önceki cevaba göre uyarlayarak (teşhis et, daralt, teyit et) görüşme yapar; güncel bir spesifikasyonu görünür tutar, hazır olma kontrol listesi karşılandığında durur ve yapılandırılmış bir gereksinim özetiyle bitirir. Bir ihtiyaç belirsiz olduğunda (\"bir dashboard lazım\", \"onayları otomatikleştirelim\"), kullanıcı \"bana soru sor\", \"bunu netleştirmeme yardım et\" dediğinde veya zayıf bir girdiden story ya da PRD yazılmadan önce kullanılır.
- Örnek istek: _"Geliştirilebilecek netliğe gelene kadar benimle görüş: tedarikçilerin faturalarını e-postayla göndermek yerine kendilerinin yüklemesini istiyoruz."_
- İlgili: `request-clarification-questions`, `requirements-gap-analysis`, `user-story`, `acceptance-criteria`, `edge-case-elicitation`
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/requirements-interview/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/requirements-interview/SKILL.tr.md)

#### Gereksinim Dokümantasyonu

**İş Gereksinimleri Dokümanı (BRD) yazma** · `brd-writing`

- Ne zaman: İş problemini, ölçülebilir başarı kriterli hedefleri, kapsamı, paydaşları, üst düzey iş gereksinimlerini, iş kurallarını, kısıtları, varsayımları ve riskleri herhangi bir çözüm tasarımından bağımsız olarak ortaya koyan bir İş Gereksinimleri Dokümanı (BRD) yazar. Bir girişimin çözüm veya fonksiyonel tasarımdan önce uzlaşılmış bir iş temeline ihtiyacı olduğunda ya da bir proje veya değişiklik için 'BRD yaz' dendiğinde kullanılır.
- Örnek istek: _"Manuel tedarikçi kaydını (e-posta ve Excel) self-servis bir süreçle değiştirmek için BRD yaz; çalıştay notları ekte."_
- İlgili: `request-intake-document`, `frd-writing`, `stakeholder-identification`, `requirements-review-checklist`, `requirements-sign-off`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.tr.md)

**Fonksiyonel Gereksinim Dokümanı (FRD) yazma** · `frd-writing`

- Ne zaman: Sistem davranışını fonksiyon bazında tanımlayan bir Fonksiyonel Gereksinim Dokümanı (FRD) yazar: aktörler ve yetkiler, tetikleyiciler, doğrulamalarıyla girdiler, işleme ve iş kuralları, çıktılar, durumlar, hata yönetimi ve arayüzler; her gereksinim benzersiz ID'li, test edilebilir ve bir iş ihtiyacına izlenebilir. İş gereksinimleri uzlaşılmışsa ve geliştirme ekibi veya tedarikçi belirsizlik içermeyen bir davranış tanımına ihtiyaç duyuyorsa ya da 'FRD yaz' dendiğinde kullanılır.
- Örnek istek: _"Bu BRD'ye dayanarak tedarikçi self-servis kayıt ve doküman doğrulama fonksiyonları için FRD yaz."_
- İlgili: `brd-writing`, `use-case-spec`, `business-rules-catalog`, `nfr-specification`, `traceability-matrix`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.tr.md)

**Kullanıcı hikayesi yazma** · `user-story`

- Ne zaman: Kullanıcı hikayelerini somut bir persona, gerçek bir sonuç, bağlam, iş kuralları, bağımlılıklar ve kabul kriteri başlıklarıyla \\\"... olarak ... istiyorum ki ...\\\" kalıbında yazar; aslında teknik görev olan veya bölünmesi gereken maddeleri işaretler. Bir ihtiyaç, gereksinim veya özelliğin backlog maddelerine dönüşmesi gerektiğinde ya da 'hikaye yaz', 'bunu user story'ye çevir' veya zayıf hikayeleri yeniden yaz dendiğinde kullanılır.
- Örnek istek: _"Mağaza müdürlerinin personel vardiya değişimlerini telefondan onaylayabilmesi için kullanıcı hikayeleri yaz."_
- İlgili: `acceptance-criteria`, `invest-check`, `story-splitting`, `persona`, `epic-breakdown`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.tr.md)

**Kabul kriteri yazma** · `acceptance-criteria`

- Ne zaman: Bir kullanıcı hikayesi veya gereksinim için Given/When/Then senaryoları ya da kural biçiminde test edilebilir kabul kriterleri yazar; mutlu yolu, iş kuralı varyasyonlarını, doğrulamayı, yetkileri ve hata durumlarını senaryo başına tek tetikleyici ve tek sonuçla kapsar. Bir hikayenin tamamlanma koşulları gerektiğinde, kriterler muğlak veya test edilemez olduğunda ya da 'kabul kriteri', 'AC', 'Gherkin' veya 'Given/When/Then' istendiğinde kullanılır.
- Örnek istek: _"Şu hikaye için kabul kriterleri yaz: Mağaza müdürü olarak bekleyen bir vardiya değişimini telefonumdan onaylamak veya reddetmek istiyorum."_
- İlgili: `user-story`, `invest-check`, `edge-case-elicitation`, `bdd-feature-file`, `test-scenarios-from-requirements`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.tr.md)

**Kullanım senaryosu (use case) yazma** · `use-case-spec`

- Ne zaman: Hedef, birincil ve destekleyici aktörler, paydaş çıkarları, tetikleyici, ön koşullar, asgari ve başarı garantileri, numaralı ana başarı senaryosu ve ayrıldıkları adıma bağlı alternatif ve istisna akışlarıyla bir kullanım senaryosu (use case) tanımı yazar. Bir etkileşimin çok dalı, birden fazla aktörü veya sistemden sisteme adımları olduğunda ya da 'use case', 'UC tanımı' veya 'ayrıntılı kullanım senaryosu' istendiğinde kullanılır.
- Örnek istek: _"Kartla iadeler ve fişi olmayan durumlarla birlikte 'Satın alınan ürünü mağazada iade etme' kullanım senaryosunu yaz."_
- İlgili: `frd-writing`, `user-story`, `business-rules-catalog`, `error-scenario-catalog`, `sequence-flow`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.tr.md)

**Fonksiyonel olmayan gereksinimleri tanımlama** · `nfr-specification`

- Ne zaman: Fonksiyonel olmayan gereksinimleri kalite karakteristikleri (performans, erişilebilirlik/kesintisizlik, güvenilirlik, güvenlik, mahremiyet, kullanılabilirlik, erişilebilirlik, bakım yapılabilirlik, uyumluluk, taşınabilirlik, işletilebilirlik, mevzuat uyumu) boyunca; her biri metrik, hedef, ölçüm koşulu, doğrulama yöntemi ve kaynakla ölçülebilir ifadeler olarak tanımlar. Kalite beklentileri muğlak olduğunda ('hızlı', 'güvenli', '7/24'), BRD veya FRD'de NFR eksik olduğunda ya da 'NFR tanımla' dendiğinde kullanılır.
- Örnek istek: _"Yeni müşteri self-servis portalımız için NFR'leri tanımla; iş birimi sadece hızlı, güvenli ve her zaman açık olmalı dedi."_
- İlgili: `frd-writing`, `nfr-to-architecture`, `slo-definition`, `security-requirements`, `performance-test-plan`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.tr.md)

**İş kuralları kataloğu** · `business-rules-catalog`

- Ne zaman: Doküman, not, gereksinim veya kod tariflerinden iş kurallarını çıkarır ve ID, kural tipi (kısıt, hesaplama, çıkarım, aksiyon tetikleyici, olgu), atomik ve bildirimsel ifade, kaynak, sahip, geçerlilik tarihleri, istisnalar ve kuralı kullanan gereksinimlerle bir katalogda standartlaştırır. Kurallar dağınık veya süreç ve ekranlara gömülü olduğunda, kaynaklar arasında çeliştiğinde ya da 'iş kurallarını listele' veya kural kitabı oluştur dendiğinde kullanılır.
- Örnek istek: _"Bu kredi başvurusu prosedür notlarındaki iş kurallarını çıkar ve bir katalogda standartlaştır."_
- İlgili: `document-analysis`, `decision-table-testing`, `requirements-consistency-check`, `frd-writing`, `glossary-builder`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.tr.md)

**Veri gereksinimlerini tanımlama** · `data-requirements`

- Ne zaman: Veri gereksinimlerini iş bakış açısıyla tanımlar: varlıklar ve ilişkileri; anlamı, tipi, formatı, zorunluluk kuralı, doğrulamaları ve izin verilen değerleriyle nitelikler; tanımlayıcılar, veri sahipliği, kaynaklar ve tüketiciler, hassasiyet sınıfı, kalite beklentileri, saklama ve silme. Bir özellik veya sistem veri oluşturduğunda ya da değiştirdiğinde, geliştirme veya taşıma için veri sözlüğü gerektiğinde ya da 'veriyi tanımla', 'hangi alanlar lazım' dendiğinde kullanılır.
- Örnek istek: _"Tedarikçi kayıt özelliği için veri gereksinimlerini tanımla: tedarikçi, iletişim kişileri, banka bilgileri ve dokümanlar."_
- İlgili: `conceptual-data-model`, `data-classification`, `data-quality-rules`, `retention-policy`, `frd-writing`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.tr.md)

**Rapor gereksinimi tanımlama** · `report-requirements`

- Ne zaman: Rapor gereksinimlerini raporun desteklediği karardan başlayarak tanımlar: hedef kitle, cevaplanan sorular, kesin hesaplaması ve granülerliğiyle alanlar ve ölçüler, boyutlar, filtreler ve parametreler, sıralama ve gruplama, veri kaynakları ve güncellik, erişim ve maskeleme, teslim ve format, mutabakat rakamına karşı kabul kontrolleri. Biri yeni bir rapor, dışa aktarım veya liste istediğinde, mevcut bir raporun rakamları tartışmalı olduğunda ya da 'rapor gereksinimi yaz' dendiğinde kullanılır.
- Örnek istek: _"Finans'ın istediği, müşteri segmenti ve yaşlandırma dilimine göre aylık vadesi geçmiş alacaklar raporunun gereksinimlerini yaz."_
- İlgili: `dashboard-spec`, `metric-definition`, `data-requirements`, `kpi-definition`, `request-intake-document`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.tr.md)

**Ekran gereksinimi tanımlama** · `screen-requirements`

- Ne zaman: Ekran veya UI gereksinimlerini ekran bazında, görsel tasarımı dayatmadan tanımlar: amaç ve giriş noktaları, roller ve yetkiler; kaynağı, formatı, zorunluluk kuralı, varsayılanı ve mesaj davranışlı doğrulamalarıyla alanlar; aksiyonlar ve sonuçları; ekran durumları (boş, yükleniyor, hata, salt okunur, yetkisiz), gezinme, erişilebilirlik ve duyarlı tasarım ihtiyaçları. Tasarım ve geliştirme için bir ekran, form veya sayfanın tanımlanması gerektiğinde ya da 'bu ekran ne yapmalı' sorulduğunda kullanılır.
- Örnek istek: _"Çağrı merkezi uygulamasındaki 'Müşteri adresini düzenle' formu için ekran gereksinimlerini yaz."_
- İlgili: `wireframe-spec`, `error-message-writing`, `frd-writing`, `data-requirements`, `accessibility-audit`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.tr.md)

**Entegrasyon gereksinimi tanımlama** · `integration-requirements`

- Ne zaman: Sistemler arası entegrasyon gereksinimlerini; katılan sistemleri, yönü, aktarılan veriyi, tetikleyiciyi ve sıklığı, hacimleri, hata yönetimini, güvenliği ve SLA'ları iki tarafın da geliştirip test edebileceği biçimde tanımlar. Bir özelliğin başka bir sisteme veri göndermesi veya oradan veri alması gerektiğinde, yeni bir arayüz ya da API talep edildiğinde veya tasarımdan önce bir tedarikçi/üçüncü taraf entegrasyonu üzerinde anlaşılması gerektiğinde kullanılır.
- Örnek istek: _"E-ticaret platformumuzdan onaylanan siparişlerin ERP'ye gönderilmesi ve stok seviyelerinin geri alınması için entegrasyon gereksinimlerini tanımla."_
- İlgili: `field-mapping`, `error-scenario-catalog`, `api-contract`, `integration-pattern-selection`, `data-requirements`
- Dosya: [skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.tr.md)

#### Gereksinim Kalitesi

**Gereksinimlerde eksik bulma** · `requirements-gap-analysis`

- Ne zaman: Bir gereksinim setini (BRD, FRD, kullanıcı hikayeleri, use case'ler) inceler ve eksikleri tespit eder: akışlar, aktörler ve roller, uç durumlar, hata yönetimi, veri kuralları, fonksiyonel olmayan gereksinimler ve geçiş ihtiyaçları. Gereksinimler tamam görünse de sınanmamışsa, tahmin veya onaydan önce ya da 'neyi atlıyoruz?' sorusu sorulduğunda kullanılır.
- Örnek istek: _"Kredi başvuru modülünün FRD'si ekte. Tahmine göndermeden önce eksikleri bul."_
- İlgili: `ambiguity-detection`, `requirements-consistency-check`, `requirements-review-checklist`, `nfr-specification`, `error-scenario-catalog`
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.tr.md)

**Belirsiz gereksinim tespiti** · `ambiguity-detection`

- Ne zaman: Gereksinim metnini muğlak sözcükler, tanımsız terimler, zayıf veya öznel ifadeler, sınırsız listeler, aktörü belirsiz edilgen cümleler ve test edilemez ifadeler açısından tarar; net yeniden yazımlar önerir. Gereksinimler, kullanıcı hikayeleri veya kabul kriterleri netlik açısından incelenirken ya da testçiler veya geliştiriciler bir gereksinimin birden fazla şekilde okunabildiğini söylediğinde kullanılır.
- Örnek istek: _"Bu 20 gereksinimi belirsiz ifadeler açısından kontrol et ve test edilebilir yeniden yazımlar öner."_
- İlgili: `requirements-gap-analysis`, `requirements-consistency-check`, `glossary-builder`, `acceptance-criteria`, `testability-review`
- Dosya: [skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.tr.md)

**Uç durumları ortaya çıkarma** · `edge-case-elicitation`

- Ne zaman: Bir özellik, akış, API veya gereksinim için sınırlar, boş/null, mükerrer kayıtlar, eşzamanlılık, saat dilimleri ve tarihler, yetkiler, kısmi hata, yeniden deneme ve idempotency, hacim ve kötüye kullanım başlıklarında uç durumları sistematik olarak ortaya çıkarır; her birini beklenen davranışa veya açık soruya dönüştürür. Bir story, spesifikasyon veya tasarım yalnızca mutlu yolu anlatıyorsa, kabul kriteri veya test tasarımından önce ya da \"ne ters gidebilir?\", \"hangi durumları atlıyoruz?\" sorulduğunda kullanılır.
- Örnek istek: _"Bu story için uç durumları bul: depo görevlisi olarak müşteri siparişi için stok ayırmak istiyorum, böylece ürünler iki kez satılmaz."_
- İlgili: `acceptance-criteria`, `error-scenario-catalog`, `equivalence-boundary-analysis`, `requirements-gap-analysis`, `test-scenarios-from-requirements`
- Dosya: [skills/01-business-analysis/business-analyst/quality/edge-case-elicitation/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/edge-case-elicitation/SKILL.tr.md)

**Gereksinim tutarlılık kontrolü** · `requirements-consistency-check`

- Ne zaman: Gereksinimleri birbirleriyle ve iş kuralları, sözlük, veri ve NFR'lerle karşılaştırarak çelişkileri, tekrarları, örtüşmeleri, tutarsız terimleri ve çatışan değerleri bulur; her biri için bir çözüm yolu önerir. Aynı kapsamı birden fazla doküman, yazar veya sürüm tarif ettiğinde, farklı ekiplerin hikayeleri birleştirildiğinde ya da gereksinimler temel sürüme (baseline) alınmadan önce kullanılır.
- Örnek istek: _"Aynı faturalama kapsamı için bir BRD, bir FRD ve 45 kullanıcı hikayemiz var. Çelişkileri ve tekrarları bul."_
- İlgili: `ambiguity-detection`, `requirements-gap-analysis`, `business-rules-catalog`, `glossary-builder`, `traceability-matrix`
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.tr.md)

**INVEST kontrolü** · `invest-check`

- Ne zaman: Kullanıcı hikayelerini INVEST kriterlerine (Bağımsız, Tartışılabilir, Değerli, Tahmin Edilebilir, Küçük, Test Edilebilir) göre değerlendirir, her kriteri kanıtıyla puanlar ve bölme, yeniden yazma veya eksik kabul kriteri gibi somut düzeltmeler önerir. Backlog iyileştirmesi sırasında, hikayeler bir iterasyona veya taahhüde girmeden önce ya da bir hikaye sürekli yeniden tahmin edilip devrediliyorsa kullanılır.
- Örnek istek: _"Ödeme epiğindeki bu 8 hikayeye INVEST kontrolü yap, hangileri hazır değil söyle."_
- İlgili: `user-story`, `acceptance-criteria`, `story-splitting`, `definition-of-ready`, `backlog-refinement`
- Dosya: [skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.tr.md)

**İzlenebilirlik matrisi** · `traceability-matrix`

- Ne zaman: İş hedeflerini ve kaynakları gereksinimlere, tasarım öğelerine, test senaryolarına ve sürümlere iki yönlü bağlayan bir gereksinim izlenebilirlik matrisi oluşturur; sahipsiz öğeleri, karşılanmamış gereksinimleri ve kapsam yüzdelerini raporlar. Denetim, düzenleyici kurum veya müşteri kapsam kanıtı istediğinde, sürüm veya UAT öncesinde ya da bir değişikliğin etkilediği öğeler araştırılırken kullanılır.
- Örnek istek: _"Bu 30 gereksinim ve 55 test senaryosundan izlenebilirlik matrisi oluştur, nelerin karşılanmadığını göster."_
- İlgili: `requirements-gap-analysis`, `impact-analysis`, `test-scenarios-from-requirements`, `requirements-sign-off`, `release-quality-gate`
- Dosya: [skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.tr.md)

**Gereksinim önceliklendirme** · `requirements-prioritization`

- Ne zaman: Bir gereksinim setini uygun bir teknikle (MoSCoW, Kano, değer/efor, ağırlıklı puanlama veya gecikme maliyeti) önceliklendirir, kriterleri açıkça ortaya koyar ve her sıralamayı kanıt ve belirtilen varsayımlarla gerekçelendirir. Kapsamın bir tarihe veya bütçeye sığdırılması gerektiğinde, paydaşlar neyin önce geleceği konusunda anlaşamadığında ya da bir sürüm veya MVP kapsamı için savunulabilir bir sıra gerektiğinde kullanılır.
- Örnek istek: _"İlk sürüm için bu 25 gereksinimi MoSCoW ile önceliklendir; canlıya geçiş tarihimiz sabit."_
- İlgili: `backlog-prioritization`, `decision-matrix`, `mvp-scoping`, `stakeholder-map`, `requirements-sign-off`
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.tr.md)

**Gereksinim gözden geçirme** · `requirements-review-checklist`

- Ne zaman: Bir gereksinim dokümanını veya hikaye setini onaydan önce kontrol listesine dayalı, yapılandırılmış bir incelemeden geçirir: yapı, tekil gereksinim kalitesi (ISO/IEC/IEEE 29148 özellikleri), set düzeyinde bütünlük ve tutarlılık, NFR'ler, izlenebilirlik ve onaya hazırlık. Bulguları ve geçer/geçmez önerisini döndürür. Bir BRD, FRD, SRS veya backlog dilimi temel sürüme alınmadan, tedarikçiye verilmeden veya onaylanmadan önce kullanılır.
- Örnek istek: _"Bu FRD'yi iş birimine onaya göndermeden önce incele. Düzgün bir kontrol listesi kullan ve hazır olup olmadığını söyle."_
- İlgili: `ambiguity-detection`, `requirements-gap-analysis`, `requirements-consistency-check`, `requirements-sign-off`, `document-review`
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.tr.md)

#### Süreç Analizi

**Mevcut süreci (as-is) belgeleme** · `as-is-process`

- Ne zaman: Mevcut (as-is) iş sürecini görüşme ve gözlem notları, prosedürler veya sistem kayıtlarından belgeler: tetikleyici, adımlar, aktörler, sistemler, girdi/çıktılar, karar noktaları, süreler, hacimler, sorunlar ve geçici çözümler. Bir süreç iyileştirilecek, otomatikleştirilecek veya değiştirilecekse ve ekibin önce işin bugün gerçekte nasıl yapıldığına dair ortak, kanıta dayalı bir resme ihtiyacı varsa kullanılır.
- Örnek istek: _"Muhasebe ve iki departman yöneticisiyle yapılan görüşme notlarından tedarikçi fatura onayı için mevcut süreci belgele."_
- İlgili: `to-be-process`, `bpmn-model`, `value-stream-map`, `observation-notes`, `interview-notes-analysis`
- Dosya: [skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.tr.md)

**Hedef süreci (to-be) tasarlama** · `to-be-process`

- Ne zaman: Mevcut süreç tarifi, sorunlar ve hedeflerden iyileştirilmiş (to-be) bir iş süreci tasarlar: yeniden tasarım kaldıraçlarını (kaldır, sadeleştir, otomatikleştir, paralelleştir, kararı taşı, kontrol ekle) uygular, her değişikliği as-is'e göre gösterir, beklenen etkileri, varsayımları ve gereken sağlayıcıları belirtir. Bir süreç iyileştirilecek, dijitalleştirilecek veya yeniden yapılandırılacaksa ve gereksinim ya da sistem tasarımından önce hedef çalışma biçiminde uzlaşılması gerekiyorsa kullanılır.
- Örnek istek: _"Bu mevcut fatura onay süreci ve sorunlarından yola çıkarak onay süresini yarıya indiren bir hedef süreç tasarla."_
- İlgili: `as-is-process`, `process-gap-analysis`, `bpmn-model`, `value-stream-map`, `business-rules-catalog`
- Dosya: [skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.tr.md)

**BPMN süreç modeli** · `bpmn-model`

- Ne zaman: Bir süreç tarifini BPMN 2.0 modeline dönüştürür: havuzlar ve kulvarlar, olaylar, görevler, geçitler, mesaj akışları ve veri nesneleri; çıktıyı yapılandırılmış bir öğe listesi ile çizilebilir veya içe aktarılabilir diyagram kodu olarak verir. Bir sürecin biçimsel olarak çizilmesi gerektiğinde, metin olarak yazılmış bir as-is veya to-be süreç diyagrama çevrilecekse ya da BPMN, kulvar diyagramı veya süreç diyagramı kodu istendiğinde kullanılır.
- Örnek istek: _"Bu satın alma onay sürecini BPMN ile modelle: çalışan talep girer, yönetici 10 bine kadar onaylar, üstünde finans da onaylar, sonra satın alma sipariş verir."_
- İlgili: `as-is-process`, `to-be-process`, `diagram-as-code`, `business-rules-catalog`, `use-case-spec`
- Dosya: [skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.tr.md)

**As-is/to-be fark analizi** · `process-gap-analysis`

- Ne zaman: Mevcut (as-is) süreci hedef (to-be) süreçle adım adım karşılaştırır; her farkı insan, süreç, teknoloji, veri veya politika boyutunda gereken bir değişiklik olarak, etkisi, bağımlılıkları ve sorumlusuyla listeler. Hedef süreç tasarlandıktan sonra oraya ulaşmak için değişiklik listesi, iş paketleri veya geçiş planı gerektiğinde ya da 'as-is'ten to-be'ye geçmek için ne değişmeli?' sorulduğunda kullanılır.
- Örnek istek: _"Fatura onay sürecimizin as-is ve to-be hallerini paylaşıyorum. Fark analizini ve nelerin değişmesi gerektiğini çıkar."_
- İlgili: `as-is-process`, `to-be-process`, `impact-analysis`, `fit-gap-analysis`, `raci-matrix`
- Dosya: [skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.tr.md)

**Değer akışı haritalama** · `value-stream-map`

- Ne zaman: Müşteri talebinden teslim edilen değere kadar bir değer akışını haritalar; her adımda işlem süresini bekleme süresinden ayırır, adımları değer katan, gerekli ama değer katmayan veya israf olarak sınıflandırır ve toplam süre (lead time), işlem süresi, akış verimliliği ve yeniden işleme oranlarını hesaplar. Bir süreç veya teslimat akışı yavaş geldiğinde, toplam sürenin kısaltılması gerektiğinde ya da israfın, beklemenin veya darboğazın nerede olduğu sorulduğunda kullanılır.
- Örnek istek: _"Müşteri kazanım sürecimizin değer akışını çıkar: başvurudan aktif hesaba yaklaşık 12 gün sürüyor, zamanın nereye gittiğini görmek istiyoruz."_
- İlgili: `as-is-process`, `to-be-process`, `cycle-time-analysis`, `five-whys`, `process-gap-analysis`
- Dosya: [skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.tr.md)

#### Çözüm Değerlendirme

**Fizibilite değerlendirmesi** · `feasibility-study`

- Ne zaman: Önerilen bir girişimin veya çözüm seçeneğinin teknik, operasyonel, ekonomik, zaman, yasal/uyum ve organizasyonel açıdan yapılabilir olup olmadığını değerlendirir; her boyutu kanıtla puanlar, koşulları ve engelleyicileri adlandırır, devam, koşullu devam veya durdurma önerir. Bir fikir veya talep yatırım öncesi değerlendirilecekse, çözüm seçenekleri üst düzeyde karşılaştırılacaksa ya da 'bunu gerçekten yapabilir miyiz?' diye sorulduğunda kullanılır.
- Örnek istek: _"Şirket içi CRM'imizi 6 ay içinde bir SaaS CRM ile değiştirmenin fizibilitesini değerlendir; 2 geliştiricimiz var ve KVKK gereksinimlerimiz sıkı."_
- İlgili: `cost-benefit-analysis`, `build-vs-buy`, `pre-mortem`, `risk-register`, `technology-selection`
- Dosya: [skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.tr.md)

**Maliyet-fayda analizi** · `cost-benefit-analysis`

- Ne zaman: Bir girişimin veya rakip seçeneklerin maliyet ve faydalarını belirli bir dönem boyunca sayısallaştırır; tek seferlik ve tekrarlayan kalemleri, somut ve soyut faydaları ayırır; net faydayı, ROI'yi, geri dönüş süresini ve istenirse NPV'yi temel varsayımlara duyarlılık analiziyle hesaplar. Bir iş gerekçesi, yatırım kararı veya seçenek karşılaştırması rakam gerektirdiğinde ya da 'değer mi?' veya 'ROI ne?' diye sorulduğunda kullanılır.
- Örnek istek: _"Fatura eşleştirme otomasyonu için maliyet-fayda analizi yap: lisans yıllık 40 bin, uygulama 120 bin, 3 FTE'lik manuel işi azaltması bekleniyor."_
- İlgili: `feasibility-study`, `budget-proposal`, `cloud-cost-estimate`, `benefits-realization`, `decision-matrix`
- Dosya: [skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.tr.md)

**Etki analizi** · `impact-analysis`

- Ne zaman: Önerilen bir değişikliğin süreçler, sistemler, arayüzler, veri, raporlar, kullanıcılar, dokümanlar, kontroller ve testler üzerindeki etkisini doğrudan ve dolaylı bağımlılıkları izleyerek analiz eder; her etkiyi kanıt ve güven düzeyiyle puanlar. Yeni bir gereksinim, değişiklik talebi, kural değişikliği veya sistem değişikliği önerildiğinde ve ekibin tahmin, onay veya yayın öncesinde başka neyin etkilendiğini bilmesi gerektiğinde kullanılır.
- Örnek istek: _"Ana bankacılık sistemimizde müşteri numarasını sayısaldan alfanümeriğe çevirmenin etkisi ne olur?"_
- İlgili: `change-request-analysis`, `traceability-matrix`, `process-gap-analysis`, `regression-selection`, `dependency-map`
- Dosya: [skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.tr.md)

**Değişiklik talebi analizi** · `change-request-analysis`

- Ne zaman: Bir değişiklik talebini üzerinde anlaşılmış temel sürüme (baseline) göre analiz eder: talebi sınıflandırır (yeni kapsam, değişiklik, netleştirme, kılık değiştirmiş hata), değer, kapsam, efor sürücüleri, zaman, maliyet ve risk etkisini değerlendirir, seçenekleri listeler ve değişiklik otoritesi için gerekçeli kabul, ödünleşimli kabul, erteleme veya ret önerir. Gereksinimler onaylandıktan sonra veya teslimat sırasında bir paydaş ekleme ya da değişiklik istediğinde veya bir değişiklik kontrol kurulu karar dokümanı beklediğinde kullanılır.
- Örnek istek: _"Pazarlama, canlıya geçişe iki hafta kala sadakat sürümüne SMS bildirimi eklemek istiyor. Değişiklik talebini analiz et ve öneri ver."_
- İlgili: `impact-analysis`, `change-control`, `change-request-rfc`, `requirements-sign-off`, `trade-off-analysis`
- Dosya: [skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.tr.md)

**Gereksinim onayı hazırlama** · `requirements-sign-off`

- Ne zaman: Gereksinim onay paketini hazırlar: onaylanan temel sürüm (dokümanlar, sürümler, gereksinim ID'leri), son incelemeden bu yana değişenler, açık konular ve kabul edilen riskler, koşullar, gereken onaycılar ve sonraki değişikliklerin nasıl kontrol edileceği. Gereksinimler incelenip temel sürüme bağlanmaya hazır olduğunda, sponsor 'tam olarak neyi imzalıyorum?' diye sorduğunda ya da tasarım, geliştirme veya bir sözleşme kilometre taşı başlamadan önce kullanılır.
- Örnek istek: _"Hasar portalı FRD v1.3 için onay paketini hazırla; iş sahibi ve BT lideri bu hafta onaylayabilsin."_
- İlgili: `requirements-review-checklist`, `traceability-matrix`, `change-control`, `change-request-analysis`, `decision-log`
- Dosya: [skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.tr.md)

### Sistem Analisti

#### Sistem Tanımı

**Yazılım Gereksinim Şartnamesi (SRS) yazma** · `srs-writing`

- Ne zaman: ISO/IEC/IEEE 29148 ile uyumlu bir Yazılım Gereksinim Şartnamesi (SRS) yazar: amaç ve kapsam, sistem bağlamı ve arayüzler, fonksiyonel gereksinimler, kalite nitelikleri, veri, kısıtlar ve her gereksinim için doğrulama yöntemi; her gereksinim tekil ID'li ve izlenebilirdir. Bir sistem veya alt sistemin tasarım, geliştirme, tedarikçi ya da denetim için tanımlanması gerektiğinde veya iş gereksinimlerinin doğrulanabilir bir sistem şartnamesine dönüştürülmesi gerektiğinde kullanılır.
- Örnek istek: _"Bu FRD ve arayüz listesine göre ödeme mutabakat servisi için bir SRS yaz."_
- İlgili: `frd-writing`, `nfr-specification`, `use-case-spec`, `integration-requirements`, `traceability-matrix`
- Dosya: [skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.tr.md)

**Durum modeli çıkarma** · `state-model`

- Ne zaman: Bir iş varlığının (sipariş, başvuru, hasar dosyası, sözleşme, kayıt) yaşam döngüsünü modeller: durumlar, geçişler, tetikleyici olaylar, koşullar (guard), eylemler, her geçişi kimin tetikleyebileceği ve geçersiz geçişler; çıktı bir geçiş tablosu ve diyagram kodudur. Bir varlığın davranışı belirleyen durumları olduğunda, durum kuralları dağınık veya tartışmalı olduğunda ya da iş akışı, API veya durum geçiş testleri tasarlanmadan önce kullanılır.
- Örnek istek: _"Bir sigorta hasar dosyasının başvurudan ödemeye veya redde kadar durumlarını, yeniden açma ve iptal dahil modelle."_
- İlgili: `business-rules-catalog`, `state-transition-testing`, `sequence-flow`, `error-scenario-catalog`, `diagram-as-code`
- Dosya: [skills/01-business-analysis/system-analyst/specification/state-model/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/state-model/SKILL.tr.md)

**Sistem etkileşim akışı** · `sequence-flow`

- Ne zaman: Uçtan uca tek bir senaryoda sistemlerin, servislerin ve aktörlerin nasıl etkileştiğini tarif eder: katılımcılar, sıralı mesajlar, senkron veya asenkron yapı, temel yük alanları, yanıtlar, zaman aşımları, yeniden denemeler ve alternatif ya da hata yolları; çıktı bir adım tablosu ve sıralama diyagramı kodudur. Bir senaryo birden çok sistemi kestiğinde, entegrasyon davranışı ekipler arasında netleştirilmesi gerektiğinde ya da 'ne neyi, hangi sırayla çağırıyor, hata olursa ne oluyor?' sorusu sorulduğunda kullanılır.
- Örnek istek: _"Online sipariş için akışı tarif et: web mağaza, sipariş servisi, ödeme geçidi, stok servisi ve bildirim; ödeme zaman aşımı dahil."_
- İlgili: `integration-requirements`, `api-contract`, `error-scenario-catalog`, `state-model`, `diagram-as-code`
- Dosya: [skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.tr.md)

**Sistemler arası alan eşleme** · `field-mapping`

- Ne zaman: İki sistem veya mesaj arasında kaynak-hedef alan eşlemesi üretir: her hedef alan için kaynak, dönüşüm, varsayılan değer, doğrulama, kod değeri çevirisi, boş ve hatalı değer yönetimi; ayrıca iki taraftaki eşlenmeyen alanlar ve açık kararlar. Bir entegrasyon, API adaptörü, veri değişim dosyası veya sistem değişimi yapılırken, iki sistemin kayıt alışverişi gerektiğinde ya da 'hangi alan nereye gidiyor, nasıl dönüştürülüyor?' sorusu sorulduğunda kullanılır.
- Örnek istek: _"CRM dışa aktarımındaki müşteri alanlarını yeni faturalama sisteminin müşteri API'sine kod dönüşümleri dahil eşle."_
- İlgili: `integration-requirements`, `api-contract`, `source-to-target-mapping`, `data-quality-rules`, `error-scenario-catalog`
- Dosya: [skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.tr.md)

**Hata senaryoları kataloğu** · `error-scenario-catalog`

- Ne zaman: Bir özellik, akış veya arayüz için hata senaryoları kataloğu oluşturur: her hata durumu için tetikleyici, tespit noktası, beklenen sistem davranışı, sonrasındaki veri durumu, kullanıcıya veya çağırana dönen mesaj, hata kodu, loglama ve alarm ile kurtarma yolu. Gereksinimler yalnızca mutlu yolu anlattığında, bir entegrasyon veya işlem akışı tasarlanıp test edilmeden önce ya da destek ekibi ile geliştiriciler bir şey başarısız olduğunda sistemin ne yapması gerektiği konusunda anlaşamadığında kullanılır.
- Örnek istek: _"Para transferi akışımız için hata senaryoları kataloğu oluştur: doğrulama, limitler, core banking zaman aşımı ve tekrarlanan gönderimler."_
- İlgili: `error-message-writing`, `edge-case-elicitation`, `sequence-flow`, `resilience-review`, `test-case-writing`
- Dosya: [skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.tr.md)

## Ürün Yönetimi

### Ürün Yöneticisi

#### Ürün Stratejisi

**Ürün vizyonu yazma** · `product-vision`

- Ne zaman: Hedef kitle, ihtiyaçlar, ürün ve iş hedeflerini kapsayan, ilham veren ve sınanabilir bir ürün vizyonu cümlesi ile vizyon panosu yazar. Yeni bir ürün veya büyük bir yön değişikliği ortak bir yöne ihtiyaç duyduğunda, ekipler ürünün ne için var olduğunda anlaşamadığında ya da vizyon cümlesi veya vizyon panosu istendiğinde kullanılır.
- Örnek istek: _"Küçük işletme müşterilerimize yönelik self-servis fatura portalı için ürün vizyonu ve vizyon panosu yaz."_
- İlgili: `product-strategy-one-pager`, `positioning-statement`, `north-star-metric`, `persona`, `okr-definition`
- Dosya: [skills/02-product/product-manager/strategy/product-vision/SKILL.tr.md](skills/02-product/product-manager/strategy/product-vision/SKILL.tr.md)

**Tek sayfalık ürün stratejisi** · `product-strategy-one-pager`

- Ne zaman: Teşhisi, nerede oynanacağını, nasıl kazanılacağını, az sayıdaki stratejik bahsi ve açık hedef dışı konuları vizyon ve sonuç metriklerine bağlayarak tek sayfalık bir ürün stratejisi yazar. Bir ürünün önümüzdeki 12-24 ay için stratejiye ihtiyacı olduğunda, yol haritasının gerekçesi olmadığında ya da yönetim \"ürün stratejimiz ne\" diye sorduğunda kullanılır.
- Örnek istek: _"B2B saha servis uygulamamız için önümüzdeki 18 aya yönelik tek sayfalık ürün stratejisi taslağı hazırla."_
- İlgili: `product-vision`, `market-analysis`, `competitor-analysis`, `okr-definition`, `roadmap`
- Dosya: [skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.tr.md](skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.tr.md)

**OKR tanımlama** · `okr-definition`

- Ne zaman: Her biri 2-5 ölçülebilir anahtar sonuç içeren sonuç odaklı hedefler yazar; başlangıç değeri, hedef, ölçüm kaynağı ve sorumluyu ekler, çıktı odaklı veya ölçülemeyen anahtar sonuçları işaretler. Bir ekip çeyrek veya yarıyıl planladığında, strateji ölçülebilir hedeflere dönüştürülmek istendiğinde ya da OKR yazılması veya gözden geçirilmesi istendiğinde kullanılır.
- Örnek istek: _"Yeni müşterilerin değere daha hızlı ulaşması hedefine göre onboarding ekibimiz için 3. çeyrek OKR'larını yaz."_
- İlgili: `product-strategy-one-pager`, `north-star-metric`, `kpi-definition`, `goal-setting`, `quarterly-planning`
- Dosya: [skills/02-product/product-manager/strategy/okr-definition/SKILL.tr.md](skills/02-product/product-manager/strategy/okr-definition/SKILL.tr.md)

**Pazar analizi** · `market-analysis`

- Ne zaman: TAM/SAM/SOM büyüklük hesabı (yukarıdan aşağı ve aşağıdan yukarı, her rakam kaynaklı ya da varsayım olarak işaretli), segmentler, trendler, itici güçler ve engellerle yapılandırılmış bir pazar analizi hazırlar. Yeni bir pazar, ürün fikri veya genişleme değerlendirilirken, iş gerekçesi pazar büyüklüğüne ihtiyaç duyduğunda ya da pazarın ne kadar büyük olduğu veya hangi segmentin hedefleneceği sorulduğunda kullanılır.
- Örnek istek: _"Türkiye'deki bağımsız fizyoterapi klinikleri için randevu planlama SaaS ürününün pazar analizini yap."_
- İlgili: `competitor-analysis`, `business-model-canvas`, `product-strategy-one-pager`, `persona`, `pricing-analysis`
- Dosya: [skills/02-product/product-manager/strategy/market-analysis/SKILL.tr.md](skills/02-product/product-manager/strategy/market-analysis/SKILL.tr.md)

**Rakip analizi** · `competitor-analysis`

- Ne zaman: Doğrudan, dolaylı ve ikame rakipleri hedef segment, karşılanan iş, özellikler, fiyatlandırma ve konumlandırma açısından karşılaştırır; tarihli kaynaklarla boşlukları, tehditleri ve farklılaşma fırsatlarını belirler. Bir pazara girerken, strateji veya konumlandırma planlarken, satış kayıplarına hazırlanırken ya da ürünün rakiplerle nasıl kıyaslandığı sorulduğunda kullanılır.
- Örnek istek: _"Masraf yönetimi uygulamamızı Türk KOBİ'lerinin kullandığı başlıca rakiplerle karşılaştır ve nerede farklılaşabileceğimizi göster."_
- İlgili: `market-analysis`, `positioning-statement`, `pricing-analysis`, `product-strategy-one-pager`, `swot-analysis`
- Dosya: [skills/02-product/product-manager/strategy/competitor-analysis/SKILL.tr.md](skills/02-product/product-manager/strategy/competitor-analysis/SKILL.tr.md)

**PESTLE analizi** · `pestle-analysis`

- Ne zaman: Bir ürün, pazara giriş veya stratejik karar için PESTLE analizi (politik, ekonomik, sosyal, teknolojik, yasal, çevresel) yapar; her faktörü etki, olasılık ve zaman ufkuna göre puanlar ve en önemli faktörleri somut ürün ve iş etkilerine çevirir. Yeni bir pazara veya ülkeye girerken, strateji veya yol haritası gözden geçirilirken, mevzuat veya makro risk değerlendirilirken ya da PESTEL/PEST veya \"dış çevre\" taraması istendiğinde kullanılır.
- Örnek istek: _"KOBİ bordro SaaS ürünümüzü gelecek yıl Almanya'da piyasaya sürmek için PESTLE analizi yap."_
- İlgili: `market-analysis`, `swot-analysis`, `porters-five-forces`, `product-strategy-one-pager`, `assumption-mapping`
- Dosya: [skills/02-product/product-manager/strategy/pestle-analysis/SKILL.tr.md](skills/02-product/product-manager/strategy/pestle-analysis/SKILL.tr.md)

**Porter'ın beş gücü analizi** · `porters-five-forces`

- Ne zaman: Bir sektörü veya pazar segmentini Porter'ın beş gücüyle (rekabet, yeni girenlerin tehdidi, ikame ürünlerin tehdidi, alıcı gücü, tedarikçi gücü) analiz eder; her gücü etkenleri ve kanıtlarıyla puanlar ve yapının kârlılık, konumlandırma ve ürün stratejisi için ne anlama geldiğini çıkarır. Bir pazarın veya segmentin çekiciliği değerlendirilirken, strateji veya giriş kararı hazırlanırken, marj baskısı açıklanırken ya da beş güç veya sektör yapısı analizi istendiğinde kullanılır.
- Örnek istek: _"Türkiye'de orta ölçekli şirketlere yönelik saha servis yönetimi yazılımı segmenti için beş güç analizi yap; bu segmente girip girmemeye karar veriyoruz."_
- İlgili: `pestle-analysis`, `competitor-analysis`, `market-analysis`, `swot-analysis`, `pricing-analysis`
- Dosya: [skills/02-product/product-manager/strategy/porters-five-forces/SKILL.tr.md](skills/02-product/product-manager/strategy/porters-five-forces/SKILL.tr.md)

**Rekabet kartı hazırlama** · `competitive-battle-card`

- Ne zaman: Satış ve ön satış ekipleri için adı belli bir rakibe karşı tek sayfalık rekabet kartı hazırlar; ne zaman kazanıp ne zaman kaybettiğimizi, iki tarafın güçlü ve zayıf yönlerini, keşif ve tuzak sorularını, kanıtlı itiraz yanıtlarını ve kısa savuşturma cümlelerini içerir. Satış ekibi anlaşmalarda bir rakiple karşılaştığında, rekabetçi bir sunum veya RFP öncesinde, kazanma/kaybetme notları sahaya yönelik rehbere dönüştürülecekse ya da \"battle card\", \"rakibi nasıl yeneriz\" istendiğinde kullanılır.
- Örnek istek: _"Satış ekibimiz için VendorX'e karşı bir rekabet kartı hazırla; orta ölçekli anlaşmaları fiyat yüzünden onlara kaybediyoruz ama entegrasyon önemli olduğunda kazanıyoruz."_
- İlgili: `competitor-analysis`, `positioning-statement`, `pricing-analysis`, `rfp-response`, `elevator-pitch`
- Dosya: [skills/02-product/product-manager/strategy/competitive-battle-card/SKILL.tr.md](skills/02-product/product-manager/strategy/competitive-battle-card/SKILL.tr.md)

**İş modeli / lean kanvas** · `business-model-canvas`

- Ne zaman: Bir ürün fikri için İş Modeli Kanvası veya Lean Kanvas'ı doldurur; kanıtı varsayımdan ayırır ve önce sınanacak en riskli varsayımları sıralar. Yeni bir fikir, girişim veya ürün hattının iş mantığının ortaya konması gerektiğinde, iş modeli seçenekleri karşılaştırılırken ya da iş modeli veya lean kanvas istendiğinde kullanılır.
- Örnek istek: _"Serbest çalışan mali müşavirleri küçük e-ticaret satıcılarıyla buluşturan bir pazaryeri için lean kanvas doldur."_
- İlgili: `market-analysis`, `pricing-analysis`, `assumption-mapping`, `hypothesis-statement`, `product-vision`
- Dosya: [skills/02-product/product-manager/strategy/business-model-canvas/SKILL.tr.md](skills/02-product/product-manager/strategy/business-model-canvas/SKILL.tr.md)

**Fiyatlandırma analizi** · `pricing-analysis`

- Ne zaman: Fiyat modellerini (sabit, kademeli, kullanıcı başı, kullanım bazlı, freemium, hibrit) değer metriği, hizmet maliyeti, rakip çıpaları ve ödeme isteği sinyallerine göre karşılaştırır; fiyat testi seçenekleriyle bir model önerir. Bir ürün yayına alınırken, ücretli bir paket eklenirken, fiyatlar yeniden ele alınırken ya da bir ürünün nasıl fiyatlanacağı veya paketleneceği sorulduğunda kullanılır.
- Örnek istek: _"API izleme aracımız için fiyatlandırma seçeneklerini analiz et; şu an aylık sabit 49 USD."_
- İlgili: `market-analysis`, `competitor-analysis`, `business-model-canvas`, `experiment-design`, `persona`
- Dosya: [skills/02-product/product-manager/strategy/pricing-analysis/SKILL.tr.md](skills/02-product/product-manager/strategy/pricing-analysis/SKILL.tr.md)

#### Keşif

**Persona oluşturma** · `persona`

- Ne zaman: Bağlam, hedefler, sorunlar, davranışlar, karar kriterleri ve alıntılarla kanıta dayalı bir persona oluşturur; her niteliği araştırmaya bağlar ve proto-persona varsayımlarını işaretler. Araştırma verisinin (görüşmeler, anketler, analitik, destek kayıtları) ortak bir kullanıcı modeline dönüştürülmesi gerektiğinde ya da tasarım ve ürün kararları için persona veya kullanıcı profili istendiğinde kullanılır.
- Örnek istek: _"Bu 8 görüşme özetinden depo vardiya amirleri için bir persona oluştur."_
- İlgili: `jobs-to-be-done`, `customer-journey-map`, `research-synthesis`, `feedback-synthesis`, `problem-interview-script`
- Dosya: [skills/02-product/product-manager/discovery/persona/SKILL.tr.md](skills/02-product/product-manager/discovery/persona/SKILL.tr.md)

**Yapılacak İşler (JTBD)** · `jobs-to-be-done`

- Ne zaman: Çözümden bağımsız bir temel iş ifadesi, ilişkili ve duygusal/sosyal işler, iş adımları ile önem ve memnuniyete göre önceliklendirilebilecek ölçülebilir istenen sonuç ifadeleri yazarak Yapılacak İşler (JTBD) çerçevesini kurar. Müşterilerin neyi başarmaya çalıştığı tanımlanırken, inovasyon veya yol haritası çalışması çözümden bağımsız bir çerçeveye ihtiyaç duyduğunda ya da JTBD, iş hikâyeleri veya istenen sonuçlar istendiğinde kullanılır.
- Örnek istek: _"Tedarikçi siparişlerini yöneten restoran sahipleri için yapılacak işleri (JTBD) çerçevele."_
- İlgili: `persona`, `opportunity-solution-tree`, `customer-journey-map`, `problem-interview-script`, `feedback-synthesis`
- Dosya: [skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.tr.md](skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.tr.md)

**Değer önerisi kanvası** · `value-proposition-canvas`

- Ne zaman: Tek bir müşteri segmenti için değer önerisi kanvasını doldurur; müşteri işlerini, sorunlarını ve kazanımlarını ürün ve hizmetlerle, sorun gidericilerle ve kazanım yaratıcılarla eşler, bunları önem sırasına koyar, problem-çözüm uyumunu kontrol eder ve sınanacak varsayımları listeler. Bir değer önerisi tanımlanırken veya keskinleştirilirken, bir ürün fikrinin gerçek sorunlara dokunup dokunmadığı kontrol edilirken, konumlandırma veya keşif çalışması hazırlanırken ya da \"değer önerisi kanvası\" veya \"uyum\" analizi istendiğinde kullanılır.
- Örnek istek: _"Orta ölçekli distribütörlerdeki saha satış temsilcileri için masraf uygulamamızın değer önerisi kanvasını doldur."_
- İlgili: `jobs-to-be-done`, `persona`, `positioning-statement`, `business-model-canvas`, `hypothesis-statement`
- Dosya: [skills/02-product/product-manager/discovery/value-proposition-canvas/SKILL.tr.md](skills/02-product/product-manager/discovery/value-proposition-canvas/SKILL.tr.md)

**Müşteri yolculuğu haritası** · `customer-journey-map`

- Ne zaman: Bir persona ve senaryo için müşteri yolculuğunu aşamalar boyunca eylemler, düşünceler, duygular, temas noktaları, kanallar, sorunlar, kritik anlar ve arka plandaki sorumlularla haritalar; iyileştirme fırsatlarını sıralar. Uçtan uca bir deneyimin anlaşılması, müşterilerin nerede zorlandığının veya vazgeçtiğinin bulunması, kanallar arası ekiplerin hizalanması gerektiğinde ya da yolculuk haritası istendiğinde kullanılır.
- Örnek istek: _"Web sitemiz ve çağrı merkezimiz üzerinden ilk kez konut sigortası alan müşterinin yolculuğunu haritala."_
- İlgili: `persona`, `jobs-to-be-done`, `funnel-analysis`, `user-flow`, `as-is-process`
- Dosya: [skills/02-product/product-manager/discovery/customer-journey-map/SKILL.tr.md](skills/02-product/product-manager/discovery/customer-journey-map/SKILL.tr.md)

**Fırsat-çözüm ağacı** · `opportunity-solution-tree`

- Ne zaman: Tek bir ölçülebilir hedef sonucu araştırmadan gelen müşteri fırsatlarına (ihtiyaçlar, sorunlar, istekler), hedef fırsat başına birden fazla aday çözüme ve varsayım testlerine bağlayan bir fırsat-çözüm ağacı oluşturur. Bir ekibin bir sonucu etkilemek için neye odaklanacağını seçmesi gerektiğinde, keşif çalışması yapıdan yoksun olduğunda ya da bir hedefi fikirlere ve deneylere bağlamak istendiğinde kullanılır.
- Örnek istek: _"Yeni mobil bankacılık kullanıcılarının 30 günlük elde tutma oranını artırmak için bir fırsat-çözüm ağacı oluştur."_
- İlgili: `okr-definition`, `jobs-to-be-done`, `hypothesis-statement`, `experiment-design`, `assumption-mapping`
- Dosya: [skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.tr.md](skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.tr.md)

**Ürün hipotezi yazma** · `hypothesis-statement`

- Ne zaman: Bir ürün fikrini, özellik talebini veya varsayımı \"İnanıyoruz ki / şu sonucu doğuracak / bunu şuradan anlayacağız\" formatında, hedef segmenti, en riskli varsayımı, ölçülebilir sinyali, eşik değeri ve süre sınırı olan yanlışlanabilir bir hipoteze dönüştürür. Ekip bir fikri tam geliştirmeden önce sınamak istediğinde, bir backlog maddesinin beklenen sonucu belirsiz olduğunda ya da ürün hipotezi yazılması, keskinleştirilmesi veya gözden geçirilmesi istendiğinde kullanılır.
- Örnek istek: _"Sepeti sonraya kaydet\" butonu için bir hipotez yaz; mobilde ödeme adımındaki terk oranını düşüreceğini düşünüyoruz."_
- İlgili: `experiment-design`, `assumption-mapping`, `opportunity-solution-tree`, `problem-statement`, `ab-test-analysis`
- Dosya: [skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.tr.md](skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.tr.md)

**Ürün deneyi tasarlama** · `experiment-design`

- Ne zaman: Bir hipotezden yola çıkarak ürün deneyi (A/B testi, sahte kapı, boyalı kapı, concierge veya prototip testi) tasarlar; varyantları, rastgeleleştirme birimini, birincil ve koruma metriklerini, tespit edilebilir en küçük etkiyi, örneklem büyüklüğünü ve süreyi, durdurma kurallarını ve önceden taahhüt edilmiş karar kuralını belirler. Ekip bir hipotezi gerçek kullanıcılarla doğrulamak istediğinde, A/B veya sahte kapı testinin nasıl kurulacağını sorduğunda ya da bir deney planının yayından önce kontrol edilmesi gerektiğinde kullanılır.
- Örnek istek: _"Yeni fiyatlandırma sayfası tasarımımız için bir A/B testi tasarla; haftada yaklaşık 40.000 ziyaretçimiz var ve deneme kaydı oranı %3,2."_
- İlgili: `hypothesis-statement`, `ab-test-analysis`, `assumption-mapping`, `metric-definition`, `funnel-analysis`
- Dosya: [skills/02-product/product-manager/discovery/experiment-design/SKILL.tr.md](skills/02-product/product-manager/discovery/experiment-design/SKILL.tr.md)

**Müşteri geri bildirimi sentezi** · `feedback-synthesis`

- Ne zaman: Ham müşteri geri bildirimlerini (destek kayıtları, NPS/CSAT yorumları, uygulama mağazası değerlendirmeleri, satış notları, topluluk gönderileri) sıklık, önem derecesi, etkilenen segmentler, anonimleştirilmiş temsilî alıntılar ve her talebin arkasındaki asıl ihtiyaçla temalara ayırır. Birikmiş geri bildirimin önceliklendirilebilir içgörülere dönüştürülmesi gerektiğinde, \"müşteriler bize ne söylüyor\" sorulduğunda ya da yol haritası ve backlog görüşmelerinden önce kullanılır.
- Örnek istek: _"Geçen çeyreğin 120 NPS yorumu burada; bunları temalara ayır ve en önemli olanları söyle."_
- İlgili: `research-synthesis`, `jobs-to-be-done`, `opportunity-solution-tree`, `persona`, `backlog-prioritization`
- Dosya: [skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.tr.md](skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.tr.md)

**Problem görüşmesi senaryosu** · `problem-interview-script`

- Ne zaman: The Mom Test yaklaşımıyla, görüş veya satış konuşması yerine geçmiş davranışları, gerçek harcamaları ve mevcut geçici çözümleri soran, yönlendirmeyen bir müşteri problem görüşmesi senaryosu yazar; huni sıralı rehber, derinleştirme soruları, taahhüt sinyalleri ve not formu içerir. Ekip bir problemin var olduğunu geliştirmeden önce doğrulamak istediğinde, keşif görüşmelerine hazırlanırken ya da yönlendirici veya varsayımsal olabilecek soruların gözden geçirilmesi istendiğinde kullanılır.
- Örnek istek: _"Küçük klinik sahiplerinin randevuya gelmeyen hastalarla gerçekten sorun yaşayıp yaşamadığını anlamak için bir problem görüşmesi senaryosu yaz."_
- İlgili: `interview-question-set`, `research-plan`, `screener-survey`, `jobs-to-be-done`, `research-synthesis`
- Dosya: [skills/02-product/product-manager/discovery/problem-interview-script/SKILL.tr.md](skills/02-product/product-manager/discovery/problem-interview-script/SKILL.tr.md)

#### Ürün Tanımı

**Ürün Gereksinim Dokümanı (PRD) yazma** · `prd-writing`

- Ne zaman: Problem ve kanıtları, hedefleri ve başarı metriklerini, hedef kullanıcıları, kapsam ve hedef dışı konuları, kabul kriterleriyle önceliklendirilmiş gereksinimleri, kullanıcı deneyimini, fonksiyonel olmayan ihtiyaçları, bağımlılıkları, riskleri, yayın planını ve açık soruları kapsayan bir Ürün Gereksinim Dokümanı (PRD) yazar. Bir ürün girişiminin geliştirme öncesinde mühendislik, tasarım ve paydaşlar arasında hizalanması gerektiğinde, PRD veya ürün spesifikasyonu istendiğinde ya da mevcut bir PRD'nin eksikler açısından gözden geçirilmesi gerektiğinde kullanılır.
- Örnek istek: _"B2B müşterilerin belirli bir tutarın üzerindeki satın alma siparişleri için onay akışı tanımlayabilmesi için bir PRD yaz."_
- İlgili: `feature-brief`, `mvp-scoping`, `epic-breakdown`, `nfr-specification`, `acceptance-criteria`
- Dosya: [skills/02-product/product-manager/definition/prd-writing/SKILL.tr.md](skills/02-product/product-manager/definition/prd-writing/SKILL.tr.md)

**Özellik özeti yazma** · `feature-brief`

- Ne zaman: Ekibi tek bir özellik etrafında hizalayan tek sayfalık bir özellik özeti yazar: problem ve kimin yaşadığı, beklenen sonuç ve başarı sinyali, önerilen yaklaşım, kapsam sınırları, temel riskler ve hâlâ gereken kararlar. Özellik tam bir PRD gerektirmeyecek kadar küçükse, bir paydaş kickoff veya refinement öncesinde \"kısa bir yazı\" istediğinde ya da bir talebin yap/yapma görüşmesi için çerçevelenmesi gerektiğinde kullanılır.
- Örnek istek: _"CRM'imize kişilerin toplu CSV ile içe aktarılması için bir özellik özeti yaz."_
- İlgili: `prd-writing`, `hypothesis-statement`, `mvp-scoping`, `epic-breakdown`, `problem-statement`
- Dosya: [skills/02-product/product-manager/definition/feature-brief/SKILL.tr.md](skills/02-product/product-manager/definition/feature-brief/SKILL.tr.md)

**MVP kapsamını belirleme** · `mvp-scoping`

- Ne zaman: Bir ürün veya özellik kapsamını, en riskli değer varsayımını gerçek kullanıcılarla sınayan en küçük sürüme indirir; varsayım odaklı kesim, mutlaka/sonra/asla kapsam tablosu, açık bir kalite tabanı, öğrenme hedefleri ve çıkış kriterleri kullanır. Kapsam eldeki süreye göre çok büyükse, \"MVP'miz ne\" diye sorulduğunda ya da ekip ilk sürümden neyi dışarıda bırakacağına karar vermesi gerektiğinde kullanılır.
- Örnek istek: _"Saha servis planlama uygulaması için 8 haftamız ve 40 maddelik bir özellik listemiz var; MVP kapsamını belirlememe yardım et."_
- İlgili: `hypothesis-statement`, `story-mapping`, `prd-writing`, `assumption-mapping`, `release-planning`
- Dosya: [skills/02-product/product-manager/definition/mvp-scoping/SKILL.tr.md](skills/02-product/product-manager/definition/mvp-scoping/SKILL.tr.md)

**Epic'i hikayelere bölme** · `epic-breakdown`

- Ne zaman: Bir epic'i belirli bir persona, gerçek bir sonuç ve ilk dilim olarak uçtan uca bir iskelet (walking skeleton) içeren, değer, risk ve bağımlılığa göre sıralanmış ince, dikey ve bağımsız değer üreten hikayelere böler. Bir epic, girişim veya büyük özellik backlog maddelerine dönüşecekse, hikayeler katman (UI/API/DB) ya da teknik görev olarak çıkıyorsa veya ekip \"bu epic'i nasıl bölelim\" diye soruyorsa kullanılır.
- Örnek istek: _"Bu epic'i hikayelere böl: \"KOBİ müşterileri için müşteri portalında self-servis sözleşme yenileme\"."_
- İlgili: `story-splitting`, `user-story`, `acceptance-criteria`, `story-mapping`, `invest-check`
- Dosya: [skills/02-product/product-manager/definition/epic-breakdown/SKILL.tr.md](skills/02-product/product-manager/definition/epic-breakdown/SKILL.tr.md)

**Kullanıcı hikaye haritası** · `story-mapping`

- Ne zaman: Soldan sağa kullanıcı aktiviteleri ve adımlarından oluşan bir omurga, her adımın altında önceliğe göre dizilmiş hikayeler ve her biri kullanılabilir uçtan uca bir sonuç sunan yatay sürüm dilimleriyle kullanıcı hikaye haritası oluşturur. Bir ürün veya büyük özellik tüm kullanıcı yolculuğu boyunca planlanacaksa, düz backlog büyük resmi kaybettirdiyse ya da ekip ilk ve sonraki sürümlere ne gireceğinde uzlaşmalıysa kullanılır.
- Örnek istek: _"B2B masraf yönetimi uygulamamız için, çalışanın fiş göndermesinden finansın ödemesine kadar bir hikaye haritası çıkar."_
- İlgili: `epic-breakdown`, `mvp-scoping`, `release-planning`, `customer-journey-map`, `roadmap`
- Dosya: [skills/02-product/product-manager/definition/story-mapping/SKILL.tr.md](skills/02-product/product-manager/definition/story-mapping/SKILL.tr.md)

#### Metrikler

**Kuzey Yıldızı metriği tanımlama** · `north-star-metric`

- Ne zaman: Müşterinin üründen aldığı değeri yakalayan ve gelire bağlanan bir Kuzey Yıldızı metriği seçer; bunu sahipleri ve karşı metrikleriyle birlikte kontrol edilebilir 3-5 girdi metriğinden oluşan bir ağaca ayırır. Ürün ekibinin ortak bir değer metriği yoksa, ekipler birbiriyle çelişen sayıları optimize ediyorsa ya da biri \"Kuzey Yıldızımız ne olmalı\" diye soruyor veya ürün için metrik ağacı istiyorsa kullanılır.
- Örnek istek: _"Küçük işletmelere yönelik B2B faturalama SaaS ürünümüz için Kuzey Yıldızı metriği ve girdi metrik ağacı tanımla."_
- İlgili: `kpi-definition`, `okr-definition`, `metric-definition`, `product-strategy-one-pager`, `funnel-analysis`
- Dosya: [skills/02-product/product-manager/metrics/north-star-metric/SKILL.tr.md](skills/02-product/product-manager/metrics/north-star-metric/SKILL.tr.md)

**KPI tanımlama** · `kpi-definition`

- Ne zaman: Ürün KPI'larını ad, amaç, formül, dahil etme kuralları, veri kaynağı, başlangıç değeri, hedef, eşikler, sahip, periyot ve her KPI'nın beslediği kararı içeren, belirsizliği olmayan bir KPI tablosu olarak tanımlar. Bir ürün, özellik veya ekip için KPI seti gerektiğinde, mevcut KPI'lar belirsiz veya tartışmalıysa ya da biri \"hangi KPI'ları izlemeliyiz ve tam olarak nasıl hesaplanıyor\" diye sorduğunda kullanılır.
- Örnek istek: _"Otellerdeki yeni mobil self check-in özelliğimiz için KPI'ları tanımla."_
- İlgili: `north-star-metric`, `metric-definition`, `okr-definition`, `dashboard-spec`, `feature-adoption-review`
- Dosya: [skills/02-product/product-manager/metrics/kpi-definition/SKILL.tr.md](skills/02-product/product-manager/metrics/kpi-definition/SKILL.tr.md)

**Huni analizi** · `funnel-analysis`

- Ne zaman: Bir dönüşüm hunisini adım adım analiz eder; adım ve kümülatif dönüşümü hesaplar, en büyük mutlak kayıpları bulur, bunları segmentlere ayırır, veri kaynaklı sapmaları gerçek davranıştan ayırır ve bulguları sıralanmış, test edilebilir iyileştirme hipotezlerine dönüştürür. Kayıt, onboarding, ödeme veya aktivasyon için huni sayıları ya da olay verisi verildiğinde veya biri \"kullanıcıları nerede kaybediyoruz ve neden\" diye sorduğunda kullanılır.
- Örnek istek: _"Geçen ayın adım ve cihaz bazında kayıt hunisi sayıları burada; kullanıcıları nerede kaybettiğimizi ve ne denememiz gerektiğini bul."_
- İlgili: `experiment-design`, `hypothesis-statement`, `customer-journey-map`, `north-star-metric`, `data-exploration`
- Dosya: [skills/02-product/product-manager/metrics/funnel-analysis/SKILL.tr.md](skills/02-product/product-manager/metrics/funnel-analysis/SKILL.tr.md)

**Özellik benimsenme analizi** · `feature-adoption-review`

- Ne zaman: Yayınlanmış bir özelliğin benimsenmesini, tutunmasını ve sonucunu, lansman öncesi belirlenen hedeflere göre erişim-aktivasyon-tutunma-sonuç kırılımı, segment ayrımları ve nitel sinyallerle değerlendirir; sürdür, iyileştir, yaygınlaştır veya kaldır önerisiyle bitirir. Bir sürümden birkaç hafta sonra, lansman sonrası değerlendirmede ya da biri \"bu özelliği kullanan var mı, işe yaradı mı\" diye sorduğunda kullanılır.
- Örnek istek: _"8 hafta önce yayınladığımız toplu düzenleme özelliğinin benimsenmesini değerlendir; kullanım sayıları ve destek kayıtları burada."_
- İlgili: `kpi-definition`, `funnel-analysis`, `feedback-synthesis`, `benefits-realization`, `product-sunset-plan`
- Dosya: [skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.tr.md](skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.tr.md)

#### Lansman

**Pazara çıkış planı** · `go-to-market-plan`

- Ne zaman: Bir ürün veya büyük özellik için lansman seviyesi, hedef segment ve alıcı, konumlandırma ve mesajlar, kanallar, fiyat ve paketleme bağlantıları, hazırlık kapılarıyla zaman çizelgesi, satış/destek hazırlığı ve lansman başarı metriklerini kapsayan bir pazara çıkış (GTM) planı yazar. Bir ürün, özellik veya pazar girişi lansmana yaklaşıyorsa, biri GTM veya lansman planı istiyorsa ya da pazarlama, satış ve destek tek ve uyumlu bir plana ihtiyaç duyuyorsa kullanılır.
- Örnek istek: _"Yapay zeka destekli fatura eşleştirme modülümüzü mevcut orta ölçekli ERP müşterilerine sunmak için bir pazara çıkış planı yaz."_
- İlgili: `positioning-statement`, `release-announcement`, `pricing-analysis`, `competitive-battle-card`, `communication-plan`
- Dosya: [skills/02-product/product-manager/launch/go-to-market-plan/SKILL.tr.md](skills/02-product/product-manager/launch/go-to-market-plan/SKILL.tr.md)

**Sürüm duyurusu yazma** · `release-announcement`

- Ne zaman: Okuyucuya sağlanan faydayla başlayan, neyin değiştiğini ve kimi etkilediğini anlatan, erişilebilirliği ve gereken aksiyonu belirten, net bir sonraki adımla biten ve kanala (e-posta, blog, uygulama içi, sosyal medya) uyarlanmış müşteriye yönelik bir sürüm duyurusu yazar. Bir özellik veya ürün sürümü müşterilere açıldığında, sürüm notlarının pazarlamaya hazır metne dönüştürülmesi gerektiğinde ya da bir sürümü \"duyurmak\" veya \"müşterilere anlatmak\" istendiğinde kullanılır.
- Örnek istek: _"Önümüzdeki salı e-posta ve uygulama içi bildirimle çıkacak yeni toplu fatura yükleme özelliğimiz için müşteri duyurusu yaz."_
- İlgili: `positioning-statement`, `go-to-market-plan`, `release-notes`, `announcement`, `microcopy`
- Dosya: [skills/02-product/product-manager/launch/release-announcement/SKILL.tr.md](skills/02-product/product-manager/launch/release-announcement/SKILL.tr.md)

**Konumlandırma cümlesi** · `positioning-statement`

- Ne zaman: Bir ürün veya özellik için belirli bir hedef segmente, gerçek bir alternatife ve kanıtlanabilir bir farka dayanan konumlandırma cümlesini Kimin için/Kim/Nedir/Ne yapar/Rakiplerden farkı formatında yazar; ardından kanıt noktalarını ve mesaj sınırlarını çıkarır. Bir ürün veya büyük bir özellik lansmana hazırlanırken, satış ve pazarlama ürünü farklı anlatırken ya da \"bunu nasıl konumlandıralım\", \"bizi farklı kılan ne\" diye sorulduğunda kullanılır.
- Örnek istek: _"Orta ölçekli üreticilerin finans ekiplerine yönelik yeni fatura eşleştirme modülümüz için konumlandırma cümlesi yaz."_
- İlgili: `value-proposition-canvas`, `competitor-analysis`, `persona`, `go-to-market-plan`, `elevator-pitch`
- Dosya: [skills/02-product/product-manager/launch/positioning-statement/SKILL.tr.md](skills/02-product/product-manager/launch/positioning-statement/SKILL.tr.md)

**Tersine çalışma basın bülteni ve SSS** · `press-release-faq`

- Ne zaman: Bir ürün fikrinin, hiçbir şey geliştirilmeden önce ilgi çekici, anlaşılır ve yapılabilir olup olmadığını sınamak için gelecekteki bir lansman tarihli tersine çalışma basın bülteni, müşteri SSS'si ve iç SSS yazar; dokümanın ortaya çıkardığı açık sorular ve risklerle biter. Yeni bir ürün veya büyük bir özellik önerildiğinde, ekibin tasarımdan önce müşteri sonucunda uzlaşması gerektiğinde ya da \"PR/FAQ\", \"working backwards\" dokümanı veya \"gelecekteki basın bülteni\" istendiğinde kullanılır.
- Örnek istek: _"B2B müşterilerimizin portala giriş yapmadan WhatsApp üzerinden teslimat tahmini (ETA) alabildiği bir özellik için tersine çalışma PR/FAQ yaz."_
- İlgili: `product-vision`, `prd-writing`, `value-proposition-canvas`, `positioning-statement`, `pre-mortem`
- Dosya: [skills/02-product/product-manager/launch/press-release-faq/SKILL.tr.md](skills/02-product/product-manager/launch/press-release-faq/SKILL.tr.md)

#### Ürün Yaşam Döngüsü

**Ürün/özellik kullanımdan kaldırma planı** · `product-sunset-plan`

- Ne zaman: Bir ürünün, paketin veya özelliğin kullanımdan kaldırılmasını; açık karar kriterleri, etkilenen müşteri segmentleri, geçiş yolları, aşamalı iletişim sırası, takvim kapıları ve veri saklama/silme yükümlülükleriyle planlar. Bir ürün veya özellik emekliye ayrılırken, yenisiyle değiştirilirken ya da birleştirilirken veya \"müşteri ve güven kaybetmeden bunu nasıl kapatırız\" sorusu sorulduğunda kullanılır.
- Örnek istek: _"Eski raporlama modülümüzü gelecek yıl kapatıp herkesi yeni analitik panoya taşımak istiyoruz. Kullanımdan kaldırma planını hazırla."_
- İlgili: `communication-plan`, `migration-strategy`, `api-deprecation-plan`, `impact-analysis`, `kpi-definition`
- Dosya: [skills/02-product/product-manager/lifecycle/product-sunset-plan/SKILL.tr.md](skills/02-product/product-manager/lifecycle/product-sunset-plan/SKILL.tr.md)

### Ürün Sahibi

#### Backlog Yönetimi

**Backlog iyileştirme** · `backlog-refinement`

- Ne zaman: Bir grup backlog maddesini iyileştirme oturumuna hazırlar; bunları kabul kriterleri, açık sorular ve hazır olma kararı içeren, net, uygun boyutta, tahmine hazır ve sıralı iş maddelerine dönüştürür. Backlog düzenlenmesi gerektiğinde, maddeler iterasyon/sprint planlaması öncesinde belirsiz veya çok büyük olduğunda ya da hikayelerin hazırlanması istendiğinde kullanılır.
- Örnek istek: _"Gelecek haftaki planlama için bu 8 backlog maddesini iyileştir; hangileri hazır, hangileri bölünmeli ve iş birimine daha neler sormalıyız söyle."_
- İlgili: `story-splitting`, `definition-of-ready`, `acceptance-criteria`, `backlog-prioritization`, `estimation-session`
- Dosya: [skills/02-product/product-owner/backlog/backlog-refinement/SKILL.tr.md](skills/02-product/product-owner/backlog/backlog-refinement/SKILL.tr.md)

**Backlog önceliklendirme** · `backlog-prioritization`

- Ne zaman: Backlog maddelerini açık ve savunulabilir bir yöntemle (WSJF, RICE, değer/efor, MoSCoW veya gecikme maliyeti) sıralar; puanlar, gerekçeler, duyarlılık notları ve ertelenecek veya çıkarılacak maddelerle birlikte sıralı bir liste üretir. Ürün sahibinin sıradaki işe karar vermesi gerektiğinde, paydaşlar öncelikler konusunda anlaşamadığında ya da backlog sırasının puanlanması ve gerekçelendirilmesi istendiğinde kullanılır.
- Örnek istek: _"Bu 12 backlog maddesini WSJF ile önceliklendir; efor tahminleri tabloda, değer bilgisi satış ve destek geri bildirimlerinden geliyor."_
- İlgili: `backlog-refinement`, `requirements-prioritization`, `portfolio-prioritization`, `roadmap`, `decision-matrix`
- Dosya: [skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.tr.md](skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.tr.md)

**Büyük hikayeleri bölme** · `story-splitting`

- Ne zaman: Büyük bir kullanıcı hikayesini veya iş maddesini adlandırılmış desenlerle (iş akışı adımı, iş kuralı, veri çeşitliliği, arayüz, işlem, olumlu/olumsuz yol, spike) ince ve bağımsız değer taşıyan dikey dilimlere böler; her dilim için kabul kriterlerini ve önerilen sırayı gösterir. Bir hikaye tek iterasyona/sprint'e sığmadığında, tahminler çok dağınık olduğunda ya da bir hikayenin bölünmesi, dilimlenmesi istendiğinde kullanılır.
- Örnek istek: _"Bu hikaye 21 puan ve kimse tahmine güvenmiyor: 'Müşteri olarak faturamı çevrim içi ödemek istiyorum.' Böl."_
- İlgili: `epic-breakdown`, `invest-check`, `backlog-refinement`, `acceptance-criteria`, `user-story`
- Dosya: [skills/02-product/product-owner/backlog/story-splitting/SKILL.tr.md](skills/02-product/product-owner/backlog/story-splitting/SKILL.tr.md)

**Hazır Tanımı (DoR) oluşturma** · `definition-of-ready`

- Ne zaman: Bir ekibin Hazır Tanımını (DoR) oluşturur veya revize eder: ekibin bir iş maddesini taahhüt etmeden veya başlatmadan önce aranan giriş kriterlerini madde türlerine göre uyarlar, her kriterin nasıl kontrol edileceğini ve hangi durumlarda istisna yapılabileceğini belirtir. Ekip belirsiz işlere başlayıp takıldığında, planlama eksik bilgi yüzünden durduğunda ya da DoR, hazır olma kriterleri veya giriş kontrol listesi istendiğinde kullanılır.
- Örnek istek: _"Ekibimiz için bir Hazır Tanımı yaz; B2B bir web portalı geliştiriyoruz ve sürekli eksik API sözleşmeleri ve UX tasarımları yüzünden takılıyoruz."_
- İlgili: `definition-of-done`, `backlog-refinement`, `invest-check`, `acceptance-criteria`, `working-agreement`
- Dosya: [skills/02-product/product-owner/backlog/definition-of-ready/SKILL.tr.md](skills/02-product/product-owner/backlog/definition-of-ready/SKILL.tr.md)

**Bitti Tanımı (DoD) oluşturma** · `definition-of-done`

- Ne zaman: Bir Bitti Tanımı (DoD) oluşturur veya revize eder: her artımın veya iş maddesinin tamamlanmış sayılması için geçmesi gereken ortak kalite kontrol listesini madde, sürüm ve kurum seviyelerine ayırır; her kriter için doğrulama yöntemini ve eksikleri kapatma planını verir. 'Bitti' herkes için farklı anlama geldiğinde, kalite sorunları canlıya sızdığında ya da DoD veya tamamlanma kriterleri istendiğinde kullanılır.
- Örnek istek: _"Mobil bankacılık ekibimiz için bir Bitti Tanımı taslağı hazırla; kod incelemesi ve birim testlerimiz var ama sürümler hâlâ erişilebilirlik ve güvenlik kontrollerinde sorun çıkarıyor."_
- İlgili: `definition-of-ready`, `release-quality-gate`, `acceptance-criteria`, `coding-standards`, `working-agreement`
- Dosya: [skills/02-product/product-owner/backlog/definition-of-done/SKILL.tr.md](skills/02-product/product-owner/backlog/definition-of-done/SKILL.tr.md)

**Backlog sağlık kontrolü** · `backlog-health-check`

- Ne zaman: Bir backlog dökümünü veya listesini sağlık sorunları (bayat, tekrar eden, fazla büyük, sahipsiz, önceliksiz veya hedefsiz maddeler, çok fazla veya çok az hazır iş) açısından denetler; metriklerle bulgular, temizlik önerisi ve düzen kuralları üretir. Backlog yönetilemez hale geldiğinde, kimse ona güvenmediğinde, planlama döngüsünden önce ya da backlog'un temizlenmesi, denetlenmesi istendiğinde kullanılır.
- Örnek istek: _"Ekte 340 maddelik backlog dökümümüz var (başlık, tür, oluşturma tarihi, son güncelleme, epic, durum). Sağlığını kontrol et ve neleri silmem gerektiğini söyle."_
- İlgili: `backlog-refinement`, `backlog-prioritization`, `definition-of-ready`, `roadmap`, `cycle-time-analysis`
- Dosya: [skills/02-product/product-owner/backlog/backlog-health-check/SKILL.tr.md](skills/02-product/product-owner/backlog/backlog-health-check/SKILL.tr.md)

#### Planlama

**Ürün yol haritası** · `roadmap`

- Ne zaman: Sonuçlara bağlı bir ürün yol haritası oluşturur; Şimdi/Sonra/Daha Sonra ya da güven seviyeli zaman çizelgesi biçiminde temaları, hedef sonuçları, ana girişimleri, bağımlılıkları, açıkça planlanmayanları ve yol haritasının nasıl güncelleneceğini gösterir. Ürün sahibi veya yöneticisinin yönü paydaşlara anlatması, önümüzdeki çeyrekler için ekipleri hizalaması ya da bir özellik listesini sonuç odaklı bir plana dönüştürmesi gerektiğinde kullanılır.
- Örnek istek: _"İK self-servis uygulamamız için bu 25 özellik talebini Şimdi/Sonra/Daha Sonra yol haritasına dönüştür; bu yılki hedeflerimiz daha az İK talebi ve daha yüksek mobil kullanım."_
- İlgili: `product-vision`, `okr-definition`, `release-planning`, `backlog-prioritization`, `program-roadmap`
- Dosya: [skills/02-product/product-owner/planning/roadmap/SKILL.tr.md](skills/02-product/product-owner/planning/roadmap/SKILL.tr.md)

**Sürüm planlama** · `release-planning`

- Ne zaman: Bir sürümü planlar: hedef sonuç, taahhüt edilen ve esnek olarak ayrılmış aday kapsam, verim veya hız aralıklarına dayanarak kapsamın ne zaman bitebileceğine dair öngörü, bağımlılıklar, kilometre taşları, riskler, güven seviyesi ve kapsam-tarih ödünleşim seçenekleri. Ürün sahibinin bir sürümde ne olacağını ve ne zaman çıkacağını cevaplaması, sabit bir tarih için pazarlık yapması ya da paydaşlar için sürüm planı hazırlaması gerektiğinde kullanılır.
- Örnek istek: _"Yeni onboarding akışını 15 Mart'a kadar yayınlamak istiyoruz. Kalan 18 madde ve son 8 iterasyonun verimi burada. Mümkün mü, hangi kapsamı taahhüt etmeliyiz?"_
- İlgili: `roadmap`, `monte-carlo-forecast`, `velocity-analysis`, `release-plan`, `dependency-map`
- Dosya: [skills/02-product/product-owner/planning/release-planning/SKILL.tr.md](skills/02-product/product-owner/planning/release-planning/SKILL.tr.md)

**İterasyon hedefi yazma** · `iteration-goal`

- Ne zaman: Ekibin taahhüt ettiği sonucu, bunun neden önemli olduğunu ve başarının nasıl gözlemleneceğini belirten tek ve tutarlı bir iterasyon/sprint hedefi yazar; aday maddelerden hangilerinin hedefe hizmet ettiğini, hangilerinin etmediğini kontrol eder. İterasyon/sprint planlamasına hazırlanırken, taslak hedef sadece bir kayıt listesiyse ya da sprint hedefi veya iterasyon amacı istendiğinde kullanılır.
- Örnek istek: _"Sonraki sprint adaylarımız: SSO girişi, parola sıfırlama e-postası düzeltmesi, denetim logu dışa aktarma ve iki teknik borç maddesi. Bir sprint hedefi yaz."_
- İlgili: `iteration-planning`, `backlog-prioritization`, `roadmap`, `okr-definition`, `iteration-review-prep`
- Dosya: [skills/02-product/product-owner/planning/iteration-goal/SKILL.tr.md](skills/02-product/product-owner/planning/iteration-goal/SKILL.tr.md)

**Ürün değerlendirme toplantısı hazırlığı** · `stakeholder-review-prep`

- Ne zaman: Bir ürün veya paydaş değerlendirme toplantısını hazırlar: ne yapıldı ve neden, ürün hedefini nasıl ilerletiyor, kimden hangi geri bildirim gerekiyor, hangi kararlar alınmalı; demo akışı ve güncel görünümle birlikte bir gündem sunar. İterasyon/sprint değerlendirmesi, aylık ürün değerlendirmesi veya paydaşların ilerlemeyi inceleyip girdi vermesi gereken ürün kontrol noktalarından önce kullanılır.
- Örnek istek: _"Satış ve operasyon direktörleriyle aylık ürün değerlendirme toplantımızı hazırla: toplu yükleme ve yeni fatura ekranını yayınladık; fiyatlandırma sayfası için karar ve mobil beta için geri bildirim almam gerekiyor."_
- İlgili: `iteration-review-prep`, `demo-script`, `roadmap`, `feature-adoption-review`, `meeting-agenda`
- Dosya: [skills/02-product/product-owner/planning/stakeholder-review-prep/SKILL.tr.md](skills/02-product/product-owner/planning/stakeholder-review-prep/SKILL.tr.md)

## Proje ve Teslimat Yönetimi

### Proje Yöneticisi

#### Başlatma

**Proje başlatma belgesi** · `project-charter`

- Ne zaman: Projeyi resmi olarak yetkilendiren proje başlatma belgesini (project charter) hazırlar; amaç, ölçülebilir hedefler, üst düzey kapsam, kilit paydaşlar, bütçe zarfı, kilometre taşları, riskler ve proje yöneticisinin yetkilerini içerir. Bir proje onaylandığında ya da onay beklerken sponsor tarafından imzalanacak tek belgelik bir yetki metni gerektiğinde kullanılır.
- Örnek istek: _"Şirket içi CRM'imizi SaaS platforma taşıma projesi için proje başlatma belgesi yaz; sponsor Satış Direktörü, hedef canlıya geçiş 2. çeyrek."_
- İlgili: `scope-statement`, `stakeholder-register`, `kickoff-deck`, `business-model-canvas`, `governance-framework`
- Dosya: [skills/03-delivery/project-manager/initiation/project-charter/SKILL.tr.md](skills/03-delivery/project-manager/initiation/project-charter/SKILL.tr.md)

**Kapsam tanımı yazma** · `scope-statement`

- Ne zaman: Kapsam içi ve dışı işleri, kabul kriterleriyle teslimatları, kısıtları, varsayımları ve hariç tutulanları tanımlayan, değişiklik kontrolü için baz çizgisi oluşturan proje kapsam tanımını yazar. Başlatma belgesi hazır olduğunda kapsamın planlama, tahmin ve sözleşme yapılabilecek netliğe getirilmesi gerektiğinde ya da kapsam kaymasına karşı açık bir referans gerektiğinde kullanılır.
- Örnek istek: _"Bu başlatma belgesine ve çalıştay notlarına göre müşteri self-servis portalı projesi için kapsam tanımı yaz."_
- İlgili: `project-charter`, `wbs`, `change-control`, `acceptance-certificate`, `statement-of-work`
- Dosya: [skills/03-delivery/project-manager/initiation/scope-statement/SKILL.tr.md](skills/03-delivery/project-manager/initiation/scope-statement/SKILL.tr.md)

**Proje açılış toplantısı hazırlığı** · `kickoff-deck`

- Ne zaman: Proje açılış toplantısını hazırlar; ekip ve sponsorlar için hedefleri, kapsamı, ekip ve rolleri, plan ve kilometre taşlarını, çalışma biçimini, riskleri ve ilk adımları içeren süreli gündem ile slayt slayt içerik üretir. Bir proje başlamak üzereyken ya da yeni bir faz veya büyük ekip değişikliği ortak bir başlangıç gerektirdiğinde kullanılır.
- Örnek istek: _"Veri ambarı modernizasyon projemizin açılış toplantısını hazırla: 20 kişi, sponsor ilk 30 dakikaya katılıyor."_
- İlgili: `project-charter`, `scope-statement`, `stakeholder-register`, `communication-plan`, `meeting-agenda`
- Dosya: [skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.tr.md](skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.tr.md)

**Paydaş kaydı** · `stakeholder-register`

- Ne zaman: Her paydaşın rolünü, ilgisini, etkisini, mevcut ve hedeflenen katılımını, temel kaygılarını ve iletişim ihtiyaçlarını, grup bazında katılım stratejisiyle birlikte listeleyen proje paydaş kaydını oluşturur. Proje başladığında, yeni taraflar katıldığında ya da bir grubun direnci veya sessizliği katılımın bilinçli planlanması gerektiğini gösterdiğinde kullanılır.
- Örnek istek: _"Üç fabrikaya ERP geçişimiz için paydaş kaydı oluştur; organizasyon şeması ve başlatma belgesi ekte."_
- İlgili: `stakeholder-identification`, `stakeholder-map`, `raci-matrix`, `communication-plan`, `project-charter`
- Dosya: [skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.tr.md](skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.tr.md)

#### Planlama

**İş kırılım yapısı (WBS)** · `wbs`

- Ne zaman: Proje kapsamını numaralı bir iş paketi hiyerarşisine bölen, teslimat odaklı bir iş kırılım yapısı (WBS) ve açıklama, sahip, kabul ve bağımlılıkları içeren WBS sözlüğü oluşturur. Kapsam üzerinde anlaşıldığında ve tahmin, takvim, kaynak planlama ve ilerleme takibi için bölünmesi gerektiğinde kullanılır.
- Örnek istek: _"Bu kapsam tanımını kullanarak mobil bankacılık uygulaması yeniden tasarımı için WBS oluştur."_
- İlgili: `scope-statement`, `estimation-three-point`, `schedule-plan`, `resource-plan`, `task-breakdown`
- Dosya: [skills/03-delivery/project-manager/planning/wbs/SKILL.tr.md](skills/03-delivery/project-manager/planning/wbs/SKILL.tr.md)

**Üç noktalı (PERT) tahmin** · `estimation-three-point`

- Ne zaman: Her iş öğesi için üç noktalı tahmin (iyimser, en olası, kötümser) üretir ve bunları PERT veya üçgen dağılım formülleriyle beklenen değer, standart sapma ve toplam için güven aralıklarına dönüştürür. Efor veya süre belirsiz olduğunda ve paydaşlar tek bir sayı yerine belirtilmiş bir güven düzeyiyle aralık istediğinde kullanılır.
- Örnek istek: _"Bu 12 iş paketi için üç noktalı tahmin ver ve toplamı %85 güvenle söyle."_
- İlgili: `wbs`, `schedule-plan`, `budget-plan`, `technical-estimation`, `monte-carlo-forecast`
- Dosya: [skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.tr.md](skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.tr.md)

**Proje takvimi oluşturma** · `schedule-plan`

- Ne zaman: İş paketlerini bağımlılık türleri ve gecikmeleriyle sıralayarak, süreleri atayarak, kilometre taşlarını belirleyerek, kritik yolu ve bolluğu hesaplayarak ve takvim tamponları ekleyerek proje takvimi oluşturur. WBS ve tahminler hazır olduğunda baz takvim, kritik yol veya gerçekçi bir bitiş tarihi üretilmesi ya da kontrol edilmesi gerektiğinde kullanılır.
- Örnek istek: _"Bu iş paketleri ve sürelerden bir takvim oluştur ve Haziran canlıya geçişine giden kritik yolu göster."_
- İlgili: `wbs`, `estimation-three-point`, `dependency-map`, `resource-plan`, `release-planning`
- Dosya: [skills/03-delivery/project-manager/planning/schedule-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/schedule-plan/SKILL.tr.md)

**Kaynak planı** · `resource-plan`

- Ne zaman: Zaman içinde gereken rolleri ve yetkinlikleri, dönem bazında kişi veya rol atamalarını, aşırı yüklemeleri, kapasite açıklarını ve bunları kapatma seçeneklerini (işe alım, dış kaynak, yeniden önceliklendirme, yeniden planlama) gösteren proje kaynak planını oluşturur. Takvim hazır olduğunda ekip kurulacaksa, kişiler projeler arasında paylaşılıyorsa ya da bir yetkinlik açığı planı tehdit ediyorsa kullanılır.
- Örnek istek: _"Ödeme geçidi projemizin önümüzdeki 6 ayı için kaynak planı oluştur; takvim ve müsaitlikleriyle ekip listesi ekte."_
- İlgili: `schedule-plan`, `wbs`, `budget-plan`, `raci-matrix`, `onboarding-plan-30-60-90`
- Dosya: [skills/03-delivery/project-manager/planning/resource-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/resource-plan/SKILL.tr.md)

**Proje bütçesi** · `budget-plan`

- Ne zaman: WBS ve maliyet kategorisine göre maliyet kırılımı, gerektiğinde capex/opex ayrımı, yedek pay ve yönetim rezervi ile maliyet baz çizgisini oluşturan zamana yayılmış nakit akışını içeren proje bütçesini hazırlar. Bir proje onay için bütçeye, izleme için maliyet baz çizgisine ya da kapsam veya takvim değişikliği sonrası yeniden tahmine ihtiyaç duyduğunda kullanılır.
- Örnek istek: _"Bu kaynak planı ve tedarikçi tekliflerinden yedek paylı ve aylık nakit akışlı bir proje bütçesi oluştur."_
- İlgili: `wbs`, `resource-plan`, `estimation-three-point`, `earned-value-analysis`, `cloud-cost-estimate`
- Dosya: [skills/03-delivery/project-manager/planning/budget-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/budget-plan/SKILL.tr.md)

**İletişim planı** · `communication-plan`

- Ne zaman: Her hedef kitle için hangi bilgiyi, ne zaman ve hangi sıklıkta, hangi kanaldan, kimden alacağını ve geri bildirim ile eskalasyonların nasıl geri akacağını belirleyen proje iletişim planını oluşturur. Proje başında, paydaşlar bilgisiz kaldıklarından veya aşırı yüklendiklerinden şikayet ettiğinde ya da yönetişim ve raporlama ritimleri üzerinde anlaşılması gerektiğinde kullanılır.
- Örnek istek: _"Ana bankacılık yükseltmemiz için yöneticileri, şube personelini, BT operasyonu ve tedarikçiyi kapsayan bir iletişim planı oluştur."_
- İlgili: `stakeholder-register`, `project-status-report`, `governance-framework`, `status-update`, `announcement`
- Dosya: [skills/03-delivery/project-manager/planning/communication-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/communication-plan/SKILL.tr.md)

**Risk kaydı** · `risk-register`

- Ne zaman: Neden-olay-etki biçiminde risk ifadeleri, olasılık ve etki puanları, yakınlık, sahipler, aksiyon ve tetikleyicileriyle yanıt stratejileri (kaçın, azalt, devret, kabul et, fırsatı kullan) ve kalıntı risk içeren proje risk kaydını oluşturur. Proje planlanırken, bir geçiş kapısı veya yönlendirme toplantısı öncesinde ya da yeni tehdit veya fırsatlar ortaya çıktığında kullanılır.
- Örnek istek: _"Depo yönetim sistemi geçişimiz için risk kaydı oluştur; plan ve açılış toplantısında dile getirilen kaygılar ekte."_
- İlgili: `raid-log`, `pre-mortem`, `technical-risk-review`, `it-risk-assessment`, `budget-plan`
- Dosya: [skills/03-delivery/project-manager/planning/risk-register/SKILL.tr.md](skills/03-delivery/project-manager/planning/risk-register/SKILL.tr.md)

**Bağımlılık haritası** · `dependency-map`

- Ne zaman: Projenin iç ve dış bağımlılıklarını haritalar; neyin, kimden, ne zamana kadar gerektiğini, sağlayan ve alan sahipleri, taahhüt durumunu, kritikliği ve bağımlılık kayarsa geri dönüş planını belirtir. Proje başka ekiplere, tedarikçilere, platformlara veya kararlara dayandığında ya da kaçırılan devirler kilometre taşlarını tehdit ettiğinde kullanılır.
- Örnek istek: _"Sadakat programı lansmanımızın tüm bağımlılıklarını haritala: pazarlama, POS tedarikçisi, veri ekibi ve hukuk incelemesi."_
- İlgili: `schedule-plan`, `raid-log`, `cross-team-dependency-board`, `risk-register`, `integration-requirements`
- Dosya: [skills/03-delivery/project-manager/planning/dependency-map/SKILL.tr.md](skills/03-delivery/project-manager/planning/dependency-map/SKILL.tr.md)

#### İzleme ve Kontrol

**Proje durum raporu** · `project-status-report`

- Ne zaman: Genel ve boyut bazında RAG durumunu (takvim, maliyet, kapsam, kalite, kaynak), kilometre taşlarına göre ilerlemeyi, sapma açıklamalarını, öncelikli riskleri ve sorunları ve sponsorlardan gereken kararları içeren dönemsel proje durum raporunu yazar. Sponsorlara veya yönlendirme kurullarına haftalık ya da aylık raporlamada veya proje sağlığının plan ve gerçekleşme verisinden nesnel olarak özetlenmesi gerektiğinde kullanılır.
- Örnek istek: _"İK sistemi projesinin bu ayki durum raporunu bu kilometre taşı güncellemeleri, bütçe gerçekleşmeleri ve RAID kaydından yaz."_
- İlgili: `status-update`, `steering-committee-pack`, `earned-value-analysis`, `raid-log`, `executive-summary`
- Dosya: [skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.tr.md)

**RAID kaydı tutma** · `raid-log`

- Ne zaman: Riskleri, Varsayımları, Sorunları ve Bağımlılıkları tutarlı numaralar, sahipler, tarihler, durumlar ve çapraz bağlantılarla tek yerde izleyen RAID kaydını oluşturur veya günceller ve neyin değiştiğine ve neyin dikkat gerektirdiğine dair kısa bir özet üretir. Süregelen proje kontrolünde, ham notların, toplantı çıktılarının veya e-postaların doğru RAID kategorisine ayrılması gerektiğinde ya da durum raporlamasından önce kullanılır.
- Örnek istek: _"Bugünkü yönlendirme toplantısı notlarındaki maddelerle RAID kaydımızı güncelle ve neyin eskale edilmesi gerektiğini söyle."_
- İlgili: `risk-register`, `issue-management`, `dependency-map`, `decision-log`, `project-status-report`
- Dosya: [skills/03-delivery/project-manager/monitoring/raid-log/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/raid-log/SKILL.tr.md)

**Kazanılmış değer analizi** · `earned-value-analysis`

- Ne zaman: Maliyet yüklü bir temel plan ve ilerleme verisinden kazanılmış değer analizi yapar; PV, EV, AC, SV, CV, SPI, CPI, EAC, ETC, VAC ve TCPI değerlerini hesaplar, sapmaları yorumlar ve varsayımlarını belirterek tamamlanma maliyetini ve tarihini öngörür. Bütçe ve takvim temeli olan bir projede nesnel performans okuması, tamamlanmadaki maliyet tahmini ya da durum raporu veya yönlendirme kararı için kanıt gerektiğinde kullanılır.
- Örnek istek: _"İş paketi bazında temel planımız, bu ayın gerçekleşen maliyetleri ve tamamlanma yüzdeleri ekte. Kazanılmış değer analizi yap ve bütçe içinde bitirip bitiremeyeceğimizi söyle."_
- İlgili: `budget-plan`, `schedule-plan`, `project-status-report`, `change-control`, `monte-carlo-forecast`
- Dosya: [skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.tr.md)

**Değişiklik kontrolü** · `change-control`

- Ne zaman: Bir değişiklik talebini değişiklik kontrolünden geçirir; talebi kaydeder, kapsam, takvim, maliyet, kalite, risk ve sözleşme üzerindeki etkisini değerlendirir, seçenekleri ortaya koyar, doğru karar merciine yönlendirir ve değişiklik kaydını ve temel planları günceller. Onaylı kapsam, tarih veya bütçeye ekleme, çıkarma ya da değişiklik istendiğinde, bir tedarikçi değişiklik talebi sunduğunda veya kapsam kaymasının görünür kılınıp karara bağlanması gerektiğinde kullanılır.
- Örnek istek: _"Müşteri artık kararlaştırılan girişe ek olarak kendi Azure AD'leriyle SSO istiyor. Değişiklik kurulu için etki değerlendirmeli bir değişiklik talebi hazırla."_
- İlgili: `scope-statement`, `impact-analysis`, `raid-log`, `decision-log`, `earned-value-analysis`
- Dosya: [skills/03-delivery/project-manager/monitoring/change-control/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/change-control/SKILL.tr.md)

**Sorun yönetimi** · `issue-management`

- Ne zaman: Tek bir proje sorununu kayıttan kapanışa kadar yönetir; sorunu net biçimde tanımlar, etkisini ve aciliyetini değerlendirir, nedenini bulur, sahip ve tarihlerle çözüm planı kurar, eskalasyon tetikleyicilerini ve kapanış kriterlerini belirler ve doğrulanmış çözüme kadar izler. Engellenen bir ekip, aksayan bir bağımlılık, tedarikçi gecikmesi veya gerçekleşmiş bir risk gibi, şu anda ters giden ve kapsamı, takvimi, maliyeti ya da kaliteyi etkileyen bir durum olduğunda kullanılır.
- Örnek istek: _"Test ortamımız 4 gündür çalışmıyor ve tedarikçi sürekli erteliyor. Bunu bir sorun olarak kaydedip eskalasyon yoluyla yönetmeme yardım et."_
- İlgili: `raid-log`, `escalation-message`, `five-whys`, `change-control`, `decision-log`
- Dosya: [skills/03-delivery/project-manager/monitoring/issue-management/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/issue-management/SKILL.tr.md)

**Tedarikçi performans değerlendirmesi** · `vendor-status-review`

- Ne zaman: Bir tedarikçinin teslimat performansını sözleşmeye veya iş tanımına (SOW) göre değerlendirir; teslimatlar ve kilometre taşları, SLA ve KPI sonuçları, kalite, kadro, faturalar ve her iki tarafın açık yükümlülüklerini inceler ve kanıta dayalı puanlı bir değerlendirme, sorunlar ve kararlaştırılan aksiyonlar üretir. Dönemsel tedarikçi yönetişim toplantısı öncesinde, bir tedarikçi geciktiğinde, bir fatura veya kilometre taşı ödemesi onaylanmadan önce ya da eskalasyon veya sözleşme yaptırımlarına karar verirken kullanılır.
- Örnek istek: _"SOW kilometre taşlarını, uygulama ortağımızın durum raporunu ve SLA raporumuzu kullanarak aylık performans değerlendirmesini hazırla."_
- İlgili: `statement-of-work`, `sla-breach-analysis`, `issue-management`, `acceptance-certificate`, `vendor-evaluation`
- Dosya: [skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.tr.md)

#### Kapanış

**Proje kapanış raporu** · `project-closure-report`

- Ne zaman: Sonuçları özgün hedefler ve temel planlarla karşılaştıran, kapsam, takvim, maliyet ve kalite sapmalarını açıklayan, kabulü ve operasyona devri teyit eden, açık maddeleri sahipleriyle listeleyen, öğrenilen dersleri kaydeden ve fayda takibini kuran bir proje kapanış raporu yazar. Bir proje veya faz sona ererken, sponsorun resmî bir kapanış kararına ihtiyacı olduğunda ya da iptal edilen bir projenin düzenli biçimde kapatılması gerektiğinde kullanılır.
- Örnek istek: _"CRM taşıma projemiz geçen ay canlıya çıktı. Proje başlatma belgesi, son durum raporu ve gerçekleşen bütçeden kapanış raporunu yaz."_
- İlgili: `acceptance-certificate`, `handover-document`, `lessons-learned`, `benefits-realization`, `earned-value-analysis`
- Dosya: [skills/03-delivery/project-manager/closure/project-closure-report/SKILL.tr.md](skills/03-delivery/project-manager/closure/project-closure-report/SKILL.tr.md)

**Teslimat kabul belgesi** · `acceptance-certificate`

- Ne zaman: Neyin teslim edildiğini, kararlaştırılan kabul kriterlerini ve her birinin kanıtını, açık hataları ve kabul edilen sapmaları, koşullu kabul şartlarını ve yetkili tarafların onaylarını kayıt altına alan bir teslimat kabul belgesi hazırlar. Bir teslimatın, kilometre taşının veya fazın müşteri, sponsor ya da iş sahibi tarafından resmî olarak kabul edilmesi gerektiğinde, bir kilometre taşı ödemesinden önce veya bir tedarikçi teslimatının kayıtlı olarak kabul ya da reddedilmesi gerektiğinde kullanılır.
- Örnek istek: _"2. kilometre taşı (raporlama modülü) için kabul belgesini hazırla. UAT tamamlandı, 3 küçük hata açık; müşteri koşullu imzalamak istiyor."_
- İlgili: `acceptance-criteria`, `uat-plan`, `statement-of-work`, `project-closure-report`, `change-control`
- Dosya: [skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.tr.md](skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.tr.md)

### Scrum Master / Çevik Koç

#### Ekip Etkinlikleri

**İterasyon planlaması kolaylaştırma** · `iteration-planning`

- Ne zaman: Bir iterasyon/sprint planlama oturumunu baştan sona kolaylaştırır: gerçekçi kapasiteyi hesaplar, iterasyon hedefini teyit eder, kapasiteye sığan işi seçip görevlere böler, riskleri ve ortaya çıkan planı kaydeder. Ekip yeni bir iterasyona/sprint'e başlamak üzereyken, planlama gündemi veya kapasite hesabı istendiğinde ya da geçmiş planlar sürekli aşırı taahhütle bittiğinde kullanılır.
- Örnek istek: _"2 haftalık sprint için 6 geliştiricili sprint planlamasını yürütmeme yardım et; biri 3 gün izinli ve son gün sürüm dondurma var. En üstteki 12 backlog maddesi ekte."_
- İlgili: `iteration-goal`, `estimation-session`, `velocity-analysis`, `task-breakdown`, `definition-of-ready`
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.tr.md)

**Günlük toplantı özeti** · `daily-sync-summary`

- Ne zaman: Günlük ekip toplantısının (stand-up) notlarını veya dökümünü; iterasyon hedefine göre ilerlemeyi, günün planını, sahipli engelleri ve takip görüşmelerini kişi ve ekip bazında veren kısa bir özete dönüştürür. Stand-up notları, asenkron güncelleme mesajları veya toplantı dökümü paylaşılıp özet, engel listesi ya da katılmayanlar için bilgi istendiğinde kullanılır.
- Örnek istek: _"Bu notlardan bugünkü stand-up'ı özetle ve engelleri listele: Emre ödeme API mock'unu bitirdi, test ortamı sertifikasında takıldı; Selin Emre'nin PR'ını inceliyor, sonra iade akışına başlayacak..."_
- İlgili: `impediment-tracking`, `meeting-summary`, `action-item-extraction`, `burndown-analysis`, `iteration-goal`
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.tr.md)

**İterasyon değerlendirmesi hazırlığı** · `iteration-review-prep`

- Ne zaman: Bir iterasyon/sprint değerlendirmesini hazırlar: artımı iterasyon hedefine göre özetler, demoyu kullanıcı senaryoları etrafında sıralar, yapılmayanları ve nedenlerini belirtir, hedefli geri bildirim soruları ve backlog etkisi soruları taslaklar. Ekibin iterasyon değerlendirmesi, sprint review veya iterasyon sonu demosu yaklaştığında ve gündem, demo sırası veya artım özeti istendiğinde kullanılır.
- Örnek istek: _"Perşembe günkü sprint review'ı hazırla. Hedef 'üye işyerleri kısmi iade yapabilir' idi. Biten: iade API, iade arayüzü, e-posta bildirimi. Bitmeyen: iade raporu. Finans ve destekten 8 paydaş gelecek."_
- İlgili: `stakeholder-review-prep`, `demo-script`, `iteration-goal`, `burndown-analysis`, `retrospective-facilitation`
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.tr.md)

**Retrospektif kolaylaştırma** · `retrospective-facilitation`

- Ne zaman: Bir ekip retrospektifini baştan sona planlar ve yürütür: ortamı hazırlar, veri toplar, içgörü üretir, not al ve oyla yöntemiyle yakınsar, az sayıda sahipli ve doğrulanabilir iyileştirme aksiyonu çıkarır ve önceki aksiyonları takip eder. Retrospektif zamanı geldiğinde, retro panosu notları paylaşılıp aksiyon istendiğinde veya geçmiş retroların aksiyonları hiç hayata geçmediğinde kullanılır.
- Örnek istek: _"Sprint retromuzu yürüt: 7 kişilik uzaktan ekip, 60 dakika. Geçen sprint iki üretim olayı ve çok fazla bağlam değiştirme yaşandı. Önceki retro aksiyonları: incelemelerde eşli çalışma (yapılmadı), kararsız testleri düzeltme (yapıldı)."_
- İlgili: `retrospective-format`, `team-health-check`, `working-agreement`, `five-whys`, `impediment-tracking`
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.tr.md)

**Retrospektif formatı tasarlama** · `retrospective-format`

- Ne zaman: Ekibin o anki ruh haline, konuya, büyüklüğüne ve ortamına uygun bir retrospektif formatı tasarlar: her retro aşaması için etkinlik seçer veya uyarlar, yönergeleri, süreleri ve malzemeleri yazar, formatın neden uygun olduğunu açıklar. Retrolar tekdüzeleştiğinde, belirli bir tema (olay, çatışma, kilometre taşı, yeni ekip) için özel bir retro gerektiğinde veya yeni bir retro fikri ya da şablonu istendiğinde kullanılır.
- Örnek istek: _"Retrolarımız sıkıcı hale geldi ve hep aynı üç kişi konuşuyor. Zor bir sürümden sonra yorgun, 9 kişilik ekip için 45 dakikalık uzaktan bir retro formatı tasarla."_
- İlgili: `retrospective-facilitation`, `team-health-check`, `workshop-plan`, `facilitation-guide`, `conflict-resolution`
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.tr.md)

**Göreli tahmin oturumu** · `estimation-session`

- Ne zaman: Göreli tahmin oturumunu (planning poker, tişört bedeni, benzerlik tahmini) hazırlar ve yönlendirir: ölçeği seçer, referans hikaye merdiveni kurar, varsayımları ortaya çıkaran tahmin turlarını yürütür ve boyutları, dağılımı ve takip işlerini kaydeder. Ekip backlog maddelerini boyutlandırmak, yeni bir ölçeği kalibre etmek veya yavaş tahmin toplantılarını hızlandırmak istediğinde ya da planning poker veya tişört bedeni oturumunun nasıl yürütüleceği sorulduğunda kullanılır.
- Örnek istek: _"Yeni onboarding epic'i için boyutlandırılmamış 25 hikayemiz ve 1 saatlik bir oturumumuz var. Ekip yeni ve referans hikaye yok. Nasıl tahmin yapalım?"_
- İlgili: `backlog-refinement`, `story-splitting`, `technical-estimation`, `velocity-analysis`, `iteration-planning`
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.tr.md)

#### Akış ve Metrikler

**Hız/verim analizi** · `velocity-analysis`

- Ne zaman: Bir ekibin hız (iterasyon başına puan) veya verim (hafta/iterasyon başına madde) geçmişini analiz eder: trend, değişkenlik, aykırı değerler ve nedenleri ile kalan iş için aralık tabanlı bir öngörü üretir. İterasyon veya verim rakamları paylaşılıp ekibin hızlanıp yavaşladığı, ne kadar öngörülebilir olduğu ya da bir backlog'un kaç iterasyon süreceği sorulduğunda kullanılır.
- Örnek istek: _"Son 10 sprint hızımız: 21, 34, 29, 18, 31, 33, 12, 30, 28, 32. Sürümde 180 puan kaldı. Bu bize ne söylüyor ve ne zaman bitirebiliriz?"_
- İlgili: `monte-carlo-forecast`, `burndown-analysis`, `cycle-time-analysis`, `release-planning`, `engineering-metrics-review`
- Dosya: [skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.tr.md)

**Burndown/burnup analizi** · `burndown-analysis`

- Ne zaman: Bir iterasyon veya sürüm için burndown ve burnup grafiklerini ya da bunların günlük verisini yorumlar: grafiğin şeklini okur, ilerlemeyi kapsam değişikliğinden ayırır, geç düşüş, yatay çizgi ve kapsam kayması gibi örüntüleri tespit eder, riskleri önerilen aksiyonlarla işaretler. Biri burndown/burnup grafiği veya günlük kalan iş rakamlarını paylaştığında ya da iterasyonun veya sürümün yolunda olup olmadığını sorduğunda kullanılır.
- Örnek istek: _"Sprintin 10 gününden 7.'sindeyiz. Günlere göre kalan puan: 40, 40, 38, 38, 38, 35, 35. 4. gün iki hikâye eklendi. Yetişecek miyiz?"_
- İlgili: `velocity-analysis`, `monte-carlo-forecast`, `daily-sync-summary`, `iteration-planning`, `project-status-report`
- Dosya: [skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.tr.md)

**Döngü/teslim süresi analizi** · `cycle-time-analysis`

- Ne zaman: İş maddelerinin başlangıç/bitiş tarihlerinden döngü süresini (cycle time) ve teslim süresini (lead time) analiz eder: yüzdelikleri hesaplar, dağılımı okur, durumda geçen süreden darboğaz durumları bulur, devam eden işleri geçmiş yüzdeliklere göre yaşlanma açısından işaretler ve bir hizmet seviyesi beklentisi önerir. Madde başlangıç/bitiş tarihleri veya pano durum geçmişi paylaşılıp işin ne kadar sürdüğü, nerede beklediği ya da hangi maddelerin takılma riski taşıdığı sorulduğunda kullanılır.
- Örnek istek: _"Başlangıç ve bitiş tarihleriyle 40 biten madde ve başlangıç tarihleriyle devam eden 9 madde var. İşimiz ne kadar sürüyor ve ne takılmış?"_
- İlgili: `wip-policy`, `monte-carlo-forecast`, `velocity-analysis`, `value-stream-map`, `engineering-metrics-review`
- Dosya: [skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.tr.md)

**WIP limiti ve akış kuralları** · `wip-policy`

- Ne zaman: Bir panoyu ve akış kurallarını tasarlar: bekleme durumları dahil gerçek iş akışını yansıtan kolonlar, kolon veya kişi başına devam eden iş (WIP) limitleri, açık giriş ve çıkış kriterleri, hizmet sınıfları, bloke ve yaşlanan madde kuralları ve limitlerin ayarlanması için bir gözden geçirme sıklığı. Bir ekip panosunu kurarken veya yeniden tasarlarken, çok iş başlatılıp az iş bitiyorken ya da hangi WIP limitlerinin ve çekme kurallarının kullanılacağı sorulduğunda kullanılır.
- Örnek istek: _"6 geliştirici ve 1 test uzmanıyız, her şey 'devam ediyor' ve hiçbir şey bitmiyor. Pano kolonlarını ve WIP limitlerini belirlememize yardım et."_
- İlgili: `cycle-time-analysis`, `working-agreement`, `definition-of-ready`, `definition-of-done`, `impediment-tracking`
- Dosya: [skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.tr.md)

**Monte Carlo ile teslim tahmini** · `monte-carlo-forecast`

- Ne zaman: Geçmiş verim (throughput) verisinden Monte Carlo simülasyonuyla olasılıksal teslim öngörüsü üretir: 'N madde ne zaman biter?' veya 'D tarihine kadar kaç madde biter?' sorularını güven seviyeleriyle (%50/85/95) yanıtlar, backlog büyümesini ve bölünmeyi hesaba katar, yöntemi ve uyarıları açıklar. Haftalık veya iterasyon başına verim paylaşılıp sürüm tarihi, bir son tarih için kapsam öngörüsü ya da bir taahhüdü tutturma olasılığı sorulduğunda kullanılır.
- Örnek istek: _"Son 12 haftadaki haftalık verimimiz: 3, 5, 4, 0, 6, 4, 5, 3, 7, 4, 2, 5. 38 madde kaldı. %85 güvenle ne zaman bitiririz?"_
- İlgili: `velocity-analysis`, `cycle-time-analysis`, `release-planning`, `burndown-analysis`, `schedule-plan`
- Dosya: [skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.tr.md)

**Engel takibi** · `impediment-tracking`

- Ne zaman: Bir engel kaydı oluşturur ve sürdürür: her engeli bloke ettiği iş, etkisi, sorumlusu ve sonraki aksiyonuyla kaydeder, kaldırmak için neye ihtiyaç duyulduğuna göre (ekip, başka ekip, yönetim, dış taraf) sınıflandırır, süre eşikleriyle bir eskalasyon basamağı uygular ve tekrarlayan sistemik nedenleri ortaya çıkarır. Ekip günlük senkronda engel bildirdiğinde, iş başkalarını beklerken takıldığında ya da açık engellerin düzenlenmesi, eskale edilmesi veya raporlanması istendiğinde kullanılır.
- Örnek istek: _"Bu haftaki senkronlardan çıkan engeller: test ortamı salıdan beri çalışmıyor, güvenlik ekibinin firewall kuralı onayını bekliyoruz, product owner iade kurallarına dönmedi. Düzenle ve neyi eskale etmem gerektiğini söyle."_
- İlgili: `daily-sync-summary`, `escalation-message`, `cross-team-dependency-board`, `raid-log`, `retrospective-facilitation`
- Dosya: [skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.tr.md)

#### Ekip Gelişimi

**Ekip çalışma sözleşmesi** · `working-agreement`

- Ne zaman: Ekip çalışma sözleşmesini kolaylaştırır ve yazar: iletişim kanalları ve yanıt süreleri, erişilebilirlik ve ortak çalışma saatleri, kod incelemesi ve eşli çalışma, toplantılar, karar alma, nöbet ve çatışma yönetimine dair normları toplar, bunları somut ve gözlemlenebilir taahhütlere dönüştürür, sözleşmenin nasıl gözden geçirilip uygulanacağını belirler. Ekip kurulduğunda veya değiştiğinde, tekrarlayan sürtünmeler (yavaş incelemeler, toplantı yükü, mesai dışı mesajlar) görüldüğünde ya da ekip tüzüğü veya temel kurallar istendiğinde kullanılır.
- Örnek istek: _"Ekibimiz artık İstanbul ve Berlin arasında bölünmüş durumda, incelemeler günlerce bekliyor ve insanlara gece mesaj atılıyor. Bir çalışma sözleşmesi taslağı hazırlamamıza yardım et."_
- İlgili: `wip-policy`, `team-health-check`, `retrospective-facilitation`, `definition-of-done`, `conflict-resolution`
- Dosya: [skills/03-delivery/agile-delivery/team/working-agreement/SKILL.tr.md](skills/03-delivery/agile-delivery/team/working-agreement/SKILL.tr.md)

**Ekip sağlık kontrolü** · `team-health-check`

- Ne zaman: Bir ekip sağlık kontrolünü tasarlar ve analiz eder: 8-12 boyut seçer (ör. değer teslimi, hız, kod tabanı sağlığı, öğrenme, misyon netliği, keyif, destek, psikolojik güvenlik), trafik ışığı veya 1-5 derecelendirme ifadeleri yazar, anonim yürütür, sonuçları ve boyut bazında trendleri okur, en düşük veya düşen alanları sahibi belli az sayıda takip aksiyonuna dönüştürür. Bir ekip veya yönetici ekibin nabzını ölçmek, önceki turla karşılaştırmak ya da bir sağlık kontrolü oturumu hazırlamak istediğinde kullanılır.
- Örnek istek: _"Geçen çeyrek ve bu çeyrek 10 boyuttaki sağlık kontrolü sonuçlarımız burada (kişi başı yeşil/sarı/kırmızı). Ne öne çıkıyor ve ne yapmalıyız?"_
- İlgili: `retrospective-facilitation`, `working-agreement`, `agile-maturity-assessment`, `questionnaire-design`, `engineering-metrics-review`
- Dosya: [skills/03-delivery/agile-delivery/team/team-health-check/SKILL.tr.md](skills/03-delivery/agile-delivery/team/team-health-check/SKILL.tr.md)

**Çeviklik olgunluk değerlendirmesi** · `agile-maturity-assessment`

- Ne zaman: Bir ekibin veya birimin çeviklik olgunluğunu metodolojiden bağımsız biçimde değerlendirir: pratik alanlarını (müşteri değeri ve ürün sahipliği, planlama ve öngörü, akış ve teslimat, teknik pratikler, kalite, sürekli iyileştirme, ekip özerkliği, paydaş iş birliği) kanıta dayalı 1-5 ölçeğinde puanlar, ortalama almak yerine kısıtı belirler ve gözlemlenebilir sonuçlarla sonraki 2-3 iyileştirmeyi önerir. Bir lider veya koç ekibin gerçekte ne kadar çevik olduğunu sorduğunda, bir dönüşüm öncesi başlangıç değeri gerektiğinde ya da sırada neyin iyileştirileceğine karar verilmek istendiğinde kullanılır.
- Örnek istek: _"Ekibimizin çeviklik olgunluğunu değerlendir. İki haftalık iterasyonlarla çalışıyoruz, sürümler üç ayda bir çıkıyor, product owner yarı zamanlı ve test otomasyonu yok."_
- İlgili: `team-health-check`, `retrospective-facilitation`, `wip-policy`, `engineering-metrics-review`, `current-state-assessment`
- Dosya: [skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.tr.md](skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.tr.md)

### Program Yöneticisi / PMO

#### Portföy ve Program

**Proje portföyü önceliklendirme** · `portfolio-prioritization`

- Ne zaman: Bir proje veya girişim portföyünü değer, stratejik uyum, risk ve efor üzerinden puanlayarak önceliklendirir; sıralamayı gerçek kapasite ve bağımlılıklarla sınar ve her biri için gerekçeli fonla / sıraya al / durdur önerisi üretir. Kapasiteden fazla girişim olduğunda, yıllık veya çeyreklik portföy planlamasında, yeni bir talebin yerleştirilmesi gerektiğinde ya da yönetim \"neyi fonlayalım, neyi durduralım\" diye sorduğunda kullanılır.
- Örnek istek: _"Önümüzdeki yıl için bu 12 girişimi önceliklendir; yaklaşık 6 teslimat ekibimiz var ve strateji dijital satışı büyütmek ve işletme maliyetini düşürmek."_
- İlgili: `decision-matrix`, `cost-benefit-analysis`, `okr-definition`, `program-roadmap`, `steering-committee-pack`
- Dosya: [skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.tr.md)

**Program yol haritası** · `program-roadmap`

- Ne zaman: Birden fazla ekibin veya projenin işini ortak sonuçlara doğru sıralayan; ekipler arası kilometre taşlarını, entegrasyon noktalarını, karar kapılarını ve kritik yolu sahte kesinlik yerine güven düzeyleriyle gösteren bir program yol haritası oluşturur. Program birden fazla ekibe veya tedarikçiye yayıldığında, yönetim paralel iş akışlarının nasıl birleştiğini tek görünümde görmek istediğinde ya da program düzeyinde plan, zaman çizelgesi veya bütünleşik yol haritası istendiğinde kullanılır.
- Örnek istek: _"Çekirdek bankacılık geçişimiz için program yol haritası oluştur: 5 ekip, bir tedarikçi ve 4. çeyrekte yasal zorunlu canlıya geçiş var."_
- İlgili: `cross-team-dependency-board`, `portfolio-prioritization`, `roadmap`, `release-planning`, `schedule-plan`
- Dosya: [skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.tr.md)

**Ekipler arası bağımlılık planlaması** · `cross-team-dependency-board`

- Ne zaman: Ekipler arası bağımlılık planlamasını yürütür; ekipler arasındaki her bağımlılığı ortaya çıkarır, her birini açık hale getirir (sağlayan, tüketen, ne, gereken tarih), bir taahhüt ya da alternatif üzerinde müzakere eder ve eskalasyon kurallarıyla ortak bir panoda durumunu izler. Birden fazla ekip aynı dönemi birlikte planlarken, bir program ekipler arası beklemeler yüzünden sürekli kayarken veya ekipler arası bağımlılıkların haritalanması, müzakere edilmesi ya da izlenmesi istendiğinde kullanılır.
- Örnek istek: _"Önümüzdeki çeyreğin planlaması için bir bağımlılık panosu kur; 4 ekip var ve ödeme adımı ekibi neredeyse her şey için ödeme ve kimlik ekiplerine bağımlı."_
- İlgili: `dependency-map`, `program-roadmap`, `raid-log`, `escalation-message`, `negotiation-prep`
- Dosya: [skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.tr.md)

**Yönlendirme kurulu sunumu** · `steering-committee-pack`

- Ne zaman: Gereken kararlarla başlayan, ardından baz plana göre kısa durum, başlıca riskler ve sorunlar, finansal durum (bütçe, gerçekleşen, tahmin) ve fayda görünümünü veren, her karar için seçenekler ve öneri içeren bir yönlendirme kurulu sunumu hazırlar. Bir yönlendirme kurulu, proje kurulu veya sponsor değerlendirmesi öncesinde, aylık program raporunun karar odaklı bir pakete dönüştürülmesi gerektiğinde ya da bir proje veya program için \"steerco sunumu\" veya \"kurul güncellemesi\" hazırlanması istendiğinde kullanılır.
- Örnek istek: _"Gelecek perşembe için yönlendirme kurulu sunumunu hazırla: entegrasyon testinde 3 hafta gerideyiz, bütçeyi %8 aştık ve raporlama modülünün kapsamdan çıkarılması için karar gerekiyor."_
- İlgili: `project-status-report`, `executive-summary`, `raid-log`, `decision-log`, `presentation-outline`
- Dosya: [skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.tr.md)

**Proje yönetişimi tanımlama** · `governance-framework`

- Ne zaman: Riskine göre boyutlandırılmış proje veya program yönetişimini tanımlar: karar türüne göre karar yetkileri, üyeliği ve yetki alanı belli kurullar, giriş kriterli aşama veya karar kapıları, toleranslar ve eskalasyon yolları ile her kurulu besleyen raporlama sıklığı. Yeni bir proje veya program kurulurken, kararlar tıkandığında ya da yanlış yerde alındığında, bir denetim veya sponsor \"kim neye karar veriyor\" diye sorduğunda ya da mevcut yönetişim fazla ağır veya fazla hafif olduğunda kullanılır.
- Örnek istek: _"Dış bir entegratörün, üç iş biriminin ve halihazırda var olan bir BT yönlendirme kurulunun yer aldığı 14 aylık ERP değişim programı için yönetişim tanımla."_
- İlgili: `raci-matrix`, `steering-committee-pack`, `project-charter`, `change-control`, `communication-plan`
- Dosya: [skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.tr.md)

**Fayda gerçekleşme takibi** · `benefits-realization`

- Ne zaman: Teslimat sonrası fayda gerçekleşmesini izler; planlanan faydaları baz değer, hedef, sahip ve ölçüm tarihleri olan ölçülebilir göstergelere dönüştürür, planlanan ve gerçekleşen değerleri karşılaştırır, değişimin ne kadarının girişime ait olduğunu değerlendirir ve düzeltici aksiyon ya da yeniden tahmin önerir. Bir proje veya program canlıya geçtikten sonra, uygulama sonrası veya fayda gözden geçirmesinde, iş gerekçesinin sonuçlarla karşılaştırılması gerektiğinde ya da \"vaat ettiğimiz değeri aldık mı\" diye sorulduğunda kullanılır.
- Örnek istek: _"Self-servis portalımızın canlıya geçişinden altı ay sonra fayda gerçekleşmesini kontrol et; iş gerekçesi çağrı merkezi temaslarında %30 azalma ve daha hızlı müşteri kaydı vaat ediyordu."_
- İlgili: `kpi-definition`, `cost-benefit-analysis`, `feature-adoption-review`, `project-closure-report`, `portfolio-prioritization`
- Dosya: [skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.tr.md)

## Mimari

### Kurumsal Mimar

#### Mimari Strateji

**Mimari ilkeler tanımlama** · `architecture-principles`

- Ne zaman: Kurumsal veya alan düzeyinde az sayıda mimari ilke tanımlar; her ilke için TOGAF tarzında ifade, gerekçe ve etkileri, uyumun nasıl denetleneceğini ve istisnaların nasıl yönetileceğini belirler. Kurumun mimari kararlar için yol gösterici kurallara ihtiyacı olduğunda, ilkeler içi boş sloganlara dönüştüğünde veya tasarım incelemelerinde aynı ödünleşimler tekrar tekrar tartışıldığında kullanılır.
- Örnek istek: _"Bulut-yerel ve olay güdümlü sistemlere geçişimiz için 8-10 mimari ilke tanımla; hedeflerimiz daha hızlı teslimat, daha düşük işletim maliyeti ve KVKK uyumu."_
- İlgili: `architecture-review`, `adr`, `target-state-architecture`, `technology-strategy`, `governance-framework`
- Dosya: [skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.tr.md)

**İş yetkinlik haritası** · `capability-map`

- Ne zaman: Olgunluk, stratejik önem ve ısı haritası içeren hiyerarşik bir iş yetkinlik haritası (seviye 1-3) oluşturur; uygulamaları ve sahipleri yetkinliklere eşler. Yatırım planlarken, uygulama sadeleştirmesi yaparken, bir dönüşümün kapsamını belirlerken veya BT'yi iş stratejisiyle hizalarken ya da organizasyon şemasından ve sistemlerden bağımsız olarak işin ne yaptığı sorulduğunda kullanılır.
- Örnek istek: _"Bireysel bankamız için olgunluk ve stratejik önem içeren seviye 2 yetkinlik haritası oluştur ve gelecek yıl nereye yatırım yapmamız gerektiğini vurgula."_
- İlgili: `application-portfolio-assessment`, `target-state-architecture`, `value-stream-map`, `bounded-context-map`, `portfolio-prioritization`
- Dosya: [skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.tr.md)

**Uygulama portföyü değerlendirmesi** · `application-portfolio-assessment`

- Ne zaman: Uygulama portföyünü iş uygunluğu ve teknik uygunluk açısından değerlendirir; her uygulamaya gerekçe, maliyet ve risk sinyalleriyle bir TIME kararı (Tolere et, Yatırım yap, Taşı, Kaldır) ve sıralanmış bir sadeleştirme planı atar. Uygulama sadeleştirmesinde, bütçe döneminde, bulut veya ERP programlarının planlanmasında ya da birleşme sonrası çakışan sistemler olduğunda kullanılır.
- Örnek istek: _"Sahipleri, maliyetleri ve kullanıcı sayılarıyla 40 uygulamalık listemiz ekte; bunları TIME ile sınıflandır ve önce hangilerini kaldırmamız gerektiğini öner."_
- İlgili: `capability-map`, `modernization-assessment`, `tech-debt-assessment`, `build-vs-buy`, `target-state-architecture`
- Dosya: [skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.tr.md)

**Hedef mimari tanımlama** · `target-state-architecture`

- Ne zaman: Mevcut durumu, iş, veri, uygulama ve teknoloji görünümlerinde hedef durumu, aralarındaki farkları ve bağımlılıklar ile karar noktaları içeren ara durumlardan oluşan bir geçiş yol haritasını tanımlayarak hedef mimariyi ortaya koyar. Bir dönüşüm, platform birleştirme veya çok yıllı program, mimarinin nereye gitmesi gerektiği ve oraya nasıl varılacağı konusunda ortak bir resme ihtiyaç duyduğunda kullanılır.
- Örnek istek: _"Monolitik sipariş yönetimimizi ve gece çalışan toplu entegrasyonlarımızı üç yıl içinde olay akışı kullanan alan servislerine taşımak için hedef mimariyi tanımla."_
- İlgili: `capability-map`, `architecture-principles`, `migration-strategy`, `application-portfolio-assessment`, `roadmap`
- Dosya: [skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.tr.md)

**Teknoloji radarı** · `tech-radar`

- Ne zaman: Teknolojileri çeyrekler (teknikler, platformlar, araçlar, diller ve framework'ler) boyunca Benimse, Dene, Değerlendir ve Beklet halkalarına yerleştiren bir teknoloji radarı oluşturur veya günceller; kanıta dayalı gerekçe, önceki sürüme göre hareket ve ekipler için yönlendirme içerir. Teknoloji yelpazesini standartlaştırırken, dönemsel bir radar yayınlarken veya bir ekibin yeni bir teknolojiyi kullanıp kullanamayacağına karar verirken kullanılır.
- Örnek istek: _"Teknoloji radarımızı şu önerilerle güncelle: gRPC'yi Değerlendir'den Dene'ye taşı, AngularJS'i Beklet'e al ve OpenTelemetry'yi ekle."_
- İlgili: `technology-selection`, `architecture-principles`, `technology-strategy`, `adr`, `dependency-upgrade`
- Dosya: [skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.tr.md)

### Çözüm Mimarı

#### Çözüm Tasarımı

**Çözüm mimarisi dokümanı** · `solution-architecture-document`

- Ne zaman: Gereksinimlerden ve tasarım notlarından arc42 yapısında bir çözüm mimarisi dokümanı yazar - hedefler ve kalite gereksinimleri, kısıtlar, bağlam ve kapsam, çözüm stratejisi, yapı taşları, çalışma zamanı senaryoları, dağıtım, kesişen kavramlar, kararlar, riskler ve sözlük. Bir çözümün inceleme, devir, onay veya denetim için belgelenmesi gerektiğinde ya da mevcut tasarım yalnızca slaytlarda ve kişilerin kafasında olduğunda kullanılır.
- Örnek istek: _"Yeni kredi başvuru platformumuz için çözüm mimarisi dokümanı yaz; gereksinimler, entegrasyon listesi ve beyaz tahta notlarımız ekte."_
- İlgili: `c4-model`, `adr`, `nfr-to-architecture`, `architecture-review`, `technical-design-doc`
- Dosya: [skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.tr.md](skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.tr.md)

**C4 ile mimari tanımlama** · `c4-model`

- Ne zaman: Bir yazılım sistemini C4 modeliyle - sistem bağlamı, konteyner ve faydalı olduğu yerde bileşen diyagramları - tutarlı öğe adları, sorumluluklar, teknolojiler ve etiketli ilişkilerle kod olarak diyagram (Structurizr DSL, PlantUML C4 veya Mermaid) biçiminde tanımlar. Bir tasarım, inceleme, oryantasyon veya dokümantasyon için mimari diyagram gerektiğinde ya da metinsel bir tanım veya mevcut bir taslak C4 görünümlerine dönüştürülmek istendiğinde kullanılır.
- Örnek istek: _"E-ticaret ödeme akışımız için Structurizr DSL ile C4 bağlam ve konteyner diyagramları oluştur: web mağaza, mobil uygulama, checkout API, ödeme sağlayıcı, sipariş veritabanı ve mesaj kuyruğu."_
- İlgili: `solution-architecture-document`, `diagram-as-code`, `bounded-context-map`, `adr`, `architecture-review`
- Dosya: [skills/04-architecture/solution-architect/design/c4-model/SKILL.tr.md](skills/04-architecture/solution-architect/design/c4-model/SKILL.tr.md)

**Mimari karar kaydı (ADR) yazma** · `adr`

- Ne zaman: Bağlamı, karar etkenlerini, artı ve eksileriyle değerlendirilen seçenekleri, kararı ve sonuçlarını Nygard veya MADR tarzında, durum ve yerine geçme bağlantılarıyla birlikte kaydeden bir Mimari Karar Kaydı (ADR) yazar. Mimari açıdan önemli bir karar verildiğinde veya verilmesi gerektiğinde, geçmiş bir kararın geriye dönük belgelenmesi gerektiğinde ya da bir karar geri alınırken kullanılır.
- Örnek istek: _"Sipariş servisi için MongoDB yerine PostgreSQL seçimimizle ilgili bir ADR yaz; etkenler işlemsel tutarlılık, ekip yetkinliği ve raporlama ihtiyaçları."_
- İlgili: `decision-log`, `trade-off-analysis`, `technology-selection`, `solution-architecture-document`, `architecture-principles`
- Dosya: [skills/04-architecture/solution-architect/design/adr/SKILL.tr.md](skills/04-architecture/solution-architect/design/adr/SKILL.tr.md)

**Teknoloji seçimi** · `technology-selection`

- Ne zaman: Yapılandırılmış bir teknoloji seçimi yürütür - problemin çerçevelenmesi, kalite nitelikleri, maliyet, risk ve ekosistem sağlığını içeren ağırlıklı ölçütler, uzun listeden kısa listeye iniş, geçti/kaldı kriterli bir kavram kanıtı (PoC) planı ve ADR olarak kaydedilen bir öneri. Önemli bir ihtiyaç için veritabanı, mesaj kuyruğu, framework, platform, SaaS ürünü veya kütüphane seçerken ya da bir ekibin tercih ettiği aracın nesnel olarak gerekçelendirilmesi gerektiğinde kullanılır.
- Örnek istek: _"Sipariş ve stok olayları için bir mesaj kuyruğu seçmemize yardım et; sipariş bazında sıralama, 7 gün geriye oynatma gerekiyor ve Kubernetes üzerinde çalışıyoruz."_
- İlgili: `adr`, `build-vs-buy`, `tech-radar`, `vendor-evaluation`, `spike-report`
- Dosya: [skills/04-architecture/solution-architect/design/technology-selection/SKILL.tr.md](skills/04-architecture/solution-architect/design/technology-selection/SKILL.tr.md)

**Entegrasyon deseni seçimi** · `integration-pattern-selection`

- Ne zaman: Sistemler arasındaki her etkileşim için entegrasyon desenini (senkron API, asenkron mesajlaşma, olay akışı, dosya/batch aktarımı, CDC, paylaşılan veritabanı) bağımlılık, gecikme, tutarlılık, hacim, sıralama ve hata davranışını analiz ederek seçer ve ödünleşimleri kaydeder. İki veya daha fazla sistemin veri ya da komut alışverişi tasarlanırken, noktadan noktaya veya dosya arayüzleri değiştirilirken ya da bir entegrasyon yük veya değişiklik altında sürekli bozulduğunda kullanılır.
- Örnek istek: _"Sipariş sistemi, ERP ve depo sistemi arasındaki entegrasyon desenlerini seç; ERP yalnızca SOAP ve gece dosyalarını destekliyor, depo stok güncellemesini bir dakika içinde istiyor."_
- İlgili: `integration-requirements`, `event-driven-design`, `api-contract`, `adr`, `resilience-review`
- Dosya: [skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.tr.md](skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.tr.md)

**NFR'leri mimari taktiklere eşleme** · `nfr-to-architecture`

- Ne zaman: Fonksiyonel olmayan gereksinimleri ölçülebilir kalite niteliği senaryolarına (kaynak, uyaran, ortam, eser, yanıt, yanıt ölçüsü) dönüştürür ve her birini ödünleşimleri ve doğrulama yöntemiyle birlikte mimari taktiklere eşler. NFR'ler belirsiz olduğunda (\"hızlı\", \"güvenli\", \"yüksek erişilebilir\"), bir tasarımın kalite hedeflerini nasıl karşıladığını göstermesi gerektiğinde veya mimari inceleme ya da ATAM öncesinde kullanılır.
- Örnek istek: _"Bu NFR'leri mimari taktiklere eşle: ödeme adımı hızlı olmalı, 7/24 erişilebilir olmalı, Black Friday tepe yüklerini kaldırmalı ve PCI DSS'e uymalı."_
- İlgili: `nfr-specification`, `solution-architecture-document`, `atam-evaluation`, `trade-off-analysis`, `slo-definition`
- Dosya: [skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.tr.md](skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.tr.md)

**Yap ya da satın al kararı** · `build-vs-buy`

- Ne zaman: Bir yetkinlik için kendin geliştirme, satın alma (COTS/SaaS), mevcut platformu genişletme veya açık kaynak kullanma seçeneklerini stratejik farklılaşma, fonksiyonel uygunluk, çok yıllık toplam sahip olma maliyeti, risk, değere ulaşma süresi ve çıkış maliyeti açısından karşılaştırır ve gerekçeli bir öneri üretir. Bir ekip bir yetkinliği içeride mi geliştireceğine yoksa satın mı alacağına karar vermek zorunda olduğunda veya mevcut özel bir sistem ya da ürün yenilenecekse kullanılır.
- Örnek istek: _"Müşteri bildirim servisimizi kendimiz mi geliştirelim yoksa SaaS bir ürün mü alalım? Ayda yaklaşık 2 milyon e-posta ve SMS gönderiyoruz, Türkçe ve İngilizce şablon gerekiyor."_
- İlgili: `technology-selection`, `vendor-evaluation`, `cost-benefit-analysis`, `fit-gap-analysis`, `adr`
- Dosya: [skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.tr.md](skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.tr.md)

**Tasarımın bulut maliyet tahmini** · `cloud-cost-estimate`

- Ne zaman: Bir çözüm tasarımının her bileşenini (hesaplama, depolama, veritabanı, ağ çıkışı, yönetilen servisler, gözlemlenebilirlik, lisanslar) iş yükü sürücülerinden boyutlandırır ve aralıkları, varsayımları ve maliyet düşürme kaldıraçlarıyla şeffaf bir aylık işletim maliyeti tahmini üretir. Bir tasarımın onay için maliyet rakamına ihtiyacı olduğunda, mimari seçenekler maliyetle karşılaştırılırken veya geliştirme öncesinde bulut bütçesi belirlenirken kullanılır.
- Örnek istek: _"Bu tasarımın aylık bulut maliyetini tahmin et: 6 konteynerli servis, yönetilen PostgreSQL, Redis, 5 TB doküman için nesne depolama ve ayda yaklaşık 20 milyon API çağrısı."_
- İlgili: `finops-review`, `capacity-planning`, `build-vs-buy`, `solution-architecture-document`, `budget-proposal`
- Dosya: [skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.tr.md](skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.tr.md)

#### Mimari Gözden Geçirme

**Mimari gözden geçirme** · `architecture-review`

- Ne zaman: Bir çözüm veya yazılım mimarisini iş sürücüleri, kalite niteliği gereksinimleri, mimari ilkeler, bilinen riskler ve yaygın anti-desenlere göre gözden geçirir; somut önerilerle önem derecelendirilmiş bulgular ve bir inceleme kararı üretir. Bir tasarım dokümanı, diyagram seti veya ADR'ler mimari kurul onayına sunulduğunda, büyük bir geliştirme ya da canlıya geçiş öncesinde veya bir sistemde tekrarlayan yapısal sorunlar görüldüğünde kullanılır.
- Örnek istek: _"Gelecek haftaki mimari kurul öncesinde yeni kredi başvuru platformumuzun çözüm mimarisi dokümanını gözden geçir."_
- İlgili: `architecture-principles`, `nfr-to-architecture`, `atam-evaluation`, `resilience-review`, `scalability-review`
- Dosya: [skills/04-architecture/solution-architect/review/architecture-review/SKILL.tr.md](skills/04-architecture/solution-architect/review/architecture-review/SKILL.tr.md)

**ATAM tarzı değerlendirme** · `atam-evaluation`

- Ne zaman: Architecture Tradeoff Analysis Method (ATAM) örnek alınarak bir değerlendirmeyi planlar ve belgeler; iş sürücülerini, önceliklendirilmiş kalite niteliği fayda ağacını, mimari yaklaşımların öncelikli senaryolara göre analizini ve ortaya çıkan hassasiyet noktalarını, ödünleşim noktalarını, riskleri, risk olmayanları ve risk temalarını üretir. Önemli bir mimari taahhüt öncesinde paydaşlarla değerlendirilecekse, kalite hedefleri çelişiyorsa veya bağımsız, yapılandırılmış bir değerlendirme isteniyorsa kullanılır.
- Örnek istek: _"Olay güdümlü ödeme platformumuz için ATAM tarzı bir değerlendirme hazırla; temel kaygılar gecikme, iki veri merkezinde erişilebilirlik ve denetlenebilirlik."_
- İlgili: `nfr-to-architecture`, `architecture-review`, `trade-off-analysis`, `workshop-plan`, `adr`
- Dosya: [skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.tr.md](skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.tr.md)

**Dayanıklılık incelemesi** · `resilience-review`

- Ne zaman: Bir sistemin dayanıklılığını, her kritik akışı ve bağımlılığı hata modları üzerinden geçirerek inceler; zaman aşımları, yeniden denemeler, devre kesiciler, bölmeler (bulkhead), idempotency, kademeli bozulma, veri kalıcılığı ve felaket kurtarmayı erişilebilirlik hedeflerine (SLO, RTO, RPO) göre kontrol eder. Kritik bir servis canlıya çıkmadan önce, bağımlılık hatalarından kaynaklanan olaylardan sonra, yeni bir dış bağımlılık eklenirken veya DR hazırlığının kanıtlanması gerektiğinde kullanılır.
- Örnek istek: _"Ödeme akışımızın dayanıklılığını incele: fiyatlama, stok, ödeme sağlayıcısı ve fraud servisini senkron çağırıyor; geçen ay fraud servisi yavaşladığında iki kesinti yaşadık."_
- İlgili: `chaos-experiment`, `dr-plan`, `slo-definition`, `integration-pattern-selection`, `architecture-review`
- Dosya: [skills/04-architecture/solution-architect/review/resilience-review/SKILL.tr.md](skills/04-architecture/solution-architect/review/resilience-review/SKILL.tr.md)

**Ölçeklenebilirlik incelemesi** · `scalability-review`

- Ne zaman: Bir sistemin nasıl ölçeklendiğini, yük artışını her bileşene göre modelleyerek inceler; darboğazları (CPU, I/O, kilitler, bağlantılar, sıcak bölümler, paylaşılan durum) bulur; durumsuzluk, bölümleme, önbellek, asenkron işleme ve veri katmanı limitlerini değerlendirir; önceliklendirilmiş öneriler ve mevcut tasarımın ölçekleme sınırını verir. Beklenen bir büyüme adımı veya tepe olay öncesinde, gecikme yükle birlikte bozulduğunda ya da dikey ve yatay ölçekleme arasında seçim yapılırken kullanılır.
- Örnek istek: _"Raporlama API'mizin ölçeklenebilirliğini incele; büyük bir müşteriyi aldıktan sonra trafik 5 katına çıkacak ve p95 gecikme ay sonunda şimdiden sert yükseliyor."_
- İlgili: `capacity-planning`, `performance-test-plan`, `load-test-analysis`, `resilience-review`, `query-optimization`
- Dosya: [skills/04-architecture/solution-architect/review/scalability-review/SKILL.tr.md](skills/04-architecture/solution-architect/review/scalability-review/SKILL.tr.md)

### Yazılım Mimarı

#### Alan Tasarımı

**Event storming** · `event-storming`

- Ne zaman: Genel resim (big picture) veya tasarım düzeyinde bir event storming oturumunu planlar ya da yürütür ve sonucu alan olayları, komutlar, aktörler, politikalar, okuma modelleri, dış sistemler, aggregate'ler ve sıcak noktalardan oluşan yapılandırılmış bir modele dönüştürür. Bir ekip bir iş akışını ortak şekilde anlamak, sınırlı bağlamları veya aggregate'leri keşfetmek ya da dağınık bir yapışkan not duvarını toparlamak istediğinde kullanılır.
- Örnek istek: _"Sipariş-teslimat akışımız için tasarım düzeyinde bir event storming yürütmeme yardım et ve dünkü oturumun notlarını yapılandır."_
- İlgili: `bounded-context-map`, `aggregate-design`, `event-driven-design`, `workshop-plan`, `glossary-builder`
- Dosya: [skills/04-architecture/software-architect/domain/event-storming/SKILL.tr.md](skills/04-architecture/software-architect/domain/event-storming/SKILL.tr.md)

**Sınırlı bağlam haritası** · `bounded-context-map`

- Ne zaman: Her sınırlı bağlamı, ortak dilini (ubiquitous language) ve sahipliğini adlandıran; bağlamlar arası ilişkileri (partnership, paylaşılan çekirdek, müşteri-tedarikçi, conformist, ACL, OHS, published language, ayrı yollar) upstream/downstream yönü ve entegrasyon biçimiyle sınıflandıran bir bağlam haritası üretir. Modül veya servis sınırları tanımlanırken, bir ekip sistem haritasına alıştırılırken ya da ekipler arası bağımlılık ve çeviri sorunları teşhis edilirken kullanılır.
- Örnek istek: _"Perakende platformumuz için bağlam haritası çiz: katalog, fiyatlama, sipariş, ödeme (harici PSP), depo ve CRM; dört ekip sahip."_
- İlgili: `event-storming`, `service-decomposition`, `aggregate-design`, `integration-pattern-selection`, `team-topology`
- Dosya: [skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.tr.md](skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.tr.md)

**Aggregate tasarımı** · `aggregate-design`

- Ne zaman: DDD aggregate'lerini tek işlemde (transaction) korunması gereken değişmezlerden yola çıkarak kök, sınır ve üyeleriyle tasarlar; komutları, yayınlanan olayları, kimliği, aggregate'ler arası referansları ve nihai tutarlılık kurallarını tanımlar, boyut ve çekişmeyi kontrol eder. Bir alan modeli tutarlılık sınırlarına dönüştürülecekse, aggregate'ler çok büyükse veya kilit çekişmesine yol açıyorsa ya da neyin anında, neyin nihai olarak tutarlı olacağına karar verilecekse kullanılır.
- Örnek istek: _"Sipariş bağlamımız için aggregate'leri tasarla; kurallar müşteri başına kredi limiti, sipariş başına en fazla 50 satır ve sevkiyattan sonra değişiklik yapılamaması."_
- İlgili: `event-storming`, `bounded-context-map`, `event-driven-design`, `database-schema-design`, `business-rules-catalog`
- Dosya: [skills/04-architecture/software-architect/domain/aggregate-design/SKILL.tr.md](skills/04-architecture/software-architect/domain/aggregate-design/SKILL.tr.md)

**Olay güdümlü akış tasarımı** · `event-driven-design`

- Ne zaman: Olay güdümlü bir akışı uçtan uca tasarlar; olay türleri ve adlandırma, şemalar ve sürümleme, topic'ler ve bölümleme anahtarları, sıralama, teslim semantiği, idempotent tüketiciler, outbox ile yayınlama, yeniden deneme ve dead-letter kuyruklarıyla hata yönetimi ile telafili saga orkestrasyonu veya koreografisini kapsar. Servisler olaylar üzerinden asenkron entegre olacaksa, bir iş süreci birden fazla servise yayılıyorsa ya da mevcut bir olay akışında mükerrer işleme, kayıp mesaj veya sıralama hataları varsa kullanılır.
- Örnek istek: _"Sipariş, ödeme, stok ve sevkiyat servisleri arasında sipariş verme olay akışını, ödeme başarısız olduğunda telafiyle birlikte tasarla."_
- İlgili: `event-storming`, `aggregate-design`, `integration-pattern-selection`, `data-contract`, `schema-evolution-plan`
- Dosya: [skills/04-architecture/software-architect/domain/event-driven-design/SKILL.tr.md](skills/04-architecture/software-architect/domain/event-driven-design/SKILL.tr.md)

**Servislere ayrıştırma** · `service-decomposition`

- Ne zaman: İş yetkinliklerini, sınırlı bağlamları, veri sahipliğini, değişim ve ölçekleme etkenlerini ve ekip yapısını birleştirerek bir sistemi veya monoliti servis ya da modül sınırlarına ayrıştırır; her adayı bağımlılık, geveze iletişim (chattiness) ve dağıtık işlem riski açısından değerlendirir ve servisler gerekçelendirilemiyorsa modüler monolit dahil bir ayrıntı düzeyi önerir. Bir monolit bölünürken, yeni bir servis yapısı tasarlanırken veya mevcut servislerin çok ince ya da çok kaba olup olmadığı incelenirken kullanılır.
- Örnek istek: _"400 bin satırlık sigorta monolitimizi servislere bölmek istiyoruz; poliçe, hasar, faturalama ve müşteri için sınırları ve veri sahipliğini bulmamıza yardım et."_
- İlgili: `bounded-context-map`, `event-storming`, `migration-strategy`, `team-topology`, `database-schema-design`
- Dosya: [skills/04-architecture/software-architect/domain/service-decomposition/SKILL.tr.md](skills/04-architecture/software-architect/domain/service-decomposition/SKILL.tr.md)

#### Mimari Evrim

**Teknik borç değerlendirmesi** · `tech-debt-assessment`

- Ne zaman: Kod, mimari, testler, altyapı, bağımlılıklar ve dokümantasyondaki borç öğelerinin envanterini çıkararak, bunları sınıflandırarak (bilinçli/farkında olmadan, tedbirli/pervasız), anaparayı (düzeltme maliyeti) ve faizi (süregelen maliyet ve risk) tahmin ederek ve iş etkisine bağlı bir geri ödeme planında önceliklendirerek bir teknik borç kaydı oluşturur. Ekip kod tabanı yüzünden yavaşladığını hissettiğinde, yönetim ne kadar borç olduğunu ve önce neyin düzeltileceğini sorduğunda ya da borcun planlamada gerekçelendirilmesi gerektiğinde kullanılır.
- Örnek istek: _"Faturalama platformumuzdaki teknik borcu değerlendir; sürümler iki hafta sürüyor, test kapsamı %30 ve hâlâ desteği bitmiş bir framework sürümü kullanıyoruz."_
- İlgili: `code-quality-report`, `refactoring`, `modernization-assessment`, `dependency-upgrade`, `technical-risk-review`
- Dosya: [skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.tr.md](skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.tr.md)

**Göç stratejisi planlama** · `migration-strategy`

- Ne zaman: Mevcut bir sistemden veya platformdan hedefe geçişi; strangler fig, paralel çalıştırma, aşamalı ve tek seferde geçiş yaklaşımlarını karşılaştırarak, dilimleri ve sıralarını, veri taşıma ve senkronizasyonu, birlikte çalışma ve yönlendirmeyi, her adım için doğrulama ve geri dönüşü ve geçiş (cutover) kriterlerini tanımlayarak planlar. Bir sistem değiştirilirken veya platform değiştirirken, monolitten servis ayrılırken, yeni bir veritabanına ya da buluta geçilirken veya bir göç planının risk incelemesi gerektiğinde kullanılır.
- Örnek istek: _"Şirket içindeki sipariş yönetimi monolitimizin yeni bulut tabanlı sipariş servislerine, satış sezonunda kesinti olmadan göçünü planla."_
- İlgili: `target-state-architecture`, `service-decomposition`, `modernization-assessment`, `rollback-plan`, `schema-migration-plan`
- Dosya: [skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.tr.md](skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.tr.md)

**Eski sistem modernizasyon değerlendirmesi** · `modernization-assessment`

- Ne zaman: Eski (legacy) bir sistemi iş uyumu, teknik sağlık, operasyonel risk ve değişim etkenleri açısından değerlendirir; ardından 7R seçeneklerini (emekliye ayır, olduğu gibi tut, yeniden barındır, yer değiştir, platform değiştir, hazır ürün al, yeniden yapılandır/yeniden mimarile) göreli efor, değer ve riskle karşılaştırır, karar kriterleri ve ilk adımlarla bir yol önerir. Eski bir uygulama baskı altındayken (destek sonu, maliyet, yetkinlik, ölçeklenebilirlik, uyum), yönetim \"X sistemiyle ne yapmalıyız?\" diye sorduğunda veya bir taşıma ya da yeniden yazıma bütçe ayırmadan önce kullanılır.
- Örnek istek: _"Şirket içinde çalışan 15 yıllık .NET Framework sipariş yönetimi monolitimizi değerlendir. İşletim sisteminin desteği seneye bitiyor ve sistemi yalnızca iki kişi biliyor. Seçeneklerimiz neler?"_
- İlgili: `legacy-code-comprehension`, `tech-debt-assessment`, `migration-strategy`, `build-vs-buy`, `application-portfolio-assessment`
- Dosya: [skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.tr.md](skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.tr.md)

**API kullanımdan kaldırma planı** · `api-deprecation-plan`

- Ne zaman: Bir API'nin, sürümün, endpoint'in, alanın veya olayın kullanımdan kaldırılmasını; tüketici envanteri, sürümleme stratejisi, makinece okunabilir Deprecation/Sunset sinyalleri, geçiş rehberi, brownout'lar ve ölçülebilir kaldırma kapılarıyla planlar. Kırıcı bir değişiklik, yeni bir API sürümü veya kaldırılan bir endpoint, iç ekiplere, iş ortaklarına ya da herkese açık tüketicilere sürpriz kesinti yaşatmadan ulaştırılacağı zaman kullanılır.
- Örnek istek: _"/v1/orders yerine /v2/orders geliyor (yeni sayfalama ve para formatı). İş ortaklarımız ve iç uygulamalarımız için v1'in kullanımdan kaldırma planını hazırla."_
- İlgili: `api-design-review`, `api-contract`, `migration-strategy`, `api-reference-docs`, `product-sunset-plan`
- Dosya: [skills/04-architecture/software-architect/evolution/api-deprecation-plan/SKILL.tr.md](skills/04-architecture/software-architect/evolution/api-deprecation-plan/SKILL.tr.md)

**API tasarımı inceleme** · `api-design-review`

- Ne zaman: Bir API tasarımını (OpenAPI/AsyncAPI spesifikasyonu, gRPC/protobuf tanımı, GraphQL şeması veya yazılı öneri) kaynak modellemesi, isimlendirme tutarlılığı, sürümleme ve uyumluluk, hata modeli, sayfalama ve filtreleme, idempotency ve eşzamanlılık, güvenlik ve işletilebilirlik açısından inceler; derecelendirilmiş bulguları somut düzeltmelerle verir. Bir API uygulanmadan veya yayımlanmadan önce önerildiğinde ya da değiştiğinde, genel veya iş ortağı API'si yayına çıkmak üzereyken veya mevcut bir API'nin tutarlılık denetimi gerektiğinde kullanılır.
- Örnek istek: _"Yeni sipariş API'mizin OpenAPI spesifikasyonunu iş ortaklarına yayımlamadan önce incele. Sürümleme, hatalar ve sayfalamaya odaklan."_
- İlgili: `api-contract`, `api-deprecation-plan`, `api-test-design`, `threat-model`, `api-reference-docs`
- Dosya: [skills/04-architecture/software-architect/evolution/api-design-review/SKILL.tr.md](skills/04-architecture/software-architect/evolution/api-design-review/SKILL.tr.md)

## Yazılım Geliştirme

### Geliştirici (Backend/Frontend/Mobil)

#### Teknik Tasarım

**Teknik tasarım dokümanı (RFC)** · `technical-design-doc`

- Ne zaman: Değişikliğin büyüklüğüne uygun olarak problem, hedefler ve hedef dışı konular, önerilen tasarım, alternatifler, yayına alma, riskler ve açık soruları kapsayan bir teknik tasarım dokümanı (RFC) yazar. Bir özellik veya değişiklik kodlamadan önce incelenmesi gerekecek kadar büyük, riskli ya da ekipler arası olduğunda veya RFC, tasarım dokümanı ya da teknik öneri istendiğinde kullanılır.
- Örnek istek: _"Sipariş onay e-postalarını checkout isteği içinde senkron göndermek yerine outbox ve arka plan worker'ı ile göndermek için bir tasarım dokümanı yaz."_
- İlgili: `adr`, `solution-architecture-document`, `task-breakdown`, `api-contract`, `trade-off-analysis`
- Dosya: [skills/05-engineering/developer/design/technical-design-doc/SKILL.tr.md](skills/05-engineering/developer/design/technical-design-doc/SKILL.tr.md)

**Hikayeyi görevlere bölme** · `task-breakdown`

- Ne zaman: Bir kullanıcı hikayesini veya iş kalemini bağımlılıkları, göreli tahminleri ve her biri için tamamlanma tanımı olan, sıralı ve bağımsız doğrulanabilir teknik görevlere böler. Bir geliştirici veya ekip bir hikayeyi ele aldığında ve uygulama planına ihtiyaç duyduğunda, işi paralelleştirmek istediğinde veya hikayenin görevlere nasıl bölüneceği sorulduğunda kullanılır.
- Örnek istek: _"Bu hikayeyi teknik görevlere böl: Müşteri olarak sipariş geçmişi sayfasından faturalarımı PDF olarak indirmek istiyorum."_
- İlgili: `user-story`, `story-splitting`, `technical-estimation`, `implement-from-story`, `technical-design-doc`
- Dosya: [skills/05-engineering/developer/design/task-breakdown/SKILL.tr.md](skills/05-engineering/developer/design/task-breakdown/SKILL.tr.md)

**API sözleşmesi yazma** · `api-contract`

- Ne zaman: Gereksinimlerden kaynaklar, operasyonlar, şemalar, hata modeli, güvenlik, sürümleme ve örnekler içeren OpenAPI (HTTP) veya AsyncAPI (olay/mesaj) şartnamesi biçiminde bir API sözleşmesi yazar. Yeni bir uç nokta, servis veya olayın uygulamadan önce üretici ve tüketiciler arasında mutabık kalınması gerektiğinde ya da OpenAPI/Swagger veya AsyncAPI şartnamesi istendiğinde kullanılır.
- Örnek istek: _"İş ortaklarının gönderi oluşturmasını, gönderi durumunu sorgulamasını ve teslim alınmadan önce gönderiyi iptal etmesini sağlayan bir servis için OpenAPI sözleşmesi yaz."_
- İlgili: `api-design-review`, `api-reference-docs`, `integration-requirements`, `technical-design-doc`, `api-test-design`
- Dosya: [skills/05-engineering/developer/design/api-contract/SKILL.tr.md](skills/05-engineering/developer/design/api-contract/SKILL.tr.md)

**Veritabanı şeması tasarlama** · `database-schema-design`

- Ne zaman: Bir alan tanımından ilişkisel veritabanı şeması tasarlar: tablolar, kolonlar ve tipler, birincil ve yabancı anahtarlar, kısıtlar, erişim desenlerine dayalı indeksler ve migration betiği taslağı. Yeni bir özellik kalıcı depolamaya ihtiyaç duyduğunda, mevcut şema genişletilecekse ya da bir alan için tablolar, ER modeli, DDL veya indeks istendiğinde kullanılır.
- Örnek istek: _"Toplantı odası rezervasyon özelliği için veritabanı şemasını tasarla: odalar, başlangıç/bitiş saatli rezervasyonlar, katılımcılar ve aynı odada çakışan rezervasyon olmaması."_
- İlgili: `logical-data-model`, `data-requirements`, `schema-migration-plan`, `index-recommendation`, `aggregate-design`
- Dosya: [skills/05-engineering/developer/design/database-schema-design/SKILL.tr.md](skills/05-engineering/developer/design/database-schema-design/SKILL.tr.md)

**Spike raporu yazma** · `spike-report`

- Ne zaman: Süre sınırlı bir araştırmanın yanıtlaması gereken soruyu, denenenleri, bulunan kanıtları, artı ve eksileriyle seçenekleri ve takip işleriyle birlikte net bir öneriyi kaydeden bir spike raporu yazar. Bir spike, proof of concept veya teknik araştırma bittiğinde (ya da planlanırken) ve ekibin karar verip tahmin yapabilmesi için sonucun paylaşılması gerektiğinde kullanılır.
- Örnek istek: _"Bir spike raporu yaz: mevcut aramamızın yazım hatasına toleranslı ürün aramasını kaldırıp kaldıramayacağını ya da ayrı bir arama motoruna ihtiyacımız olup olmadığını iki gün inceledik."_
- İlgili: `technical-design-doc`, `adr`, `technology-selection`, `trade-off-analysis`, `task-breakdown`
- Dosya: [skills/05-engineering/developer/design/spike-report/SKILL.tr.md](skills/05-engineering/developer/design/spike-report/SKILL.tr.md)

#### Kodlama

**Hikayeden özellik geliştirme** · `implement-from-story`

- Ne zaman: Kabul kriterlerini davranışlara eşleyerek, mevcut kod kurallarını okuyarak, kodu ve testleri küçük doğrulanabilir adımlarla yazarak ve neyin geliştirildiğini, nasıl doğrulandığını ve neyin açık kaldığını raporlayarak bir kullanıcı hikayesinden özellik planlar ve geliştirir. Bir geliştirici verilen kabul kriterlerine göre bir hikaye, kayıt veya özelliğin geliştirilmesini istediğinde kullanılır.
- Örnek istek: _"Bu hikayeyi servisimizde geliştir: müşteri varsayılan teslimat adresi belirleyebilir; yalnızca bir adres varsayılan olabilir; varsayılan adres checkout'ta önceden seçili gelir."_
- İlgili: `task-breakdown`, `acceptance-criteria`, `tdd-cycle`, `unit-test-writing`, `pull-request-description`
- Dosya: [skills/05-engineering/developer/coding/implement-from-story/SKILL.tr.md](skills/05-engineering/developer/coding/implement-from-story/SKILL.tr.md)

**Kodu yeniden düzenleme** · `refactoring`

- Ne zaman: Bir sonraki değişiklik için önemli olan kod kokularını belirleyerek, davranışı karakterizasyon testleriyle güvenceye alarak ve adlandırılmış refactoring'leri (Extract Function, Replace Conditional with Polymorphism, Introduce Parameter Object vb.) davranışı koruyan küçük adımlarla uygulayarak kodu güvenli biçimde yeniden düzenler. Kod değiştirilmesi zor olduğunda, dağınık koda özellik eklemeden önce ya da davranışı değiştirmeden kodun temizlenmesi, yeniden yapılandırılması istendiğinde kullanılır.
- Örnek istek: _"Bu 200 satırlık calculatePrice metodunu refactor et; gelecek sprint yeni bir indirim türü eklemem gerekiyor ve burada her değişiklik bir şeyi bozuyor."_
- İlgili: `clean-code-review`, `legacy-code-comprehension`, `unit-test-writing`, `tech-debt-assessment`, `code-review`
- Dosya: [skills/05-engineering/developer/coding/refactoring/SKILL.tr.md](skills/05-engineering/developer/coding/refactoring/SKILL.tr.md)

**Clean Code incelemesi** · `clean-code-review`

- Ne zaman: Kodu sürdürülebilirlik açısından inceler: isimlendirme, fonksiyon büyüklüğü ve sorumluluğu, SOLID ve bağımlılık, tekrar, yorumlar ve tanınabilir kod kokuları; konum, etki ve somut düzeltme içeren önceliklendirilmiş bulgular üretir. Kodun temiz, okunabilir veya iyi tasarlanmış olup olmadığı sorulduğunda, bir dosya, sınıf veya modül için sürdürülebilirlik incelemesi istendiğinde ya da kod devre hazırlanırken kullanılır.
- Örnek istek: _"Bu OrderService sınıfına Clean Code incelemesi yap; iki yılda büyüdü ve yeni gelenler değiştirmekte zorlanıyor."_
- İlgili: `refactoring`, `code-review`, `coding-standards`, `review-comment-writing`, `code-quality-report`
- Dosya: [skills/05-engineering/developer/coding/clean-code-review/SKILL.tr.md](skills/05-engineering/developer/coding/clean-code-review/SKILL.tr.md)

**Hata yönetimi incelemesi** · `error-handling-review`

- Ne zaman: Kodun hataları nasıl tespit ettiğini, ilettiğini, yeniden denediğini, yedek davranışa geçtiğini ve raporladığını inceler: istisna tasarımı, yutulan veya fazla geniş catch'ler, yeniden deneme ve zaman aşımı politikası, idempotency, kaynak temizliği, transaction tutarlılığı ve kullanıcıya gösterilen hata mesajları. Hatalar sessiz veya kafa karıştırıcı olduğunda, bir servis veya entegrasyon sağlamlaştırılmadan önce ya da kodun hata yönetimi, istisnaları veya dayanıklılığı incelenmek istendiğinde kullanılır.
- Örnek istek: _"Bu ödeme istemcisindeki hata yönetimini incele: sağlayıcıyı HTTP ile çağırıyor, hata olursa yeniden deniyor ve sipariş durumunu güncelliyor."_
- İlgili: `resilience-review`, `logging-instrumentation`, `error-message-writing`, `code-review`, `error-scenario-catalog`
- Dosya: [skills/05-engineering/developer/coding/error-handling-review/SKILL.tr.md](skills/05-engineering/developer/coding/error-handling-review/SKILL.tr.md)

**Loglama ve ölçümleme ekleme** · `logging-instrumentation`

- Ne zaman: Koda, gerçek operasyonel soruları yanıtlayan noktalarda yapılandırılmış log, metrik ve dağıtık iz (trace) ekler; tutarlı alan adları, doğru seviyeler, düşük kardinaliteli metrik etiketleri, trace bağlamı aktarımı sağlar ve sır ya da kişisel veri yazmaz. Bir özellik canlıya çıkacağında, bir olay görünürlük eksikliğini ortaya koyduğunda veya koda loglama, metrik, tracing ya da telemetri (ör. OpenTelemetry) eklenmesi istendiğinde kullanılır.
- Örnek istek: _"Dosya okuyan, satırları doğrulayan ve stok API'sini çağıran bu sipariş içe aktarma işine loglama, metrik ve tracing ekle."_
- İlgili: `observability-plan`, `alert-design`, `slo-definition`, `error-handling-review`, `log-analysis`
- Dosya: [skills/05-engineering/developer/coding/logging-instrumentation/SKILL.tr.md](skills/05-engineering/developer/coding/logging-instrumentation/SKILL.tr.md)

**Performans iyileştirme** · `performance-optimization`

- Ne zaman: Koddaki performans darboğazlarını tahminle değil ölçümle bulur ve giderir: hedef metriği tanımlar, profil, trace veya sorgu planlarını okur, darboğazları maliyet payına göre sıralar, beklenen kazanç ve ödünleşimlerle çözüm önerir ve iyileşmenin nasıl doğrulanacağını belirtir. Kod, bir uç nokta veya bir iş çok yavaş ya da çok kaynak tüketiyorsa veya optimize etme, hızlandırma ya da CPU, bellek veya gecikmeyi azaltma istendiğinde kullanılır.
- Örnek istek: _"Sipariş arama uç noktamızın normal yükte p95 değeri 2,4 sn. Handler kodu ve CPU profili burada, hızlandırmama yardım et."_
- İlgili: `sql-query-writing`, `query-optimization`, `load-test-analysis`, `web-performance-audit`, `logging-instrumentation`
- Dosya: [skills/05-engineering/developer/coding/performance-optimization/SKILL.tr.md](skills/05-engineering/developer/coding/performance-optimization/SKILL.tr.md)

**Eşzamanlılık incelemesi** · `concurrency-review`

- Ne zaman: Kodu eşzamanlılık hatalarına karşı inceler: veri yarışları, kontrol-et-sonra-yap ve kayıp güncellemeler, kilitlenmeler ve kilit sırası, güvensiz yayımlama, async/await yanlış kullanımı, thread pool açlığı ve dağıtık tüketicilerde mükerrer ya da sırasız işleme; her bulgu için somut bir iç içe geçme senaryosu ve çözüm verir. Kod thread, async, kilit, paylaşılan durum, arka plan işçisi, mesaj tüketicisi veya eşzamanlı veritabanı güncellemesi kullanıyorsa ya da zamanlamaya bağlı görünen aralıklı hatalar bildirildiğinde kullanılır.
- Örnek istek: _"Bu cüzdan bakiye yükleme servisini eşzamanlılık sorunlarına karşı incele; bakiyeyi okuyor, tutarı ekliyor ve kaydediyor, hem API'den hem de bir mesaj tüketicisinden çağrılıyor."_
- İlgili: `code-review`, `error-handling-review`, `debugging-hypotheses`, `resilience-review`, `integration-test-writing`
- Dosya: [skills/05-engineering/developer/coding/concurrency-review/SKILL.tr.md](skills/05-engineering/developer/coding/concurrency-review/SKILL.tr.md)

**Bağımlılık güncelleme** · `dependency-upgrade`

- Ne zaman: Bir kütüphane, framework veya çalışma ortamı güncellemesini planlar ve uygular: mevcut ve hedef sürüm arasındaki sürüm notlarını ve geçiş kılavuzlarını okur, kod tabanını gerçekten etkileyen kırıcı değişiklikleri listeler, geçiş adımlarını sıralar, geçişli bağımlılık çakışmalarını ele alır, doğrulama ve geri dönüşü tanımlar. Güvenlik, destek sonu veya ihtiyaç duyulan bir özellik nedeniyle bağımlılık güncellenmesi gerektiğinde, otomatik güncelleme pull request'i başarısız olduğunda veya X sürümünden Y'ye nasıl geçileceği sorulduğunda kullanılır.
- Örnek istek: _"Web framework'ümüzü 6. ana sürümden 8'e yükseltmeyi planla; bağımlılık manifesti ve kullandığımız özelliklerin listesi burada."_
- İlgili: `dependency-vulnerability-review`, `semantic-versioning`, `refactoring`, `changelog-entry`, `pull-request-description`
- Dosya: [skills/05-engineering/developer/coding/dependency-upgrade/SKILL.tr.md](skills/05-engineering/developer/coding/dependency-upgrade/SKILL.tr.md)

**Kodu açıklama** · `code-explanation`

- Ne zaman: Bir kod parçasının ne yaptığını, muhtemelen neden böyle yazıldığını ve hangi riskleri taşıdığını okuyucunun ihtiyaç duyduğu derinlikte açıklar: tek paragraflık özet, kontrol ve veri akışının adım adım anlatımı, yan etkiler, varsayımlar, uç durumlar ve şüpheli noktalar. Biri kod yapıştırıp ne yaptığını, nasıl çalıştığını, neden belli bir şekilde davrandığını sorduğunda ya da kodu değiştirmeden veya incelemeden önce anlaması gerektiğinde kullanılır.
- Örnek istek: _"Bu fonksiyonun ne yaptığını açıkla ve içinde riskli görünen bir şey var mı söyle."_
- İlgili: `legacy-code-comprehension`, `code-documentation`, `clean-code-review`, `regex-builder`, `technical-onboarding`
- Dosya: [skills/05-engineering/developer/coding/code-explanation/SKILL.tr.md](skills/05-engineering/developer/coding/code-explanation/SKILL.tr.md)

**Eski kodu anlama** · `legacy-code-comprehension`

- Ne zaman: Yabancı veya eski (legacy) bir kodun çalışılabilir haritasını çıkarır: giriş noktaları, modüller ve sorumlulukları, ana çalışma akışları, veri depoları, dış entegrasyonlar, gizli iş kuralları, ölü veya riskli alanlar ve güvenle değiştirilebilecek yerler; her sonucu koddaki bir kanıta bağlar. Bir geliştirici bir sistemi devraldığında, kimsenin tam anlamadığı kodu değiştirmesi gerektiğinde, bir modernizasyon planlandığında veya eski bir kod tabanının nasıl çalıştığı sorulduğunda kullanılır.
- Örnek istek: _"Dokümantasyonu olmayan bu faturalama modülünü devraldım. Klasör yapısı ve ana sınıflar burada; bir faturanın nasıl oluşturulduğunu anlamama yardım et."_
- İlgili: `code-explanation`, `refactoring`, `tech-debt-assessment`, `modernization-assessment`, `business-rules-catalog`
- Dosya: [skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.tr.md](skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.tr.md)

**Regex oluşturma ve açıklama** · `regex-builder`

- Ne zaman: Belirtilen eşleşme ihtiyacı için hedef motorun lehçesinde bir düzenli ifade (regex) yazar; sade dille parça parça açıklama, eşleşmesi ve eşleşmemesi gereken test durumları tablosu, çapa ve kaçış kararları ve felaket düzeyinde geri izleme (catastrophic backtracking) kontrolü sunar. Mevcut bir regex'i açıklar veya düzeltir. Metni doğrulamak, çıkarmak, aramak veya değiştirmek için desen gerektiğinde, biri regex yapıştırıp ne yaptığını sorduğunda ya da fazla, eksik eşleşen veya yavaş çalışan bir regex bildirdiğinde kullanılır.
- Örnek istek: _"E-posta konularından INV-2024-000123 gibi fatura numaralarını çıkaran bir regex yaz; JavaScript'te kullanıyoruz."_
- İlgili: `code-explanation`, `unit-test-writing`, `data-quality-rules`, `secure-code-review`, `business-rules-catalog`
- Dosya: [skills/05-engineering/developer/coding/regex-builder/SKILL.tr.md](skills/05-engineering/developer/coding/regex-builder/SKILL.tr.md)

**SQL sorgusu yazma** · `sql-query-writing`

- Ne zaman: Belirtilen bir soru için hedef veritabanı lehçesinde doğru, okunabilir ve indeks dostu bir SQL sorgusu yazar: sonuç taneciğini (grain) ve join kardinalitesini netleştirir, NULL'ları, mükerrer kayıtları ve saat dilimlerini ele alır, sargable koşullar ve parametreler kullanır, dayandığı indeksleri ve sonuçların nasıl doğrulanacağını belirtir. Bir rapor, özellik, veri düzeltme veya inceleme için sorgu gerektiğinde, bir sorunun SQL'e çevrilmesi istendiğinde ya da mevcut bir sorgunun doğruluk veya okunabilirlik için yeniden yazılması istendiğinde kullanılır.
- Örnek istek: _"Siparişi olmayanlar dahil her müşteri için son 90 gündeki sipariş sayısını ve toplam cirosunu döndüren bir PostgreSQL sorgusu yaz."_
- İlgili: `query-optimization`, `index-recommendation`, `database-schema-design`, `metric-definition`, `performance-optimization`
- Dosya: [skills/05-engineering/developer/coding/sql-query-writing/SKILL.tr.md](skills/05-engineering/developer/coding/sql-query-writing/SKILL.tr.md)

#### Geliştirici Testleri

**Birim testi yazma** · `unit-test-writing`

- Ne zaman: Bir fonksiyonun, sınıfın veya modülün gözlemlenebilir davranışını Arrange-Act-Assert yapısında sabitleyen birim testleri yazar; mutlu yolu, denklik sınıflarını, sınır değerleri, hata yollarını ve durum geçişlerini kapsar, test dublörlerini yalnızca gerçek sınırlarda kullanır ve test adlarını birer şartname gibi yazar. Birim testi yazma, ekleme veya iyileştirme, belirli bir kodun kapsamını artırma ya da değişiklikten önce kodu güvence altına alma istendiğinde kullanılır.
- Örnek istek: _"Bu ShippingCostCalculator sınıfı için birim testleri yaz; ağırlık kademeleri, belli tutarın üzerinde ücretsiz kargo ve ekspres ek ücreti kuralları var."_
- İlgili: `tdd-cycle`, `test-gap-finder`, `integration-test-writing`, `equivalence-boundary-analysis`, `refactoring`
- Dosya: [skills/05-engineering/developer/testing/unit-test-writing/SKILL.tr.md](skills/05-engineering/developer/testing/unit-test-writing/SKILL.tr.md)

**Entegrasyon testi yazma** · `integration-test-writing`

- Ne zaman: Kodu gerçek sınırlar (veritabanı, mesaj kuyruğu, HTTP API'leri, dosya deposu, önbellek) üzerinden çalıştıran entegrasyon testleri yazar; mümkün olduğunda geçici gerçek bağımlılıklar, yalnızca ekibin sahibi olmadığı sistemler için test dublörleri kullanır; eşleme, transaction, serileştirme, hata ve zaman aşımı davranışını izole veri ve deterministik hazırlıkla kapsar. Entegrasyon testi istendiğinde, bir repository, API uç noktası, tüketici veya dış istemcinin gerçek altyapıya karşı doğrulanması gerektiğinde ya da mock'lu birim testleri davranışı kanıtlayamadığında kullanılır.
- Örnek istek: _"OrderRepository ve OrderPlaced tüketicisi için entegrasyon testleri yaz; ilişkisel veritabanı ve mesaj kuyruğu kullanıyoruz."_
- İlgili: `unit-test-writing`, `api-test-design`, `test-data-design`, `flaky-test-analysis`, `test-gap-finder`
- Dosya: [skills/05-engineering/developer/testing/integration-test-writing/SKILL.tr.md](skills/05-engineering/developer/testing/integration-test-writing/SKILL.tr.md)

**TDD ile geliştirme** · `tdd-cycle`

- Ne zaman: Bir davranışı kodlamayı katı kırmızı-yeşil-refactor döngüleriyle yönetir: en basitten en zora sıralı bir test listesi, her seferinde doğru nedenle kırıldığı görülen tek bir başarısız test, geçmek için gereken en az kod ve yalnızca yeşildeyken refactoring; başarısız bir test olmadan üretim kodu yazılmaz. Bir özellik, fonksiyon veya hata düzeltmesi test önce yaklaşımıyla geliştirilmek istendiğinde, TDD adımları sorulduğunda ya da somut bir davranış üzerinde TDD pratiği veya gösterimi yapılmak istendiğinde kullanılır.
- Örnek istek: _"TDD ile bir parola gücü doğrulayıcısı geliştirelim: en az 12 karakter, en az bir rakam ve bir sembol, kullanıcının e-postasını içermemeli."_
- İlgili: `unit-test-writing`, `implement-from-story`, `refactoring`, `acceptance-criteria`, `test-gap-finder`
- Dosya: [skills/05-engineering/developer/testing/tdd-cycle/SKILL.tr.md](skills/05-engineering/developer/testing/tdd-cycle/SKILL.tr.md)

**Test edilmemiş yolları bulma** · `test-gap-finder`

- Ne zaman: Kodu mevcut testleriyle karşılaştırarak test edilmemiş yolları bulur: dalları, sınırları, hata işleyicilerini, durum geçişlerini ve gereksinim kurallarını sıralar, her birini kapsayan testlerle eşler, boşlukları ve zayıf testleri (assertion'sız, aşırı mock'lu, yalnızca mutlu yol) işaretler ve eklenecek somut testle birlikte riske göre sıralar. Testlerde neyin eksik olduğu sorulduğunda, kapsam anlamlı biçimde artırılmak istendiğinde, bir pull request'in testleri incelendiğinde ya da elde bir kapsam raporu olup hangi boşlukların önemli olduğu bilinmek istendiğinde kullanılır.
- Örnek istek: _"InvoiceService ve test sınıfı burada. Hangi yollar test edilmemiş ve hangi boşluklar en önemli?"_
- İlgili: `unit-test-writing`, `integration-test-writing`, `code-review`, `regression-selection`, `risk-based-testing`
- Dosya: [skills/05-engineering/developer/testing/test-gap-finder/SKILL.tr.md](skills/05-engineering/developer/testing/test-gap-finder/SKILL.tr.md)

#### Kod İşbirliği

**Commit mesajı yazma** · `commit-message`

- Ne zaman: Conventional Commits formatında; net bir başlık, değişikliğin nedenini açıklayan bir gövde ve kırıcı değişiklik ile iş kaydı referansları için alt bilgiler içeren commit mesajı yazar. Geliştiricinin elinde bir diff, değişiklik listesi veya kısa bir açıklama olduğunda ve commit mesajına ihtiyaç duyduğunda ya da karışık bir değişikliği iyi kapsamlanmış commit'lere bölmek istediğinde kullanılır.
- Örnek istek: _"Bu diff için commit mesajı yaz. Ödeme istemcisine backoff ile yeniden deneme ekliyor ve timeout yapılandırma anahtarının adını düzeltiyor."_
- İlgili: `pull-request-description`, `changelog-entry`, `semantic-versioning`, `branching-strategy`
- Dosya: [skills/05-engineering/developer/collaboration/commit-message/SKILL.tr.md](skills/05-engineering/developer/collaboration/commit-message/SKILL.tr.md)

**Pull request açıklaması** · `pull-request-description`

- Ne zaman: Neyin değiştiğini, nedenini, nasıl test edildiğini, riskleri ve yayına alma notlarını ve inceleyenlerin nereye odaklanması gerektiğini anlatan bir pull request açıklaması yazar. Geliştirici bir pull/merge request açtığında veya güncellediğinde ve elindeki diff, commit listesi, iş kaydı veya kaba notları inceleyenler için özetlemesi gerektiğinde kullanılır.
- Örnek istek: _"Bu commit'ler için PR açıklaması yaz. Değişiklik fatura PDF üretimini arka plan işine taşıyor."_
- İlgili: `commit-message`, `code-review`, `implement-from-story`, `release-notes`, `rollback-plan`
- Dosya: [skills/05-engineering/developer/collaboration/pull-request-description/SKILL.tr.md](skills/05-engineering/developer/collaboration/pull-request-description/SKILL.tr.md)

**Pull request inceleme** · `code-review`

- Ne zaman: Bir pull request'i veya diff'i doğruluk, tasarım, testler, güvenlik, performans ve okunabilirlik açısından inceler; önceliklendirilmiş, uygulanabilir bulgular ve net bir karar sunar. Birisi merge öncesinde bir PR'ın, diff'in, yamanın veya kod parçasının incelenmesini istediğinde ya da bir değişiklik için ikinci görüş aradığında kullanılır.
- Örnek istek: _"Bu pull request diff'ini incele. Sipariş servisine indirim hesaplama endpoint'i ekliyor."_
- İlgili: `review-comment-writing`, `clean-code-review`, `secure-code-review`, `error-handling-review`, `pull-request-description`
- Dosya: [skills/05-engineering/developer/collaboration/code-review/SKILL.tr.md](skills/05-engineering/developer/collaboration/code-review/SKILL.tr.md)

**İnceleme yorumu yazma** · `review-comment-writing`

- Ne zaman: Kod inceleme yorumlarını somut, nazik ve uygulanabilir olacak şekilde yazar veya yeniden yazar; her yorumu önem ve niyetine göre etiketler (Critical, Required, Nit, Optional, FYI; ayrıca soru ve takdir) ve gerekçe ile önerilen değişiklikle destekler. İnceleyenin bir pull request üzerinde ham gözlemleri veya sert taslak yorumları olduğunda ve bunları net ifade etmek istediğinde ya da inceleme yazışmaları gerginleştiğinde kullanılır.
- Örnek istek: _"İnceleme yorumlarımı sert olmadan ama net olacak şekilde yeniden yaz. İlki şu: 'bu yanlış, neden döngü içinde sorgu atıyorsun?'"_
- İlgili: `code-review`, `feedback-sbi`, `tone-rewrite`, `coding-standards`, `conflict-resolution`
- Dosya: [skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.tr.md](skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.tr.md)

**Branch stratejisi seçme** · `branching-strategy`

- Ne zaman: Sürüm sıklığı, paralel desteklenen sürüm sayısı, ekip büyüklüğü, CI olgunluğu ve uyum gereksinimlerine göre bir branch stratejisi (trunk-based development, GitHub Flow, GitFlow veya belgelenmiş bir varyant) önerir ve ortaya çıkan branch, merge ve sürüm kurallarını tanımlar. Ekip yeni bir repository kurduğunda, merge çakışmaları veya uzun ömürlü branch'lerle boğuştuğunda, sürüm modelini değiştirdiğinde ya da birden fazla canlı sürümü desteklemesi gerektiğinde kullanılır.
- Örnek istek: _"Tek serviste 12 geliştiriciyiz, haftalık yayına çıkıyoruz ama günlük istiyoruz; develop branch'i yüzünden hotfix'ler çok uzun sürüyor. Hangi branch stratejisini kullanalım?"_
- İlgili: `pipeline-design`, `release-plan`, `semantic-versioning`, `deployment-strategy`, `working-agreement`
- Dosya: [skills/05-engineering/developer/collaboration/branching-strategy/SKILL.tr.md](skills/05-engineering/developer/collaboration/branching-strategy/SKILL.tr.md)

#### Hata Ayıklama

**Hatayı yeniden üretme** · `bug-reproduction`

- Ne zaman: Belirsiz bir hata bildirimini; kesin adımlar, ortam, veri ön koşulları, beklenen ve gerçekleşen sonuç ile tekrar oranı içeren minimal ve deterministik bir yeniden üretime dönüştürür, mümkünse başarısız olan otomatik bir testle bitirir. Bir hata zor üretilebilir, aralıklı, ortama özgü olduğunda veya yalnızca kullanıcı diliyle anlatıldığında ve düzeltmeye başlamadan önce kullanılır.
- Örnek istek: _"Kullanıcılar dışa aktarımın bazen boş dosya ürettiğini söylüyor. Güvenilir bir yeniden üretim kurmama yardım et."_
- İlgili: `bug-report`, `debugging-hypotheses`, `log-analysis`, `unit-test-writing`, `flaky-test-analysis`
- Dosya: [skills/05-engineering/developer/debugging/bug-reproduction/SKILL.tr.md](skills/05-engineering/developer/debugging/bug-reproduction/SKILL.tr.md)

**Stack trace analizi** · `stack-trace-analysis`

- Ne zaman: Bir stack trace'i veya çökme raporunu analiz ederek hatalı çerçeveyi, istisna zincirini ve kök neden adaylarını belirler; çözümler ve sonraki teşhis adımını önerir. Geliştirici herhangi bir dil veya runtime'dan bir istisna, stack trace, çökme logu, panic veya yakalanmamış hata yapıştırıp neyin yanlış gittiğini ya da nereye bakacağını sorduğunda kullanılır.
- Örnek istek: _"Bu stack trace'e ne sebep oluyor? OrderController.getOrder'dan çağrılan OrderMapper.toDto içinde NullPointerException."_
- İlgili: `debugging-hypotheses`, `log-analysis`, `bug-reproduction`, `error-handling-review`, `code-explanation`
- Dosya: [skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.tr.md](skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.tr.md)

**Log analizi** · `log-analysis`

- Ne zaman: Uygulama, altyapı veya erişim loglarını analiz ederek zaman çizelgesi oluşturur, olayları request veya trace ID ile servisler arasında ilişkilendirir, anomalileri ve hata kümelerini bulur; kanıtın neyi desteklediğini ve neyi desteklemediğini belirtir. Geliştirici bir olay, hata, yavaşlama veya tuhaf davranış çevresindeki log parçalarını ya da dökümlerini paylaşıp ne olduğunu, ne zaman başladığını veya hangi bileşenin sorumlu olduğunu sorduğunda kullanılır.
- Örnek istek: _"14:00 ile 14:20 arasındaki API gateway ve sipariş servisi logları burada. Ödeme akışı hata vermeye başladığında ne oldu?"_
- İlgili: `stack-trace-analysis`, `debugging-hypotheses`, `incident-response`, `postmortem`, `logging-instrumentation`
- Dosya: [skills/05-engineering/developer/debugging/log-analysis/SKILL.tr.md](skills/05-engineering/developer/debugging/log-analysis/SKILL.tr.md)

**Hata ayıklama hipotezleri** · `debugging-hypotheses`

- Ne zaman: Belirti ve kanıtlardan sıralı bir hata ayıklama hipotezleri listesi üretir ve her birini en ucuz ayırt edici testle eşleştirir; böylece araştırma dağılmak yerine sonuca yaklaşır. Bir hatanın nedeni bilinmediğinde, birkaç açıklama makul göründüğünde, hata ayıklama oturumu kısır döngüye girdiğinde veya ekip araştırma işini bölüşmek istediğinde kullanılır.
- Örnek istek: _"Son dağıtımdan sonra API isteklerinin yaklaşık %2'si 5 saniyeyi aşıyor, yalnızca bazı pod'larda. Sıralı hipotezler ve her birinin nasıl test edileceğini ver."_
- İlgili: `bug-reproduction`, `stack-trace-analysis`, `log-analysis`, `five-whys`, `fishbone-analysis`
- Dosya: [skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.tr.md](skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.tr.md)

#### Geliştirici Dokümantasyonu

**README yazma** · `readme-writing`

- Ne zaman: Projenin ne olduğunu, kimin için olduğunu, nasıl çalıştırılacağını, nasıl kullanılıp yapılandırılacağını ve nasıl katkı verileceğini kopyalanıp doğrulanabilir komutlarla anlatan bir repository README'si yazar veya yeniden düzenler. Repository'de README yoksa, mevcut olan eskimiş veya dağınıksa, yeni katılanlar projeyi çalıştırmakta zorlanıyorsa ya da bir kütüphane veya servis diğer ekiplerle paylaşılmak üzereyse kullanılır.
- Örnek istek: _"Dahili invoice-service repository'miz için README yaz. PostgreSQL veritabanı ve bir arka plan worker'ı olan bir REST API; klasör yapısı ve Makefile ekte."_
- İlgili: `code-documentation`, `api-reference-docs`, `technical-onboarding`, `how-to-guide`, `changelog-entry`
- Dosya: [skills/05-engineering/developer/docs/readme-writing/SKILL.tr.md](skills/05-engineering/developer/docs/readme-writing/SKILL.tr.md)

**Kod dokümantasyonu** · `code-documentation`

- Ne zaman: Docstring'leri, API yorumlarını ve satır içi yorumları, kodun ne yaptığını tekrar etmek yerine sözleşmeyi, niyeti, kısıtları ve açık olmayan gerekçeleri (neden) anlatacak şekilde yazar veya iyileştirir; yanlış, eskimiş veya koda dönüşmesi gereken yorumları işaretler. Bir geliştirici bir fonksiyonun, sınıfın, modülün veya public API'nin belgelenmesini, mevcut yorumların gözden geçirilmesini ya da kodun devre hazırlanmasını istediğinde kullanılır.
- Örnek istek: _"Bu fiyatlandırma modülüne düzgün dokümantasyon ekle. İşe yarar olsun; kodu tekrar eden yorumlar istemiyorum."_
- İlgili: `readme-writing`, `api-reference-docs`, `clean-code-review`, `code-explanation`, `legacy-code-comprehension`
- Dosya: [skills/05-engineering/developer/docs/code-documentation/SKILL.tr.md](skills/05-engineering/developer/docs/code-documentation/SKILL.tr.md)

**API referans dokümanı** · `api-reference-docs`

- Ne zaman: HTTP, RPC veya mesaj tabanlı API'ler için kimlik doğrulamayı, her uç noktayı veya işlemi parametreleriyle, istek ve yanıt örneklerini, hata kodlarını, sayfalamayı, hız sınırlarını ve sürümlemeyi kapsayan API referans dokümantasyonunu bir sözleşmeden, koddan veya notlardan yazar. Bir API'nin tüketicilere yönelik referans dokümanına ihtiyacı olduğunda, mevcut doküman uygulamadan saptığında veya şartname olduğu hâlde açıklama ve örnek içermediğinde kullanılır.
- Örnek istek: _"Bu OpenAPI dosyasından sipariş API'miz için referans doküman yaz. Tüketiciler hata kodlarının ne anlama geldiğini ve sayfalamanın nasıl çalıştığını sürekli soruyor."_
- İlgili: `api-contract`, `api-design-review`, `readme-writing`, `error-message-writing`, `changelog-entry`
- Dosya: [skills/05-engineering/developer/docs/api-reference-docs/SKILL.tr.md](skills/05-engineering/developer/docs/api-reference-docs/SKILL.tr.md)

**Değişiklik günlüğü girdisi** · `changelog-entry`

- Ne zaman: Commit'lerden, merge edilmiş pull request'lerden veya bir değişiklik listesinden Keep a Changelog formatında (Added, Changed, Deprecated, Removed, Fixed, Security) değişiklik günlüğü girdileri yazar; yazılımı kullananlar için yazılır, kırıcı değişiklikleri ve geçiş adımlarını öne çıkarır. Bir sürüm bölümü hazırlanırken, bir merge sonrasında Unreleased bölümü güncellenirken veya gürültülü commit geçmişi okunabilir bir değişiklik geçmişine dönüştürülürken kullanılır.
- Örnek istek: _"Merge edilmiş bu PR başlıklarını istemci kütüphanemizin 2.4.0 sürümü için bir değişiklik günlüğü girdisine dönüştür."_
- İlgili: `commit-message`, `release-notes`, `semantic-versioning`, `pull-request-description`, `app-store-release-notes`
- Dosya: [skills/05-engineering/developer/docs/changelog-entry/SKILL.tr.md](skills/05-engineering/developer/docs/changelog-entry/SKILL.tr.md)

#### Frontend'e Özel

**UI bileşeni tasarlama** · `component-design`

- Ne zaman: Bir UI bileşeninin teknik API'sini geliştirme öncesinde framework'ten bağımsız biçimde tasarlar: sorumluluk, prop'lar veya girdiler, iç ve kontrollü durum, olaylar, slot'lar veya kompozisyon noktaları, varyantlar, görsel ve etkileşim durumları, erişilebilirlik semantiği ve klavye davranışı, test durumları. Bir geliştirici yeniden kullanılabilir bir bileşen yazmak veya yeniden düzenlemek üzereyken, bir tasarım teslimi bileşen sözleşmesine dönüştürülecekken ya da bir bileşenin prop sayısı kontrolden çıktığında kullanılır.
- Örnek istek: _"Yönetim ekranlarımızda tekrar kullanacağımız aranabilir bir seçim kutusu (combobox) için bileşen API'si tasarla. Asenkron seçenekler ve çoklu seçim gerekiyor."_
- İlgili: `design-system-component-spec`, `accessibility-audit`, `state-management-design`, `unit-test-writing`, `design-handoff`
- Dosya: [skills/05-engineering/developer/frontend/component-design/SKILL.tr.md](skills/05-engineering/developer/frontend/component-design/SKILL.tr.md)

**Erişilebilirlik denetimi (WCAG)** · `accessibility-audit`

- Ne zaman: Bir web veya mobil arayüzü (sayfa, akış, bileşen ya da işaretleme kodu) WCAG 2.2 A ve AA başarı kriterlerine göre denetler; her bulguyu kriter, etkilenen kullanıcılar, kanıt ve önem derecesiyle kaydeder, somut kod veya tasarım düzeltmeleri önerir. Bir ekran veya bileşenin yayın öncesi erişilebilirlik kontrolü gerektiğinde, bir şikâyet ya da yasal talep sonrasında veya \"bu erişilebilir mi?\", \"WCAG'ye göre kontrol et\" dendiğinde kullanılır.
- Örnek istek: _"Bu ödeme formu işaretlemesini WCAG 2.2 AA'ya göre denetle ve önce neyi düzeltmem gerektiğini söyle."_
- İlgili: `component-design`, `heuristic-evaluation`, `design-handoff`, `microcopy`, `test-case-writing`
- Dosya: [skills/05-engineering/developer/frontend/accessibility-audit/SKILL.tr.md](skills/05-engineering/developer/frontend/accessibility-audit/SKILL.tr.md)

**Web performans denetimi** · `web-performance-audit`

- Ne zaman: Bir web sayfasını veya front-end uygulamasını Core Web Vitals (LCP, INP, CLS) ve destekleyici metriklerle yükleme ve çalışma zamanı performansı açısından denetler; her sorunu kritik render yolu, JavaScript, görseller, fontlar veya üçüncü taraf kodlardaki nedenine bağlar ve beklenen etkisi ile doğrulama yöntemi belirtilmiş öncelikli düzeltmeler verir. Bir sayfa yavaş hissettirdiğinde, saha verisinde Core Web Vitals kaldığında, performans bütçesi aşıldığında veya bir lab raporu ya da trace'in yorumlanması gerektiğinde kullanılır.
- Örnek istek: _"Ürün listeleme sayfamızda mobilde LCP 4,8 sn, INP 350 ms civarında. Lab raporu ve sayfanın head bölümü ekte. Önce neyi düzeltmeliyiz?"_
- İlgili: `performance-optimization`, `performance-test-plan`, `observability-plan`, `slo-definition`, `component-design`
- Dosya: [skills/05-engineering/developer/frontend/web-performance-audit/SKILL.tr.md](skills/05-engineering/developer/frontend/web-performance-audit/SKILL.tr.md)

**Durum yönetimi tasarımı** · `state-management-design`

- Ne zaman: Front-end'deki her durum parçasının nerede tutulacağını (yerel bileşen, URL, form, paylaşılan istemci, sunucu önbelleği, kalıcı depolama) ve nasıl aktığını, eşitlendiğini, geçersiz kılındığını ve test edildiğini framework'ten bağımsız biçimde tasarlar; global store kullanımını gerekçelendirir. Bir front-end özelliği veya uygulaması başlarken, durum ekranlar arasında tekrarlandığında ya da tutarsızlaştığında, ekip global store eklemeyi veya kaldırmayı tartışırken ya da sunucu verisi önbellekleme ve iyimser güncelleme kararları verilecekken kullanılır.
- Örnek istek: _"Sipariş yönetimi ekranlarımız düzenlemeden sonra eski veri gösteriyor ve her şey tek bir global store'da. Durum yönetimini yeniden tasarlamamıza yardım et."_
- İlgili: `component-design`, `technical-design-doc`, `api-contract`, `adr`, `web-performance-audit`
- Dosya: [skills/05-engineering/developer/frontend/state-management-design/SKILL.tr.md](skills/05-engineering/developer/frontend/state-management-design/SKILL.tr.md)

#### Mobile Özel

**Uygulama mağazası sürüm notları** · `app-store-release-notes`

- Ne zaman: Bir changelog, iş kaydı listesi veya pull request başlıklarından mobil uygulama mağazaları için kısa, kullanıcıya dönük \"Yenilikler\" sürüm notları yazar; iç değişiklikleri ayıklar, her mağazanın karakter sınırına uyar ve yerelleştirilmiş varyantlar hazırlar. Bir mobil sürüm mağazaya gönderilmek üzereyken, ham bir changelog mağaza metnine dönüştürülecekken veya notların bir mağaza için yerelleştirilmesi ya da kısaltılması gerektiğinde kullanılır.
- Örnek istek: _"Bu sprintte merge edilen PR başlıklarını 5.3 sürümü için App Store ve Google Play sürüm notlarına çevir, İngilizce ve Türkçe."_
- İlgili: `release-notes`, `changelog-entry`, `mobile-release-checklist`, `microcopy`, `voice-and-tone-guide`
- Dosya: [skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.tr.md](skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.tr.md)

**Mobil sürüm kontrol listesi** · `mobile-release-checklist`

- Ne zaman: Bir mobil uygulama sürümü için sürümleme, build ve imzalama, izinler ve gizlilik beyanları, mağaza sayfası ve görselleri, kalite kapıları, backend ve zorunlu güncelleme uyumluluğu, kademeli yayın, izleme ve geri alma konularını kapsayan bir go/no-go kontrol listesi oluşturup yürütür; her maddeyi kanıtıyla tamam, açık veya engelli olarak raporlar. Bir iOS veya Android build'i mağaza gönderimine ya da kademeli yayına hazırlanırken veya ekip tekrarlanabilir bir mobil sürüm kontrol listesi istediğinde kullanılır.
- Örnek istek: _"Android ve iOS uygulamalarımızın 4.2.0 sürümünü gelecek salı gönderiyoruz. Konuma dayalı kampanyalar ekliyor. Mobil sürüm kontrol listesini benimle birlikte yürüt."_
- İlgili: `app-store-release-notes`, `release-quality-gate`, `deployment-checklist`, `rollback-plan`, `go-no-go`
- Dosya: [skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.tr.md](skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.tr.md)

### Teknik Lider

#### Teknik Liderlik

**Kodlama standartları yazma** · `coding-standards`

- Ne zaman: Bir ekibin kodlama standartlarını kısa ve numaralı kurallar olarak yazar veya günceller; her kural gerekçe, iyi ve kötü örnek, önem derecesi (zorunlu veya önerilen) ve nasıl uygulatıldığıyla (formatter, linter, inceleme, test) birlikte gelir ve araçların çözemediği kararlara odaklanır. Bir ekip kurulurken veya birleşirken, incelemelerde aynı stil ya da tasarım konuları sürekli tartışıldığında, yeni bir dil veya framework benimsendiğinde ya da mevcut standartlar çok uzun, eskimiş veya uygulanmıyorsa kullanılır.
- Örnek istek: _"Backend ekibimiz için kodlama standartları yaz. İncelemelerde exception yönetimi, isimlendirme ve pull request'in ne kadar büyük olması gerektiği konusunda sürekli tartışıyoruz."_
- İlgili: `clean-code-review`, `code-review`, `review-comment-writing`, `working-agreement`, `adr`
- Dosya: [skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.tr.md)

**Teknik iş tahmini** · `technical-estimation`

- Ne zaman: Teknik bir işi bağımlılık ve riske göre sıralanmış, doğrulanabilir küçük görevlere böler; her görevi aralık olarak tahmin eder, varsayımları ve bilinmeyenleri açık yazar, entegrasyon, test ve sürüm eforunu ekler, güven düzeyini ve rakamı neyin değiştireceğini belirtir. Teknik lidere \"bu ne kadar sürer?\" sorulduğunda, bir özellik, taşıma veya teknik girişimin planlama ya da taahhüt için boyutlandırılması gerektiğinde veya mevcut bir tahminin sorgulanıp yeniden baz alınması gerektiğinde kullanılır.
- Örnek istek: _"Ürün ekibi web uygulamamıza kurumsal kimlik sağlayıcımızla SSO eklemenin ne kadar süreceğini soruyor. Aralıklar ve varsayımlarla bir tahmin ver."_
- İlgili: `task-breakdown`, `estimation-three-point`, `spike-report`, `technical-risk-review`, `monte-carlo-forecast`
- Dosya: [skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.tr.md)

**Geliştirici oryantasyonu** · `technical-onboarding`

- Ne zaman: Ekibe katılan bir geliştirici için teknik oryantasyon planı hazırlar: doğrulama adımlı ortam kurulumu, rehberli kod tabanı ve mimari turu, çalışma biçimi, giderek zorlaşan ilk işler, kilit kişiler ve kontrol noktaları; hepsini kişinin deneyimine ve rolüne göre uyarlar. Yeni veya başka ekipten gelen bir geliştirici başladığında, teknik liderin yeni gelen için ilk haftaları hazırlaması gerektiğinde ya da mevcut oryantasyon çok yavaş olduğu için yeniden yapılandırılacağında kullanılır.
- Örnek istek: _"Pazartesi ödeme ekibimize orta seviye bir backend geliştirici katılıyor. Kurulum ve ilk işler dahil ilk iki hafta için teknik oryantasyon planı hazırla."_
- İlgili: `onboarding-plan-30-60-90`, `readme-writing`, `legacy-code-comprehension`, `coding-standards`, `onboarding-guide`
- Dosya: [skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.tr.md)

**Teknik risk incelemesi** · `technical-risk-review`

- Ne zaman: Bir özellik, proje veya sürüm planı için yapılandırılmış bir teknik risk incelemesi yapar: mimari, bağımlılıklar, teknoloji yeniliği, veri, entegrasyon, performans, güvenlik, işletilebilirlik, yetkinlik ve takvim boyunca teslimat ve kalite risklerini belirler, olasılık ve etkiyi puanlar, erken uyarı sinyallerini adlandırır, sorumlularıyla azaltma aksiyonlarını ve riski en ucuza düşüren deneyleri önerir. Başlangıçta veya bir plana taahhüt vermeden önce, büyük bir sürümden önce, proje uyarı işaretleri gösterdiğinde veya paydaşlar teknik olarak neyin ters gidebileceğini sorduğunda kullanılır.
- Örnek istek: _"Fatura üretimini olay güdümlü bir servise taşıyacağımız 3 aylık bir projeye başlıyoruz. Plana taahhüt vermeden önce teknik riskleri incele."_
- İlgili: `risk-register`, `technical-estimation`, `spike-report`, `threat-model`, `architecture-review`
- Dosya: [skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.tr.md)

**Kod kalitesi raporu** · `code-quality-report`

- Ne zaman: Statik analiz ve kod metriklerini (kapsam, karmaşıklık, tekrar, code smell'ler, güvenlik açıkları, bağımlılık yaşı) ve trendlerini sinyali gürültüden ayıran, sıcak noktaları değişim sıklığı ve hatalarla ilişkilendiren ve az sayıda önceliklendirilmiş aksiyon öneren bir kod kalitesi raporuna dönüştürür. Teknik lider kod sağlığını ekibe veya yönetime raporlayacağında, kalite kapısı sonuçları veya bir metrik panosu yorumlanacağında ya da refactoring eforunun nereye yatırılacağına karar verilirken kullanılır.
- Örnek istek: _"Son üç sürümün statik analiz dökümü ekte. Mühendislik yöneticisi için bir kod kalitesi raporu yaz ve gelecek çeyrekte nereye odaklanmamız gerektiğini söyle."_
- İlgili: `tech-debt-assessment`, `coding-standards`, `test-gap-finder`, `refactoring`, `defect-trend-analysis`
- Dosya: [skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.tr.md)

## Kalite Güvence ve Test

### Test Analisti / Test Mühendisi

#### Test Stratejisi ve Planlama

**Test stratejisi yazma** · `test-strategy`

- Ne zaman: Bir ürün, program veya kurum için test seviyelerini, test türlerini, ortamları, araç kategorilerini, veri yaklaşımını ve risk bazlı odağı tanımlayan bir test stratejisi yazar. Yeni bir ürün veya büyük bir girişim başladığında, ekipler arasında test yaklaşımı tutarsız olduğunda ya da bir sistemin genel olarak nasıl test edileceği sorulduğunda kullanılır.
- Örnek istek: _"Yeni müşteri kazanım platformumuz için test stratejisi yaz: web + mobil ön yüz, 12 mikroservis, core banking ve KYC sağlayıcısı entegrasyonları var."_
- İlgili: `test-plan`, `risk-based-testing`, `environment-strategy`, `automation-framework-design`, `nfr-specification`
- Dosya: [skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.tr.md)

**Test planı yazma** · `test-plan`

- Ne zaman: Bir sürüm, proje veya özellik seti için test öğelerini, kapsamı, yaklaşımı, ortamları, takvimi, rolleri, giriş/çıkış ve askıya alma kriterlerini, teslimatları ve riskleri ISO/IEC/IEEE 29119-3 ile uyumlu biçimde ele alan bir test planı yazar. Bir sürüm veya proje için üzerinde anlaşılmış test kapsamı ve takvimi gerektiğinde ya da test planı dokümanı istendiğinde kullanılır.
- Örnek istek: _"Hasar portalının 4.2 sürümü için test planı hazırla: yeni doküman yükleme, revize onay akışı ve iki hata düzeltmesi var. Code freeze üç hafta sonra."_
- İlgili: `test-strategy`, `risk-based-testing`, `release-quality-gate`, `test-summary-report`, `uat-plan`
- Dosya: [skills/06-quality/qa-analyst/strategy/test-plan/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/test-plan/SKILL.tr.md)

**Risk bazlı test önceliklendirme** · `risk-based-testing`

- Ne zaman: Ürün risk öğelerini olasılık ve etkiye göre değerlendirerek test eforunu önceliklendirir; risk matrisi, öğe bazında test derinliği ve koşum sırası üretir. Zaman veya kişi kısıtlı olduğunda, önce neyin ve ne derinlikte test edileceğine karar verilirken ya da paydaşlar hangi risklerin kapsandığını ve hangilerinin kaldığını görmek istediğinde kullanılır.
- Örnek istek: _"Bu sürüm için 5 test günümüz var. İşte 14 değişiklik. Önce neyi, ne derinlikte test edelim?"_
- İlgili: `test-strategy`, `test-plan`, `regression-selection`, `risk-register`, `impact-analysis`
- Dosya: [skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.tr.md)

**Gereksinimlerin test edilebilirlik incelemesi** · `testability-review`

- Ne zaman: Gereksinimleri, user story'leri veya kabul kriterlerini test edilebilirlik açısından inceler; belirsiz, ölçülemez, eksik, test edilemez veya hata davranışı tanımlanmamış maddeleri her biri için somut bir yeniden yazım önerisiyle işaretler. Test tasarımı veya tahminden önce, refinement oturumlarında ya da gereksinimlerin test için yeterince net olup olmadığı sorulduğunda kullanılır.
- Örnek istek: _"Test case yazmaya başlamadan önce bu 8 user story'yi test edilebilirlik açısından kontrol et."_
- İlgili: `ambiguity-detection`, `acceptance-criteria`, `requirements-review-checklist`, `test-scenarios-from-requirements`, `nfr-specification`
- Dosya: [skills/06-quality/qa-analyst/strategy/testability-review/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/testability-review/SKILL.tr.md)

#### Test Tasarımı

**Gereksinimden test senaryosu çıkarma** · `test-scenarios-from-requirements`

- Ne zaman: Gereksinimlerden, user story'lerden, use case'lerden veya kabul kriterlerinden kaynağa izlenebilir ve öncelikli üst düzey test senaryoları (pozitif, negatif, uç, yetki, entegrasyon, fonksiyonel olmayan) çıkarır. Bir özellik için test tasarımı başladığında, bir story'nin kapsamı kontrol edilirken ya da bir gereksinim için neyin test edilmesi gerektiği sorulduğunda kullanılır.
- Örnek istek: _"Bu story için test senaryolarını çıkar: müşteri siparişini kargoya verilene kadar iptal edebilir ve ödemesi orijinal ödeme yöntemine iade edilir."_
- İlgili: `test-case-writing`, `testability-review`, `equivalence-boundary-analysis`, `traceability-matrix`, `bdd-feature-file`
- Dosya: [skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.tr.md](skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.tr.md)

**Test case yazma** · `test-case-writing`

- Ne zaman: ID, başlık, ön koşullar, test verisi, numaralı adımlar, adım bazında beklenen sonuçlar, öncelik ve gereksinim izlenebilirliği içeren ayrıntılı ve koşturulabilir test case'ler yazar. Senaryoların tekrarlanabilir manuel case'lere dönüştürülmesi gerektiğinde, koşum veya otomasyon için case hazırlanırken ya da bir özellik veya story için test case yazılması istendiğinde kullanılır.
- Örnek istek: _"Şifre sıfırlama akışı için test case yaz: e-posta bağlantısı 30 dakika geçerli, yeni şifre politikaya uymalı, eski oturumlar kapatılıyor."_
- İlgili: `test-scenarios-from-requirements`, `equivalence-boundary-analysis`, `test-data-design`, `test-automation-script`, `traceability-matrix`
- Dosya: [skills/06-quality/qa-analyst/design/test-case-writing/SKILL.tr.md](skills/06-quality/qa-analyst/design/test-case-writing/SKILL.tr.md)

**Denklik sınıfı ve sınır değer analizi** · `equivalence-boundary-analysis`

- Ne zaman: Girdi alanlarına, parametrelere ve iş kurallarına denklik sınıfı bölümleme ve sınır değer analizi uygular; geçerli ve geçersiz sınıfları, sınır değerlerini (iki veya üç değerli) ve beklenen sonuçlarıyla en küçük test değeri setini üretir. Bir girdide aralık, uzunluk, format, tarih veya sabit liste olduğunda ya da bir alan veya kural için hangi değerlerin test edileceği sorulduğunda kullanılır.
- Örnek istek: _"Kredi başvurusuna sınır değer analizi uygula: tutar 1.000-50.000, vade 6-60 ay, başvuru sahibinin kredi bitişindeki yaşı 18-70."_
- İlgili: `test-case-writing`, `decision-table-testing`, `pairwise-testing`, `test-data-design`, `test-scenarios-from-requirements`
- Dosya: [skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.tr.md](skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.tr.md)

**Karar tablosu testi** · `decision-table-testing`

- Ne zaman: İş kurallarından koşulları ve aksiyonları listeleyerek karar tabloları kurar, kombinasyonları çıkarır, ilgisiz olanları daraltır ve her kural sütunu için bir test türetir; bu sırada eksik ve çelişkili kuralları ortaya çıkarır. Davranış koşul kombinasyonlarına bağlı olduğunda (uygunluk, fiyatlama, onaylar, indirimler, yönlendirme) ya da bir eğer-ise kural setinin test edilmesi istendiğinde kullanılır.
- Örnek istek: _"Kargo ücreti için karar tablosu kur: 200 TL üzeri üyelere ücretsiz, standart 29 TL, ekspres +40 TL, adalara +50 TL, üyelere ekspres yarı fiyat."_
- İlgili: `equivalence-boundary-analysis`, `business-rules-catalog`, `test-case-writing`, `pairwise-testing`, `state-transition-testing`
- Dosya: [skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.tr.md](skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.tr.md)

**Durum geçiş testi** · `state-transition-testing`

- Ne zaman: Bir varlığı veya iş akışını durumlar, olaylar, koşullar ve aksiyonlar olarak modeller; ardından tüm geçerli geçişler, geçersiz geçişler (reddedilmesi gereken durum-olay çiftleri) ve önemli geçiş dizileri (0-switch ve 1-switch kapsamı) için testler türetir. Davranış duruma veya geçmişe bağlı olduğunda (sipariş, başvuru, onay, hesap, oturum, cihaz) ya da bir iş akışının veya yaşam döngüsünün test edilmesi istendiğinde kullanılır.
- Örnek istek: _"Satın alma talebi için durum geçiş testleri oluştur: Taslak, Gönderildi, Onaylandı, Reddedildi, İptal, Sipariş verildi. Yalnızca talep sahibi, sipariş verilmeden önce iptal edebilir."_
- İlgili: `state-model`, `decision-table-testing`, `test-case-writing`, `test-scenarios-from-requirements`, `api-test-design`
- Dosya: [skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.tr.md](skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.tr.md)

**İkili kombinasyon testi** · `pairwise-testing`

- Ne zaman: Parametre değerlerinin her ikilisini (kritik parametreler için daha yüksek dereceyi) değerler arası kısıtlara uyarak kapsayan azaltılmış bir test kombinasyonu seti üretir; azaltmayı ve kalan riski açıklar. Çok sayıda parametre veya yapılandırma (tarayıcı, cihaz, rol, ayar, ürün seçeneği) birleşince tümünü test etmek mümkün olmadığında kullanılır.
- Örnek istek: _"Ödeme adımı için ikili kombinasyonlar üret: 4 tarayıcı, 3 ödeme yöntemi, 2 kullanıcı tipi, 3 teslimat seçeneği, kupon var/yok. Apple Pay yalnızca Safari'de."_
- İlgili: `equivalence-boundary-analysis`, `decision-table-testing`, `test-case-writing`, `risk-based-testing`, `test-data-design`
- Dosya: [skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.tr.md](skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.tr.md)

**Keşif testi görev tanımı** · `exploratory-test-charter`

- Ne zaman: Görev, hedef alanlar, kaynaklar, yoklanacak riskler, test sezgisel yöntemleri ve kâhinler (oracle), süre sınırı ve not, hata ve sorular için bir değerlendirme şablonu içeren oturum bazlı keşif testi görev tanımları yazar. Yeni veya değişen bir özellik için keşif testi gerektiğinde, senaryolu testler henüz yokken veya yetmediğinde ya da keşif testi fikirleri istendiğinde kullanılır.
- Örnek istek: _"CSV'den toplu ürün fiyatı içe aktarma özelliği için keşif testi görev tanımları yaz. Bir öğleden sonra için 2 test uzmanımız var."_
- İlgili: `test-scenarios-from-requirements`, `risk-based-testing`, `bug-report`, `heuristic-evaluation`, `test-summary-report`
- Dosya: [skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.tr.md](skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.tr.md)

**Test verisi tasarlama** · `test-data-design`

- Ne zaman: Gerçekçi, gizlilik açısından güvenli; denklik sınıflarını, sınırları, durumları ve ilişkisel uç durumları kapsayan test veri setleri ile ortam bazında hazırlama ve sıfırlama yaklaşımı tasarlar. Testler belirli veriye ihtiyaç duyduğunda, test için üretim verisi kullanılması gündeme geldiğinde, veri hazırlığı koşumu veya otomasyonu engellediğinde ya da bir özelliğin testi için hangi verinin gerektiği sorulduğunda kullanılır.
- Örnek istek: _"Kredi başvuru akışımız için test verisi tasarla: farklı gelir bantlarında başvuranlar, ortak başvuranlar, mevcut müşteriler ve kara listedeki kimlikler; SIT ve UAT için."_
- İlgili: `equivalence-boundary-analysis`, `test-case-writing`, `data-classification`, `environment-strategy`, `privacy-impact-assessment`
- Dosya: [skills/06-quality/qa-analyst/design/test-data-design/SKILL.tr.md](skills/06-quality/qa-analyst/design/test-data-design/SKILL.tr.md)

**BDD feature dosyası yazma** · `bdd-feature-file`

- Ne zaman: İş tarafının okuyabileceği özellik açıklaması, background, bildirimsel senaryolar ve örnek tablolu scenario outline'lar içeren, etiketli ve gereksinimlere izlenebilir Gherkin feature dosyaları yazar. Ekip davranış odaklı geliştirme veya örneklerle tanımlama uyguluyorsa, kabul kriterleri çalıştırılabilir tanımlara dönüşecekse ya da mevcut Gherkin emir kipinde, arayüze bağımlı veya bakımı zor ise kullanılır.
- Örnek istek: _"Kupon kuralı için feature dosyası yaz: sipariş başına bir kupon, en az 250 TL sepet, kampanyalı fiyatlarla birleşmez, süresi dolmuş kupon reddedilir."_
- İlgili: `acceptance-criteria`, `user-story`, `test-scenarios-from-requirements`, `test-automation-script`, `equivalence-boundary-analysis`
- Dosya: [skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.tr.md](skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.tr.md)

**API testi tasarlama** · `api-test-design`

- Ne zaman: Her endpoint için sözleşme ve şema, durum kodları, kimlik doğrulama ve yetkilendirme, girdi doğrulama, iş kuralları, idempotency, sayfalama, eşzamanlılık ve hata formatını; negatif ve güvenlik odaklı durumlarla birlikte kapsayan API testleri tasarlar. Bir API sözleşmesi (OpenAPI, GraphQL şeması, gRPC proto veya gayriresmî tanım) için test tasarımı gerektiğinde, API testleri otomatikleştirilmeden önce ya da mevcut API testlerinin yeterliliği incelenirken kullanılır.
- Örnek istek: _"POST /orders ve GET /orders/{id} için API testleri tasarla: JWT ile kimlik doğrulama, müşteriler yalnızca kendi siparişlerini görür, Idempotency-Key başlığı, doğrulama hatalarında 422."_
- İlgili: `api-contract`, `api-design-review`, `test-automation-script`, `security-requirements`, `integration-test-writing`
- Dosya: [skills/06-quality/qa-analyst/design/api-test-design/SKILL.tr.md](skills/06-quality/qa-analyst/design/api-test-design/SKILL.tr.md)

#### Koşum ve Hatalar

**Hata raporu yazma** · `bug-report`

- Ne zaman: Net başlık, ortam ve build, ön koşullar, en az sayıda numaralı adım, beklenen ve gerçekleşen sonuç, tekrarlanma oranı, kanıt, etki ve önerilen önem derecesi içeren, tekrarlanabilir ve önceliklendirmeye hazır bir hata raporu yazar. Bir test uzmanı, geliştirici veya kullanıcı bir hata bulduğunda ve kaydedilmesi gerektiğinde, mevcut rapor belirsiz ya da tekrarlanamıyorsa veya biri gözlemlerini yapıştırıp hata kaydına dönüştürülmesini istediğinde kullanılır.
- Örnek istek: _"Hata raporu yaz: iOS uygulamasında ödeme adımında teslimat adresi değiştirildikten sonra kargo ücreti hâlâ eski şehre göre hesaplanıyor. Çoğu zaman oluyor, staging'de build 4.12.0."_
- İlgili: `bug-triage`, `bug-reproduction`, `log-analysis`, `test-case-writing`, `ticket-triage`
- Dosya: [skills/06-quality/qa-analyst/execution/bug-report/SKILL.tr.md](skills/06-quality/qa-analyst/execution/bug-report/SKILL.tr.md)

**Hata önceliklendirme** · `bug-triage`

- Ne zaman: Bir grup hatayı; bütünlüğünü doğrulayarak, mükerrerleri bularak, önem derecesini (etki) öncelikten (düzeltme sırası) ayırarak, sorumlu ve hedef atayarak ve sürümü engelleyenleri işaretleyerek önceliklendirir; bir karar tablosu ve takip listesi üretir. Yeni veya birikmiş hatalar bir önceliklendirme toplantısında gözden geçirilecekse, sürüm yaklaşırken açık hatalar için engelleyici kararı gerekiyorsa ya da önce hangi hataların düzeltileceği sorulduğunda kullanılır.
- Örnek istek: _"Cuma günkü sürüm öncesi bu 14 açık hatayı önceliklendir: önem, öncelik, mükerrerler ve hangilerinin sürümü engellediğine karar ver."_
- İlgili: `bug-report`, `release-quality-gate`, `defect-trend-analysis`, `risk-based-testing`, `ticket-triage`
- Dosya: [skills/06-quality/qa-analyst/execution/bug-triage/SKILL.tr.md](skills/06-quality/qa-analyst/execution/bug-triage/SKILL.tr.md)

**Regresyon testi seçimi** · `regression-selection`

- Ne zaman: Belirli bir değişiklik için neyin değiştiğini, doğrudan ve dolaylı etkisini (ortak kod, veri, entegrasyonlar, konfigürasyon), riski ve yakın dönem hata geçmişini analiz ederek regresyon test seti seçer; testleri zorunlu, önerilen ve isteğe bağlı olarak katmanlar ve kalan riski açıkça yazar. Bir sürüm, hotfix veya merge regresyon testi gerektirdiğinde ama tam set çok yavaş ya da pahalıysa veya bir değişiklikten sonra neyin yeniden test edilmesi gerektiği sorulduğunda kullanılır.
- Örnek istek: _"İndirim hesaplama servisini değiştirdik ve PDF kütüphanesini yükselttik. Yarınki hotfix öncesi hangi regresyon testlerini koşmamız şart?"_
- İlgili: `impact-analysis`, `risk-based-testing`, `test-summary-report`, `automation-candidate-selection`, `test-gap-finder`
- Dosya: [skills/06-quality/qa-analyst/execution/regression-selection/SKILL.tr.md](skills/06-quality/qa-analyst/execution/regression-selection/SKILL.tr.md)

**Test özet raporu** · `test-summary-report`

- Ne zaman: Test edilen ve edilmeyen kapsamı, koşum sonuçlarını, gereksinim ve risklere göre kapsamı, önem derecesine göre açık hataları, plandan sapmaları, kalan riski ve net bir öneriyi belirten, ISO/IEC/IEEE 29119-3 içeriğiyle uyumlu bir test özet (tamamlama) raporu yazar. Bir test seviyesi, iterasyon veya sürüm döngüsünün sonunda, paydaşların karar vermeye hazır bir kalite durumuna ihtiyacı olduğunda ya da ham koşum sayılarının rapora dönüşmesi gerektiğinde kullanılır.
- Örnek istek: _"Şu sayılarla 3.4 sürümünün test özet raporunu yaz: 412 case, 389 geçti, 11 kaldı, 12 bloke, 7 açık hata (1 kritik), performans testi koşulmadı."_
- İlgili: `test-plan`, `release-quality-gate`, `bug-triage`, `defect-trend-analysis`, `executive-summary`
- Dosya: [skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.tr.md](skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.tr.md)

**Sürüm kalite kapısı değerlendirmesi** · `release-quality-gate`

- Ne zaman: Sürüm hazırlığını üzerinde anlaşılmış çıkış kriterlerine (testler, hatalar, kapsam, fonksiyonel olmayan sonuçlar, operasyonel hazırlık, onaylar) göre değerlendirir; her kriteri kanıtıyla sağlandı, sağlanmadı veya muaf tutuldu olarak derecelendirir ve koşullar ile kabul edilen risklerle birlikte yayına al, koşullu yayına al veya yayına alma önerisi üretir. Bir üretim sürümü veya büyük bir dağıtım öncesinde, bir go/no-go toplantısında ya da bir build'in yayına hazır olup olmadığı sorulduğunda kullanılır.
- Örnek istek: _"5.2 sürümünü çıkış kriterlerimize göre değerlendir: açık kritik/majör hata yok, %95 geçme oranı, regresyon tamam, performans p95 800 ms altında, güvenlik taraması temiz."_
- İlgili: `test-summary-report`, `bug-triage`, `go-no-go`, `deployment-checklist`, `rollback-plan`
- Dosya: [skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.tr.md](skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.tr.md)

**Hata trendi analizi** · `defect-trend-analysis`

- Ne zaman: Hata verisini zaman içinde analiz ederek yoğunluk, kaçak hata (leakage) oranı, yeniden açılma oranı, yaşlanma ve kök neden kategorilerini ortaya koyar; gerçek kalite sinyalini raporlama gürültüsünden ayırır ve kanıta dayalı iyileştirme aksiyonlarıyla bitirir. Ekip kalitenin neden düştüğünü sorduğunda, retrospektif veya kalite değerlendirmesi hazırlanırken, canlıya kaçan hatalar açıklanmak istendiğinde ya da elde bir hata dökümü olup trendlerin yorumlanması gerektiğinde kullanılır.
- Örnek istek: _"Son 6 sürümün hata dökümü ekte. Trendleri analiz et: hatalar nereden geliyor, ne kadarı canlıya kaçıyor, neyi değiştirmeliyiz?"_
- İlgili: `bug-triage`, `test-summary-report`, `five-whys`, `engineering-metrics-review`, `code-quality-report`
- Dosya: [skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.tr.md](skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.tr.md)

#### Kullanıcı Kabul

**Kullanıcı kabul testi planı** · `uat-plan`

- Ne zaman: Kullanıcı kabul testini planlar: hedefler, iş tarafı katılımcıları ve rolleri, senaryo kapsamı, ortam ve veri hazırlığı, takvim, hata yönetimi, giriş/çıkış kriterleri ve resmî onay yolu. Bir sürüm, proje aşaması veya tedarikçi teslimatı iş birimi kabulü gerektirdiğinde, UAT'nin nasıl organize edileceği sorulduğunda ya da iş kullanıcılarının canlıya geçmeden önce çözümün gerçek işlerini desteklediğini teyit etmesi gerektiğinde kullanılır.
- Örnek istek: _"Yeni faturalama modülü için UAT planla: finans ve satış kullanıcıları canlıya geçişten önce iki hafta test edecek."_
- İlgili: `uat-scenarios`, `test-plan`, `acceptance-certificate`, `requirements-sign-off`, `release-quality-gate`
- Dosya: [skills/06-quality/qa-analyst/uat/uat-plan/SKILL.tr.md](skills/06-quality/qa-analyst/uat/uat-plan/SKILL.tr.md)

**Kabul testi senaryoları** · `uat-scenarios`

- Ne zaman: Ekranlar ve tıklamalar yerine gerçek roller, iş olayları ve sonuçlar üzerine kurulu, iş dilinde uçtan uca kullanıcı kabul senaryoları yazar; her senaryoda gerçekçi veri, iş tarafının doğrulayabileceği kontrol noktaları ve geçme kriteri bulunur. İş kullanıcılarının UAT'de koşacağı senaryolar gerektiğinde, gereksinimler veya süreçler kabul akışlarına dönüştürülecekken ya da mevcut UAT metinleri teknik test case gibi okunduğunda kullanılır.
- Örnek istek: _"İade süreci için UAT senaryoları yaz: mağaza personeli, depo ve finans yeni iade akışını uçtan uca test edecek."_
- İlgili: `uat-plan`, `test-scenarios-from-requirements`, `to-be-process`, `acceptance-criteria`, `test-data-design`
- Dosya: [skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.tr.md](skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.tr.md)

### Test Otomasyon Mühendisi

#### Otomasyon

**Otomasyon adayı seçimi** · `automation-candidate-selection`

- Ne zaman: Adayları koşum sıklığı, iş riski, özelliğin kararlılığı, deterministiklik, veri ve ortam kontrolü ile yazma/bakım maliyetine göre puanlayarak hangi testlerin otomatikleştirileceğini seçer; her birini güvenilir en ucuz test seviyesine yerleştirir ve kaba geri dönüş tahminiyle sıralı bir backlog verir. Ekip sırada neyi otomatikleştireceğini sorduğunda, büyük bir manuel regresyon seti olduğunda, otomasyon yatırımı gerekçelendirilecekken ya da düşük değerli UI testlerinin otomasyonu durdurulmak istendiğinde kullanılır.
- Örnek istek: _"350 manuel regresyon case'imiz var. Önce hangilerini, hangi seviyede otomatikleştirmeliyiz?"_
- İlgili: `automation-framework-design`, `test-automation-script`, `regression-selection`, `risk-based-testing`, `flaky-test-analysis`
- Dosya: [skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.tr.md](skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.tr.md)

**Otomatik test yazma** · `test-automation-script`

- Ne zaman: Ekibin dili ve framework'ünde page object veya API istemcileri, bağımsız test verisi, koşula dayalı açık beklemeler ve kesin doğrulamalar kullanan bakımı kolay bir otomatik test yazar; önce testin doğru nedenle kaldığını gösterir. Manuel bir test case, senaryo veya Gherkin adımı otomatik test koduna dönüştürülecekken, bir UI veya API testi yazılması istendiğinde ya da mevcut bir otomatik test güvenilir olacak şekilde yeniden yazılacakken kullanılır.
- Örnek istek: _"Bu test case'i TypeScript setimizde API testi olarak otomatikleştir: süresi dolmuş kuponla sipariş oluşturmak 422 dönmeli ve stok ayırmamalı."_
- İlgili: `automation-candidate-selection`, `automation-framework-design`, `test-case-writing`, `bdd-feature-file`, `flaky-test-analysis`
- Dosya: [skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.tr.md](skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.tr.md)

**Kararsız test analizi** · `flaky-test-analysis`

- Ne zaman: Kararsız (flaky) otomatik testleri analiz eder: koşum geçmişinden kararsızlık oranını ölçer, nedeni sınıflar (zamanlama ve async, paylaşılan durum ve sıra bağımlılığı, test verisi, ortam ve altyapı, dış bağımlılıklar, eşzamanlılık, ürünün deterministik olmayan davranışı), tek değişkenli deneylerle teyit eder ve kök nedene yönelik kararlılaştırma ile karantina politikası önerir. Kod değişmeden testler bazen geçip bazen kaldığında, CI'da yeniden koşum rutinleştiğinde ya da ekip kırmızı build'lere artık güvenmediğinde kullanılır.
- Örnek istek: _"Bu 6 uçtan uca test CI'da yaklaşık 10 koşumda bir rastgele kalıyor, lokalde hiç kalmıyor. Hata logları ekte. Neden ve nasıl düzeltiriz?"_
- İlgili: `test-automation-script`, `automation-framework-design`, `debugging-hypotheses`, `pipeline-failure-triage`, `log-analysis`
- Dosya: [skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.tr.md](skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.tr.md)

**Test otomasyon çatısı tasarımı** · `automation-framework-design`

- Ne zaman: Bir test otomasyon çatısı tasarlar: test seviyeleri ve payları, katmanlı mimari (testler, iş aksiyonları, page object/API istemcileri, sürücüler), test verisi ve ortam yönetimi, konfigürasyon ve gizli bilgiler, raporlama ve izlenebilirlik, paralellik ve kalite kapılarıyla CI entegrasyonu ve bakım kolaylığı için kurallar. Bir ekip otomasyona başladığında, mevcut set yavaş, kırılgan veya sahipsiz olup yeniden tasarım gerektirdiğinde ya da UI, API ve sözleşme testleri için bir yapı seçilecekken kullanılır.
- Örnek istek: _"Web uygulamamız ve REST API'lerimiz için bir test otomasyon çatısı tasarla; set her pull request'te 15 dakikadan kısa sürede koşmalı."_
- İlgili: `test-strategy`, `automation-candidate-selection`, `test-automation-script`, `pipeline-design`, `flaky-test-analysis`
- Dosya: [skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.tr.md](skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.tr.md)

### Performans Test Mühendisi

#### Performans Testi

**Performans test planı** · `performance-test-plan`

- Ne zaman: Ölçülebilir kabul kriterlerine (gecikme yüzdelikleri, verim, hata oranı, kaynak sınırları) bağlı hedefler, üretim verisinden veya iş tahminlerinden türetilmiş bir iş yükü modeli, test türleri (yük, stres, dayanıklılık, ani yük, ölçeklenebilirlik), senaryolar, test verisi, ortam ve üretimden farkları, izleme, giriş/çıkış kriterleri ve riskler içeren bir performans test planı yazar. Bir sürüm, taşıma veya beklenen trafik artışı öncesinde, fonksiyonel olmayan gereksinimlerin doğrulanması gerektiğinde ya da sıfırdan bir performans testi tasarlanacağında kullanılır.
- Örnek istek: _"Ödeme trafiğini üç katına çıkarabilecek bir kampanya başlatıyoruz. Checkout API'si ve bağımlılıkları için bir performans test planı yaz."_
- İlgili: `load-test-analysis`, `capacity-test-report`, `slo-definition`, `test-data-design`, `nfr-to-architecture`
- Dosya: [skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.tr.md](skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.tr.md)

**Yük testi sonuç analizi** · `load-test-analysis`

- Ne zaman: Yük testi sonuçlarını analiz eder: test koşumunu doğrular, verimi, gecikme yüzdeliklerini ve hata oranlarını kabul kriterleriyle karşılaştırır, darboğazı bulmak için istemci tarafı sonuçları sunucu tarafı kaynak, havuz, kuyruk ve veritabanı metrikleriyle ilişkilendirir, kanıta dayalı düzeltmeler ve yeniden testler önerir. Bir yük, stres, ani yük veya dayanıklılık testi koşulduğunda ve raporu, metrikleri veya grafikleri yorumlanacağında ya da bir test sonucu tartışmalı olup ikinci bir görüş gerektiğinde kullanılır.
- Örnek istek: _"Dünkü checkout yük testinin sonuçları ekte: özet tablo, gecikme grafiği açıklaması ve veritabanı CPU'su. Geçtik mi, darboğaz nerede?"_
- İlgili: `performance-test-plan`, `capacity-test-report`, `performance-optimization`, `query-optimization`, `observability-plan`
- Dosya: [skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.tr.md](skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.tr.md)

**Kapasite raporu** · `capacity-test-report`

- Ne zaman: Kademeli yük veya stres testi sonuçlarından SLO'lar içinde sürdürülebilir maksimum yükü belirleyen, sınırlayıcı kaynağı tespit eden, mevcut ve tahmini zirvelere göre payı hesaplayan, ölçekleme davranışını ve sınırlarını açıklayan ve tetikleyicileriyle kapasite aksiyonları öneren bir kapasite raporu yazar. Kapasite, stres veya ölçeklenebilirlik testlerinden sonra, yönetim sistemin ne kadar büyümeyi kaldırabileceğini sorduğunda ya da altyapı boyutlandırması ve ölçekleme sınırlarının test kanıtıyla gerekçelendirilmesi gerektiğinde kullanılır.
- Örnek istek: _"Arama servisinde kırılana kadar kademeli yük testi koştuk. Bir kapasite raporu yaz: gelecek yılın tahminine göre ne kadar payımız var?"_
- İlgili: `load-test-analysis`, `performance-test-plan`, `capacity-planning`, `scalability-review`, `finops-review`
- Dosya: [skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.tr.md](skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.tr.md)

## DevOps, SRE ve Platform

### DevOps / Platform Mühendisi

#### CI/CD

**CI/CD hattı tasarlama** · `pipeline-design`

- Ne zaman: CI ürününden bağımsız olarak uçtan uca bir CI/CD hattı tasarlar: aşamalar, kalite ve güvenlik kapıları, artefakt yönetimi, ortamlar ve terfi kuralları. Yeni bir hat kurulurken, yavaş veya kırılgan bir hat yeniden yapılandırılırken ya da kodun commit'ten üretime nasıl ilerlediği dokümante edilecekken kullanılır.
- Örnek istek: _"Kubernetes üzerinde dev, staging ve prod ortamlarına dağıtılan .NET API'miz için, prod öncesi manuel onay içeren bir CI/CD hattı tasarla."_
- İlgili: `environment-strategy`, `deployment-strategy`, `branching-strategy`, `release-quality-gate`, `secrets-management-plan`
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.tr.md)

**Hat hatası analizi** · `pipeline-failure-triage`

- Ne zaman: Başarısız bir CI/CD çalıştırmasını logları ve bağlamı üzerinden analiz eder; hatayı sınıflandırır (kod, test, kararsız test, bağımlılık, altyapı, yapılandırma, kimlik bilgisi), en olası nedeni kanıtıyla belirler, çözüm ve önleme adımı önerir. Build, test, tarama veya dağıtım işi başarısız olduğunda ve log ya da hata metni paylaşıldığında kullanılır.
- Örnek istek: _"Main branch hattımız bu sabahtan beri Docker build adımında kırılıyor, log ekte. Sorun ne ve nasıl düzeltiriz?"_
- İlgili: `pipeline-design`, `flaky-test-analysis`, `log-analysis`, `stack-trace-analysis`, `dependency-upgrade`
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.tr.md)

**Dağıtım stratejisi seçme** · `deployment-strategy`

- Ne zaman: Belirli bir servis için risk, durum tutma, veritabanı değişiklikleri, trafik kontrolü, maliyet ve geri dönüş hızını tartarak bir dağıtım stratejisi (recreate, rolling, blue-green, canary, shadow, feature flag veya bunların birleşimi) önerir. Bir sürümün kullanıcıya nasıl ulaşacağına karar verilirken ya da mevcut sürümler kesintiye veya riskli toplu geçişlere yol açıyorsa kullanılır.
- Örnek istek: _"Ödeme servisimizi 20 dakikalık bakım penceresiyle dağıtıyoruz. Kesintisiz dağıtım için hangi stratejiye geçmeliyiz?"_
- İlgili: `pipeline-design`, `rollback-plan`, `release-plan`, `schema-migration-plan`, `slo-definition`
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.tr.md)

**Ortam stratejisi** · `environment-strategy`

- Ne zaman: Bir sistemin ortam yapısını tanımlar: hangi ortamların neden var olduğu, üretimle eşdeğerlik, test verisi politikası, erişim ve değişiklik yetkileri, yaşam döngüsü (kalıcı veya geçici) ve sahiplik. Ortamlar amaçsızca çoğaldığında, testler staging'de geçip üretimde kırıldığında ya da yeni bir platform için ortam modeli üzerinde uzlaşılması gerektiğinde kullanılır.
- Örnek istek: _"dev, test, uat, preprod ve prod ortamlarımız var ve hangisinin ne için kullanıldığını kimse bilmiyor. Bizim için bir ortam stratejisi tanımla."_
- İlgili: `pipeline-design`, `test-data-design`, `secrets-management-plan`, `finops-review`, `deployment-strategy`
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.tr.md)

#### Altyapı ve Konteynerler

**Dockerfile inceleme** · `dockerfile-review`

- Ne zaman: Bir Dockerfile'ı (veya Containerfile) imaj boyutu, katman ve önbellek verimliliği, güvenlik sıkılaştırması ve derleme tekrarlanabilirliği açısından inceler; düzeltilmiş kod parçalarıyla önceliklendirilmiş bulgular verir. Bir Dockerfile inceleme için paylaşıldığında, imaj büyük veya yavaş derleniyorsa ya da tarayıcı bulgu veriyorsa ve bir servisin ilk üretim sürümünden önce kullanılır.
- Örnek istek: _"Node.js servisimizin bu Dockerfile'ını incele. İmaj 1,2 GB ve güvenlik taraması 40 zafiyet raporluyor."_
- İlgili: `kubernetes-manifest-review`, `pipeline-design`, `secrets-management-plan`, `dependency-vulnerability-review`
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.tr.md)

**Kubernetes manifest inceleme** · `kubernetes-manifest-review`

- Ne zaman: Kubernetes manifest'lerini, Helm chart'larını veya Kustomize çıktısını kaynak istek ve limitleri, sağlık probe'ları, güvenlik bağlamı, erişilebilirlik (replika, kesinti bütçesi, dağılım), yapılandırma ve secret yönetimi ile işletilebilirlik açısından inceler. Düzeltilmiş YAML ile önceliklendirilmiş bulgular verir. Manifest'ler incelemeye geldiğinde, pod'lar yeniden başladığında veya tahliye edildiğinde ya da bir iş yükü üretime hazırlanırken kullanılır.
- Örnek istek: _"Üretim cluster'ına çıkmadan önce sipariş API'mizin bu Deployment ve Service YAML'ını incele."_
- İlgili: `dockerfile-review`, `secrets-management-plan`, `capacity-planning`, `deployment-strategy`, `resilience-review`
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.tr.md)

**Kod olarak altyapı incelemesi** · `iac-review`

- Ne zaman: Kod olarak altyapıyı (Terraform/OpenTofu, Bicep, CloudFormation, Pulumi, Ansible vb.) ve plan çıktısını güvenlik yanlış yapılandırmaları, state ve sapma riskleri, yıkıcı değişiklikler, modülerlik, adlandırma/etiketleme ve maliyet açısından inceler. Bir IaC pull request'i veya planı incelenecekken, paylaşımlı ya da üretim altyapısına değişiklik uygulanmadan önce veya mevcut bir IaC kod tabanı denetlenirken kullanılır.
- Örnek istek: _"Bu Terraform modülünü ve plan çıktısını incele. Yeni servisimiz için bir storage bucket, bir veritabanı ve bir VPC oluşturuyor."_
- İlgili: `secrets-management-plan`, `finops-review`, `environment-strategy`, `threat-model`, `pipeline-design`
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.tr.md)

**Gizli bilgi yönetimi planı** · `secrets-management-plan`

- Ne zaman: Bir gizli bilgi yönetimi planı üretir: secret envanteri ve sınıflandırması, merkezi kasa seçim kriterleri, en az yetkiyle kimlik tabanlı erişim, iş yüklerine ve hatlara enjeksiyon, rotasyon ve iptal, denetim ve acil erişim (break-glass). Bir ekip secret'ları kodda, yapılandırma dosyalarında veya hat değişkenlerinde tutuyorsa, bir sızıntıdan sonra ya da yeni bir platform için secret yönetimi tasarlanırken kullanılır.
- Örnek istek: _"Veritabanı şifrelerimiz ve API anahtarlarımız appsettings dosyalarında ve hat değişkenlerinde duruyor. Düzgün bir secret yönetimine geçiş planı yaz."_
- İlgili: `iac-review`, `pipeline-design`, `authn-authz-design`, `security-requirements`, `kubernetes-manifest-review`
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.tr.md)

**Bulut maliyet incelemesi** · `finops-review`

- Ne zaman: Bulut veya platform harcamasını inceleyerek israfı, doğru boyutlandırma fırsatlarını, taahhüt ve fiyatlandırma modeli seçeneklerini, depolama ve veri transferi tasarruflarını ve etiketleme/dağıtım boşluklarını bulur; efor ve riskle önceliklendirilmiş bir tasarruf listesi verir. Bir maliyet raporu, fatura dökümü veya kaynak envanteri paylaşıldığında, maliyetler beklenmedik şekilde arttığında ya da periyodik maliyet incelemesi zamanı geldiğinde kullanılır.
- Örnek istek: _"Son üç ayın servis ve kaynak grubu bazında bulut maliyetleri ekte. Nerede para israf ediyoruz ve önce ne yapmalıyız?"_
- İlgili: `cloud-cost-estimate`, `capacity-planning`, `iac-review`, `environment-strategy`, `budget-proposal`
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.tr.md)

### Sürüm Yöneticisi

#### Sürüm Yönetimi

**Sürüm planı yazma** · `release-plan`

- Ne zaman: Sürüm içeriğini, dondurma ve geçiş noktalarını içeren takvimi, isimli sorumluları, bağımlılıkları, iletişimi ve geri dönüş karar noktasını netleştiren bir sürüm planı yazar. Bir sürüm birden fazla ekip, bileşen veya ortamı kapsadığında, değişiklik penceresi gerektirdiğinde ya da sürüm takvimi, geçiş planı veya sürüm akışı istendiğinde kullanılır.
- Örnek istek: _"4.2 sürümü için sürüm planı yaz: üç servis, bir veritabanı migration'ı ve bir mobil uygulama güncellemesi var, hedef üretim tarihi önümüzdeki perşembe gecesi."_
- İlgili: `deployment-checklist`, `rollback-plan`, `go-no-go`, `release-notes`, `change-request-rfc`
- Dosya: [skills/07-devops-sre/release-manager/release/release-plan/SKILL.tr.md](skills/07-devops-sre/release-manager/release/release-plan/SKILL.tr.md)

**Sürüm notları yazma** · `release-notes`

- Ne zaman: Bir değişiklik listesinden, commit'lerden veya iş kalemlerinden; yeni özellikler, iyileştirmeler, düzeltmeler, kırıcı değişiklikler, kullanımdan kaldırmalar ve bilinen sorunlar olarak gruplanmış ve belirli bir hedef kitle (son kullanıcılar, yöneticiler, API tüketicileri veya iç ekipler) için yazılmış sürüm notları hazırlar. Bir sürüm yayına çıkmak üzereyken kullanıcıların, müşterilerin veya desteğin neyin değiştiğini ve ne yapmaları gerektiğini bilmesi gerektiğinde kullanılır.
- Örnek istek: _"Birleştirilmiş şu 23 kaydı 3.8 sürümü için müşterilerimizin sistem yöneticilerine yönelik sürüm notlarına dönüştür."_
- İlgili: `changelog-entry`, `semantic-versioning`, `release-announcement`, `app-store-release-notes`, `release-plan`
- Dosya: [skills/07-devops-sre/release-manager/release/release-notes/SKILL.tr.md](skills/07-devops-sre/release-manager/release/release-notes/SKILL.tr.md)

**Dağıtım kontrol listesi** · `deployment-checklist`

- Ne zaman: Sistemin bileşenlerine, veri değişikliklerine ve dağıtım mekanizmasına göre uyarlanmış, her biri sorumlu, beklenen sonuç ve durdurma koşulu içeren dağıtım öncesi, sırası ve sonrası kontrollerden oluşan bir dağıtım kontrol listesi hazırlar. Bir üretim dağıtımı planlandığında, dağıtımlar unutulan adımlar yüzünden başarısız olduğunda ya da geçiş veya dağıtım günü kontrol listesi istendiğinde kullanılır.
- Örnek istek: _"Bu geceki sürüm için dağıtım kontrol listesi hazırla: Kubernetes üzerinde iki API servisi, bir SQL migration'ı ve gateway'de bir yapılandırma değişikliği var."_
- İlgili: `release-plan`, `rollback-plan`, `go-no-go`, `runbook`, `deployment-strategy`
- Dosya: [skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.tr.md](skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.tr.md)

**Geri dönüş planı** · `rollback-plan`

- Ne zaman: Bir sürüm veya değişiklik için ölçülebilir tetikleyiciler, karar sahibi ve son saati, bileşen bazlı adımlar, veri ve şema konuları, ileri düzeltme alternatifleri ve geri dönüş sonrası doğrulama içeren bir geri dönüş planı yazar. Bir üretim değişikliği onaylanmadan önce, değişiklik migration'lar veya geri alınamaz adımlar içerdiğinde ya da bir sürümün nasıl geri alınacağı sorulduğunda kullanılır.
- Örnek istek: _"Sipariş servisini yükselten ve sipariş durum kolonunu metinden enum tablosuna taşıyan sürümümüz için bir geri dönüş planı yaz."_
- İlgili: `deployment-checklist`, `release-plan`, `deployment-strategy`, `schema-migration-plan`, `backup-restore-plan`
- Dosya: [skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.tr.md](skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.tr.md)

**Yayına alma kararı** · `go-no-go`

- Ne zaman: Bir sürüm veya geçiş için yayına alma (go/no-go) kararını hazırlar ve kaydeder: üzerinde anlaşılmış kriterler, kriter başına kanıt, sorumlusu belli açık riskler, koşullu onay koşulları ve onaylayıcıları içeren bir karar kaydı. Bir sürüm, migration veya lansman resmi bir karar gerektirdiğinde, go/no-go toplantı paketi veya kontrol listesi istendiğinde ya da ekibin neden yayına çıktığını veya ertelediğini belgelemesi gerektiğinde kullanılır.
- Örnek istek: _"Yarınki CRM migration geçişi için go/no-go hazırla. Test sonuçları, açık hatalar ve prova notları ekte."_
- İlgili: `release-quality-gate`, `release-plan`, `rollback-plan`, `decision-log`, `test-summary-report`
- Dosya: [skills/07-devops-sre/release-manager/release/go-no-go/SKILL.tr.md](skills/07-devops-sre/release-manager/release/go-no-go/SKILL.tr.md)

**Sürüm numarası belirleme** · `semantic-versioning`

- Ne zaman: Semantic Versioning 2.0.0 kurallarını bir değişiklik listesine uygulayarak sonraki sürüm numarasını belirler: her değişikliği public API'ye göre sınıflandırır, gizli kırıcı değişiklikleri yakalar, 0.x, pre-release ve build metadata durumlarını ele alır. Bir kütüphane, API, SDK, paket veya servis yayına çıkmak üzereyken hangi sürüm olması gerektiği ya da bir değişikliğin major artış gerektirip gerektirmediği sorulduğunda kullanılır.
- Örnek istek: _"Mevcut sürüm 2.4.1. Değişiklikler: isteğe bağlı 'locale' parametresi eklendi, INVALID_TOKEN hata kodu TOKEN_INVALID olarak değiştirildi, yuvarlama hatası düzeltildi. Sonraki sürüm ne olmalı?"_
- İlgili: `release-notes`, `changelog-entry`, `api-deprecation-plan`, `api-design-review`, `release-plan`
- Dosya: [skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.tr.md](skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.tr.md)

### Site Güvenilirlik Mühendisi

#### Güvenilirlik

**SLI ve SLO tanımlama** · `slo-definition`

- Ne zaman: Bir servis için kullanıcı odaklı SLI ve SLO'lar tanımlar: kritik kullanıcı yolculuklarını belirler, gösterge türlerini (erişilebilirlik, gecikme, tazelik, doğruluk, verim) seçer, iyi/geçerli olay tanımlarını ve ölçüm noktalarını netleştirir, hedefleri ve uyum pencerelerini ortaya çıkan hata bütçesiyle belirler. Bir servisin güvenilirlik hedeflerine ihtiyacı olduğunda, alarmlar gürültülü veya kullanıcı acısıyla ilgisiz olduğunda ya da bir SLO'nun ne olması gerektiği sorulduğunda kullanılır.
- Örnek istek: _"Checkout API'miz için SLI ve SLO tanımla. Load balancer logları ve Prometheus metriklerimiz var; iş birimi checkout'un 'her zaman çalışması' gerektiğini söylüyor."_
- İlgili: `error-budget-policy`, `alert-design`, `observability-plan`, `nfr-specification`, `kpi-definition`
- Dosya: [skills/07-devops-sre/sre/reliability/slo-definition/SKILL.tr.md](skills/07-devops-sre/sre/reliability/slo-definition/SKILL.tr.md)

**Hata bütçesi politikası** · `error-budget-policy`

- Ne zaman: Tanımlı bütçe tüketim eşiklerinde geliştirme ve operasyon ekiplerinin ne yapması gerektiğini (sürüm kısıtları, güvenilirlik çalışması, olay sonrası analiz gereksinimleri), istisnalara kimin karar verdiğini ve anlaşmazlıkların nasıl eskale edildiğini belirten bir hata bütçesi politikası yazar. SLO'lar var ama hiçbir sonucu yoksa, özellik baskısı sürekli güvenilirliği ezip geçiyorsa ya da hata bütçesi bittiğinde ne olacağı sorulduğunda kullanılır.
- Örnek istek: _"Checkout SLO'muz 28 günde %99,9 ve bütçenin %80'ini ilk haftada harcadık. Ürün ve mühendislik liderlerinin imzalayabileceği bir hata bütçesi politikası yaz."_
- İlgili: `slo-definition`, `alert-design`, `postmortem`, `release-quality-gate`, `go-no-go`
- Dosya: [skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.tr.md](skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.tr.md)

**Alarm tasarımı** · `alert-design`

- Ne zaman: Bir servis için sayfalama (page) ve kayıt (ticket) alarm setini tasarlar: SLO'lara bağlı belirti bazlı alarmlar, çok pencereli ve çok burn-rate'li koşullar, önem derecesi ve yönlendirme, runbook bağlantıları ve mevcut gürültülü alarmların denetimi. Alarm yoksa, gürültülüyse, kullanıcı etkisi yerine nedene (CPU, disk) dayalıysa, nöbetçiler tükeniyorsa veya yeni SLO'lar için alarm gerekiyorsa kullanılır.
- Örnek istek: _"Ödeme API'miz için alarm tasarla. SLO 28 günde %99,9 erişilebilirlik; şu an CPU > %80 olunca page atıyoruz ve haftada 40 page geliyor."_
- İlgili: `slo-definition`, `error-budget-policy`, `observability-plan`, `runbook`, `incident-response`
- Dosya: [skills/07-devops-sre/sre/reliability/alert-design/SKILL.tr.md](skills/07-devops-sre/sre/reliability/alert-design/SKILL.tr.md)

**Gözlemlenebilirlik planı** · `observability-plan`

- Ne zaman: Bir veya birden çok servis için gözlemlenebilirliği planlar: hangi metriklerin, yapılandırılmış logların ve dağıtık izlerin üretileceği, korelasyon ve bağlam aktarımı, kardinalite ve saklama bütçeleri, hedef kitleye göre panolar ve SLO'lar ile runbook'lara karşı eksikler. Servis geliştirilirken veya canlıya alınırken, olayların teşhisi uzun sürdüğünde, telemetri maliyeti kontrolden çıktığında ya da neyin enstrümante edileceği sorulduğunda kullanılır.
- Örnek istek: _"Sipariş servisimiz için gözlemlenebilirlik planla: .NET API, Kafka consumer, PostgreSQL. Bugün yalnızca konteyner CPU/bellek grafikleri ve yapılandırılmamış loglarımız var."_
- İlgili: `slo-definition`, `alert-design`, `logging-instrumentation`, `dashboard-spec`, `runbook`
- Dosya: [skills/07-devops-sre/sre/reliability/observability-plan/SKILL.tr.md](skills/07-devops-sre/sre/reliability/observability-plan/SKILL.tr.md)

**Kapasite planlama** · `capacity-planning`

- Ne zaman: Bir servis veya platform için kapasite planı çıkarır: organik büyüme ve bilinen olaylardan talep öngörüsü, yük testlerinden veya canlı veriden kaynak bazında doygunluk sınırları, pay (headroom) ve N+1 yedeklilikle gereken kapasite, tedarik süreleri, ölçekleme tetikleyicileri ve maliyet etkisi. Bir lansman, kampanya veya sezonsal zirve yaklaşırken, kullanım sınırlara doğru ilerlerken ya da sonraki dönemin altyapı bütçesi planlanırken kullanılır.
- Örnek istek: _"Black Friday için checkout kapasitesini planla. Normal zirve 800 istek/sn, pazarlama 4 kat trafik bekliyor; 12 pod ve tek bir birincil veritabanıyla çalışıyoruz."_
- İlgili: `capacity-test-report`, `load-test-analysis`, `scalability-review`, `finops-review`, `observability-plan`
- Dosya: [skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.tr.md](skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.tr.md)

**Kaos deneyi tasarlama** · `chaos-experiment`

- Ne zaman: Kontrollü bir kaos deneyi tasarlar: kararlı durum tanımı, yanlışlanabilir hipotez, enjekte edilecek hata, etki alanı ve kademeli kapsam, durdurma koşulları ve geri alma, gözlem planı, ön koşullar ve bulgu kaydı. Bir ekip dayanıklılık iddialarını (failover, retry, timeout, autoscaling) doğrulamak, bir game day hazırlamak ya da bir felaket kurtarma veya kademeli bozulma tasarımına güvenmeden önce onu sınamak istediğinde kullanılır.
- Örnek istek: _"Sipariş servisimizin üç Redis replikasından birini kaybettiğinde müşteriye görünür hata olmadan ayakta kaldığını kontrol eden bir kaos deneyi tasarla."_
- İlgili: `resilience-review`, `dr-plan`, `slo-definition`, `runbook`, `observability-plan`
- Dosya: [skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.tr.md](skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.tr.md)

**Felaket kurtarma planı** · `dr-plan`

- Ne zaman: Bir sistem için felaket kurtarma planı yazar: servis katmanına göre iş gereksinimine dayalı RTO/RPO, felaket senaryoları, kurtarma stratejisi ve bağımlılık sırası, adım adım failover ve failback prosedürleri, roller ve felaket ilan yetkisi, iletişim ve kanıtlı bir test takvimi. Sistemde DR planı yoksa, RTO/RPO hedefleri belirlenmeli veya doğrulanmalıysa, bir denetim öncesinde ya da bir DR testi veya olay eksikleri ortaya çıkardıktan sonra kullanılır.
- Örnek istek: _"Çekirdek bankacılık API'miz ve PostgreSQL veritabanı için DR planı yaz. İş birimi RTO 1 saat ve RPO 5 dakika istiyor; tek bölgede çalışıyoruz ve gecelik yedek alıyoruz."_
- İlgili: `backup-restore-plan`, `runbook`, `chaos-experiment`, `incident-communication`, `resilience-review`
- Dosya: [skills/07-devops-sre/sre/reliability/dr-plan/SKILL.tr.md](skills/07-devops-sre/sre/reliability/dr-plan/SKILL.tr.md)

#### Olay Yönetimi

**Runbook yazma** · `runbook`

- Ne zaman: Tek bir alarm veya hata modu için operasyonel runbook yazar: belirtiler ve etki, hızlı ön değerlendirme, net kontroller ve beklenen sonuçlarla teşhis dalları, doğrulama ve geri almayla güvenli çözüm adımları, eskalasyon ve takip. Bir page alarmının runbook'u yoksa, nöbetçiler yazılı olmayan bilgiye dayanıyorsa, bir olay eksik bir prosedürü gösterdiyse ya da tekrarlayan bir operasyonel sorunun nasıl ele alınacağı sorulduğunda kullanılır.
- Örnek istek: _"OrderQueueLagHigh alarmı için runbook yaz: order-events topic'inde Kafka consumer lag'i 10 dakika boyunca 10 bin'in üzerinde."_
- İlgili: `alert-design`, `incident-response`, `known-error-article`, `postmortem`, `observability-plan`
- Dosya: [skills/07-devops-sre/sre/incident/runbook/SKILL.tr.md](skills/07-devops-sre/sre/incident/runbook/SKILL.tr.md)

**Olay müdahalesi yürütme** · `incident-response`

- Ne zaman: Canlı bir olayı ilandan çözüme kadar yönetir: önem derecesi değerlendirmesi, rol ataması (olay komutanı, operasyon, iletişim, kayıt tutucu), hipotezler ve paralel iş kollarıyla önce hafifletmeye odaklı plan, zaman damgalı zaman çizelgesi, güncelleme sıklığı ve çıkış kriterleri. Bir kesinti veya performans düşüşü yaşanırken ya da şüphelenilirken, canlı ortam etkisi için şu an ne yapılması gerektiği sorulduğunda veya devam eden bir olay kanalını düzene sokmak için kullanılır.
- Örnek istek: _"Bir olayımız var: 14:05 deploy'undan on dakika sonra checkout hata oranı %15'e çıktı. Yönetmeme yardım et."_
- İlgili: `runbook`, `incident-communication`, `postmortem`, `log-analysis`, `security-incident-response`
- Dosya: [skills/07-devops-sre/sre/incident/incident-response/SKILL.tr.md](skills/07-devops-sre/sre/incident/incident-response/SKILL.tr.md)

**Olay iletişimi yazma** · `incident-communication`

- Ne zaman: Her aşama (araştırılıyor, tespit edildi, izleniyor, çözüldü) ve hedef kitle için olay iletişimini yazar: iç paydaş güncellemeleri, yönetici özetleri ve herkese açık durum sayfası paylaşımları; teyitli etki, müşteri aksiyonları, sonraki güncelleme zamanı içerir ve neden hakkında spekülasyon yapmaz. Bir olay sırasında veya hemen sonrasında bir güncelleme, durum sayfası girdisi, müşteri bildirimi ya da yönetim brifingi yazılması veya gözden geçirilmesi gerektiğinde kullanılır.
- Örnek istek: _"İlk durum sayfası güncellemesini ve iç Slack güncellemesini yaz: 09:40'tan beri AB müşterilerinin yaklaşık %20'sinde ödemeler başarısız, neden bilinmiyor, ekip inceliyor."_
- İlgili: `incident-response`, `customer-outage-notice`, `postmortem`, `bad-news-delivery`, `status-update`
- Dosya: [skills/07-devops-sre/sre/incident/incident-communication/SKILL.tr.md](skills/07-devops-sre/sre/incident/incident-communication/SKILL.tr.md)

**Suçlamasız olay sonrası analiz** · `postmortem`

- Ne zaman: Olay notlarından, sohbet loglarından, alarmlardan ve zaman çizelgelerinden suçlamasız bir olay sonrası analiz (postmortem) yazar: özet, müşteri ve iş etkisi, zaman damgalı zaman çizelgesi, tespit ve müdahale analizi, tetikleyicinin ötesine izlenen katkıda bulunan etkenler ve kök nedenler, iyi gidenler ve sorumlu ile tarihleri belli önceliklendirilmiş düzeltici aksiyonlar. Bir olay çözüldükten sonra, bir SLO ihlali veya kıl payı atlatılan bir durum resmi incelemeyi gerektirdiğinde ya da taslak bir postmortem'in suçlamasız ve uygulanabilir hale getirilmesi gerektiğinde kullanılır.
- Örnek istek: _"Dün geceki ödeme kesintisinin sohbet logu ve alarm geçmişi ekte. Zaman çizelgesi, kök nedenler ve aksiyon maddeleriyle suçlamasız bir postmortem yaz."_
- İlgili: `incident-response`, `incident-communication`, `runbook`, `error-budget-policy`, `alert-design`
- Dosya: [skills/07-devops-sre/sre/incident/postmortem/SKILL.tr.md](skills/07-devops-sre/sre/incident/postmortem/SKILL.tr.md)

**Nöbet devri** · `on-call-handover`

- Ne zaman: Çıkan nöbetin notlarından, alarmlarından, olaylarından ve değişiklik takviminden gelen nöbetçi için bir nöbet devri yazar: açık olaylar ve durumları, yakın geçmişteki ve yaklaşan değişiklikler, bilinen riskler ve bozulmuş bileşenler, gürültülü veya susturulmuş alarmlar, sorumlusu belli bekleyen takipler ve eşikleri ile ilk aksiyonları açıkça tanımlanmış izlenecekler. Bir nöbet vardiyası veya rotasyonu sona erdiğinde, tatil ya da değişiklik dondurma döneminden önce veya bir üretim sisteminin sorumluluğu kişiler ya da ekipler arasında devredildiğinde kullanılır.
- Örnek istek: _"Nöbet haftam yarın bitiyor. Notlarım, alarm özeti ve değişiklik takvimi ekte. Sonraki nöbetçi için devir notunu yaz."_
- İlgili: `incident-response`, `runbook`, `postmortem`, `alert-design`, `incident-communication`
- Dosya: [skills/07-devops-sre/sre/incident/on-call-handover/SKILL.tr.md](skills/07-devops-sre/sre/incident/on-call-handover/SKILL.tr.md)

## Veri ve Yapay Zeka

### Veri Mimarı

#### Veri Modelleme

**Kavramsal veri modeli** · `conceptual-data-model`

- Ne zaman: Temel iş varlıklarını, tanımlarını ve aralarındaki ilişkileri teknolojiden bağımsız olarak iş dilinde ifade eden kavramsal veri modelini oluşturur. Yeni bir alan, platform veya entegrasyon başlarken, paydaşlar arasında ortak terminoloji kurulurken ya da varlık haritası, konu alanı modeli veya iş nesnesi modeli istendiğinde kullanılır.
- Örnek istek: _"Bu çalıştay notlarından B2B siparişten tahsilata alanımız için kavramsal veri modeli çıkar."_
- İlgili: `logical-data-model`, `glossary-builder`, `bounded-context-map`, `event-storming`, `data-requirements`
- Dosya: [skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.tr.md](skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.tr.md)

**Mantıksal veri modeli** · `logical-data-model`

- Ne zaman: Kavramsal modeli veya gereksinimleri; varlıklar, nitelikler, değer alanları, birincil/alternatif/yabancı anahtarlar, kısıtlar ve tarihçe yönetimi içeren, veritabanı ürününden bağımsız normalize bir mantıksal veri modeline dönüştürür. Fiziksel şema tasarımına hazırlanırken, gereksinimleri veriyle doğrularken ya da ERD, 3NF model veya nitelik düzeyinde model istendiğinde kullanılır.
- Örnek istek: _"Hasar alanı için bu kavramsal modelden ve ekteki alan listesinden 3NF mantıksal veri modeli çıkar."_
- İlgili: `conceptual-data-model`, `database-schema-design`, `data-requirements`, `business-rules-catalog`, `data-classification`
- Dosya: [skills/08-data/data-architect/modeling/logical-data-model/SKILL.tr.md](skills/08-data/data-architect/modeling/logical-data-model/SKILL.tr.md)

**Boyutsal model tasarlama** · `dimensional-model`

- Ne zaman: İş süreçlerinden boyutsal (yıldız/kar tanesi) model tasarlar: tanecik (grain), olgu tabloları ve ölçü toplanabilirliği, ortak (conformed) boyutlar, nitelik bazında SCD tipi ve geç gelen ile bilinmeyen üyelerin yönetimi. Veri ambarı veya lakehouse gold/mart katmanı, BI için semantik model kurulurken ya da yıldız şema, bus matrix veya olgu/boyut tasarımı istendiğinde kullanılır.
- Örnek istek: _"Perakende satış ve iade analizi için yıldız şema tasarla; kullanıcılar günlük mağaza/ürün KPI'larına ve müşteri segmenti tarihçesine ihtiyaç duyuyor."_
- İlgili: `metric-definition`, `dashboard-spec`, `report-requirements`, `data-vault-model`, `source-to-target-mapping`
- Dosya: [skills/08-data/data-architect/modeling/dimensional-model/SKILL.tr.md](skills/08-data/data-architect/modeling/dimensional-model/SKILL.tr.md)

**Data Vault modeli tasarlama** · `data-vault-model`

- Ne zaman: Data Vault 2.0 modeli tasarlar: iş anahtarlarından hub'lar, ilişki ve işlemler için link'ler, kaynağa ve değişim hızına göre bölünmüş satellite'lar; hash key, load date, record source ve business vault yapıları (PIT, bridge, effectivity). Çok sayıda değişken kaynak üzerinde denetlenebilir, kaynakları entegre eden ham katman kurulurken ya da hub, link ve satellite istendiğinde kullanılır.
- Örnek istek: _"CRM, çekirdek bankacılık ve web müşteri edinim uygulamasından gelen müşteri ve sözleşme verisi için Data Vault tasarla."_
- İlgili: `dimensional-model`, `logical-data-model`, `master-data-strategy`, `incremental-load-design`, `data-lineage-doc`
- Dosya: [skills/08-data/data-architect/modeling/data-vault-model/SKILL.tr.md](skills/08-data/data-architect/modeling/data-vault-model/SKILL.tr.md)

**Veri platformu tasarlama** · `data-platform-architecture`

- Ne zaman: Tedarikçiden bağımsız bir veri platformu mimarisi tasarlar: alım (ingestion), depolama ve işleme katmanları, sunum örüntüleri, yönetişim, güvenlik, işletim modeli ve warehouse, lakehouse, mesh ya da hibrit arasındaki seçim; kararlar gereksinimlere izlenir. Hedef veri platformu tanımlanırken, eski bir veri ambarı modernize edilirken ya da lakehouse, data mesh veya referans veri mimarisi istendiğinde kullanılır.
- Örnek istek: _"SAP, MES ve IoT kaynakları, BI ve ML tüketicileri ve küçük bir merkezi veri ekibi olan bir üretici için hedef veri platformu tasarla."_
- İlgili: `target-state-architecture`, `technology-selection`, `adr`, `data-contract`, `cloud-cost-estimate`
- Dosya: [skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.tr.md](skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.tr.md)

**Veri sözleşmesi yazma** · `data-contract`

- Ne zaman: Veri üreticisi ile tüketicileri arasında veri sözleşmesi yazar: şema, anlam, kalite beklentileri, tazelik ve erişilebilirlik SLA'ları, sahiplik, erişim ve gizlilik koşulları, sürümleme ve değişiklik/kullanımdan kaldırma kuralları; makinece okunmaya uygun bir biçimde. Bir veri seti, olay akışı veya veri ürünü yayımlanırken, yeni bir tüketici alınırken ya da üretici-tüketici beklentileri resmileştirilmek istendiğinde kullanılır.
- Örnek istek: _"Finans ve öneri ekibinin tükettiği sipariş olay akışı için veri sözleşmesi yaz."_
- İlgili: `schema-evolution-plan`, `data-quality-rules`, `api-contract`, `data-catalog-entry`, `data-classification`
- Dosya: [skills/08-data/data-architect/modeling/data-contract/SKILL.tr.md](skills/08-data/data-architect/modeling/data-contract/SKILL.tr.md)

#### Veri Yönetişimi

**Veri kataloğu kaydı** · `data-catalog-entry`

- Ne zaman: Bir veri seti, tablo, rapor veya veri ürünü için veri kataloğu kaydı yazar: iş açıklaması, sahip ve veri sorumlusu (steward), tanecik, anahtar alanlar, köken özeti, kalite durumu, tazelik, hassasiyet ve erişim, kullanım rehberi. Bir veri seti keşif için kaydedilirken veya belgelenirken, self-servise hazırlanırken ya da bir tablo veya veri ürünü katalog için tarif edilmek istendiğinde kullanılır.
- Örnek istek: _"Bu DDL'i ve finans ekibinin notlarını kullanarak sales.fact_invoice_line tablosu için katalog kaydı yaz."_
- İlgili: `data-lineage-doc`, `data-classification`, `data-quality-rules`, `data-contract`, `glossary-builder`
- Dosya: [skills/08-data/data-architect/governance/data-catalog-entry/SKILL.tr.md](skills/08-data/data-architect/governance/data-catalog-entry/SKILL.tr.md)

**Veri hassasiyet sınıflandırması** · `data-classification`

- Ne zaman: Veri setlerini ve alanları hassasiyet ve gizlilik kategorisine göre sınıflandırır: gizlilik düzeyi, kişisel veri, KVKK Madde 6 ve GDPR Madde 9-10 kapsamında özel nitelikli veri, doğrudan ve dolaylı tanımlayıcılar; buradan maskeleme, şifreleme, erişim ve saklama gibi işleme kontrollerini türetir. Veri bir platforma alınırken, DPIA veya erişim modeli hazırlanırken ya da kişisel veya hassas sütunlar etiketlenmek istendiğinde kullanılır.
- Örnek istek: _"Müşteri ve kredi başvuru tablolarımızın sütunlarını KVKK'ya göre sınıflandır ve maskeleme kuralları öner."_
- İlgili: `privacy-impact-assessment`, `retention-policy`, `data-catalog-entry`, `access-review`, `secrets-management-plan`
- Dosya: [skills/08-data/data-architect/governance/data-classification/SKILL.tr.md](skills/08-data/data-architect/governance/data-classification/SKILL.tr.md)

**Veri kalitesi kuralları** · `data-quality-rules`

- Ne zaman: Bir veri seti veya veri ürünü için bütünlük, geçerlilik, teklik, tutarlılık, referans bütünlüğü, güncellik ve hacim boyutlarında test edilebilir veri kalitesi kuralları tanımlar; her kural için eşik, önem derecesi, hata durumunda aksiyon ve sorumlu belirler. Bir veri setine kalite kontrolü gerektiğinde, veri sözleşmesinin kalite bölümü yazılırken, tekrarlayan veri sorunları önlenmek istendiğinde veya bir tabloya ya da veri hattına hangi kontrollerin konacağı sorulduğunda kullanılır.
- Örnek istek: _"Aylık gelir raporunu besleyen müşteri ve sipariş tabloları için veri kalitesi kurallarını tanımla."_
- İlgili: `data-contract`, `data-catalog-entry`, `pipeline-spec`, `business-rules-catalog`, `pipeline-failure-analysis`
- Dosya: [skills/08-data/data-architect/governance/data-quality-rules/SKILL.tr.md](skills/08-data/data-architect/governance/data-quality-rules/SKILL.tr.md)

**Veri kökeni dokümantasyonu** · `data-lineage-doc`

- Ne zaman: Veri kökenini kaynak sistemlerden alım, dönüşüm ve depolama katmanları üzerinden raporlara, modellere ve diğer tüketicilere kadar, veri seti ve kritik sütun düzeyinde, dönüşüm mantığı, sahipler ve doğrulama durumuyla belgeler. Bir rakamın nereden geldiği sorulduğunda, değişiklik öncesi etki analizi için, denetim veya yasal izlenebilirlik gerektiğinde ya da ekibe tanımadığı bir veri akışı anlatılırken kullanılır.
- Örnek istek: _"Finans panosundaki 'net gelir' rakamının kaynak sistemlere kadar veri kökenini belgele."_
- İlgili: `data-catalog-entry`, `source-to-target-mapping`, `impact-analysis`, `data-quality-rules`, `diagram-as-code`
- Dosya: [skills/08-data/data-architect/governance/data-lineage-doc/SKILL.tr.md](skills/08-data/data-architect/governance/data-lineage-doc/SKILL.tr.md)

**Ana veri yönetimi tanımlama** · `master-data-strategy`

- Ne zaman: Bir veya daha fazla alan (müşteri, ürün, tedarikçi, lokasyon vb.) için ana veri yönetimi yaklaşımını tanımlar: nitelik bazında kayıt sistemi, altın kayıt ve hayatta kalma kuralları, eşleştirme/birleştirme mantığı, uygulama stili, veri sorumluluğu rolleri ve iş akışları, tüketen sistemlere dağıtım. Aynı varlık sistemler arasında tutarsız bulunduğunda, mükerrer kayıtlar operasyona veya raporlamaya zarar verdiğinde ya da bir ana veri veya altın kayıt girişimi kapsamlandırılırken kullanılır.
- Örnek istek: _"CRM, ERP ve e-ticaret platformunda bulunan müşteri verisi için bir ana veri yaklaşımı tanımla."_
- İlgili: `data-quality-rules`, `logical-data-model`, `data-lineage-doc`, `raci-matrix`, `data-classification`
- Dosya: [skills/08-data/data-architect/governance/master-data-strategy/SKILL.tr.md](skills/08-data/data-architect/governance/master-data-strategy/SKILL.tr.md)

**Veri saklama politikası** · `retention-policy`

- Ne zaman: Veri setleri veya sistemler için veri saklama politikası tanımlar: yasal veya iş gerekçesiyle saklama süreleri, süreyi başlatan olaylar, arşiv katmanları, silme veya anonimleştirme yöntemleri, hukuki muhafaza (legal hold), yedeklerin ele alınışı ve imha kanıtı. Veri varsayılan olarak süresiz tutuluyorsa, KVKK veya GDPR gibi bir gizlilik mevzuatı saklama sınırlaması istiyorsa, depolama maliyetleri artıyorsa ya da verinin ne kadar süre tutulabileceği veya tutulması gerektiği sorulduğunda kullanılır.
- Örnek istek: _"KVKK ve GDPR kapsamında müşteri, sipariş ve uygulama log verilerimiz için saklama politikası tanımla."_
- İlgili: `data-classification`, `privacy-impact-assessment`, `backup-restore-plan`, `policy-writing`, `data-catalog-entry`
- Dosya: [skills/08-data/data-architect/governance/retention-policy/SKILL.tr.md](skills/08-data/data-architect/governance/retention-policy/SKILL.tr.md)

### Veri Mühendisi

#### Veri Hatları

**Veri hattı tanımlama** · `pipeline-spec`

- Ne zaman: Toplu (batch) veya akış (streaming) bir veri hattını uçtan uca tanımlar: kaynaklar ve çekme, zamanlama veya tetikleyici, bağımlılıklar, dönüşüm adımları, hedefler ve yazma modu, yükleme stratejisi, veri kalitesi kapıları, SLA'lar, hata yönetimi, geriye dönük yükleme, gözlemlenebilirlik, güvenlik ve sahiplik. Bir veri hattı kurulmadan veya değiştirilmeden önce, iş bir mühendise devredilirken ya da bir ETL/ELT veya streaming işinin tasarlanması veya belgelenmesi istendiğinde kullanılır.
- Örnek istek: _"ERP veritabanından günlük siparişleri finans martı için veri ambarına yükleyen veri hattının tanımını yaz."_
- İlgili: `source-to-target-mapping`, `incremental-load-design`, `data-quality-rules`, `data-contract`, `runbook`
- Dosya: [skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.tr.md](skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.tr.md)

**Kaynak-hedef eşleme dokümanı** · `source-to-target-mapping`

- Ne zaman: Bir veri yüklemesi için sütun düzeyinde kaynak-hedef eşleme (STTM) dokümanı yazar: tip ve boş olabilirlikle hedef sütunlar, kaynak sütunlar, dönüşüm ve iş kuralları, lookup'lar, varsayılanlar, anahtar üretimi, filtreler, join koşulları, reddedilen kayıtların ele alınışı ve test senaryoları. Bir veri hattı, veri göçü veya entegrasyon yüklemesi kurulacak ya da gözden geçirilecekse, türetilmiş alanların iş kuralları netleştirilecekse veya iki şema arasında eşleme tablosu istendiğinde kullanılır.
- Örnek istek: _"CRM müşteri ve adres tablolarından dim_customer tablomuza kaynak-hedef eşleme dokümanı oluştur."_
- İlgili: `pipeline-spec`, `field-mapping`, `data-lineage-doc`, `dimensional-model`, `test-data-design`
- Dosya: [skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.tr.md](skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.tr.md)

**Artımlı yükleme tasarımı** · `incremental-load-design`

- Ne zaman: Bir tablo veya akış için artımlı yükleme tasarlar: değişiklik tespit yöntemi (log tabanlı CDC, zaman damgası veya sıra numarası watermark'ı, snapshot karşılaştırma), watermark yönetimi, idempotent merge, silmelerin iletimi, geç ve sırasız gelen verinin ele alınışı, mutabakat ve tam yeniden yükleme yedeği. Tam yüklemeler çok yavaş veya maliyetli hale geldiğinde, bir kaynağın düşük gecikmeyle çoğaltılması gerektiğinde ya da yalnızca değişen verinin güvenle nasıl yükleneceği sorulduğunda kullanılır.
- Örnek istek: _"Tam yüklemesi 6 saat süren 400 milyon satırlık işlem tablosu için artımlı yükleme tasarla."_
- İlgili: `pipeline-spec`, `source-to-target-mapping`, `data-vault-model`, `schema-evolution-plan`, `pipeline-failure-analysis`
- Dosya: [skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.tr.md](skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.tr.md)

**Veri hattı hata analizi** · `pipeline-failure-analysis`

- Ne zaman: Başarısız olan veya sessizce yanlış veri üreten bir veri hattı çalışmasını analiz eder: zaman çizelgesini çıkarır, kök nedeni (kaynak, kod, altyapı, veri, bağımlılık) ayırır, bölümler, tablolar ve tüketiciler üzerindeki veri etkisini ölçer, güvenli ve idempotent bir geriye dönük yükleme ile önleme planı üretir. Bir yükleme hata verdiğinde, mükerrer, eksik veya geç veri ürettiğinde, bir kalite kontrolü tetiklendiğinde ya da bir tüketici rakamların tutmadığını bildirdiğinde kullanılır.
- Örnek istek: _"Dün geceki sipariş yüklemesi başarılı görünüyor ama bugünkü ciro panosu %12 düşük. Çalışma logları ve satır sayıları ekte; ne olduğunu ve veriyi nasıl düzelteceğimizi bul."_
- İlgili: `incremental-load-design`, `pipeline-spec`, `data-lineage-doc`, `data-quality-rules`, `postmortem`
- Dosya: [skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.tr.md](skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.tr.md)

**Şema evrimi planlama** · `schema-evolution-plan`

- Ne zaman: Bir veri hattında, olay akışında veya paylaşılan veri setinde şema değişikliğini planlar: her değişikliği geriye, ileriye, tam uyumlu veya kırıcı olarak sınıflar, evrim desenini (eklemeli, expand-contract, sürümlü veri seti veya topic, çift yazma) seçer ve üretici, veri hattı ve tüketici değişikliklerini backfill, doğrulama ve kullanımdan kaldırmayla sıralar. Bir kaynak alan eklediğinde, yeniden adlandırdığında, tipini değiştirdiğinde veya kaldırdığında, bir veri sözleşmesi değişmesi gerektiğinde ya da tüketiciler üst akıştaki şema kaymasıyla sürekli kırıldığında kullanılır.
- Örnek istek: _"CRM ekibi gelecek ay customer_type alanını segment olarak yeniden adlandırıp serbest metinden enum'a çevirecek. Veri hattımız ve 6 alt akış tüketicisi için şema evrimini planla."_
- İlgili: `data-contract`, `schema-migration-plan`, `incremental-load-design`, `source-to-target-mapping`, `data-lineage-doc`
- Dosya: [skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.tr.md](skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.tr.md)

### Veritabanı Yöneticisi

#### Veritabanı Operasyonları

**Yavaş sorgu iyileştirme** · `query-optimization`

- Ne zaman: Yavaş bir SQL sorgusunu metni, çalışma planı ve istatistikleri üzerinden teşhis eder; baskın maliyeti (hatalı kardinalite tahmini, yanlış join sırası veya yöntemi, taramalar, diske taşmalar, sargable olmayan koşullar, parametre hassasiyeti, bloklanma) bulur ve beklenen etki ile doğrulama yöntemiyle sıralanmış yeniden yazım, indeks veya istatistik önerileri sunar. Bir sorgu, rapor veya endpoint yavaşsa, bir sürüm ya da veri büyümesi sonrası plan kötüleştiyse veya biri çalışma planını paylaşıp neden yavaş olduğunu sorduğunda kullanılır.
- Örnek istek: _"Bu sipariş arama sorgusu geçen haftaki veri aktarımından sonra 200 ms'den 9 saniyeye çıktı. Sorgu ve gerçek çalışma planı ekte; neden yavaş ve nasıl düzeltiriz?"_
- İlgili: `index-recommendation`, `database-health-check`, `sql-query-writing`, `performance-optimization`, `schema-migration-plan`
- Dosya: [skills/08-data/dba/database/query-optimization/SKILL.tr.md](skills/08-data/dba/database/query-optimization/SKILL.tr.md)

**İndeks önerisi** · `index-recommendation`

- Ne zaman: Bir tablo veya veritabanı için gerçek iş yükünden indeks önerir: sorguları erişim desenine göre gruplar, anahtar sütun sırasını, dahil edilen sütunları, filtreli/kısmi indeksleri tasarlar, örtüşen indeksleri birleştirir ve kullanılmayanları kaldırır; okuma kazancını yazma yükü, depolama ve bakım maliyetine karşı tartar. Yeni bir şema veya özellik için indeks tasarlanırken, fazla ya da eksik indeksli bir tablo gözden geçirilirken veya motorun eksik indeks önerileri değerlendirilirken kullanılır.
- Örnek istek: _"orders tablomuzda 14 indeks var, insert'ler yavaşlıyor ve bazı raporlar hâlâ tarama yapıyor. En pahalı 20 sorgu ve indeks kullanım istatistikleri ekte; bir indeks seti öner."_
- İlgili: `query-optimization`, `database-health-check`, `schema-migration-plan`, `database-schema-design`, `capacity-planning`
- Dosya: [skills/08-data/dba/database/index-recommendation/SKILL.tr.md](skills/08-data/dba/database/index-recommendation/SKILL.tr.md)

**Şema geçiş planı** · `schema-migration-plan`

- Ne zaman: Canlı bir sistemde sıfır veya asgari kesintiyle veritabanı şema geçişi planlar: her DDL'in kilit ve yeniden yazma davranışını değerlendirir, kırıcı değişiklikleri uygulama sürümleriyle hizalı expand-migrate-contract adımlarına böler, parçalı backfill tasarlar ve doğrulama, geri dönüş ile geri dönüşü olmayan noktayı tanımlar. Üretim veritabanlarında sütun, tablo, kısıt veya indeks eklenirken, yeniden adlandırılırken, tipi değiştirilirken veya silinirken ya da bir geçiş betiği yayından önce güvenlik incelemesine ihtiyaç duyduğunda kullanılır.
- Örnek istek: _"90 milyon satırlık bir PostgreSQL tablosunda customers.full_name sütununu kesinti olmadan first_name ve last_name olarak bölmemiz gerekiyor. Geçiş planını yaz."_
- İlgili: `schema-evolution-plan`, `index-recommendation`, `backup-restore-plan`, `deployment-strategy`, `rollback-plan`
- Dosya: [skills/08-data/dba/database/schema-migration-plan/SKILL.tr.md](skills/08-data/dba/database/schema-migration-plan/SKILL.tr.md)

**Yedekleme ve geri yükleme planı** · `backup-restore-plan`

- Ne zaman: RPO ve RTO'dan türetilmiş bir veritabanı yedekleme ve geri yükleme planı tasarlar: yedek tipleri ve sıklığı (tam, fark/artımlı, log veya sürekli arşivleme, snapshot), saklama ve değiştirilemez/tesis dışı kopyalar, şifreleme ve erişim, her arıza senaryosu için geri yükleme prosedürleri ve kanıt üreten periyodik geri yükleme testi programı. Bir veritabanı için yedekleme kurulurken veya gözden geçirilirken, başarısız ya da yavaş bir geri yüklemeden sonra, denetim kanıtı için veya RPO/RTO hedefleri değiştiğinde kullanılır.
- Örnek istek: _"2 TB'lık sipariş veritabanımız için yedekleme ve geri yükleme planı tasarla: RPO 15 dakika, RTO 2 saat; denetim için aylık yedekleri 1 yıl saklamamız da gerekiyor."_
- İlgili: `dr-plan`, `retention-policy`, `database-health-check`, `schema-migration-plan`, `runbook`
- Dosya: [skills/08-data/dba/database/backup-restore-plan/SKILL.tr.md](skills/08-data/dba/database/backup-restore-plan/SKILL.tr.md)

**Veritabanı sağlık kontrolü** · `database-health-check`

- Ne zaman: Kullanıcının sağladığı metrikler, görünümler ve ayarlar üzerinden bir veritabanı instance'ının yapılandırılmış sağlık kontrolünü yapar: bekleme profili, en çok kaynak tüketen sorgular, kilitlenme ve bloklanma, depolama büyümesi ve şişkinlik/parçalanma, indeks ve istatistik sağlığı, yapılandırma, replikasyon, yedekler ve temel güvenlik; ardından bulguları kanıt ve çözümleriyle önceliklendirir. Periyodik veritabanı incelemelerinde, yoğun sezon veya geçiş öncesinde, veritabanı genel olarak yavaş hissettirdiğinde ya da tanınmayan bir veritabanı devralındığında kullanılır.
- Örnek istek: _"Üretimdeki SQL veritabanımızın sağlık kontrolünü yap. En yüksek beklemeleri, CPU'ya göre ilk 10 sorguyu, dosya boyutlarını ve yapılandırma ayarlarını yapıştırdım."_
- İlgili: `query-optimization`, `index-recommendation`, `backup-restore-plan`, `capacity-planning`, `alert-design`
- Dosya: [skills/08-data/dba/database/database-health-check/SKILL.tr.md](skills/08-data/dba/database/database-health-check/SKILL.tr.md)

### Veri / BI Analisti

#### Analitik ve Raporlama

**Analiz planı yazma** · `analysis-plan`

- Ne zaman: Herhangi bir sorgu çalıştırılmadan önce iş sorusunu, hipotezleri, veri kaynaklarını, yöntemi, geçerlilik kontrollerini ve çıktıyı netleştiren bir analiz planı yazar. Bir paydaş \"X neden değişti\", \"Y işe yarıyor mu\" veya \"Z'yi yapmalı mıyız\" diye sorduğunda ve kapsamın, yöntemin ve beklentilerin baştan uzlaşılması gerektiğinde kullanılır.
- Örnek istek: _"Şu soru için analiz planı yaz: pazarlama, yeni onboarding e-posta serisinin 30 günlük elde tutmayı artırıp artırmadığını öğrenmek istiyor."_
- İlgili: `metric-definition`, `data-exploration`, `ab-test-analysis`, `insight-summary`, `hypothesis-statement`
- Dosya: [skills/08-data/data-analyst/analytics/analysis-plan/SKILL.tr.md](skills/08-data/data-analyst/analytics/analysis-plan/SKILL.tr.md)

**Gösterge paneli tanımlama** · `dashboard-spec`

- Ne zaman: Bir gösterge panelini (dashboard) inşa edilmeden önce tanımlar; hedef kitle, desteklenen kararlar, sorular, tanımlarıyla KPI'lar, görseller, filtreler, detaya inme yolları, yenileme ve erişim kuralları. Yeni bir dashboard veya rapor sayfası istendiğinde, karmaşık bir panel yeniden tasarlanacağında ya da BI geliştiricisinin tahmin yürütmeden uygulayabileceği bir tanım gerektiğinde kullanılır.
- Örnek istek: _"Müşteri destek yönetimi için iş kaydı birikimini, SLA uyumunu ve temsilci iş yükünü haftalık izleyecek bir dashboard tanımla."_
- İlgili: `metric-definition`, `kpi-definition`, `report-requirements`, `data-requirements`, `insight-summary`
- Dosya: [skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.tr.md](skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.tr.md)

**İçgörü özeti yazma** · `insight-summary`

- Ne zaman: Analiz sonuçlarını, sorgu çıktılarını veya grafikleri kısa bir \"ne anlama geliyor\" içgörü özetine dönüştürür; ana bulgu, kanıt, güven düzeyi, etkiler ve önerilen aksiyon. Rakamlar hazır olduğunda ama kitlenin ne anlama geldiğini ve ne yapılacağını bilmesi gerektiğinde kullanılır; örneğin bir analizden, aylık gözden geçirmeden veya dashboard'daki bir anomaliden sonra.
- Örnek istek: _"Şu sonuçlardan içgörü özeti yaz: Q3'te müşteri kaybı %3,1'den %4,0'a çıktı, çoğunlukla aylık plandaki KOBİ segmentinde."_
- İlgili: `analysis-plan`, `executive-summary`, `ab-test-analysis`, `dashboard-spec`, `presentation-outline`
- Dosya: [skills/08-data/data-analyst/analytics/insight-summary/SKILL.tr.md](skills/08-data/data-analyst/analytics/insight-summary/SKILL.tr.md)

**Metriği kesin tanımlama** · `metric-definition`

- Ne zaman: Bir iş metriğini, iki analistin aynı sayıyı hesaplayacağı kesinlikte tanımlar; amaç, formül, pay/payda, filtreler, tanecik, zaman mantığı, uç durumlar, kaynak alanlar ve sahip. Bir metrik tartışmalı olduğunda, ekipler arasında farklı raporlandığında, dashboard'a veya OKR'a eklenmek üzereyken ya da metrik kataloğuna yazılması gerektiğinde kullanılır.
- Örnek istek: _"Aktif müşteri\" metriğini kesin olarak tanımla; finans ve ürün her ay farklı sayı raporluyor."_
- İlgili: `kpi-definition`, `dashboard-spec`, `north-star-metric`, `data-quality-rules`, `glossary-builder`
- Dosya: [skills/08-data/data-analyst/analytics/metric-definition/SKILL.tr.md](skills/08-data/data-analyst/analytics/metric-definition/SKILL.tr.md)

**Veri setini keşfetme** · `data-exploration`

- Ne zaman: Tanıdık olmayan bir veri seti için yapılandırılmış bir keşifsel veri analizi yürütür; yapı, tanecik, dağılımlar, boş değerler, mükerrer kayıtlar, aykırı değerler, zaman kapsamı, ilişkiler ve kalite sorunları; bulguları ve kullanıma uygunluğu raporlar. Yeni bir tablo, veri çekimi veya dosya geldiğinde, üzerine model, metrik veya dashboard kurulmadan önce ya da \"bu veride ne var?\" sorulduğunda kullanılır.
- Örnek istek: _"Bu veri setini keşfet: order_id, customer_id, order_ts, amount, currency, status, channel kolonlarını içeren 250 bin e-ticaret siparişlik bir CSV. Profil çıktısı ekte."_
- İlgili: `analysis-plan`, `data-quality-rules`, `metric-definition`, `feature-engineering-plan`, `data-catalog-entry`
- Dosya: [skills/08-data/data-analyst/analytics/data-exploration/SKILL.tr.md](skills/08-data/data-analyst/analytics/data-exploration/SKILL.tr.md)

**A/B testi analizi** · `ab-test-analysis`

- Ne zaman: Bir A/B veya çok değişkenli testi baştan sona analiz eder; geçerlilik kontrolleri (örneklem oranı uyumsuzluğu, maruziyet, süre), güven aralığıyla birincil metrik etkisi, koruyucu metrikler, segmentler ve yayına al / iyileştir / durdur önerisi. Deney sonuçları geldiğinde ve karar gerektiğinde ya da bir test sonucunun anlamlı veya güvenilir olup olmadığı sorulduğunda kullanılır.
- Örnek istek: _"Bu A/B testini analiz et: kontrol 48.210 kullanıcı %2,31 dönüşüm, varyant 48.950 kullanıcı %2,52 dönüşüm, 14 gün sürdü; koruyucu metrik iade oranı."_
- İlgili: `experiment-design`, `hypothesis-statement`, `metric-definition`, `insight-summary`, `analysis-plan`
- Dosya: [skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.tr.md](skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.tr.md)

### Veri Bilimci / ML ve YZ Mühendisi

#### Makine Öğrenmesi

**ML problemini tanımlama** · `ml-problem-framing`

- Ne zaman: Bir iş ihtiyacını makine öğrenmesi problemi olarak tanımlar; desteklenen karar, tahmin hedefi ve etiket, tahminin birimi ve zamanı, tahmin anında mevcut öznitelikler, başarı metrikleri (çevrim dışı ve iş), taban çizgisi, veri fizibilitesi ve devam/dur kararı. Biri \"X'i tahmin etmek için ML/YZ kullanalım\" dediğinde, herhangi bir veri çalışması veya model seçimi başlamadan önce kullanılır.
- Örnek istek: _"Bunu bir ML problemi olarak tanımla: tahsilat ekibi, faturasını zamanında ödemeyecek müşterileri tahmin edip onları daha erken aramak istiyor."_
- İlgili: `ai-use-case-assessment`, `feature-engineering-plan`, `model-evaluation-report`, `analysis-plan`, `problem-statement`
- Dosya: [skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.tr.md)

**Öznitelik mühendisliği planı** · `feature-engineering-plan`

- Ne zaman: Tahmine dayalı bir model için öznitelikleri planlar; hipoteze göre aday öznitelikler, kaynak ve tahmin anındaki erişilebilirlik, zamana göre doğruluk (point-in-time), sızıntı kontrolleri, dönüşümler, kodlama, eksik değer stratejisi ve doğrulama yaklaşımı. ML problemi tanımlandıktan sonra ve model eğitiminden önce ya da bir model şüphe uyandıracak kadar iyi performans gösterdiğinde ve sızıntıdan şüphelenildiğinde kullanılır.
- Örnek istek: _"Bir telekom abonelik tabanı için churn modelinin öznitelik mühendisliğini planla; tahmin her ay sonraki 60 gün için yapılıyor."_
- İlgili: `ml-problem-framing`, `data-exploration`, `model-evaluation-report`, `source-to-target-mapping`, `data-quality-rules`
- Dosya: [skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.tr.md)

**Model değerlendirme raporu** · `model-evaluation-report`

- Ne zaman: Aday bir modeli taban çizgisi ve mevcut modelle karşılaştıran bir model değerlendirme raporu yazar; belirsizlikle genel metrikler, eşik seçimi, kalibrasyon, dilim performansı, hata analizi, adillik ve yayın önerisi. Bir model eğitildiğinde ve canlıya alınmak üzere onaylanması, alternatiflerle karşılaştırılması ya da bir performans şikâyeti sonrası gözden geçirilmesi gerektiğinde kullanılır.
- Örnek istek: _"Dolandırıcılık modelimiz v3'ü v2 ile karşılaştıran bir değerlendirme raporu yaz; test seti metrikleri, karışıklık matrisleri ve kanal ile ülke bazında dilim sonuçları ekte."_
- İlgili: `ml-problem-framing`, `model-card`, `ml-monitoring-plan`, `feature-engineering-plan`, `llm-eval-set`
- Dosya: [skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.tr.md)

**Model kartı yazma** · `model-card`

- Ne zaman: Eğitilmiş bir modelin kullanım amacını, kapsam dışı kullanımlarını, eğitim ve değerlendirme verisini, genel ve grup bazında performansını, sınırlamalarını, etik ve gizlilik değerlendirmelerini ve sahipliğini belgeleyen bir model kartı yazar. Bir model yayına alındığında, ekipler arasında paylaşıldığında, yönetişim veya denetim incelemesine sunulduğunda ya da kullanıcıların modele neyde güvenip neyde güvenemeyeceğini bilmesi gerektiğinde kullanılır.
- Örnek istek: _"İK işe alım uzmanlarının kullandığı CV eleme sıralama modelimiz için model kartı yaz; değerlendirme sonuçları ve eğitim verisi özeti ekte."_
- İlgili: `model-evaluation-report`, `ml-monitoring-plan`, `ml-problem-framing`, `privacy-impact-assessment`, `ai-use-case-assessment`
- Dosya: [skills/08-data/ml-ai-engineer/ml/model-card/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/model-card/SKILL.tr.md)

**Model izleme planı** · `ml-monitoring-plan`

- Ne zaman: Bir makine öğrenmesi modeli için veri ve tahmin kayması, gecikmeli etiketlerle performans düşüşü, veri kalitesi, operasyonel sağlık, alarm eşikleri, sorumlular ve yeniden eğitim tetikleyicilerini kapsayan üretim izleme planı hazırlar. Model canlıya çıkmak üzereyken, sessiz model bozulmasının yol açtığı bir olaydan sonra veya modelin hâlâ çalışıp çalışmadığının nasıl anlaşılacağı sorulduğunda kullanılır.
- Örnek istek: _"Churn modelimiz için izleme planı yaz; tüm müşterileri her gece skorluyor ve gerçek churn'ü ancak 60 gün sonra öğreniyoruz."_
- İlgili: `model-evaluation-report`, `model-card`, `alert-design`, `observability-plan`, `feature-engineering-plan`
- Dosya: [skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.tr.md)

#### Üretken Yapay Zeka

**Prompt tasarlama** · `prompt-design`

- Ne zaman: Bir dil modeli özelliği için rol, görev, bağlam, kısıtlar, örnekler, çıktı formatı ve hata davranışı içeren üretim prompt'u tasarlar veya yeniden yazar; doğrulamak için küçük bir test seti de hazırlar. Yeni bir LLM destekli özellik geliştirilirken, mevcut prompt tutarsız, gereksiz uzun ya da yanlış formatlı yanıtlar verdiğinde veya bir prompt'un iyileştirilmesi, yapılandırılması ya da sağlamlaştırılması istendiğinde kullanılır.
- Örnek istek: _"Gelen destek e-postalarını 8 kategoriye ayıran ve kategori, güven düzeyi ve tek satırlık gerekçe içeren JSON döndüren bir prompt tasarla."_
- İlgili: `llm-eval-set`, `rag-design`, `ai-skill-authoring`, `ai-use-case-assessment`
- Dosya: [skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.tr.md)

**LLM değerlendirme seti** · `llm-eval-set`

- Ne zaman: Bir LLM özelliği için kategorilere ayrılmış test vakaları, puanlama kriterleri (rubric), değerlendirici seçimi (birebir eşleşme, programatik, model ile puanlama, insan), geçme eşikleri ve regresyon süreci içeren bir değerlendirme seti oluşturur. Bir LLM özelliği, prompt veya RAG hattı yayından önce ölçülebilir kalite gerektirdiğinde, modeller ya da prompt sürümleri karşılaştırılırken veya \"yeni prompt daha iyi mi bilmiyoruz\" dendiğinde kullanılır.
- Örnek istek: _"Sözleşme özetleme asistanımız için, yayından önce iki prompt sürümünü karşılaştırabileceğimiz bir değerlendirme seti oluştur."_
- İlgili: `prompt-design`, `rag-design`, `model-evaluation-report`, `test-strategy`, `ai-use-case-assessment`
- Dosya: [skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.tr.md)

**RAG sistemi tasarlama** · `rag-design`

- Ne zaman: Doküman kümesi ve erişim kontrolü, veri alımı, parçalama, embedding, hibrit erişim, yeniden sıralama, kaynak gösteren dayanaklı yanıt üretimi, değerlendirme ve operasyonu kapsayan bir erişimle zenginleştirilmiş üretim (RAG) sistemi tasarlar. Bir LLM'in kurum dokümanlarından veya verisinden yanıt vermesi gerektiğinde, mevcut RAG yanlış ya da kaynaksız yanıtlar verdiğinde veya RAG, fine-tuning ve düz prompt arasında seçim yapılırken kullanılır.
- Örnek istek: _"3.000 İK politika PDF'i ve intranet sayfasından çalışan sorularını yanıtlayan, ülkeye özel erişim kurallarına uyan bir RAG asistanı tasarla."_
- İlgili: `prompt-design`, `llm-eval-set`, `ai-use-case-assessment`, `data-classification`, `solution-architecture-document`
- Dosya: [skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.tr.md)

**Yeni YZ skill'i yazma** · `ai-skill-authoring`

- Ne zaman: Bu kütüphanenin yazım rehberine uyan yeni, taşınabilir ve iki dilli bir skill (İngilizce SKILL.md ve Türkçe SKILL.tr.md) yazar; katalog satırını, üç alanlı frontmatter'ı, sabit dokuz bölümü, yapısal sınırları ve içerik kurallarını kapsar. Kütüphaneye yeni bir skill eklenmek istendiğinde, tekrarlanan bir görev veya kontrol listesi skill'e dönüştürülecekken ya da bir skill taslağı kurallara uygunluk açısından incelenecekken kullanılır.
- Örnek istek: _"Kütüphanemiz için destek mühendisinin müşteriye kesinti bildirimi yazmasına yardım eden yeni bir skill yaz; katalog satırını ve iki dil dosyasını ver."_
- İlgili: `prompt-design`, `llm-eval-set`, `document-review`, `technical-translation`, `style-guide-check`
- Dosya: [skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.tr.md)

**YZ kullanım senaryosu değerlendirmesi** · `ai-use-case-assessment`

- Ne zaman: Önerilen bir yapay zeka veya makine öğrenmesi kullanım senaryosunu iş değeri, teknik fizibilite, veri hazırlığı, risk (gizlilik, adillik, güvenlik, mevzuat) ve işletme maliyeti açısından değerlendirir; en küçük sonraki deneyle birlikte puanlı bir devam / pilot / dur önerisi verir. Birisi \"X için yapay zeka kullanalım\" dediğinde, bir YZ fikirleri portföyü önceliklendirilirken veya bir YZ pilotu finanse edilmeden önce kullanılır.
- Örnek istek: _"Bu fikri değerlendir: çağrı merkezi temsilcilerimiz için gelen tüm müşteri şikâyetlerine ilk yanıt taslağını bir LLM hazırlasın."_
- İlgili: `ml-problem-framing`, `rag-design`, `privacy-impact-assessment`, `cost-benefit-analysis`, `decision-matrix`
- Dosya: [skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.tr.md)

## Güvenlik ve Uyum

### Güvenlik Mimarı / Uygulama Güvenliği Mühendisi

#### Güvenli Tasarım

**Tehdit modeli oluşturma** · `threat-model`

- Ne zaman: Bir sistem veya özellik için tehdit modeli oluşturur: sistemi veri akış diyagramına ayırır, her eleman ve güven sınırı için STRIDE uygular, tehditleri derecelendirir ve sorumlusuyla birlikte önlemler önerir. Yeni bir sistem tasarlanırken, entegrasyon eklenirken, güven sınırları veya veri akışları değişirken ya da güvenlik açısından neyin ters gidebileceği sorulduğunda kullanılır.
- Örnek istek: _"Yeni mobil bankacılık API'miz için tehdit modeli çıkar: mobil uygulama, API gateway, .NET backend, PostgreSQL ve üçüncü taraf bir KYC sağlayıcısı var."_
- İlgili: `security-requirements`, `authn-authz-design`, `solution-architecture-document`, `pentest-scope`, `it-risk-assessment`
- Dosya: [skills/09-security/security-engineer/design/threat-model/SKILL.tr.md](skills/09-security/security-engineer/design/threat-model/SKILL.tr.md)

**Güvenlik gereksinimleri** · `security-requirements`

- Ne zaman: Bir sistem veya özellik için OWASP ASVS seviye ve bölümleriyle uyumlu, gerekçesi, doğrulama yöntemi ve önceliği belli, test edilebilir güvenlik gereksinimleri tanımlar. Yeni bir uygulama veya özellik için güvenlik kabul kriterleri gerektiğinde, tehdit modeli backlog kalemlerine dönüştürülecekken ya da müşteri veya denetçi güvenlik gereksinimi temel çizgisi istediğinde kullanılır.
- Örnek istek: _"Yeni müşteri self-servis portalımız için güvenlik gereksinimlerini tanımla; portal kişisel veri işliyor, ödemeler barındırılan ödeme sayfası üzerinden alınıyor."_
- İlgili: `threat-model`, `nfr-specification`, `authn-authz-design`, `secure-code-review`, `acceptance-criteria`
- Dosya: [skills/09-security/security-engineer/design/security-requirements/SKILL.tr.md](skills/09-security/security-engineer/design/security-requirements/SKILL.tr.md)

**Kimlik doğrulama ve yetkilendirme tasarımı** · `authn-authz-design`

- Ne zaman: Bir uygulama veya API için kimlik doğrulama ve yetkilendirme tasarlar: kimlik sağlayıcı ve protokol seçimi (OIDC, OAuth 2.x, SAML), giriş ve token akışları, token süreleri ve saklama, roller, claim'ler veya öznitelikler ve en az yetki uygulama noktaları. Yeni uygulama veya API geliştirilirken, SSO ya da MFA eklenirken, API'ler iş ortaklarına veya makine istemcilerine açılırken ya da rol modeli yeniden tasarlanırken kullanılır.
- Örnek istek: _"B2B SaaS ürünümüz için kimlik doğrulama ve yetkilendirme tasarla: web SPA, iş ortakları için açık REST API, çok kiracılı yapı; müşteriler kendi Entra ID veya Okta'ları ile SSO istiyor."_
- İlgili: `security-requirements`, `threat-model`, `access-review`, `api-design-review`, `secrets-management-plan`
- Dosya: [skills/09-security/security-engineer/design/authn-authz-design/SKILL.tr.md](skills/09-security/security-engineer/design/authn-authz-design/SKILL.tr.md)

#### Güvenlik Değerlendirmesi

**Güvenli kod incelemesi** · `secure-code-review`

- Ne zaman: Kaynak kodu veya bir diff'i güvenlik zafiyetleri açısından inceler; bulguları OWASP Top 10 kategorileri ve CWE numaralarıyla eşler, güvenilmeyen girdiyi kaynaktan hedefe (sink) izler ve her bulgu için önem derecesi, kanıt ve somut düzeltme verir. Bir pull request kimlik doğrulama, yetkilendirme, girdi işleme, kriptografi, dosya veya ağ erişimine dokunduğunda ya da kodun zafiyet açısından kontrol edilmesi istendiğinde kullanılır.
- Örnek istek: _"Merge etmeden önce bu ASP.NET Core controller'ı ve repository sınıfını güvenlik açısından incele."_
- İlgili: `code-review`, `security-finding-report`, `vulnerability-triage`, `security-requirements`, `threat-model`
- Dosya: [skills/09-security/security-engineer/assessment/secure-code-review/SKILL.tr.md](skills/09-security/security-engineer/assessment/secure-code-review/SKILL.tr.md)

**Zafiyet önceliklendirme** · `vulnerability-triage`

- Ne zaman: Bildirilen bir zafiyeti (tarayıcı sonucu, bug bounty raporu, CVE duyurusu, sızma testi bulgusu) doğrular, CVSS ile puanlar, istismar edilebilirlik (EPSS, bilinen istismar durumu) ve gerçek ortamdaki erişilebilirliğe göre ayarlar; SLA ve sorumlusu belli, önceliklendirilmiş bir düzeltme planı üretir. Yeni bir zafiyet geldiğinde ve ekibin ne kadar acil davranacağına karar vermesi gerektiğinde kullanılır.
- Örnek istek: _"Şunu önceliklendir: tarayıcımız fatura içe aktarma servisinin kullandığı XML ayrıştırıcıda CVSS 9.8'lik bir CVE raporluyor. Bizim için ne kadar acil?"_
- İlgili: `dependency-vulnerability-review`, `security-finding-report`, `security-incident-response`, `bug-triage`, `it-risk-assessment`
- Dosya: [skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.tr.md](skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.tr.md)

**Bağımlılık zafiyetleri incelemesi** · `dependency-vulnerability-review`

- Ne zaman: Üçüncü taraf bağımlılıklar ve container image'lar için yazılım bileşen analizi (SCA) bulgularını inceler; paket bazında gruplar, doğrudan ve geçişli yolları belirler, en küçük güvenli yükseltme yollarını önerir ve henüz düzeltilemeyenler için risk kabulünü belgeler. SCA, SBOM veya container tarama raporunun uygulanabilir bir yükseltme planına dönüştürülmesi gerektiğinde ya da bilinen zafiyetli bileşenler için sürüm geçiş kapısı öncesinde kullanılır.
- Örnek istek: _"Node.js API'mizin SCA raporu burada: 47 bulgu, 6'sı kritik. Bunu yükseltme planına çevir ve şimdilik neyi kabul edebileceğimizi söyle."_
- İlgili: `vulnerability-triage`, `dependency-upgrade`, `dockerfile-review`, `security-finding-report`, `release-quality-gate`
- Dosya: [skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.tr.md](skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.tr.md)

**Sızma testi kapsamı** · `pentest-scope`

- Ne zaman: Yetkili bir sızma testinin kapsamını ve çalışma kurallarını tanımlar: hedefler, kapsam içi varlıklar, hariç tutulanlar, test türü ve derinliği, test pencereleri, hesaplar ve veriler, iletişim ve durdurma koşulları, yasal yetkilendirme ve raporlama beklentileri. İç veya dış sızma testi sipariş edilirken, test firmasıyla iş tanımı hazırlanırken ya da sürüm öncesi güvenlik testi planlanırken kullanılır.
- Örnek istek: _"Canlıya çıkmadan önce yeni müşteri portalımız ve açık API'miz için sızma testi kapsamını tanımla; dış bir firma grey-box test yapacak."_
- İlgili: `threat-model`, `security-finding-report`, `vulnerability-triage`, `audit-preparation`, `statement-of-work`
- Dosya: [skills/09-security/security-engineer/assessment/pentest-scope/SKILL.tr.md](skills/09-security/security-engineer/assessment/pentest-scope/SKILL.tr.md)

**Güvenlik bulgusu yazma** · `security-finding-report`

- Ne zaman: Başlık, etkilenen varlık, önem derecesi ve puanlama, açıklama, etki, tekrar üretme adımları, kanıt, çözüm ve referanslar içeren, sızma testi raporu, bug bounty yanıtı veya iç takip sistemi için uygun, net ve tekrar üretilebilir bir güvenlik bulgusu yazar. Doğrulanmış veya şüpheli bir güvenlik sorununun geliştiriciler, yönetim veya denetçiler için belgelenmesi gerektiğinde kullanılır.
- Örnek istek: _"Şunun için güvenlik bulgusu yaz: giriş yapmış herhangi bir kullanıcı URL'deki fatura numarasını değiştirerek başka bir kullanıcının fatura PDF'ini indirebiliyor."_
- İlgili: `vulnerability-triage`, `secure-code-review`, `pentest-scope`, `bug-report`, `security-incident-response`
- Dosya: [skills/09-security/security-engineer/assessment/security-finding-report/SKILL.tr.md](skills/09-security/security-engineer/assessment/security-finding-report/SKILL.tr.md)

#### Güvenlik Operasyonları

**Güvenlik olayına müdahale** · `security-incident-response`

- Ne zaman: Şüpheli veya doğrulanmış bir güvenlik olayına müdahaleyi ilk değerlendirme, sınırlandırma, kanıtların korunması, temizleme, kurtarma ve bildirim adımlarıyla yönetir; KVKK ve GDPR kişisel veri ihlali yükümlülüklerini içerir, olay kaydı ve aksiyon planı üretir. Sızma belirtisi, kimlik bilgisi sızıntısı, zararlı yazılım, veri kaçırma veya yetkisiz erişim işaretleri olduğunda ve ekibin yapılandırılmış, savunma odaklı bir müdahaleye ihtiyacı olduğunda kullanılır.
- Örnek istek: _"CI kullanıcımızın AWS erişim anahtarını herkese açık bir GitHub reposunda bulduk ve CloudTrail bilinmeyen bir IP'den çağrılar gösteriyor. Müdahale etmemize yardım et."_
- İlgili: `incident-response`, `incident-communication`, `postmortem`, `vulnerability-triage`, `security-finding-report`
- Dosya: [skills/09-security/security-engineer/operations/security-incident-response/SKILL.tr.md](skills/09-security/security-engineer/operations/security-incident-response/SKILL.tr.md)

**Erişim yetkisi gözden geçirme** · `access-review`

- Ne zaman: Bir uygulama, veritabanı, bulut hesabı veya dizin grubu için kullanıcı erişim gözden geçirmesi (erişim yeniden onayı) yapar: yetkileri İK ve rol verileriyle karşılaştırarak fazla, sahipsiz, kullanılmayan, paylaşılan ve görevler ayrılığıyla çakışan yetkileri tespit eder, denetçiler için kanıtlı kaldır/koru kararları üretir. ISO 27001, SOC 2, SOX veya BDDK kapsamındaki periyodik erişim gözden geçirmelerinde, yeniden yapılanmalardan sonra ya da yetki birikmesinden şüphelenildiğinde kullanılır.
- Örnek istek: _"ERP'mizden alınan kullanıcı-rol listesi ve İK'nın aktif çalışan listesi burada. Çeyreklik erişim gözden geçirmesini yap ve kaldırılması gerekenleri işaretle."_
- İlgili: `authn-authz-design`, `audit-preparation`, `control-mapping`, `it-risk-assessment`, `raci-matrix`
- Dosya: [skills/09-security/security-engineer/operations/access-review/SKILL.tr.md](skills/09-security/security-engineer/operations/access-review/SKILL.tr.md)

### Yönetişim, Risk ve Uyum

#### Uyum

**Kişisel veri etki değerlendirmesi** · `privacy-impact-assessment`

- Ne zaman: Bir özellik veya sistem için KVKK/GDPR kişisel veri etki değerlendirmesi (DPIA) yapar: işleme faaliyetlerini, hukuki sebepleri, veri akışlarını ve aktarımları çıkarır, ilgili kişiler açısından riskleri puanlar ve tasarımda gizlilik önlemleri önerir. Yeni bir özellik veya sistem kişisel ya da özel nitelikli veri işlediğinde, profilleme, izleme, yeni alıcılar veya yurt dışı aktarım getirdiğinde ya da hukuk birimi veya veri koruma sorumlusu DPIA istediğinde kullanılır.
- Örnek istek: _"Mağaza ziyaretlerini konumla izleyip kişiye özel kampanya gönderen yeni müşteri sadakat uygulamamız için kişisel veri etki değerlendirmesi yap."_
- İlgili: `data-classification`, `threat-model`, `retention-policy`, `security-requirements`, `it-risk-assessment`
- Dosya: [skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.tr.md](skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.tr.md)

**Kontrolleri standarda eşleme** · `control-mapping`

- Ne zaman: Kurumun mevcut kontrollerini, süreçlerini ve kanıtlarını ISO/IEC 27001 Ek A veya SOC 2 Trust Services Criteria gibi bir hedef standarda eşler; kapsama oranını, kanıt eksiklerini ve diğer çerçevelerle örtüşmeleri gösterir. Sertifikasyona hazırlanırken, müşteri güvenlik anketini yanıtlarken, çerçeveleri birleştirirken (ISO 27001, SOC 2, KVKK, PCI DSS) veya bir kontrolün gerçekten denetim kanıtı üretip üretmediğini kontrol ederken kullanılır.
- Örnek istek: _"Mevcut kontrollerimizi ISO 27001:2022 Ek A'ya eşle ve hangilerinin kanıtı olmadığını göster."_
- İlgili: `audit-preparation`, `policy-writing`, `it-risk-assessment`, `access-review`, `traceability-matrix`
- Dosya: [skills/09-security/compliance/compliance/control-mapping/SKILL.tr.md](skills/09-security/compliance/compliance/control-mapping/SKILL.tr.md)

**Güvenlik/BT politikası yazma** · `policy-writing`

- Ne zaman: Amaç, kapsam, uygulanabilir kurallar, roller, istisnalar, uyum ölçümü ve gözden geçirme döngüsü içeren bir güvenlik veya BT politikası yazar ya da revize eder; politikayı standart ve prosedürlerden ayırır. Bir politika eksik, güncelliğini yitirmiş veya denetimde bulgu almışsa ya da ISO 27001, SOC 2, KVKK veya iç yönetişim için gerekiyorsa (ör. kabul edilebilir kullanım, erişim kontrolü, parola, yedekleme, uzaktan çalışma, yapay zekâ kullanımı) kullanılır.
- Örnek istek: _"Şirketimiz için erişim kontrol politikası yaz; ISO 27001'e hazırlanıyoruz, Entra ID ve GitHub kullanıyoruz."_
- İlgili: `control-mapping`, `audit-preparation`, `it-risk-assessment`, `retention-policy`, `document-review`
- Dosya: [skills/09-security/compliance/compliance/policy-writing/SKILL.tr.md](skills/09-security/compliance/compliance/policy-writing/SKILL.tr.md)

**Denetime hazırlık** · `audit-preparation`

- Ne zaman: Bir ekibi iç, sertifikasyon, müşteri veya düzenleyici denetimine hazırlar: kapsamı ve kriterleri teyit eder, sorumlu ve teslim tarihli kanıt talep listesi oluşturur, hazırlık eksiklerini kontrol eder, denetim haftasını ve denetlenenlerin bilgilendirilmesini planlar. Bir denetim tarihi açıklandığında (ISO 27001, SOC 2, KVKK, PCI DSS, BDDK, müşteri denetimi), denetçi talep listesi gönderdiğinde veya önceki bulgular bir sonraki denetimden önce kapatılmalıysa kullanılır.
- Örnek istek: _"ISO 27001 gözetim denetimimiz altı hafta sonra. Kanıt listesini, eksikleri ve planı hazırla."_
- İlgili: `control-mapping`, `access-review`, `policy-writing`, `it-risk-assessment`, `schedule-plan`
- Dosya: [skills/09-security/compliance/compliance/audit-preparation/SKILL.tr.md](skills/09-security/compliance/compliance/audit-preparation/SKILL.tr.md)

**BT risk değerlendirmesi** · `it-risk-assessment`

- Ne zaman: Bir varlık veya hizmet kapsamı için BT ve bilgi güvenliği riskini değerlendirir: varlıkları, tehditleri ve zafiyetleri belirler, mevcut kontrollerle olasılık ve etkiyi puanlar, işleme seçeneğine (azaltma, transfer, kaçınma, kabul) karar verir ve her risk için bir risk kaydı üretir. ISO 27001 risk değerlendirmesi kurulurken veya yenilenirken, yeni bir tedarikçi, sistem ya da değişiklik değerlendirilirken, risk kabulü hazırlanırken veya yönetim bir şeyin ne kadar riskli olduğunu sorduğunda kullanılır.
- Örnek istek: _"Şirket içi ERP'mizi barındırılan bir bulut sağlayıcıya taşımanın BT riskini, tedarikçi ve veri riskleri dahil değerlendir."_
- İlgili: `threat-model`, `risk-register`, `control-mapping`, `vulnerability-triage`, `privacy-impact-assessment`
- Dosya: [skills/09-security/compliance/compliance/it-risk-assessment/SKILL.tr.md](skills/09-security/compliance/compliance/it-risk-assessment/SKILL.tr.md)

## UX / UI Tasarım

### UX Araştırmacısı

#### Kullanıcı Araştırması

**Araştırma planı** · `research-plan`

- Ne zaman: Araştırmanın desteklediği kararı, araştırma hedeflerini ve sorularını, yöntem seçimini ve gerekçesini, katılımcı kriterlerini ve örneklemi, lojistiği, etik ve onamı, takvimi ve çıktıları içeren bir kullanıcı araştırması planı yazar. Ekip \"kullanıcılarla konuşmak\", bir konsepti doğrulamak, bir davranışı anlamak veya bir tasarımı değerlendirmek istediğinde ve katılımcı toplamadan ya da oturum ayarlamadan önce kullanılır.
- Örnek istek: _"Küçük işletme sahiplerinin fatura uygulamamızı ilk hafta içinde neden bıraktığını anlamak için bir araştırma planı yaz."_
- İlgili: `screener-survey`, `usability-test-script`, `interview-question-set`, `research-synthesis`, `hypothesis-statement`
- Dosya: [skills/10-design/ux-researcher/research/research-plan/SKILL.tr.md](skills/10-design/ux-researcher/research/research-plan/SKILL.tr.md)

**Kullanılabilirlik testi senaryosu** · `usability-test-script`

- Ne zaman: Moderatörlü veya moderatörsüz bir kullanılabilirlik testi senaryosu yazar; giriş ve onay, ısınma, gerçekçi görev senaryoları, yönlendirmesiz sorular, gözlemlenebilir başarı kriterleri, görev sonrası ve test sonrası ölçümler ile kapanışı içerir. Bir prototip veya canlı ürün kullanıcılarla test edilecekse, \"test görevleri\" ya da \"moderatör rehberi\" istendiğinde veya bir kullanılabilirlik oturumu planlanmadan önce kullanılır.
- Örnek istek: _"Yeni ödeme adımı prototipimiz için kullanılabilirlik testi senaryosu yaz; ilk kez alışveriş yapanların indirim kodu uygulayıp kartla ödeme yapabildiğini görmek istiyoruz."_
- İlgili: `research-plan`, `screener-survey`, `research-synthesis`, `heuristic-evaluation`, `interview-question-set`
- Dosya: [skills/10-design/ux-researcher/research/usability-test-script/SKILL.tr.md](skills/10-design/ux-researcher/research/usability-test-script/SKILL.tr.md)

**Araştırma bulgularını sentezleme** · `research-synthesis`

- Ne zaman: Ham araştırma verisini (görüşme notları, kullanılabilirlik gözlemleri, açık uçlu anket yanıtları) benzerlik gruplamasıyla kanıta dayalı bulgulara, içgörülere ve önceliklendirilmiş önerilere dönüştürür; her biri için sıklık, önem ve güven düzeyi verir. Görüşmeler veya kullanılabilirlik oturumlarından sonra, \"ne öğrendik\" sorulduğunda ya da notların bir karar için sunuma dönüşmesi gerektiğinde kullanılır.
- Örnek istek: _"8 onboarding görüşmesinin notlarını ürün ekibi için temel içgörülere ve önerilere dönüştür."_
- İlgili: `research-plan`, `usability-test-script`, `interview-notes-analysis`, `feedback-synthesis`, `customer-journey-map`
- Dosya: [skills/10-design/ux-researcher/research/research-synthesis/SKILL.tr.md](skills/10-design/ux-researcher/research/research-synthesis/SKILL.tr.md)

**Katılımcı eleme anketi** · `screener-survey`

- Ne zaman: Bir çalışma için doğru kullanıcıları seçen katılımcı eleme anketi yazar; davranışa dayalı dahil etme ve hariç tutma kriterleri, doğru cevabı belli etmeyen yönlendirmesiz sorular, segment kotaları, eleme mantığı ve onay içerir. Görüşme, kullanılabilirlik testi veya günlük çalışması için katılımcı bulmadan önce ya da \"kiminle konuşmalıyız\" veya \"katılımcı seçme anketi yaz\" dendiğinde kullanılır.
- Örnek istek: _"En az ayda bir fatura kesen ve son bir yılda rakip bir uygulamayı denemiş 8 küçük işletme sahibini bulmak için eleme anketi yaz."_
- İlgili: `research-plan`, `usability-test-script`, `questionnaire-design`, `persona`, `interview-question-set`
- Dosya: [skills/10-design/ux-researcher/research/screener-survey/SKILL.tr.md](skills/10-design/ux-researcher/research/screener-survey/SKILL.tr.md)

### UX / UI Tasarımcı

#### Etkileşim ve Görsel Tasarım

**Kullanıcı akışı tasarlama** · `user-flow`

- Ne zaman: Tek bir kullanıcı hedefi için kullanıcı akışı tasarlar; giriş noktaları, ekranlar ve adımlar, karar noktaları, sistem aksiyonları, hata ve kurtarma yolları, boş ve uç durumlar ile çıkış noktalarını bir adım tablosu ve diagram-as-code akış şemasıyla verir. Bir özellik veya yolculuk ekran ekran tasarlanacaksa, \"adımlar neler\" ya da \"mutlu ve mutsuz yolları çıkar\" dendiğinde veya wireframe'den önce kullanılır.
- Örnek istek: _"Mobil bankacılık uygulamamızda unutulan şifreyi sıfırlama için kullanıcı akışını hatalar ve hesap kilitlenmesi dahil tasarla."_
- İlgili: `customer-journey-map`, `wireframe-spec`, `information-architecture`, `edge-case-elicitation`, `diagram-as-code`
- Dosya: [skills/10-design/ux-ui-designer/design/user-flow/SKILL.tr.md](skills/10-design/ux-ui-designer/design/user-flow/SKILL.tr.md)

**Bilgi mimarisi oluşturma** · `information-architecture`

- Ne zaman: Bir ürünün veya sitenin bilgi mimarisini oluşturur; içerik envanteri, düzenleme şeması, site haritası hiyerarşisi, navigasyon modeli, etiketleme sistemi ve bunu doğrulamak için kart sıralama veya ağaç testi planı üretir. Bir ürün, portal veya dokümantasyon sitesi kurulurken ya da yeniden yapılandırılırken, kullanıcılar \"aradığını bulamıyorsa\" veya navigasyon ve menü etiketlerine karar verilecekse kullanılır.
- Örnek istek: _"İK self servis portalımızın navigasyonunu yeniden yapılandır; çalışanlar izin, bordro ve masraf sayfalarını bulamıyor."_
- İlgili: `user-flow`, `wireframe-spec`, `docs-information-architecture`, `research-plan`, `persona`
- Dosya: [skills/10-design/ux-ui-designer/design/information-architecture/SKILL.tr.md](skills/10-design/ux-ui-designer/design/information-architecture/SKILL.tr.md)

**Wireframe tarifi** · `wireframe-spec`

- Ne zaman: Tek bir ekran veya görünüm için wireframe'i metinle tarif eder; amaç, yerleşim bölgeleri, bileşenler, içerik önceliği, etkileşimler, tüm durumlar (varsayılan, yükleniyor, boş, hata, kısmi, yetki), duyarlı davranış ve erişilebilirlik notlarını kapsar. Bir ekranın görsel maketten önce veya onun yerine tanımlanması gerektiğinde, \"bu ekranda ne olacak\" sorulduğunda ya da wireframe'in ürün ve yazılım ekiplerince metin üzerinden incelenmesi gerektiğinde kullanılır.
- Örnek istek: _"E-ticaret web uygulamamızın sipariş geçmişi ekranı için boş ve hata durumları dahil wireframe tarifi yaz."_
- İlgili: `user-flow`, `information-architecture`, `screen-requirements`, `design-handoff`, `microcopy`
- Dosya: [skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.tr.md](skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.tr.md)

**Sezgisel değerlendirme** · `heuristic-evaluation`

- Ne zaman: Bir ürünü, akışı veya ekranları Nielsen'in 10 kullanılabilirlik ilkesine göre değerlendirir; ihlal edilen ilke, kanıt, 0-4 önem derecesi ve somut öneriyle konumlandırılmış bulgular ile önceliklendirilmiş bir özet üretir. Kullanıcı testinden önce veya onun yerine hızlı bir uzman kullanılabilirlik incelemesi gerektiğinde, \"bu arayüzde ne yanlış\" sorulduğunda ya da ekran görüntüleri, prototipler veya canlı bir akış denetlenecekse kullanılır.
- Örnek istek: _"Masraf girişi akışımız için sezgisel değerlendirme yap; 4 ekranın görüntüleri ekte."_
- İlgili: `usability-test-script`, `accessibility-audit`, `design-critique`, `research-synthesis`, `user-flow`
- Dosya: [skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.tr.md](skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.tr.md)

**Tasarım eleştirisi** · `design-critique`

- Ne zaman: Tasarımın hedeflerine, kullanıcılarına ve kısıtlarına dayanan, konum ve etki açısından somut, gözlemi görüşten ayıran ve geri bildirimi önerilen yönlerle birlikte mutlaka düzeltilmeli, değerlendirilmeli ve ufak dokunuşlar olarak önceliklendiren yapılandırılmış tasarım eleştirisi verir. Bir tasarımcı devam eden işini paylaşıp geri bildirim istediğinde, tasarım incelemesine veya eleştiri oturumuna hazırlanırken ya da \"bu tasarım hakkında ne düşünüyorsun\" sorulduğunda kullanılır.
- Örnek istek: _"Bu gösterge paneli yeniden tasarımını eleştir; hedef, operasyon yöneticilerinin sorunlu mağazaları 10 saniye içinde görebilmesi."_
- İlgili: `heuristic-evaluation`, `accessibility-audit`, `wireframe-spec`, `feedback-sbi`, `review-comment-writing`
- Dosya: [skills/10-design/ux-ui-designer/design/design-critique/SKILL.tr.md](skills/10-design/ux-ui-designer/design/design-critique/SKILL.tr.md)

**Tasarım sistemi bileşeni tanımlama** · `design-system-component-spec`

- Ne zaman: Yeniden kullanılabilir bir tasarım sistemi bileşenini amacı, anatomisi, varyantları, boyutları, durumları, tasarım token'ları, davranışı, içerik kuralları, erişilebilirlik gereksinimleri, yap/yapma kullanım kuralları ve geliştirme için API/prop'larıyla tanımlar. Tasarım sistemine yeni bir bileşen önerildiğinde, mevcut bir bileşenin dokümante edilmesi veya kırıcı bir değişiklik geçirmesi gerektiğinde ya da ekipler aynı kalıbın farklı sürümlerini geliştirdiğinde kullanılır.
- Örnek istek: _"Web ve mobil ekiplerin aynı şekilde geliştirebileceği bir Toast bildirim bileşeni için tasarım sistemi spesifikasyonu yaz."_
- İlgili: `design-handoff`, `wireframe-spec`, `component-design`, `accessibility-audit`, `microcopy`
- Dosya: [skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.tr.md](skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.tr.md)

**Tasarım teslimi hazırlama** · `design-handoff`

- Ne zaman: Bir ekran, akış veya özellik için geliştiriciye hazır bir tasarım teslimi hazırlar; yerleşim ve boşluk ölçüleri, tasarım token'ları, bileşen eşlemesi, etkileşimler ve hareket, tüm uç durumlar, duyarlı (responsive) kurallar, erişilebilirlik notları, içerik ve varlıklar ile açık kararları kapsar. Bir tasarım onaylanıp geliştirmeye geçerken, geliştiriciler \"bu tam olarak ne yapmalı\" diye sorduğunda veya maket ya da tasarım dosyasının yanına bir teslim notu gerektiğinde kullanılır.
- Örnek istek: _"Web ekibi bir sonraki iterasyonda başlayabilsin diye yeni ödeme adımının (kart ile ödeme) tasarım teslimini hazırla."_
- İlgili: `wireframe-spec`, `design-system-component-spec`, `user-flow`, `microcopy`, `acceptance-criteria`
- Dosya: [skills/10-design/ux-ui-designer/design/design-handoff/SKILL.tr.md](skills/10-design/ux-ui-designer/design/design-handoff/SKILL.tr.md)

### UX Yazarı / İçerik Tasarımcısı

#### İçerik

**Mikro metin yazma** · `microcopy`

- Ne zaman: Buton ve bağlantı etiketleri, form etiketleri, yardımcı metinler, yer tutucular, araç ipuçları, boş durumlar, onaylar ve başarı mesajları gibi arayüz mikro metinlerini kullanıcının görevine, ürünün sesine, uzunluk sınırlarına ve yerelleştirmeye uygun şekilde yazar. Bir ekranın veya akışın arayüz metinlerinin yazılması ya da iyileştirilmesi gerektiğinde, etiketler belirsiz veya tutarsız olduğunda ya da \"bu buton ne demeli\" sorusu sorulduğunda kullanılır.
- Örnek istek: _"Yeni \"ekip arkadaşı davet et\" penceremizin mikro metinlerini yaz: başlık, alan etiketleri, yardımcı metin, butonlar ve boş durum."_
- İlgili: `error-message-writing`, `voice-and-tone-guide`, `design-handoff`, `style-guide-check`, `glossary-builder`
- Dosya: [skills/10-design/ux-writer/content/microcopy/SKILL.tr.md](skills/10-design/ux-writer/content/microcopy/SKILL.tr.md)

**Hata mesajı yazma** · `error-message-writing`

- Ne zaman: Kullanıcıya dönük hata, doğrulama ve uyarı mesajlarını ne olduğunu, yardımcı olacaksa nedenini ve şimdi ne yapılacağını söyleyecek şekilde; suçlama, jargon veya iç detay sızdırmadan, doğru konum, önem derecesi ve erişilebilirlik davranışıyla yazar. Hata durumları için metin gerektiğinde, mevcut mesajlar belirsiz (\"Bir şeyler ters gitti\") veya teknik olduğunda ya da bir hata kataloğu kullanıcıya dönük metne çevrilecekse kullanılır.
- Örnek istek: _"Bu beş ödeme hata mesajını kullanıcı ne olduğunu ve ne yapacağını anlayacak şekilde yeniden yaz; şu an sadece API hata kodlarını gösteriyorlar."_
- İlgili: `microcopy`, `voice-and-tone-guide`, `error-scenario-catalog`, `error-handling-review`, `design-handoff`
- Dosya: [skills/10-design/ux-writer/content/error-message-writing/SKILL.tr.md](skills/10-design/ux-writer/content/error-message-writing/SKILL.tr.md)

**Ses ve ton rehberi** · `voice-and-tone-guide`

- Ne zaman: Bir ürün veya marka için ses ve ton rehberi yazar; her biri ne olduğu ve ne olmadığıyla tanımlanan 3-5 ses ilkesi, yap/yapma örnek çiftleri, kullanıcı bağlamına göre değişen bir ton haritası (başarı, hata, ilk kullanım, hassas anlar), dil bilgisi ve terminoloji kuralları ile yazarlar için bir gözden geçirme listesi içerir. Bir üründe tutarlı arayüz yazımı olmadığında, birden fazla ekip farklı yazdığında, yeni bir dile veya pazara girilirken ya da mevcut rehber uygulanamayacak kadar belirsiz olduğunda kullanılır.
- Örnek istek: _"B2B faturalama uygulamamız için Türkçe ve İngilizce bir ses ve ton rehberi oluştur; metinlerimiz şu an her ekranda farklı konuşuyor."_
- İlgili: `microcopy`, `error-message-writing`, `style-guide-check`, `positioning-statement`, `glossary-builder`
- Dosya: [skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.tr.md](skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.tr.md)

## Destek ve BT Operasyonları

### Destek Mühendisi (L1-L3)

#### Kayıt Yönetimi

**Destek kaydı sınıflandırma** · `ticket-triage`

- Ne zaman: Gelen bir destek kaydını sınıflandırır: türünü belirler (olay, hizmet talebi, soru, hata, güvenlik veya kişisel veri bildirimi), etki ve aciliyetten önceliği çıkarır, mükerrer kayıt veya süren bir kesinti olup olmadığını kontrol eder, eksik bilgileri belirler ve doğru kuyruğa veya seviyeye yönlendirir. Destek kuyruğuna yeni bir kayıt, e-posta veya sohbet talebi geldiğinde, sınıflandırılmamış kayıt birikimi ayıklanacağında veya öncelik tartışmalı olduğunda kullanılır.
- Örnek istek: _"Bu kaydı sınıflandır: 'Bu sabahtan beri 40 şube kullanıcımızın hiçbiri POS'tan fatura yazdıramıyor, elle yazıyoruz.'"_
- İlgili: `ticket-response`, `ticket-escalation-summary`, `known-error-article`, `incident-response`, `bug-report`
- Dosya: [skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.tr.md)

**Destek kaydı yanıtı** · `ticket-response`

- Ne zaman: Bir destek kaydına müşteriye yönelik yanıt yazar: sorunu kabul eder, bilineni söyler, sahibi ve zamanı belli net bir yanıt veya sonraki adım verir ve yalnızca gereken bilgiyi ister. Yeni veya güncellenmiş bir kayda yanıt verirken, bekleyen bir kaydı takip ederken, çözüm iletirken, bir talebi reddederken ya da fazla teknik, uzun veya savunmacı bir taslak yanıtı yeniden yazarken kullanılır.
- Örnek istek: _"Bu müşteriye yanıt yaz: parola sıfırlamadan sonra giriş yapamıyor, bu hafta ikinci kez oluyor ve çok sinirli."_
- İlgili: `ticket-triage`, `ticket-escalation-summary`, `known-error-article`, `tone-rewrite`, `bad-news-delivery`
- Dosya: [skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.tr.md)

**Eskalasyon için kayıt özeti** · `ticket-escalation-summary`

- Ne zaman: Bir destek kaydını ve geçmişini bir sonraki destek seviyesi, yazılım ekibi veya tedarikçi için eskalasyon özetine dönüştürür: iş etkisi, kesin belirti, ortam, zaman çizelgesi, denenenler ve sonuçları, kanıtlar ve net talep. Kayıt L1'den L2/L3'e, ürün ekibine veya üçüncü tarafa geçeceğinde, uzun bir kayıt yazışması için devir notu gerektiğinde veya müşteri eskalasyon için baskı yaptığında kullanılır.
- Örnek istek: _"30 mesajlık bu kaydı L3 için özetle: kullanıcılar salıdan beri web portalında birkaç dakikada bir 'oturum süresi doldu' hatası alıyor; önbellekleri temizledik, parolaları sıfırladık, değişen bir şey yok."_
- İlgili: `ticket-triage`, `ticket-response`, `log-analysis`, `bug-report`, `problem-management`
- Dosya: [skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.tr.md)

**Bilinen hata makalesi** · `known-error-article`

- Ne zaman: Destek bilgi bankası için bilinen hata makalesi yazar: aranabilir belirti, kapsam ve etkilenen sürümler, doğrulanmış veya şüphelenilen neden, riskleriyle adım adım geçici çözüm, kalıcı çözüm durumu ve ilişkili kayıtlar. Bir problemin kök nedeni veya geçici çözümü belgelendiğinde, aynı kayıt tekrar tekrar geldiğinde ya da kalıcı çözüm beklenirken destek ekibinin tutarlı bir yanıt vermesi gerektiğinde kullanılır.
- Örnek istek: _"Bilinen hata makalesi yaz: 7.3 sürümünden beri 10.000 satırı aşan raporlarda PDF dışa aktarma 'Error 500' ile başarısız oluyor; geçici çözüm CSV'ye aktarmak; düzeltme 7.4'te planlandı."_
- İlgili: `problem-management`, `ticket-response`, `ticket-triage`, `how-to-guide`, `faq-builder`
- Dosya: [skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.tr.md)

**Müşteriye kesinti bildirimi** · `customer-outage-notice`

- Ne zaman: Bir hizmet kesintisinin her aşaması (inceleniyor, neden bulundu, izleniyor, çözüldü) ve planlı bakım için müşteriye yönelik kesinti bildirimleri yazar: sade dille etki, etkilenen hizmetler ve bölgeler, durum, geçici çözüm ve sonraki güncelleme zamanı; spekülasyon ve suçlama içermez. Müşteriler bir kesinti veya performans düşüşünden etkilendiğinde, durum sayfası veya e-posta güncellemesi gerektiğinde ya da planlı bakım duyurulacağında kullanılır.
- Örnek istek: _"İlk durum sayfası bildirimini yaz: 14:05'ten beri Türkiye'deki müşterilerin yaklaşık %30'unda kartla ödeme başarısız oluyor, neden bilinmiyor, ekip inceliyor."_
- İlgili: `incident-communication`, `incident-response`, `ticket-response`, `postmortem`, `known-error-article`
- Dosya: [skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.tr.md)

### BT Hizmet Yönetimi

#### ITSM Süreçleri

**Problem yönetimi** · `problem-management`

- Ne zaman: Tekrarlayan veya büyük olaylar için problem yönetimi yürütür: ilişkili olayları gruplar, problemi tanımlar, kanıta dayalı kök neden analizini yönetir, geçici çözümüyle birlikte bilinen hata kaydı oluşturur ve doğrulama kriterleriyle kalıcı çözümleri değişiklik kontrolü üzerinden önerir. Aynı olay türü tekrarladığında, büyük bir olaydan sonra, olay eğilimleri altta yatan bir nedene işaret ettiğinde veya bir problem kaydı açılacağında, ilerletileceğinde ya da kapatılacağında kullanılır.
- Örnek istek: _"Problem kaydı aç: 3 haftada gece batch'inin uzayıp sabah raporlarının geciktiği 7 olay yaşadık; her birinde job yeniden başlatılarak çözüldü."_
- İlgili: `known-error-article`, `five-whys`, `fishbone-analysis`, `change-request-rfc`, `postmortem`
- Dosya: [skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.tr.md)

**Değişiklik talebi (RFC) yazma** · `change-request-rfc`

- Ne zaman: Değişiklik onayı veya değişiklik danışma kurulu (CAB) için hazır bir BT değişiklik talebi (RFC) yazar: gerekçe, kapsam ve etkilenen konfigürasyon öğeleri, değişiklik türü, risk ve etki değerlendirmesi, uygulama planı, test kanıtları, tetikleyicisiyle geri alma planı, takvim, iletişim ve doğrulama. Altyapı, uygulama, yapılandırma veya veride bir üretim değişikliği onay gerektirdiğinde, CAB'a sunum yapılacağında veya acil bir değişikliğin belgelenmesi gerektiğinde kullanılır.
- Örnek istek: _"Üretimdeki PostgreSQL kümesini bu cumartesi gecesi 14'ten 16'ya yükseltmek için RFC yaz; 3 uygulama buna bağlı, geçen hafta staging'de test ettik."_
- İlgili: `rollback-plan`, `deployment-checklist`, `deployment-strategy`, `technical-risk-review`, `problem-management`
- Dosya: [skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.tr.md)

**SLA ihlal analizi** · `sla-breach-analysis`

- Ne zaman: Bir dönemdeki SLA ihlallerini analiz eder: veriyi ve süre sayım kurallarını doğrular, ihlal oranlarını öncelik, kategori, ekip, zaman ve müşteri bazında ölçer, örüntüleri ve kök nedenleri (süreç, kapasite, yönlendirme, bağımlılık, ölçüm) bulur ve sahipli, hedef metrikli, önceliklendirilmiş iyileştirme aksiyonları önerir. SLA performansı düştüğünde, bir hizmet değerlendirmesi veya sözleşme görüşmesi öncesinde, ceza veya iade söz konusu olduğunda ya da bir ekip kayıtların neden hedefi kaçırdığını anlamak istediğinde kullanılır.
- Örnek istek: _"Geçen çeyreğin SLA ihlallerini analiz et: P2 çözüm hedefi 8 iş saati, %90 hedefe karşı %71 tutturduk; kayıt dökümü ekte."_
- İlgili: `problem-management`, `ticket-triage`, `slo-definition`, `kpi-definition`, `dashboard-spec`
- Dosya: [skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.tr.md)

**Hizmet kataloğu kaydı** · `service-catalog-entry`

- Ne zaman: Müşteri diliyle bir hizmet kataloğu kaydı yazar: hizmetin ne olduğu ve ne olmadığı, kimlerin kullanabileceği, talep seçenekleri ve nasıl talep edileceği, onaylar, karşılama adımları, hizmet seviyeleri ve destek saatleri, ücretliyse maliyetler, bağımlılıklar, sorumluluklar ve sahiplik. Yeni bir BT veya iç hizmet devreye alındığında, mevcut bir kayıt eskidiğinde veya belirsizleştiğinde, talep edenler bir şeyi nasıl alacaklarını sürekli sorduğunda ya da hizmet seviyelerinin kullanıcılara duyurulması gerektiğinde kullanılır.
- Örnek istek: _"'Geliştirici VM' hizmetimiz için katalog kaydı yaz: geliştiriciler 8 vCPU/32 GB Linux VM talep ediyor, yönetici onayı gerekiyor, 2 iş gününde teslim ediliyor, uzatılmazsa 90 gün sonra siliniyor."_
- İlgili: `slo-definition`, `sla-breach-analysis`, `raci-matrix`, `user-guide`, `faq-builder`
- Dosya: [skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.tr.md)

## Teknik Yazarlık

### Teknik Yazar

#### Ürün Dokümantasyonu

**Kullanıcı kılavuzu yazma** · `user-guide`

- Ne zaman: Bir ürün veya özellik için, kullanıcıların başarması gereken işler etrafında düzenlenmiş; ön koşullar, numaralı adımlar, beklenen sonuçlar, ekran görüntüsü yer tutucuları, sorun giderme ve çapraz bağlantılar içeren görev bazlı bir kullanıcı kılavuzu yazar. Son kullanıcıların veya yöneticilerin yeni ya da değişen bir özellik için dokümantasyona ihtiyaç duyduğunda, bir sürüm kullanıcıya yönelik doküman gerektirdiğinde veya mevcut kılavuz özellik odaklı olup zor takip edildiğinde kullanılır.
- Örnek istek: _"Bu spesifikasyonlara ve ekran adlarına göre finans onaylayıcıları için yeni fatura onay akışımızın kullanıcı kılavuzu bölümünü yaz."_
- İlgili: `how-to-guide`, `tutorial`, `docs-information-architecture`, `style-guide-check`, `faq-builder`
- Dosya: [skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.tr.md)

**Eğitim (tutorial) yazma** · `tutorial`

- Ne zaman: Diátaxis anlamında öğrenme odaklı bir eğitim (tutorial) yazar; yeni başlayan birinin somut bir şey inşa ettiği, tanımlı bir öğrenme çıktısı, ön koşulları, küçük ve doğrulanabilir adımları, her adımdan sonra görünür sonuçları olan ve sapma içermeyen tek bir yönlendirilmiş yol sunar. Yeni kullanıcıları veya geliştiricileri bir ürüne, API'ye, SDK'ya ya da platforma alıştırırken, bir \"başlarken\" veya ilk proje dersi gerektiğinde ya da mevcut başlangıç içeriği referans ve nasıl yapılır karışımı olduğunda kullanılır.
- Örnek istek: _"Ödeme API'miz için, bir geliştiricinin yaklaşık 30 dakikada test ödemesi oluşturup webhook'u işlediği bir başlangıç eğitimi yaz."_
- İlgili: `how-to-guide`, `user-guide`, `docs-information-architecture`, `technical-onboarding`, `readme-writing`
- Dosya: [skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.tr.md)

**Nasıl yapılır rehberi** · `how-to-guide`

- Ne zaman: Diátaxis anlamında hedef odaklı bir nasıl yapılır rehberi yazar; temel bilgiye sahip okuru belirli bir başlangıç noktasından tek bir gerçek sonuca götüren, ön koşulları, numaralı eylem adımları, karar noktaları, doğrulama ve sorun giderme içeren, öğretim ya da arka plan sapması barındırmayan odaklı bir tarif sunar. Kullanıcılar \"... nasıl yapılır\" diye sorduğunda, bir destek kaydı veya tekrarlayan soru dokümansız bir görevi ortaya çıkardığında ya da mevcut dokümanlar pratik bir görev için eğitim, referans ve açıklamayı karıştırdığında kullanılır.
- Örnek istek: _"Entegrasyon geliştiricileri için platformumuzda API imzalama anahtarını kesinti olmadan yenilemeyi anlatan bir nasıl yapılır rehberi yaz."_
- İlgili: `tutorial`, `user-guide`, `docs-information-architecture`, `style-guide-check`, `runbook`
- Dosya: [skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.tr.md)

**Doküman bilgi mimarisi** · `docs-information-architecture`

- Ne zaman: Bir doküman setinin bilgi mimarisini Diátaxis dört türüne (eğitim, nasıl yapılır, referans, açıklama) göre tasarlar veya yeniden yapılandırır; mevcut sayfaları denetler, karışık içeriği sınıflandırıp böler, gezinme, adlandırma ve sayfa türlerini tanımlar, hedef site haritası ve geçiş planı üretir. Dokümanlarda gezinmek zor olduğunda, sayfalar öğrenme, görev, referans ve kavramı karıştırdığında, yeni bir ürün veya portal doküman yapısına ihtiyaç duyduğunda ya da bir doküman taşıma veya birleştirme öncesinde kullanılır.
- Örnek istek: _"Mevcut 60 sayfalık doküman menümüz burada; geliştiricilerin kurulumu, görevleri ve API referansını daha hızlı bulması için yeniden yapılandırma öner."_
- İlgili: `tutorial`, `how-to-guide`, `user-guide`, `api-reference-docs`, `glossary-builder`
- Dosya: [skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.tr.md)

**Stil rehberi kontrolü** · `style-guide-check`

- Ne zaman: Bir dokümanı stil rehberine ve terminoloji listesine göre kontrol eder; her sapmayı konum, kural, önem derecesi ve somut yeniden yazımla raporlar: terminoloji, anlatım ve ton, dil bilgisi ve yazım, biçim kuralları, arayüz ve kod atıfları, kapsayıcı ve erişilebilir dil. Dokümantasyon, arayüz metni, sürüm notu veya bilgi bankası makalesi yayımlanmadan ya da gözden geçirmeye gönderilmeden önce, birden fazla yazar tutarsız içerik ürettiğinde ya da bir ekip kendi veya kamuya açık bir stil rehberini uygulamak istediğinde kullanılır.
- Örnek istek: _"Bu kurulum kılavuzunu stil rehberimize ve terminoloji listemize göre kontrol et, düzeltmeleri tablo olarak ver."_
- İlgili: `glossary-builder`, `document-review`, `document-simplify`, `user-guide`, `how-to-guide`
- Dosya: [skills/12-technical-writing/technical-writer/docs/style-guide-check/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/style-guide-check/SKILL.tr.md)

## Mühendislik Yönetimi ve Liderlik

### Mühendislik Yöneticisi

#### İnsan Yönetimi

**Birebir görüşme hazırlığı** · `one-on-one-prep`

- Ne zaman: Ekip üyesiyle yapılacak birebir görüşme için önceki görüşmeden takipleri, çalışanın kendi gündemini, açık uçlu koçluk sorularını ve dikkat edilecek sinyalleri içeren odaklı bir plan hazırlar. Yaklaşan bir birebir görüşme olduğunda, düzenli birebirler yapılandırılmak istendiğinde veya zor bir konuşmaya (geri bildirim, iş yükü, kariyer, motivasyon) hazırlanırken kullanılır.
- Örnek istek: _"Yarın Ayşe ile birebirime hazırlan. Geçen sefer faturalama geçişinde tıkandığını ve tasarımda daha fazla sorumluluk almak istediğini söyledi."_
- İlgili: `one-on-one-notes`, `feedback-sbi`, `career-development-plan`, `goal-setting`, `conflict-resolution`
- Dosya: [skills/13-leadership/engineering-manager/people/one-on-one-prep/SKILL.tr.md](skills/13-leadership/engineering-manager/people/one-on-one-prep/SKILL.tr.md)

**Birebir görüşme notları** · `one-on-one-notes`

- Ne zaman: Birebir görüşmenin ham notlarını veya dökümünü; konuşulan konular, sorumlu ve tarihli taahhütler, verilen/alınan geri bildirim ve takip edilecek kariyer veya iyi oluş sinyallerinden oluşan kısa ve olgusal notlara dönüştürür. Bir ekip üyesi veya mentiyle yapılan birebirden sonra ya da ileride değerlendirme ve gelişim planlarını besleyecek sürekli bir birebir kaydı tutarken kullanılır.
- Örnek istek: _"Bugün Emre ile yaptığım birebirin notlarını düzenle ve ikimizin de neyi taahhüt ettiğini çıkar."_
- İlgili: `one-on-one-prep`, `action-item-extraction`, `performance-review`, `career-development-plan`, `meeting-notes`
- Dosya: [skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.tr.md](skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.tr.md)

**Performans değerlendirmesi yazma** · `performance-review`

- Ne zaman: Bir mühendis veya ekip üyesi için kanıta dayalı, yetkinliklerle uyumlu ve dengeli bir performans değerlendirmesi yazar; kalibre edilmiş puan gerekçesi, güçlü yönler, gelişim alanları ve sonraki dönem odağını içerir. Değerlendirme dönemi geldiğinde, birebir notları, ekip arkadaşı geri bildirimleri ve teslimat kanıtları yazılı bir değerlendirmeye dönüştürülürken veya taslak bir değerlendirme önyargı ve dayanaksız iddialar açısından kontrol edilirken kullanılır.
- Örnek istek: _"Bu notlardan, ekip arkadaşı geri bildirimlerinden ve hedeflerinden Can'ın yıllık değerlendirmesinin taslağını çıkar. Kariyer basamağımızdaki seviyesi Kıdemli Mühendis."_
- İlgili: `career-ladder`, `goal-setting`, `one-on-one-notes`, `career-development-plan`, `feedback-sbi`
- Dosya: [skills/13-leadership/engineering-manager/people/performance-review/SKILL.tr.md](skills/13-leadership/engineering-manager/people/performance-review/SKILL.tr.md)

**Bireysel hedef belirleme** · `goal-setting`

- Ne zaman: Bir mühendis veya ekip üyesi için ekip sonuçlarını kişinin gelişimiyle birleştiren, ölçüt, ara hedef ve gereken destekle birlikte 3-5 SMART bireysel hedef taslağı hazırlar. Değerlendirme döneminin başında, terfi veya rol değişikliğinden sonra ya da hedefler belirsiz, aktivite odaklı veya ekip öncelikleriyle bağlantısız olduğunda kullanılır.
- Örnek istek: _"Orta seviye backend mühendisi Deniz için ikinci yarı hedeflerini belirlememe yardım et. Ekip OKR'ı ödeme adımındaki gecikmeyi azaltmak, o da kıdemli seviyeye ilerlemek istiyor."_
- İlgili: `okr-definition`, `performance-review`, `career-development-plan`, `career-ladder`, `one-on-one-prep`
- Dosya: [skills/13-leadership/engineering-manager/people/goal-setting/SKILL.tr.md](skills/13-leadership/engineering-manager/people/goal-setting/SKILL.tr.md)

**Kariyer gelişim planı** · `career-development-plan`

- Ne zaman: Kişinin mevcut seviyesini hedef seviye veya kariyer yoluyla karşılaştıran, yetkinlik bazında kanıta dayalı eksikleri belirleyen ve gelişim aksiyonlarını, fırsatları, desteği ve kontrol noktalarını tanımlayan bir kariyer gelişim planı oluşturur. Biri terfi veya yol değişikliği (uzman ya da yönetici, uzmanlaşma) sorduğunda, bir değerlendirmeden sonra veya yöneticinin yapılandırılmış bir gelişim konuşmasına ihtiyacı olduğunda kullanılır.
- Örnek istek: _"18 ay içinde Staff seviyesine geçmek isteyen Kıdemli Mühendis Burak için gelişim planı oluştur."_
- İlgili: `career-ladder`, `goal-setting`, `performance-review`, `one-on-one-prep`, `onboarding-plan-30-60-90`
- Dosya: [skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.tr.md](skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.tr.md)

**Performans iyileştirme planı** · `underperformance-plan`

- Ne zaman: Belirli beklenti açıkları, ölçülebilir başarı kriterleri, sağlanan destek, ara değerlendirmeler ve açıkça belirtilmiş sonuçlarla adil ve kanıta dayalı bir performans iyileştirme planı (PIP) taslağı hazırlar; plan İK incelemesine hazır olur. Gayri resmi geri bildirimle çözülmeyen süregelen bir performans açığı olduğunda veya yönetici bir durumun resmi plana hazır olup olmadığını kontrol etmek istediğinde kullanılır.
- Örnek istek: _"Nisan'dan beri geri bildirime rağmen PR'ları sürekli incelemeden geçemeyen ve üç sprint taahhüdünü kaçıran bir geliştirici için 60 günlük iyileştirme planı taslağı hazırla."_
- İlgili: `performance-review`, `feedback-sbi`, `one-on-one-notes`, `bad-news-delivery`, `goal-setting`
- Dosya: [skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.tr.md](skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.tr.md)

**Takdir mesajı yazma** · `recognition-message`

- Ne zaman: Bir kişi veya ekip için somut davranışı, ortaya çıkardığı sonucu ve neden önemli olduğunu belirten, kanala (özel, ekip, şirket geneli) uygun, somut ve etki odaklı bir takdir mesajı yazar. Bir yönetici veya ekip arkadaşı birine emeği için teşekkür etmek, görünmeyen katkıları öne çıkarmak ya da bir lansmanı, olay müdahalesini veya mentorluk çabasını kutlamak istediğinde kullanılır.
- Örnek istek: _"Hafta sonunu veri taşıma geri alma işini çözmeye harcayan ve temiz bir postmortem yazan Selin için ekip kanalına teşekkür mesajı yaz."_
- İlgili: `feedback-sbi`, `announcement`, `tone-rewrite`, `performance-review`
- Dosya: [skills/13-leadership/engineering-manager/people/recognition-message/SKILL.tr.md](skills/13-leadership/engineering-manager/people/recognition-message/SKILL.tr.md)

#### İşe Alım

**İş ilanı yazma** · `job-description`

- Ne zaman: Bir yazılım rolü için rolün amacını, ilk yıl sonuçlarını, sorumlulukları, olmazsa olmaz ve tercih sebebi gereksinimleri, ekip bağlamını ve pratik bilgileri içeren kapsayıcı ve doğru bir iş ilanı yazar ve metni önyargılı veya dışlayıcı dil açısından kontrol eder. Yeni bir pozisyon açılırken, güncelliğini yitirmiş bir ilan yeniden yazılırken veya ilan yanlış adayları ya da çok az çeşitlilikte başvuru çektiğinde kullanılır.
- Örnek istek: _"İstanbul'daki platform ekibimiz için hibrit çalışan, Kafka ve Spark ile streaming pipeline'lar üzerinde çalışacak Kıdemli Veri Mühendisi ilanı yaz."_
- İlgili: `role-definition`, `interview-plan`, `career-ladder`, `onboarding-plan-30-60-90`, `tone-rewrite`
- Dosya: [skills/13-leadership/engineering-manager/hiring/job-description/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/job-description/SKILL.tr.md)

**Mülakat süreci tasarlama** · `interview-plan`

- Ne zaman: Bir rol için yapılandırılmış bir mülakat süreci tasarlar; her yetkinliği onu ölçen aşamalara eşler, aşama formatlarını, sürelerini, mülakatçı profillerini, puanlama ölçütlerini, aday iletişimini ve önyargıyı azaltan karar kurallarını belirler. Bir rol açılırken, mevcut süreç yavaş, tutarsız veya teklif kabul oranı düşük olduğunda ya da mülakatçılar aynı şeyleri ölçüp bazı alanları atladığında kullanılır.
- Örnek istek: _"Orta seviye frontend mühendisi için bir mülakat süreci tasarla. Adaydan en fazla dört saat alabiliriz."_
- İlgili: `job-description`, `technical-interview-questions`, `interview-scorecard`, `candidate-debrief`, `career-ladder`
- Dosya: [skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.tr.md)

**Teknik mülakat soruları** · `technical-interview-questions`

- Ne zaman: Tek bir mülakat aşaması için seviyeye göre ayarlanmış teknik sorular, takip soruları ve davranışa dayalı bir puanlama ölçeği hazırlar. Kodlama, sistem tasarımı, hata ayıklama veya alan bilgisi aşaması için soru seti gerektiğinde, soruları bir seviyeye kalibre ederken ya da ezber ve bulmaca sorularını işle ilgili sorularla değiştirirken kullanılır.
- Örnek istek: _"Kıdemli backend mühendisi için 60 dakikalık sistem tasarımı soru seti ve puanlama ölçeği hazırla. Olay güdümlü sipariş işleme üzerinde çalışıyoruz."_
- İlgili: `interview-plan`, `interview-scorecard`, `career-ladder`, `job-description`, `candidate-debrief`
- Dosya: [skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.tr.md)

**Mülakat değerlendirme formu** · `interview-scorecard`

- Ne zaman: Mülakatçının ham notlarını yetkinlik başına birebir kanıt, ölçeğe dayalı puan ve gerekçeli, bağımsız bir işe alım önerisi içeren bir değerlendirme formuna dönüştürür. Mülakattan hemen sonra, notların değerlendirme toplantısından önce yazılması gerektiğinde ya da bir formu eksik kanıt, önyargı veya olgu gibi sunulan izlenimler açısından kontrol ederken kullanılır.
- Örnek istek: _"B adayıyla yaptığım sistem tasarımı mülakatının notları burada. Kıdemli seviye ölçeğimize göre değerlendirme formuna dönüştür."_
- İlgili: `technical-interview-questions`, `candidate-debrief`, `interview-plan`, `bias-check`
- Dosya: [skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.tr.md)

**Aday değerlendirme toplantısı özeti** · `candidate-debrief`

- Ne zaman: Mülakat değerlendirme formlarını yetkinlik kapsama matrisi, çelişen sinyaller, çözülen ve çözülmeyen sorular ile seviyesiyle birlikte belgelenmiş bir işe alım kararı içeren yapılandırılmış bir toplantı özetine dönüştürür. Aday değerlendirme toplantısı hazırlanırken veya yapılırken, mülakatçılar anlaşamadığında ya da kararın kanıtı ve gerekçesiyle kayda geçmesi gerektiğinde kullanılır.
- Örnek istek: _"Bu dört değerlendirme formundan B adayının toplantı özetini çıkar ve kıdemli seviye için karar taslağı hazırla."_
- İlgili: `interview-scorecard`, `interview-plan`, `decision-log`, `onboarding-plan-30-60-90`, `bias-check`
- Dosya: [skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.tr.md)

**30-60-90 günlük oryantasyon planı** · `onboarding-plan-30-60-90`

- Ne zaman: Yeni bir çalışan için aşama başına sonuçlar, somut ilk görevler, tanışılacak kişiler, erişim ve öğrenme ara hedefleri ile görüşme noktaları içeren 30-60-90 günlük bir oryantasyon planı yazar. Biri yeni bir ekibe veya role katıldığında, mentor ya da yöneticinin yapılandırılmış bir uyum sürecine ihtiyacı olduğunda veya mevcut plan yalnızca okunacak doküman listesinden ibaretse kullanılır.
- Örnek istek: _"Gelecek ay ödeme ekibimize katılacak orta seviye bir backend mühendisi için 30-60-90 günlük plan yaz."_
- İlgili: `technical-onboarding`, `onboarding-guide`, `goal-setting`, `one-on-one-prep`, `job-description`
- Dosya: [skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.tr.md)

#### Ekip ve Organizasyon Tasarımı

**Ekip topolojisi tasarlama** · `team-topology`

- Ne zaman: Değer akışları, bilişsel yük ve bağımlılıklara dayanarak akışa hizalı, platform, destekleyici ve karmaşık alt sistem ekip türleri ile etkileşim modlarını kullanan bir ekip topolojisi tasarlar veya inceler. Ekipler kurulurken veya bölünürken, devirler ve ekipler arası bağımlılıklar teslimatı yavaşlattığında, bir platform ekibi düşünüldüğünde ya da ekip sınırları mimariyle örtüşmediğinde kullanılır.
- Örnek istek: _"5 ekibimiz ve 40 mühendisimiz var, her özellik 3 ekibe ihtiyaç duyuyor. E-ticaret platformumuz için bir ekip topolojisi öner."_
- İlgili: `bounded-context-map`, `service-decomposition`, `role-definition`, `cross-team-dependency-board`, `org-change-communication`
- Dosya: [skills/13-leadership/engineering-manager/team/team-topology/SKILL.tr.md](skills/13-leadership/engineering-manager/team/team-topology/SKILL.tr.md)

**Rol tanımlama** · `role-definition`

- Ne zaman: Bir rolü misyonu, sonuçları, sorumlulukları, karar yetkileri, diğer rollerle arayüzleri ve rolün hesap vermediği konularla birlikte tanımlar. Yeni bir rol (ör. staff mühendis, teknik lider, platform ürün sahibi) oluşturulurken, iki rol çakıştığında veya çatıştığında ya da karar yetkileri belirsiz olduğu için işler rollerin arasında kaldığında kullanılır.
- Örnek istek: _"Ekiplerimizdeki teknik lider rolünü tanımla; insanlar bu rolü mühendislik yöneticisi ve mimarla karıştırıyor."_
- İlgili: `raci-matrix`, `career-ladder`, `job-description`, `team-topology`, `governance-framework`
- Dosya: [skills/13-leadership/engineering-manager/team/role-definition/SKILL.tr.md](skills/13-leadership/engineering-manager/team/role-definition/SKILL.tr.md)

**Kariyer basamakları oluşturma** · `career-ladder`

- Ne zaman: Bir meslek ailesi için seviyeleri, seviye başına kapsam ve etkiyi, gözlemlenebilir örneklerle yetkinlik beklentilerini ve paralel bireysel katkıcı ile yönetim yollarını içeren kariyer basamakları oluşturur veya revize eder. Terfi, işe alım ve değerlendirmelerde tutarlı seviyelendirme gerektiğinde, seviyeler belirsiz veya ekipler arasında tutarsız olduğunda ya da staff/principal veya yönetim yolu eklenirken kullanılır.
- Örnek istek: _"Yazılım mühendislerimiz için junior'dan principal'a kariyer basamakları oluştur; takım liderinden direktöre ayrı bir yönetim yolu olsun."_
- İlgili: `role-definition`, `performance-review`, `career-development-plan`, `job-description`, `interview-plan`
- Dosya: [skills/13-leadership/engineering-manager/team/career-ladder/SKILL.tr.md](skills/13-leadership/engineering-manager/team/career-ladder/SKILL.tr.md)

**Mühendislik metrikleri incelemesi (DORA/SPACE)** · `engineering-metrics-review`

- Ne zaman: Mühendislik teslimat metriklerini DORA (dağıtım sıklığı, değişiklik teslim süresi, değişiklik hata oranı, geri yükleme süresi) ve SPACE boyutlarıyla inceler, eğilimleri bağlamıyla yorumlar, manipülasyonu ve veri kalitesi sorunlarını tespit eder ve iyileştirme deneyleri önerir. Bir ekip veya organizasyon için metrik incelemesi hazırlanırken, yönetim verimlilik rakamları istediğinde ya da metrikler bireyleri karşılaştırmak için yanlış kullanıldığında kullanılır.
- Örnek istek: _"Dört ekibin son iki çeyreğe ait DORA rakamları burada. İncele ve ekiplerle neleri konuşmam gerektiğini söyle."_
- İlgili: `cycle-time-analysis`, `team-health-check`, `kpi-definition`, `metric-definition`, `velocity-analysis`
- Dosya: [skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.tr.md](skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.tr.md)

### CTO / Başkan Yardımcısı / Direktör

#### Teknoloji Stratejisi

**Teknoloji stratejisi yazma** · `technology-strategy`

- Ne zaman: İş hedeflerine bağlı, açık ödünleşimler, yapılmayacaklar ve ilerleme ölçütleri içeren; teşhis, yol gösterici politika ve tutarlı aksiyonlar şeklinde yapılandırılmış bir teknoloji stratejisi yazar. Bir CTO veya teknoloji liderinin çok yıllı bir yöne ihtiyacı olduğunda, mevcut planlar seçim içermeyen dilek listeleri olduğunda ya da mimari, platform, yetenek ve yatırım kararlarını iş stratejisiyle hizalarken kullanılır.
- Örnek istek: _"Sigorta şirketimiz için 3 yıllık teknoloji stratejisi yaz; eski bir çekirdek sistemimiz, yavaş sürümlerimiz ve yeni bir dijital satış hedefimiz var."_
- İlgili: `target-state-architecture`, `architecture-principles`, `product-strategy-one-pager`, `tech-radar`, `budget-proposal`
- Dosya: [skills/13-leadership/executive/strategy/technology-strategy/SKILL.tr.md](skills/13-leadership/executive/strategy/technology-strategy/SKILL.tr.md)

**Çeyreklik planlama** · `quarterly-planning`

- Ne zaman: Bir teknoloji organizasyonu için çeyreklik planlama döngüsünü yürütür; stratejiyi ve talepleri kapasiteye dayalı taahhütlere, iddialı hedeflere (stretch) ve açık ödünleşimlere dönüştürür, bağımlılıkları ve riskleri görünür kılar. Bir CTO, başkan yardımcısı veya direktör ekiplerin gelecek çeyrekte neyi taahhüt edeceğine karar vermek zorunda olduğunda, talep kapasiteyi aştığında ya da önceki çeyrekler fazla taahhüt edilip eksik teslim edildiğinde kullanılır.
- Örnek istek: _"6 mühendislik ekibimiz için 3. çeyreği planlamama yardım et; işten 40 talep var, bir platform geçişi var ve kapasitenin %20'si zaten desteğe gidiyor."_
- İlgili: `technology-strategy`, `capacity-planning`, `okr-definition`, `portfolio-prioritization`, `cross-team-dependency-board`
- Dosya: [skills/13-leadership/executive/strategy/quarterly-planning/SKILL.tr.md](skills/13-leadership/executive/strategy/quarterly-planning/SKILL.tr.md)

**Bütçe teklifi yazma** · `budget-proposal`

- Ne zaman: Yatırım (değişim) ile işletim maliyetlerini ayıran, her kalemi bir iş sonucuna bağlayan, finanse edilmemenin maliyetini gösteren ve sonuçlarıyla birlikte finansman senaryoları sunan bir teknoloji bütçe teklifi yazar. Bir teknoloji yöneticisi yıllık veya proje bütçesi istemek ya da savunmak, kişi sayısı, lisans veya bulut harcamasını gerekçelendirmek ya da finans veya üst yönetime seçenek sunmak zorunda olduğunda kullanılır.
- Örnek istek: _"Gelecek yılın BT bütçe teklifini hazırla; bulut ve lisanslar yüzünden işletim maliyetleri %12 artıyor, ayrıca bir veri platformu ve 4 mühendis daha için finansman istiyoruz."_
- İlgili: `technology-strategy`, `cost-benefit-analysis`, `cloud-cost-estimate`, `budget-plan`, `board-update`
- Dosya: [skills/13-leadership/executive/strategy/budget-proposal/SKILL.tr.md](skills/13-leadership/executive/strategy/budget-proposal/SKILL.tr.md)

**Tedarikçi değerlendirme (RFP)** · `vendor-evaluation`

- Ne zaman: Bir teknoloji satın alımı için tedarikçileri veya ürünleri değerlendirir; gereksinimler ve eleme kriterlerinden, yanıtlar okunmadan önce sabitlenen ağırlıklı puanlama modeline, kanıta dayalı puanlamaya, toplam sahip olma maliyeti ve riske, oradan da belgelenmiş bir öneriye kadar ilerler. Bir yazılım ürünü, platform, bulut veya hizmet sağlayıcı seçilirken, RFP hazırlanır veya puanlanırken ya da tedarikçi seçiminin satın alma, denetim veya yönetim önünde savunulabilir olması gerektiğinde kullanılır.
- Örnek istek: _"API yönetim platformu RFP'mize 3 yanıt geldi; değerlendirme modelini kur ve bir tedarikçi öner."_
- İlgili: `decision-matrix`, `build-vs-buy`, `fit-gap-analysis`, `vendor-status-review`, `it-risk-assessment`
- Dosya: [skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.tr.md](skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.tr.md)

**Yönetim kurulu güncellemesi** · `board-update`

- Ne zaman: Teknoloji üzerine kısa bir üst yönetim veya yönetim kurulu güncellemesi yazar: son güncellemeden bu yana ne değişti, hedeflere göre birkaç sonuç metriği, eğilim ve azaltım planıyla en önemli riskler ve açık talepler ya da gereken kararlar. Bir CTO, CIO veya teknoloji direktörü yönetim kuruluna, icra kuruluna veya yatırımcılara rapor verirken ya da uzun bir teknik durumun teknik olmayan üst düzey okuyucular için yoğunlaştırılması gerektiğinde kullanılır.
- Örnek istek: _"Yönetim kurulu için çeyreklik teknoloji güncellememi yaz; bulut geçişi %60 tamamlandı, iki büyük kesinti yaşadık ve bir güvenlik yatırımı için onay almam gerekiyor."_
- İlgili: `executive-summary`, `status-update`, `technology-strategy`, `budget-proposal`, `risk-register`
- Dosya: [skills/13-leadership/executive/strategy/board-update/SKILL.tr.md](skills/13-leadership/executive/strategy/board-update/SKILL.tr.md)

**Organizasyon değişikliği iletişimi** · `org-change-communication`

- Ne zaman: Bir organizasyon değişikliğinin (yeniden yapılanma, yeni ekipler, raporlama hattı değişiklikleri, rol değişiklikleri, ofis veya süreç değişiklikleri) iletişimini planlar ve yazar: neden, ne değişiyor, ne değişmiyor, kim etkileniyor, zaman çizelgesi, destek ve nereye sorulacağı; etkilenenlerin önce ve özel olarak duyacağı şekilde sıralanır. Bir yönetici yeniden yapılanma veya ekip değişikliği duyururken, söylentilere yanıt vermek gerektiğinde ya da farklı kitleler için bir mesaj seti gerektiğinde kullanılır.
- Örnek istek: _"Gelecek ay mobil ve web ekiplerini ürün odaklı ekiplerde birleştiriyoruz; duyuruyu ve kimin neyi ne zaman duyacağını gösteren planı yaz."_
- İlgili: `team-topology`, `announcement`, `bad-news-delivery`, `faq-builder`, `communication-plan`
- Dosya: [skills/13-leadership/executive/strategy/org-change-communication/SKILL.tr.md](skills/13-leadership/executive/strategy/org-change-communication/SKILL.tr.md)

## Ön Satış ve Danışmanlık

### Ön Satış / Çözüm Danışmanı

#### Teklif Süreci

**RFP analizi** · `rfp-analysis`

- Ne zaman: Bir müşteri RFP/RFQ/ihale dokümanını teklif veren tarafından analiz eder; zorunlu ve puanlanan gereksinimleri, değerlendirme kriterlerini, ticari ve hukuki koşulları, tarihleri, örtük beklentileri ve riskleri çıkarır, bir uyum matrisi ve gerekçeli bir teklif ver/verme önerisi üretir. Yeni bir RFP veya ihale geldiğinde, ön satış eforu harcamadan önce ya da ekip teklif verip vermeyeceğine ve nasıl vereceğine karar vermek zorunda olduğunda kullanılır.
- Örnek istek: _"Core banking entegrasyon projesi için gelen bu 80 sayfalık RFP'yi analiz et ve teklif verip vermememiz gerektiğini söyle."_
- İlgili: `rfp-response`, `effort-estimate-for-bid`, `proposal-writing`, `requirements-gap-analysis`, `risk-register`
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.tr.md)

**RFP yanıtı yazma** · `rfp-response`

- Ne zaman: RFP/RFI/ihale gereksinimlerine uyumlu ve fayda odaklı yanıtlar yazar; her gereksinim için önce uyum düzeyini, ardından çözümün onu nasıl karşıladığını, kanıtı ve müşteriye faydayı, müşterinin formatında ve sınırlar içinde verir. Bir RFP soru listesine veya uyum tablosuna yanıt taslaklanırken ya da iyileştirilirken, yanıtlar fazla genel veya özellik odaklı kaldığında ya da kısmi uyumun dürüstçe belirtilmesi gerektiğinde kullanılır.
- Örnek istek: _"Bu RFP'deki R-10 ile R-25 arası gereksinimlere yanıtlarımızı yaz; ürünümüz çoğunu karşılıyor, ikisi özelleştirme gerektiriyor."_
- İlgili: `rfp-analysis`, `proposal-writing`, `effort-estimate-for-bid`, `statement-of-work`, `traceability-matrix`
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.tr.md)

**Teklif dokümanı yazma** · `proposal-writing`

- Ne zaman: Müşteri odaklı bir teklif dokümanı yazar; yönetici özeti, müşterinin durumu ve hedeflerine dair anlayış, önerilen çözüm, teslimat yaklaşımı, plan ve kilometre taşları, ekip, varsayımlar ve ticari özeti müşterinin kendi önceliklerine bağlanmış kazanma temaları ve kanıtlarla içerir. Bir müşteri talebine veya RFP'ye anlatı biçiminde teklifle yanıt verilirken, bir çözüm satın alma kararı için sunulacakken ya da taslak teklif genel bir yetkinlik broşürü gibi okunuyorsa kullanılır.
- Örnek istek: _"Bir lojistik firmasının eski sevkiyat sistemini modernize etmek için teklif dokümanı yaz; keşif notları ve efor tahminimiz ekte."_
- İlgili: `rfp-analysis`, `rfp-response`, `effort-estimate-for-bid`, `statement-of-work`, `executive-summary`
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.tr.md)

**Teklif için efor tahmini** · `effort-estimate-for-bid`

- Ne zaman: Bir teklif için efor tahmini oluşturur; iş kırılımından gelen aşağıdan-yukarı tahmini yukarıdan-aşağı veya benzetme kontrolüyle birleştirir, her varsayımı ve kapsam dışını açık yazar, riske dayalı yedek pay ekler ve eforu rol bazlı bir kadro profiline çevirir. Ön satış ekibinin sabit fiyatlı veya zaman-malzeme teklifi fiyatlaması gerektiğinde, bir RFP efor veya ekip büyüklüğü istediğinde ya da mevcut bir teklif tahmininin sağlamasının yapılması gerektiğinde kullanılır.
- Örnek istek: _"SSO, sipariş takibi ve ERP entegrasyonu olan bir B2B müşteri portalı teklifimiz için efor tahmini yap; müşteri sabit fiyat istiyor."_
- İlgili: `rfp-analysis`, `proposal-writing`, `statement-of-work`, `estimation-three-point`, `wbs`
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.tr.md)

**İş tanımı (SOW) yazma** · `statement-of-work`

- Ne zaman: Hedefleri, kapsam içi ve kapsam dışı işleri, kabul kriterleri ve prosedürüyle teslimatları, kilometre taşlarını, iki tarafın rol ve sorumluluklarını, varsayımları, bağımlılıkları, değişiklik kontrolünü ve ticari referansları sınanabilir ve yoruma kapalı bir dille tanımlayan bir iş tanımı (SOW) yazar. Bir teklif kabul edilip kapsamın sözleşmeyle sabitlenmesi gerektiğinde, bir çerçeve sözleşme altında proje veya faz için SOW gerektiğinde ya da mevcut bir SOW belirsizlik ve kapsam kayması riski açısından gözden geçirilecekse kullanılır.
- Örnek istek: _"Müşteri portalı projesinin 1. fazı için SOW taslağı hazırla: SSO, sipariş takibi ve ERP sipariş senkronizasyonu, sabit fiyat, 4 ay."_
- İlgili: `proposal-writing`, `effort-estimate-for-bid`, `scope-statement`, `acceptance-certificate`, `change-control`
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.tr.md)

#### Danışmanlık

**Müşteri keşif çalıştayı** · `discovery-workshop`

- Ne zaman: Erken aşamadaki bir müşteri işi için keşif çalıştayı tasarlar ve belgeler; hedefler, katılımcı karışımı, ön hazırlık, süreleri belli bir gündem, konu bazlı soru bankası, grup çalışması ve not-yaz-oyla (note-and-vote) yakınsama mekaniği ile yapılandırılmış bir çıktı (hedefler, sorunlar, mevcut yapı, gereksinim temaları, kısıtlar, riskler, sonraki adımlar) içerir. Yeni bir müşteri işi veya ön satış fırsatı başlarken, belirsiz bir müşteri ihtiyacı kapsama dönüştürülecekken ya da çalıştay notları bir keşif özetine çevrilecekken kullanılır.
- Örnek istek: _"E-ticaret platformunu \"modernize etmek\" isteyen ve ayrıntı paylaşmamış bir perakende müşterisiyle bir günlük keşif çalıştayı planla."_
- İlgili: `workshop-plan`, `facilitation-guide`, `current-state-assessment`, `stakeholder-map`, `interview-question-set`
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.tr.md)

**Müşteri mevcut durum değerlendirmesi** · `current-state-assessment`

- Ne zaman: Bir müşterinin mevcut durumunu iş süreci, uygulamalar, veri, teknoloji, organizasyon ve teslimat pratikleri boyutlarında değerlendirir; kanıta dayalı bulgular, belirtilmiş bir ölçekle boyut bazında olgunluk puanı, kök nedene bağlanmış sorunlar ve hızlı kazanımlar ile üst düzey yol haritası içeren önceliklendirilmiş öneriler üretir. Müşteri \"neredeyiz\" diye sorduğunda, bir dönüşüm veya modernizasyon teklifinden önce ya da keşif çıktıları, görüşmeler ve dokümanlar bir değerlendirme raporunda birleştirilecekken kullanılır.
- Örnek istek: _"Bu görüşme notları ve sistem envanterinden orta ölçekli bir sigortacının hasar platformunun mevcut durumunu değerlendir ve nereden başlanması gerektiğini öner."_
- İlgili: `discovery-workshop`, `fit-gap-analysis`, `modernization-assessment`, `capability-map`, `client-steering-report`
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.tr.md)

**Fit-gap analizi** · `fit-gap-analysis`

- Ne zaman: Gereksinimleri bir paketin, platformun veya referans sürecin standart yetenekleriyle karşılaştıran bir fit-gap analizi yapar; her gereksinimi uygun (fit), konfigürasyonla uygun, boşluk (gap) veya uygulanamaz olarak sınıflandırır, her boşluk için efor bandı ve riskiyle bir çözüm önerir (süreç değişikliği, konfigürasyon, genişletme, entegrasyon, üçüncü taraf, geçici çözüm, erteleme) ve uyum oranını ve gereken kararları özetler. Bir ERP, CRM, SaaS veya başka bir paket çözüm değerlendirilirken ya da uygulanırken, müşteri paketin ne kadar özelleştirme gerektireceğini sorduğunda veya gereksinimler standart bir sürece hizalanacakken kullanılır.
- Örnek istek: _"Bu 40 siparişten tahsilata (order-to-cash) gereksinimini standart bir bulut ERP satış modülüyle karşılaştıran fit-gap analizi yap ve özelleştirmenin kaçınılmaz olduğu yerleri söyle."_
- İlgili: `requirements-gap-analysis`, `build-vs-buy`, `vendor-evaluation`, `current-state-assessment`, `effort-estimate-for-bid`
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.tr.md)

**Müşteri yönlendirme raporu** · `client-steering-report`

- Ne zaman: Bir danışmanlık veya teslimat işi için müşteriye yönelik yönlendirme komitesi raporu yazar; açık bir puanlama kuralıyla plana göre genel durumu, kilometre taşlarındaki ilerlemeyi, üzerinde uzlaşılan sonuçlara göre sağlanan değeri, bütçe ve efor tüketimini, öne çıkan risk ve sorunları, değişiklik taleplerini ve müşteri yönlendirme grubunun alması gereken kararları kapsar. Bir müşteri yönlendirme komitesi veya yönetici incelemesi öncesinde, dönemsel bir iş raporu zamanı geldiğinde ya da teslimat verileri karar odaklı bir müşteri güncellemesine çevrilecekken kullanılır.
- Örnek istek: _"Müşterimizin CRM geçişi için aylık yönlendirme raporunu yaz: 2. faz iki hafta geride, bütçe yolunda, veri taşıma kapsamı için karar gerekiyor."_
- İlgili: `steering-committee-pack`, `project-status-report`, `benefits-realization`, `raid-log`, `bad-news-delivery`
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.tr.md)
