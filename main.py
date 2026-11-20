
from src.cep_api import cepapi
from src.load import load_dados_banco
from src.transform import transf


def execute():

    cursor_transf = transf() 
    print(cursor_transf)

    
   
    cursor_api = cepapi()
    print(cursor_api)

    if cursor_api is not None and not cursor_api.empty:
        load_dados_banco(cursor_api)

if __name__ == '__main__':

    execute()