import pandas as pd
import requests as rq
from src.transform import transf
import numpy as np

def cepapi():
    dfc = transf()


    dfc['Cidade'] = ""
    dfc['Estado'] = ""
    dfc['Logradouro'] = ""


    ceplist = dfc['Cep'].to_list()

    for index, row in dfc.iterrows():

        cep = row['Cep']
        url = rq.get(f'https://viacep.com.br/ws/{cep}/json/')

        if url.status_code == 200:
            dados = url.json()

            if 'erro' in dados:
                print(f"CEP não encontrado na base: {cep}")
            else:
                try:
                    dfc.loc[index, 'Cidade'] = dados.get('localidade')
                    dfc.loc[index, 'Logradouro'] = dados.get('logradouro')
                    dfc.loc[index, 'Estado'] = dados.get('estado')
                    print(f"Sucesso!")
                    
                except Exception as e:
                    print(f"Erro ao atualiza o DataFraeme para o Cep {cep}: {e}")

        else:
            print(f"Erro ao conecta Cep com Api. Code: {url.status_code}")



    dfc
    dfc['Cidade'] = dfc['Cidade'].replace(r'^\s*$', np.nan, regex=True).fillna('Sem-Dados')
    dfc['Logradouro'] = dfc['Logradouro'].replace(r'^\s*$', np.nan, regex=True).fillna('Sem-Dados')
    dfc['Estado'] = dfc['Estado'].replace(r'^\s*$', np.nan, regex=True).fillna('Sem-Dados')

    dfc.to_csv("data/dados_limpos.csv", index=False, sep=';', encoding='utf-8')
    print("Arquivo salvo com sucesso!")

    return dfc

