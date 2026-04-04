# Lire les flux

- Auteurs: Noelia Ruiz Martínez, Mesar Hameed

Cette extension offre un moyen simple de lire les flux aux formats Atom ou RSS avec NVDA.
Les flux ne seront pas actualisés automatiquement.
Ci-dessous, quand nous mentionnons des flux, nous entendons par là les flux RSS et ATOM.

## Commandes

### Dialogue de lecture des flux

Vous pouvez accéder à la boîte de dialogue Lire les flux à partir du menu Nvda, sous-menu Outils, élément Flux.

Elle contient les contrôles suivants:

- Filtrer par: Un champ d'édition pour rechercher des flux précédemment enregistrés.
- Une liste des flux enregistrés, sur laquelle se trouve le focus à l'ouverture de la boîte de dialogue.
- Liste des articles: Ouvre une boîte de dialogue qui présente la liste des articles du flux sélectionné. Sélectionnez l'article que vous souhaitez lire et appuyez sur Entrée ou sur le bouton Ouvrir la page web de l'article sélectionné pour ouvrir la page correspondante dans votre navigateur. Appuyez sur le bouton À propos de l'article pour ouvrir une boîte de dialogue affichant le titre et le lien de l'article sélectionné; à partir de cette boîte de dialogue, vous pourrez copier ces informations dans le presse-papiers.
- Ouvrir le flux: Ouvre le flux sélectionné dans l'application par défaut.
- Ouvrir le flux en HTML: Ouvre le flux sélectionné dans votre navigateur web par défaut. Vous pourrez afficher ou masquer les dates de publication et les boutons pour copier les informations sur les articles dans le presse-papiers.
- Copier l'adresse du flux: Ouvre une boîte de dialogue pour confirmer si vous souhaitez copier l'adresse du flux dans le presse-papiers.
- Nouveau: Ouvre une boîte de dialogue avec un champ d'édition pour entrer l'adresse d'un nouveau flux. Si l'adresse est valide et que le flux peut être enregistré, son nom, basé sur le titre du flux, apparaîtra au bas de la liste des flux.
- Renommer: Ouvre une boîte de dialogue avec un champ d'édition pour renommer le flux sélectionné.
- Supprimer: Ouvre une boîte de dialogue pour supprimer le flux sélectionné après confirmation.
- Définir par défaut: Définit le flux sélectionné comme flux par défaut, afin que ses articles soient accessibles avec les commandes de NVDA.
- Importer des flux à partir d'un fichier OPML: Ouvre une boîte de dialogue pour ajouter de nouveaux flux à partir d'un fichier OPML.
- Enregistrer les flux dans un fichier OPML: Ouvre une boîte de dialogue pour enregistrer les flux disponibles dans la boîte de dialogue Flux dans un fichier OPML.
- Préférences: Ouvre la boîte de dialogue des paramètres pour le lecteur de flux, également disponible dans le menu NVDA, Préférences, paramètres, catégorie Lecteur de flux.
- Fermer: Ferme la boîte de dialogue Flux.

### Notes

- Le champ d'édition Filtrer par peut être placé après le bouton Ouvrir l'article à partir du menu NVDA, Préférences, Paramètres, catégorie Lecteur de Flux, ou en appuyant sur le bouton Préférences de la boîte de dialogue Flux.
- Ce panneau dispose d'une option pour afficher les dates des articles dans la boîte de dialogue Liste des articles.

### Commandes clavier

- Ctrl+Shift+NVDA+Espace : Annonce l'URL de l'article sélectionné. Un double appui ouvrira la page web.
- Ctrl+Shift+NVDA+8 : Actualise le flux sélectionné et annonce son titre le plus récent.
- Ctrl+Shift+NVDA+I : Annonce le titre et le lien du flux sélectioné. Appuyer deux fois copiera le titre et le lien associé dans le presse-papiers.
- Ctrl+Shift+NVDA+U : Annonce leCtrl+Shift+NVDA+U : Annonce le titre du flux précédent.
- Ctrl+Shift+NVDA+O : Annonce le titre du flux suivant.

