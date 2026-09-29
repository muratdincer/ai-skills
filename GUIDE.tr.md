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

- Ne zaman: Hedefin asenkron karşılanıp karşılanamayacağını değerlendirir, alternatif önerir
- Dosya: [skills/00-shared/meetings/before/meeting-necessity-check/SKILL.tr.md](skills/00-shared/meetings/before/meeting-necessity-check/SKILL.tr.md)

#### Toplantı Sırasında

**Yapılandırılmış toplantı notu tutma** · `meeting-notes`

- Ne zaman: Ham notu veya dökümü konu bazlı yapılandırılmış notlara çevirir
- Dosya: [skills/00-shared/meetings/during/meeting-notes/SKILL.tr.md](skills/00-shared/meetings/during/meeting-notes/SKILL.tr.md)

**Toplantı dökümünü temizleme** · `transcript-cleanup`

- Ne zaman: Dolgu sözcüklerini ayıklar, konuşmacıları düzeltir, anlamı korur
- Dosya: [skills/00-shared/meetings/during/transcript-cleanup/SKILL.tr.md](skills/00-shared/meetings/during/transcript-cleanup/SKILL.tr.md)

**Toplantı kolaylaştırma** · `facilitation-guide`

- Ne zaman: Süre planı, yönlendirici sorular ve çatışma yönetimi içeren kolaylaştırıcı metni verir
- Dosya: [skills/00-shared/meetings/during/facilitation-guide/SKILL.tr.md](skills/00-shared/meetings/during/facilitation-guide/SKILL.tr.md)

#### Toplantı Sonrası

**Toplantı özeti çıkarma** · `meeting-summary`

- Ne zaman: Sonuçların, kararların ve açık noktaların kısa yönetici özetini çıkarır
- Dosya: [skills/00-shared/meetings/after/meeting-summary/SKILL.tr.md](skills/00-shared/meetings/after/meeting-summary/SKILL.tr.md)

**Resmi toplantı tutanağı yazma** · `meeting-minutes`

- Ne zaman: Katılımcı, gündem maddeleri ve kararlarla resmi tutanak oluşturur
- Dosya: [skills/00-shared/meetings/after/meeting-minutes/SKILL.tr.md](skills/00-shared/meetings/after/meeting-minutes/SKILL.tr.md)

**Aksiyon maddelerini çıkarma** · `action-item-extraction`

- Ne zaman: Tüm taahhütleri bulur, sorumlu, tarih ve durum atar
- Dosya: [skills/00-shared/meetings/after/action-item-extraction/SKILL.tr.md](skills/00-shared/meetings/after/action-item-extraction/SKILL.tr.md)

**Karar kaydı tutma** · `decision-log`

- Ne zaman: Kararları bağlamı, alternatifleri ve gerekçesiyle kaydeder
- Dosya: [skills/00-shared/meetings/after/decision-log/SKILL.tr.md](skills/00-shared/meetings/after/decision-log/SKILL.tr.md)

**Toplantı sonrası takip mesajı** · `meeting-follow-up`

- Ne zaman: Kararlar, aksiyonlar ve sonraki toplantıyla özet mesajı yazar
- Dosya: [skills/00-shared/meetings/after/meeting-follow-up/SKILL.tr.md](skills/00-shared/meetings/after/meeting-follow-up/SKILL.tr.md)

**Açık soruları takip etme** · `open-questions-tracker`

- Ne zaman: Çözülmemiş soruları sorumlu ve gereken tarihle listeler
- Dosya: [skills/00-shared/meetings/after/open-questions-tracker/SKILL.tr.md](skills/00-shared/meetings/after/open-questions-tracker/SKILL.tr.md)

### İletişim

#### Yazılı İletişim

**Durum güncellemesi yazma** · `status-update`

- Ne zaman: İlerlemeyi, riskleri ve sonraki adımları RAG durumuyla özetler
- Dosya: [skills/00-shared/communication/written/status-update/SKILL.tr.md](skills/00-shared/communication/written/status-update/SKILL.tr.md)

**Yönetici özeti yazma** · `executive-summary`

- Ne zaman: Herhangi bir içeriği karar odaklı tek sayfalık özete indirger
- Dosya: [skills/00-shared/communication/written/executive-summary/SKILL.tr.md](skills/00-shared/communication/written/executive-summary/SKILL.tr.md)

**Paydaş e-postası yazma** · `stakeholder-email`

- Ne zaman: Amacı önde olan, hedef kitleye ve tona uygun e-posta yazar
- Dosya: [skills/00-shared/communication/written/stakeholder-email/SKILL.tr.md](skills/00-shared/communication/written/stakeholder-email/SKILL.tr.md)

**Eskalasyon mesajı yazma** · `escalation-message`

- Ne zaman: Olgu, etki, seçenekler ve net bir taleple eskalasyon yazar
- Dosya: [skills/00-shared/communication/written/escalation-message/SKILL.tr.md](skills/00-shared/communication/written/escalation-message/SKILL.tr.md)

**Duyuru yazma** · `announcement`

- Ne zaman: Değişiklik, sürüm veya kararı ne/neden/etki/ne zaman yapısıyla duyurur
- Dosya: [skills/00-shared/communication/written/announcement/SKILL.tr.md](skills/00-shared/communication/written/announcement/SKILL.tr.md)

**Ton düzenleme** · `tone-rewrite`

- Ne zaman: Mesajı daha net, yumuşak, kararlı veya resmi olacak şekilde yeniden yazar
- Dosya: [skills/00-shared/communication/written/tone-rewrite/SKILL.tr.md](skills/00-shared/communication/written/tone-rewrite/SKILL.tr.md)

**Kötü haber iletme** · `bad-news-delivery`

- Ne zaman: Gecikme, iptal veya başarısızlığı şeffaf biçimde iletir
- Dosya: [skills/00-shared/communication/written/bad-news-delivery/SKILL.tr.md](skills/00-shared/communication/written/bad-news-delivery/SKILL.tr.md)

#### Sunum ve Sözlü

**Sunum iskeleti çıkarma** · `presentation-outline`

- Ne zaman: Hedef kitleye göre akış ve slayt slayt iskelet çıkarır
- Dosya: [skills/00-shared/communication/verbal/presentation-outline/SKILL.tr.md](skills/00-shared/communication/verbal/presentation-outline/SKILL.tr.md)

**Demo senaryosu yazma** · `demo-script`

- Ne zaman: Akış, anlatım noktaları ve yedek planla ürün/özellik demosu senaryosu yazar
- Dosya: [skills/00-shared/communication/verbal/demo-script/SKILL.tr.md](skills/00-shared/communication/verbal/demo-script/SKILL.tr.md)

**Asansör konuşması hazırlama** · `elevator-pitch`

- Ne zaman: Bir fikri belirli bir kitleye 30-60 saniyede anlatır
- Dosya: [skills/00-shared/communication/verbal/elevator-pitch/SKILL.tr.md](skills/00-shared/communication/verbal/elevator-pitch/SKILL.tr.md)

#### Kişilerarası

**Geri bildirim verme (SBI)** · `feedback-sbi`

- Ne zaman: Geri bildirimi Durum-Davranış-Etki kalıbında, yapıcı ve somut kurgular
- Dosya: [skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.tr.md](skills/00-shared/communication/interpersonal/feedback-sbi/SKILL.tr.md)

**Çatışma çözme** · `conflict-resolution`

- Ne zaman: Pozisyonları ve çıkarları haritalar, arabulucu bir çözüm önerir
- Dosya: [skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.tr.md](skills/00-shared/communication/interpersonal/conflict-resolution/SKILL.tr.md)

**Müzakereye hazırlanma** · `negotiation-prep`

- Ne zaman: BATNA, çıkarlar, tavizler ve açılış pozisyonunu belirler
- Dosya: [skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.tr.md](skills/00-shared/communication/interpersonal/negotiation-prep/SKILL.tr.md)

### Dokümantasyon

#### Yazım

**Doküman iskeleti çıkarma** · `document-outline`

- Ne zaman: Amacından yola çıkarak her tür doküman için yapı önerir
- Dosya: [skills/00-shared/documentation/authoring/document-outline/SKILL.tr.md](skills/00-shared/documentation/authoring/document-outline/SKILL.tr.md)

**Sözlük oluşturma** · `glossary-builder`

- Ne zaman: Alan terimlerini çıkarır ve belirsizlik içermeyen tanımlar yazar
- Dosya: [skills/00-shared/documentation/authoring/glossary-builder/SKILL.tr.md](skills/00-shared/documentation/authoring/glossary-builder/SKILL.tr.md)

**SSS oluşturma** · `faq-builder`

- Ne zaman: Kaynak materyalden olası soru ve cevapları üretir
- Dosya: [skills/00-shared/documentation/authoring/faq-builder/SKILL.tr.md](skills/00-shared/documentation/authoring/faq-builder/SKILL.tr.md)

**Kod olarak diyagram üretme** · `diagram-as-code`

- Ne zaman: Bir tarifi Mermaid/PlantUML diyagramına çevirir
- Dosya: [skills/00-shared/documentation/authoring/diagram-as-code/SKILL.tr.md](skills/00-shared/documentation/authoring/diagram-as-code/SKILL.tr.md)

**Teknik çeviri** · `technical-translation`

- Ne zaman: Teknik metni terminolojiyi koruyarak EN<->TR çevirir
- Dosya: [skills/00-shared/documentation/authoring/technical-translation/SKILL.tr.md](skills/00-shared/documentation/authoring/technical-translation/SKILL.tr.md)

#### Gözden Geçirme

**Doküman gözden geçirme** · `document-review`

- Ne zaman: Açıklık, bütünlük, tutarlılık ve hedef kitleye uygunluk açısından inceler
- Dosya: [skills/00-shared/documentation/review/document-review/SKILL.tr.md](skills/00-shared/documentation/review/document-review/SKILL.tr.md)

**Dokümanı sadeleştirme** · `document-simplify`

- Ne zaman: Anlamı kaybetmeden uzunluğu ve jargonu azaltır
- Dosya: [skills/00-shared/documentation/review/document-simplify/SKILL.tr.md](skills/00-shared/documentation/review/document-simplify/SKILL.tr.md)

**Doküman değişikliklerini özetleme** · `doc-diff-summary`

- Ne zaman: İki sürümü karşılaştırır, neyin değiştiğini ve önemini açıklar
- Dosya: [skills/00-shared/documentation/review/doc-diff-summary/SKILL.tr.md](skills/00-shared/documentation/review/doc-diff-summary/SKILL.tr.md)

### Problem Çözme ve Karar Araçları

#### Problem Tanımlama

**Problem tanımı yazma** · `problem-statement`

- Ne zaman: Kimin, ne zaman, hangi etkiyle hangi problemi yaşadığını tanımlar
- Dosya: [skills/00-shared/thinking-tools/problem/problem-statement/SKILL.tr.md](skills/00-shared/thinking-tools/problem/problem-statement/SKILL.tr.md)

**5 Neden analizi** · `five-whys`

- Ne zaman: Belirtiden kök nedene iner
- Dosya: [skills/00-shared/thinking-tools/problem/five-whys/SKILL.tr.md](skills/00-shared/thinking-tools/problem/five-whys/SKILL.tr.md)

**Balık kılçığı analizi** · `fishbone-analysis`

- Ne zaman: Olası nedenleri kategorize eder (Ishikawa)
- Dosya: [skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.tr.md](skills/00-shared/thinking-tools/problem/fishbone-analysis/SKILL.tr.md)

**Varsayım haritalama** · `assumption-mapping`

- Ne zaman: Varsayımları listeler, risk ve kanıta göre sıralar
- Dosya: [skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.tr.md](skills/00-shared/thinking-tools/problem/assumption-mapping/SKILL.tr.md)

#### Karar Verme

**Ağırlıklı karar matrisi** · `decision-matrix`

- Ne zaman: Seçenekleri ağırlıklı kriterlere göre puanlar
- Dosya: [skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.tr.md](skills/00-shared/thinking-tools/decision/decision-matrix/SKILL.tr.md)

**Artı-eksi analizi** · `pros-cons`

- Ne zaman: Önerisiyle birlikte dengeli artı/eksi listesi çıkarır
- Dosya: [skills/00-shared/thinking-tools/decision/pros-cons/SKILL.tr.md](skills/00-shared/thinking-tools/decision/pros-cons/SKILL.tr.md)

**SWOT analizi** · `swot-analysis`

- Ne zaman: Güçlü/zayıf yönler, fırsatlar ve tehditleri aksiyonlarıyla çıkarır
- Dosya: [skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.tr.md](skills/00-shared/thinking-tools/decision/swot-analysis/SKILL.tr.md)

**Ödünleşim analizi** · `trade-off-analysis`

- Ne zaman: Her seçenekte neyin kazanılıp neyin kaybedildiğini açıkça ortaya koyar
- Dosya: [skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.tr.md](skills/00-shared/thinking-tools/decision/trade-off-analysis/SKILL.tr.md)

**Pre-mortem** · `pre-mortem`

- Ne zaman: Başarısızlığı varsayıp nasıl olduğunu listeleyerek riskleri erken bulur
- Dosya: [skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.tr.md](skills/00-shared/thinking-tools/decision/pre-mortem/SKILL.tr.md)

### Bilgi Yönetimi

#### Kayıt ve Aktarım

**Çıkarılan dersleri kaydetme** · `lessons-learned`

- Ne zaman: Neyin işe yarayıp neyin yaramadığını ve korunacak/değişecek aksiyonları kaydeder
- Dosya: [skills/00-shared/knowledge/capture/lessons-learned/SKILL.tr.md](skills/00-shared/knowledge/capture/lessons-learned/SKILL.tr.md)

**Devir-teslim dokümanı yazma** · `handover-document`

- Ne zaman: Sahipliği devreder: bağlam, durum, iletişim, riskler, açık işler
- Dosya: [skills/00-shared/knowledge/capture/handover-document/SKILL.tr.md](skills/00-shared/knowledge/capture/handover-document/SKILL.tr.md)

**Bilgi bankası makalesi yazma** · `kb-article`

- Ne zaman: Aranabilir bir nasıl-yapılır veya açıklama makalesi yazar
- Dosya: [skills/00-shared/knowledge/capture/kb-article/SKILL.tr.md](skills/00-shared/knowledge/capture/kb-article/SKILL.tr.md)

**Oryantasyon rehberi yazma** · `onboarding-guide`

- Ne zaman: Yeni geleni bağlam, araçlar, kişiler ve ilk görevler boyunca yönlendirir
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

- Ne zaman: Talep sahibine sorulacak soruları gruplu ve önceliklendirilmiş şekilde üretir
- Dosya: [skills/01-business-analysis/business-analyst/intake/request-clarification-questions/SKILL.tr.md](skills/01-business-analysis/business-analyst/intake/request-clarification-questions/SKILL.tr.md)

**Gelen talepleri sınıflandırma** · `request-triage`

- Ne zaman: Talepleri tür, aciliyet ve değere göre sınıflandırır ve yönlendirir
- Dosya: [skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.tr.md](skills/01-business-analysis/business-analyst/intake/request-triage/SKILL.tr.md)

**Talep eksiklik kontrolü** · `request-completeness-check`

