import os

# Carpeta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Archivos de entrada y salida
INPUT_FILE = os.path.join(BASE_DIR, "data", "input", "England 2 CSV.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "output", "deportes_limpio.csv")
