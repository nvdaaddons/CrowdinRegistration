# Gelişmiş dokunmatik ekran hareketleri #

* Yazarlar: Joseph Lee ve Kefas Lungu

Bu eklenti NVDA'ya ek dokunma hareketleri ekler. Ayrıca tarama kipinde daha kolay dolaşım için ek hareketler sunar.

Not: Bu eklenti, Windows 10 veya 11 yüklü dokunmatik ekranlı bir bilgisayarda NVDA 2024.1 veya sonrası sürümlerin çalışmasını gerektirir.

## Hareketler

### Her yerde kullanılabilen hareketler

* 4 parmakla çift dokunma: girdi yardımını açıp kapatır.
* Dört parmakla sağa fiske: dokunmatik klavyeyi açıp kapatır (genellikle açar).
* Dört parmakla sola fiske: dikteyi açıp kapatır (Windows+H; Windows 10 1709 sürümü veya daha sonrası).
* 4 parmakla yukarı fiske: Odaklanılan pencerenin başlığını söyler.
* 4 parmakla aşağı fiske: Durum çubuğu metnini okur.
* 3 parmakla aşağı fiske: odaklanılan pencereyi okur.
* 3 parmakla sola fiske: odaklanılan nesneyi söyler.
* 3 parmakla sağa fiske: nesne sunucusunun odaklanmış olduğu nesneyi söyler.
* 3 parmakla çift dokunma: Hangi simgelerin söyleneceğini belirleyen konuşma simgesi düzeyleri arasında geçiş yapar
* 2 parmakla üç kez dokunma: NVDA'dan çıkar!.
* 4 parmakla dokunma: Ses Zayıflaması modları arasında geçiş yapar.
* Üç kez dokunma: Bip sesleri, konuşma, bip sesleri ve konuşma arasında geçiş yapar ve kapatır.

## Web dokunma kipi

Tarama kipinde geçiş yapılan bu kip, belgeyi seçilen öğe türüne göre dolaşmanızı sağlar. Web kipine geçmek için, tarama kipindeyken ve bir belgenin içindeyken üç parmakla dokunun. Bu kipte bir parmakla yukarı veya aşağı fiske yaparak mevcut olan öğe dolaşım modları arasında dolaşabilir, bir parmakla sağa veya sola fiske yaparak sırasıyla sonraki veya önceki öğeye gidebilirsiniz. Tarama kipinin kullanıldığı belgeden uzaklaştığınızda öğe dokunma kipine geçiş yapılır.
Mevcut web modları: varsayılan, bağlantılar, düğmeler, form alanları, başlıklar, çerçeveler, tablolar, listeler, grafikler ve yer işaretleri.
## Sentezleyici ayarları dokunma kipi

Ses seçimi, ses seviyesi gibi sentezleyici ayarlarını yapmak için bu kipi kullanabilirsiniz. İki parmakla sola veya sağa fiske yaparak sentezleyici ayarları arasında dolaşabilir, iki parmakla yukarı veya aşağı fiske yaparak ayarları değiştirebilirsiniz. Bu hareketler klavyedeki hızlı sentezleyici ayarlarını dokunmatik ekrana aktarır.

## Sürüm 25.07

* Pyright (bir Python statik tür denetleyicisi) yardımıyla eklenti kodu daha sağlam hale getirildi.

## Sürüm 25.02

* Windows 8.1 için sınırlı destek geri yüklendi.

## Sürüm 25.01

* Eklenti sürümlerinin indirme bağlantıları artık eklenti belgelerine dahil edilmemektedir. Eklentiyi NV Access eklenti mağazasından indirebilirsiniz.
* Linting aracı Flake8'den Ruff'a değiştirildi ve NVDA kodlama standartlarıyla daha iyi uyum sağlamak için eklenti modülleri yeniden biçimlendirildi.
* Eklenti Güncelleyici eklentisinden otomatik eklenti güncellemeleri özelliği desteği kaldırıldı.

