import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
host = "sql10.freesqldatabase.com"  # Substitua pelo seu host do banco
database = "sql10759376" # Substitua pelo nome do banco de dados
user = "sql10759376"             # Substitua pelo seu nome de usuário
password = "TFXidvBhtc"           # Substitua pela sua senha

print('INICIANDO O SCRIPT DE CONEXÃO AO BANCO DE DADOS...')

try:
    print ('Criando a conexão com o banco de dados')
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        use_pure=True
    )
    print('Conexão bem sucedida')
    if connection.is_connected():
        print("Conexão bem-sucedida ao banco de dados!")
        
        # Opcional: Consultar informações do servidor
        server_info = connection.get_server_info()
        print("Versão do servidor MySQL:", server_info)

        # Criando um cursor para executar comandos SQL
        cursor = connection.cursor()

        # Criando uma tabela de teste
        create_table_query = """
        CREATE TABLE IF NOT EXISTS teste (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            idade INT NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print("Tabela 'teste' criada com sucesso!")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        # Fechando o cursor
        cursor.close()
        connection.close()
        print("Conexão ao banco de dados foi encerrada.")