- Ne zaman: İş başlamadan önce talepteki eksik veya belirsiz noktaları bulur
- Dosya: [skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.tr.md](skills/01-business-analysis/business-analyst/intake/request-completeness-check/SKILL.tr.md)

#### Paydaş Analizi

**Paydaşları belirleme** · `stakeholder-identification`

- Ne zaman: Etkilenen, etkileyen veya karar veren herkesi listeler
- Dosya: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.tr.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-identification/SKILL.tr.md)

**Güç/ilgi paydaş haritası** · `stakeholder-map`

- Ne zaman: Paydaşları güç/ilgi matrisine yerleştirir, iletişim stratejisi belirler
- Dosya: [skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.tr.md](skills/01-business-analysis/business-analyst/stakeholders/stakeholder-map/SKILL.tr.md)

**RACI matrisi** · `raci-matrix`

- Ne zaman: Her aktivite için Sorumlu/Hesap Veren/Danışılan/Bilgilendirilen atar
- Dosya: [skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.tr.md](skills/01-business-analysis/business-analyst/stakeholders/raci-matrix/SKILL.tr.md)

#### Gereksinim Toplama

**Görüşme soruları hazırlama** · `interview-question-set`

- Ne zaman: Paydaş tipine göre açık uçlu, derinleştirici ve doğrulayıcı sorular hazırlar
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/interview-question-set/SKILL.tr.md)

**Görüşme notlarını analiz etme** · `interview-notes-analysis`

- Ne zaman: Görüşme notlarından ihtiyaç, sorun, kural ve çelişkileri çıkarır
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/interview-notes-analysis/SKILL.tr.md)

**Gereksinim çalıştayı planlama** · `workshop-plan`

- Ne zaman: Çalıştayın hedeflerini, aktivitelerini, zamanlamasını ve çıktılarını tasarlar
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/workshop-plan/SKILL.tr.md)

**Anket tasarlama** · `questionnaire-design`

- Ne zaman: Gereksinimleri geniş kitleden toplamak için yanlılıksız anket hazırlar
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/questionnaire-design/SKILL.tr.md)

**Mevcut dokümanlardan gereksinim çıkarma** · `document-analysis`

- Ne zaman: Şartname, kılavuz ve mevzuattan gereksinim çıkarır
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/document-analysis/SKILL.tr.md)

**Gözlem notlarını yapılandırma** · `observation-notes`

- Ne zaman: Gözlem notlarını görev, sorun ve geçici çözümlere çevirir
- Dosya: [skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.tr.md](skills/01-business-analysis/business-analyst/elicitation/observation-notes/SKILL.tr.md)

#### Gereksinim Dokümantasyonu

**İş Gereksinimleri Dokümanı (BRD) yazma** · `brd-writing`

- Ne zaman: İş hedefleri, kapsam, paydaşlar ve üst düzey gereksinimleri belgeler
- Dosya: [skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/brd-writing/SKILL.tr.md)

**Fonksiyonel Gereksinim Dokümanı (FRD) yazma** · `frd-writing`

- Ne zaman: Sistem davranışını, girdileri, çıktıları ve kuralları tanımlar
- Dosya: [skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/frd-writing/SKILL.tr.md)

**Kullanıcı hikayesi yazma** · `user-story`

- Ne zaman: Bağlamıyla birlikte "... olarak ... istiyorum ki ..." hikayeleri yazar
- Dosya: [skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/user-story/SKILL.tr.md)

**Kabul kriteri yazma** · `acceptance-criteria`

- Ne zaman: Given/When/Then veya kural biçiminde test edilebilir kriterler yazar
- Dosya: [skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/acceptance-criteria/SKILL.tr.md)

**Kullanım senaryosu (use case) yazma** · `use-case-spec`

- Ne zaman: Aktörler, ön koşullar, ana/alternatif/istisna akışları
- Dosya: [skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/use-case-spec/SKILL.tr.md)

**Fonksiyonel olmayan gereksinimleri tanımlama** · `nfr-specification`

- Ne zaman: Performans, güvenlik, erişilebilirlik vb. gereksinimleri ölçülebilir kılar
- Dosya: [skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/nfr-specification/SKILL.tr.md)

**İş kuralları kataloğu** · `business-rules-catalog`

- Ne zaman: İş kurallarını ID ve kaynaklarıyla çıkarıp standartlaştırır
- Dosya: [skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/business-rules-catalog/SKILL.tr.md)

**Veri gereksinimlerini tanımlama** · `data-requirements`

- Ne zaman: Varlıklar, nitelikler, doğrulamalar, sahiplik ve saklama süresi
- Dosya: [skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/data-requirements/SKILL.tr.md)

**Rapor gereksinimi tanımlama** · `report-requirements`

- Ne zaman: Raporun amacını, alanlarını, filtrelerini, hesaplamalarını ve kitlesini tanımlar
- Dosya: [skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/report-requirements/SKILL.tr.md)

**Ekran gereksinimi tanımlama** · `screen-requirements`

- Ne zaman: Ekran bazında alanları, doğrulamaları, durumları ve davranışları tarif eder
- Dosya: [skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/screen-requirements/SKILL.tr.md)

**Entegrasyon gereksinimi tanımlama** · `integration-requirements`

- Ne zaman: Sistemleri, aktarılan veriyi, sıklığı, hataları ve SLA'ları tanımlar
- Dosya: [skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.tr.md](skills/01-business-analysis/business-analyst/documentation/integration-requirements/SKILL.tr.md)

#### Gereksinim Kalitesi

**Gereksinimlerde eksik bulma** · `requirements-gap-analysis`

- Ne zaman: Eksik akışları, rolleri, uç durumları, hataları ve NFR'leri tespit eder
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-gap-analysis/SKILL.tr.md)

**Belirsiz gereksinim tespiti** · `ambiguity-detection`

- Ne zaman: Muğlak ifadeleri, tanımsız terimleri ve test edilemez cümleleri işaretler
- Dosya: [skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/ambiguity-detection/SKILL.tr.md)

**Gereksinim tutarlılık kontrolü** · `requirements-consistency-check`

- Ne zaman: Gereksinimler arasındaki çelişki ve tekrarları bulur
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-consistency-check/SKILL.tr.md)

**INVEST kontrolü** · `invest-check`

- Ne zaman: Hikayeleri Bağımsız, Tartışılabilir, Değerli, Tahmin Edilebilir, Küçük, Test Edilebilir kriterlerine göre değerlendirir
- Dosya: [skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/invest-check/SKILL.tr.md)

**İzlenebilirlik matrisi** · `traceability-matrix`

- Ne zaman: Gereksinimleri hedeflere, tasarıma, testlere ve sürümlere bağlar
- Dosya: [skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/traceability-matrix/SKILL.tr.md)

**Gereksinim önceliklendirme** · `requirements-prioritization`

- Ne zaman: MoSCoW, Kano veya değer/efor uygular ve sıralamayı gerekçelendirir
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-prioritization/SKILL.tr.md)

**Gereksinim gözden geçirme** · `requirements-review-checklist`

- Ne zaman: Onay öncesi kontrol listesine dayalı inceleme yapar
- Dosya: [skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.tr.md](skills/01-business-analysis/business-analyst/quality/requirements-review-checklist/SKILL.tr.md)

#### Süreç Analizi

**Mevcut süreci (as-is) belgeleme** · `as-is-process`

- Ne zaman: Mevcut adımları, aktörleri, sistemleri, sorunları ve süreleri kaydeder
- Dosya: [skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/as-is-process/SKILL.tr.md)

**Hedef süreci (to-be) tasarlama** · `to-be-process`

- Ne zaman: İyileştirilmiş süreci önerir, değişiklikleri vurgular
- Dosya: [skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/to-be-process/SKILL.tr.md)

**BPMN süreç modeli** · `bpmn-model`

- Ne zaman: BPMN öğelerini (olay, geçit, kulvar) metin/diyagram kodu olarak üretir
- Dosya: [skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/bpmn-model/SKILL.tr.md)

**As-is/to-be fark analizi** · `process-gap-analysis`

- Ne zaman: İnsan, süreç ve teknolojide farkları ve gereken değişiklikleri listeler
- Dosya: [skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/process-gap-analysis/SKILL.tr.md)

**Değer akışı haritalama** · `value-stream-map`

- Ne zaman: Değer katan adımları israftan ayırır, bekleme/işlem sürelerini çıkarır
- Dosya: [skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.tr.md](skills/01-business-analysis/business-analyst/process/value-stream-map/SKILL.tr.md)

#### Çözüm Değerlendirme

**Fizibilite değerlendirmesi** · `feasibility-study`

- Ne zaman: Teknik, operasyonel, ekonomik ve zaman fizibilitesini değerlendirir
- Dosya: [skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/feasibility-study/SKILL.tr.md)

**Maliyet-fayda analizi** · `cost-benefit-analysis`

- Ne zaman: Maliyet, fayda, ROI ve geri dönüş süresini sayısallaştırır
- Dosya: [skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/cost-benefit-analysis/SKILL.tr.md)

**Etki analizi** · `impact-analysis`

- Ne zaman: Etkilenen süreç, sistem, veri, kullanıcı ve raporları bulur
- Dosya: [skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/impact-analysis/SKILL.tr.md)

**Değişiklik talebi analizi** · `change-request-analysis`

- Ne zaman: Kapsam, efor ve riski değerlendirir; kabul/erteleme/ret önerir
- Dosya: [skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/change-request-analysis/SKILL.tr.md)

**Gereksinim onayı hazırlama** · `requirements-sign-off`

- Ne zaman: Temel sürümü, açık konuları ve gereken onayları özetler
- Dosya: [skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.tr.md](skills/01-business-analysis/business-analyst/solution/requirements-sign-off/SKILL.tr.md)

### Sistem Analisti

#### Sistem Tanımı

**Yazılım Gereksinim Şartnamesi (SRS) yazma** · `srs-writing`

- Ne zaman: ISO/IEC/IEEE 29148 uyumlu SRS hazırlar
- Dosya: [skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/srs-writing/SKILL.tr.md)

**Durum modeli çıkarma** · `state-model`

- Ne zaman: Bir varlığın durumlarını, geçişlerini, tetikleyicilerini ve koşullarını tanımlar
- Dosya: [skills/01-business-analysis/system-analyst/specification/state-model/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/state-model/SKILL.tr.md)

**Sistem etkileşim akışı** · `sequence-flow`

- Ne zaman: Sistemler arası bir senaryo için sıralama diyagramı üretir
- Dosya: [skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/sequence-flow/SKILL.tr.md)

**Sistemler arası alan eşleme** · `field-mapping`

- Ne zaman: Dönüşüm ve kurallarıyla kaynak-hedef eşlemesi yapar
- Dosya: [skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/field-mapping/SKILL.tr.md)

**Hata senaryoları kataloğu** · `error-scenario-catalog`

- Ne zaman: Hata durumlarını, mesajları ve beklenen sistem davranışını listeler
- Dosya: [skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.tr.md](skills/01-business-analysis/system-analyst/specification/error-scenario-catalog/SKILL.tr.md)

## Ürün Yönetimi

### Ürün Yöneticisi

#### Ürün Stratejisi

**Ürün vizyonu yazma** · `product-vision`

- Ne zaman: Vizyon cümlesi ve vizyon panosu (hedef kitle, ihtiyaç, ürün, hedefler)
- Dosya: [skills/02-product/product-manager/strategy/product-vision/SKILL.tr.md](skills/02-product/product-manager/strategy/product-vision/SKILL.tr.md)

**Tek sayfalık ürün stratejisi** · `product-strategy-one-pager`

- Ne zaman: Nerede oynanacağı, nasıl kazanılacağı, bahisler ve hedef dışı olanlar
- Dosya: [skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.tr.md](skills/02-product/product-manager/strategy/product-strategy-one-pager/SKILL.tr.md)

**OKR tanımlama** · `okr-definition`

- Ne zaman: Sonuç odaklı hedefler ve ölçülebilir anahtar sonuçlar yazar
- Dosya: [skills/02-product/product-manager/strategy/okr-definition/SKILL.tr.md](skills/02-product/product-manager/strategy/okr-definition/SKILL.tr.md)

**Pazar analizi** · `market-analysis`

- Ne zaman: TAM/SAM/SOM, segmentler, trendler ve itici güçler
- Dosya: [skills/02-product/product-manager/strategy/market-analysis/SKILL.tr.md](skills/02-product/product-manager/strategy/market-analysis/SKILL.tr.md)

**Rakip analizi** · `competitor-analysis`

- Ne zaman: Özellik, fiyat ve konumlandırma karşılaştırması ile boşluklar
- Dosya: [skills/02-product/product-manager/strategy/competitor-analysis/SKILL.tr.md](skills/02-product/product-manager/strategy/competitor-analysis/SKILL.tr.md)

**İş modeli / lean kanvas** · `business-model-canvas`

- Ne zaman: Bir fikir için İş Modeli veya Lean Kanvas'ı doldurur
- Dosya: [skills/02-product/product-manager/strategy/business-model-canvas/SKILL.tr.md](skills/02-product/product-manager/strategy/business-model-canvas/SKILL.tr.md)

**Fiyatlandırma analizi** · `pricing-analysis`

- Ne zaman: Fiyat modellerini ve ödeme isteği sinyallerini karşılaştırır
- Dosya: [skills/02-product/product-manager/strategy/pricing-analysis/SKILL.tr.md](skills/02-product/product-manager/strategy/pricing-analysis/SKILL.tr.md)

#### Keşif

**Persona oluşturma** · `persona`

- Ne zaman: Hedefleri, sorunları ve davranışlarıyla kanıta dayalı persona oluşturur
- Dosya: [skills/02-product/product-manager/discovery/persona/SKILL.tr.md](skills/02-product/product-manager/discovery/persona/SKILL.tr.md)

**Yapılacak İşler (JTBD)** · `jobs-to-be-done`

- Ne zaman: İş ifadelerini ve istenen sonuçları yazar
- Dosya: [skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.tr.md](skills/02-product/product-manager/discovery/jobs-to-be-done/SKILL.tr.md)

**Müşteri yolculuğu haritası** · `customer-journey-map`

- Ne zaman: Aşamalar, eylemler, düşünceler, duygular, temas noktaları, sorunlar
- Dosya: [skills/02-product/product-manager/discovery/customer-journey-map/SKILL.tr.md](skills/02-product/product-manager/discovery/customer-journey-map/SKILL.tr.md)

**Fırsat-çözüm ağacı** · `opportunity-solution-tree`

- Ne zaman: Hedef sonucu fırsatlara, çözümlere ve deneylere bağlar
- Dosya: [skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.tr.md](skills/02-product/product-manager/discovery/opportunity-solution-tree/SKILL.tr.md)

**Ürün hipotezi yazma** · `hypothesis-statement`

- Ne zaman: "İnanıyoruz ki / sonuç / bunu şuradan anlayacağız" formatında hipotez yazar
- Dosya: [skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.tr.md](skills/02-product/product-manager/discovery/hypothesis-statement/SKILL.tr.md)

**Ürün deneyi tasarlama** · `experiment-design`

