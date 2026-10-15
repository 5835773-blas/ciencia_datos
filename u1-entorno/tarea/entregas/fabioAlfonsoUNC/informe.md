# Informe de unidad

## Unidad U1: mi primer aporte reproducible

**Nombre:** Fabio Alfonso

**Fecha:** 15 de octubre de 2026

**Tag de cierre:** `u1-completa`

### Que se hizo

1. **Configuración del entorno:** Realicé el fork del repositorio `curso-datos` y levanté el entorno de desarrollo en un Codespace, validando las dependencias con `python u1-entorno/tarea/verificar_entorno.py` hasta obtener la salida `OK`.
2. **Estructura y control de versiones:** Creé la rama de trabajo `u1/fabioAlfonsoUNC` y copié el archivo base a `entregas/fabioAlfonsoUNC/ejercicio.py`.
3. **Refactorización y linter:** Utilicé `ruff` por primera vez en el proyecto para identificar violaciones de estilo y malas prácticas (`ruff check --fix` y `ruff format`), resolviendo manualmente las advertencias semánticas que el formateador no corrige por sí solo (corrección de nombres `CamelCase`, imports en desuso, excepciones desnudas y concatenaciones redundantes).
4. **Corrección de bugs e implementación de pruebas:** Identifiqué y corregí un bug crítico de asignación en `resumen_por_marca`. Desarrollé el archivo `test_ejercicio.py` con una suite de pruebas en `pytest` que cubre tanto el flujo nominal como casos borde.
5. **Cierre:** Commits atómicos documentando cada paso y preparación del pull request hacia el repositorio central del curso.


### Una decisión de diseño, explicada

**Sustitución de argumento mutable por defecto en `resumen_por_marca`**

El código original definía la función como `def resumen_por_marca(ventas, acumulado={}):`. En Python, los argumentos por defecto se evalúan una sola vez al cargar la definición de la función y no en cada invocación. Utilizar un objeto mutable (como un diccionario) provoca que múltiples llamadas sucesivas compartan la misma referencia en memoria, acumulando datos previos de forma residual (*state leakage*).

Decidí reemplazar la firma por `acumulado=None` y agregar una guarda al inicio:

```python
if acumulado is None:
    acumulado = {}
```
### Un problema que apareció
Al ser mi primera experiencia utilizando ruff, confié inicialmente en que cambiar la firma a acumulado=None para satisfacer la advertencia de argumento mutable era suficiente. Sin embargo, no me percaté de que el cuerpo de la función seguía asumiendo que acumulado era un diccionario indexable

#### Cómo se resolvió:
Inicialicé explícitamente acumulado = {} dentro de la función cuando el argumento recibido es None.

### USO DE IA
Utilize ia para mejorar la redaccion de este informe y tambien para aprender el uso de ruff porque es la primera vez que lo utilizo