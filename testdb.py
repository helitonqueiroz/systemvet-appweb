import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do banco de dados
host = os.getenv('DB_HOST')  # Substitua pelo seu host do banco
database = os.getenv('DB_NAME') # Substitua pelo nome do banco de dados
user = os.getenv('DB_USER')             # Substitua pelo seu nome de usuário
password = os.getenv('DB_PASSWORD')           # Substitua pela sua senha

print('INICIANDO O SCRIPT DE CONEXÃO AO BANCO DE DADOS...')

try:
    print ('Criando a conexão com o banco de dados')
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        # use_pure=True
    )
    print('Conexão bem sucedida')
    if connection.is_connected():
        print("Conexão bem-sucedida ao banco de dados!")
        
        # Opcional: Consultar informações do servidor
        server_info = connection.get_server_info()
        print("Versão do servidor MySQL:", server_info)

        # Criando um cursor para executar comandos SQL
        cursor = connection.cursor()


except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        # Fechando o cursor
        cursor.close()
        connection.close()
        print("Conexão ao banco de dados foi encerrada.")