- Ne zaman: Metrik, örneklem ve durdurma kurallarıyla A/B veya sahte kapı testi tasarlar
- Dosya: [skills/02-product/product-manager/discovery/experiment-design/SKILL.tr.md](skills/02-product/product-manager/discovery/experiment-design/SKILL.tr.md)

**Müşteri geri bildirimi sentezi** · `feedback-synthesis`

- Ne zaman: Geri bildirimleri sıklık ve önem derecesiyle temalara ayırır
- Dosya: [skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.tr.md](skills/02-product/product-manager/discovery/feedback-synthesis/SKILL.tr.md)

**Problem görüşmesi senaryosu** · `problem-interview-script`

- Ne zaman: Yönlendirmeyen müşteri görüşmesi (Mom Test tarzı)
- Dosya: [skills/02-product/product-manager/discovery/problem-interview-script/SKILL.tr.md](skills/02-product/product-manager/discovery/problem-interview-script/SKILL.tr.md)

#### Ürün Tanımı

**Ürün Gereksinim Dokümanı (PRD) yazma** · `prd-writing`

- Ne zaman: Problem, hedefler, kullanıcılar, kapsam, gereksinimler, metrikler, riskler
- Dosya: [skills/02-product/product-manager/definition/prd-writing/SKILL.tr.md](skills/02-product/product-manager/definition/prd-writing/SKILL.tr.md)

**Özellik özeti yazma** · `feature-brief`

- Ne zaman: Uyum için bir özelliğin tek sayfalık özeti
- Dosya: [skills/02-product/product-manager/definition/feature-brief/SKILL.tr.md](skills/02-product/product-manager/definition/feature-brief/SKILL.tr.md)

**MVP kapsamını belirleme** · `mvp-scoping`

- Ne zaman: Kapsamı test edilebilir en küçük değere indirir
- Dosya: [skills/02-product/product-manager/definition/mvp-scoping/SKILL.tr.md](skills/02-product/product-manager/definition/mvp-scoping/SKILL.tr.md)

**Epic'i hikayelere bölme** · `epic-breakdown`

- Ne zaman: Epic'leri ince dikey dilimlere böler
- Dosya: [skills/02-product/product-manager/definition/epic-breakdown/SKILL.tr.md](skills/02-product/product-manager/definition/epic-breakdown/SKILL.tr.md)

**Kullanıcı hikaye haritası** · `story-mapping`

- Ne zaman: Ana aktiviteler, adımlar, hikayeler ve sürüm dilimleri
- Dosya: [skills/02-product/product-manager/definition/story-mapping/SKILL.tr.md](skills/02-product/product-manager/definition/story-mapping/SKILL.tr.md)

#### Metrikler

**Kuzey Yıldızı metriği tanımlama** · `north-star-metric`

- Ne zaman: Değer metriğini ve girdi metrik ağacını belirler
- Dosya: [skills/02-product/product-manager/metrics/north-star-metric/SKILL.tr.md](skills/02-product/product-manager/metrics/north-star-metric/SKILL.tr.md)

**KPI tanımlama** · `kpi-definition`

- Ne zaman: Ad, formül, kaynak, hedef, sahip, periyot
- Dosya: [skills/02-product/product-manager/metrics/kpi-definition/SKILL.tr.md](skills/02-product/product-manager/metrics/kpi-definition/SKILL.tr.md)

**Huni analizi** · `funnel-analysis`

- Ne zaman: Kayıp noktalarını ve iyileştirme hipotezlerini bulur
- Dosya: [skills/02-product/product-manager/metrics/funnel-analysis/SKILL.tr.md](skills/02-product/product-manager/metrics/funnel-analysis/SKILL.tr.md)

**Özellik benimsenme analizi** · `feature-adoption-review`

- Ne zaman: Yayınlanmış bir özelliğin kullanımını, tutunmasını ve sonucunu değerlendirir
- Dosya: [skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.tr.md](skills/02-product/product-manager/metrics/feature-adoption-review/SKILL.tr.md)

#### Lansman

**Pazara çıkış planı** · `go-to-market-plan`

- Ne zaman: Hedef kitle, mesaj, kanallar, zamanlama, hazırlık
- Dosya: [skills/02-product/product-manager/launch/go-to-market-plan/SKILL.tr.md](skills/02-product/product-manager/launch/go-to-market-plan/SKILL.tr.md)

**Sürüm duyurusu yazma** · `release-announcement`

- Ne zaman: Faydaya odaklanan müşteriye yönelik duyuru
- Dosya: [skills/02-product/product-manager/launch/release-announcement/SKILL.tr.md](skills/02-product/product-manager/launch/release-announcement/SKILL.tr.md)

**Konumlandırma cümlesi** · `positioning-statement`

- Ne zaman: Kimin için/kim/nedir/ne yapar/rakiplerden farkı formatı
- Dosya: [skills/02-product/product-manager/launch/positioning-statement/SKILL.tr.md](skills/02-product/product-manager/launch/positioning-statement/SKILL.tr.md)

### Ürün Sahibi

#### Backlog Yönetimi

**Backlog iyileştirme** · `backlog-refinement`

- Ne zaman: Maddeleri netleştirir, böler, tahmine hazır hale getirir ve sıralar
- Dosya: [skills/02-product/product-owner/backlog/backlog-refinement/SKILL.tr.md](skills/02-product/product-owner/backlog/backlog-refinement/SKILL.tr.md)

**Backlog önceliklendirme** · `backlog-prioritization`

- Ne zaman: WSJF, RICE, değer/efor ile gerekçeli sıralama yapar
- Dosya: [skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.tr.md](skills/02-product/product-owner/backlog/backlog-prioritization/SKILL.tr.md)

**Büyük hikayeleri bölme** · `story-splitting`

- Ne zaman: İş akışı, kural, veri, arayüz veya spike'a göre böler
- Dosya: [skills/02-product/product-owner/backlog/story-splitting/SKILL.tr.md](skills/02-product/product-owner/backlog/story-splitting/SKILL.tr.md)

**Hazır Tanımı (DoR) oluşturma** · `definition-of-ready`

- Ne zaman: İşin başlaması için giriş kriterleri
- Dosya: [skills/02-product/product-owner/backlog/definition-of-ready/SKILL.tr.md](skills/02-product/product-owner/backlog/definition-of-ready/SKILL.tr.md)

**Bitti Tanımı (DoD) oluşturma** · `definition-of-done`

- Ne zaman: İşin tamamlanması için kalite kontrol listesi
- Dosya: [skills/02-product/product-owner/backlog/definition-of-done/SKILL.tr.md](skills/02-product/product-owner/backlog/definition-of-done/SKILL.tr.md)

**Backlog sağlık kontrolü** · `backlog-health-check`

- Ne zaman: Bayat, tekrar eden, fazla büyük veya sahipsiz maddeleri tespit eder
- Dosya: [skills/02-product/product-owner/backlog/backlog-health-check/SKILL.tr.md](skills/02-product/product-owner/backlog/backlog-health-check/SKILL.tr.md)

#### Planlama

**Ürün yol haritası** · `roadmap`

- Ne zaman: Sonuçlara bağlı Şimdi/Sonra/Daha Sonra veya zaman çizelgeli yol haritası
- Dosya: [skills/02-product/product-owner/planning/roadmap/SKILL.tr.md](skills/02-product/product-owner/planning/roadmap/SKILL.tr.md)

**Sürüm planlama** · `release-planning`

- Ne zaman: Bir sürüm için kapsam, tarihler, bağımlılıklar ve güven seviyesi
- Dosya: [skills/02-product/product-owner/planning/release-planning/SKILL.tr.md](skills/02-product/product-owner/planning/release-planning/SKILL.tr.md)

**İterasyon hedefi yazma** · `iteration-goal`

- Ne zaman: Bir sprint/iterasyon için tek ve tutarlı hedef
- Dosya: [skills/02-product/product-owner/planning/iteration-goal/SKILL.tr.md](skills/02-product/product-owner/planning/iteration-goal/SKILL.tr.md)

**Ürün değerlendirme toplantısı hazırlığı** · `stakeholder-review-prep`

- Ne zaman: Ne yapıldı, hangi geri bildirim isteniyor, hangi kararlar gerekiyor
- Dosya: [skills/02-product/product-owner/planning/stakeholder-review-prep/SKILL.tr.md](skills/02-product/product-owner/planning/stakeholder-review-prep/SKILL.tr.md)

## Proje ve Teslimat Yönetimi

### Proje Yöneticisi

#### Başlatma

**Proje başlatma belgesi** · `project-charter`

- Ne zaman: Amaç, hedefler, kapsam, paydaşlar, bütçe, yetki
- Dosya: [skills/03-delivery/project-manager/initiation/project-charter/SKILL.tr.md](skills/03-delivery/project-manager/initiation/project-charter/SKILL.tr.md)

**Kapsam tanımı yazma** · `scope-statement`

- Ne zaman: Kapsam içi/dışı, teslimatlar, kısıtlar, varsayımlar
- Dosya: [skills/03-delivery/project-manager/initiation/scope-statement/SKILL.tr.md](skills/03-delivery/project-manager/initiation/scope-statement/SKILL.tr.md)

**Proje açılış toplantısı hazırlığı** · `kickoff-deck`

- Ne zaman: Ekip ve sponsorlar için açılış gündemi ve içeriği
- Dosya: [skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.tr.md](skills/03-delivery/project-manager/initiation/kickoff-deck/SKILL.tr.md)

**Paydaş kaydı** · `stakeholder-register`

- Ne zaman: Roller, ilgiler, etki, iletişim ihtiyaçları
- Dosya: [skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.tr.md](skills/03-delivery/project-manager/initiation/stakeholder-register/SKILL.tr.md)

#### Planlama

**İş kırılım yapısı (WBS)** · `wbs`

- Ne zaman: Teslimatları iş paketlerine böler
- Dosya: [skills/03-delivery/project-manager/planning/wbs/SKILL.tr.md](skills/03-delivery/project-manager/planning/wbs/SKILL.tr.md)

**Üç noktalı (PERT) tahmin** · `estimation-three-point`

- Ne zaman: İyimser/olası/kötümser ile beklenen değer ve aralık
- Dosya: [skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.tr.md](skills/03-delivery/project-manager/planning/estimation-three-point/SKILL.tr.md)

**Proje takvimi oluşturma** · `schedule-plan`

- Ne zaman: Görevleri, bağımlılıkları, kilometre taşlarını ve kritik yolu sıralar
- Dosya: [skills/03-delivery/project-manager/planning/schedule-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/schedule-plan/SKILL.tr.md)

**Kaynak planı** · `resource-plan`

- Ne zaman: Zamana yayılmış yetkinlik, atama ve eksikler
- Dosya: [skills/03-delivery/project-manager/planning/resource-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/resource-plan/SKILL.tr.md)

**Proje bütçesi** · `budget-plan`

- Ne zaman: Maliyet kırılımı, yedek pay ve nakit akışı
- Dosya: [skills/03-delivery/project-manager/planning/budget-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/budget-plan/SKILL.tr.md)

**İletişim planı** · `communication-plan`

- Ne zaman: Kime, ne, ne zaman, nasıl, kimden
- Dosya: [skills/03-delivery/project-manager/planning/communication-plan/SKILL.tr.md](skills/03-delivery/project-manager/planning/communication-plan/SKILL.tr.md)

**Risk kaydı** · `risk-register`

- Ne zaman: Olasılık, etki, sahip ve yanıtıyla riskler
- Dosya: [skills/03-delivery/project-manager/planning/risk-register/SKILL.tr.md](skills/03-delivery/project-manager/planning/risk-register/SKILL.tr.md)

**Bağımlılık haritası** · `dependency-map`

- Ne zaman: Sahip ve tarihleriyle iç/dış bağımlılıklar
- Dosya: [skills/03-delivery/project-manager/planning/dependency-map/SKILL.tr.md](skills/03-delivery/project-manager/planning/dependency-map/SKILL.tr.md)

#### İzleme ve Kontrol

**Proje durum raporu** · `project-status-report`

- Ne zaman: Takvim, maliyet, kapsam, riskler, gereken kararlar
- Dosya: [skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/project-status-report/SKILL.tr.md)

**RAID kaydı tutma** · `raid-log`

- Ne zaman: Riskler, Varsayımlar, Sorunlar, Bağımlılıklar
- Dosya: [skills/03-delivery/project-manager/monitoring/raid-log/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/raid-log/SKILL.tr.md)

**Kazanılmış değer analizi** · `earned-value-analysis`

- Ne zaman: PV, EV, AC, SPI, CPI ve tahmin
- Dosya: [skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/earned-value-analysis/SKILL.tr.md)

**Değişiklik kontrolü** · `change-control`

- Ne zaman: Kapsam/zaman/maliyet değişikliklerini değerlendirir ve kaydeder
- Dosya: [skills/03-delivery/project-manager/monitoring/change-control/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/change-control/SKILL.tr.md)

**Sorun yönetimi** · `issue-management`

- Ne zaman: Sorunu kaydeder, değerlendirir, atar ve kapanışa kadar izler
- Dosya: [skills/03-delivery/project-manager/monitoring/issue-management/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/issue-management/SKILL.tr.md)

**Tedarikçi performans değerlendirmesi** · `vendor-status-review`

- Ne zaman: Teslimatları, SLA'ları ve sözleşme yükümlülüklerini kontrol eder
- Dosya: [skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.tr.md](skills/03-delivery/project-manager/monitoring/vendor-status-review/SKILL.tr.md)

#### Kapanış

**Proje kapanış raporu** · `project-closure-report`

- Ne zaman: Hedeflere karşı sonuçlar, sapmalar, devir, dersler
- Dosya: [skills/03-delivery/project-manager/closure/project-closure-report/SKILL.tr.md](skills/03-delivery/project-manager/closure/project-closure-report/SKILL.tr.md)

**Teslimat kabul belgesi** · `acceptance-certificate`

- Ne zaman: Kriterler ve onaylarla kabul kaydı
- Dosya: [skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.tr.md](skills/03-delivery/project-manager/closure/acceptance-certificate/SKILL.tr.md)

### Scrum Master / Çevik Koç

#### Ekip Etkinlikleri

**İterasyon planlaması kolaylaştırma** · `iteration-planning`

- Ne zaman: Kapasite, hedef, seçim ve görev kırılımı
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/iteration-planning/SKILL.tr.md)

**Günlük toplantı özeti** · `daily-sync-summary`

- Ne zaman: Kişi ve ekip bazında ilerleme, plan, engeller
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/daily-sync-summary/SKILL.tr.md)

**İterasyon değerlendirmesi hazırlığı** · `iteration-review-prep`

- Ne zaman: Demo sırası, artım özeti, geri bildirim soruları
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/iteration-review-prep/SKILL.tr.md)

**Retrospektif kolaylaştırma** · `retrospective-facilitation`

- Ne zaman: Format seçer, yürütür ve aksiyon üretir
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-facilitation/SKILL.tr.md)

**Retrospektif formatı tasarlama** · `retrospective-format`

- Ne zaman: Ekibin durumuna ve konuya uygun retro formatı tasarlar
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/retrospective-format/SKILL.tr.md)

**Göreli tahmin oturumu** · `estimation-session`

