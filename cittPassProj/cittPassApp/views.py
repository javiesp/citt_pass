from django.shortcuts import redirect, render
from django.http import JsonResponse
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
    documentos = coleccionUsuario.find().sort("fecha_registro", pymongo.DESCENDING).limit(5)

    # Pasar los documentos al contexto de la plantilla
    context = {'documentos': documentos}

    # Renderizar la plantilla con el contexto
    return render(request, 'main.html', context)

def add_nuevo_ingreso(uid, nombre, apellido):
    client = MongoClient('mongodb+srv://javiesp:Ja22041982@cluster0.yuojwoc.mongodb.net/')
    db = client['cittpass']
    coleccionUsuario = db["ingresoUsuario"]


    # si existe agregar a bd nuevo ingreso
    ingresoUsuario = {
            "fecha_ingreso" : fecha_de_hoy,
            "UID" : uid,
            "Alumno: " : nombre + apellido,
            "comentario" : "Hola Mundo"
        }

    coleccionUsuario.insert_one(ingresoUsuario)

    return 'agregado'

def verificar_uid_existente(request):
    uid = request.GET.get('uid', None)

    if uid:
        # Conexión a la base de datos de MongoDB
        client = MongoClient('mongodb+srv://javiesp:Ja22041982@cluster0.yuojwoc.mongodb.net/')
        db = client['cittpass']
        coleccionUsuario = db["UsuariosCitt"]

        # Verificar si el UID existe en la base de datos
        user = coleccionUsuario.find_one({'UID': uid}, {'nombre': 1, 'apellido': 1})

        # si existe agregar a bd nuevo ingreso
        if user:
            add_nuevo_ingreso(uid, user.get('nombre'), user.get('apellido'))
            print('hola')

        return JsonResponse({'existe': user is not None})
    else:
        return JsonResponse({'existe': False})

    

def add_user(request):
    if request.method == 'POST':
        fecha_registro = request.POST.get('fecha_registro')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        semestre = request.POST.get('semestre')
        comentario = request.POST.get('comentario')
        rol = request.POST.get('rol')
        UID = request.POST.get('UID')

        # Connect to MongoDB
        client = MongoClient('mongodb+srv://javiesp:Ja22041982@cluster0.yuojwoc.mongodb.net/')
        db = client['cittpass']
        coleccionUsuario = db["UsuariosCitt"]

        # Insert the new user into MongoDB
        new_user = {
            "fecha_ingreso": fecha_registro,
            "nombre": nombre,
            "apellido": apellido,
            "semestre": semestre,
            "UID": UID,
            "comentario": comentario,
            "rol": rol
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
