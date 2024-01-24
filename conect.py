import os
from dotenv import load_dotenv
import mysql.connector


def success__database():
    
    load_dotenv()
    
    config = {
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT')),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_DATABASE'),
    }

    try:
        conection_data_base = mysql.connector.connect(**config)
        return conection_data_base
    except mysql.connector.errors as error:
        print(f("Error conection of data base"))
        return None
    
    
def close_database (conection_data_base , cursos = None):
    if cursos:
        cursos.close()
    if conection_data_base and conection_data_base.is_connected():
        cursos.close()
        print("close data base")

    
    
    
    



