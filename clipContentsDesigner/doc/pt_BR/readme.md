# Clip Contents Designer #
*   Autores: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Comandos de teclado ##
*   NVDA+windows+c: Acrescenta o texto selecionado, os caracteres braille
    Unicode que representem objetos MathML, ou a sequência (string) que foi
    marcada com o cursor de exploração, à área de transferência.
*   NVDA+windows+x: Apaga o conteúdo da área de transferência.
*    Não atribuído: copia (ou corta) a área de transferência, com a
     possibilidade de ser solicitada uma confirmação prévia.
*    Não atribuído: Mostra o texto da área de transferência como HTML no modo de
     navegação ou anuncia se a área de transferência está vazia ou possui
     conteúdos que não podem ser apresentados em uma mensagem navegável, por
     exemplo, se arquivos ou pastas foram copiados do Windows Explorer.
*    Não atribuído: Mostra o conteúdo textual da área de transferência como
     texto simples no modo de navegação ou anuncia se a área de transferência
     está vazia ou tem conteúdos que não podem ser apresentados em uma mensagem
     navegável, por exemplo, se arquivos ou pastas foram copiados do Windows
     Explorer.

## Configurações do Gestor do Conteúdo de Transferência ##

Este painel está disponível no menu do NVDA, submenu Preferências, diálogo de
Configurações.

Contém os seguintes controles:

* Digite a sequência de caracteres a ser usada como separador entre os conteúdos
  adicionados à área de transferência: Permite definir um separador que pode ser
  usado para localizar os segmentos de texto, uma vez que todo o texto
  adicionado é colado.
* Adicionar texto antes dos dados da transferência: Também é possível escolher
  se o texto adicionado será anexado ou prefixado.
* Selecione as ações que requerem confirmação prévia: Você pode escolher, para
  cada ação disponível, se ela deve ser realizada imediatamente ou após a
  confirmação. As ações disponíveis são: adicionar texto, limpar área de
  transferência, emular copiar e emular cortar.
* Solicitar confirmação antes de executar as ações selecionadas quando: Você
  pode selecionar se as confirmações serão solicitadas sempre, apenas se houver
  texto na área de transferência ou se a área de transferência não estiver vazia
  (por exemplo, se você copiou um arquivo, não um texto).
* Format to show the clipboard text as HTML in browse mode: If you're learning
  HTML markup language, you may choose Preformatted text in HTML or HTML as
  shown in a web browser, to have an idea of how your HTML code will be rendered
  by NVDA in a browser. The difference between preformatted and conventional
  HTML is that the first option will preserve consecutive spaces and line
  breaks, and the second one will compact them. For example, write some HTML
  tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and
  use clipContentsDesigner add-on to show the text in a browseable message.
* Número máximo de caracteres ao mostrar o texto da área de transferência no
  modo de navegação: Lembre-se de que aumentar este limite pode causar problemas
  se a área de transferência contiver grandes cadeias de texto. O limite padrão
  é 100000 caracteres.
* Restaurar os padrões.

Notas:

*   Confirmações não serão solicitadas quando uma caixa de mensagem do NVDA
    ainda estiver aberta. Nesses casos, as ações serão executadas imediatamente.
* Os comandos emular cópia e emular corte significam que, quando esses recursos
  estão ativados, o complemento assumirá o controle de control+c e control+x.
  Isso permitirá selecionar se uma confirmação deve ser solicitada antes de
  realizar as ações correspondentes a essas teclas.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape key.

## Mudanças na 40.0.0
* Adicionado suporte ao teclado hebraico.

## Mudanças na 22.0.0
* Foi adicionado um botão para restaurar os padrões no painel de configurações
  do complemento.
* O add-on não pode ser executado no modo seguro.

## Mudanças na 17.0
* Compatível com o NVDA 2023.1.

## Mudanças na 16.0
* Requer NVDA 2022.1 ou posterior.

## Mudanças na 15.0
* O comando para adicionar texto à área de transferência é novamente apresentado
  na caixa de diálogo de gestos de entrada.
* Corrigidos os gestos para copiar e cortar com o teclado persa, graças a
  Mohammadhosein Ghezelsofla.

## Mudanças na 14.0
* Compatível com o NVDA 2021.1.

## Changes for 13.0
* Corrigido um problema no leiaute visual do painel de configurações, graças a
  Cyrille Bougot.
