import pandas as pd
from Config.config import INPUT_FILE

def extract_data():
    """Extrae datos desde el CSV original"""
    df = pd.read_csv(INPUT_FILE)
    print(f"✅ Datos extraídos: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df
