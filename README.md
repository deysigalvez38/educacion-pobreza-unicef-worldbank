📘 Educación y Pobreza: UNICEF + World Bank Data Project
👩‍💻 Autora: Deysi Galvez / Borja Rubio
Proyecto individual — Ironhack Data Analytics Bootcamp

📌 1. Introducción
Este proyecto analiza la relación entre:

Pobreza extrema global
Indicador del Banco Mundial: SI.POV.DDAY (personas con menos de $2.15/día)

Asistencia escolar primaria
Dataset UNICEF: Adjusted Net Attendance Rate (ANAR)


🎯 Objetivo: Evaluar si la pobreza económica está relacionada con la asistencia escolar infantil y detectar los países más vulnerables.

🎯 2. Hipótesis

H1: Mayores niveles de pobreza → menor asistencia escolar.
H2: África Subsahariana concentra las cifras más críticas.
H3: Existe correlación negativa entre pobreza y asistencia escolar.

🗂️ 3. Fuentes de Datos
✔ Banco Mundial (API)

Indicador: SI.POV.DDAY
Formato: JSON vía API
Años: 2010–2022

Documentación: https://data.worldbank.org/


✔ UNICEF (CSV)

Indicador: Adjusted Net Attendance Rate (ANAR), Primary

Descargado desde dataset oficial de UNICEF:
https://data.unicef.org/resources/dataset/education-statistics/

🔧 4. Metodología
🔹 a) Recopilación de datos

World Bank → llamado API usando requests
UNICEF → archivo CSV procesado manualmente

🔹 b) Limpieza y normalización
Se aplicaron técnicas como:

Normalización de columnas
Conversión numérica
Eliminación de nulos
Filtrado de códigos ISO
Homologación de años
Eliminación de duplicados
Unificación de nombres de país

🔹 c) Fusión final
La unión se realizó usando:
country_code + year

🔹 d) Análisis exploratorio (EDA)
Incluyó:


Ranking de países críticos
Cálculo de correlación
Gráficos de dispersión
Análisis por regiones

📊 5. Resultados principales
🔥 1. Países con menor asistencia escolar (más vulnerables)
Los más críticos son:

Tanzanía
Mozambique
Níger
Chad
Liberia
Sudán del Sur
República Centroafricana


📉 2. Relación pobreza ↔ educación
Se encontró una correlación negativa, confirmando que:

A mayor pobreza → menor asistencia escolar.

🌍 3. Patrón regional
África Subsahariana concentra los peores indicadores.

🧪 6. Conclusiones
✔ Existe una fuerte relación pobreza–educación.
✔ La brecha es especialmente grande en África.
✔ La fusión de datos es clave para entender realidades globales.
✔ La hipótesis H1 y H2 quedan confirmadas.

🤔 7. Preguntas futuras


¿Cómo cambia la asistencia escolar cuando baja la pobreza?
¿Hay políticas educativas que mitiguen la pobreza infantil?
¿Cómo afectan conflictos armados a estos indicadores?
¿Qué ocurre con asistencia preescolar y secundaria?



🧰 8. Estructura del proyecto
educacion-pobreza-unicef-worldbank/
│
├── data/
│   ├── Datos_de_asistencia_escolar.csv
│   ├── merged_unicef_worldbank.csv
│
├── notebooks/
│   └── analisis_educacion_pobreza.ipynb
│
├── src/
│   ├── get_worldbank_api.py
│   ├── clean_unicef_data.py
│   ├── merge_datasets.py
│   └── analysis_functions.py
│
├── README.md
└── requirements.txt


🔗 9. Enlaces del proyecto
📁 Repositorio GitHub
https://github.com/deysigalvez38/educacion-pobreza-unicef-worldbank

📌 Tablero Kanban / Trello
(agregar enlace aquí)
🎥 Presentación Google Slides
(agregar enlace aquí)

🙌 Gracias por leer este proyecto
Este análisis combina data wrangling, APIs y análisis exploratorio para comprender cómo la pobreza afecta la educación infantil a nivel global.