- Ne zaman: Planning poker / tişört bedeni yönlendirmesi ve referans hikayeler
- Dosya: [skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.tr.md](skills/03-delivery/agile-delivery/ceremonies/estimation-session/SKILL.tr.md)

#### Akış ve Metrikler

**Hız/verim analizi** · `velocity-analysis`

- Ne zaman: Trendler, değişkenlik ve öngörü
- Dosya: [skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/velocity-analysis/SKILL.tr.md)

**Burndown/burnup analizi** · `burndown-analysis`

- Ne zaman: Grafikleri yorumlar, riskleri işaretler
- Dosya: [skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/burndown-analysis/SKILL.tr.md)

**Döngü/teslim süresi analizi** · `cycle-time-analysis`

- Ne zaman: Yüzdelikler, darboğazlar, yaşlanan işler
- Dosya: [skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/cycle-time-analysis/SKILL.tr.md)

**WIP limiti ve akış kuralları** · `wip-policy`

- Ne zaman: Pano kolonları, WIP limitleri, giriş/çıkış kuralları
- Dosya: [skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/wip-policy/SKILL.tr.md)

**Monte Carlo ile teslim tahmini** · `monte-carlo-forecast`

- Ne zaman: Verim verisinden olasılıksal "ne zaman/kaç tane" tahmini
- Dosya: [skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/monte-carlo-forecast/SKILL.tr.md)

**Engel takibi** · `impediment-tracking`

- Ne zaman: Engelleri kaydeder, eskale eder ve çözer
- Dosya: [skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.tr.md](skills/03-delivery/agile-delivery/flow/impediment-tracking/SKILL.tr.md)

#### Ekip Gelişimi

**Ekip çalışma sözleşmesi** · `working-agreement`

- Ne zaman: İletişim, erişilebilirlik, inceleme, toplantı normları
- Dosya: [skills/03-delivery/agile-delivery/team/working-agreement/SKILL.tr.md](skills/03-delivery/agile-delivery/team/working-agreement/SKILL.tr.md)

**Ekip sağlık kontrolü** · `team-health-check`

- Ne zaman: Anket boyutları, trendler ve takip aksiyonları
- Dosya: [skills/03-delivery/agile-delivery/team/team-health-check/SKILL.tr.md](skills/03-delivery/agile-delivery/team/team-health-check/SKILL.tr.md)

**Çeviklik olgunluk değerlendirmesi** · `agile-maturity-assessment`

- Ne zaman: Pratikleri puanlar, sonraki iyileştirmeleri önerir
- Dosya: [skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.tr.md](skills/03-delivery/agile-delivery/team/agile-maturity-assessment/SKILL.tr.md)

### Program Yöneticisi / PMO

#### Portföy ve Program

**Proje portföyü önceliklendirme** · `portfolio-prioritization`

- Ne zaman: Girişimleri değer, risk, stratejik uyum ve kapasiteye göre puanlar
- Dosya: [skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/portfolio-prioritization/SKILL.tr.md)

**Program yol haritası** · `program-roadmap`

- Ne zaman: Ekipler arası kilometre taşları ve entegrasyon noktaları
- Dosya: [skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/program-roadmap/SKILL.tr.md)

**Ekipler arası bağımlılık planlaması** · `cross-team-dependency-board`

- Ne zaman: Ekipler arası bağımlılıkları belirler, müzakere eder ve izler
- Dosya: [skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/cross-team-dependency-board/SKILL.tr.md)

**Yönlendirme kurulu sunumu** · `steering-committee-pack`

- Ne zaman: Durum, gereken kararlar, riskler, finansal durum
- Dosya: [skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/steering-committee-pack/SKILL.tr.md)

**Proje yönetişimi tanımlama** · `governance-framework`

- Ne zaman: Karar yetkileri, kurullar, geçiş kapıları, raporlama sıklığı
- Dosya: [skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/governance-framework/SKILL.tr.md)

**Fayda gerçekleşme takibi** · `benefits-realization`

- Ne zaman: Teslimat sonrası planlanan ve gerçekleşen faydalar
- Dosya: [skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.tr.md](skills/03-delivery/program-pmo/portfolio/benefits-realization/SKILL.tr.md)

## Mimari

### Kurumsal Mimar

#### Mimari Strateji

**Mimari ilkeler tanımlama** · `architecture-principles`

- Ne zaman: İlke, gerekçe ve etkiler (TOGAF tarzı)
- Dosya: [skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/architecture-principles/SKILL.tr.md)

**İş yetkinlik haritası** · `capability-map`

- Ne zaman: Olgunluk ve ısı haritasıyla hiyerarşik yetkinlikler
- Dosya: [skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/capability-map/SKILL.tr.md)

**Uygulama portföyü değerlendirmesi** · `application-portfolio-assessment`

- Ne zaman: TIME modeli: tolere et, yatırım yap, taşı, kaldır
- Dosya: [skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/application-portfolio-assessment/SKILL.tr.md)

**Hedef mimari tanımlama** · `target-state-architecture`

- Ne zaman: Mevcut, hedef, fark ve geçiş yol haritası
- Dosya: [skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/target-state-architecture/SKILL.tr.md)

**Teknoloji radarı** · `tech-radar`

- Ne zaman: Teknolojileri benimse/dene/değerlendir/beklet olarak sınıflar
- Dosya: [skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.tr.md](skills/04-architecture/enterprise-architect/strategy/tech-radar/SKILL.tr.md)

### Çözüm Mimarı

#### Çözüm Tasarımı

**Çözüm mimarisi dokümanı** · `solution-architecture-document`

- Ne zaman: arc42 tarzı doküman: bağlam, kısıtlar, yapı taşları, çalışma zamanı, dağıtım
- Dosya: [skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.tr.md](skills/04-architecture/solution-architect/design/solution-architecture-document/SKILL.tr.md)

**C4 ile mimari tanımlama** · `c4-model`

- Ne zaman: Bağlam, konteyner, bileşen diyagramlarını kod olarak üretir
- Dosya: [skills/04-architecture/solution-architect/design/c4-model/SKILL.tr.md](skills/04-architecture/solution-architect/design/c4-model/SKILL.tr.md)

**Mimari karar kaydı (ADR) yazma** · `adr`

- Ne zaman: Bağlam, seçenekler, karar, sonuçlar
- Dosya: [skills/04-architecture/solution-architect/design/adr/SKILL.tr.md](skills/04-architecture/solution-architect/design/adr/SKILL.tr.md)

**Teknoloji seçimi** · `technology-selection`

- Ne zaman: Kriterler, kısa liste, PoC planı ve öneri
- Dosya: [skills/04-architecture/solution-architect/design/technology-selection/SKILL.tr.md](skills/04-architecture/solution-architect/design/technology-selection/SKILL.tr.md)

**Entegrasyon deseni seçimi** · `integration-pattern-selection`

- Ne zaman: Ödünleşimleriyle senkron/asenkron, API, mesajlaşma, dosya, CDC
- Dosya: [skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.tr.md](skills/04-architecture/solution-architect/design/integration-pattern-selection/SKILL.tr.md)

**NFR'leri mimari taktiklere eşleme** · `nfr-to-architecture`

- Ne zaman: Kalite niteliği senaryoları ve taktikler
- Dosya: [skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.tr.md](skills/04-architecture/solution-architect/design/nfr-to-architecture/SKILL.tr.md)

**Yap ya da satın al kararı** · `build-vs-buy`

- Ne zaman: TCO, uygunluk, risk ve stratejik değer karşılaştırması
- Dosya: [skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.tr.md](skills/04-architecture/solution-architect/design/build-vs-buy/SKILL.tr.md)

**Tasarımın bulut maliyet tahmini** · `cloud-cost-estimate`

- Ne zaman: Bileşenleri boyutlandırır, aylık işletim maliyetini tahmin eder
- Dosya: [skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.tr.md](skills/04-architecture/solution-architect/design/cloud-cost-estimate/SKILL.tr.md)

#### Mimari Gözden Geçirme

**Mimari gözden geçirme** · `architecture-review`

- Ne zaman: İlkelere, NFR'lere, risklere ve anti-desenlere göre kontrol eder
- Dosya: [skills/04-architecture/solution-architect/review/architecture-review/SKILL.tr.md](skills/04-architecture/solution-architect/review/architecture-review/SKILL.tr.md)

**ATAM tarzı değerlendirme** · `atam-evaluation`

- Ne zaman: Fayda ağacı, hassasiyet noktaları, ödünleşimler, riskler
- Dosya: [skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.tr.md](skills/04-architecture/solution-architect/review/atam-evaluation/SKILL.tr.md)

**Dayanıklılık incelemesi** · `resilience-review`

- Ne zaman: Hata modları, zaman aşımı, yeniden deneme, devre kesici, felaket kurtarma
- Dosya: [skills/04-architecture/solution-architect/review/resilience-review/SKILL.tr.md](skills/04-architecture/solution-architect/review/resilience-review/SKILL.tr.md)

**Ölçeklenebilirlik incelemesi** · `scalability-review`

- Ne zaman: Darboğazlar, durum yönetimi, bölümleme, önbellek
- Dosya: [skills/04-architecture/solution-architect/review/scalability-review/SKILL.tr.md](skills/04-architecture/solution-architect/review/scalability-review/SKILL.tr.md)

### Yazılım Mimarı

#### Alan Tasarımı

**Event storming** · `event-storming`

- Ne zaman: Alan olayları, komutlar, aggregate'ler, politikalar, sıcak noktalar
- Dosya: [skills/04-architecture/software-architect/domain/event-storming/SKILL.tr.md](skills/04-architecture/software-architect/domain/event-storming/SKILL.tr.md)

**Sınırlı bağlam haritası** · `bounded-context-map`

- Ne zaman: Bağlamlar ve ilişkileri (ACL, OHS, paylaşılan çekirdek)
- Dosya: [skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.tr.md](skills/04-architecture/software-architect/domain/bounded-context-map/SKILL.tr.md)

**Aggregate tasarımı** · `aggregate-design`

- Ne zaman: Değişmezler, sınırlar, tutarlılık kuralları
- Dosya: [skills/04-architecture/software-architect/domain/aggregate-design/SKILL.tr.md](skills/04-architecture/software-architect/domain/aggregate-design/SKILL.tr.md)

**Olay güdümlü akış tasarımı** · `event-driven-design`

- Ne zaman: Olaylar, şemalar, topic'ler, sıralama, idempotency, saga'lar
- Dosya: [skills/04-architecture/software-architect/domain/event-driven-design/SKILL.tr.md](skills/04-architecture/software-architect/domain/event-driven-design/SKILL.tr.md)

**Servislere ayrıştırma** · `service-decomposition`

- Ne zaman: Servis sınırlarını ve veri sahipliğini belirler
- Dosya: [skills/04-architecture/software-architect/domain/service-decomposition/SKILL.tr.md](skills/04-architecture/software-architect/domain/service-decomposition/SKILL.tr.md)

#### Mimari Evrim

**Teknik borç değerlendirmesi** · `tech-debt-assessment`

- Ne zaman: Envanter çıkarır, sınıflar, maliyetini tahmin eder ve önceliklendirir
- Dosya: [skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.tr.md](skills/04-architecture/software-architect/evolution/tech-debt-assessment/SKILL.tr.md)

**Göç stratejisi planlama** · `migration-strategy`

- Ne zaman: Riskleriyle strangler fig, paralel çalıştırma, tek seferde geçiş
- Dosya: [skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.tr.md](skills/04-architecture/software-architect/evolution/migration-strategy/SKILL.tr.md)

**Eski sistem modernizasyon değerlendirmesi** · `modernization-assessment`

- Ne zaman: Efor ve değerle 7R seçenekleri
- Dosya: [skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.tr.md](skills/04-architecture/software-architect/evolution/modernization-assessment/SKILL.tr.md)

**API tasarımı inceleme** · `api-design-review`

- Ne zaman: İsimlendirme, sürümleme, hatalar, sayfalama, idempotency, güvenlik
- Dosya: [skills/04-architecture/software-architect/evolution/api-design-review/SKILL.tr.md](skills/04-architecture/software-architect/evolution/api-design-review/SKILL.tr.md)

## Yazılım Geliştirme

### Geliştirici (Backend/Frontend/Mobil)

#### Teknik Tasarım

**Teknik tasarım dokümanı (RFC)** · `technical-design-doc`

- Ne zaman: Problem, yaklaşım, alternatifler, yayına alma, riskler
- Dosya: [skills/05-engineering/developer/design/technical-design-doc/SKILL.tr.md](skills/05-engineering/developer/design/technical-design-doc/SKILL.tr.md)

**Hikayeyi görevlere bölme** · `task-breakdown`

- Ne zaman: Sıralı ve tahminli teknik görevler
- Dosya: [skills/05-engineering/developer/design/task-breakdown/SKILL.tr.md](skills/05-engineering/developer/design/task-breakdown/SKILL.tr.md)

**API sözleşmesi yazma** · `api-contract`

- Ne zaman: Gereksinimlerden OpenAPI/AsyncAPI şartnamesi
- Dosya: [skills/05-engineering/developer/design/api-contract/SKILL.tr.md](skills/05-engineering/developer/design/api-contract/SKILL.tr.md)

**Veritabanı şeması tasarlama** · `database-schema-design`

- Ne zaman: Alan modelinden tablolar, anahtarlar, kısıtlar, indeksler
- Dosya: [skills/05-engineering/developer/design/database-schema-design/SKILL.tr.md](skills/05-engineering/developer/design/database-schema-design/SKILL.tr.md)

**Spike raporu yazma** · `spike-report`

- Ne zaman: Soru, bulgular, seçenekler, öneri
- Dosya: [skills/05-engineering/developer/design/spike-report/SKILL.tr.md](skills/05-engineering/developer/design/spike-report/SKILL.tr.md)

#### Kodlama

**Hikayeden özellik geliştirme** · `implement-from-story`

- Ne zaman: Kabul kriterlerine göre planlar ve uygular
- Dosya: [skills/05-engineering/developer/coding/implement-from-story/SKILL.tr.md](skills/05-engineering/developer/coding/implement-from-story/SKILL.tr.md)

**Kodu yeniden düzenleme** · `refactoring`

- Ne zaman: Testlerle güvence altında adlandırılmış refactoring'ler uygular
- Dosya: [skills/05-engineering/developer/coding/refactoring/SKILL.tr.md](skills/05-engineering/developer/coding/refactoring/SKILL.tr.md)

**Clean Code incelemesi** · `clean-code-review`

- Ne zaman: İsimlendirme, fonksiyonlar, SOLID, tekrar, kod kokuları
- Dosya: [skills/05-engineering/developer/coding/clean-code-review/SKILL.tr.md](skills/05-engineering/developer/coding/clean-code-review/SKILL.tr.md)

**Hata yönetimi incelemesi** · `error-handling-review`

- Ne zaman: İstisnalar, yeniden denemeler, yedek davranışlar, kullanıcıya gösterilen hatalar
- Dosya: [skills/05-engineering/developer/coding/error-handling-review/SKILL.tr.md](skills/05-engineering/developer/coding/error-handling-review/SKILL.tr.md)

**Loglama ve ölçümleme ekleme** · `logging-instrumentation`

