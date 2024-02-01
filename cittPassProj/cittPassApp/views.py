from django.shortcuts import redirect, render
import pymongo
from pymongo import MongoClient
from datetime import datetime



fecha_de_hoy = datetime.now().strftime('%d-%m-%Y')

# Create your views here.
def main(request):
    # Conexión a la base de datos de MongoDB
    client = MongoClient('mongodb+srv://javiesp:Ja22041982@cluster0.yuojwoc.mongodb.net/')
    db = client['cittpass']
    coleccionUsuario = db["UsuariosCitt"]

    # Obtener documentos de la colección
    documentos = coleccionUsuario.find().sort("fecha_ingreso", pymongo.DESCENDING).limit(5)

    # Pasar los documentos al contexto de la plantilla
    context = {'documentos': documentos}

    # Renderizar la plantilla con el contexto
    return render(request, 'main.html', context)

def add_user(request):
    if request.method == 'POST':
        fecha_ingreso = request.POST.get('fecha_ingreso')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        semestre = request.POST.get('semestre')
        UID = request.POST.get('UID')

        # Connect to MongoDB
        client = MongoClient('mongodb+srv://javiesp:Ja22041982@cluster0.yuojwoc.mongodb.net/')
        db = client['cittpass']
        coleccionUsuario = db["UsuariosCitt"]

        # Insert the new user into MongoDB
        new_user = {
            "fecha_ingreso": fecha_ingreso,
            "nombre": nombre,
            "apellido": apellido,
            "semestre": semestre,
            "UID": UID
        }
        coleccionUsuario.insert_one(new_user)

        # Redirect to the main page or any other page as needed
        return redirect('main')
    print('insertado')
    return render(request, 'main.html')


#Conexión bd mongodb atlas
client = MongoClient('mongodb+srv://javiesp:Ja22041982@cluster0.yuojwoc.mongodb.net/')
db = client['cittpass']

coleccionUsuario = db["UsuariosCitt"]

print(coleccionUsuario)

# ingresoUsuario = {
#     "fecha_ingreso" : "11-01-2024",
#     "UID" : "AL234BJ234",
#     "comentario" : "Hola Mundo"
# }

# inserta
# coleccionUsuario.insert_many([ingresoUsuario])

# lee
documentos = coleccionUsuario.find()

# Imprimir cada documento
for documento in documentos:
    print(documento)

#print(client)
#print(db)
