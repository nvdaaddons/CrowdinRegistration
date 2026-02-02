[[!meta title="Zaključavanje unosa"]]

* Autor: Jose Manuel Delicado
* NVDA kompatibilnost: 2023.3.4 i novije verzije
* Preuzmite [stabilnu verziju][1]

## Uvod

Imate li djecu ili kućne ljubimce? Imate li možda mačku koja se jako voli penjati po vašem stolu i hodati po tastaturi? Pomičete li slučajno miš na nasumične dijelove zaslona dok koristite prijenosni računar? Onda je ovaj dodatak za vas! Moći ćete bez rizika ostaviti svoj računar uključenim na miru.

Jednom kad se instalira, moći ćete zaključati svoju tastaturu, dodirni zaslon (ako ga vaš računar ima), dodirnu ploču, miš i brajev zaslon.

## Upotreba

Ovaj dodatak dodaje tri geste. Po zadanim postavkama su one nedodijeljene, pa ćete ih trebati dodijeliti iz dijaloga ulaznih gesti. Pročitajte NVDA korisnički vodič za više informacija.

Kada pritisnete gestu za zaključavanje tastature, NVDA će izgovoriti "Tastatura je zaključana". Vaši ulazni uređaji će biti blokirani sve dok ponovo ne pritisnete istu gestu. U tom trenutku će NVDA izgovoriti "Tastatura je otključana" i sve će raditi kao i obično.
Zaključavanje dodirne ploče može spriječiti neželjene radnje slučajnim dodirivanjem, posebno ako volite direktno koristiti tastaturu prijenosnog računara. Kada pritisnete gestu za zaključavanje dodirne ploče, NVDA će izgovoriti "Dodirna ploča je zaključana". Vaša dodirna ploča će biti blokirana sve dok ponovo ne pritisnete istu gestu. U tom trenutku će NVDA izgovoriti "Dodirna ploča je otključana" i sve će raditi kao i obično.

Ako pritisnete gestu za zaključavanje miša, vaš miš će biti zaključan. Pritisnite tu gestu ponovo da biste ga otključali. Dok je miš zaključan, možete koristiti NVDA geste da ga pomijerate i simulirate lijevi i desni klik. Međutim, miš kao takav neće reagovati na pomijeranje i klikove. Klikovi miša mogu biti onemogućeni u kategoriji "Zaključavanje unosa"  u NVDA postavkama (2018.2 i novije) ili kroz dijalog postavki dodatka za starije verzije, inače dostupan u podizborniku "Postavke". Osim toga, u ovim postavkama možete odrediti hoće li se miš zaključati kada se NVDA pokrene.

Napomena: kad su blokirani klikovi miša, nećete moći koristiti NVDA geste za rad s mišem.

## Ograničenja i poznati problemi

Zaključavanje unosa ima sljedeće poznate probleme:

* Prečice `Control+Alt+Delete` i `Windows+L` mogu se koristiti čak i kada je tastatura zaključana.
* Za geste zaključavanja i otključavanja dodirne ploče, probajte dodijeliti što jednostavniju prečicu. Preporučuje se da to bude NVDA+slova ili brojevi, Control+F tipke i tako dalje.

## Promjene

### Verzija 1.13

* Sada je minimalna podržana verzija 2023.3.4.
* Ažurirani su prijevodi. Počevši od verzije 1.13, odjeljak promjena neće biti ažuriran kada nova verzija sadrži samo ažuriranja prijevoda.
* Dodana je gesta (po zadanim postavkama je nedodijeljena) za zaključavanje i otključavanje dodirne ploče.

### Verzija 1.12

* Osigurana je kompatibilnost s novijim NVDA verzijama.
* Ažurirani su prijevodi.

### Verzija 1.11

* Osigurana je kompatibilnost s novijim NVDA verzijama.
* Ažurirani su prijevodi.
* Sada je minimalna podržana verzija 2022.4.

### Verzija 1.10

* Osigurana je kompatibilnost s novijim NVDA verzijama.
* Ažurirani su prijevodi.
* Ažurirana je dokumentacija.
* Sada je minimalna podržana verzija 2021.3.
* Unos će od sada ostati zaključan i nakon buđenja iz načina mirovanja. Hvala Javiju Dominguezu.

### Verzija 1.9

* Osigurana je kompatibilnost s novijim NVDA verzijama.
* Ažurirani su prijevodi.
* Ažurirana je dokumentacija.

### Verzija 1.8

* Osigurana je kompatibilnost s novijim NVDA verzijama.
* Ažurirani su prijevodi.

### Verzija 1.7

* Osigurana je kompatibilnost s novijim NVDA verzijama.
* Ažurirani su prijevodi.

### Verzija 1.6

* Sada se postavke uklanjaju samo kada se dodatak deinstalira. Konfiguracija se ne postavlja ponovno nakon ažuriranja.
* Dodani su novi prijevodi i ažurirani su postojeći.

### Verzija 1.5

* Osigurana je kompatibilnost s novijim NVDA verzijama.
* Dodani su novi prijevodi i ažurirani su postojeći.

### Verzija 1.4

* Geste dodatka sada su po zadanim postavkama nedodijeljene.

### Verzija 1.3

* Dodan je panel postavki. Za starije NVDA verzije, dodani su i stavka izbornika i dijalog.
* Dodana je postavka za zaključavanje miša kad se NVDA pokrene.
* Dodana je postavka za blokiranje klikova kad je miš zaključan.
* Ispravljene su male greške, izvršene su neke optimizacije koda i manje je duplikovanih nizova za prevoditelje

### Verzija 1.2

* Sada se miš također može zaključati
* Dodana je nova komanda za zaključavanje i otključavanje samo miša

### Verzija 1.1

* Ako je neki drugi dodatak prethodno dodao funkciju snimanja u InputManager, ona se vraća kada se unos otključa.

### Verzija 1.0

* Početno izdanje

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
