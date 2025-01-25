import pymysql
from db.db_connections import create_db_connection
from faker import Faker

# Função para inserir dados falsos na tabela tutores
def insert_fake_data():
    fake = Faker()
    connection = create_db_connection()

    try:
        with connection.cursor() as cursor:
            for _ in range(100):  # Loop para inserir 100 registros
                # Gerando dados falsos
                nome = fake.name()
                cidade = fake.city()
                logradouro = fake.street_address()
                bairro = fake.street_name()
                cep = fake.zipcode()
                cpf = fake.ssn()

                # Comando SQL para inserir os dados
                cursor.execute("""
                    INSERT INTO tutores (nome, cidade, logradouro, bairro, cep, cpf)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (nome, cidade, logradouro, bairro, cep, cpf))
        
        # Commit para salvar as mudanças no banco
        connection.commit()
        print("100 records inserted successfully.")
    finally:
        connection.close()

if __name__ == "__main__":
    insert_fake_data()