## Sürüm 24.05

* Eklentiyi kullanabilmek için NVDA 2024.1 veya sonrası gerekli.

## Sürüm 23.06.1

* nvda'nın konuşma durdurma komutuyla çakışması nedeniyle sesin kısılması 4 parmakla dokunmaya taşındı.

## Sürüm 23.06

* Geliştirilmiş Dokunma hareketleri nvda-EKLENTİSİ artık Kefas Lungu tarafından korunuyor.
* Nesne modundaki tüm hareketler artık her yerde kullanılabiliyor.
* Artık yeni hareketler mevcut.
  * 3 parmakla çift dokunma: Hangi simgelerin söyleneceğini belirleyen konuşma simgesi düzeyleri arasında geçiş yapar
  * 2 parmakla üç kez dokunma: NVDA'dan çıkar!.
  * 4 parmakla dokunma: Ses Zayıflaması modları arasında geçiş yapar.
  * Üç kez dokunma: Bip sesleri, konuşma, bip sesleri ve konuşma arasında geçiş yapar ve kapatır.
* Web modunda, halihazırda mevcut olan göz atma öğesi listesine ek olarak düğmeleri, grafikleri ve yer işaretlerini kullanmak artık mümkün.
* Web modunda, diğer göz atma öğeleri listesinden varsayılan gezinmeye geçtiğinizde NVDA artık normal değil, varsayılan diyecek. Örneğin, düğmelerden geçiş yaparken NVDA artık varsayılan diyecek.

## Sürüm 23.02

* Eklentiyi kullanabilmek için NVDA 2022.4 veya sonrası gerekli.
* Windows 10 21H2 (Kasım 2021 Güncelleme/Build 19044) veya daha sonraki sürümler gereklidir.

## Sürüm 23.01

* Eklentiyi kullanabilmek için NVDA 2022.3 veya sonrası gerekli.
* Windows 8.1 Ocak 2023 itibariyle Microsoft tarafından artık desteklenmediğinden Windows 10 veya daha sonraki sürümler gereklidir.
* Girdi hareketleri iletişim kutusunda, Geliştirilmiş Dokunmatik Hareketler kategorisi altındaki dokunmatik klavye ve dikte geçiş komutlarını yeniden atamak mümkündür.
* Windows 10'da çözüldüğü için dokunmatik klavye tuşları için salt okunur durum geçici çözümü kaldırıldı.

## Sürüm 22.03

* Eklentiyi kullanabilmek için NVDA 2021.3 veya sonrası gerekli.
* Eklentiyi Windows 7, 8 ve 8.1'e yüklemeye çalışırken bir uyarı mesajı gösterilecek.

## Sürüm 21.10

* Bu eklentiyi etkileyen NVDA'daki değişiklikler nedeniyle NVDA 2021.2 veya sonraki sürümler gereklidir.

## Sürüm 21.08

* Windows 11 için ilk destek.

## Sürüm 21.01

* Eklentiyi kullanabilmek için NVDA 2020.3 veya sonrası gerekli.
* Windows 10 1709 veya daha üzeri sürümlerinde dört parmak sola fiske dikteyi açıp kapatır (Windows+H).
* Eklentiden dokunmatik etkileşim desteği ayarı kaldırıldı.
* Dokunmatik etkileşim desteği ayarı NVDA'nın dokunmatik etkileşim ayarlarından değiştirilebildiğinden, geliştirilmiş dokunmatik ekran hareketleri ayarları iletişim kutusu kaldırıldı.

## Sürüm 20.09

* NVDA'nın 10 saniye boyunca dokunmatik ekran desteğini devredışı bırakmaya yarayan dokunmatik hareketi yoksayma özelliği kaldırıldı.
* Bip sesi ile koordinat belirtme özelliği kaldırıldı.

## Sürüm 20.07

