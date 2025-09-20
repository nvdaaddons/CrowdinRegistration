# NVDA için Proxy Desteği

* Yazar: José Manuel Delicado
* NVDA uyumluluğu: 2023.3.4 ve sonrası
* [kararlı sürümü indir][1]

Bu eklenti, NVDA ekran okuyucusunun bir veya daha fazla proxy sunucusu aracılığıyla İnternet'e bağlanmasına olanak tanır. Bunu mümkün kılmak için, standart Python kitaplığına çeşitli yamalar uygular veya seçilen konfigürasyona bağlı olarak belirli ortam değişkenlerini değiştirir. NVDA'yı ve eklentilerini kurumsal ortamınızdan otomatik olarak güncelleyebilecek ve hatta kuruluş proxy sunucunuzun izin vermesi koşuluyla uzak oturumlar gerçekleştirebileceksiniz.

## Özellikler

* Çeşitli proxy sunucu türleri için destek: http, çorap4 ve çorap5.
* Tüm trafiği proxy sunucusu veya yalnızca belirli trafik (http, https, ftp) üzerinden yeniden yönlendirme yeteneği.
* Tüm trafiği bir proxy sunucusu üzerinden yeniden yönlendirme ve ardından belirli trafiği diğer sunucular (iç içe geçmiş proxy'ler) üzerinden yeniden yönlendirme yeteneği.
* Profil değiştirme ve yapılandırma sıfırlama farkındalığı: Genellikle NVDA'nın taşınabilir bir kopyasıyla çalışıyorsanız, farklı ortamlar (ev, iş, ofis1, ofis2) için çeşitli profiller oluşturabilir ve bunları manuel olarak etkinleştirebilirsiniz.

## Kullanım

Bu eklenti, NVDA Ayarları iletişim kutusuna "Proxy" adlı yeni bir kategori ekler. Bu kategoride dört ayar grubu bulacaksınız. Birincisi, tüm trafik için genel bir proxy yapılandırmanıza izin verir. Diğer gruplar Proxy sunucularını yalnızca belirli protokoller için yapılandırmanıza izin verir. Tüm grupların aşağıdaki alanları vardır:

* Ana bilgisayar: proxy sunucusunun ana bilgisayar adı veya ip adresi. Söz konusu proxy'yi devre dışı bırakmak için boş bırakın.
* Bağlantı noktası: sunucu bağlantı noktası.
* Kullanıcı adı: isteğe bağlı. Sunucu yetkilendirmesi için kullanıcı adı.
* Şifre: isteğe bağlı. Sunucu yetkilendirmesi için parola. Socks4 sunucuları için şifre gerekmediğini unutmayın.

Önceki alanlara ek olarak, ilk ayarlar grubunda aşağıdaki seçenekler mevcuttur:

* SOCKS proxy türü: socks4, socks5 veya http seçilebilir.
* Mümkünse dns istekleri için proxy kullan: Bu onay kutusu işaretlendiğinde, ana bilgisayar adları veya alan adları doğrudan proxy sunucusuna gönderilir ve burada çözümlenir. İşareti kaldırıldığında, isimler yerel olarak çözülecek ve sunucu sadece hedef ip adresini alacaktır. Tüm stock4 proxy sunucularının bu seçeneği desteklemediğini unutmayın.

Genellikle çoğu kullanıcının yalnızca ilk ayar grubunu yapılandırması gerekir. Proxy ayrıntılarınızı bilmiyorsanız, daha fazla bilgi için kuruluş ağ yöneticinize danışın.

## Sınırlamalar

* Çok sınırlı IPV6 desteği.
* UDP trafiği tüm proxy sunucularında desteklenmez.
* Harici DLL kitaplıkları bu eklentide yapılandırılan ayarlara uymaz.
* Http proxy sunucuları için yalnızca temel kimlik doğrulama desteklenir. Özet kimlik doğrulaması desteklenmiyor.
* Tüm trafiği (https bağlantıları dahil) bir http proxy üzerinden yeniden yönlendirmek için sunucunun CONNECT http yöntemini desteklemesi gerekir.
* Bir "doğrudan bağlantı" modu yapılandırılamaz. Belirli bir proxy'yi devre dışı bırakırsanız, bunun yerine sistem varsayılanı kullanılır.

## Değişiklik Günlüğü

### Sürüm 1.2

* NVDA 2023.1 ile uyumlu.
* Güvenlik sebeplerinden dolayı minimum NVDA sürümü 2022.4'e ayarlanmıştır.
* Çeviriler güncellendi.

### Sürüm 1.1

* NVDA 2022.1 ile uyumlu.
* Güvenlik sebeplerinden dolayı minimum NVDA sürümü 2021.1'e ayarlanmıştır.
* "Mümkünse dns istekleri için proxy kullan" onay kutusu işaretlendiğinde ve genel bir proxy yapılandırıldığında socket.getaddrinfo işlevini yama.
* Çeviriler güncellendi.

### Sürüm 1.0

* İlk sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=nvdaproxy
