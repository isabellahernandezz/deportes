from Config.config import OUTPUT_FILE

def load_data(df):
    """Carga los datos transformados a un CSV limpio"""
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Datos cargados en {OUTPUT_FILE}")
