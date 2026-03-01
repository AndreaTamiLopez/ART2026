# ART2026 — Matching semántico (Top-K) entre indicadores PATR y MGA / SisPT

Este repositorio implementa un proceso de matching semántico entre:

Indicadores de producto PATR asociados a proyectos

Indicadores de Producto (MGA / SisPT) usados como catálogo de políticas

El objetivo es identificar, para cada proyecto, los Top-K indicadores o políticas más similares en significado, usando modelos de lenguaje multilingües.

¿QUÉ HACE ESTE CÓDIGO?

Dadas dos tablas con texto:

Genera embeddings multilingües con Sentence Transformers

Calcula similitud semántica usando similitud coseno

Aplica k-Nearest Neighbors (Top-K) para cada proyecto

Filtra resultados por un umbral mínimo de similitud

Entrega el resultado en formato long (una fila por match)

Cada fila del resultado incluye:

texto del indicador o política emparejado

similarity_score

rank (1 = mejor match)

ESTRUCTURA DEL REPOSITORIO

.
├── src/
│ └── semantic_matching/
│ ├── init.py
│ └── matcher.py
├── scripts/
│ └── run_matching.py
├── data/
│ ├── raw/ (archivos de entrada, uso local, NO subir)
│ └── outputs/ (resultados, uso local, NO subir)
├── requirements.txt
├── .gitignore
└── README.md

Los archivos con datos reales no deben subirse al repositorio.
El archivo .gitignore ya excluye data/raw y data/outputs.

REQUISITOS

Python 3.9 o superior

Librerías principales:

pandas

numpy

scikit-learn

sentence-transformers

openpyxl

Instalación recomendada usando entorno virtual:

python -m venv .venv
Windows:
.venv\Scripts\activate

Mac / Linux:
source .venv/bin/activate

pip install -r requirements.txt

USO

Coloca tus archivos de entrada en la carpeta data/raw
(por ejemplo: politicas.xlsx y proyectos.xlsx)

Ajusta en scripts/run_matching.py:

rutas de los archivos

nombres de las columnas de texto

parámetros del modelo

Ejecuta el script:

Mac / Linux:
PYTHONPATH=src python scripts/run_matching.py

Windows (PowerShell):
$env:PYTHONPATH="src"
python scripts/run_matching.py

El archivo de salida se genera en:

data/outputs/cruce_top10.xlsx

PARÁMETROS PRINCIPALES

top_k
Número de indicadores o políticas a devolver por proyecto (default: 10)

min_score
Umbral mínimo de similitud semántica (default: 0.35)

model_name
Modelo de embeddings
Default: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

device
"cpu" (recomendado por estabilidad) o "cuda" si se dispone de GPU
Si se usa GPU, reducir batch_size según la memoria disponible.

NOTAS TÉCNICAS

Los embeddings se normalizan, por lo que la similitud coseno equivale al producto punto.

El resultado está en formato long, lo que facilita análisis, filtros y visualización.

Si muchos proyectos quedan sin match, se recomienda bajar min_score.

Si aparecen matches poco relevantes, se recomienda aumentar el umbral.
