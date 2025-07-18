# Clip Contents Designer #
*   Auteurs : Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Commandes clavier ##
*   NVDA+windows+c : Ajoute le texte sélectionné, les caractères braille Unicode
    qui représentent les objets MathML ou la chaîne qui a été marquée avec le
    curseur de revue, dans le presse-papiers.
*   NVDA+windows+x : Vide le contenu du presse-papiers.
*    Non assigné : Copier vers (ou couper depuis) le presse-papiers, avec la
     possibilité d'une demande de confirmation préalable.
*    Non assigné : affiche le texte du presse-papiers au format HTML en mode
     navigation, ou annonce si le presse-papiers est vide ou a un contenu qui ne
     peut pas être présenté dans un message consultable, par exemple si des
     fichiers ou des dossiers ont été copiés à partir de l'Explorateur Windows.
*    Non assigné : affiche le contenu textuel du presse-papiers sous forme de
     texte brut en mode navigation, ou annonce si le presse-papiers est vide ou
     a un contenu qui ne peut pas être présenté dans un message consultable, par
     exemple si des fichiers ou des dossiers ont été copiés à partir de
     l'explorateur Windows.

## Paramètres de Clip Contents Designer ##

Ce panneau est disponible depuis le menu de NVDA, le sous-menu Préférences, le
dialogue Paramètres.

Il contient les contrôles suivants :

* Tapez la chaîne à utiliser comme séparateur entre les contenus ajoutés au
  presse-papiers : Permet de définir un séparateur qui peut être utilisé pour
  trouver les segments de texte une fois que tout le texte ajouté est collé.
* Ajouter du texte au début du presse-papiers : il est également possible de
  choisir si le texte ajouté sera ajouté à la fin ou ajouté au début.
* Sélectionnez les actions qui nécessitent une confirmation préalable : Vous
  pouvez choisir, pour chaque action disponible, si elle doit être effectuée
  immédiatement ou après confirmation. Les actions disponibles sont : ajouter du
  texte, effacer le presse-papiers, émuler la copie et émuler la coupe.
* Demander une confirmation avant d'effectuer les actions sélectionnées quand :
  Vous pouvez sélectionner si les confirmations seront toujours demandées, juste
  si du texte est contenu dans le presse-papiers, ou si le presse-papiers n'est
  pas vide (par exemple si vous avez copié un fichier, pas du texte).
* Format to show the clipboard text as HTML in browse mode: If you're learning
  HTML markup language, you may choose Preformatted text in HTML or HTML as
  shown in a web browser, to have an idea of how your HTML code will be rendered
  by NVDA in a browser. The difference between preformatted and conventional
  HTML is that the first option will preserve consecutive spaces and line
  breaks, and the second one will compact them. For example, write some HTML
  tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and
  use clipContentsDesigner add-on to show the text in a browseable message.
* Nombre maximal de caractères lors de l'affichage du texte du presse-papiers en
  mode navigation : veuillez noter que l'augmentation de cette limite peut
  entraîner des problèmes si le presse-papiers contient de grandes chaînes de
  texte. La limite par défaut est de 100 000 caractères.
* Restaurer les valeurs par défaut.

Notes :

*   Les confirmations ne seront pas demandées lorsqu'une boîte de message de
    NVDA est toujours ouverte. Dans ce cas, les actions seront effectuées
    immédiatement.
* Emuler les commandes copier et couper signifie que, lorsque ces
  fonctionnalités sont activées, l'extension prendra le contrôle de contrôle+c
  et contrôle+x. Cela permettra de sélectionner si une confirmation doit être
  demandée avant d'effectuer les actions correspondant à ces frappes.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape key.

## Changements pour la version 40.0.0
* Ajout de la prise en charge du clavier hébreu.

## Changements pour la version 22.0.0
* Ajout d'un bouton pour restaurer aux paramètres par défaut dans le panneau de
  paramètres de l'extension.
* L'extension ne peut pas être exécuté en mode sécurisé.

## Changements pour la version 17.0
* Compatible avec NVDA 2023.1.

## Changements pour la version 16.0
* Nécessite NVDA 2022.1 ou ultérieur.

## Changements pour la version 15.0
* La commande pour ajouter du texte au presse-papiers est à nouveau présentée
  dans la boîte de dialogue des gestes de commande.
* Correction des gestes pour copier et couper avec le clavier persan, grâce à
  Mohammadhosein Ghezelsofla.

## Changements pour la version 14.0
* Compatible avec NVDA 2021.1.

## Changes for 13.0
* Correction d'un problème dans la disposition visuelle du panneau des
  paramètres, grâce à Cyrille Bougot.
