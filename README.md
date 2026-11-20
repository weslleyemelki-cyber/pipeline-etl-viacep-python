# 🚀 Pipeline ETL em Python com Enriquecimento de Dados via API (ViaCEP) e PostgreSQL

Pipeline de dados end-to-end desenvolvido em Python para extração, limpeza, enriquecimento em tempo real via API externa e persistência estruturada em banco de dados relacional **PostgreSQL**.

## 📌 Sobre o Projeto
Este projeto simula um cenário real de engenharia de dados corporativa. O objetivo é processar dados brutos e desestruturados de clientes, limpar inconsistências, consultar a API pública do **ViaCEP** para normalizar os endereços em tempo real, estruturar o conjunto final de dados e persistir o resultado em um banco **PostgreSQL** via **SQLAlchemy**.

## 🛠️ Tecnologias e Ferramentas Utilizadas
- **Python** (Linguagem principal)
- **Pandas & NumPy** (Manipulação, limpeza e transformação de dados)
- **Requests** (Consumo de API REST em tempo real)
- **SQLAlchemy** (Conexão e persistência relacional via `DataFrame.to_sql`)
- **PostgreSQL & Psycopg2** (Banco de dados relacional de destino e driver de conexão)
- **Python-dotenv** (Carregamento de variáveis de ambiente a partir do `.env`)
- **Git & GitHub** (Controle de versão)

## 🗂️ Estrutura do Projeto
O repositório foi organizado seguindo boas práticas de arquitetura de software para garantir modularidade e clareza:

```text
pipeline-etl-viacep-python/
│
├── data/                      # Arquivos CSV de entrada e saída (dados brutos e limpos)
│   ├── dados_sujos.csv
│   └── endereco_clientes.csv
│
├── src/                       # Código-fonte (regras de negócio e ETL)
│   ├── transform.py           # Limpeza e padronização inicial dos dados
│   ├── cep_api.py             # Consulta ao ViaCEP e enriquecimento de endereços
│   └── load.py                # Persistência dos dados no PostgreSQL via SQLAlchemy
│
├── .env.example               # Modelo de variáveis de ambiente (sem credenciais reais)
├── .gitignore                 # Arquivos ignorados pelo Git (inclui .env)
├── main.py                    # Script principal de orquestração do pipeline
└── requirements.txt           # Dependências do projeto