# Clip Contents Designer #
*   Autori: Noelia și Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Comenzi de taste ##
*   NVDA+Windows+C: Adaugă textul selectat, caracterele Unicode braille care
    reprezintă obiectele MathML, sau string-ul care a fost marcat cu cursorul de
    vizualizare, pe planșetă.
*   NVDA+Windows+X: Curăță contentul de pe planșetă.
*    Not assigned: Copies to (or cuts from) the clipboard, with the possibility
     of being asked for a previous confirmation.
*    Not assigned: Shows the clipboard text as HTML in browse mode, or announces
     if clipboard is empty or has contents which can't be presented in a
     browseable message, for instance if files or folders are been copied from
     Windows Explorer.
*    Not assigned: Shows the textual clipboard contents as plain text in browse
     mode, or announces if clipboard is empty or has contents which can't be
     presented in a browseable message, for instance if files or folders are
     been copied from Windows Explorer.

## Clip Contents Designer settings ##

This panel is available from NVDA's menu, Preferences submenu, Settings dialog.

It contains the following controls:

* Type the string to be used as a separator between contents added to the
  clipboard: Allows to set a separator which can be used to find the text
  segments once the entire added text is pasted.
* Add text before clip data: It's also possible to choose if the added text will
  be appended or prepended.
* Select the actions which require previous confirmation: You can choose, for
  each action available, if it should be performed inmediately or after
  confirmation. Available actions are: add text, clear clipboard, emulate copy
  and emulate cut.
* Request confirmation before performing the selected actions when: You can
  select if confirmations will be requested always, just if text is contained in
  the clipboard, or if clipboard is not empty (for example if you've copied a
  file, not text).
* Format to show the clipboard text as HTML in browse mode: If you're learning
  HTML markup language, you may choose Preformatted text in HTML or HTML as
  shown in a web browser, to have an idea of how your HTML code will be rendered
  by NVDA in a browser. The difference between preformatted and conventional
  HTML is that the first option will preserve consecutive spaces and line
  breaks, and the second one will compact them. For example, write some HTML
  tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and
  use clipContentsDesigner add-on to show the text in a browseable message.
* Maximum number of characters when showing clipboard text in browse mode:
  Please, be aware that increasing this limit may produce issues if the
  clipboard contains large strings of text. The default limit is 100000
  characters.
* Restore defaults.

Note:

*   Confirmations won't be requested when a message box of NVDA is still opened.
    In those cases, actions will be inmediately performed.
* Emulate copy and emulate cut commands mean that, when these features are
  enabled, the add-on will take control of control+c and control+x. This will
  allow to select if a confirmation should be requested before performing the
  actions corresponding to these keystrokes.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape key.

## Changes for 40.0.0
* Added support for Hebrew keyboard.

## Changes for 22.0.0
* Added a button to restore defaults in the add-on settings panel.
* The add-on cannot be run in secure mode.

## Changes for 17.0
* Compatible with NVDA 2023.1.

## Changes for 16.0
* Reqires NVDA 2022.1 or later.

## Changes for 15.0
* The command to add text to clipboard is again presented in the input gestures
  dialog.
* Fixed gestures to copy and cut with Persian keyboard, thanks to Mohammadhosein
  Ghezelsofla.

## Changes for 14.0
* Compatible with NVDA 2021.1.

## Changes for 13.0
* Fixed an issue in visual layout of the settings panel, thanks to Cyrille
  Bougot.
* Improved documentation.
* Added a Clip Contents Designer category to assign input gestures to all
  commands available for this add-on.
* Fixed bugs when using emulate copy in browsers if focus mode is active.
* You can assign different gestures to show the clipboard textual contents as
  raw text or formatted in HTML. The Format to show the clipboard text in the
  settings panel has being modified accordingly, to select the two options
  available for HTML format.

## Changes for 12.0
* Fixed bugs when using emulate copy in applications like LibreOffice Writer.

## Changes for 11.0
* Now it's possible to add text marked with the review cursor using standard
  commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer used,
  for a better integration with the new NVDA+shift+f9 command.
* Requires NVDA 2019.3 or later.

## Modificări în 10.0
* S-a rezolvat o problemă în dialog care făcea să se afișeze textul de pe
  planșetă când titlul său conținea caractere nelatine.
* S-a rezolvat o problemă întâmpinată la utilizarea copierii și a tăierii
  simulate cu o tastatură arabă. A fost rezolvată de Abdel, care acum are
  statutul de autor al suplimentului.

## Modificări în 9.0

* Acum, este posibilă afișarea textului aflat pe planșetă în modul de navigare.
* S-a adăugat o opțiune care vă permite să alegeți dacă vor fi sau nu necesare
  confirmările îb cazul în care planșeta nu este goală, un bun exemplu fiind
  copierea fișierelor sau a folderelor.
* Necesită NVDA 2018.4 sau mai nou.

## Modificări în 8.0 ##

* Setările suplimentului sunt afișate în categoria corespunzătoare a dialogului
  setărilor NVDA..
* Necesită NVDA 2018.2 sau mai nou.

## Modificări în 7.0

* În dialogul pentru configurarea copierii și tăierii simulate la instalare,
  dacă alegeți nu, comenzile pentru aceste caracteristici vor fi șterse, astfel
  încât să puteți restaura comportamentul normal pentru control+c și control+x.

## Modificări în 6.0

*    Added options to choose if available actions should be performed after
     confirmation.
*   Added Emulate copy and Emulate cut commands, which could be assigned from
    the Input gestures dialog.
*    Added a dialog to configure the Emulate copy and Emulate cut
     functionalities at installation. This allows to add the control+c and
     control+x commands to copy and cut, and be asked if you want to replace the
     clipboard contents when pressing these keystrokes.
*   Fixed documentation for script_add (Windows+NVDA+c).

## Modificări în 5.0 ##

*   Prezentarea vizuală a dialogului a fost îmbunătățită, aderând la aspectul
    dialogurilor afișate în NVDA.
*   Necesită NVDA 2016.4 sau mai nou.

## Modificări din 4.0 ##
*   Setările suplimentului sunt gestionate din configurarea NVDA, deci
    profilurile implicite pot fi folosite pentru a salva diferite separatoare,
    și nu este nevoie să copiezi setările pentru a le importa la reinstalare.
*   Acum este posibilă selectarea dacă textul adăugat va fi anexat sau prefixat,
    utilizând căsuța Adăugare text din dialogul de setări al Clip Contents
    Designer-ului.

## Modificări din 3.0 ##
*   Reprezentarea Braille din obiectele MathML poate fi adăugat pe planșetă dacă
    MathPlayer este instalat.
*   Dacă niciun separator nu este setat, o singură linie va fi adăugată între
    segmentele textului adăugat.
*   O scurtătură poate fi definită pentru a deschide setările Clip Contents
    Designer-ului.
*   A fost adăugată o căsuță în dialogul de setări, pentru a selecta dacă
    separatorul trebuie să fie copiat pentru a fi immportat când reinstalezi
    add-on-ul.

## Modificări din 2.0 ##
*   Caracterele indiene pot fi folosite ca separator între content-ul adăugat.

## Modificări din 1.0 ##
*   Versiunea inițială.
