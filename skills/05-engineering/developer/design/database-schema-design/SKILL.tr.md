---
description: "Bir alan tanımından ilişkisel veritabanı şeması tasarlar: tablolar, kolonlar ve tipler, birincil ve yabancı anahtarlar, kısıtlar, erişim desenlerine dayalı indeksler ve migration betiği taslağı. Yeni bir özellik kalıcı depolamaya ihtiyaç duyduğunda, mevcut şema genişletilecekse ya da bir alan için tablolar, ER modeli, DDL veya indeks istendiğinde kullanılır."
related: "logical-data-model, data-requirements, schema-migration-plan, index-recommendation, aggregate-design"
prompt: "Toplantı odası rezervasyon özelliği için veritabanı şemasını tasarla: odalar, başlangıç/bitiş saatli rezervasyonlar, katılımcılar ve aynı odada çakışan rezervasyon olmaması."
---

# Veritabanı Şeması Tasarlama

## Amaç
Alanın değişmez kurallarını (invariant) veritabanında zorlayan, gerçek erişim desenlerini verimli karşılayan ve güvenli migration'larla evrilebilen bir şema üretmek.

## Ne zaman kullanılır
- Bir özellik saklanması gereken yeni varlıklar veya ilişkiler getiriyorsa.
- Mevcut bir şema genişletiliyor ve değişikliğin geriye dönük uyumlu kalması gerekiyorsa.
- Sorgu performansı veya veri bütünlüğü sorunları tablo tasarımını işaret ediyorsa.

## Ne zaman kullanılmaz
- Kurumsal veya sistemler arası veri modellemesi gerekiyorsa `logical-data-model` veya `conceptual-data-model` kullanılır.
- Yavaş bir sorgu için yalnızca indeks gerekiyorsa `index-recommendation` veya `query-optimization` kullanılır.
- Bir şema değişikliğini üretime almak gerekiyorsa `schema-migration-plan` kullanılır.

## Girdiler
Zorunlu:
- Kurallarıyla birlikte alan tanımı veya varlıklar ve hedef veritabanı motoru (ya da "ilişkisel, motordan bağımsız").

İsteğe bağlı, kaliteyi artırır:
- Temel okuma/yazma erişim desenleri ve beklenen hacimler, saklama ihtiyaçları, multi-tenancy modeli.
- İsimlendirme kuralları, mevcut şema, kimlik stratejisi, audit/soft delete politikası.

Motor bilinmiyorsa taşınabilir SQL yaz ve motora özgü seçimleri `[MOTORA-ÖZGÜ]` olarak işaretle.

