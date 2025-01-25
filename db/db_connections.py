import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_db_connection():
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')
    ssl_ca = os.getenv('DB_SSL_CA', 'C:/Users/HenriQ/Documents/certsAWS/us-east-2-bundle.pem')

    if port is None:
        raise ValueError("DB_PORT environment variable is not set")

    return pymysql.connect(
        host=host,
        db=database,
        user=user,
        password=password,
        port=int(port),
        ssl={'ca': ssl_ca}
    )

def create_tutores_table():
    connection = create_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tutores (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    cidade VARCHAR(255) NOT NULL,
                    logradouro VARCHAR(255) NOT NULL,
                    bairro VARCHAR(255) NOT NULL,
                    cep VARCHAR(20) NOT NULL,
                    cpf VARCHAR(20) NOT NULL
                )
            """)
        connection.commit()
    finally:
        connection.close()

if __name__ == "__main__":
    try:
        create_tutores_table()
    except Exception as e:
        print(f"An error occurred: {e}")
