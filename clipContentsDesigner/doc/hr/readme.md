# Clip Contents Designer #
*   Authors: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Tipkovnički prečaci ##
*   NVDA+windows+c: U međuspremnik dodaj označeni tekst, brajične znakove u
    unikodu koji predstavljaju MathML objekte ili znakovni niz koji je označen
    pomoću preglednog kursora.
*   NVDA+windows+x: Obriši sadržaj međuspremnika.
*    Nije dodijeljeno: Kopira u međuspremnik (ili se reže iz njega), s
     mogućnošću da se prethodno od korisnika traži potvrda.
*    Nije dodijeljeno: Prikazuje tekst međuspremnika u modusu čitanja ili
     najavljuje prazno stanje međuspremnika ili sadržaj koji se ne može
     predstaviti u pregledavajućoj poruci, na primjer ako su datoteke ili mape
     kopirane iz Windows Explorera.
*    Nije dodijeljeno: Prikazuje tekstualni sadržaj međuspremnika kao običan
     tekst u modusu čitanja ili najavljuje prazno stanje međuspremnika ili
     sadržaj koji se ne može predstaviti u pregledavajućoj poruci, na primjer
     ako su datoteke ili mape kopirane iz Windows Explorer.

## Postavke dodatka „Upravljanje sadržajem međuspremnika” ##

Ova je ploča dostupna u NVDA izborniku, podizbornik Postavke, dijaloški okvir
Postavke.

Sadrži sljedeće kontrole:

* Upiši znakovni niz koji će se koristiti kao razdjeljivač između sadržaja koji
  su dodani u međuspremnik: Omogućuje postavljanje razdjeljivača koji se može
  koristiti za pronalaženje segmenata teksta nakon što je cijeli dodani tekst
  umetnut.
* Dodaj tekst prije podataka međuspremnika: Također je moguće odabrati, hoće li
  se dodani tekst umetnuti ispred ili iza.
* Odaberi radnje koje zahtijevaju prethodnu potvrdu: Za svaku dostupnu radnju
  možeš odabrati, hoće li se izvršiti odmah ili nakon potvrde. Dostupne radnje
  su: dodaj tekst, isprazni međuspremnik, emuliraj kopiranje i emuliraj
  izrezivanje.
* Zatraži potvrdu prije izvođenja odabranih radnji: Možeš odabrati hoće li se
  potvrde zatražiti uvijek, samo ako se tekst nalazi u međuspremniku ili ako
  međuspremnik nije prazan (na primjer ako si kopirao/la datoteku, a ne tekst).
* Format to show the clipboard text as HTML in browse mode: If you're learning
  HTML markup language, you may choose Preformatted text in HTML or HTML as
  shown in a web browser, to have an idea of how your HTML code will be rendered
  by NVDA in a browser. The difference between preformatted and conventional
  HTML is that the first option will preserve consecutive spaces and line
  breaks, and the second one will compact them. For example, write some HTML
  tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and
  use clipContentsDesigner add-on to show the text in a browseable message.
* Maksimalni broj znakova kada se prikazuje tekst međuspremnika u modusu
  čitanja: imaj na umu da povećanje ovog ograničenja može uzrokovati probleme
  ako međuspremnik sadrži dugačke tekstove. Standardno ograničenje je 100.000
  znakova.
* Obnovi standardne vrijednosti.

Napomene:

*   Neće biti potrebno potvrditi, ako se neka NVDA poruka još uvijek prikazuje.
    U tim će se slučajevima radnje izvršavati odmah.
* Naredbe za emuliranje kopiranja i emuliranje izrezivanja znače, da će dodatak
  preuzeti kontrolu nad kontrol+c i kontrol+x kad su ove funkcije aktivirane.
  Time se može odabrati mogućnost za potvrdom prije izvođenja radnji koje
  odgovaraju tim prečacima.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape key.

## Changes for 40.0.0
* Added support for Hebrew keyboard.

## Promjene u verziji 22.0.0
* Dodan je gumb za obnavljanje zadanih postavki u ploči postavki dodatka.
* Dodatak se ne može pokrenuti u sigurnom modusu.

## Promjene u verziji 17.0
* Kompatibilno s NVDA čitačem 2023.1.

## Promjene u verziji 16.0
* Zahtijeva NVDA 2022.1 ili noviju verziju.

## Promjene u verziji 15.0
* Naredba za dodavanje teksta u međuspremnik ponovo se prikazuje u dijaloškom
  okviru gesta unosa.
* Ispravljene su geste za kopiranje i rezanje s perzijskom tipkovnicom, hvala
  Mohammadhosein Ghezelsofla.

## Promjene u verziji 14.0
* Kompatibilno s NVDA čitačem 2021.1.

## Changes for 13.0
* Ispravljen je problem s vizualnim izgledom u ploči s postavkama. Hvala Cyrille
  Bougot.
