# Informe de unidad -- plantilla

Informe técnico acotado para el cierre de cada unidad

---

## Unidad: [1 mi primer aporte reproducible]
 

**Nombre:** [Victor Robles]

**Fecha:**  [12/10/2026]
**Tag de cierre:** (por ejemplo, `u1-completa`)
 

### Que se hizo

Hice el entregable de la tarea a partir de un fork del repositorio, haciendo los cambios dentro de una rama de git de la que hare pull request, lo primero que hice fue el forck de repo original, luego cree un nuevo codeespace, active el entorno, ejecute verificar_entorno.py, cree la rama u1/VictoRobles, tambien una carpeta con una copia de ejercicios.py que corregi, hice 6 commits y finalmente este informe. lo que se ejecuta es u1-tarea.yml, la revision con ruff, pytest y validar_entrega.py.

### Una decisión de diseño, explicada

Decidi hacer commit separados en vez de un solo comiit con el archivo ejercicio.py ya corregido, hice un commit para el automatico de ruff, otro para b006, otro para avisos restantes, otro para prueba, porque si algo salia mal podia ver exactamente que cambio es lo causo.

### Un problema que apareció

la primera vez que ejecute verifica_entorno.py decia FALTA para pytest, ruff y precommit. Mi terminal usaba el python general asi que ejecute source.venv/bin/activate, pytest y ruff aparecieron, el codespace si la habia instalado pero dentro del entorno. 

### Que harías distinto con mas tiempo  


