# Clip Contents Designer #
*   Autores: Noelia, Abdel.

This add-on is used to add text to the clipboard, which can be useful when you
want to join sections of text together ready for pasting. The clipboard content
can also be cleared an shown in browse mode.

## Órdenes de teclado ##
*   NVDA+windows+c: añade el texto seleccionado, los caracteres braille Unicode
    que representan objetos MathML, o la cadena que se haya marcado con el
    cursor de revisión, al portapapeles.
*   NVDA+windows+x: Limpia el contenido del portapapeles.
*    Sin asignar: copia hacia (o desde) el portapapeles, con la posibilidad de
     solicitar una confirmación previa.
*    Sin asignar: Muestra el texto del portapapeles como HTML en modo
     exploración, o lo anuncia si el portapapeles está vacío o si tiene
     contenidos que no se pueden presentar en un mensaje navegable, por ejemplo
     si se están copiando archivos o carpetas desde el Explorador de Windows.
*    Sin asignar: Muestra el texto del portapapeles como texto sin formato en
     modo exploración, o lo anuncia si el portapapeles está vacío o si tiene
     contenidos que no se pueden presentar en un mensaje navegable, por ejemplo
     si se están copiando archivos o carpetas desde el Explorador de Windows.

## Opciones de Clip Contents Designer ##

Este panel se encuentra disponible en el menú NVDA, submenú Preferencias,
diálogo Opciones.

Contiene los siguientes controles:

* Teclea la cadena que se usará como separador entre contenidos añadidos al
  portapapeles: permite configurar un separador que puede usarse para buscar los
  segmentos de texto una vez que se pega el texto completo.
* Añadir texto antes de los datos del portapapeles: también es posible elegir si
  el texto añadido irá antes o después.
* Elige las acciones que requieren confirmación previa: puedes elegir, en cada
  acción disponible, si se debe realizar inmediatamente o tras una confirmación.
  Las acciones disponibles son: añadir texto, limpiar portapapeles, emular copia
  y emular cortar.
* Cuándo solicitar confirmación antes de realizar las acciones seleccionadas:
  puedes elegir si se solicitarán confirmaciones siempre, sólo si el
  portapapeles contiene texto, o si el portapapeles no está vacío (por ejemplo
  si has copiado un archivo, y no texto).
* Format to show the clipboard text as HTML in browse mode: If you're learning
  HTML markup language, you may choose Preformatted text in HTML or HTML as
  shown in a web browser, to have an idea of how your HTML code will be rendered
  by NVDA in a browser. The difference between preformatted and conventional
  HTML is that the first option will preserve consecutive spaces and line
  breaks, and the second one will compact them. For example, write some HTML
  tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and
  use clipContentsDesigner add-on to show the text in a browseable message.
* Máximo de caracteres cuando se muestra el texto del portapapeles en modo
  exploración: por favor, ten en cuenta que aumentar este límite puede producir
  problemas si el portapapeles contiene grandes cadenas de texto. El límite
  predeterminado es de 100000 caracteres.
* Restaurar valores por defecto.

Notas:

*   No se solicitarán confirmaciones cuando siga abierto un cuadro de mensaje de
    NVDA. En esos casos, las acciones se realizarán inmediatamente.
* Las órdenes Emular copiar y Emular cortar significan que, cuando estas
  funciones están activadas, el complemento tomará el control de control+c y
  control+x. Esto permitirá elegir si se debería solicitar una confirmación
  antes de realizar las acciones correspondientes a estos atajos de teclado.

## Changes for 46.0.0
* NVDA will sanitize HTML in browseable messages.
* Added a button to close browseable messages, in addition to the Escape key.

## Cambios para 40.0.0
* Se añade soporte para el teclado hebreo.

## Cambios para 22.0.0
* Se ha añadido un botón para restaurar valores por defecto en el panel de
  opciones del complemento.
* El complemento no se puede ejecutar en modo seguro.

## Cambios para 17.0
* Compatible con NVDA 2023.1.

## Cambios para 16.0
* Requiere NVDA 2022.1 o posterior.

## Cambios para 15.0
* La orden para añadir texto al portapapeles se presenta de nuevo en el diálogo
  Gestos de entrada.
* Se corrigen los gestos de copiar y cortar en el teclado persa. Gracias a
  Mohammadhosein Ghezelsofla.

## Cambios para 14.0
* Compatible con NVDA 2021.1.

