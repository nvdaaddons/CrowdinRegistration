# nvda Geliştirici ve Test Araç Kutusu

* Yazar: Cyrille Bougot
* NVDA uyumluluğu: 2019.2 ve sonrası
* [Kararlı Sürümü İndir][1]

Bu eklenti, NVDA hata ayıklama ve test için çeşitli özellikleri bir araya getirir.

## Özellikler

* NVDA'yı yeniden başlatırken bazı ek seçenekleri belirlemek için geliştirilmiş bir yeniden başlatma iletişim kutusu.
* Günlüğe kaydedilen hatalarla ilgili çeşitli özellikler.
* Nesne özelliği gezgini.
* Komut dosyası araçları: genişletilmiş komut dosyası açıklama modu ve komut dosyası açıcı.
* Günlük okuma ve analizine yardımcı olacak komutlar.
* Eski günlük yedekleri
* Python konsol çalışma alanında, bir nesnenin kaynak kodunu açmak için kullanılan bir işlev.
* Python konsolu için özel bir başlangıç ​​komut dosyası
* speech.speak işlevinin yığın izini günlüğe kaydetmek için bir komut.
* Arayüz öğelerini tersine çevirmek için bir komut.

## Komutlar

Bu eklenti, eklediği tüm yeni komutlar için katmanlı komutlar kullanır.
Bu komutların giriş noktası `NVDA+X`'tir; bu nedenle tüm komutlar `NVDA+X` tuşuna basıldıktan sonra başka bir harf veya hareketle yürütülmelidir.
`NVDA+X, H` tuşlarına basarak mevcut tüm katman komutlarını listeleyebilirsiniz.

Daha sık kullandığınız komutlar için, girdi hareketleri iletişim kutusunda doğrudan bir hareket tanımlayabilirsiniz.

## Gelişmiş Yeniden Başlat iletişim kutusu

`NVDA+X, Q` komutu, NVDA'yı yeniden başlatmadan önce bazı ek seçenekleri belirlemek için bir iletişim kutusu açar.
Belirtilebilecek seçenekler, `nvda.exe` ile kullanılabilen [komut satırı seçenekleri][2] ile aynıdır, örneğin yapılandırma yolu için `-c`, eklentileri devre dışı bırakmak için `--disable-addons` vb.

## Günlüğe kaydedilen hatalarla ilgili özellikler

### Son kaydedilen hatayı bildir

NVDA+X, E tuşlarına basarak, günlüğü açmaya gerek kalmadan son kaydedilen hatayı bildirebilirsiniz. İkinci kez basıldığında, hafızaya alınan son hata silinir.

### Günlüğe kaydedilen hatalar için bir ses çal

[“Kaydedilen hatalar için ses çal” ayarı][4] NVDA 2021.3 sürümünde eklenmiştir ve NVDA'nın bir hata kaydedildiğinde hata sesi çalmasını belirlemenizi sağlar.

Bu eklenti, bu ayarı değiştirmek için ek bir komut (`NVDA+X, shift+E`) sağlar.
Seçenekleriniz:

* “Yalnızca test sürümlerinde” (varsayılan) seçeneği, NVDA'nın yalnızca mevcut NVDA sürümü bir test sürümü (alfa, beta veya kaynaktan çalıştırılan) ise hata sesleri çalmasını sağlar.
* Geçerli NVDA sürümünüz ne olursa olsun hata seslerini etkinleştirmek için "Evet".

2021.3 öncesindeki NVDA sürümleri için, bu eklenti bu özelliğin geriye dönük uyumluluğunu ve klavye komutuyla kontrol etme imkanını sağlar.
Ancak, Gelişmiş ayarlar panelindeki onay kutusu geriye uyarlanmamıştır.

## Nesne özellik gezgini

Bu özellik, günlük görüntüleyiciyi açmadan mevcut gezgin nesnesinin bazı özelliklerinin raporlanmasına olanak tanır.

Bir nesnenin özelliklerini listelemek için gezgin nesnesini ona taşıyın ve aşağıdaki komutları kullanın:

* `NVDA+X, yukarı ok`: Bir önceki özelliği seçer ve gezgin nesnesi için bildirir.
* `NVDA+X, aşağı ok`: Bir sonraki özelliği seçer ve gezgin nesnesi için bildirir.
* NVDA+X, N : Gezgin nesnesi için seçili olan özelliği bildirir
* NVDA+X, shift+N : Gezgin nesnesi için seçili olan özelliği göz atılabilir bir mesajda görüntüler

