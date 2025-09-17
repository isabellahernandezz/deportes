from Extract.extractor import extract_data
from Transform.transformer import transform_data
from Load.loader import load_data

def main():
    print("🚀 Iniciando ETL de Deportes...")
    
    # Extraer
    df = extract_data()
    
    # Transformar
    df_clean = transform_data(df)
    
    # Cargar
    load_data(df_clean)

    print("🎉 ETL completado con éxito")

if __name__ == "__main__":
    main()
