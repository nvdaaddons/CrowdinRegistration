# RDAccess: Etätyöpöydän saavutettavuus

* Tekijä: [Leonard de Ruijter][1]
* Lataa [uusin vakaa versio][2]
* Yhteensopivuus: NVDA 2024.1 ja uudemmat

RDAccess-lisäosa lisää NVDA:han tuen etätyöpöytäistunnoille Microsoft Etätyöpöytää, Citrixiä, Parallels RASia tai VMware Horizonia käyttäen.
Kun tämä lisäosa on asennettu NVDA:han sekä asiakas- että palvelinkoneessa, palvelimella tuotettu puhe ja pistekirjoitus puhutaan ja näytetään asiakaskoneessa.
Tämä mahdollistaa käyttäjäkokemuksen, jossa etäjärjestelmän hallinta tuntuu aivan paikallisen järjestelmän käyttämiseltä.

## Ominaisuudet

* Tuki Microsoft Etätyöpöydälle (Azure Virtual Desktop ja Microsoft Cloud PC mukaan lukien), Citrixille, Parallels RASille sekä VMware Horizonille
* Puheen ja pistekirjoituksen tuottaminen
* Automaattinen etäpistenäyttöjen tunnistus NVDA:n automaattista pistenäytön tunnistusta käyttäen
* Automaattinen etäpuhesyntetisaattoreiden tunnistus erityistä tunnistusmenetelmää käyttäen, joka voidaan poistaa käytöstä NVDA:n asetusvalintaikkunassa
* Tuki palvelimella käynnissä olevalle NVDA:n massamuistiversiolle (Citrixiä varten tarvitaan lisämäärityksiä)
* Täysi tuki asiakaskoneessa käynnissä olevalle NVDA:n massamuistiversiolle (lisäosan asentamiseen ei tarvita järjestelmänvalvojan oikeuksia)
* Samanaikaisesti useita aktiivisia asiakasistuntoja
* Etätyöpöytä on käytettävissä heti NVDA:n käynnistyksen jälkeen
* Mahdollisuus muuttaa tiettyjä syntetisaattori- ja pistenäyttöasetuksia etäistunnosta poistumatta
* Mahdollisuus käyttää puhetta ja pistenäyttöä käyttäjäistunnosta suojatulla työpöydällä oltaessa

## Muutosloki

### Versio 1.6

* Parallels RAS -tukea dokumentoitu ja paranneltu.
* NVDA:n yhteensopiva vähimmäisversio on nyt 2025.1. Vanhempien versioiden tuki on poistettu.
* RdPipe-riippuvuus päivitetty.
* Lisätty mahdollisuus RdPipen lokitason määrittämiseen.
* Lisätty asetuspaneeliin RdPipe-lokin tarkastelutoiminto.
* Asennuksen poiston toimintaa paranneltu (ei aiheuta enää virheitä eikä poista Citrix-tukea, jos Citrix ei ole käytettävissä).

### Versio 1.5

