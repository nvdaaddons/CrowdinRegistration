# eMule #

*	Yazarlar: Noelia, Chris ve Alberto.

Bu eklenti NVDA ile eMule erişilebilirliğinin geliştirilmesine yardımcı olur.
Ayrıca farklı pencerelerde hareket etmek için ek klavye komutları sağlar ve Emule hakkında yararlı bilgiler verir.

Bu eklenti aynı yazar tarafından geliştirilen eMuleNVDASupport adlı eklentiye dayanılarak geliştirildi. Her ikisin ortak tuş komutlarına ve benzer özelliklere sahip olduğu için bunu kurmadan önce eskisini kaldırmalısınız.

[eMule][1] 0.50a ve 70b test edilmiştir.

## Tuş komutları: ##

*	kontrol+shift+h: odak ve fareyi Ana araç çubuğuna taşır.
*	kontrol + shift + t: Geçerli pencereyi okur.
*	kontrol + shift + n: Bul penceresinde odağı Ad alanınna taşır.
*	kontrol + shift + p: Arama penceresinde, odağı ve fareyi arama parametreleri listesine veya alan düzenleme seçeneklerine taşır.
*	kontrol+shift+b: Odağı geçerli penceredeki listeye taşır. Örneğin, Arama penceresinde kullanılabilir, transfer penceresinde indirilenler vb.
*	kontrol+shift+o: Odağı geçerli penceredeki salt okunur düzenleme kutularına taşır. Örneğin, IRC alınan mesajlar, mevcut Sunucular vb.
*	kontrol+NVDA+f: İmleç salt okunur bir düzenleme kutusunda bulunuyorsa, NVDA'da bulunan metin arama komutlarını kullanmak için bir bul iletişim kutusu açar.
*	kontrol + shift + l: Fare ve nesne sunucusunu Mevcut listenin başlıkları üzerine taşır.
*	kontrol + shift + q: durum çubuğunda ilk nesneyi okur; son etkinlik hakkında bilgi verir.
*	kontrol + shift + w: geçerli sunucu üzerinde dosya ve kullanıcılar hakkında bilgi içeren durum çubuğunun ikinci nesnesini okur.
*	kontrol + shift + e: yükleme ve indirme hızıyla ilgili bilgi veren durum çubuğunun üçüncü nesnesini okur.
*	kontrol+Shift+R: Durum çubuğunun dördüncü nesnesini okur; eD2K ve KAD Network'ün bağlanmasına ilişkin raporlar.
* Atanmadı: Kaydırıcıları okumak için alternatif bir yaklaşımın kullanımını açıp kapatır.

## Sütunların yönetimi. ##

Bir liste içindeyken, alt + kontrol + yön tuşlarıyla satır ve sütunlar arasında dolaşabilirsiniz.
Bu Eklentide aşağıdaki tuş komutları da mevcuttur:

*	nvda + kontrol + 1-0: ilk 10 sütunu okur.
*	nvda + shift + 1-0: 11-20 sütunları okur.
*	nvda + shift + C: son okunan sütunun içeriğini panoya kopyalar .


## 20.0.0 İçin Değişiklikler
* Bu eklentinin yazarlarından Alberto Buffolino tarafından geliştirilen [LabelautofinderCore Projesi] (https://github.com/abuffer/labelautofindercore) sayesinde bazı düzenleme kutuları ve kaydırıcılar etiketlenmiştir.
* Kaydırıcıları okumak için alternatif bir yaklaşımın kullanımını değiştirmek için bir komut (atanmamış) eklendi (varsayılan olarak kapalı).

## 7.0 İçin Değişiklikler
* NVDA 2023.1 ile uyumlu.

## 6.0 İçin Değişiklikler
*	NVDA 2022.1 veya sonraki sürümünü gerektirir.

## 5.0 İçin Değişiklikler
*	NVDA 2021.1 ile uyumlu.

## 4.0 İçin Değişiklikler ##
*	NVDA 2019.3 veya sonraki sürümünü gerektirir.

## 3.0 İçin Değişiklikler ##
*	 Salt okunur düzenleme kutularında metin aramak için bulma iletişim kutusunu etkinleştirmek amacıyla nvda+control+f gibi bulma iletişim kutusu kullanılabilir.

## 2.0 İçin Değişiklikler ##
*	 Eklenti yardımı, Eklenti Mağazasından edinilebilir.

## 1.2 İçin Değişiklikler ##
*	 IRC mesajları arasında dolaşılırken, seçilen metin düzgün bildiriliyor.
*	 Arama sonuçları listesine gitmek için kullanılan Kısayol tuşu, odağı geçerli pencerede mevcut herhangi bir listeye taşıyabilecek şekilde genelleştirilmiştir.
*	 IRC mesajlarına odaklanmak için kullanılan komut, herhangi bir salt okunur düzenleme kutusuna taşınacak şekilde genelleştirildi, bu da Sunucular penceresinde bağlantı bilgilerinin gözden geçirilmesini mümkün kıldı.
*	 Fare ve odak araç çubuğuna taşınırken, bazı durumlarda iki kez anons ediliyordu. Bu düzeltildi.

## 1.1 İçin Değişiklikler ##
*	 NVDA'nın yardım menüsündeki eMule öğesinde, kullanıcı Konfigürasyon klasörü adı Latin alfabesi dışındaki karakterler içerdiğinde ortaya çıkan hata düzeltildi.
*	 Kısayollar artık NVDA girdi hareketleri iletişim kutusu kullanılarak yeniden atanabilir.

## 1.0 İçin Değişiklikler ##
*	 İlk sürüm.

[1]: http://www.emule-project.net
