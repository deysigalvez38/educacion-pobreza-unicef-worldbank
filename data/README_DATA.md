# Data

## Archivos
- `Datos_de_asistencia_escolar.csv` : CSV original de UNICEF (ANAR) — Ajusted Net Attendance Rate (Primary)
- `merged_unicef_worldbank.csv` : Resultado del merge entre UNICEF y World Bank (por country_code y year)

Descripción:
Análisis de la relación entre pobreza extrema (Banco Mundial) y asistencia escolar primaria (UNICEF).

## Fuentes
- UNICEF: https://data.unicef.org/resources/dataset/education-statistics/
- World Bank: https://data.worldbank.org/indicator/SI.POV.DDAY (API)

## Notas
- Los datos de UNICEF fueron limpiados y normalizados a columnas: country_code (ISO3), country_name, year, school_attendance
- Los datos del Banco Mundial se obtienen por países (códigos ISO3) mediante la API y el indicador SI.POV.DDAY

Estructura recomendada del repositorio incluida en /project_files:
- data/
- notebooks/
- reports/
- src/
