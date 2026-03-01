from __future__ import annotations

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors


def topk_politicas_por_proyecto(
    df_politicas: pd.DataFrame,
    df_proyectos: pd.DataFrame,
    col_text_politica: str,
    col_text_proyecto: str,
    col_id_proyecto: str,
    top_k: int = 10,
    min_score: float = 0.35,
    model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    batch_size: int = 64,
    device: str = "cpu",
) -> pd.DataFrame:
    """
    Devuelve TOP-K políticas por cada proyecto usando embeddings + similitud coseno.

    Output (formato long):
      - columnas del proyecto
      - matched_politica_text
      - similarity_score
      - rank
    """

    # Validaciones
    if col_text_politica not in df_politicas.columns:
        raise ValueError(f"df_politicas no tiene la columna requerida: {col_text_politica}")
    for c in [col_text_proyecto, col_id_proyecto]:
        if c not in df_proyectos.columns:
            raise ValueError(f"df_proyectos no tiene la columna requerida: {c}")

    if len(df_politicas) == 0 or len(df_proyectos) == 0:
        return pd.DataFrame()

    # Modelo
    model = SentenceTransformer(model_name, device=device)

    # Textos
    pol_texts = df_politicas[col_text_politica].fillna("").astype(str).tolist()
    proy_texts = df_proyectos[col_text_proyecto].fillna("").astype(str).tolist()

    # Embeddings normalizados (cosine ~ dot)
    E_pol = model.encode(
        pol_texts,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
    )
    E_proy = model.encode(
        proy_texts,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
    )

    # Vecinos
    n_neighbors = min(top_k, len(df_politicas))
    nn = NearestNeighbors(n_neighbors=n_neighbors, metric="cosine", algorithm="brute")
    nn.fit(E_pol)

    distances, indices = nn.kneighbors(E_proy, return_distance=True)
    scores = 1.0 - distances

    # Construcción del resultado
    out_rows: list[dict] = []
    for i in range(len(df_proyectos)):
        base = df_proyectos.iloc[i].to_dict()

        for rank in range(n_neighbors):
            j = int(indices[i, rank])
            sc = float(scores[i, rank])

            if sc < min_score:
                continue

            out_rows.append(
                {
                    **base,
                    "matched_politica_text": df_politicas.iloc[j][col_text_politica],
                    "similarity_score": sc,
                    "rank": rank + 1,
                }
            )

    df_out = pd.DataFrame(out_rows)
    if not df_out.empty:
        df_out = df_out.sort_values([col_id_proyecto, "rank"]).reset_index(drop=True)

    return df_out
