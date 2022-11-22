import pandas as pd

import datetime
"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

def clean_data():
    
    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col= 0, encoding="utf-8")

    df = df.dropna()

    df["sexo"] = df.sexo.str.lower()
    df["sexo"] = df.sexo.str.strip()

    df["tipo_de_emprendimiento"] = df.tipo_de_emprendimiento.str.lower()
    df["tipo_de_emprendimiento"] = df.tipo_de_emprendimiento.str.strip()

    df["idea_negocio"] = df.idea_negocio.str.lower()
    df["idea_negocio"] = df.idea_negocio.str.strip()
    df["idea_negocio"] = df.idea_negocio.str.replace("_", " ")
    df["idea_negocio"] = df.idea_negocio.str.replace("-", " ")
    df["idea_negocio"] = df.idea_negocio.str.replace("__", " ")
    df["idea_negocio"] = df.idea_negocio.str.replace("  ", " ")

    df["barrio"] = df.barrio.str.lower()
    df["barrio"] = df.barrio.str.strip()
    df["barrio"] = df.barrio.str.replace("_", " ")
    df["barrio"] = df.barrio.str.replace("-", " ")
    df["barrio"] = df.barrio.str.replace("__", " ")
    df["barrio"] = df.barrio.str.replace("  ", " ")

    def clean_currency(x):
        if isinstance(x, str):
            return(x.replace('$', '').replace(',', '').replace('.00', ''))

        return(x)

    df['monto_del_credito'] = df.monto_del_credito.apply(clean_currency).astype('float')


    for date in df["fecha_de_beneficio"]:
        if len(date.split("/")[0]) == 4:
            date = datetime.datetime.strptime(date, "%Y/%m/%d").strftime("%d/%m/%Y")
        else:
            date = datetime.datetime.strptime(date, "%d/%m/%Y")



    df["línea_credito"] = df.línea_credito.str.lower()
    df["línea_credito"] = df.línea_credito.str.replace("_", " ")
    df["línea_credito"] = df.línea_credito.str.replace("-", " ")
    df["línea_credito"] = df.línea_credito.str.replace("__", " ")

    df = df.drop_duplicates()

    return df

clean_data()
