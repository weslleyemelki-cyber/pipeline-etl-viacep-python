import sqlite3
from src.cep_api import cepapi
from src.transform import transf

def execute():


    cursor = transf()
    
    print(cursor)

    
    
    cursor = cepapi()
    print(cursor)

    try:
        conexao = sqlite3.connect('database/Banco_cliente.db')
        cursor.to_sql('Tabela_Pronta', con=conexao,if_exists='replace', index=False)

        conexao.close()
        print("Processo de dados concluido")

    except Exception as e:
        print(f"Erro ao tenta fazer conexão com SQL: {e}")

if __name__ == '__main__':

    execute()