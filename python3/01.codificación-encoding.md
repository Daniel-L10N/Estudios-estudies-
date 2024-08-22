## 2.2.1. Codificación del código fuente
- De forma predeterminada, los archivos fuente de Python se tratan como codificados en UTF-8. En esa codificación, los caracteres de la mayoría de los idiomas del mundo se pueden usar simultáneamente en literales, identificadores y comentarios, aunque la biblioteca estándar solo usa caracteres ASCII para los identificadores, una convención que debería seguir cualquier código que sea portable.Para mostrar todos estos caracteres correctamente, tu editor debe reconocer que el archivo es UTF-8, y debe usar una fuente que admita todos los caracteres del archivo.

- Para declarar una codificación que no sea la predeterminada, se debe agregar una línea de comentario especial como la primera línea del archivo. La sintaxis es la siguiente:

# -*- coding: encoding -*-
donde encoding es uno de los codecs soportados por Python.

Por ejemplo, para declarar que se utilizará la codificación de Windows-1252, la primera línea del archivo de código fuente debe ser:

# -*- coding: cp1252 -*-
Una excepción a la regla de primera línea es cuando el código fuente comienza con una linea UNIX «shebang». En ese caso, la declaración de codificación debe agregarse como la segunda línea del archivo. Por ejemplo:

#!/usr/bin/env python3
# -*- coding: cp1252 -*-