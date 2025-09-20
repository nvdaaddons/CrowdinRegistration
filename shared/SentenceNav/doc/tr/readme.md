# nvda cümle dolaşımı
Cümle dolaşımı, metni paragraflar veya kelimeler yerine cümlelerle okumanızı sağlayan bir NVDA eklentisidir.

"Metin içeren bir sonraki paragrafa atla" özelliğinin ayrıca yüklenmesi gereken [MetinDolaşımı](http://github.com/mltony/nvda-text-nav/) eklentisine taşındığını lütfen unutmayın.
## Klavye Komutları
* Alt+Aşağı: Bir sonraki cümleye gider.
* Alt+Yukarı: Önceki cümleye gider.
* NVDA+Alt+S: Geçerli cümleyi söyler.
* Alt+Windows+Aşağı: Sonraki ifadeye gider.
* Alt+Windows+Yukarı: Önceki ifadeye gider.

"Metin içeren bir sonraki paragrafa atla" özelliğinin ayrıca yüklenmesi gereken [MetinDolaşımı](http://github.com/mltony/nvda-text-nav/) eklentisine taşındığını lütfen unutmayın.

## Notlar ve bilinen sorunlar
* Cümle işaretleme sezgisel algoritmalar tarafından yapılır ve %100 doğru değildir. Cümle Dolaşımı'nın zaman zaman hatalar yapması beklenebilir, örneğin bir cümleyi kırılmaması gereken yerde kırmak veya tam tersi şekilde iki cümle arasındaki sınırı kaçırmak ve bunları birlikte konuşmak gibi.
* 2.8 sürümünden itibaren Microsoft Word ve WordPad için deneysel destek eklenmiştir.
* Cümle dolaşımı tuş vuruşları Alt+Yukarı/Aşağı, uygulamalardaki yerleşik tuş vuruşlarıyla çakışabilir. Cümle Dolaşımı geliştiricileri mümkün olduğunca bu çatışmaları çözmek için çaba göstermektedir. Ancak, böyle bir durumla karşılaşırsanız, bu tuş vuruşunun Cümle Dolaşımı tarafından değil, uygulama tarafından işleneceğinden emin olmak için NVDA + F2 (Sonraki tuş vuruşunu yok say) tuşlarına basmak ve ardından çakışan tuş vuruşu Alt + Yukarı / Aşağı tuşlarına basmak basit bir çözümdür.

## Algoritma
Cümle Dolaşımı, cümle sınırlarını bulmak için düzenli bir ifade kullanır. Düzenli ifadede şunlar aranır:
* Nokta, ünlem işareti veya soru işareti gibi bir veya daha fazla "cümle bozucu" noktalama işareti ve hemen ardından bir veya daha fazla boşluk.
* Cümle ayırıcılar isteğe bağlı olarak parantez kapatma veya tırnak işareti gibi bir veya daha fazla "Atlanabilir" noktalama işareti takip edebilir.
* Cümle ayırıcılar isteğe bağlı olarak Vikipedi tarzı bir referans takip edebilir, örneğin [4] veya [alıntı gerekli].
* Cümle ayırıcılardan önce Dr., Mr., Prof. vb. istisnai kısaltmalar gelmemelidir. İstisnai kısaltmalar dile bağlıdır. İstisnai kısaltmalar, çoğu durumda cümlenin sonunu göstermeyen nokta ile yazılan kısaltmalar olarak tanımlanır.
* Cümle ayırıcılardan önce tek bir büyük harf gelmemelidir. Bu, George R. R. Martin gibi insanların baş harflerinde cümlelerin kırılmasını önlemek içindir. Büyük harf listesi dile bağlıdır.
* Alternatif olarak, normal ifade, tam genişlikte cümle ayırıcılardan biriyle eşleşebilir. Çince ve Japonca gibi bazı dillerde tam genişlikte noktalama işaretleri kullanılır ve cümle sınırı olarak sayılmak için ardından veya önünde herhangi bir şeyin gelmesi gerekliliği yoktur.
* Alternatif olarak, çift yeni satır cümle ayırıcı olarak sayılır.

Cümle algılama, aşağıdakilerle eşleşen başka bir normal ifade tarafından gerçekleştirilir:
* Bir veya daha fazla "cümle bozucu" noktalama işareti ve hemen ardından bir veya daha fazla boşluk.
* Ya da alternatif olarak, bir veya daha fazla "sabit genişlikli" ifade frenleyicisi, ardından boşluk gelme zorunluluğu olmaksızın.
* Veya alternatif olarak, çift yeni satır.

## Diğer ayarlar
* Birden fazla paragrafta cümleleri yeniden yapılandırın: cümleler birden fazla paragrafa yayılabilir. Bu genellikle hatalı biçimlendirilmiş PDF belgelerinde veya düz metin olarak yazılmış e-posta mesajlarında olur. Bu açılan kutu ile SentenceNav'a bu cümleleri tanımlamaya çalışmasını ve doğru şekilde konuşmasını söyleyebilirsiniz. Ancak bazen, cümle olması gerekmeyen paragrafları birlikte söyler. Bu durumda bu özelliği devre dışı bırakabilirsiniz.
* Uygulamalarda Cümle Dolaşımı'nı devre dışı bırak: Belirli uygulamalarda Cümle Dolaşımı'nı devre dışı bırakabilirsiniz. Örneğin, bazı uygulamalar diğer işlevleri gerçekleştirmek için Alt+Aşağı tuşlarını kullanır. Bu, cümle gezintisinin devre dışı bırakılacağı uygulamaların virgülle ayrılmış bir kara listesidir. Uygulamanızın adının ne olması gerektiğinden emin değilseniz, o uygulamaya geçin, NVDA konsolunu açmak için NVDA+Control+Z tuşlarına basın ve şunu yazın: "focus.appModule.appName" tırnak işaretleri olmadan yazarak mevcut uygulamanın adını öğrenin.

## Kaynak kodu
Kaynak kodu şu adreste mevcuttur: <http://github.com/mltony/nvda-sentence-nav>.

## İndirin
* Mevcut kararlı sürüm: [CümleDolaşımı](https://github.com/mltony/nvda-sentence-nav/releases/latest/download/SentenceNav.nvda-addon)
* Son Python 2 sürümü (NVDA 2019.2 ve öncesi ile uyumlu): [CümleDolaşımı v2.5](https://github.com/mltony/nvda-sentence-nav/releases/download/v2.5/SentenceNav-2.5.nvda-addon)
