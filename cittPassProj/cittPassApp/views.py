from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.
def main(request):
    # Obtener documentos de la colección
    documentos = conectar_bd().find()
    # Pasar los documentos al contexto de la plantilla
    context = {'documentos': documentos}

    # Renderizar la plantilla con el contexto
    return render(request, 'main.html', context)

def agregar_usuario():
    return 0 

# Conectar a la base de datos mongo 
def conectar_bd():
    client = MongoClient('mongodb+srv://javiesp:Ja22041982@cluster0.yuojwoc.mongodb.net/')
    db = client['cittpass']
    coleccionUsuario = db["UsuariosCitt"]

    return coleccionUsuario


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
