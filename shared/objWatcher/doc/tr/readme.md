# nesne İzleyici

**Bu NVDA eklentisi, gezinme nesnelerinin özniteliklerindeki değişiklikleri izler.**

* Yazarlar: Cary-rowen (<manchen_0528@outlook.com>), hwf1324 (<1398969445@qq.com>)
* Uyumluluk: NVDA 2023.1 veya sonrası

## Olası Kullanım Örnekleri

1. **Altyazı ve Şarkı Sözleri İzleme:**
   Belirli oynatıcıların altyazılarını veya şarkı sözlerini izleyebilir ve yenilendiğinde otomatik raporlamayı etkinleştirebilir.
2. **Sohbet Etkinliği İzleme:**
   Unigram veya WeChat konuşma listesindeki grup sohbeti listesinde ilgi çekici öğeleri izle. Yeni mesajlar otomatik olarak raporlanabilir ve arka plan raporlaması desteklenir.
3. **Test ve hata ayıklama:**
   Düzenleme sırasında satır ve sütunlardaki değişiklikleri otomatik olarak bildirmek için not defteri gibi uygulamaların durum çubuğunu izler.

## Kısayollar

### İzleyici Katmanı Komutları

`NVDA+Alt+W` tuşlarına basarak izleme katmanını etkinleştirin. Burada izleme eylemlerini gerçekleştirebilirsiniz:

- **Sayısal tuşlar (0-9):** Geçerli gezgin nesnesini belirli bir konuma ekler veya o konumda zaten izlenmekte olan bir nesnenin durumunu bildirir.
- **Sil:** Son izlenen nesneyi kaldırmak için bir kez basın; İzlenen tüm nesneleri kaldırmak için iki kez basın.
- **T:** Geçerli ön plan penceresinin izleme durumunu değiştirir.
- **P:** Tüm izleme etkinliklerini duraklatır veya devam ettirir.
- **Escape:** İzleyici katmanından çıkar.

İzleyici katmanına girerken eklenti mevcut durumu duyurur:

- *"Hiçbir öğe izlenmiyor. Lütfen izlenecek öğeler ekleyin."*
- *"İzleme devam ediyor. {n} öğe izleniyor."*
- *"İzleme duraklatıldı. {n} öğe izleme listesinde."*

### Diğer Kısayollar

Aşağıdaki eylemler desteklenir ancak atanmış varsayılan hareketler yoktur. Kullanıcılar, Girdi Hareketleri iletişim kutusu aracılığıyla bu eylemlere hareketler atayabilir:

- **Geçerli gezgin nesnesini izleme listesine ekler.**
  - **Not:** Bu eylem yalnızca ana tuşun bir değiştirici ile birlikte sayısal bir tuş (0–9) olduğu hareketlere atanabilir, örneğin `NVDA+Alt+0–9`.
- **Geçerli pencerenin izleme durumunu değiştirir.**
- **İzlemeyi duraklat/devam ettir arasında geçiş yapar.**
- **Son izlenen nesneyi silmek için bir kez basın; İzlenen tüm nesneleri silmek için iki kez basın.**

## Ayarlar

Aşağıdaki seçenekleri yapılandırmak için NVDA’nın Tercihler menüsünden Ayarlar Paneline erişin:

- **İzleyici Zamanlayıcı Aralığı:** İzleme aralığını milisaniye cinsinden ayarlayın (varsayılan 100 ms'dir)

## Katkıda bulunanlar

- **Yazarlar:**
  - Cary-rowen: Çekirdek geliştirici
  - hwf1324: Kod katkısı sağlayan
  - Ibrahim Hamadeh: Kod katkısı sağlayan

- **Yerelleştirmeye Katkıda Bulunanlar:**
  - Ibrahim Hamadeh: Arapça çeviriler
  - VovaMobile: Ukrayna çeviriler

**Yerelleştirmeye katkıda bulunan diğer kişilerin adlarını istediğiniz şekilde bana bildirmekten çekinmeyin.**

## Katkı

1. [GitHub][GitHub] aracılığıyla yeni özellikler veya yerel çeviriler için çekme isteklerini (PRS) gönderin.
2. [GitHub Sorunları sayfası][GitHubIssue] aracılığıyla hataları bildirin veya geri bildirim sağlayın.

## Sürüm Notları
### Sürüm 1.0.2
- Belge Markdown işleme sorunu düzeltildi.

### Sürüm 1.0.1
- Eklenen nesnelerin yinelenmesi sorunu düzeltildi
- Diğer iyileştirmeler

### Sürüm 1.0.0
- İzleyici katmanı komutları eklendi ( ). NVDA+Alt+W.
- Birden fazla nesne için izleme özelliği eklendi.
- Ön plandaki pencerenin hızlı izlenmesi eklendi.
- İzlemeyi duraklatma/devam ettirme desteği.

### Sürüm 0.4.5
- Yerelleştirme güncellemeleri.

### Sürüm 0.4.4
- NVDA2024.1'de isteğe bağlı konuşma modu desteklenmektedir.
- Yerelleştirme güncellemeleri.

### Sürüm 0.4.0
- Nesneleri izlemek için yapılandırılabilir bir zamanlayıcı aralığı eklendi.

[GitHub]: https://github.com/cary-rowen/objWatcher
[Github sorun]: https://github.com/cary-rowen/objWatcher/issues
