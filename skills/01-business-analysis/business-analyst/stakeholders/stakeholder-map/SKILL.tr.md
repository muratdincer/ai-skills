---
name: stakeholder-map
description: "Paydaşları her puan için kanıtıyla birlikte güç/ilgi matrisine yerleştirir, mevcut ve hedeflenen tutumu ekler; her çeyrek ve kilit kişi için iletişim stratejisi, kanal ve sıklık belirler. Paydaşlar belirlendikten sonra, iletişim planı öncesinde veya girişime desteğin belirsiz olduğu durumlarda kullanılır; 'güç ilgi matrisi', 'kimi yakından yönetmeliyiz?' gibi ifadeler tetikleyicidir."
license: MIT
metadata:
  version: "1.0.0"
  language: tr
  category: 01-business-analysis
  role: business-analyst
  area: stakeholders
  title: "Güç/ilgi paydaş haritası"
  related: "stakeholder-identification, raci-matrix, communication-plan, stakeholder-register, conflict-resolution"
  prompt: "CRM geçişi için bu 9 paydaşı güç/ilgi matrisine yerleştir ve her biriyle nasıl ilerlememiz gerektiğini söyle."
---

# Güç/İlgi Paydaş Haritası

## Amaç
Her paydaşın gücünü, ilgisini ve tutumunu açık hale getirerek iletişim ve katılım emeğinin nereye harcanacağına karar vermek ve bunu somut bir plana dönüştürmek.

## Ne zaman kullanılır
- Paydaş listesi hazır ve katılım emeğinin önceliklendirilmesi gerektiğinde.
- Girişim dirençle veya belirsiz destekle karşılaştığında.
- İletişim planı veya yönlendirme kurulu yapısı tanımlanmadan önce.

## Ne zaman kullanılmaz
- Paydaş listesi henüz yoksa önce `stakeholder-identification` kullanılır.
- Görevler kişilere atanacaksa `raci-matrix` kullanılır.
- Ayrıntılı bir iletişim takvimi gerekiyorsa `communication-plan` kullanılır.

## Girdiler
Zorunlu:
- Rolleriyle paydaş listesi (isimler isteğe bağlı).
- Bir iki cümleyle girişim.

İsteğe bağlı, kaliteyi artırır:
- Bilinen tutumlar, geçmiş çatışmalar, raporlama hatları, bütçe yetkisi.
- Belirli onaylar gerektiren yaklaşan kararlar.

Paydaş listesi yoksa iste veya önce `stakeholder-identification` çalıştırmayı öner.

## Süreç
1. Bu girişim için gücü tanımla: resmi yetki (bütçe, onay, veto) ve gayriresmi etki (uzmanlık, ilişki ağı, kaynak veya veri üzerindeki kontrol).
2. İlgiyi tanımla: sonuç, kişinin işini, hedeflerini veya riskini ne kadar değiştiriyor.
3. Her paydaşı iki eksende Yüksek/Düşük olarak puanla ve kanıtı tek ifadeyle yaz. Tahminleri `[VARSAYIM]` olarak işaretle.
4. Mevcut tutumu (şampiyon, destekçi, tarafsız, şüpheci, engelleyici, bilinmiyor) ve belirli bir kilometre taşına kadar hedeflenen tutumu kaydet. Doğrudan kanıta değil duyuma dayanan tutum `[VARSAYIM]` olarak işaretlenir.
5. Çeyreklere yerleştir: Yakından yönet (yüksek/yüksek), Memnun tut (yüksek güç, düşük ilgi), Bilgilendir (düşük güç, yüksek ilgi), İzle (düşük/düşük).
6. Her çeyrek için strateji, kanal ve sıklık belirle; yüksek güçlü her paydaş için kişisel bir aksiyon ekle (hangi mesaj, kim tarafından, ne zamana kadar).
7. Boşlukları bul: sahibi olmayan yüksek güçlü şüpheciler, değerlendirilmeyen şampiyonlar, tutumu bilinmeyen paydaşlar.
8. Konumların değiştiğini unutma; bir gözden geçirme tetikleyicisi belirle (faz değişimi, kilit karar, yeniden yapılanma).
9. Hedef devam ediyorsa iletişim aksiyonlarını takvime bağlamak için `communication-plan`, karar sahipliğini netleştirmek için `raci-matrix` öner.

## Çıktı formatı
```markdown
# Paydaş Haritası: <girişim>

| Paydaş | Güç (Y/D) – kanıt | İlgi (Y/D) – kanıt | Tutum şimdi → hedef | Çeyrek |
|---|---|---|---|---|

## Matris
- Yakından yönet: ...
- Memnun tut: ...
- Bilgilendir: ...
- İzle: ...

## Katılım stratejisi
| Çeyrek / kişi | Hedef | Mesaj | Kanal | Sıklık | Sorumlu |
|---|---|---|---|---|---|

## Riskler ve boşluklar
- ...
Gözden geçirme tetikleyicisi: <olay>
```

## Kalite kontrol listesi
- [ ] Her puanın tek ifadelik bir gerekçesi var veya `[VARSAYIM]` olarak işaretli.
- [ ] Tutum, güç ve ilgiden ayrı kaydedildi.
- [ ] Yüksek güçlü her paydaşın adı belli bir sorumlusu ve aksiyonu var.
- [ ] Engelleyiciler ve şüpheciler için yalnızca "bilgilendir" değil, somut bir aksiyon var.
- [ ] Haritada kişiler hakkında yargılayıcı ifade yok.
- [ ] Bir gözden geçirme tetikleyicisi tanımlandı.
- [ ] Tüm kontroller geçiyor; biri geçmiyorsa çıktıyı düzelt ve yanıtlamadan önce listeyi yeniden çalıştır.

## Sık yapılan hatalar
- Hiyerarşiyi güçle eşitlemek. Bir sistem sahibi veya kıdemli bir uzman, bir direktörden daha fazla engel olabilir.
- Herkesi "yakından yönet" çeyreğine koymak. Listenin üçte birinden fazlası oradaysa puanları yeniden gözden geçir.
- Ham haritayı geniş kitleyle paylaşmak. Tutum notları hassastır; çalışma sürümünü çekirdek ekipte tut.

## Örnek
Girdi: "CRM geçişi; paydaşlar arasında Satış Direktörü, çağrı merkezi temsilcileri, BT güvenliği, KVKK irtibat kişisi, pazarlama analistleri var."

Çıktıdan bir bölüm:
| Paydaş | Güç | İlgi | Tutum şimdi → hedef | Çeyrek |
|---|---|---|---|---|
| Satış Direktörü | Y – bütçe sahibi | Y – satış hunisi görünürlüğü | Destekçi → açılışa kadar Şampiyon | Yakından yönet |
| KVKK irtibat kişisi | Y – veri aktarımını durdurabilir | D – veri korumayla sınırlı | Bilinmiyor → geçiş tasarımından önce Tarafsız | Memnun tut |
| Çağrı merkezi temsilcileri | D | Y – günlük araçları değişiyor | Şüpheci → UAT'ye kadar Tarafsız | Bilgilendir |
