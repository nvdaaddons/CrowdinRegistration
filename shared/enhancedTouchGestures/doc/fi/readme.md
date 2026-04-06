# Enhanced Touchscreen Gestures

* Tekijät: Joseph Lee ja Kefas Lungu

Tämä lisäosa tarjoaa NVDA:lle lisäeleitä kosketusnäytön käyttämiseen. Lisäksi se sisältää eleitä selaustilan helpompaa käyttöä varten.

Note: this add-on requires NVDA 2025.3.2 or later running on a touchscreen computer with Windows 10 or 11.

## Komennot

### Käytettävissä kaikkialla

* Two finger tripple tap: quits NVDA!
* Three finger flick right: press Tab.
* Three finger flick left: press Shift+Tab.
* Three finger flick down (object mode): read current window.
* Three finger double tap: cycles through speech symbol levels which determine what symbols are spoken.
* Three finger triple tap: toggles screen curtain.
* Four finger tap: cycles through audio ducking modes.
* Four finger double tap: toggle input help mode.
* Four finger flick left: report object with focus.
* Four finger flick right: report current navigator object.
* Four finger flick up: report title of the current window.
* Four finger flick down: report status bar text.

## Kosketusselaustila

Tämä selaustilassa käytettävissä oleva kosketustila mahdollistaa dokumentissa liikkumisen valitun elementtityypin mukaan. Voit siirtyä selaustiladokumenteissa selaustilaan napauttamalla kolmella sormella. Tässä tilassa pyyhkäisy yhdellä sormella ylös tai alas vaihtaa käytettävissä olevien elementtinavigointitilojen välillä, ja pyyhkäisy yhdellä sormella oikealle tai vasemmalle siirtää seuraavaan tai edelliseen valitun tyyppiseen elementtiin. Kun siirryt pois selaustiladokumenteista, käyttöön otetaan objektikosketustila.

Available web modes are: default (move through elements/objects regardless of type), links, buttons, form fields, headings, frames, tables, lists, graphics, landmarks, embedded objects (dialogs and web apps, for example), and text paragraphs.

## Syntetisaattorin asetukset

Voit käyttää tätä tilaa nopeaan syntetisaattoriasetusten säätämiseen, kuten puheäänen valitsemiseen ja äänenvoimakkuuden muuttamiseen. Käytä kahden sormen pyyhkäisyä vasemmalle tai oikealle siirtyäksesi asetusten välillä ja kahden sormen pyyhkäisyä ylös tai alas muuttaaksesi arvoja. Nämä eleet peilaavat näppäimistöllä käytettäviä syntetisaattorin asetusrenkaan komentoja.

## Versio 26.03

* Uudelleennimetty "verkkotila" muotoon "selaustila", koska tämä tila kattaa myös muita tilanteita, mukaan lukien Word 365:n selaustilan.

## Version 26.02

* NVDA 2025.3.2 or later is required.
* A warning will be presented when installing the add-on on computers without touchscreens or portable NVDA version is in use.
* Gestures from the add-on will not be shown in input gestures dialog when the add-on is installed on a portable NVDA version.
* Touch gesture changes, including pressing Tab (three finger flick right), pressing Shift+Tab (three finger flick left), reporting focused object (four finger flick left), and reporting navigator object (four finger flick right).
* Removed touch keyboard and dictation toggle gestures due to reliability issues with the former and dictation being replaced by Voice Access in Windows 11.
* Removed progress bar output settings toggle gesture (one finger triple tap).
* Added screen curtain toggle gesture (three finger triple tap).
* Read current window gesture (three finger flick down) will be limited to object touch mode.
* Added embedded object and text paragraph navigation to web touch mode.

## Versio 25.07

* Koodin vakautta parannettu Pyrightin (Pythonin staattisen tyypintarkistustyökalun) avulla.

## Versio 25.02

* Palautettu rajoitettu tuki Windows 8.1:lle.

## Versio 25.01

* Latauslinkkiä ei enää sisällytetä lisäosan dokumentaatioon. Voit ladata lisäosan NV Accessin lisäosakaupasta.
* Virheidentarkistustyökalu vaihdettu Flake8:sta Ruff:iin ja lisäosamoduulit muotoiltu uudelleen paremmin NVDA:n koodauskäytäntöjä vastaaviksi.
* Poistettu tuki Lisäosien päivittäjä -lisäosan automaattiselle päivitystoiminnolle.

