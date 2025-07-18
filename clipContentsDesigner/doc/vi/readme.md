# Clip Contents Designer #
*   Tác giả: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Các phím lệnh ##
*   NVDA+windows+c: thêm văn bản đã chọn vào bộ nhớ tạm, bao gồm các kí tự chữ
    nổi Unicode thể hiện dưới dạng đối tượng MathML hoặc các chuỗi được đánh dấu
    với con trỏ duyệt.
*   NVDA+windows+x: xóa nội dung bộ nhớ tạm.
*    Chưa gán: chép vào (hoặc cắt từ) bộ nhớ tạm với khả năng yêu cầu xác nhận
     trước đó.
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

Lưu ý:

*   Sẽ không có yêu cầu xác nhận khi có một hộp thông điệp của NVDA đang mở. Các
    trường hợp này, các hành động sd4 được thực hiện ngay lập tức.
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

## Các thay đổi cho bản 11.0
* Giờ đây đã có thể them các điểm đánh dấu văn bản với con trỏ duyệt với phím
  lệnh chuẩn của NVDA (NVDA+f9 và NVDA+f10). NVDA+windows+f9 không còn được dùng
  nữa, để cho một sự tích hợp mới tốt hơn với lệnh NVDA+shift+f9.
* Yêu cầu NVDA 2019.3 trở lên.

## Các thay đổi cho bản 10.0
* Sửa một lỗi trong hộp thoại dùng để hiển thị văn bản trong bộ nhớ tạm khi tên
  của nó có chứa các kí tự không phải chữ latin.
* Sửa một lỗi khi dùng các tính năng mô phỏng sao chép và cắt với kiểu bàn phím
  tiếng Ả Rập. Nó được sửa bởi Abdel, được xem như một tác giả của add-on.

## Các thay đổi cho bản 9.0

* Thêm khả năng hiển thị văn bản trong bộ nhớ tạm ở chế độ duyệt.
* Thêm tùy chọn để yêu cầu xác nhận khi bộ nhớ tạm không rỗng. ví dụ, nó đã chép
  các tập tin hay thư mục.
* Yêu cầu NVDA 2018.4 trở lên.

## Các thay đổi cho bản 8.0 ##

* Bản thiết lập của add-on được hiển thị ở phân loại thích hợp trong hộp thoại
  cấu hình NVDA.
* Yêu cầu NVDA 2018.2 trở lên.

## Các thay đổi cho bản 7.0

* Ở hộp thoại cấu hình tính năng mô phỏng cắt và sao chép trong khi cài đặt, nếu
  chọn không (no), dòng lệnh cho tính năng này sẽ bị gỡ bỏvà bạn có thể sử dụng
  cách thức bình thường cho lệnh control+c và control+x.

## Các thay đổi cho bản 6.0

*    Added options to choose if available actions should be performed after
     confirmation.
*   Added Emulate copy and Emulate cut commands, which could be assigned from
    the Input gestures dialog.
*    Added a dialog to configure the Emulate copy and Emulate cut
     functionalities at installation. This allows to add the control+c and
     control+x commands to copy and cut, and be asked if you want to replace the
     clipboard contents when pressing these keystrokes.
*   Fixed documentation for script_add (Windows+NVDA+c).

## Các thay đổi cho bản 5.0 ##

*   Cải thiện trình bày giao diện của hộp thoại, tuân theo cách trình bày của
    các hộp thoại khác của NVDA.
*   Yêu cầu NVDA 2016.4 trở lên.

## Các thay đổi cho bản 4.0 ##
*   Add-on settings are managed from NVDA configuration, so that standard
    profiles can be used to save different separators, and it's not needed to
    copy the settings for importing at reinstallation.
*   Now it's possible to choose if the added text will be appended or prepended,
    using the Add text before clip data check box from the Clip Contents
    Designer settings dialog.

## Các thay đổi cho bản 3.0 ##
*   Braille representation of MathML objects can be added to the clipboard if
    MathPlayer is installed.
*   Nếu không có dấu phân cách, sẽ chỉ có một dòng trắng được đặt giữa các phần
    văn bản được thêm vào.
*   A shortcut can be assigned to open the Clip Contents Designer settings
    dialog.
*   Added a check box in the settings dialog, for choosing if the separator
    should be copied to be imported when reinstalling the add-on.

## Các thay đổi cho bản 2.0 ##
*   Có thể dùng các kí tự chữ Hindi để phân cách giữa các phần nội dung đã thêm
    vào.

## Các thay đổi cho bản 1.0 ##
*   Phiên bản đầu tiên
