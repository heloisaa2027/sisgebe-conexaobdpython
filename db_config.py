# db_config.py

import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root', # Troque se necessário
        password='eec123456@#$', # Troque se necesário
        database='sgb' # Nome do seu banco
        )
        if conexao.is_connectd():
            print("Conexão bem-sucedida com o banco e dados!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None    