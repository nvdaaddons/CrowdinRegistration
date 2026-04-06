# Hata Ayıklama Yardımcısı

* Yazar: Luke Davis
* [Kararlı sürümü indir][1]

Bu eklentinin amacı, NVDA'da hata ayıklamayı kolaylaştırmaktır.
Kullanıcı önerilerine göre yeni özellikler eklenecektir. Geri bildirim veya özellik fikirleri içeren tüm e -postalar veya [GitHub sorunları](https://github.com/xltechie/debughelper) en hoş karşılanır.

## Kısayol

* NVDA+Shift+F1: NVDA günlüğüne bir işaret satırı ekler.

## Açıklama ve Kullanım

Komut tuşuna bastığınızda, eklenti NVDA günlüğüne (bilgi düzeyinde) aşağıdakiler gibi bir satır ekler:

```
-- İşaret 1 --
```

Ayrıca şunu da duyuracak: "Günlüğe Kaydedilen İşaret 1!"

Tuşa tekrar basarsanız, şunları elde edersiniz:

```
-- İşaret 2 --
```

ve "Kayıtlı İşaret 2!" konuşulacak.

Örneğin, NVDA günlüğünde uzun hata içeriği oluşturduğunu bildiğiniz bir dizi görevi gerçekleştirmek üzere olduğunuzu varsayalım. Günlüğünüzün ilgili bölümlerini bir posta listesine veya [VDA GitHub sorun izleyicisine](https://github.com/nvaccess/nvda/issues) gndereceksiniz. Ancak, ilgili içeriği bulmak için günlüğünüzün tamamında arama yapmak istemezsiniz. Yani bu eklentiyi, ilk hataya neden olan şeyi yapmadan hemen önce işaret 1'i eklemek için kullanırsınız. Başka bir şeyin daha fazla hata veya farklı türde bir hata oluşturacağını biliyorsanız, bu hatayı öncekinden ayırmak için başka bir işaret eklersiniz veya "bazı hataların meydana geldiği 3. işarette yaptığım şey buydu" diyebilirsiniz.
Başka bir örnek: Bazı uygulamaları kullanırken hataya neden olan bir şey olur (belki Windows hata sesini duyarsınız). Daha sonra geri dönüp bu hatayı bulmak istiyorsunuz, ancak çalışmayı durdurmak ve günlüğü hemen kaydetmek istemiyorsunuz. Bu nedenle, günlüğünüze bir işaret eklemek için bu eklentiyi tekrar kullanırsınız. Bu sefer işaret, günlüğünüzdeki hatalardan önce değil, sonra görünecektir. Ancak her iki durumda da işaretler, günlüğünüzün önemli bölümlerini daraltmanıza yardımcı olacaktır.

Yukarıda gösterilen işaret satırları, not defteri veya notepad ++ gibi bir metin düzenleyicisindeki Find komutuyla kolayca aranabilir.
Ayrıca, varsayılan olarak her işaretin üzerine boş bir satır eklenir. İşaretten sonra boş satırlar da mümkündür. NVDA'nın günlük görüntüleyicisini veya başka bir metin düzenleyicisini kullanıyorsanız ve belirli bir işareti bulmak için günlüğü hızlı bir şekilde yukarı/aşağı okumak için ok tuşlarını kullanmak istiyorsanız boş satırlar yardımcı olabilir. Günlükte hızla ilerlerken, konuşulan bir grup metinden "boş" kelimesini seçmek kolaydır. Gerçekten hızlı ok atarsanız, ayarlardan ayarlayabileceğiniz birden fazla boş satıra ihtiyacınız olabilir.

Not: İşaret sayısı, eklentilerin (NVDA+Kontrol+F3) yeniden yüklenmesinden sonra da geçerli olacaktır, ancak NVDA'yı yeniden başlattığınızda yeniden birden başlayacaktır.

## Yapılandırma:

NVDA Tercihlerinin Ayarlar bölümünde bir "Hata Ayıklama Yardımcısı" kategorisi bulacaksınız. Ayarlar iletişim kutusunda, her işaret satırından önce ve sonra eklenen boş satırların sayısını değiştirebilirsiniz. Varsayılan, önce bir satır ve sonra sıfırdır, ancak her ikisi için de 0 ila 10 satır kullanabilirsiniz. NVDA'nın Girdi Hareketleri panelinin Araçlar kategorisi altında, NVDA+Shift+F1'i istediğiniz bir tuş dizisine değiştirebilirsiniz.
NVDA'nın Girdi Hareketleri panelinin Araçlar kategorisi altında, NVDA+Shift+F1 tuş kombinasyonunu istediğiniz bir tuş dizisiyle değiştirebilirsiniz.

## Uyumluluk:

Bu eklenti NVDA sürümleri 2017.3 (Windows XP ile kullanılır) ve tüm yeni sürümlerle uyumludur. Son olarak 2019.3 ile test edildi.

## Değişiklik günlüğü

* Sürüm 1.0.2 (28-08-2019)
    - Çeviri ve Kod Temizleme.
* Sürüm 1.0.1 (26-08-2019)
    - Windows'un belirli sürümlerindeki bir yükleme sorununu muhtemelen düzeltmek için küçük hata düzeltme sürümü.
* Sürüm 1.0 (22-08-2019)
    - İlk sürüm. Aşağıdaki özellikler dahil:
        + Günlükte (bilgi düzeyinde) numaralı işaret satırları oluşturma yeteneği.
        + Her işaretleme satırından önce ve sonra 0-10 boş satır ekleyebilme.
        + NVDA Ayarları iletişim sistemi üzerinden yapılandırma.

[1]: https://addons.nvda-project.org/files/get.php?file=debughelper
