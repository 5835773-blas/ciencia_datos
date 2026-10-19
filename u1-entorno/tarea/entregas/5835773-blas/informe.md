# Informe de unidad 1

**Nombre:** Blas Antonio Zavala
**Tag de cierre:** `u1-completa`

## Entorno

[~90 palabras] El Codespace desde el navegador, Python 3.12.11, que
`verificar_entorno.py` termina en OK, y el comando clave que usaste
(`source .venv/bin/activate`).

## Flujo de Git

[~110 palabras] Fork de ubuntumb/ciencia_datos, rama `u1/5835773-blas`,
los 3 commits y POR QUÉ cada uno (estilo / bug+pruebas / informe), y que
el PR va al repo del curso tocando solo tu carpeta.

## Un problema que apareció

[~120 palabras] El mejor: la prueba `test_resumen_por_marca...` falló en
rojo con `AssertionError: {'Ford': 1000.0, 'Toyota': 500.0}` — el dict
por defecto compartía memoria entre llamadas — y cómo lo resolviste
(`acumulado=None` + `if acumulado is None`). Puedes mencionar en una
frase también que `pre-commit` faltaba en el entorno y lo instalaste.

## Reflexión

[~110 palabras] Qué aprendiste (por qué `is None` y no `== None`, por
qué los tests antes de dar por cerrado el código, qué harías distinto
con más tiempo).

## Ayudas externas

[~80 palabras] OBLIGATORIO: declara que usaste un asistente de IA para
guiarte paso a paso y que verificaste cada comando ejecutándolo tú en el
Codespace, más lo que consultaste (docs de ruff/pytest).