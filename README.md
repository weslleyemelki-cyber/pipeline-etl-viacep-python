# 🚀 Pipeline ETL em Python com Enriquecimento de Dados via API (ViaCEP) e SQLite

Pipeline de dados end-to-end desenvolvido em Python para extração, limpeza, enriquecimento em tempo real via API externa e persistência estruturada em banco de dados relacional.

## 📌 Sobre o Projeto
Este projeto simula um cenário real de engenharia de dados corporativa. O objetivo é processar dados brutos e desestruturados de clientes, limpar inconsistências, consultar a API pública do **ViaCEP** para normalizar os endereços em tempo real, estruturar o conjunto final de dados e salvá-lo de forma segura em um banco de dados.

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python 3.14** (Linguagem principal)
* **Pandas & NumPy** (Manipulação, limpeza e transformação de dados)
* **Requests** (Consumo de API REST em tempo real)
* **SQLite3** (Armazenamento e persistência relacional local)
* **Colorama** (Feedback visual e logs coloridos no terminal)
* **Git & GitHub** (Controle de versão)

## 🗂️ Estrutura do Projeto
O repositório foi organizado seguindo boas práticas de arquitetura de software para garantir modularidade e clareza:

```text
VStest/
│
├── data/                      # Arquivos CSV de entrada e saída (dados brutos e limpos)
│   ├── dados_sujos.csv
│   └── endereco_clientes.csv
│
├── database/                  # Banco de dados SQLite persistido
│   └── Banco_cliente.db
│
├── src/                       # Código-fonte (regras de negócio e ETL)
│   ├── transform.py
│   └── cep_api.py
│
├── main.py                    # Script principal de orquestração
└── requirements.txt           # Dependências do projeto