# src/merge_datasets.py
"""
Script principal para ejecutar:
1) limpiar UNICEF (CSV local)
2) obtener datos World Bank para los países relevantes
3) merge por country_code + year
4) guardar merged CSV en data/
"""

import pandas as pd
from clean_unicef_data import load_and_clean_unicef
from get_worldbank_api import fetch_worldbank_by_countries
import os

UNICEF_PATH = os.path.join("data","Datos_de_asistencia_escolar.csv")
OUTPUT_PATH = os.path.join("data","merged_unicef_worldbank.csv")

def main():
    print("1) Cargando y limpiando UNICEF...")
    unicef = load_and_clean_unicef(UNICEF_PATH)
    print(f"  UNICEF registros limpios: {len(unicef)}; países: {unicef['country_code'].nunique()}")

    # Seleccionar países: top 30 con menor asistencia (más críticos)
    top30 = unicef.sort_values("school_attendance", ascending=True).drop_duplicates("country_code").head(30)
    codes = top30['country_code'].tolist()
    print("2) Solicitando datos World Bank para top30:", codes)

    wb = fetch_worldbank_by_countries(codes)
    print(f"  World Bank registros descargados: {len(wb)}; países: {wb['country_code'].nunique()}")

    # merge
    merged = pd.merge(wb, unicef, on=['country_code','year'], how='inner', suffixes=('_wb','_unicef'))
    print(f"3) Registros tras merge: {len(merged)}; países en merged: {merged['country_code'].nunique()}")

    # limpiar y ordenar
    merged = merged[['country_code','country_name_wb','year','poverty_rate','school_attendance']].rename(columns={'country_name_wb':'country_name'})
    merged.to_csv(OUTPUT_PATH, index=False)
    print("4) Guardado:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
