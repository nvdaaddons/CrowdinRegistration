# nvda-tonys-enhancements
Esse complemento contém vários pequenos aprimoramentos no leitor de tela NVDA, cada um deles pequeno demais para merecer um complemento separado.

Esse complemento é compatível com o NVDA versão 2024.2 ou posterior

## Downloads

Instale a versão mais recente da loja de complementos do NVDA.

## Comandos de navegação de tabela aprimorados
* NVDA+Controle+dígito - pula para a 1ª/2ª/3ª/... 10ª coluna da tabela.
* NVDA+Alt+digito - pula para a 1ª/2ª/3ª/... 10ª linha da tabela.

## Cópia de tabelas para a área de transferência

Com os atalhos a seguir, você pode copiar toda a tabela, a linha atual ou a coluna atual de forma formatada, para que possa colá-la como uma tabela em editores de rich text, como o Microsoft Word ou o WordPad.
- NVDA+Alt+T - mostra o menu pop-up com opções para copiar a tabela ou parte dela.
Também há scripts separados para copiar tabelas, linhas, colunas e células, mas eles não têm atalhos de teclado atribuídos por padrão; os atalhos de teclado personalizados para eles podem ser atribuídos na caixa de diálogo InputGestures do NVDA.

## Histórico da área de transferência

A partir do NVDA v2024.4, o recurso integrado de histórico da área de transferência do Windows não funciona bem com o NVDA. Como substituto imediato, esse complemento oferece um recurso de histórico da área de transferência totalmente acessível. Ele está vinculado a `Windows+V` por padrão, portanto, substitui o recurso incorporado.

## Troca automática de idioma
Permite alternar automaticamente o idioma do sintetizador por conjunto de caracteres. A expressão regular para cada idioma pode ser configurada na janela de preferências desse complemento. Certifique-se de que seu sintetizador seja compatível com todos os idiomas de seu interesse. No momento, não há suporte para a alternância entre dois idiomas baseados em latim ou dois idiomas cujos conjuntos de caracteres sejam semelhantes.

## Comandos de busca rápida

