# Intuitive Care - Nivelamento (Teste API)
# Acesse os testes anteriores clicando [aqui👈](https://github.com/danilohsaraiva/intuitivecare_nivelamento)
Desenvolvimento de uma interface web usando Vue.js com interação com servidor Python
####   ❓ Desenvolvimento de uma intercafe wev usando Vue.js
####    ✅  Crie um servidor com uma rota que realize uma busca textual na lista de cadastros de operadoras ([**📃Relatorio_codap.csv**]()) e retorne os registros mais relevantes.<br>
####    ✅  Elabore uma coleção no Postman para demonstrar o resultado.

📌 Linguagem utilizada: Python <br>
📌 IDE: VsCode

## 👁‍🗨 Primeira vez usando Python
Deixar salientado que esse projeto foi/esta sendo desenvolvido utilizando IA (CharGPT), como não tenho familiaridade com Python, estou utilizando do recurso para criar a parte de Servidor utilizando dos mesmos.


## 🚀 O que é um servidor Flask?
Flask é um framework web para Python que permite com que você crie um servidor web, ou seja, um programa que:
- Fica "ligado" esperando requisições de outras aplicações (como navegadores ou apps).

- Responde essas requisições com dados ou páginas.

- Permite criar rotas que executam ações diferentes.

## 📁 Estrutura do Projeto

```
├── app/                       # Diretório principal da aplicação
│   ├── __init__.py             # Inicializa a aplicação Flask e configura o app
│   ├── routes.py               # Define as rotas da API (endpoints HTTP)
│   ├── services.py             # Contém a lógica de negócio, como leitura e filtragem dos dados
├── data/                      # Pasta para armazenar arquivos de dados
│   └── Relatorio_cadop.csv     # Arquivo CSV com os dados das operadoras
├── server.py                  # Arquivo principal para iniciar o servidor Flask
├── requirements.txt           # Lista de dependências do projeto (para instalação com pip)
└── README.md                  # Documentação do projeto
```
⛔ Observação: É necessário ativar o ambiente virtual toda vez que for trabalhar no projeto (mas apenas durante a duração do terminal atual)

Comando para ativar o Ambiente Virtual:
```
.\venv\Scripts\activate
```

⛔ Observação: O arquivo requirements.txt permite definir um ambiente de desenvolvimento que contém os nomes e versões das bibliotecas que seu projeto precisa para funcionar corretamente, serve para que qualquer pessoa (ou máquina) possa:

- Criar um ambiente virtual (limpo, isolado).

- Instalar exatamente as mesmas bibliotecas que você usou.

- Garantir que o projeto funcione sem erros de compatibilidade.

Para gerá-la automaticamente com base em suas libs instaladas no ambiente virtual:

``` 
pip freeze > requirements.txt
```