- Ne zaman: Doğru noktalarda yapılandırılmış log, metrik ve iz
- Dosya: [skills/05-engineering/developer/coding/logging-instrumentation/SKILL.tr.md](skills/05-engineering/developer/coding/logging-instrumentation/SKILL.tr.md)

**Performans iyileştirme** · `performance-optimization`

- Ne zaman: Profil verisine dayalı darboğazlar ve çözümler
- Dosya: [skills/05-engineering/developer/coding/performance-optimization/SKILL.tr.md](skills/05-engineering/developer/coding/performance-optimization/SKILL.tr.md)

**Eşzamanlılık incelemesi** · `concurrency-review`

- Ne zaman: Yarış durumları, kilitlenmeler, thread güvenliği, async tuzakları
- Dosya: [skills/05-engineering/developer/coding/concurrency-review/SKILL.tr.md](skills/05-engineering/developer/coding/concurrency-review/SKILL.tr.md)

**Bağımlılık güncelleme** · `dependency-upgrade`

- Ne zaman: Kırıcı değişiklikler, geçiş adımları, doğrulama
- Dosya: [skills/05-engineering/developer/coding/dependency-upgrade/SKILL.tr.md](skills/05-engineering/developer/coding/dependency-upgrade/SKILL.tr.md)

**Kodu açıklama** · `code-explanation`

- Ne zaman: Kodun ne yaptığını, nedenini ve risklerini açıklar
- Dosya: [skills/05-engineering/developer/coding/code-explanation/SKILL.tr.md](skills/05-engineering/developer/coding/code-explanation/SKILL.tr.md)

**Eski kodu anlama** · `legacy-code-comprehension`

- Ne zaman: Yabancı kodda modülleri, akışları ve gizli kuralları çıkarır
- Dosya: [skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.tr.md](skills/05-engineering/developer/coding/legacy-code-comprehension/SKILL.tr.md)

**Regex oluşturma ve açıklama** · `regex-builder`

- Ne zaman: Düzenli ifade yazar, test durumlarını verir ve açıklar
- Dosya: [skills/05-engineering/developer/coding/regex-builder/SKILL.tr.md](skills/05-engineering/developer/coding/regex-builder/SKILL.tr.md)

**SQL sorgusu yazma** · `sql-query-writing`

- Ne zaman: Doğru, okunabilir, indeks dostu sorgular
- Dosya: [skills/05-engineering/developer/coding/sql-query-writing/SKILL.tr.md](skills/05-engineering/developer/coding/sql-query-writing/SKILL.tr.md)

#### Geliştirici Testleri

**Birim testi yazma** · `unit-test-writing`

- Ne zaman: Davranış ve uç durumları kapsayan AAA testleri
- Dosya: [skills/05-engineering/developer/testing/unit-test-writing/SKILL.tr.md](skills/05-engineering/developer/testing/unit-test-writing/SKILL.tr.md)

**Entegrasyon testi yazma** · `integration-test-writing`

- Ne zaman: Gerektiğinde test dublörleriyle gerçek sınırlar arası testler
- Dosya: [skills/05-engineering/developer/testing/integration-test-writing/SKILL.tr.md](skills/05-engineering/developer/testing/integration-test-writing/SKILL.tr.md)

**TDD ile geliştirme** · `tdd-cycle`

- Ne zaman: Bir davranış için kırmızı-yeşil-refactor adımları
- Dosya: [skills/05-engineering/developer/testing/tdd-cycle/SKILL.tr.md](skills/05-engineering/developer/testing/tdd-cycle/SKILL.tr.md)

**Test edilmemiş yolları bulma** · `test-gap-finder`

- Ne zaman: Dallar ve uç durumlar için eksik testleri bulur
- Dosya: [skills/05-engineering/developer/testing/test-gap-finder/SKILL.tr.md](skills/05-engineering/developer/testing/test-gap-finder/SKILL.tr.md)

#### Kod İşbirliği

**Commit mesajı yazma** · `commit-message`

- Ne zaman: Nedeniyle birlikte Conventional Commits formatında
- Dosya: [skills/05-engineering/developer/collaboration/commit-message/SKILL.tr.md](skills/05-engineering/developer/collaboration/commit-message/SKILL.tr.md)

**Pull request açıklaması** · `pull-request-description`

- Ne zaman: Ne, neden, nasıl test edildi, riskler, ekran görüntüleri
- Dosya: [skills/05-engineering/developer/collaboration/pull-request-description/SKILL.tr.md](skills/05-engineering/developer/collaboration/pull-request-description/SKILL.tr.md)

**Pull request inceleme** · `code-review`

- Ne zaman: Doğruluk, tasarım, testler, güvenlik, okunabilirlik
- Dosya: [skills/05-engineering/developer/collaboration/code-review/SKILL.tr.md](skills/05-engineering/developer/collaboration/code-review/SKILL.tr.md)

**İnceleme yorumu yazma** · `review-comment-writing`

- Ne zaman: Somut, nazik, uygulanabilir, etiketli (nit/blocker)
- Dosya: [skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.tr.md](skills/05-engineering/developer/collaboration/review-comment-writing/SKILL.tr.md)

**Branch stratejisi seçme** · `branching-strategy`

- Ne zaman: Bağlama göre trunk-based, GitFlow veya GitHub Flow
- Dosya: [skills/05-engineering/developer/collaboration/branching-strategy/SKILL.tr.md](skills/05-engineering/developer/collaboration/branching-strategy/SKILL.tr.md)

#### Hata Ayıklama

**Hatayı yeniden üretme** · `bug-reproduction`

- Ne zaman: Minimum tekrar adımları ve ortam
- Dosya: [skills/05-engineering/developer/debugging/bug-reproduction/SKILL.tr.md](skills/05-engineering/developer/debugging/bug-reproduction/SKILL.tr.md)

**Stack trace analizi** · `stack-trace-analysis`

- Ne zaman: Hatalı çerçeveyi, nedeni ve çözüm adaylarını bulur
- Dosya: [skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.tr.md](skills/05-engineering/developer/debugging/stack-trace-analysis/SKILL.tr.md)

**Log analizi** · `log-analysis`

- Ne zaman: Olayları ilişkilendirir, anomali ve zaman çizelgesi çıkarır
- Dosya: [skills/05-engineering/developer/debugging/log-analysis/SKILL.tr.md](skills/05-engineering/developer/debugging/log-analysis/SKILL.tr.md)

**Hata ayıklama hipotezleri** · `debugging-hypotheses`

- Ne zaman: Sıralı hipotezler ve her biri için en ucuz test
- Dosya: [skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.tr.md](skills/05-engineering/developer/debugging/debugging-hypotheses/SKILL.tr.md)

#### Geliştirici Dokümantasyonu

**README yazma** · `readme-writing`

- Ne zaman: Amaç, kurulum, kullanım, yapılandırma, katkı
- Dosya: [skills/05-engineering/developer/docs/readme-writing/SKILL.tr.md](skills/05-engineering/developer/docs/readme-writing/SKILL.tr.md)

**Kod dokümantasyonu** · `code-documentation`

- Ne zaman: Neyi değil nedeni açıklayan docstring/yorumlar
- Dosya: [skills/05-engineering/developer/docs/code-documentation/SKILL.tr.md](skills/05-engineering/developer/docs/code-documentation/SKILL.tr.md)

**API referans dokümanı** · `api-reference-docs`

- Ne zaman: Uç noktalar, parametreler, örnekler, hatalar
- Dosya: [skills/05-engineering/developer/docs/api-reference-docs/SKILL.tr.md](skills/05-engineering/developer/docs/api-reference-docs/SKILL.tr.md)

**Değişiklik günlüğü girdisi** · `changelog-entry`

- Ne zaman: Keep a Changelog formatında girdiler
- Dosya: [skills/05-engineering/developer/docs/changelog-entry/SKILL.tr.md](skills/05-engineering/developer/docs/changelog-entry/SKILL.tr.md)

#### Frontend'e Özel

**UI bileşeni tasarlama** · `component-design`

- Ne zaman: Prop'lar, durum, olaylar, varyantlar, erişilebilirlik
- Dosya: [skills/05-engineering/developer/frontend/component-design/SKILL.tr.md](skills/05-engineering/developer/frontend/component-design/SKILL.tr.md)

**Erişilebilirlik denetimi (WCAG)** · `accessibility-audit`

- Ne zaman: WCAG 2.2 kriterlerini kontrol eder, düzeltme önerir
- Dosya: [skills/05-engineering/developer/frontend/accessibility-audit/SKILL.tr.md](skills/05-engineering/developer/frontend/accessibility-audit/SKILL.tr.md)

**Web performans denetimi** · `web-performance-audit`

- Ne zaman: Core Web Vitals sorunları ve çözümleri
- Dosya: [skills/05-engineering/developer/frontend/web-performance-audit/SKILL.tr.md](skills/05-engineering/developer/frontend/web-performance-audit/SKILL.tr.md)

**Durum yönetimi tasarımı** · `state-management-design`

- Ne zaman: Yerel, global ve sunucu durumu kararları
- Dosya: [skills/05-engineering/developer/frontend/state-management-design/SKILL.tr.md](skills/05-engineering/developer/frontend/state-management-design/SKILL.tr.md)

#### Mobile Özel

**Uygulama mağazası sürüm notları** · `app-store-release-notes`

- Ne zaman: Mağaza sınırlarına uygun kısa kullanıcı notları
- Dosya: [skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.tr.md](skills/05-engineering/developer/mobile/app-store-release-notes/SKILL.tr.md)

**Mobil sürüm kontrol listesi** · `mobile-release-checklist`

- Ne zaman: Sürümleme, imzalama, izinler, mağaza görselleri, kademeli yayın
- Dosya: [skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.tr.md](skills/05-engineering/developer/mobile/mobile-release-checklist/SKILL.tr.md)

### Teknik Lider

#### Teknik Liderlik

**Kodlama standartları yazma** · `coding-standards`

- Ne zaman: Örnek ve gerekçeleriyle ekip kuralları
- Dosya: [skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/coding-standards/SKILL.tr.md)

**Teknik iş tahmini** · `technical-estimation`

- Ne zaman: Böler, aralık ve varsayımlarla tahmin eder
- Dosya: [skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/technical-estimation/SKILL.tr.md)

**Geliştirici oryantasyonu** · `technical-onboarding`

- Ne zaman: Kod tabanı turu, kurulum, ilk işler, kişiler
- Dosya: [skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/technical-onboarding/SKILL.tr.md)

**Teknik risk incelemesi** · `technical-risk-review`

- Ne zaman: Teslimat ve kalite risklerini erken belirler
- Dosya: [skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/technical-risk-review/SKILL.tr.md)

**Kod kalitesi raporu** · `code-quality-report`

- Ne zaman: Statik analiz metriklerini ve trendleri yorumlar
- Dosya: [skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.tr.md](skills/05-engineering/tech-lead/leadership/code-quality-report/SKILL.tr.md)

## Kalite Güvence ve Test

### Test Analisti / Test Mühendisi

#### Test Stratejisi ve Planlama

**Test stratejisi yazma** · `test-strategy`

- Ne zaman: Seviyeler, türler, ortamlar, araçlar, risk bazlı odak
- Dosya: [skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/test-strategy/SKILL.tr.md)

**Test planı yazma** · `test-plan`

- Ne zaman: Kapsam, yaklaşım, takvim, giriş/çıkış kriterleri (ISO 29119)
- Dosya: [skills/06-quality/qa-analyst/strategy/test-plan/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/test-plan/SKILL.tr.md)

**Risk bazlı test önceliklendirme** · `risk-based-testing`

- Ne zaman: Olasılık x etki ile test eforunu odaklar
- Dosya: [skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/risk-based-testing/SKILL.tr.md)

**Gereksinimlerin test edilebilirlik incelemesi** · `testability-review`

- Ne zaman: Test edilemez veya belirsiz gereksinimleri işaretler
- Dosya: [skills/06-quality/qa-analyst/strategy/testability-review/SKILL.tr.md](skills/06-quality/qa-analyst/strategy/testability-review/SKILL.tr.md)

#### Test Tasarımı

**Gereksinimden test senaryosu çıkarma** · `test-scenarios-from-requirements`

- Ne zaman: Üst düzey pozitif, negatif ve uç senaryolar
- Dosya: [skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.tr.md](skills/06-quality/qa-analyst/design/test-scenarios-from-requirements/SKILL.tr.md)

**Test case yazma** · `test-case-writing`

- Ne zaman: Adımlar, veri, beklenen sonuç, ön koşullar
- Dosya: [skills/06-quality/qa-analyst/design/test-case-writing/SKILL.tr.md](skills/06-quality/qa-analyst/design/test-case-writing/SKILL.tr.md)

**Denklik sınıfı ve sınır değer analizi** · `equivalence-boundary-analysis`

- Ne zaman: Girdileri bölümler, sınır değerleri seçer
- Dosya: [skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.tr.md](skills/06-quality/qa-analyst/design/equivalence-boundary-analysis/SKILL.tr.md)

**Karar tablosu testi** · `decision-table-testing`

- Ne zaman: Kurallar için koşul ve aksiyonları birleştirir
- Dosya: [skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.tr.md](skills/06-quality/qa-analyst/design/decision-table-testing/SKILL.tr.md)

**Durum geçiş testi** · `state-transition-testing`

- Ne zaman: Geçerli/geçersiz geçişleri kapsar
- Dosya: [skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.tr.md](skills/06-quality/qa-analyst/design/state-transition-testing/SKILL.tr.md)

**İkili kombinasyon testi** · `pairwise-testing`

- Ne zaman: Çiftleri kapsayarak kombinasyon sayısını azaltır
- Dosya: [skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.tr.md](skills/06-quality/qa-analyst/design/pairwise-testing/SKILL.tr.md)

**Keşif testi görev tanımı** · `exploratory-test-charter`

- Ne zaman: Görev, alanlar, sezgisel yöntemler, süre
- Dosya: [skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.tr.md](skills/06-quality/qa-analyst/design/exploratory-test-charter/SKILL.tr.md)

**Test verisi tasarlama** · `test-data-design`

- Ne zaman: Gerçekçi, anonimleştirilmiş, uç durumları kapsayan veri setleri
- Dosya: [skills/06-quality/qa-analyst/design/test-data-design/SKILL.tr.md](skills/06-quality/qa-analyst/design/test-data-design/SKILL.tr.md)

**BDD feature dosyası yazma** · `bdd-feature-file`

- Ne zaman: Gherkin senaryoları ve senaryo taslakları
- Dosya: [skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.tr.md](skills/06-quality/qa-analyst/design/bdd-feature-file/SKILL.tr.md)

**API testi tasarlama** · `api-test-design`

- Ne zaman: Sözleşme, durum kodları, yetkilendirme, doğrulama, negatif durumlar
- Dosya: [skills/06-quality/qa-analyst/design/api-test-design/SKILL.tr.md](skills/06-quality/qa-analyst/design/api-test-design/SKILL.tr.md)

#### Koşum ve Hatalar

**Hata raporu yazma** · `bug-report`

- Ne zaman: Başlık, adımlar, beklenen/gerçekleşen, ortam, kanıt, önem
- Dosya: [skills/06-quality/qa-analyst/execution/bug-report/SKILL.tr.md](skills/06-quality/qa-analyst/execution/bug-report/SKILL.tr.md)

