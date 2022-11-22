import pandas as pd

import datetime
"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

def clean_data():
    
    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col= 0)

    df = df.dropna()

    df["sexo"] = df.sexo.str.lower()

    df["tipo_de_emprendimiento"] = df.tipo_de_emprendimiento.str.lower()
    

    df["idea_negocio"] = df.idea_negocio.str.lower()
    df["idea_negocio"] = df.idea_negocio.str.replace("_", " ")
    df["idea_negocio"] = df.idea_negocio.str.replace("-", " ")
    df["idea_negocio"] = df.idea_negocio.str.replace("__", " ")
    df["idea_negocio"] = df.idea_negocio.str.strip()

    df["barrio"] = df.barrio.str.lower()
    df["barrio"] = df.barrio.str.replace("_", " ")
    df["barrio"] = df.barrio.str.replace("-", " ")
    df["barrio"] = df.barrio.str.replace("__", " ")
    df["barrio"] = df.barrio.str.strip()

    def clean_currency(x):
        if isinstance(x, str):
            return(x.replace('$', '').replace(',', '').replace(' ', ''))

        return(x)

    df['monto_del_credito'] = df.monto_del_credito.apply(clean_currency).astype(float)


    # for date in df["fecha_de_beneficio"]:
    #     if len(date.split("/")[0]) == 4:
    #         date = datetime.datetime.strptime(date, "%Y/%m/%d").strftime("%d/%m/%Y")
    #     else:
    #         date = datetime.datetime.strptime(date, "%d/%m/%Y")
    #     df["fecha_de_beneficio"] = date
    def dates(fecha):
        p = fecha.split('/')
        if len(p[0]) == 4:
            date = '/'.join(reversed(p))
        else:
            date = '/'.join(p)
        return date

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(dates)

    df["línea_credito"] = df.línea_credito.str.lower()
    df["línea_credito"] = df.línea_credito.str.replace("_", " ")
    df["línea_credito"] = df.línea_credito.str.replace("-", " ")
    df["línea_credito"] = df.línea_credito.str.replace("__", " ")

    df = df.drop_duplicates()
   

    return df

if __name__ == "__main__":
    
    clean_data()
    print(clean_data().sexo.value_counts().to_list() )
    clean_data().to_csv("solicitudes_credito_clean.csv", sep= ",")
    #== [6617, 3589]