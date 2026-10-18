Se crea el usuario dianamorefacet para realizar el trabajo
Se crea un fork del proyecto ciencia_datos
Se crea la rama u1/dianamorefacet dentro del proyecto fork
Se realiza el trabajo utilizando el codespace de github
Se inicia el entorno de trabajo, se activa el virtualenv ".venv"
Se crean los directorios entregas/dianamorefacet dentro del directorio u1-entorno/tarea
Se copia el archivo ejercicio.py e informe.md dentro del nuevo directorio de entregas
Se corre la funcion "ruff check --fix" y "ruff format" sobre el archivo ejercicio.py dentro del directorio de entregas
Realizado el formateo y fix automático se procede a corregir el archivo según las recomendaciones de Ruff
- Se quita la linea 23 del archivo donde se inicializa la variable total, ya que esta nunca se utiliza
- Se corrigen las comparaciones con valores nulos ("None") reemplazando "==" por "is"
- Se corrige "except" genérico en línea 41 por "except ValueError" que es la única excepción esperada al intentar convertir un valor no numérico a numérico
- Se corrige la función "resumen_por_marca" para que el valor por defecto del parámetro "acumulado" sea "None" en vez de "{}", ya que see detecta un error al intentar llamar varias veces a la función sin enviar el parámetro "acumulado"
Se crea el archivo test_ejercicio.py dentro del directorio entregas
Se crea una función de prueba para cada función del ejercicio
Para la función "resumen_por_marca", donde se identifica un caso de borde se crea una función de prueba adicional donde se realizan varias llamadas a la función sin pasar el parámetro "acumulado"



# Informe de unidad -- plantilla

Informe técnico acotado para el cierre de cada unidad

---

## Unidad: [numero y nombre]
 

**Nombre:**

**Fecha:**

**Tag de cierre:** (por ejemplo, `u1-completa`)
 

### Que se hizo

Que construiste, en que orden, que corre al final.

### Una decisión de diseño, explicada

Elegí una decisión concreta que tomaste durante la unidad (por ejemplo,  "por que append y no merge", "por que dos dimensiones y no cuatro", "por que el schedule queda apagado") y explica por que la tomaste, no solo
que la tomaste.

### Un problema que apareció

Algo que no funciono a la primera, y como lo resolviste. Si no encontraste ningún problema real, es una buena señal de que no probaste lo suficiente puedes volver a intentarlo antes de dar la unidad por cerrada. 

### Que harías distinto con mas tiempo  
Opcional, pero valorado. Una limitación que ves en tu propia entrega.

