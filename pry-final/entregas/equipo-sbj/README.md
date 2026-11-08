# Equipo-sbj - Pipeline Minimercado

## Reproducción
```bash
# Generar datos
python generar_datos.py

# Ingesta dlt
python pipeline.py

# dbt
dbt --project-dir dbt_project build
dbt --project-dir dbt_project docs generate
dbt --project-dir dbt_project docs serve

# Orquestación
dagster dev -f orchestration/definitions.py

# Pruebas
pytest test_pipeline.py
```

## Integrantes
* Integrante 1: Ingeniería de Datos
* Integrante 2: Analytics Engineering
* Integrante 3: Orquestación & QA
