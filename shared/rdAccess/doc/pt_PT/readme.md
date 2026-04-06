# RDAccess: Acessibilidade do ambiente de trabalho remoto

* Autores: [Leonard de Ruijter][1]
* Descarregar [última versão estável][2]
* Compatibilidade com NVDA: 2024.1 e posterior

O complemento RDAccess (Remote Desktop Accessibility) adiciona suporte para sessões remotas do Microsoft Remote Desktop, Citrix, Parallels RAS ou VMware Horizon ao NVDA.
Quando instalado no cliente e no servidor do NVDA, a fala e o braille gerados no servidor serão falados e apresentados em braille no computador cliente.
Isto permite uma experiência de utilizador em que a gestão de um sistema remoto é tão simples como a operação do sistema local.

## Características

* Suporte para Microsoft Remote Desktop (incluindo Azure Virtual Desktop e Microsoft Cloud PC), Citrix, Parallels RAS e VMware Horizon
* Saída de voz e braille
* Deteção automática de braille remoto utilizando a deteção automática de ecrã braille do NVDA
* Deteção automática de voz remota utilizando um processo de deteção dedicado que pode ser desativado na caixa de diálogo de definições do NVDA
* Suporte para cópias portáteis do NVDA em execução num servidor (configuração adicional necessária para Citrix)
* Suporte total para cópias portáteis do NVDA em execução num cliente (não são necessários privilégios administrativos adicionais para instalar o complemento)
* Várias sessões de cliente activas em simultâneo
* Ambiente de trabalho remoto disponível instantaneamente após o arranque do NVDA
* Capacidade de controlar definições específicas do sintetizador e do ecrã braille sem sair da sessão remota
* Capacidade de utilizar a voz e o braille a partir da sessão do utilizador ao aceder a ambientes de trabalho seguros

## Relatório de alterações

### Versão 1.6

* Suporte documentado e melhorado ao Parallels RAS.
* A versão mínima compatível do NVDA é agora a 2025.1. Removido o suporte para versões anteriores.
* Atualização da dependência do RdPipe.
* Adicionada a capacidade de configurar o nível de registo do RdPipe.
* Adicionado um visualizador para o registo RdPipe, disponível no painel de definições.
* Comportamento de desinstalação aprimorado (não gera mais erros ou remove o suporte Citrix quando o Citrix não está disponível).

### Versão 1.5

