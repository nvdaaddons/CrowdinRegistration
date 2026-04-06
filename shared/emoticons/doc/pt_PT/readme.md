# Emoticons #

* Autores: Chris Leo, Noelia Ruiz Martínez, Mesar Hameed, Francisco Javier Estrada Martínez

Usando este extra, o texto falado que contém caracteres emoticon será substituído por uma descrição mais fácil de entender.

Por exemplo: a sequência “:)” será pronunciada como “smiley sorridente” ou, por exemplo, o NVDA reconhecerá o significado de cada emoji.

Você pode aproveitar os seguintes recursos:

## Inserir Emoticon ##

Às vezes, uma imagem vale mais que mil palavras: use os novos emojis para animar as suas mensagens instantâneas e mostrar aos seus amigos como se está a senti-rse.

Quando você não tiver certeza dos caracteres para um determinado smiley, este complemento permite selecioná-lo e inseri-lo em seu texto, como em um chat.

Pressione NVDA+I ou, no menu Ferramentas -> Emoticons > Inserir emoticon, para abrir uma caixa de diálogo com os emoticons ou emojis disponíveis.

Esta caixa de diálogo permite que você escolha um emoticon e visualize os emoticons que lhe interessam:

*	Um campo editável permite filtrar a pesquisa pelo emoticon desejado entre os emoticons disponíveis.
*	Através de um conjunto de botões de opção, você pode escolher visualizar apenas a categoria de emojis (alt+E), apenas a categoria de emoticons padrão (alt+s) ou todos os emoticons disponíveis (alt+A).
*	Na lista de emoticons (alt+L) são exibidos em três colunas, respectivamente: o nome do emoticon, o tipo de emoticon (emoticon padrão ou emoji) e o caractere correspondente.

Ao pressionar OK, os caracteres do emoticon escolhido serão copiados para a área de transferência, prontos para serem colados.

## Insira o símbolo ##

Esta caixa de diálogo permite escolher um dos símbolos disponíveis na caixa de diálogo Pontuação/pronúncia de símbolos do NVDA. Você pode usar a caixa de edição Filtro ou as teclas de seta para selecionar um item da lista de símbolos.

Se você deseja copiar vários símbolos, use o botão Adicionar para anexá-los à caixa de edição Símbolos a copiar.

Em seguida, pressione OK e o emoji ou símbolo selecionado, ou os símbolos contidos na caixa de edição mencionada, serão copiados para a área de transferência, prontos para serem colados.

## Associe gestos a símbolos ##

No menu do NVDA, submenu Preferências, caixa de diálogo Gestos de entrada, categoria Inserir símbolos ou Copiar símbolos, você pode configurar o NVDA para digitar símbolos por meio de gestos associados.

Você pode usar a caixa de edição do campo Editar para reduzir o número de símbolos apresentados, de modo que essa categoria possa ser expandida mais rapidamente.

## dicionário de Emoticons ##

O complemento Emoticons permite ter diferentes dicionários de fala usando perfis de configuração.

Isso significa que você pode criar ou editar um dicionário de fala específico para cada perfil personalizado.

No MENU do NVDA, em Preferências -> Dicionários de voz -> Dicionário de emoticons, você pode abrir uma caixa de diálogo para adicionar ou editar os emoticons disponíveis.

Salvando suas personalizações, as novas configurações de leitura dos emoticons serão aplicadas apenas ao perfil que você está editando no momento.

Por exemplo, você pode desejar que o NVDA fale emoticons personalizados apenas no programa XxChat, mas não em outros programas de bate-papo: você pode fazer isso criando um perfil para o aplicativo XxChat e atribuindo a ele um dicionário de fala no menu Dicionários de fala, opção Dicionário de emoticons. Veja abaixo as configurações de emoticons em relação aos perfis de configuração.

Você também pode exportar cada dicionário de voz personalizado clicando no botão “Salvar e exportar dicionário”: dessa forma, seus dicionários de voz serão salvos na pasta de configuração do usuário, na subpasta speechDicts/emoticons.

O nome e a localização exatos do arquivo do dicionário serão baseados no perfil de configuração de edição, que será exibido no título da caixa de diálogo Dicionário de Emoticons.

## Configurações de emoticons

No menu Preferências -> Configurações -> Emoticons, abre-se um painel para configurar a ativação dos seus dicionários de voz para cada perfil.

No painel de configurações de Emoticons, você pode escolher se o dicionário de fala deve ser ativado automaticamente quando o NVDA mudar para o perfil que você está editando no momento. Por padrão, ele está desativado na configuração normal do NVDA e em todos os seus novos perfis.

Além disso, é possível determinar se os emojis adicionais devem ser falados. Isso pode ser útil para preservar a pronúncia dos símbolos se os emojis estiverem incluídos na configuração do NVDA.

Se os símbolos inseridos usando gestos associados não forem pronunciados no seu sistema, mesmo quando o NVDA estiver configurado para pronunciar os caracteres digitados, você pode tentar ativar uma caixa de seleção para garantir a pronúncia dos símbolos inseridos.


Se desejar manter suas pastas de configuração organizadas, nesta caixa de diálogo também é possível escolher se os dicionários não utilizados (associados a perfis inexistentes) serão removidos do complemento quando ele for descarregado.

## Teclas de atalho

Estes são os comandos de teclado disponíveis por padrão. Você pode editá-los ou adicionar uma nova tecla para abrir o painel de configurações de Emoticons ou a caixa de diálogo Dicionário de Emoticons:

