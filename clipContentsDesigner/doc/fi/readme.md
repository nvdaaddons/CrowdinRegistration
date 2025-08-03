# Clip Contents Designer #
*   Tekijät: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Näppäinkomennot ##
*   NVDA+Windows+C: Lisää valittu/tarkastelukohdistimella merkitty teksti tai
    MathML-objekteja kuvaavat Unicode-pistekirjoitusmerkit leikepöydälle.
*   NVDA+Windows+X: Tyhjennä leikepöydän sisältö.
*    Ei määritetty: Kopioi leikepöydälle tai leikkaa siltä ja pyytää
     vaihtoehtoisesti vahvistuksen.
*    Ei määritetty: Näyttää leikepöydällä olevan tekstin HTML-muodossa
     selaustilassa tai ilmoittaa, mikäli leikepöytä on tyhjä tai jos sillä on
     sisältöä, jota ei voida näyttää, esim. Resurssienhallinnasta kopioituja
     tiedostoja tai kansioita.
*    Ei määritetty: Näyttää leikepöydällä olevan tekstin pelkkänä tekstinä
     selaustilassa tai ilmoittaa, mikäli leikepöytä on tyhjä tai jos sillä on
     sisältöä, jota ei voida näyttää, esim. Resurssienhallinnasta kopioituja
     tiedostoja tai kansioita.

## Leikepöydän sisällön käsittelijän asetukset ##

Tämä paneeli löytyy kohdasta NVDA-valikko -> Asetukset -> Asetukset.

Se sisältää seuraavat säätimet:

* Kirjoita merkkijono, jota käytetään erottimena leikepöydälle lisättyjen
  tekstiosuuksien välissä: Mahdollistaa erottimen asettamisen, jota voidaan
  käyttää tekstiosioiden etsimiseen.
* Lisää teksti leikepöydällä olevan tekstin eteen: Voit myös valita, liitetäänkö
  lisätty teksti leikepöydällä jo olevan sisällön jälkeen vai eteen.
* Valitse vahvistusta edellyttävät toiminnot: Voit valita kullekin käytettävissä
  olevalle toiminnolle, suoritetaanko se heti vai vahvistuksen jälkeen.
  Käytettävissä ovat seuraavat toiminnot: lisää tekstiä, tyhjennä leikepöytä,
  kopioinnin emulointi sekä leikkaamisen emulointi.
* Pyydä vahvistus ennen valittujen toimintojen suorittamista: Voit valita,
  pyydetäänkö vahvistus aina, vain, jos leikepöydällä on tekstiä tai mikäli
  leikepöytä ei ole tyhjä (esim. jos olet kopioinut tiedoston tekstin asemesta).
* Format to show the clipboard text as HTML in browse mode: If you're learning
  HTML markup language, you may choose Preformatted text in HTML or HTML as
  shown in a web browser, to have an idea of how your HTML code will be rendered
  by NVDA in a browser. The difference between preformatted and conventional
  HTML is that the first option will preserve consecutive spaces and line
  breaks, and the second one will compact them. For example, write some HTML
  tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and
  use clipContentsDesigner add-on to show the text in a browseable message.
* Merkkien enimmäismäärä selaustilassa leikepöydän tekstiä näytettäessä: Huomaa,
  että tämän rajan nostaminen saattaa aiheuttaa ongelmia, mikäli leikepöydällä
  on paljon tekstiä. Oletusraja on 100 000 merkkiä.
* Palauta oletukset.

Huomautuksia:

*   Vahvistusta ei pyydetä NVDA:n ilmoitusruudun ollessa avoimena, vaan
    toiminnot suoritetaan heti.
* Kun kopioinnin ja leikkaamisen emulointi on otettu käyttöön, tämä lisäosa
  ottaa hallintaansa Ctrl+C- ja Ctrl+X-komennot. Tämä mahdollistaa valinnaisen
  vahvistuksen pyytämisen ennen näiden komentojen suorittamista.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape key.

## Muutokset versiossa 40.0.0
* Lisätty tuki hepreankieliselle näppäimistölle.

## Muutokset versiossa 22.0.0
* Lisäosan asetuspaneeliin lisätty painike oletusarvojen palauttamista varten.
* Lisäosaa ei voi käyttää suojatussa tilassa.

## Muutokset versiossa 17.0
* Yhteensopiva NVDA 2023.1:n kanssa.

## Muutokset versiossa 16.0
* Edellyttää NVDA 2022.4:ää tai uudempaa.

## Muutokset versiossa 15.0
* Tekstiä leikepöydälle lisäävä komento näytetään taas
  Näppäinkomennot-valintaikkunassa.
* Korjattu kopioinnin ja leikkaamisen näppäinkomennot persiankielisellä
  näppäimistöllä. Kiitokset Mohammadhosein Ghezelsofla'lle.

## Muutokset versiossa 14.0
* Yhteensopiva NVDA 2021.1:n kanssa.

## Changes for 13.0
* Korjattu ongelma asetuspaneelin visuaalisessa ulkoasussa; kiitos Cyrille
  Bougotille.
* Dokumentaatiota paranneltu.
* Lisätty Leikepöydän sisällön käsittelijä -kategoria, josta voidaan määrittää
  näppäinkomennot kaikille tämän lisäosan komennoille.
