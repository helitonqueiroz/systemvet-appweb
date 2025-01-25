from db.db_connections import create_db_connection
import pymysql

def show_tutores_table():
    connection = create_db_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM tutores")
            result = cursor.fetchall()
            return result
        print(result)
    finally:
        connection.close()

if __name__ == "__main__":
    try:
        tutores = show_tutores_table()
        for tutor in tutores:
            print(tutor)
    except Exception as e:
        print(f"An error occurred: {e}")
