# Informação do caracter

* Autor: Cyrille Bougot
* Compatibilidade com NVDA: 2022.3.3 e posterior

Este extra permite apresentar numa mensagem várias informações sobre um carater.
Também permite personalizar as informações comunicadas sobre um carácter quando se utilizam comandos de navegação do carácter do cursor de revisão ou múltiplas pressões do comando do carácter de revisão.

### Características

* Apresentar informações detalhadas sobre um carácter, por exemplo, nome Unicode, número, CLDR, nome do símbolo, etc.
* Essas informações podem ser exibidas no local do cursor de revisão ou no local do cursor do sistema.
* Personaliza a informação reportada quando se prime `numpad2`.
* Utilize a mesma informação personalizada quando mover o cursor de revisão por carácter.

## Comandos

* `Numpad2` (todos os layouts de teclado) ou `NVDA+.` (layout de laptop): quando pressionado 4 vezes, exibe informações sobre o caractere do objeto do navegador atual onde o cursor de revisão está situado. Este comando também pode ser personalizado nas configurações do add-on.
* Não atribuído: Apresenta uma mensagem com informações detalhadas sobre o carácter onde se encontra o cursor de revisão. Se não se sentir à vontade com o gesto de premir quatro vezes, pode utilizar este comando.
* Não atribuído: Apresenta uma mensagem com informações detalhadas sobre o carácter na posição do cursor (funciona apenas em locais onde existe um cursor).
* Não atribuído: Abre as definições do suplemento Informações sobre caracteres.

Para poderem ser utilizados, os comandos não atribuídos têm primeiro de ser atribuídos na caixa de diálogo Gestos de entrada.

## Informações pormenorizadas sobre uma personagem

As informações apresentadas incluem as seguintes secções:

* Unicode: informações da norma Unicode, ou seja, nome, nome CLDR, valor, bloco, etc.
* Tipo de letra MS, apenas para caracteres escritos com tipos de letra proprietários da Microsoft (Symbol, Wingding 1, 2, 3 e Webding): nome e informações sobre o carácter Unicode equivalente.
* Descrição do símbolo NVDA: informações que permitem compreender como a NVDA reporta a descrição do símbolo. A NVDA utiliza as informações das linhas superiores que contêm informações disponíveis para fornecer a descrição de um símbolo.
* Descrição do carácter NVDA: informação que permite compreender a forma como o NVDA reporta a descrição do carácter (por exemplo, "alfa" para "A"). O NVDA utiliza as informações das linhas superiores que contêm informações disponíveis para fornecer a descrição de um carácter.

As informações fornecidas na secção Unicode estão em inglês, uma vez que fazem parte da norma Unicode. Se existir uma tradução local para este suplemento, a informação também é fornecida juntamente com o inglês.

Relativamente à secção de descrição de símbolos do NVDA: Este add-on ainda não suporta dicionários de símbolos personalizados (introduzidos no NVDA 2024.4).
Já aparecem na lista "Opções utilizadas para calcular o símbolo", mas não na tabela propriamente dita.

## Configurações

Esta extensão tem a sua própria categoria na caixa de diálogo de definições do NVDA, onde pode configurar as seguintes opções.

### Ação para múltiplas pressões do comando de caracteres de revisão do relatório

As três caixas combinadas deste grupo permitem personalizar o que é reportado pelo comando de caracteres de revisão do relatório (`numpad2`) quando se utilizam duas, três ou quatro pressões.
Por predefinição, o NVDA apresenta a descrição do carácter na segunda pressão e o seu valor numérico, decimal e hexadecimal, na terceira pressão.
É possível alterar o que é reportado no carácter na posição do cursor de revisão após múltiplas pressões.
Por exemplo, pode indicar o seu nome CLDR em inglês na segunda pressão, o seu nome Unicode na terceira pressão e apresentar informações detalhadas sobre o mesmo na quarta pressão.

### Lembre-se destas acções durante a navegação de caracteres

Quando tiver reportado informação específica com o comando reportar carácter de revisão (`numpad2`) chamado várias vezes, pode querer continuar a reportar a mesma informação enquanto navega com o cursor de revisão (`numpad1` e `numpad3`).
Se selecionar esta opção, poderá fazê-lo, desde que navegue com o cursor de revisão por carácter logo após uma pressão múltipla de `numpad2`.

## Registro de Alterações

### Versão 3.5

