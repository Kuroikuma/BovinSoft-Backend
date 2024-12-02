import json
import bcrypt
from flask import request, jsonify
from models.User import UserModel
from controllers.jwt import crear_token
import smtplib
from email.mime.text import MIMEText
import yagmail
from jinja2 import Template


#configuracion del correo
CORREO_REMITENTE = "bovinsoft@gmail.com"
PASSWORD_CORREO = "vsal gtkx dchi xyip"

# Función para enviar correo de verificación
def enviar_correo_verificacion(correo_destinatario, nombre, apellido):
    try:
      # Create a yagmail object
      yagD = yagmail.SMTP(CORREO_REMITENTE, PASSWORD_CORREO)
      yagR = yagmail.SMTP(CORREO_REMITENTE, PASSWORD_CORREO)
      
      # Send the email
      yagD.send(
          to=correo_destinatario,
          subject="Verificación de registro",
          contents=f"""\
              <html>
              <body>
                  <h1>Verificación de registro</h1>
                  <p>Hola {nombre} {apellido}, gracias por registrarte!</p>
                  <img src='https://st2.depositphotos.com/1765488/5294/i/450/depositphotos_52940845-stock-photo-herd-of-cows-at-summer.jpg'/>
              </body>
              </html>
              """)

      yagR.send(
          to=CORREO_REMITENTE,
          subject="Verificación de registro",
          contents=f"""\
              <html>
              <body>
                  <h1>Verificación de registro de usuarios</h1>
                  <p>Felicidades, se ha registrado un usuario nuevo: {nombre} {apellido}</p>
                  <img src='https://st2.depositphotos.com/1765488/5294/i/450/depositphotos_52940845-stock-photo-herd-of-cows-at-summer.jpg'/>
              </body>
              </html>
              """)
    except Exception as x:
        return False
    

##funcion para validar si el correo existe
def validacion_gmail(coll, email):
    doc = coll.find_one({'email':email})
    if doc:
        return True
    return False

##valiar si el password existe
def validar_password(coll, password):
    passEncriptado = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    doc = coll.find_one({'password': passEncriptado})
    if doc:
        return True
    return False

##controlador para registro de usuarios
def signin(collections):
    try:
        data = json.loads(request.data)
        user_instace = UserModel(data)

        #verificar si el correo ya existe
        if validacion_gmail(collections, user_instace.email):
            response = jsonify({"message": "El correo electrónico ya está en uso"})
            response.status_code = 400
            return response

        #encriptando password
        password = user_instace.password.encode('utf-8')
        salt = bcrypt.gensalt()
        passEncriptado = bcrypt.hashpw(password, salt)
        user_instace.password = passEncriptado.decode('utf-8')

        #insertando password y usuario a la db
        id = collections.insert_one(user_instace.__dict__).inserted_id
        user_instace._id = str(user_instace._id)
        user_instace.create_at = str(user_instace.create_at)
        user_instace.update_at = str(user_instace.update_at)
        user_data = {
            "id": user_instace._id,
            "nombre": user_instace.nombre,
            "apellido": user_instace.apellido,
            "fecha_nacimiento": user_instace.fecha_nacimiento,
            "email": user_instace.email,
            "telefono": user_instace.telefono,
            "rol": user_instace.rol,
            "direccion": user_instace.direccion,
            "tipoSuscripcion": user_instace.tipoSuscripcion
        }
        token = crear_token(data=user_instace.__dict__)
        enviar_correo_verificacion(user_instace.email, user_instace.nombre, user_instace.apellido)
        return jsonify({'id':str(id), "token":token.decode('utf-8')})

    except Exception as x:
        response = jsonify({"menssage","error de registro"})
        response.status = 400
        return response


#controllador de logeo de usuarios
def login(collections):
    try:
        data = json.loads(request.data)
        user_instance = UserModel(data)

        # Validar si el correo electrónico existe
        if not validacion_gmail(collections, user_instance.email):
            response = jsonify({"message": "El correo electrónico no existe"})
            response.status_code = 401
            return response

        # Obtener el documento del usuario
        user_doc = collections.find_one({'email': user_instance.email})
        user_doc["_id"] = str(user_doc['_id'])
        user_doc["create_at"] = str(user_doc['create_at'])
        user_doc["update_at"] = str(user_doc['update_at'])
        
        user_data = {
            "id": str(user_doc['_id']),
            "nombre": user_doc['nombre'],
            "apellido": user_doc['apellido'],
            "fecha_nacimiento": user_doc['fecha_nacimiento'],
            "email": user_doc['email'],
            "password": user_doc['password'],
            "telefono": user_doc['telefono'],
            "rol": user_doc['rol'],
            "direccion": user_doc['direccion'],
            "tipoSuscripcion": user_doc['tipoSuscripcion']
        }
        # Validar la contraseña
        if not bcrypt.checkpw(user_instance.password.encode('utf-8'), user_doc['password'].encode('utf-8')):
            response = jsonify({"message": "La contraseña no es válida"})
            response.status_code = 401
            return response

        # Crear y enviar el token
        token = crear_token(data=user_doc)
        return jsonify({'id': str(user_doc['_id']), "token": token.decode('utf-8')})
    except Exception as e:
        print(str(e))
        response = jsonify({"message": "Error de inicio de sesión"})
        response.status_code = 400
        return response