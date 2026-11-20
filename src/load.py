from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()

def obter_db_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
            raise ValueError(
            print("A variavel do banco de dados não está definida!")
            )
    return url

def load_dados_banco(
            df,
            nome_tabela: str = "clientes_enriquecidos",
            database_url: str | None = None,
) -> None:
    """
    Salva o DataFrame tratado em um banco PostgreSQL utilizando SQLAlchemy.
    """

    try:
        url = database_url or obter_db_url()
        engine = create_engine(url)

        df.to_sql(
            name = nome_tabela,
            con = engine,
            if_exists = 'replace',
            index = False,
        )

        print('foi')
    except SQLAlchemyError as e:
        raise RuntimeError(f"Falha ao gravar no PostgreSQL: {e}") from e