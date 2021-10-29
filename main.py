from flask import Flask,redirect,request,flash,session,escape,render_template
import sqlite3
import os
<<<<<<< HEAD
from forms.formularios import Login, Registro, Comentarios
=======
from forms.formularios import Login, Registro,comentarios
>>>>>>> e0e3ff337655a15d4d6f965b388fd5b4448fa441
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
        username = escape(frm.username.data)
        password = escape(frm.password.data)
        # Cifra la contraseña
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        #Conectar a la BD
        with sqlite3.connect("cineRoyal.db") as con:
            # Crea cursos para manipular la BD
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            #Prepara la sentencia SQL a ejecutar
            cursor.execute("SELECT username, id_usuario ,nombre, id_rol FROM usuario WHERE username = ? AND password = ?", [username, pass_enc])
            row = cursor.fetchone()
            if row:
                session["usuario"] = username
                session["ide"] = row["id_usuario"]
                session["nombre"] = row["nombre"]
                session["id_rol"] = row["id_rol"]
                
                if session["id_rol"] == 1:
                    return redirect("/perfil")
                elif session['id_rol'] == 2:
                    return "No definido"
                elif session["id_rol"] == 3:
                    return "Tampoco"
            else:
<<<<<<< HEAD
                flash("Usuario/Password errados")
=======
                return f"Usuario/Password errados"
>>>>>>> e0e3ff337655a15d4d6f965b388fd5b4448fa441

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
        email = frm.email.data
        password = frm.password.data
        id_rol = frm.id_rol.data
        # Cifra la contraseña
        enc = hashlib.sha256(password.encode())
        pass_enc = enc.hexdigest()

        #Conectar a la BD
        with sqlite3.connect("cineRoyal.db") as con:
            # Crea cursos para manipular la BD
            cursor = con.cursor()
            #Prepara la sentencia SQL a ejecutar
            cursor.execute("INSERT INTO usuario (nombre, email, username, password,id_rol) VALUES (?,?,?,?,?)", [nombre,email,username,pass_enc,id_rol])
            #Ejecuta la sentencia SQL
            con.commit()
            flash("Guardado con éxito")
    return render_template("registro.html", frm= frm) #Respuesta

@app.route("/busqueda")
def buscar():
    return render_template("search.html")

@app.route("/perfil")
def perfil():
    if "usuario" in session and session["id_rol"]==1:
        return render_template("profile.html")

@app.route("/cartelera")
def cartelera():
    return render_template("cartelera.html")
####################################################################################################################################
######################################################################################################################
##################################################################################################################


#----------------------------------------CREAR CRUD COMENTARIOS ------------------------------------------------#
<<<<<<< HEAD
@app.route('/cartelera/comentarios', methods=["GET","POST"])
def comentario():
    frm = Comentarios()#Instancia de la clase en formulario.py
    if frm.validate_on_submit():
        #Recupera datos
        id_comentario = frm.id_comentario.data
        comentario = frm.comentario.data
        titulo = frm.titulo.data
        nombre = frm.nombre.data

        with sqlite3.connect("cineRoyal.db") as con:
            # Crea cursos para manipular la BD
            cursor = con.cursor()
            #Prepara la sentencia SQL a ejecutar
            cursor.execute ("INSERT INTO comentario (id_comentario,comentario,titulo,nombre) VALUES (?,?,?,?)",[id_comentario,comentario,titulo,nombre])
            con.commit()
            flash("Guardado con éxito")
    return render_template("comentarios.html", frm= frm) #Respuesta    

#----------------------------------------EDITAR CRUD COMENTARIOS ------------------------------------------------#
# @app.route('/comentarios/actualizar/', methods=["POST"])
# def actualizarC():
    
#     form = comentarios()#Instancia de la clase en formulario.py
#     if request.method == "POST":
#         documento = form.documento.data# docu es vuelos
#         nombre = form.nombre.data
#         pelicula = form.pelicula.data
#         mensaje = form.mensaje.data
        
#         with sqlite3.connect("cineRoyal.db") as conn:
#             cur = conn.cursor()
#             cur.execute(
#                 "UPDATE comentario SET id_comentario = ?, mensaje = ?, id_pelicula = ? WHERE nombre = ?",
#              [documento, mensaje, pelicula, nombre]
#              )
#             conn.commit()#Confirmación de inserción de datos :)
#             return "¡Datos actualizados exitosamente ^v^!"
#     return "No se pudo actualizar "
=======
@app.route('/comentarios', methods=["GET","POST"])

def comentario():
        frm = comentarios()#Instancia de la clase en formulario.py
        if frm.validate_on_submit():
          #Recupera datos
            
            comentario = frm.comentario.data
            titulo = frm.titulo.data
            nombre = frm.nombre.data
            with sqlite3.connect("cineRoyal.db") as con:
                # Crea cursos para manipular la BD
                cursor = con.cursor()
                #Prepara la sentencia SQL a ejecutar
                cursor.execute ("INSERT INTO comentario (comentario,titulo,nombre) VALUES (?,?,?)",[comentario,titulo,nombre])
                con.commit()
                return "Guardado con éxito"
        return render_template("comentarios.html", frm= frm) #Respuesta    

#----------------------------------------EDITAR CRUD COMENTARIOS ------------------------------------------------#
@app.route('/comentarios/actualizar/', methods=["POST","GET"])
def actualizarC():
        form = comentarios()#Instancia de la clase en formulario.py
        if request.method == "POST":
            nombre = form.nombre.data
       
            with sqlite3.connect("cineRoyal.db") as conn:
                cur = conn.cursor()
                cur.execute(
                    "UPDATE comentario SET mensaje = ? WHERE nombre = ?", [nombre]
                )
                conn.commit()#Confirmación de inserción de datos :)
                return "¡Datos actualizados exitosamente ^v^!"
        return "No se pudo actualizar "
>>>>>>> e0e3ff337655a15d4d6f965b388fd5b4448fa441
#----------------------------------------VISUALIZAR CRUD COMENTARIO ---------------------------------------------#
# @app.route('/comentarios/eliminar/', methods=["POST"])
# def eliminarC():
   
#     form = comentarios()
#     if request.method == "POST":
#         docum = form.documento.data
#         with sqlite3.connect("cineRoyal.db") as conn:
#             conn.row_factory = sqlite3.Row
#             cur = conn.cursor()#manipula la db
#             cur.execute("DELETE FROM comentario WHERE id_comentario = ?", [docum])
#             if conn.total_changes > 0:
#                 return "Comentario  borrado ^v^"
#             return render_template("comentarios.html")
#     return "Error"
#----------------------------------------BORRAR CRUD COMENTARIOS ------------------------------------------------#

@app.route("/funciones")
def funciones():
    return render_template("funciones.html")

<<<<<<< HEAD
@app.route("/cartelera/romance")
def romance():
    return render_template("romance.html")

@app.route("/cartelera/comedia")
def comedia():
    return render_template("comedia.html")

@app.route("/cartelera/animadas")
def animadas():
    return render_template("animadas.html")

@app.route("/cartelera/terror")
def terror():
    return render_template("terror.html")

@app.route("/cartelera/drama")
def drama():
    return render_template("drama.html")

=======
>>>>>>> e0e3ff337655a15d4d6f965b388fd5b4448fa441
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.run(debug=True)