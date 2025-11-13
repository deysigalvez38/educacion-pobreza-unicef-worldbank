# src/get_worldbank_api.py
"""
Funciones para descargar datos del World Bank API.
Uso:
    from get_worldbank_api import fetch_worldbank_by_countries
    df = fetch_worldbank_by_countries(["TZA","MOZ"], indicator="SI.POV.DDAY", start=2010, end=2022)
"""

import requests
import pandas as pd
from typing import List

BASE = "https://api.worldbank.org/v2/country/{countries}/indicator/{indicator}?format=json&date={start}:{end}&per_page=20000"

def fetch_worldbank_by_countries(country_codes: List[str],
                                 indicator: str = "SI.POV.DDAY",
                                 start: int = 2010,
                                 end: int = 2022) -> pd.DataFrame:
    """Descarga datos del World Bank para una lista de códigos ISO3."""
    if not country_codes:
        raise ValueError("country_codes cannot be empty")
    countries = ";".join(country_codes)
    url = BASE.format(countries=countries, indicator=indicator, start=start, end=end)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if len(data) < 2 or data[1] is None:
        return pd.DataFrame(columns=["country_code","country_name","year","value"])
    records = data[1]
    df = pd.DataFrame(records)
    # extraer campos útiles
    df = df[['country', 'date', 'value']].copy()
    df['country_name'] = df['country'].apply(lambda x: x.get('value') if isinstance(x, dict) else None)
    df['country_code'] = df['country'].apply(lambda x: x.get('id') if isinstance(x, dict) else None)
    df.rename(columns={'value': 'poverty_rate', 'date': 'year'}, inplace=True)
    df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
    df = df[['country_code','country_name','year','poverty_rate']]
    # filtrar códigos ISO3 válidos
    df = df[df['country_code'].str.fullmatch(r'[A-Z]{3}', na=False)]
    df.dropna(subset=['poverty_rate','year'], inplace=True)
    df['poverty_rate'] = pd.to_numeric(df['poverty_rate'], errors='coerce')
    return df.reset_index(drop=True)

if __name__ == "__main__":
    # ejemplo rápido
    sample = ["TZA","MOZ","NER","SSD","BFA"]
    print("Descargando ejemplo...")
    df = fetch_worldbank_by_countries(sample)
    print(df.head())