* NVDA+E: ativar/desativar emoticons falantes, alterna entre ler o texto tal como está escrito ou substituir os emoticons por descrições humanas.
* NVDA+I: exibe uma caixa de diálogo para selecionar o emoticon que você deseja copiar.
* Não atribuído: mostra um diálogo para seleccionar um símbolo do NVDA que deseja copiar.
* Não atribuído: abre uma mensagem navegável mostrando o símbolo onde o cursor de revisão está posicionado, para que toda a descrição possa ser revisada no modo de navegação.
* Não atribuído: abre uma mensagem navegável mostrando o símbolo onde o cursor está posicionado, para que toda a descrição possa ser revista no modo de navegação.

Observação: no Windows 10 e versões superiores, também é possível usar o painel de emojis integrado.

## Alterações para a versão 34.0.0

* Adicionada a capacidade de copiar para a área de transferência e colar símbolos individuais, útil quando os gestos associados aos scripts Inserir símbolos não funcionam.


## Alterações para a versão 33.0.0

* Corrigido bug em Salvar e exportar dicionários.
* Adicionados botões de copiar e fechar às mensagens apresentadas no modo de navegação.
* Ao usar comandos para inserir símbolos, eles podem ser pronunciados de acordo com a opção “pronunciar caracteres digitados”.

## Alterações para a versão 22.0.0 ##

* Requer NVDA 2023.2 ou posterior.

## Alterações para a versão 17.0 ##

* Adicionada a capacidade de associar gestos para digitar símbolos.
* Adicionada a capacidade de copiar vários símbolos ao mesmo tempo.

## Alterações para a versão 16.0 ##

* Compatibilidade com NVDA 2023.1

## Alterações para a versão 15.0 ##

* Requer NVDA 2022.1 ou posterior.
* Não pode ser usado no modo seguro.

## Alterações para a versão 14.0 ##

* Compatível com o NVDA 2021.1.

## Alterações para a versão 13.0 ##

* Corrigidos erros na caixa de diálogo Inserir Emoticon.
* Adicionado um diálogo para inserir um símbolo disponível na Pronúncia de Pontuação/Símbolo do NVDA.

## Alterações para a versão 12.0 ##

* Requer NVDA 2019.3 ou superiores.

## Alterações para a versão 11.0 ##

* Quando o extra é actualizado, os dicionários guardados na versão anterior do extra serão automaticamente copiados para a nova versão, a menos que prefira importar dicionários guardados na pasta principal de dicionários do NVDA.
* Ao mostrar o símbolo onde o cursor ou o cursor de revisão estão posicionados, as palavras Caractere e Substituição são usadas para distinguir entre o símbolo em si e sua descrição no modo de navegação, útil para usuários de voz.

## Alterações para a versão 10.0 ##

* Adicionados comandos para mostrar o símbolo onde o cursor de revisão ou o cursor de inserção estão posicionados. Os gestos para esses comandos podem ser atribuídos na caixa de diálogo Gestos de entrada, categoria Revisão de texto.

## Alterações para a versão 9.0 ##

* Adicionada a possibilidade de escolher se os emojis adicionais devem ser falados.
* Utilizou codificação apropriada para nomes de dicionários, corrigindo erros quando estes contêm determinados caracteres.
* O resumo traduzido do complemento é usado corretamente para o título apresentado na ajuda do complemento, acessível a partir do gerenciador de complementos.
* Adicionada uma nota mencionando o painel de emojis disponível no Windows 10.

## Alterações para a versão 8.0 ##

* Compatível com NVDA 2018.3 ou posterior (necessário).

## Alterações para a versão 7.0 ##

* A caixa de diálogo Configurações de ativação foi movida para um painel nas configurações do NVDA, de modo que o perfil atual será exibido no título da caixa de diálogo Configurações do NVDA.
* O menu Gerenciar Emoticons foi removido: agora, Inserir emoticon será encontrado no menu Ferramentas, e Personalizar Emoticons será exibido em Dicionários de fala, como Dicionário de Emoticons.
* Requer NVDA 2018.2 ou posterior.

## Alterações para a versão 6.0 ##

* Adicionado suporte para perfis de configuração.
* No NVDA 2017.4 ou posterior, as configurações e os dicionários personalizados serão alterados automaticamente de acordo com os perfis selecionados. Na versão 2017.3 ou anterior, você pode aplicar as alterações recarregando os plug-ins (pressionando Control+NVDA+F3).
* Se você optar por importar as configurações ao atualizar o complemento, os arquivos obsoletos (emoticons.ini e emoticons.dic) serão removidos ou adaptados a esta versão.

## Alterações para a versão 5.0 ##

* Adicionado suporte para emojis.
* Melhorias na caixa de diálogo Inserir Emoticon com um campo de filtro e botões de opção para escolher os emoticons exibidos.
* Utilização do guiHelper para a caixa de diálogo Configurações de ativação e a caixa de diálogo Inserir emoticon: requer NVDA 2016.4 ou versões superiores.

## Alterações para a versão 4.0 ##

* Se a caixa de diálogo Inserir smiley for aberta quando outra caixa de diálogo de configurações estiver ativa, o NVDA exibirá a mensagem de erro correspondente.


## Alterações para a versão 3.0 ##

* Na caixa de diálogo Personalizar emoticons, agora é possível especificar que um padrão só deve corresponder se for uma palavra inteira, de acordo com os dicionários de fala do NVDA 2014.4.


## Alterações para a versão 2.0 ##

* A ajuda sobre complementos está disponível no Gerenciador de Complementos.


## Alterações para a versão 1.1 ##

* Removido emoticon duplicado.
* Adicionadas algumas carinhas.

## Alterações para a versão 1.0 ##

* Versão inicial.