* Implementação parcial do suporte para dicionários personalizados (introduzido no NVDA 2024.4).
* Suporte Unicode 16.0 corrigido: nomes de blocos para inglês e francês actualizados.
* Compatibilidade com NVDA 2025.1.

### Versão 3.4

* Foi corrigido um problema que impedia o NVDA de executar scripts seguros no ecrã de bloqueio.

### Versão 3.3

* Atualização para Unicode 16.0.

### Versão 3.2

* Correção: os caracteres para os quais apenas o nível de voz foi alterado já não impedem a apresentação do relatório de informações.

### Versão 3.1

* Foi corrigido um erro quando não havia nenhum valor a reportar para um carácter.
* Compatibilidade com o NVDA 2024.1.

### Versão 3.0

* Agora é possível configurar a propriedade relatada para o caractere sob o cursor de revisão ao pressionar várias vezes o `numpad2`. Opcionalmente, depois de ter usado múltiplos pressionamentos no `numpad2`, a última propriedade reportada também pode ser reportada desde que você navegue por caractere com o cursor de revisão (`numpad1` e `numpad3`).
* Prepara a compatibilidade com o NVDA 2024.1: suporte de voz a pedido.
* Resolve potenciais problemas de segurança relacionados com [GHSA-xg6w-23rw-39r8][4] ao utilizar o suplemento com versões mais antigas do NVDA. No entanto, recomenda-se a utilização do NVDA 2023.3.3 ou superior.

### Versão 2.6

* Atualização para Unicode 15.1.
* Adiciona suporte para Python 3.11 para preparar a compatibilidade com o NVDA 2024.1.
* Nota: A partir de agora, as actualizações de tradução deixarão de aparecer no registo de alterações.

### Versão 2.5

* Correção do erro de importação com as últimas versões alfa do NVDA, ciclo de desenvolvimento do NVDA 2023.2 (contribuição de Noelia Ruiz Martínez).

### Versão 2.4

* Traduções actualizadas.

### Versão 2.3

* Traduções actualizadas.

### Versão 2.2

* Removido o canal de desenvolvimento.
* Traduções actualizadas.

### Versão 2.1

* Foram corrigidos alguns erros que impediam a apresentação do relatório de informações sobre os caracteres quando eram utilizadas algumas opções.
* Traduções actualizadas.

### Versão 2.0


* Melhoria do relatório de informações sobre caracteres com informações sobre o símbolo NVDA e a descrição do carácter NVDA.
* Adicionado o suporte de caracteres compostos, por exemplo, letras com diacríticos que consistem em dois ou mais caracteres Unicode.
* Atualização para Unicode 15.0
* Dados actualizados do bloco francês.
* A visualização de informações de caracteres não é permitida no ecrã de bloqueio e nos ecrãs seguros.
* No ecrã de bloqueio do Windows, o script para rever o carácter atual pode agora funcionar normalmente (pressão simples, dupla ou tripla).
* Compatibilidade com o NVDA 2023.1.
* Deixa de ser compatível com o NVDA abaixo de 2022.3.3. A última versão compatível com o NVDA 2019.3 é a [1.8][3].
* Atualizar as localizações.

### Versão 1.8

* Atualização para Unicode 14.0.
* Compatibilidade com NVDA 2022.1.
* Deixa de ser compatível com o NVDA abaixo de 2019.3. A última versão compatível com o NVDA 2017.3 é a [1.7][2].
* O lançamento é agora efectuado graças a uma ação GitHub em vez de appVeyor.
* Atualizar as localizações.

### Versão 1.7

* Adicionadas traduções.

### Versão 1.6

* Compatibilidade com o NVDA 2021.1.

### Versão 1.5

* Preparar a compatibilidade com o NVDA 2021.1 (contribuição de Lukasz Golonka).
* Atualizar juntamente com as últimas modificações no modelo de suplemento.

### Versão 1.4

* Adicionado um script para obter informações sobre o carácter na posição do cursor (contribuição de Lukasz Golonka).
* Atualização para Unicode 13.0.

### Versão 1.3

* Corrige um erro com o NVDA 2019.3.


### Versão 1.2

* Fornece informações adicionais sobre caracteres escritos com tipos de letra Microsoft.


### Versão 1.1

* Actualizações para suportar as versões mais recentes do NVDA (Compatibilidade com Python 2 e 3)
* actualizações realizadas agora com o apveyor


### Versão 1.0

* Lançamento inicial.

[2]: https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]: https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]: https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
