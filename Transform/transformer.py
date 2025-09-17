import pandas as pd

def transform_data(df):
    """Transforma los datos (limpieza básica)"""
    # Eliminar duplicados
    df = df.drop_duplicates()

    # Eliminar columnas completamente vacías
    df = df.dropna(axis=1, how='all')

    # Rellenar valores nulos con 0 en numéricos y 'Desconocido' en texto
    df = df.fillna({
        col: 0 if pd.api.types.is_numeric_dtype(df[col]) else "Desconocido"
        for col in df.columns
    })

    print(f"✅ Datos transformados: {df.shape[0]} filas, {df.shape[1]} columnas")
    return df
