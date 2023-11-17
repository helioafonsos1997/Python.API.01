# -*- coding: utf-8 -*-
# Importa dependências  que são partes do meu programa que não foram feitos por mim porém  dependo delas para funcionar"
import json
import sqlite3
import os

# Definição do caminho do banco de dados, utilizando uma variável.
database = './db/temp_db.db'

# Função para obter todos os itens da tabela 'item'.


def get_all_items():
    #pra tentar executar o codigo- validar o codigo(captura o erro e tenta resolver se não ele avisa o usuario e executa o exept e não deixa o programa parar)
    try:
        # Conectar ao banco de dados SQLite.
        conn = sqlite3.connect(database) # cria um espaço na memoria chamado conn e conecta o banco de dados sqlite( se fosse SQL Não e database)
        conn.row_factory = sqlite3.Row #cria um exaço na memoria chamado factory e faz a troca de informações do banco de dados e python em forma de linha
        cursor = conn.cursor() # cria um curso que e quem gerencia o SQlite

        # Consulta SQL para selecionar todos os itens ativos.
        sql = "SELECT * FROM item WHERE item_status != 'off'" #cria funções que o SQLite Entende 
        cursor.execute(sql)# executa os dados que estão na memoria e trazer pra dentro do PYTHON
        rows_data = cursor.fetchall()
        conn.close()# fecha o banco de dados

        # Converter os resultados em uma lista de dicionários.
        list_data = []
        for row_data in rows_data:#roda um loop le e armazena os itens em rows_data
            list_data.append(dict(row_data))# adiciona item que foi armazenado em row_data e transforma em Dicionario e adicionana lista
#append=adiciona
        # Retornar os dados ou um erro se nenhum item for encontrado.
        if list_data:
            return list_data
        else:
            return {"error": "Nenhum item encontrado"}

    # Tratamento de exceções.
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}

# Função para obter um item específico pelo ID.


def get_one_item(id):
    try:
        # Conectar ao banco de dados SQLite.
        conn = sqlite3.connect(database)# cria um espaço na memoria chamado conn e conecta o banco de dados sqlite( se fosse SQL Não e database)
        conn.row_factory = sqlite3.Row # cria um espaço na memoria chamado row_factory e troca informaçõs entre o python e o banco de dados em forma de linhas
        cursor = conn.cursor()# cria um cursor que gerencia o SQLite

        # Consulta SQL para selecionar um item específico por ID.
        sql = "SELECT * FROM item WHERE item_status != 'off' AND item_id = ?" #cria funções que o SQLite Entende 
        cursor.execute(sql, (id,))
        row_data = cursor.fetchone() # row_data = cursor.fetchone() é comumente usado em linguagens de programação, como Python, para recuperar a próxima linha de dados de um conjunto de resultados obtido a partir de uma consulta a um banco de dados.
        conn.close() # é utilizado para fechar a conexão com o banco de dados. 

        # Retornar os dados do item ou um erro se não for encontrado.
        if row_data:
            return dict(row_data)
        else:
            return {"error": "Item não encontrado"}
    
    # Tratamento de exceções.
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


# Limpar a tela do console.
os.system('cls')

# Imprimir todos os itens formatados como JSON.
print(#comando do python pra exibir no console
    json.dumps(#Pega uma lista de dicionarios e  tenta converter para Json
        get_all_items(),
        ensure_ascii=False,# para formatar em UTF-8
        indent=2
    )
)

print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')

# Imprimir um item específico pelo ID formatado como JSON.
print(
    json.dumps(
        get_one_item(2),
        ensure_ascii=False,
        indent=2
    )
)
