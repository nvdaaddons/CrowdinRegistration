# Windowsin suurennuslasi

* Tekijä: Cyrille Bougot
* yhteensopivuus: NVDA 2019.2.1 ja uudemmat

Tämä lisäosa parantaa Windowsin suurennuslasin käytettävyyttä NVDA:lla.


## Ominaisuudet

* Mahdollistaa joidenkin alkuperäisten suurennuslasin ja värisuodatuksen näppäinkomentojen tulosten ilmoittamisen.
* Vähentää tapauksia, joissa taulukkonavigointikomennot ovat ristiriidassa suurennuslasikomentojen kanssa.
* Lisää pikanäppäimiä useiden alkuperäisten suurennuslasin asetusten muuttamiseen.
* Mahdollistaa suurennuslasin asetusten tallentamisen ja palauttamisen.
* Lisää muutaman ominaisuuden, joita Windowsin suurennuslasi ei tarjoa (siirrä hiiri näkymään, suurennuslasi ei päällimmäisenä)

## Asetukset

Windowsin suurennuslasi -lisäosan asetuspaneelissa voidaan määrittää, miten NVDA reagoi suurennuslasin alkuperäisiin komentoihin.
Saatat haluta enemmän tai vähemmän komentoja ilmoitettavan riippuen siitä, minkä verran näet.
Paneelissa on myös asetus, jolla voi muokata suurennuslasin ohjausikkunan toimintaa.

Tämä paneeli voidaan avata Valitsemalla NVDA-valikosta Mukautukset -> Asetukset ja sitten avautuvasta asetusikkunasta Windowsin suurennuslasi -kategoria.
Tämä asetuspaneeli voidaan myös avata suoraan painamalla näppäinkomentoa NVDA+Win+O ja sitten O.

Paneelissa on seuraavat asetukset:

* Ilmoita näkymän siirtäminen: määrittää, mitä ilmoitetaan, kun näkymää siirretään Ctrl+Alt+nuolinäppäimillä. Käytettävissä olevat kolme vaihtoehtoa ovat:
  
    * Ei käytössä: Mitään ei ilmoiteta.
    * Puheella: Puhuttu viesti ilmaisee zoomatun näkymän sijainnin suunnassa, johon näkymää siirretään.
    * Merkkiäänillä: Toistettava merkkiääni ja sen korkeus ilmaisevat zoomatun näkymän sijainnin suunnassa, johon näkymää siirretään.
  
  Tämä asetus ei vaikuta kiinnitetyn näkymän tilaan.

* Ilmoita näytön reunat: Määrittää, mitä ilmoitetaan, kun näytön reuna saavutetaan siirrettäessä näkymää Ctrl+Alt+nuolinäppäimillä.
  Käytettävissä olevat kolme vaihtoehtoa ovat: Ei käytössä, Puheella ja Merkkiäänillä.
  Tämä asetus ei vaikuta kiinnitetyn näkymän tilaan.
* Näkymän sijainnin ilmoittavien merkkiäänien voimakkuus: Mahdollistaa merkkiäänien voimakkuuden määrittämisen, mikäli olet valinnut näkymän siirtämisen tai näytön reunojen ilmoittamisen merkkiäänillä.
* Ilmoita käyttöön ottaminen tai käytöstä poistaminen:
  Jos tämä on valittuna, suurennuslasin tila ilmoitetaan käytettäessä Win++- tai Win+Esc-komentoja sen käyttöön ottamiseksi tai käytöstä poistamiseksi.
* Ilmoita zoomauksen taso:
  Jos tämä on valittuna, suurennuslasin zoomauksen taso puhutaan käyttäessäsi zoomauskomentoja Win++ tai Win+-.
* Puhu värin inversio:
  Jos tämä on valittuna, värin inversion tila ilmoitetaan käytettäessä tilanvaihtokomentoa Ctrl+Alt+I.
* Ilmoita näkymän muutos:
  Jos tämä on valittuna, näkymän tyyppi puhutaan käytettäessä sitä vaihtavaa komentoa (Ctrl+Alt+M, Ctrl+Alt+F, Ctrl+Alt+D ja Ctrl+Alt+L).
