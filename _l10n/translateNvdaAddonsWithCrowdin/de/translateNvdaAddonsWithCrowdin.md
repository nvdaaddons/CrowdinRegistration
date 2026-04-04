# translateNvdaAddonsWithCrowdin

The goal of this add-on is help translators work more efficiently when using this [project to translate NVDA add-ons with Crowdin](https://crowdin.com/project/nvdaaddons).

## Danach können Sie normal arbeiten und es sollte eine Meldung angezeigt werden, wenn der Vorgang abgeschlossen ist.

Obwohl die meisten Übersetzer diese Funktion nicht verwenden müssen, wird ein Dialogfeld zum Speichern des Crowdin-Tokens und zur Auswahl des Verzeichnisses bereitgestellt, in dem Dokumentations- und Schnittstellennachrichtendateien gespeichert werden.
Um dieses Dialogfeld zu öffnen, gehen Sie zum NVDA-Menü, Untermenü Optionen Dialogfeld „Einstellungen“ und der Kategorie „NVDA-Add-ons mit Crowdin übersetzen“.

Außerdem kann eine Geste zugewiesen werden, um die Add-on-Einstellungen über das Dialogfeld „Tastenbefehle“ zu öffnen.

## Translate add-ons with Crowdin

This dialog can be accessed from NVDA menu, Tools submenu, or assigning a gesture from the Input gestures dialog.

Folgende Steuerelemente stehen zur Verfügung:

- Ein Kombinationsfeld zur Auswahl der Übersetzungssprache.
- Ein Bearbeitungsfeld zum Filtern der Liste der zur Übersetzung verfügbaren Dateien.
- A list of files with po and md extensions. Dies wird beim Öffnen des Dialogs hervorgehoben. Drücken Sie die Eingabetaste, um die ausgewählte Datei zu öffnen.
- Eine Schaltfläche zum Öffnen der ausgewählten Datei. The file will be opened in the application associated with each kind of file on your system. Im Allgemeinen lässt sich die Dokumentation jedoch einfacher über die Crowdin-Weboberfläche übersetzen.
- Eine Schaltfläche zum Hochladen der ausgewählten übersetzten Datei.
- Eine Schaltfläche zum Herunterladen von Übersetzungen für die ausgewählte Sprache.
- A button to download all translations
- A button to close the dialog.

## Downloading and uploading translations

- This process may take several minutes, and may not be available if you reach your Crowdin token limits.
- NVDA may block during a few seconds when these processes are started. Danach können Sie normal arbeiten und es sollte eine Meldung angezeigt werden, wenn der Vorgang abgeschlossen ist