## Versio 24.05

* Edellyttää NVDA 2024.1:tä tai uudempaa.

## Versio 23.06.1

* Äänenvaimennus siirretty neljän sormen napautukseen, koska aiempi komento oli ristiriidassa NVDA:n puheen lopetuskomennon kanssa.

## Versio 23.06

* Changed add-on maintainer to Kefas Lungu.
* Objektitilan eleet ovat nyt käytettävissä kaikkialla.
* Uusia eleitä on nyt käytettävissä.
  * Kaksoisnapautus kolmella sormella: Vaihtaa puheen symbolitasoa, joka määrittää, mitkä symbolit puhutaan.
  * 2 finger triple tap: Quit NVDA!.
  * Napautus neljällä sormella: Vaihtaa äänenvaimennuksen tilaa.
  * Triple tap: Cycles progress bar output between beeps, speech, beeps and speech, and off.
* Verkkotilassa on nyt mahdollista käyttää painikkeita, grafiikoita ja kiintopisteitä muiden jo elementtilistassa käytettävissä olevien vaihtoehtojen lisäksi.
* NVDA ei enää sano verkkotilassa "normaali" vaan "oletus" vaihdettaessa takaisin oletusnavigointiin jostakin muusta elementtilistan tilasta, esim. painikkeista.

## Versio 23.02

* Edellyttää NVDA 2022.4:ää tai uudempaa.
* Edellyttää Windows 10 21H2:ta (marraskuun 2021 päivitys/koontiversio 19044) tai uudempaa.

## Versio 23.01

* Edellyttää NVDA 2022.3:a tai uudempaa.
* Edellyttää Windows 10:tä tai uudempaa, koska Microsoft ei enää tue Windows 8.1:tä tammikuusta 2023 alkaen.
* Kosketusnäppäimistön ja sanelun tilanvaihtokomennot on mahdollista uudelleenmäärittää Näppäinkomennot-valintaikkunan Laajennetut kosketuseleet -kategoriasta.
* Kosketusnäppäimistön näppäinten vain luku -tilan ohitus on poistettu, koska se on ratkaistu Windows 10:ssä.

## Versio 22.03

* Edellyttää NVDA 2021.3:a tai uudempaa.
* A warning message will be displayed when attempting to install the add-on on Windows 7, 8, and 8.1.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.

## Version 21.08

* Initial support for Windows 11.

## Version 21.01

* NVDA 2020.3 or later is required.
* On Windows 10 Version 1709 and later, doing a four finger flick left will toggle dictation (Windows+H).
* Remove dedicated touch interaction support toggle command from the add-on.
* As touch interaction support can be toggled from NVDA's touch interaction settings panel, a dedicated Enhanced Touch Gestures settings panel has been removed.

## Version 20.09

* Removed ability to let NVDA turn off touch interaction for up to ten seconds (touch command passthrough).
* Removed coordinate announcement beep feature.

## Version 20.07

* Added a keyboard command to toggle touch interaction or enable/disable touch passthrough (Control+Alt+NVDA+T).
* As NVDA 2020.1 and later includes a touch command to perform right mouse click (one finger tap and hold), the command has been removed from this add-on. AS a result, NVDA 2020.1 or later is required.
* The ability to let NVDA turn off touch interaction for up to ten seconds (touch command passthrough) is deprecated. In the future this feature will toggle touch interaction instead.
* In NVDA development snapshots, due to touch interaction feature changes, touch command passthrough feature and Enhanced Touch Gestures settings panel will be disabled. The command used to enable touch command passthrough will toggle touch interaction instead.
* Coordinate announcement beep feature is deprecated and will be removed in a future add-on release.
* Coordinate announcement beep will not be heard while using touch keyboard.
* NVDA will no longer appear to do nothing or play error tones while exploring modern input facility such as emoji panel via touch.
* NVDA will present an error message if touch keyboard cannot be activated (four finger flick right).

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Right mouse click gesture (one finger tap and hold) is now part of NVDA 2020.1.

## Version 20.01

* NVDA 2019.3 or later is required.
* Touch support toggle command (including touch passthrough) will no longer function if touch support is turned off completely.

## Version 19.11

* Added input help messages for additional touch commands.

## Version 19.09

* Touch support can now be disabled from everywhere, not just from profiles other than normal profile.

