Informe de unidad 1

Nombre: Blas Antonio Zavala

Tag de cierre: u1-completa

Entorno

Trabajé en un Codespace, que es el entorno de desarrollo que GitHub abre en el navegador sobre un contenedor Docker. No instalé Python ni git en mi computadora.

El repositorio trae un archivo .devcontainer que, al crearse el Codespace, ejecuta uv sync --all-groups y prepara el entorno virtual del proyecto. Antes de tocar código lo activé con source .venv/bin/activate, y el prompt cambió y mostró (curso-analisis-datos).

Después ejecuté python u1-entorno/tarea/verificar_entorno.py, que revisa la versión mínima de Python, git y las herramientas del curso. En mi caso uso Python 3.12.11, pytest 9.1.1 y ruff 0.16.10.

La primera verificación falló: dijo que pre-commit NO ENCONTRADO. Lo instalé con uv pip install pre-commit y la segunda vez todo salió OK.

Para mí este paso es lo más importante de la unidad: sin un entorno verificado, el trabajo no se puede reproducir.

Flujo de Git

Empecé haciendo un fork de ubuntumb/ciencia_datos a mi cuenta. Es mi propia copia, donde puedo probar cosas sin romper el repositorio del curso.

Dentro del Codespace creé la rama de la unidad con git switch -c u1/5835773-blas. Vi que uv.lock aparecía modificado por la instalación del entorno, así que lo restauré con git restore uv.lock para empezar con el árbol limpio. El pull request solo debe tocar mi carpeta.

Hice cuatro commits pequeños en lugar de uno grande:

La corrección de estilo que pide la guía.
El bug real, junto con las pruebas que lo detectan.
El informe.
La ampliación del informe hasta el rango pedido.

Los commits cortos, con mensajes que explican el porqué, permiten revisar cada decisión por separado y volver atrás sin perder el resto.

La entrega es un pull request al repositorio del curso, con base en main y comparado contra mi rama.

Un problema que apareció

El problema más interesante no lo encontró ruff, sino una prueba. La función resumen_por_marca tenía acumulado={} como valor por defecto. Python crea ese diccionario una sola vez, cuando define la función, y lo reutiliza en todas las llamadas.

Primero escribí la prueba que lo muestra: al llamar la función dos veces, el primer resultado incluía las ventas de la segunda. Pytest falló con este mensaje: AssertionError: {'Ford': 1000.0, 'Toyota': 500.0} == {'Ford': 1000.0}.

La solución fue el patrón habitual: usar acumulado=None y crear el diccionario dentro de la función con if acumulado is None. Así cada llamada recibe un diccionario nuevo y la función hace lo que dice su docstring.

Reflexión

Antes de esta unidad pensaba que los linters servían para regañar. Ahora los leo como una lista de pistas:

N802 me llevó a usar nombres en snake_case.
E711 me llevó a comparar con is None.
F841 me llevó a borrar código que no se usa.
E722 me llevó a evitar el except sin tipo de error.

Mi decisión favorita fue separar los cambios de estilo de los cambios de lógica en commits distintos.

Si tuviera más tiempo, ampliaría las pruebas con casos límite, como precio negativo, venta sin campos y fecha inválida. También escribiría siempre la prueba antes que la corrección, como pasó aquí: ver el error en rojo de pytest fue lo que de verdad me hizo entender el bug.

Ayudas externas

Usé un asistente de IA, opencode, como guía. Me explicó los conceptos de git, me sugirió comandos y me ayudó a interpretar los errores de ruff y de pytest.

Todos los comandos los escribí y ejecuté yo en el Codespace, y revisé cada salida antes de seguir. Este informe lo redacté con base en mi propia experiencia durante la sesión.

También consulté la documentación de ruff sobre las reglas de estilo y la de pytest sobre cómo ejecutar pruebas. Declaro este uso según las reglas del curso.

Qué cambié:

Dividí las frases largas en frases más cortas.
Cambié palabras formales por otras más directas (“el corazón de la unidad” → “lo más importante para mí”).
Puse en lista los cuatro commits y las reglas de ruff para que se lean más fácil.
Eliminé la frase repetida sobre pre-commit en la sección del problema.