from flask import Flask, render_template
import sqlite3
import os
from forms.formularios import Login, Registro
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return render_template("inicio.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    frm = Login()
    if frm.validate_on_submit():
        username = frm.username.data
        password = frm.password.data
        # Cifra la contraseña
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        #Conectar a la BD
        with sqlite3.connect("usuarios.db") as con:
            # Crea cursos para manipular la BD
            cursor = con.cursor()
            #Prepara la sentencia SQL a ejecutar
            cursor.execute("SELECT username FROM usuario WHERE username = ? AND password = ?", [username, pass_enc])
            if cursor.fetchone():
                return "Bienvenido!!!"
            else:
                return "Usuario/Password errado"
            #Ejecuta la sentencia SQL

    return render_template("ingreso.html", frm = frm)

#API Rest de registro de Usuarios
@app.route("/registrarse", methods=["GET", "POST"]) #Ruta
def registrar(): #Endpoint
    frm = Registro()
    # Valida los datos del formulario
    if frm.validate_on_submit():
        #Captura los datos del formulario
        username = frm.username.data
        nombre = frm.nombre.data
        correo = frm.correo.data
        password = frm.password.data
        # Cifra la contraseña
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        #Conectar a la BD
        with sqlite3.connect("usuarios.db") as con:
            # Crea cursos para manipular la BD
            cursor = con.cursor()
            #Prepara la sentencia SQL a ejecutar
            cursor.execute("INSERT INTO usuario (nombre, username, correo, password) VALUES (?,?,?,?)", [nombre, username, correo, pass_enc])
            #Ejecuta la sentencia SQL
            con.commit()
            return "Guardado con éxito"

    return render_template("registro.html", frm= frm) #Respuesta
@app.route("/busqueda")
def buscar():
    return render_template("search.html")

@app.route("/perfil")
def perfil():
    return render_template("profile.html")

@app.route("/cartelera")
def cartelera():
    return render_template("cartelera.html")

@app.route("/funciones")
def funciones():
    return render_template("funciones.html")

app.run(debug=True)