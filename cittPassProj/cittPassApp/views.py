from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.


#Conexión bd mongodb atlas
client = MongoClient('mongodb+srv://javiesp:ja123456@cluster0.yuojwoc.mongodb.net/')
db = client['cittpass']

coleccionUsuario = db["UsuariosCitt"]

print(coleccionUsuario)

ingresoUsuario = {
    "fecha_ingreso" : "11-01-2024",
    "UID" : "AL234BJ234",
    "comentario" : "Hola Mundo"
}

# inserta
coleccionUsuario.insert_many([ingresoUsuario])

# lee
documentos = coleccionUsuario.find()

# Imprimir cada documento
for documento in documentos:
    print(documento)

#print(client)
#print(db)