## Changes for 13.0
* Se ha corregido un problema en la disposición visual del panel de opciones,
  gracias a Cyrille Bougot.
* Se ha mejorado la documentación.
* Se ha añadido una categoría Clip Contents Designer para asignar gestos de
  entrada a todas las órdenes disponibles para este complemento.
* Se han corregido fallos al usar Emular copia en navegadores si el modo foco
  está activo.
* Puedes asignar diferentes gestos para mostrar el contenido textual del
  portapapeles como texto sin formato o formateado en HTML. Se ha modificado
  apropiadamente el formato en el que se muestra el texto del portapapeles en el
  panel de opciones para seleccionar las dos opciones disponibles para el
  formato HTML.

## Cambios para 12.0
* Se han corregido fallos al usar Emular copia en aplicaciones como Libre Office
  Writer.

## Cambios para 11.0
* Ahora es posible añadir texto marcado con el cursor de revisión usando órdenes
  estándar de NVDA (NVDA+f9 y NVDA+f10). Ya no se usa NVDA+windows+f9, para
  mejorar la integración con la nueva orden NVDA+shift+f9.
* Se requiere NVDA 2019.3 o posterior.

## Cambios para 10.0
* Corregido un problema en el diálogo usado para mostrar el texto del
  portapapeles, cuando su título contiene caracteres no latinos.
* Corregido un problema al usar las funciones de emular cortar y copiar con la
  distribución de teclado árabe. Esto ha sido corregido por Abdel, que se ha
  añadido como autor del complemento.

## Cambios para 9.0

* Añadida la posibilidad de mostrar el texto del portapapeles en modo
  exploración.
* Añadida una opción para elegir si se requerirá confirmación si el portapapeles
  no está vacío, por ejemplo, si se están copiando archivos o carpetas.
* Se requiere de NVDA 2018.4 o posterior.

## Cambios para 8.0 ##

* La configuración del complemento se muestra en la categoría correspondiente
  del diálogo Opciones de NVDA.
* Se requiere de NVDA 2018.2 o posterior.

## Cambios para 7.0

* En el diálogo para configurar las funciones Emular copiar y Emular cortar en
  la instalación, si eliges no, los comandos para estas características se
  eliminarán, de manera que puedas restaurar el comportamiento anterior de
  ctrl+c y ctrl+x.

## Cambios para 6.0

*    Se han añadido opciones para elegir si se deberían realizar las acciones
     disponibles tras una confirmación.
*   Añadidas órdenes para emular cortar y emular copiar, que se pueden asignar
    desde el diálogo Gestos de entrada.
*    Añadido un diálogo para configurar las funcionalidades Emular cortar y
     Emular copiar en la instalación. Esto permite añadir las órdenes control+c
     y control+x para copiar y cortar, y preguntar si quieres reemplazar los
     contenidos del portapapeles al pulsar estos atajos de teclado.
*   Corregida la documentación de script_add (Windows+NVDA+c).

## Cambios para 5.0 ##

*   La presentación visual del diálogo se ha mejorado, adhiriéndose a la
    apariencia de los diálogos mostrados por NVDA.
*   Se requiere de NVDA 2016.4 o posterior.

## Cambios para 4.0 ##
*   Ahora las opciones del complemento se gestionan desde la configuración de
    NVDA, así que pueden utilizarse perfiles estándar para guardar diferentes
    separadores, y no es necesario copiar las opciones para importarlas en la
    reinstalación.
*   Ahora es posible elegir si el texto añadido se anexará o se antepondrá,
    utilizando la casilla de verificacción Añadir texto antes de clip data desde
    el diálogo de opciones de Clip Contents Designer.

## Cambios para 3.0 ##
*   Se puede añadir al portapapeles la representación braille de objetos MathML
    si MathPlayer está instalado.
*   <Si no se a puesto un separador, se colocará una sola línea entre los
    segmentos de texto añadido.
*   Se puede asignar un atajo de teclado para abrir el diálogo de Opciones de
    Clip Contents Designer.
*   Añadida una casilla de verificación en el diálogho de opciones, para elegir
    si el separador debería copiarse para importarse cuando se reinstale el
    complemento.

## Cambios para 2.0 ##
*   Se pueden utilizar caracteres hindi como separador entre contenidos
    añadidos.

## Cambios para 1.0 ##
*   Versión inicial.