* Ilmoita linssi- tai kiinnitetyn ikkunan koon muuttaminen:
  Jos tämä on valittuna, NVDA antaa ilmoituksen käytettäessä koonmuuttamiskomentoja (Alt+Vaihto+nuolinäppäimet).
  Kiinnitetyn ikkunan tilassa ilmoitetaan korkeus tai leveys.
  Linssitilassa uutta mittaa ei toistaiseksi voida ilmoittaa.
  Nämä koonmuutoskomennot eivät näytä olevan käytettävissä kaikissa Windows-versioissa; mikäli Windows-versiosi ei tue niitä, älä valitse tätä asetusta.
* Välitä Ctrl+Alt+nuolet asiakirjoissa ja luettelonäkymissä Windowsin suurennuslasille:
  Mahdollisia vaihtoehtoja on kolme:
  
    * Ei koskaan: Komentoa ei välitetä Windowsin suurennuslasille, ja tavallinen NVDA:n taulukkonavigointi toimii.
      Kun Ctrl+Alt+Nuolinäppäin-komentoa käytetään asiakirjoissa olevien taulukoiden ulkopuolella, NVDA ilmoittaa virheen "Ei taulukossa".
      NVDA toimii näin ilman tätä lisäosaa.
      Voit edelleen käyttää NVDA+Win+O:ta ja sitten nuolinäppäimiä suurennetun näkymän siirtämiseen.
    * Vain, kun ei taulukossa: Taulukko- tai luettelonäkymissä Ctrl+Alt+Nuoli-komentoja voidaan käyttää tavalliseen taulukkonavigointiin.
      Ctrl+Alt+nuoli-komennot suorittavat tavallisia suurennuslasin näkymänsiirtokomentoja, kun niitä käytetään asiakirjoissa olevien taulukoiden ulkopuolella.
      Mikäli haluat silti siirtää Windowsin suurennuslasin näkymää taulukko- tai luettelonäkymässä, sinun on painettava NVDA+F2 ennen kuin käytät Ctrl+Alt+Nuoli-komentoja, tai käytä vaihtoehtoisesti NVDA+Win+O:ta ja sitten nuolinäppäimiä.
      Tämä vaihtoehto on paras kompromissi, jos haluat käyttää Ctrl+Alt+Nuoli-näppäinyhdistelmää sekä suurennuslasissa että taulukossa liikkumiseen.
    * Aina: Ctrl+Alt+nuoli-komennot siirtävät suurennuslasin näkymää kaikissa tapauksissa.
      Tämä vaihtoehto voi olla hyödyllinen, mikäli et käytä Ctrl+Alt+nuoli-komentoja taulukossa liikkumiseen, esim. koska olet vaihtanut NVDA:n taulukkonavigointikomentoja tai koska käytät yksinomaan [Helppo taulukossa liikkuminen][5] -lisäosaa taulukkonavigointiin.

* Pidä Windowsin suurennuslasin komentoikkuna aina päällimmäisenä:
  Jos tämä ei ole valittuna, suurennuslasin säädinikkunaa ei pidetä aina muiden ikkunoiden päällä.
* Ilmoita värisuodatin:
  Jos tämä on valittuna, käytössä oleva värisuodatin ilmoitetaan käytettäessä tilanvaihtokomentoa `Win+Ctrl+C`.

## Lisäosan lisäämät komennot

Tämä lisäosa tarjoaa alkuperäisten suurennuslasikomentojen lisäksi seuraavia lisäkomentoja:

* Komentoja, joiden avulla voi hallita suurennuslasin asetuksia avaamatta sen asetussivua.
* Tämän lisäosan lisäkomentoja.

Kaikki nämä lisäkomennot ovat käytettävissä suurennuslasin komentokerroksen, NVDA+Win+O, kautta:

