# traduireDesExtensionsNVDAAvecCrowdin

The goal of this add-on is help translators work more efficiently when using this [project to translate NVDA add-ons with Crowdin](https://crowdin.com/project/nvdaaddons).

## Paramètres

Même si la plupart des traducteurs n'auront pas besoin d'utiliser cette fonctionnalité, une boîte de dialogue est fournie pour enregistrer le jeton Crowdin et pour sélectionner le répertoire où les fichiers de documentation et de messages d'interface seront stockés.
Pour ouvrir cette boîte de dialogue, accédez au menu NVDA, sous-menu Préférences, boîte de dialogue Paramètres, catégorie Traduire les extensions NVDA avec Crowdin.

Vous pouvez également attribuer un geste pour ouvrir les paramètres de l’extension depuis la boîte de dialogue Gestes de commandes.

## Traduire des extensions avec Crowdin

Cette boîte de dialogue est accessible depuis le menu NVDA, sous-menu Outils, ou en assignant un raccourci depuis la boîte de dialogue Gestes de commandes.

Les contrôles suivants sont disponibles:

- Une liste déroulante pour sélectionner la langue de traduction.
- Une zone d'édition pour filtrer la liste des fichiers disponibles à traduire.
- A list of files with po and md extensions. This will be focused when the dialog is opened. Press enter to open the selected file.
- A button to open the selected file. The file will be opened in the application associated with each kind of file on your system. De toute façon, en général, la documentation sera plus facile à traduire depuis l’interface web de Crowdin.
- A button to upload the selected translated file.
- A button to download translations for the selected language.
- A button to download all translations
- A button to close the dialog.

## Downloading and uploading translations

- This process may take several minutes, and may not be available if you reach your Crowdin token limits.
- NVDA may block during a few seconds when these processes are started. Après cela, vous pouvez travailler normalement et un message s'affichera lorsque le processus sera terminé