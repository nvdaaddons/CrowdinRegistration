# eMule #

*	Autores: Noelia, Chris, Alberto.

Esse complemento ajuda a melhorar a acessibilidade do eMule com o nVDA.
Ele também fornece comandos de teclado adicionais para movimentação em diferentes janelas e fornece informações úteis sobre o eMule.

Ele é baseado no complemento eMuleNVDASupport, desenvolvido pelo mesmo autor. Você deve desinstalar esse complemento antigo para usar este, pois ambos têm teclas e recursos comuns.

Testado no [eMule][1] 0.50a e 70b.

## Teclas de atalho

*	control+shift+h: Move o foco e o mouse para a barra de ferramentas principal.
*	control+shift+t: Lê a janela atual.
*	control+shift+n: Move o foco para o campo Nome na janela Localizar.
*	control+shift+p: Na janela Pesquisar, move o foco e o mouse para a lista de parâmetros de pesquisa ou para as opções do campo de edição.
*	control+shift+b: Move o foco para a lista na janela atual. Por exemplo, utilizável na janela Pesquisar, downloads na janela Transferir, etc.
*	control+shift+o: Move o foco para caixas de edição somente leitura na janela atual. Por exemplo, as mensagens recebidas do IRC, os servidores disponíveis, etc.
*	control+NVDA+f: Se o cursor estiver localizado em uma caixa de edição somente leitura, abrirá uma caixa de diálogo de localização para usar os comandos de pesquisa de texto disponíveis no NVDA.
*	control+shift+l: Move o objeto do navegador e o mouse para os cabeçalhos da lista atual.
*	control+shift+q: lê o primeiro objeto na barra de status; fornece informações sobre a atividade recente.
*	control+shift+w: Lê o segundo objeto da barra de status; contém informações sobre arquivos e usuários no servidor atual.
*	control+shift+e: Lê o terceiro objeto da barra de status; útil para saber a velocidade de UpLoad/DownLoad.
*	control+shift+r: Lê O quarto objeto da barra de status; informa sobre a conexão do eD2K e da rede Kad.
* Não atribuído: Alterna o uso de uma abordagem alternativa para ler os controles deslizantes.

## Gerenciando colunas. ##

Em uma lista, você pode mover o cursor entre as linhas e colunas usando alt+control+ setas.
Nesse complemento, os seguintes comandos principais também estão disponíveis:

*	nvda+control+1-0: Lê as 10 primeiras colunas.
*	nvda+shift+1-0: Lê as colunas 11 a 20.
*	nvda+shift+C: copia o conteúdo da última coluna lida para a área de transferência.


## Alterações para a versão 20.0.0
* Algumas caixas de edição e controles deslizantes são rotulados, graças ao projeto [labelAutofinderCore] (https://github.com/ABuffEr/labelAutofinderCore) desenvolvido por Alberto Buffolino, um dos autores desse complemento.
* Foi adicionado um comando (não atribuído) para alternar o uso de uma abordagem alternativa para ler os controles deslizantes (desativado por padrão).

## Alterações para a versão 7.0
* Compatibilidade com NVDA 2023.1

## Alterações para a versão 6.0
*	Requer o NVDA 2022.1 ou posterior.

## Alterações para a versão 5.0
*	Compatível com o NVDA 2021.1.

## Alterações para a versão 4.0 ##
*	Requer NVDA 2019.3 ou superiores.

## Alterações para a versão 3.0 ##
*	 Para pesquisar texto nas caixas de edição somente leitura, a caixa de diálogo localizar pode ser usada, como nvda+control+f para ativar a caixa de diálogo localizar.

## Alterações para a versão 2.0 ##
*	 A ajuda do add-on está disponível no Add-ons Manager.

## Alterações para a versão 1.2 ##
*	 Ao passar para as mensagens do IRC, o texto selecionado é relatado corretamente.
*	 O pressionamento de tecla usado para mover para a lista de resultados da pesquisa foi generalizado para poder mover o foco para qualquer lista disponível na janela atual.
*	 O comando usado para focalizar as mensagens de IRC foi generalizado para ser movido para qualquer caixa de edição somente leitura, possibilitando a revisão das informações de conexão na janela Servidores.
*	 Ao mover o mouse e o foco para a barra de ferramentas, em alguns casos ela era anunciada duas vezes. Isso foi corrigido.

## Alterações para a versão 1.1 ##
*	 Foi corrigido o erro no item do eMule no menu de ajuda do NVDA, quando o nome da pasta de configuração do usuário contém caracteres não latinos.
*	 Os atalhos agora podem ser reatribuídos usando a caixa de diálogo de entrada de gestos do NVDA.

## Alterações para 1.0 ##
*	 Versão inicial.

[1]: http://www.emule-project.net