* NVDA+Win+O ja sitten C: Ottaa käyttöön tai poistaa käytöstä kohdistimen seurannan.
* NVDA+Win+O ja sitten F: Ottaa käyttöön tai poistaa käytöstä kohdistuksen seurannan.
* NVDA+Win+O ja sitten M: Ottaa käyttöön tai poistaa käytöstä hiiren seurannan.
* NVDA+Win+O ja sitten T: Ottaa käyttöön tai poistaa käytöstä seurannan järjestelmänlaajuisesti.
  Kun seuranta otetaan uudelleen käyttöön, käytössä on ennen sen käytöstä poistamista aktiivisena ollut asetus.
* NVDA+Win+O ja sitten S: Ottaa käyttöön tai poistaa käytöstä pehmennyksen.
* NVDA+Win+O ja sitten R: Vaihtaa hiiren osoittimen seurannan tilaa (näytön reunojen sisäpuolella tai näytöllä keskitettynä). Tämä ominaisuus on käytettävissä vain Windows 10:n koontiversiossa 17643 tai sitä uudemmassa.
* NVDA+Win+O ja sitten X: Vaihtaa tekstikohdistimen seurannan tilaa (näytön reunojen sisäpuolella tai näytöllä keskitettynä). Tämä ominaisuus on käytettävissä vain Windows 10:n koontiversiossa 18894 tai sitä uudemmassa.
* NVDA+Win+O ja sitten Vaihto+P: Tallentaa nykyiset suurennuslasin asetukset NVDA:n asetuksiin.
* NVDA+Win+O ja sitten P: Palauttaa suurennuslasin nykyiset asetukset NVDA:n asetuksista.
  Mikäli asetuksia ei ole aiemmin tallennettu, Windowsin suurennuslasin oletusasetukset palautetaan.
* NVDA+Win+O ja sitten nuolinäppäimet: Siirtää suurennettua näkymää.
* NVDA+Win+O ja sitten V: Siirtää hiirikohdistimen suurennetun näkymän keskelle (komento ei ole käytettävissä kiinnitetyn näkymän tilassa).
* NVDA+Win+O ja sitten W: Ottaa käyttöön tai poistaa käytöstä tilan, joka pitää Windowsin suurennuslasin ikkunan muiden ikkunoiden päällä.
  Tämä ominaisuus on käytettävissä vain NVDA:n asennetuissa versioissa.
* NVDA+Win+O ja sitten O: Avaa Windowsin suurennuslasi -lisäosan asetukset.
* NVDA+Win+O ja sitten H: Näyttää suurennuslasin komentokerroskomentojen ohjeen.

Komennoilla ei ole oletusarvoisia näppäinkomentoja, mutta voit halutessasi määrittää ne normaalisti Näppäinkomennot-valintaikkunassa.
Samalla tavalla voit myös muuttaa tai poistaa suurennuslasin komentokerroksen aktivointikomennon (NVDA+Win+O).
Komentokerroksen alikomentojen muuttaminen ei kuitenkaan ole mahdollista.


## Alkuperäiset suurennuslasikomennot

Asetuksista riippuen seuraavien alkuperäisten suurennuslasi- tai muiden helppokäyttötoimintojen komentojen tulokset ilmoitetaan tätä lisäosaa käytettäessä:

* Käynnistä suurennuslasi: Win++ (numeroriviltä tai laskinnäppäimistöltä)
* Lopeta suurennuslasi: Win+Esc
* Lähennä: Win++ (numeroriviltä tai laskinnäppäimistöltä)
* Loitonna: Win+- (numeroriviltä tai laskinnäppäimistöltä)
* Ota käyttöön tai poista käytöstä käänteiset värit: Ctrl+Alt+I
* Valitse kiinnitetty näkymä: Ctrl+Alt+D
* Valitse koko ruudun näkymä: Ctrl+Alt+F
* Valitse linssinäkymä: Ctrl+Alt+L
* Vaihda kolmen näkymätyypin välillä: Ctrl+Alt+M
* Muuta linssin kokoa näppäimistöllä: Vaihto+Alt+Nuoli vasemmalle/oikealle/ylös/alas.
  Huom: Tämä pikanäppäin näyttää olevan poistettu viimeisimmistä Windows-versioista, kuten Windows 10 2004, vaikkei sitä ole dokumentoitu missään.
