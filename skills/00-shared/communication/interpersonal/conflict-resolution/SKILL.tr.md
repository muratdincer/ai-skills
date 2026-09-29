---
description: Bir iş yeri çatışmasını taraflar, dile getirilen pozisyonlar, altta yatan çıkarlar, olgular ile algılar ve çatışma türü olarak haritalar; ardından ortak çıkarlara hizmet eden seçenekler ve üzerinde anlaşılan sonraki adımlarla arabulucu bir çözüm yolu önerir. İki kişi, ekip veya birim öncelikler, sahiplik, yaklaşım ya da davranış konusunda anlaşamadığında ve bu anlaşmazlık işi durdurduğunda veya ilişkiye zarar verdiğinde kullanılır.
related: feedback-sbi, negotiation-prep, facilitation-guide, trade-off-analysis, decision-log
prompt: Backend ve mobil ekiplerimiz API versiyonlamanın kimde olduğu konusunda sürekli tartışıyor ve sürümler kayıyor. Arabuluculuk yapmama yardım et.
---

# Çatışma Çözme

## Amaç
Bir çatışmayı birbirine karşı pozisyonlardan tarafların gerçek çıkarlarına dayanan bir anlaşmaya taşımak ve anlaşma sağlanamazsa net bir karar yolu belirlemek; böylece iş yeniden akar ve çalışma ilişkisi korunur.

## Ne zaman kullanılır
- İki kişi veya ekip sahiplik, öncelik, teknik yaklaşım ya da çalışma biçimi konusunda anlaşamıyor ve bu teslimatı engelliyorsa.
- Bir yönetici veya lider, ekip üyeleri ya da eşdüzey ekipler arasında arabuluculuk yapacaksa.
- Tekrarlayan bir gerginlik için toplantı öncesi hazırlık gerekiyorsa.

## Ne zaman kullanılmaz
- İki taraflı bir anlaşmazlık değil, bir kişinin davranışına geri bildirim gerekiyorsa. `feedback-sbi` kullanın.
- Siz taraflardan birisiniz ve dış bir tarafla koşulları pazarlık ediyorsunuz. `negotiation-prep` kullanın.
- Anlaşmazlık, seçenekleri net tanımlanmış bir teknik tercih ise. `trade-off-analysis` kullanın.

## Girdiler
Zorunlu:
- Kullanıcının anlattığı şekliyle kimin kiminle ve ne konuda çatıştığı.
- Kullanıcının rolü (arabulucu, yönetici, taraflardan biri).

İsteğe bağlı:
- Her tarafın kendi sözleriyle görüşü, geçmiş, teslimata etkisi, karar yetkisi (anlaşma olmazsa kim karar verir), kurumsal kısıtlar.

Yalnızca bir tarafın görüşü varsa bunu belirtin, diğer tarafın bakış açısını `[BİLİNMİYOR]` veya `[VARSAYIM]` olarak işaretleyin ve çözüm önermeden önce onu dinlemeyi planlayın. İsim ve kişisel ayrıntıları gereken en az düzeyde tutun; karakteri değil davranışı anlatın. Çatışma taciz, ayrımcılık veya güvenlik içeriyorsa durun ve İK'yı ya da resmi kanalı önerin.

## Süreç
1. Kullanıcının rolünü ve tarafsızlığını netleştirin. Taraflardan biriyse arabuluculuk yapamaz; tarafsız bir kolaylaştırıcı önerin veya `negotiation-prep`'e geçin.
2. Tarafları ve etkilenen ya da karar yetkisi olan diğer kişileri haritalayın.
3. Her tarafın pozisyonunu (ne talep ettiği) çıkarlarından (neden: iş yükü, hesap verebilirlik, kalite, takdir, risk) ayırın. Çıkarım yapılan her çıkarı `[VARSAYIM]` olarak işaretleyin.
4. Olguları (doğrulanabilir) algı ve duygulardan ayırın; doğrulanacak olguları listeleyin.
5. Çatışmayı sınıflandırın: görev (ne), süreç (nasıl, kimin sorumluluğu), ilişki (güven, saygı) veya değer/öncelik. İlişki çatışması önce baş başa ele alınır; görev ve süreç çatışmaları ortak çalışılabilir.
6. Ortak çıkarları ve çatışmanın sürmesinin her iki taraf için maliyetini bulun; bunlar ortak konuşmayı açar.
7. Süreci planlayın: ayrı ayrı birebir dinleme görüşmeleri, ardından kurallı bir ortak oturum (tek konuşmacı, cevaplamadan önce karşı tarafı özetleme, geleceğe odak).
8. Her iki tarafın çıkarına hizmet eden seçenekler üretin (kriterlere göre bölünmüş sahiplik, rotasyon, gözden geçirmeli deneme dönemi, açık bir arayüz veya çalışma anlaşması); kimseyi tatmin etmeyen bir orta yol değil.
9. Seçenekler arasında seçim için nesnel kriterler (teslim tarihi, olay sayısı, efor) ve bir geri dönüş yolu belirleyin: anlaşma olmazsa kim, hangi tarihe kadar karar verir.
10. Anlaşmanın biçimini tanımlayın: ne değişiyor, sorumlular, gözden geçirme tarihi, bir dahaki sefere sorunların erken nasıl dile getirileceği.
11. Kullanıcının hedefi devam ediyorsa ortak oturum için `facilitation-guide`, anlaşmayı kaydetmek için `decision-log`, bireysel davranış takibi için `feedback-sbi` öner.

