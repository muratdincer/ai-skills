---
name: wip-policy
description: "Bir panoyu ve akış kurallarını tasarlar: bekleme durumları dahil gerçek iş akışını yansıtan kolonlar, kolon veya kişi başına devam eden iş (WIP) limitleri, açık giriş ve çıkış kriterleri, hizmet sınıfları, bloke ve yaşlanan madde kuralları ve limitlerin ayarlanması için bir gözden geçirme sıklığı. Bir ekip panosunu kurarken veya yeniden tasarlarken, çok iş başlatılıp az iş bitiyorken ya da hangi WIP limitlerinin ve çekme kurallarının kullanılacağı sorulduğunda kullanılır."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 03-delivery
  role: agile-delivery
  area: flow
  title: "WIP limiti ve akış kuralları"
  related: "cycle-time-analysis, working-agreement, definition-of-ready, definition-of-done, impediment-tracking"
  prompt: "6 geliştirici ve 1 test uzmanıyız, her şey 'devam ediyor' ve hiçbir şey bitmiyor. Pano kolonlarını ve WIP limitlerini belirlememize yardım et."
---

# WIP Limiti ve Akış Kuralları

## Amaç
Ekibin iş akışını açık hale getirmek ve devam eden işi sınırlamak. Böylece maddeler daha hızlı ve öngörülebilir biçimde biter; kurallar da herkesin bir maddenin ilerleyip ilerleyemeyeceğini ve limit dolduğunda ne yapılacağını anlayabileceği kadar nettir.

## Ne zaman kullanılır
- Ekip panosunu oluştururken veya yeniden tasarlarken.
- Çok sayıda madde başlatılıp azı bitiyor ve döngü süresi artıyorken.
- Devirler (inceleme, test, deployment) birikiyor ve yeni iş başlatmayı ne zaman durduracağını kimse bilmiyorken.

## Ne zaman kullanılmaz
- Maddelerin ne kadar sürdüğünü ölçmek veya darboğazı veriden bulmak için önce `cycle-time-analysis` kullanılır, sonra buraya dönülür.
- Genel ekip normları (çalışma saatleri, iletişim, toplantılar) için `working-agreement` kullanılır.
- Backlog maddeleri için "hazır" veya "bitti"nin tanımı için `definition-of-ready` veya `definition-of-done` kullanılır.

## Girdiler
Zorunlu:
- İşin şu anda fikirden üretime nasıl aktığı (adımlar, devirler) ve beceriye göre ekip bileşimi.

İsteğe bağlı, kaliteyi artırır:
- Mevcut pano kolonları ve kolon başına madde sayısının anlık görüntüsü.
- Döngü süresi veya verim verisi, bilinen darboğazlar.
- İş türleri ve aciliyet seviyeleri (hatalar, acil talepler, sabit tarihli işler).
- Kurumsal kısıtlar (ayrı test ekibi, sürüm pencereleri, onaylar).

İş akışı bilinmiyorsa kullanıcıdan son biten maddeyi adım adım anlatmasını iste; bunu ilk taslak olarak kullan.

