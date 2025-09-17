# scripts/transformacion.py
import pandas as pd
import os

# Definir rutas directamente (rutas relativas desde el root del proyecto)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "data/input")
OUTPUT_PATH = os.path.join(BASE_DIR, "data/output")


def transformar_datos():
    # 1️⃣ Cargar dataset limpio
    df = pd.read_csv(f"{INPUT_PATH}/deportes_limpio.csv")
    print("📥 Dataset limpio cargado:", df.shape)

    # 2️⃣ Seleccionar columnas relevantes (según dataset real)
    columnas = ["League", "Date", "HomeTeam", "AwayTeam", "FTH Goals", "FTA Goals", "FT Result"]
    df = df[columnas]
    print("✅ Columnas seleccionadas:", df.shape)

    # 3️⃣ Convertir fechas a formato estándar
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # 4️⃣ Renombrar columnas para claridad
    df = df.rename(columns={
        "League": "Liga",
        "Date": "Fecha",
        "HomeTeam": "Equipo_Local",
        "AwayTeam": "Equipo_Visitante",
        "FTH Goals": "Goles_Local",
        "FTA Goals": "Goles_Visitante",
        "FT Result": "Resultado"
    })

    # 5️⃣ Crear nueva columna: Diferencia de goles
    df["Diferencia_Goles"] = df["Goles_Local"] - df["Goles_Visitante"]

    # 6️⃣ Guardar dataset transformado
    output_file = f"{OUTPUT_PATH}/deportes_transformado.csv"
    df.to_csv(output_file, index=False)
    print(f"📂 Dataset transformado guardado en: {output_file}")

if __name__ == "__main__":
    transformar_datos()