* Dokunmatik etkileşimi veya dokunmatik hareket yoksayma özelliğini açıp kapatmak için bir klavye kısayolu eklendi (Kontrol+Alt+NVDA+T).
* NVDA 2020.1 veya üzeri sürümlerde sağ fare tıklaması bir parmakla dokunup basılı tutularak gerçekleştirilebildiğinden, söz konusu komut eklentiden kaldırıldı. Eklentiyi kullanabilmek için NVDA 2020.1 veya daha üzeri bir sürüm gerekli.
* NVDA'nın dokunmatik ekran desteğini 10 saniye boyunca devredışı bırakmaya yarayan dokunmatik hareketi yoksayma özelliği kaldırıldı. Gelecekte aynı komutla dokunmatik etkileşim ayarı değiştirilebilecek.
* NVDA snapshotlarında yapılan dokunmatik etkileşim değişikliklerinden dolayı, dokunmatik hareketi yoksayma özelliği ve geliştirilmiş dokunmatik ekran hareketleri ayarları iletişim kutusu devredışı bırakılacak. Dokunmatik hareketi yoksayma özelliğini açıp kapatmayı sağlayan ayar dokunmatik etkileşimi açıp kapatmak için kullanılacak.
* Bip sesi ile koordinat belirtme özelliği devredışı bırakıldı ve gelecek bir sürümde kaldırılacak.
* Dokunmatik klavye kullanılırken bip sesi ile koordinat belirtilmeyecek.
* Emoji gibi modern giriş olanakları dokunmatik etkileşim yoluyla kullanılırken NVDA hiçbir şey yapmıyormuş gibi görünmeyecek veya hata sesi çalmayacak.
* NVDA, dokunmatik klavye etkinleştirilemiyorsa bir hata mesajı verecek (dört parmakla sağa fiske hareketi).

## Sürüm 20.06

* Flake8 ile ilgili birçok kodlama biçimi sorunu ve potansiyel hata düzeltildi.

## Sürüm 20.04

* Fare ile sağ tıklama hareketi (bir parmakla dokunup basılı tutma) NVDA 2020.1 sürümüne eklendi.

## Sürüm 20.01

* Eklentiyi kullanabilmek için NVDA 2019.3 veya sonrası gerekli.
* Dokunmatik ekran desteği tamamen kapatıldığında, dokunmatik hareketi yoksayma özelliği dahil olmak üzere dokunmatik destek ayarı kullanılamayacak.

## Sürüm 19.11

* Ek hareketler için girdi yardımı mesajları eklendi.

## Sürüm 19.09

* Dokunmatik ekran desteği önceden sadece normal profili dışındaki profillerde devredışı bırakılabiliyordu. Artık her yerden devredışı bırakılabiliyor.

## Sürüm 19.07

* Gelecek NVDA sürümlerini desteklemek için dahili değişiklikler yapıldı.

## Sürüm 18.12

* Gelecekteki NVDA sürümlerini desteklemek için dahili değişiklikler.

## Sürüm 18.08

* Eklenti NVDA 2018.3 ve üzeri sürümler için uyumlu hâle getirildi.

## Sürüm 18.06

* Eklenti ayarları NVDA'nın çok kategorili eklenti ayarları iletişim kutusuna taşındı. Sonuç olarak eklentiyi kullanabilmek için NVDA 2018.2 sürümü gerekli.
* WxPython 4 ile ilgili uyumluluk sorunları giderildi.

## Sürüm 18.04

* Eklentinin yaptığı değişikliklerden dolayı NVDA ayarları iletişim kutusundaki dokunmatik etkileşim kategorisinde hata sesleri duyulma sorunu giderildi.

## Sürüm 18.03

* Eklentiyi kullanabilmek için NVDA 2018.1 sürümü gerekli.
* Dokunmatik yazma onay kutusu NVDA 2018.1 sürümüne eklendiğinden söz konusu onay kutusu eklentiden kaldırıldı.

## Sürüm 17.12

