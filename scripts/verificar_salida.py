import os
from Config.config import OUTPUT_FILE

def verificar_archivo():
    if os.path.exists(OUTPUT_FILE):
        print(f"✅ Archivo generado: {OUTPUT_FILE}")
    else:
        print("❌ El archivo limpio no se generó correctamente.")

if __name__ == "__main__":
    verificar_archivo()
