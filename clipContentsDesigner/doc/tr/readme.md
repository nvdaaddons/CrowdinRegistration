# Clip Contents Designer #
*   Yazarlar: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Klavye komutları ##
*   NVDA+windows+c: Seçilen metni, MathML nesnelerini temsil eden Unicode
    braille karakterlerini veya inceleme imleciyle işaretlenmiş dizeyi panoya
    ekler.
*   NVDA+windows+x: Pano içeriğini temizle.NVDA+windows+x: Pano içeriğini siler.
*    Atanmamış: Panoya kopyalar (veya panodan keser), önceden onay istenme
     olasılığı ile.
*    Atanmamış: Pano metnini HTML olarak Tarama kipi modunda gösterir veya
     panonun boş olup olmadığını veya örneğin dosyalar veya klasörler Windows
     Gezgini'nden kopyalanmışsa, bir iletide gösterilemeyen içeriğe sahip olup
     olmadığını bildir.
*    Atanmamış: Metinsel pano içeriğini tarama kipi modunda düz metin olarak
     gösterir veya panonun boş olup olmadığını veya örneğin dosyalar veya
     klasörler Windows Gezgini'nden kopyalanmışsa, göz atılabilir bir iletide
     gösterilemeyen içeriğe sahip olup olmadığını bildir.

## Pano İçeriği düzenleyici ayarları ##

Bu panele NVDA menüsü tercihler alt menüsünden Ayarlar iletişim kutusuna girerek
erişilebilir.

Aşağıdaki kontrolleri içerir:

* Panoya eklenen içerikler arasında ayraç olarak kullanılacak metni yazın:
  Eklenen metnin tamamı yapıştırıldıktan sonra metin bölümlerini bulmak için
  kullanılabilecek bir ayırıcı ayarlamayı sağlar.
* Metni panodaki verilerden önce ekle: Eklenen metnin sona mı yoksa başa mı
  ekleneceğini seçmek de mümkündür.
* Önceden onay gerektiren eylemleri seçin: Mevcut her eylem için hemen mi yoksa
  onaydan sonra mı gerçekleştirileceğini seçebilirsiniz. Kullanılabilir eylemler
  şunlardır: metin ekle, panoyu temizle, kopyalamayı taklit et ve kesmeyi taklit
  et.
* Şu durumlarda seçili eylemleri gerçekleştirmeden önce onay iste: Yalnızca
  panoda metin varsa veya pano boş değilse (örneğin metin değil de bir dosya
  kopyaladıysanız) onayın her zaman istenip istenmeyeceğini seçebilirsiniz.
* Format to show the clipboard text as HTML in browse mode: If you're learning
  HTML markup language, you may choose Preformatted text in HTML or HTML as
  shown in a web browser, to have an idea of how your HTML code will be rendered
  by NVDA in a browser. The difference between preformatted and conventional
  HTML is that the first option will preserve consecutive spaces and line
  breaks, and the second one will compact them. For example, write some HTML
  tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and
  use clipContentsDesigner add-on to show the text in a browseable message.
* Pano metnini Tarama kipi modunda gösterirken maksimum karakter sayısı: Pano
  büyük metin dizeleri içeriyorsa, bu sınırı artırmanın sorunlara yol
  açabileceğini lütfen unutmayın. Varsayılan sınır 100000 karakterdir.
* Varsayılanları geri yükln.

Notlar:

*   Eğer NVDA'nın bir mesaj kutusu hala açıksa bir işlem için onay
    istenmeyecektir. Bu gibi durumlarda, işlemler derhal gerçekleştirilecektir.
* Kopyalamayı taklit et ve kesmeyi taklit et komutları, bu özellikler
  etkinleştirildiğinde, eklentinin kontrol+c ve kontrol+x'in kontrolünü alacağı
  anlamına gelir. Bu, bu tuş vuruşlarına karşılık gelen eylemleri
  gerçekleştirmeden önce bir onay istenip istenmeyeceğini seçmeye izin
  verecektir.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape key.

## 40.0.0 için Değişiklikler
* İbranice klavye için destek eklendi.

## 22.0.0 için Değişiklikler
* Eklenti ayarları panelinde varsayılanları geri yüklemek için bir düğme
  eklendi.
* Eklenti güvenli modda çalıştırılamaz.

## 17.0 için Değişiklikler
* NVDA 2023.1 ile uyumlu.

## 16.0 için Değişiklikler
* NVDA 2022.1 veya sonraki bir sürümü gerektirir.

## 15.0 için Değişiklikler
* Panoya metin ekleme komutu, girdi hareketleri iletişim kutusuna tekrar
  eklendi.
* Mohammadhosein Ghezelsofla sayesinde Farsça klavyeyle kopyalama ve kesme
  hareketleri düzeltildi.

## 14.0 için değişiklikler
* NVDA 2021.1 ile uyumlu.

## Changes for 13.0
* Ayarlar panelinin görsel düzenindeki bir sorun düzeltildi, teşekkürler Cyrille
  Bougot.