## Notifications

- When the title or URL have been copied.
- When unable to connect/refresh a feed, or the URL does not correspond to a valid feed.
- NVDA will display an error message if a new feed cannot be created.
- The title of the articles list dialog displays the selected feed name and number of items available.

## Changes for 44.0.0

- Removed xml package, included in NVDA.

## Changes for 39.0.0

- Improved notifications when title or URL are copied.

## Changes for 34.0.0

- Added support for rss.cbc.ca feeds.

## Changes for 21.0

- Feeds with untitled articles can be presented in the Articles dialog, and opened as HTML.

## Changes for 20.0

- universalFeedParser is updated to 5.0.1, adding support for more feeds.

## Changes for 15.0

- Compatible with NVDA 2023.1.

## Changes for 14.0

- Fixed a bug that made impossible to add some feeds.

## Changes for 13.0

- The add-on cannot be used on secure screens.
- Feeds are managed from OPML files.
- Due to changes in the feeds management system, there are changes in the configuration file where the default feed is set. Please, use the Feeds dialog if you want to set it again.
- Your old text files used in previous versions will be automatically imported into the new OPML format when the add-on is started.
- The copy and restore feeds feature has been replaced with the ability to import from and save to OPML files.
- Non well-formed feeds can be processed before being added to make them compatible with the add-on.
- In the Read Feeds settings panel, a new option allows to show article dates on the List of articles dialog.

## Changes for 12.0

- Fixed a bug which made shortcuts for items of NVDA's tools menu don't work as expected.

## Changes for 11.0

- Compatible with NVDA 2021.1

## Changes for 10.0

- Added a button to open the selected feed as HTML in the default web browser.
- If a new feed cannot be created, this will be notified in an error dialog.
- Improved order and presentation of some articles.
- More feeds may be supported.
- When the feeds dialog is opened, the list of feeds will be focused instead of the search edit box.
- You can choose if the search edit box is placed after the list of feeds, useful to focus the list even when switching from another window without closing the Feeds dialog.
- Added a button to copy the feed address to clipboard from the feeds dialog.

## Changes for 9.0

- Requires NVDA 2019.3 or later.

## Changes for 8.0

- When the add-on is updated, feeds saved in the previous version of the add-on will be automatically copied to the new version, unless you prefer to import feeds saved in the main configuration folder of NVDA.
- When using the dialog to copy feeds, if the chosen folder is not named personalFeeds, a subfolder with this name will be created to prevent the deletion of directories containing important data, such as Documents or Downloads.

## Changes for 7.0

- The Feeds dialog includes a button to open a folder which may contain a backup of feeds.
- When using the edit box to filter feeds, if no results are found, the list of feeds and other controls are disabled, so that NVDA doesn't report "unknown" in the empty list.
- If the list of articles dialog can't be shown, for example due to errors in the feed, NVDA will raise an error, so that the feeds dialog can be used without restarting NVDA.

## Changes for 6.0

- When the default feed has been updated and it stops working due to server issues, the previous articles aren't deleted and can be read with the corresponding keystrokes.
- Fix regression: The default feed can be updated twice again.

## Changes for 5.0

- The articles list dialog has been enhanced.
- Compatible with NVDA 2018.3 or later (required).

## Changes for 4.0

- Added a button to open the selected feed from the Feeds dialog.

## Changes for 3.0

- The dialogs to manage feed files have been removed. Now their functionality is included in the Feeds dialog.
- The visual presentation of the dialogs has been enhanced, adhering to the appearance of the dialogs shown in NVDA.
- The default feed is saved on the NVDA's configuration. Therefore, it's possible to set different default feeds in configuration profiles.
- Requires NVDA 2016.4.

## Changes for 2.0

- Add-on help is available from the Add-ons Manager.

## Changes for 1.0

- Initial version.
