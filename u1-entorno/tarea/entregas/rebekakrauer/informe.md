# Informe de unidad -- plantilla

Informe técnico acotado para el cierre de cada unidad

---

## Unidad: [U1. mi primer aporte reproducible]
 

**Nombre:**[Rebeka Rojas]

**Fecha:**[12/10/2026]

**Tag de cierre:** (por ejemplo, `u1-completa`)
 

### Que se hizo

Construí una entrega del trabajo a partir de un fork realizando los cambios dentro de una rama de la que hare pull request, el orden seguido fue: hacer el forck de repo original, abrir un codeespace, activar el entorno virtual(.venv), instalar pre-commit, ejecutar 'verificar_entorno.py, crear u1/miusuario a partir de main, una carpeta entregas/rebekrauer/ con una copia de ejercicios.py dentro, corregi dicha copia, 6 commits y el actual informe,me percate que no tenia test para el error principal y lo añadi, me refiero a resumen_por_marca.
Fnalmente lo que corre es u1-tarea.yml, la revision con ruff, pytest y validar_entrega.py.

### Una decisión de diseño, explicada

En la función descripcion_venta use except (KeyError, TypeError, ValueError) y no 'except:' ni 'except Exception'.Porque asi se atrapan solo los 3 fallos que se esperan para los que el 0 es una respuesta razonable(no tiene sale_price, el precio es None u otro que no se puede convertir, o el precio no es un numero). Cualquier otro error significa que algo más está mal, y es mejor que se vea que taparlo con un 0 silencioso.

### Un problema que apareció

Luego de activar el entorno y ejecutar verificar_entorno.py me salia que faltaba pre-commit, ejecute 'pip install -r requirements.txt' pero me retorno 'No such file' luego me percate que el repositorio usa pyproject.toml y uv.lock, no requirements.txt como decia en el README original que fue corregido, pero pre.commit tampoco esta en la lista de dependencias de pyproject.toml, asi que ejecute uv pip install pre-commit y luego la verificacion me retorno OK.

### Que harías distinto con mas tiempo  
Instalé pre-commit a mano porque el repositorio no lo declara, y ese paso no queda registrado para nadie más. Con más tiempo agregaria a la lista de dependencias del proyecto. No lo hice dentro de mi entrega porque el pull request solo puede tocar mi carpeta.

