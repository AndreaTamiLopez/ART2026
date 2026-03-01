import os
import pandas as pd

from semantic_matching import topk_politicas_por_proyecto


def main():
    # Ajusta estas rutas/nombres a tus archivos reales (no los subas si son sensibles)
    politicas_path = "data/raw/politicas.xlsx"
    proyectos_path = "data/raw/proyectos.xlsx"

    df_politicas = pd.read_excel(politicas_path)
    df_proyectos = pd.read_excel(proyectos_path)

    df_matches = topk_politicas_por_proyecto(
        df_politicas=df_politicas,
        df_proyectos=df_proyectos,
        col_text_politica="Indicador de Producto(MGA)",
        col_text_proyecto="Indicadores de producto PATR",
        col_id_proyecto="codigo_proyecto",
        top_k=10,
        min_score=0.35,
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        batch_size=64,
        device="cpu",
    )

    os.makedirs("data/outputs", exist_ok=True)
    output_path = "data/outputs/cruce_top10.xlsx"
    df_matches.to_excel(output_path, index=False)
    print("Guardado:", output_path)


if __name__ == "__main__":
    main()
