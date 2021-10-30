from flask import Flask,redirect,request,flash,session,escape,render_template
import sqlite3
import os
from forms.formularios import Login, Registro,comentarios, funcion, new
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
                    return redirect("/cartelera")
                elif session['id_rol'] == 2:
                    return redirect("/dashboard/administrador")
                elif session["id_rol"] == 3:
                    return redirect("/dashboard/superadministrador")
            else:
                flash("Usuario/Password errados")

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

@app.route("/cartelera")
def cartelera():
    if "usuario" in session and session["id_rol"] == 1 or 3:
        return render_template("cartelera.html")
    else:
        return redirect("/")

@app.route("/cartelera/romance")
def romance():
    if "usuario" in session and session["id_rol"] == 1 or 3:
        return render_template("romance.html")
    else:
        return redirect("/")

@app.route("/cartelera/comedia")
def comedia():
    if "usuario" in session and session["id_rol"] == 1 or 3:
        return render_template("comedia.html")
    else:
        return redirect("/")

@app.route("/cartelera/animadas")
def animadas():
    if "usuario" in session and session["id_rol"] == 1 or 3:
        return render_template("animadas.html")
    else:
        return redirect("/")

@app.route("/cartelera/accion")
def terror():
    if "usuario" in session and session["id_rol"] == 1 or 3:
        return render_template("accion.html")
    else:
        return redirect("/")

@app.route("/cartelera/drama")
def drama():
    if "usuario" in session and session["id_rol"] == 1 or 3:
        return render_template("drama.html")
    else:
        return redirect("/")

@app.route("/cartelera/estrenos")
def estrenos():
    if "usuario" in session and session["id_rol"] == 1 or 3:
        return render_template("estrenos.html")
    else:
        return redirect("/")

@app.route('/cartelera/comentarios', methods=["GET","POST"])
def comentario():
    if "usuario" in session and session["id_rol"] == 1 or 3:
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
                cursor.execute ("INSERT INTO comentario (id_comentario,comentario,titulo,nombre) VALUES (?,?,?,?)",[None,comentario,titulo,nombre])
                con.commit()
                flash("Guardado con éxito")
        return render_template("comentarios.html", frm= frm) #Respuesta
    else:
        return redirect("/")


@app.route("/dashboard/administrador",methods=["POST","GET"])
def dashboard_admin():
    if "usuario" in session and session["id_rol"] == 2 or 3:
        return render_template ("dashboard_admin.html")
    else:
        return redirect("/")

@app.route('/listarcomentario')
def listarC():
    if "usuario" in session and session["id_rol"] == 2 or 3:
        con = sqlite3.connect("cineRoyal.db")#conexion
        con.row_factory = sqlite3.Row
        cur = con.cursor()#manipula la db
        cur.execute("select * FROM comentario")
        rows = cur.fetchall()
        return render_template("listarcomentario.html", rows = rows)
    else:
        return redirect("/")

@app.route("/funcion")
def funciones():
    if "usuario" in session and session["id_rol"] == 2 or 3:
        frm = funcion()
        return render_template("funcion.html", frm=frm)
    else:
        return redirect("/")

@app.route("/funcion/guardar", methods=["POST","GET"])
def funciong():
    if "usuario" in session:
        frm = funcion()#Instancia de la clase en formulario.py
    
        #Recupera datos      
        id_funcion = frm.id_funcion.data
        titulo = frm.titulo.data
        horario = frm.horario.data

        with sqlite3.connect("cineRoyal.db") as con:
            # Crea cursos para manipular la BD
            cursor = con.cursor()
            #Prepara la sentencia SQL a ejecutar
            cursor.execute ("INSERT INTO funcion (id_funcion,titulo,horario) VALUES (?,?,?)",[id_funcion,titulo,horario])
            con.commit()
            flash ("Guardado con éxito")
    else:
        return redirect("/")
    return render_template("funcion.html", frm=frm) #Respuesta


@app.route('/funcion/consultar', methods=["POST"])
def listarf():
    if "usuario" in session:
        frm = funcion()
        id_funcion = frm.id_funcion.data
        if len(id_funcion)>0:
            with sqlite3.connect("cineRoyal.db") as con:#conexion
                con.row_factory = sqlite3.Row
                cursor = con.cursor()#manipula la db
                cursor.execute("SELECT * FROM funcion WHERE id_funcion = ?", [id_funcion])
                row = cursor.fetchone()
                if row:
                    frm.titulo.data = row["titulo"]
                    frm.horario.data = row["horario"]
                else:
                    frm.id_funcion.data = ""
                    frm.titulo.data = ""
                    frm.horario.data = ""
                    flash("Funcion no encontrada")
        else:
            flash("Debe digitar el ID de la funcion")

        return render_template("funcion.html", frm = frm)
    else:
        return redirect("/")