## Çıktı formatı
```markdown
# Çatışma Haritası ve Çözüm Planı: <konu>
Arabulucu: <rol> | Tür: Görev / Süreç / İlişki / Değer | Aciliyet: <teslimata etkisi>

| Taraf | Pozisyon (söylenen) | Çıkarlar (neden) | Olgular | Algılar |
|---|---|---|---|---|
| A | ... | ... [VARSAYIM] | ... | ... |
| B | ... | ... | ... | ... |

Ortak çıkarlar: ...
Çözümsüzlüğün maliyeti: ...

## Süreç
1. A ile birebir – sorular: ...
2. B ile birebir – sorular: ...
3. Ortak oturum – kurallar, gündem, süre

## Seçenekler
| Seçenek | A'ya faydası | B'ye faydası | Risk |
Karar kriterleri: ...  | Geri dönüşte karar veren ve son tarih: ...

## Anlaşma taslağı
- Değişiklik: ... | Sorumlu: ... | Gözden geçirme tarihi: ... | Eskalasyon yolu: ...
Açık sorular / doğrulanacak olgular: ...
```

## Kalite kontrol listesi
- [ ] Her taraf için pozisyon ve çıkarlar ayrılmış, çıkarımlar işaretlenmiş.
- [ ] Her iki tarafın görüşü yer alıyor ya da eksik görüş `[BİLİNMİYOR]` olarak işaretli.
- [ ] Olgular ve algılar ayrılmış; suçlayıcı dil yok.
- [ ] Seçenekler iki tarafın çıkarına da hizmet ediyor ve nesnel seçim kriterleri var.
- [ ] Anlaşma olmazsa karar verecek kişi ve son tarih belli.
- [ ] Güvenlik, taciz veya ayrımcılık konuları resmi kanala yönlendirilmiş.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Pozisyonlarda ortayı bulmak. Çıkarlar üzerinde çalışın; orta nokta çoğu zaman kimsenin gerçek sorununu çözmez.
- Önce ortak oturumu yapmak. Her tarafı önce baş başa dinleyin ki kimse pusuya düşürülmüş hissetmesin.
- Gözden geçirme tarihi koymadan ayrılmak. Anlaşmalar zamanla aşınır; bir kontrol planlayın.

## Örnek
Girdi: Backend ve mobil ekipler API versiyonlamanın kimde olduğunu tartışıyor; sürümler kayıyor.

Zayıf: "İki ekip daha iyi iletişim kurmalı ve birbirine saygı göstermeli. Bir toplantı yapalım."

Güçlü (alıntı):
- Backend pozisyonu: "Mobil, API değişikliklerimize uyum sağlamalı." Çıkar `[VARSAYIM]`: uygulama mağazası döngülerini beklemeden servisleri geliştirebilmek.
- Mobil pozisyonu: "Backend API'yi asla bozmamalı." Çıkar: eski uygulama sürümündeki kullanıcıların çalışmaya devam etmesi.
- Tür: Süreç (sahiplik). Ortak çıkar: daha az sürüm kayması.
- Seçenek: versiyonlama backend'de, son `[TBD: n]` API sürümünü destekler; mobil, minimum sürüme yükseltme penceresine uyar. İki sürüm sonra gözden geçirilir.