* Lisätty mahdollisuus luoda virheenjäljityksen vianmääritysraportti painikkeen avulla RDAccessin asetuspaneelissa [#23](https://github.com/leonardder/rdAccess/pull/23).
* Tuki monirivisille pistenäytöille NVDA 2025.1:ssä ja sitä uudemmissa [#19](https://github.com/leonardder/rdAccess/pull/13).
* NVDA:n yhteensopiva vähimmäisversio on nyt 2024.1. Aiempien versioidenn tuki on poistettu.
* Lisätty asiakasyhteyden ilmoitukset [#25](https://github.com/leonardder/rdAccess/pull/25).
* RdPipe-riippuvuus päivitetty.
* Käännöksiä päivitetty.

### Versio 1.4

* Uusi vakaa versio.

### Versio 1.3

* Rikkoutuneet pistenäyttöjen näppäinkomennot korjattu.

### Versio 1.2

* Koodin muotoilijana ja tarkistustyökaluna käytetään [Ruffia](https://github.com/astral-sh/ruff). [#13](https://github.com/leonardder/rdAccess/pull/13).
* Korjattu ongelma, joka aiheutti sen, että NVDA tuotti asiakaskoneella virheen, kun puhe tauotettiin palvelimella.
* Korjattu `winAPI.secureDesktop.post_secureDesktopStateChange`:n tuki.
* Ajurin alustusta paranneltu palvelimella.

### Versio 1.1

* Lisätty tuki NVDA 2023.3:n tyyliselle pistenäyttöjen automaattisen tunnistuksen laiterekisteröinnille. [#11](https://github.com/leonardder/rdAccess/pull/11).
* Lisätty tuki NVDA 2024.1 alfan `winAPI.secureDesktop.post_secureDesktopStateChange`-laajennuspisteelle. [#12](https://github.com/leonardder/rdAccess/pull/12).

### Versio 1.0

Ensimmäinen vakaa versio.

## Aloittaminen

1. Asenna RDAccess NVDA:han sekä asiakas- että palvelinkoneella.
1. Etäjärjestelmän pitäisi alkaa puhua paikallista puhesyntetisaattoria käyttäen. Jos näin ei tapahdu, valitse etäpuhesyntetisaattori palvelimella käynnissä olevan NVDA:n Valitse syntetisaattori -valintaikkunasta.
1. Voit käyttää pistekirjoitusta ottamalla käyttöön automaattisen pistenäytön tunnistuksen "Valitse pistenäyttö" -valintaikkunassa.

## Asetusten määrittäminen

Kun RDAccess-lisäosa on asennettu, sen asetukset voidaan määrittää NVDA:n asetusvalintaikkunasta, johon pääsee valitsemalla NVDA-valikosta Mukautukset > Asetukset...
Valitse lopuksi Etätyöpöytä-kategoria.

Tämä valintaikkuna sisältää seuraavat asetukset:

### Ota etätyöpöydän saavutettavuus käyttöön

Tämän luettelon valintaruuduilla voit valita lisäosan toimintatilan. Seuraavat vaihtoehdot ovat käytettävissä:

* Saapuville yhteyksille (etätyöpöytäpalvelin): Valitse tämä vaihtoehto, jos nykyinen NVDA-kopio on käynnissä etätyöpöytäpalvelimella.
* Lähteville yhteyksille (etätyöpöytäasiakas): Valitse tämä vaihtoehto, jos nykyinen NVDA-kopio on käynnissä etätyöpöytäasiakkaalla, joka muodostaa yhteyden yhteen tai useampaan palvelimeen.
* Suojatun työpöydän läpivienti: Valitse tämä vaihtoehto, jos haluat käyttää NVDA:n käyttäjäkopion pistenäyttöä ja puhetta etätyöpöytää käyttäessäsi. Huom: Jotta tätä toimintoa voisi käyttää, RDAccess-lisäosa on kopioitava suojatulla työpöydällä käytettävään NVDA-versioon. Tämä tehdään valitsemalla NVDA:n yleisistä asetuksista "Käytä tallennettuja asetuksia kirjautumisikkunassa ja suojatuissa ruuduissa (edellyttää järjestelmänvalvojan oikeuksia)".

Kaikki asetukset ovat oletusarvoisesti käytössä, jotta varmistetaan sujuva lisäosan käytön aloitus. Sinua kuitenkin kannustetaan poistamaan käytöstä tarpeen mukaan joko palvelin- tai asiakastila.

### Palauta etäpuhe automaattisesti yhteyden katkettua

Tämä asetus on käytettävissä vain palvelintilassa. Se varmistaa, että yhteys muodostetaan automaattisesti uudelleen, kun etäpuhesyntetisaattori on käytössä yhteyden katketessa. Tämä toiminnallisuus on samankaltainen kuin pistenäytön automaattinen tunnistus.

Asetus on oletusarvoisesti käytössä. Sen käytössä pitäminen on erittäin suositeltavaa, mikäli etätyöpöytäpalvelimella ei ole äänilaitetta.

### Anna etäjärjestelmän muuttaa ajurin asetuksia

Tämä asiakasasetus mahdollistaa käytössä ollessaan ajurin asetusten (kuten syntetisaattorin puheäänen ja äänenkorkeuden) muuttamisen etäjärjestelmästä. Etäjärjestelmässä tehdyt muutokset toteutetaan automaattisesti paikallisessa järjestelmässä.

### Säilytä asiakastuki NVDA:ta suljettaessa

Tämä asiakasasetus, joka on käytettävissä vain NVDA:n asennetuissa versioissa, varmistaa käytössä ollessaan, että NVDA:n asiakasosa ladataan etätyöpöytäasiakkaaseesi, vaikka NVDA ei olisi käynnissä.

Windowsin rekisteriin on tehtävä muutoksia, jotta RDAccessin asiakasosaa voidaan käyttää.
Lisäosa varmistaa, että nämä muutokset tehdään nykyiseen käyttäjäprofiiliin.
Siksi NVDA voi käynnistettäessä tehdä tarvittavat muutokset automaattisesti ja perua ne suljettaessa. Tämä varmistaa, että lisäosa on täysin yhteensopiva NVDA:n massamuistiversioiden kanssa.

Tämä asetus on oletusarvoisesti poissa käytöstä. Jos käytössäsi kuitenkin on NVDA:n asennettu versio ja olet järjestelmän ainoa käyttäjä, tämän asetuksen käyttöönotto on suositeltavaa. Tämä varmistaa sujuvan toiminnan muodostettaessa yhteyttä etäjärjestelmään NVDA:n käynnistyksen jälkeen.

### Ota käyttöön oletusetätyöpöydän tuki

Tämä asetus on oletusarvoisesti käytössä ja varmistaa, että RDAccessin asiakasosa ladataan Microsoft-etätyöpöytäasiakkaaseen NVDA:ta käynnistettäessä.
Tätä asetusta tarvitaan myös VMware Horizonille, Parallels RASille, Azure Virtual Desktopille jne.
Asetuksen tekemät muutokset perutaan automaattisesti NVDA:ta suljettaessa, ellei asiakastuen säilyttämistä ole otettu käyttöön.

### Ota käyttöön Citrix Workspacen tuki

Tämä asetus on oletusarvoisesti käytössä ja varmistaa, että RDAccessin asiakasosa ladataan Citrix Workspace -sovellukseen NVDA:ta käynnistettäessä.
Asetuksen tekemät muutokset perutaan automaattisesti NVDA:ta suljettaessa, ellei asiakastuen säilyttämistä ole otettu käyttöön.

Tämä asetus on käytettävissä vain seuraavissa tilanteissa:

* Citrix Workspace on asennettu. Huom: Sovelluksen Windows Store -versiota ei tueta sen rajoitusten vuoksi.
* RDAccess on mahdollista rekisteröidä nykyiselle käyttäjälle. Tämä tehdään aloittamalla etäistunto kerran sovelluksen asennuksen jälkeen.

### Ilmoita yhteyden muutokset

Tästä yhdistelmäruudusta voit hallita ilmoituksia, jotka vastaanotetaan, kun etäjärjestelmä avaa tai sulkee etäpuhe- tai pistenäyttöyhteyden.
Seuraavat vaihtoehdot ovat käytettävissä:

* Ei käytössä (ei ilmoituksia)
* Ilmoituksilla (esim. "Etäpistenäyttö yhdistetty")
* Äänillä (NVDA 2025.1 ja uudemmat)
* Ilmoituksilla ja äänillä

Huomaa, että äänet eivät ole käytettävissä NVDA 2025.1:tä vanhemmissa versioissa. Vanhemmissa versioissa käytetään merkkiääniä.

### Avaa vianmääritysraportti

Tämä painike avaa erillisessä ikkunassa JSON-muotoisen tulosteen useista vianmäärityksistä, jotka voivat mahdollisesti auttaa virheenjäljityksessä.
Kun [teet GitHubissa][4] ilmoituksen ongelmasta, sinua saatetaan pyytää toimittamaan tämä raportti lisäosan tekijöille.

## Citrix-ohjeet

RDAccessin käytössä Citrix Workspace -sovelluksen kanssa on otettava huomioon joitakin tärkeitä seikkoja:

### Asiakaspuolen vaatimukset

1. Sovelluksen Windows Store -versiota ei tueta.
1. Kun olet asentanut Citrix Workspace -sovelluksen, sinun on käynnistettävä etäistunto kerran, jotta RDAccess voi rekisteröidä itsensä. Syynä tähän on se, että sovellus kopioi järjestelmän asetukset käyttäjän asetuksiin luodessaan istunnon ensimmäistä kertaa. Tämän jälkeen RDAccess voi rekisteröidä itsensä nykyiselle käyttäjälle.

### Palvelinpuolen vaatimus

Citrix otti käyttöön Citrix Virtual Apps and Desktopsin versiossa 2109 niin kutsutun virtuaalikanavan sallittujen luettelon. Tämä tarkoittaa, että kolmannen osapuolen virtuaalikanavia, RDAccessin tarvitsema kanava mukaan lukien, ei oletusarvoisesti sallita.
Katso lisätietoja [tästä Citrixin blogikirjoituksesta](https://www.citrix.com/blogs/2021/10/14/virtual-channel-allow-list-now-enabled-by-default/).

RDAccessin tarvitseman RdPipe-kanavan erikseen sallimista ei ole vielä testattu. Toistaiseksi on suositeltavaa poistaa sallittujen luettelo kokonaan käytöstä. Mikäli järjestelmäsi ylläpitäjä ei ole tyytyväinen tähän ratkaisuun, voit [ottaa asian esiin täällä][3].

## Ongelmat ja kehitykseen osallistuminen

Jos haluat ilmoittaa ongelmasta tai osallistua tämän lisäosan kehitykseen, tutustu [GitHubin issues-sivuun][4].

## Ulkoiset osat

Tämä lisäosa on riippuvainen [RD Pipestä][5], Rust-ohjelmointikielellä kirjoitetusta kirjastosta, joka mahdollistaa etätyöpöytäasiakkaan tuen.
RD Pipeä jaetaan tämän lisäosan mukana Free Software Foundationin julkaiseman [GNU AGPL -lisenssin version 3][6] ehtojen mukaisesti.

[[!tag stable dev beta]]

[1]: https://github.com/leonardder/

[2]: https://www.nvaccess.org/addonStore/legacy?file=rdAccess

[3]: https://github.com/leonardder/rdAccess/issues/1

[4]: https://github.com/leonardder/rdAccess/issues

[5]: https://github.com/leonardder/rd_pipe-rs

[6]: https://github.com/leonardder/rd_pipe-rs/blob/master/LICENSE