* Siirrä suurennettua näkymää: Ctrl+Alt+nuolinäppäimet
* Ota käyttöön tai poista käytöstä värisuodattimet: `Win+Ctrl+C` (jos olet ottanut tämän pikanäppäimen käyttöön Windowsin asetuksista kohdasta [Helppokäyttötoiminnot -> Värisuodattimet][9])

Tässä on lisäksi luettelo muista Suurennuslasin alkuperäisistä komennoista:

* Ctrl+Alt+hiiren vieritysrulla: Lähennä tai loitonna hiiren vieritysrullaa käyttäen.
* Ctrl+Win+M: Avaa suurennuslasin asetusikkunan.
* Ctrl+Alt+R: Muuttaa linssin kokoa hiiren avulla.
* Ctrl+Alt+Väli: Näyttää nopeasti koko työpöydän koko näytön näkymää käytettäessä.

Alkuperäisiä suurennuslasikomentoja ei voi muuttaa.


## Huomautukset

* Intel-näytönohjaimella varustetuissa tietokoneissa Ctrl+Alt+Nuoli vasemmalle/oikealle/ylös/alas ovat myös näytön suunnan muuttamisen pikanäppäimiä.
  Nämä pikanäppäimet ovat oletusarvoisesti käytössä ja ristiriidassa Windowsin suurennuslasin näkymänsiirtopikanäppäinten kanssa.
  Ne on poistettava käytöstä, jotta voit käyttää niitä suurennuslasissa.
  Ne voidaan poistaa käytöstä Intelin ohjauspaneelista tai ilmaisinalueen Intel-valikosta.
* Windows-versiostasi riippuen Alt+Vaihto+nuoli-komennot ovat Windowsin suurennuslasin pikanäppäimiä suurennetun näkymän koon muuttamiseen linssi- tai kiinnitetyssä näkymässä.
  Kun suurennuslasi on käytössä (jopa koko näytön tilassa), se kaappaa nämä pikanäppäimet, eikä niitä voi välittää aktiiviselle sovellukselle, vaikka painaisit ensin NVDA+F2.
  Mikäli haluat käyttää näitä pikanäppäimiä nykyisessä sovelluksessa, sinun on suljettava suurennuslasi (Win+Esc) ja avattava se uudelleen sen jälkeen (Win++).
  Esimerkiksi Microsoft Wordissa otsikkotason pienentämiseksi:
  
    * Sulje suurennuslasi painamalla Win+Esc.
    * Pienennä nykyistä otsikkotasoa painamalla Alt+Vaihto+nuoli oikealle.
    * Avaa suurennuslasi uudelleen painamalla Win++.

