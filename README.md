# 🏟️ Proyecto ETL de Deportes

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** sobre un dataset de partidos de fútbol.  
Fue desarrollado en **Python** utilizando **pandas**, **seaborn** y **matplotlib**, organizado con una arquitectura modular.

---

## 📂 Estructura del proyecto

etl-deportes/
├── Config/ # Configuración de rutas y parámetros
│ └── config.py
├── Extract/ # Módulo de extracción
│ └── extractor.py
├── Transform/ # Módulo de transformación
│ └── transformer.py
├── Load/ # Módulo de carga
│ └── loader.py
├── data/
│ ├── input/ # Datos originales y limpios
│ │ ├── deportes.csv
│ │ └── deportes_limpio.csv
│ └── output/ # Datos transformados y gráficos
│ ├── deportes_transformado.csv
│ ├── grafico_partidos_por_anio.png
│ ├── grafico_promedio_goles.png
│ └── grafico_resultados.png
├── scripts/ # Scripts auxiliares
│ ├── limpieza.py
│ ├── transformacion.py
│ ├── graficos.py
│ └── verificar_salida.py
├── main.py # Script principal que ejecuta todo el ETL
├── requirements.txt # Librerías necesarias
└── README.md # Documentación del proyecto


---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/isabellahernandezz/deportes.git
   cd deportes/etl-deportes


Instalar dependencias:

pip install -r requirements.txt

🚀 Ejecución del ETL

Puedes correr cada paso por separado o todo desde main.py.

1️⃣ Limpieza
python3 scripts/limpieza.py


Genera data/input/deportes_limpio.csv.

2️⃣ Transformación
python3 scripts/transformacion.py


Genera data/output/deportes_transformado.csv.

3️⃣ Visualización
python3 scripts/graficos.py


Genera 3 gráficos en data/output/.

4️⃣ Ejecución completa
python3 main.py
