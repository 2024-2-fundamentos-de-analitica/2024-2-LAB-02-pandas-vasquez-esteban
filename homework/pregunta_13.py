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


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    tbl0 = load_data("files/input/tbl0.tsv")
    tbl2 = load_data("files/input/tbl2.tsv")

    tbl02 = pd.merge(tbl0, tbl2, on="c0")
    result = tbl02.groupby("c1")["c5b"].sum()

    return result
