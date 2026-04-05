# Lire les flux

- Auteurs: Noelia Ruiz Martínez, Mesar Hameed
- NVDA compatibility: 2018.3 to 2019.2
- Download [stable version][1]
- Download [development version][2]

This addon provides a straightforward  way to read feeds in Atom or RSS formats using NVDA.
Les flux ne seront pas actualisés automatiquement.
Ci-dessous, quand nous mentionnons des flux, nous entendons par là les flux RSS et ATOM.

## Installation or Update:

If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder,
when installing the current version, a dialog will ask if you want to upgrade or install.
Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.

## Commands:

### Read Feeds menu

You can access the Read Feeds submenu from the nvda menu, Tools submenu, where the following menu options are available:

#### Feeds...

Opens a dialog with the following controls:

- Filtrer par: Un champ d'édition pour rechercher des flux précédemment enregistrés.
- A list of the saved feeds.
- Liste des articles: Ouvre une boîte de dialogue qui présente la liste des articles du flux sélectionné. Sélectionnez l'article que vous souhaitez lire et appuyez sur Entrée ou sur le bouton Ouvrir la page web de l'article sélectionné pour ouvrir la page correspondante dans votre navigateur. Appuyez sur le bouton À propos de l'article pour ouvrir une boîte de dialogue affichant le titre et le lien de l'article sélectionné; à partir de cette boîte de dialogue, vous pourrez copier ces informations dans le presse-papiers.
- Ouvrir le flux: Ouvre le flux sélectionné dans l'application par défaut.
- Nouveau: Ouvre une boîte de dialogue avec un champ d'édition pour entrer l'adresse d'un nouveau flux. Si l'adresse est valide et que le flux peut être enregistré, son nom, basé sur le titre du flux, apparaîtra au bas de la liste des flux.
- Renommer: Ouvre une boîte de dialogue avec un champ d'édition pour renommer le flux sélectionné.
- Supprimer: Ouvre une boîte de dialogue pour supprimer le flux sélectionné après confirmation.
- Définir par défaut: Définit le flux sélectionné comme flux par défaut, afin que ses articles soient accessibles avec les commandes de NVDA.
- Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
- Fermer: Ferme la boîte de dialogue Flux.

##### Notes

- If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
- The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.

\####Copy feeds folder... ####

Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.

#### Restore feeds...

Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.

### Keyboard commands:

- Ctrl+Shift+NVDA+Espace : Annonce l'URL de l'article sélectionné. Un double appui ouvrira la page web.
- Ctrl+Shift+NVDA+8 : Actualise le flux sélectionné et annonce son titre le plus récent.
- Ctrl+Shift+NVDA+I : Annonce le titre et le lien du flux sélectioné. Appuyer deux fois copiera le titre et le lien associé dans le presse-papiers.
- Ctrl+Shift+NVDA+U : Annonce leCtrl+Shift+NVDA+U : Annonce le titre du flux précédent.
- Ctrl+Shift+NVDA+O : Annonce le titre du flux suivant.

## Notifications:

- When the title or URL have been copied.
- When unable to connect/refresh a feed, or the URL does not correspond to a valid feed.
- NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder.
- The title of the articles list dialog displays the selected feed name and number of items available.

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
- If needed, you can download the [last version compatible with NVDA 2017.3][3].

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

[1]: http://addons.nvda-project.org/files/get.php?file=rf
[2]: http://addons.nvda-project.org/files/get.php?file=rf-dev
[3]: http://addons.nvda-project.org/files/get.php?file=rf-o
