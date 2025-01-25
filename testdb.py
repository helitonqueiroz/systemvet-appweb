import pymysql
from pymysql import MySQLError
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

try:
    # Criando a conexão com o banco de dados
    connection = pymysql.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=int(port),
    )

    if connection.open:
        print("Conexão bem-sucedida ao banco de dados!")
        
        # Opcional: Consultar informações do servidor
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            server_info = cursor.fetchone()
            print("Versão do servidor MySQL:", server_info)

except MySQLError as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Conexão ao banco de dados foi encerrada.")