Desteklenen özelliklerin listesi aşağıdaki gibidir:
ad, rol, durum, değer, windowClassName, windowControlID, windowHandle, konum, Python sınıfı, Python sınıfı mro.

Nesne gezinme komutlarını kullanırken, NVDA olağan nesne raporlaması yerine şu anda seçilen özelliğin rapor edilmesini de seçebilirsiniz.
Bir geçiş komutu olan `NVDA+X, kontrol+N`, nesnelerin bu özel raporlaması ile NVDA'nın normal raporlaması arasında geçiş yapmanızı sağlar.

Örneğin, “windowClassName” özelliğini seçip özel nesne raporlamasını etkinleştirebilirsiniz.
Ardından, gezgin nesnesini bir sonraki veya önceki nesneye taşıdığınızda, normal raporlama yerine nesnenin windowClassName adını duyacaksınız.

## Komut Dosyası Araçları

<a id="scriptOpener"></a>
### Komut dosyası açıcı

Script opener komutu, bir komut dosyasının hareketini bilerek kodunu açmaya olanak tanır.

Kullanmak için `NVDA+x, C` tuşlarına basın ve ardından kodunu görmek istediğiniz komut dosyasının hareketini yapın.
Örneğin, ön plandaki pencerenin başlığını bildiren komut dosyasının kodunu görmek için `NVDA+X, C` ve ardından `NVDA+T` tuşlarına basın.

