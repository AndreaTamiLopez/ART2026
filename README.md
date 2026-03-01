Matching semántico Top-K entre indicadores PATR y MGA / SisPT

Este repositorio contiene una herramienta para realizar matching semántico entre indicadores de producto asociados a proyectos (PATR) y un catálogo de indicadores o políticas (MGA / SisPT).

El objetivo es identificar, para cada proyecto, los Top-K indicadores más cercanos en significado, utilizando modelos de lenguaje multilingües y métricas de similitud semántica.

📌 Alcance

El código permite:

Comparar descripciones textuales de proyectos contra un catálogo de indicadores

Encontrar correspondencias semánticas, incluso cuando no hay coincidencia literal de palabras

Obtener resultados ordenados por nivel de similitud

El resultado final se entrega en un archivo Excel, con una fila por cada relación proyecto–indicador.

⚙️ Metodología

El proceso de matching sigue los siguientes pasos:

Generación de embeddings multilingües usando Sentence Transformers

Normalización de vectores para similitud coseno

Búsqueda de vecinos más cercanos mediante k-Nearest Neighbors (Top-K)

Filtrado de resultados usando un umbral mínimo de similitud

📂 Estructura del proyecto
src/
 └── semantic_matching/
     ├── __init__.py
     └── matcher.py
scripts/
 └── run_matching.py
data/
 ├── raw/        # datos de entrada (uso local, no versionar)
 └── outputs/    # resultados generados (uso local, no versionar)
requirements.txt
.gitignore
README.md
🧩 Requisitos

Python 3.9 o superior

Dependencias principales:

pandas

numpy

scikit-learn

sentence-transformers

openpyxl

Las dependencias se instalan desde requirements.txt.

▶️ Uso

Colocar los archivos de entrada en la carpeta data/raw/

Configurar rutas y nombres de columnas en scripts/run_matching.py

Ejecutar el script desde la raíz del proyecto

El archivo de salida se genera automáticamente en data/outputs/ en formato Excel.

🔧 Parámetros clave

top_k
Número máximo de indicadores devueltos por proyecto (default: 10)

min_score
Umbral mínimo de similitud semántica (default: 0.35)

model_name
Modelo multilingüe de Sentence Transformers utilizado para los embeddings

device
cpu (recomendado por estabilidad) o cuda si se dispone de GPU

📝 Notas técnicas

La normalización de embeddings permite que la similitud coseno sea consistente.

El formato de salida es long, facilitando análisis, filtros y visualización.

El umbral de similitud puede ajustarse según la calidad deseada de los matches.

El resultado está en formato long, lo que facilita análisis, filtros y visualización.

Si muchos proyectos quedan sin match, se recomienda bajar min_score.

Si aparecen matches poco relevantes, se recomienda aumentar el umbral.