**Hata önceliklendirme** · `bug-triage`

- Ne zaman: Önem ve öncelik, tekrarlar, atama
- Dosya: [skills/06-quality/qa-analyst/execution/bug-triage/SKILL.tr.md](skills/06-quality/qa-analyst/execution/bug-triage/SKILL.tr.md)

**Regresyon testi seçimi** · `regression-selection`

- Ne zaman: Değişiklik etkisine göre test seçer
- Dosya: [skills/06-quality/qa-analyst/execution/regression-selection/SKILL.tr.md](skills/06-quality/qa-analyst/execution/regression-selection/SKILL.tr.md)

**Test özet raporu** · `test-summary-report`

- Ne zaman: Kapsam, sonuçlar, hatalar, kalan risk, öneri
- Dosya: [skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.tr.md](skills/06-quality/qa-analyst/execution/test-summary-report/SKILL.tr.md)

**Sürüm kalite kapısı değerlendirmesi** · `release-quality-gate`

- Ne zaman: Çıkış kriterlerine göre yayına alınır/alınmaz kararı
- Dosya: [skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.tr.md](skills/06-quality/qa-analyst/execution/release-quality-gate/SKILL.tr.md)

**Hata trendi analizi** · `defect-trend-analysis`

- Ne zaman: Yoğunluk, kaçak hatalar, kök neden kategorileri
- Dosya: [skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.tr.md](skills/06-quality/qa-analyst/execution/defect-trend-analysis/SKILL.tr.md)

#### Kullanıcı Kabul

**Kullanıcı kabul testi planı** · `uat-plan`

- Ne zaman: Katılımcılar, senaryolar, takvim, onay
- Dosya: [skills/06-quality/qa-analyst/uat/uat-plan/SKILL.tr.md](skills/06-quality/qa-analyst/uat/uat-plan/SKILL.tr.md)

**Kabul testi senaryoları** · `uat-scenarios`

- Ne zaman: İş dilinde uçtan uca senaryolar
- Dosya: [skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.tr.md](skills/06-quality/qa-analyst/uat/uat-scenarios/SKILL.tr.md)

### Test Otomasyon Mühendisi

#### Otomasyon

**Otomasyon adayı seçimi** · `automation-candidate-selection`

- Ne zaman: Neyin otomatikleştirileceğini ROI'ye göre seçer
- Dosya: [skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.tr.md](skills/06-quality/automation-engineer/automation/automation-candidate-selection/SKILL.tr.md)

**Otomatik test yazma** · `test-automation-script`

- Ne zaman: Framework'ten bağımsız page/API object test kodu
- Dosya: [skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.tr.md](skills/06-quality/automation-engineer/automation/test-automation-script/SKILL.tr.md)

**Kararsız test analizi** · `flaky-test-analysis`

- Ne zaman: Nedenleri sınıflar, kararlı hale getirme önerir
- Dosya: [skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.tr.md](skills/06-quality/automation-engineer/automation/flaky-test-analysis/SKILL.tr.md)

**Test otomasyon çatısı tasarımı** · `automation-framework-design`

- Ne zaman: Katmanlar, desenler, raporlama, CI entegrasyonu
- Dosya: [skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.tr.md](skills/06-quality/automation-engineer/automation/automation-framework-design/SKILL.tr.md)

### Performans Test Mühendisi

#### Performans Testi

**Performans test planı** · `performance-test-plan`

- Ne zaman: İş yükü modeli, senaryolar, SLA'lar, ortam
- Dosya: [skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.tr.md](skills/06-quality/performance-engineer/performance/performance-test-plan/SKILL.tr.md)

**Yük testi sonuç analizi** · `load-test-analysis`

- Ne zaman: Verim, gecikme yüzdelikleri, hatalar, darboğazlar
- Dosya: [skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.tr.md](skills/06-quality/performance-engineer/performance/load-test-analysis/SKILL.tr.md)

**Kapasite raporu** · `capacity-test-report`

- Ne zaman: Sürdürülebilir maksimum yük ve pay
- Dosya: [skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.tr.md](skills/06-quality/performance-engineer/performance/capacity-test-report/SKILL.tr.md)

## DevOps, SRE ve Platform

### DevOps / Platform Mühendisi

#### CI/CD

**CI/CD hattı tasarlama** · `pipeline-design`

- Ne zaman: Aşamalar, kapılar, artefaktlar, ortamlar, terfi
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-design/SKILL.tr.md)

**Hat hatası analizi** · `pipeline-failure-triage`

- Ne zaman: Logları okur, nedeni bulur, çözüm önerir
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/pipeline-failure-triage/SKILL.tr.md)

**Dağıtım stratejisi seçme** · `deployment-strategy`

- Ne zaman: Blue-green, canary, rolling, feature flag
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/deployment-strategy/SKILL.tr.md)

**Ortam stratejisi** · `environment-strategy`

- Ne zaman: Ortam amaçları, eşdeğerlik, veri, erişim
- Dosya: [skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.tr.md](skills/07-devops-sre/devops-engineer/cicd/environment-strategy/SKILL.tr.md)

#### Altyapı ve Konteynerler

**Dockerfile inceleme** · `dockerfile-review`

- Ne zaman: Boyut, katmanlar, güvenlik, tekrarlanabilirlik
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/dockerfile-review/SKILL.tr.md)

**Kubernetes manifest inceleme** · `kubernetes-manifest-review`

- Ne zaman: Kaynaklar, probe'lar, güvenlik bağlamı, yüksek erişilebilirlik
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/kubernetes-manifest-review/SKILL.tr.md)

**Kod olarak altyapı incelemesi** · `iac-review`

- Ne zaman: Terraform/Bicep vb. için güvenlik, sapma, modülerlik
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/iac-review/SKILL.tr.md)

**Gizli bilgi yönetimi planı** · `secrets-management-plan`

- Ne zaman: Kasa, rotasyon, enjeksiyon, en az yetki
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/secrets-management-plan/SKILL.tr.md)

**Bulut maliyet incelemesi** · `finops-review`

- Ne zaman: İsraf, doğru boyutlandırma, taahhütler, etiketleme
- Dosya: [skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.tr.md](skills/07-devops-sre/devops-engineer/infrastructure/finops-review/SKILL.tr.md)

### Sürüm Yöneticisi

#### Sürüm Yönetimi

**Sürüm planı yazma** · `release-plan`

- Ne zaman: İçerik, takvim, sorumlular, iletişim, geri dönüş
- Dosya: [skills/07-devops-sre/release-manager/release/release-plan/SKILL.tr.md](skills/07-devops-sre/release-manager/release/release-plan/SKILL.tr.md)

**Sürüm notları yazma** · `release-notes`

- Ne zaman: Özellikler, düzeltmeler, kırıcı değişiklikler, bilinen sorunlar
- Dosya: [skills/07-devops-sre/release-manager/release/release-notes/SKILL.tr.md](skills/07-devops-sre/release-manager/release/release-notes/SKILL.tr.md)

**Dağıtım kontrol listesi** · `deployment-checklist`

- Ne zaman: Dağıtım öncesi, sırası ve sonrası kontroller
- Dosya: [skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.tr.md](skills/07-devops-sre/release-manager/release/deployment-checklist/SKILL.tr.md)

**Geri dönüş planı** · `rollback-plan`

- Ne zaman: Tetikleyiciler, adımlar, veri konuları, doğrulama
- Dosya: [skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.tr.md](skills/07-devops-sre/release-manager/release/rollback-plan/SKILL.tr.md)

**Yayına alma kararı** · `go-no-go`

- Ne zaman: Kriterler, kanıtlar, karar kaydı
- Dosya: [skills/07-devops-sre/release-manager/release/go-no-go/SKILL.tr.md](skills/07-devops-sre/release-manager/release/go-no-go/SKILL.tr.md)

**Sürüm numarası belirleme** · `semantic-versioning`

- Ne zaman: Değişiklik listesinden SemVer uygular
- Dosya: [skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.tr.md](skills/07-devops-sre/release-manager/release/semantic-versioning/SKILL.tr.md)

### Site Güvenilirlik Mühendisi

#### Güvenilirlik

**SLI ve SLO tanımlama** · `slo-definition`

- Ne zaman: Kullanıcı odaklı göstergeler, hedefler, zaman pencereleri
- Dosya: [skills/07-devops-sre/sre/reliability/slo-definition/SKILL.tr.md](skills/07-devops-sre/sre/reliability/slo-definition/SKILL.tr.md)

**Hata bütçesi politikası** · `error-budget-policy`

- Ne zaman: Bütçe tükendiğinde yapılacaklar
- Dosya: [skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.tr.md](skills/07-devops-sre/sre/reliability/error-budget-policy/SKILL.tr.md)

**Alarm tasarımı** · `alert-design`

- Ne zaman: Belirti bazlı, aksiyon alınabilir, burn-rate alarmları
- Dosya: [skills/07-devops-sre/sre/reliability/alert-design/SKILL.tr.md](skills/07-devops-sre/sre/reliability/alert-design/SKILL.tr.md)

**Gözlemlenebilirlik planı** · `observability-plan`

- Ne zaman: Servis başına log, metrik, iz ve panolar
- Dosya: [skills/07-devops-sre/sre/reliability/observability-plan/SKILL.tr.md](skills/07-devops-sre/sre/reliability/observability-plan/SKILL.tr.md)

**Kapasite planlama** · `capacity-planning`

- Ne zaman: Talep ve kaynakları pay bırakarak öngörür
- Dosya: [skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.tr.md](skills/07-devops-sre/sre/reliability/capacity-planning/SKILL.tr.md)

**Kaos deneyi tasarlama** · `chaos-experiment`

- Ne zaman: Hipotez, etki alanı, durdurma koşulları
- Dosya: [skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.tr.md](skills/07-devops-sre/sre/reliability/chaos-experiment/SKILL.tr.md)

**Felaket kurtarma planı** · `dr-plan`

- Ne zaman: RTO/RPO, senaryolar, prosedürler, testler
- Dosya: [skills/07-devops-sre/sre/reliability/dr-plan/SKILL.tr.md](skills/07-devops-sre/sre/reliability/dr-plan/SKILL.tr.md)

#### Olay Yönetimi

**Runbook yazma** · `runbook`

- Ne zaman: Belirti, teşhis, çözüm, eskalasyon
- Dosya: [skills/07-devops-sre/sre/incident/runbook/SKILL.tr.md](skills/07-devops-sre/sre/incident/runbook/SKILL.tr.md)

**Olay müdahalesi yürütme** · `incident-response`

- Ne zaman: Roller, önem derecesi, zaman çizelgesi, hafifletme adımları
- Dosya: [skills/07-devops-sre/sre/incident/incident-response/SKILL.tr.md](skills/07-devops-sre/sre/incident/incident-response/SKILL.tr.md)

**Olay iletişimi yazma** · `incident-communication`

- Ne zaman: Aşama bazında iç ve durum sayfası güncellemeleri
- Dosya: [skills/07-devops-sre/sre/incident/incident-communication/SKILL.tr.md](skills/07-devops-sre/sre/incident/incident-communication/SKILL.tr.md)

**Suçlamasız olay sonrası analiz** · `postmortem`

- Ne zaman: Zaman çizelgesi, etki, kök nedenler, aksiyonlar
- Dosya: [skills/07-devops-sre/sre/incident/postmortem/SKILL.tr.md](skills/07-devops-sre/sre/incident/postmortem/SKILL.tr.md)

**Nöbet devri** · `on-call-handover`

- Ne zaman: Açık olaylar, riskler, değişiklikler, izlenecekler
- Dosya: [skills/07-devops-sre/sre/incident/on-call-handover/SKILL.tr.md](skills/07-devops-sre/sre/incident/on-call-handover/SKILL.tr.md)

## Veri ve Yapay Zeka

### Veri Mimarı

#### Veri Modelleme

**Kavramsal veri modeli** · `conceptual-data-model`

- Ne zaman: İş dilinde varlıklar ve ilişkiler
- Dosya: [skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.tr.md](skills/08-data/data-architect/modeling/conceptual-data-model/SKILL.tr.md)

**Mantıksal veri modeli** · `logical-data-model`

- Ne zaman: Normalize varlıklar, nitelikler, anahtarlar
- Dosya: [skills/08-data/data-architect/modeling/logical-data-model/SKILL.tr.md](skills/08-data/data-architect/modeling/logical-data-model/SKILL.tr.md)

**Boyutsal model tasarlama** · `dimensional-model`

- Ne zaman: Olgular, boyutlar, tanecik, SCD tipleri
- Dosya: [skills/08-data/data-architect/modeling/dimensional-model/SKILL.tr.md](skills/08-data/data-architect/modeling/dimensional-model/SKILL.tr.md)

**Data Vault modeli tasarlama** · `data-vault-model`

- Ne zaman: Hub, link, satellite yapıları
- Dosya: [skills/08-data/data-architect/modeling/data-vault-model/SKILL.tr.md](skills/08-data/data-architect/modeling/data-vault-model/SKILL.tr.md)

**Veri platformu tasarlama** · `data-platform-architecture`

- Ne zaman: Lakehouse/warehouse/mesh katmanları ve akışları
- Dosya: [skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.tr.md](skills/08-data/data-architect/modeling/data-platform-architecture/SKILL.tr.md)

**Veri sözleşmesi yazma** · `data-contract`

- Ne zaman: Şema, anlam, SLA, sahiplik, sürümleme
- Dosya: [skills/08-data/data-architect/modeling/data-contract/SKILL.tr.md](skills/08-data/data-architect/modeling/data-contract/SKILL.tr.md)

#### Veri Yönetişimi

**Veri kataloğu kaydı** · `data-catalog-entry`

- Ne zaman: Açıklama, sahip, köken, kalite, hassasiyet
- Dosya: [skills/08-data/data-architect/governance/data-catalog-entry/SKILL.tr.md](skills/08-data/data-architect/governance/data-catalog-entry/SKILL.tr.md)

**Veri hassasiyet sınıflandırması** · `data-classification`

- Ne zaman: KVKK/GDPR kapsamında kişisel/özel nitelikli veri etiketleme
- Dosya: [skills/08-data/data-architect/governance/data-classification/SKILL.tr.md](skills/08-data/data-architect/governance/data-classification/SKILL.tr.md)

**Veri kalitesi kuralları** · `data-quality-rules`

- Ne zaman: Bütünlük, geçerlilik, teklik, güncellik kontrolleri
- Dosya: [skills/08-data/data-architect/governance/data-quality-rules/SKILL.tr.md](skills/08-data/data-architect/governance/data-quality-rules/SKILL.tr.md)

**Veri kökeni dokümantasyonu** · `data-lineage-doc`

- Ne zaman: Dönüşümleriyle kaynaktan tüketime akış
- Dosya: [skills/08-data/data-architect/governance/data-lineage-doc/SKILL.tr.md](skills/08-data/data-architect/governance/data-lineage-doc/SKILL.tr.md)

**Ana veri yönetimi tanımlama** · `master-data-strategy`

