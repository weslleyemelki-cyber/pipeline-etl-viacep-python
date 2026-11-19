import pandas as pd
import numpy as np

def transf():

    df = pd.read_csv("data/dados_sujos.csv", sep=';', encoding = 'utf-8' )


    df["nome_cliente"] = df["nome_cliente"].str.strip().str.title()
    df["nome_cliente"] = df["nome_cliente"].replace(r'^\s*$', np.nan, regex=True).fillna('Sem-Dados')

    df["cep"] = df["cep"].str.strip().str.replace('-', '', regex=False)


    df["valor_compra"] = df["valor_compra"].str.replace(',', '.', regex=False).fillna(0.0)
    df["valor_compra"] = df["valor_compra"].astype(float)
    

    df = df.drop_duplicates(subset=["id_cliente"])

    df["data_compra"] = pd.to_datetime(df["data_compra"].str.strip(), format= 'mixed', dayfirst= True)

    df['Status_Compra'] = np.where(df["valor_compra"] >= 400.00, 'Compra-Alta', 'Compra-Baixa')


    df.columns = df.columns.str.strip().str.title()



    return df
