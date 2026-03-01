# Modelo 1

## Matching semántico entre indicadores PATR y MGA / SisPT

Este repositorio implementa un proceso de matching semántico entre indicadores de producto asociados a proyectos (PATR) y un catálogo de indicadores o políticas (MGA / SisPT).

El objetivo es identificar, para cada proyecto, los Top-K indicadores más similares en significado, utilizando modelos de lenguaje multilingües.

## Metodología

El proceso de emparejamiento sigue los siguientes pasos:

- Generación de embeddings multilingües usando Sentence Transformers
- Normalización de vectores para similitud coseno
- Búsqueda de vecinos más cercanos mediante k-Nearest Neighbors (Top-K)
- Filtrado de resultados usando un umbral mínimo de similitud

El resultado se entrega en formato long, con una fila por cada relación proyecto–indicador.

## Estructura del proyecto

src/
semantic_matching/
__init__.py
matcher.py
scripts/
run_matching.py
data/
raw/
outputs/
requirements.txt
.gitignore
README.md

## Requisitos

Python 3.9 o superior.

Dependencias principales:

- pandas
- numpy
- scikit-learn
- sentence-transformers
- openpyxl

Las dependencias se instalan desde requirements.txt.

## Uso

1. Colocar los archivos de entrada en la carpeta data/raw/
2. Configurar rutas y nombres de columnas en scripts/run_matching.py
3. Ejecutar el script desde la raíz del proyecto

El archivo de salida se genera en la carpeta data/outputs/ en formato Excel.

## Parámetros principales

top_k: número máximo de indicadores devueltos por proyecto  
min_score: umbral mínimo de similitud semántica  
model_name: modelo de Sentence Transformers utilizado  
device: cpu (recomendado) o cuda si se dispone de GPU

## Licencia

Este proyecto puede publicarse bajo una licencia abierta (MIT, Apache-2.0 u otra).
