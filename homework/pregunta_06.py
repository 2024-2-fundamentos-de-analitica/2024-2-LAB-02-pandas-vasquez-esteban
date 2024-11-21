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


def unique_c4(df):
    """Agrupar por registros únicos de c4"""
    return df["c4"].unique()


def sort_mayus(input_list):
    """Convert to mayus & sort"""
    return sorted([l.upper() for l in input_list])


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    df = load_data("files/input/tbl1.tsv")
    return sort_mayus(unique_c4(df))