Bu özelliğin çalışması için, eklentinin ayarlarında [favori editörünüzün komutunu](#settingsOpenCommand) yapılandırmış olmanız gerekir.
NVDA'yı kaynak kodundan çalıştırmıyorsanız, [NVDA kaynak kodunun konumu](#settingsNvdaSourcePath) da yapılandırılmış olmalıdır.

### Genişletilmiş komut dosyası açıklama modu

Genişletilmiş komut dosyası açıklama modu, girdi yardımı modunda açıklaması olmayan komut dosyaları hakkında raporlanmış bilgilere sahip olmanızı sağlar.

Genişletilmiş komut dosyası açıklama modu etkin olduğunda, giriş yardımı modu (NVDA+1) aşağıdaki şekilde değiştirilir.
Bir komut dosyasının açıklaması yoksa, komut dosyasının adı ve sınıfı bildirilir.
Bir komut dosyasının açıklaması varsa, açıklaması normal şekilde bildirilir.
Bu özelliği etkinleştirmek veya devre dışı bırakmak için kullanılacak tuş kombinasyonu `NVDA+X, D`'dir.

Girdi yardım kipinde açıklama olmadan bir komut dosyasına bağlı bir hareketin yürütülmesi, hareket yönetimi iletişim kutusunda bu komut dosyası için bir giriş oluşturur.
Bu giriş, “Açıklamasız komut dosyaları (kendi sorumluluğunuzda değiştirin!)” adlı özel bir kategoride yer almaktadır.
Bu, bu komut dosyası için yerel NVDA hareketlerini kolayca eklemenizi, silmenizi veya değiştirmenizi sağlar.
Bununla birlikte, bu tür komut dosyasının kullanıcının ilişkili hareketi değiştirmesini önleyecek herhangi bir açıklamaya sahip olmamasının genellikle amaçlandığını unutmayın.
Aslında, bu hareket bir uygulama kısayol tuşuna eşleştirilmek üzere tanımlanabilir.
Örneğin, NVDAObjects.window.winword.WordDocument üzerindeki script_toggleItalic komut dosyası control+I tuşuna bağlıdır ve bu tuş kombinasyonu uygulamaya aktarılarak kısayol tuşunu gerçekten çalıştırdığı için değiştirilmemelidir.

### Kullanım Örneği

Kontrol+shift+I tuşları, NVDA tarafından yerel olarak bildirilmese bile Word'de italik yazıyı da değiştirir.
NVDA tarafından kontrol+shift+I sonucunun kontrol+I olarak bildirilmesi için aşağıdaki adımları uygulamanız gerekir:

* Bir Word belgesi açın.
* NVDA+X, D tuşlarıyla genişletilmiş komut dosyası açıklama modunu etkinleştirin.
* NVDA+1 ile girdi yardım kipine girin.
* Kontrol+I tuşlarına basarak italik yazı tipini bildir ve bunu hareket diyalog penceresine ekle.
* NVDA+1 ile girdi yardım kipinden çıkın.
* Girdi hareketleri iletişim kutusunu açın.
* “Açıklamasız komut dosyaları (kendi sorumluluğunuzda değiştirin!)” kategorisinde, “toggleItalic on NVDAObjects.window.winword.WordDocument” komutunu seçin.
* Kontrol+Shift+I kısayolunu ekleyin ve onaylayın.
* İsterseniz, `NVDA+X, D` tuşlarıyla genişletilmiş komut dosyası açıklama modundan çıkabilirsiniz.

Bilinen hata: Hareket Yöneticisi başka bir bağlamda açılmış olsa bile belirli bir sınıf için eklenen bir komut dosyası görünür.

## Günlük okuma ve analiz özellikleri

<a id="logPlaceMarkers"></a>
### Günlüğe işaretler yerleştir

Test veya çalışma sırasında, günlüğü okurken daha sonra kolayca geri dönebilmek için günlüğün belirli bir anını işaretlemek isteyebilirsiniz.
Günlüğe bir işaret mesajı eklemek için `NVDA+X, K` tuşlarına basın.
BİLGİ düzeyinde aşağıdaki gibi bir mesaj kaydedilecektir:
`-- NDTT işaret 0 --`
Günlüğe istediğiniz kadar işaret ekleyebilirsiniz.
İşaretçinin numarası, günlüğe her işaretçi yerleştirdiğinizde artacaktır; yalnızca NVDA yeniden başlatıldığında sıfırlanacaktır.

### Günlük Okuyucu Modu

Günlük okuyucu modu, günlük okuma ve analizini kolaylaştırmak için komutlar sağlar.
Günlük görüntüleyici penceresinde günlük okuyucusu varsayılan olarak etkinleştirilir, böylece günlük okuma komutları anında kullanılabilir.
Editör (ör. Notepad++) veya web sayfası (ör. GitHub sorunu) gibi başka bir metin okuma alanında, günlük okuyucu modunu etkinleştirmek ve komutlarını kullanmak için `NVDA+X, L` tuşlarına basmanız gerekir.
Günlük okuma ve analiz görevlerini tamamladığınızda, günlük okuyucu modunu devre dışı bırakmak için `NVDA+X, L` tuşlarını tekrar kullanabilirsiniz.

Günlük okuyucu modunda kullanılabilen komutlar aşağıda açıklanmıştır.

<a id="logReaderQuickNavigationCommands"></a>
#### Hızlı gezinme komutları

Gözatma modundaki hızlı gezinme tuşlarına benzer tek harfli komutlar, çeşitli türdeki günlük mesajlarına geçmenizi sağlar:

* m: Herhangi bir mesaj
* e: Hata mesajları (`ERROR` ve `CRITICAL`)
* w: Uyarı Mesajları (`` uyarı '))
* f: Bilgi mesajları (`INFO`)
* k: daha önce [günlüğe yerleştirilmiş işaretçiler](#logPlaceMarkers)
* g: Hata ayıklama uyarı mesajları (`DEBUGWARNING`)
* i: Giriş/çıkış mesajları (`IO`)
* n: giriş mesajları
* s: konuşma mesajları
* d: Hata Ayıklama Mesajları (`DEBUG`)

Tek harfe basıldığında, bu mesajın bir sonraki geçtiği yere geçilir. Harfi shift tuşuyla birlikte kullanıldığında, bu mesajın bir önceki geçtiği yere geçilir.

#### Konuşma mesajının çevirisi

Bazen, anlamadığınız bir yabancı dilde bir sistemde alınan bir günlüğü incelemek zorunda kalabilirsiniz. Örneğin, günlük Çince bir sistemde / NVDA'da alınmışken, siz sadece Fransızca biliyorsunuz.
[Anında Çeviri][3] eklentisi yüklüyse, bunu [hızlı günlük gezinme komutları](#logReaderQuickNavigationCommands) ile birlikte kullanarak sesli mesajları çevirebilirsiniz.

* Öncelikle Anında Çeviri'nin dillerini yapılandırın. Kaynak dil, günlüğün alındığı sistemin dili olmalıdır (örneğin Çince). Hedef dil ise sizin diliniz olmalıdır (örneğin Fransızca).
* Günlüğü aç
* Günlükte otomatik konuşma çevirisini etkinleştirmek için t tuşuna basın
* Günlükteki Hızlı gezinme komutlarını kullanın, örneğin S, I, vb. Bir konuşma mesajıyla karşılaşıldığında, bu mesaj sizin dilinizde konuşulacaktır (önceki örneğimizde Fransızca)

Konuşma çevirisini devre dışı bırakmak istiyorsanız, T tuşuna tekrar basın.



<a id="logReaderOpenSourceFile"></a>
#### Kaynak kod dosyasını düzenleyicide aç

Günlükte bazı satırlar kaynak koduna atıfta bulunabilir:

* Geri izlemeye ait bir satır, bir dosyadaki yolu ve satırı içerir, örneğin:
  `  File "virtualBuffers\__init__.pyc", line 226, in _getStoryLength`
* Günlüğe kaydedilen bir mesajın başlık satırı, bu mesajı günlüğe kaydeden işlevi içerir, örneğin:
  `INFO - config.ConfigManager._loadConfig (22:45:26.145) - MainThread (16580):`
* Girdi yardım modunda günlüğe kaydedilen bir mesajın içeriği (bilgi düzeyinde günlüğe kaydedilir):
  `Girdi Yardımı: gesture kb(desktop):NVDA+t, globalCommands.GlobalCommands'da komut dosyası başlığına bağlı`

İzleme bilgisinin veya kaydedilen mesajın bağlamını anlamak için bu kodu içeren dosyayı açmak isteyebilirsiniz.
Bu dosyayı açmak için C tuşuna basın.

Bu özelliğin çalışması için, eklentinin ayarlarında [favori editörünüzün komutunu](#settingsOpenCommand) yapılandırmış olmanız gerekir.
NVDA'yı kaynak kodundan çalıştırmıyorsanız, [NVDA kaynak kodunun konumu](#settingsNvdaSourcePath) da yapılandırılmış olmalıdır.

<a id="oldLogsBackup"></a>
## Eski günlük yedekleri

NVDA, NVDA'nın önceki oturumunun günlüğünün yedeğini zaten sağlar; dosya adı `nvda-old.log` şeklindedir.
Bazen, örneğin `nvda-old.log` dosyasına bakmadan önce NVDA'yı yeniden başlatmak zorunda kaldığınız için, eski günlük dosyalarına erişmek isteyebilirsiniz.
Bu eklenti, eski günlükleri yedeklemek isteyip istemediğinizi ve kaç tanesini yedeklemek istediğinizi yapılandırmanıza olanak tanır; bu, [eklentinin ayarlarında](#settingsLogsBackup) yapılır.

Günlük yöneticisi iletişim kutusu, yedeklenen günlükleri görüntülemenizi sağlar.
NVDA menüsü -> Araçlar -> Günlük yöneticisine gidilerek açılabilir
Bu iletişim kutusunda, tüm yedekleme günlüklerinin listesini görebilir ve seçilen günlükte çeşitli eylemler gerçekleştirebilirsiniz:

* aç (`` enter 'tuşuna basın)
* sil (`Delete 'tuşuna basın)
* günlük dosyasını kopyala (`kontrol+C`)

Ayrıca, birden fazla günlüğü seçerek hepsinde aynı işlemi gerçekleştirebilirsiniz.

Bir günlüğü açabilmek için, önce [Tercih ettiğiniz düzenleyicide bir dosyayı açma komutunu](#settingsOpenCommand) yapılandırmış olmanız gerekir.

## Python konsol eklentisi

<a id="pythonConsoleOpenCodeFile"></a>
### `openCodeFile` fonksiyonu

Konsolda, 'myVar' değişkenini tanımlayan kaynak kodunu görüntülemek için aşağıdaki işlevi çağırabilirsiniz:
`openCodeFile(myVar)`

Bu özelliğin çalışması için, eklentinin ayarlarında [favori editörünüzün komutunu](#settingsOpenCommand) yapılandırmış olmanız gerekir.
NVDA'yı kaynak kodundan çalıştırmıyorsanız, [NVDA kaynak kodunun konumu](#settingsNvdaSourcePath) da yapılandırılmış olmalıdır.

`openCodeFile` işlevleri, NVDA'nın kodunda tanımlanan nesneler üzerinde veya eklentiler tarafından tanımlanan nesneler üzerinde çağrılabilir.
Python yerleşik işlevleri gibi kaynak kodu mevcut olmayan nesneler üzerinde çağrılabilir.

Nesneyi konsola henüz içe aktarmadıysanız, adını `openCodeFile` işlevine parametre olarak da aktarabilirsiniz.

Aşağıda NVDA kodunda çağrı örnekleri verilmiştir:

* `speech.speech.speak` fonksiyonunun tanımını görüntüleyin:
  `openCodeFile(speech.speech.speak)`
  veya parametre olarak iletilen adla:
  `openCodeFile("speech.speech.speak")`
* `TextInfo` sınıfının tanımını görüntüleyin:
  `openCodeFile(textInfos.TextInfo)`
* `TextInfo` sınıfının `copyToClipboard` metodunun tanımını görüntüleyin:
  `openCodeFile(textInfos.TextInfo.copyToClipboard)`
* Odaklanılan nesnenin sınıfının tanımını görüntüleyin:
  `openCodeFile(Odak)`
* `Api` modülünü tanımlayan 'api.py' dosyasını açın:
  `openCodeFile(api)`

### Python konsolu başlangıç ​​komut dosyası

Python konsolunun ilk açıldığında veya konsol açıldıktan sonra eklenti yeniden yüklendiğinde (NVDA+F3) konsolun ad alanında yürütülecek özel bir komut dosyası tanımlayabilirsiniz.

Örneğin, komut dosyası, aşağıda gösterildiği gibi, yeni içe aktarmaları yürütmenize ve doğrudan konsolda kullanabileceğiniz takma adları tanımlamanıza olanak tanır:

    # Konsolda istediğim çeşitli içe aktarmalar.
    globalVars'ı gv olarak içe aktar
    çekirdeği içe aktar
    Kullanıcı arayüzünü içe aktar
    # Takma adlar
    kda = Kod Dosyasını Aç

Python konsolu komut dosyası aşağıdaki konuma yerleştirilmelidir: `pathToNVDAConfig\ndtt\consoleStartup.py`
Örneğin: `C:\Users\kullanıcıadı\AppData\Roaming\nvda\ndtt\consoleStartup.py`

## Konuşma işlevinin yığın izlemesini günlüğe kaydet

Bazen, kodun hangi kısmının bir şeyi söylemekten sorumlu olduğunu görmek isteyebilirsiniz.
Bunun için, `NVDA+X, S` tuşlarına basarak konuşma işlevinin yığın izleme günlüğünü etkinleştirebilirsiniz.
NVDA her konuştuğunda, ilgili yığın izleme günlüğüne kaydedilir.

Not: Başka bir işlevi düzeltmek için komut dosyasını doğrudan değiştirebilirsiniz.
Kullanımla ilgili ayrıntılar için dosyadaki tüm talimatlara bakın.

<a id="reverseTranslationCommand"></a>
## Ters Çeviri Komutu

Birçok testçi NVDA'yı İngilizce'den başka bir dilde kullanır.
Ancak GitHub'da test sonuçlarını bildirirken, değiştirilen seçeneklerin açıklaması veya NVDA tarafından bildirilen mesajlar İngilizce yazılmalıdır.
Seçeneklerin veya mesajların tam olarak ne anlama geldiğini kontrol etmek için NVDA'yı İngilizce olarak yeniden başlatmak zorunda kalmak oldukça sinir bozucu ve zaman alıcı bir iş.

Bunu önlemek için, eklenti ters çeviri komutu (`NVDA+X, R`) sağlar ve NVDA'nın arayüzünü, örneğin mesajları, GUI'deki kontrol etiketlerini vb. tersine çevirmeye olanak tanır.
Bu komut, NVDA'nın gettext çevirisini kullanarak son konuşmayı tersine çevirmeye çalışır.
Daha spesifik olarak, son konuşma dizisinin ilk dizesi ters çevrilir.

Örneğin, Fransızca NVDA'da, “Outils” adlı Araçlar menüsüne aşağı ok tuşuyla gittiğimde, NVDA “Outils  sous-Menu  o” diye seslendirir, bu da “Araçlar  alt Menüsü  o” anlamına gelir.
Hemen ardından ters çeviri komutuna basarsam, NVDA “Outils” kelimesini “Tools” olarak ters çevirir.

Daha sonra günlüğe baktığımızda şu satırları bulabiliriz:
```
IO - speech.speech.speak (23:38:24.450) - Ana İş Parçacığı (2044):
Konuşma ['Outils', 'sous-Menu', CharacterModeCommand(True), 'o', CharacterModeCommand(False), CancellableSpeech (still valid)]
```
Bu, “Outils'ın konuşma dizisinde ilk kelime olduğunu” doğrulamaktadır.

Ters çevirinin iki veya daha fazla olası sonuç vermesi durumunda, tüm olasılıkları listeleyen bir bağlam menüsü açılır.

Ters çevirinin sonucu, ilgili [seçenek](#settingsCopyReverseTranslation) etkinleştirilmişse, varsayılan değer olan panoya da kopyalanır.

<a id="settings"></a>
## Ayarlar

Eklentinin bazı özellikleri belirli bir yapılandırma gerektirebilir.
Ayarlar paneli, bunları etkinleştirmenize veya nasıl çalıştıklarını kontrol etmenize olanak tanır.
Bu ayarları görüntülemek ve değiştirmek için NVDA Menüsü -> Tercihler adresine gidin ve NVDA Geliştirici ve Test Araç Kutusu kategorisini seçin.
Bu ayarlar iletişim kutusuna, Günlük Yöneticisi iletişim kutusundan da doğrudan erişilebilir.

Bu ayarlar genel ayarlardır ve yalnızca varsayılan profil etkin olduğunda yapılandırılabilir.

<a id="settingsOpenCommand"></a>
### Favori düzenleyicinizde bir dosya açma komutu

Bazı özellikler, içeriği favori düzenleyicinizde görüntülemenizi sağlar.
Buna, kaynak dosyayı [günlükten](#logReaderOpenSourceFile), [konsoldaki bir nesneden](#pythonConsoleOpenCodeFile) veya [yazılan bir hareketle](#scriptOpener) görüntüleme komutları ile [günlük yöneticisinin](#oldLogsBackup) Aç düğmesi dahildir.

Bunları kullanmak için, önce dosyayı favori düzenleyicinizde açmak için çağrılacak komutu yapılandırmanız gerekir.
Komut şu biçimde olmalıdır:
`"C:\path\to\my\editor\editor.exe" "{path}":{line}`
Elbette bu satırı, editörünüzün gerçek adı ve konumu ile dosyaları açmak için kullandığı sözdizimine göre değiştirmelisiniz.
`{path}`, açılacak dosyanın tam yolu ile ve `{line}`, imlecin yerleştirilmesini istediğiniz satır numarası ile değiştirilecektir.
Örneğin Notepad++ için konsola yazılacak komut şöyle olacaktır:
`"C:\Program Files\Notepad++\notepad++.exe" "{path}" -n{line}`

<a id="settingsNvdaSourcePath"></a>
### NVDA kaynak kodu yolu

Kaynak dosyayı görüntülemek için bir komut kullanırken [günlükten](#logReaderOpenSourceFile), [konsoldaki bir nesneden](#pythonConsoleOpenCodeFile) veya [yazılan bir hareketle](#scriptOpener), dosya NVDA'ya ait olabilir.
NVDA'yı kaynak koddan çalıştırmıyorsanız, NVDA'nız yalnızca derlenmiş dosyaları içerir.
Böylece, ilgili kaynak dosyanın bulunacağı alternatif bir konum belirtebilirsiniz, örneğin NVDA kaynak dosyalarını kopyaladığınız yer, böylece kaynak dosya yine de açılabilir.
Yol şu şekilde olmalıdır:
`C:\pathExample\GIT\nvda\source`
Elbette, NVDA kaynağının yolunu doğru olanla değiştirin.

Bununla birlikte, kaynak dosyanızın (ör. Git taahhüdü) sürümünün NVDA'nın çalışan örneğinden biri ile aynı olduğundan emin olun.

<a id="settingsLogsBackup"></a>
### Eski günlük yedekleri

Eski günlüklerin yedeklenmesi açılır menüsü, [özelliği](#oldLogsBackup) etkinleştirmenize veya devre dışı bırakmanıza olanak tanır.
Etkinleştirilirse, aşağıdaki “Yedekleme sayısını sınırla” bölümünde saklamak istediğiniz maksimum yedekleme sayısını da belirtebilirsiniz.
Bu ayarlar, yedekleme işlemi gerçekleştirildiğinde yalnızca bir sonraki NVDA başlatma sırasında etkili olur.

<a id="settingsCopyReverseTranslation"></a>
### Ters çeviriyi panoya kopyala

Bu seçenek, [ters çeviri komutu](#reverseTranslationCommand) sonucunu da panoya kopyalamayı seçmenizi sağlar.

## Değişiklik günlüğü

### Sürüm 7.1

* NVDA 2025.1 ile uyumluluk.

### Sürüm 7.0

* Katmanlı komutlar eklendi; giriş noktası 'NVDA+X'tir.
  Mevcut komutlar şuna göre değiştirildi.
* Son konuşulan mesajı tersine çevirmek için yeni bir komut (`NVDA+X, R`).
* Bir sonraki basılan harekete bağlı komut dosyasının kaynak kodunu açmak için yeni bir komut (`NVDA+X, C`).
* İsteğe bağlı konuşma desteği eklendi.
* Günlük yöneticisi artık, diyaloglardaki özel düğmelerle veya listedeki klavye kısayollarıyla daha fazla eylem gerçekleştirilmesine izin vermektedir: günlük dosyasını açmak için `enter`, günlük dosyasını kopyalamak için `control+C` ve günlük dosyasını silmek için `delete`.
* Günlük yöneticisindeki sıralama düzeni tersine çevrilmiştir (en son günlük en üstte).
* OpenCodeFile işleviyle bir Python modülünü açmaya çalışırken ortaya çıkan bir sorun düzeltildi.

### Sürüm 6.3

* NVDA 2024.1 ile uyumluluk.

### Sürüm 6.2

* NVDA < 2021.1 için konsol açılmasını geri yükler.
* Eklentiyi NVDA'nın eski sürümleriyle kullanırken [GHSA-xg6w-23rw-39r8][5] ile ilgili olası güvenlik sorunlarını giderir. Ancak NVDA 2023.3.3 veya üstü sürümlerin kullanılması önerilir.

### Sürüm 6.1

* Bir paketin alt modülünde bulunan bir nesnenin kaynak dosyasını açma işlevi artık çalışıyor.
* Hata düzeltmesi: Geliştirilmiş çıkış diyalog penceresi artık kapatıldıktan sonra yeniden açılabilir ve beklendiği gibi kullanılabilir. (Łukasz Golonka'nın katkısı)

### Sürüm 6.0

* Nesne gezinme komutlarını kullanırken, NVDA'nın normal nesne raporlaması yerine belirli bir nesne özelliği raporlanabilir.
* Günlük okuma modunda, günlükten bir kod dosyasını açmak için kullanılan “C” tuşu artık girdi yardım mesajında da çalışıyor.
* Hata düzeltmesi: Kaydedilecek günlüklerin sayısı maksimum değere ayarlandığında eklenti artık başarıyla başlatılabilir.
* Hata düzeltmesi: Python konsol başlangıç komut dosyasının çıktısı, sonuç gezinme komutları kullanıldığında konsolda ilk sonuca atlamayı artık engellemiyor.
* Not: Bundan sonra, yerelleştirme güncellemeleri değişiklik günlüğünde artık görünmeyecektir.

### Sürüm 5.0

* Anında çeviri eklentisi yüklenirse, artık günlük okuma komutlarını kullanırken konuşma mesajlarının anında tercüme edilmesi mümkündür.
* Günlük okuma modundayken, E veya shift+E tuşlarına basıldığında artık normal HATA mesajlarının yanı sıra KRİTİK hata mesajlarına da geçilir.
* Giriş ve konuşma mesajlarına atlamak için yeni günlük hızlı gezinme komutları eklendi.
* Yeni bir komut, günlüğe bir işaretleyici yerleştirmeye izin verir; ve günlük okuma modundaki belirli hızlı gezinme komutları bunlara atlamayı sağlar.
  Kredi: Bu özelliğe ilişkin ilk fikir, Luke Davis'in Debug Helper eklentisinden geliyor.
* Hata düzeltmesi: Bazı durumlarda son hatanın ezberlenmesi artık başarısız olmuyor.
* Hata düzeltmesi: Eklenti, NVDA 2019.2.1 ile yeniden başlatılabilir.
* Hata düzeltmesi: ASCII olmayan günlüklerde günlük kaydetme özelliği artık hata vermeyecek.

### Sürüm 4.2

* 2021.3 sürümünden önceki NVDA sürümlerinde yaşanan bir hata düzeltildi.
* Yığın izleme günlük biçimlendirme düzeltildi.
* İlk yerelleştirmeler.

### Sürüm 4.1

* Hata günlüğüne yazılırken bazı durumlarda meydana gelen bir hata düzeltildi.
* Eklentinin ayarları, yapılandırma sorunlarını önlemek için artık yalnızca varsayılan profil etkin olduğunda değiştirilebilir.

### Sürüm 4.0

* Eski günlükleri yedekleme imkanı ve günlük yöneticisinin tanıtımı.
* Son kaydedilen hatayı bildiren bir komut dosyası eklendi.
* Eski NVDA sürümlerinde son günlük mesajının okunmasını önleyen bir hata düzeltildi.

### Sürüm 3.2

* NVDA 2023.1 ile uyumluluk.

### Sürüm 3.1

* Bir nesne hakkında kullanılamayan bilgi isterken oluşan bir hata düzeltildi.

### Sürüm 3.0

* Bir günlükte, artık bir mesajın başlık satırında C tuşuna basarak onu gönderen işlevi/modülü açabilirsiniz.
* Konsolda, `openCodeFile` işlevi artık parametre olarak nesneyi veya adını içeren bir dizeyi alabilir.
* Yeni özellik: NVDA konsol başlangıç dosyası: Varsa, NVDA konsolu ilk açıldığında veya eklentiler yeniden yüklendiğinde YourNVDAConfigFolder\ndtt\consoleStartup.py dosyası çalıştırılır.
* Python konsolunun `openCodeFile` işlevi ve günlükteki bir satıra karşılık gelen kaynak dosyayı açma komutu için çeşitli küçük düzeltmeler.
* NVDA'nın eski sürümlerinde nesne gezgini için roller/durumlar bildirilmeye çalışıldığında ortaya çıkan bir sorun düzeltildi.
* Eklenti, Edge'de UIA kullanıldığında ağaç engelleyiciyle artık sorun yaratmıyor.

### Sürüm 2.1

* Tüm kullanım durumlarını ele almak için çeşitli hata düzeltmeleri ve kod yeniden düzenleme/temizleme: desteklenen tüm sürümler, yüklü ve kaynaktan çalıştırma vb. (Łukasz Golonka'nın katkısı)
* Compa Modülünün Yeniden Yazılması (łukasz Golonka'dan Katkı)
* Yeniden başlatma iletişim kutusu artık yalnızca bir kez açılabilir.
* Nesne gezgini kısayolları artık varsayılan olarak atanmamış durumdadır ve kullanıcı tarafından eşleştirilmesi gerekir.
* Nesne gezgini ile, mevcut nesnenin özelliğini bildirmek için komut dosyasını çağırmak üzere iki kez basıldığında, bildirilen bilgiler artık göz atılabilir bir mesajda görüntülenir.

### Sürüm 2.0

* Yeni özellik: NVDA'yı yeniden başlatırken bazı ekstra seçenekleri belirtmek için geliştirilmiş yeniden başlatma iletişim kutusu.
* Yeni özellik: genişletilmiş açıklama modu.
* NVDA'nın 2021.3 öncesi ve sonrası sürümleri arasında uyumlu hale getirilmiş hata sesi özelliği.
* Yeni özellik: Günlük okuyucu komutları artık günlük görüntüleyicide ve isteğe bağlı olarak düzenleme alanlarında veya web sayfalarında da kullanılabilir.
* Yeni özellik: Python konsolunda, bir nesnenin kaynak kodunu görüntülemek için `openCodeFile` işlevi kullanılabilir.
* Güvenlik nedenleriyle bazı özellikler güvenli modda devre dışı bırakılmıştır.
* Eklentinin uyumluluk aralığı genişletildi (2019.2'den 2021.1'e).
* Sürümler artık appVeyor yerine GitHub eylemiyle gerçekleştiriliyor.

### Sürüm 1.0

* İlk sürüm.

[1]: https://www.nvaccess.org/addonStore/legacy?file=nvdaDevTestToolbox

[2]: https://www.nvaccess.org/files/nvda/documentation/userGuide.html#CommandLineOptions

[3]: https://addons.nvda-project.org/addons/instantTranslate.en.html

[4]: https://www.nvaccess.org/files/nvda/documentation/userGuide.html#PlayErrorSound

[5]: https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
