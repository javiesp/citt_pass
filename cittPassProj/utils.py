from pymongo import MongoClient

def get_db_handle(connection_string, db_name):
    client = MongoClient(connection_string)
    db_handle = client[db_name]
    return db_handle, client

# Llamada a la función con la cadena de conexión y el nombre de la base de datos
connection_string = "mongodb+srv://javiesp:ja123456@cluster0.yuojwoc.mongodb.net/"
db_name = "cittpass"

db_handle, client = get_db_handle(connection_string, db_name)
