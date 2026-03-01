# ART2026
# ART2026 — Matching semántico (Top-K) entre indicadores PATR y MGA / SisPT

Este repositorio implementa un proceso de **matching semántico** entre:

- Indicadores de producto PATR asociados a proyectos
- Indicadores de Producto (MGA / SisPT) usados como catálogo de políticas

El objetivo es identificar, para cada proyecto, los **Top-K indicadores o políticas más similares en significado**, usando modelos de lenguaje multilingües.

---

## ¿Qué hace este código?

Dadas dos tablas con texto:

1. Genera embeddings multilingües con Sentence Transformers
2. Calcula similitud semántica usando similitud coseno
3. Aplica k-Nearest Neighbors (Top-K) para cada proyecto
4. Filtra resultados por un umbral mínimo de similitud
5. Entrega el resultado en formato long (una fila por match)

Cada fila del resultado incluye:
- texto del indicador o política emparejado
- similarity_score
- rank (1 = mejor match)

---

## Estructura del repositorio


.
├── src/
│ └── semantic_matching/
│ ├── init.py
│ └── matcher.py
├── scripts/
│ └── run_matching.py
├── data/
│ ├── raw/ # archivos de entrada (uso local, NO subir)
│ └── outputs/ # resultados (uso local, NO subir)
├── requirements.txt
├── .gitignore
└── README.md


Los archivos con datos reales no deben subirse al repositorio.  
El archivo `.gitignore` ya excluye `data/raw/` y `data/outputs/`.

---

## Requisitos

- Python 3.9 o superior

Librerías principales:
- pandas
- numpy
- scikit-learn
- sentence-transformers
- openpyxl

Instalación recomendada en entorno virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac / Linux
source .venv/bin/activate

pip install -r requirements.txt
Uso

Coloca tus archivos de entrada en data/raw/
(por ejemplo: politicas.xlsx y proyectos.xlsx)

Ajusta en scripts/run_matching.py:

rutas de los archivos

nombres de las columnas de texto

parámetros del modelo

Ejecuta el script:

Mac / Linux
PYTHONPATH=src python scripts/run_matching.py
Windows (PowerShell)
$env:PYTHONPATH="src"
python scripts/run_matching.py

El archivo de salida se genera en:

data/outputs/cruce_top10.xlsx
Parámetros principales

top_k
Número de indicadores o políticas a devolver por proyecto (default: 10)

min_score
Umbral mínimo de similitud semántica (default: 0.35)

model_name
Modelo de embeddings (default: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)

device
"cpu" (recomendado por estabilidad) o "cuda" si se dispone de GPU
Si se usa GPU, reducir batch_size según la memoria disponible.

Notas técnicas

Los embeddings se normalizan, por lo que la similitud coseno equivale al producto punto.

El output está en formato long, facilitando análisis, filtros y visualización.

Si muchos proyectos quedan sin match, se recomienda bajar min_score.

Si aparecen matches poco relevantes, se recomienda aumentar el umbral.

Licencia

Este proyecto puede publicarse bajo una licencia abierta (por ejemplo, MIT o Apache-2.0).
Agregar un archivo LICENSE si se requiere reutilización externa.