## Süreç
1. Varlıkları, nitelikleri ve ilişkileri kardinaliteleriyle çıkar; değişmez kuralları düz dille listele ("bir odada çakışan rezervasyon olamaz").
2. Varsayılan olarak 3NF'e normalleştir; yalnızca adı konmuş bir erişim deseni için denormalize et ve tutarlılık maliyetini yaz.
3. Anahtarları seç: surrogate birincil anahtar stratejisi (sequence, dağıtık insert'ler için UUIDv7/ULID), doğal tekil anahtarlar `UNIQUE` kısıtı olarak.
4. Kolon tiplerini kesin seç: para için ayrı para birimi kolonuyla birlikte tam ondalık, UTC'de saat dilimli timestamp, sınırlı metin uzunlukları, check veya lookup tablosu olmadan enum için serbest metin yok.
5. Değişmez kuralları mümkün olduğunca veritabanında zorla: `NOT NULL`, `CHECK`, `UNIQUE`, bilinçli `ON DELETE` davranışlı yabancı anahtarlar, motor destekliyorsa exclusion veya kısmi unique kısıtlar.
6. İndeksleri erişim desenlerinden türet: join'lerde kullanılan her yabancı anahtar, filtre-sonra-sıralama düzeninde bileşik indeksler, yalnızca sıcak sorgular için covering indeksler; yazma maliyetini not et.
7. Kesişen kolonlara karar ver: tenant id, audit (oluşturan/güncelleyen ve zamanı), iyimser eşzamanlılık için version, soft delete (ve bunun tekillikle nasıl çalıştığı).
8. Kişisel veri kolonlarını işaretle; saklama ve maskeleme ihtiyaçlarını yaz.
9. DDL'i ve geriye dönük uyumlu bir migration taslağını yaz (genişlet, doldur, geçir, daralt).
10. Varsayımları ve açık soruları, özellikle hacimler ve silme kuralları üzerine listele.
11. Hedef devam ediyorsa şemayı güvenle devreye almak için `schema-migration-plan`, gerçek sorgu desenleri netleşince `index-recommendation` öner.

## Çıktı formatı
````markdown
# Şema Tasarımı: <özellik>
Motor: <motor veya motordan bağımsız> · Varsayımlar: <liste>

## Varlıklar ve Değişmez Kurallar
| Varlık | Temel nitelikler | Değişmez kurallar |

## Tablolar
### <tablo>
| Kolon | Tip | Null | Varsayılan | Kısıt | Notlar (kişisel veri?) |

## İlişkiler
| Kaynak | Hedef | Kardinalite | Silmede FK davranışı |

## İndeksler
| İndeks | Kolonlar | Karşıladığı erişim deseni | Yazma maliyeti notu |

## DDL
```sql
CREATE TABLE ...
```

## Migration Taslağı
1. Genişlet ... 2. Doldur ... 3. Geçir ... 4. Daralt ...

## Açık Sorular
````

## Kalite kontrol listesi
- [ ] Belirtilen her değişmez kural bir kısıtla zorlanıyor ya da gerekçesiyle açıkça uygulama koduna bırakıldı.
- [ ] Her indeks bir erişim desenine eşleniyor; spekülatif indeks yok.
- [ ] Para, zaman ve kimlikler kesin ve belirsizlik içermeyen tipler kullanıyor.
- [ ] Yabancı anahtar silme davranışı varsayılana bırakılmadı, bilinçli seçildi.
- [ ] Kişisel veri kolonları işaretlendi ve saklama ele alındı.
- [ ] Migration kesinti olmadan çalışabiliyor ya da neden çalışamadığı yazıldı.
- [ ] Çıkarımlar `[VARSAYIM]` olarak etiketli ve varsayım ya da açık soru olarak listeli; dayanağı olmayan hiçbir şey olgu gibi sunulmuyor.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Tekilliği veya çakışmazlığı yalnızca uygulama kodunda zorlamak; eşzamanlı istekler bunu bozar. Kısıt veya açık kilitleme kullan.
- Unique kısıtları sessizce bozan soft delete. Kısmi unique indeks kullan veya silme işaretini kısıta dahil et.
- Yerel saati dilimsiz saklamak ya da para için float kullanmak.
- Sorgulanan ve doğrulanan veri için genel "entity-attribute-value" veya JSON kolonları. Bunları yalnızca gerçekten şemasız uzantılar için kullan.

## Örnek
Girdi: "Odalar, başlangıç/bitişli rezervasyonlar, katılımcılar, aynı odada çakışan rezervasyon yok. Motor: PostgreSQL."

Çıktıdan bir bölüm:
- `booking(id uuid PK, room_id FK → room ON DELETE RESTRICT, period tstzrange NOT NULL, organizer_id FK, version int NOT NULL DEFAULT 0)`
- Zorlanan kural: `EXCLUDE USING gist (room_id WITH =, period WITH &&)` `[MOTORA-ÖZGÜ]`; taşınabilir alternatif: oda satırında `SELECT ... FOR UPDATE` ile oda bazında insert'leri sıraya sok.
- İndeks: "bir günün oda takvimi" için `booking(room_id, lower(period))`.
- Açık soru: İptal edilen rezervasyonlar saklanıyor mu? Evetse exclusion bunları dışarıda bırakmalı `[TBD]`.