## Version 19.07

* Internal changes to support future NVDA releases.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.08

* Compatible with NVDA 2018.3 and future versions.

## Version 18.06

* Add-on settings is now found in new multi-category NVDA Settings screen under "Enhanced Touch Gestures" category. As a result, NVDA 2018.2 is required.
* Fixed compatibility issues with wxPython 4.

## Version 18.04

* Resolves an issue where touch interaction category in NVDA Settings panel may cause error sounds to be heard due to changes made from this add-on.

## Version 18.03

* NVDA 2018.1 is required.
* Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no longer included in this add-on.

## Version 17.12

* Requires NVDA 2017.4. Specifically, this add-on can now handle configuration profile switches.
* As NVDA 2017.4 includes screen orientation announcement, this feature is no longer part of this add-on.
* Kosketusvuorovaikutuksen valintaikkunaan lisätty piilotettu valintaruutu, jolla kosketustuen voi poistaa kokonaan käytöstä (käytettävissä, jos jokin muu kuin normaali asetusprofiili on käytössä).
* Mikäli käytetään NVDA 2018.1:tä tai sitä uudempaa, Kosketuksen vuorovaikutus -vaihtoehto näkyy kahdesti Asetukset-valikossa. Toisena oleva eli alempi vaihtoehto avaa tämän lisäosan valintaikkunan.
* Kosketuskirjoitustilaa ei enää näytetä lisäosan Kosketuksen vuorovaikutus -valintaikkunassa, mikäli käytetään NVDA 2018.1:tä tai uudempaa.

## Versio 17.10

* Windows 8:n alkuperäisversiota ei enää tueta Microsoftin tukikäytännön vuoksi.
* Ruudun suuntaa ei enää ilmoiteta kahdesti NVDA 2017.4:n kehitysversioita käytettäessä.

## Versio 17.07.1

* Kosketuksen vuorovaikutus -valintaikkunaan lisätty asetus kosketuseleiden läpiviennin manuaaliseen käyttöön ottoon ja käytöstä poistamiseen ilman ajastinta.
* Kosketuksen vuorovaikutus otetaan käyttöön manuaalisen läpivientitilan ollessa pois käytöstä, mikäli läpivienti otetaan käyttöön ennen sen ajan umpeutumista.

## Versio 17.07

* Lisätty Asetukset-valikkoon uusi Kosketuksen vuorovaikutus -vaihtoehto, josta avautuu valintaikkuna, jossa on mahdollista määrittää, miten NVDA toimii kosketusnäyttöä käytettäessä.
* Kun tämä versio on asennettuna, kosketusnäppäimistön näppäimiä on kaksoisnapautettava niiden painamiseksi. Voit vaihtaa takaisin vanhaan kirjoitustapaan ottamalla käyttöön kosketuskirjoituksen Kosketuksen vuorovaikutus -valintaikkunasta.
* Lisätty määrittämätön komento, jonka avulla NVDA ohittaa kosketuseleet enintään kymmenen sekunnin ajan.
* Lisätty Kosketuksen vuorovaikutus -valintaikkunaan asetus, jolla NVDA keskeyttää kosketusvuorovaikutuksen  3-10 sekunnin ajaksi, mikä mahdollistaa kosketuseleiden suoran suorittamisen (ikään kuin NVDA ei olisi käynnissä; oletus on 5 sekuntia).
* Lisätty virheenkorjauslokin ilmoitukset hiiren oikean näppäimen napsautuksille (napauta ja pidä) NVDA:n lokiin tallennettaviksi (edellyttää NVDA 2017.1:tä tai uudempaa).
* Ruudun koordinaattien ilmaisemiseen tehtyjen muutosten vuoksi edellytetään NVDA 2017.1:tä tai uudempaa.

##Versio 17.03

* Korjattu ongelma, jonka vuoksi koordinaatin ilmoitusmerkkiääntä ei toistettu tai sen asemesta kuului virheääni NVDA 2017.1:tä tai uudempaa käytettäessä.

##Versio 16.12

* Verkkotila toimii Microsoft Edgessä, Microsoft Wordissa ja muualla, missä käytetään selaustilaa.
* Luettelot ja kiintopisteet lisätty verkkotilan elementteihin.

## Versio 16.06

* Ensimmäinen vakaa versio.

[1]: https://addons.nvda-project.org/files/get.php?file=ets