* Documentação melhorada.
* Adicionada uma categoria Gestor do Conteúdo de Transferência para atribuir
  comandos — gestos — de entrada a todos os comandos disponíveis para este
  complemento.
* Falhas corrigidas ao usar emular cópia em navegadores se o modo de foco
  estiver ativo.
* Você pode atribuir diferentes gestos para mostrar o conteúdo textual da área
  de transferência como texto bruto ou formatado em HTML. O formato para mostrar
  o texto da área de transferência no painel de configurações foi modificado
  conformemente, para selecionar as duas opções disponíveis para o formato HTML.

## Mudanças na 12.0
* Falhas corrigidas ao usar emular cópia em aplicativos como o LibreOffice
  Writer.

## Mudanças na 11.0
* Agora é possível adicionar texto marcado com o cursor de exploração usando
  comandos padrão do NVDA (NVDA+f9 e NVDA+f10). NVDA+windows+f9 não é mais
  usado, por uma melhor integração com o novo comando NVDA+shift+f9.
* Requer NVDA 2019.3 ou posterior.

## Mudanças na 10.0
* Corrigida uma falha no diálogo usado para mostrar o texto da área de
  transferência, quando o título continha caracteres não latinos.
* Corrigido uma falha ao usar os recursos de emulação de corte e cópia com um
  layout de teclado árabe. Isso foi corrigido por Abdel, adicionado como um
  autor do complemento.

## Mudanças na 9.0

* Adicionada a possibilidade de mostrar o texto da área de transferência no modo
  de navegação.
* Foi adicionada uma opção para escolher se as confirmações serão necessárias se
  a área de transferência não estiver vazia, por exemplo, caso arquivos ou
  pastas foram copiados.
* Requer NVDA 2018.4 ou posterior.

## Mudanças na 8.0 ##

* As configurações do complemento são mostradas na categoria correspondente da
  caixa de diálogo Configurações do NVDA.
* Requer NVDA 2018.2 ou posterior.

## Mudanças na 7.0

* Na caixa de diálogo da instalação para configurar as funcionalidades Emular
  cópia e Emular corte, se você escolher não, os comandos para esses recursos
  serão removidos, para que você possa restaurar o comportamento normal para
  control+c e control+x.

## Mudanças na 6.0

*    Foram adicionadas opções para escolher se as ações disponíveis devem ser
     executadas após a confirmação.
*   Adição dos comandos Emular cópia e Emular corte, que podem ser atribuídos na
    caixa de diálogo Gestos de entrada.
*    Adicionada uma caixa de diálogo para configurar as funcionalidades Emular
     cópia e Emular corte na instalação. Isso permite adicionar os comandos
     control+c e control+x para copiar e cortar, e ser perguntado se você deseja
     substituir o conteúdo da área de transferência ao pressionar essas teclas.
*   Corrigida a documentação do script_add (Windows+NVDA+c).

## Mudanças na 5.0 ##

*   A apresentação visual do diálogo foi aprimorada, aderindo à aparência dos
    diálogos mostrados no NVDA.
*   Requer NVDA 2016.4 ou posterior.

## Mudanças na 4.0 ##
*   As configurações do complemento são gerenciadas a partir da configuração do
    NVDA, de modo que os perfis padrão podem ser usados para salvar separadores
    diferentes, e não é necessário copiar as configurações para importação na
    reinstalação.
*   Agora é possível escolher se o texto será acrescentado depois ou antes do
    que já está lá, usando a caixa de seleção acrescentar texto antes dos dados,
    no diálogo de opções do gestor de conteúdo da área de transferência.

## Mudanças na 3.0 ##
*   Representações braille de objetos MathML podem ser acrescentadas à área de
    transferência se o MathPlayer estiver instalado.
*   Caso nenhum separador seja configurado, apenas uma linha será colocada entre
    os segmentos de texto acrescentados.
*   Uma tecla de atalho pode ser atribuída para abrir o diálogo de opções do
    gestor do conteúdo de transferência.
*   Adicionada uma caixa de seleção ao diálogo de opções, para escolher se o
    separador deve ser copiado para ser importado ao reinstalar o complemento.

## Mudanças na 2.0 ##
*   Caracteres hindi podem ser usados como o separador entre conteúdos
    acrescentados.

## Mudanças na 1.0 ##
*   Versão inicial.