* Dokümantasyon (yardım dosyaları) geliştirildi.
* Eklenti için kullanılabilen tüm komutlara girdi hareketleri atamak için bir
  Pano İçerik Düzenleyicisi kategorisi eklendi.
* Tarayıcılarda odak modu etkinken Kopyalamayı taklit et kullanıldığında yaşanan
  hatalar düzeltildi.
* Pano metin içeriklerini ham metin olarak veya HTML olarak biçimlendirilmiş
  olarak göstermek için farklı hareketler atayabilirsiniz. Ayarlar panelinde
  pano metnini gösterecek biçim, HTML biçimi için mevcut iki seçeneği seçmek
  üzere düzenlendi.

## 12.0 için Değişiklikler
* LibreOffice Writer gibi uygulamalarda Kopyalamayı taklit et kullanırken oluşan
  hatalar düzeltildi.

## 11.0 için Değişiklikler
* Artık NVDA'nın standart komutlarını (NVDA+f9 ve NVDA+f10) kullanarak inceleme
  imleciyle işaretlenmiş metni eklemek mümkündür. Yeni NVDA+shift+f9 komutuyla
  daha iyi bir entegrasyon için NVDA+windows+f9 artık kullanılmamaktadır.
* NVDA 2019.3 veya sonraki bir sürümü gerektirir.

## 10.0 için Değişiklikler
* Başlık latin olmayan karakterler içerdiğinde pano metnini göstermek için
  kullanılan iletişim kutusundaki bir hata düzeltildi.
* Arapça klavye düzeniyle Kesmeyi taklit et ve Kopyalamayı taklit et
  özelliklerini kullanırken oluşan bir hata düzeltildi. Bu, Abdel tarafından
  düzeltildi, eklenti yazar olarak eklendi.

## 9.0 için Değişiklikler

* Pano metnini tarama kipi modunda gösterme özelliği eklendi.
* Dosyalar veya klasörler kopyalanmışsa, pano boş değilse onayın gerekli olup
  olmayacağını seçmek için bir seçenek eklendi.
* NVDA 2018.4 veya sonraki bir sürümü gerektirir.

## 8.0 için Değişiklikler ##

* Eklenti ayarları, NVDA Ayarları iletişim kutusunun ilgili kategorisinde
  gösterilir.
* NVDA 2018.2 veya sonraki bir sürümü gerektirir.

## 7.0 için Değişiklikler

* Kurulum sırasında yapılandırma iletişim kutusunda hayır'ı seçerseniz, Kesmeyi
  taklit et ve Kopyalamayı taklit et özeliklerine ilişkin komutlar kaldırılır,
  böylece kontrol+c ve kontrol+x için normal davranışı geri yükleyebilirsiniz.

## 6.0 için Değişiklikler

*    Onaydan sonra mevcut eylemlerin gerçekleştirilip gerçekleştirilmeyeceğini
     seçmek için seçenekler eklendi.
*   Girdi hareketleri iletişim kutusundan atanabilen Kopyalamayı taklit et ve
    Kesmeyi taklit et komutları eklendi.
*    Kurulum sırasında Kopyalamayı taklit et ve Kesmeyi taklit et işlevlerini
     yapılandırmak için bir iletişim kutusu eklendi. Bu, kopyalamak ve kesmek
     için control+c ve control+x komutlarının eklenmesine ve bu tuşlara
     basıldığında pano içeriğini değiştirmek isteyip istemediğinizin sorulmasına
     olanak tanır.
*   Belgeler script_add (Windows+NVDA+c) için düzeltildi.

## 5.0 için Değişiklikler ##

*   Diyaloğun görsel sunumu, NVDA'da gösterilen diyalogların görünümüne bağlı
    kalarak geliştirildi.
*   NVDA 2016.4 veya sonraki bir sürümü gerektirir.

## 4.0 için Değişiklikler ##
*   Eklenti ayarları NVDA konfigürasyonundan yönetilir, böylece farklı ayraçları
    kaydetmek için standart profiller kullanılabilir ve yeniden kurulum
    sırasında içe aktarma için ayarların kopyalanması gerekmez.
*   Artık, Pano İçerik düzenleyicisi ayarları iletişim kutusundaki metni pano
    verilerinden önce ekle onay kutusunu kullanarak, eklenecek metnin başa mı
    yoksa sona mı ekleneceğini seçmek mümkündür.

## 3.0 için Değişiklikler ##
*   MathPlayer kuruluysa, MathML nesnelerinin Braille gösterimi panoya
    eklenebilir.
*   Ayraç ayarlanmazsa, eklenen metin bölümleri arasına yalnızca tek bir satır
    yerleştirilir.
*   Pano İçerik Düzenleyicisi ayarları iletişim kutusunu açmak için bir kısayol
    atanabilir.
*   Eklentiyi yeniden yüklerken içe aktarılmak üzere ayırıcının kopyalanıp
    kopyalanmayacağını seçmek için ayarlar iletişim kutusuna bir onay kutusu
    eklendi.

## 2.0 için Değişiklikler ##
*   Hintçe karakterler, eklenen içerikler arasında ayraç olarak kullanılabilir.

## 1.0 için Değişiklikler ##
*   İlk versiyon.
