# src/clean_unicef_data.py
"""
Funciones para limpiar el CSV de UNICEF (Adjusted Net Attendance Rate).
Uso:
    from clean_unicef_data import load_and_clean_unicef
    df = load_and_clean_unicef("data/Datos_de_asistencia_escolar.csv")
"""

import pandas as pd
from typing import Optional

COMMON_COLS = [
    'ISO3','ISO_3','Country Code','Country code','country_code',
    'Country','country','Country Name','country_name',
    'Year','year','Time period','time_period',
    'Total','Adjusted net attendance rate (%)','Value','value','school_attendance'
]

def identify_columns(df: pd.DataFrame) -> dict:
    """Intenta mapear columnas encontradas a las que necesitamos."""
    cols = {c.lower(): c for c in df.columns}
    mapping = {}
    # country_code
    for cand in ['iso3','iso_3','country code','country_code','countrycode','geoarea','code']:
        if cand in cols:
            mapping['country_code'] = cols[cand]; break
    # country_name
    for cand in ['country name','country','country_name','countryname']:
        if cand in cols:
            mapping['country_name'] = cols[cand]; break
    # year
    for cand in ['year','time period','time_period','timeperiod']:
        if cand in cols:
            mapping['year'] = cols[cand]; break
    # attendance / total
    for cand in ['total','adjusted net attendance rate (%)','value','school_attendance','attendance']:
        if cand in cols:
            mapping['school_attendance'] = cols[cand]; break
    return mapping

def load_and_clean_unicef(path: str, keep_levels: Optional[list]=None) -> pd.DataFrame:
    """Carga el CSV de UNICEF y devuelve un DataFrame con columnas:
       country_code, country_name, year, school_attendance
    """
    df = pd.read_csv(path)
    # detectar mapping
    mapping = identify_columns(df)
    # si no encontramos country_code -> mostrar error explicativo
    required = ['country_code','year','school_attendance']
    for r in required:
        if r not in mapping:
            raise ValueError(f"No se detectó la columna para '{r}'. Columnas disponibles: {list(df.columns)}")
    df_clean = df[[mapping['country_code'], mapping.get('country_name', mapping['country_code']), mapping['year'], mapping['school_attendance']]].copy()
    df_clean.columns = ['country_code','country_name','year','school_attendance']
    # limpieza básica
    df_clean['country_code'] = df_clean['country_code'].astype(str).str.strip().str.upper()
    df_clean['country_name'] = df_clean['country_name'].astype(str).str.strip()
    df_clean['year'] = pd.to_numeric(df_clean['year'].astype(str).str.extract(r'(\d{4})')[0], errors='coerce').astype('Int64')
    df_clean['school_attendance'] = pd.to_numeric(df_clean['school_attendance'], errors='coerce')
    df_clean.dropna(subset=['country_code','year','school_attendance'], inplace=True)
    # filtrar códigos ISO3 válidos (opcional)
    df_clean = df_clean[df_clean['country_code'].str.fullmatch(r'[A-Z]{3}', na=False)]
    df_clean.reset_index(drop=True, inplace=True)
    return df_clean

if __name__ == "__main__":
    df = load_and_clean_unicef("data/Datos_de_asistencia_escolar.csv")
    print(df.head())