* Saat lisätietoja Windowsin suurennuslasin ominaisuuksista ja pikanäppäimistä seuraavilta sivuilta:

    * [Näytön sisällön näkyvyyden parantaminen suurennuslasin avulla](https://support.microsoft.com/fi-fi/windows/n%C3%A4yt%C3%B6n-sis%C3%A4ll%C3%B6n-n%C3%A4kyvyyden-parantaminen-suurennuslasin-avulla-414948ba-8b1c-d3bd-8615-0e5e32204198)
    * [Windowsin helppokäyttötoimintojen pikanäppäimet][4]

* Tätä lisäosaa ei ole testattu moninäyttöympäristössä, ja on mahdollista, että jokin ominaisuus ei toimi sitä käytettäessä.
  Ota minuun yhteyttä, mikäli käytät moninäyttöympäristöä ja haluat, että sitä tuetaan.
* Yleisemmin ottaen älä epäröi ottaa minuun yhteyttä tämän lisäosan [GitHub-sivulla][3] tai suoraan sähköpostitse.


## Muutosloki

### Versio 4.2

* Suurennuslasin tai värisuodatuksen komennot toimivat nyt ensimmäisellä käyttökerralla, kun tämä lisäosa on käynnissä.

### Versio 4.0

* Pikanäppäimellä `Ctrl+Win+C` käyttöön otettavan värisuodattimen tila voidaan nyt ilmoittaa. Tämä pikanäppäin on ensin otettava käyttöön Windowsin helppokäyttötoimintojen asetuksista.
* Yhteensopivuus NVDA 2025.1:n kanssa.

### Versio 3.7

* Yhteensopivuus NVDA 2024.1:n kanssa.

### Versio 3.6

* Korjattu virheellinen versioyhteensopivuus.

### Versio 3.5

* Valmisteltu yhteensopivuutta NVDA 2024.1:n kanssa.
* Ratkaisee mahdolliset [GHSA-xg6w-23rw-39r8][8]:aan liittyvät tietoturvaongelmat käytettäessä lisäosaa vanhemmilla NVDA-versioilla. NVDA 2023.3.3:n tai uudemman käyttö on kuitenkin suositeltavaa.
* Huom: Tästä lähtien käännöspäivitykset eivät enää näy muutoslokissa.

### Versio 3.4

* "Siirrä hiiri näkymään" -komento toimii taas
* Lokalisointeja päivitetty.

### Versio 3.3

* Yhteensopivuudeksi muutettu NVDA 2019.2.1 ja sitä uudemmat.
  Uusimmat NVDA 2018.3:n kanssa yhteensopivat versiot ovat [3.2][7] (osittain yhteensopiva) ja [1.1][6] (täysin yhteensopiva).
* Korjattu asetuspaneelin bugi NVDA 2019.2.1:ssä.

### Versio 3.2

* Dev-kanava poistettu.
* Lokalisointeja päivitetty.

### Versio 3.1

* Korjattu ongelma, joka esti suurennuslasin komentoikkunan palauttamisen päällimmäiseksi.
* Korjattu ongelma, joka esti lisäosan suorittamisen NVDA 2019.2.1:ssä.
* Lokalisointeja päivitetty.

### Versio 3.0

* Uusi zoomauksen taso ilmoitetaan nyt painettaessa suurennuslasin ikkunassa olevia Zoomauspainikkeita näppäimistöltä.
* Suurennuslasin säädinikkunan päällimmäisenä olemista määrittävä asetus tallennetaan nyt asetuksiin.
  Tämä tarkoittaa, että asetuksen tila muistetaan NVDA:ta uudelleenkäynnistettäessä, ja asetus voidaan ottaa käyttöön tai poistaa käytöstä aktiivisesta profiilista riippuen.
* Korjattu bugi, joka aiheutti odottamattoman näyttöverhon käytöstä poistamisen Siirry näkymään- tai Siirrä näkymää -komentoja käytettäessä.
* Aina päällimmäisenä -asetusta noudatetaan nyt myös suurennuksen tilaa vaihdettaessa.
* Lisätty mahdollisuus Windowsin suurennuslasin asetusten tallentamiseen ja palauttamiseen.
* Yhteensopivuus NVDA 2023.1:n kanssa.
* Selvennetty käytössä olevaa asetusta, kun seuranta otetaan uudelleen käyttöön.
* Lokalisointeja päivitetty.

### Versio 2.0

* Näkymää voidaan siirtää nuolinäppäimillä Windows-suurennuslasin komentokerroksessa oltaessa.
* Mahdollisuus pitää suurennuslasin komentoikkuna aina päällimmäisenä.
* Lisätty "Ilmoita näytön reunat" -ominaisuus.
* Merkkiäänien voimakkuusasetus näkymänsiirtämiskomentoja käytettäessä.
* Näkymän siirtämis- ja Siirrä hiiri näkymään -komentojen ilmoittamista tuetaan nyt linssitilassa.
* Yhteensopivuus NVDA 2022.1:n kanssa.
* Korjattu bugi, jonka vuoksi joskus ilmoitettiin virheellisesti, ettei suurennuslasi toiminut skriptiä kutsuttaessa.
* Julkaisu suoritetaan nyt appVeyorin sijasta GitHub-toiminnolla.
* Lokalisointeja päivitetty.

### Versio 1.1

* Lokalisointeja lisätty.

### Versio 1.0

* Ensimmäinen versio.

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

[6]: https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]: https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]: https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994

[9]: https://support.microsoft.com/en-us/windows/make-windows-easier-to-see-c97c2b0d-cadb-93f0-5fd1-59ccfe19345d