@app.route('/funcion/actualizar', methods=["POST"])
def actualizarf():
    if "usuario" in session:
        frm = funcion()#Instancia de la clase en formulario.py
        id_funcion = frm.id_funcion.data
        titulo = frm.titulo.data
        horario = frm.horario.data

        with sqlite3.connect("cineRoyal.db") as con:
            cursor = con.cursor()
            cursor.execute("UPDATE funcion SET titulo = ?, horario = ? WHERE id_funcion = ?;",[titulo,horario,id_funcion] )
            con.commit()#Confirmación de inserción de datos :)
            flash("Actualizado correctamente")
       
        return render_template("funcion.html",frm=frm)
    else:
        return redirect("/")

@app.route('/funcion/eliminar', methods=["POST"])
def eliminar():
    if "usuario" in session:
        frm = funcion()#Instancia de la clase en formulario.py
          #Recupera datos
        id_funcion = frm.id_funcion.data
        if len(id_funcion)>0:
            with sqlite3.connect("cineRoyal.db") as con:
                # Crea cursos para manipular la BD
                cursor = con.cursor()
                #Prepara la sentencia SQL a ejecutar
                cursor.execute ("DELETE FROM funcion WHERE id_funcion = ?", [id_funcion])
                con.commit()
                flash("funcion  borrada")
        else:
            flash("Debe digitar el ID")
        return render_template("funcion.html", frm=frm)
    else:
        return redirect("/")

@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/store', methods=['GET','POST'])
def storage():
    titulo=request.form['txtTitulo']
    genero=request.form['txtGenero']

    with sqlite3.connect("cineRoyal.db") as con:
        # Crea cursos para manipular la BD
        cursor = con.cursor()
        #Prepara la sentencia SQL a ejecutar
        cursor.execute ("INSERT INTO pelicula (id_pelicula,titulo,genero) VALUES (?,?,?)",[None,titulo,genero])
        con.commit()
        #return "Guardado con éxito"
        flash("Creada con exito")
        return render_template("crear.html") #Respuesta 

@app.route('/vistapelicula')
def ver():
    if "usuario" in session and session["id_rol"] == 2 or 3:
        with sqlite3.connect("cineRoyal.db") as con:
                # Crea cursos para manipular la BD
                cursor = con.cursor()
                #Prepara la sentencia SQL a ejecutar
                cursor.execute ("SELECT * FROM pelicula ")
                pelicula=cursor.fetchall()
                con.commit()
        return render_template("vistapelicula.html",pelicula=pelicula) #Respuesta    
    else:
        return redirect("/")

@app.route('/destroy/<int:id>')
def destroy(id):
    with sqlite3.connect("cineRoyal.db") as con:
                # Crea cursos para manipular la BD
                cursor = con.cursor()
                cursor.execute ("DELETE FROM pelicula WHERE id_pelicula = ?", [id])
                con.commit()
                return redirect("/vistapelicula")

@app.route('/edit/<int:id>')
def edita(id):
     with sqlite3.connect("cineRoyal.db") as con:
                # Crea cursos para manipular la BD
                cursor = con.cursor()
                cursor.execute ("SELECT * FROM pelicula  WHERE id_pelicula = ?", [id])
                pelicula=cursor.fetchall()
                con.commit()
                return render_template("/editar.html",pelicula=pelicula)

@app.route('/update', methods=['POST'])
def update():
    titulo=request.form['txtTitulo']
    genero=request.form['txtGenero']
    id=request.form['txtId']
    with sqlite3.connect("cineRoyal.db") as con:
                # Crea cursos para manipular la BD
                cursor = con.cursor()
                #Prepara la sentencia SQL a ejecutar
                cursor.execute ("UPDATE  pelicula  SET titulo = ?, genero = ? WHERE id_pelicula =  ?;",[titulo, genero,id])
                con.commit()
                #return "Guardado con éxito"
                return redirect("/vistapelicula")

@app.route("/dashboard/superadministrador")
def superadmin():
    if "usuario" in session and session["id_rol"] == 3:
        return render_template("dashboard_super.html")
    else:
        return redirect("/")

@app.route("/new_user", methods=["POST","GET"])
def new_user():
    if "usuario" in session and session["id_rol"] == 3:
        frm = new()
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
        return render_template("registrosuper.html", frm= frm) #Respuesta
    else:
        return redirect("/")

@app.route('/gestionarusuario')
def vista():
    if "usuario" in session and session["id_rol"] == 3:
        con = sqlite3.connect("cineRoyal.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from usuario")
        rows = cur.fetchall()
    
        return render_template("getionarusuario.html",rows=rows)
    else:
        return redirect("/") 

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.run(debug=True)