## Süreç
1. İdeal olanı değil, girdideki gerçek iş akışını haritala. Kuyruk süresi görünür olsun diye bekleme durumlarını ("İncelemeye hazır", "Teste hazır", "Deployment bekliyor") açıkça ekle. 4-8 kolonda tut.
2. Taahhüt noktasını (ekibin maddeyi bitirmeyi taahhüt ettiği yer) ve teslim noktasını (bitmiş sayıldığı yer) tanımla. Döngü süresi ikisi arasında ölçülür.
3. Her kolon için giriş ve çıkış kriterlerini kısa, kontrol edilebilir ifadeler olarak yaz. Varsa ilk kolonun girişini `definition-of-ready`, son kolonun çıkışını `definition-of-done` ile bağla.
4. Başlangıç WIP limitlerini belirle: yaygın bir başlangıç kuralı, o durumda çalışabilecek kişi sayısından eşli çalışmayı düşmektir; ekip geneli limitlerde ekip büyüklüğüne yakın başla ve zamanla daralt `[pratik kural]`. Gizli kuyrukları önlemek için bekleme durumu çiftlerine (aktif + sonrakine hazır) ortak limit koy.
5. İş türleri farklıysa hizmet sınıflarını tanımla: ör. standart, sabit tarihli, acil (aynı anda en fazla 1, limitleri aşabilir), görünmeyen iş/iyileştirme (ayrılmış kapasite). Her birinin neyi atlayabileceğini belirt.
6. Çekme kurallarını yaz: sağdan sola çek; yeni iş başlatmadan önce bitir veya yardım et; bir kolon limitteyse yeni madde başlatmak yerine sonraki adımdaki işe ekipçe odaklan.
7. Bloke ve yaşlanan madde kurallarını yaz: bloke maddelerin nasıl işaretleneceği, engellerin ne zaman eskale edileceği (ör. aynı gün günlük senkronda, 1-2 gün sonra `impediment-tracking`'e) ve konuşma başlatan bir yaş eşiği (ör. P85 döngü süresinin üstü).
8. Limit aşıldığında ne olacağını tanımla: yalnızca ekibin açık onayıyla, kayda geçirilerek ve bir sonraki gözden geçirmede konuşularak; sessizce değil.
9. Bir gözden geçirme sıklığı (ör. 2-4 haftada bir) ve limitleri ayarlamak için kullanılacak sinyalleri belirle: döngü süresi yüzdelikleri, yaşlanan maddeler, boşta kalan kişiler, bloke sayıları. Her seferinde tek bir limiti değiştir.
10. Kullanıcının vermediği her sayıyı ve kuralı ekip onayı için `[ÖNERİ]` olarak işaretle; etkiyi doğrulamak için `cycle-time-analysis`, kuralları diğer ekip normlarıyla kayda almak için `working-agreement` öner.

## Çıktı formatı
```markdown
# Pano ve Akış Kuralları – <ekip>
Taahhüt noktası: <kolon> · Teslim noktası: <kolon> · Gözden geçirme sıklığı: <...>

| Kolon | Tür (aktif/bekleme) | WIP limiti | Giriş kriterleri | Çıkış kriterleri |
|---|---|---|---|---|

## Hizmet Sınıfları
| Sınıf | Ne zaman | Kural (limit, atlama, öncelik) |
|---|---|---|

## Çekme Kuralları
- ...

## Bloke ve Yaşlanan Maddeler
- Şu durumda bloke işaretle: ... ; şu süreden sonra eskale et: ...
- Yaş eşiği: <n gün> → <aksiyon>

## Limit Aşımları
- ...

## İzlenecek Metrikler ve Ayarlama Kuralı
- ...

## Açık Sorular / Uzlaşılacak Öneriler
- [ÖNERİ] ...
```

## Kalite kontrol listesi
- [ ] Kolonlar gerçek iş akışını yansıtıyor ve bekleme durumlarını görünür kılıyor.
- [ ] Her kolonun kontrol edilebilir giriş ve çıkış kriteri var.
- [ ] WIP limitleri "WIP'i düşük tut" değil, gerekçesi belirtilmiş sayılar.
- [ ] Acil işlerin kesin bir üst sınırı var; varsayılan kulvara dönüşemez.
- [ ] Bloke, yaşlanma ve aşım kuralları kimin ne zaman harekete geçeceğini söylüyor.
- [ ] Ekibin henüz onaylamadığı öneriler `[ÖNERİ]` olarak işaretli.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Limitleri hiç devreye girmeyecek kadar yüksek koymak. Hiç ulaşılmayan limit hiçbir şeyi değiştirmez; konuşma başlatacak kadar sıkı başla.
- Yalnızca aktif kolonları sınırlamak. İş bu durumda "Geliştirme bitti / Teste hazır" kolonunda birikir; aktif ve bekleme kolonlarını birlikte sınırla.
- Yalnızca kişi başı limit koymak. Bu, akışı değil bireysel meşguliyeti optimize eder; kolon veya ekip limitlerini tercih et.

## Örnek
Girdi: 6 geliştirici, 1 test uzmanı; kolonlar Yapılacak / Devam ediyor / Bitti; devam eden 17 madde.

Çıktıdan bir bölüm:
| Kolon | Tür | WIP limiti | Çıkış kriterleri |
|---|---|---|---|
| Geliştirme | aktif | 4 [ÖNERİ] | Kod birleştirildi, birim testleri yeşil |
| Teste hazır + Test | bekleme + aktif | 3 [ÖNERİ] | Kabul kriterleri doğrulandı |
- Çekme kuralı: "Teste hazır + Test" 3'teyken geliştiriciler yeni madde başlatmadan önce teste eşli destek verir.
- Zayıf kural: "Çok iş almayın." Güçlü kural: "Geliştirme'de 4 madde varken yeni madde çekme; önce sonraki adıma yardım et."
