# nvda Geliştirici ve Test Araç Kutusu

* Yazar: Cyrille Bougot
* NVDA uyumluluğu: 2019.2 ve sonrası
* [Kararlı Sürümü İndir][1]

Bu eklenti, NVDA hata ayıklama ve test için çeşitli özellikleri bir araya getirir.

## Özellikler

* An enhanced restart dialog to specify some extra options when restarting NVDA.
* Günlüğe kaydedilen hatalarla ilgili çeşitli özellikler.
* An object property explorer.
* Script tools: an extended script description mode and a script opener.
* Commands to help log reading and analyzing.
* Eski günlük yedekleri
* In the Python console workspace, a function to open the source code of an object.
* Python konsolu için özel bir başlangıç ​​komut dosyası
* A command to log the stack trace of the speech.speak function.
* A command to reverse translate the items of the interface.

## Komutlar

This add-on uses layered commands for all of the new commands it adds.
The entry point for these commands is `NVDA+X`; thus all the commands should be executed by `NVDA+X` followed by another single letter or gesture.
You can list all the available layered commands pressing `NVDA+X, H`.

For the commands that you use more frequently, you can also define a direct gesture in the input gesture dialog.

## Gelişmiş Yeniden Başlat iletişim kutusu

The `NVDA+X, Q` command opens a dialog to specify some extra options before restarting NVDA.
The options that can be specified correspond to the [command line options][2] that can be used with `nvda.exe`, e.g. `-c` for config path, `--disable-addons` to disable add-ons, etc.

## Günlüğe kaydedilen hatalarla ilgili özellikler

### Son kaydedilen hatayı bildir

Pressing `NVDA+X, E` allows to report the last error logged without needing to open the log. A second press clears the memorized last error.

### Günlüğe kaydedilen hatalar için bir ses çal

The ["Play a sound for logged errors" setting][4] has been introduced in NVDA 2021.3 and allows to specify if NVDA will play an error sound in case an error is logged.

Bu eklenti, bu ayarı değiştirmek için ek bir komut (`NVDA+X, shift+E`) sağlar.
You can choose:

* "Only in test versions" (default) to make NVDA play error sounds only if the current NVDA version is a test version (alpha, beta or run from source).
* "Yes" to enable error sounds no matter your current NVDA version.

For NVDA prior to 2021.3, this add-on provides the backport of this feature and the possibility to control it with the keyboard command.
The checkbox in the Advanced settings panel is not backported however.

## Nesne özellik gezgini

Bu özellik, günlük görüntüleyiciyi açmadan mevcut gezgin nesnesinin bazı özelliklerinin raporlanmasına olanak tanır.

Bir nesnenin özelliklerini listelemek için gezgin nesnesini ona taşıyın ve aşağıdaki komutları kullanın:

* `NVDA+X, upArrow`: Selects the previous property and reports it for the navigator object.
* `NVDA+X, downArrow`: Selects the next property and reports it for the navigator object.
* NVDA+X, N : Gezgin nesnesi için seçili olan özelliği bildirir
* NVDA+X, shift+N : Gezgin nesnesi için seçili olan özelliği göz atılabilir bir mesajda görüntüler

The list of the supported properties is the following:
name, role, state, value, windowClassName, windowControlID, windowHandle, location, Python class, Python class mro.

Nesne gezinme komutlarını kullanırken, NVDA olağan nesne raporlaması yerine şu anda seçilen özelliğin rapor edilmesini de seçebilirsiniz.
A toggle command, `NVDA+X, control+N`, allows to switch between this custom reporting of objects and NVDA usual reporting.

For exemple, you may select "windowClassName" property and enable custom object reporting.
Then when moving the navigator object to next or previous object, you will hear the object's windowClassName instead of usual reporting.

## Komut Dosyası Araçları

<a id="scriptOpener"></a>
### Komut dosyası açıcı

The script opener command allows to open the code of a script knowing its gesture.

To use it press `NVDA+x, C` and then the gesture of the script which you want to see the code of.
For example to see the code of the script that reports the title of the foreground window, press `NVDA+X, C` and then `NVDA+T`.

