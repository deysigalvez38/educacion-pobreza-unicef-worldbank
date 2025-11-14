import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# 1. CONFIGURACIÓN INICIAL
# ===============================

# Crear carpeta reports si no existe
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

# Ruta al archivo combinado
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "merged_unicef_worldbank.csv")

# Cargar datos
df = pd.read_csv(DATA_PATH)

# Normalizar nombre de país (preferimos UNICEF)
df["country_name"] = df["country_name_y"]

print("📊 Dataset cargado correctamente:")
print(df.head())


# ===============================
# 2. SCATTER: Pobreza vs Asistencia
# ===============================

plt.figure(figsize=(10,6))
sns.scatterplot(
    data=df,
    x="poverty_rate",
    y="school_attendance",
    alpha=0.6
)
plt.title("Relación: Pobreza extrema vs Asistencia Escolar")
plt.xlabel("Pobreza extrema (% población bajo $2.15/día)")
plt.ylabel("Asistencia escolar primaria (%)")

scatter_path = os.path.join(REPORTS_DIR, "scatter_poverty_vs_attendance.png")
plt.savefig(scatter_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"📁 Scatter guardado en: {scatter_path}")


# ===============================
# 3. CORRELACIÓN
# ===============================

corr_value = df["poverty_rate"].corr(df["school_attendance"])

plt.figure(figsize=(6,4))
sns.heatmap(df[["poverty_rate","school_attendance"]].corr(), annot=True, cmap="coolwarm")
plt.title(f"Mapa de calor de correlación (corr = {corr_value:.2f})")

corr_path = os.path.join(REPORTS_DIR, "correlation_heatmap.png")
plt.savefig(corr_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"📁 Heatmap guardado en: {corr_path}")


# ===============================
# 4. TOP 20 con menor asistencia
# ===============================

top20 = df.sort_values("school_attendance").head(20)

plt.figure(figsize=(12,8))
sns.barplot(
    data=top20,
    x="school_attendance",
    y="country_name"
)
plt.title("Top 20 países con menor asistencia escolar")
plt.xlabel("Asistencia escolar (%)")
plt.ylabel("País")

top20_path = os.path.join(REPORTS_DIR, "top20_lowest_attendance.png")
plt.savefig(top20_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"📁 Ranking (asistencia) guardado en: {top20_path}")


# ===============================
# 5. TOP 20 con mayor pobreza
# ===============================

top20_poverty = df.sort_values("poverty_rate", ascending=False).head(20)

plt.figure(figsize=(12,8))
sns.barplot(
    data=top20_poverty,
    x="poverty_rate",
    y="country_name",
    palette="Reds_r"
)
plt.title("Top 20 países con mayor pobreza extrema")
plt.xlabel("Pobreza extrema (%)")
plt.ylabel("País")

top20p_path = os.path.join(REPORTS_DIR, "top20_highest_poverty.png")
plt.savefig(top20p_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"📁 Ranking (pobreza) guardado en: {top20p_path}")


# ===============================
# 6. FINAL
# ===============================

print("\n🎉 Todos los reportes fueron generados en la carpeta /reports/")