- Ne zaman: Altın kayıt, eşleştirme/birleştirme, veri sorumluluğu
- Dosya: [skills/08-data/data-architect/governance/master-data-strategy/SKILL.tr.md](skills/08-data/data-architect/governance/master-data-strategy/SKILL.tr.md)

**Veri saklama politikası** · `retention-policy`

- Ne zaman: Saklama süreleri, arşivleme, silme kuralları
- Dosya: [skills/08-data/data-architect/governance/retention-policy/SKILL.tr.md](skills/08-data/data-architect/governance/retention-policy/SKILL.tr.md)

### Veri Mühendisi

#### Veri Hatları

**Veri hattı tanımlama** · `pipeline-spec`

- Ne zaman: Kaynaklar, zamanlama, dönüşümler, hedefler, SLA
- Dosya: [skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.tr.md](skills/08-data/data-engineer/pipelines/pipeline-spec/SKILL.tr.md)

**Kaynak-hedef eşleme dokümanı** · `source-to-target-mapping`

- Ne zaman: Dönüşüm mantığıyla sütun düzeyinde eşleme
- Dosya: [skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.tr.md](skills/08-data/data-engineer/pipelines/source-to-target-mapping/SKILL.tr.md)

**Artımlı yükleme tasarımı** · `incremental-load-design`

- Ne zaman: CDC, watermark, idempotency, geç gelen veri
- Dosya: [skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.tr.md](skills/08-data/data-engineer/pipelines/incremental-load-design/SKILL.tr.md)

**Veri hattı hata analizi** · `pipeline-failure-analysis`

- Ne zaman: Kök neden, veri etkisi, geriye dönük yükleme planı
- Dosya: [skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.tr.md](skills/08-data/data-engineer/pipelines/pipeline-failure-analysis/SKILL.tr.md)

**Şema evrimi planlama** · `schema-evolution-plan`

- Ne zaman: Geriye/ileriye uyumlu değişiklikler ve geçiş
- Dosya: [skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.tr.md](skills/08-data/data-engineer/pipelines/schema-evolution-plan/SKILL.tr.md)

### Veritabanı Yöneticisi

#### Veritabanı Operasyonları

**Yavaş sorgu iyileştirme** · `query-optimization`

- Ne zaman: Çalışma planını okur, yeniden yazım/indeks önerir
- Dosya: [skills/08-data/dba/database/query-optimization/SKILL.tr.md](skills/08-data/dba/database/query-optimization/SKILL.tr.md)

**İndeks önerisi** · `index-recommendation`

- Ne zaman: Yazma maliyeti dengesiyle iş yüküne göre indeksler
- Dosya: [skills/08-data/dba/database/index-recommendation/SKILL.tr.md](skills/08-data/dba/database/index-recommendation/SKILL.tr.md)

**Şema geçiş planı** · `schema-migration-plan`

- Ne zaman: Kesintisiz adımlar, geri dönüş, doğrulama
- Dosya: [skills/08-data/dba/database/schema-migration-plan/SKILL.tr.md](skills/08-data/dba/database/schema-migration-plan/SKILL.tr.md)

**Yedekleme ve geri yükleme planı** · `backup-restore-plan`

- Ne zaman: Sıklık, saklama, geri yükleme testleri, RPO/RTO
- Dosya: [skills/08-data/dba/database/backup-restore-plan/SKILL.tr.md](skills/08-data/dba/database/backup-restore-plan/SKILL.tr.md)

**Veritabanı sağlık kontrolü** · `database-health-check`

- Ne zaman: Beklemeler, kilitler, büyüme, parçalanma, yapılandırma
- Dosya: [skills/08-data/dba/database/database-health-check/SKILL.tr.md](skills/08-data/dba/database/database-health-check/SKILL.tr.md)

### Veri / BI Analisti

#### Analitik ve Raporlama

**Analiz planı yazma** · `analysis-plan`

- Ne zaman: Soru, hipotezler, veri, yöntem, çıktı
- Dosya: [skills/08-data/data-analyst/analytics/analysis-plan/SKILL.tr.md](skills/08-data/data-analyst/analytics/analysis-plan/SKILL.tr.md)

**Gösterge paneli tanımlama** · `dashboard-spec`

- Ne zaman: Kitle, sorular, KPI'lar, görseller, filtreler
- Dosya: [skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.tr.md](skills/08-data/data-analyst/analytics/dashboard-spec/SKILL.tr.md)

**İçgörü özeti yazma** · `insight-summary`

- Ne zaman: Veri sonuçlarından "ne anlama geliyor" anlatısı
- Dosya: [skills/08-data/data-analyst/analytics/insight-summary/SKILL.tr.md](skills/08-data/data-analyst/analytics/insight-summary/SKILL.tr.md)

**Metriği kesin tanımlama** · `metric-definition`

- Ne zaman: Formül, filtreler, tanecik, uç durumlar
- Dosya: [skills/08-data/data-analyst/analytics/metric-definition/SKILL.tr.md](skills/08-data/data-analyst/analytics/metric-definition/SKILL.tr.md)

**Veri setini keşfetme** · `data-exploration`

- Ne zaman: Dağılımları, boş değerleri, aykırı değerleri ve korelasyonları profiller
- Dosya: [skills/08-data/data-analyst/analytics/data-exploration/SKILL.tr.md](skills/08-data/data-analyst/analytics/data-exploration/SKILL.tr.md)

**A/B testi analizi** · `ab-test-analysis`

- Ne zaman: Anlamlılık, etki büyüklüğü, koruyucu metrikler, karar
- Dosya: [skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.tr.md](skills/08-data/data-analyst/analytics/ab-test-analysis/SKILL.tr.md)

### Veri Bilimci / ML ve YZ Mühendisi

#### Makine Öğrenmesi

**ML problemini tanımlama** · `ml-problem-framing`

- Ne zaman: Hedef, öznitelikler, başarı metriği, taban çizgisi, fizibilite
- Dosya: [skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/ml-problem-framing/SKILL.tr.md)

**Öznitelik mühendisliği planı** · `feature-engineering-plan`

- Ne zaman: Aday öznitelikler, sızıntı kontrolleri, dönüşümler
- Dosya: [skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/feature-engineering-plan/SKILL.tr.md)

**Model değerlendirme raporu** · `model-evaluation-report`

- Ne zaman: Metrikler, dilimler, hatalar, adillik, karşılaştırma
- Dosya: [skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/model-evaluation-report/SKILL.tr.md)

**Model kartı yazma** · `model-card`

- Ne zaman: Kullanım amacı, veri, performans, sınırlar, etik
- Dosya: [skills/08-data/ml-ai-engineer/ml/model-card/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/model-card/SKILL.tr.md)

**Model izleme planı** · `ml-monitoring-plan`

- Ne zaman: Kayma, performans düşüşü, yeniden eğitim tetikleyicileri
- Dosya: [skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.tr.md](skills/08-data/ml-ai-engineer/ml/ml-monitoring-plan/SKILL.tr.md)

#### Üretken Yapay Zeka

**Prompt tasarlama** · `prompt-design`

- Ne zaman: Rol, görev, bağlam, kısıtlar, örnekler, çıktı formatı
- Dosya: [skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/prompt-design/SKILL.tr.md)

**LLM değerlendirme seti** · `llm-eval-set`

- Ne zaman: Bir LLM özelliği için test durumları, puanlama kriterleri ve değerlendiriciler
- Dosya: [skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/llm-eval-set/SKILL.tr.md)

**RAG sistemi tasarlama** · `rag-design`

- Ne zaman: Parçalama, embedding, erişim, yeniden sıralama, dayanak
- Dosya: [skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/rag-design/SKILL.tr.md)

**Yeni YZ skill'i yazma** · `ai-skill-authoring`

- Ne zaman: Bu kütüphanenin kurallarına uygun taşınabilir SKILL.md yazar
- Dosya: [skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/ai-skill-authoring/SKILL.tr.md)

**YZ kullanım senaryosu değerlendirmesi** · `ai-use-case-assessment`

- Ne zaman: Değer, fizibilite, risk, veri hazırlığı
- Dosya: [skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.tr.md](skills/08-data/ml-ai-engineer/genai/ai-use-case-assessment/SKILL.tr.md)

## Güvenlik ve Uyum

### Güvenlik Mimarı / Uygulama Güvenliği Mühendisi

#### Güvenli Tasarım

**Tehdit modeli oluşturma** · `threat-model`

- Ne zaman: Eleman bazında STRIDE ve önlemler
- Dosya: [skills/09-security/security-engineer/design/threat-model/SKILL.tr.md](skills/09-security/security-engineer/design/threat-model/SKILL.tr.md)

**Güvenlik gereksinimleri** · `security-requirements`

- Ne zaman: OWASP ASVS uyumlu gereksinimler
- Dosya: [skills/09-security/security-engineer/design/security-requirements/SKILL.tr.md](skills/09-security/security-engineer/design/security-requirements/SKILL.tr.md)

**Kimlik doğrulama ve yetkilendirme tasarımı** · `authn-authz-design`

- Ne zaman: Akışlar, token'lar, roller/claim'ler, en az yetki
- Dosya: [skills/09-security/security-engineer/design/authn-authz-design/SKILL.tr.md](skills/09-security/security-engineer/design/authn-authz-design/SKILL.tr.md)

#### Güvenlik Değerlendirmesi

**Güvenli kod incelemesi** · `secure-code-review`

- Ne zaman: OWASP Top 10 ve CWE odaklı inceleme
- Dosya: [skills/09-security/security-engineer/assessment/secure-code-review/SKILL.tr.md](skills/09-security/security-engineer/assessment/secure-code-review/SKILL.tr.md)

**Zafiyet önceliklendirme** · `vulnerability-triage`

- Ne zaman: CVSS, istismar edilebilirlik, erişilebilirlik, düzeltme planı
- Dosya: [skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.tr.md](skills/09-security/security-engineer/assessment/vulnerability-triage/SKILL.tr.md)

**Bağımlılık zafiyetleri incelemesi** · `dependency-vulnerability-review`

- Ne zaman: SCA bulguları, güncelleme yolları, risk kabulü
- Dosya: [skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.tr.md](skills/09-security/security-engineer/assessment/dependency-vulnerability-review/SKILL.tr.md)

**Sızma testi kapsamı** · `pentest-scope`

- Ne zaman: Hedefler, çalışma kuralları, hariç tutulanlar, raporlama
- Dosya: [skills/09-security/security-engineer/assessment/pentest-scope/SKILL.tr.md](skills/09-security/security-engineer/assessment/pentest-scope/SKILL.tr.md)

**Güvenlik bulgusu yazma** · `security-finding-report`

- Ne zaman: Açıklama, etki, tekrar adımları, çözüm
- Dosya: [skills/09-security/security-engineer/assessment/security-finding-report/SKILL.tr.md](skills/09-security/security-engineer/assessment/security-finding-report/SKILL.tr.md)

#### Güvenlik Operasyonları

**Güvenlik olayına müdahale** · `security-incident-response`

- Ne zaman: Sınırlandır, temizle, kurtar, bildir
- Dosya: [skills/09-security/security-engineer/operations/security-incident-response/SKILL.tr.md](skills/09-security/security-engineer/operations/security-incident-response/SKILL.tr.md)

**Erişim yetkisi gözden geçirme** · `access-review`

- Ne zaman: Fazla, sahipsiz ve çakışan yetkileri tespit eder
- Dosya: [skills/09-security/security-engineer/operations/access-review/SKILL.tr.md](skills/09-security/security-engineer/operations/access-review/SKILL.tr.md)

### Yönetişim, Risk ve Uyum

#### Uyum

**Kişisel veri etki değerlendirmesi** · `privacy-impact-assessment`

- Ne zaman: Bir özellik veya sistem için KVKK/GDPR etki değerlendirmesi
- Dosya: [skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.tr.md](skills/09-security/compliance/compliance/privacy-impact-assessment/SKILL.tr.md)

**Kontrolleri standarda eşleme** · `control-mapping`

- Ne zaman: ISO 27001 / SOC 2 kontrol-kanıt eşlemesi
- Dosya: [skills/09-security/compliance/compliance/control-mapping/SKILL.tr.md](skills/09-security/compliance/compliance/control-mapping/SKILL.tr.md)

**Güvenlik/BT politikası yazma** · `policy-writing`

- Ne zaman: Amaç, kapsam, kurallar, roller, istisnalar
- Dosya: [skills/09-security/compliance/compliance/policy-writing/SKILL.tr.md](skills/09-security/compliance/compliance/policy-writing/SKILL.tr.md)

**Denetime hazırlık** · `audit-preparation`

- Ne zaman: Kanıt listesi, eksikler, sorumlular, takvim
- Dosya: [skills/09-security/compliance/compliance/audit-preparation/SKILL.tr.md](skills/09-security/compliance/compliance/audit-preparation/SKILL.tr.md)

**BT risk değerlendirmesi** · `it-risk-assessment`

- Ne zaman: Varlık, tehdit, zafiyet, olasılık, etki
- Dosya: [skills/09-security/compliance/compliance/it-risk-assessment/SKILL.tr.md](skills/09-security/compliance/compliance/it-risk-assessment/SKILL.tr.md)

## UX / UI Tasarım

### UX Araştırmacısı

#### Kullanıcı Araştırması

**Araştırma planı** · `research-plan`

- Ne zaman: Hedefler, sorular, yöntemler, katılımcılar, takvim
- Dosya: [skills/10-design/ux-researcher/research/research-plan/SKILL.tr.md](skills/10-design/ux-researcher/research/research-plan/SKILL.tr.md)

**Kullanılabilirlik testi senaryosu** · `usability-test-script`

- Ne zaman: Görevler, yönlendirmeler, başarı kriterleri, kapanış
- Dosya: [skills/10-design/ux-researcher/research/usability-test-script/SKILL.tr.md](skills/10-design/ux-researcher/research/usability-test-script/SKILL.tr.md)

**Araştırma bulgularını sentezleme** · `research-synthesis`

- Ne zaman: Benzerlik gruplamasıyla içgörü ve öneriler
- Dosya: [skills/10-design/ux-researcher/research/research-synthesis/SKILL.tr.md](skills/10-design/ux-researcher/research/research-synthesis/SKILL.tr.md)

**Katılımcı eleme anketi** · `screener-survey`

- Ne zaman: Doğru kullanıcıları seçmek için kriterler ve sorular
- Dosya: [skills/10-design/ux-researcher/research/screener-survey/SKILL.tr.md](skills/10-design/ux-researcher/research/screener-survey/SKILL.tr.md)

### UX / UI Tasarımcı

#### Etkileşim ve Görsel Tasarım

**Kullanıcı akışı tasarlama** · `user-flow`

- Ne zaman: Adımlar, kararlar, giriş/çıkış, hata yolları
- Dosya: [skills/10-design/ux-ui-designer/design/user-flow/SKILL.tr.md](skills/10-design/ux-ui-designer/design/user-flow/SKILL.tr.md)

**Bilgi mimarisi oluşturma** · `information-architecture`

- Ne zaman: Navigasyon, hiyerarşi, etiketleme, kart sıralama planı
- Dosya: [skills/10-design/ux-ui-designer/design/information-architecture/SKILL.tr.md](skills/10-design/ux-ui-designer/design/information-architecture/SKILL.tr.md)