* Eklentiyi kullanabilmek için NVDA 2017.4 sürümü gerekli. Eklenti konfigürasyon profillerini destekliyor.
* NVDA 2017.4 sürümüne ekran yönü duyurma özelliği eklendiğinden söz konusu özellik eklentiden kaldırıldı.
* Dokunmatik etkileşim iletişim kutusuna dokunmatik ekran desteğini tamamen devredışı bırakmaya yarayan gizli bir onay kutusu eklendi. Söz konusu onay kutusu normal konfigürasyon profili dışında profiller etkinken kullanılabiliyor.
* NVDA 2018.1 veya üzeri sürümleri kullanıyorsanız NVDA'nın ayarlar menüsünde dokunmatik etkileşim iletişim kutusu iki kez görünecektir. İkinci iletişim kutusu eklentiye aittir.
* NVDA 2018.1 veya üzeri sürümleri kullanıyorsanız eklentiye ait olan dokunmatik etkileşim iletişim kutusunda dokunmatik yazma modu görünmeyecek.

## Sürüm 17.10

* Microsoft'un destek poliçesinden dolayı Windows 8 (orijinal sürüm) artık desteklenmiyor.
* NVDA 2017.4 snapshotlarında NVDA ekran yönünü iki kez söylemeyecek.

## Sürüm 17.07.1

* Dokunmatik etkileşim iletişim kutusuna dokunmatik hareketi yoksayma özelliğini süresiz şekilde kullanabilmek için bir seçenek eklendi.
* Dokunmatik hareketi yoksayma özelliği el ile kapatıldığında, dokunmatik hareketi yoksayma özelliğinin süresi dolmadan önce özellik açıldığında, dokunmatik etkileşimin devreye girme sorunu düzeltildi.

## Sürüm 17.07

* NVDA'nın ayarlar menüsüne NVDA'nın dokunmatik ekranlarla çalışma şeklini ayarlamaya yarayan dokunmatik etkileşim iletişim kutusu eklendi.
* Eklentinin bu sürümünü kurduktan sonra dokunmatik klavyede tuşlara çift dokunarak basılabilir. Eski kullanıma dönmek için dokunmatik etkileşim iletişim kutusundan dokunmatik yazmayı etkinleştirebilirsiniz.
* NVDA'nın dokunmatik hareketleri 10 saniye boyunca yoksaymasına yarayan, kısayol tuşu atanmamış bir komut eklendi.
* Dokunmatik etkileşim iletişim kutusuna NVDA'nın dokunmatik etkileşimini 3-10 saniye süre boyunca devredışı bırakma özelliğini ayarlamak için bir seçenek eklendi. Bu özellik dokunmatik hareketleri NVDA çalışmıyormuş gibi sisteme doğrudan aktarır. Varsayılan süre 5 saniyedir.
* Fareyle sağ tıklandığında (bir parmakla dokunup basılı tutma) NVDA günlüğüne hata ayıklama seviyesinde hata ayıklama mesajları kaydediliyor. Bu özellik NVDA 2017.1 veya daha üzeri sürümünü gerektirir.
* Ekran koordinatlarını duyurma ile ilgili yapılan değişikliklerden dolayı eklentiyi kullanabilmek için NVDA 2017.1 sürümü veya daha üzeri gerekli.

##Sürüm 17.03

* NVDA 2017.1 veya daha üzeri bir sürümü kullanılırken, koordinat sesinin çalınmaması veya hata sesi çalınmasıyla ilgili bir sorun düzeltildi.

##Sürüm 16.12

* Microsoft Edge, Microsoft Word ve diğerleri gibi tarama modu kullanılan uygulamalarda web dokunma kipi çalışıyor.
* Web dokunmatik kipi öğelerine listeler ve sınır imleri eklendi.

## Sürüm 16.06

* İlk kararlı sürüm.

[1]: https://addons.nvda-project.org/files/get.php?file=ets
