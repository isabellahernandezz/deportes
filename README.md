## ⚙️ Instalación

1️⃣ Clona el repositorio:
```bash
git clone https://github.com/isabellahernandezz/deportes.git
cd deportes/etl-deportes
2️⃣ Crea un entorno virtual (opcional pero recomendado):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
3️⃣ Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
📊 Pipeline ETL
1️⃣ Extracción (Extract)
El dataset original (deportes.csv) proviene de partidos de la liga inglesa.

Se guarda en data/input/.

2️⃣ Transformación (Transform)
Se eliminan duplicados y valores nulos.

Se renombran columnas para mayor claridad.

Se convierten fechas al formato estándar.

Se crean métricas como diferencia de goles.

3️⃣ Carga (Load)
Los datos transformados se guardan en:

data/input/deportes_limpio.csv (datos limpios)

data/output/deportes_transformado.csv (datos finales)

📈 Visualizaciones
El archivo scripts/graficos.py genera gráficas automáticas:

Número de partidos por año 📆

Promedio de goles locales vs visitantes ⚽

Distribución de resultados (Victoria local, Empate, Victoria visitante) 🏆

Ejecutar:

bash
Copiar código
python3 scripts/graficos.py
📂 Las imágenes se guardan en data/output/:

partidos_por_anio.png

promedio_goles.png

resultados.png

