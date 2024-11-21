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


def group_by_letter(df):
    """Agrupar por #Registros de cada letra"""
    res = df.groupby("c1").size()

    return res


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    df = load_data("files/input/tbl0.tsv")
    reg_per_letter = group_by_letter(df)

    return reg_per_letter
