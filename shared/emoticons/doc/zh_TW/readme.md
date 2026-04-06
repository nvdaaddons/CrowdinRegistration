# 表情符號

* 作者：Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez

使用此附加元件後，讀出包含表情符號字元的文字，將會被其更人性化的描述所取代。

例如：字元序列「:)」將會被讀為「smiling smiley」，或者例如 NVDA 將能識別每個表情符號的含義。

您可以利用以下功能：

## 插入表情 ##

有時一張圖勝過千言萬語：使用新的表情符號來活絡您的即時訊息，並讓您的朋友知道您的感受。

當您不確定某個特定表情的字元時，此附加元件可讓您選取並將其插入您的文字中，例如在聊天室裡。

按 NVDA+I，或從功能表的「工具」->「Emoticons」->「插入表情符號」，來開啟一個包含所提供之表情或表情符號的對話框。

此對話框允許您選擇表情符號並流覽您感興趣的表情符號：

*	一個編輯區可讓您在可用的表情符號中，篩選搜尋您想要的表情符號。
*	透過一組選擇鈕，您可以選擇只檢視表情符號類別 (alt+E)、只檢視標準 表情符號類別 (alt+S)，或檢視所有可用的表情符號 (alt+A)。
*	在表情符號清單 (alt+L) 中，內容分別以三欄顯示：表情符號名稱、表情符號類型 (標準表情符號或表情符號)，以及對應的字元。

當您按下確認後，所選表情符號的字元將會被複製至您的剪貼簿，可供貼上。

## 插入符號 ##

此對話框可讓您從 NVDA 的標點及符號讀音對話框中，選擇一個可用的符號。您可以使用篩選編輯區或方向鍵，從符號清單中選取一個項目。

若您想複製多個符號，請使用「加入」按鈕將它們附加至「複製的符號」編輯區。

然後，按下確認，所選的表情符號或符號，或是前述編輯方塊中包含的符號，將會被複製至您的剪貼簿，可供貼上。

## 為符號關聯手勢 ##

您可以從 NVDA 功能表、偏好子功能表、輸入手勢對話框、插入符號複製符號類別中，設定 NVDA 透過關聯的手勢來輸入符號。

您可以使用編輯區來減少所呈現的符號數量，以便能更快地展開此類別。

## 表情字典 ##

表情符號附加元件允許透過組態設定檔，來使用不同的語音字典。

這表示您可以為您的每個自訂設定檔，建立或編輯特定的語音字典。

從 NVDA 功能表 - >偏好 - >讀音字典 - >表情符號字典，您可以開啟一個對話框來新增或編輯可用的表情符號。

儲存您的自訂設定後，新的讀出表情符號設定將只會套用至您目前正在編輯的設定檔。

例如，您可能希望 NVDA 只在 XxChat 程式中讀出自訂的表情符號，而在其他聊天程式中則不要。您可以透過為 XxChat 應用程式建立一個設定檔，並從讀音字典功能表的表情符號字典選項中，為其指派一個讀音字典來達成。關於表情符號設定與組態設定檔的關係，請參閱下文。

您也可以透過按下儲存並匯出字典按鈕來匯出每個自訂的讀音字典。如此一來，您的讀音字典將會被儲存至您使用者組態資料夾下的 speechDicts/emoticons 子資料夾中。

字典檔案的確切名稱和位置，將取決於正在編輯的組態設定檔，此資訊會顯示在表情符號字典對話框的標題中。

## 表情符號設定 ##

從功能表的偏好 - >設定 - >表情符號，可開啟一個面板來為每個設定檔設定讀音字典的啟用狀態。

在表情符號設定面板中，您可以選擇當 NVDA 切換至您目前正在編輯的設定檔時，是否要自動啟用讀音字典。預設情況下，此功能在 NVDA 的一般組態及您所有的新設定檔中皆為停用。

此外，也可以決定是否要讀出附加元件的表情。若表情符號已包含在 NVDA 的組態中，此功能有助於保留符號的讀出方式。

若在您的系統中，即使 NVDA 已設定為讀出輸入字元，但透過關聯手勢插入的符號仍未被讀出，您可以嘗試啟用核取方塊，以確保插入的符號會被讀出。


若您希望保持組態資料夾的整潔，在此對話框中也可以選擇，當附加元件被解除安裝時，是否要從中移除未使用的字典 (與不存在的設定檔相關聯的字典)。

## 鍵盤指令： ##

