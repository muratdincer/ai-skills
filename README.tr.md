# Yazılım Ekipleri için YZ Skill'leri

[English](README.md)

Bir yazılım departmanındaki tüm rolleri kapsayan, araçtan bağımsız **420 YZ skill'i**. Kütüphane talep almadan ve toplantı özetinden mimari kararlara, test tasarımına, olay sonrası analize ve işe alıma kadar uzanıyor. Her skill, herhangi bir YZ asistanının uygulayabileceği küçük ve odaklı bir iş tanımıdır. Tüm skill'ler **Türkçe ve İngilizce** olarak hazırlandı.

- **Taşınabilir:** Açık Agent Skills formatında düz Markdown (`SKILL.md` + YAML başlığı). Yerleşik skill, kural dosyası, bilgi dosyası, sistem prompt'u veya yapıştırılan prompt olarak çalışır.
- **Parçalı:** Bir skill tek bir iş yapar ("gereksinimlerde eksik bulma", "aksiyon maddelerini çıkarma", "geri dönüş planı yazma"). Bu sayede skill'ler zincirlenebilir.
- **Güvenilir çıktı:** Her skill'in girdileri, numaralı adımları, çıktı şablonu, kalite kontrol listesi ve sık yapılan hataları vardır. Eksik bilgi işaretlenir, asla uydurulmaz.
- **Metodolojiden bağımsız:** Şelale, Scrum, Kanban, SAFe veya hibrit yapılarda kullanılabilir. Bkz. [METHODOLOGIES.tr.md](METHODOLOGIES.tr.md).

## Yapı

```
skills/<kategori>/<rol>/<alan>/<skill-id>/
├── SKILL.md      İngilizce
└── SKILL.tr.md   Türkçe
```

| # | Kategori | Roller |
|---|---|---|
| 00 | Ortak (roller arası) | Toplantılar, İletişim, Dokümantasyon, Problem çözme ve karar, Bilgi yönetimi |
| 01 | İş Analizi | İş Analisti, Sistem Analisti |
| 02 | Ürün Yönetimi | Ürün Yöneticisi, Ürün Sahibi |
| 03 | Proje ve Teslimat Yönetimi | Proje Yöneticisi, Scrum Master / Çevik Koç, Program Yöneticisi / PMO |
| 04 | Mimari | Kurumsal, Çözüm ve Yazılım Mimarı |
| 05 | Yazılım Geliştirme | Geliştirici (backend/frontend/mobil), Teknik Lider |
| 06 | Kalite Güvence ve Test | Test Analisti, Test Otomasyon Mühendisi, Performans Test Mühendisi |
| 07 | DevOps, SRE ve Platform | DevOps/Platform Mühendisi, Sürüm Yöneticisi, SRE |
| 08 | Veri ve Yapay Zeka | Veri Mimarı, Veri Mühendisi, Veritabanı Yöneticisi, Veri/BI Analisti, Veri Bilimci / ML ve YZ Mühendisi |
| 09 | Güvenlik ve Uyum | Güvenlik Mimarı / Uygulama Güvenliği Mühendisi, Yönetişim-Risk-Uyum |
| 10 | UX / UI Tasarım | UX Araştırmacısı, UX/UI Tasarımcı, UX Yazarı |
| 11 | Destek ve BT Operasyonları | Destek Mühendisi (L1-L3), BT Hizmet Yönetimi |
| 12 | Teknik Yazarlık | Teknik Yazar |
| 13 | Mühendislik Yönetimi ve Liderlik | Mühendislik Yöneticisi, CTO / Başkan Yardımcısı / Direktör |
| 14 | Ön Satış ve Danışmanlık | Ön Satış / Çözüm Danışmanı |

Tüm skill'lerle ağacın tamamı: [CATALOG.tr.md](CATALOG.tr.md).

## Hızlı başlangıç

```bash
git clone https://github.com/muratdincer/ai-skills.git && cd ai-skills

# Agent Skills uyumlu araçlar: skill'leri aracın skills klasörüne kopyala
python3 scripts/export.py skills --lang tr --dest ~/.claude/skills  # Türkçe
python3 scripts/export.py skills --dest ~/.claude/skills            # İngilizce

# Sohbet asistanları: her rol için bir bilgi dosyası
python3 scripts/export.py bundle --lang tr --role business-analyst --dest dist/is-analisti.md
```

Sonra yalnızca iste: *"Satıştan gelen talep bu, talep alma dokümanını oluştur ve eksikleri listele."*

Hiç kurulum yapmak istemiyor musun? Herhangi bir `SKILL.tr.md` dosyasını aç, sohbete yapıştır, ardından isteğini yaz.

## Dokümantasyon

| Doküman | İçerik |
|---|---|
| [USAGE.tr.md](USAGE.tr.md) | Farklı YZ araçlarına kurulum, dışa aktarma formatları, skill çağırma ve zincirleme |
| [GUIDE.tr.md](GUIDE.tr.md) | Her skill için ne zaman kullanılacağı ve örnek istek |
| [CATALOG.tr.md](CATALOG.tr.md) | Kategori / rol / alan / skill ağacının tamamı |
| [METHODOLOGIES.tr.md](METHODOLOGIES.tr.md) | Şelale, V-Modeli, Scrum, Kanban, XP, Yalın, SAFe, DevOps ve tasarım odaklı düşünmenin her adımında hangi skill'lerin kullanılacağı |
| [AUTHORING.md](AUTHORING.md) | Skill yazma ve bakım kuralları (İngilizce) |

## Katkı

1. Skill'i `catalog/catalog.txt` dosyasına ekle.
2. [AUTHORING.md](AUTHORING.md) kurallarına göre `SKILL.md` ve `SKILL.tr.md` dosyalarını yaz.
3. `python3 scripts/catalog.py && python3 scripts/sync.py && python3 scripts/guide.py` komutunu çalıştır.
4. Pull request aç. CI, `sync.py --check` çalıştırır.

## Teşekkür

Yapı ve uygulamalar aşağıdaki açık skill kütüphaneleri ve rehberlerle karşılaştırıldı, kısmen onlardan ilham alındı:
[Anthropic skill yazım rehberi](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills),
[obra/superpowers](https://github.com/obra/superpowers),
[deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills),
[product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills),
[phuryn/pm-skills](https://github.com/phuryn/pm-skills),
[45ck/business-analysis-skills](https://github.com/45ck/business-analysis-skills).
İçerik kopyalanmadı. Öz-kontrol döngüsü, önem etiketleri, talebin sözel isteğini altta yatan ihtiyaçtan ayırma ve eksiklerin yok/zayıf/ertelenmiş olarak sınıflandırılması gibi fikirler bu kütüphanenin formatında yeniden yazıldı.

## Lisans

[MIT](LICENSE)
