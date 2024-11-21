"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd  # type: ignore


def load_data(file):
    """Load tsv table"""

    return pd.read_csv(file, sep="\t")


def row_len(df):
    """Retorna la cantidad de filas"""
    return df.shape[0]


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """

    df = load_data("files/input/tbl0.tsv")
    return row_len(df)