**Wireframe tarifi** · `wireframe-spec`

- Ne zaman: Yerleşim, bileşenler, içerik önceliği, durumlar
- Dosya: [skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.tr.md](skills/10-design/ux-ui-designer/design/wireframe-spec/SKILL.tr.md)

**Sezgisel değerlendirme** · `heuristic-evaluation`

- Ne zaman: Önem derecesiyle Nielsen'in 10 ilkesi
- Dosya: [skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.tr.md](skills/10-design/ux-ui-designer/design/heuristic-evaluation/SKILL.tr.md)

**Tasarım eleştirisi** · `design-critique`

- Ne zaman: Hedef bazlı, somut, önceliklendirilmiş geri bildirim
- Dosya: [skills/10-design/ux-ui-designer/design/design-critique/SKILL.tr.md](skills/10-design/ux-ui-designer/design/design-critique/SKILL.tr.md)

**Tasarım sistemi bileşeni tanımlama** · `design-system-component-spec`

- Ne zaman: Anatomi, varyantlar, durumlar, token'lar, kullanım kuralları
- Dosya: [skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.tr.md](skills/10-design/ux-ui-designer/design/design-system-component-spec/SKILL.tr.md)

**Tasarım teslimi hazırlama** · `design-handoff`

- Ne zaman: Geliştiriciler için ölçüler, etkileşimler, uç durumlar, varlıklar
- Dosya: [skills/10-design/ux-ui-designer/design/design-handoff/SKILL.tr.md](skills/10-design/ux-ui-designer/design/design-handoff/SKILL.tr.md)

### UX Yazarı / İçerik Tasarımcısı

#### İçerik

**Mikro metin yazma** · `microcopy`

- Ne zaman: Butonlar, etiketler, ipuçları, boş durumlar
- Dosya: [skills/10-design/ux-writer/content/microcopy/SKILL.tr.md](skills/10-design/ux-writer/content/microcopy/SKILL.tr.md)

**Hata mesajı yazma** · `error-message-writing`

- Ne zaman: Ne oldu, neden, şimdi ne yapmalı
- Dosya: [skills/10-design/ux-writer/content/error-message-writing/SKILL.tr.md](skills/10-design/ux-writer/content/error-message-writing/SKILL.tr.md)

**Ses ve ton rehberi** · `voice-and-tone-guide`

- Ne zaman: Yap/yapma örnekleriyle marka sesi ilkeleri
- Dosya: [skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.tr.md](skills/10-design/ux-writer/content/voice-and-tone-guide/SKILL.tr.md)

## Destek ve BT Operasyonları

### Destek Mühendisi (L1-L3)

#### Kayıt Yönetimi

**Destek kaydı sınıflandırma** · `ticket-triage`

- Ne zaman: Kategori, öncelik, etki, yönlendirme
- Dosya: [skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/ticket-triage/SKILL.tr.md)

**Destek kaydı yanıtı** · `ticket-response`

- Ne zaman: Empatik, net, sonraki adıma odaklı yanıt
- Dosya: [skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/ticket-response/SKILL.tr.md)

**Eskalasyon için kayıt özeti** · `ticket-escalation-summary`

- Ne zaman: Bir üst seviye için bağlam, denenenler, kanıt
- Dosya: [skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/ticket-escalation-summary/SKILL.tr.md)

**Bilinen hata makalesi** · `known-error-article`

- Ne zaman: Belirti, neden, geçici çözüm, kalıcı çözüm durumu
- Dosya: [skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/known-error-article/SKILL.tr.md)

**Müşteriye kesinti bildirimi** · `customer-outage-notice`

- Ne zaman: Etki, durum, tahmini süre, geçici çözüm
- Dosya: [skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.tr.md](skills/11-support-ops/support-engineer/tickets/customer-outage-notice/SKILL.tr.md)

### BT Hizmet Yönetimi

#### ITSM Süreçleri

**Problem yönetimi** · `problem-management`

- Ne zaman: Olayları ilişkilendirir, kök nedeni bulur, bilinen hata kaydı açar
- Dosya: [skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/problem-management/SKILL.tr.md)

**Değişiklik talebi (RFC) yazma** · `change-request-rfc`

- Ne zaman: CAB için açıklama, risk, geri alma, takvim
- Dosya: [skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/change-request-rfc/SKILL.tr.md)

**SLA ihlal analizi** · `sla-breach-analysis`

- Ne zaman: Örüntüler, nedenler, iyileştirme aksiyonları
- Dosya: [skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/sla-breach-analysis/SKILL.tr.md)

**Hizmet kataloğu kaydı** · `service-catalog-entry`

- Ne zaman: Hizmet tanımı, SLA'lar, talep süreci
- Dosya: [skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.tr.md](skills/11-support-ops/it-service-management/itsm/service-catalog-entry/SKILL.tr.md)

## Teknik Yazarlık

### Teknik Yazar

#### Ürün Dokümantasyonu

**Kullanıcı kılavuzu yazma** · `user-guide`

- Ne zaman: Adımlar ve ekran görüntüsü yer tutucularıyla görev bazlı kılavuz
- Dosya: [skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/user-guide/SKILL.tr.md)

**Eğitim (tutorial) yazma** · `tutorial`

- Ne zaman: Öğrenme odaklı adım adım anlatım (Diátaxis)
- Dosya: [skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/tutorial/SKILL.tr.md)

**Nasıl yapılır rehberi** · `how-to-guide`

- Ne zaman: Hedef odaklı tarif (Diátaxis)
- Dosya: [skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/how-to-guide/SKILL.tr.md)

**Doküman bilgi mimarisi** · `docs-information-architecture`

- Ne zaman: Dokümanları eğitim, nasıl yapılır, referans ve açıklama olarak düzenler
- Dosya: [skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/docs-information-architecture/SKILL.tr.md)

**Stil rehberi kontrolü** · `style-guide-check`

- Ne zaman: Terminoloji ve yazım kurallarıyla tutarlılık
- Dosya: [skills/12-technical-writing/technical-writer/docs/style-guide-check/SKILL.tr.md](skills/12-technical-writing/technical-writer/docs/style-guide-check/SKILL.tr.md)

## Mühendislik Yönetimi ve Liderlik

### Mühendislik Yöneticisi

#### İnsan Yönetimi

**Birebir görüşme hazırlığı** · `one-on-one-prep`

- Ne zaman: Gündem, sorular, önceki görüşmeden takipler
- Dosya: [skills/13-leadership/engineering-manager/people/one-on-one-prep/SKILL.tr.md](skills/13-leadership/engineering-manager/people/one-on-one-prep/SKILL.tr.md)

**Birebir görüşme notları** · `one-on-one-notes`

- Ne zaman: Konular, taahhütler, kariyer sinyalleri
- Dosya: [skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.tr.md](skills/13-leadership/engineering-manager/people/one-on-one-notes/SKILL.tr.md)

**Performans değerlendirmesi yazma** · `performance-review`

- Ne zaman: Kanıta dayalı, yetkinliklerle uyumlu, dengeli
- Dosya: [skills/13-leadership/engineering-manager/people/performance-review/SKILL.tr.md](skills/13-leadership/engineering-manager/people/performance-review/SKILL.tr.md)

**Bireysel hedef belirleme** · `goal-setting`

- Ne zaman: Ekip sonuçlarına ve gelişime bağlı SMART hedefler
- Dosya: [skills/13-leadership/engineering-manager/people/goal-setting/SKILL.tr.md](skills/13-leadership/engineering-manager/people/goal-setting/SKILL.tr.md)

**Kariyer gelişim planı** · `career-development-plan`

- Ne zaman: Mevcut ve hedef seviye, eksikler, aksiyonlar
- Dosya: [skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.tr.md](skills/13-leadership/engineering-manager/people/career-development-plan/SKILL.tr.md)

**Performans iyileştirme planı** · `underperformance-plan`

- Ne zaman: Beklentiler, destek, ara hedefler, sonuçlar
- Dosya: [skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.tr.md](skills/13-leadership/engineering-manager/people/underperformance-plan/SKILL.tr.md)

**Takdir mesajı yazma** · `recognition-message`

- Ne zaman: Somut, etki odaklı takdir
- Dosya: [skills/13-leadership/engineering-manager/people/recognition-message/SKILL.tr.md](skills/13-leadership/engineering-manager/people/recognition-message/SKILL.tr.md)

#### İşe Alım

**İş ilanı yazma** · `job-description`

- Ne zaman: Rolün amacı, sorumluluklar, gereksinimler, kapsayıcı dil
- Dosya: [skills/13-leadership/engineering-manager/hiring/job-description/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/job-description/SKILL.tr.md)

**Mülakat süreci tasarlama** · `interview-plan`

- Ne zaman: Aşamalar, aşama başına yetkinlikler, mülakatçılar
- Dosya: [skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/interview-plan/SKILL.tr.md)

**Teknik mülakat soruları** · `technical-interview-questions`

- Ne zaman: Seviyeye göre ayarlanmış sorular ve puanlama
- Dosya: [skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/technical-interview-questions/SKILL.tr.md)

**Mülakat değerlendirme formu** · `interview-scorecard`

- Ne zaman: Yetkinlik başına kanıt ve işe alım önerisi
- Dosya: [skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/interview-scorecard/SKILL.tr.md)

**Aday değerlendirme toplantısı özeti** · `candidate-debrief`

- Ne zaman: Sinyalleri birleştirip karara bağlar
- Dosya: [skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/candidate-debrief/SKILL.tr.md)

**30-60-90 günlük oryantasyon planı** · `onboarding-plan-30-60-90`

- Ne zaman: Yeni çalışan için hedefler ve ara hedefler
- Dosya: [skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.tr.md](skills/13-leadership/engineering-manager/hiring/onboarding-plan-30-60-90/SKILL.tr.md)

#### Ekip ve Organizasyon Tasarımı

**Ekip topolojisi tasarlama** · `team-topology`

- Ne zaman: Akışa hizalı, platform, destekleyici, alt sistem ekipleri
- Dosya: [skills/13-leadership/engineering-manager/team/team-topology/SKILL.tr.md](skills/13-leadership/engineering-manager/team/team-topology/SKILL.tr.md)

**Rol tanımlama** · `role-definition`

- Ne zaman: Sorumluluklar, karar yetkileri, arayüzler
- Dosya: [skills/13-leadership/engineering-manager/team/role-definition/SKILL.tr.md](skills/13-leadership/engineering-manager/team/role-definition/SKILL.tr.md)

**Kariyer basamakları oluşturma** · `career-ladder`

- Ne zaman: Yetkinlik bazında beklentileriyle seviyeler
- Dosya: [skills/13-leadership/engineering-manager/team/career-ladder/SKILL.tr.md](skills/13-leadership/engineering-manager/team/career-ladder/SKILL.tr.md)

**Mühendislik metrikleri incelemesi (DORA/SPACE)** · `engineering-metrics-review`

- Ne zaman: Metrikleri manipülasyona açık hale getirmeden teslimat metriklerini yorumlar
- Dosya: [skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.tr.md](skills/13-leadership/engineering-manager/team/engineering-metrics-review/SKILL.tr.md)

### CTO / Başkan Yardımcısı / Direktör

#### Teknoloji Stratejisi

**Teknoloji stratejisi yazma** · `technology-strategy`

- Ne zaman: Teşhis, yol gösterici politika, tutarlı aksiyonlar
- Dosya: [skills/13-leadership/executive/strategy/technology-strategy/SKILL.tr.md](skills/13-leadership/executive/strategy/technology-strategy/SKILL.tr.md)

**Çeyreklik planlama** · `quarterly-planning`

- Ne zaman: Kapasite, öncelikler, taahhütler, ödünleşimler
- Dosya: [skills/13-leadership/executive/strategy/quarterly-planning/SKILL.tr.md](skills/13-leadership/executive/strategy/quarterly-planning/SKILL.tr.md)

**Bütçe teklifi yazma** · `budget-proposal`

- Ne zaman: Yatırımlar, işletim maliyetleri, gerekçe, senaryolar
- Dosya: [skills/13-leadership/executive/strategy/budget-proposal/SKILL.tr.md](skills/13-leadership/executive/strategy/budget-proposal/SKILL.tr.md)

**Tedarikçi değerlendirme (RFP)** · `vendor-evaluation`

- Ne zaman: Gereksinimler, puanlama modeli, karşılaştırma, öneri
- Dosya: [skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.tr.md](skills/13-leadership/executive/strategy/vendor-evaluation/SKILL.tr.md)

**Yönetim kurulu güncellemesi** · `board-update`

- Ne zaman: Öne çıkanlar, metrikler, riskler, talepler
- Dosya: [skills/13-leadership/executive/strategy/board-update/SKILL.tr.md](skills/13-leadership/executive/strategy/board-update/SKILL.tr.md)

**Organizasyon değişikliği iletişimi** · `org-change-communication`

- Ne zaman: Neden, ne değişiyor, ne değişmiyor, destek
- Dosya: [skills/13-leadership/executive/strategy/org-change-communication/SKILL.tr.md](skills/13-leadership/executive/strategy/org-change-communication/SKILL.tr.md)

## Ön Satış ve Danışmanlık

### Ön Satış / Çözüm Danışmanı

#### Teklif Süreci

**RFP analizi** · `rfp-analysis`

- Ne zaman: Gereksinimler, değerlendirme kriterleri, riskler, teklif ver/verme
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/rfp-analysis/SKILL.tr.md)

**RFP yanıtı yazma** · `rfp-response`

- Ne zaman: Her gereksinime uyumlu ve fayda odaklı yanıtlar
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/rfp-response/SKILL.tr.md)

**Teklif dokümanı yazma** · `proposal-writing`

- Ne zaman: Anlayış, çözüm, yaklaşım, plan, ekip, ticari koşullar
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/proposal-writing/SKILL.tr.md)

**Teklif için efor tahmini** · `effort-estimate-for-bid`

- Ne zaman: Varsayımlar ve yedek payla yukarıdan-aşağı/aşağıdan-yukarı tahmin
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/effort-estimate-for-bid/SKILL.tr.md)

**İş tanımı (SOW) yazma** · `statement-of-work`

- Ne zaman: Kapsam, teslimatlar, kabul, sorumluluklar, varsayımlar
- Dosya: [skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/bid/statement-of-work/SKILL.tr.md)

#### Danışmanlık

**Müşteri keşif çalıştayı** · `discovery-workshop`

- Ne zaman: Erken aşama için gündem, sorular ve çıktı
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/discovery-workshop/SKILL.tr.md)

**Müşteri mevcut durum değerlendirmesi** · `current-state-assessment`

- Ne zaman: Bulgular, olgunluk, sorunlar, öneriler
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/current-state-assessment/SKILL.tr.md)

**Fit-gap analizi** · `fit-gap-analysis`

- Ne zaman: Paket/standart yetenekleri gereksinimlerle karşılaştırır
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/fit-gap-analysis/SKILL.tr.md)

**Müşteri yönlendirme raporu** · `client-steering-report`

- Ne zaman: İlerleme, sağlanan değer, riskler, kararlar
- Dosya: [skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.tr.md](skills/14-presales-consulting/presales-consultant/consulting/client-steering-report/SKILL.tr.md)