A partir da versão v1.18, os comandos do QuickSearch foram movidos para o [complemento IndentNav] (https://github.com/mltony/nvda-indent-nav).

## Suprimir discurso indesejado "não selecionado" do NVDA

Suponha que você tenha algum texto selecionado em editores de texto. Em seguida, você pressiona uma tecla, como Home ou Seta para cima, que deve levá-lo a outra parte do documento. O NVDA anunciaria "não selecionado" e, em seguida, falaria a seleção anterior, o que, às vezes, pode ser inconveniente. Esse recurso impede que o NVDA fale o texto selecionado anteriormente em situações como essa.

## Pressionamentos de teclas dinâmicos

Você pode atribuir determinadas teclas para serem dinâmicas. Depois de pressionar essa tecla, o NVDA verificará se há atualizações na janela em foco e, se a linha for atualizada, o NVDA falará automaticamente. Por exemplo, determinados pressionamentos de tecla em editores de texto devem ser marcados como dinâmicos, como pular para o marcador, pular para outra linha e pressionamentos de tecla de depuração, como entrar/passar.

O formato da tabela dinâmica de pressionamentos de teclas é simples: cada linha contém uma regra no seguinte formato:
```
pressionamento de tecla appName
```
em que `appName` é o nome do aplicativo em que esse pressionamento de tecla é marcado como dinâmico (ou `*` para ser marcado como dinâmico em todos os aplicativos) e `keystroke` é um pressionamento de tecla no formato NVDA, por exemplo, `control+alt+shift+pagedown`.

Para descobrir o appName do seu aplicativo, faça o seguinte:

1. Mude para seu aplicativo.
2. Abra o console do NVDA Python pressionando NVDA+Shift+Z.
3. Digite `focus.appModule.appName` e pressione Enter.
4. Pressione F6 para ir para o painel de saída e encontrar o valor de appName na última linha.

## Exibição e ocultação de janelas

A partir da versão v1.18, os comandos mostrar/ocultar foram movidos para [complemento do Task Switcher] (https://github.com/mltony/nvda-task-switcher).

## Bip quando o NVDA está ocupado

Marque essa opção para que o NVDA forneça feedback de áudio quando o NVDA estiver ocupado. O fato de o NVDA estar ocupado não indica necessariamente um problema com o NVDA, mas é um sinal para o usuário de que os comandos do NVDA não serão processados imediatamente.

## Aplicação Ajuste de volume

Esse recurso permite ajustar o volume do NVDA e de outros aplicativos de forma independente. Os seguintes comandos estão disponíveis:

* NVDA+Ctrl+PageUp: Aumenta o volume do NVDA.
* NVDA+Ctrl+PageDown: diminui o volume do NVDA.
* NVDA+Alt+PageUp: Aumenta o volume de outros aplicativos.
* NVDA+Alt+PageDown: diminui o volume de outros aplicativos.
* Silenciar ou ativar o silêncio de outros aplicativos: Esse comando não tem um gesto padrão atribuído. Você pode atribuir um gesto personalizado na caixa de diálogo "Input Gestures" (Gestos de entrada) do NVDA.

## Microfone desligado

Esse complemento fornece um comando para alternar o microfone. Não há nenhum gesto atribuído a esse comando por padrão; você pode atribuir um gesto na caixa de diálogo "Input Gestures" (Gestos de entrada) do NVDA, se necessário.

## Divisão de som

Essa funcionalidade foi incorporada ao núcleo do NVDA e está disponível no NVDA v2024.2 ou posterior.

## Funções aprimoradas do mouse

* Alt+NumPadDivide: Aponta o cursor do mouse para o objeto atual e clica nele.
* Alt+NumPadMultiply: Aponte o cursor do mouse para o objeto atual e clique nele com o botão direito do mouse.
* Alt+NumPadDelete: Move o cursor do mouse para fora do caminho, para o canto superior esquerdo da tela. Isso pode ser útil para evitar que o mouse passe por cima de janelas indesejadas em determinados aplicativos.

A funcionalidade de rolagem da roda do mouse foi incorporada ao núcleo do NVDA e está disponível no NVDA v2024.3 ou posterior.

## Detecção do modo de inserção em editores de texto

Se essa opção estiver ativada, o NVDA emitirá um bipe quando detectar o modo de inserção em editores de texto.

## Bloqueio do pressionamento de tecla de inserção dupla

In NVDA pressing Insert key twice in a row toggles insert mode in applications. However, sometimes it happens accidentally and it triggers insert mode. Since this is a special keystroke, it cannot be disabled in the settings. This add-on provides a way to block this keyboard shortcut. When double insert is blocked, insert mode can stil be toggled by pressing NVDA+F2 and then Insert.

Essa opção está desativada por padrão e deve ser ativada nas configurações.

## Bloqueio do pressionamento duplo da tecla Caps Lock

In NVDA, when Caps Lock is set as an NVDA key, pressing it twice in a row toggles between uppercase and lowercase input modes. However, this can sometimes cause unintentional switching between these modes. Since this key’s behavior is unique and cannot be disabled through settings, this add-on offers a method to block this specific keyboard shortcut. When the double Caps Lock key press is blocked, you can still switch between uppercase and lowercase input modes by pressing NVDA+F2 followed by the Caps Lock key.

Essa opção está desativada por padrão e deve ser ativada nas configurações.

## Prioridade do sistema do processo NVDA

Isso permite aumentar a prioridade do sistema do processo do NVDA, o que pode melhorar a capacidade de resposta do NVDA, especialmente quando a carga da CPU é alta.

## Correção de um erro quando o foco fica preso na barra de tarefas ao pressionar Windows+Numbers

Esse recurso foi removido a partir da versão v1.18. Se precisar de uma funcionalidade de alternância de tarefas mais confiável, considere o uso do [complemento Task Switcher] (https://github.com/mltony/nvda-task-switcher).