* Korjattu bugeja käytettäessä kopioinnin emulointia selaimissa selaustilan
  ollessa käytössä.
* Voit määrittää eri näppäinkomennot näyttämään leikepöydän tekstisisällön joko
  raakatekstinä tai muotoiltuna HTML:nä.

## Muutokset versiossa 12.0
* Korjattu bugeja käytettäessä kopioinnin emulointia sellaisissa sovelluksissa
  kuin LibreOffice Writer.

## Muutokset versiossa 11.0
* Nyt on mahdollista lisätä tarkastelukohdistimella merkittyä tekstiä tavallisia
  NVDA-komentoja(NVDA+F9 ja NVDA+F10) käyttäen. Komentoa NVDA+Win+F9 ei enää
  käytetä paremman uuteen NVDA+Vaihto+F9-komentoon integroinnin takia.
* Edellyttää NVDA 2019.3:a tai uudempaa.

## Muutokset versiossa 10.0
* Korjattu ohjelmavirhe leikepöydän sisältämän tekstin näyttämiseen
  käytettävässä valintaikkunassa, kun sen nimi sisälsi ei-latinalaisia merkkejä.
* Korjattu ohjelmavirhe leikkaamisen ja kopioinnin emulointitoiminnoissa
  arabialaista näppäimistöasettelua käytettäessä. Tämän korjasi Abdel, joka on
  lisätty lisäosan tekijäksi.

## Muutokset versiossa 9.0

* Lisätty mahdollisuus leikepöydän tekstin näyttämiseen selaustilassa.
* Lisätty asetus, jolla voidaan valita, kysytäänkö vahvistus, jos leikepöytä ei
  ole tyhjä esim. tiedostoja tai kansioita kopioitaessa.
* Edellyttää NVDA 2018.4:ää tai uudempaa.

## Muutokset versiossa 8.0 ##

* Lisäosan asetukset näkyvät omassa kategoriassaan NVDA:n
  Asetukset-valintaikkunassa.
* Edellyttää NVDA 2018.2:ta tai uudempaa.

## Muutokset versiossa 7.0

* Jos valitset Ei Määritä kopioinnin ja leikkaamisen emuloinnin
  märitysvalintaikkunassa, joka tulee näkyviin lisäosaa asennettaessa, näiden
  ominaisuuksien komennot poistetaan käytöstä, mikä palauttaa normaalin Ctrl+C-
  ja Ctrl+X-toiminnallisuuden.

## Muutokset versiossa 6.0

*    Lisätty vaihtoehdot, joilla voidaan valita, pyydetäänkö käytettävissä
     olevien toimintojen suorittamiseen vahvistus.
*   Lisätty Vahvista kopioinnin emulointi- ja Vahvista leikkaamisen emulointi
    -asetukset, joille voidaan määrittää näppäinkomennot
    Näppäinkomennot-valintaikkunasta.
*    Lisätty valintaikkuna Vahvista kopioinnin emulointi- ja Vahvista
     leikkaamisen emulointi -toiminnallisuuksien määrittämiseen lisäosan
     asennuksen aikana. Kun nämä asetukset ovat käytössä, kopioinnin (Ctrl+C) ja
     leikkaamisen (Ctrl+X) suorittamiselle ja leikepöydän sisällön korvaamiselle
     pyydetään vahvistus.
*   Korjattu tekstinlisäämiskomennon (Windows+NVDA+C) ohje.

## Muutokset versiossa 5.0 ##

*   Valintaikkunan visuaalista esitystä on parannettu noudattamaan NVDA:n
    ikkunoiden ulkoasua.
*   Edellyttää NVDA:n 2016.4-versiota tai uudempaa.

## Muutokset versiossa 4.0 ##
*   NVDA hallitsee nyt lisäosan asetuksia, jotta profiilien käyttäminen eri
    erottimien tallentamiseen olisi mahdollista, eikä asetusten kopiointia
    tarvita niiden tuomiseksi asennettaessa lisäosaa uudelleen.
*   Lisäosan asetusvalintaikkunan Lisää teksti leikepöydän nykyisen sisällön
    alkuun -valintaruutua käyttäen on nyt mahdollista valita, liitetäänkö
    lisätty teksti leikepöydällä jo olevan tekstin loppuun vai alkuun.

## Muutokset versiossa 3.0 ##
*   MathML-objekteja kuvaavat pistekirjoitusmerkit voidaan lisätä leikepöydälle,
    mikäli MathPlayer on asennettu.
*   Mikäli erotinta ei ole määritetty, tekstiosuuksien väliin lisätään yksi
    tyhjä rivi.
*   Leikepöydän sisällön käsittelijän asetusvalintaikkunan avaamista varten
    voidaan määrittää pikanäppäin.
*   Asetusvalintaikkunaan lisätty valintaruutu, jolla voidaan määrittää,
    kopioidaanko erotin käyttäjän NVDA-asetusten kansioon, josta se voidaan
    tuoda asennettaessa lisäosaa uudelleen.

## Muutokset versiossa 2.0 ##
*   Hindinkielisiä merkkejä voidaan käyttää tekstiosuuksien välisenä erottimena.

## Muutokset versiossa 1.0 ##
*   Ensimmäinen versio.