* Poboljšana dokumentacija.
* Dodatku „Upravljanje sadržajem međuspremnika” je dodana kategorija za dodjelu
  gesta unosa svim naredbama koje su dostupne za ovaj dodatak.
* Ispravljene su greške prilikom korištenja emuliranja kopiranja u preglednicima
  ako je modus fokusa aktiviran.
* Mogu se dodijeliti različite geste za prikaz tekstualnog sadržaja
  međuspremnika kao neobrađeni tekst ili formatiran u HTML-u. Format za prikaz
  teksta međuspremnika je u ploči postavki u skladu s time promijenjen, što
  omogućuje biranje tih dviju opcija dostupne za HTML format.

## Promjene u verziji 12.0
* Ispravljene su greške prilikom korištenja emuliranja kopiranja u programima
  poput LibreOffice Writer.

## Promjene u verziji 11.0
* Sada je moguće dodati tekst koji je označen preglednim kursorom, pomoću
  standardnih naredbi NVDA (NVDA+f9 i NVDA+f10). NVDA+windows+f9 se više ne
  koristi, radi boljw integracijw s novom naredbom NVDA+šift+f9.
* Zahtijeva NVDA verziju 2019.3 ili noviju.

## Promjene u verziji 10.0
* Ispravljana je greška u dijaloškom okviru za prikaz teksta međuspremnika, kad
  naslov sadrži ne-latinične znakove.
* Ispravljena je greška kad se koriste funkcije emuliranja izrezivanja i
  kopiranja s arapskim rasporedom tipkovnice. To je ispravio Abdel, dodan je kao
  autor dodatka.

## Promjene u verziji 9.0

* Dodana je mogućnost prikazivanja teksta međuspremnika u modusu čitanja.
* Dodana je opcija za potrebu potvrđivanja ako međuspremnik nije prazan, na
  primjer, ako su kopirane datoteke ili mape.
* Zahtijeva NVDA verziju 2018.4 ili noviju.

## Promjene u verziji 8.0 ##

* Postavke dodatka se prikazuju u odgovarajućoj kategoriji dijaloškog okvira za
  NVDA Postavke.
* Zahtijeva NVDA verziju 2018.2 ili noviju.

## Promjene u verziji 7.0

* Ako se u dijaloškom okviru za konfiguriranje funkcionalnosti „Emuliraj
  kopiranje” i „Emuliraj izrezivanje” odabere „ne”, naredbe za ove funkcije će
  se ukloniti kako bi se omogućio normalni način rada za kontrol+c i kontrol+x.

## Promjene u verziji 6.0

*    Dodane su opcije s kojima se može odlučiti je li se dostupne radnje trebaju
     izvršiti nakon potvrde.
*   Dodane su naredbe „Emuliraj kopiranje” i „Emuliraj izrezivanje”, koje je
    moguće dodijeliti u dijaloškom okviru „Ulazne geste”.
*    Dodan je dijaloški okvir za podešavanje naredbi „Emuliraj kopiranje” i
     „Emuliraj izrezivanje”, tijekom instaliranja. Ovo dozvoljava dodavanje
     naredbi kontrol+c i kontrol+x za kopiranje i izrezivanje, te postavljanjem
     pitanja, želiš li zamijeniti sadržaj međuspremnika pri korištenju ovih
     tipkovničkih prečaca.
*   Ispravljena je dokumentacija za script_add (Windows+NVDA+c).

## Promjene u verziji 5.0 ##

*   Vizualni prikaz dijaloških okvira je poboljašn, slično dijaloškim okvirima
    koji su prikazani u programu NVDA.
*   Zahtijeva NVDA verziju 2016.4 ili noviju.

## Promjene u verziji 4.0 ##
*   Postavkama dodatka se upravlja NVDA konfiguracijom, tako da je moguće
    koristiti standardne profile za spremanje raznih rastavljača te nije
    potrebno kopirati postavke nakon reinstalacije.
*   Sad je moguće izabrati, hoće li dodani tekst biti dodan ispred ili iza
    postojećeg teksta, koristeći izborno polje „Dodaj tekst ispred podataka
    međuspremnika” u postavkama dodatka.

## Promjene u verziji 3.0 ##
*   Brajičin prikaz MathML objekata se može dodati u privremenu memoriju, ako je
    MathPlayer instaliran.
*   Ako nema razdvajača, dodat će se samo jedan redak između dodanih segmenata
    teksta.
*   Moguće je odrediti prečac za otvaranje dijaloškog okvira za postavke
    dodatka.
*   U dijaloškom okviru za postavke je dodan potvrdni okvir, kojim se odlučuje o
    tome, treba li razdvajač kopirati za uvoz nakon ponovnog instaliranja
    dodatka.

## Promjene u verziji 2.0 ##
*   Znakovi devanagari pisma se mogu koristiti kao rastavljači između dodanog
    sadržaja.

## Promjene u verziji 1.0 ##
*   Prva verzija.