以下為預設可用的按鍵指令，您可以編輯這些指令，或新增按鍵來開啟表情符號設定或表情字典對話框：

* NVDA+E：開啟/關閉讀出表情符號，可在「照原文朗與將表情符號替換為人性化描述後讀出之間切換。
* NVDA+I：顯示一個對話框，以選取您想複製的表情符號。
* 未指派：顯示一個對話框，以選取您想複製的 NVDA 符號。
* 未指派：開啟一個可瀏覽訊息，顯示檢閱游標所在位置的符號，以便能在瀏覽模式中檢視其完整描述。
* 未指派：開啟一個可瀏覽訊息，顯示游標所在位置的符號，以便能在瀏覽模式中檢視其完整描述。

請注意：在 Windows 10 及更新版本上，也可以使用內建的表情符號面板。

## 34.0.0 版的變更

* 新增了複製至剪貼簿及貼上個別符號的功能，在與「插入符號」腳本關聯的手勢無效時相當實用。


## 33.0.0 版的變更

* 修正了「儲存並匯出字典」的錯誤。
* 為以瀏覽模式呈現的訊息新增了複製和關閉按鈕。
* When using commands to insert symbols, they may be spoken according to the speak typed characters option.

## Changes for 22.0.0 ##

* Requires NVDA 2023.2 or later.

## Changes for 17.0 ##

* Added ability to associate gestures to type symbols.
* Added ability to copy various symbols at the same time.

## Changes for 16.0 ##

* Compatible with NVDA 2023.1.

## Changes for 15.0 ##

* Requires NVDA 2022.1 or later.
* Cannot be used in secure mode.

## Changes for 14.0 ##

* Compatible with NVDA 2021.1.

## Changes for 13.0 ##

* Fixed errors in Insert Emoticon dialog.
* Added a dialog to insert a symbol available in the Punctuation/symbol pronunciation of NVDA.

## Changes for 12.0 ##

* Requires NVDA 2019.3 or later.

## Changes for 11.0 ##

* When the add-on is updated, dictionaries saved in the previous version of the add-on will be automatically copied to the new version, unless you prefer to import dictionaries saved in the main dictionaries folder of NVDA.
* When showing the symbol where the caret or the review cursor are positioned, the words Character and Replacement are used to distinguish between the symbol itself and its description in browse mode, useful for speech users.

## Changes for 10.0 ##

* Added commands to show the symbol where the review cursor or caret are positioned. Gestures for these commands can be assigned from the Input gestures dialog, Text review category.

## Changes for 9.0 ##

* Added the possibility of choosing if add-on emojis should be spoken.
* Used appropiate encoding for dictionary names, fixing errors when they contain certain characters.
* The translated summary of the add-on is properly used for the title presented in add-on help, accessible from the add-on manager.
* Added a note mentioning the emoji panel available on Windows 10.

## Changes for 8.0 ##

* Compatible with NVDA 2018.3 or later (required).

## Changes for 7.0 ##

* The Activation settings dialog has been moved to a panel in NVDA settings, so that the current profile will be shown in the title of the NVDA settings dialog.
* The Manage Emoticons menu has been removed: now Insert emoticon will be found under the Tools menu, and Customize Emoticons will be shown under Speech dictionaries like Emoticons dictionary.
* Requires NVDA 2018.2 or later.

## Changes for 6.0 ##

* Added support for configuration profiles.
* In NVDA 2017.4 or later, the configuration settings and custom dictionaries will change automatically according with the selected profiles. In 2017.3 or earlier, you can apply changes by reloading plugins (pressing control+NVDA+f3).
* If you choose to import settings when updating the add-on, deprecated files (emoticons.ini and emoticons.dic) will be removed or adapted to this version.

## Changes for 5.0 ##

* Added support for emojis.
* Improvements for Insert Emoticon dialog with a filter field and radio buttons to choose displayed emoticons.
* Using guiHelper for Activation settings dialog and Insert Emoticon dialog: requires NVDA 2016.4 or higher versions

## Changes for 4.0 ##

* If the Insert smiley dialog is opened when another settings dialog is active, NVDA will show the corresponding error message.


## Changes for 3.0 ##

* In the Customize emoticons dialog, it is now possible to specify that a pattern should only match if it is a whole word, according to speech dictionaries of NVDA 2014.4.


## Changes for 2.0 ##

* Add-on help is available from the Add-ons Manager.


## Changes for 1.1 ##

* Removed duplicated emoticon.
* Added some smileys.

## Changes for 1.0 ##

* Initial version.