* Adicionar a capacidade de criar um relatório de diagnóstico de depuração através de um botão no painel de definições do RDAccess [#23](https://github.com/leonardder/rdAccess/pull/23).
* Suporte para ecrãs braille de várias linhas no NVDA 2025.1 e mais recente [#19](https://github.com/leonardder/rdAccess/pull/13).
* A versão mínima compatível do NVDA é agora a 2024.1. Removido o suporte para versões anteriores.
* Adicionadas notificações de ligação do cliente [#25](https://github.com/leonardder/rdAccess/pull/25).
* Atualização da dependência do RdPipe.
* Traduções actualizadas.

### Versão 1.4

* Nova versão estável.

### Versão 1.3

* Correção de gestos de visualização em braille avariados.

### Versão 1.2

* Utilize [Ruff](https://github.com/astral-sh/ruff) como formatador e linter. [#13](https://github.com/leonardder/rdAccess/pull/13).
* Foi corrigido um problema em que o NVDA no cliente gerava um erro ao colocar a fala em pausa no servidor.
* Corrigido o suporte para `winAPI.secureDesktop.post_secureDesktopStateChange`.
* Melhoria da inicialização do driver no servidor.

### Versão 1.1

* Adicionado suporte para o registo de dispositivos de estilo NVDA 2023.3 para deteção automática de ecrãs braille. [#11](https://github.com/leonardder/rdAccess/pull/11).
* Adicionado suporte para o ponto de extensão NVDA 2024.1 Alpha `winAPI.secureDesktop.post_secureDesktopStateChange`. [#12](https://github.com/leonardder/rdAccess/pull/12).

### Versão 1.0

Versão estável inicial.

## Começar

1. Instale o RDAccess numa cópia de cliente e de servidor do NVDA.
1. O sistema remoto deve começar a falar automaticamente usando o sintetizador de fala local. Caso contrário, na instância do NVDA no servidor, selecione o sintetizador de voz remoto na caixa de diálogo de seleção do sintetizador do NVDA.
1. Para utilizar braille, active a deteção automática de ecrã braille utilizando a caixa de diálogo de seleção de ecrã braille.

## Configuração

Após a instalação, o complemento RDAccess pode ser configurado utilizando a caixa de diálogo de definições do NVDA, acessível a partir do menu NVDA, selecionando Preferências > Definições...
Em seguida, selecione a categoria Ambiente de trabalho remoto.

Esta caixa de diálogo contém as seguintes definições:

### Ativar a acessibilidade do ambiente de trabalho remoto para

Esta lista de caixas de verificação controla o modo de funcionamento do add-on. Escolha entre:

* Conexões de entrada (servidor de área de trabalho remota): Escolha esta opção se a instância atual do NVDA estiver sendo executada em um servidor de área de trabalho remota.
* Ligações de saída (cliente de ambiente de trabalho remoto): Escolha esta opção se a instância atual do NVDA estiver sendo executada em um cliente de área de trabalho remota que se conecta a um ou mais servidores.
* Passagem do ambiente de trabalho seguro: Escolha esta opção se pretender utilizar o braille e a voz da instância do utilizador do NVDA ao aceder ao ambiente de trabalho seguro. Note que, para que isto funcione, é necessário disponibilizar o suplemento RDAccess na cópia do NVDA para o ambiente de trabalho seguro. Para tal, escolha "Utilizar definições atualmente guardadas durante o início de sessão e em ecrãs seguros (requer privilégios de administrador)" nas definições gerais do NVDA.

Para garantir um início sem problemas com o add-on, todas as opções estão activadas por defeito. No entanto, encorajamo-lo a desativar o modo de servidor ou de cliente, conforme apropriado.

### Recuperar automaticamente o discurso remoto após perda de ligação

Esta opção só está disponível no modo de servidor. Assegura que a ligação é restabelecida automaticamente quando o sintetizador de voz remoto está ativo e a ligação se perde, à semelhança da deteção automática do ecrã braille.

Esta opção está activada por predefinição. Recomenda-se vivamente que deixe esta opção activada se o servidor de Ambiente de Trabalho Remoto não tiver saída de áudio.

### Permitir que o sistema remoto controle as definições do condutor

Quando activada no cliente, esta opção permite-lhe controlar as definições do controlador (como a voz e o tom do sintetizador) a partir do sistema remoto. As alterações efectuadas no sistema remoto serão automaticamente reflectidas localmente.

### Persistir o suporte ao cliente ao sair do NVDA

Esta opção de cliente, disponível em cópias instaladas do NVDA, garante que a parte do cliente do NVDA é carregada no seu cliente de ambiente de trabalho remoto, mesmo quando o NVDA não está a ser executado.

Para utilizar a parte cliente do RDAccess, é necessário efetuar alterações no Registo do Windows.
O add-on garante que estas alterações são efectuadas no perfil do utilizador atual, não necessitando de privilégios administrativos.
Por conseguinte, o NVDA pode aplicar automaticamente as alterações necessárias quando é carregado e anular essas alterações quando sai do NVDA, garantindo a compatibilidade com versões portáteis do NVDA.

Esta opção está desactivada por predefinição. No entanto, se estiver a executar uma cópia instalada e for o único utilizador do sistema, é aconselhável ativar esta opção para um funcionamento suave ao ligar a um sistema remoto após o início do NVDA.

### Ativar o suporte predefinido para o ambiente de trabalho remoto

Esta opção, activada por predefinição, garante que a parte do cliente do RDAccess é carregada no cliente Microsoft Remote Desktop (mstsc) ao iniciar o NVDA.
Isto também é necessário para o VMware Horizon, o Parallels RAS, o Ambiente de Trabalho Virtual do Azure, etc.
As alterações efectuadas através desta opção serão automaticamente anuladas quando sair do NVDA, a menos que o suporte de cliente persistente esteja ativado.

### Ativar o suporte do Citrix Workspace

Esta opção, activada por predefinição, assegura que a parte do cliente do RDAccess é carregada na aplicação Citrix Workspace quando se inicia o NVDA.
As alterações efectuadas através desta opção serão automaticamente anuladas quando sair do NVDA, a menos que o suporte de cliente persistente esteja ativado.

Esta opção só está disponível nas seguintes condições:

* O Citrix Workspace está instalado. Note-se que a versão Windows Store da aplicação não é suportada devido a limitações da própria aplicação.
* É possível registar o RDAccess no contexto do utilizador atual. Depois de instalar a aplicação, tem de iniciar uma sessão remota uma vez para ativar esta opção.

### Notificar as alterações de ligação com

Esta caixa combinada permite-lhe controlar as notificações recebidas quando um sistema remoto abre ou fecha a ligação remota de voz ou braille.
Pode escolher entre:

* Desligado (Sem notificações)
* Mensagens (por exemplo, "Braille remoto ligado")
* Sons (NVDA 2025.1+)
* Mensagens e sons

Note que os sons não estão disponíveis nas versões do NVDA anteriores à 2025.1. Os sinais sonoros serão utilizados em versões mais antigas.

### Abrir relatório de diagnóstico

Este botão abre uma mensagem navegável com saída JSON contendo vários diagnósticos que podem eventualmente ajudar na depuração.
Ao [registar um problema no GitHub][4], poderá ser-lhe pedido que forneça este relatório.

## Instruções específicas da Citrix

Existem pontos importantes a ter em conta quando se utiliza o RDAccess com a aplicação Citrix Workspace:

### Requisitos do lado do cliente

1. A variante Windows Store da aplicação *não* é suportada.
1. Depois de instalar o Citrix Workspace, é necessário iniciar uma sessão remota uma vez para permitir que o RDAccess se registe. Isto acontece porque a aplicação copia as definições do sistema para as definições do utilizador durante a configuração inicial da sessão. Depois disso, o RDAccess pode registar-se no contexto do utilizador atual.

### Requisito do lado do servidor

No Citrix Virtual Apps and Desktops 2109, a Citrix activou a chamada lista de permissões de canais virtuais, restringindo canais virtuais de terceiros, incluindo o canal exigido pelo RDAccess, por predefinição.
Para obter mais informações, [consulte esta publicação no blogue da Citrix] (https://www.citrix.com/blogs/2021/10/14/virtual-channel-allow-list-now-enabled-by-default/).

Permitir explicitamente o canal RdPipe requerido pelo RDAccess ainda não foi testado. Por enquanto, é melhor desativar a lista de permissões completamente. Se o administrador do sistema tiver dúvidas, sinta-se à vontade para [abordar o problema aqui][3].

## Questões e contributos

Para reportar um problema ou contribuir, consulte [a página de problemas no Github][4].

## Componentes externos

Este complemento baseia-se no [RD Pipe][5], uma biblioteca escrita em Rust que suporta o cliente de ambiente de trabalho remoto.
O RD Pipe é redistribuído como parte deste add-on sob os termos da [versão 3 da GNU Affero General Public License][6].

[[!tag stable dev beta]]

[1]: https://github.com/leonardder/

[2]: https://www.nvaccess.org/addonStore/legacy?file=rdAccess

[3]: https://github.com/leonardder/rdAccess/issues/1

[4]: https://github.com/leonardder/rdAccess/issues

[5]: https://github.com/leonardder/rd_pipe-rs

[6]: https://github.com/leonardder/rd_pipe-rs/blob/master/LICENSE
