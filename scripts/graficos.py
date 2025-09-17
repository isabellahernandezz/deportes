# scripts/graficos.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configuración de paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "data/output")
DATA_FILE = os.path.join(OUTPUT_PATH, "deportes_transformado.csv")

def generar_graficos():
    # 1️⃣ Cargar dataset transformado
    df = pd.read_csv(DATA_FILE)
    print("📥 Dataset transformado cargado:", df.shape)

    # Asegurar que la fecha sea datetime
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce", dayfirst=True)

    # ==============================
    # 📈 1. Número de partidos por año
    # ==============================
    df["Año"] = df["Fecha"].dt.year
    partidos_por_anio = df.groupby("Año").size().reset_index(name="Partidos")

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=partidos_por_anio, x="Año", y="Partidos", marker="o")
    plt.title("📈 Número de partidos por año")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de Partidos")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "grafico_partidos_por_anio.png"))
    plt.close()

    # =====================================
    # ⚽ 2. Promedio de goles locales vs visitantes
    # =====================================
    promedio_goles = {
        "Goles_Local": df["Goles_Local"].mean(),
        "Goles_Visitante": df["Goles_Visitante"].mean()
    }
    goles_df = pd.DataFrame(list(promedio_goles.items()), columns=["Tipo", "Promedio"])

    plt.figure(figsize=(8, 6))
    sns.barplot(data=goles_df, x="Tipo", y="Promedio", palette="coolwarm")
    plt.title("⚽ Promedio de goles locales vs visitantes")
    plt.ylabel("Promedio de Goles")
    plt.xlabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "grafico_promedio_goles.png"))
    plt.close()

    # =====================================
    # 🏆 3. Distribución de resultados
    # =====================================
    resultados = df["Resultado"].value_counts().reset_index()
    resultados.columns = ["Resultado", "Cantidad"]

    plt.figure(figsize=(8, 6))
    sns.barplot(data=resultados, x="Resultado", y="Cantidad", palette="Set2")
    plt.title("🏆 Distribución de resultados")
    plt.ylabel("Cantidad de Partidos")
    plt.xlabel("Resultado")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "grafico_resultados.png"))
    plt.close()

    print("✅ Gráficas generadas en:", OUTPUT_PATH)

if __name__ == "__main__":
    generar_graficos()