* Documentation améliorée.
* Ajout d'une catégorie Clip Contents Designer pour attribuer des gestes
  d'entrée à toutes les commandes disponibles pour cette extension.
* Correction de bugs lors de l'utilisation de la copie d'émulation dans les
  navigateurs si le mode focus est actif.
* Vous pouvez assigner différents gestes pour afficher le contenu textuel du
  presse-papiers sous forme de texte brut ou formaté en HTML. Le Format pour
  afficher le texte du presse-papiers dans le panneau des paramètres a été
  modifié en conséquence, pour sélectionner les deux options disponibles pour le
  format HTML.

## Changements pour la version 12.0
* Correction de bogues lors de l'utilisation de l'émulation de copie dans les
  applications telles que LibreOffice Writer.

## Changements pour la version 11.0
* Il est maintenant possible d'ajouter du texte marqué avec le curseur de revue
  à l'aide de commandes standards de NVDA (NVDA+f9 et NVDA+f10). NVDA+Windows+f9
  n'est plus utilisé pour une meilleure intégration avec na nouvelle commande de
  NVDA NVDA+maj+f9.
* Nécessite NVDA 2019.3 ou ultérieur.

## Changements pour la version 10.0
* Correction d'un bogue dans le dialogue présentant le texte du presse-papiers,
  quand son titre contient des caractères non latins.
* Correction d'un bogue lors de l'utilisation des fonctionnalités d'émulation de
  copier ou couper avec une configuration clavier Arabe. Ceci a été corrigé par
  Abdel, ajouté comme auteur de l'extension.

## Changements pour la version 9.0

* Ajout de la possibilité de voir le contenu du presse-papiers en mode
  navigation.
* Ajout d'une option pour définir si une confirmation sera requise quand le
  presse-papiers n'est pas vide, par exemple si des fichiers ou dossiers sont en
  cours de copie.
* Nécessite NVDA 2018.4 ou ultérieur.

## Changements pour la version 8.0 ##

* Les paramètres de l'extension sont affichés dans la catégorie correspondante
  au dialogue Paramètres NVDA.
* Nécessite NVDA 2018.2 ou ultérieur.

## Changements pour la version 7.0

* Dans le dialogue pour configurer les fonctionnalités Émuler copier et Émuler
  couper à l'installation, si vous choisissez non, les commandes pour ces
  fonctionnalités seront supprimées, de sorte que vous pouvez restaurer le
  comportement normal pour contrôle+c et contrôle+x.

## Changements pour la version 6.0

*    Ajout d'options pour choisir si les actions disponibles doivent être
     effectuées après confirmation.
*   Ajout des commandes Émuler copier et Émuler couper, qui peuvent être
    affectées à partir de la boîte de dialogue Gestes de commandes.
*    Ajout d'une boîte de dialogue pour configurer les fonctionnalités Émuler
     copier et Émuler couper lors de l'installation. Cela permet d'ajouter les
     commandes Contrôle+c et Contrôle+x pour copier et couper et de demander si
     vous voulez remplacer le contenu du presse-papiers en appuyant sur ces
     combinaisons de touches.
*   Correction de la documentation pour le script_add (Windows+NVDA+c).

## Changements pour la version 5.0 ##

*   La présentation visuelle de la boîte de dialogue a été améliorée, en
    respectant l'apparence des dialogues présentés dans NVDA.
*   Nécessite NVDA 2016.4 ou ultérieur.

## Changements pour la version 4.0 ##
*   Les paramètres de l'extension sont gérés à partir de la configuration NVDA,
    afin que les profils standard puisse être utilisés pour enregistrer des
    séparateurs différents, et les paramètres n'ont pas besoin d'être copiés
    lors de l'importation pendant la réinstallation.
*   Il est maintenant possible de choisir si l’ajout de texte sera ajouté à la
    fin ou ajouté au début, en utilisant la case à cocher Ajouter du texte avant
    l'insertion des données à partir de la boîte de dialogue Paramètres de Clip
    Contents Designer.

## Changements pour la version 3.0 ##
*   La représentation en braille des objets MathML peut être ajoutée dans le
    presse-papiers si MathPlayer est installé.
*   Si aucun séparateur n'est définie, juste une seule ligne sera placée entre
    les segments du texte ajouté.
*   Un raccourci peut être assigné pour ouvrir le dialogue paramètres Clip
    Contents Designer.
*   Ajouté une case à cocher dans la boîte de dialogue paramètres, afin de
    choisir si le séparateur doit être copié pour être importé lors de la
    réinstallation de l'extension.

## Changements pour la version 2.0 ##
*   Les caractères Hindous peuvent être utilisés comme séparateur entre les
    contenus concaténés.

## Changements pour la version 1.0 ##
*   Première version.