For this feature to work, you need to have configured your [favorite editor's command](#settingsOpenCommand) in the add-on's settings.
If you are not running NVDA from source, the [location of NVDA source code](#settingsNvdaSourcePath) should also have been configured.

### Genişletilmiş komut dosyası açıklama modu

The extended script description mode allows to have reported information on scripts without description in input help mode.

When the Extended script description mode is active, the input help mode (NVDA+1) is modified as follows.
If a script has no description, the script's name and class are reported.
If a script has a description, its description is reported as usual.
The gesture to activate or deactivate this feature is `NVDA+X, D`.

Executing a gesture bound to a script without description in input help mode also create an entry for this script in the gesture management dialog.
This entry is located in a dedicated category called "Scripts without description (modify at your own risk!)".
This allow to easily add, delete or change the native NVDA gestures for these script.
Be aware however that it is often intended that such script do not have any description to prevent the user to modify the associated gesture.
Indeed, the gesture may be defined to match an application shortcut key.
For example the script script_toggleItalic on NVDAObjects.window.winword.WordDocument is bound to control+I and this should not be modified since the gesture is passed to the application to actually execute the shortcut key.

### Kullanım Örneği

Control+shift+I also toggle italic in Word, even if it is not natively reported by NVDA.
To have the control+shift+I result reported by NVDA as control+I, you should perform the following steps:

* Open a Word document.
* Enable the extended script description mode with `NVDA+X, D`.
* Enter input help mode with NVDA+1.
* Press control+I to report the italic script and have it added in the gesture dialog.
* Exit input help mode with NVDA+1.
* Open the input gestures dialog.
* In the category "Scripts without description (modify at your own risk!)", select the command "toggleItalic on NVDAObjects.window.winword.WordDocument".
* Add the control+shift+I shortcut and validate.
* If you want, exit the extended script description mode with `NVDA+X, D`.

Known bug: A script added for a specific class is visible even if gesture manager is opened in another context.

## Günlük okuma ve analiz özellikleri

<a id="logPlaceMarkers"></a>
### Günlüğe işaretler yerleştir

While testing or working, you may want to mark a specific moment in the log, so that you can turn to it easily later when reading the log.
To add a marker message in the log, press `NVDA+X, K`.
A message as follows will be logged at INFO level:
`-- NDTT marker 0 --`
You can add as many markers as you want in the log.
The marker's number will be incremented each time you place a marker in the log; it will only be reset when NVDA is restarted.

### Günlük Okuyucu Modu

A log reader mode provides commands to ease log reading and analyzing.
In the log viewer window the log reader is enabled by default, thus log reading commands are available immediately.
In another text reading area such as an editor (e.g. Notepad++) or a webpage (e.g. GitHub issue), you need to press `NVDA+X, L` to enable log reader mode and use its commands.
When you are done with log reading and analyzing tasks, you can disable again `NVDA+X, L` to disable the log reader mode.

The commands available in log reader mode are described hereafter.

<a id="logReaderQuickNavigationCommands"></a>
#### Hızlı gezinme komutları

Single letter command similar to browse mode quick navigation keys allow to move to various type of log messages:

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

Pressing the single letter moves to the next occurrence of this message. Combining the letter with the shift key moves to the previous occurrence of this message.

#### Konuşma mesajının çevirisi

Sometimes, you may have to look at a log taken on a system in a foreignh language that you do not understand. E.g. the log was taken on a Chinese system / NVDA, whereas you only understand French.
If you have [Instant Translate][3] add-on installed, you may use it in conjonction with [quick log navigation commands](#logReaderQuickNavigationCommands) to have speech messages translated.

* First configure Instant Translate's languages. The source language should be the language of the system where the log has been taken (e.g. Chinese). The target language should be your language (e.g. French).
* Günlüğü aç
* Günlükte otomatik konuşma çevirisini etkinleştirmek için t tuşuna basın
* Günlükteki Hızlı gezinme komutlarını kullanın, örneğin S, I, vb. Bir konuşma mesajıyla karşılaşıldığında, bu mesaj sizin dilinizde konuşulacaktır (önceki örneğimizde Fransızca)

If you want to disable speech translation, press T again.



<a id="logReaderOpenSourceFile"></a>
#### Kaynak kod dosyasını düzenleyicide aç

In the log some line may refer to the source code:

* A line belonging to a traceback contains the path and the line in a file, e.g.:
  `  Dosya “virtualBuffers\__init__.pyc”, satır 226, _getStoryLength içinde`
* The header line of a logged message contains the function which has logged this message, e.g.:
  `BİLGİ - yapılandırma. ConfigManager._loadConfig (22:45:26.145) - Ana İş Parçacığı (16580):`
* The content of a message logged in input help mode (logged at info level):
  `Input help: gesture kb(desktop):NVDA+t, bound to script title on globalCommands.GlobalCommands`

You may want to open the file containing this code to understand the context of the traceback or the logged message.
Just press C to open this file.

For this feature to work, you need to have configured your [favorite editor's command](#settingsOpenCommand) in the add-on's settings.
If you are not running NVDA from source, the [location of NVDA source code](#settingsNvdaSourcePath) should also have been configured.

<a id="oldLogsBackup"></a>
## Eski günlük yedekleri

NVDA already provides a backup of the log of the previous session of NVDA; the file is called `nvda-old.log`.
Sometimes however you may want to access older logs, e.g. because you have had to restart NVDA again before looking at `nvda-old.log`.
This add-on allows you to configure if you want to backup old logs and how many of them; this is done in the [add-on's settings](#settingsLogsBackup).

A log manager dialog allows to view the backed up logs.
NVDA menüsü -> Araçlar -> Günlük yöneticisine gidilerek açılabilir
In this dialog, you can see the list of all the backup logs and perform various actions on the selected log:

* Aç (`` enter 'tuşuna basın)
* sil (`Delete 'tuşuna basın)
* günlük dosyasını kopyala (`kontrol+C`)

You can also select multiple logs to perform an actions on all of them.

To be able to open a log, you should first have configured the [Command to open a file in your favorite editor](#settingsOpenCommand).

## Python konsol eklentisi

<a id="pythonConsoleOpenCodeFile"></a>
### `openCodeFile` function

In the console, you can call the following function to view the source code that defines the variable `myVar`:
`openCodeFile(myVar)`

For this feature to work, you need to have configured your [favorite editor's command](#settingsOpenCommand) in the add-on's settings.
If you are not running NVDA from source, the [location of NVDA source code](#settingsNvdaSourcePath) should also have been configured.

The `openCodeFile` functions can be called on objects defined in NVDA's code or on objects defined by add-ons.
It cannot be called on objects whose source code is not available such as python builtins.

If you have not yet imported the object in the console, you can also pass its name as parameter to the `openCodeFile` function.

Below are examples of call in NVDA's code:

* View the definition of the function `speech.speech.speak`:
  `openCodeFile(speech.speech.speak)`
  or with the name passed as parameter:
  `openCodeFile("speech.speech.speak")`
* View the definition of the class `TextInfo`:
  `openCodeFile(textInfos.TextInfo)`
* View the definition of the method `copyToClipboard` of the class `TextInfo`:
  `openCodeFile(textInfos.TextInfo.copyToClipboard)`
* View the definition of the class of the focused object:
  `openCodeFile(focus)`
* Open the file `api.py` defining the module `api`:
  `openCodeFile(api)`

### Python konsolu başlangıç ​​komut dosyası

You can define a custom script which will be executed in the Python console's namespace when it is first opened, or if the add-on is reloaded (NVDA+F3) after the console has already been opened.

For example, the script allows you to execute new imports and define aliases that you will be able to use directly in the console, as shown below:

    # Konsolda istediğim çeşitli içe aktarmalar.
    globalVars'ı gv olarak içe aktar
    çekirdeği içe aktar
    Kullanıcı arayüzünü içe aktar
    # Takma adlar
    kda = Kod Dosyasını Aç

Python konsol komut dosyası şu konuma yerleştirilmelidir: `pathToNVDAConfig\ndtt\consoleStartup.py`
Örneğin: `C:\Users\kullanıcıadı\AppData\Roaming\nvda\ndtt\consoleStartup.py`

## Konuşma işlevinin yığın izlemesini günlüğe kaydet

Sometimes, you may want to see which part of the code is responsible for speaking something.
For this, you can enable the stack trace logging of the speech function pressing `NVDA+X, S`.
Each time NVDA speaks, a corresponding stack trace will be logged in the log.

Note: You may modify the script's file directly to patch another function.
See all instructions in the file for details on usage.

<a id="reverseTranslationCommand"></a>
## Ters Çeviri Komutu

Many testers use NVDA in another language than English.
But when reporting test results on GitHub, the description of the modified options or the messages reported by NVDA should be written in English.
Its quite frustrating and time consuming to have to restart NVDA in English to check the exact wording of the options or messages.

To avoid this, the add-on provides a reverse translation command (`NVDA+X, R`) allowing to reverse translate NVDA's interface such as messages, control labels in the GUI, etc.
This command uses NVDA's gettext translation to try to reverse translate the last speech.
More specifically, the first string of the last speech sequence is reverse translated.

For example, in French NVDA, if I arrow down to the Tools menu named "Outils", NVDA will say "Outils  sous-Menu  o" which stands for "Tools  subMenu  o".
If I press the reverse translation command just after that, NVDA will reverse translate "Outils" to "Tools".

Looking at the log afterwards, we can find the following lines:
```
IO - speech.speech.speak (23:38:24.450) - MainThread (2044):
Konuşma ['Outils', 'sous-Menu', CharacterModeCommand(True), 'o', CharacterModeCommand(False), CancellableSpeech (still valid)]
```
This confirms that "Outils was the first string in the speech sequence.

In case the reverse translation leads to two or more possible results, a context menu is opened listing all the possibilities.

The result of the reverse translation is also copied to the clipboard if the corresponding [option](#settingsCopyReverseTranslation) is enabled, which is the default value.

<a id="settings"></a>
## Ayarlar

Some features of the add-on may require a specific configuration.
A settings panel allows to enable them or to control how they work.
Bu ayarları görüntülemek ve değiştirmek için NVDA Menüsü -> Tercihler adresine gidin ve NVDA Geliştirici ve Test Araç Kutusu kategorisini seçin.
This settings dialog can also be accessed directly from the Logs Manager dialog.

These settings are global and can only be configured when the default profile is active.

<a id="settingsOpenCommand"></a>
### Favori düzenleyicinizde bir dosya açma komutu

Some features allow to see content in your favorite editor.
This includes the commands to view the source file [from a log](#logReaderOpenSourceFile), [from an object in the console](#pythonConsoleOpenCodeFile) or [from a typed gesture](#scriptOpener), as well as the [log manager](#oldLogsBackup)'s Open button.

To use them, you first need to configure the command that will be called to open the file in your favorite editor.
The command should be of the form:
`"C:\path\to\my\editor\editor.exe" "{path}":{line}`
You should of course modify this line according to the real name and location of your editor and the syntax used by it to open files.
`{path}` will be replaced by the full path of the file to open and `{line}` by the line number where you want the cursor to be set.
For Notepad++ for example the command to type in the console would be:
`"C:\Program Files\Notepad++\notepad++.exe" "{path}" -n{line}`

<a id="settingsNvdaSourcePath"></a>
### NVDA kaynak kodu yolu

When using a command to view the source file [from a log](#logReaderOpenSourceFile), [from an object in the console](#pythonConsoleOpenCodeFile) or [from a typed gesture](#scriptOpener), the file may belong to NVDA itself.
If you are not running NVDA from source, your NVDA only contains compiled files.
Thus you may specify here an alternate location where the corresponding source file will be found, e.g. the place where you have cloned NVDA source files, so that a source file can be opened anyway.
The path should be such as:
`C:\pathExample\GIT\nvda\source`
Of course, replace the path of NVDA source with the correct one.

Be sure however that the version of your source file (e.g. GIT commit) is the same as the one of the running instance of NVDA.

<a id="settingsLogsBackup"></a>
### Eski günlük yedekleri

The combobox Backup of old logs allows to enable or disable the [feature](#oldLogsBackup).
If it is enabled, you can also specify below in "Limit the number of backups" the maximum number of backups you want to keep.
These settings only take effect at next NVDA startup when the backup takes place.

<a id="settingsCopyReverseTranslation"></a>
### Ters çeviriyi panoya kopyala

This option allows to choose if the [reverse translation command](#reverseTranslationCommand) also copies its result to the clipboard.

## Değişiklik günlüğü

### Sürüm 7.1

* NVDA 2025.1 ile uyumluluk.

### Sürüm 7.0

* Layered commands have been introduced; the entry point is `NVDA+X`.
  The existing commands have been modified accordingly.
* A new command (`NVDA+X, R`) to reverse translate the last spoken message.
* A new command (`NVDA+X, C`) to open the source code of the script associated to the next pressed gesture.
* Added speech on demand support.
* The log manager now allows more actions, either with the dedicated buttons in the dialogs or using keyboard shortcuts in the list: `enter` to open the log, `control+C` to copy the log file and `delete` to delete a log file.
* The sorting order in the log manager has been reversed (most recent log on top).
* Fixed an issue when trying to open a Python module with openCodeFile function.

### Sürüm 6.3

* NVDA 2024.1 ile uyumluluk.

### Sürüm 6.2

* Restores console opening for NVDA < 2021.1.
* Addresses potential security issues related to [GHSA-xg6w-23rw-39r8][5] when using the add-on with older versions of NVDA. However, it is recommended to use NVDA 2023.3.3 or higher.

### Sürüm 6.1

* Opening the source file of an object located in the submodule of a package is now working.
* Hata düzeltmesi: Geliştirilmiş çıkış diyalog penceresi artık kapatıldıktan sonra yeniden açılabilir ve beklendiği gibi kullanılabilir. (Łukasz Golonka'nın katkısı)

### Sürüm 6.0

* While using object navigation commands, a specific object property can be reported instead of NVDA usual object reporting.
* In log reading mode, the "C" key to open a code file from the log now also works on an input help message.
* Bugfix: The add-on can now start successfully when the number of logs to save is set to its maximum value.
* Bugfix: Python console startup script's output does not prevent anymore to jump to the first result in the console when using result navigation commands.
* Note: From now on, localization updates will not appear anymore in the change log.

### Sürüm 5.0

* If Instant Translate add-on is installed, it is now possible to have speech messages translated on the fly when using log reading commands.
* While in log reading mode, pressing E or shift+E now jumps to CRITICAL erorr messages as well as normal ERROR messages.
* New log quick navigation commands have been added to jump to input and to speech messages.
* A new command allow to place a marker in the log; and specific quick navigation commands in log reading mode allow to jump to them.
  Credit: the initial idea for this feature comes from Debug Helper add-on by Luke Davis.
* Bubfix: The memorization of the last error do not fail anymore in some cases.
* Bugfix: The add-on can initialize again with NVDA 2019.2.1.
* Bugfix: Log saving feature will not fail anymore with non-ASCII logs.

### Sürüm 4.2

* Fixed an error with NVDA version below 2021.3.
* Fixed the stack trace log formatting.
* First localizations.

### Sürüm 4.1

* Fixed a bug occurring in some situations while logging an error.
* The add-on's settings can now be modified only when the default profile is active to avoid config issues.

### Sürüm 4.0

* Possibility to back up old logs and introduction of a logs manager.
* Added a script to report the last logged error.
* Fixed a bug preventing last log message to be read in older NVDA versions.

### Sürüm 3.2

* NVDA 2023.1 ile uyumluluk.

### Sürüm 3.1

* Fixed an error occurring when requesting unavailable information on an object.

### Sürüm 3.0

* In a log, you can now press C on a message's header line to open the function/module which has emitted it.
* In the console, `openCodeFile` function can now receive as parameter the object or a string containing its name.
* New feature: NVDA console startup file: If it exists, the file YourNVDAConfigFolder\ndtt\consoleStartup.py will be executed when NVDA console is first opened or when add-ons are reloaded.
* Various minor fixes for `openCodeFile` Python console's function and the command to open the source file corresponding to a line in the log.
* Fixed an issue when trying to report roles/states for object explorer in older version of NVDA.
* The add-on does not cause a problem anymore with the tree interceptor when using UIA in Edge.

### Sürüm 2.1

* Tüm kullanım durumlarını ele almak için çeşitli hata düzeltmeleri ve kod yeniden düzenleme/temizleme: desteklenen tüm sürümler, yüklü ve kaynaktan çalıştırma vb. (Łukasz Golonka'nın katkısı)
* Compa Modülünün Yeniden Yazılması (łukasz Golonka'dan Katkı)
* The restart dialog can now be opened only once.
* The object explorer shortcuts are now unassigned by default and need to be mapped by the user.
* With the object explorer, a double-press to call the script to report the current object's property now displays the reported information in a browseable message.

### Sürüm 2.0

* New feature: Enhanced restart dialog to specify some extra options when restarting NVDA.
* New feature: extended description mode.
* Play error sound feature harmonized between pre and post 2021.3 versions of NVDA.
* New feature: Log reader commands are now available in the log viewer and also optionally in edit fields or webpages.
* New feature: In the Python console, an `openCodeFile` function is available to view the source code of an object.
* Some features are now disabled in secure mode for security reasons.
* The add-on's compatibility range has been extended (from 2019.2 to 2021.1).
* Releases are now performed with GitHub action instead of appVeyor.

### Sürüm 1.0

* Initial release.

[1]: https://www.nvaccess.org/addonStore/legacy?file=nvdaDevTestToolbox

[2]: https://www.nvaccess.org/files/nvda/documentation/userGuide.html#CommandLineOptions

[3]: https://addons.nvda-project.org/addons/instantTranslate.en.html

[4]: https://www.nvaccess.org/files/nvda/documentation/userGuide.html#PlayErrorSound

[5]: https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
