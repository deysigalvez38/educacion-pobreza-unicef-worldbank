# src/analysis_functions.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional

def plot_scatter_poverty_vs_attendance(df: pd.DataFrame, hue: Optional[str]='country_name', savepath:Optional[str]=None):
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='poverty_rate', y='school_attendance', hue=hue, legend=False)
    sns.regplot(data=df, x='poverty_rate', y='school_attendance', scatter=False, lowess=True, line_kws={'color':'black','lw':1})
    plt.xlabel("Pobreza extrema (% población < $2.15/día)")
    plt.ylabel("Asistencia escolar primaria (%)")
    plt.title("Pobreza vs Asistencia escolar")
    plt.tight_layout()
    if savepath:
        plt.savefig(savepath, dpi=150)
    plt.show()

def plot_top_countries_bar(df: pd.DataFrame, top_n:int=30, savepath:Optional[str]=None):
    top = df.sort_values('school_attendance').head(top_n)
    plt.figure(figsize=(8,12))
    sns.barplot(x='school_attendance', y='country_name', data=top, orient='h')
    plt.xlabel("Asistencia escolar (%)")
    plt.ylabel("")
    plt.title(f"Top {top_n} países con menor asistencia escolar")
    plt.tight_layout()
    if savepath:
        plt.savefig(savepath, dpi=150)
    plt.show()
